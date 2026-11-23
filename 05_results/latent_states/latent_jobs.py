"""Run independent seed-0 exports with the V3 CPU configuration."""
import os, sys
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
from contextlib import redirect_stdout, redirect_stderr
import multiprocessing as mp

ROOT = Path.cwd()
OUT = ROOT / 'results' / 'latent_figures_seed0'
sys.path.insert(0, str(ROOT / 'scripts'))

def worker(job):
    tag, kind, ix = job
    import export_latent as e
    import torch
    torch.set_num_threads(1)
    with (OUT / f'{tag}_{ix}.log').open('w', buffering=1) as log, redirect_stdout(log), redirect_stderr(log):
        cfg = e.load_cfg(str(ROOT / 'configs/full.yaml'))
        cfg.update(data_dir=str(ROOT / 'data'), device='cpu')
        ctx = e.ex.Ctx(cfg, str(OUT), print)
        if tag == 'E0':
            e.run_e0(ctx, 0, OUT / 'latent_E0.npz')
        else:
            orig = e.folds
            e.folds = lambda k, s: [pair if i == ix else ([], []) for i, pair in enumerate(orig(k, s))]
            try:
                e.run_folds(ctx, kind, 0, OUT / f'{tag}_{ix}.npz')
            finally:
                e.folds = orig
    return tag, ix

if __name__ == '__main__':
    import numpy as np
    jobs = [('E0', None, 0)] + [('E1E2', 'manuscript', i) for i in range(5)] + [('E3', 'leave_class_out', i) for i in range(7)]
    with ProcessPoolExecutor(max_workers=13, mp_context=mp.get_context('fork')) as pool:
        for res in pool.map(worker, jobs): print(res, flush=True)
    for tag, nf in [('E1E2', 5), ('E3', 7)]:
        acc = {}
        for i in range(nf):
            with np.load(OUT / f'{tag}_{i}.npz') as data:
                assert not set(acc).intersection(data.files)
                acc.update({k: data[k] for k in data.files})
        np.savez_compressed(OUT / f'latent_{tag}.npz', **acc)
    print('EXPORT_COMPLETE', flush=True)
