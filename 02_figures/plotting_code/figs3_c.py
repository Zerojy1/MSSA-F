import numpy as np, pandas as pd, json
from scipy.stats import norm, gaussian_kde
from matplotlib.gridspec import GridSpec
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from matplotlib.colors import TwoSlopeNorm
from styleA import *
from common import *
NUM = {}
LS = {'E1E2': '-', 'E3': (0, (3, 1.5))}


# ============================================================== Fig 9  ensemble spaghetti (NeuralGCM Fig 4a style)
import glob, re
h = 6
picks = {}
for n, d in sorted(E['E3'].items(), key=lambda x: int(x[0][3:])):
    picks.setdefault(d['cls'], n)
mem = {}
for f in glob.glob(R + 'pred/ALL_E3_f*_s*_*.npz'):
    mm = re.search(r'_f(\d+)_s(\d+)_(mssa|gbm_residual)\.npz', f)
    z = np.load(f, allow_pickle=True)
    for b, n in enumerate([str(x) for x in z['names']]):
        mem.setdefault(n, []).append((mm.group(3), z['hmu'][b, :, h - 1]))
fig, axs = plt.subplots(2, 4, figsize=(W2, 86 * MM), layout='constrained', sharey=True, sharex=True)
for i, c_ in enumerate(CLS_SHORT):
    ax = axs.flat[i]; n = picks[c_]; d = E['E3'][n]
    y = d['y']; T = len(y); N = d['N'] / 1e6; x = N[h:]
    for kind, mu_s in mem[n]:
        ax.plot(x, mu_s[:T - h], color='#9ec5f4' if kind == 'mssa' else '#a8dcc8', lw=0.35, zorder=1)
    mu = d['F_h'][0][:T - h, h - 1]
    ax.plot(x, mu, color=M['F'][0], lw=1.0, zorder=3)
    ax.plot(N, y, 'o', ms=1.4, color=REF, mew=0, zorder=4)
    rm = np.sqrt(np.mean((y[h:] - mu) ** 2))
    ax.text(0.97, 0.05, f'RMSE = {rm:.2f} mm', transform=ax.transAxes, ha='right', fontsize=6.2)
    title(ax, f'{n}, class {CLS_SHORT[c_]}'); ax.set_ylim(0, 12.5); ax.set_xlim(-1, 62)
    if i % 4 == 0: ax.set_ylabel('Rut depth (mm)')
    if i >= 3: ax.set_xlabel('Cumulative ESAL (million)')
    label(ax, 'abcdefg'[i], x=-0.06 if i % 4 else -0.16)
axs.flat[3].tick_params(labelbottom=True)
ax = axs.flat[7]; ax.axis('off')
hd = [Line2D([], [], marker='o', ls='', ms=2.5, color=REF), Line2D([], [], color=M['F'][0], lw=1.0),
      Line2D([], [], color='#9ec5f4', lw=0.8), Line2D([], [], color='#a8dcc8', lw=0.8)]
ax.legend(hd, ['Survey', 'MSSA-F (6 surveys ahead)', 'MSSA members (5 seeds)', 'GBM members (5 seeds)'], loc='center left', fontsize=6.5)
ax.text(0.02, 0.12, 'Each class held out in turn', transform=ax.transAxes, fontsize=6.3, color=INK2)
save(fig, 'Fig9_unseen_trajectories')

