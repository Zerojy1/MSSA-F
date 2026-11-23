#!/usr/bin/env bash
# Run every experiment x seed as an independent process, then merge into one report.
# Usage: bash scripts/run_parallel.sh [MAX_JOBS] [CONFIG]
set -euo pipefail
cd "$(dirname "$0")/.."
MAX_JOBS=${1:-8}
CONFIG=${2:-configs/full.yaml}
STAMP=$(date +%Y%m%d_%H%M%S)
ROOT=results/parallel_${STAMP}
mkdir -p "$ROOT"
SEEDS=$(python -c "import yaml,sys;c=yaml.safe_load(open('$CONFIG'));print(' '.join(map(str,c.get('seeds',[0]))))")
EXPS=$(python -c "import yaml;c=yaml.safe_load(open('$CONFIG'));print(' '.join(c['experiments']['run']))")
jobs_running() { jobs -rp | wc -l; }
for e in $EXPS; do
  for s in $SEEDS; do
    while [ "$(jobs_running)" -ge "$MAX_JOBS" ]; do sleep 5; done
    echo "launch $e seed $s"
    python run_all.py --config "$CONFIG" --only "$e" --seeds "$s" --threads 1 --out "$ROOT/${e}_s${s}" \
      > "$ROOT/${e}_s${s}.stdout" 2>&1 &
  done
done
wait
python run_all.py --merge $(ls -d "$ROOT"/*/) --out "$ROOT/merged"
echo "DONE -> $ROOT/merged/REPORT.md"
