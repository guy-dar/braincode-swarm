"""Where the loop's files live and how they are named, assembled and parsed —
shared by loop.py, translate_batch.py, migrate.py and inspector.py so the
naming contract (doc_formats/) is implemented exactly once.

Translator id: `<batch_id>-<tnum_inside_batch>`, both 1-based and unpadded
(`7-23` is the 23rd translator of batch 7). It is the file name stem of every
per-translator file.
"""
import json
import re
from datetime import datetime, timezone
from pathlib import Path

SELF_DIR = Path(__file__).resolve().parent
DATA_DIR = SELF_DIR / "data"
REFERENCE_DIR = SELF_DIR / "reference"
TRANSLATIONS_DIR = SELF_DIR / "translations"
SUCCESS_DIR = TRANSLATIONS_DIR / "successful"
FAILED_DIR = TRANSLATIONS_DIR / "failed"
SUGGESTIONS_DIR = SELF_DIR / "translator_suggestions"
COUNTS_CSV = SUGGESTIONS_DIR / "suggestion_counts.csv"
MIGRATIONS_DIR = SELF_DIR / "migrations"
RUNS_DIR = SELF_DIR / "runs"
PLAN_PATH = RUNS_DIR / "plan.jsonl"
STATE_PATH = RUNS_DIR / "loop_state.json"
HISTORY_DIR = REFERENCE_DIR / "history"
PROVENANCE_PATH = REFERENCE_DIR / "glossary-provenance.jsonl"
FAILURES_DIR = SELF_DIR / "failures" / "loop"
DOC_FORMATS_DIR = SELF_DIR / "doc_formats"
KIT_DIR = SELF_DIR / "kit"
TASKS_DIR = SELF_DIR / "tasks"

DATASETS = ("mind2web", "alfred", "swebench", "prism", "paths", "thoughttrace")

SUGGESTION_HEAD_RE = re.compile(
    r"^###\s+S(?P<n>\d+)\s*\|\s*type:\s*(?P<type>add|refine)\s*\|\s*dimension:\s*(?P<dim>[a-z\-]+)\s*\|\s*"
    r"(?P<field>symbol|target):\s*(?P<value>.+?)\s*$", re.M)
LOOSE_HEAD_RE = re.compile(r"^###\s+S\d+\b.*$", re.M)
ADD_DIMENSIONS = {"vocabulary-member", "member-family", "constructor", "composite", "lexical-group"}
REFINE_DIMENSIONS = {"refine-entry", "resolve-overlap"}
STATUS_RE = re.compile(r"^\s*Status:\s*(success|failed)\s*$", re.I)


# ---------------------------------------------------------------------- ids

def translator_id(batch_id: int, tnum: int) -> str:
    return f"{int(batch_id)}-{int(tnum)}"


def parse_translator_id(tid: str):
    m = re.match(r"^(\d+)-(\d+)$", tid)
    return (int(m.group(1)), int(m.group(2))) if m else None


def batch_file_re(batch_id: int):
    """Exactly this batch's per-translator files: batch 1 never matches 10-12.md."""
    return re.compile(rf"^{int(batch_id)}-\d+\.md$")


def batch_tag(batch_id: int) -> str:
    return f"batch-{int(batch_id):03d}"


# ---------------------------------------------------------------------- paths

def success_path(dataset: str, tid: str) -> Path:
    return SUCCESS_DIR / dataset / f"{tid}.md"


def failed_path(dataset: str, tid: str) -> Path:
    return FAILED_DIR / dataset / f"{tid}.md"


def suggestions_path(tid: str) -> Path:
    return SUGGESTIONS_DIR / f"{tid}.md"


def finished_path(dataset: str, tid: str):
    """The routed translation for this translator, if it already finished."""
    for path in (success_path(dataset, tid), failed_path(dataset, tid)):
        if path.exists():
            return path
    return None


def batch_suggestion_files(batch_id: int) -> list:
    if not SUGGESTIONS_DIR.is_dir():
        return []
    pattern = batch_file_re(batch_id)
    files = [p for p in SUGGESTIONS_DIR.iterdir() if p.is_file() and pattern.match(p.name)]
    return sorted(files, key=lambda p: parse_translator_id(p.stem)[1])


# ---------------------------------------------------------------------- plan

def load_plan(path: Path = PLAN_PATH) -> list:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def plan_batches(plan: list) -> dict:
    batches = {}
    for row in plan:
        batches.setdefault(int(row["batch_id"]), []).append(row)
    return dict(sorted(batches.items()))


