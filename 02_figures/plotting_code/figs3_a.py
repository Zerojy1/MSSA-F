"""Figures 3-6 in Nature-family style (Severson 2019 Nat Energy; NeuralGCM 2024 Nature; GenCast 2024 Nature;
Wang 2024 Nat Commun)."""
import numpy as np, pandas as pd, json
from scipy.stats import spearmanr
from matplotlib.gridspec import GridSpec
from matplotlib.lines import Line2D
from matplotlib.colors import Normalize, LinearSegmentedColormap
from matplotlib import cm as mcm
from styleA import *
from common import *
NUM = {}
D = pd.read_csv('/home/claude/v3/data/rutting_long.csv')
ST = pd.read_csv('/home/claude/v3/data/structures.csv').set_index('STR')
ST['AC'] = ST[[c for c in ST.columns if not c.startswith('Base') and c != 'Struct_Class']].sum(axis=1)

# ============================================================== Fig 3  data (Severson Fig 1 layout)
fin = D.sort_values('Observation_Order').groupby('STR').Rutting_Depth_mm.last()
COOL = LinearSegmentedColormap.from_list('cw', ['#1c5cab', '#6da7ec', '#d8d7d2', '#ec8f8e', '#b8312f'])
norm = Normalize(5, 11.6)
fig = plt.figure(figsize=(W2, 105 * MM), layout='constrained')
gs = GridSpec(2, 3, figure=fig, height_ratios=[1.1, 1])
ax = fig.add_subplot(gs[0, :2])
for s, g in sorted(D.groupby('STR'), key=lambda x: fin[x[0]]):
    ax.plot(g.Cum_Load_10k / 100, g.Rutting_Depth_mm, color=COOL(norm(fin[s])), lw=0.8)
ax.set_xlabel('Cumulative ESAL (million)'); ax.set_ylabel('Rut depth (mm)'); ax.set_xlim(0, 61); ax.set_ylim(0, 12.2)
ax.axvspan(0, 8, color='#f0efec', lw=0, zorder=0); ax.text(4, 0.4, 'b', ha='center', fontsize=6.5, color=INK2)
sm = mcm.ScalarMappable(norm=norm, cmap=COOL)
cb = fig.colorbar(sm, ax=ax, pad=0.01, aspect=18); cb.set_label('Final rut depth (mm)'); cb.outline.set_visible(False)
cb.ax.tick_params(width=0.4, length=2)
title(ax, '19 structures, 2,753 surveys, 2016–2021'); label(ax, 'a', x=-0.07)
ax = fig.add_subplot(gs[0, 2])
for s, g in D.groupby('STR'):
    g = g[g.Cum_Load_10k <= 800]
    ax.plot(g.Cum_Load_10k / 100, g.Rutting_Depth_mm, color=COOL(norm(fin[s])), lw=0.7, marker='o', ms=1.2, mew=0)
ax.set_xlabel('Cumulative ESAL (million)'); ax.set_ylabel('Rut depth (mm)'); ax.set_xlim(0, 8)
title(ax, 'First 8 million ESAL'); label(ax, 'b', x=-0.17)
# c-e: what predicts the final rut?
cut = lambda g, f: g.sort_values('Observation_Order').Rutting_Depth_mm.values[max(1, int(len(g) * f)) - 1]
feats = [('AC', ST['AC'], 'Total asphalt thickness (cm)'),
         ('r10', D.groupby('STR').apply(lambda g: cut(g, 0.1), include_groups=False), 'Rut depth at 10% of record (mm)'),
         ('r40', D.groupby('STR').apply(lambda g: cut(g, 0.4), include_groups=False), 'Rut depth at 40% of record (mm)')]
NUM['rho'] = {}
sub = gs[1, :].subgridspec(1, 3, wspace=0.08)
for i, (k, x, lab) in enumerate(feats):
    ax = fig.add_subplot(sub[0, i])
    x = x[fin.index]
    ax.scatter(x, fin, s=14, c=COOL(norm(fin.values)), edgecolor='white', lw=0.4, zorder=3)
    rho = spearmanr(x, fin).correlation; NUM['rho'][k] = round(rho, 2)
    ax.text(0.05, 0.92, f'$\\rho$ = {rho:.2f}', transform=ax.transAxes, fontsize=6.8)
    ax.set_xlabel(lab); ax.set_ylabel('Final rut depth (mm)' if i == 0 else '')
    ax.set_ylim(4.5, 12.2); label(ax, 'cde'[i], x=-0.15 if i == 0 else -0.08)
