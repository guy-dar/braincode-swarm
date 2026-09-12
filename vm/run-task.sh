#!/bin/bash
# Kick off a swarm run on the VM, detached in tmux so it keeps running after
# you disconnect (and regardless of whether this laptop is open). Task- and
# harness-agnostic: sample_batch.py/spawn_batch.py already take those from
# SWARM_TASK/SWARM_HARNESS (default discovery/pi, see ADVANCED.md), this
# script just needs to not collide when more than one tag is running at once.
#
#   ./vm/run-task.sh <experiment-tag> [count] [--restartable] [--task NAME] [--harness NAME]
#
# [count] defaults to a large number so sample_batch.py just draws every
# remaining eligible record (it caps to whatever's available and prints a
# NOTE if it came up short). --task/--harness override SWARM_TASK/
# SWARM_HARNESS for this run only; omit either to use whatever swarm/.env
# already has.
#
# --restartable installs (and enables, but does not start) a systemd unit
# that re-invokes this exact batch file on boot. It's not what makes the run
# itself resumable — spawn_batch.py's own startup scan already skips every
# hash with a metadata.json, on any invocation — it's what makes sure
# *something* re-launches it after a reboot, since a bare tmux session dies
# with the VM. Safe to add after the fact: re-run this command with the same
# tag and --restartable, and it'll pick up wherever the current batch is.
set -euo pipefail
cd "$(dirname "$0")"
. ./config.sh

usage() { echo "usage: ./vm/run-task.sh <experiment-tag> [count] [--restartable] [--task NAME] [--harness NAME] [--data PATH] [--min-chars N] [--max-chars N] [--no-latin-only]" >&2; exit 1; }

[ $# -ge 1 ] || usage
TAG="$1"; shift
COUNT=100000
RESTARTABLE=0
TASK=""
HARNESS=""
DATA=""
# Tuned for the sharechat/discovery corpus (short-ish, Latin-script chat
# transcripts) — not a universal contract. A source with a different shape
# (e.g. long multi-turn tool-use trajectories) needs its own thresholds here
# rather than silently losing records to defaults that don't fit it.
MIN_CHARS=500
MAX_CHARS=20000
LATIN_ONLY=1
if [ $# -gt 0 ] && [[ "$1" != --* ]]; then COUNT="$1"; shift; fi
while [ $# -gt 0 ]; do
  case "$1" in
    --restartable) RESTARTABLE=1; shift ;;
    --task) TASK="${2:?--task needs a value}"; shift 2 ;;
    --harness) HARNESS="${2:?--harness needs a value}"; shift 2 ;;
    # Points sample_batch.py at a different data source (default: swarm/data/)
    # — mainly for testing against a small isolated file instead of the
    # shared corpus, so a test run can't draw a record another run is
    # already mid-flight on.
    --data) DATA="${2:?--data needs a value}"; shift 2 ;;
    --min-chars) MIN_CHARS="${2:?--min-chars needs a value}"; shift 2 ;;
    --max-chars) MAX_CHARS="${2:?--max-chars needs a value}"; shift 2 ;;
    --no-latin-only) LATIN_ONLY=0; shift ;;
    *) usage ;;
  esac
done

# tmux session names and systemd unit names both need to be filesystem/
# shell-safe; two different tags must not collide, which is what lets two
# different tasks (or two experiments on the same task) run side by side.
# printf, not echo: echo's trailing newline isn't in the allowed set either,
# so tr would turn it into a trailing '-' (found by actually running this).
SESSION=$(printf '%s' "$TAG" | tr -c 'A-Za-z0-9._-' '-')
UNIT_NAME="swarm-$SESSION"
LOG_FILE="$SESSION.log"

if ssh "$VM_HOST" "tmux has-session -t $SESSION 2>/dev/null"; then
  echo "A '$SESSION' tmux session is already running on the VM. Attach with:"
  echo "  ssh $VM_HOST -t 'tmux attach -t $SESSION'"
  exit 1
fi

