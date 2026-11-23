#!/usr/bin/env python
"""Master switch for all MSSA-Rut experiments.

  python run_all.py                       # everything in configs/full.yaml
  python run_all.py --config configs/smoke.yaml   # quick end-to-end check
  python run_all.py --only E1E2,E6_ablation --seeds 0,1 --device cuda
  python run_all.py --report-only results/<run_id>
"""
import argparse
import copy
import datetime as dt
import json
import os
import platform
import sys
import time

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'src'))


def deep_update(a, b):
    for k, v in b.items():
        if isinstance(v, dict) and isinstance(a.get(k), dict):
            deep_update(a[k], v)
        else:
            a[k] = v
    return a


def load_cfg(path):
    with open(path) as f:
        c = yaml.safe_load(f)
    if 'base' in c:
        base = load_cfg(os.path.join(os.path.dirname(path), c.pop('base')))
        c = deep_update(base, c)
    return c


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--config', default=os.path.join(HERE, 'configs', 'full.yaml'))
    ap.add_argument('--only', default=None, help='comma list of experiments to run (overrides config)')
    ap.add_argument('--seeds', default=None)
    ap.add_argument('--device', default=None)
    ap.add_argument('--out', default=None)
    ap.add_argument('--report-only', default=None)
    ap.add_argument('--merge', nargs='+', default=None, help='merge several run directories into --out')
    ap.add_argument('--threads', type=int, default=None, help='torch/BLAS threads per process')
    args = ap.parse_args()

    if args.threads:
        for v in ('OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'OPENBLAS_NUM_THREADS'):
            os.environ[v] = str(args.threads)
        try:
            import torch
            torch.set_num_threads(args.threads)
        except ImportError:
            pass

    from rut_mssa import report
    if args.report_only:
        report.make_report(args.report_only)
        return
    if args.merge:
        report.merge_runs(args.merge, args.out)
        cfg_used = None
        for d in args.merge:
            pth = os.path.join(d, 'config_used.yaml')
            if os.path.exists(pth):
                with open(pth) as fh:
                    cfg_used = yaml.safe_load(fh)
                break
        if cfg_used is not None:
            from rut_mssa import posthoc
            posthoc.run_posthoc(args.out, cfg_used)
        report.make_report(args.out)
        print('merged report:', os.path.join(args.out, 'REPORT.md'))
        return

    cfg = load_cfg(args.config)
    if args.only:
        cfg['experiments']['run'] = args.only.split(',')
    if args.seeds:
        cfg['seeds'] = [int(s) for s in args.seeds.split(',')]
    if args.device:
        cfg['device'] = args.device
    cfg['data_dir'] = os.path.join(HERE, cfg['data_dir']) if not os.path.isabs(cfg['data_dir']) else cfg['data_dir']
    run_id = dt.datetime.now().strftime('%Y%m%d_%H%M%S') + '_' + os.path.splitext(os.path.basename(args.config))[0]
    out = args.out or os.path.join(HERE, cfg.get('out_root', 'results'), run_id)
    os.makedirs(os.path.join(out, 'pred'), exist_ok=True)
    logf = open(os.path.join(out, 'log.txt'), 'a')

    def log(msg):
        line = f'[{dt.datetime.now().strftime("%H:%M:%S")}] {msg}'
        print(line, flush=True)
        logf.write(line + '\n')
        logf.flush()

    try:
        import torch
        tv = torch.__version__
    except ImportError:
        tv = None
    with open(os.path.join(out, 'config_used.yaml'), 'w') as f:
        yaml.safe_dump(cfg, f, sort_keys=False, allow_unicode=True)
    with open(os.path.join(out, 'environment.json'), 'w') as f:
        json.dump({'python': sys.version, 'platform': platform.platform(), 'torch': tv}, f, indent=1)
    log(f'run {run_id} -> {out}; torch={tv}')

    from rut_mssa import experiments as ex
    ctx = ex.Ctx(cfg, out, log)
    smoke_folds = cfg['experiments'].get('smoke_max_folds')
    if smoke_folds:
        _orig = ex.folds
        ex.folds = lambda kind, S: _orig(kind, S)[:smoke_folds]
    if tv is None:
        log('WARNING: PyTorch not installed -> MSSA, LSTM and PatchTST are skipped; numpy baselines still run.')
        for k in ('E1E2', 'E3'):
            cfg['experiments'][k]['models'] = [m for m in cfg['experiments'][k]['models']
                                               if not (m.startswith('mssa') or m in ('lstm', 'patchtst'))]
    t0 = time.time()
    plan = cfg['experiments']['run']
    for e in plan:
        log(f'===== {e} =====')
        if tv is None and e in ('E0', 'E5', 'E6_ablation'):
            log(f'skip {e} (needs PyTorch)')
            continue
        try:
            if e == 'E0':
                ex.exp_E0(ctx)
            elif e == 'E1E2':
                ex.exp_main(ctx, 'manuscript', 'E1E2')
            elif e == 'E3':
                ex.exp_main(ctx, 'leave_class_out', 'E3')
            elif e == 'E5':
                ex.exp_E5(ctx)
            elif e == 'E6_ablation':
                ex.exp_ablation(ctx)
            else:
                log(f'unknown experiment {e}')
        except Exception as err:
            import traceback
            log(f'!! experiment {e} crashed: {err}\n{traceback.format_exc()}')
    log(f'all done in {(time.time() - t0) / 60:.1f} min; building report')
    try:
        if len(cfg['seeds']) > 1:   # single-seed jobs (parallel runs) are ensembled at merge time
            from rut_mssa import posthoc
            posthoc.run_posthoc(out, cfg, log)
    except Exception as err:
        log(f'!! posthoc ensembles failed: {err}')
    report.make_report(out)
    log('report written: ' + os.path.join(out, 'REPORT.md'))


if __name__ == '__main__':
    main()
