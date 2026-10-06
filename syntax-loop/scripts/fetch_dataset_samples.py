#!/usr/bin/env python3
"""Pull a small random sample of real items from every dataset (closed + open class, see
datasets/README.md) into datasets/samples/*.jsonl so the Critic simulates the language on genuine
trajectories/conversations instead of the committed illustrative *.seed.jsonl fallbacks. Run once;
re-run with a different --seed for a fresh sample.

    python scripts/fetch_dataset_samples.py --n 1000
    python scripts/fetch_dataset_samples.py --only alfred --n 50 --seed 7

Requires network access and the optional packages in requirements.txt (`duckdb`, `py7zr`).
Output rows share the field names simulation.py reads: id, nl, steps, source
(+ domain/task_type). Default --n is 1000 for every dataset except SWE-bench_Verified, whose test
split only has 500 rows total (its own fetch call is capped in main(), not in fetch_swebench()
itself — kept on Verified rather than switching to the larger, non-human-validated full
princeton-nlp/SWE-bench, a deliberate choice to keep the human-validation guarantee).

Closed class (structured, single-outcome tasks): mind2web, alfred, swebench (+ seed_tasks, not
fetched by this script — hand-curated in braincode_loop/seed_tasks.json).
Open class (free-form human<->LLM conversations, added for the same reason SWE-bench was: more
linguistic/structural diversity than closed-class trajectories): prism, paths, thoughttrace.

Mind2Web note: its raw JSON files bundle full page HTML per action step, so most of the train
split's 11 files are ~500-650 MB each (one, `train_10.json`, is a ~28 MB outlier with only 9
tasks). Rather than downloading any of those raw files, we query Hugging Face's auto-generated
**Parquet** conversion of the dataset via `duckdb`'s `httpfs` extension, selecting only the
lightweight text columns (`confirmed_task`, `action_reprs`, `domain`, `website`, ...) and never
touching the `actions` column where the embedded HTML lives. This is a normal columnar HTTP
range-read — not Hugging Face's Xet chunk-reconstruction protocol, which turned out to be
unreliable on constrained networks — and it reservoir-samples across the *entire* public train
split (1,009 rows) instead of being stuck with whatever landed in one arbitrary shard. Note: the
public train split itself only spans 3 domains (Travel/Shopping/Entertainment) — Mind2Web's other
~28 domains live in its restricted-access test splits, so that's a real dataset limit, not
something better sampling can fix.

SWE-bench_Verified note: real GitHub issue -> patch pairs, fetched the same Parquet-projection
way. Chosen over Mind2Web/ALFRED-style corpora specifically for structural/linguistic diversity —
measured phenomena rates (conditional/negation/quantifier/correction-language keyword hits) on
its 500-row test split came out far higher than Mind2Web (69% vs. 2% conditional, 67% vs. 2%
negation) because bug reports are inherently "expected X, got Y" narratives, and `problem_statement`
averages ~1,700 characters vs. Mind2Web's one-line tasks. Two other real-content candidates were
tested and rejected: WildChat-1M (536s for 159 rows — its `conversation` field is a nested
STRUCT[] that Parquet can't column-prune the way it can flat columns — and the content itself was
mostly non-task chat/jailbreak noise) and OASST2 (195s for 45 rows, similarly weak phenomena
rates despite its tree structure). ToolBench is gated and needs manual access approval, so it
isn't fetchable here at all. (These two rejections predate the open class below — WildChat-1M and
OASST2 were being evaluated as closed-class candidates at the time; PRISM/PATHs/ThoughtTrace are a
separate, later addition specifically for the open class.)

Open-class notes:
- **PRISM** (`HannahRoseKirk/prism-alignment`, `conversations` config, 8,011 rows) — one row is
  already a full conversation with per-turn model/score metadata and free-text `open_feedback`.
  `conversation_history` is a *nested* `list<struct>` column, the same shape that made WildChat-1M
  slow above — but PRISM is far smaller (8,011 vs. 1M rows), so `fetch_prism` times itself and
  prints the elapsed seconds; if that ever proves too slow in practice, `fetch_prism_flat` is a
  documented fallback using PRISM's flat `utterances` config (68,371 rows, one row per utterance),
  grouped back into conversations by `conversation_id`.
- **PATHs** (`microsoft/prototypical-hai-collaborations`, config
  `wildchat1m_en3u-task_utterance_wintent_anns`, 32,697 rows) — GPT-4o-annotated WildChat
  conversations (task/utterance-type/writing-intent labels), human-validated only on a subset, not
  full human ground truth. One row is already a full conversation.
- **ThoughtTrace** (`SCAI-JHU/ThoughtTrace`, 2,155 rows — its natural ceiling, not an error) — one
  row is a full conversation; `messages` is a `list<string>` of JSON-*encoded* message objects
  (not a typed struct), decoded with `json.loads()` in Python after fetching, each carrying
  `reasons`/`reactions` feedback on user/assistant messages respectively.

A note on Hugging Face's public API: it occasionally rate-limits or WAF-challenges requests with
curl's bare default User-Agent (a plain `curl -v` sometimes returns a cryptic
`{"error":"Invalid username or password."}` 401 even fully anonymous and nowhere near the
`ratelimit` header's quota) — `urllib.request` with an explicit browser-style User-Agent has
proven reliable throughout, which is why `_fetch_json` below always sets one.
"""
from __future__ import annotations

