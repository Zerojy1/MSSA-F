import numpy as np, pandas as pd, json
from scipy.stats import norm
from matplotlib.gridspec import GridSpec
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from styleA import *
from common import *
NUM = {}

models = {'E1E2': ['PERS', 'LSTM', 'PT', 'EnKF', 'GE', 'ME', 'F'], 'E3': ['PERS', 'LSTM', 'PT', 'EnKF', 'GE', 'ME', 'F']}
# ============================================================== Fig 7  reduced information
fig, axs = plt.subplots(2, 3, figsize=(W2, 98 * MM), layout='constrained', gridspec_kw=dict(width_ratios=[1, 1, 0.85]))
for r, e in enumerate(['E1E2', 'E3']):
    mm = [k for k in models[e] if k != 'PERS']
    ax = axs[r, 0]
    for k in mm:
        line(ax, [1, 2, 4, 8], [val(e, INV[k], 'sparse_all', s) for s in [1, 2, 4, 8]], k)
    ax.set_xscale('log', base=2); ax.set_xticks([1, 2, 4, 8]); ax.set_xticklabels(['1', '2', '4', '8']); ax.minorticks_off()
    ax.set_ylabel('Pooled RMSE (mm)'); ax.grid(axis='y'); ax.set_axisbelow(True)
    title(ax, 'Sparse surveys'); ax.text(-0.3, 0.5, ['Seen classes', 'Unseen classes'][r], transform=ax.transAxes, rotation=90, va='center', ha='center', fontsize=7, fontweight='bold')
    if r == 1: ax.set_xlabel('Survey interval $k$ (every $k$-th survey used)')
    label(ax, 'ad'[r], x=-0.16)
    ax = axs[r, 1]
    for k in mm:
        line(ax, [20, 40, 60], [val(e, INV[k], 'early_life', s) for s in [0.2, 0.4, 0.6]], k)
    ax.set_xticks([20, 40, 60]); ax.set_xticklabels(['20%', '40%', '60%']); ax.set_yscale('log')
    ax.set_yticks([0.5, 1, 2, 3]); ax.set_yticklabels(['0.5', '1', '2', '3']); ax.minorticks_off()
    ax.grid(axis='y'); ax.set_axisbelow(True); ax.set_xlim(14, 66)
    if r == 1: ax.set_xlabel('Record observed before free-run forecast')
    title(ax, 'Early-life extrapolation'); label(ax, 'be'[r], x=-0.08)
    ax = axs[r, 2]
    ks = [k for k in mm if k not in ('PT', 'LSTM')]
    vals = [val(e, INV[k], 'cold_start', 0) for k in ks]
    o = np.argsort(vals)[::-1]
    for j, i in enumerate(o):
        k = ks[i]; ci = boot_pooled(e, INV[k], 'cold_start', 0)
        ax.plot(ci, [j, j], color=M[k][0], lw=1.0, solid_capstyle='round')
        ax.plot(vals[i], j, M[k][1], color=M[k][0], mec='white', mew=0.5, ms=5)
        ax.text(ci[1] + 0.04, j, f'{vals[i]:.2f}', va='center', fontsize=6, color=M[k][0])
    ax.set_yticks(range(len(ks))); ax.set_yticklabels([M[ks[i]][3] for i in o]); ax.tick_params(axis='y', length=0)
    ax.spines['left'].set_visible(False); ax.set_xlim(0.9, 2.75); ax.grid(axis='x'); ax.set_axisbelow(True)
    title(ax, 'Cold start (no survey)')
    ax.set_ylim(-0.5, len(ks) - 0.5)
    if r == 1: ax.set_xlabel('Pooled RMSE (mm), 95% CI')
    label(ax, 'cf'[r], x=-0.32)