# ============================================================== Fig 10  end-of-record parity (Severson Fig 3 style) + decision
fig = plt.figure(figsize=(W2, 112 * MM), layout='constrained')
gs = GridSpec(2, 3, figure=fig)
NUM['parity'] = {}
for j, f in enumerate([0.2, 0.4, 0.6]):
    ax = fig.add_subplot(gs[0, j]); boxed(ax)
    errs_u = []
    for e, mk, col, lab in [('E1E2', 'o', SEEN, 'Seen classes'), ('E3', 's', UNSEEN, 'Unseen classes')]:
        o, p = [], []
        for n, d in E[e].items():
            o.append(d['y'][-1]); p.append(d[f'F_e{f}'][0][-1])
        o, p = np.array(o), np.array(p)
        ax.scatter(o, p, s=13, marker=mk, color=col, edgecolor='white', lw=0.4, zorder=3, label=lab)
        rm = np.sqrt(np.mean((p - o) ** 2)); NUM['parity'][f'{e}_{f}'] = round(rm, 2)
        if e == 'E3': errs_u = p - o
        ax.text(4.4, 12.0 - (0.62 if e == 'E1E2' else 1.24), f'{lab.split()[0]}  {rm:.2f} mm', fontsize=6, color=col, va='top')
    ax.text(4.4, 12.0, 'RMSE', fontsize=6, va='top', fontweight='bold')
    ax.plot([4, 12.5], [4, 12.5], color=REF, lw=0.6)
    ax.set_xlim(4, 12.5); ax.set_ylim(4, 12.5); ax.set_aspect('equal')
    ax.set_xlabel('Observed final rut (mm)'); ax.set_ylabel('Predicted final rut (mm)' if j == 0 else '')
    title(ax, f'Forecast from first {int(f * 100)}% of record')
    ins = ax.inset_axes([0.6, 0.08, 0.36, 0.25])
    ins.hist(errs_u, bins=np.arange(-3, 3.01, 0.5), color=UNSEEN, lw=0)
    ins.axvline(0, color=REF, lw=0.4); ins.set_yticks([]); ins.set_xticks([-2, 0, 2]); ins.tick_params(labelsize=5, length=1.5, pad=1)
    for s_ in ['left', 'top', 'right']: ins.spines[s_].set_visible(False)
    label(ax, 'abc'[j], x=-0.18 if j == 0 else -0.08)
    if j == 0: ax.legend(loc='upper left', bbox_to_anchor=(0.0, 0.76), handletextpad=0.1)
for i, (e, ks) in enumerate([('E1E2', ['F', 'ME', 'GE', 'EnKF', 'PT', 'LSTM']), ('E3', ['F', 'ME', 'GE', 'EnKF', 'PT', 'LSTM'])]):
    ax = fig.add_subplot(gs[1, i])
    for k in ks:
        v = [val(e, INV[k], 'early_life', s, 'end_abs_err_mean') for s in [0.2, 0.4, 0.6]]
        line(ax, [20, 40, 60], v, k)
    ax.set_yscale('log'); ax.set_yticks([0.4, 0.6, 1, 2, 4]); ax.set_yticklabels(['0.4', '0.6', '1', '2', '4']); ax.minorticks_off()
    ax.set_xticks([20, 40, 60]); ax.set_xticklabels(['20%', '40%', '60%']); ax.set_xlim(12, 64)
    ax.set_xlabel('Record observed'); ax.set_ylabel('Mean abs. error, final rut (mm)' if i == 0 else '')
    title(ax, ['Seen structure classes', 'Unseen structure classes'][i])
    if i == 0: ax.legend(loc='upper right', ncol=2, columnspacing=0.6, fontsize=6)
    label(ax, 'de'[i], x=-0.18 if i == 0 else -0.08)
ax = fig.add_subplot(gs[1, 2]); thr = 8.0
sc = [('cold', 'Cold'), ('e0.2', '20%'), ('e0.4', '40%'), ('e0.6', '60%')]
for k in ['F', 'ME', 'GE']:
    bs = []
    for key, _ in sc:
        sq = []
        for n, d in E['E3'].items():
            y = d['y']; T = len(y); mu, var = d[f'{k}_{key}']
            cut = 0 if key == 'cold' else max(2, int(T * float(key[1:])))
            p = 1 - norm.cdf((thr - mu[cut:]) / np.sqrt(var[cut:]))
            sq.append((p - (y[cut:] > thr)) ** 2)
        bs.append(np.mean(np.concatenate(sq)))
    line(ax, range(4), bs, k)
