"""Point, interval and probabilistic metrics; adaptive conformal inference; first-passage diagnostics."""
from __future__ import annotations

import math

import numpy as np
from scipy.stats import norm


def point(y, yhat):
    ok = np.isfinite(y) & np.isfinite(yhat)
    e = yhat[ok] - y[ok]
    if e.size == 0:
        return {'n': 0, 'RMSE': np.nan, 'MAE': np.nan, 'R2': np.nan, 'bias': np.nan}
    ss = np.sum((y[ok] - y[ok].mean()) ** 2)
    return {'n': int(e.size), 'RMSE': float(np.sqrt(np.mean(e ** 2))), 'MAE': float(np.mean(np.abs(e))),
            'R2': float(1 - np.sum(e ** 2) / ss) if ss > 0 else np.nan, 'bias': float(np.mean(e))}


def gaussian(y, mu, var, level=0.95):
    ok = np.isfinite(y) & np.isfinite(mu) & np.isfinite(var) & (var > 0)
    if ok.sum() == 0:
        return {'PICP': np.nan, 'MPIW': np.nan, 'IS': np.nan, 'CRPS': np.nan, 'NLL': np.nan}
    y, mu, sd = y[ok], mu[ok], np.sqrt(var[ok])
    z = norm.ppf(0.5 + level / 2)
    lo, hi = mu - z * sd, mu + z * sd
    a = 1 - level
    IS = (hi - lo) + 2 / a * (lo - y) * (y < lo) + 2 / a * (y - hi) * (y > hi)
    w = (y - mu) / sd
    crps = sd * (w * (2 * norm.cdf(w) - 1) + 2 * norm.pdf(w) - 1 / math.sqrt(math.pi))
    nll = 0.5 * np.log(2 * math.pi * sd ** 2) + 0.5 * w ** 2
    return {'PICP': float(np.mean((y >= lo) & (y <= hi))), 'MPIW': float(np.mean(hi - lo)),
            'IS': float(np.mean(IS)), 'CRPS': float(np.mean(crps)), 'NLL': float(np.mean(nll))}


def aci(y, mu, sd, alpha=0.05, gamma=0.01, warmup=10):
    """Adaptive conformal inference (Gibbs & Candes 2021) on normalized scores |y-mu|/sd, run online per
    series. Returns lower, upper arrays (NaN during warm-up)."""
    n = len(y)
    lo, hi = np.full(n, np.nan), np.full(n, np.nan)
    scores = []
    a_t = alpha
    for t in range(n):
        if not (np.isfinite(y[t]) and np.isfinite(mu[t]) and np.isfinite(sd[t])):
            continue
        if len(scores) >= warmup:
            q = np.quantile(scores, min(1.0, max(0.0, 1 - a_t)), method='higher') if a_t > 0 else np.inf
            lo[t], hi[t] = mu[t] - q * sd[t], mu[t] + q * sd[t]
            err = float(not (lo[t] <= y[t] <= hi[t]))
            a_t = a_t + gamma * (alpha - err)
        scores.append(abs(y[t] - mu[t]) / sd[t])
    return lo, hi


def interval_stats(y, lo, hi, alpha=0.05):
    ok = np.isfinite(lo) & np.isfinite(hi) & np.isfinite(y)
    if ok.sum() == 0:
        return {'PICP': np.nan, 'MPIW': np.nan, 'IS': np.nan}
    y, lo, hi = y[ok], lo[ok], hi[ok]
    IS = (hi - lo) + 2 / alpha * (lo - y) * (y < lo) + 2 / alpha * (y - hi) * (y > hi)
    return {'PICP': float(np.mean((y >= lo) & (y <= hi))), 'MPIW': float(np.mean(hi - lo)), 'IS': float(np.mean(IS))}


def first_crossing(N, series, thr):
    idx = np.where(series >= thr)[0]
    return float(N[idx[0]]) if idx.size else np.nan
