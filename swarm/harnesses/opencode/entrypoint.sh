#!/bin/sh
# This harness's entire CLI invocation lives here, not on the host — mounts are
# fixed by convention (see ../../spawn_batch.py): /reference/DESIGN_DOC.md,
# /trajectory.json, /prompt.md read-only; /output writable. SWARM_MODEL,
# PROXY_API_KEY, PROXY_BASE_URL come in as env vars.
set -e
PROMPT="$(cat /prompt.md)"

# The message positional must come before -f <file> — opencode's arg parser
# swallows it into -f's file list otherwise (found the hard way).
exec opencode run --dir /reference --model "$SWARM_MODEL" --auto "$PROMPT" -f /trajectory.json
