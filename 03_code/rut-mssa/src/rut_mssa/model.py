"""MSSA-Rut: code-grounded state-space model trained end-to-end through a constrained EKF (PyTorch)."""
from __future__ import annotations

import copy
import math
import time

import numpy as np

from . import physics as ph
from .data import AC_SLOTS, CLASSES, pad_batch

try:
    import torch
    import torch.nn as nn
except ImportError:  # the package can still run numpy-only parts
    torch = None
    nn = None


def _inv_softplus(x):
    return math.log(math.expm1(x))


class MSSA(nn.Module if nn is not None else object):
    """Variants (cfg['variant']):
      full            JTG skeleton + discrepancy + reversible + projection
      no_disc         g = 0
      no_rev          reversible component removed
      no_proj         no inequality projection in the update
      no_defl         deflection driver/feature removed
      fixed_mat       material offsets frozen at the lab prior
      neural_ssm      skeleton replaced by a monotone neural increment (no JTG law)
      no_ms           trained with filtering likelihood only (no multi-step term)
      no_rate         structure-specific log-rate state theta removed
      no_rw           datum d0 kept constant (no random walk)
    """

    def __init__(self, cfg, r0_prior, r0_known, t_off_prior, mu_d0):
        super().__init__()
        self.cfg = cfg
        v = cfg.get('variant', 'full')
        self.variant = v
        self.use_disc = v not in ('no_disc', 'neural_ssm')
        self.use_rev = v != 'no_rev'
        self.project = v != 'no_proj'
        self.use_defl = v != 'no_defl' and cfg.get('use_deflection', True)
        self.skeleton = 'neural' if v == 'neural_ssm' else 'jtg'
        self.fixed_mat = v == 'fixed_mat'
        self.use_rate = v != 'no_rate' and cfg.get('use_rate_state', True)
        self.use_rw = v != 'no_rw' and cfg.get('datum_random_walk', True)
        n_s, n_c = len(AC_SLOTS), len(CLASSES)
        dt = torch.float64
        known = np.asarray(r0_known, bool).copy()
        for s in cfg.get('hide_R0', []):
            known[AC_SLOTS.index(s)] = False
        base = np.where(known, r0_prior, np.nanmean(np.where(known, r0_prior, np.nan)))
        self.register_buffer('R0_base', torch.tensor(base, dtype=dt))
        self.register_buffer('R0_known', torch.tensor(known.astype(float), dtype=dt))
        self.register_buffer('E20_slot', torch.tensor(cfg['E20_slot'], dtype=dt))
        self.t_off_prior = float(t_off_prior)
        P = lambda x: nn.Parameter(torch.tensor(x, dtype=dt))
        self.log_scale = P(float(cfg.get('log_scale_init', 0.0)))
        self.log_cls = P(np.zeros(n_c))
        self.b_beta = P(0.0)
        self.c_gamma = P(0.0)
        self.u_mat = P(np.zeros(n_s))
        self.T_bar = P(float(cfg.get('T_bar_init', 12.0)))
        self.T_off = P(self.t_off_prior)
        self.log_damp = P(math.log(cfg.get('damp_mm_init', 300.0)))
        self.raw_cE = P(_inv_softplus(cfg.get('cE_init', 0.06)))
        self.kappa_T = P(np.zeros(n_c))
        self.kappa_D = P(np.zeros(n_c))
        self.mu_d0 = P(float(mu_d0))
        self.raw_sig_d0 = P(_inv_softplus(0.5))
        self.logit_phi = P(math.log(0.7 / 0.3))
        self.raw_sig_r = P(_inv_softplus(0.1))
        self.raw_q_rel = P(_inv_softplus(0.3))
        self.raw_q_abs = P(_inv_softplus(0.01))
        self.raw_sig_m = P(_inv_softplus(cfg.get('sig_m_init', 0.15)))
        self.raw_sig_theta = P(_inv_softplus(cfg.get('sig_theta_init', 0.4)))
        self.raw_q_theta = P(_inv_softplus(cfg.get('q_theta_init', 0.02)))
        self.raw_q_d0 = P(_inv_softplus(cfg.get('q_d0_init', 0.03)))
        hid = cfg.get('hidden', 32)
        self.emb = nn.Embedding(n_s, 6).double()
        nin = 6 + 5 + (1 if self.skeleton == 'neural' else 0)
        self.net = nn.Sequential(nn.Linear(nin, hid), nn.SiLU(), nn.Linear(hid, hid), nn.SiLU(),
                                 nn.Linear(hid, 1)).double()
        nn.init.zeros_(self.net[-1].weight)
        nn.init.zeros_(self.net[-1].bias)
        self.g_max = cfg.get('g_max', 1.5)

    # ------------------------------------------------------------------ parameters
    def phys_params(self):
        sp = torch.nn.functional.softplus
        u = self.u_mat * (0.0 if self.fixed_mat else 1.0)
        # known lab R0: multiplicative offset around the prior; unknown slots: free level around the mean
        R0 = self.R0_base * torch.exp(u)
        scale = torch.exp(self.log_scale + self.log_cls)
        return dict(T_bar=self.T_bar, T_off=self.T_off, damp_mm=torch.exp(self.log_damp), cE=sp(self.raw_cE),
                    E20_slot=self.E20_slot, R0_slot=R0, scale_cls=scale,
                    gamma=2.93 * torch.exp(self.c_gamma), beta=0.48 * torch.exp(self.b_beta),
                    kappa_T=self.kappa_T, kappa_D=self.kappa_D * (1.0 if self.use_defl else 0.0),
                    mu_d0=self.mu_d0, sig_d0=sp(self.raw_sig_d0) + 1e-3, sig_r=sp(self.raw_sig_r) + 1e-4,
                    phi=torch.sigmoid(self.logit_phi) * 0.98, q_rel=sp(self.raw_q_rel), q_abs=sp(self.raw_q_abs),
                    sig_m=sp(self.raw_sig_m) + 0.02, sig_theta=sp(self.raw_sig_theta) + 1e-3,
                    q_theta=sp(self.raw_q_theta) + 1e-4,
                    q_d0=(sp(self.raw_q_d0) + 1e-4) if self.use_rw else 1e-5)

    def _features(self, B, batch, inputs):
        slot = torch.as_tensor(batch['slot'], device=inputs['C'].device)
        Bsz, T, K = inputs['C'].shape
        e = self.emb(slot)[:, None, :, :].expand(Bsz, T, K, 6)
        z = B.asarray(batch['zmid'])[:, None, :].expand(Bsz, T, K) / 200.0
        Tl = inputs['T_layer'] / 40.0
        lN = torch.log1p(B.asarray(batch['N']))[:, :, None].expand(Bsz, T, K) / 18.0
        d0n = B.asarray(batch['d0n'])[:, :, None].expand(Bsz, T, K)
        if not self.use_defl:
            d0n = d0n * 0.0 + 1.0
        ha = B.asarray(batch['ha'])[:, None, None].expand(Bsz, T, K) / 500.0
        f = [e, z[..., None], Tl[..., None], lN[..., None], d0n[..., None], ha[..., None]]
        if self.skeleton == 'neural':
            f.append((inputs['dN'][:, :, None].expand(Bsz, T, K) / 1e6)[..., None])
        return torch.cat(f, -1)

    def build(self, batch, device='cpu'):
        B = ph.TorchBackend(device)
        p = self.phys_params()
        inputs = ph.build_inputs(B, batch, p)
        g, inc_override = None, None
        if self.skeleton == 'neural':
            f = self._features(B, batch, inputs)
            rate = torch.nn.functional.softplus(self.net(f).squeeze(-1) - 2.0)
            inc_override = rate * inputs['dN'][:, :, None] / 1e6 * inputs['lmask'][:, None, :]
        elif self.use_disc:
            f = self._features(B, batch, inputs)
            g = self.g_max * torch.tanh(self.net(f).squeeze(-1)) * inputs['lmask'][:, None, :]
        return B, p, inputs, g, inc_override

    def filter(self, batch, obs_mask=None, device='cpu', store=True):
        B, p, inputs, g, io = self.build(batch, device)
        om = None if obs_mask is None else B.asarray(obs_mask)
        out = ph.run_filter(B, inputs, p, g=g, inc_override=io, obs_mask=om, use_rev=self.use_rev,
                            project=self.project, store=store, use_rate=self.use_rate)
        return B, p, inputs, g, io, out

    # ------------------------------------------------------------------ forecasting
    def _gather_future(self, inputs, g, io, bidx, t0, h, T):
        steps = torch.arange(1, h + 1, device=bidx.device)
        tt = (t0[:, None] + steps[None, :]).clamp(max=T - 1)
        valid = (t0[:, None] + steps[None, :]) <= (T - 1)
        fut = {'C': inputs['C'][bidx[:, None], tt], 'dN': inputs['dN'][bidx[:, None], tt] * valid,
               'drv': inputs['drv'][bidx[:, None], tt], 'lmask': inputs['lmask'][bidx]}
        gf = None if g is None else g[bidx[:, None], tt]
        iof = None if io is None else io[bidx[:, None], tt] * valid[..., None]
        return fut, gf, iof, tt, valid

    def forecast_all(self, batch, obs_mask, h, device='cpu'):
        """Predict t+1..t+h from every origin t. Returns numpy mu,var [B,T,h] and filtered one-step stats."""
        with torch.no_grad():
            B, p, inputs, g, io, out = self.filter(batch, obs_mask, device)
            Bsz, T, K = inputs['C'].shape
            bidx = torch.arange(Bsz, device=inputs['C'].device).repeat_interleave(T)
            t0 = torch.arange(T, device=inputs['C'].device).repeat(Bsz)
            fut, gf, iof, _, _ = self._gather_future(inputs, g, io, bidx, t0, h, T)
            m0 = out['m'][bidx, t0]
            P0 = out['P'][bidx, t0]
            mu, var, _ = ph.forecast_from(B, m0, P0, fut, p, gf, iof, self.use_rev, self.use_rate)
            mu = mu.reshape(Bsz, T, h).cpu().numpy()
            var = var.reshape(Bsz, T, h).cpu().numpy()
            res = {'mu': mu, 'var': var, 'pred_mu': out['pred_mu'].cpu().numpy(),
                   'pred_var': out['pred_var'].cpu().numpy(),
                   'Rperm': ((out['m'][:, :, :K] * inputs['lmask'][:, None, :]).sum(-1)).cpu().numpy(),
                   'd0': out['m'][:, :, K].cpu().numpy(), 'r': out['m'][:, :, K + 1].cpu().numpy()}
            res['theta'] = (out['m'][:, :, K + 2].cpu().numpy() if self.use_rate else np.zeros_like(res['d0']))
            res['P_perm'] = (out['P'][:, :, :K, :K] * (inputs['lmask'][:, None, :, None] * inputs['lmask'][:, None, None, :])).sum((-1, -2)).cpu().numpy()
            if g is not None:
                res['g'] = g.cpu().numpy()
        return res

    # ------------------------------------------------------------------ loss
    def loss(self, batch, device='cpu', obs_mask=None, rng=None):
        cfg = self.cfg
        B, p, inputs, g, io, out = self.filter(batch, obs_mask, device)
        tm = inputs['tmask']
        nll_f = -(out['ll'][:, 1:]).sum() / tm[:, 1:].sum()
        loss = nll_f
        lam_mse = cfg.get('lambda_mse', 0.0)
        if lam_mse > 0:
            ef = (out['pred_mu'][:, 1:] - inputs['y'][:, 1:]) ** 2 * tm[:, 1:]
            loss = loss + lam_mse * ef.sum() / tm[:, 1:].sum()
        nll_ms = torch.zeros((), dtype=nll_f.dtype)
        lam_ms = 0.0 if self.variant == 'no_ms' else cfg.get('lambda_ms', 1.0)
        if lam_ms > 0:
            Bsz, T, K = inputs['C'].shape
            h = cfg.get('ms_horizon', 12)
            n_o = cfg.get('ms_origins', 24)
            rng = rng or np.random.default_rng(0)
            lens = tm.sum(1).long().cpu().numpy()
            bl, tl = [], []
            for b in range(Bsz):
                hi = max(1, lens[b] - 2)
                t0 = rng.integers(0, hi, size=n_o)
                bl.append(np.full(n_o, b))
                tl.append(t0)
            bidx = torch.as_tensor(np.concatenate(bl), device=tm.device)
            t0 = torch.as_tensor(np.concatenate(tl), device=tm.device)
            fut, gf, iof, tt, valid = self._gather_future(inputs, g, io, bidx, t0, h, T)
            mu, var, _ = ph.forecast_from(B, out['m'][bidx, t0], out['P'][bidx, t0], fut, p, gf, iof, self.use_rev,
                                          self.use_rate)
            yt = inputs['y'][bidx[:, None], tt]
            w = valid * tm[bidx[:, None], tt]
            nll = 0.5 * (torch.log(2 * math.pi * var) + (yt - mu) ** 2 / var)
            nll_ms = (nll * w).sum() / w.sum().clamp(min=1.0)
            loss = loss + lam_ms * nll_ms
            if lam_mse > 0:
                loss = loss + lam_mse * (((yt - mu) ** 2) * w).sum() / w.sum().clamp(min=1.0)
        pen = cfg.get('lambda_u', 0.5) * (self.u_mat ** 2).sum() + cfg.get('lambda_cls', 0.5) * (self.log_cls ** 2).sum()
        pen = pen + cfg.get('lambda_toff', 0.05) * (self.T_off - self.t_off_prior) ** 2
        pen = pen + 0.1 * (self.b_beta ** 2 + self.c_gamma ** 2)
        if g is not None:
            pen = pen + cfg.get('lambda_g', 0.05) * (g ** 2).mean()
        loss = loss + pen / max(1, len(batch['names']))
        return loss, {'nll_f': float(nll_f), 'nll_ms': float(nll_ms)}

    def summary(self):
        with torch.no_grad():
            p = self.phys_params()
            return {'beta': float(p['beta']), 'gamma': float(p['gamma']), 'scale': float(torch.exp(self.log_scale)),
                    'scale_cls': p['scale_cls'].cpu().numpy().tolist(), 'R0_eff': p['R0_slot'].cpu().numpy().tolist(),
                    'T_off': float(p['T_off']), 'damp_mm': float(p['damp_mm']), 'T_bar': float(p['T_bar']),
                    'cE': float(p['cE']), 'phi': float(p['phi']), 'sig_r': float(p['sig_r']),
                    'sig_m': float(p['sig_m']), 'q_rel': float(p['q_rel']), 'mu_d0': float(p['mu_d0']),
                    'sig_theta': float(p['sig_theta']), 'q_theta': float(p['q_theta']), 'q_d0': float(p['q_d0']),
                    'kappa_T': p['kappa_T'].cpu().numpy().tolist(), 'kappa_D': p['kappa_D'].cpu().numpy().tolist()}


