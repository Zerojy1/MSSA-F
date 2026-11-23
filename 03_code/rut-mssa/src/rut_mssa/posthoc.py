"""Post-hoc seed ensembles and physics-data fusion, computed from saved predictions of all seeds.

  mssa_ens  : 5-seed ensemble of MSSA (mixture moments; deep-ensemble style, Lakshminarayanan et al. 2017)
  gbm_ens   : the same seed ensemble for the strongest baseline (fair comparison of the ensembling effect)
  fusion    : equal-weight combination of mssa_ens and gbm_ens (Bates & Granger 1969). Equal weights are used
              on purpose: no weight is estimated, so no data (and no test structure) is used to build it, and
              simple averages are known to be hard to beat by estimated weights (forecast-combination puzzle).
Evaluated with exactly the same protocol code as the individual models.
"""
from __future__ import annotations

import glob
import os
import re

import numpy as np
import pandas as pd

from . import experiments as ex
from .data import load_structures, pad_batch


def _pairs(arr):
    out = {}
    for k in arr.files:
        if k.endswith('_mu') or k == 'hmu':
            base = 'h' if k == 'hmu' else k[:-3]
            vk = 'hvar' if k == 'hmu' else base + '_var'
            if vk in arr.files:
                out[base] = (arr[k], arr[vk])
    return out


def combine(list_of_pairs):
    keys = set.intersection(*[set(p) for p in list_of_pairs])
    out = {}
    for k in keys:
        M = np.stack([p[k][0] for p in list_of_pairs])
        V = np.stack([p[k][1] for p in list_of_pairs])
        out[k] = (M.mean(0), V.mean(0) + M.var(0))
    return out


def fuse(a, b, w=0.5):
    out = {}
    for k in set(a) & set(b):
        (ma, va), (mb, vb) = a[k], b[k]
        mu = w * ma + (1 - w) * mb
        out[k] = (mu, w * va + (1 - w) * vb + w * (1 - w) * (ma - mb) ** 2)
    return out


def rows_from(batch, A, meta, ecfg):
    rows = []
    y, tm = batch['y'], batch['tmask']
    Bsz, T = y.shape
    mu, var = A['h']
    for h in ecfg['horizons']:
        tgt = np.full((Bsz, T), np.nan)
        tgt[:, :T - h] = y[:, h:]
        ok = np.zeros((Bsz, T), bool)
        ok[:, :T - h] = tm[:, h:] > 0
        rows += ex._per_structure(dict(meta, protocol='horizon', setting=h), batch['names'], tgt, mu[:, :, h - 1],
                                  var[:, :, h - 1], ok)
    for k in ecfg['sparse_k']:
        if f's{k}' not in A:
            continue
        pm, pv = A[f's{k}']
        om = (np.arange(T)[None, :] % k == 0).astype(float) * np.ones_like(y)
        ok = tm > 0
        ok[:, 0] = False
        rows += ex._per_structure(dict(meta, protocol='sparse_all', setting=k), batch['names'], y, pm, pv, ok)
        if k > 1:
            rows += ex._per_structure(dict(meta, protocol='sparse_unobserved', setting=k), batch['names'], y, pm, pv,
                                      ok & (om == 0))
    for f in ecfg['early_fracs']:
        if f'e{f}' in A:
            pm, pv = A[f'e{f}']
            rows += ex.early_rows(batch, f, {'pred_mu': pm, 'pred_var': pv}, meta, ecfg['thresholds'])
    if 'cold' in A:
        rows += ex.cold_rows(batch, A['cold'][0], A['cold'][1], meta)
    return rows


def run_posthoc(out_dir, cfg, log=print):
    S = load_structures(cfg['data_dir'], cfg['model'])
    ecfg = cfg['experiments']['protocols']
    files = glob.glob(os.path.join(out_dir, 'pred', 'ALL_*.npz'))
    pat = re.compile(r'ALL_(?P<tag>[^_]+(?:_ablation)?)_f(?P<fold>\d+)_s(?P<seed>-?\d+)_(?P<model>.+)\.npz$')
    idx = {}
    for f in files:
        m = pat.search(os.path.basename(f))
        if m:
            idx.setdefault((m['tag'], int(m['fold'])), {}).setdefault(m['model'], []).append(f)
    new_main, new_aci = {}, {}
    for (tag, fold), models in sorted(idx.items()):
        any_f = next(iter(models.values()))[0]
        names = [str(n) for n in np.load(any_f)['names']]
        batch = pad_batch([S[n] for n in names])
        ens = {}
        for model, label in (('mssa', 'mssa_ens'), ('gbm_residual', 'gbm_ens')):
            if models.get(model):
                ens[label] = combine([_pairs(np.load(f)) for f in sorted(models[model])])
                ens[label + '_nseeds'] = len(models[model])
        if 'mssa_ens' in ens and 'gbm_ens' in ens:
            ens['fusion'] = fuse(ens['mssa_ens'], ens['gbm_ens'])
        for label in ('mssa_ens', 'gbm_ens', 'fusion'):
            if label not in ens:
                continue
            meta = dict(exp=tag, folds='posthoc', fold=fold, seed=-1, model=label)
            new_main.setdefault(tag, []).extend(rows_from(batch, ens[label], meta, ecfg))
            if 's1' in ens[label]:
                pm, pv = ens[label]['s1']
                new_aci.setdefault(tag, []).extend(ex.protocol_aci({'pred_mu': pm, 'pred_var': pv}, batch, meta))
        log(f'posthoc {tag} fold {fold}: ' + ', '.join(f'{k}={v}' for k, v in ens.items() if k.endswith('_nseeds')))
    for tag, rows in new_main.items():
        _append(os.path.join(out_dir, f'main_{tag}.csv'), rows)
    for tag, rows in new_aci.items():
        _append(os.path.join(out_dir, f'uq_aci_{tag}.csv'), rows)


def _append(path, rows):
    new = pd.DataFrame(rows)
    if os.path.exists(path):
        old = pd.read_csv(path)
        old = old[~old.model.isin(new.model.unique())]
        new = pd.concat([old, new], ignore_index=True)
    new.to_csv(path, index=False)
