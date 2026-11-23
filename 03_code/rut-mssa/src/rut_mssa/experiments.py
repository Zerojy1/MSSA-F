"""Experiment protocols E0-E6 (see README). Every function appends tidy rows to result tables."""
from __future__ import annotations

import json
import os
import time

import numpy as np
import pandas as pd
from scipy.stats import mannwhitneyu, spearmanr

from . import baselines as bl
from . import metrics as mt
from . import physics as ph
from .data import AC_SLOTS, CLASSES, folds, load_structures, material_prior, pad_batch, surface_air_offset

try:
    import torch
    from .model import export_numpy, train_mssa
except ImportError:
    torch = None


# ============================================================================ helpers
class Ctx:
    def __init__(self, cfg, out_dir, log):
        self.cfg, self.out_dir, self.log = cfg, out_dir, log
        self.data_dir = cfg['data_dir']
        self.S = load_structures(self.data_dir, cfg['model'])
        self.r0, self.known = material_prior(self.data_dir)
        self.t_off = surface_air_offset(self.data_dir)
        self.device = cfg.get('device', 'cpu')
        self.rows = {}

    def add(self, table, rows):
        if not rows:
            return
        self.rows.setdefault(table, []).extend(rows)
        pd.DataFrame(self.rows[table]).to_csv(os.path.join(self.out_dir, f'{table}.csv'), index=False)


class MSSAPredictor:
    def __init__(self, model, device):
        self.model, self.device, self.name = model, device, 'mssa'

    def forecast_all(self, batch, obs_mask, h):
        return self.model.forecast_all(batch, obs_mask, h, self.device)


def inner_split(train_names, n_val, seed, anchors=('STR4', 'STR5', 'STR9', 'STR14')):
    rng = np.random.default_rng(seed)
    cand = [n for n in train_names if n not in anchors]
    val = list(rng.choice(cand, size=min(n_val, len(cand)), replace=False)) if n_val > 0 else []
    return [n for n in train_names if n not in val], val


def fit_mssa(ctx, train_names, seed, variant='full', extra=None, n_val=None):
    cfgm = dict(ctx.cfg['model'])
    cfgm.update(ctx.cfg['train'])
    cfgm['variant'] = variant
    if extra:
        cfgm.update(extra)
    n_val = ctx.cfg['train'].get('n_inner_val', 2) if n_val is None else n_val
    tr, va = inner_split(train_names, n_val, seed)
    t0 = time.time()
    model = train_mssa(cfgm, [ctx.S[n] for n in tr], [ctx.S[n] for n in va], ctx.r0, ctx.known, ctx.t_off,
                       seed=seed, device=ctx.device, log=ctx.log)
    ctx.log(f'    MSSA[{variant}] trained on {len(tr)} (+{len(va)} inner val) in {time.time() - t0:.0f}s')
    return model


def fit_baseline(ctx, name, train_names, seed):
    m = bl.make_baseline(name)
    structs = [ctx.S[n] for n in train_names]
    cfgb = dict(ctx.cfg['baselines'])
    cfgb['device'] = ctx.device
    cfgb.update({k: ctx.cfg['model'][k] for k in ('E20_slot', 'T_bar_init', 'damp_mm_init', 'cE_init') if k in ctx.cfg['model']})
    if name in ('jtg_global', 'jtg_enkf'):
        return m.fit(structs, cfgb, seed, r0=ctx.r0, known=ctx.known, t_off=ctx.t_off)
    return m.fit(structs, cfgb, seed)


def test_batch(ctx, names):
    b = pad_batch([ctx.S[n] for n in names])
    return b


def _per_structure(rows_meta, names, y, mu, var, mask):
    out = []
    for i, n in enumerate(names):
        m = mask[i]
        r = dict(rows_meta, structure=n, cls=None)
        r.update(mt.point(y[i][m], mu[i][m]))
        if var is not None:
            r.update(mt.gaussian(y[i][m], mu[i][m], var[i][m]))
        out.append(r)
    return out


# ============================================================================ protocols
def protocol_horizons(pred, batch, meta, horizons):
    H = max(horizons)
    res = pred.forecast_all(batch, None, H)
    y, tm = batch['y'], batch['tmask']
    Bsz, T = y.shape
    rows = []
    for h in horizons:
        tgt = np.full((Bsz, T), np.nan)
        tgt[:, :T - h] = y[:, h:]
        ok = np.zeros((Bsz, T), bool)
        ok[:, :T - h] = tm[:, h:] > 0
        mu = res['mu'][:, :, h - 1]
        var = None if res.get('var') is None else res['var'][:, :, h - 1]
        rows += _per_structure(dict(meta, protocol='horizon', setting=h), batch['names'], tgt, mu, var, ok)
    return rows, res


