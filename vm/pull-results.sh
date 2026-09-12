#!/bin/bash
# Pull discovery-run results (and failure logs) back down to this laptop.
set -euo pipefail
cd "$(dirname "$0")"
. ./config.sh

mkdir -p "$LOCAL_ROOT/swarm/output" "$LOCAL_ROOT/swarm/failures"

echo "==> Pulling output/"
rsync -avz "$VM_HOST:$SWARM_DIR/output/" "$LOCAL_ROOT/swarm/output/"

echo "==> Pulling failures/"
rsync -avz "$VM_HOST:$SWARM_DIR/failures/" "$LOCAL_ROOT/swarm/failures/"

echo "==> Done."
