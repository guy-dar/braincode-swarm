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
#   defaults: 1000 records *per namespace* (~36MB each at this corpus's
#   ~36KB/record average), 5s. Ctrl-C to stop.
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

# Every run lives under output/<namespace>/ and failures/<namespace>/ (see
# utils.failures_dir / spawn_batch.py) -- not a special "live run" shape, just
# the ordinary one, so this mirrors each namespace's own recent window rather
# than treating $SWARM_DIR/output's top level as records directly.
sync_one_namespace() {
  local remote_dir="$1" local_dir="$2"
  mkdir -p "$local_dir"
  local recent
  # -n: this runs inside the `while read` loop below (via sync_recent), whose
  # stdin is the namespace list piped in through <<<. A plain `ssh` with no
  # stdin of its own would otherwise consume the rest of that list, so every
  # namespace after the first would silently vanish from the loop -- found by
  # tracing exactly that (only the first namespace ever got mirrored).
  recent=$(ssh -n "$VM_HOST" "cd $remote_dir 2>/dev/null && ls -t | head -n $N" || true)
  # A sibling cache file (not inside local_dir, so it's never mistaken for a
  # record and never touched by the prune below) holding the exact listing
  # from the previous round. When it's byte-identical to this round's, that's
  # a proof, not a guess, that nothing entered, left, or changed inside the
  # window -- this listing IS what determines window membership -- so rsync
  # has nothing to do and is skipped. Without this, a namespace whose run has
  # already finished (its output never changes again) still costs a full ssh
  # + rsync round-trip every single loop forever, and with several such
  # namespaces accumulating over a session, that cost is paid serially ahead
  # of whichever namespace is actually still growing -- found by watching a
  # live run's own namespace lag several rounds behind older finished ones
  # that had nothing left to sync.
  local cache_file="${local_dir%/}.recent-cache"
  local last_recent=""
  [ -f "$cache_file" ] && last_recent=$(cat "$cache_file")
  if [ -n "$recent" ] && [ "$recent" != "$last_recent" ]; then
    # A bare name in --files-from is one opaque item to rsync (it creates the
    # directory but does not descend into it) — the trailing slash is what
    # makes it recurse and actually copy each record's files.
    sed 's|$|/|' <<< "$recent" | rsync -az --files-from=- "$VM_HOST:$remote_dir/" "$local_dir/" 2>/dev/null || true
  fi
  printf '%s' "$recent" > "$cache_file"
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

sync_recent() {
  local remote_dir="$1" local_dir="$2"
  mkdir -p "$local_dir"
  local namespaces
  namespaces=$(ssh -n "$VM_HOST" "cd $remote_dir 2>/dev/null && ls -d */ 2>/dev/null | sed 's|/\$||'" || true)
  [ -z "$namespaces" ] && return 0
  local ns
  while IFS= read -r ns; do
    [ -n "$ns" ] || continue
    sync_one_namespace "$remote_dir/$ns" "$local_dir/$ns"
  done <<< "$namespaces"
  # Prune local namespace folders that no longer exist remotely.
  local nd nsname
  for nd in "$local_dir"/*/; do
    [ -e "$nd" ] || continue
    nsname=$(basename "$nd")
    if ! grep -qxF "$nsname" <<< "$namespaces"; then
      rm -rf "$nd" "${nd%/}.recent-cache"
    fi
  done
}

echo "Mirroring the $N most recent records per namespace from $VM_HOST -> $LOCAL_OUT every ${INTERVAL}s. Ctrl-C to stop."
echo "Open visualizer/index.html, pick vm/live-output (or vm/live-failures), then choose a namespace."

while true; do
  sync_recent "$SWARM_DIR/output" "$LOCAL_OUT"
  sync_recent "$SWARM_DIR/failures" "$LOCAL_FAIL"
  sleep "$INTERVAL"
done
