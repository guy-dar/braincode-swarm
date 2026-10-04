#!/usr/bin/env python3
"""Download larger samples (~10k per dataset where the source has that many) of the six
datasets syntax-loop simulates on, normalize them into the swarm's record format, and write a
stratified 80/20 train/test split per dataset plus a README report.

    python fetch_datasets.py                    # all six, --n 10000
    python fetch_datasets.py --only alfred --n 500
    python fetch_datasets.py --report-only      # rebuild data/README.md from data/*/stats.json

Output, per dataset: data/<name>/{train,test}.jsonl and data/<name>/stats.json. Each record has
`content` (`<|user|>`/`<|assistant|>` turns — the swarm's contract, see sample_batch.py), plus
`id`, `source`, `split`, and the dataset's metadata/stratification fields.

Adapted from syntax-loop/scripts/fetch_dataset_samples.py (same duckdb Parquet column projection,
same ALFRED lite archive). Differences: SWE-bench uses the full princeton-nlp/SWE-bench train
split (19,008 rows, not human-validated) instead of the 500-row Verified set, so it can reach 10k;
Mind2Web adds the public test splits from osunlp/Multimodal-Mind2Web (one row per *action* there,
grouped back into tasks by annotation_id) to cover all its domains.

Requires network access plus `duckdb` and `py7zr`.
"""
from __future__ import annotations

import argparse
import json
import os
import random
import re
import statistics
import tempfile
import time
import urllib.request
from collections import Counter, defaultdict

SELF_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SELF_DIR, "data")

ALFRED_URL = "https://ai2-vision-alfred.s3-us-west-2.amazonaws.com/json_2.1.0.7z"
PRISM_REPO = "HannahRoseKirk/prism-alignment"
PATHS_REPO = "microsoft/prototypical-hai-collaborations"
PATHS_CONFIG = "wildchat1m_en3u-task_utterance_wintent_anns"
THOUGHTTRACE_REPO = "SCAI-JHU/ThoughtTrace"

DATASETS = ["mind2web", "alfred", "swebench", "prism", "paths", "thoughttrace"]

# What each dataset is stratified on, and which other fields stats.json/README report.
STRATIFY = {
    "mind2web": "domain",
    "alfred": "task_type",
    "swebench": "repo_stratum",
    "prism": "conversation_type",
    "paths": "primary_task",
    "thoughttrace": "model_provider",
}
SECONDARY = {
    "mind2web": ["subdomain", "orig_split"],
    "alfred": [],
    "swebench": ["repo"],
    "prism": ["included_in_balanced_subset", "has_feedback"],
    "paths": ["model"],
    "thoughttrace": ["model_name", "has_feedback"],
}

INFO = {
    "mind2web": {
        "title": "Mind2Web",
        "class": "closed",
        "hf": "osunlp/Mind2Web (train) + osunlp/Multimodal-Mind2Web (test_task, test_website, test_domain)",
        "license": "CC BY 4.0",
        "ceiling": "~2,022 tasks: all public Mind2Web tasks (train 1,009 + test_task 177 + test_website 142 + test_domain 694). "
                   "Everything available was downloaded.",
    },
    "alfred": {
        "title": "ALFRED",
        "class": "closed",
        "hf": "askforalfred/alfred json_2.1.0 lite archive (train)",
        "license": "MIT",
        "ceiling": "Sampled by trial; each trial has ~3 crowd-written annotations.",
    },
    "swebench": {
        "title": "SWE-bench (full)",
        "class": "closed",
        "hf": "princeton-nlp/SWE-bench (train)",
        "license": "MIT",
        "ceiling": "19,008 train rows available. This is the full SWE-bench, not Verified, so it is **not human-validated**.",
    },
    "prism": {
        "title": "PRISM",
        "class": "open",
        "hf": "HannahRoseKirk/prism-alignment (conversations)",
        "license": "CC BY-NC 4.0 (see dataset card)",
        "ceiling": "8,011 conversations, the dataset's full size. Everything available was downloaded.",
    },
    "paths": {
        "title": "PATHs (annotated WildChat)",
        "class": "open",
        "hf": f"microsoft/prototypical-hai-collaborations ({PATHS_CONFIG})",
        "license": "ODC-BY",
        "ceiling": "32,697 conversations available. Task and intent labels are **LLM-generated (GPT-4o)**, not human ground truth.",
    },
    "thoughttrace": {
        "title": "ThoughtTrace",
        "class": "open",
        "hf": "SCAI-JHU/ThoughtTrace",
        "license": "CC BY 4.0",
        "ceiling": "2,155 conversations, the dataset's full size. Everything available was downloaded.",
    },
}