from matplotlib.lines import Line2D
hd = [Line2D([], [], color=M[k][0], marker=M[k][1], ls=M[k][2], ms=3.2, mec='white', mew=0.4, lw=1.0) for k in ['F', 'ME', 'GE', 'EnKF', 'PT', 'LSTM']]
fig.legend(hd, [M[k][3] for k in ['F', 'ME', 'GE', 'EnKF', 'PT', 'LSTM']], loc='outside upper center', ncol=6)
save(fig, 'Fig7_reduced_information')
# ============================================================== Fig 7  paired forest
scen = [('horizon', 1, '$h$ = 1'), ('horizon', 3, '$h$ = 3'), ('horizon', 6, '$h$ = 6'), ('horizon', 12, '$h$ = 12'),
        ('sparse_all', 4, '$k$ = 4'), ('sparse_all', 8, '$k$ = 8'), ('early_life', 0.2, 'Early 20%'),
        ('early_life', 0.4, 'Early 40%'), ('early_life', 0.6, 'Early 60%'), ('cold_start', 0, 'Cold start')]
fig, axs = plt.subplots(1, 2, figsize=(W2, 78 * MM), layout='constrained', sharey=True)
for ax, e, L in zip(axs, ['E1E2', 'E3'], 'ab'):
    P = pd.read_csv(R + f'paired_vs_fusion_{e}.csv')
    for i in range(len(scen)):
        if i % 2 == 0:
            ax.axhspan(len(scen) - 1 - i - 0.5, len(scen) - 1 - i + 0.5, color='#f6f6f4', lw=0, zorder=0)
    for mdl, off in [('gbm_ens', 0.16), ('mssa_ens', -0.16)]:
        k = CODE[mdl]
        for i, (p, s, lab) in enumerate(scen):
            x = P[(P.protocol == p) & np.isclose(P.setting, s) & (P.model == mdl)].iloc[0]
            y = len(scen) - 1 - i + off
            sig = x.ci_low > 0 or x.ci_high < 0
            ax.plot([x.ci_low, x.ci_high], [y, y], color=M[k][0], lw=0.9, solid_capstyle='round')
            ax.plot(x.mean_RMSE_diff, y, M[k][1], color=M[k][0] if sig else 'white', mec=M[k][0], mew=0.8, ms=4)
            ax.text(1.01, y, f'{int(x.structures_ref_better)}/{int(x.n_structures)}', transform=ax.get_yaxis_transform(),
                    fontsize=6, color=M[k][0], va='center')
    ax.axvline(0, color=INK2, lw=0.5)
    ax.set_yticks(range(len(scen))); ax.set_yticklabels([s[2] for s in scen][::-1]); ax.tick_params(axis='y', length=0)
    ax.spines['left'].set_visible(False); ax.set_xlim(-0.3, 0.42); ax.set_ylim(-0.6, len(scen) - 0.4)
    ax.set_xlabel('Structure-level RMSE difference (mm); > 0 favours MSSA-F')
    title(ax, ['Seen structure classes', 'Unseen structure classes'][L == 'b'])
    ax.text(1.01, 1.01, 'wins', transform=ax.transAxes, fontsize=6, color=INK2, va='bottom')
    label(ax, L, x=-0.08 if L == 'a' else -0.03)
hd = [Line2D([], [], color=M[k][0], marker=M[k][1], ms=4, lw=0.9) for k in ('GE', 'ME')] + \
     [Line2D([], [], color=INK2, marker='o', ms=4, lw=0, mfc='white', mec=INK2)]
fig.legend(hd, ['GBM-E − MSSA-F', 'MSSA-E − MSSA-F', 'open: 95% CI includes 0'], loc='outside upper center', ncol=3)
save(fig, 'Fig8_paired')

