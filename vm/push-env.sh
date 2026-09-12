#!/bin/bash
# Push secrets to the VM. Not part of deploy.sh on purpose: run this once, or
# whenever a credential actually rotates, so routine deploys don't re-push
# secrets or clobber the VM-only PROXY_BASE_URL override below.
set -euo pipefail
cd "$(dirname "$0")"
. ./config.sh

echo "==> Pushing vertex-proxy/.env (as-is)"
rsync -avz "$LOCAL_ROOT/vertex-proxy/.env" "$VM_HOST:$PROXY_DIR/.env"

echo "==> Pushing swarm/.env (PROXY_BASE_URL rewritten to the co-located proxy)"
# Records run inside docker containers on their own bridge network, where
# 127.0.0.1 means the container itself, not the VM — so this has to be the
# docker0 bridge gateway IP, not localhost. The proxy binds 0.0.0.0 to be
# reachable there; it's still not internet-exposed (no firewall rule opens
# $PROXY_PORT to 0.0.0.0/0, only to the internal VPC range, and it's behind
# PROXY_API_KEY regardless).
DOCKER_GATEWAY=$(ssh "$VM_HOST" "docker network inspect bridge --format '{{(index .IPAM.Config 0).Gateway}}'")
sed "s|^PROXY_BASE_URL=.*|PROXY_BASE_URL=http://${DOCKER_GATEWAY}:${PROXY_PORT}/v1|" \
  "$LOCAL_ROOT/swarm/.env" | ssh "$VM_HOST" "cat > $SWARM_DIR/.env"

ssh "$VM_HOST" "chmod 600 $PROXY_DIR/.env $SWARM_DIR/.env"

echo "==> Done. Remote swarm/.env now points at the on-VM proxy, not Render."
