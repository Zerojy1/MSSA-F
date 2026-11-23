"""Baselines sharing one interface: forecast_all(batch, obs_mask, h) -> {'mu': [B,T,h], 'var' or None,
'pred_mu': [B,T]} where mu[b,t,j] predicts y[b,t+j+1] from information up to t (masked observations),
and pred_mu[b,t] predicts y[b,t] from information up to t-1.

  persistence     last available measurement (manuscript baseline)
  gbm_residual    direct multi-horizon gradient boosting on the change from the last measurement
                  (input-matched residual-target control of the manuscript, extended to horizons/gaps)
  jtg_global      JTG D50-2017 layered law with globally calibrated beta1..beta3 (Wu et al. 2022 form),
                  no measurement updating
  jtg_enkf        same law, parameters and datum updated by an ensemble Kalman filter (Haddad et al. 2023)
  lstm / patchtst sequence networks with masked history and known future covariates (torch)
"""
from __future__ import annotations

import numpy as np
from scipy.optimize import least_squares

from . import physics as ph
from .data import CLASSES, SLOTS, pad_batch

try:
    import xgboost as xgb
except ImportError:
    xgb = None


def last_obs_index(obs):
    """obs [B,T] in {0,1} -> index of the last observed step <= t (or -1)."""
    Bsz, T = obs.shape
    idx = np.full((Bsz, T), -1)
    cur = np.full(Bsz, -1)
    for t in range(T):
        cur = np.where(obs[:, t] > 0, t, cur)
        idx[:, t] = cur
    return idx


def _obs(batch, obs_mask):
    return batch['tmask'] if obs_mask is None else batch['tmask'] * obs_mask


# --------------------------------------------------------------------------- persistence
class Persistence:
    name = 'persistence'

    def fit(self, train_structs, cfg, seed=0):
        self.mu_first = float(np.mean([s.y[0] for s in train_structs]))
        return self

    def forecast_all(self, batch, obs_mask, h):
        obs = _obs(batch, obs_mask)
        li = last_obs_index(obs)
        Bsz, T = obs.shape
        ylast = np.where(li >= 0, np.take_along_axis(batch['y'], np.maximum(li, 0), 1), self.mu_first)
        mu = np.repeat(ylast[:, :, None], h, 2)
        pred = np.concatenate([np.full((Bsz, 1), self.mu_first), ylast[:, :-1]], 1)
        return {'mu': mu, 'var': None, 'pred_mu': pred}


# --------------------------------------------------------------------------- gradient boosting
def _pair_features(batch, b, l, tau):
    """Features for predicting y[b,tau] from the last observation at l (l may be -1 -> cold start)."""
    N, T_air, y, d0n = batch['N'][b], batch['T_air'][b], batch['y'][b], batch['d0n'][b]
    th = batch['thickness'][b]
    if l >= 0:
        yl, pk, Nl, d0 = y[l], y[:l + 1].max(), N[l], d0n[l]
        Tm = T_air[l + 1:tau + 1].mean()
    else:
        yl, pk, Nl, d0 = np.nan, np.nan, 0.0, 1.0
        Tm = T_air[:tau + 1].mean()
    return np.concatenate([[yl, pk, np.log1p(Nl), (N[tau] - Nl) / 1e6, np.log1p(N[tau]), Tm, T_air[tau],
                            tau - l, d0, float(l < 0)], th])


