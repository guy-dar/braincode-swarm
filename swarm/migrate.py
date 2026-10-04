#!/usr/bin/env python3
"""Migrate one batch's suggestions into the glossary.

A. Pre-migrators (translator-class model, up to 5 in parallel): the batch's
   suggestion files are split into up to 5 groups of up to 6; each group is
   merged into one merged suggestion file (tasks/premigrator.md). No
   glossary access. Every input suggestion must be accounted for; an unusable
   result gets one retry, then a host-made pass-through stands in.
B1. Consolidate (MIGRATOR_MODEL): the merged files become one consolidated
   suggestion file, blocks C#S1… (tasks/migrator_consolidate.md). Same
   accounting rule; fallback is a host-made pass-through.
    Host pre-search: for every consolidated suggestion, the closest existing
   glossary entries (RAG), attached to the next steps.
B2. Drafters (translator-class model, up to 5 in parallel): each turns a
   slice of the consolidated suggestions into draft ops (tasks/drafter.md).
   The host validates every draft op on its own and notes the result.
B3. Review (MIGRATOR_MODEL): approve / replace / drop every draft, add missing
   ops (tasks/migrator_review.md). The host assembles the final ops, applies
   them in memory, validates (schema, references, acyclic expansions, nothing
   removed, every consolidated suggestion addressed); invalid -> one repair
   round of the review; still invalid -> nothing installed.
Install: snapshot to reference/history/batch-NNN/, write glossary.jsonl,
   append provenance (mapped back C -> M -> translator suggestions), bump
   the version, re-render glossary.md, refresh the manifest, reload the RAG.

Every agent gets its inputs attached to its first message, and streams a live
progress log (one line per turn / tool call / model reply, with token usage)
to migrations/batch-NNN/<stage>/progress.log.

    python migrate.py --batch 3        # standalone (re-)run of one batch's migration
"""
import argparse
import json
import math
import random
import re
import shutil
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import loop_files as lf
import utils
from glossary import manifest
from glossary import records as rec_mod
from glossary import schema
from glossary import render
from translate_batch import fill_template, run_container_logged, snapshot_reference

MIGRATOR_REFERENCE_FILES = ("language-spec.md", "language-spec.compact.md", "purpose.md", "glossary.jsonl",
                            "glossary.md", "examples.jsonl")
# Pre-migrators merge suggestions with each other only: no glossary.
PREMIGRATOR_REFERENCE_FILES = ("language-spec.compact.md", "purpose.md")
MAX_PREMIGRATORS = 5
FILES_PER_PREMIGRATOR = 6
MAX_DRAFTERS = 5
PRESEARCH_PER_SUGGESTION = 6

REF_RE = re.compile(r"\b(?:\d+-\d+|M\d+|C)#S\d+\b")
SOURCES_RE = re.compile(r"^-\s*Sources:\s*(.+)$", re.M)
NOT_CARRIED_RE = re.compile(r"^##\s+Not carried forward\s*$(.*?)(?=^##\s|\Z)", re.M | re.S)
PROPOSED_RE = re.compile(r"^-\s*Proposed record:\s*(.+)$", re.M)


# ---------------------------------------------------------------------- refs and accounting

def suggestion_refs(files: list) -> list:
    refs = []
    for path in files:
        for s in lf.parse_suggestions(path.read_text(encoding="utf-8", errors="replace")):
            refs.append({"ref": f"{path.stem}#S{s['n']}", "type": s["type"], "dimension": s["dimension"],
                         "value": s["value"]})
    return refs


def group_files(files: list, max_groups: int = MAX_PREMIGRATORS, per_group: int = FILES_PER_PREMIGRATOR) -> list:
    """Split suggestion files into up to `max_groups` near-equal groups of up
    to `per_group` (more per group only if a batch has more than
    max_groups*per_group files). Files are ordered by dataset first, so a
    group tends to hold related items whose suggestions overlap."""
    if not files:
        return []

    def key(p):
        text = p.read_text(encoding="utf-8", errors="replace")
        return (lf.header_field(text, "Dataset"), lf.parse_translator_id(p.stem) or (0, 0))
    return _split_even(sorted(files, key=key), min(max_groups, math.ceil(len(files) / per_group)))


def _split_even(items: list, n_groups: int) -> list:
    n_groups = max(1, min(n_groups, len(items)))
    size, extra = divmod(len(items), n_groups)
    groups, start = [], 0
    for g in range(n_groups):
        end = start + size + (1 if g < extra else 0)
        groups.append(items[start:end])
        start = end
    return groups


def blocks_of(text: str) -> list:
    """[{n, type, dimension, field, value, body, sources}] for each suggestion block."""
    heads = list(lf.SUGGESTION_HEAD_RE.finditer(text))
    out = []
    for i, m in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        body = text[m.end():end]
        not_carried_m = NOT_CARRIED_RE.search(body)
        if not_carried_m:
            body = body[:not_carried_m.start()]
        src = SOURCES_RE.search(body)
        out.append({"n": int(m.group("n")), "type": m.group("type"), "dimension": m.group("dim"),
                    "field": m.group("field"), "value": m.group("value"), "head": m.group(0), "body": body,
                    "sources": REF_RE.findall(src.group(1)) if src else []})
    return out


