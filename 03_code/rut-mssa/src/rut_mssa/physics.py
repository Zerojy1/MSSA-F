"""Backend-agnostic physics and constrained extended Kalman filter.

Every function takes a backend object `B` (NumpyBackend or TorchBackend) so the same equations run in
numpy (testing, Monte Carlo, synthetic data) and in torch (end-to-end training).

State per structure: x = [R_1 .. R_K, d0, r]
  R_k : permanent deformation of asphalt sublayer k (mm), JTG D50-2017 layered law, time hardening
  d0  : initial deformation / measurement datum (mm), constant
  r   : reversible, temperature-driven component (mm), AR(1)
Observation: y_t = sum_k R_k + d0 + r + v_t
"""
from __future__ import annotations

import math

import numpy as np

A_JTG = 2.31e-8
H0_MM = 50.0          # thickness of the wheel-tracking specimen (JTG: h0)
Q_TYRE = 0.70         # MPa, standard axle BZZ-100 tyre pressure
A_TYRE = 106.5        # mm, radius of one tyre contact circle (d = 213 mm)
R_DUAL = 319.5        # mm, centre spacing of dual tyres (1.5 d)


class NumpyBackend:
    name = 'numpy'

    def __init__(self):
        self.xp = np

    def asarray(self, x):
        return np.asarray(x, dtype=float)

    exp = staticmethod(np.exp)
    log = staticmethod(np.log)
    sqrt = staticmethod(np.sqrt)
    tanh = staticmethod(np.tanh)
    einsum = staticmethod(np.einsum)
    maximum = staticmethod(np.maximum)
    minimum = staticmethod(np.minimum)
    where = staticmethod(np.where)

    def clip(self, x, lo=None, hi=None):
        return np.clip(x, lo, hi)

    def softplus(self, x):
        return np.logaddexp(0.0, x)

    def sigmoid(self, x):
        return 1.0 / (1.0 + np.exp(-x))

    def zeros(self, shape):
        return np.zeros(shape)

    def ones(self, shape):
        return np.ones(shape)

    def eye(self, n):
        return np.eye(n)

    def cat(self, xs, axis=-1):
        return np.concatenate(xs, axis=axis)

    def stack(self, xs, axis=0):
        return np.stack(xs, axis=axis)

    def diag_embed(self, v):
        return v[..., :, None] * np.eye(v.shape[-1])

    def take(self, table, idx):
        return np.asarray(table)[idx]

    def power(self, a, b):
        return np.power(a, b)


class TorchBackend:
    name = 'torch'

    def __init__(self, device='cpu', dtype=None):
        import torch
        self.torch = torch
        self.device = device
        self.dtype = dtype or torch.float64

    def asarray(self, x):
        t = self.torch
        if isinstance(x, t.Tensor):
            return x.to(self.device, self.dtype)
        return t.as_tensor(np.asarray(x, dtype=float), device=self.device, dtype=self.dtype)

    def exp(self, x):
        return self.torch.exp(x)

    def log(self, x):
        return self.torch.log(x)

    def sqrt(self, x):
        return self.torch.sqrt(x)

    def tanh(self, x):
        return self.torch.tanh(x)

    def einsum(self, s, *a):
        return self.torch.einsum(s, *a)

    def maximum(self, a, b):
        t = self.torch
        if not isinstance(b, t.Tensor):
            return t.clamp(a, min=b)
        if not isinstance(a, t.Tensor):
            return t.clamp(b, min=a)
        return t.maximum(a, b)

    def minimum(self, a, b):
        t = self.torch
        if not isinstance(b, t.Tensor):
            return t.clamp(a, max=b)
        return t.minimum(a, b)

    def where(self, c, a, b):
        t = self.torch
        c = c if isinstance(c, t.Tensor) else self.asarray(c)
        return t.where(c.bool(), a, b)

    def clip(self, x, lo=None, hi=None):
        return self.torch.clamp(x, min=lo, max=hi)

    def softplus(self, x):
        return self.torch.nn.functional.softplus(x)

    def sigmoid(self, x):
        return self.torch.sigmoid(x)

    def zeros(self, shape):
        return self.torch.zeros(shape, device=self.device, dtype=self.dtype)

    def ones(self, shape):
        return self.torch.ones(shape, device=self.device, dtype=self.dtype)

    def eye(self, n):
        return self.torch.eye(n, device=self.device, dtype=self.dtype)

    def cat(self, xs, axis=-1):
        return self.torch.cat(xs, dim=axis)

    def stack(self, xs, axis=0):
        return self.torch.stack(xs, dim=axis)

    def diag_embed(self, v):
        return self.torch.diag_embed(v)

    def take(self, table, idx):
        idx = idx if isinstance(idx, self.torch.Tensor) else self.torch.as_tensor(idx, device=self.device)
        return table[idx.long()]

    def power(self, a, b):
        return self.torch.pow(a, b)