import argparse
import json
import os
import random
import re
import sys
import tempfile
import time
import urllib.request

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAMPLES_DIR = os.path.join(BASE_DIR, "datasets", "samples")

# `syntax-loop/datasets/` is importable as a namespace package and could shadow a same-named
# library when this script runs with cwd=syntax-loop — drop those entries first, defensively.
sys.path[:] = [p for p in sys.path if p not in ("", ".", BASE_DIR, os.path.join(BASE_DIR, "datasets"))]

ALFRED_URL = "https://ai2-vision-alfred.s3-us-west-2.amazonaws.com/json_2.1.0.7z"
PRISM_REPO = "HannahRoseKirk/prism-alignment"
PATHS_REPO = "microsoft/prototypical-hai-collaborations"
PATHS_CONFIG = "wildchat1m_en3u-task_utterance_wintent_anns"
THOUGHTTRACE_REPO = "SCAI-JHU/ThoughtTrace"


def _fetch_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.load(resp)


def _parquet_urls(repo: str, split: str, config: str = "default") -> list[str]:
    data = _fetch_json(f"https://huggingface.co/api/datasets/{repo}/parquet")
    return data[config][split]


def _duckdb_connect():
    import duckdb

    con = duckdb.connect()
    con.execute("INSTALL httpfs; LOAD httpfs;")
    return con


def _write_jsonl(path: str, rows: list[dict]) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"wrote {len(rows)} rows -> {os.path.relpath(path, BASE_DIR)}")


def fetch_mind2web(n: int, seed: int) -> list[dict]:
    url_list = "[" + ", ".join(f"'{u}'" for u in _parquet_urls("osunlp/Mind2Web", "train")) + "]"

    con = _duckdb_connect()
    df = con.execute(f"""
        SELECT annotation_id, website, domain, subdomain, confirmed_task, action_reprs
        FROM read_parquet({url_list})
        USING SAMPLE {int(n)} ROWS (reservoir, {int(seed)})
    """).df()

    return [
        {
            "id": row.annotation_id,
            "nl": row.confirmed_task,
            "domain": row.domain,
            "subdomain": row.subdomain,
            "website": row.website,
            "steps": list(row.action_reprs) if row.action_reprs is not None else [],
            "source": "Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)",
        }
        for row in df.itertuples(index=False)
    ]


def fetch_swebench(n: int, seed: int) -> list[dict]:
    url_list = "[" + ", ".join(f"'{u}'" for u in _parquet_urls("princeton-nlp/SWE-bench_Verified", "test")) + "]"

    con = _duckdb_connect()
    df = con.execute(f"""
        SELECT instance_id, repo, problem_statement, patch, difficulty
        FROM read_parquet({url_list})
        USING SAMPLE {int(n)} ROWS (reservoir, {int(seed)})
    """).df()

    rows = []
    for row in df.itertuples(index=False):
        # Lightweight proxy for "what the fix touched" — the file list, not the (often long) diff
        # body itself, keeping the same "don't embed heavy payloads" approach as the Mind2Web fetch.
        files = sorted(set(re.findall(r"diff --git a/(\S+) b/\S+", row.patch or "")))
        rows.append({
            "id": row.instance_id,
            "nl": row.problem_statement,
            "domain": row.repo,
            "difficulty": row.difficulty,
            "steps": [f"modify {f}" for f in files[:12]],
            "source": "SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)",
        })
    return rows