class GBMResidual:
    name = 'gbm_residual'

    def fit(self, train_structs, cfg, seed=0):
        rng = np.random.default_rng(seed)
        batch = pad_batch(train_structs)
        batch['thickness'] = np.stack([s.thickness_cm for s in train_structs])
        X, Y = [], []
        max_rows = cfg.get('gbm_max_rows', 80000)
        lens = batch['tmask'].sum(1).astype(int)
        per = max_rows // len(train_structs)
        for b, n in enumerate(lens):
            ls = rng.integers(-1, n - 1, size=per)
            # log-uniform gaps: short horizons are as well represented as long free-run gaps
            gaps = np.floor(np.exp(rng.uniform(0.0, np.log(n), size=per))).astype(int).clip(1, n - 1)
            for l, gp in zip(ls, gaps):
                tau = min(n - 1, l + gp) if l >= 0 else min(n - 1, gp)
                if tau <= l:
                    continue
                X.append(_pair_features(batch, b, l, tau))
                base = batch['y'][b, l] if l >= 0 else 0.0
                Y.append(batch['y'][b, tau] - base)
        X, Y = np.asarray(X), np.asarray(Y)
        self.mu_first = float(np.mean([s.y[0] for s in train_structs]))
        if xgb is not None:
            self.m = xgb.XGBRegressor(n_estimators=cfg.get('gbm_trees', 400), max_depth=4, learning_rate=0.035,
                                      subsample=0.9, colsample_bytree=0.9, reg_lambda=2.0, tree_method='hist',
                                      random_state=seed)
            self.backend = 'xgboost'
        else:
            from sklearn.ensemble import HistGradientBoostingRegressor
            self.m = HistGradientBoostingRegressor(max_iter=cfg.get('gbm_trees', 400), max_depth=4,
                                                   learning_rate=0.035, l2_regularization=2.0, random_state=seed)
            self.backend = 'sklearn-hgb'
        self.m.fit(X, Y)
        res = Y - self.m.predict(X)
        self.sd = float(np.std(res))
        return self

    def _predict_pairs(self, batch, pairs):
        X = np.asarray([_pair_features(batch, b, l, tau) for b, l, tau in pairs])
        d = self.m.predict(X)
        base = np.array([batch['y'][b, l] if l >= 0 else 0.0 for b, l, _ in pairs])
        return base + d

    def forecast_all(self, batch, obs_mask, h, structs=None):
        obs = _obs(batch, obs_mask)
        li = last_obs_index(obs)
        Bsz, T = obs.shape
        lens = batch['tmask'].sum(1).astype(int)
        mu = np.full((Bsz, T, h), np.nan)
        pairs, where = [], []
        for b in range(Bsz):
            for t in range(lens[b]):
                for j in range(h):
                    tau = t + j + 1
                    if tau < lens[b]:
                        pairs.append((b, li[b, t], tau))
                        where.append((b, t, j))
        if pairs:
            v = self._predict_pairs(batch, pairs)
            for (b, t, j), val in zip(where, v):
                mu[b, t, j] = val
        pred = np.full((Bsz, T), np.nan)
        pp, ww = [], []
        for b in range(Bsz):
            for t in range(lens[b]):
                l = li[b, t - 1] if t > 0 else -1
                pp.append((b, l, t))
                ww.append((b, t))
        v = self._predict_pairs(batch, pp)
        for (b, t), val in zip(ww, v):
            pred[b, t] = val
        return {'mu': mu, 'var': np.full_like(mu, self.sd ** 2), 'pred_mu': pred, 'pred_var': np.full_like(pred, self.sd ** 2)}


# --------------------------------------------------------------------------- JTG law baselines
class JTGLaw:
    """Layered JTG law with time hardening; global parameters theta = [log_scale, b_beta, c_gamma, mu_d0]."""

    def __init__(self, cfg, r0, known, t_off):
        self.cfg, self.r0, self.known, self.t_off = cfg, r0, known, t_off
        self.base = np.where(known, r0, np.nanmean(r0))

    def coef(self, batch, theta):
        B = ph.NumpyBackend()
        p = dict(T_bar=self.cfg.get('T_bar_init', 12.0), T_off=self.t_off, damp_mm=self.cfg.get('damp_mm_init', 300.0),
                 cE=self.cfg.get('cE_init', 0.06), E20_slot=np.asarray(self.cfg['E20_slot'], float),
                 R0_slot=self.base, scale_cls=np.ones(len(CLASSES)) * np.exp(theta[0]),
                 gamma=2.93 * np.exp(theta[2]), kappa_T=np.zeros(len(CLASSES)), kappa_D=np.zeros(len(CLASSES)))
        return ph.build_inputs(B, batch, p)

    @staticmethod
    def simulate(inp, beta, log_mult=None, d0=None, R_init=None, t_start=0):
        """Deterministic time hardening. log_mult [M] multiplies C per member. Returns R_total [M,T]."""
        C, N, dN, lm = inp['C'], inp['N'], inp['dN'], inp['lmask']
        Bsz, T, K = C.shape
        mult = np.ones(Bsz) if log_mult is None else np.exp(log_mult)
        Cm = C * mult[:, None, None]
        if R_init is None:
            R = Cm[:, 0, :] * np.power(np.maximum(N[:, 0], 1.0)[:, None], beta)
        else:
            R = R_init.copy()
        out = np.zeros((Bsz, T))
        out[:, t_start] = R.sum(-1)
        for t in range(t_start + 1, T):
            Neq = np.power(np.maximum(R, 1e-6) / np.maximum(Cm[:, t, :], 1e-30), 1 / beta)
            R = np.where(lm > 0, np.maximum(Cm[:, t, :] * np.power(Neq + dN[:, t, None], beta), R), 0.0)
            out[:, t] = R.sum(-1)
        return out, R