def protocol_sparse(pred, batch, meta, ks, store=None):
    rows = []
    T = batch['y'].shape[1]
    tm = batch['tmask'] > 0
    for k in ks:
        om = (np.arange(T)[None, :] % k == 0).astype(float) * np.ones_like(batch['y'])
        res = pred.forecast_all(batch, om, 1)
        if store is not None:
            store[k] = (res['pred_mu'], res.get('pred_var'))
        ok = tm.copy()
        ok[:, 0] = False
        var = res.get('pred_var')
        rows += _per_structure(dict(meta, protocol='sparse_all', setting=k), batch['names'], batch['y'], res['pred_mu'],
                               var, ok)
        ok2 = ok & (om == 0)
        if k > 1:
            rows += _per_structure(dict(meta, protocol='sparse_unobserved', setting=k), batch['names'], batch['y'],
                                   res['pred_mu'], var, ok2)
    return rows


def early_mask(batch, frac):
    lens = batch['tmask'].sum(1).astype(int)
    T = batch['y'].shape[1]
    cut = np.maximum(2, (lens * frac).astype(int))
    om = (np.arange(T)[None, :] < cut[:, None]).astype(float)
    return om, cut


def protocol_early(pred, batch, meta, fracs, thresholds):
    rows, store = [], {}
    tm = batch['tmask'] > 0
    lens = batch['tmask'].sum(1).astype(int)
    for f in fracs:
        om, cut = early_mask(batch, f)
        res = pred.forecast_all(batch, om, 1)
        rows += early_rows(batch, f, res, meta, thresholds)
        store[f] = res
    return rows, store


def early_rows(batch, f, res, meta, thresholds):
    rows = []
    tm = batch['tmask'] > 0
    lens = batch['tmask'].sum(1).astype(int)
    if True:
        om, cut = early_mask(batch, f)
        ok = tm & (om == 0)
        var = res.get('pred_var')
        rr = _per_structure(dict(meta, protocol='early_life', setting=f), batch['names'], batch['y'], res['pred_mu'],
                            var, ok)
        for i, r in enumerate(rr):
            e = res['pred_mu'][i, lens[i] - 1] - batch['y'][i, lens[i] - 1]
            r['end_abs_err'] = float(abs(e))
            pm = res['pred_mu'][i, cut[i]:lens[i]]
            r['mono_viol_frac'] = float(np.mean(np.diff(pm) < -0.05)) if len(pm) > 2 else np.nan
            if 'Rperm' in res:
                rp = res['Rperm'][i, cut[i]:lens[i]]
                r['perm_mono_viol_frac'] = float(np.mean(np.diff(rp) < -1e-9)) if len(rp) > 2 else np.nan
            for thr in thresholds:
                No = mt.first_crossing(batch['N'][i, :lens[i]], batch['y'][i, :lens[i]], thr)
                Np = mt.first_crossing(batch['N'][i, :lens[i]], np.where(np.arange(lens[i]) < cut[i], -np.inf,
                                                                          res['pred_mu'][i, :lens[i]]), thr)
                pre = np.any(batch['y'][i, :cut[i]] >= thr)
                r[f'fpt_obs_{thr}'] = No if not pre else np.nan
                r[f'fpt_pred_{thr}'] = Np if not pre else np.nan
                r[f'fpt_abs_err_Mload_{thr}'] = abs(Np - No) / 1e6 if (np.isfinite(No) and np.isfinite(Np) and not pre) else np.nan
        rows += rr
    return rows


def protocol_cold(pred, batch, meta, store=None):
    om = np.zeros_like(batch['y'])
    res = pred.forecast_all(batch, om, 1)
    if store is not None:
        store['cold'] = (res['pred_mu'], res.get('pred_var'))
    return cold_rows(batch, res['pred_mu'], res.get('pred_var'), meta)


def cold_rows(batch, mu, var, meta):
    ok = batch['tmask'] > 0
    return _per_structure(dict(meta, protocol='cold_start', setting=0), batch['names'], batch['y'], mu, var, ok)


def protocol_counterfactual(pred, batch, meta, frac=0.4, dT=5.0):
    """E4: perturb only the inputs AFTER the forecast origin (early-life cut); history, observations and the
    assimilated state are unchanged. A physically consistent model must predict more rutting for a warmer
    future (+dT on air temperature) and for heavier future traffic (load increments x2)."""
    om, cut = early_mask(batch, frac)
    T = batch['y'].shape[1]
    after = np.arange(T)[None, :] >= cut[:, None]
    base = pred.forecast_all(batch, om, 1)['pred_mu']
    b2 = {k: (v.copy() if isinstance(v, np.ndarray) else v) for k, v in batch.items()}
    b2['T_air'] = np.where(after, batch['T_air'] + dT, batch['T_air'])
    warm = pred.forecast_all(b2, om, 1)['pred_mu']
    b3 = {k: (v.copy() if isinstance(v, np.ndarray) else v) for k, v in batch.items()}
    b3['dN'] = np.where(after, batch['dN'] * 2.0, batch['dN'])
    b3['N'] = np.cumsum(b3['dN'], 1)
    heavy = pred.forecast_all(b3, om, 1)['pred_mu']
    lens = batch['tmask'].sum(1).astype(int)
    rows = []
    for name, alt in (('temp_plus5', warm), ('load_x2', heavy)):
        d_all, d_end = [], []
        for i in range(len(lens)):
            d = alt[i, cut[i]:lens[i]] - base[i, cut[i]:lens[i]]
            d_all.append(d)
            d_end.append(d[-1])
        d_all = np.concatenate(d_all)
        d_end = np.asarray(d_end)
        rows.append(dict(meta, protocol='counterfactual', setting=name, frac_increase=float(np.mean(d_all > 1e-6)),
                         frac_decrease=float(np.mean(d_all < -1e-6)), mean_delta=float(np.mean(d_all)),
                         frac_increase_at_end=float(np.mean(d_end > 1e-6))))
    return rows


