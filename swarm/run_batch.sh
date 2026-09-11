#!/bin/sh
# Draw a batch and run it.  ./run_batch.sh <experiment-tag> [count]
set -e
cd "$(dirname "$0")"
TAG="${1:?usage: ./run.sh <experiment-tag> [count]}"
python3 sample_batch.py -n "${2:-30}" --min-chars 500 --max-chars 20000 --latin-only
SWARM_EXPERIMENT="$TAG" python3 spawn_batch.py "$(ls -t batches/batch-*.jsonl | head -1)" output/