# ---------------------------------------------------------------- physics blocks

def layer_temperature(B, T_air, zmid, p):
    """Sublayer temperature from interval-average air temperature.

    T_layer = T_bar + (T_air - T_bar + T_off) * exp(-z / d)
    Depth damping of the seasonal wave with a surface-air offset (prior from the FWD records) is the
    form used for RIOHTrack depth-temperature fitting (Xiao et al., 2020); d and T_off are learnable.
    T_air: [B,T]; zmid: [B,K] (mm) -> [B,T,K]
    """
    damp = B.exp(-zmid[:, None, :] / p['damp_mm'])
    return p['T_bar'] + (T_air[:, :, None] - p['T_bar'] + p['T_off']) * damp


def effective_temperature(B, T_layer, t_floor=1.0, sharp=1.0):
    """Smooth positive temperature for the power law (JTG uses a positive equivalent temperature)."""
    return t_floor + B.softplus(sharp * (T_layer - t_floor)) / sharp


def k_R(B, zmid, ha):
    """JTG D50-2017 comprehensive correction coefficient k_Ri (z in mm, h_a in mm capped at 200)."""
    ha = B.minimum(ha, 200.0)[:, None]
    d1 = -1.35e-4 * ha ** 2 + 8.18e-2 * ha - 14.50
    d2 = 8.78e-7 * ha ** 2 - 1.50e-3 * ha + 0.90
    k = (d1 + d2 * zmid) * B.exp(zmid * math.log(0.9731))
    return B.maximum(k, 0.0)


def vertical_stress(B, h, T_layer, E20, cE, f_odemark=0.9):
    """Vertical compressive stress at the top of each sublayer (MPa), Odemark + Boussinesq.

    Odemark equivalent depth of the top of sublayer i in the modulus of sublayer i:
        h_e,i = f * sum_{j<i} h_j (E_j / E_i)^(1/3)
    Asphalt modulus E(T) = E20 * exp(-cE (T - 20)). Only layers above i enter, so base moduli are not
    needed for asphalt sublayers. Stress = on-axis circular load + adjacent dual tyre as point load.
    h: [B,K]; T_layer: [B,T,K]; E20: [B,K] -> [B,T,K]
    """
    K = h.shape[-1]
    Ec = (E20[:, None, :] * B.exp(-cE * (T_layer - 20.0))) ** (1.0 / 3.0)
    U = B.asarray(np.tril(np.ones((K, K)), -1))            # U[i,j] = 1 if j < i
    he = f_odemark * B.einsum('kj,btj->btk', U, h[:, None, :] * Ec) / Ec
    a2 = A_TYRE ** 2
    on_axis = Q_TYRE * (1.0 - he ** 3 / (a2 + he ** 2) ** 1.5)
    P = Q_TYRE * math.pi * a2
    adjacent = 3.0 * P * he ** 3 / (2.0 * math.pi * (R_DUAL ** 2 + he ** 2) ** 2.5)
    return on_axis + adjacent


def jtg_coefficient(B, kR, Teff, p_i, h, R0eff, scale, gamma):
    """C = 2.31e-8 * scale * k_R * T^gamma * p^1.8 * (h/h0) * R0  so that R = C * N^beta (JTG form)."""
    return A_JTG * scale * kR[:, None, :] * Teff ** gamma * p_i ** 1.80 * (h[:, None, :] / H0_MM) * R0eff[:, None, :]


# ---------------------------------------------------------------- filter

