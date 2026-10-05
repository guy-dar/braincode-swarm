#!/usr/bin/env python3
"""Qualitative expressivity analysis (round trip, scored by BLEU / ROUGE-L /
word-Levenshtein): which kinds of input-output differences the back-translations
show, in general and per model, written by Claude from measured evidence.

For every scored pair (original item text vs its reconstruction from the
BrainCode alone, the same pairs as expressivity.md) it measures difference
types:

  length change        reconstruction words / original words
  language switch      original mostly non-English, reconstruction English
  turn structure       number of <|user|>/<|assistant|> turns differs
  list steps           number of numbered/bulleted steps differs
  numbers lost         share of the original's numbers missing from the output
  names lost           share of the original's capitalised names missing
  identifiers lost     share of code-like tokens (a_b, a.b, a/b, f()) missing
  added words          share of output words that never occur in the original

and writes results/<results>/expressivity_differences.md/.csv (the measured
table), then asks Claude Opus 5.5 to interpret it with paired examples and
writes qualitative_expressivity_bleu_rouge_levenshtein.md (its evidence bundle
next to it).

    python qualitative_expressivity.py --run main --results main-cov-det [--exclude a,b] [--dry-run]
"""
import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

EVAL_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(EVAL_DIR))
import analyze  # noqa: E402
import qualitative  # noqa: E402

NAME = "qualitative_expressivity_bleu_rouge_levenshtein"
TURN_RE = re.compile(r"<\|(user|assistant)\|>")
STEP_RE = re.compile(r"(?m)^\s*(?:\d+[.)]|[-*•])\s+")
NUMBER_RE = re.compile(r"\b\d+(?:[.,:]\d+)*\b")
NAME_RE = re.compile(r"(?<![.!?]\s)(?<!^)\b[A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)*")
IDENT_RE = re.compile(r"\b[A-Za-z_][\w]*(?:[._/][\w]+)+\b|\b\w+\(\)")
WORD_RE = re.compile(r"[^\W_]+", re.U)
EN_WORDS = {"the", "and", "to", "of", "a", "in", "is", "it", "you", "that", "for", "on", "with", "i", "this", "be",
            "are", "can", "my", "your", "what", "how", "do", "have", "not"}


def words(text):
    return [w.lower() for w in WORD_RE.findall(TURN_RE.sub(" ", text))]


def english_share(ws):
    return sum(w in EN_WORDS for w in ws) / max(1, len(ws))


def lost_share(pattern, original, recon):
    items = {m.strip().lower() for m in pattern.findall(TURN_RE.sub(" ", original))}
    if not items:
        return None
    rec = recon.lower()
    return sum(i not in rec for i in items) / len(items)


def differences(original: str, recon: str) -> dict:
    wo, wr = words(original), words(recon)
    so = set(wo)
    turns_o, turns_r = len(TURN_RE.findall(original)), len(TURN_RE.findall(recon))
    steps_o, steps_r = len(STEP_RE.findall(original)), len(STEP_RE.findall(recon))
    return {
        "length_ratio": len(wr) / max(1, len(wo)),
        "language_switch": english_share(wo) < 0.08 and english_share(wr) >= 0.08 and len(wo) >= 20,
        "turns_differ": turns_o != turns_r,
        "turns_original": turns_o, "turns_reconstruction": turns_r,
        "steps_differ": abs(steps_o - steps_r) >= 2,
        "numbers_lost": lost_share(NUMBER_RE, original, recon),
        "names_lost": lost_share(NAME_RE, original, recon),
        "identifiers_lost": lost_share(IDENT_RE, original, recon),
        "added_words": sum(w not in so for w in wr) / max(1, len(wr)),
    }


def mean(xs):
    xs = [x for x in xs if x is not None]
    return float(np.mean(xs)) if xs else None


