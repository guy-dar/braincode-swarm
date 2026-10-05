#!/usr/bin/env python3
"""Run one batch of translators: one isolated container per plan row, all in
parallel (the batch size is the concurrency), each with its own pre-run
glossary retrieval.

Per translator `<batch_id>-<tnum>`:
  1. host-side retrieval (rag: needs -> candidates -> expanded records)
  2. one `docker run` of the harness with tasks/translator.md
  3. validate /output (Status line; suggestions format on failure), one retry
     if malformed
  4. route: translations/successful|failed/<dataset>/<tid>.md, and
     translator_suggestions/<tid>.md for a failure

Normally driven by loop.py; standalone for re-running one batch:

    python translate_batch.py --batch 3
"""
import argparse
import contextlib
import json
import os
import random
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import traceback
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import loop_files as lf
import utils
from rag import needs as needs_mod
from rag.retrieve import BRAINCODE_BLOCK_RE, render_check, render_context

TIMEOUT_RETURNCODE = -9
# Set when the loop is shutting down: no new container starts, no retry is
# attempted, and an interrupted attempt is not recorded as a failure.
STOPPING = threading.Event()
REFERENCE_FILES = ("language-spec.md", "language-spec.compact.md", "glossary.jsonl", "glossary.md",
                   "examples.jsonl")
# Attached to the translator's first message (harness /attach), in this
# order, so it doesn't spend a model turn reading each one. (source, name)
ATTACH = (("reference:language-spec.compact.md", "1-language-spec.md"),
          ("work:rag_context.md", "2-rag_context.md"),
          ("kit:README.md", "3-kit-README.md"),
          ("formats:successful_translation.md", "4-format-successful_translation.md"),
          ("formats:failed_translation.md", "5-format-failed_translation.md"),
          ("formats:suggestions.md", "6-format-suggestions.md"),
          ("reference:examples.jsonl", "7-examples.jsonl"))


def _decode(stream) -> str:
    if stream is None:
        return ""
    return stream if isinstance(stream, str) else stream.decode("utf-8", "replace")


def snapshot_reference(dest: Path, files=REFERENCE_FILES) -> Path:
    """A frozen copy of exactly the reference files a container may read —
    the whole batch sees one glossary version, and history/ isn't exposed."""
    dest.mkdir(parents=True, exist_ok=True)
    for name in files:
        src = lf.REFERENCE_DIR / name
        if src.exists():
            shutil.copy2(src, dest / name)
    return dest


def run_container(cmd: list, container_name: str, timeout_s: int):
    started = time.monotonic()
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace",
                                timeout=timeout_s)
    except subprocess.TimeoutExpired as expired:
        # Killing `docker run` only detaches the CLI; the container itself
        # has to be killed by name (see spawn_batch.py for the history).
        subprocess.run(["docker", "kill", container_name], capture_output=True, text=True)
        result = subprocess.CompletedProcess(
            cmd, returncode=TIMEOUT_RETURNCODE, stdout=_decode(expired.stdout),
            stderr=_decode(expired.stderr) + f"\nError: timed out after {timeout_s}s and was killed.")
    return result, time.monotonic() - started


def _event_summary(event: dict, turn: list):
    """One progress-log line for a pi JSON event, or None to skip it."""
    kind = event.get("type")
    if kind == "turn_start":
        turn[0] += 1
        return f"turn {turn[0]}"
    if kind == "tool_execution_start":
        args = event.get("args") or {}
        detail = args.get("command") or args.get("path") or json.dumps(args)[:120]
        return f"  tool {event.get('toolName', '?')}: {str(detail)[:160]}"
    if kind == "message_end" and (event.get("message") or {}).get("role") == "assistant":
        u = event["message"].get("usage") or {}
        return (f"  model reply: in {u.get('input', 0)} + cached {u.get('cacheRead', 0)}, "
                f"out {u.get('output', 0)} (+{u.get('reasoning', 0)} reasoning)")
    if kind in ("agent_end", "agent_settled"):
        return "agent finished"
    return None


