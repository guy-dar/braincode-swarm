# Advanced

Everything here is optional context for extending, configuring, or debugging the
pipeline — not needed for normal use (see `README.md` for that).

## Config

| Var | Default | Meaning |
|---|---|---|
| `PROXY_API_KEY` | *(required)* | — |
| `PROXY_BASE_URL` | vertex-proxy's URL | model backend |
| `SWARM_HARNESS` | `pi` | picks `harnesses/$SWARM_HARNESS/` |
| `SWARM_TASK` | `discovery` | picks `tasks/$SWARM_TASK.md` |
| `SWARM_MODEL` | `vertex-proxy/gemini-3.5-flash` | passed to the harness |
| `SWARM_CONCURRENCY` | `16` | concurrent `docker run`s |
| `SWARM_STAGGER` | `0` | each worker waits a random `0..N` seconds before starting |
| `SWARM_TIMEOUT` | `1200` | seconds before a record's container is killed |
| `SWARM_EXPERIMENT` | *(unset, → `default`)* | recorded in `metadata.json`; also the namespace subfolder every run's output/failures land under (see "Output" below) |

A batch file is just a list of records, and nothing anywhere depends on how long
it is: `spawn_batch.py` reads every line and feeds a fixed-size worker pool, so
30 records and 300 differ only in how long the run takes. Sizes on disk already
range from 30 to 100. Size the batch to what you want to inspect together — one
spec version's worth of output, one experiment tag — rather than to a fixed
number.

`SWARM_STAGGER` is off by default and probably not worth turning on. It was added
on the theory that the pool stays phase-locked — every worker starts at the same
instant, and the `pi` harness's retry backoff has no jitter
(`harnesses/pi/settings.json`: plain `baseDelayMs * 2**(attempt-1)`) — so all N
workers would retry a proxy outage in the same moment and knock the restarting
instance over again. **That did not hold up:** the proxy usually survives the
returning traffic, so staggering only adds latency to every run. The knob remains
for experimenting.

Failure rates here track the proxy's health over time far more than they track
concurrency. One session ran, in order, concurrency 8 → 32 → 24 → 16
and saw failure rates of 0% → 9% → 77% → 53%: monotonic in *when* the run
happened, not in how wide it was. Before tuning `SWARM_CONCURRENCY`, check
whether the proxy is answering at all (`curl $PROXY_BASE_URL/models`); a run that
fails at 16 may succeed at 32 an hour later. The failures are all origin-side —
`503`, `520`, `429`, and mid-stream `Stream ended without finish_reason` — none
of which any client-side setting prevents.

## Output

Every run lives under its own **namespace** subfolder, keyed by
`SWARM_EXPERIMENT` (`default` if unset) — not a special mode, just the
ordinary way any two runs coexist. The out-dir you pass on the command line
(conventionally `output/`) is the *base*; `spawn_batch.py` writes into
`<base>/<namespace>/` itself, and its own resume/dedup scan
(`utils.scan_existing_output`) only looks inside that one namespace. So
replaying the exact same batch file under a new `SWARM_EXPERIMENT` — the way
to re-run the same examples against a later spec revision — re-translates
every record instead of finding them all already-done, and never touches any
other namespace's output. `sample_batch.py`'s own "already spoken for" check
(see its docstring) is the one place that still looks *across* every
namespace, since sampling a fresh batch should avoid content that's done
anywhere, not just in one namespace.

**If you ever reorganize where a corpus's output lives (as the move to
namespaces itself was), update every existing `--restartable` unit's
`SWARM_EXPERIMENT` to match, or don't leave any enabled.** Found in
production: two units created before namespacing existed kept their original
tag after their corpus was migrated into `default`, so on the next reboot
each landed in a namespace that was empty from its own point of view and
re-translated its entire corpus from scratch, unattended, before anyone
noticed. There's no way to tell that apart from a genuine deliberate rerun by
looking at the data alone — replaying a batch under a namespace where that
work is already done elsewhere is exactly what namespacing is *for* — so this
isn't something the pipeline can safely refuse on your behalf; it's on
whoever does the reorganizing to check `systemctl list-unit-files
'swarm-*'` (and any equivalent) against it.

Each record's folder is named `<hash6>-<slug>`: the first 6 hex chars of a
sha256 of the record's raw line, and a short slug describing that specific
trajectory (generated via `litellm`, see `utils.py`). On the rare occasion two
records would get the same name, the second gets `-2`, the third `-3`, and so
on.

`output/<namespace>/<hash6>-<slug>/`:

- `source.json` — the input record, copied verbatim. Note this is the full
  record; what the container itself sees at `/trajectory.txt` is just the
  decoded `content` (see "Adding a harness" below).
- `metadata.json` — written only on success:
  `{"harness", "task", "model", "hash", "timestamp", "experiment"}`. `hash` is
  the full sha256 (the folder name only has the first 6 chars); `timestamp` is
  when it finished; `experiment` is `SWARM_EXPERIMENT` or `null` (the record
  still physically lands under the `default` namespace either way — see
  "Output" above). This file's presence (with a `hash` matching a record's
  content) is also what a rerun checks to skip an already-done record, scoped
  to that run's own namespace.
- Whatever the task wrote. For `discovery`: `translation.bc`, `decisions.md`,
  `uncertainties.md`, `keywords.md`.