def not_carried(text: str) -> list:
    m = NOT_CARRIED_RE.search(text)
    if not m:
        return []
    refs = []
    for line in m.group(1).splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells and REF_RE.fullmatch(cells[0] or ""):
            refs.append(cells[0])
    return refs


def _ref_key(ref: str):
    head, _, n = ref.partition("#S")
    return ([int(x) for x in re.findall(r"\d+", head)], int(n or 0))


def accounting_problems(text: str, input_refs: list) -> list:
    """Why a merged/consolidated file doesn't account for its inputs."""
    problems = list(lf.suggestion_problems(text))
    expected = set(input_refs)
    covered = set()
    for b in blocks_of(text):
        if not b["sources"]:
            problems.append(f"S{b['n']} has no `- Sources:` line")
        for ref in b["sources"]:
            if ref not in expected:
                problems.append(f"S{b['n']} names unknown source {ref}")
            covered.add(ref)
    dropped = set(not_carried(text))
    for ref in dropped - expected:
        problems.append(f"'Not carried forward' names unknown source {ref}")
    missing = sorted(expected - covered - dropped, key=_ref_key)
    if missing:
        problems.append("inputs not accounted for (neither in Sources nor Not carried forward): " + ", ".join(missing))
    return problems


def passthrough(title: str, blocks_with_refs: list) -> str:
    """A host-made stand-in for an agent that failed twice: every input block
    carried over unmerged, each naming its own source."""
    lines = [title, "", "- Note: pass-through made by the host (the agent's output was unusable); not merged.", ""]
    for k, (ref, b) in enumerate(blocks_with_refs, 1):
        lines.append(f"### S{k} | type: {b['type']} | dimension: {b['dimension']} | {b['field']}: {b['value']}")
        lines.append(f"- Sources: {ref}")
        lines.append(SOURCES_RE.sub("", b["body"]).strip("\n"))
        lines.append("")
    return "\n".join(lines)


def source_map(texts: dict) -> dict:
    """{"<gid>#S<k>": [source refs]} for merged ({"M2": text}) or consolidated ({"C": text}) files."""
    return {f"{gid}#S{b['n']}": list(b["sources"]) for gid, text in texts.items() for b in blocks_of(text)}


def chain_sources(c_sources: dict, m_sources: dict) -> dict:
    """C refs -> original translator suggestions, through the merged files."""
    out = {}
    for c_ref, m_refs in c_sources.items():
        origs = []
        for m in m_refs:
            for o in m_sources.get(m, [m]):
                if o not in origs:
                    origs.append(o)
        out[c_ref] = origs
    return out


# ---------------------------------------------------------------------- ops

