"""Publication style v2: Nature/Elsevier conventions.
- final size: 190 mm (double) / 90 mm (single); sans-serif 7 pt text, 8 pt bold lowercase panel labels
- lines 0.5-1.2 pt, axes 0.5 pt, outward ticks; no panel titles (descriptors as small grey text)
- one categorical palette (CVD-validated); blue = MSSA-F, orange = physics, teal = data, violet = code baseline
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

MM = 1 / 25.4
W2, W1, W15 = 190 * MM, 90 * MM, 140 * MM
plt.rcParams.update({
    'font.family': 'Liberation Sans', 'font.size': 7, 'axes.labelsize': 7, 'axes.titlesize': 7,
    'xtick.labelsize': 6.5, 'ytick.labelsize': 6.5, 'legend.fontsize': 6.5, 'legend.title_fontsize': 6.5,
    'axes.linewidth': 0.5, 'xtick.major.width': 0.5, 'ytick.major.width': 0.5, 'xtick.minor.width': 0.4,
    'ytick.minor.width': 0.4, 'xtick.major.size': 2.5, 'ytick.major.size': 2.5, 'xtick.minor.size': 1.5,
    'ytick.minor.size': 1.5, 'xtick.direction': 'out', 'ytick.direction': 'out', 'xtick.major.pad': 2,
    'ytick.major.pad': 2, 'axes.labelpad': 2.5, 'axes.spines.top': False, 'axes.spines.right': False,
    'axes.edgecolor': '#3a3a38', 'xtick.color': '#3a3a38', 'ytick.color': '#3a3a38', 'axes.labelcolor': '#0b0b0b',
    'text.color': '#0b0b0b', 'lines.linewidth': 1.0, 'lines.markersize': 3.5, 'patch.linewidth': 0.5,
    'legend.frameon': False, 'legend.handlelength': 1.6, 'legend.handletextpad': 0.4, 'legend.borderaxespad': 0.2,
    'legend.labelspacing': 0.3, 'legend.columnspacing': 1.0, 'grid.color': '#e8e7e3', 'grid.linewidth': 0.4,
    'axes.grid': False, 'mathtext.fontset': 'custom', 'mathtext.rm': 'Liberation Sans',
    'mathtext.it': 'Liberation Sans:italic', 'mathtext.bf': 'Liberation Sans:bold', 'pdf.fonttype': 42,
    'ps.fonttype': 42, 'savefig.dpi': 600, 'figure.dpi': 200, 'svg.fonttype': 'none'})

INK, INK2, MUTED, HAIR = '#0b0b0b', '#52514e', '#8a8984', '#e8e7e3'
# name -> colour, marker, linestyle, label
M = {
    'F':    ('#2a78d6', 'o', '-', 'MSSA-F'),
    'ME':   ('#eb6834', 's', '-', 'MSSA-E'),
    'GE':   ('#1baf7a', '^', '-', 'GBM-E'),
    'EnKF': ('#6250d6', 'D', '-', 'JTG-EnKF'),
    'PT':   ('#8a8984', 'v', (0, (3, 1.5)), 'PatchTST'),
    'LSTM': ('#3a3a38', 'P', (0, (3, 1.5)), 'LSTM'),
    'PERS': ('#b9b8b1', 'X', (0, (1, 1.2)), 'Persistence'),
    'MSSA': ('#eb6834', 's', '-', 'MSSA'),
    'GBM':  ('#1baf7a', '^', '-', 'GBM'),
}
CODE = {'fusion': 'F', 'mssa_ens': 'ME', 'gbm_ens': 'GE', 'jtg_enkf': 'EnKF', 'patchtst': 'PT', 'lstm': 'LSTM',
        'persistence': 'PERS', 'mssa': 'MSSA', 'gbm_residual': 'GBM'}
INV = {v: k for k, v in CODE.items()}
SEEN, UNSEEN = '#52514e', '#2a78d6'   # validation-scheme colours (grey / blue)
CLS = ['I_SemiRigid_12cmAC', 'II_RigidComposite_12cmAC', 'III_SemiRigid_16_18cmAC', 'IV_Inverted_24_28cmAC',
       'V_ThickAC_I_24_28cm', 'VI_ThickAC_II_36cm', 'VII_FullDepth_48_52cm']
CLS_SHORT = dict(zip(CLS, ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']))
CLS_LONG = dict(zip(CLS, ['Semi-rigid, 12 cm AC', 'Rigid composite, 12 cm AC', 'Semi-rigid, 16–18 cm AC',
                          'Inverted, 24–28 cm AC', 'Thick AC, 24–28 cm', 'Thick AC, 36 cm', 'Full-depth AC, 48–52 cm']))
# diverging blue <-> red with grey midpoint; sequential blue; sequential orange (depth)
DIV = LinearSegmentedColormap.from_list('div', ['#184f95', '#6da7ec', '#f0efec', '#ec8f8e', '#a3302f'])
SEQB = LinearSegmentedColormap.from_list('seqb', ['#f4f8fd', '#cde2fb', '#86b6ef', '#3987e5', '#1c5cab', '#0d366b'])
ORANGES = ['#fbdcc8', '#f7bc97', '#f19a66', '#eb6834', '#c9501f', '#9c3b14', '#6e2a0e', '#4a1c09']


def label(ax, s, x=-0.02, y=1.0, fig=None):
    """Bold lowercase panel label placed just outside the top-left corner of the axes."""
    ax.text(x, y, s, transform=ax.transAxes, fontsize=8, fontweight='bold', va='bottom', ha='right')


def note(ax, s, x=0.02, y=0.98, ha='left', va='top', **kw):
    ax.text(x, y, s, transform=ax.transAxes, fontsize=6.5, color=INK2, ha=ha, va=va, **kw)


def line(ax, x, y, key, lw=None, ms=3.2, label=True, **kw):
    c, mk, ls, lab = M[key]
    return ax.plot(x, y, color=c, marker=mk, ls=ls, ms=ms, mec='white', mew=0.4,
                   lw=lw or (1.3 if key == 'F' else 0.9), label=lab if label else None, zorder=5 if key == 'F' else 3, **kw)


def end_label(ax, x, y, key, dy=0.0, dx=0.25, text=None):
    c = M[key][0]
    ax.text(x + dx, y + dy, text or M[key][3], color=c if key not in ('PERS',) else MUTED, fontsize=6.3, va='center',
            ha='left', fontweight='bold' if key == 'F' else None)


def spread_labels(vals, gap):
    """Return y positions for end labels pushed apart by at least `gap` (keeps order)."""
    order = sorted(range(len(vals)), key=lambda i: vals[i])
    pos = [vals[i] for i in order]
    for k in range(1, len(pos)):
        pos[k] = max(pos[k], pos[k - 1] + gap)
    out = [0] * len(vals)
    for k, i in enumerate(order):
        out[i] = pos[k]
    return out


def save(fig, name, outdir='/home/claude/paper4/fig/'):
    import os
    os.makedirs(outdir, exist_ok=True)
    fig.savefig(outdir + name + '.pdf')
    fig.savefig(outdir + name + '.png', dpi=300)
    fig.savefig(outdir + name + '.tiff', dpi=600, pil_kwargs={'compression': 'tiff_lzw'})
    plt.close(fig)

# ---- v3 additions (learned from Nature-family figures) ----
M['LSTM'] = ('#c45a9e', 'P', (0, (3, 1.5)), 'LSTM')     # muted pink, as secondary baselines in NeuralGCM
M['PT'] = ('#8a8984', 'v', (0, (3, 1.5)), 'PatchTST')
REF = '#0b0b0b'                                         # reference model drawn black dashed


def title(ax, s, **kw):
    """Short centred panel title (Nature style)."""
    kw.setdefault('pad', 3)
    ax.set_title(s, fontsize=7, loc='center', **kw)


def boxed(ax):
    for s in ['top', 'right']:
        ax.spines[s].set_visible(True)
