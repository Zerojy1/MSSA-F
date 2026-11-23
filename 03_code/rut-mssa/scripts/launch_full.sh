#!/usr/bin/env bash
set -euo pipefail
source /home/zyl105/Zerojy/use-zerojy.sh
cd /home/zyl105/Zerojy/projects/rut-mssa-20261119
export PATH=/home/zyl105/Zerojy/environments/rut-mssa-20261119/bin:$PATH
export OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1 MPLBACKEND=Agg
python -u run_all.py --config configs/smoke_remaining.yaml --threads 1 --out results/smoke_remaining > results/smoke_remaining.stdout 2>&1
python - <<'PY'
from pathlib import Path
import pandas as pd
import numpy as np
for run in ['smoke','smoke_remaining']:
    p=Path('results')/run
    text=(p/'log.txt').read_text()
    assert 'report written:' in text, 'Smoke report did not complete'
    assert '!!' not in text and 'non-finite loss' not in text, 'Smoke run failed'
    assert not (p/'failures.csv').exists(), 'Smoke model failures'
    for f in p.glob('main_*.csv'):
        df=pd.read_csv(f)
        assert np.isfinite(df.loc[df.n>0,['RMSE','MAE']]).all().all(), str(f)
assert len(pd.read_csv('results/smoke_remaining/E5_hidden_material.csv'))>0
assert pd.read_csv('results/smoke_remaining/main_E6_ablation.csv').model.nunique()==7
print('Extended smoke validation passed',flush=True)
PY
exec python -u scripts/supervise_full.py