def run_container_logged(cmd: list, container_name: str, timeout_s: int, progress_path: Path):
    """Like run_container, for a harness started with PI_JSON=1: streams pi's
    JSON events into a timestamped progress log (one line per turn, tool call
    and model reply) and totals token usage. Returns (CompletedProcess,
    duration_s, usage dict)."""
    progress_path.parent.mkdir(parents=True, exist_ok=True)
    usage = {"calls": 0, "input": 0, "cacheRead": 0, "cacheWrite": 0, "output": 0, "reasoning": 0}
    started = time.monotonic()
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8",
                            errors="replace")
    stderr_chunks = []
    reader = threading.Thread(target=lambda: stderr_chunks.append(proc.stderr.read()), daemon=True)
    reader.start()
    killed = threading.Event()

    def watchdog():
        if not killed.wait(timeout_s):
            subprocess.run(["docker", "kill", container_name], capture_output=True, text=True)
            killed.set()
    threading.Thread(target=watchdog, daemon=True).start()
    turn = [0]
    stdout_tail = []
    with progress_path.open("w", encoding="utf-8") as log_fh:
        for line in proc.stdout:
            stdout_tail.append(line)
            stdout_tail[:] = stdout_tail[-200:]
            try:
                event = json.loads(line)
            except ValueError:
                continue
            # In JSON mode a failed model call can surface as an event rather
            # than on stderr; keep it in the `Error:` convention so
            # last_error_line (and the proxy-error backoff) still sees it.
            message = event.get("message") or {}
            err = event.get("errorMessage") or message.get("errorMessage") or (
                event.get("error") if isinstance(event.get("error"), str) else None)
            if err:
                stderr_chunks.append(f"\nError: {str(err)[:300]}")
            if event.get("type") == "message_end" and message.get("role") == "assistant":
                u = message.get("usage") or {}
                usage["calls"] += 1
                for k in ("input", "cacheRead", "cacheWrite", "output", "reasoning"):
                    usage[k] += u.get(k) or 0
            summary = _event_summary(event, turn)
            if summary:
                log_fh.write(f"{time.monotonic() - started:7.1f}s {summary}\n")
                log_fh.flush()
    proc.wait()
    timed_out = killed.is_set()
    killed.set()
    reader.join(timeout=5)
    stderr = "".join(stderr_chunks)
    if timed_out:
        stderr += f"\nError: timed out after {timeout_s}s and was killed."
    result = subprocess.CompletedProcess(cmd, TIMEOUT_RETURNCODE if timed_out else proc.returncode,
                                         stdout="".join(stdout_tail), stderr=stderr)
    return result, time.monotonic() - started, usage


def record_failure(tid: str, attempt: int, result, duration_s: float, problem: str, scratch: Path, cfg) -> Path:
    dest = lf.FAILURES_DIR / f"{tid}-attempt{attempt}"
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    (dest / "stdout.log").write_text(result.stdout or "", encoding="utf-8")
    (dest / "stderr.log").write_text(result.stderr or "", encoding="utf-8")
    partial = [p.name for p in scratch.iterdir()] if scratch.exists() else []
    if partial:
        shutil.copytree(scratch, dest / "partial")
    (dest / "failure.json").write_text(json.dumps({
        "translator_id": tid, "attempt": attempt, "returncode": result.returncode,
        "problem": problem, "partial_files": partial, "duration_s": round(duration_s, 1),
        "error": utils.last_error_line(result.stderr or ""), "model": cfg.model,
        "harness": cfg.harness_name, "timestamp": lf.now_iso(),
    }, indent=2), encoding="utf-8")
    return dest


def validate_output(scratch: Path):
    """(status, translation_body, suggestions_body, problem). problem is None
    when the output is usable."""
    translation = scratch / "translation.md"
    if not translation.exists():
        return None, None, None, "no /output/translation.md written"
    body = translation.read_text(encoding="utf-8", errors="replace")
    status = lf.parse_status(body)
    if status is None:
        return None, body, None, "translation.md does not start with 'Status: success|failed'"
    if "```braincode" not in body:
        return status, body, None, "translation.md has no ```braincode block"
    if not BRAINCODE_BLOCK_RE.search(body):
        return status, body, None, "the ```braincode block is never closed with ```"
    suggestions = scratch / "suggestions.md"
    sugg_body = suggestions.read_text(encoding="utf-8", errors="replace") if suggestions.exists() else None
    if status == "failed":
        if sugg_body is None:
            return status, body, None, "failed translation without /output/suggestions.md"
        problems = lf.suggestion_problems(sugg_body)
        if problems:
            return status, body, sugg_body, "suggestions.md: " + "; ".join(problems)
    return status, body, sugg_body, None