# ============================================================== Fig 9  latent decomposition (real structures, unseen classes)
L3 = np.load(LAT + 'latent_E3.npz', allow_pickle=True)
def lat(n, k): return L3[f'{n}__{k}']
fig = plt.figure(figsize=(W2, 100 * MM), layout='constrained')
gs = GridSpec(2, 3, figure=fig, width_ratios=[1.25, 1, 1], height_ratios=[1, 1])
n0 = 'STR10'
y, N = lat(n0, 'y'), lat(n0, 'N') / 1e6
d0, r, Rp = lat(n0, 'd0'), lat(n0, 'r'), lat(n0, 'Rperm')
perm = d0 + Rp; tot = perm + r
ax = fig.add_subplot(gs[0, 0])
ax.fill_between(N, perm, tot, where=r >= 0, color='#ec8f8e', alpha=0.6, lw=0, interpolate=True)
ax.fill_between(N, perm, tot, where=r < 0, color='#86b6ef', alpha=0.7, lw=0, interpolate=True)
ax.plot(N, perm, color=M['ME'][0], lw=1.1)
ax.plot(N, tot, color=INK, lw=0.5, alpha=0.6)
ax.plot(N, y, 'o', ms=1.5, color=INK, mew=0)
ax.set_ylabel('Rut depth (mm)'); ax.set_xlim(-1, 62); ax.set_ylim(0, 12)
title(ax, f'{n0}, class IV held out')
hd = [Line2D([], [], marker='o', ls='', ms=2.5, color=INK), Line2D([], [], color=M['ME'][0], lw=1.1),
      Patch(color='#ec8f8e', alpha=0.6, lw=0), Patch(color='#86b6ef', alpha=0.7, lw=0)]
ax.legend(hd, ['survey', 'permanent + datum', '$r$ > 0', '$r$ < 0'], loc='lower right', ncol=2, columnspacing=0.8)
label(ax, 'a', x=-0.1)
# b stacked sublayers
ax = fig.add_subplot(gs[1, 0], sharex=ax)
RL, zm, lm = lat(n0, 'R_layer'), lat(n0, 'zmid'), lat(n0, 'lmask'); K_ = len(zm); RL, lm = RL[:, :K_], lm[:K_]
ks = [k for k in np.argsort(zm) if lm[k] > 0]
cols = [ORANGES[min(int(i * (len(ORANGES) - 1) / max(1, len(ks) - 1)), len(ORANGES) - 1)] for i in range(len(ks))]
ax.stackplot(N, *[RL[:, k] for k in ks], colors=cols, lw=0.2, edgecolor='white')
ax.set_ylabel('Permanent rut (mm)'); ax.set_xlabel('Cumulative ESAL (million)'); ax.set_ylim(0, 10)
for i, k in enumerate(ks):
    if RL[-1, k] > 0.45:
        yc = RL[-1, ks[:i]].sum() + RL[-1, k] / 2
        ax.text(57, yc, f'{zm[k]:.0f} mm', fontsize=5.6, va='center', ha='right', color='white' if i >= 3 else INK)
title(ax, 'Permanent rut by sublayer')
label(ax, 'b', x=-0.1)
# c depth share at end of record, all 19 structures grouped by class
bins = [0, 40, 100, 200, 600]; blab = ['0–40', '40–100', '100–200', '> 200']
bcol = [ORANGES[0], ORANGES[2], ORANGES[4], ORANGES[6]]
ax = fig.add_subplot(gs[:, 1])
names = sorted({k.split('__')[0] for k in L3.files}, key=lambda s: int(s[3:]))
rows = []
for c in CLS:
    for n in names:
        if str(lat(n, 'cls')) == c:
            RL, zm, lm = lat(n, 'R_layer'), lat(n, 'zmid'), lat(n, 'lmask'); K_ = len(zm); RL, lm = RL[:, :K_], lm[:K_]
            fin = RL[-1] * lm
            sh = [fin[(zm >= bins[j]) & (zm < bins[j + 1]) & (lm > 0)].sum() for j in range(4)]
            rows.append((n, c, np.array(sh) / max(fin.sum(), 1e-9) * 100))
yy = 0; yt, yl = [], []; prev = None
for n, c, sh in rows:
    if prev is not None and c != prev: yy += 0.6
    left = 0
    for j in range(4):
        ax.barh(yy, sh[j], left=left, color=bcol[j], height=0.8, edgecolor='white', lw=0.4)
        left += sh[j]
    yt.append(yy); yl.append(f'{n}  {CLS_SHORT[c]}'); prev = c; yy += 1