def protocol_aci(res_dense, batch, meta, alpha=0.05, gamma=0.01):
    rows = []
    lens = batch['tmask'].sum(1).astype(int)
    pv = res_dense.get('pred_var')
    if pv is None:
        return rows
    for i, n in enumerate(batch['names']):
        y = batch['y'][i, 1:lens[i]]
        mu = res_dense['pred_mu'][i, 1:lens[i]]
        sd = np.sqrt(pv[i, 1:lens[i]])
        lo, hi = mt.aci(y, mu, sd, alpha, gamma)
        ok = np.isfinite(lo)
        z = 1.959964
        nat = mt.interval_stats(y[ok], (mu - z * sd)[ok], (mu + z * sd)[ok], alpha)
        ac = mt.interval_stats(y, lo, hi, alpha)
        rows.append(dict(meta, protocol='aci', setting='native', structure=n, **nat))
        rows.append(dict(meta, protocol='aci', setting='aci', structure=n, **ac))
    return rows


def fpt_monte_carlo(model, batch, frac, thresholds, n_samp, device, rng):
    """Sample state trajectories after the early-life cut; distribution of first crossing (Si et al. 2011)."""
    om, cut = early_mask(batch, frac)
    ex = export_numpy(model, batch, om, device)
    p = ex['p']
    lens = batch['tmask'].sum(1).astype(int)
    rows = []
    Bn = ph.NumpyBackend()
    K = ex['C'].shape[-1]
    for i, n in enumerate(batch['names']):
        t0 = cut[i] - 1
        m0, P0 = ex['m'][i, t0], ex['P'][i, t0]
        L = np.linalg.cholesky(P0 + 1e-9 * np.eye(len(m0)))
        x = m0[None, :] + rng.standard_normal((n_samp, len(m0))) @ L.T
        x[:, :K] = np.maximum(x[:, :K], 1e-5) * ex['lmask'][i]
        traj = np.full((n_samp, lens[i]), np.nan)
        for t in range(t0 + 1, lens[i]):
            C = np.repeat(ex['C'][i:i + 1, t], n_samp, 0)
            lm = np.repeat(ex['lmask'][i:i + 1], n_samp, 0)
            g = np.zeros_like(C) if ex['g'] is None else np.repeat(ex['g'][i:i + 1, t], n_samp, 0)
            io = None if ex['io'] is None else np.repeat(ex['io'][i:i + 1, t], n_samp, 0)
            dN = np.full(n_samp, ex['dN'][i, t])
            drv = np.full(n_samp, ex['drv'][i, t])
            mn, _, inc = ph.propagate(Bn, x, np.zeros((n_samp, len(m0), len(m0))), C, dN, g, lm, drv, float(p['beta']),
                                      p, io, ex['use_rev'], ex.get('use_rate', False))
            noise = np.zeros_like(mn)
            noise[:, :K] = np.abs(rng.standard_normal((n_samp, K))) * (float(p['q_rel']) * inc) * lm
            if ex['use_rev']:
                noise[:, K + 1] = rng.standard_normal(n_samp) * float(p['sig_r'])
            x = mn + noise
            yv = (x[:, :K] * lm).sum(-1) + x[:, K] + (x[:, K + 1] if ex['use_rev'] else 0.0)
            traj[:, t] = yv + rng.standard_normal(n_samp) * float(p['sig_m'])
        N = batch['N'][i, :lens[i]]
        for thr in thresholds:
            if np.any(batch['y'][i, :cut[i]] >= thr):
                continue
            No = mt.first_crossing(N, batch['y'][i, :lens[i]], thr)
            fc = np.array([mt.first_crossing(N, np.where(np.arange(lens[i]) <= t0, -np.inf, tr), thr) for tr in traj])
            fin = np.isfinite(fc)
            r = dict(structure=n, frac=frac, threshold=thr, obs_crossing_Mload=No / 1e6 if np.isfinite(No) else np.nan,
                     p_cross_by_end=float(fin.mean()))
            if fin.sum() >= 10:
                q5, q50, q95 = np.percentile(fc[fin] / 1e6, [5, 50, 95])
                r.update(median_Mload=q50, q5=q5, q95=q95)
                if np.isfinite(No):
                    r['obs_in_90pct'] = bool(q5 <= No / 1e6 <= q95)
                    r['median_abs_err_Mload'] = abs(q50 - No / 1e6)
            rows.append(r)
    return rows