ax.set_xticks(range(4)); ax.set_xticklabels([l for _, l in sc]); ax.set_xlabel('Record observed')
ax.set_ylabel('Brier score'); title(ax, 'P(rut > 8 mm), unseen classes'); ax.legend(loc='upper right')
label(ax, 'f', x=-0.18)
save(fig, 'Fig10_end_of_record')
# ============================================================== Fig 12  probabilistic quality
fig, axs = plt.subplots(1, 4, figsize=(W2, 58 * MM), layout='constrained')
levels = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95])
ax = axs[0]
for e in ['E1E2', 'E3']:
    for k in ['F', 'ME', 'GE']:
        z = []
        for n, d in E[e].items():
            y = d['y']; T = len(y); mu, var = d[f'{k}_h'][0][:T - 6, 5], d[f'{k}_h'][1][:T - 6, 5]
            z.append((y[6:] - mu) / np.sqrt(var))
        z = np.abs(np.concatenate(z))
        cov = [(z <= norm.ppf(0.5 + p / 2)).mean() for p in levels]
        ax.plot(levels, cov, color=M[k][0], marker=M[k][1], ms=2.4, mec='white', mew=0.3, ls=LS[e], lw=0.9)
ax.plot([0, 1], [0, 1], color=INK2, lw=0.5)
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.set_aspect('equal')
ax.set_xlabel('Nominal coverage'); ax.set_ylabel('Empirical coverage'); title(ax, 'Reliability, $h$ = 6')
label(ax, 'a', x=-0.25)
ax = axs[1]
bins = np.linspace(0, 1, 11)
for k in ['GE', 'ME', 'F']:
    pit = []
    for n, d in E['E3'].items():
        y = d['y']; T = len(y); mu, var = d[f'{k}_h'][0][:T - 6, 5], d[f'{k}_h'][1][:T - 6, 5]
        pit.append(norm.cdf((y[6:] - mu) / np.sqrt(var)))
    hh, _ = np.histogram(np.concatenate(pit), bins=bins, density=True)
    ax.stairs(hh, bins, color=M[k][0], lw=1.1 if k == 'F' else 0.9, label=M[k][3], baseline=None)
ax.axhline(1, color=INK2, lw=0.5, ls='--'); ax.set_ylim(0, 2.2); ax.set_xlim(0, 1)
ax.set_xlabel('PIT'); ax.set_ylabel('Density'); ax.legend(loc='upper center', fontsize=6); title(ax, 'PIT, unseen classes, $h$ = 6')
label(ax, 'b', x=-0.22)
ax = axs[2]
NUM['ssr'] = {}
for e in ['E1E2', 'E3']:
    for k in ['F', 'ME', 'GE']:
        ss = []
        for hh in range(1, 13):
            er, vv = [], []
            for n, d in E[e].items():
                y = d['y']; T = len(y)
                er.append(d[f'{k}_h'][0][:T - hh, hh - 1] - y[hh:]); vv.append(d[f'{k}_h'][1][:T - hh, hh - 1])
            er, vv = np.concatenate(er), np.concatenate(vv)
            ss.append(np.sqrt(vv.mean()) / np.sqrt((er ** 2).mean()))
        NUM['ssr'][f'{e}_{k}'] = np.round(ss, 2).tolist()
        ax.plot(range(1, 13), ss, color=M[k][0], ls=LS[e], lw=1.1 if k == 'F' else 0.9)
ax.axhline(1, color=INK2, lw=0.5, ls='--')
ax.set_xticks([1, 3, 6, 9, 12]); ax.set_xlabel('Forecast horizon $h$'); ax.set_ylabel('Spread–skill ratio')
ax.set_ylim(0.55, 1.25); title(ax, 'Spread–skill ratio')
ax.text(12, 0.6, 'under-dispersed', ha='right', fontsize=6, color=INK2)
label(ax, 'c', x=-0.22)
ax = axs[3]
for e in ['E1E2', 'E3']:
    base = [val(e, 'gbm_ens', 'horizon', h, 'CRPS_mean') for h in [1, 3, 6, 12]]
    for k in ['F', 'ME', 'EnKF']:
        v = [val(e, INV[k], 'horizon', h, 'CRPS_mean') for h in [1, 3, 6, 12]]
        ax.plot([1, 3, 6, 12], (np.array(v) / np.array(base) - 1) * 100, color=M[k][0], marker=M[k][1], ms=2.6, mec='white',
                mew=0.3, ls=LS[e], lw=1.1 if k == 'F' else 0.9)