ax.set_yticks(yt); ax.set_yticklabels(yl, fontsize=5.8); ax.invert_yaxis(); ax.tick_params(axis='y', length=0)
ax.spines['left'].set_visible(False); ax.set_xlim(0, 100); ax.set_xlabel('Share of permanent rut (%)')
title(ax, 'Depth distribution at end of record'); ax.legend([Patch(color=c_) for c_ in bcol], blab, title='Depth (mm)', loc='lower center', bbox_to_anchor=(0.5, 1.0), ncol=4,
          handlelength=1.0, columnspacing=0.6)
label(ax, 'c', x=-0.2, y=1.07)
NUM['depth_share'] = {n: np.round(sh, 1).tolist() for n, c, sh in rows}
# d recoverable vs temperature, all structures
ax = fig.add_subplot(gs[0, 2])
Ts = np.concatenate([lat(n, 'T_air') for n in names]); rs = np.concatenate([lat(n, 'r') for n in names])
edges = np.arange(-4, 36, 4); xc, mmn, se = [], [], []
for a, b in zip(edges[:-1], edges[1:]):
    m = (Ts >= a) & (Ts < b)
    if m.sum() > 10:
        xc.append((a + b) / 2); mmn.append(rs[m].mean()); se.append(rs[m].std() / np.sqrt(m.sum()))
ax.scatter(Ts, rs, s=1.2, color=MUTED, alpha=0.25, lw=0, rasterized=True)
ax.errorbar(xc, mmn, yerr=1.96 * np.array(se), color=M['ME'][0], marker='o', ms=3, lw=1.0, elinewidth=0.6, capsize=0, mec='white', mew=0.4)
ax.axhline(0, color=INK2, lw=0.4)
rho = np.corrcoef(Ts, rs)[0, 1]; NUM['r_T_corr'] = round(rho, 2)
title(ax, 'Recoverable component vs temperature'); ax.text(0.03, 0.95, f'Pearson $\\rho$ = {rho:.2f}', transform=ax.transAxes, fontsize=6.5, va='top')
ax.set_xlabel('Air temperature (°C)'); ax.set_ylabel('Recoverable $r$ (mm)'); ax.set_ylim(-1.0, 1.0)
label(ax, 'd', x=-0.2)
# e theta (rate state) at end of record by structure
ax = fig.add_subplot(gs[1, 2])
th = [(n, str(lat(n, 'cls')), float(lat(n, 'theta')[-1])) for n in names]
for i, c in enumerate(CLS):
    v = [t for n, cc, t in th if cc == c]
    ax.scatter(np.full(len(v), i), np.exp(v), s=10, color=M['ME'][0], edgecolor='white', lw=0.4, zorder=3)
ax.axhline(1, color=INK2, lw=0.5, ls='--')
ax.set_xticks(range(7)); ax.set_xticklabels([CLS_SHORT[c] for c in CLS]); ax.tick_params(axis='x', length=0)
ax.set_ylabel('Rate multiplier e$^{\\theta}$ at end'); ax.set_xlabel('Structure class (held out)')
title(ax, 'Structure rate state at end of record'); ax.set_ylim(0.55, 1.75)
label(ax, 'e', x=-0.2)
save(fig, 'Fig11_decomposition')

# ============================================================== Fig 10  regime dumbbell
groups = [('History', SETTINGS[:4]), ('Survey density', SETTINGS[4:7]), ('Lead time', SETTINGS[7:])]
fig, axs = plt.subplots(1, 2, figsize=(W2, 80 * MM), layout='constrained', sharey=True)
ylabs, ypos = [], []; yy = 0; gpos = []
for gname, sc in groups:
    gpos.append((gname, yy))
    for p, s, lab in sc:
        ypos.append(yy); ylabs.append(lab.replace('k=', '$k$ = ').replace('h=', '$h$ = ')); yy += 1
    yy += 0.7
