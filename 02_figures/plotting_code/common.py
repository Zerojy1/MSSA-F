import pickle, numpy as np, pandas as pd
R = '/home/claude/res4/merged_v3b/'
LAT = '/home/claude/latent/'
E = pickle.load(open('/home/claude/paper2/data/ens.pkl', 'rb'))
SUM = {e: pd.read_csv(R + f'summary_{e}.csv') for e in ['E1E2', 'E3']}
MAIN = {e: pd.read_csv(R + f'main_{e}.csv') for e in ['E1E2', 'E3']}
rng = np.random.default_rng(0)


def val(e, model, prot, sett, col='RMSE_mean'):
    d = SUM[e]
    x = d[(d.model == model) & (d.protocol == prot) & (np.isclose(d.setting, sett))]
    return np.nan if x.empty else float(x[col].iloc[0])


def per_struct(e, model, prot, sett):
    d = MAIN[e]
    d = d[(d.model == model) & (d.protocol == prot) & (np.isclose(d.setting, sett))]
    return d.assign(mse=d.RMSE ** 2).groupby('structure').agg(mse=('mse', 'mean'), n=('n', 'mean'))


def boot_pooled(e, model, prot, sett, B=2000):
    g = per_struct(e, model, prot, sett)
    if g.empty:
        return np.nan, np.nan
    mse, n = g.mse.values, g.n.values
    idx = rng.integers(0, len(mse), (B, len(mse)))
    v = np.sqrt((mse[idx] * n[idx]).sum(1) / n[idx].sum(1))
    return np.percentile(v, [2.5, 97.5])


def rel_gain(e, a, b, prot, sett, B=2000):
    A, Bm = per_struct(e, a, prot, sett), per_struct(e, b, prot, sett)
    A, Bm = A.align(Bm, join='inner', axis=0)
    n = A.n.values
    def f(i):
        ra = np.sqrt((A.mse.values[i] * n[i]).sum() / n[i].sum()); rb = np.sqrt((Bm.mse.values[i] * n[i]).sum() / n[i].sum())
        return (ra - rb) / ra * 100
    est = f(np.arange(len(n)))
    bs = [f(rng.integers(0, len(n), len(n))) for _ in range(B)]
    return est, *np.percentile(bs, [2.5, 97.5])


SETTINGS = [('cold_start', 0, 'Cold'), ('early_life', 0.2, '20%'), ('early_life', 0.4, '40%'), ('early_life', 0.6, '60%'),
            ('sparse_all', 8, 'k=8'), ('sparse_all', 4, 'k=4'), ('sparse_all', 2, 'k=2'),
            ('horizon', 12, 'h=12'), ('horizon', 6, 'h=6'), ('horizon', 3, 'h=3'), ('horizon', 1, 'h=1')]
