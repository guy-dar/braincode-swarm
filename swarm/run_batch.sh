#!/bin/sh
# Draw a batch and run it.  ./run_batch.sh <experiment-tag> [count]
set -e
cd "$(dirname "$0")"
TAG="${1:?usage: ./run_batch.sh <experiment-tag> [count]}"
# On Windows `python3` is often the Microsoft Store stub, which exists but doesn't run.
PY=python3
"$PY" -c "" 2>/dev/null || PY=python
"$PY" sample_batch.py -n "${2:-30}" --min-chars 500 --max-chars 20000 --latin-only
SWARM_EXPERIMENT="$TAG" "$PY" spawn_batch.py "$(ls -t batches/batch-*.jsonl | head -1)" output/
