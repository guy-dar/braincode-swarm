#!/bin/bash
# Mirror only the N most-recently-created records from the VM's output/ (and
# failures/), pruning anything older as new ones land. A rolling window for
# "what's happening right now" in a live run, not a full local copy — a full
# run's output/ can run into the tens of GB, which doesn't fit on a
# space-constrained laptop.
#
# The visualizer (visualizer/index.html) is pure client-side
# (File System Access API, no server, nothing over the network by design —
# see visualizer/README.md), so it needs an actual local folder; this keeps
# that folder small and fresh instead of a full mirror.
#
#   ./vm/watch-results.sh [record-count] [interval-seconds]
#   defaults: 1000 records (~36MB at this corpus's ~36KB/record average), 5s
#   Ctrl-C to stop.
set -euo pipefail
cd "$(dirname "$0")"
. ./config.sh

N="${1:-1000}"
INTERVAL="${2:-5}"
# Deliberately NOT swarm/output — that directory holds your
# own prior local corpus, unrelated to the VM run, and this function prunes
# anything not in its recent window. A dedicated empty folder means the prune
# can never touch data it didn't put there itself.
LOCAL_OUT="$LOCAL_ROOT/vm/live-output"
LOCAL_FAIL="$LOCAL_ROOT/vm/live-failures"
mkdir -p "$LOCAL_OUT" "$LOCAL_FAIL"

sync_recent() {
  local remote_dir="$1" local_dir="$2"
  local recent
  recent=$(ssh "$VM_HOST" "cd $remote_dir 2>/dev/null && ls -t | head -n $N" || true)
  [ -z "$recent" ] && return 0
  # A bare name in --files-from is one opaque item to rsync (it creates the
  # directory but does not descend into it) — the trailing slash is what
  # makes it recurse and actually copy each record's files.
  sed 's|$|/|' <<< "$recent" | rsync -az --files-from=- "$VM_HOST:$remote_dir/" "$local_dir/" 2>/dev/null || true
  # Prune local entries that fell out of the recent window.
  local name
  for d in "$local_dir"/*/; do
    [ -e "$d" ] || continue
    name=$(basename "$d")
    if ! grep -qxF "$name" <<< "$recent"; then
      rm -rf "$d"
    fi
  done
}

echo "Mirroring the $N most recent records from $VM_HOST -> $LOCAL_OUT every ${INTERVAL}s. Ctrl-C to stop."
echo "Open visualizer/index.html and pick vm/live-output (or vm/live-failures)."

while true; do
  sync_recent "$SWARM_DIR/output" "$LOCAL_OUT"
  sync_recent "$SWARM_DIR/failures" "$LOCAL_FAIL"
  sleep "$INTERVAL"
done