def fetch_alfred(n: int, seed: int) -> list[dict]:
    import py7zr

    rng = random.Random(seed)
    with tempfile.TemporaryDirectory() as tmp:
        archive = os.path.join(tmp, "json_2.1.0.7z")
        print(f"downloading {ALFRED_URL} (~35 MB) ...")
        urllib.request.urlretrieve(ALFRED_URL, archive)
        with py7zr.SevenZipFile(archive, mode="r") as z:
            names = [m for m in z.getnames() if "/train/" in m.replace("\\", "/") and m.endswith("traj_data.json")]
            # Sample trials first so we never extract the whole >1 GB tree.
            chosen = rng.sample(names, min(len(names), max(n, 1) * 2))
            z.extract(path=tmp, targets=chosen)
        rows = []
        for name in chosen:
            path = os.path.join(tmp, name)
            if not os.path.exists(path):
                continue
            with open(path, "r", encoding="utf-8") as f:
                traj = json.load(f)
            trial = os.path.basename(os.path.dirname(name))
            for i, ann in enumerate(traj.get("turk_annotations", {}).get("anns", [])):
                desc = (ann.get("task_desc") or "").strip()
                if not desc:
                    continue
                rows.append({
                    "id": f"{trial}#{i}",
                    "nl": desc,
                    "task_type": traj.get("task_type"),
                    "steps": [s.strip() for s in ann.get("high_descs", []) if s and s.strip()],
                    "source": "ALFRED (json_2.1.0, train)",
                })
    rng.shuffle(rows)
    return rows[:n]


def fetch_prism(n: int, seed: int) -> list[dict]:
    """Primary PRISM fetch: the `conversations` config's nested `conversation_history` column
    (see module docstring's Open-class notes for why this is timed empirically rather than just
    trusted). If this proves too slow at real scale, use fetch_prism_flat() instead."""
    start = time.perf_counter()
    url_list = "[" + ", ".join(f"'{u}'" for u in _parquet_urls(PRISM_REPO, "train", config="conversations")) + "]"

    con = _duckdb_connect()
    df = con.execute(f"""
        SELECT conversation_id, opening_prompt, conversation_history, open_feedback
        FROM read_parquet({url_list})
        USING SAMPLE {int(n)} ROWS (reservoir, {int(seed)})
    """).df()

    rows = []
    for row in df.itertuples(index=False):
        turns = list(row.conversation_history) if row.conversation_history is not None else []
        steps = [
            f"{t.get('role', '?')} ({t.get('model_name', '?')}, score={t.get('score')}): {t.get('content', '')}"
            for t in turns
        ]
        feedback = (row.open_feedback or "").strip()
        if feedback:
            steps.append(f"feedback: {feedback}")
        rows.append({
            "id": str(row.conversation_id),
            "nl": row.opening_prompt,
            "steps": steps,
            "source": "PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)",
        })
    print(f"fetch_prism: {time.perf_counter() - start:.1f}s for {len(rows)} rows")
    return rows


def fetch_prism_flat(n: int, seed: int) -> list[dict]:
    """Fallback for fetch_prism() if the nested conversation_history column proves too slow in
    practice: reads the flat `utterances` config (68,371 rows, one row per utterance), samples
    conversation_ids first (a cheap distinct-column query), then pulls and groups only their
    utterances, ordered by turn/within_turn_id."""
    url_list = "[" + ", ".join(f"'{u}'" for u in _parquet_urls(PRISM_REPO, "train", config="utterances")) + "]"
    con = _duckdb_connect()
    ids_df = con.execute(f"""
        SELECT DISTINCT conversation_id FROM read_parquet({url_list})
        USING SAMPLE {int(n)} ROWS (reservoir, {int(seed)})
    """).df()
    ids = ", ".join(f"'{i}'" for i in ids_df.conversation_id)
    df = con.execute(f"""
        SELECT conversation_id, opening_prompt, turn, role, content, model_name, score, open_feedback
        FROM read_parquet({url_list}) WHERE conversation_id IN ({ids})
        ORDER BY conversation_id, turn, within_turn_id
    """).df()

    grouped: dict[str, dict] = {}
    for row in df.itertuples(index=False):
        cid = str(row.conversation_id)
        if cid not in grouped:
            grouped[cid] = {"opening_prompt": row.opening_prompt, "steps": [], "feedback": row.open_feedback}
        grouped[cid]["steps"].append(f"{row.role} ({row.model_name}, score={row.score}): {row.content}")

    rows = []
    for cid, data in grouped.items():
        steps = list(data["steps"])
        feedback = (data["feedback"] or "").strip()
        if feedback:
            steps.append(f"feedback: {feedback}")
        rows.append({
            "id": cid,
            "nl": data["opening_prompt"],
            "steps": steps,
            "source": "PRISM (HannahRoseKirk/prism-alignment, utterances config, grouped, Parquet fallback)",
        })
    return rows