PROXY_BACKOFF_S = (60, 180)
# Sent instead of the full prompt when attempt 2 resumes attempt 1's session.
CONTINUE_PROMPT = (
    "Your previous run stopped before it finished ({problem}). Everything you read and did so far is above, and "
    "anything you already wrote is still in /output. Continue from where you stopped. Don't redo finished work. "
    "Make sure /output/translation.md (and /output/suggestions.md if the translation failed) are complete and in "
    "the required format before you end.")
# Context limits, applied by the harness's context-limits.ts extension:
# every tool result is cut to TOOL_RESULT_MAX_CHARS (whole-category glossary
# greps were 28-51k characters, re-sent on every later turn), and before a
# model call whose context is over COMPACT_AT (estimated) tokens the older
# turns are replaced by a summary; the first message (spec, retrieval,
# formats) stays verbatim and the latest KEEP_RECENT_TOKENS stay as they are.
# The first message alone is ~27-38k tokens, so each compaction folds ~20k+.
TOOL_RESULT_MAX_CHARS = int(os.environ.get("TOOL_RESULT_MAX_CHARS", 8000))
COMPACT_AT = int(os.environ.get("TRANSLATOR_COMPACT_AT", 70000))
KEEP_RECENT_TOKENS = int(os.environ.get("TRANSLATOR_KEEP_RECENT_TOKENS", 12000))
# The extension logs each compaction (with the summary call's usage) here;
# .log, not .jsonl, so it never looks like a pi session to the resume check.
CONTEXT_LOG_NAME = "context-limits.log"
CONTEXT_LIMITS_ENV = {"PI_TOOL_RESULT_MAX_CHARS": TOOL_RESULT_MAX_CHARS, "PI_COMPACT_AT": COMPACT_AT,
                      "PI_KEEP_RECENT_TOKENS": KEEP_RECENT_TOKENS, "PI_CONTEXT_LOG": f"/session/{CONTEXT_LOG_NAME}"}
NEEDS_CACHE_DIR = lf.RUNS_DIR / "needs_cache"
TRANSLATOR_LOG_DIR = lf.RUNS_DIR / "translator_logs"   # live per-attempt progress (turns, tools, tokens)
SESSIONS_DIR = lf.RUNS_DIR / "translator_sessions"     # full pi transcripts, one per translator


def collect_context_log(session_dir: Path, used: dict, dest: Path) -> dict:
    """Fold the context-limits extension's log of one attempt into its usage:
    the compaction summary calls (tokens and calls), plus counts of
    compactions and truncated tool results. The log is moved to `dest` (next
    to the progress log), so the next attempt starts a fresh one."""
    src = session_dir / CONTEXT_LOG_NAME
    out = {k: used.get(k, 0) for k in ("calls", "input", "cacheRead", "cacheWrite", "output", "reasoning")}
    out.update(compactions=0, truncated_tool_results=0)
    if not src.exists():
        return out
    for line in src.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            e = json.loads(line)
        except ValueError:
            continue
        if e.get("event") == "truncated":
            out["truncated_tool_results"] += 1
        elif e.get("event") == "compacted":
            out["compactions"] += 1
            u = e.get("usage") or {}
            if u:
                out["calls"] += 1
                for k in ("input", "cacheRead", "cacheWrite", "output", "reasoning"):
                    out[k] += u.get(k) or 0
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(src), dest)
    return out


def keep_session(session_dir: Path, dest: Path) -> None:
    """Save pi's session transcript(s) from a work dir that is about to be
    deleted: every message the model received and sent, tool calls and tool
    results included (view with show_session.py). Resumed attempts continue
    the same session, so one file normally holds all attempts."""
    files = sorted(session_dir.rglob("*.jsonl")) if session_dir.is_dir() else []
    if not files:
        return
    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open("w", encoding="utf-8") as out:
        for f in files:
            out.write(f.read_text(encoding="utf-8", errors="replace"))


