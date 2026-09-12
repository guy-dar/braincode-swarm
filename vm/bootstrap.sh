#!/bin/bash
# One-time VM setup. Safe to re-run (idempotent). Run from this laptop:
#   ./vm/bootstrap.sh
set -euo pipefail
cd "$(dirname "$0")"
. ./config.sh

echo "==> Registering plain SSH alias for GCE instances (gcloud compute config-ssh)"
gcloud compute config-ssh --quiet

echo "==> Resizing boot disk to 60GB (no-op if already >= 60GB)"
CURRENT_SIZE=$(gcloud compute disks describe "$VM_NAME" --zone="$VM_ZONE" --format="value(sizeGb)")
if [ "$CURRENT_SIZE" -lt 60 ]; then
  gcloud compute disks resize "$VM_NAME" --zone="$VM_ZONE" --size=60GB --quiet
else
  echo "    already ${CURRENT_SIZE}GB, skipping"
fi

echo "==> Growing filesystem + installing packages on $VM_HOST"
ssh "$VM_HOST" bash -s <<'REMOTE'
set -euo pipefail

sudo apt-get update -qq
sudo apt-get install -y -qq rsync tmux python3-venv python3-pip cloud-guest-utils

# Grow the root partition/filesystem to fill the resized disk, if needed.
ROOT_DEV=$(findmnt -no SOURCE /)
DISK=$(lsblk -no PKNAME "$ROOT_DEV")
PART_NUM=$(echo "$ROOT_DEV" | grep -oE '[0-9]+$')
sudo growpart "/dev/$DISK" "$PART_NUM" || true
sudo resize2fs "$ROOT_DEV" || true

if ! command -v docker >/dev/null; then
  curl -fsSL https://get.docker.com | sudo sh
fi
sudo usermod -aG docker "$(whoami)"
sudo systemctl enable --now docker

mkdir -p ~/vertex-proxy ~/swarm
echo "bootstrap done"
REMOTE

echo "==> Installing systemd unit for the proxy"
REMOTE_USER=$(ssh "$VM_HOST" whoami)
ssh "$VM_HOST" bash -s <<REMOTE
sudo tee /etc/systemd/system/vertex-proxy.service > /dev/null <<UNIT
[Unit]
Description=Vertex LLM proxy (litellm)
After=network.target

[Service]
Type=simple
User=$REMOTE_USER
WorkingDirectory=$PROXY_DIR
# --workers: a single uvicorn process became the actual bottleneck at
# SWARM_CONCURRENCY=512 (connection errors + sub-linear throughput, while VM
# CPU/RAM stayed nearly idle and Vertex-side errors stayed flat) — multiple
# worker processes let concurrent requests actually run in parallel instead
# of queueing on one event loop.
ExecStart=$PROXY_DIR/.venv/bin/uvicorn main:app --host 0.0.0.0 --port $PROXY_PORT --workers 8
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
UNIT
sudo systemctl daemon-reload
REMOTE

cat <<EOF

Bootstrap complete. Next steps:
  1. ./vm/deploy.sh       # push code
  2. ./vm/push-env.sh     # push secrets (one-time, or whenever they rotate)
  3. ./vm/restart-proxy.sh
  4. ./vm/run-task.sh <experiment-tag> [count]

Note: this session's docker group membership needs a fresh login to take
effect. Scripts here use one-shot 'ssh host cmd' invocations, which are each
a fresh login, so this is already handled.
EOF
