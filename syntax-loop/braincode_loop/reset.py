"""Reset the workspace to seed state so a fresh run starts from Sprint 0: docs/ is restored from
braincode_loop/seed_docs/, runtime outputs under runs/ are moved out of the way, and the
auto-logged section of sources/previous_work.md is emptied. Nothing else (config, datasets,
sources tables) is touched.

**Nothing is deleted.** Everything a reset displaces — the previous docs/ files, runs/
kpi_history.jsonl and budget_log.json, docs/notes-status.json, and the auto-logged source rows —
is moved into runs/archive/reset_<timestamp>/ first. Per-run logs under runs/logs/ are never
touched.

import_baseline() is the alternative starting point: a reset, then an existing product's
language-spec.md + glossary.md copied (read-only — the product folder is never written to) over
the seed templates, so the loop skips Sprint 0 and continues sprint numbering from the baseline.
The product folder may hold the two files directly, or versioned subfolders (v1/, v2/, ...), in
which case the highest version is used.

Also holds snapshot_docs(), the reverse direction: archiving a run's *produced* docs/ (not the
pristine templates) into seed_docs/runs/<run_id>/ — see its docstring.
"""
from __future__ import annotations

import logging
import datetime
import os
import re
import shutil

logger = logging.getLogger("braincode_loop")

SEED_DOCS_DIR = os.path.join(os.path.dirname(__file__), "seed_docs")
SEED_DOC_FILES = ("language-spec.md", "glossary.md", "backlog.md", "changelog.md")
RUN_OUTPUTS = ("kpi_history.jsonl", "budget_log.json")
LOOP_OWNED_DOC_FILES = ("notes-status.json",)  # loop state kept in docs/ but not seeded from a template
BASELINE_FILES = ("language-spec.md", "glossary.md")
_SPRINT_STAMP_RE = re.compile(r"sprint (\d+), version", re.IGNORECASE)
_VERSION_DIR_RE = re.compile(r"^v(\d+)$", re.IGNORECASE)
_AUTO_LOGGED_HEADING = "## Sources found during sprints (auto-logged)"


def _new_archive_dir(runs_abs: str) -> str:
    stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(runs_abs, "archive", f"reset_{stamp}")
    n = 1
    while os.path.exists(path):  # two resets in the same second
        n += 1
        path = os.path.join(runs_abs, "archive", f"reset_{stamp}_{n}")
    return path


def reset_workspace(base_dir: str, docs_dir: str = "docs", runs_dir: str = "runs",
                    sources_path: str = "sources/previous_work.md") -> list[str]:
    actions: list[str] = []
    docs_abs = os.path.join(base_dir, docs_dir)
    runs_abs = os.path.join(base_dir, runs_dir)
    archive = _new_archive_dir(runs_abs)

    def _archive(path: str, rel: str) -> None:
        dest = os.path.join(archive, rel)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.move(path, dest)
        actions.append(f"archived {rel} -> {os.path.relpath(dest, base_dir)}")

    os.makedirs(docs_abs, exist_ok=True)
    for name in SEED_DOC_FILES:
        path = os.path.join(docs_abs, name)
        if os.path.exists(path):
            _archive(path, f"{docs_dir}/{name}")
        shutil.copyfile(os.path.join(SEED_DOCS_DIR, name), path)
        actions.append(f"restored {docs_dir}/{name}")
    for name in LOOP_OWNED_DOC_FILES:
        path = os.path.join(docs_abs, name)
        if os.path.exists(path):
            _archive(path, f"{docs_dir}/{name}")

    for name in RUN_OUTPUTS:
        path = os.path.join(runs_abs, name)
        if os.path.exists(path):
            _archive(path, f"{runs_dir}/{name}")

    sources_abs = os.path.join(base_dir, sources_path)
    if os.path.exists(sources_abs):
        with open(sources_abs, "r", encoding="utf-8") as f:
            content = f.read()
        idx = content.find(_AUTO_LOGGED_HEADING)
        if idx != -1:
            head = content[:idx]
            body = content[idx:]
            logged_rows = re.findall(r"(?m)^- \*\*.*$", body)
            if logged_rows:
                os.makedirs(archive, exist_ok=True)
                with open(os.path.join(archive, "sources_auto_logged.md"), "w", encoding="utf-8") as f:
                    f.write(f"{_AUTO_LOGGED_HEADING}\n\n" + "\n".join(logged_rows) + "\n")
                actions.append(f"archived {len(logged_rows)} auto-logged source row(s)")
            body = re.sub(r"(?m)^- \*\*.*$\n?", "", body)  # drop logged rows (archived above)
            if "*(Empty at seed.)*" not in body:
                body = body.rstrip() + "\n\n*(Empty at seed.)*\n"
            with open(sources_abs, "w", encoding="utf-8") as f:
                f.write(head + body)
            actions.append(f"emptied auto-logged section of {sources_path}")

    for a in actions:
        logger.info("reset: %s", a)
    return actions