def calibrate_scale(cfg, structs, r0, known, t_off, mu_d0):
    """Initial global scale so that the uncalibrated layered law matches the mean measured growth."""
    B = ph.NumpyBackend()
    batch = pad_batch(structs)
    base = np.where(known, r0, np.nanmean(r0))
    p = dict(T_bar=cfg.get('T_bar_init', 12.0), T_off=t_off, damp_mm=cfg.get('damp_mm_init', 300.0),
             cE=cfg.get('cE_init', 0.06), E20_slot=np.asarray(cfg['E20_slot'], float), R0_slot=base,
             scale_cls=np.ones(len(CLASSES)), gamma=2.93, kappa_T=np.zeros(len(CLASSES)), kappa_D=np.zeros(len(CLASSES)))
    inp = ph.build_inputs(B, batch, p)
    C, N = inp['C'], inp['N']
    # time-hardening integration without noise
    K = C.shape[-1]
    R = C[:, 0, :] * np.power(np.maximum(N[:, 0], 1.0)[:, None], 0.48)
    R0 = R.sum(-1).copy()
    for t in range(1, C.shape[1]):
        Neq = np.power(np.maximum(R, 1e-6) / np.maximum(C[:, t, :], 1e-30), 1 / 0.48)
        R = np.where(inp['lmask'] > 0, np.maximum(C[:, t, :] * np.power(Neq + inp['dN'][:, t, None], 0.48), R), 0)
    growth_phys = (R.sum(-1) - R0).mean()
    lens = batch['tmask'].sum(1).astype(int)
    growth_obs = np.mean([batch['y'][b, lens[b] - 1] - batch['y'][b, 0] for b in range(len(lens))])
    return float(np.log(max(growth_obs, 1e-3) / max(growth_phys, 1e-6)))


