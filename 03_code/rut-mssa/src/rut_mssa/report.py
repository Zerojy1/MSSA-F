"""Aggregate result tables into REPORT.md, summary CSVs and figures."""
from __future__ import annotations

import glob
import os

import numpy as np
import pandas as pd


def _md(df):
    try:
        return df.to_markdown(index=False)
    except Exception:
        return "```\n" + df.to_string(index=False) + "\n```"


def _pool(g):
    n = g['n'].clip(lower=0)
    w = n / n.sum() if n.sum() > 0 else n
    out = {'n': int(n.sum()), 'RMSE': float(np.sqrt((w * g['RMSE'] ** 2).sum())), 'MAE': float((w * g['MAE']).sum())}
    for c in ['PICP', 'MPIW', 'IS', 'CRPS', 'NLL', 'end_abs_err', 'mono_viol_frac', 'perm_mono_viol_frac']:
        if c in g and g[c].notna().any():
            gg = g[g[c].notna()]
            ww = gg['n'] / gg['n'].sum() if c not in ('end_abs_err', 'mono_viol_frac', 'perm_mono_viol_frac') else None
            out[c] = float((ww * gg[c]).sum()) if ww is not None else float(gg[c].mean())
    for c in [c for c in g.columns if c.startswith('fpt_abs_err')]:
        if g[c].notna().any():
            out[c.replace('fpt_abs_err_Mload_', 'FPTerr_')] = float(g[c].mean())
    return pd.Series(out)


def summarize_main(df):
    df = df[df['n'] > 0]
    keys = ['model', 'protocol', 'setting', 'seed']
    by_seed = pd.DataFrame([dict(zip(keys, k), **_pool(g).to_dict()) for k, g in df.groupby(keys)])
    val_cols = [c for c in by_seed.columns if c not in ('model', 'protocol', 'setting', 'seed')]
    by_seed[val_cols] = by_seed[val_cols].apply(pd.to_numeric, errors='coerce')
    agg = by_seed.groupby(['model', 'protocol', 'setting'])[val_cols].agg(['mean', 'std'])
    agg.columns = [f'{a}_{b}' for a, b in agg.columns]
    return by_seed, agg.reset_index()


def paired_vs_reference(df, ref='mssa', n_boot=10000, seed=0):
    """Structure-level paired comparison: RMSE averaged over seeds per structure, bootstrap over structures."""
    rng = np.random.default_rng(seed)
    rows = []
    d = df[df['n'] > 0]
    piv = d.groupby(['protocol', 'setting', 'structure', 'model'])['RMSE'].mean().unstack('model')
    if ref not in piv.columns:
        return pd.DataFrame()
    for m in piv.columns:
        if m == ref:
            continue
        for (prot, sett), g in piv.groupby(level=[0, 1]):
            ds = (g[m] - g[ref]).dropna().to_numpy()
            if ds.size == 0:
                continue
            bs = rng.choice(ds, size=(n_boot, len(ds)), replace=True).mean(1)
            rows.append(dict(protocol=prot, setting=sett, model=m, reference=ref, mean_RMSE_diff=float(ds.mean()),
                             ci_low=float(np.percentile(bs, 2.5)), ci_high=float(np.percentile(bs, 97.5)),
                             structures_ref_better=int((ds > 0).sum()), n_structures=len(ds)))
    return pd.DataFrame(rows)


def _fig(agg, protocol, out_png, xlabel):
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
    except ImportError:
        return
    a = agg[agg.protocol == protocol]
    if a.empty:
        return
    fig, ax = plt.subplots(figsize=(6, 4))
    for m, g in a.groupby('model'):
        g = g.sort_values('setting')
        x = g['setting'].astype(float)
        ax.errorbar(x, g['RMSE_mean'], yerr=g['RMSE_std'].fillna(0), marker='o', capsize=3, label=m)
    ax.set_xlabel(xlabel)
    ax.set_ylabel('RMSE (mm)')
    ax.set_title(protocol)
    ax.grid(alpha=0.3)
    ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(out_png, dpi=200)
    plt.close(fig)


def _read(f):
    try:
        d = pd.read_csv(f)
        return None if d.empty else d
    except pd.errors.EmptyDataError:
        return None