save(fig, 'Fig3_data')

# ============================================================== Fig 4  identifiability (+ inset histogram)
E0 = pd.read_csv(R + 'E0_identifiability.csv')
L0 = np.load(LAT + 'latent_E0.npz', allow_pickle=True)
fig = plt.figure(figsize=(W2, 60 * MM), layout='constrained')
gs = GridSpec(2, 3, figure=fig, width_ratios=[1.05, 1.4, 0.95])
ax = fig.add_subplot(gs[:, 0])
pars = [('beta', r'$\beta$'), ('gamma', r'$\gamma$'), ('phi', r'$\phi$'), ('sig_m', r'$\sigma_m$'), ('sig_r', r'$\sigma_r$')]
for j, lv in enumerate(sorted(E0.sig_m_true.unique())):
    d = E0[E0.sig_m_true == lv]
    for i, (p, lab) in enumerate(pars):
        tru = lv if p == 'sig_m' else d[p + '_true']
        rel = (d[p + '_hat'] / tru - 1) * 100
        y = len(pars) - 1 - i + (0.13 if j == 0 else -0.13)
        ax.scatter(rel, np.full(len(rel), y), s=8, marker='o', facecolor=[M['F'][0], 'white'][j], edgecolor=M['F'][0],
                   lw=0.6, zorder=3, label=f'$\\sigma_m$ = {lv:.1f} mm' if i == 0 else None)
ax.axvline(0, color=REF, lw=0.6, ls='--')
ax.set_yticks(range(len(pars))); ax.set_yticklabels([l for _, l in pars][::-1], fontsize=7.5)
ax.tick_params(axis='y', length=0); ax.spines['left'].set_visible(False); ax.set_ylim(-0.6, 4.6)
ax.set_xlabel('Relative error (%)'); ax.set_xlim(-20, 10)
ax.legend(loc='upper right', handletextpad=0.1, borderaxespad=0.0)
title(ax, 'Parameter recovery'); label(ax, 'a', x=-0.1)
names = [str(n) for n in L0['names']]; i0 = names.index('STR1')
T = int(L0['tmask'][i0].sum()); t = np.arange(1, T + 1)
axt = fig.add_subplot(gs[0, 1]); axr = fig.add_subplot(gs[1, 1], sharex=axt)
axt.plot(t, L0['Rperm_true'][i0, :T], color=REF, lw=0.9, label='True')
axt.plot(t, L0['Rperm_hat'][i0, :T], color=M['ME'][0], lw=0.9, ls=(0, (3, 1.2)), label='Filtered')
axt.set_ylabel('$R_{perm}+d_0$ (mm)'); axt.tick_params(labelbottom=False); axt.legend(loc='lower right', ncol=2)
title(axt, 'Synthetic structure (STR1 inputs)')
axr.axhline(0, color=MUTED, lw=0.4)
axr.plot(t, L0['rev_true'][i0, :T], color=REF, lw=0.9)
axr.plot(t, L0['rev_hat'][i0, :T], color='#c9501f', lw=0.9, ls=(0, (3, 1.2)))
axr.set_ylabel('$r$ (mm)'); axr.set_xlabel('Survey occasion'); title(axr, 'Recoverable component, same structure')
label(axt, 'b', x=-0.12); label(axr, 'c', x=-0.12)
axp = fig.add_subplot(gs[:, 2])
ok = L0['tmask'] > 0
xt, xh = L0['rev_true'][ok], L0['rev_hat'][ok]
axp.scatter(xt, xh, s=1.5, color=M['F'][0], alpha=0.25, lw=0, rasterized=True)
axp.plot([-1.2, 1.2], [-1.2, 1.2], color=REF, lw=0.6)
axp.set_xlim(-1.2, 1.2); axp.set_ylim(-1.2, 1.2); axp.set_aspect('equal'); boxed(axp)
axp.set_xlabel('True $r$ (mm)'); axp.set_ylabel('Filtered $r$ (mm)')
rm = np.sqrt(np.mean((xt - xh) ** 2)); rr = np.corrcoef(xt, xh)[0, 1]
axp.text(-1.1, 1.0, f'RMSE = {rm:.3f} mm\n$r$ = {rr:.2f}', fontsize=6.5, va='top')
ins = axp.inset_axes([0.58, 0.07, 0.38, 0.3])
ins.hist(xh - xt, bins=30, range=(-0.4, 0.4), color='#3a3a38', lw=0)
ins.set_xticks([-0.3, 0, 0.3]); ins.set_yticks([]); ins.tick_params(labelsize=5, length=1.5, pad=1)
for s in ['left', 'top', 'right']: ins.spines[s].set_visible(False)
title(axp, 'All 19 structures'); label(axp, 'd', x=-0.2)
save(fig, 'Fig4_identifiability')