def train_mssa(cfg, train_structs, val_structs, r0, known, t_off, seed=0, device='cpu', log=print):
    torch.manual_seed(seed)
    rng = np.random.default_rng(seed)
    mu_d0 = float(np.mean([s.y[0] for s in train_structs]))
    cfg = dict(cfg)
    if 'log_scale_init' not in cfg:
        cfg['log_scale_init'] = calibrate_scale(cfg, train_structs, r0, known, t_off, mu_d0)
    model = MSSA(cfg, r0, known, t_off, mu_d0).to(device)
    phys = [p for n, p in model.named_parameters() if not (n.startswith('net') or n.startswith('emb'))]
    nnp = [p for n, p in model.named_parameters() if n.startswith('net') or n.startswith('emb')]
    opt = torch.optim.Adam([{'params': phys, 'lr': cfg.get('lr_phys', 1e-2)},
                            {'params': nnp, 'lr': cfg.get('lr_nn', 2e-3)}])
    tb = pad_batch(train_structs)
    vb = pad_batch(val_structs) if val_structs else None
    best, best_state, bad = float('inf'), None, 0
    epochs, patience, every = cfg.get('epochs', 300), cfg.get('patience', 8), cfg.get('val_every', 10)
    t_start = time.time()
    for ep in range(1, epochs + 1):
        model.train()
        opt.zero_grad()
        loss, info = model.loss(tb, device, rng=rng)
        if not torch.isfinite(loss):
            log(f'  non-finite loss at epoch {ep}; stopping')
            break
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), cfg.get('grad_clip', 5.0))
        opt.step()
        if ep % every == 0 or ep == epochs:
            if vb is not None:
                model.eval()
                res = model.forecast_all(vb, None, cfg.get('val_horizon', 6), device)
                err = val_metric(res, vb, cfg.get('val_horizon', 6))
            else:
                err = float(loss)
            if err < best - 1e-5:
                best, best_state, bad = err, copy.deepcopy(model.state_dict()), 0
            else:
                bad += 1
            if ep % (every * 5) == 0:
                log(f'  ep {ep:4d} loss {float(loss):.4f} nll_f {info["nll_f"]:.3f} nll_ms {info["nll_ms"]:.3f} '
                    f'val {err:.4f} ({time.time() - t_start:.0f}s)')
            if bad >= patience:
                break
    if best_state is not None:
        model.load_state_dict(best_state)
    model.eval()
    return model