def parse_ops(text: str, name: str = "ops.jsonl") -> tuple:
    ops, errors = [], []
    for n, line in enumerate(text.splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("//"):
            continue
        try:
            op = json.loads(line)
        except ValueError as e:
            errors.append(f"{name} line {n}: invalid JSON ({e})")
            continue
        if not isinstance(op, dict):
            errors.append(f"{name} line {n}: not a JSON object")
            continue
        ops.append(op)
    return ops, errors


def hint_edits(hints: dict) -> list:
    """rag_hints.json -> [(record id, field, values)]."""
    edits = []
    if not isinstance(hints, dict):
        return edits
    for field in ("aliases", "related"):
        for rid, values in (hints.get(field) or {}).items():
            if values:
                edits.append((rid, field, [str(v) for v in values]))
    return edits


def _op_refs(op: dict) -> list:
    raw = op.get("suggestions", op.get("suggestion", []))
    return [raw] if isinstance(raw, str) else list(raw or [])


def evaluate_ops(ops: list, records: list, refs: list, batch_id: int, sources: dict = None,
                 hints: dict = None) -> dict:
    """Apply and validate final ops. `refs` are the suggestions the ops must
    address (consolidated refs); `sources` maps each to the original
    translator suggestions for provenance. Returns {ok, errors, soft,
    new_records, report, ops}."""
    out = {"ok": False, "errors": [], "soft": [], "new_records": None, "report": [], "ops": ops}
    addressed = {r for op in ops for r in _op_refs(op)}
    missing = [r["ref"] for r in refs if r["ref"] not in addressed]
    if missing:
        out["soft"].append("suggestions not addressed by any op: " + ", ".join(missing))
    applied = ops
    if sources:
        applied = []
        for op in ops:
            expanded = []
            for ref in _op_refs(op):
                for orig in sources.get(ref, [ref]):
                    if orig not in expanded:
                        expanded.append(orig)
            applied.append({**op, "suggestions": expanded})
    try:
        new_records, report = rec_mod.apply_ops(records, applied, batch=batch_id,
                                                migration_ref=f"migrations/{lf.batch_tag(batch_id)}.md")
        ids = rec_mod.by_id(new_records)
        for rid, field, values in hint_edits(hints or {}):
            target = ids.get(rid)
            if target is None:
                out["soft"].append(f"rag_hints.json: no record {rid} (hint ignored)")
                continue
            added = [v for v in values if v not in (target.get(field) or []) and v != rid
                     and (field != "related" or v in ids)]
            if added:
                target[field] = list(target.get(field) or []) + added
                rec_mod._bump(target)
                report.append({"op": "hint", "target": rid, "targets": [rid], "suggestions": [],
                               "translator_ids": [], "outcome": f"rag hint: {field} += {', '.join(added)}"})
        out["new_records"], out["report"] = new_records, report
        out["errors"] += rec_mod.validate(new_records, previous=records)
    except rec_mod.OpError as e:
        out["errors"].append(str(e))
    out["ok"] = not out["errors"]
    return out


VALUE_IN_SYMBOL_RE = re.compile(r"(^|_)\d+(_|$)|\d+(gb|tb|mb|kg|km|min|h|plus)\b")


def check_single_op(op: dict, records: list) -> str:
    """'ok' or why this op alone wouldn't apply/validate against the glossary,
    plus a warning when a new value/composite symbol carries a value in its name."""
    try:
        new, _ = rec_mod.apply_ops(records, [op])
    except rec_mod.OpError as e:
        return f"cannot apply: {e}"
    errors = rec_mod.validate(new, previous=records)
    note = "ok" if not errors else "; ".join(errors[:4])
    rec = op.get("record") if op.get("op") == "add" else None
    if isinstance(rec, dict) and rec.get("kind") in ("value", "composite") \
            and VALUE_IN_SYMBOL_RE.search(str(rec.get("symbol", "")).lower()):
        note += ("; WARNING: the symbol bakes a value into its name; use measure/at_least/at_most/character_trait/"
                 "requirement with an argument instead (proper names excepted)")
    return note


def install(new_records: list, batch_id: int, retriever, note: str, report: list = None) -> str:
    tag = lf.batch_tag(batch_id)
    snap = lf.HISTORY_DIR / tag
    snap.mkdir(parents=True, exist_ok=True)
    for name in ("glossary.jsonl", "glossary.md", "reference-manifest.json"):
        src = lf.REFERENCE_DIR / name
        if src.exists():
            shutil.copy2(src, snap / name)
    rec_mod.save(new_records)
    if report:
        rec_mod.append_provenance(rec_mod.provenance_events(report, batch_id, f"migrations/{tag}.md"))
    version = manifest.bump_version(note=note, batch=batch_id)
    render.render_all(new_records, version)
    manifest.refresh()
    if retriever is not None:
        retriever.reload()
    return version


# ---------------------------------------------------------------------- running agents

def run_agent(stage_dir: Path, name: str, task: str, values: dict, model: str, image: str, cfg, trajectory: str,
              attachments: dict, mounts: list = (), reference_files=MIGRATOR_REFERENCE_FILES, rag: bool = False,
              timeout_s: int = None, memory: str = "1g", extra_prompt: str = "", log=print) -> dict:
    """Run one migration agent: inputs attached to its first message, a live
    progress log at <stage_dir>/progress.log, outputs copied to
    <stage_dir>/output/. Returns {output, returncode, error, duration_s, usage}."""
    stage_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=f"mig-{name}-") as work:
        work = Path(work)
        ref = snapshot_reference(work / "reference", reference_files)
        attach = work / "attach"
        attach.mkdir()
        for i, (fname, content) in enumerate(attachments.items(), 1):
            target = attach / f"{i}-{fname}"
            if isinstance(content, Path):
                shutil.copy2(content, target)
            else:
                target.write_text(content, encoding="utf-8")
        (work / "trajectory.txt").write_text(trajectory, encoding="utf-8")
        prompt = fill_template((lf.TASKS_DIR / task).read_text(encoding="utf-8"), values) + extra_prompt
        (work / "prompt.md").write_text(prompt, encoding="utf-8")
        scratch = work / "out"
        scratch.mkdir()
        (work / "session").mkdir()
        uid, gid = utils.host_uid_gid() or (None, None)
        container = f"swarm-mig-{name}-{random.randint(1000, 9999)}"
        cmd = utils.build_docker_cmd(
            uid, gid, model, ref, work / "trajectory.txt", work / "prompt.md", scratch, image,
            container_name=container, add_host=True, memory=memory,
            extra_mounts=[*mounts, (attach, "/attach"), (lf.DOC_FORMATS_DIR, "/doc_formats")]
            + ([(lf.KIT_DIR, "/kit")] if rag else []),
            extra_env={"PI_JSON": "1", "RAG_PORT": cfg.rag_port, "PI_SESSION_DIR": "/session"},
            writable_mounts=[(work / "session", "/session")])
        proc, duration, usage = run_container_logged(cmd, container, timeout_s or cfg.migrator_timeout_s,
                                                     stage_dir / "progress.log")
        out_dir = stage_dir / "output"
        if out_dir.exists():
            shutil.rmtree(out_dir)
        shutil.copytree(scratch, out_dir)
        (stage_dir / "stderr.log").write_text(proc.stderr or "", encoding="utf-8")
        (stage_dir / "usage.json").write_text(json.dumps(usage), encoding="utf-8")
        from translate_batch import keep_session
        keep_session(work / "session", stage_dir / "session.jsonl")   # full transcript (show_session.py)
    error = utils.last_error_line(proc.stderr or "") or ""
    return {"output": out_dir, "returncode": proc.returncode, "error": error, "duration_s": round(duration, 1),
            "usage": usage}