# ============================================================================ experiments
def evaluate_all_protocols(ctx, pred, batch, meta, ecfg, tag):
    rows, res = protocol_horizons(pred, batch, meta, ecfg['horizons'])
    sp = {}
    rows += protocol_sparse(pred, batch, meta, ecfg['sparse_k'], sp)
    er, store = protocol_early(pred, batch, meta, ecfg['early_fracs'], ecfg['thresholds'])
    rows += er
    cs = {}
    rows += protocol_cold(pred, batch, meta, cs)
    ctx.add('main_' + tag, rows)
    if ecfg.get('counterfactual', True):
        ctx.add('counterfactual_' + tag, protocol_counterfactual(pred, batch, meta))
    dense1 = pred.forecast_all(batch, None, 1)
    ctx.add('uq_aci_' + tag, protocol_aci(dense1, batch, meta))
    if meta['model'] in ctx.cfg['experiments'].get('save_pred_models', ['mssa', 'gbm_residual']) and res.get('var') is not None:
        arr = {'names': np.array(batch['names']), 'hmu': res['mu'], 'hvar': res['var']}
        for k, (m_, v_) in sp.items():
            arr[f's{k}_mu'], arr[f's{k}_var'] = m_, v_
        for f, r_ in store.items():
            arr[f'e{f}_mu'], arr[f'e{f}_var'] = r_['pred_mu'], r_.get('pred_var')
        arr['cold_mu'], arr['cold_var'] = cs['cold']
        np.savez_compressed(os.path.join(ctx.out_dir, 'pred', f"ALL_{tag}_f{meta['fold']}_s{meta['seed']}_{meta['model']}.npz"),
                            **{k: v for k, v in arr.items() if v is not None})
    return res, store


def exp_main(ctx, fold_kind='manuscript', tag='E1E2'):
    """E1 (multi-horizon + early-life), E2 (sparse), cold start, E4 counterfactual, UQ/ACI, baselines (E6)."""
    cfg = ctx.cfg
    ecfg = cfg['experiments']['protocols']
    seeds = cfg['seeds']
    models = cfg['experiments'][tag]['models']
    det = {'persistence', 'jtg_global', 'jtg_enkf'}
    fl = folds(fold_kind, ctx.S)
    for fi, (train, test) in enumerate(fl):
        if not test:
            continue
        batch = test_batch(ctx, test)
        cache = {}
        for seed in seeds:
            for mname in models:
                if mname in det and seed != seeds[0]:
                    continue
                meta = dict(exp=tag, folds=fold_kind, fold=fi, seed=seed, model=mname)
                ctx.log(f'[{tag}] fold {fi} seed {seed} model {mname} test={test}')
                try:
                    if mname.startswith('mssa_h'):
                        main = cache.get((fi, seed, 'full')) or fit_mssa(ctx, train, seed, 'full')
                        cache[(fi, seed, 'full')] = main
                        hyb = cache.get((fi, seed, 'hybrid')) or HybridMSSA(ctx).fit(train, seed, main_model=main)
                        cache[(fi, seed, 'hybrid')] = hyb
                        evaluate_all_protocols(ctx, hyb.view(monotone=not mname.endswith(':free')), batch, meta, ecfg, tag)
                    elif mname.startswith('mssa'):
                        variant = mname.split(':')[1] if ':' in mname else 'full'
                        model = cache.get((fi, seed, variant)) or fit_mssa(ctx, train, seed, variant)
                        cache[(fi, seed, variant)] = model
                        pred = MSSAPredictor(model, ctx.device)
                        res, store = evaluate_all_protocols(ctx, pred, batch, meta, ecfg, tag)
                        np.savez_compressed(os.path.join(ctx.out_dir, 'pred', f'{tag}_f{fi}_s{seed}_{mname.replace(":", "-")}.npz'),
                                            names=np.array(batch['names']), y=batch['y'], N=batch['N'],
                                            mu=res['mu'], var=res['var'], Rperm=res['Rperm'], r=res['r'], d0=res['d0'],
                                            **{f'early_{k}': v['pred_mu'] for k, v in store.items()},
                                            **{f'early_var_{k}': v['pred_var'] for k, v in store.items()})
                        if variant == 'full' and cfg['experiments'].get('fpt_mc', True):
                            rng = np.random.default_rng(seed)
                            for f in ecfg['early_fracs']:
                                rr = fpt_monte_carlo(model, batch, f, ecfg['thresholds'], cfg['experiments'].get('fpt_samples', 500),
                                                     ctx.device, rng)
                                ctx.add('fpt_mc_' + tag, [dict(meta, **r) for r in rr])
                        ctx.add('params_' + tag, [dict(meta, **{k: json.dumps(v) if isinstance(v, list) else v
                                                               for k, v in model.summary().items()})])
                    else:
                        m = fit_baseline(ctx, mname, train, seed)
                        evaluate_all_protocols(ctx, m, batch, meta, ecfg, tag)
                except Exception as e:  # keep the run going; failures are logged and tabulated
                    import traceback
                    ctx.log(f'  !! {mname} failed: {e}\n{traceback.format_exc()}')
                    ctx.add('failures', [dict(meta, error=str(e))])


