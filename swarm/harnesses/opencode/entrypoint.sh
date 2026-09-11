#!/bin/sh
# This harness's entire CLI invocation lives here, not on the host — mounts are
# fixed by convention (see ../../spawn_batch.py): /reference/DESIGN_DOC.md,
# /trajectory.txt, /prompt.md read-only; /output writable. SWARM_MODEL,
# PROXY_API_KEY, PROXY_BASE_URL come in as env vars.
set -e
PROMPT="$(cat /prompt.md)"

# Named explicitly because config *discovery* can't be used here: opencode looks
# in its working directory, which is /reference, and that path is a read-only
# host mount holding the spec (see the Dockerfile).
export OPENCODE_CONFIG=/opt/opencode.jsonc

# The message positional must come before -f <file> — opencode's arg parser
# swallows it into -f's file list otherwise (found the hard way).
exec opencode run --dir /reference --model "$SWARM_MODEL" --auto "$PROMPT" -f /trajectory.txt