def init_state(B, C0, N0, beta, lmask, p, use_rate=False, use_shape=False):
    """Prior at the first observation: R_k from the layered law at N0, d0 ~ N(mu_d0, s_d0^2), r ~ stationary,
    optional structure-specific log-rate theta ~ N(0, s_theta^2) (state augmentation for joint
    state-parameter estimation, as in EnKF updating of rutting models; Haddad et al. 2023)."""
    Bsz, K = C0.shape
    R = C0 * B.power(B.maximum(N0, 1.0)[:, None], beta) * lmask
    d0 = B.ones((Bsz, 1)) * p['mu_d0']
    r = B.zeros((Bsz, 1))
    parts = [R, d0, r]
    var_r = p['sig_r'] ** 2 / (1.0 - p['phi'] ** 2 + 1e-6)
    v = [(0.5 * R + 1e-3) ** 2 * lmask + 1e-8, B.ones((Bsz, 1)) * p['sig_d0'] ** 2, B.ones((Bsz, 1)) * var_r]
    if use_rate:
        parts.append(B.zeros((Bsz, 1)))
        v.append(B.ones((Bsz, 1)) * p['sig_theta'] ** 2)
    if use_shape:
        parts.append(B.zeros((Bsz, 1)))
        v.append(B.ones((Bsz, 1)) * p['sig_eta'] ** 2)
    return B.cat(parts, -1), B.diag_embed(B.cat(v, -1))


def propagate(B, m, P, C, dN, g, lmask, drv, beta, p, inc_override=None, use_rev=True, use_rate=False,
              use_shape=False):
    """One time-hardening step for each sublayer with multiplicative discrepancy exp(g).

    Structure-specific level theta and growth exponent eta (beta_s = beta * exp(eta)), with the level pinned at
    a reference load N_ref so that eta changes the curvature, not the level:
      A = C exp(theta) N_ref^(beta - beta_s);  N_eq = (R / A)^(1/beta_s)
      R' = R + exp(g) * (A (N_eq + dN)^beta_s - R)
    Jacobian (analytic, verified by finite differences in tests):
      dR'/dR     = 1 + exp(g) * (((N_eq + dN)/N_eq)^(beta_s-1) - 1)
      dR'/dtheta = exp(g) * A (N_eq + dN)^(beta_s-1) dN
      dR'/deta   = exp(g) * beta_s * [ f (ln Nn - N_eq ln N_eq / Nn) - A Nn^(beta_s-1) dN ln N_ref ],  f = A Nn^beta_s
    """
    K = C.shape[-1]
    eps = 1e-5
    R = B.maximum(m[:, :K], eps)
    Csafe = B.where(lmask > 0, C, B.ones(C.shape))
    th = m[:, K + 2:K + 3] if use_rate else None
    et = m[:, K + 3:K + 4] if use_shape else None
    ex = B.exp(th) if use_rate else 1.0
    lnNref = math.log(p.get('N_ref', 1e7)) if isinstance(p, dict) else math.log(1e7)
    if use_shape:
        bs = beta * B.exp(et)
        A = B.maximum(Csafe * ex * B.exp((beta - bs) * lnNref), 1e-30)
    else:
        bs = beta
        A = B.maximum(Csafe * ex, 1e-30)
    if inc_override is None:
        Neq = B.power(R / A, 1.0 / bs)
        Nn = Neq + dN[:, None]
        f = A * B.power(Nn, bs)
        inc = B.maximum(f - R, 0.0)
        ratio = B.power(Nn / B.maximum(Neq, 1e-12), bs - 1.0)
        eg = B.exp(g)
        Rn = R + eg * inc * lmask
        J = 1.0 + eg * (ratio - 1.0) * lmask
        inc_eff = eg * inc * lmask
        dAterm = A * B.power(Nn, bs - 1.0) * dN[:, None]
        dth = eg * dAterm * lmask
        if use_shape:
            Neq_s = B.maximum(Neq, 1e-12)
            deta = eg * bs * (f * (B.log(Nn) - Neq_s * B.log(Neq_s) / Nn) - dAterm * lnNref) * lmask
    else:
        inc_eff = inc_override * ex * lmask
        Rn = R + inc_eff
        J = B.ones(R.shape)
        dth = inc_eff
        deta = inc_eff * 0.0
    d0 = m[:, K:K + 1]
    r = m[:, K + 1:K + 2]
    phi = p['phi']
    if use_rev:
        rn = phi * r + (1.0 - phi) * drv[:, None]
        Jr = B.ones(r.shape) * phi
        qr = B.ones(r.shape) * p['sig_r'] ** 2
    else:
        rn = r * 0.0
        Jr = B.zeros(r.shape)
        qr = B.ones(r.shape) * 1e-10
    parts = [Rn * lmask, d0, rn]
    Jd_parts = [J, B.ones(d0.shape), Jr]
    q_parts = [(p['q_rel'] * inc_eff) ** 2 + p['q_abs'] ** 2 * lmask + 1e-10,
               B.ones(d0.shape) * (p['q_d0'] ** 2 if 'q_d0' in p else 1e-10), qr]
    if use_rate:
        parts.append(th)
        Jd_parts.append(B.ones(th.shape))
        q_parts.append(B.ones(th.shape) * p['q_theta'] ** 2)
    if use_shape:
        parts.append(et)
        Jd_parts.append(B.ones(et.shape))
        q_parts.append(B.ones(et.shape) * p['q_eta'] ** 2)
    mn = B.cat(parts, -1)
    Jd = B.cat(Jd_parts, -1)
    S = Jd.shape[-1]
    F = B.diag_embed(Jd)
    if use_rate:
        col = B.cat([dth, B.zeros((dth.shape[0], S - K))], -1)
        F = F + col[:, :, None] * B.asarray(np.eye(S)[K + 2])[None, None, :]
    if use_shape:
        col = B.cat([deta, B.zeros((deta.shape[0], S - K))], -1)
        F = F + col[:, :, None] * B.asarray(np.eye(S)[K + 3])[None, None, :]
    Pn = B.einsum('bij,bjk,blk->bil', F, P, F)
    Pn = Pn + B.diag_embed(B.cat(q_parts, -1))
    return mn, Pn, inc_eff


