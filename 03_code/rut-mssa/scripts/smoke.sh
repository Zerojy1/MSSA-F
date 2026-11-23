#!/usr/bin/env bash
# 5-15 min end-to-end check of every code path (run this first on the server).
set -euo pipefail
cd "$(dirname "$0")/.."
python run_all.py --config configs/smoke.yaml --out results/smoke_test
grep -c "!!" results/smoke_test/log.txt && echo "^^^ failures above, see results/smoke_test/log.txt" || echo "SMOKE TEST PASSED (no failures)"