ax.axhline(0, color=M['GE'][0], lw=0.8)
ax.text(12, -1.5, 'GBM-E = 0', color=M['GE'][0], fontsize=6, ha='right', va='top')
ax.set_xticks([1, 3, 6, 12]); ax.set_xlabel('Forecast horizon $h$'); ax.set_ylabel('CRPS relative to GBM-E (%)')
ax.set_ylim(-25, 42); title(ax, 'CRPS versus GBM-E'); label(ax, 'd', x=-0.22)
hd = [Line2D([], [], color=M[k][0], marker=M[k][1], ms=3, mec='white', mew=0.3, lw=1) for k in ['F', 'ME', 'GE', 'EnKF']] + \
     [Line2D([], [], color=INK2, ls='-', lw=0.9), Line2D([], [], color=INK2, ls=(0, (3, 1.5)), lw=0.9)]
fig.legend(hd, ['MSSA-F', 'MSSA-E', 'GBM-E', 'JTG-EnKF', 'seen classes', 'unseen classes'], loc='outside upper center', ncol=6)
save(fig, 'Fig14_probabilistic')

# ============================================================== Fig 14  counterfactual consistency
CF = pd.read_csv(R + 'summary_counterfactual_E1E2.csv')
ks = ['mssa', 'jtg_enkf', 'gbm_residual', 'patchtst', 'lstm']
fig, axs = plt.subplots(1, 2, figsize=(W2 * 0.75, 50 * MM), layout='constrained', gridspec_kw=dict(width_ratios=[1.15, 1]))
ax = axs[0]
for i, m in enumerate(ks):
    k = CODE[m]; yv = len(ks) - 1 - i
    a = CF[(CF.model == m) & (CF.setting == 'temp_plus5')].iloc[0].frac_increase * 100
    b = CF[(CF.model == m) & (CF.setting == 'load_x2')].iloc[0].frac_increase * 100
    ax.plot([a, b], [yv, yv], color=HAIR, lw=2.2, solid_capstyle='round')
    ax.plot(a, yv + 0.13, 'o', color='#a3302f', ms=4.5, mec='white', mew=0.4)
    ax.plot(b, yv - 0.13, 's', color=INK2, ms=4.2, mec='white', mew=0.4)
ax.set_yticks(range(len(ks))); ax.set_yticklabels([M[CODE[m]][3] for m in ks][::-1]); ax.tick_params(axis='y', length=0)
ax.spines['left'].set_visible(False); ax.set_xlim(40, 103); ax.grid(axis='x'); ax.set_axisbelow(True)
ax.set_xlabel('Forecast points with rut increase (%)')
ax.legend([Line2D([], [], marker='o', ls='', color='#a3302f', ms=4), Line2D([], [], marker='s', ls='', color=INK2, ms=4)],
          ['air temp. +5 °C', 'traffic ×2'], loc='upper left', borderaxespad=0.1)
title(ax, 'Direction of response'); label(ax, 'a', x=-0.25)
ax = axs[1]
for i, m in enumerate(ks):
    yv = len(ks) - 1 - i
    a = CF[(CF.model == m) & (CF.setting == 'temp_plus5')].iloc[0].mean_delta
    b = CF[(CF.model == m) & (CF.setting == 'load_x2')].iloc[0].mean_delta
    ax.plot(a, yv + 0.12, 'o', color='#a3302f', ms=4.5, mec='white', mew=0.4)
    ax.plot(b, yv - 0.12, 's', color=INK2, ms=4.2, mec='white', mew=0.4)
ax.axvline(0, color=INK2, lw=0.5)
ax.set_yticks(range(len(ks))); ax.set_yticklabels([]); ax.tick_params(axis='y', length=0); ax.spines['left'].set_visible(False)
ax.set_xlabel('Mean change of forecast (mm)'); ax.grid(axis='x'); ax.set_axisbelow(True); title(ax, 'Magnitude of response')
label(ax, 'b', x=-0.05)
save(fig, 'Fig15_counterfactual')

