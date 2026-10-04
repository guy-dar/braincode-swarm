"""reference/reference-manifest.json: what the reference directory currently
holds, with checksums, and the glossary's version.

The glossary version is `<language version>+g<revision>`: the revision counts
installed glossary changes (one per accepted migration or manual edit), so a
translation's recorded version pins exactly which glossary it was made with.
"""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

from . import records as rec_mod

REF_DIR = rec_mod.REF_DIR
MANIFEST = REF_DIR / "reference-manifest.json"
LANGUAGE_VERSION = "19.0.0-draft.1"
TRACKED = ("language-spec.md", "language-spec.compact.md", "glossary.jsonl", "glossary.md",
           "glossary-provenance.jsonl", "examples.jsonl", "purpose.md")


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(ref_dir: Path = REF_DIR) -> dict:
    path = ref_dir / "reference-manifest.json"
    if path.exists():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if "glossary_revision" in data:
                return data
        except ValueError:
            pass
    return {"language_version": LANGUAGE_VERSION, "glossary_revision": 0, "revisions": []}


def version_string(revision: int) -> str:
    return f"{LANGUAGE_VERSION}+g{revision}"


def current_version(ref_dir: Path = REF_DIR) -> str:
    return version_string(load(ref_dir)["glossary_revision"])


def write(data: dict, ref_dir: Path = REF_DIR) -> dict:
    data["language_version"] = LANGUAGE_VERSION
    data["glossary_version"] = version_string(data["glossary_revision"])
    data["updated_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    data["files"] = [{"file": name, "sha256": _sha(ref_dir / name)}
                     for name in TRACKED if (ref_dir / name).exists()]
    (ref_dir / "reference-manifest.json").write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n",
                                                     encoding="utf-8", newline="\n")
    return data


def bump_version(note: str, batch=None, ref_dir: Path = REF_DIR) -> str:
    """Record one installed glossary change and return the new version string.
    Call before rendering so the rendered headers carry the new version;
    call refresh() after rendering to update file checksums."""
    data = load(ref_dir)
    data["glossary_revision"] += 1
    data.setdefault("revisions", []).append({
        "revision": data["glossary_revision"], "batch": batch, "note": note,
        "at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    })
    write(data, ref_dir)
    return version_string(data["glossary_revision"])


def refresh(ref_dir: Path = REF_DIR) -> dict:
    """Recompute checksums without changing the version."""
    return write(load(ref_dir), ref_dir)


def glossary_sha(ref_dir: Path = REF_DIR) -> str:
    path = ref_dir / "glossary.jsonl"
    return _sha(path) if path.exists() else ""
