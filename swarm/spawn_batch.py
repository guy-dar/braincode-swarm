#!/usr/bin/env python3
"""Usage: spawn_batch.py <batch.jsonl> <output-dir>

One isolated `docker run` per record, generic across any tasks/<name>.md and
harnesses/<name>/ — see README.md for basic usage and ADVANCED.md for config
vars, output format, and adding a task/harness.
"""
import json
import os
import random
import shutil
import subprocess
import sys
import tempfile
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

import utils

SELF_DIR = Path(__file__).resolve().parent

# Distinct from any exit code a harness produces, so failure.json's returncode
# says "we killed this" rather than being mistaken for the container's own.
TIMEOUT_RETURNCODE = -9


def _decode(stream) -> str:
    """TimeoutExpired carries whatever was captured before the kill, as bytes
    or None depending on the platform."""
    if stream is None:
        return ""
    return stream if isinstance(stream, str) else stream.decode("utf-8", "replace")


def process_record(record_line: str, full_hash: str, image: str,
                    reference_dir: Path, prompt_file: Path, model: str,
                    api_key: str, base_url: str, harness_name: str,
                    task_name: str, experiment: str, timeout_s: int,
                    out_dir: Path, names: set, names_lock: threading.Lock,
                    stagger_s: float = 0.0):
    # Optional start jitter, off unless SWARM_STAGGER is set (see utils.load_config).
    if stagger_s:
        time.sleep(random.uniform(0, stagger_s))
    slug = utils.generate_slug(record_line, model, api_key, base_url)
    name = utils.reserve_name(utils.build_folder_name(full_hash, slug), names, names_lock)

    dest = out_dir / name
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "source.json").write_text(record_line)

    # The container gets the decoded turns as text, not the raw JSON record —
    # see utils.trajectory_text. source.json above keeps the full record.
    #
    # write_text() flushes before docker mounts the file; a handle left open
    # across subprocess.run() below once caused the container to see an
    # empty trajectory.
    traj_fd, traj_name = tempfile.mkstemp(suffix=".txt")
    os.close(traj_fd)
    traj_path = Path(traj_name)
    traj_path.write_text(utils.trajectory_text(record_line))

    uid, gid = utils.host_uid_gid() or (None, None)
    with tempfile.TemporaryDirectory() as scratch:
        try:
            container_name = f"swarm-{name}"
            cmd = utils.build_docker_cmd(uid, gid, model, reference_dir, traj_path,
                                          prompt_file, scratch, image,
                                          container_name=container_name)
            started = time.monotonic()
            try:
                result = subprocess.run(cmd, capture_output=True, text=True,
                                        timeout=timeout_s)
            except subprocess.TimeoutExpired as expired:
                # A container that never finishes on its own. Seen for real: an
                # agent ran `grep -rn BrainCode /` and sat at 100% CPU for 37
                # minutes with an empty /output, and 15 of them at once starved
                # a 14-core host. Nothing upstream bounds this — docker has no
                # deadline, the harness had already stopped talking to the API,
                # and the pool slot is held the whole time — so the ceiling has
                # to live here.
                subprocess.run(["docker", "kill", container_name],
                               capture_output=True, text=True)
                result = subprocess.CompletedProcess(
                    cmd, returncode=TIMEOUT_RETURNCODE,
                    stdout=_decode(expired.stdout),
                    # Harnesses buffer their output, so a killed container's
                    # transcript is usually empty — say why the record ended,
                    # or failure.json would show a bare exit code and nothing
                    # to explain it. Written in the harnesses' own `Error:`
                    # convention, and last, so last_error_line reports the
                    # timeout rather than whatever the harness said before it
                    # stopped making progress.
                    stderr=(_decode(expired.stderr)
                            + f"\nError: timed out after {timeout_s}s and was killed."),
                )
            duration_s = time.monotonic() - started
            produced = any(Path(scratch).iterdir())
            if result.returncode == 0 and produced:
                for item in Path(scratch).iterdir():
                    dest_item = dest / item.name
                    if item.is_dir():
                        shutil.copytree(item, dest_item, dirs_exist_ok=True)
                    else:
                        shutil.copy2(item, dest_item)
                # Only written on success; a rerun's startup scan checks this
                # to skip an already-done hash.
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
                # A previous failure of this record is deliberately left in
                # failures/ — it's a history of attempts, and "this eventually
                # succeeded" is already answerable from out_dir. Which records
                # still need work is out_dir's job (scan_existing_output), not
                # something failures/ has to stay in sync with.
                return name, True, None
            else:
                # Failures are preserved outside out_dir, keyed by content hash
                # (see utils.record_failure), so out_dir holds successes only
                # and a retry replaces its predecessor instead of leaving
                # another near-duplicate folder behind. The half-written
                # out_dir folder is removed rather than left for the next run's
                # prune pass to find.
                utils.record_failure(
                    out_dir=out_dir, full_hash=full_hash, attempt_name=name,
                    record_line=record_line, stdout=result.stdout,
                    stderr=result.stderr, returncode=result.returncode,
                    produced=produced, duration_s=duration_s,
                    harness_name=harness_name, task_name=task_name,
                    model=model, experiment=experiment,
                    produced_dir=scratch,
                )
                shutil.rmtree(dest, ignore_errors=True)
                tail = utils.last_error_line(result.stderr) or (
                    f"no error reported — exit {result.returncode}, "
                    f"wrote nothing, after {duration_s:.0f}s"
                )
                if produced:
                    # Worth calling out: the harness wrote files and still
                    # failed, so this record was close and its partial output
                    # is kept for inspection rather than thrown away.
                    tail += " — partial output kept"
                return name, False, tail
        finally:
            traj_path.unlink(missing_ok=True)