def simulate_synthetic(ctx, truth, seed):
    """E0: generate rut series from the state-space model with known parameters on the real inputs."""
    rng = np.random.default_rng(seed)
    names = sorted(ctx.S.keys(), key=lambda s: int(s[3:]))
    structs = [ctx.S[n] for n in names]
    batch = pad_batch(structs)
    B = ph.NumpyBackend()
    base = np.where(ctx.known, ctx.r0, np.nanmean(ctx.r0))
    u = rng.normal(0, truth['u_sd'], len(AC_SLOTS))
    p = dict(T_bar=12.0, T_off=ctx.t_off, damp_mm=300.0, cE=0.06, E20_slot=np.asarray(ctx.cfg['model']['E20_slot'], float),
             R0_slot=base * np.exp(u), scale_cls=np.ones(len(CLASSES)) * np.exp(truth['log_scale']),
             gamma=truth['gamma'], kappa_T=np.full(len(CLASSES), truth['kappa_T']), kappa_D=np.zeros(len(CLASSES)))
    inp = ph.build_inputs(B, batch, p)
    C, dN, lm = inp['C'], inp['dN'], inp['lmask']
    Bsz, T, K = C.shape
    beta = truth['beta']
    R = C[:, 0, :] * np.power(np.maximum(inp['N'][:, 0], 1.0)[:, None], beta)
    d0 = rng.normal(truth['mu_d0'], 0.3, Bsz)
    r = np.zeros(Bsz)
    Ys, Rp, Rv = np.zeros((Bsz, T)), np.zeros((Bsz, T)), np.zeros((Bsz, T))
    for t in range(T):
        if t > 0:
            Neq = np.power(np.maximum(R, 1e-6) / np.maximum(C[:, t, :], 1e-30), 1 / beta)
            inc = np.maximum(C[:, t, :] * np.power(Neq + dN[:, t, None], beta) - R, 0) * lm
            R = R + inc * np.exp(truth['q_rel'] * rng.standard_normal(inc.shape) - 0.5 * truth['q_rel'] ** 2)
            r = truth['phi'] * r + (1 - truth['phi']) * inp['drv'][:, t] + truth['sig_r'] * rng.standard_normal(Bsz)
        Rp[:, t] = (R * lm).sum(-1) + d0
        Rv[:, t] = r
        Ys[:, t] = Rp[:, t] + r + truth['sig_m'] * rng.standard_normal(Bsz)
    synth = {}
    import copy
    for b, s in enumerate(structs):
        s2 = copy.deepcopy(s)
        n = len(s.y)
        s2.y = Ys[b, :n]
        synth[s.name] = s2
    return synth, {'u': u, 'Rperm': Rp, 'rev': Rv}


def exp_E0(ctx):
    ecfg = ctx.cfg['experiments']['E0']
    for level in ecfg['noise_levels']:
        for seed in ctx.cfg['seeds']:
            truth = dict(ecfg['truth'])
            truth['sig_m'] = level
            # calibrate log_scale so that synthetic growth is realistic
            from .model import calibrate_scale
            names = sorted(ctx.S.keys(), key=lambda s: int(s[3:]))
            cfgm = dict(ctx.cfg['model'])
            truth['log_scale'] = calibrate_scale(cfgm, [ctx.S[n] for n in names], ctx.r0, ctx.known, ctx.t_off, 1.5) + truth.get('log_scale_shift', 0.0)
            synth, gt = simulate_synthetic(ctx, truth, seed)
            saved = ctx.S
            ctx.S = synth
            try:
                model = fit_mssa(ctx, names, seed, 'no_disc', n_val=0)
            finally:
                ctx.S = saved
            sm = model.summary()
            base = np.where(ctx.known, ctx.r0, np.nanmean(ctx.r0))
            u_hat = np.log(np.asarray(sm['R0_eff']) / base)
            present = np.array([any(sl.slot_idx == k for s in synth.values() for sl in s.sublayers) for k in range(len(AC_SLOTS))])
            batch = pad_batch([synth[n] for n in names])
            res = model.forecast_all(batch, None, 1, ctx.device)
            ok = batch['tmask'] > 0
            row = dict(exp='E0', seed=seed, sig_m_true=level, beta_true=truth['beta'], beta_hat=sm['beta'],
                       gamma_true=truth['gamma'], gamma_hat=sm['gamma'], phi_true=truth['phi'], phi_hat=sm['phi'],
                       sig_m_hat=sm['sig_m'], sig_r_true=truth['sig_r'], sig_r_hat=sm['sig_r'],
                       u_spearman=float(spearmanr(gt['u'][present], u_hat[present]).correlation),
                       u_rmse=float(np.sqrt(np.mean((gt['u'][present] - u_hat[present]) ** 2))),
                       Rperm_rmse=float(np.sqrt(np.mean(((res['Rperm'] + res['d0']) - gt['Rperm'])[ok] ** 2))),
                       rev_rmse=float(np.sqrt(np.mean((res['r'] - gt['rev'])[ok] ** 2))),
                       rev_sd_true=float(np.std(gt['rev'][ok])))
            ctx.log(f'[E0] {row}')
            ctx.add('E0_identifiability', [row])


