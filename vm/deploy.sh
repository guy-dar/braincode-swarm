#!/bin/bash
# Push local code changes to the VM. No git, no credentials beyond your own
# SSH access — this is a plain rsync of the working tree. Safe to run as
# often as you like; only changed files transfer.
#
#   ./vm/deploy.sh            # sync both proxy and swarm code
#   ./vm/deploy.sh --data     # also (re)sync the swarm/data/ corpus (~1.5GB,
#                              # only needed once or when the dataset changes)
set -euo pipefail
cd "$(dirname "$0")"
. ./config.sh

echo "==> Syncing vertex-proxy/ -> $VM_HOST:$PROXY_DIR"
rsync -avz --delete \
  --exclude='.git' --exclude='.env' --exclude='__pycache__/' \
  --exclude='.pytest_cache/' --exclude='old_main.py' --exclude='.venv/' \
  "$LOCAL_ROOT/vertex-proxy/" "$VM_HOST:$PROXY_DIR/"

echo "==> Syncing swarm/ -> $VM_HOST:$SWARM_DIR"
EXCLUDES=(--exclude='.env' --exclude='__pycache__/' --exclude='.pytest_cache/'
          --exclude='output/' --exclude='failures/' --exclude='batches/'
          --exclude='.venv/')
if [ "${1:-}" != "--data" ]; then
  EXCLUDES+=(--exclude='data/')
fi
rsync -avz "${EXCLUDES[@]}" \
  "$LOCAL_ROOT/swarm/" "$VM_HOST:$SWARM_DIR/"

echo "==> Installing/updating Python deps"
ssh "$VM_HOST" bash -s <<REMOTE
set -e
cd $PROXY_DIR
python3 -m venv .venv 2>/dev/null || true
.venv/bin/pip install -q -r requirements.txt

cd $SWARM_DIR
python3 -m venv .venv 2>/dev/null || true
.venv/bin/pip install -q -r requirements.txt
REMOTE

echo "==> Done."