def fetch_paths(n: int, seed: int) -> list[dict]:
    url_list = "[" + ", ".join(f"'{u}'" for u in _parquet_urls(PATHS_REPO, "train", config=PATHS_CONFIG)) + "]"
    con = _duckdb_connect()
    df = con.execute(f"""
        SELECT convid, model, turns, coarse_tasks, writing_intents
        FROM read_parquet({url_list})
        USING SAMPLE {int(n)} ROWS (reservoir, {int(seed)})
    """).df()

    rows = []
    for row in df.itertuples(index=False):
        turns = list(row.turns) if row.turns is not None else []
        user_turns = [t for t in turns if t.get("author") == "user"]
        if not user_turns:
            continue
        first_idx = turns.index(user_turns[0])
        steps = [f"{t.get('author', '?')}: {t.get('utterance', '')}" for t in turns[first_idx + 1:]]
        tasks = list(row.coarse_tasks) if row.coarse_tasks is not None else []
        intents = list(row.writing_intents) if row.writing_intents is not None else []
        steps.append(f"[annotations — LLM-generated, GPT-4o: coarse_tasks={tasks}, writing_intents={intents}]")
        rows.append({
            "id": str(row.convid),
            "nl": user_turns[0]["utterance"],
            "steps": steps,
            "task_type": ", ".join(tasks) if tasks else "",
            "source": f"PATHs (microsoft/prototypical-hai-collaborations, {PATHS_CONFIG}, model={row.model})",
        })
    return rows


def fetch_thoughttrace(n: int, seed: int) -> list[dict]:
    url_list = "[" + ", ".join(f"'{u}'" for u in _parquet_urls(THOUGHTTRACE_REPO, "train")) + "]"
    con = _duckdb_connect()
    df = con.execute(f"""
        SELECT messages FROM read_parquet({url_list})
        USING SAMPLE {int(n)} ROWS (reservoir, {int(seed)})
    """).df()

    rows = []
    for i, row in enumerate(df.itertuples(index=False)):
        # row.messages is a numpy array (via duckdb's .df()) — `x or []` calls bool() on it and
        # raises "truth value of an array... is ambiguous" for any array with >1 element; unlike
        # a plain Python list, numpy arrays don't short-circuit safely in a boolean context.
        raw_messages = row.messages if row.messages is not None else []
        msgs = [json.loads(m) for m in raw_messages]
        user_msgs = [m for m in msgs if m.get("type") == "user"]
        if not user_msgs:
            continue
        first_idx = msgs.index(user_msgs[0])
        steps = []
        for m in msgs[first_idx + 1:]:
            steps.append(f"{m.get('type', '?')}: {m.get('content', '')}")
            for r in (m.get("reasons") or []):
                steps.append(f"  [feedback: {r.get('label', '?')}] {r.get('content', '')}")
            for r in (m.get("reactions") or []):
                steps.append(f"  [feedback: {r.get('label', '?')}] {r.get('content', '')}")
        rows.append({
            "id": msgs[0].get("id") or f"thoughttrace-{i + 1}",
            "nl": user_msgs[0].get("content", ""),
            "steps": steps,
            "source": "ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)",
        })
    return rows


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--n", type=int, default=1000, help="items per dataset (default 1000; SWE-bench_Verified is capped at its actual max of 500 regardless)")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--only", choices=["mind2web", "alfred", "swebench", "prism", "paths", "thoughttrace"], default=None)
    args = p.parse_args()

    if args.only in (None, "mind2web"):
        _write_jsonl(os.path.join(SAMPLES_DIR, "mind2web.jsonl"), fetch_mind2web(args.n, args.seed))
    if args.only in (None, "alfred"):
        _write_jsonl(os.path.join(SAMPLES_DIR, "alfred.jsonl"), fetch_alfred(args.n, args.seed))
    if args.only in (None, "swebench"):
        _write_jsonl(os.path.join(SAMPLES_DIR, "swebench.jsonl"), fetch_swebench(min(args.n, 500), args.seed))
    if args.only in (None, "prism"):
        _write_jsonl(os.path.join(SAMPLES_DIR, "prism.jsonl"), fetch_prism(args.n, args.seed))
    if args.only in (None, "paths"):
        _write_jsonl(os.path.join(SAMPLES_DIR, "paths.jsonl"), fetch_paths(args.n, args.seed))
    if args.only in (None, "thoughttrace"):
        _write_jsonl(os.path.join(SAMPLES_DIR, "thoughttrace.jsonl"), fetch_thoughttrace(args.n, args.seed))


if __name__ == "__main__":
    main()