# ============================================================== Fig 5  skill relative to GBM-E (NeuralGCM Fig 2 grid)
H = [1, 3, 6, 12]
fig, axs = plt.subplots(3, 2, figsize=(W15, 112 * MM), layout='constrained', sharex=True)
rowsel = {'E1E2': ['F', 'ME', 'EnKF', 'PT', 'LSTM'], 'E3': ['F', 'ME', 'EnKF', 'PT', 'LSTM']}
NUM['rel'] = {}
for c, e in enumerate(['E1E2', 'E3']):
    for r, (col, ylab) in enumerate([('RMSE_mean', 'RMSE versus GBM-E (%)'), ('CRPS_mean', 'CRPS versus GBM-E (%)')]):
        ax = axs[r, c]
        base = np.array([val(e, 'gbm_ens', 'horizon', h, col) for h in H])
        for k in rowsel[e]:
            if col == 'CRPS_mean' and k in ('PT', 'LSTM'):
                pass
            v = np.array([val(e, INV[k], 'horizon', h, col) for h in H]) / base * 100
            if np.all(np.isnan(v)): continue
            ax.plot(H, v, color=M[k][0], ls=M[k][2], lw=1.2 if k == 'F' else 0.9, marker=M[k][1], ms=2.6, mec='white', mew=0.3,
                    label=M[k][3])
            NUM['rel'][f'{e}_{col}_{k}'] = np.round(v, 1).tolist()
        ax.axhline(100, color=REF, lw=0.8, ls=(0, (3, 1.5)), label='GBM-E')
        if c == 0: ax.set_ylabel(ylab)
        ax.set_ylim(78, 150)
    ax = axs[2, c]
    for k in ['F', 'ME', 'GE']:
        ss = []
        for hh in range(1, 13):
            er, vv = [], []
            for n, d in E[e].items():
                y = d['y']; T = len(y)
                er.append(d[f'{k}_h'][0][:T - hh, hh - 1] - y[hh:]); vv.append(d[f'{k}_h'][1][:T - hh, hh - 1])
            er, vv = np.concatenate(er), np.concatenate(vv)
            ss.append(np.sqrt(vv.mean() / (er ** 2).mean()))
        ax.plot(range(1, 13), ss, color=M[k][0] if k != 'GE' else REF, ls='-' if k != 'GE' else (0, (3, 1.5)),
                lw=1.2 if k == 'F' else 0.9, label=M[k][3])
    ax.axhline(1, color=MUTED, lw=0.5)
    ax.set_ylim(0.45, 1.15); ax.set_xlabel('Forecast horizon (surveys)'); ax.set_xticks([1, 3, 6, 9, 12])
    if c == 0: ax.set_ylabel('Spread–skill ratio')
    nm = ['seen classes', 'unseen classes'][c]
    title(axs[0, c], f'RMSE, {nm}'); title(axs[1, c], f'CRPS, {nm}'); title(axs[2, c], f'Spread–skill ratio, {nm}')
for i, ax in enumerate(axs.flat):
    label(ax, 'abcdef'[[0, 3, 1, 4, 2, 5][i]] if False else 'abcdef'[i], x=-0.17 if i % 2 == 0 else -0.08)
h_, l_ = axs[0, 0].get_legend_handles_labels()
axs[0, 1].legend(h_, l_, loc='upper left', ncol=2, columnspacing=0.8)
axs[2, 0].legend(loc='lower left')
save(fig, 'Fig5_skill')

# ============================================================== Fig 6  scorecard with hatching + per-structure violins
fig = plt.figure(figsize=(W2, 105 * MM), layout='constrained')
gs = GridSpec(2, 1, figure=fig, height_ratios=[1.05, 1])
ax = fig.add_subplot(gs[0])
rows = ['ME', 'GE', 'EnKF', 'PT', 'LSTM', 'PERS']
cols = SETTINGS[::-1]
nc = len(cols)
Mx = np.full((len(rows), 2 * nc + 1), np.nan); SIG = np.zeros_like(Mx, bool)
for j, e in enumerate(['E1E2', 'E3']):
    P = pd.read_csv(R + f'paired_vs_fusion_{e}.csv')
    for ci_, (p, s, _) in enumerate(cols):
        f = val(e, 'fusion', p, s)
        for i, k in enumerate(rows):
            v = val(e, INV[k], p, s)
            Mx[i, j * (nc + 1) + ci_] = (v / f - 1) * 100
            x = P[(P.protocol == p) & np.isclose(P.setting, s) & (P.model == INV[k])]
            if len(x): SIG[i, j * (nc + 1) + ci_] = (x.ci_low.iloc[0] > 0) or (x.ci_high.iloc[0] < 0)