allsc = [s for _, g in groups for s in g]
NUM['regime'] = {}
for ax, mode, L in zip(axs, ['phys', 'fusion'], 'ab'):
    for (p, s, lab), y0 in zip(allsc, ypos):
        pts = {}
        for e in ['E1E2', 'E3']:
            if mode == 'phys':
                g = rel_gain(e, 'gbm_ens', 'mssa_ens', p, s)
            else:
                best = 'gbm_ens' if val(e, 'gbm_ens', p, s) < val(e, 'mssa_ens', p, s) else 'mssa_ens'
                g = rel_gain(e, best, 'fusion', p, s)
            pts[e] = g
            NUM['regime'][f'{mode}_{e}_{lab}'] = round(g[0], 1)
        ax.plot([pts['E1E2'][0], pts['E3'][0]], [y0, y0], color=HAIR, lw=2.2, zorder=1, solid_capstyle='round')
        for e, col, mk, dy in [('E1E2', SEEN, 'o', -0.14), ('E3', UNSEEN, 's', 0.14)]:
            g = pts[e]
            ax.plot([g[1], g[2]], [y0 + dy, y0 + dy], color=col, lw=0.6, alpha=0.6)
            ax.plot(g[0], y0 + dy, mk, color=col, ms=4, mec='white', mew=0.4, zorder=3)
    ax.axvline(0, color=INK2, lw=0.5)
    ax.set_yticks(ypos); ax.set_yticklabels(ylabs); ax.tick_params(axis='y', length=0); ax.spines['left'].set_visible(False)
    ax.grid(axis='x'); ax.set_axisbelow(True)
    if mode == 'phys':
        ax.invert_yaxis()
        ax.set_xlabel('RMSE reduction of MSSA-E relative to GBM-E (%)'); ax.set_xlim(-45, 50)
        ax.text(0.98, 1.0, 'physics better →', transform=ax.transAxes, ha='right', va='bottom', fontsize=6, color=INK2)
        ax.text(0.02, 1.0, '← data better', transform=ax.transAxes, ha='left', va='bottom', fontsize=6, color=INK2)
    else:
        ax.set_xlabel('RMSE reduction of MSSA-F relative to its better component (%)'); ax.set_xlim(-30, 25)
    label(ax, L, x=-0.13 if L == 'a' else -0.03); title(ax, 'Physics versus data' if mode == 'phys' else 'Fusion versus better component')
for gname, y0 in gpos:
    axs[0].text(-0.3, y0 - 0.45, gname, transform=axs[0].get_yaxis_transform(), fontsize=6.5, fontweight='bold', color=INK2, va='bottom')
hd = [Line2D([], [], color=SEEN, marker='o', ls='', ms=4), Line2D([], [], color=UNSEEN, marker='s', ls='', ms=4)]
fig.legend(hd, ['Seen structure classes', 'Unseen structure classes'], loc='outside upper center', ncol=2)
save(fig, 'Fig12_regime')

# ============================================================== Fig 11  complementarity
def errs(e, key, a='ME', b='GE', c='F'):
    out = {a: [], b: [], c: []}
    for n, d in E[e].items():
        y = d['y']; T = len(y)
        for m in out:
            if key.startswith('h'):
                hh = int(key[1:]); out[m].append(d[f'{m}_h'][0][:T - hh, hh - 1] - y[hh:])
            else:
                mu = d[f'{m}_{key}'][0]
                cut = 0 if key == 'cold' else (1 if key.startswith('s') else max(2, int(T * float(key[1:]))))
                out[m].append(mu[cut:] - y[cut:])
    return {m: np.concatenate(v) for m, v in out.items()}
