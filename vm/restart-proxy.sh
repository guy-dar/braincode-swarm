#!/bin/bash
# (Re)start the proxy systemd service on the VM and confirm it's answering.
set -euo pipefail
cd "$(dirname "$0")"
. ./config.sh

ssh "$VM_HOST" "sudo systemctl restart vertex-proxy && sleep 2 && sudo systemctl --no-pager status vertex-proxy | head -10"

echo "==> Health check (GET /v1/models)"
ssh "$VM_HOST" "curl -sf http://127.0.0.1:${PROXY_PORT}/v1/models -H \"Authorization: Bearer \$(grep ^PROXY_API_KEY= $PROXY_DIR/.env | cut -d= -f2-)\" | head -c 300; echo"