# Unquoted: task/harness names are plain identifiers (see ADVANCED.md), and
# this same string gets reused verbatim in a systemd Environment= line below,
# which does not use shell quoting rules — a quoted value there would become
# part of the literal env var instead of being stripped.
ENV_PREFIX=""
[ -n "$TASK" ] && ENV_PREFIX="SWARM_TASK=$TASK $ENV_PREFIX"
[ -n "$HARNESS" ] && ENV_PREFIX="SWARM_HARNESS=$HARNESS $ENV_PREFIX"

DATA_ARG=""
[ -n "$DATA" ] && DATA_ARG="--data $DATA"

LATIN_ARG=""
[ "$LATIN_ONLY" = "1" ] && LATIN_ARG="--latin-only"

echo "==> Drawing the batch"
ssh "$VM_HOST" "cd $SWARM_DIR && source .venv/bin/activate && $ENV_PREFIX python3 sample_batch.py -n $COUNT --min-chars $MIN_CHARS --max-chars $MAX_CHARS $LATIN_ARG $DATA_ARG"
BATCH_FILE=$(ssh "$VM_HOST" "cd $SWARM_DIR && ls -t batches/batch-*.jsonl | head -1")
echo "    -> $BATCH_FILE"

# The default open-file limit (1024 on this image) is per-shell/per-service,
# not shared, but two concurrent runs (or one run plus a lot of concurrency)
# each opening docker/subprocess fds can still hit it independently — found by
# running a second experiment alongside a long discovery-run tail and watching
# the latter die mid-record with "OSError: Too many open files".
ssh "$VM_HOST" "cd $SWARM_DIR && tmux new-session -d -s $SESSION \
  \"ulimit -n 65536; source .venv/bin/activate && $ENV_PREFIX SWARM_EXPERIMENT='$TAG' python3 spawn_batch.py $BATCH_FILE output/ 2>&1 | tee -a $LOG_FILE; echo '--- run exited: '\\\$? >> $LOG_FILE\""

if [ "$RESTARTABLE" = "1" ]; then
  echo "==> Installing restart-survival unit (enabled, not started — tmux is already running it)"
  REMOTE_USER=$(ssh "$VM_HOST" whoami)
  ssh "$VM_HOST" bash -s <<REMOTE
sudo tee /etc/systemd/system/$UNIT_NAME.service > /dev/null <<UNIT
[Unit]
Description=braincode-swarm run: $TAG
After=network.target docker.service vertex-proxy.service
Requires=docker.service

[Service]
Type=oneshot
User=$REMOTE_USER
WorkingDirectory=$SWARM_DIR
Environment=$ENV_PREFIX SWARM_EXPERIMENT=$TAG
# Raised from systemd's low default (1024 on this image): a second experiment
# running alongside this one's docker/subprocess fds hit that ceiling and
# crashed this unit mid-run with "OSError: Too many open files".
LimitNOFILE=65536
ExecStart=$SWARM_DIR/.venv/bin/python3 spawn_batch.py $BATCH_FILE output/

[Install]
WantedBy=multi-user.target
UNIT
sudo systemctl daemon-reload
sudo systemctl enable $UNIT_NAME.service
REMOTE
fi

cat <<EOF
Started. This keeps running on the VM independent of this laptop.

  Watch live:     ssh $VM_HOST -t 'tmux attach -t $SESSION'   (detach: Ctrl-b d)
  Tail the log:   ssh $VM_HOST 'tail -f $SWARM_DIR/$LOG_FILE'
  Check if done:  ssh $VM_HOST 'tmux has-session -t $SESSION' (exits nonzero once finished)
  Pull results:   ./vm/pull-results.sh
EOF
if [ "$RESTARTABLE" = "1" ]; then
  cat <<EOF
  Restart-safe:   yes — a VM reboot re-launches this exact batch (already-done records are skipped)

  The commands above only apply to THIS tmux-launched run. If the VM ever
  restarts, systemd takes over directly (no tmux involved — its server dies
  with the VM, so 'tmux attach'/'has-session' will show nothing even though
  the run is fine) — after a restart, use instead:

  Watch live:     ssh $VM_HOST 'journalctl -u $UNIT_NAME -f'
  Check status:   ssh $VM_HOST 'systemctl status $UNIT_NAME'
EOF
fi
