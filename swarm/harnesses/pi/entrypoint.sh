#!/bin/sh
# This harness's entire CLI invocation lives here, not on the host — mounts are
# fixed by convention (see ../../spawn_batch.py): /reference/DESIGN_DOC.md,
# /trajectory.txt, /prompt.md read-only; /output writable. SWARM_MODEL,
# PROXY_API_KEY, PROXY_BASE_URL come in as env vars.
set -e

# Unlike opencode's config, Pi writes auth.json into its own config dir on
# every run, so it can't be read-only — build a writable one under $HOME
# (set to /tmp by the host, see spawn_batch.py) each time. baseUrl isn't a
# secret, so it's resolved here with a literal substitution; apiKey stays a
# $VAR reference, resolved by Pi itself from the environment at request time.
mkdir -p "$HOME/pi-config"
sed "s|__PROXY_BASE_URL__|$PROXY_BASE_URL|" /opt/models.template.json > "$HOME/pi-config/models.json"
export PI_CODING_AGENT_DIR="$HOME/pi-config"

PROMPT="$(cat /prompt.md)"
exec pi --print --no-session --no-context-files --approve \
  --model "$SWARM_MODEL" "@/trajectory.txt" "$PROMPT"