def _usage_total(stages_dir: Path) -> dict:
    total = {"calls": 0, "input": 0, "cacheRead": 0, "output": 0, "reasoning": 0}
    for path in stages_dir.rglob("usage.json"):
        try:
            u = json.loads(path.read_text(encoding="utf-8"))
        except ValueError:
            continue
        for k in total:
            total[k] += u.get(k, 0)
    return total


def _common_attachments() -> dict:
    return {"language-spec.md": lf.REFERENCE_DIR / "language-spec.compact.md",
            "purpose.md": lf.REFERENCE_DIR / "purpose.md"}


def _evidence_dirs(work: Path, files: list) -> tuple:
    sugg_dir, trans_dir = work / "suggestions", work / "translations"
    sugg_dir.mkdir(parents=True, exist_ok=True)
    trans_dir.mkdir(parents=True, exist_ok=True)
    for path in files:
        shutil.copy2(path, sugg_dir / path.name)
        dataset = lf.header_field(path.read_text(encoding="utf-8", errors="replace"), "Dataset")
        failed = lf.failed_path(dataset, path.stem) if dataset else None
        if failed and failed.exists():
            shutil.copy2(failed, trans_dir / path.name)
    return sugg_dir, trans_dir


# ---------------------------------------------------------------------- A: pre-migrators

def run_premigrator(batch_id: int, group_id: str, files: list, cfg, image: str, raw_dir: Path, log=print) -> dict:
    input_refs = [r["ref"] for r in suggestion_refs(files)]
    stage = raw_dir / "premigration" / group_id
    with tempfile.TemporaryDirectory(prefix=f"pre-{batch_id}-{group_id}-") as work:
        sugg_dir, trans_dir = _evidence_dirs(Path(work), files)
        trajectory = (f"# Batch {batch_id}, group {group_id}: {len(files)} suggestion files, {len(input_refs)} "
                      f"suggestions\n\n" + "\n\n---\n\n".join(p.read_text(encoding="utf-8", errors="replace")
                                                             for p in files))
        attachments = {**_common_attachments(),
                       "merged_suggestions.md": lf.DOC_FORMATS_DIR / "merged_suggestions.md",
                       "suggestions.md": lf.DOC_FORMATS_DIR / "suggestions.md"}
        problems = []
        for attempt in (1, 2):
            extra = ("" if not problems else "\n\n## Your previous attempt was rejected\n\nFix every problem and "
                     "write the complete `/output/merged.md` again:\n\n" + "\n".join(f"- {p}" for p in problems))
            res = run_agent(stage / f"attempt{attempt}", f"pre-{batch_id}-{group_id}-{attempt}", "premigrator.md",
                            {"GROUP": group_id, "BATCH_ID": batch_id, "N_FILES": len(files)}, cfg.model, image, cfg,
                            trajectory, attachments, mounts=[(sugg_dir, "/suggestions"), (trans_dir, "/translations")],
                            reference_files=PREMIGRATOR_REFERENCE_FILES, timeout_s=cfg.timeout_s,
                            extra_prompt=extra, log=log)
            merged = res["output"] / "merged.md"
            if not merged.exists():
                problems = ["no /output/merged.md written" + (f" ({res['error']})" if res["error"] else "")]
            elif res["returncode"] != 0:
                problems = [f"harness exited {res['returncode']}" + (f" ({res['error']})" if res["error"] else "")
                            + "; merged.md may be an unfinished draft"]
            else:
                text = merged.read_text(encoding="utf-8", errors="replace")
                problems = accounting_problems(text, input_refs)
                if not problems:
                    n = len(blocks_of(text))
                    log(f"migrate: pre-migrator {group_id}: {len(input_refs)} suggestions from {len(files)} files "
                        f"-> {n} merged ({res['duration_s']:.0f}s)")
                    return {"group": group_id, "text": text, "status": "merged", "inputs": len(input_refs),
                            "blocks": n, "dropped": len(not_carried(text)), "files": [p.stem for p in files]}
            log(f"migrate: pre-migrator {group_id} attempt {attempt} unusable: {'; '.join(problems)[:300]}")
    blocks = [(f"{p.stem}#S{b['n']}", b) for p in files
              for b in blocks_of(p.read_text(encoding="utf-8", errors="replace"))]
    text = passthrough(f"# Merged suggestions {group_id} — batch {batch_id}", blocks)
    log(f"migrate: pre-migrator {group_id} failed twice — passing its {len(input_refs)} suggestions through unmerged")
    return {"group": group_id, "text": text, "status": "passthrough", "inputs": len(input_refs),
            "blocks": len(blocks), "dropped": 0, "files": [p.stem for p in files]}


# ---------------------------------------------------------------------- B1: consolidate

