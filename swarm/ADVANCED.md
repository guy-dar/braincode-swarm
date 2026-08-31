# Advanced

Everything here is optional context for extending, configuring, or debugging the
pipeline — not needed for normal use (see `README.md` for that).

## Config

| Var | Default | Meaning |
|---|---|---|
| `PROXY_API_KEY` | *(required)* | — |
| `PROXY_BASE_URL` | vertex-proxy's URL | model backend |
| `SWARM_HARNESS` | `opencode` | picks `harnesses/$SWARM_HARNESS/` |
| `SWARM_TASK` | `discovery` | picks `tasks/$SWARM_TASK.md` |
| `SWARM_MODEL` | `vertex-proxy/gemini-flash` | passed to the harness |
| `SWARM_CONCURRENCY` | `4` | concurrent `docker run`s |
| `SWARM_BATCH_SIZE` | `20` | informational — how you split data, not enforced |
| `SWARM_EXPERIMENT` | *(unset)* | recorded in `metadata.json`; tags which run a record came from |

## Output

Each record's folder is named `<hash6>-<slug>`: the first 6 hex chars of a
sha256 of the record's raw line, and a short slug describing that specific
trajectory (generated via `litellm`, see `utils.py`). On the rare occasion two
records would get the same name, the second gets `-2`, the third `-3`, and so
on.

`output/<hash6>-<slug>/`:

- `source.json` — the input record, copied verbatim. Note this is the full
  record; what the container itself sees at `/trajectory.txt` is just the
  decoded `content` (see "Adding a harness" below).
- `metadata.json` — written only on success:
  `{"harness", "task", "model", "hash", "timestamp", "experiment"}`. `hash` is
  the full sha256 (the folder name only has the first 6 chars); `timestamp` is
  when it finished; `experiment` is `SWARM_EXPERIMENT` or `null`. This file's
  presence (with a `hash` matching a record's content) is also what a rerun
  checks to skip an already-done record.
- Whatever the task wrote. For `discovery`: `translation.bc`, `decisions.md`,
  `uncertainties.md`, `keywords.md`.

`output/` holds successes only. A record that fails leaves nothing behind here
— its half-written folder is removed and its logs go to `failures/` instead
(below). Any folder without a `metadata.json` is removed at the start of the
next run, which now only ever catches crash orphans: a process killed before
it could finish a record.

## Failures

`failures/`, a sibling of the output dir you passed on the command line
(`swarm/output/` → `swarm/failures/`). Nothing in here is touched by the
pruning above, so a failure's logs survive the next run — no rescuing anything
by hand first.

`failures/<hash6>[-n]/`, one directory **per attempt**:

- `source.json` — the input record, verbatim.
- `stdout.log`, `stderr.log` — the container's full transcript.
- `failure.json` — `{"hash", "attempt_name", "returncode", "produced_files",
  "duration_s", "timestamp", "harness", "task", "model", "experiment",
  "error"}`. `returncode` and `produced_files` are the fields the logs can't
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