def obs_vector(B, lmask, use_rev=True, use_rate=False, use_shape=False):
    Bsz = lmask.shape[0]
    rcoef = B.ones((Bsz, 1)) if use_rev else B.zeros((Bsz, 1))
    parts = [lmask, B.ones((Bsz, 1)), rcoef]
    if use_rate:
        parts.append(B.zeros((Bsz, 1)))
    if use_shape:
        parts.append(B.zeros((Bsz, 1)))
    return B.cat(parts, -1)


def predict_obs(B, m, P, H, sig_m):
    mu = (H * m).sum(-1)
    var = B.einsum('bi,bij,bj->b', H, P, H) + sig_m ** 2
    return mu, var


def update(B, m, P, y, obs, H, sig_m, R_lb=None, K=None, project=True):
    """Kalman update with scalar observation; projection of permanent states onto R >= R_lb.

    Projection follows the estimate-projection approach for state constraints (Simon & Chia 2002;
    Simon 2010): the unconstrained update is projected onto the feasible set, here a box.
    """
    mu, s = predict_obs(B, m, P, H, sig_m)
    innov = y - mu
    Ph = B.einsum('bij,bj->bi', P, H)
    Kg = Ph / s[:, None]
    mu_new = m + Kg * innov[:, None]
    P_new = P - Kg[:, :, None] * Kg[:, None, :] * s[:, None, None]
    if project and R_lb is not None:
        Rp = B.maximum(mu_new[:, :K], R_lb)
        mu_new = B.cat([Rp, mu_new[:, K:]], -1)
    o = obs[:, None]
    m_out = B.where(o > 0, mu_new, m)
    P_out = B.where(o[:, :, None] > 0, P_new, P)
    ll = -0.5 * (B.log(2.0 * math.pi * s) + innov ** 2 / s) * obs
    return m_out, P_out, ll, mu, s


def run_filter(B, inputs, p, g=None, inc_override=None, obs_mask=None, use_rev=True, project=True,
               store=True, use_rate=False, use_shape=False):
    """Filter a padded batch. inputs (backend arrays): C [B,T,K], dN [B,T], N [B,T], y [B,T],
    tmask [B,T], lmask [B,K], drv [B,T]. Returns dict with per-step predictive mean/var (one-step-ahead,
    before the update), filtered means/covs, total log-likelihood per structure.
    """
    C, dN, N, y = inputs['C'], inputs['dN'], inputs['N'], inputs['y']
    tmask, lmask, drv = inputs['tmask'], inputs['lmask'], inputs['drv']
    Bsz, T, K = C.shape
    obs = tmask if obs_mask is None else obs_mask * tmask
    beta = p['beta']
    H = obs_vector(B, lmask, use_rev, use_rate, use_shape)
    m, P = init_state(B, C[:, 0, :], N[:, 0], beta, lmask, p, use_rate, use_shape)
    zeroK = B.zeros((Bsz, K))
    pred_mu, pred_var, ms, Ps, lls, incs = [], [], [], [], [], []
    for t in range(T):
        if t > 0:
            gt = zeroK if g is None else g[:, t, :]
            io = None if inc_override is None else inc_override[:, t, :]
            R_prev = m[:, :K]
            m, P, inc = propagate(B, m, P, C[:, t, :], dN[:, t], gt, lmask, drv[:, t], beta, p, io, use_rev, use_rate, use_shape)
        else:
            R_prev = None
            inc = zeroK
        m, P, ll, mu, s = update(B, m, P, y[:, t], obs[:, t], H, p['sig_m'], R_prev, K, project)
        if store:
            pred_mu.append(mu)
            pred_var.append(s)
            ms.append(m)
            Ps.append(P)
            incs.append(inc)
        lls.append(ll)
    out = {'ll': B.stack(lls, 1)}
    if store:
        out.update(pred_mu=B.stack(pred_mu, 1), pred_var=B.stack(pred_var, 1), m=B.stack(ms, 1),
                   P=B.stack(Ps, 1), inc=B.stack(incs, 1), H=H)
    return out