def consolidate(batch_id: int, merged_texts: dict, cfg, image: str, raw_dir: Path, log=print) -> dict:
    m_refs = list(source_map(merged_texts))
    trajectory = (f"# Batch {batch_id}: {len(merged_texts)} merged files, {len(m_refs)} merged suggestions\n\n"
                  + "\n\n---\n\n".join(merged_texts.values()))
    attachments = {f"{gid}.md": text for gid, text in merged_texts.items()}
    attachments.update({**_common_attachments(),
                        "merged_suggestions.md": lf.DOC_FORMATS_DIR / "merged_suggestions.md"})
    problems = []
    for attempt in (1, 2):
        extra = ("" if not problems else "\n\n## Your previous attempt was rejected\n\nFix every problem and write "
                 "the complete `/output/consolidated_suggestions.md` again:\n\n" + "\n".join(f"- {p}" for p in problems))
        res = run_agent(raw_dir / "consolidate" / f"attempt{attempt}", f"con-{batch_id}-{attempt}",
                        "migrator_consolidate.md", {"BATCH_ID": batch_id, "N_MERGED": len(merged_texts)},
                        cfg.migrator_model, image, cfg, trajectory, attachments, memory="2g", extra_prompt=extra,
                        log=log)
        path = res["output"] / "consolidated_suggestions.md"
        if not path.exists():
            problems = ["no /output/consolidated_suggestions.md written" + (f" ({res['error']})" if res["error"] else "")]
        elif res["returncode"] != 0:
            problems = [f"harness exited {res['returncode']}" + (f" ({res['error']})" if res["error"] else "")]
        else:
            text = path.read_text(encoding="utf-8", errors="replace")
            problems = accounting_problems(text, m_refs)
            if not problems:
                log(f"migrate: consolidated {len(m_refs)} merged suggestions -> {len(blocks_of(text))} "
                    f"({res['duration_s']:.0f}s)")
                return {"text": text, "status": "consolidated"}
        log(f"migrate: consolidation attempt {attempt} unusable: {'; '.join(problems)[:300]}")
    blocks = [(f"{gid}#S{b['n']}", b) for gid, text in merged_texts.items() for b in blocks_of(text)]
    log(f"migrate: consolidation failed twice — passing {len(blocks)} merged suggestions through")
    return {"text": passthrough(f"# Consolidated suggestions — batch {batch_id}", blocks), "status": "passthrough"}


def presearch(c_text: str, retriever) -> str:
    """Host pre-search: closest existing glossary entries per consolidated
    suggestion, so drafters and the review rarely need to search themselves."""
    lines = ["# Closest existing glossary entries per consolidated suggestion", "",
             "Found by the host's RAG search on each suggestion's symbol and proposed definition. `exact` = the "
             "proposed symbol (or an alias) already exists.", ""]
    for b in blocks_of(c_text):
        proposed = PROPOSED_RE.search(b["body"])
        meaning = b["value"].replace("_", " ")
        if proposed:
            try:
                rec = json.loads(proposed.group(1).strip().strip("`"))
                meaning += " " + (rec.get("definition") or "")
            except ValueError:
                meaning += " " + proposed.group(1)[:300]
        cands = retriever.search_need(meaning[:500], kind="", k=15, keep=PRESEARCH_PER_SUGGESTION)
        idx = retriever.index
        lines.append(f"## C#S{b['n']} — {b['type']} {b['field']} `{b['value']}`")
        if not cands:
            lines.append("- (no close entries)")
        for c in cands[:PRESEARCH_PER_SUGGESTION + 2]:
            rec = idx.by_id[c["id"]]
            lines.append(f"- `{rec['symbol']}` ({', '.join(c['reasons'])}): {render.compact_line(rec)[:300]}")
        lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------- B2: drafters

def run_drafter(batch_id: int, did: str, blocks: list, c_text: str, matches: str, cfg, image: str, raw_dir: Path,
                log=print) -> dict:
    refs = [f"C#S{b['n']}" for b in blocks]
    slice_text = (f"# Slice {did} of the consolidated suggestions — batch {batch_id}\n\n"
                  + "\n".join(b["head"] + b["body"] for b in blocks))
    wanted = {f"## C#S{b['n']} " for b in blocks}
    match_text = "\n".join(sec for sec in re.split(r"(?=^## C#S)", matches, flags=re.M)
                           if any(sec.startswith(w) for w in wanted))
    attachments = {"slice.md": slice_text, "existing_matches.md": match_text,
                   "migration_ops.md": lf.DOC_FORMATS_DIR / "migration_ops.md", **_common_attachments(),
                   "glossary.md": lf.REFERENCE_DIR / "glossary.md"}
    problems = []
    for attempt in (1, 2):
        extra = ("" if not problems else "\n\n## Your previous attempt was rejected\n\nFix and write the complete "
                 "`/output/ops.jsonl` again:\n\n" + "\n".join(f"- {p}" for p in problems))
        res = run_agent(raw_dir / "drafts" / did / f"attempt{attempt}", f"draft-{batch_id}-{did}-{attempt}",
                        "drafter.md", {"DRAFTER": did, "BATCH_ID": batch_id}, cfg.model, image, cfg, slice_text,
                        attachments, rag=True, timeout_s=cfg.timeout_s, extra_prompt=extra, log=log)
        path = res["output"] / "ops.jsonl"
        if not path.exists():
            problems = ["no /output/ops.jsonl written" + (f" ({res['error']})" if res["error"] else "")]
        elif res["returncode"] != 0:
            problems = [f"harness exited {res['returncode']}" + (f" ({res['error']})" if res["error"] else "")]
        else:
            ops, errors = parse_ops(path.read_text(encoding="utf-8", errors="replace"))
            missing = [r for r in refs if r not in {x for op in ops for x in _op_refs(op)}]
            problems = errors + ([f"suggestions with no op: {', '.join(missing)}"] if missing else [])
            if not errors and (not missing or attempt == 2):
                log(f"migrate: drafter {did}: {len(blocks)} suggestions -> {len(ops)} draft ops "
                    f"({res['duration_s']:.0f}s)")
                return {"drafter": did, "ops": ops, "refs": refs, "status": "drafted"}
        log(f"migrate: drafter {did} attempt {attempt} unusable: {'; '.join(problems)[:300]}")
    return {"drafter": did, "ops": [], "refs": refs, "status": "failed"}


