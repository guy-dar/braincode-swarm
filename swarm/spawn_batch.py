#!/usr/bin/env python3
"""Usage: spawn_batch.py <batch.jsonl> <output-dir>

One isolated `docker run` per record, generic across any tasks/<name>.md and
harnesses/<name>/ — see README.md for basic usage and ADVANCED.md for config
vars, output format, and adding a task/harness.
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


def process_record(record_line: str, full_hash: str, image: str,
                    design_doc: Path, prompt_file: Path, model: str,
                    api_key: str, base_url: str, harness_name: str,
                    task_name: str, experiment: str, out_dir: Path,
                    names: set, names_lock: threading.Lock):
    slug = utils.generate_slug(record_line, model, api_key, base_url)
    name = utils.reserve_name(utils.build_folder_name(full_hash, slug), names, names_lock)

    dest = out_dir / name
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "source.json").write_text(record_line)

    # write_text() flushes before docker mounts the file; a handle left open
    # across subprocess.run() below once caused the container to see an
    # empty trajectory.
    traj_fd, traj_name = tempfile.mkstemp(suffix=".json")
    os.close(traj_fd)
    traj_path = Path(traj_name)
    traj_path.write_text(record_line)

    uid, gid = os.getuid(), os.getgid()
    with tempfile.TemporaryDirectory() as scratch:
        try:
            cmd = utils.build_docker_cmd(uid, gid, model, design_doc, traj_path,
                                          prompt_file, scratch, image)
            result = subprocess.run(cmd, capture_output=True, text=True)
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
                return name, True, None
            else:
                # Preserve the transcript even on failure rather than losing it.
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

    try:
        config = utils.load_config(SELF_DIR)
    except ValueError as e:
        sys.exit(f"spawn_batch: {e}")

    image = f"braincode-swarm-{config.harness_name}"
    print(f"spawn_batch: building harness '{config.harness_name}'...", file=sys.stderr)
    subprocess.run(["docker", "build", "-t", image, str(config.harness_dir)], check=True)

    out_dir.mkdir(parents=True, exist_ok=True)
    design_doc = SELF_DIR / "DESIGN_DOC.md"
    prompt_file = Path(tempfile.mkstemp(suffix=".md")[1])
    prompt_file.write_text(config.task_file.read_text())

    pruned = utils.prune_incomplete_folders(out_dir)
    if pruned:
        print(f"spawn_batch: pruned {len(pruned)} incomplete folder(s) from a previous crash",
              file=sys.stderr)

    done_hashes, names = utils.scan_existing_output(out_dir)
    names_lock = threading.Lock()

    records, skipped = utils.load_batch(batch_path, done_hashes)
    if skipped:
        print(f"spawn_batch: skipping {skipped} already-completed record(s)", file=sys.stderr)

    try:
        with ThreadPoolExecutor(max_workers=config.concurrency) as pool:
            futures = [
                pool.submit(process_record, line, full_hash, image, design_doc,
                            prompt_file, config.model, config.api_key, config.base_url,
                            config.harness_name, config.task_name, config.experiment,
                            out_dir, names, names_lock)
                for line, full_hash in records
            ]
            for future in as_completed(futures):
                name, ok, tail = future.result()
                if not ok:
                    print(f"spawn_batch: {name} — no files written to /output (stderr: {tail})",
                          file=sys.stderr)
    finally:
        prompt_file.unlink(missing_ok=True)

    print(f"spawn_batch: {batch_path} (harness: {config.harness_name}, task: {config.task_name}) "
          f"— {len(records)} dispatched, {skipped} skipped (already done)", file=sys.stderr)


if __name__ == "__main__":
    main()
