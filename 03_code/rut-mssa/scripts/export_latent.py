#!/usr/bin/env python
"""Export filtered latent states for the manuscript figures (Fig. 3b, Fig. 8).

Trains the full MSSA model with the same settings as the main run and saves, for every held-out
structure, the filtered permanent rut per sublayer, the datum d0, the recoverable component r and
the rate state theta. Also repeats one synthetic identifiability case (E0) and saves the true and
recovered latent paths.

  python scripts/export_latent.py --device cuda --seed 0 --out results/latent
Output: latent_E1E2.npz, latent_E3.npz, latent_E0.npz  (about 10-30 min on an RTX 2080)
"""
import argparse
import os
import sys

import numpy as np
import yaml

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(HERE, 'src'))
sys.path.insert(0, HERE)

from run_all import load_cfg  # noqa: E402
from rut_mssa import experiments as ex  # noqa: E402
from rut_mssa.data import folds, pad_batch  # noqa: E402


def states(model, batch, device):
    import torch
    with torch.no_grad():
        B, p, inputs, g, io, out = model.filter(batch, None, device)
        K = inputs['C'].shape[-1]
        lm = inputs['lmask'].cpu().numpy()
        m = out['m'].cpu().numpy()
        P = out['P'].cpu().numpy()
    res = model.forecast_all(batch, None, 1, device)
    return dict(R_layer=m[:, :, :K] * lm[:, None, :], R_layer_sd=np.sqrt(np.maximum(np.diagonal(P[:, :, :K, :K], axis1=2, axis2=3), 0)) * lm[:, None, :],
                d0=m[:, :, K], r=m[:, :, K + 1], r_sd=np.sqrt(np.maximum(P[:, :, K + 1, K + 1], 0)),
                theta=res['theta'], Rperm=res['Rperm'], P_perm=res['P_perm'], pred_mu=res['pred_mu'],
                pred_var=res['pred_var'], lmask=lm)


def run_folds(ctx, kind, seed, out_path):
    store = {}
    for fi, (train, test) in enumerate(folds(kind, ctx.S)):
        if not test:
            continue
        model = ex.fit_mssa(ctx, train, seed, 'full')
        batch = pad_batch([ctx.S[n] for n in test])
        st = states(model, batch, ctx.device)
        for b, n in enumerate(test):
            s = ctx.S[n]
            T = len(s.y)
            store[n] = dict(fold=fi, y=batch['y'][b, :T], N=batch['N'][b, :T],
                            slot=np.array([sl.slot_idx for sl in s.sublayers]), zmid=np.array([sl.z_mid_mm for sl in s.sublayers]),
                            h=np.array([sl.h_mm for sl in s.sublayers]), cls=s.cls, T_air=s.T_air,
                            **{k: (v[b, :T] if v.ndim >= 2 and k != 'lmask' else v[b]) for k, v in st.items()})
        ctx.log(f'[{kind}] fold {fi} exported {test}')
    flat = {}
    for n, d in store.items():
        for k, v in d.items():
            flat[f'{n}__{k}'] = np.asarray(v)
    np.savez_compressed(out_path, **flat)


def run_e0(ctx, seed, out_path):
    from rut_mssa.model import calibrate_scale
    ecfg = ctx.cfg['experiments']['E0']
    truth = dict(ecfg['truth'])
    truth['sig_m'] = ecfg['noise_levels'][0]
    names = sorted(ctx.S.keys(), key=lambda s: int(s[3:]))
    cfgm = dict(ctx.cfg['model'])
    truth['log_scale'] = calibrate_scale(cfgm, [ctx.S[n] for n in names], ctx.r0, ctx.known, ctx.t_off, 1.5) + truth.get('log_scale_shift', 0.0)
    synth, gt = ex.simulate_synthetic(ctx, truth, seed)
    saved = ctx.S
    ctx.S = synth
    try:
        model = ex.fit_mssa(ctx, names, seed, 'no_disc', n_val=0)
    finally:
        ctx.S = saved
    batch = pad_batch([synth[n] for n in names])
    res = model.forecast_all(batch, None, 1, ctx.device)
    np.savez_compressed(out_path, names=np.array(names), y=batch['y'], tmask=batch['tmask'],
                        Rperm_true=gt['Rperm'], rev_true=gt['rev'], Rperm_hat=res['Rperm'] + res['d0'],
                        rev_hat=res['r'], P_perm=res['P_perm'])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--config', default=os.path.join(HERE, 'configs', 'full.yaml'))
    ap.add_argument('--device', default='cpu')
    ap.add_argument('--seed', type=int, default=0)
    ap.add_argument('--out', default=os.path.join(HERE, 'results', 'latent'))
    args = ap.parse_args()
    cfg = load_cfg(args.config)
    cfg['device'] = args.device
    cfg['data_dir'] = os.path.join(HERE, cfg['data_dir']) if not os.path.isabs(cfg['data_dir']) else cfg['data_dir']
    os.makedirs(args.out, exist_ok=True)
    ctx = ex.Ctx(cfg, args.out, print)
    run_e0(ctx, args.seed, os.path.join(args.out, 'latent_E0.npz'))
    run_folds(ctx, 'manuscript', args.seed, os.path.join(args.out, 'latent_E1E2.npz'))
    run_folds(ctx, 'leave_class_out', args.seed, os.path.join(args.out, 'latent_E3.npz'))
    print('done ->', args.out)


if __name__ == '__main__':
    main()