def drafts_document(drafts: list, records: list) -> tuple:
    """(numbered draft ops {D<k>: op}, drafts.md text) with the host's
    validation note on every op, grouped by consolidated suggestion."""
    numbered, by_ref = {}, {}
    k = 0
    for d in drafts:
        for op in d["ops"]:
            k += 1
            did = f"D{k}"
            numbered[did] = op
            for ref in _op_refs(op) or ["(no suggestion)"]:
                by_ref.setdefault(ref, []).append(did)
    lines = ["# Draft operations", "",
             "Each draft op with the host's validation of it on its own against the current glossary.", ""]
    failed = [d["drafter"] for d in drafts if d["status"] != "drafted"]
    if failed:
        lines += [f"Drafters {', '.join(failed)} produced nothing usable; their suggestions have no drafts. "
                  f"Add ops for them.", ""]
    for ref in sorted(by_ref, key=_ref_key):
        lines.append(f"## {ref}")
        for did in by_ref[ref]:
            note = check_single_op(numbered[did], records)
            lines.append(f"- **{did}** ({note}): `{json.dumps(numbered[did], ensure_ascii=False)}`")
        lines.append("")
    return numbered, "\n".join(lines)


# ---------------------------------------------------------------------- B3: review

def assemble(review_text: str, numbered: dict) -> tuple:
    """(final ops, log rows, errors) from review.jsonl. Drafts the review
    doesn't mention are kept (approved by default) and reported."""
    decisions, errors = parse_ops(review_text, "review.jsonl")
    seen, final, rows = set(), [], []
    for i, d in enumerate(decisions, 1):
        decision = d.get("decision")
        did = d.get("draft")
        reason = d.get("reason", "")
        if did is not None and did not in numbered:
            errors.append(f"review.jsonl line {i}: unknown draft {did}")
            continue
        if decision == "approve" and did:
            final.append(numbered[did])
            seen.add(did)
            rows.append((numbered[did], "approved", reason))
        elif decision == "replace" and did and isinstance(d.get("op"), dict):
            final.append(d["op"])
            seen.add(did)
            rows.append((d["op"], f"replaced {did}", reason))
        elif decision == "drop" and did:
            seen.add(did)
            rows.append((numbered[did], f"dropped {did}", reason))
        elif decision == "add" and isinstance(d.get("op"), dict):
            final.append(d["op"])
            rows.append((d["op"], "added in review", reason))
        else:
            errors.append(f"review.jsonl line {i}: decision {decision!r} needs "
                          + ("an `op`" if decision in ("replace", "add") else "a `draft`"))
    for did, op in numbered.items():
        if did not in seen:
            final.append(op)
            rows.append((op, f"kept {did} (not reviewed)", ""))
    return final, rows, errors


def migration_log(rows: list, c_refs: list) -> str:
    lines = ["| suggestion | op | record | decision | reason |", "|---|---|---|---|---|"]
    for op, decision, reason in rows:
        target = (op.get("record") or {}).get("symbol") or op.get("id") or op.get("into") or "—"
        for ref in _op_refs(op) or ["—"]:
            lines.append(f"| {ref} | {op.get('op')} | {target} | {decision} | {str(reason).replace('|', '/')} |")
    return "\n".join(lines)


