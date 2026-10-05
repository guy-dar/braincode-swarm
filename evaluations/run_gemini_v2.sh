#!/bin/sh
# Gemini evaluation, setup v2: remaining forward runs, one back-translation per
# model and item, failure documentation, analysis. Resumable: rerun to continue.
cd "$(dirname "$0")" || exit 1
PY=../.venv/Scripts/python.exe
export SWARM_MODEL=vertex-proxy/gemini-flash PYTHONIOENCODING=utf-8 PYTHONUNBUFFERED=1
MODELS=gemini-flash-3.7,gemini-flash-high-3.7
$PY run_eval.py translate --run main --runs 3 --models $MODELS \
  && $PY run_eval.py backtranslate --run main --models $MODELS \
  && $PY run_eval.py document --run main \
  && $PY analyze.py --run main