@contextlib.contextmanager
def translator_workdir(tid: str):
    """A translator's temporary work dir; its session transcript is kept
    (runs/translator_sessions/<tid>.jsonl) however the translator ends."""
    with tempfile.TemporaryDirectory(prefix=f"tr-{tid}-") as work:
        try:
            yield work
        finally:
            try:
                keep_session(Path(work) / "session", SESSIONS_DIR / f"{tid}.jsonl")
            except OSError:
                pass


def build_attachments(dest: Path, ref_snapshot: Path, work: Path) -> Path:
    """The files the harness attaches to the translator's first message."""
    dest.mkdir(parents=True, exist_ok=True)
    roots = {"reference": ref_snapshot, "work": work, "kit": lf.KIT_DIR, "formats": lf.DOC_FORMATS_DIR}
    for source, name in ATTACH:
        root, _, rel = source.partition(":")
        src = roots[root] / rel
        if src.exists():
            shutil.copy2(src, dest / name)
    return dest


# ---------------------------------------------------------------------- needs prefetch

def _content_sha(content: str) -> str:
    import hashlib
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def load_cached_needs(tid: str, content: str):
    """Prefetched needs for this translator, if present and for this exact item."""
    path = NEEDS_CACHE_DIR / f"{tid}.json"
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except ValueError:
        return None
    if data.get("content_sha") != _content_sha(content) or not data.get("needs"):
        return None
    if data.get("needs_version") != needs_mod.NEEDS_VERSION:   # older format: extract again
        return None
    return data


def prefetch_needs(rows: list, workers: int = 4, log=print) -> dict:
    """Extract needs for upcoming translators ahead of time (step 1 of
    retrieval needs no glossary, so it can run while the previous batch
    migrates). Only LLM decompositions are cached; a heuristic fallback is
    left for the translator to retry live."""
    NEEDS_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    todo = [r for r in rows if lf.finished_path(r["dataset"], r["translator_id"]) is None
            and load_cached_needs(r["translator_id"], lf.item_content(r)) is None]
    counts = {"cached": 0, "fallback": 0, "skipped": len(rows) - len(todo)}

    def one(row):
        if STOPPING.is_set():
            return "skipped"
        content = lf.item_content(row)
        _, needs, method = needs_mod.extract_needs(content, use_llm=True)
        if not method.startswith("llm"):
            return "fallback"
        stripped = [{k: v for k, v in n.items() if k not in ("id", "context")} for n in needs]
        (NEEDS_CACHE_DIR / f"{row['translator_id']}.json").write_text(json.dumps(
            {"translator_id": row["translator_id"], "content_sha": _content_sha(content), "method": method,
             "needs_version": needs_mod.NEEDS_VERSION, "needs": stripped, "at": lf.now_iso()}, ensure_ascii=False), encoding="utf-8")
        return "cached"

    with ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
        for outcome in pool.map(one, todo):
            counts[outcome] = counts.get(outcome, 0) + 1
    return counts


def is_proxy_error(error_line: str) -> bool:
    """A failure of the model proxy (rate limit / gateway), not of the translator."""
    return bool(re.match(r"^HTTP (429|5\d\d)\b", error_line or ""))


def success_gate_problems(report: dict) -> list:
    """Why a claimed success isn't one, from the host's check. Needs must be
    covered by a used symbol or declared in the coverage table (opaque /
    not-applicable / label-preserved count as declared); no invented symbols
    in statement heads; no invalid value-group atoms or retired bare symbols;
    no coverage claims for symbols the BrainCode never uses. Quoted-string
    and unbound-value warnings stay advisory: some literals are legitimate."""
    problems = []
    if report.get("unresolved"):
        problems.append(f"{len(report['unresolved'])} need(s) neither covered nor declared "
                        f"({', '.join(report['unresolved'][:12])})")
    if report.get("unknown_symbols_in_head_position"):
        problems.append("non-glossary symbols: " + ", ".join(report["unknown_symbols_in_head_position"]))
    if report.get("claimed_but_absent"):
        problems.append("coverage table names unused symbols: " + ", ".join(report["claimed_but_absent"]))
    # value groups (spec §3.1): an invalid atom or a retired bare symbol is not
    # valid BrainCode; a non-canonical alias (atom_warnings) stays advisory
    if report.get("atom_errors"):
        problems.append("invalid value-group atoms: " + "; ".join(report["atom_errors"][:8]))
    if report.get("retired_symbols_used"):
        problems.append("retired bare symbols: " + ", ".join(report["retired_symbols_used"][:8]))
    # spec §13: an opaque span "does not count as fully formalized coverage", and
    # sentence-length text in any quoted literal is natural language carried, not encoded
    if report.get("opaque_needs"):
        problems.append("needs marked opaque (not formalized; encode them or report a failure): "
                        + ", ".join(report["opaque_needs"][:12]))
    if report.get("sentence_literals"):
        problems.append(f"{len(report['sentence_literals'])} sentence-length quoted literal(s) carry natural "
                        "language instead of encoding it: " + " | ".join(report["sentence_literals"][:3]))
    return problems