def make_report(out_dir):
    lines = ['# MSSA-Rut experiment report', '', f'Run directory: `{out_dir}`', '']
    fig_dir = os.path.join(out_dir, 'figures')
    os.makedirs(fig_dir, exist_ok=True)
    for f in sorted(glob.glob(os.path.join(out_dir, 'main_*.csv'))):
        tag = os.path.basename(f)[5:-4]
        df = _read(f)
        if df is None:
            continue
        by_seed, agg = summarize_main(df)
        agg.to_csv(os.path.join(out_dir, f'summary_{tag}.csv'), index=False)
        by_seed.to_csv(os.path.join(out_dir, f'summary_by_seed_{tag}.csv'), index=False)
        refs = [r for r in ('fusion', 'mssa_ens', 'mssa') if r in df.model.unique()]
        lines += [f'## {tag}', '']
        for prot in agg.protocol.unique():
            a = agg[agg.protocol == prot]
            cols = ['model', 'setting', 'RMSE_mean', 'RMSE_std', 'MAE_mean'] + \
                   [c for c in ['PICP_mean', 'MPIW_mean', 'CRPS_mean', 'end_abs_err_mean', 'mono_viol_frac_mean',
                                'perm_mono_viol_frac_mean', 'FPTerr_8.0_mean', 'FPTerr_10.0_mean'] if c in a]
            lines += [f'### {prot}', '', _md(a[cols].round(4)), '']
            _fig(agg, prot, os.path.join(fig_dir, f'{tag}_{prot}.png'),
                 {'horizon': 'horizon (observations ahead)', 'sparse_all': 'assimilate every k-th measurement',
                  'sparse_unobserved': 'k', 'early_life': 'fraction of record observed', 'cold_start': '-'}.get(prot, 'setting'))
        for ref in refs:
            pv = paired_vs_reference(df, ref)
            if not pv.empty:
                pv.to_csv(os.path.join(out_dir, f'paired_vs_{ref}_{tag}.csv'), index=False)
                lines += [f'### Paired structure-level RMSE difference (model - {ref}), bootstrap 95% CI', '',
                          _md(pv.round(4)), '']
    for name, title in [('counterfactual', 'Counterfactual physical consistency (E4)'), ('uq_aci', 'Native vs ACI intervals'),
                        ('fpt_mc', 'First-passage Monte Carlo')]:
        for f in sorted(glob.glob(os.path.join(out_dir, f'{name}_*.csv'))):
            df = _read(f)
            if df is None:
                continue
            tag = os.path.basename(f)[len(name) + 1:-4]
            if name == 'counterfactual':
                cc = [c for c in ['frac_increase', 'frac_decrease', 'mean_delta', 'frac_increase_at_end'] if c in df]
                s = df.groupby(['model', 'setting'])[cc].mean().reset_index()
            elif name == 'uq_aci':
                s = df.groupby(['model', 'setting'])[['PICP', 'MPIW', 'IS']].mean().reset_index()
            else:
                cols = [c for c in ['p_cross_by_end', 'obs_in_90pct', 'median_abs_err_Mload'] if c in df]
                s = df.groupby(['frac', 'threshold'])[cols].mean(numeric_only=True).reset_index() if cols else df.head()
            s.to_csv(os.path.join(out_dir, f'summary_{name}_{tag}.csv'), index=False)
            lines += [f'## {title} [{tag}]', '', _md(s.round(4)), '']
    for f, title in [('E0_identifiability.csv', 'E0 synthetic identifiability'), ('E5_params.csv', 'E5 learned parameters'),
                     ('E5_hidden_material_summary.csv', 'E5 hidden-material recovery'), ('E5_H1_test.csv', 'E5 H1 discrepancy test'),
                     ('failures.csv', 'Failures')]:
        p = os.path.join(out_dir, f)
        if os.path.exists(p) and _read(p) is not None:
            df = _read(p)
            lines += [f'## {title}', '', _md(df.round(4)), '']
    with open(os.path.join(out_dir, 'REPORT.md'), 'w') as fh:
        fh.write('\n'.join(lines))


def merge_runs(dirs, out):
    """Concatenate result tables of several run directories (e.g. parallel jobs) into `out`."""
    import shutil
    os.makedirs(os.path.join(out, 'pred'), exist_ok=True)
    tables = {}
    for d in dirs:
        for f in glob.glob(os.path.join(d, '*.csv')):
            b = os.path.basename(f)
            if b.startswith(('summary_', 'paired_')):
                continue
            df = _read(f)
            if df is not None:
                tables.setdefault(b, []).append(df)
        for f in glob.glob(os.path.join(d, 'pred', '*.npz')):
            shutil.copy(f, os.path.join(out, 'pred'))
        lg = os.path.join(d, 'log.txt')
        if os.path.exists(lg):
            with open(os.path.join(out, 'log_merged.txt'), 'a') as fo, open(lg) as fi:
                fo.write(f'===== {d} =====\n' + fi.read())
    for b, dfs in tables.items():
        pd.concat(dfs, ignore_index=True).drop_duplicates().to_csv(os.path.join(out, b), index=False)