# ---------------------------------------------------------------------------- fetch helpers

def _fetch_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def _parquet_urls(repo: str, split: str, config: str = "default") -> list[str]:
    return _fetch_json(f"https://huggingface.co/api/datasets/{repo}/parquet")[config][split]


def _url_list(urls: list[str]) -> str:
    return "[" + ", ".join(f"'{u}'" for u in urls) + "]"


def _duckdb_connect():
    import duckdb

    con = duckdb.connect()
    con.execute("INSTALL httpfs; LOAD httpfs;")
    return con


def _query(con, sql: str) -> list[dict]:
    cur = con.execute(sql)
    cols = [d[0] for d in cur.description]
    return [dict(zip(cols, row)) for row in cur.fetchall()]


def _turns(pairs: list[tuple[str, str]]) -> str:
    """[(role, text), ...] -> '<|user|>...<|assistant|>...'. Empty turns are dropped (an empty
    tag gives the translator nothing to read); consecutive same-role turns stay separate tags,
    since the pipeline doesn't require strict alternation."""
    return "".join(f"<|{role}|>{text}" for role, text in pairs if text and text.strip())


def _translatable(content: str) -> bool:
    """Starts with a user turn and has at least one non-empty assistant turn."""
    return content.startswith("<|user|>") and "<|assistant|>" in content


def _numbered(steps: list[str]) -> str:
    return "\n".join(f"{i}. {s}" for i, s in enumerate(steps, 1))


# ---------------------------------------------------------------------------- per-dataset fetchers

def _mind2web_record(r: dict, orig_split: str, source: str) -> dict:
    steps = list(r["action_reprs"] or [])
    return {
        "id": f"mind2web-{r['annotation_id']}",
        "source": source,
        "content": _turns([("user", r["confirmed_task"]), ("assistant", _numbered(steps))]),
        "domain": r["domain"],
        "subdomain": r["subdomain"],
        "website": r["website"],
        "orig_split": orig_split,
        "steps_count": len(steps),
    }


def fetch_mind2web(n: int, seed: int) -> list[dict]:
    con = _duckdb_connect()
    cols = "annotation_id, website, domain, subdomain, confirmed_task, action_reprs"
    rows = [
        _mind2web_record(r, "train", "Mind2Web (osunlp/Mind2Web, train)")
        for r in _query(con, f"SELECT {cols} FROM read_parquet({_url_list(_parquet_urls('osunlp/Mind2Web', 'train'))})")
    ]
    mm = _fetch_json("https://huggingface.co/api/datasets/osunlp/Multimodal-Mind2Web/parquet")["default"]
    for split in ("test_task", "test_website", "test_domain"):
        # One row per action step here; the task-level columns repeat, so group them back into tasks.
        # Only lightweight text columns are projected — never raw_html/cleaned_html/screenshot.
        tasks = _query(con, f"""
            SELECT annotation_id, any_value(website) AS website, any_value(domain) AS domain,
                   any_value(subdomain) AS subdomain, any_value(confirmed_task) AS confirmed_task,
                   any_value(action_reprs) AS action_reprs
            FROM read_parquet({_url_list(mm[split])}) GROUP BY annotation_id
        """)
        rows += [_mind2web_record(r, split, f"Mind2Web (osunlp/Multimodal-Mind2Web, {split})") for r in tasks]
        print(f"  mind2web {split}: {len(tasks)} tasks")
    seen, unique = set(), []
    for r in rows:
        if r["id"] not in seen:
            seen.add(r["id"])
            unique.append(r)
    random.Random(seed).shuffle(unique)
    return unique[:n]


