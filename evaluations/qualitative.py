#!/usr/bin/env python3
"""Qualitative determinism analysis (JS divergence of symbol use) of a finished evaluation run, written by Claude.

Builds a compact evidence bundle from the run (analyze.py's summary.json plus
per-model structural counts, symbols and symbol types a model uses far less
than the others, and the most divergent translations of the same item), asks
Claude Opus 5.5 the evaluation design's four questions, and writes
results/<run>/qualitative_determinism_js.md (the bundle is saved next to it as
qualitative_determinism_js_evidence.json).

    python qualitative.py --run main            # needs results/<run>/summary.json (python analyze.py first)
    python qualitative.py --run main --dry-run  # build and save the bundle only

Key: ANTHROPIC_API_KEY or the user variable CLAUDE_API_KEY (never printed).
"""
import argparse
import json
import re
import sys
import urllib.request
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

EVAL_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(EVAL_DIR))
import metrics  # noqa: E402
import run_eval  # noqa: E402

MODEL = "claude-opus-5-5"
HEAD_RE = re.compile(r"^\s*(RECORD\s+ACTION|RECORD\s+GENERATE|ACTION|GENERATE|UTTER|TERM|CLAIM|LINK|CALL|CHECK|"
                     r"IF|FOR\s+EACH|LET|RETURN|TURN|TASK)\b", re.M)
QUESTIONS = """1. Are there parts of speech, language-spec constructs or symbol types that particular models use more than others?
2. Are there symbol groups (value groups such as object_label, or symbol families) that certain models avoid?
3. In complex texts, are there repetitive structural patterns that certain models prefer or avoid?
4. For translation differences, give common examples of differences that appeared."""


def structure(code: str) -> Counter:
    """Statement heads of a BrainCode document, plus a few shape measures."""
    c = Counter(re.sub(r"\s+", " ", h) for h in HEAD_RE.findall(code))
    c["opaque content= fallbacks"] = len(re.findall(r"\bcontent\s*=", code))
    c["lines"] = len([line for line in code.splitlines() if line.strip()])
    return c


def bundle(run: str, results: str = None) -> dict:
    d = EVAL_DIR / "runs" / run
    summary = json.loads((EVAL_DIR / "results" / (results or run) / "summary.json").read_text(encoding="utf-8"))
    labels = {m["name"]: m["label"] for m in summary["models"]}
    kinds = metrics.glossary_kinds(d / "reference" / "glossary.jsonl")
    items = {i["item_key"]: i for i in run_eval.items_of(run)}
    docs = defaultdict(dict)        # item -> model -> first usable run's document
    struct = defaultdict(Counter)
    n_docs = Counter()
    sym = defaultdict(Counter)
    for p in sorted(d.glob("*/*/r*/translation.md")):
        model, item = p.parts[-4], p.parts[-3]
        if model not in labels or not items.get(item, {}).get("all_models"):
            continue
        # errors (incl. successes the gate rejected on re-check) are left out
        if json.loads((p.parent / "result.json").read_text(encoding="utf-8"))["status"] not in ("success", "failed"):
            continue
        text = p.read_text(encoding="utf-8")
        code = metrics.code_of(text)
        struct[model].update(structure(code))
        n_docs[model] += 1
        sym[model].update(metrics.symbol_counts(text, kinds)[0])
        docs[item].setdefault(model, metrics.braincode_code(text)[:2500])
    per_doc = {labels[m]: {k: round(v / n_docs[m], 2) for k, v in struct[m].most_common(16)} for m in struct}
    # symbols a model uses far less than the other models (avoidance)
    avoided = {}
    for m in sym:
        others = Counter()
        for o in sym:
            if o != m:
                others.update(sym[o])
        tot_m, tot_o = sum(sym[m].values()) or 1, sum(others.values()) or 1
        rows = []
        for s, n in others.most_common(80):
            share_o = n / tot_o
            share_m = sym[m][s] / tot_m
            if share_o >= 0.004 and share_m < share_o / 4:
                rows.append(f"{s} ({share_m:.1%} vs {share_o:.1%} in the others)")
        avoided[labels[m]] = rows[:12]
    # most divergent same-item pairs across models
    pairs = []
    for item, by_model in docs.items():
        for a, b in combinations(sorted(by_model), 2):
            sa = metrics.symbol_counts(by_model[a], kinds)[0]
            sb = metrics.symbol_counts(by_model[b], kinds)[0]
            pairs.append((metrics.js_divergence(sa, sb), item, a, b))
    pairs.sort(reverse=True)
    examples = []
    seen = set()
    for js, item, a, b in pairs:
        if item in seen:
            continue
        seen.add(item)
        examples.append({"item": item, "dataset": items[item]["dataset"], "js": round(js, 3),
                         "source": (d / "items" / item / "item_raw.txt").read_text(encoding="utf-8")[:1200],
                         labels[a]: docs[item][a], labels[b]: docs[item][b]})
        if len(examples) == 6:
            break
    return {"run": run, "models": summary["models"], "coverage": summary["coverage"], "determinism_pairs": summary["determinism_pairs"],
            "determinism_self": summary["determinism_self"], "top_symbols": summary["top_symbols"],
            "type_counts": summary["type_counts"], "statements_per_translation": per_doc,
            "symbols_avoided": avoided, "divergent_examples": examples}


