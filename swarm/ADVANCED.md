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

- `source.json` — the input record, copied verbatim.
- `metadata.json` — written only on success:
  `{"harness", "task", "model", "hash", "timestamp", "experiment"}`. `hash` is
  the full sha256 (the folder name only has the first 6 chars); `timestamp` is
  when it finished; `experiment` is `SWARM_EXPERIMENT` or `null`. This file's
  presence (with a `hash` matching a record's content) is also what a rerun
  checks to skip an already-done record.
- Whatever the task wrote. For `discovery`: `translation.bc`, `decisions.md`,
  `uncertainties.md`, `keywords.md`.
- On failure (no `metadata.json`): `stdout.log`, `stderr.log`.

A folder with none of the above (killed mid-run before anything was written) is
a crash orphan — removed automatically at the start of the next run.

## Adding a task

Add `tasks/<name>.md`. Its content becomes the literal prompt sent to the
subagent — no other file to touch. Run with `SWARM_TASK=<name>`.

## Adding a harness

Add `harnesses/<name>/` with:

- `Dockerfile` — `FROM` an existing image, or build one from scratch.
- `entrypoint.sh` — reads `/prompt.md` and `/trajectory.json`, uses
  `$SWARM_MODEL`/`$PROXY_API_KEY`/`$PROXY_BASE_URL`, writes results to
  `/output`.
- Whatever config file the CLI itself needs.

Every container gets, always:

```
read-only: /reference/DESIGN_DOC.md, /trajectory.json, /prompt.md
writable:  /output
env:       PROXY_API_KEY, PROXY_BASE_URL, SWARM_MODEL, HOME=/tmp
```

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