def resolve_baseline_dir(src_dir: str) -> str:
    """The folder holding the baseline's language-spec.md + glossary.md: `src_dir` itself, or —
    for a versioned products folder — its highest-numbered vN/ subfolder that has both files."""
    src_abs = os.path.abspath(src_dir)
    if all(os.path.exists(os.path.join(src_abs, n)) for n in BASELINE_FILES):
        return src_abs
    versions = []
    if os.path.isdir(src_abs):
        for entry in os.listdir(src_abs):
            m = _VERSION_DIR_RE.match(entry)
            sub = os.path.join(src_abs, entry)
            if m and all(os.path.exists(os.path.join(sub, n)) for n in BASELINE_FILES):
                versions.append((int(m.group(1)), sub))
    if not versions:
        raise FileNotFoundError(
            f"baseline folder {src_abs} has neither {' + '.join(BASELINE_FILES)} nor a vN/ subfolder containing them"
        )
    return max(versions)[1]


def import_baseline(base_dir: str, src_dir: str, docs_dir: str = "docs", runs_dir: str = "runs",
                    sources_path: str = "sources/previous_work.md") -> list[str]:
    """Reset, then start from an existing product instead of the empty seed spec. The product's
    files are only copied, never modified. Only the spec and glossary are imported — the changelog
    and backlog start fresh (the previous ones are archived by the reset) with one Baseline entry
    recording where sprint numbering resumes."""
    src_abs = resolve_baseline_dir(os.path.join(base_dir, src_dir))

    actions = reset_workspace(base_dir, docs_dir=docs_dir, runs_dir=runs_dir, sources_path=sources_path)
    docs_abs = os.path.join(base_dir, docs_dir)
    for name in BASELINE_FILES:
        shutil.copyfile(os.path.join(src_abs, name), os.path.join(docs_abs, name))
        actions.append(f"imported {docs_dir}/{name} from {src_abs}")

    with open(os.path.join(docs_abs, "language-spec.md"), "r", encoding="utf-8") as f:
        spec = f.read()
    version = re.search(r"\*\*Version:\*\*\s*(\d+\.\d+\.\d+)", spec)
    last_sprint = max((int(n) for n in _SPRINT_STAMP_RE.findall(spec)), default=0)
    with open(os.path.join(docs_abs, "changelog.md"), "a", encoding="utf-8") as f:
        f.write(
            f"\n## Baseline — imported v{version.group(1) if version else '?'} from `{src_abs}` — "
            f"{datetime.date.today().isoformat()}\n\n"
            f"- **Continues from sprint:** {last_sprint}\n"
            f"- Spec and glossary imported as-is; earlier sprint history is not carried into this "
            f"changelog.\n"
        )
    for name in BASELINE_FILES:
        logger.info("import: %s/%s from %s", docs_dir, name, src_abs)
    logger.info("import: baseline changelog entry written (continues from sprint %d)", last_sprint)
    actions.append(f"baseline changelog entry written (continues from sprint {last_sprint})")
    return actions


def snapshot_docs(base_dir: str, docs_dir: str, run_id: str) -> str | None:
    """Copy the current docs/ state (language-spec.md, glossary.md, backlog.md, changelog.md)
    into <base_dir>/braincode_loop/seed_docs/runs/<run_id>/, so a run's documentation output
    survives even after a later `--reset` wipes docs/ back to the pristine template, or a later
    run overwrites it further. `run_id` should match the same run identifier already used for
    runs/logs/run_<run_id>/ (see orchestrator.py::Orchestrator.run()), so a run's logs and its doc
    snapshot are correlated by the same name.

    Deliberately resolved from `base_dir`, NOT from `SEED_DOCS_DIR` (this module's own `__file__`
    location) — unlike reset_workspace()'s read of the pristine templates (correctly shared/
    static across every base_dir), this is a WRITE of per-run output, and must land inside
    whichever project instance is actually running (e.g. a test's isolated tmp_path copy of
    braincode_loop/), never unconditionally into the real installed package's directory.

    Returns the snapshot folder path, or None if nothing in docs/ existed to copy (e.g. docs_dir
    doesn't exist at all yet)."""
    docs_abs = os.path.join(base_dir, docs_dir)
    if not os.path.isdir(docs_abs):
        return None
    dest = os.path.join(base_dir, "braincode_loop", "seed_docs", "runs", run_id)
    os.makedirs(dest, exist_ok=True)
    for name in SEED_DOC_FILES + LOOP_OWNED_DOC_FILES:
        src = os.path.join(docs_abs, name)
        if os.path.exists(src):
            shutil.copyfile(src, os.path.join(dest, name))
    return dest