cmap = LinearSegmentedColormap.from_list('sc', ['#c0392b', '#f2b8b5', '#ffffff', '#b7d3f6', '#1c5cab'])
cmap.set_bad('white')
im = ax.imshow(np.ma.masked_invalid(np.clip(Mx, -30, 30)), cmap=cmap, vmin=-30, vmax=30, aspect='auto')
for i in range(Mx.shape[0]):
    for j in range(Mx.shape[1]):
        if np.isfinite(Mx[i, j]) and not SIG[i, j]:
            ax.add_patch(plt.Rectangle((j - 0.5, i - 0.5), 1, 1, fill=False, hatch='//////', edgecolor='#9a9994', lw=0))
xl = [c[2].replace('k=', '$k$=').replace('h=', '$h$=') for c in cols]
ax.set_xticks(list(range(nc)) + list(range(nc + 1, 2 * nc + 1))); ax.set_xticklabels(xl + xl, fontsize=6)
ax.set_yticks(range(len(rows))); ax.set_yticklabels([M[k][3] for k in rows]); ax.tick_params(length=0)
for s in ax.spines.values(): s.set_visible(False)
ax.text((nc - 1) / 2, -0.95, 'Seen structure classes', ha='center', fontsize=7)
ax.text(nc + 1 + (nc - 1) / 2, -0.95, 'Unseen structure classes', ha='center', fontsize=7)
ax.set_ylim(len(rows) - 0.5, -1.3)
cb = fig.colorbar(im, ax=ax, shrink=0.85, aspect=14, pad=0.01, extend='both', ticks=[-30, -15, 0, 15, 30])
cb.set_label('RMSE versus MSSA-F (%)'); cb.outline.set_visible(False); cb.ax.tick_params(width=0.4, length=2)
cb.ax.text(2.6, 1.02, 'MSSA-F\nbetter', transform=cb.ax.transAxes, fontsize=5.8, color='#1c5cab', va='bottom', ha='center')
label(ax, 'a', x=-0.05, y=1.02); title(ax, 'RMSE relative to MSSA-F across all settings')
# b violins (Wang 2024 style): per-structure RMSE at h = 6
sub = gs[1].subgridspec(1, 2)
for j, e in enumerate(['E1E2', 'E3']):
    ax = fig.add_subplot(sub[0, j])
    ks = ['F', 'ME', 'GE', 'EnKF']
    for i, k in enumerate(ks):
        v = np.sqrt(per_struct(e, INV[k], 'horizon', 6).mse.values)
        vp = ax.violinplot(v, positions=[i], widths=0.7, showextrema=False)
        for b in vp['bodies']:
            b.set_facecolor(M[k][0]); b.set_alpha(0.28); b.set_edgecolor(M[k][0]); b.set_linewidth(0.6)
        ax.scatter(np.full(len(v), i) + rng.uniform(-0.08, 0.08, len(v)), v, s=4, color=M[k][0], lw=0, zorder=3)
        ax.plot([i - 0.18, i + 0.18], [v.mean()] * 2, color=REF, lw=1.0, zorder=4)
        ax.plot([i, i], [v.mean() - v.std(), v.mean() + v.std()], color=REF, lw=0.6, zorder=4)
    ax.set_xticks(range(4)); ax.set_xticklabels([M[k][3] for k in ks]); ax.tick_params(axis='x', length=0)
    ax.set_ylabel('Structure RMSE, $h$ = 6 (mm)' if j == 0 else ''); ax.set_ylim(0.15, 1.15)
    title(ax, ['Seen structure classes (15)', 'Unseen structure classes (19)'][j])
    label(ax, 'bc'[j], x=-0.12 if j == 0 else -0.06)
save(fig, 'Fig6_scorecard')
json.dump(NUM, open('/home/claude/paper4/numbers_a.json', 'w'), indent=1, default=float)
print(NUM['rho'])