A record whose container passes `SWARM_TIMEOUT` is killed and recorded as a
failure with `returncode: -9`. The ceiling exists because nothing else bounds a
container: docker imposes no deadline, and a harness that stops making progress
holds its pool slot indefinitely — one agent ran `grep -rn BrainCode /` at 100%
CPU for 37 minutes with an empty `/output`, and fifteen at once starved the
host. 1200s is far above a normal record (2-5 minutes, or ~15 while riding out
proxy outages through the harness's own retries), so hitting it means something
is wrong rather than slow. Killing needs the container's name, not just the
`docker run` process — that only detaches the client and leaves the container
running — which is why `build_docker_cmd` names it.

`output/` holds successes only. A record that fails leaves nothing behind here
— its half-written folder is removed and its logs go to `failures/` instead
(below). Any folder without a `metadata.json` is removed at the start of the
next run, which now only ever catches crash orphans: a process killed before
it could finish a record.

## Failures

`failures/<namespace>/` mirrors `output/<namespace>/` one level up — same
namespace, sibling of the *base* output dir rather than of the namespace
folder itself (`swarm/output/<namespace>/` → `swarm/failures/<namespace>/`;
see `utils.failures_dir`). Nothing in here is touched by the pruning above, so
a failure's logs survive the next run — no rescuing anything by hand first.

`failures/<namespace>/<hash6>[-n]/`, one directory **per attempt**:

- `source.json` — the input record, verbatim.
- `stdout.log`, `stderr.log` — the container's full transcript.
- `partial/` — whatever the harness wrote before it died, when it wrote
  anything. A record that produces three of four files and then hits a 429 has
  done nearly all the work; that output is kept for inspection rather than
  discarded. It is still a failure: the task's contract is *all* its files, so
  no `metadata.json` is written and a rerun retries the record from scratch.
- `failure.json` — `{"hash", "attempt_name", "returncode", "produced_files",
  "partial_files", "duration_s", "timestamp", "harness", "task", "model",
  "experiment", "error"}`. `returncode` and `produced_files` are the fields the logs can't
  give you: a container that exits 0 having written nothing is a different
  problem from one that was killed, and the two look identical afterwards
  without them. `error` is the last `Error:` line the harness printed, and is
  `null` exactly when it reported no error at all — which is its own
  diagnostic signature, not missing data. A handful of entries predate this
  file and were backfilled from the logs alone: those carry a `note` saying so,
  and a `null` `returncode` meaning "not captured" rather than "exited 0".

**On the `-n` suffix:** it is assigned blindly, taking the first free name, so
it means only "that name was taken". Two unrelated things cause that:

- the same record failing again — the common case, since re-running a batch
  retries exactly the records that failed;
- a different record whose hash happens to share the first 6 hex chars — rare
  for any given pair, but near-certain across a corpus of this size (24 bits
  collides on the order of a hundred times at ~70k records).

So `abcdef` and `abcdef-2` are *not* reliably the same record twice, and not
reliably two different records either. `failure.json`'s full `hash` is what
groups attempts by record; count the directories sharing one to see how many
times that record has failed.

A later success does not clear an earlier failure: `failures/` is a history of
attempts, and whether a record eventually succeeded is already answered by
`output/`.

## Adding a task

Add `tasks/<name>.md`. Its content becomes the literal prompt sent to the
subagent — no other file to touch. Run with `SWARM_TASK=<name>`.

## Adding a harness

Add `harnesses/<name>/` with:

- `Dockerfile` — `FROM` an existing image, or build one from scratch.
- `entrypoint.sh` — reads `/prompt.md` and `/trajectory.txt`, uses
  `$SWARM_MODEL`/`$PROXY_API_KEY`/`$PROXY_BASE_URL`, writes results to
  `/output`.
- Whatever config file the CLI itself needs.

Every container gets, always:

```
read-only: /reference/DESIGN_DOC.md, /trajectory.txt, /prompt.md
writable:  /output
env:       PROXY_API_KEY, PROXY_BASE_URL, SWARM_MODEL, HOME=/tmp
```

`/trajectory.txt` is the record's decoded `content` — the turns as plain text,
not the raw JSONL line. It's deliberately not JSON: handed the raw record,
agents spent turns shelling out to `python3`/`node`/`jq`/`perl` to pretty-print
the escaped newlines, none of which exist in these images. A harness should
pass the file to its CLI as-is and not parse it.

Run with `SWARM_HARNESS=<name>`. The two existing harnesses, for reference:

| | `opencode` | `pi` |
|---|---|---|
| Base image | `ghcr.io/anomalyco/opencode` (official) | `node:24-bookworm-slim` (built here) |
| Config | baked in, read-only | rebuilt writable at container start (writes `auth.json` next to it) |
| Secrets | `{env:VAR}` in `config.jsonc` | `$VAR` in `models.template.json` |

## Security

- Non-root (`--user` matches host UID), `--cap-drop=ALL`,
  `--security-opt no-new-privileges`, memory/CPU capped.
- Mount surface: exactly the 3 read-only paths + 1 writable dir above — nothing
  else from the host is reachable.
- Network is **not** restricted — every harness needs to reach the model API.
- Neither harness restricts its own tools; the container/mount surface above is
  the only boundary.

## Tests

```bash
pip install -r requirements-test.txt
pytest tests/                          # fast, fully mocked, no credentials needed
pytest tests/ -m integration           # 1 real model call, needs PROXY_API_KEY
```

`-m integration` tests are excluded from the plain `pytest tests/` run by
default (see `pytest.ini`) even if `.env` has real credentials.

## Not implemented

No shared corpus/retrieval, so vocabulary doesn't converge across records on its
own. `decisions.md`/`uncertainties.md`/`keywords.md` are raw material for a
future review task — not built yet.