def val_metric(res, batch, h):
    """Mean RMSE over horizons 1..h on observed targets (inner validation)."""
    mu = res['mu']
    y, tm = batch['y'], batch['tmask']
    Bsz, T, H = mu.shape
    errs = []
    for j in range(H):
        tgt = np.full((Bsz, T), np.nan)
        tgt[:, :T - j - 1] = y[:, j + 1:]
        ok = np.zeros((Bsz, T), bool)
        ok[:, :T - j - 1] = tm[:, j + 1:] > 0
        e = (mu[:, :, j] - tgt)[ok]
        errs.append(np.sqrt(np.mean(e ** 2)))
    return float(np.mean(errs))


def export_numpy(model, batch, obs_mask=None, device='cpu'):
    """Inputs, discrepancy, filtered states and parameters as numpy (for Monte Carlo / analysis)."""
    with torch.no_grad():
        B, p, inputs, g, io, out = model.filter(batch, obs_mask, device)
        cv = lambda x: None if x is None else (x.detach().cpu().numpy() if hasattr(x, 'detach') else x)
        pn = {k: cv(v) for k, v in p.items()}
        return {'C': cv(inputs['C']), 'dN': cv(inputs['dN']), 'drv': cv(inputs['drv']), 'lmask': cv(inputs['lmask']),
                'g': cv(g), 'io': cv(io), 'm': cv(out['m']), 'P': cv(out['P']), 'p': pn, 'use_rev': model.use_rev,
                'use_rate': model.use_rate}