def review(batch_id: int, c_text: str, matches: str, numbered: dict, drafts_md: str, records: list, refs: list,
           sources: dict, cfg, image: str, raw_dir: Path, log=print) -> tuple:
    attachments = {"drafts.md": drafts_md, "consolidated_suggestions.md": c_text, "existing_matches.md": matches,
                   "migration_ops.md": lf.DOC_FORMATS_DIR / "migration_ops.md", **_common_attachments(),
                   "glossary.md": lf.REFERENCE_DIR / "glossary.md"}
    attempts, previous = [], None
    for attempt in (1, 2):
        extra = ""
        if previous:
            extra = ("\n\n## Repair round\n\nYour previous review produced a glossary that failed validation, so "
                     "nothing was installed. Write the complete corrected `/output/review.jsonl` again (all decisions, "
                     "not a diff), fixing every problem:\n\n" + "\n".join(f"- {e}" for e in previous[:80]))
        stage = raw_dir / "review" / f"attempt{attempt}"
        res = run_agent(stage, f"rev-{batch_id}-{attempt}", "migrator_review.md",
                        {"BATCH_ID": batch_id, "N_DRAFTS": len(numbered)}, cfg.migrator_model, image, cfg,
                        drafts_md, attachments, rag=True, memory="2g", extra_prompt=extra, log=log)
        path = res["output"] / "review.jsonl"
        if not path.exists():
            result = {"ok": False, "errors": ["no /output/review.jsonl written"
                                              + (f" ({res['error']})" if res["error"] else "")], "soft": []}
            rows = []
        else:
            final, rows, errors = assemble(path.read_text(encoding="utf-8", errors="replace"), numbered)
            hints = {}
            hints_path = res["output"] / "rag_hints.json"
            if hints_path.exists():
                try:
                    hints = json.loads(hints_path.read_text(encoding="utf-8"))
                except ValueError:
                    errors.append("rag_hints.json: invalid JSON")
            result = evaluate_ops(final, records, refs, batch_id, sources=sources, hints=hints)
            result["errors"] = errors + result["errors"]
            result["ok"] = not result["errors"]
            if res["returncode"] != 0 and result["ok"]:
                result["errors"].append(f"harness exited {res['returncode']}"
                                        + (f" ({res['error']})" if res["error"] else ""))
                result["ok"] = False
            (stage / "final_ops.jsonl").write_text("".join(json.dumps(o, ensure_ascii=False) + "\n" for o in final),
                                                   encoding="utf-8")
            (stage / "hints.json").write_text(json.dumps(hints), encoding="utf-8")
            result["log"] = migration_log(rows, [r["ref"] for r in refs])
        result["duration_s"] = res["duration_s"]
        attempts.append(result)
        if result["ok"] and (not result["soft"] or attempt == 2):
            return result, attempts
        log(f"migrate: review attempt {attempt} not installable: "
            + "; ".join((result["errors"] + result["soft"])[:4])[:400])
        previous = result["errors"] + result["soft"]
    return None, attempts


# ---------------------------------------------------------------------- report

def write_report(batch_id: int, status: str, refs: list, attempts: list, version_before: str, version_after: str,
                 final: dict = None, premigration: list = None, stats: dict = None) -> Path:
    tag = lf.batch_tag(batch_id)
    lf.MIGRATIONS_DIR.mkdir(parents=True, exist_ok=True)
    counts = {}
    for entry in (final or {}).get("report", []):
        counts[entry["op"]] = counts.get(entry["op"], 0) + 1
    stats = stats or {}
    lines = [
        f"# Migration — batch {batch_id}",
        "",
        f"- Status: **{status}**",
        f"- Glossary version: {version_before} → {version_after}",
        f"- Translator suggestions: {len(refs)} ({sum(r['type'] == 'add' for r in refs)} add, "
        f"{sum(r['type'] == 'refine' for r in refs)} refine)",
        f"- Pipeline: {len(premigration or [])} pre-migrator(s) → {stats.get('merged', '?')} merged → "
        f"{stats.get('consolidated', '?')} consolidated → {stats.get('drafts', '?')} draft ops from "
        f"{stats.get('drafters', '?')} drafter(s) → {len((final or {}).get('ops') or [])} final ops",
        f"- Operations applied: {', '.join(f'{k} {v}' for k, v in sorted(counts.items())) or 'none'}",
        f"- Token usage (all migration agents): {stats.get('usage', {})}",
        f"- Raw output and live progress logs: `migrations/{tag}/`",
        "",
    ]
    if premigration:
        lines += ["## Pre-migration", "", "| group | translator files | suggestions in | merged out | not carried | status |",
                  "|---|---|---:|---:|---:|---|"]
        for p in premigration:
            lines.append(f"| {p['group']} | {', '.join(p['files'])} | {p['inputs']} | {p['blocks']} | {p['dropped']} | "
                         f"{p['status']} |")
        lines.append("")
    for i, att in enumerate(attempts, 1):
        if att.get("errors") or att.get("soft"):
            lines += [f"## Validation, review attempt {i}", ""]
            lines += [f"- {e}" for e in att.get("errors", [])[:60]]
            lines += [f"- (warning) {e}" for e in att.get("soft", [])]
            lines.append("")
    if final and final.get("report"):
        lines += ["## Applied operations", "", "| op | record | translator suggestions | outcome |", "|---|---|---|---|"]
        for e in final["report"]:
            lines.append(f"| {e['op']} | {e['target'] or '—'} | {', '.join(e['suggestions']) or '—'} | "
                         f"{str(e['outcome']).replace('|', '/')} |")
        lines.append("")
    if final and final.get("log"):
        lines += ["## Migration log (review decisions)", "", final["log"], ""]
    path = lf.MIGRATIONS_DIR / f"{tag}.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