def item_id(row: dict) -> str:
    try:
        return str(json.loads(row["record_line"]).get("id") or "")
    except (ValueError, TypeError):
        return ""


def item_content(row: dict) -> str:
    try:
        record = json.loads(row["record_line"])
        content = record.get("content")
        if isinstance(content, str) and content.strip():
            return content
    except (ValueError, TypeError):
        pass
    return row["record_line"]


# ---------------------------------------------------------------------- parsing

def parse_status(text: str):
    for line in text.splitlines():
        if line.strip():
            m = STATUS_RE.match(line)
            return m.group(1).lower() if m else None
    return None


def parse_suggestions(text: str) -> list:
    """[{n, type, dimension, field, value}] for every well-formed heading."""
    return [{"n": int(m.group("n")), "type": m.group("type"), "dimension": m.group("dim"),
             "field": m.group("field"), "value": m.group("value")}
            for m in SUGGESTION_HEAD_RE.finditer(text)]


def suggestion_problems(text: str) -> list:
    """Why a suggestions body is unusable (empty list = fine). Strict, because
    the inspector's counts and the migrator's references both key off these
    headings."""
    problems = []
    parsed = parse_suggestions(text)
    loose = LOOSE_HEAD_RE.findall(text)
    if not parsed:
        problems.append("no well-formed '### S<k> | type: … | dimension: … | symbol|target: …' heading")
    if len(loose) != len(parsed):
        good = {m.group(0) for m in SUGGESTION_HEAD_RE.finditer(text)}
        bad = [h for h in loose if h not in good]
        problems.append("malformed suggestion heading(s): " + "; ".join(bad[:3]))
    numbers = [s["n"] for s in parsed]
    if len(numbers) != len(set(numbers)):
        problems.append("suggestion numbers are not unique")
    for s in parsed:
        allowed = ADD_DIMENSIONS if s["type"] == "add" else REFINE_DIMENSIONS
        if s["dimension"] not in allowed:
            problems.append(f"S{s['n']}: dimension {s['dimension']!r} is not valid for type {s['type']}")
        if s["type"] == "add" and s["field"] != "symbol":
            problems.append(f"S{s['n']}: an add names `symbol:`")
        if s["type"] == "refine" and s["field"] != "target":
            problems.append(f"S{s['n']}: a refine names `target:`")
    return problems


def header_field(text: str, name: str) -> str:
    m = re.search(rf"^- {re.escape(name)}:\s*(.+)$", text, re.M)
    return m.group(1).strip() if m else ""


# ---------------------------------------------------------------------- assembly

def _fence(text: str) -> str:
    longest = max((len(m) for m in re.findall(r"`{3,}", text)), default=2)
    return "`" * max(3, longest + 1)


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def compose_translation(meta: dict, numbered_item: str, body: str) -> str:
    """Final translation document: host header + original item + translator body."""
    status = meta["status"]
    fence = _fence(numbered_item)
    lines = [
        f"# Translation {meta['translator_id']} — {status}",
        "",
        f"- Translator ID: {meta['translator_id']}",
        f"- Batch: {meta['batch_id']}",
        f"- Dataset: {meta['dataset']}",
        f"- Item ID: {meta['item_id']}",
        f"- Glossary version: {meta['glossary_version']} (sha {meta['glossary_sha'][:12]})",
        f"- Model: {meta['model']}",
        f"- Translated at: {meta.get('at') or now_iso()}",
        f"- Needs: {meta['needs_count']} (decomposition: {meta['needs_method']})",
        "",
        "## Original data item",
        "",
        f"{fence}text",
        numbered_item,
        fence,
        "",
        "## Translation",
        "",
        body.strip(),
        "",
    ]
    return "\n".join(lines)


def compose_suggestions(meta: dict, body: str) -> str:
    lines = [
        f"# Suggestions from translator {meta['translator_id']}",
        "",
        f"- Translator ID: {meta['translator_id']}",
        f"- Batch: {meta['batch_id']}",
        f"- Dataset: {meta['dataset']}",
        f"- Item ID: {meta['item_id']}",
        f"- Glossary version: {meta['glossary_version']} (sha {meta['glossary_sha'][:12]})",
        f"- Translation: translations/failed/{meta['dataset']}/{meta['translator_id']}.md",
        "",
        body.strip(),
        "",
    ]
    return "\n".join(lines)
