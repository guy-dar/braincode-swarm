#!/usr/bin/env python3
"""Assemble this folder for Google Colab (run locally, from the repository).

    python finetune-llama/build_folder.py

Writes, next to this script:
  data/train.jsonl, data/val.jsonl   training examples (item -> BrainCode), validated
  data/translations/...              the full successful translation documents they come from
  data/manifest.json                 counts and what was filtered out, and why
  braincode_kit/                     the BrainCode reference (glossary g19, compact spec, standards)
                                     and the swarm's RAG + checker code, with the prebuilt index
  benchmark/                         the 50 BBEH-mini items and their retrieved glossary context

Training data = every successful translation (swarm batches + the evaluation's
forward runs) whose BrainCode still passes today's host check against glossary
g19: no unknown symbols, no invalid/retired group values, no quoted string of
8+ words outside names/titles, no needs marked opaque. Identical BrainCode is
kept once. Validation items are disjoint from training items.
"""
import hashlib
import re
import json
import random
import shutil
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
SWARM = REPO / "swarm"
EVAL = REPO / "evaluations"
sys.path.insert(0, str(SWARM))
import loop_files as lf  # noqa: E402
import translate_batch as tb  # noqa: E402
from rag.retrieve import Retriever, braincode_code  # noqa: E402

KIT = HERE / "braincode_kit"
DATA = HERE / "data"
BENCH = HERE / "benchmark"
EXCLUDED_MODELS = {"gpt-6.1-sol", "gpt-6-luna"}
VAL_SHARE = 0.05
SEED = 2026


def build_kit():
    if KIT.exists():
        shutil.rmtree(KIT)
    (KIT / "rag").mkdir(parents=True)
    for f in ("__init__.py", "retrieve.py", "index.py", "needs.py", "server.py"):
        shutil.copy2(SWARM / "rag" / f, KIT / "rag" / f)
    shutil.copytree(SWARM / "glossary", KIT / "glossary", ignore=shutil.ignore_patterns("__pycache__"))
    ref = KIT / "reference"
    ref.mkdir()
    for f in ("glossary.jsonl", "glossary.md", "language-spec.compact.md", "examples.jsonl", "retired-symbols.json"):
        shutil.copy2(SWARM / "reference" / f, ref / f)
    shutil.copytree(SWARM / "reference" / "standards", ref / "standards")
    shutil.copytree(EVAL / "runs" / "main" / "rag_index", KIT / "rag" / "index")


def candidates():
    """(id, source, dataset, model, item_key, item_text, translation_path)"""
    plan = {r["translator_id"]: r for r in lf.load_plan()}
    for p in sorted((SWARM / "translations" / "successful").glob("*/*.md")):
        row = plan[p.stem]
        yield (f"swarm-{p.stem}", "swarm", p.parent.name, "gemini-flash-3.7 (swarm)", f"swarm-{p.stem}",
               lf.item_content(row), p)
    for res in sorted((EVAL / "runs" / "main").glob("*/*/r*/result.json")):
        r = json.loads(res.read_text(encoding="utf-8"))
        if r["status"] != "success" or r["model"] in EXCLUDED_MODELS:
            continue
        doc = res.parent / "translation.md"
        raw = EVAL / "runs" / "main" / "items" / r["item"] / "item_raw.txt"
        if doc.exists() and raw.exists():
            yield (f"eval-{r['model']}-{r['item']}-r{r['run']}", "evaluation", r["dataset"], r["model"],
                   f"eval-{r['item']}", raw.read_text(encoding="utf-8"), doc)


def build_data():
    retriever = Retriever(dense=False, glossary_path=KIT / "reference" / "glossary.jsonl",
                          index_dir=EVAL / "runs" / "main" / "rag_index", use_llm=False)
    if DATA.exists():
        shutil.rmtree(DATA)
    (DATA / "translations").mkdir(parents=True)
    kept, dropped, seen = [], Counter(), set()
    for cid, source, dataset, model, item_key, text, path in candidates():
        doc = path.read_text(encoding="utf-8")
        code = braincode_code(doc).strip()
        if not code or code == doc.strip():
            dropped["no braincode block"] += 1
            continue
        problems = tb.success_gate_problems(retriever.check(doc, []))
        if problems:
            dropped[re.sub(r"^\d+ ", "", problems[0].split(":")[0])[:70]] += 1
            continue
        h = hashlib.sha1(code.encode("utf-8")).hexdigest()
        if h in seen:
            dropped["duplicate BrainCode"] += 1
            continue
        seen.add(h)
        dst = DATA / "translations" / source / dataset / f"{cid}.md"
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(doc, encoding="utf-8")
        kept.append({"id": cid, "source": source, "dataset": dataset, "model": model, "item_key": item_key,
                     "item": text, "braincode": code})
    items = sorted({k["item_key"] for k in kept})
    rng = random.Random(SEED)
    val_items = set(rng.sample(items, max(1, int(len(items) * VAL_SHARE))))
    split = {"train": [k for k in kept if k["item_key"] not in val_items],
             "val": [k for k in kept if k["item_key"] in val_items]}
    for name, rows in split.items():
        with (DATA / f"{name}.jsonl").open("w", encoding="utf-8") as fh:
            for r in rows:
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    chars = [len(k["item"]) + len(k["braincode"]) for k in kept]
    manifest = {"glossary": "g19 (19.0.0-draft.2-lexical-groups)", "kept": len(kept),
                "train": len(split["train"]), "val": len(split["val"]), "distinct_items": len(items),
                "by_source": dict(Counter(k["source"] for k in kept)),
                "by_dataset": dict(Counter(k["dataset"] for k in kept)),
                "by_model": dict(Counter(k["model"] for k in kept)),
                "dropped": dict(dropped),
                "approx_tokens_per_example": {"median": sorted(chars)[len(chars) // 2] // 4,
                                              "max": max(chars) // 4},
                "note": "evaluation items come from the datasets' test splits: a model tuned on them must not be "
                        "evaluated on those items again (coverage / determinism / expressivity)."}
    (DATA / "manifest.json").write_text(json.dumps(manifest, indent=1), encoding="utf-8")
    return manifest


def build_benchmark():
    src = EVAL / "improvement"
    if BENCH.exists():
        shutil.rmtree(BENCH)
    (BENCH / "items").mkdir(parents=True)
    shutil.copy2(src / "sample.jsonl", BENCH / "sample.jsonl")
    for d in (src / "items").iterdir():
        (BENCH / "items" / d.name).mkdir()
        for f in ("rag_context.md", "needs.json"):
            shutil.copy2(d / f, BENCH / "items" / d.name / f)
    shutil.copy2(src / "prompts" / "translate.md", BENCH / "translate_prompt_incontext.md")


if __name__ == "__main__":
    build_kit()
    m = build_data()
    build_benchmark()
    print(json.dumps(m, indent=1))
