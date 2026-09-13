# VM workflow

Runs the vertex-proxy and a braincode-swarm discovery run on `braincode-machine`
(GCE, `us-central1-c`), driven from this laptop. No git on the VM, no git
credentials sent anywhere — code is pushed with plain `rsync` over SSH.

## One-time setup

```
cp vm/config.local.sh.example vm/config.local.sh   # fill in your VM/project details (gitignored)
./vm/bootstrap.sh   # installs docker/rsync/tmux/venv, grows the disk, adds the systemd unit
./vm/deploy.sh --data   # first sync: code + the ~1.5GB data/ corpus
./vm/push-env.sh    # pushes vertex-proxy/.env and a VM-specific swarm/.env
./vm/restart-proxy.sh
```

## Day to day

```
./vm/deploy.sh              # push local code edits (fast, no data/ resync)
./vm/run-task.sh <tag> [count] [--restartable] [--task NAME] [--harness NAME] [--batch PATH]
./vm/pull-results.sh        # bring output/ and failures/ back to this laptop
./vm/watch-results.sh       # live-mirror the 1000 most-recent records *per
                            # namespace* into vm/live-output for the
                            # visualizer, bounded so it never grows unbounded
                            # on this laptop
```

## Notes

- **Every run lives under its own namespace** (`output/<experiment>/`,
  `failures/<experiment>/`, keyed by `SWARM_EXPERIMENT`, `default` if unset —
  see `swarm/ADVANCED.md`). There's no separate "rerun" mechanism: pass
  `--batch` with a new `<tag>` to `run-task.sh` to re-translate the exact same
  records under a fresh namespace, e.g. to compare a spec revision's effect on
  a fixed set of examples. `watch-results.sh` and the visualizer both
  understand this — the visualizer shows a namespace picker when a folder
  holds more than one.
- **All machine-specific values (VM name/zone/GCP project, remote paths) live
  in `vm/config.local.sh`, which is gitignored.** `config.sh` itself is
  generic and committed; it errors out with a clear message if
  `config.local.sh` is missing. This repo is shared with collaborators who
  have no reason to see (or need) any particular VM/project's identity.
- The proxy binds `0.0.0.0:8000` on the VM (not just `127.0.0.1`) — required
  so docker's bridge network can reach it (a container's own `127.0.0.1` is
  itself, not the host). Not internet-exposed: no firewall rule opens the
  port to `0.0.0.0/0`, and it's gated by `PROXY_API_KEY` regardless.
  `swarm/.env` on the VM points `PROXY_BASE_URL` at the docker0 gateway IP,
  not at `127.0.0.1` and not at the Render deployment.
- `push-env.sh` is separate from `deploy.sh` on purpose: routine deploys never
  touch secrets or the VM-only `PROXY_BASE_URL` override.
- The boot disk was resized 10GB -> 500GB (pd-balanced) to hold a full run's
  output plus Docker images without running out of room; resizable further,
  live, any time.
- `run-task.sh` runs inside `tmux` on the VM, so it keeps going whether or
  not this laptop is open or connected. That alone does **not** survive a VM
  reboot (tmux's server dies with the VM) — pass `--restartable` to also
  install a systemd unit that re-invokes the same batch file on boot;
  `spawn_batch.py`'s own startup scan skips every already-succeeded hash
  regardless of what invokes it, so a restart just resumes in place. Tested
  by actually rebooting `braincode-machine` mid-run: `discovery-run` was back
  and dispatching real work within ~30s of boot, no data lost. After a
  restart, though, monitoring shifts from `tmux attach`/`has-session` (dead —
  its server never comes back on its own) to `systemctl status <unit>` /
  `journalctl -u <unit> -f`, which the script prints when `--restartable` is
  used.
- `run-task.sh` is task/harness-agnostic — `SWARM_TASK`/`SWARM_HARNESS`
  already come from `swarm/.env` (or `--task`/`--harness` to override for one
  run) since `sample_batch.py`/`spawn_batch.py` only ever read them as env
  vars. The tmux session name and systemd unit name are both derived from the
  experiment tag, so two different tags (different tasks, or two experiments
  on the same task) can run side by side without colliding.
- `watch-results.sh` deliberately mirrors into `vm/live-output`, never into
  `swarm/output` — the latter can hold your own unrelated local corpus, and
  this script prunes anything outside its recent window.
- **A VM restart can change its external IP**, breaking SSH until you refresh
  it. `braincode-machine` has an *ephemeral* external IP (the default,
  cheaper than a reserved/static one), and GCE is free to hand out a new one
  on every stop/start cycle — internal IP stays fixed, only the external one
  moves. Confirmed on this VM: a restart changed it from `34.9.123.203` to
  `34.44.111.214`, and every plain `ssh`/`rsync` call in `vm/` (via
  `config.sh`'s `VM_HOST` alias) started timing out until re-running
  `gcloud compute config-ssh` picked up the new address. This isn't specific
  to running Vertex AI workloads or to this machine type — it's generic GCE
  ephemeral-IP behavior, so it'll recur on *any* restart (planned or not)
  unless the VM is given a reserved static IP, which we've deliberately not
  done (see the tradeoffs below). If a script suddenly can't reach the VM,
  check this before assuming something's actually broken:
  `gcloud compute instances describe braincode-machine --zone=us-central1-c
  --format="value(networkInterfaces[0].accessConfigs[0].natIP)"` — if it
  doesn't match what's in `~/.ssh/config`, re-run `gcloud compute
  config-ssh`.
- **Running two experiments concurrently can exhaust open-file descriptors.**
  The image's default `ulimit -n` is 1024, and each running experiment's
  docker/subprocess fds count against it independently per shell/service —
  found when `discovery-run` (the systemd-managed main run) died mid-record
  with `OSError: [Errno 24] Too many open files` while an unrelated 18-record
  test batch was running alongside it in tmux. `run-task.sh` now raises this
  to 65536 for both the tmux path (`ulimit -n` before `spawn_batch.py`) and
  the `--restartable` systemd unit (`LimitNOFILE=`); an already-installed unit
  from before this fix needs `LimitNOFILE=65536` added under its `[Service]`
  section by hand (then `daemon-reload` + restart) to pick it up.
- We looked at dropping the external IP entirely (SSH via IAP tunnel +
  Private Google Access for reaching Vertex AI) to sidestep the above, and
  deliberately didn't: none of the prerequisites exist yet (Private Google
  Access is off on the subnet, no Cloud NAT, no IAP firewall rule), general
  internet access (`docker pull`, `npm`, `apt`) would need Cloud NAT to keep
  working at all — a real ongoing cost, not a one-time setup — and every
  script here would need reworking to tunnel through IAP instead of
  connecting directly. Revisit only if the IP-change friction becomes a real
  problem, not preemptively.