FAILURE_GATE_FEEDBACK = (
    "\n\n## Your previous attempt was rejected\n\n"
    "It declared `Status: failed`, but its BrainCode carries sentences in quoted strings (`content=`, "
    "`target=`, `message=`, any slot) instead of encoding them. A failed translation is still the best encoding you can write: express what the glossary "
    "allows with its symbols, mark each line that needs a missing symbol `# PROPOSED: S<k>`, and suggest those "
    "symbols. No quoted string may hold 8 or more words, in any slot except names and titles "
    "(name=, title=, label=, caption=).\n\n")


def failure_gate_problems(report: dict) -> list:
    """Why a declared failure isn't a usable one: it must still be an encoding
    (spec §13), so sentence-length text in any quoted literal is rejected.
    Opaque needs stay allowed: a failure is where gaps are reported."""
    if report.get("sentence_literals"):
        return [f"{len(report['sentence_literals'])} sentence-length quoted literal(s) carry natural language "
                "instead of encoding it: " + " | ".join(report["sentence_literals"][:3])]
    return []


def fill_template(text: str, values: dict) -> str:
    for key, value in values.items():
        text = text.replace("{{" + key + "}}", str(value))
    return text


def process_translator(row: dict, cfg, retriever, image: str, ref_snapshot: Path, glossary_version: str,
                       log=print) -> dict:
    tid, dataset, batch_id = row["translator_id"], row["dataset"], int(row["batch_id"])
    done = lf.finished_path(dataset, tid)
    if done is not None:
        return {"tid": tid, "dataset": dataset, "outcome": "skipped", "detail": str(done.relative_to(lf.SELF_DIR))}

    content = lf.item_content(row)
    try:
        cached = load_cached_needs(tid, content)
        if cached:
            result = retriever.retrieve(content, needs=cached["needs"], needs_method=cached["method"] + " (prefetched)")
        else:
            result = retriever.retrieve(content)
    except Exception as e:
        traceback.print_exc()
        return {"tid": tid, "dataset": dataset, "outcome": "error", "detail": f"retrieval failed: {e}"}
    numbered = needs_mod.numbered_text(result["segments"])
    needs = [{k: v for k, v in n.items()} for n in result["needs"]]
    meta = {"translator_id": tid, "batch_id": batch_id, "dataset": dataset, "item_id": lf.item_id(row),
            "glossary_version": glossary_version, "glossary_sha": result["glossary_sha"], "model": cfg.model,
            "needs_count": len(needs), "needs_method": result["needs_method"]}

    with translator_workdir(tid) as work:
        work = Path(work)
        (work / "trajectory.txt").write_text(numbered, encoding="utf-8")
        (work / "item_raw.txt").write_text(content, encoding="utf-8")
        (work / "rag_context.md").write_text(render_context(result, retriever, glossary_version), encoding="utf-8")
        (work / "needs.json").write_text(json.dumps({"translator_id": tid, "needs": needs}, ensure_ascii=False,
                                                    indent=1), encoding="utf-8")
        prompt = fill_template((lf.TASKS_DIR / "translator.md").read_text(encoding="utf-8"),
                               {"TRANSLATOR_ID": tid, "BATCH_ID": batch_id, "TNUM": row["tnum"], "DATASET": dataset})
        attach_dir = build_attachments(work / "attach", ref_snapshot, work)
        uid, gid = utils.host_uid_gid() or (None, None)

        last_problem = None
        feedback = ""
        usage = {}
        # The pi session persists here across attempts, and so does /output:
        # attempt 2 resumes attempt 1's conversation (sending only a short
        # continuation message) instead of re-reading everything and redoing
        # the work — a proxy outage costs the remaining work, not all of it.
        session_dir = work / "session"
        session_dir.mkdir()
        scratch = work / "out"
        scratch.mkdir()
        for attempt in (1, 2):
            if STOPPING.is_set():
                return {"tid": tid, "dataset": dataset, "outcome": "interrupted", "detail": "loop stopping"}
            resume = attempt > 1 and any(session_dir.rglob("*.jsonl"))
            prompt_path = work / f"prompt{attempt}.md"
            if resume:
                prompt_path.write_text(CONTINUE_PROMPT.format(problem=last_problem or "interrupted") + feedback,
                                       encoding="utf-8")
            else:
                prompt_path.write_text(prompt + feedback, encoding="utf-8")
            container = f"swarm-tr-{tid}-{attempt}-{random.randint(1000, 9999)}"
            env = {"TRANSLATOR_ID": tid, "DATASET": dataset, "BATCH_ID": batch_id, "RAG_PORT": cfg.rag_port,
                   "PI_JSON": "1", "PI_SESSION_DIR": "/session", **CONTEXT_LIMITS_ENV}
            if resume:
                env["PI_RESUME"] = "1"
            cmd = utils.build_docker_cmd(
                uid, gid, cfg.model, ref_snapshot, work / "trajectory.txt", prompt_path, scratch, image,
                container_name=container, add_host=True,
                extra_mounts=[(work / "item_raw.txt", "/item_raw.txt"), (work / "rag_context.md", "/rag_context.md"),
                              (work / "needs.json", "/needs.json"), (lf.KIT_DIR, "/kit"),
                              (lf.DOC_FORMATS_DIR, "/doc_formats"), (attach_dir, "/attach")],
                writable_mounts=[(session_dir, "/session")],
                extra_env=env)
            proc, duration, used = run_container_logged(cmd, container, cfg.timeout_s,
                                                        TRANSLATOR_LOG_DIR / f"{tid}-attempt{attempt}.log")
            used = {**used, **collect_context_log(session_dir, used,
                                                  TRANSLATOR_LOG_DIR / f"{tid}-attempt{attempt}.context.jsonl")}
            for key, value in used.items():
                usage[key] = usage.get(key, 0) + value
            status, body, sugg, problem = validate_output(scratch)
            tail = utils.last_error_line(proc.stderr or "") or ""
            if problem is None and proc.returncode != 0:
                # Files on disk from a run that died (proxy error, timeout)
                # are whatever draft it had written so far — not a result.
                problem = (f"harness exited {proc.returncode}"
                           + (f" ({tail})" if tail else "") + "; its files may be an unfinished draft")
            report = None
            if problem is None:
                try:
                    report = retriever.check(body, needs)
                except Exception as e:
                    log(f"translate: {tid} host check failed ({e}); accepting without it")
                if report is not None and status == "success":
                    gate = success_gate_problems(report)
                    if gate:
                        problem = "claimed success but the host check found: " + "; ".join(gate)
                        feedback = ("\n\n## Your previous attempt was rejected\n\n"
                                    "It declared `Status: success`, but the host's check of its BrainCode found "
                                    "problems. Fix every one (cover the need, widen the search, or mark it "
                                    "not-applicable with a reason), or report a failure with suggestions:\n\n"
                                    + render_check(report))
                elif report is not None and status == "failed":
                    gate = failure_gate_problems(report)
                    if gate:
                        problem = "failed translation rejected: " + "; ".join(gate)
                        feedback = FAILURE_GATE_FEEDBACK + render_check(report)
            if problem is None:
                meta["status"] = status
                meta["at"] = lf.now_iso()
                # The host's own run of step 5, attached for the migrator and
                # for auditing: a translator's self-report is not the only
                # record of what its BrainCode actually uses.
                if report is not None:
                    body = body.rstrip() + "\n\n## Host check\n\n" + render_check(report).replace(
                        "# Coverage check", "").strip() + "\n"
                if status == "success":
                    dest = lf.success_path(dataset, tid)
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    dest.write_text(lf.compose_translation(meta, numbered, body), encoding="utf-8")
                    if sugg:
                        log(f"translate: {tid} succeeded but also wrote suggestions — ignored (suggestions are for failures)")
                else:
                    dest = lf.failed_path(dataset, tid)
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    dest.write_text(lf.compose_translation(meta, numbered, body), encoding="utf-8")
                    spath = lf.suggestions_path(tid)
                    spath.parent.mkdir(parents=True, exist_ok=True)
                    spath.write_text(lf.compose_suggestions(meta, sugg), encoding="utf-8")
                return {"tid": tid, "dataset": dataset, "outcome": status, "attempts": attempt,
                        "suggestions": len(lf.parse_suggestions(sugg or "")) if status == "failed" else 0,
                        "duration_s": round(duration, 1), "usage": usage}
            if STOPPING.is_set():
                return {"tid": tid, "dataset": dataset, "outcome": "interrupted", "detail": "loop stopping"}
            last_problem = problem
            where = record_failure(tid, attempt, proc, duration, problem, scratch, cfg)
            log(f"translate: {tid} attempt {attempt} unusable ({problem}{'; ' + tail if tail and tail not in problem else ''})"
                f" — logs in {where.relative_to(lf.SELF_DIR)}")
            if attempt == 1 and is_proxy_error(tail):
                # Retrying straight into a rate limit just fails again; give
                # the proxy time, with jitter so retries don't arrive together.
                wait = random.uniform(*PROXY_BACKOFF_S)
                log(f"translate: {tid} waiting {wait:.0f}s before retrying (proxy error)")
                if STOPPING.wait(wait):
                    return {"tid": tid, "dataset": dataset, "outcome": "interrupted", "detail": "loop stopping"}
    return {"tid": tid, "dataset": dataset, "outcome": "error", "detail": last_problem, "usage": usage}