def main():
    if len(sys.argv) != 3:
        sys.exit("usage: spawn_batch.py <batch.jsonl> <output-dir>")
    batch_path, base_out_dir = Path(sys.argv[1]), Path(sys.argv[2])

    try:
        config = utils.load_config(SELF_DIR)
    except ValueError as e:
        sys.exit(f"spawn_batch: {e}")

    # Every run lives under its own namespace subfolder, keyed by
    # SWARM_EXPERIMENT ("default" if unset) — not a special "rerun" mode, just
    # the ordinary way any two runs (a fresh corpus, a resample, the same
    # batch replayed under a later spec) coexist without one's done-hashes
    # shadowing the other's. Same shape one level down for failures/, so
    # `output/<namespace>/` and `failures/<namespace>/` always pair up (see
    # utils.failures_dir).
    namespace = config.experiment or "default"
    out_dir = base_out_dir / namespace

    image = f"braincode-swarm-{config.harness_name}"
    print(f"spawn_batch: building harness '{config.harness_name}'...", file=sys.stderr)
    subprocess.run(["docker", "build", "-t", image, str(config.harness_dir)], check=True)

    out_dir.mkdir(parents=True, exist_ok=True)
    reference_dir = SELF_DIR / "reference"
    prompt_file = Path(tempfile.mkstemp(suffix=".md")[1])
    prompt_file.write_text(config.task_file.read_text())

    pruned = utils.prune_incomplete_folders(out_dir)
    if pruned:
        print(f"spawn_batch: pruned {len(pruned)} folder(s) without metadata.json "
              f"(previous failures and crash orphans)",
              file=sys.stderr)

    done_hashes, names = utils.scan_existing_output(out_dir)
    names_lock = threading.Lock()

    records, skipped = utils.load_batch(batch_path, done_hashes)
    if skipped:
        print(f"spawn_batch: skipping {skipped} already-completed record(s)", file=sys.stderr)

    failed = 0
    try:
        with ThreadPoolExecutor(max_workers=config.concurrency) as pool:
            futures = [
                pool.submit(process_record, line, full_hash, image, reference_dir,
                            prompt_file, config.model, config.api_key, config.base_url,
                            config.harness_name, config.task_name, config.experiment,
                            config.timeout_s, out_dir, names, names_lock,
                            config.stagger_s)
                for line, full_hash in records
            ]
            for future in as_completed(futures):
                name, ok, tail = future.result()
                if not ok:
                    failed += 1
                    print(f"spawn_batch: {name} — failed ({tail})", file=sys.stderr)
    finally:
        prompt_file.unlink(missing_ok=True)

    print(f"spawn_batch: {batch_path} (harness: {config.harness_name}, task: {config.task_name}, "
          f"namespace: {namespace}) — {len(records) - failed} succeeded, {failed} failed, "
          f"{skipped} skipped (already done)", file=sys.stderr)
    if failed:
        print(f"spawn_batch: failure logs in {utils.failures_dir(out_dir)}/<hash6>[-n]/ "
              f"— one directory per attempt; re-run this batch to retry just the "
              f"records that failed", file=sys.stderr)


if __name__ == "__main__":
    main()