def summarise(pairs):
    d = [p["diff"] for p in pairs]
    return {
        "pairs": len(pairs),
        "rouge_l": mean([p["rouge_l"] for p in pairs]), "bleu": mean([p["bleu"] for p in pairs]),
        "word_lev_sim": mean([p["word_lev_sim"] for p in pairs]),
        "length_ratio": mean([x["length_ratio"] for x in d]),
        "compressed_share": mean([x["length_ratio"] < 0.6 for x in d]),
        "expanded_share": mean([x["length_ratio"] > 1.4 for x in d]),
        "language_switch_share": mean([x["language_switch"] for x in d]),
        "turns_differ_share": mean([x["turns_differ"] for x in d]),
        "steps_differ_share": mean([x["steps_differ"] for x in d]),
        "numbers_lost": mean([x["numbers_lost"] for x in d]),
        "names_lost": mean([x["names_lost"] for x in d]),
        "identifiers_lost": mean([x["identifiers_lost"] for x in d]),
        "added_words": mean([x["added_words"] for x in d]),
    }


COLS = [("pairs", "pairs", 0), ("rouge_l", "ROUGE-L", 3), ("length_ratio", "length ratio", 2),
        ("compressed_share", "compressed (<0.6)", 2), ("expanded_share", "expanded (>1.4)", 2),
        ("language_switch_share", "language switch", 2), ("turns_differ_share", "turns differ", 2),
        ("steps_differ_share", "steps differ", 2), ("numbers_lost", "numbers lost", 2),
        ("names_lost", "names lost", 2), ("identifiers_lost", "identifiers lost", 2),
        ("added_words", "added words", 2)]


def table(rows, first):
    head = "| " + " | ".join([first] + [c[1] for c in COLS]) + " |"
    sep = "|---|" + "---:|" * len(COLS)
    lines = [head, sep]
    for key, r in rows:
        lines.append("| " + " | ".join([key] + [analyze.fmt(r[c[0]], c[2]) if c[2] else str(r[c[0]])
                                               for c in COLS]) + " |")
    return lines


