#!/bin/sh
# Claude evaluation (direct API keys, no proxy; OpenAI stopped by the user after 18 runs per model, all failed): the 18 items shared
# with the Gemini models, 3 runs each, setup v2. Runs beside the Gemini process:
# its own RAG port; its containers (swarm-ev-<model>-...) are its own to clean up.
cd "$(dirname "$0")" || exit 1
export EVAL_RAG_PORT=8777 PYTHONIOENCODING=utf-8 PYTHONUNBUFFERED=1
../.venv/Scripts/python.exe run_eval.py translate --run main --runs 3 \
  --models claude-sonnet-5.5,claude-haiku-4.5