# ============================================================== Fig 15  exponents (raincloud)
P = pd.concat([pd.read_csv(R + 'params_E1E2.csv').assign(E='E1E2'), pd.read_csv(R + 'params_E3.csv').assign(E='E3')])
P = P[P.model == 'mssa']
fig, axs = plt.subplots(1, 2, figsize=(W2, 52 * MM), layout='constrained')
spec = [('beta', r'Load exponent $\beta$', (0.176, 0.292), 0.48, 'a', (0.12, 0.54)),
        ('gamma', r'Temperature exponent $\gamma$', (3.499, 3.735), 2.93, 'b', (2.8, 3.9))]
r2 = np.random.default_rng(3)
for ax, (p, lab, band, code, L, lim) in zip(axs, spec):
    ax.axvspan(*band, color=M['GE'][0], alpha=0.14, lw=0)
    ax.axvline(code, color=M['EnKF'][0], lw=0.9, ls='--')
    for j, (e, col) in enumerate([('E1E2', SEEN), ('E3', UNSEEN)]):
        v = P[P.E == e][p].values
        xs = np.linspace(*lim, 400); kde = gaussian_kde(v, bw_method=0.35)(xs); kde = kde / kde.max() * 0.38
        ax.fill_between(xs, j + 0.08, j + 0.08 + kde, color=col, alpha=0.35, lw=0)
        ax.plot(xs, j + 0.08 + kde, color=col, lw=0.6)
        ax.scatter(v, j - 0.14 + r2.uniform(-0.06, 0.06, len(v)), s=5, color=col, alpha=0.8, lw=0)
        q1, q2, q3 = np.percentile(v, [25, 50, 75])
        ax.plot([q1, q3], [j - 0.02] * 2, color=INK, lw=1.6, solid_capstyle='butt'); ax.plot(q2, j - 0.02, '|', color='white', ms=4, mew=1)
        ax.text(xs[np.argmax(kde)], j + 0.08 + kde.max() + 0.03, f'{np.mean(v):.3f} ± {np.std(v):.3f}' if p == 'beta' else f'{np.mean(v):.2f} ± {np.std(v):.2f}',
                ha='center', va='bottom', fontsize=6, color=col)
    ax.set_yticks([0, 1]); ax.set_yticklabels(['Seen-class\nfolds (n = 25)', 'Unseen-class\nfolds (n = 35)'])
    ax.tick_params(axis='y', length=0); ax.spines['left'].set_visible(False)
    ax.set_ylim(-0.35, 1.9); ax.set_xlim(*lim); ax.set_xlabel(lab); title(ax, 'Load exponent' if p == 'beta' else 'Temperature exponent')
    ax.legend([Patch(color=M['GE'][0], alpha=0.14), Line2D([], [], color=M['EnKF'][0], ls='--', lw=0.9)],
              ['Wu et al. (2022) field recalibration', 'JTG D50-2017 value'], loc='upper left', fontsize=6.3)
    ax.set_ylim(-0.35, 2.2)
    label(ax, L, x=-0.2 if L == 'a' else -0.2)
save(fig, 'Fig16_exponents')

# ============================================================== A1 ablation heatmap
A = pd.read_csv('/home/claude/paper/ablation.csv', header=[0, 1], index_col=0)
names = {'mssa:no_rate': 'no structure rate state θ', 'mssa:neural_ssm': 'neural transition replaces JTG law',
         'mssa:no_rw': 'datum held constant', 'mssa:no_rev': 'no recoverable component',
         'mssa:no_proj': 'no monotone projection', 'mssa:no_ms': 'no multi-step loss',
         'mssa:no_disc': 'no discrepancy term', 'mssa:no_defl': 'no deflection input', 'mssa:fixed_mat': 'material terms fixed'}
cols = [('horizon', '1.0', '$h$=1'), ('horizon', '6.0', '$h$=6'), ('horizon', '12.0', '$h$=12'), ('sparse_all', '8.0', '$k$=8'),
        ('early_life', '0.4', '40%'), ('cold_start', '0.0', 'Cold')]