def excerpt(text, n=700):
    text = text.strip()
    return text if len(text) <= n else text[:n] + " …[truncated]"


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--run", default="main")
    p.add_argument("--results", default=None)
    p.add_argument("--exclude", default="gpt-6.1-sol,gpt-6-luna")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args(argv)
    sys.path.insert(0, str(EVAL_DIR.parent / "swarm"))
    out = EVAL_DIR / "results" / (args.results or args.run)
    data = analyze.load(args.run, exclude=set(filter(None, args.exclude.split(","))))
    labels = {m["name"]: m["label"] for m in data["models"]}
    pairs = []
    for r in data["runs"]:
        if not r.get("back") or r["status"] not in ("success", "failed"):
            continue
        b = r["back"]
        pairs.append({"model": labels[r["model"]], "item": r["item"], "dataset": analyze.DS_LABELS[r["dataset"]],
                      "forward_status": r["status"], "shared": r["shared"], "rouge_l": b["rouge_l"],
                      "bleu": b["bleu"], "word_lev_sim": b["word_lev_sim"],
                      "quoted_share": analyze.quoted_share(r),
                      "diff": differences(b["original"], b["reconstruction"]),
                      "original": b["original"], "reconstruction": b["reconstruction"]})
    by_model, by_ds, by_model_ds = defaultdict(list), defaultdict(list), defaultdict(list)
    for x in pairs:
        by_model[x["model"]].append(x)
        by_ds[x["dataset"]].append(x)
        by_model_ds[(x["model"], x["dataset"])].append(x)
    model_rows = [(m, summarise(v)) for m, v in by_model.items()]
    shared_rows = [(m, summarise([x for x in v if x["shared"]])) for m, v in by_model.items()]
    ds_rows = [(d, summarise(by_ds[d])) for d in analyze.DS_LABELS.values() if by_ds.get(d)]
    analyze.write_csv(out / "expressivity_differences.csv",
                      [{"model": x["model"], "item": x["item"], "dataset": x["dataset"],
                        "forward_status": x["forward_status"], "rouge_l": x["rouge_l"], "bleu": x["bleu"],
                        "word_lev_sim": x["word_lev_sim"], "quoted_share": x["quoted_share"], **x["diff"]}
                       for x in pairs])
    md = ["# Expressivity: types of input-output differences (BLEU / ROUGE-L / word-Levenshtein round trip)", "",
          "Measured on every scored round trip (original item text vs the reconstruction written from the "
          "BrainCode alone). Shares are the fraction of pairs; `lost` columns are the mean share of the "
          "original's numbers / capitalised names / code-like identifiers missing from the reconstruction; "
          "`added words` is the share of reconstruction words that never occur in the original. "
          "`language switch` = original mostly non-English, reconstruction English. `turns differ` = number of "
          "user/assistant turns differs; `steps differ` = numbered/bulleted steps differ by 2 or more.", "",
          "## Per model (each model's full sample)", "", *table(model_rows, "model"), "",
          "## Per model (the 18 shared items only)", "", *table(shared_rows, "model"), "",
          "## Per dataset (all models)", "", *table(ds_rows, "dataset")]
    (out / "expressivity_differences.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    # examples: per model and dataset, the lowest- and highest-ROUGE-L pair
    examples = []
    for (m, d), v in sorted(by_model_ds.items()):
        v = sorted(v, key=lambda x: x["rouge_l"])
        for x in ({v[0]["item"]: v[0], v[-1]["item"]: v[-1]}).values():
            examples.append({"model": m, "dataset": d, "item": x["item"], "rouge_l": round(x["rouge_l"], 3),
                             "bleu": round(x["bleu"], 3), "word_lev_sim": round(x["word_lev_sim"], 3),
                             "differences": {k: (round(val, 2) if isinstance(val, float) else val)
                                             for k, val in x["diff"].items()},
                             "original": excerpt(x["original"]), "reconstruction": excerpt(x["reconstruction"])})
    evidence = {"metrics": "BLEU (n-gram precision), ROUGE-L (longest common subsequence F1), word-Levenshtein "
                           "similarity (1 - word edit distance / longer length); all on lower-cased words, 0-1, "
                           "higher = closer to the original",
                "per_model": dict(model_rows), "per_model_shared_items": dict(shared_rows),
                "per_dataset": dict(ds_rows), "examples": examples}
    (out / f"{NAME}_evidence.json").write_text(json.dumps(evidence, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"wrote {out / 'expressivity_differences.md'}; evidence {len(json.dumps(evidence)):,} chars")
    if args.dry_run:
        return
    report = qualitative.call_claude(
        "You are analyzing the expressivity evaluation of BrainCode, a formal language that LLM translators write "
        "with a fixed glossary of symbols. Each item (a prompt or a conversation) was translated into BrainCode, "
        "and the same model then reconstructed the natural-language item from the BrainCode alone, without seeing "
        "the original. The round trip is scored with BLEU, ROUGE-L and word-Levenshtein similarity. Below are "
        "measured difference types per model and per dataset, and paired examples (original vs reconstruction, "
        "the lowest- and highest-ROUGE-L pair per model and dataset).\n\n"
        "Write a qualitative analysis for a research paper, grounded only in this evidence:\n"
        "1. The general types of input-output differences (what is lost, changed or added in a round trip), "
        "with how common each is and short quoted examples.\n"
        "2. Per model: which difference types each model tends to produce more or less than the others, with "
        "numbers and examples.\n"
        "3. Per dataset: which kinds of input lose the most or least, and why, judging from the examples.\n"
        "4. How the three metrics react to these difference types (for example, which differences BLEU punishes "
        "that ROUGE-L or word-Levenshtein tolerate), with cases where they disagree.\n"
        "Cite numbers from the tables and quote short fragments. Say where the evidence is too thin (some models "
        "have few pairs).\n\nFormat: Markdown, sections '## 1. Types of differences', '## 2. Per model', "
        "'## 3. Per dataset', '## 4. Metrics and difference types', then '## Caveats'.\n\n"
        "<evidence>\n" + json.dumps(evidence, ensure_ascii=False, indent=1)[:180_000] + "\n</evidence>")
    (out / f"{NAME}.md").write_text(
        f"# Qualitative analysis: expressivity (BLEU / ROUGE-L / word-Levenshtein round trip), written by "
        f"{qualitative.MODEL}\n\n" + report + "\n", encoding="utf-8")
    print(f"wrote {out / (NAME + '.md')}")


if __name__ == "__main__":
    main()