def run_batch(batch_id: int, rows: list, cfg, retriever, image: str, glossary_version: str, log=print) -> dict:
    with tempfile.TemporaryDirectory(prefix=f"ref-{batch_id}-") as ref_dir:
        ref_snapshot = snapshot_reference(Path(ref_dir) / "reference")
        results = []
        with ThreadPoolExecutor(max_workers=max(1, cfg.concurrency)) as pool:
            futures = {pool.submit(process_translator, row, cfg, retriever, image, ref_snapshot, glossary_version,
                                   log): row for row in rows}
            for future in as_completed(futures):
                row = futures[future]
                try:
                    res = future.result()
                except Exception as e:
                    traceback.print_exc()
                    res = {"tid": row["translator_id"], "dataset": row["dataset"], "outcome": "error", "detail": str(e)}
                results.append(res)
                log(f"translate: {res['tid']} ({res['dataset']}) -> {res['outcome']}"
                    + (f", {res['suggestions']} suggestion(s)" if res.get("suggestions") else "")
                    + (f" [{res['detail']}]" if res.get("detail") and res["outcome"] == "error" else ""))
    counts, usage = {}, {}
    for r in results:
        counts[r["outcome"]] = counts.get(r["outcome"], 0) + 1
        for key, value in (r.get("usage") or {}).items():
            usage[key] = usage.get(key, 0) + value
    return {"batch_id": batch_id, "counts": counts, "usage": usage,
            "results": sorted(results, key=lambda r: lf.parse_translator_id(r["tid"]))}


def main(argv=None):
    import loop
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--batch", type=int, required=True)
    p.add_argument("--no-dense", action="store_true")
    args = p.parse_args(argv)
    cfg = loop.load_loop_config()
    plan = lf.plan_batches(lf.load_plan())
    if args.batch not in plan:
        sys.exit(f"translate_batch: batch {args.batch} is not in {lf.PLAN_PATH}")
    with loop.rag_service(cfg, dense=not args.no_dense) as retriever:
        image = loop.build_image(cfg.harness_name)
        from glossary import manifest
        summary = run_batch(args.batch, plan[args.batch], cfg, retriever, image, manifest.current_version())
    print(json.dumps(summary["counts"]))


if __name__ == "__main__":
    main()
