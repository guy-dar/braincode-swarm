#!/usr/bin/env python3
"""Usage: spawn_batch.py <batch.jsonl> <output-dir>

Generic across any task under tasks/ and any harness under harnesses/. Each
harness folder is just a Dockerfile + an entrypoint.sh baked into its own
image — the entrypoint knows that harness's exact CLI invocation, so this
script's `docker run` is byte-identical regardless of which harness is
selected; only the image tag differs. tasks/<SWARM_TASK>.md's content *is*
the prompt, verbatim, mounted read-only at /prompt.md.

Every container gets, always:
  read-only: /reference/DESIGN_DOC.md, /trajectory.json, /prompt.md
  writable:  /output
  env:       PROXY_API_KEY, PROXY_BASE_URL, SWARM_MODEL, HOME=/tmp

Config (SWARM_HARNESS, SWARM_TASK, SWARM_MODEL, SWARM_CONCURRENCY,
SWARM_EXPERIMENT, PROXY_API_KEY, PROXY_BASE_URL, ...) comes from the
environment, with a local .env file (stdlib-parsed, no dependency) filling in
anything not already set — see .env.example. Real env vars always win over
.env.

Each record's output folder is named `<hash6>-<slug>` (see utils.py): a
6-hex-char content-hash prefix plus a short LLM-generated slug describing
what's specific about that one trajectory. The full hash and a completion
timestamp live in the folder's metadata.json; a record whose hash is already
present there (scanned once at startup) is skipped on a rerun rather than
redone, so re-running a batch after a partial failure only fills in what's
missing. Folders left behind by a process that was killed mid-run — no
metadata.json, no stdout.log/stderr.log — are pruned at startup before that
scan, so a retry reclaims the original name instead of piling up `-2`, `-3`,
... for the same content.

One batch file is not "the dataset" — there's no assumption anywhere here that
records all come from one static source. Call this once per batch file, as
many times as you have batches, from as many sources as you're mixing in;
output/ accumulates across calls regardless of when or where each record came
from. Folder names are derived from content, not from any `id` a record might
carry, so mixing sources never collides two unrelated records into the same
folder — see .claude/skills/miner and .claude/skills/orchestrator for the
fuller guidance on sourcing and batching.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

import utils

SELF_DIR = Path(__file__).resolve().parent


def load_dotenv(path: Path):
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def docker_security_args():
    # Non-root (matches the host UID, so the writable /output mount just
    # works), all capabilities dropped, no privilege escalation, resource
    # capped. Not restricted: network — every harness needs to reach the
    # model API, so egress stays open. The mount surface (see module
    # docstring) is deliberately narrow enough that this is an acceptable
    # trade-off: there's nothing sensitive in the container for untrusted
    # trajectory content to find even with full tool access.
    uid, gid = os.getuid(), os.getgid()
    return [
        "--user", f"{uid}:{gid}",
        "-e", "HOME=/tmp",
        "--cap-drop=ALL",
        "--security-opt", "no-new-privileges:true",
        "--memory", "1g",
        "--cpus", "1",
    ]


def scan_existing_output(out_dir: Path):
    """One pass over out_dir at startup: which content hashes are already
    done (have a metadata.json with a timestamp — written only on success),
    and every folder name already in use (for -n collision avoidance below,
    regardless of whether that folder succeeded, failed, or is unrelated).
    """
    done_hashes = set()
    names = set()
    if not out_dir.exists():
        return done_hashes, names
    for entry in out_dir.iterdir():
        if not entry.is_dir():
            continue
        names.add(entry.name)
        meta_path = entry / "metadata.json"
        if not meta_path.exists():
            continue
        try:
            meta = json.loads(meta_path.read_text())
        except (json.JSONDecodeError, OSError):
            continue
        if meta.get("hash") and meta.get("timestamp"):
            done_hashes.add(meta["hash"])
    return done_hashes, names


def reserve_name(base: str, names: set, names_lock: threading.Lock) -> str:
    """Thread-safe: claims `base`, or `base-2`, `base-3`, ... if taken —
    covers both names already on disk at startup and ones claimed by a
    sibling worker earlier in this same run.
    """
    with names_lock:
        if base not in names:
            names.add(base)
            return base
        n = 2
        while f"{base}-{n}" in names:
            n += 1
        name = f"{base}-{n}"
        names.add(name)
        return name


def process_record(record_line: str, full_hash: str, image: str,
                    design_doc: Path, prompt_file: Path, model: str,
                    api_key: str, base_url: str, harness_name: str,
                    task_name: str, experiment: str, out_dir: Path,
                    names: set, names_lock: threading.Lock):
    slug = utils.generate_slug(record_line, model, api_key, base_url)
    name = reserve_name(utils.build_folder_name(full_hash, slug), names, names_lock)

    dest = out_dir / name
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "source.json").write_text(record_line)

    # write_text() opens, writes, and closes in one call — guaranteed flushed
    # to disk before docker mounts it. (A file handle left open across the
    # subprocess.run() call below is not guaranteed to be flushed yet — an
    # intermittent race that once showed up as the container seeing an empty
    # trajectory.)
    traj_fd, traj_name = tempfile.mkstemp(suffix=".json")
    os.close(traj_fd)
    traj_path = Path(traj_name)
    traj_path.write_text(record_line)

    with tempfile.TemporaryDirectory() as scratch:
        try:
            cmd = [
                "docker", "run", "--rm", *docker_security_args(),
                "-e", "PROXY_API_KEY", "-e", "PROXY_BASE_URL",
                "-e", f"SWARM_MODEL={model}",
                "-v", f"{design_doc}:/reference/DESIGN_DOC.md:ro",
                "-v", f"{traj_path}:/trajectory.json:ro",
                "-v", f"{prompt_file}:/prompt.md:ro",
                "-v", f"{scratch}:/output",
                image,
            ]
            result = subprocess.run(cmd, capture_output=True, text=True)
            produced = any(Path(scratch).iterdir())
            if result.returncode == 0 and produced:
                for item in Path(scratch).iterdir():
                    dest_item = dest / item.name
                    if item.is_dir():
                        shutil.copytree(item, dest_item, dirs_exist_ok=True)
                    else:
                        shutil.copy2(item, dest_item)
                # Written last, only on success — this is also the marker a
                # rerun's startup scan checks to skip an already-done hash.
                (dest / "metadata.json").write_text(json.dumps(
                    {
                        "harness": harness_name,
                        "task": task_name,
                        "model": model,
                        "hash": full_hash,
                        "timestamp": datetime.now(timezone.utc).isoformat(),
                        "experiment": experiment,
                    },
                    indent=2,
                ))
                return name, True, None
            else:
                # Nothing landed in the harness's output dir — keep the raw
                # transcript instead of silently losing it; this script
                # doesn't try to interpret why the harness didn't produce
                # anything, it just preserves the evidence.
                (dest / "stdout.log").write_text(result.stdout)
                (dest / "stderr.log").write_text(result.stderr)
                tail = "\n".join(result.stderr.strip().splitlines()[-3:])
                return name, False, tail
        finally:
            traj_path.unlink(missing_ok=True)


def main():
    if len(sys.argv) != 3:
        sys.exit("usage: spawn_batch.py <batch.jsonl> <output-dir>")
    batch_path, out_dir = Path(sys.argv[1]), Path(sys.argv[2])

    load_dotenv(SELF_DIR / ".env")

    harness_name = os.environ.get("SWARM_HARNESS", "opencode")
    task_name = os.environ.get("SWARM_TASK", "discovery")
    model = os.environ.get("SWARM_MODEL", "vertex-proxy/gemini-flash")
    concurrency = int(os.environ.get("SWARM_CONCURRENCY", "4"))
    experiment = os.environ.get("SWARM_EXPERIMENT") or None
    base_url = os.environ.setdefault("PROXY_BASE_URL", "https://vertex-proxy-v26q.onrender.com/v1")
    api_key = os.environ.get("PROXY_API_KEY")
    if not api_key:
        sys.exit("spawn_batch: PROXY_API_KEY not set (checked environment and .env)")

    harness_dir = SELF_DIR / "harnesses" / harness_name
    if not (harness_dir / "Dockerfile").exists():
        sys.exit(f"spawn_batch: no such harness: {harness_dir}")
    task_file = SELF_DIR / "tasks" / f"{task_name}.md"
    if not task_file.exists():
        sys.exit(f"spawn_batch: no such task file: {task_file}")

    image = f"braincode-swarm-{harness_name}"
    print(f"spawn_batch: building harness '{harness_name}'...", file=sys.stderr)
    subprocess.run(["docker", "build", "-t", image, str(harness_dir)], check=True)

    out_dir.mkdir(parents=True, exist_ok=True)
    design_doc = SELF_DIR / "DESIGN_DOC.md"
    prompt_file = Path(tempfile.mkstemp(suffix=".md")[1])
    prompt_file.write_text(task_file.read_text())

    pruned = utils.prune_incomplete_folders(out_dir)
    if pruned:
        print(f"spawn_batch: pruned {len(pruned)} incomplete folder(s) from a previous crash",
              file=sys.stderr)

    done_hashes, names = scan_existing_output(out_dir)
    names_lock = threading.Lock()

    records = []
    skipped = 0
    with batch_path.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            full_hash = utils.content_hash(line)
            if full_hash in done_hashes:
                skipped += 1
                continue
            records.append((line, full_hash))

    if skipped:
        print(f"spawn_batch: skipping {skipped} already-completed record(s)", file=sys.stderr)

    try:
        with ThreadPoolExecutor(max_workers=concurrency) as pool:
            futures = [
                pool.submit(process_record, line, full_hash, image, design_doc,
                            prompt_file, model, api_key, base_url, harness_name,
                            task_name, experiment, out_dir, names, names_lock)
                for line, full_hash in records
            ]
            for future in as_completed(futures):
                name, ok, tail = future.result()
                if not ok:
                    print(f"spawn_batch: {name} — no files written to /output (stderr: {tail})",
                          file=sys.stderr)
    finally:
        prompt_file.unlink(missing_ok=True)

    print(f"spawn_batch: {batch_path} (harness: {harness_name}, task: {task_name}) "
          f"— {len(records)} dispatched, {skipped} skipped (already done)", file=sys.stderr)


if __name__ == "__main__":
    main()
