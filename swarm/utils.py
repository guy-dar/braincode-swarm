"""Helpers for spawn_batch.py, kept out of the dispatcher to keep it lean.

Currently: turning one record into the two things its output folder name is
built from — a content hash (stable identity, for skip-on-rerun and for
detecting real collisions) and a short LLM-generated slug (for skimmability
across a batch of otherwise similar-looking trajectories). Needs `litellm`
installed (`pip install litellm`) — the one dependency this repo has beyond
the standard library, isolated here rather than in spawn_batch.py itself.
"""
import hashlib
import re
import shutil
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