fig = plt.figure(figsize=(W2, 62 * MM), layout='constrained')
gs = GridSpec(1, 4, figure=fig, width_ratios=[1, 1, 1.05, 1.05])
for i, e in enumerate(['E1E2', 'E3']):
    ax = fig.add_subplot(gs[0, i]); er = errs(e, 'h6')
    ax.hexbin(er['ME'], er['GE'], gridsize=34, extent=(-2.2, 2.2, -2.2, 2.2), cmap=SEQB, mincnt=1, bins='log', lw=0)
    ax.plot([-2.2, 2.2], [-2.2, 2.2], color=INK2, lw=0.5, ls='--')
    ax.set_xlim(-2.2, 2.2); ax.set_ylim(-2.2, 2.2); ax.set_aspect('equal')
    ax.set_xlabel('MSSA-E error (mm)'); ax.set_ylabel('GBM-E error (mm)' if i == 0 else '')
    title(ax, f"{['Seen', 'Unseen'][i]} classes, $h$ = 6"); ax.text(-2.0, 1.9, f"$\\rho$ = {np.corrcoef(er['ME'], er['GE'])[0, 1]:.2f}", fontsize=6.5, va='top')
    label(ax, 'ab'[i], x=-0.18 if i == 0 else -0.08)
ax = fig.add_subplot(gs[0, 2])
NUM['corr'] = {}
for e, col, mk in [('E1E2', SEEN, 'o'), ('E3', UNSEEN, 's')]:
    rs_ = [np.corrcoef(*[errs(e, f'h{hh}')[m] for m in ('ME', 'GE')])[0, 1] for hh in range(1, 13)]
    NUM['corr'][e] = np.round(rs_, 2).tolist()
    ax.plot(range(1, 13), rs_, color=col, marker=mk, ms=3, mec='white', mew=0.4, label=['Seen', 'Unseen'][e == 'E3'])
ax.set_ylim(0.5, 0.85); ax.set_xticks([1, 3, 6, 9, 12]); ax.set_xlabel('Forecast horizon $h$'); ax.set_ylabel('Error correlation $\\rho$')
ax.legend(loc='lower left'); ax.grid(axis='y'); ax.set_axisbelow(True); label(ax, 'c', x=-0.2)
ax = fig.add_subplot(gs[0, 3])
lam = np.linspace(0.6, 1.6, 300); cc = np.linspace(0.4, 1.0, 300)
LL, CC = np.meshgrid(lam, cc)
G = (np.minimum(1, LL) - 0.5 * np.sqrt(1 + LL ** 2 + 2 * CC * LL)) / np.minimum(1, LL) * 100
cs = ax.contourf(LL, CC, G, levels=[-30, -20, -10, 0, 5, 10, 15, 20], cmap=DIV.reversed(), vmin=-20, vmax=20, alpha=0.55)
cl = ax.contour(LL, CC, G, levels=[0], colors=INK2, linewidths=0.6)
ax.clabel(cl, fmt={0: 'no gain'}, fontsize=5.5, inline=True)
keys = ['h1', 'h3', 'h6', 'h12', 's2', 's4', 's8', 'e0.2', 'e0.4', 'e0.6', 'cold']
NUM['comb'] = {}
for e, col, mk in [('E1E2', SEEN, 'o'), ('E3', UNSEEN, 's')]:
    for kk in keys:
        er = errs(e, kk)
        sa, sb = np.sqrt(np.mean(er['ME'] ** 2)), np.sqrt(np.mean(er['GE'] ** 2))
        c_ = np.mean(er['ME'] * er['GE']) / (sa * sb)
        ax.plot(sb / sa, c_, mk, color=col, ms=3.6, mec='white', mew=0.5, zorder=4)
        NUM['comb'][f'{e}_{kk}'] = (round(sb / sa, 3), round(c_, 3))
        if e == 'E3' and kk in ('cold', 'e0.2'):
            ax.annotate({'cold': 'cold', 'e0.2': '20%'}[kk], (sb / sa, c_), xytext=(4, -6), textcoords='offset points', fontsize=5.6, color=col)
ax.set_xlabel('RMSE ratio, GBM-E / MSSA-E'); ax.set_ylabel('Error co-movement $c$')
ax.set_xlim(0.6, 1.6); ax.set_ylim(0.4, 1.0)
cb = fig.colorbar(cs, ax=ax, shrink=0.8, aspect=16, pad=0.02); cb.set_label('Fusion gain (%)'); cb.outline.set_visible(False)
cb.ax.tick_params(width=0.4, length=2)
label(ax, 'd', x=-0.22)
save(fig, 'Fig13_complementarity')
print('b done')
