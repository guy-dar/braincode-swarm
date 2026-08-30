"""Helpers for spawn_batch.py, kept out of the dispatcher to keep it lean:
env loading, output-folder naming (content hash + LLM-generated slug), and the
startup bookkeeping that makes reruns skip already-done records instead of
redoing them. Needs `litellm` installed (`pip install litellm`) — the one
dependency this repo has beyond the standard library, isolated here rather
than in spawn_batch.py itself.
"""
import hashlib
import json
import os
import re
import shutil
import threading
from dataclasses import dataclass
from pathlib import Path

import litellm

SLUG_PROMPT = """Read the trajectory below and produce a short filesystem-safe \
slug describing it: lowercase words separated by single hyphens, 3 to 6 words, \
no punctuation, no quotes. It is one of many similar trajectories in the same \
batch, so name what's actually distinct about this one — the specific subject, \
action, or detail — not a generic description that could apply to any of them. \
Output only the slug, nothing else.

Trajectory:
{content}"""


def load_dotenv(path: Path):
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


@dataclass
class Config:
    harness_name: str
    task_name: str
    model: str
    concurrency: int
    experiment: str
    base_url: str
    api_key: str
    harness_dir: Path
    task_file: Path


def load_config(self_dir: Path) -> Config:
    """Read spawn_batch.py's configuration from the environment (self_dir/.env
    fills in anything not already set) and resolve/validate the pieces that
    need to name a real file. Raises ValueError with a user-facing message if
    anything required is missing — the caller decides how to report it.
    """
    load_dotenv(self_dir / ".env")

    harness_name = os.environ.get("SWARM_HARNESS", "opencode")
    task_name = os.environ.get("SWARM_TASK", "discovery")
    model = os.environ.get("SWARM_MODEL", "vertex-proxy/gemini-flash")
    concurrency = int(os.environ.get("SWARM_CONCURRENCY", "4"))
    experiment = os.environ.get("SWARM_EXPERIMENT") or None
    base_url = os.environ.setdefault("PROXY_BASE_URL", "https://vertex-proxy-v26q.onrender.com/v1")
    api_key = os.environ.get("PROXY_API_KEY")
    if not api_key:
        raise ValueError("PROXY_API_KEY not set (checked environment and .env)")

    harness_dir = self_dir / "harnesses" / harness_name
    if not (harness_dir / "Dockerfile").exists():
        raise ValueError(f"no such harness: {harness_dir}")
    task_file = self_dir / "tasks" / f"{task_name}.md"
    if not task_file.exists():
        raise ValueError(f"no such task file: {task_file}")

    return Config(harness_name, task_name, model, concurrency, experiment,
                  base_url, api_key, harness_dir, task_file)


def load_batch(batch_path: Path, done_hashes: set) -> tuple:
    """Read a batch file into (line, hash) pairs, skipping blank lines and any
    record whose content hash is already in done_hashes. Returns
    (records, skipped_count).
    """
    records = []
    skipped = 0
    with batch_path.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            full_hash = content_hash(line)
            if full_hash in done_hashes:
                skipped += 1
                continue
            records.append((line, full_hash))
    return records, skipped


def prune_incomplete_folders(out_dir: Path) -> list:
    """Remove folders left behind by a process killed before it could write
    anything usable — no metadata.json (done) and no stdout.log/stderr.log (a
    harness failure recorded on purpose, for debugging, not to be deleted).
    Anything with neither is a crash orphan: dead weight that would otherwise
    just sit there forcing every retry of that hash onto a `-2` suffix.
    Returns the names removed, for the caller to log.
    """
    removed = []
    if not out_dir.exists():
        return removed
    for entry in out_dir.iterdir():
        if not entry.is_dir():
            continue
        if (entry / "metadata.json").exists():
            continue
        if (entry / "stdout.log").exists() or (entry / "stderr.log").exists():
            continue
        shutil.rmtree(entry)
        removed.append(entry.name)
    return removed


def scan_existing_output(out_dir: Path):
    """One pass over out_dir at startup: which content hashes are already
    done (have a metadata.json with a timestamp — written only on success),
    and every folder name already in use (for reserve_name's -n collision
    avoidance, regardless of whether that folder succeeded, failed, or is
    unrelated).
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


def content_hash(record_line: str) -> str:
    """Full sha256 hex digest of the raw record line — the stable identity a
    folder name's prefix and its metadata.json's `hash` field both derive
    from, regardless of whether the record has its own `id` field.
    """
    return hashlib.sha256(record_line.encode()).hexdigest()


def slugify(text: str, max_words: int = 6, max_len: int = 50) -> str:
    text = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    text = "-".join(text.split("-")[:max_words])[:max_len].strip("-")
    return text or "example"


def generate_slug(record_line: str, model: str, api_key: str, base_url: str) -> str:
    """Ask the model for a short, specific slug for this one trajectory.
    Never raises — a naming nicety isn't worth failing a whole record over;
    falls back to a generic slug if the call fails for any reason.
    """
    # SWARM_MODEL is "provider/id", meaningful to the harnesses' own config
    # (e.g. opencode's provider block). litellm talks to base_url directly
    # here, so only the id half means anything to it — the "openai/" prefix
    # tells litellm to speak the OpenAI-compatible wire format against
    # whatever base_url points at, same protocol every harness already uses.
    model_id = model.rsplit("/", 1)[-1]
    try:
        response = litellm.completion(
            model=f"openai/{model_id}",
            api_key=api_key,
            api_base=base_url,
            messages=[{"role": "user", "content": SLUG_PROMPT.format(content=record_line)}],
            # Generous on purpose, not because the slug itself is long: a
            # reasoning model's thinking counts against this same budget, and
            # a too-small cap means it spends everything thinking and returns
            # no visible text at all (verified — 30 reliably produced empty
            # output; 1024 reliably left room for both).
            max_tokens=1024,
            timeout=45,
        )
        raw = response.choices[0].message.content or ""
    except Exception:
        raw = ""
    return slugify(raw)


def build_folder_name(full_hash: str, slug: str) -> str:
    return f"{full_hash[:6]}-{slug}"


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


def build_docker_cmd(uid: int, gid: int, model: str, design_doc: Path,
                      traj_path: Path, prompt_file: Path, scratch, image: str) -> list:
    """The exact `docker run` invocation for one record: non-root (matches
    the host uid/gid, so the writable /output mount just works), all
    capabilities dropped, no privilege escalation, memory/CPU capped. Network
    is deliberately not restricted — every harness needs to reach the model
    API. Mount surface is exactly the 3 read-only paths + 1 writable dir
    below; nothing else from the host is reachable (see ADVANCED.md's
    Security section for the fuller rationale).
    """
    return [
        "docker", "run", "--rm",
        "--user", f"{uid}:{gid}",
        "-e", "HOME=/tmp",
        "--cap-drop=ALL",
        "--security-opt", "no-new-privileges:true",
        "--memory", "1g",
        "--cpus", "1",
        "-e", "PROXY_API_KEY", "-e", "PROXY_BASE_URL",
        "-e", f"SWARM_MODEL={model}",
        "-v", f"{design_doc}:/reference/DESIGN_DOC.md:ro",
        "-v", f"{traj_path}:/trajectory.json:ro",
        "-v", f"{prompt_file}:/prompt.md:ro",
        "-v", f"{scratch}:/output",
        image,
    ]