def forecast_from(B, m0, P0, inputs_future, p, g_future=None, inc_override=None, use_rev=True, use_rate=False,
                  use_shape=False):
    """Propagate without updates. inputs_future: C [B,h,K], dN [B,h], drv [B,h], lmask [B,K]."""
    C, dN, drv, lmask = inputs_future['C'], inputs_future['dN'], inputs_future['drv'], inputs_future['lmask']
    Bsz, h, K = C.shape
    H = obs_vector(B, lmask, use_rev, use_rate, use_shape)
    m, P = m0, P0
    mus, vars_, Rsum = [], [], []
    zeroK = B.zeros((Bsz, K))
    for j in range(h):
        gj = zeroK if g_future is None else g_future[:, j, :]
        io = None if inc_override is None else inc_override[:, j, :]
        m, P, _ = propagate(B, m, P, C[:, j, :], dN[:, j], gj, lmask, drv[:, j], p['beta'], p, io, use_rev, use_rate, use_shape)
        mu, var = predict_obs(B, m, P, H, p['sig_m'])
        mus.append(mu)
        vars_.append(var)
        Rsum.append((m[:, :K] * lmask).sum(-1) + m[:, K])
    return B.stack(mus, 1), B.stack(vars_, 1), B.stack(Rsum, 1)


def build_inputs(B, batch, p, t_floor=1.0):
    """Compute C [B,T,K] and the reversible driver from a padded batch (numpy dict from data.pad_batch).

    p must hold: T_bar, T_off, damp_mm, cE, E20_slot [n_slots], R0_slot [n_slots] (effective, mm),
    scale_cls [n_cls] (multiplier incl. global scale), gamma, kappa_T [n_cls], kappa_D [n_cls].
    """
    h = B.asarray(batch['h'])
    zmid = B.asarray(batch['zmid'])
    lmask = B.asarray(batch['lmask'])
    T_air = B.asarray(batch['T_air'])
    ha = B.asarray(batch['ha'])
    slot = batch['slot']
    cls = batch['cls']
    T_layer = layer_temperature(B, T_air, zmid, p)
    Teff = effective_temperature(B, T_layer, t_floor)
    E20 = B.take(p['E20_slot'], slot)
    p_i = vertical_stress(B, h, T_layer, E20, p['cE'])
    kR = k_R(B, zmid, ha)
    R0eff = B.take(p['R0_slot'], slot) * lmask
    scale = B.take(p['scale_cls'], cls)[:, None, None]
    C = jtg_coefficient(B, kR, Teff, p_i, h, R0eff, scale, p['gamma'])
    C = C * lmask[:, None, :]
    kT = B.take(p['kappa_T'], cls)[:, None]
    kD = B.take(p['kappa_D'], cls)[:, None]
    d0n = B.asarray(batch['d0n'])
    drv = kT * (T_air - p['T_bar']) / 10.0 + kD * (d0n - 1.0)
    return {'C': C, 'dN': B.asarray(batch['dN']), 'N': B.asarray(batch['N']), 'y': B.asarray(batch['y']),
            'tmask': B.asarray(batch['tmask']), 'lmask': lmask, 'drv': drv, 'T_layer': T_layer, 'p_i': p_i,
            'kR': kR}


def slice_future(inputs, t0, h):
    """Future inputs for forecasting from each origin t0 (numpy/torch index-agnostic for one origin)."""
    return {'C': inputs['C'][:, t0 + 1:t0 + 1 + h, :], 'dN': inputs['dN'][:, t0 + 1:t0 + 1 + h],
            'drv': inputs['drv'][:, t0 + 1:t0 + 1 + h], 'lmask': inputs['lmask']}