class JTGGlobal:
    name = 'jtg_global'

    def fit(self, train_structs, cfg, seed=0, r0=None, known=None, t_off=4.0):
        self.law = JTGLaw(cfg, r0, known, t_off)
        batch = pad_batch(train_structs)
        tm = batch['tmask'] > 0

        def resid(th):
            inp = self.law.coef(batch, th)
            R, _ = JTGLaw.simulate(inp, 0.48 * np.exp(th[1]))
            return ((R + th[3] - batch['y']) * tm)[tm]

        x0 = np.array([cfg.get('log_scale_init', 0.0), 0.0, 0.0, float(np.mean(batch['y'][:, 0]))])
        r = least_squares(resid, x0, bounds=([-15, -2, -1.5, -5], [15, 1.5, 1.0, 10]), max_nfev=cfg.get('jtg_nfev', 200))
        self.theta = r.x
        self.sd = float(np.std(r.fun))
        return self

    def forecast_all(self, batch, obs_mask, h):
        inp = self.law.coef(batch, self.theta)
        R, _ = JTGLaw.simulate(inp, 0.48 * np.exp(self.theta[1]))
        yhat = R + self.theta[3]
        Bsz, T = yhat.shape
        mu = np.full((Bsz, T, h), np.nan)
        for j in range(h):
            mu[:, :T - j - 1, j] = yhat[:, j + 1:]
        return {'mu': mu, 'var': np.full_like(mu, self.sd ** 2), 'pred_mu': yhat}


class JTGEnKF(JTGGlobal):
    """EnKF on augmented state [layer deformations, log multiplier, datum] (Haddad et al. 2023 style)."""
    name = 'jtg_enkf'

    def forecast_all(self, batch, obs_mask, h):
        cfg = self.law.cfg
        M = cfg.get('enkf_members', 100)
        rng = np.random.default_rng(cfg.get('enkf_seed', 0))
        inp_all = self.law.coef(batch, self.theta)
        beta = 0.48 * np.exp(self.theta[1])
        obs = _obs(batch, obs_mask)
        Bsz, T, K = inp_all['C'].shape
        sig_obs = cfg.get('enkf_sig_obs', 0.2)
        mu = np.full((Bsz, T, h), np.nan)
        var = np.full((Bsz, T, h), np.nan)
        pred = np.full((Bsz, T), np.nan)
        pvar = np.full((Bsz, T), np.nan)
        lens = batch['tmask'].sum(1).astype(int)
        for b in range(Bsz):
            C = np.repeat(inp_all['C'][b:b + 1], M, 0)
            lm = np.repeat(inp_all['lmask'][b:b + 1], M, 0)
            N, dN = inp_all['N'][b], inp_all['dN'][b]
            lmult = rng.normal(0.0, cfg.get('enkf_sd_logmult', 0.5), M)
            d0 = self.theta[3] + rng.normal(0.0, 0.5, M)
            R = C[:, 0, :] * np.exp(lmult)[:, None] * np.power(max(N[0], 1.0), beta)
            for t in range(lens[b]):
                if t > 0:
                    Cm = C[:, t, :] * np.exp(lmult)[:, None]
                    Neq = np.power(np.maximum(R, 1e-6) / np.maximum(Cm, 1e-30), 1 / beta)
                    R = np.where(lm > 0, np.maximum(Cm * np.power(Neq + dN[t], beta), R), 0.0)
                    lmult = lmult + rng.normal(0, cfg.get('enkf_q_logmult', 0.02), M)
                yens = R.sum(-1) + d0
                pred[b, t] = yens.mean()
                pvar[b, t] = yens.var() + sig_obs ** 2
                if obs[b, t] > 0:
                    Z = np.column_stack([R, lmult, d0])
                    yp = yens + rng.normal(0, sig_obs, M)
                    cz = np.cov(np.column_stack([Z, yp]).T)
                    kg = cz[:-1, -1] / cz[-1, -1]
                    Z = Z + np.outer(batch['y'][b, t] - yp, kg)
                    R = np.maximum(Z[:, :K], 0.0) * lm
                    lmult, d0 = Z[:, K], Z[:, K + 1]
                # forecast h steps from t
                Rf, lf = R.copy(), lmult.copy()
                for j in range(h):
                    tau = t + j + 1
                    if tau >= lens[b]:
                        break
                    Cm = C[:, tau, :] * np.exp(lf)[:, None]
                    Neq = np.power(np.maximum(Rf, 1e-6) / np.maximum(Cm, 1e-30), 1 / beta)
                    Rf = np.where(lm > 0, np.maximum(Cm * np.power(Neq + dN[tau], beta), Rf), 0.0)
                    ye = Rf.sum(-1) + d0
                    mu[b, t, j] = ye.mean()
                    var[b, t, j] = ye.var() + sig_obs ** 2
        return {'mu': mu, 'var': var, 'pred_mu': pred, 'pred_var': pvar}


