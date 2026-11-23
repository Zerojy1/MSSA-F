#!/usr/bin/env bash
# Sequential full run (single process). Usage: bash scripts/run_all.sh [cpu|cuda]
set -euo pipefail
cd "$(dirname "$0")/.."
python run_all.py --config configs/full.yaml --device "${1:-cpu}"