# ---------------------------------------------------------------------- the whole migration

def run_migration(batch_id: int, cfg, retriever, image: str, log=print, premigrator_image: str = None) -> dict:
    files = lf.batch_suggestion_files(batch_id)
    version_before = manifest.current_version()
    refs = suggestion_refs(files)
    if not files:
        write_report(batch_id, "skipped (no suggestions)", refs, [], version_before, version_before)
        log(f"migrate: batch {batch_id} has no suggestions — nothing to migrate")
        return {"status": "skipped", "version": version_before}
    flash_image = premigrator_image or image
    records = rec_mod.load()
    tag = lf.batch_tag(batch_id)
    raw_dir = lf.MIGRATIONS_DIR / tag
    if raw_dir.exists():
        shutil.rmtree(raw_dir)
    raw_dir.mkdir(parents=True)

    # A: pre-migrators
    groups = group_files(files)
    log(f"migrate: batch {batch_id}: {len(refs)} suggestions in {len(files)} files -> {len(groups)} pre-migrator(s)")
    with ThreadPoolExecutor(max_workers=len(groups)) as pool:
        premigration = list(pool.map(
            lambda ig: run_premigrator(batch_id, f"M{ig[0]}", ig[1], cfg, flash_image, raw_dir, log),
            enumerate(groups, 1)))
    merged_texts = {p["group"]: p["text"] for p in premigration}
    (raw_dir / "merged").mkdir()
    for gid, text in merged_texts.items():
        (raw_dir / "merged" / f"{gid}.md").write_text(text, encoding="utf-8")
    m_sources = source_map(merged_texts)

    # B1: consolidate
    con = consolidate(batch_id, merged_texts, cfg, image, raw_dir, log)
    c_text = con["text"]
    (raw_dir / "consolidated_suggestions.md").write_text(c_text, encoding="utf-8")
    c_blocks = blocks_of(c_text)
    c_refs = [{"ref": f"C#S{b['n']}", "type": b["type"]} for b in c_blocks]
    sources = chain_sources(source_map({"C": c_text}), m_sources)

    # host pre-search
    matches = presearch(c_text, retriever)
    (raw_dir / "existing_matches.md").write_text(matches, encoding="utf-8")

    # B2: drafters
    slices = _split_even(c_blocks, min(MAX_DRAFTERS, max(1, math.ceil(len(c_blocks) / 4))))
    log(f"migrate: {len(c_blocks)} consolidated suggestions -> {len(slices)} drafter(s)")
    with ThreadPoolExecutor(max_workers=len(slices)) as pool:
        drafts = list(pool.map(
            lambda isl: run_drafter(batch_id, f"D{isl[0]}", isl[1], c_text, matches, cfg, flash_image, raw_dir, log),
            enumerate(slices, 1)))
    numbered, drafts_md = drafts_document(drafts, records)
    (raw_dir / "drafts.md").write_text(drafts_md, encoding="utf-8")

    # B3: review, assemble, install
    result, attempts = review(batch_id, c_text, matches, numbered, drafts_md, records, c_refs, sources, cfg, image,
                              raw_dir, log)
    stats = {"merged": len(m_sources), "consolidated": len(c_blocks), "drafts": len(numbered),
             "drafters": len(slices), "usage": _usage_total(raw_dir)}
    if result is not None:
        note = f"batch {batch_id} migration ({len(result['report'])} ops)"
        version = install(result["new_records"], batch_id, retriever, note, result["report"])
        status = "installed" + (" (with warnings)" if result["soft"] else "")
        (raw_dir / "migration_log.md").write_text(result.get("log", ""), encoding="utf-8")
        path = write_report(batch_id, status, refs, attempts, version_before, version, result, premigration, stats)
        log(f"migrate: batch {batch_id} installed — glossary {version_before} -> {version} "
            f"({len(result['report'])} ops); tokens {stats['usage']}; report {path.relative_to(lf.SELF_DIR)}")
        return {"status": "installed", "version": version, "ops": len(result["report"]), "warnings": result["soft"],
                "usage": stats["usage"]}
    path = write_report(batch_id, "rejected (validation failed twice; glossary unchanged)", refs, attempts,
                        version_before, version_before, attempts[-1] if attempts else None, premigration, stats)
    log(f"migrate: batch {batch_id} NOT installed — glossary unchanged; see {path.relative_to(lf.SELF_DIR)}")
    return {"status": "rejected", "version": version_before, "usage": stats["usage"],
            "errors": attempts[-1].get("errors", []) if attempts else []}


def main(argv=None):
    import loop
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--batch", type=int, required=True)
    p.add_argument("--no-dense", action="store_true")
    args = p.parse_args(argv)
    cfg = loop.load_loop_config()
    with loop.rag_service(cfg, dense=not args.no_dense) as retriever:
        image = loop.build_image(cfg.migrator_harness)
        pre_image = image if cfg.harness_name == cfg.migrator_harness else loop.build_image(cfg.harness_name)
        print(json.dumps(run_migration(args.batch, cfg, retriever, image, premigrator_image=pre_image)))


if __name__ == "__main__":
    main()
