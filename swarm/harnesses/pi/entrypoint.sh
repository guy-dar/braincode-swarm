#!/bin/sh
# This harness's entire CLI invocation lives here, not on the host — mounts are
# fixed by convention (see ../../spawn_batch.py): /reference/language-spec.md (+ glossary),
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
# Pi's own retry window, widened from its defaults — see settings.json for why.
# It lives in the same config dir as models.json, so it gets copied in here
# rather than mounted.
cp /opt/settings.json "$HOME/pi-config/settings.json"
export PI_CODING_AGENT_DIR="$HOME/pi-config"

PROMPT="$(cat /prompt.md)"
# Optional /attach/: every file there is attached to the first message, in
# name order, so the agent starts with it instead of spending one model turn
# per file reading it (the loop attaches the spec, retrieval context and
# formats this way). Files go through pi's @file mechanism rather than the
# prompt argument, which is capped at 128 KB per argument by the kernel.
set --
if [ -d /attach ]; then
  for f in /attach/*; do
    [ -f "$f" ] && set -- "$@" "@$f"
  done
fi
# PI_JSON=1 streams pi's JSON events on stdout instead of only the final
# reply, so the host can log each model turn and tool call as it happens.
MODE=""
[ -n "$PI_JSON" ] && MODE="--mode json"
# PI_SESSION_DIR (a writable mount) keeps the session on disk, so a later run
# with PI_RESUME=1 continues it (sending only the new prompt) instead of
# starting over: a translator killed by a proxy outage resumes where it was.
if [ -n "$PI_SESSION_DIR" ]; then
  if [ -n "$PI_RESUME" ]; then
    exec pi --print $MODE --session-dir "$PI_SESSION_DIR" --continue --no-context-files --approve \
      --model "$SWARM_MODEL" "$PROMPT"
  fi
  exec pi --print $MODE --session-dir "$PI_SESSION_DIR" --no-context-files --approve \
    --model "$SWARM_MODEL" "$@" "@/trajectory.txt" "$PROMPT"
fi
exec pi --print $MODE --no-session --no-context-files --approve \
  --model "$SWARM_MODEL" "$@" "@/trajectory.txt" "$PROMPT"