def fetch_alfred(n: int, seed: int) -> list[dict]:
    import py7zr

    rng = random.Random(seed)
    with tempfile.TemporaryDirectory() as tmp:
        archive = os.path.join(tmp, "json_2.1.0.7z")
        print(f"  downloading {ALFRED_URL} (~35 MB) ...")
        urllib.request.urlretrieve(ALFRED_URL, archive)
        with py7zr.SevenZipFile(archive, mode="r") as z:
            names = [m for m in z.getnames() if "/train/" in m.replace("\\", "/") and m.endswith("traj_data.json")]
        print(f"  alfred: {len(names)} train trajectories in archive")
        # ~3 annotations per trial; over-pick trials, then keep whole trials until n is reached.
        chosen = rng.sample(names, min(len(names), n // 2 + 50))
        with py7zr.SevenZipFile(archive, mode="r") as z:
            z.extract(path=tmp, targets=chosen)
        rows = []
        for name in chosen:
            if len(rows) >= n:
                break
            path = os.path.join(tmp, name)
            if not os.path.exists(path):
                continue
            with open(path, "r", encoding="utf-8") as f:
                traj = json.load(f)
            trial = os.path.basename(os.path.dirname(name))
            for i, ann in enumerate(traj.get("turk_annotations", {}).get("anns", [])):
                desc = (ann.get("task_desc") or "").strip()
                steps = [s.strip() for s in ann.get("high_descs", []) if s and s.strip()]
                if not desc or not steps:
                    continue
                rows.append({
                    "id": f"alfred-{trial}#{i}",
                    "source": "ALFRED (json_2.1.0, train)",
                    "content": _turns([("user", desc), ("assistant", _numbered(steps))]),
                    "task_type": traj.get("task_type"),
                    "trial": trial,
                    "steps_count": len(steps),
                })
    return rows


def fetch_swebench(n: int, seed: int) -> list[dict]:
    con = _duckdb_connect()
    raw = _query(con, f"""
        -- ~2% of train rows have an empty gold patch: nothing to show as the fix. Filtered in a
        -- subquery because USING SAMPLE runs before a same-level WHERE and would come up short.
        SELECT * FROM (
            SELECT instance_id, repo, problem_statement, patch
            FROM read_parquet({_url_list(_parquet_urls('princeton-nlp/SWE-bench', 'train'))})
            WHERE patch LIKE '%diff --git%'
        )
        USING SAMPLE {int(n)} ROWS (reservoir, {int(seed)})
    """)
    repo_counts = Counter(r["repo"] for r in raw)
    rows = []
    for r in raw:
        # The file list stands in for "what the fix touched", as in syntax-loop; the diff body is left out.
        files = sorted(set(re.findall(r"diff --git a/(\S+) b/\S+", r["patch"] or "")))
        rows.append({
            "id": f"swebench-{r['instance_id']}",
            "source": "SWE-bench (princeton-nlp/SWE-bench, train)",
            "content": _turns([("user", r["problem_statement"]),
                               ("assistant", _numbered([f"modify {f}" for f in files]))]),
            "repo": r["repo"],
            "repo_stratum": r["repo"] if repo_counts[r["repo"]] >= 10 else "other",
            "steps_count": len(files),
        })
    return rows


def fetch_prism(n: int, seed: int) -> list[dict]:
    con = _duckdb_connect()
    raw = _query(con, f"""
        SELECT conversation_id, conversation_type, conversation_history, open_feedback,
               included_in_balanced_subset
        FROM read_parquet({_url_list(_parquet_urls(PRISM_REPO, 'train', config='conversations'))})
        USING SAMPLE {int(n)} ROWS (reservoir, {int(seed)})
    """)
    rows = []
    for r in raw:
        # Each turn has several candidate model responses; keep the one the user chose, which is
        # the path the conversation actually continued along.
        hist = sorted(r["conversation_history"] or [], key=lambda t: (t["turn"], t.get("within_turn_id") or 0))
        pairs, models = [], []
        for t in hist:
            if t["role"] == "user":
                pairs.append(("user", t["content"]))
            elif t.get("if_chosen"):
                pairs.append(("assistant", t["content"]))
                models.append(t["model_name"])
        if not pairs or pairs[0][0] != "user":
            continue
        feedback = (r["open_feedback"] or "").strip()
        rows.append({
            "id": f"prism-{r['conversation_id']}",
            "source": "PRISM (HannahRoseKirk/prism-alignment, conversations)",
            "content": _turns(pairs),
            "conversation_type": r["conversation_type"],
            "models": models,
            "feedback": feedback,
            "has_feedback": bool(feedback),
            "included_in_balanced_subset": bool(r["included_in_balanced_subset"]),
            "turns_count": len(pairs),
        })
    return rows


def fetch_paths(n: int, seed: int) -> list[dict]:
    con = _duckdb_connect()
    raw = _query(con, f"""
        SELECT convid, model, turns, coarse_tasks, writing_intents
        FROM read_parquet({_url_list(_parquet_urls(PATHS_REPO, 'train', config=PATHS_CONFIG))})
        USING SAMPLE {int(n)} ROWS (reservoir, {int(seed)})
    """)
    rows = []
    for r in raw:
        turns = list(r["turns"] or [])
        first_user = next((i for i, t in enumerate(turns) if t.get("author") == "user"), None)
        if first_user is None:
            continue
        pairs = [("user" if t["author"] == "user" else "assistant", t.get("utterance") or "")
                 for t in turns[first_user:]]
        tasks = list(r["coarse_tasks"] or [])
        rows.append({
            "id": f"paths-{r['convid']}",
            "source": f"PATHs (microsoft/prototypical-hai-collaborations, {PATHS_CONFIG})",
            "content": _turns(pairs),
            "model": r["model"],
            "coarse_tasks": tasks,
            "writing_intents": [list(w) for w in (r["writing_intents"] or [])],
            "primary_task_raw": tasks[0] if tasks else "(none)",
            "turns_count": len(pairs),
        })
    # Collapse the long tail of first-task labels so every stratum is big enough to split.
    top = {t for t, _ in Counter(r["primary_task_raw"] for r in rows).most_common(15)}
    for r in rows:
        r["primary_task"] = r["primary_task_raw"] if r["primary_task_raw"] in top else "other"
        del r["primary_task_raw"]
    return rows


def fetch_thoughttrace(n: int, seed: int) -> list[dict]:
    con = _duckdb_connect()
    raw = _query(con, f"""
        SELECT id, messages, model_name, model_provider
        FROM read_parquet({_url_list(_parquet_urls(THOUGHTTRACE_REPO, 'train'))})
        USING SAMPLE {int(n)} ROWS (reservoir, {int(seed)})
    """)
    rows = []
    for r in raw:
        msgs = [json.loads(m) if isinstance(m, str) else m for m in (r["messages"] or [])]
        first_user = next((i for i, m in enumerate(msgs) if m.get("type") == "user"), None)
        if first_user is None:
            continue
        pairs, feedback = [], []
        for m in msgs[first_user:]:
            role = "user" if m.get("type") == "user" else "assistant"
            pairs.append((role, m.get("content") or ""))
            # Per-message human feedback: kept as metadata, aligned to its turn index.
            for fb in (m.get("reasons") or []) + (m.get("reactions") or []):
                feedback.append({"turn": len(pairs) - 1, "label": fb.get("label"), "content": fb.get("content")})
        rows.append({
            "id": f"thoughttrace-{r['id']}",
            "source": "ThoughtTrace (SCAI-JHU/ThoughtTrace)",
            "content": _turns(pairs),
            "model_name": r["model_name"],
            "model_provider": r["model_provider"],
            "feedback": feedback,
            "has_feedback": bool(feedback),
            "turns_count": len(pairs),
        })
    return rows


FETCHERS = {
    "mind2web": fetch_mind2web,
    "alfred": fetch_alfred,
    "swebench": fetch_swebench,
    "prism": fetch_prism,
    "paths": fetch_paths,
    "thoughttrace": fetch_thoughttrace,
}


# ---------------------------------------------------------------------------- split + stats

def stratified_split(rows: list[dict], key: str, group: str | None = None,
                     test_frac: float = 0.2, seed: int = 42) -> tuple[list[dict], list[dict]]:
    """Split each stratum `test_frac` into test (at least one when it has 2+ units). With
    `group`, whole groups move together, so near-duplicates never straddle the split."""
    rng = random.Random(seed)
    units: dict[str, dict[str, list[dict]]] = defaultdict(lambda: defaultdict(list))
    for r in rows:
        units[str(r.get(key))][r[group] if group else r["id"]].append(r)
    train, test = [], []
    for stratum in sorted(units):
        groups = sorted(units[stratum].values(), key=lambda g: g[0]["id"])
        rng.shuffle(groups)
        k = round(len(groups) * test_frac)
        if k == 0 and len(groups) >= 2:
            k = 1
        for g in groups[:k]:
            test.extend(g)
        for g in groups[k:]:
            train.extend(g)
    rng.shuffle(train)
    rng.shuffle(test)
    return train, test


def _length_stats(rows: list[dict], field: str) -> dict:
    vals = [r[field] for r in rows if isinstance(r.get(field), int)]
    if not vals:
        return {}
    return {"mean": round(statistics.mean(vals), 2), "median": statistics.median(vals), "min": min(vals), "max": max(vals)}


def compute_stats(name: str, train: list[dict], test: list[dict], seconds: float) -> dict:
    key = STRATIFY[name]

    def dist(field):
        tr, te = Counter(str(r.get(field)) for r in train), Counter(str(r.get(field)) for r in test)
        return [{"value": v, "train": tr[v], "test": te[v]} for v, _ in (tr + te).most_common()]

    length_field = "steps_count" if name in ("mind2web", "alfred", "swebench") else "turns_count"
    content_chars = [len(r["content"]) for r in train + test]
    return {
        "name": name,
        "total": len(train) + len(test),
        "train": len(train),
        "test": len(test),
        "stratify_on": key,
        "strata": dist(key),
        "secondary": {f: dist(f) for f in SECONDARY[name]},
        "length_field": length_field,
        "length": {"train": _length_stats(train, length_field), "test": _length_stats(test, length_field)},
        "content_chars_median": statistics.median(content_chars) if content_chars else 0,
        "groups": len({r["trial"] for r in train + test}) if name == "alfred" else None,
        "fetch_seconds": round(seconds, 1),
    }


def _write_jsonl(path: str, rows: list[dict]) -> None:
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def run_dataset(name: str, n: int, seed: int) -> None:
    print(f"== {name}")
    start = time.perf_counter()
    rows = FETCHERS[name](n, seed)
    dropped = len(rows)
    rows = [r for r in rows if _translatable(r["content"])]
    dropped -= len(rows)
    if dropped:
        print(f"  dropped {dropped} records with no user turn or no assistant text")
    seconds = time.perf_counter() - start
    train, test = stratified_split(rows, STRATIFY[name], group="trial" if name == "alfred" else None, seed=seed)
    for r in train:
        r["split"] = "train"
    for r in test:
        r["split"] = "test"
    out = os.path.join(DATA_DIR, name)
    os.makedirs(out, exist_ok=True)
    _write_jsonl(os.path.join(out, "train.jsonl"), train)
    _write_jsonl(os.path.join(out, "test.jsonl"), test)
    with open(os.path.join(out, "stats.json"), "w", encoding="utf-8") as f:
        json.dump(compute_stats(name, train, test, seconds), f, indent=2, ensure_ascii=False)
    print(f"  {len(rows)} rows -> train {len(train)} / test {len(test)} ({seconds:.0f}s)")


# ---------------------------------------------------------------------------- README

def _pct(a: int, total: int) -> str:
    return f"{100 * a / total:.1f}%" if total else "-"


def _dist_table(entries: list[dict], train_n: int, test_n: int, label: str, top: int = 20) -> list[str]:
    lines = [f"| {label} | train | train % | test | test % | test share of stratum |", "|---|---:|---:|---:|---:|---:|"]
    shown, rest = entries[:top], entries[top:]
    for e in shown:
        lines.append(f"| {e['value']} | {e['train']} | {_pct(e['train'], train_n)} | {e['test']} | "
                     f"{_pct(e['test'], test_n)} | {_pct(e['test'], e['train'] + e['test'])} |")
    if rest:
        tr, te = sum(e["train"] for e in rest), sum(e["test"] for e in rest)
        lines.append(f"| *{len(rest)} more* | {tr} | {_pct(tr, train_n)} | {te} | {_pct(te, test_n)} | {_pct(te, tr + te)} |")
    return lines


def write_readme(seed: int, n: int) -> None:
    stats = {}
    for name in DATASETS:
        path = os.path.join(DATA_DIR, name, "stats.json")
        if os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                stats[name] = json.load(f)

    L = [
        "# swarm/data",
        "",
        f"Larger samples of the six datasets in `syntax-loop/datasets/`, with up to {n:,} records per dataset. "
        "Each dataset has a stratified 80/20 train/test split. Generated by `swarm/fetch_datasets.py` "
        f"(seed {seed}). To rebuild this file from the `stats.json` files, run `python fetch_datasets.py --report-only`.",
        "",
        "## Layout and format",
        "",
        "```",
        "data/<dataset>/train.jsonl   # 80%",
        "data/<dataset>/test.jsonl    # 20%",
        "data/<dataset>/stats.json    # the numbers in this report",
        "```",
        "",
        "Each line is one record in the swarm's format: `content` holds `<|user|>`/`<|assistant|>` turns, "
        "followed by `id`, `source`, `split`, and the dataset's metadata fields. "
        "In closed-class datasets the assistant turn is the numbered action or sub-goal sequence "
        "(for SWE-bench, the files the gold patch modifies). Open-class datasets keep the real conversation turns. "
        "Human feedback is stored as metadata (`feedback`) and is not part of `content`.",
        "",
        "> **Sampling note:** `sample_batch.py` defaults to all of `data/`, which would also draw from the test splits. "
        "To sample training data only, pass it explicitly: `python3 sample_batch.py -n 30 --data 'data/*/train.jsonl'`.",
        "",
        "## Summary",
        "",
        "| Dataset | Class | Source | Downloaded | Train | Test | Stratified on | Notes |",
        "|---|---|---|---:|---:|---:|---|---|",
    ]
    for name in DATASETS:
        if name not in stats:
            L.append(f"| {INFO[name]['title']} | {INFO[name]['class']} | {INFO[name]['hf']} | — | — | — | — | not fetched |")
            continue
        s = stats[name]
        L.append(f"| {INFO[name]['title']} | {INFO[name]['class']} | {INFO[name]['hf']} | {s['total']:,} | "
                 f"{s['train']:,} | {s['test']:,} | `{s['stratify_on']}` | {INFO[name]['ceiling']} |")
    total = sum(s["total"] for s in stats.values())
    L += ["", f"**Total: {total:,} records.**", ""]

    for name in DATASETS:
        if name not in stats:
            continue
        s, info = stats[name], INFO[name]
        L += [f"## {info['title']}", "",
              f"- Source: {info['hf']}. License: {info['license']}.",
              f"- Downloaded {s['total']:,}. Train {s['train']:,} ({_pct(s['train'], s['total'])}), "
              f"test {s['test']:,} ({_pct(s['test'], s['total'])}).",
              f"- {info['ceiling']}"]
        if name == "alfred":
            L.append(f"- Split by **trial**: the {s['groups']:,} trials each sit entirely in train or entirely in test, "
                     "so the ~3 annotations of one trajectory never straddle the split.")
        lt, le = s["length"]["train"], s["length"]["test"]
        if lt:
            L.append(f"- `{s['length_field']}`: train mean {lt['mean']} (median {lt['median']}, max {lt['max']}), "
                     f"test mean {le.get('mean', '-')} (median {le.get('median', '-')}, max {le.get('max', '-')}).")
        L.append(f"- Median `content` length: {s['content_chars_median']:,.0f} characters.")
        L += ["", f"**Stratified on `{s['stratify_on']}`** ({len(s['strata'])} strata):", ""]
        L += _dist_table(s["strata"], s["train"], s["test"], s["stratify_on"])
        for field, entries in s["secondary"].items():
            L += ["", f"Secondary feature `{field}` (not stratified; shown to check the split's balance):", ""]
            L += _dist_table(entries, s["train"], s["test"], field, top=12)
        L.append("")

    L += ["## Caveats", "",
          "- **SWE-bench** is the full, non-human-validated set, not the 500-row Verified subset that syntax-loop uses. "
          "Its distribution is heavily skewed toward a few repositories, especially pandas; see the strata table above.",
          "- **PATHs** task and intent labels are LLM-generated (GPT-4o) and were human-validated only on a subset.",
          "- **Mind2Web**'s original test splits (cross-task, cross-website, cross-domain) are mixed into the pool before "
          "the stratified split. Their original split is kept as `orig_split` if you need the official held-out design.",
          "- **PRISM** `content` follows the response the user chose at each turn; the other candidate responses are dropped.",
          "- All datasets are third-party research releases. Check each license before redistributing.",
          ""]
    with open(os.path.join(DATA_DIR, "README.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L))
    print(f"wrote {os.path.join(DATA_DIR, 'README.md')}")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--n", type=int, default=10000, help="records per dataset (capped by each source's size)")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--only", choices=DATASETS, action="append", help="repeatable; default all")
    p.add_argument("--report-only", action="store_true", help="only regenerate data/README.md")
    args = p.parse_args()

    if not args.report_only:
        failed = []
        for name in args.only or DATASETS:
            try:
                run_dataset(name, args.n, args.seed)
            except Exception as e:  # one source failing shouldn't lose the others
                print(f"  FAILED {name}: {type(e).__name__}: {e}")
                failed.append(name)
        if failed:
            print(f"failed: {failed}")
    write_readme(args.seed, args.n)


if __name__ == "__main__":
    main()