def exp_E5(ctx):
    """Parameters vs independent evidence: Wu et al. (2022) ranges, hidden-material recovery, discrepancy map."""
    names = sorted(ctx.S.keys(), key=lambda s: int(s[3:]))
    wu = pd.read_csv(os.path.join(ctx.data_dir, 'wu2022_jtg_correction.csv'))
    ecfg = ctx.cfg['experiments']['E5']
    for seed in ctx.cfg['seeds']:
        model = fit_mssa(ctx, names, seed, 'full', n_val=ecfg.get('n_inner_val', 2))
        sm = model.summary()
        ctx.add('E5_params', [dict(exp='E5', seed=seed, beta_hat=sm['beta'], gamma_hat=sm['gamma'],
                                   wu_load_exp_min=wu['effective_load_exponent(0.48*beta3)'].min(),
                                   wu_load_exp_max=wu['effective_load_exponent(0.48*beta3)'].max(),
                                   wu_temp_exp_min=wu['effective_temp_exponent(2.93*beta2)'].min(),
                                   wu_temp_exp_max=wu['effective_temp_exponent(2.93*beta2)'].max(),
                                   **{f'R0eff_{s}': v for s, v in zip(AC_SLOTS, sm['R0_eff'])},
                                   **{f'scale_{c}': v for c, v in zip(CLASSES, sm['scale_cls'])})])
        # discrepancy map
        batch = pad_batch([ctx.S[n] for n in names])
        res = model.forecast_all(batch, None, 1, ctx.device)
        if 'g' in res:
            g = res['g']
            rows = []
            for i, n in enumerate(names):
                T = int(batch['tmask'][i].sum())
                K = int(batch['lmask'][i].sum())
                gi = g[i, :T, :K]
                rows.append(dict(exp='E5', seed=seed, structure=n, cls=ctx.S[n].cls, mean_g=float(gi.mean()),
                                 mean_abs_g=float(np.abs(gi).mean()),
                                 **{f'g_layer{k}_{AC_SLOTS[batch["slot"][i, k]]}': float(gi[:, k].mean()) for k in range(K)}))
            ctx.add('E5_discrepancy', rows)
            df = pd.DataFrame(rows)
            grp = df.cls.isin(['II_RigidComposite_12cmAC', 'VII_FullDepth_48_52cm'])
            if grp.sum() > 0 and (~grp).sum() > 0:
                u = mannwhitneyu(df.mean_abs_g[grp], df.mean_abs_g[~grp], alternative='greater')
                ctx.add('E5_H1_test', [dict(seed=seed, mean_abs_g_II_VII=float(df.mean_abs_g[grp].mean()),
                                            mean_abs_g_others=float(df.mean_abs_g[~grp].mean()), U=float(u.statistic),
                                            p_one_sided=float(u.pvalue))])
        # hidden-material recovery
        if ecfg.get('hide_materials', True):
            lab = {s: v for s, v, k in zip(AC_SLOTS, ctx.r0, ctx.known) if k}
            rec = []
            for s in lab:
                mh = fit_mssa(ctx, names, seed, 'full', extra={'hide_R0': [s]}, n_val=ecfg.get('n_inner_val', 2))
                v = mh.summary()['R0_eff'][AC_SLOTS.index(s)]
                rec.append(dict(exp='E5', seed=seed, slot=s, R0_lab=lab[s], R0_recovered_when_hidden=v))
                ctx.add('E5_hidden_material', [rec[-1]])
            d = pd.DataFrame(rec)
            ctx.add('E5_hidden_material_summary', [dict(seed=seed, spearman=float(spearmanr(d.R0_lab, d.R0_recovered_when_hidden).correlation),
                                                        n=len(d))])