Mx = np.array([[(A.loc[k, (p, s)] / A.loc['mssa', (p, s)] - 1) * 100 for p, s, _ in cols] for k in names])
fig, ax = plt.subplots(figsize=(W15 * 0.85, 55 * MM), layout='constrained')
im = ax.imshow(Mx, cmap=DIV.reversed(), norm=TwoSlopeNorm(0, -15, 45), aspect='auto')
for i in range(Mx.shape[0]):
    for j in range(Mx.shape[1]):
        ax.text(j, i, f'{Mx[i, j]:+.1f}', ha='center', va='center', fontsize=5.8, color='white' if Mx[i, j] > 25 else INK)
ax.set_xticks(range(len(cols))); ax.set_xticklabels([c[2] for c in cols]); ax.xaxis.tick_top()
ax.set_yticks(range(len(names))); ax.set_yticklabels(list(names.values())); ax.tick_params(length=0)
for s in ax.spines.values(): s.set_visible(False)
cb = fig.colorbar(im, ax=ax, shrink=0.9, aspect=18, pad=0.02); cb.set_label('RMSE change vs full MSSA (%)'); cb.outline.set_visible(False)
save(fig, 'FigA1_ablation')

# ============================================================== A2 per-structure heatmap
d = MAIN['E3']; d = d[(d.protocol == 'horizon') & np.isclose(d.setting, 6)]
piv = d.groupby(['structure', 'model']).RMSE.mean().unstack()[['fusion', 'mssa_ens', 'gbm_ens', 'jtg_enkf', 'persistence']]
piv = piv.loc[sorted(piv.index, key=lambda s: int(s[3:]))]
rel = (piv.values[:, 1:] / piv.values[:, [0]] - 1) * 100
fig, ax = plt.subplots(figsize=(W1, 92 * MM), layout='constrained')
im = ax.imshow(rel, cmap=DIV.reversed(), norm=TwoSlopeNorm(0, -40, 110), aspect='auto')
for i in range(rel.shape[0]):
    for j in range(rel.shape[1]):
        ax.text(j, i, f'{rel[i, j]:+.0f}', ha='center', va='center', fontsize=5.6, color='white' if rel[i, j] > 60 else INK)
ax.set_xticks(range(4)); ax.set_xticklabels(['MSSA-E', 'GBM-E', 'JTG-EnKF', 'Persist.']); ax.xaxis.tick_top()
ax.set_yticks(range(len(piv))); ax.set_yticklabels([f'{s}  {piv.iloc[i, 0]:.2f}' for i, s in enumerate(piv.index)], fontsize=6)
ax.tick_params(length=0)
for s in ax.spines.values(): s.set_visible(False)
cb = fig.colorbar(im, ax=ax, shrink=0.6, aspect=20, pad=0.03); cb.set_label('RMSE above MSSA-F (%)'); cb.outline.set_visible(False)
save(fig, 'FigA2_structures')

# ============================================================== A3 hidden material
HM = pd.read_csv(R + 'E5_hidden_material.csv')
fig, ax = plt.subplots(figsize=(W1 * 0.8, 62 * MM), layout='constrained')
g = HM.groupby('slot').agg(lab=('R0_lab', 'first'), m=('R0_recovered_when_hidden', 'mean'), s=('R0_recovered_when_hidden', 'std'))
ax.errorbar(g.lab, g.m, yerr=g.s, fmt='o', color=M['ME'][0], mec='white', mew=0.4, ms=4, elinewidth=0.7, capsize=0)
lo, hi = 1.2, 3.4
ax.plot([lo, hi], [lo, hi], color=INK2, lw=0.5, ls='--'); ax.set_xlim(lo, hi); ax.set_ylim(lo, hi); ax.set_aspect('equal')
from scipy.stats import spearmanr
note(ax, f'Spearman $\\rho$ = {spearmanr(g.lab, g.m).correlation:.2f}')
ax.set_xlabel('Laboratory $R_0$ (mm)'); ax.set_ylabel('$R_0$ recovered when withheld (mm)')
save(fig, 'FigA3_material')
json.dump(NUM, open('/home/claude/paper4/numbers_c.json', 'w'), indent=1, default=float)
print(json.dumps(NUM, default=float)[:800])