def ask_claude(evidence: dict) -> str:
    return call_claude(
        "You are analyzing an evaluation of BrainCode, a formal language that LLM translators write using a fixed "
        "glossary of symbols (operations, constructors, claim relations, values, and value groups written "
        "group::key). " + f"{len(evidence['models'])} models " + "translated the same unseen items, three times each. Below is the measured "
        "evidence: coverage, Jensen-Shannon divergences, symbol and symbol-type use, statement-head counts per "
        "translation, symbols each model uses far less than the others, and the most divergent translations of the "
        "same item.\n\nAnswer these questions for a research paper, grounded only in this evidence. Cite numbers and "
        "quote short code fragments; say when the evidence is too thin to conclude something.\n\n" + QUESTIONS +
        "\n\nFormat: Markdown, one section per question (## 1. … ## 4.), then a short '## Caveats' section.\n\n"
        "<evidence>\n" + json.dumps(evidence, ensure_ascii=False, indent=1)[:180_000] + "\n</evidence>")


def call_claude(prompt: str, max_tokens: int = 8000) -> str:
    """One Messages API call to MODEL; the key comes from the environment (never printed)."""
    run_eval.prepare_keys()
    import os
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        sys.exit("qualitative: no Anthropic key (ANTHROPIC_API_KEY or CLAUDE_API_KEY)")
    body = json.dumps({"model": MODEL, "max_tokens": max_tokens,
                       "messages": [{"role": "user", "content": prompt}]}).encode("utf-8")
    req = urllib.request.Request("https://api.anthropic.com/v1/messages", data=body, method="POST", headers={
        "x-api-key": key, "anthropic-version": "2023-06-01", "content-type": "application/json"})
    with urllib.request.urlopen(req, timeout=600) as resp:
        data = json.loads(resp.read())
    return "".join(part.get("text", "") for part in data.get("content", []) if part.get("type") == "text")


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--run", default="main")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--results", default=None, help="results subfolder holding summary.json (default: the run id)")
    args = p.parse_args(argv)
    out = EVAL_DIR / "results" / (args.results or args.run)
    evidence = bundle(args.run, args.results)
    (out / "qualitative_determinism_js_evidence.json").write_text(json.dumps(evidence, ensure_ascii=False, indent=1),
                                                   encoding="utf-8")
    print(f"evidence: {len(json.dumps(evidence)):,} chars -> {out / 'qualitative_determinism_js_evidence.json'}")
    if args.dry_run:
        return
    report = ask_claude(evidence)
    name = "qualitative_determinism_js.md"
    (out / name).write_text(f"# Qualitative analysis: determinism (JS divergence of symbol use), written by {MODEL}"
                            "\n\n" + report + "\n", encoding="utf-8")
    print(f"wrote {out / name}")


if __name__ == "__main__":
    main()