# --------------------------------------------------------------------------- sequence networks
class SeqNet:
    """Direct multi-horizon network: masked past window + known future covariates -> increments."""

    def __init__(self, kind='lstm'):
        self.kind = kind
        self.name = kind

    def _windows(self, batch, obs, L, H):
        obs_i = last_obs_index(obs)
        Bsz, T = obs.shape
        lens = batch['tmask'].sum(1).astype(int)
        y = batch['y']
        Xp, Xf, S, base, idx = [], [], [], [], []
        for b in range(Bsz):
            for t in range(lens[b]):
                l = obs_i[b, t]
                yl = y[b, l] if l >= 0 else self.mu_first
                past = []
                for k in range(t - L + 1, t + 1):
                    kk = max(k, 0)
                    o = obs[b, kk] if k >= 0 else 0.0
                    lo = obs_i[b, kk] if k >= 0 else -1
                    yv = (y[b, lo] if lo >= 0 else self.mu_first) - yl
                    past.append([yv, o, np.log1p(batch['N'][b, kk]) / 18, batch['dN'][b, kk] / 1e6,
                                 batch['T_air'][b, kk] / 40, batch['d0n'][b, kk]])
                fut = []
                for j in range(1, H + 1):
                    tau = min(t + j, lens[b] - 1)
                    fut.append([(batch['N'][b, tau] - batch['N'][b, t]) / 1e6, batch['T_air'][b, tau] / 40,
                                float(t + j < lens[b])])
                Xp.append(past)
                Xf.append(fut)
                S.append(batch['thickness'][b] / 50.0)
                base.append(yl)
                idx.append((b, t))
        return (np.asarray(Xp, np.float32), np.asarray(Xf, np.float32), np.asarray(S, np.float32),
                np.asarray(base), idx)

    def _build(self, H):
        import torch.nn as nn
        import torch
        kind = self.kind

        class Net(nn.Module):
            def __init__(self):
                super().__init__()
                d = 64
                self.inp = nn.Linear(6, d)
                if kind == 'lstm':
                    self.enc = nn.LSTM(d, d, num_layers=2, batch_first=True, dropout=0.1)
                else:  # PatchTST-style: patches of length 4 as tokens
                    self.patch = 4
                    self.inp = nn.Linear(6 * self.patch, d)
                    layer = nn.TransformerEncoderLayer(d, 4, 128, 0.1, batch_first=True, activation='gelu')
                    self.enc = nn.TransformerEncoder(layer, 2)
                    self.pos = nn.Parameter(torch.zeros(1, 64, d))
                self.stat = nn.Linear(18, d)
                self.fut = nn.Linear(3 * H, d)
                self.head = nn.Sequential(nn.Linear(3 * d, d), nn.GELU(), nn.Linear(d, H))

            def forward(self, xp, xf, s):
                if kind == 'lstm':
                    hsq, _ = self.enc(self.inp(xp))
                    z = hsq[:, -1]
                else:
                    Bn, L, F = xp.shape
                    tok = self.inp(xp.reshape(Bn, L // self.patch, self.patch * F))
                    tok = tok + self.pos[:, :tok.shape[1]]
                    z = self.enc(tok).mean(1)
                return self.head(torch.cat([z, self.stat(s), self.fut(xf.reshape(xf.shape[0], -1))], -1))

        return Net()

    def fit(self, train_structs, cfg, seed=0):
        import torch
        torch.manual_seed(seed)
        rng = np.random.default_rng(seed)
        self.L, self.H = cfg.get('seq_window', 16), cfg.get('seq_horizon', 12)
        self.mu_first = float(np.mean([s.y[0] for s in train_structs]))
        batch = pad_batch(train_structs)
        batch['thickness'] = np.stack([s.thickness_cm for s in train_structs])
        XP, XF, SS, BB, YY, WW = [], [], [], [], [], []
        for k in cfg.get('seq_train_k', [1, 2, 4]):
            off = rng.integers(0, k)
            om = (np.arange(batch['y'].shape[1])[None, :] % k == off).astype(float)
            obs = batch['tmask'] * om
            xp, xf, s, base, idx = self._windows(batch, obs, self.L, self.H)
            yt = np.zeros((len(idx), self.H))
            w = np.zeros((len(idx), self.H))
            lens = batch['tmask'].sum(1).astype(int)
            for i, (b, t) in enumerate(idx):
                for j in range(self.H):
                    if t + j + 1 < lens[b]:
                        yt[i, j] = batch['y'][b, t + j + 1] - base[i]
                        w[i, j] = 1.0
            XP.append(xp); XF.append(xf); SS.append(s); BB.append(base); YY.append(yt); WW.append(w)
        xp, xf, s = map(lambda a: torch.tensor(np.concatenate(a)), (XP, XF, SS))
        yt, w = torch.tensor(np.concatenate(YY), dtype=torch.float32), torch.tensor(np.concatenate(WW), dtype=torch.float32)
        self.device = cfg.get('device', 'cpu')
        self.net = self._build(self.H).to(self.device)
        xp, xf, s, yt, w = (a.to(self.device) for a in (xp, xf, s, yt, w))
        opt = torch.optim.AdamW(self.net.parameters(), lr=cfg.get('seq_lr', 1.5e-3), weight_decay=1e-4)
        n = len(xp)
        epochs = cfg.get('seq_epochs', 60)
        for ep in range(epochs):
            self.net.train()
            perm = torch.randperm(n).to(self.device)
            for i in range(0, n, 128):
                j = perm[i:i + 128]
                opt.zero_grad()
                out = self.net(xp[j], xf[j], s[j])
                loss = (torch.nn.functional.smooth_l1_loss(out, yt[j], reduction='none') * w[j]).sum() / w[j].sum().clamp(min=1)
                loss.backward()
                torch.nn.utils.clip_grad_norm_(self.net.parameters(), 1.0)
                opt.step()
        self.net.eval()
        with torch.no_grad():
            r = ((self.net(xp, xf, s) - yt) * w)
            self.sd = float(torch.sqrt((r ** 2).sum() / w.sum()))
        return self

    def forecast_all(self, batch, obs_mask, h, structs=None):
        import torch
        obs = _obs(batch, obs_mask)
        xp, xf, s, base, idx = self._windows(batch, obs, self.L, self.H)
        with torch.no_grad():
            d = self.net(*(torch.as_tensor(a, device=self.device) for a in (xp, xf, s))).cpu().numpy()
        Bsz, T = obs.shape
        mu = np.full((Bsz, T, h), np.nan)
        hh = min(h, self.H)
        for i, (b, t) in enumerate(idx):
            mu[b, t, :hh] = base[i] + d[i, :hh]
        pred = np.full((Bsz, T), np.nan)
        pred[:, 1:] = mu[:, :-1, 0]
        return {'mu': mu, 'var': np.full_like(mu, self.sd ** 2), 'pred_mu': pred}


def make_baseline(name):
    return {'persistence': Persistence, 'gbm_residual': GBMResidual, 'jtg_global': JTGGlobal,
            'jtg_enkf': JTGEnKF, 'lstm': lambda: SeqNet('lstm'), 'patchtst': lambda: SeqNet('patchtst')}[name]()
