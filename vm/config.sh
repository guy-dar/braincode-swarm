#!/bin/sh
# Shared config for the vm/*.sh scripts. Source this, don't run it directly.
#
# Machine-specific values (VM name/zone/project, remote paths) live in
# config.local.sh, which is gitignored -- copy config.local.sh.example to
# config.local.sh and fill in your own environment before running anything
# in vm/.

if [ ! -f ./config.local.sh ]; then
  echo "vm/config.local.sh not found. Copy vm/config.local.sh.example to" >&2
  echo "vm/config.local.sh and fill in your VM/project details." >&2
  exit 1
fi
. ./config.local.sh

# Plain SSH alias set up by `gcloud compute config-ssh` (run once, see bootstrap.sh).
VM_HOST="${VM_NAME}.${VM_ZONE}.${VM_PROJECT}"

# Callers `cd` into vm/ before sourcing this, so cwd is always vm/ here.
LOCAL_ROOT="$(cd .. && pwd)"