def exp_ablation(ctx):
    cfg = ctx.cfg
    variants = cfg['experiments']['E6_ablation']['variants']
    ecfg = cfg['experiments']['protocols']
    for fi, (train, test) in enumerate(folds('manuscript', ctx.S)):
        batch = test_batch(ctx, test)
        for seed in cfg['seeds']:
            for v in variants:
                meta = dict(exp='E6_ablation', folds='manuscript', fold=fi, seed=seed, model=f'mssa:{v}')
                ctx.log(f'[E6] fold {fi} seed {seed} variant {v}')
                try:
                    model = fit_mssa(ctx, train, seed, v)
                    evaluate_all_protocols(ctx, MSSAPredictor(model, ctx.device), batch, meta, ecfg, 'E6_ablation')
                except Exception as e:
                    import traceback
                    ctx.log(f'  !! {v} failed: {e}\n{traceback.format_exc()}')
                    ctx.add('failures', [dict(meta, error=str(e))])


# ============================================================================ hybrid MSSA-H
class HybridMSSA:
    """MSSA + gradient-boosting residual corrector (MSSA-H).

    The corrector uses the same pair features as `gbm_residual` plus MSSA states/forecasts at the origin
    (forecast mean and sd, permanent part, reversible part, log-rate theta, datum). Its training residuals are
    obtained by cross-fitting: MSSA models trained on k-1 groups of the training structures forecast the held-out
    group, so the corrector never sees in-sample MSSA forecasts. Test structures are never used.
    """
    name = 'mssa_h'
    GAP_BINS = [1, 2, 4, 7, 13, 31, 10 ** 6]

    def __init__(self, ctx):
        self.ctx = ctx
        self.hcfg = ctx.cfg['experiments'].get('hybrid', {})

    # ---------------------------------------------------------------- features
    def _rows(self, batch, res, obs, pairs):
        li = bl.last_obs_index(obs)
        X, base, var, gap = [], [], [], []
        for b, t, tau in pairs:
            j = tau - t - 1
            l = li[b, t] if t >= 0 else -1
            f = bl._pair_features(batch, b, l, tau)
            mu = res['mu'][b, t, j]
            sd = float(np.sqrt(max(res['var'][b, t, j], 1e-8)))
            ylast = batch['y'][b, l] if l >= 0 else np.nan
            X.append(np.concatenate([f, [mu, sd, res['Rperm'][b, t], res['r'][b, t], res['theta'][b, t], res['d0'][b, t],
                                         tau - t, mu - ylast if l >= 0 else np.nan]]))
            base.append(mu)
            var.append(sd ** 2)
            gap.append(tau - t)
        return np.asarray(X), np.asarray(base), np.asarray(var), np.asarray(gap)

    def _sample_pairs(self, batch, obs, rng, n_per):
        lens = batch['tmask'].sum(1).astype(int)
        out = []
        for b, n in enumerate(lens):
            ts = rng.integers(0, n - 1, size=n_per)
            gaps = np.floor(np.exp(rng.uniform(0.0, np.log(n), size=n_per))).astype(int).clip(1, n - 1)
            for t, g in zip(ts, gaps):
                tau = min(n - 1, t + g)
                if tau > t:
                    out.append((b, int(t), int(tau)))
        return out

    def _schemes(self, batch, rng):
        T = batch['y'].shape[1]
        sch = [None]
        for k in self.hcfg.get('train_k', [2, 4, 8]):
            off = rng.integers(0, k)
            sch.append(((np.arange(T)[None, :] % k) == off).astype(float) * np.ones_like(batch['y']))
        for f in self.hcfg.get('train_early', [0.2, 0.4, 0.6]):
            sch.append(early_mask(batch, f)[0])
        return sch

    # pair-feature layout (baselines._pair_features): 3 = load since last obs, 4 = log cumulative load at target,
    # 5 = mean air temperature over the gap, 6 = air temperature at target -> corrector constrained non-decreasing
    MONO_IDX = (3, 4, 5, 6)
    N_FEAT = 10 + 18 + 8

    def _mono(self):
        c = [0] * self.N_FEAT
        if self.hcfg.get('monotone', True):
            for i in self.MONO_IDX:
                c[i] = 1
        return c

    def _gbm(self, seed):
        if bl.xgb is not None:
            return bl.xgb.XGBRegressor(n_estimators=self.hcfg.get('trees', 500), max_depth=self.hcfg.get('max_depth', 4),
                                       learning_rate=0.03, subsample=0.9, colsample_bytree=0.9, reg_lambda=3.0,
                                       min_child_weight=5, tree_method='hist', random_state=seed,
                                       monotone_constraints='(' + ','.join(map(str, self._mono())) + ')')
        from sklearn.ensemble import HistGradientBoostingRegressor
        return HistGradientBoostingRegressor(max_iter=self.hcfg.get('trees', 500), max_depth=self.hcfg.get('max_depth', 4),
                                             learning_rate=0.03, l2_regularization=3.0, random_state=seed,
                                             monotonic_cst=self._mono())

    # ---------------------------------------------------------------- fit
    def fit(self, train_names, seed, main_model=None):
        ctx = self.ctx
        rng = np.random.default_rng(seed + 7)
        self.main = main_model if main_model is not None else fit_mssa(ctx, train_names, seed, 'full')
        n_cf = self.hcfg.get('n_crossfit', 3)
        names = list(train_names)
        rng.shuffle(names)
        groups = [names[i::n_cf] for i in range(n_cf)]
        Xs, Ys, Vs, Gs, Gid = [], [], [], [], []
        for gi, grp in enumerate(groups):
            rest = [n for n in names if n not in grp]
            ctx.log(f'    MSSA-H cross-fit {gi + 1}/{n_cf}: hold out {grp}')
            m = fit_mssa(ctx, rest, seed + 100 + gi, 'full', extra={'epochs': self.hcfg.get('crossfit_epochs',
                                                                                             ctx.cfg['train']['epochs'])})
            batch = test_batch(ctx, grp)
            T = batch['y'].shape[1]
            for om in self._schemes(batch, rng):
                obs = batch['tmask'] if om is None else batch['tmask'] * om
                res = m.forecast_all(batch, om, T - 1, ctx.device)
                pairs = self._sample_pairs(batch, obs, rng, self.hcfg.get('pairs_per_structure', 400))
                X, base, var, gap = self._rows(batch, res, obs, pairs)
                y = np.array([batch['y'][b, tau] for b, _, tau in pairs])
                Xs.append(X); Ys.append(y - base); Vs.append(var); Gs.append(gap); Gid.append(np.full(len(y), gi))
        X, Y, V, G, gid = map(np.concatenate, (Xs, Ys, Vs, Gs, Gid))
        self._data = (X, Y, V, G, gid, seed, n_cf)
        self._views = {}
        return self

    def view(self, monotone=True):
        """Predictor with a corrector fitted on the shared cross-fitted rows (monotone or unconstrained)."""
        if monotone in self._views:
            return self._views[monotone]
        import copy as _copy
        v = _copy.copy(self)
        v.hcfg = dict(self.hcfg, monotone=monotone)
        v.name = 'mssa_h' if monotone else 'mssa_h:free'
        v._finish()
        self._views[monotone] = v
        return v

    def _finish(self):
        ctx = self.ctx
        X, Y, V, G, gid, seed, n_cf = self._data
        self.reg = self._gbm(seed).fit(X, Y)
        # variance calibration from group-wise out-of-sample corrector residuals
        oos = np.zeros_like(Y)
        for gi in range(n_cf):
            tr, te = gid != gi, gid == gi
            oos[te] = self._gbm(seed).fit(X[tr], Y[tr]).predict(X[te])
        r2 = (Y - oos) ** 2
        self.var_ratio = []
        for lo, hi in zip(self.GAP_BINS[:-1], self.GAP_BINS[1:]):
            sel = (G >= lo) & (G < hi)
            self.var_ratio.append(float(r2[sel].mean() / V[sel].mean()) if sel.sum() > 20 else 1.0)
        ctx.log(f'    {self.name} corrector rows {len(Y)}; var ratios {np.round(self.var_ratio, 2).tolist()}')

    def _ratio(self, gap):
        idx = np.clip(np.searchsorted(self.GAP_BINS, gap, side='right') - 1, 0, len(self.var_ratio) - 1)
        return np.asarray(self.var_ratio)[idx]

    # ---------------------------------------------------------------- predict
    def forecast_all(self, batch, obs_mask, h):
        ctx = self.ctx
        T = batch['y'].shape[1]
        res = self.main.forecast_all(batch, obs_mask, T - 1, ctx.device)
        obs = batch['tmask'] if obs_mask is None else batch['tmask'] * obs_mask
        lens = batch['tmask'].sum(1).astype(int)
        Bsz = len(lens)
        pairs, where = [], []
        for b in range(Bsz):
            for t in range(lens[b]):
                for j in range(h):
                    if t + j + 1 < lens[b]:
                        pairs.append((b, t, t + j + 1))
                        where.append(('mu', b, t, j))
                if t >= 1:
                    pairs.append((b, t - 1, t))
                    where.append(('pred', b, t, 0))
        X, base, var, gap = self._rows(batch, res, obs, pairs)
        corr = self.reg.predict(X)
        val = base + corr
        v = var * self._ratio(gap)
        mu = np.full((Bsz, T, h), np.nan)
        mv = np.full((Bsz, T, h), np.nan)
        pm = res['pred_mu'].copy()
        pv = res['pred_var'].copy()
        for (kind, b, t, j), a, s2 in zip(where, val, v):
            if kind == 'mu':
                mu[b, t, j], mv[b, t, j] = a, s2
            else:
                pm[b, t], pv[b, t] = a, s2
        return {'mu': mu, 'var': mv, 'pred_mu': pm, 'pred_var': pv}
