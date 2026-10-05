#!/usr/bin/env python3
"""Combine an analysis folder's reports and figures into one .docx (needs pandoc).

    python export_report.py --results main-cov-det     # -> results/main-cov-det/evaluation_report.docx
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

EVAL_DIR = Path(__file__).resolve().parent

SECTIONS = [  # (title, report file, figures with captions)
    ("Coverage", "coverage.md", [
        ("coverage_radar_shared.png", "Success rate per dataset on the 18 items shared by all models."),
        ("coverage_radar_gemini.png", "Gemini success rate per dataset on all 48 items."),
    ]),
    ("Determinism", "determinism.md", [
        ("js_heatmap_symbols.png", "JS divergence between models: symbols used."),
        ("js_heatmap_types.png", "JS divergence between models: symbol types used."),
        ("self_divergence.png", "Same-model divergence over 3 runs per item."),
        ("self_divergence_by_dataset.png", "Same-model divergence per dataset."),
        ("symbol_type_mix.png", "Share of symbol types per model."),
        ("determinism_vs_coverage.png", "Success rate against same-model divergence."),
    ]),
    ("Expressivity", "expressivity.md", [
        ("expressivity.png", "Round-trip similarity per dataset (Gemini models; OpenAI is left out of all figures, see the tables)."),
    ]),
    ("Expressivity: types of input-output differences", "expressivity_differences.md", []),
    ("Failed translations", "failures.md", []),
    ("Qualitative analysis: determinism (JS divergence of symbol use)", "qualitative_determinism_js.md", []),
    ("Qualitative analysis: expressivity (BLEU / ROUGE-L / word-Levenshtein round trip)",
     "qualitative_expressivity_bleu_rouge_levenshtein.md", []),
]


def body_of(md: str) -> str:
    """Drop the file's own H1 lines and demote the other headings one level."""
    out = []
    for line in md.splitlines():
        if re.match(r"^# ", line):
            continue
        out.append("#" + line if re.match(r"^#{2,5} ", line) else line)
    return "\n".join(out).strip()


def overview(summary: dict) -> str:
    rows = ["| company | model | tier |", "|---|---|---|"]
    rows += [f"| {m['company']} | {m['label']} | {m['tier']} |" for m in summary["models"]]
    return "\n".join([
        "## Overview", "",
        "Unseen test items were translated into BrainCode (spec 19.0.0-draft.2-lexical-groups, glossary g19) "
        "with the swarm translator setup: compact spec, glossary RAG, pi harness in Docker. Gemini models "
        "translated 48 items (8 per dataset, stratified, at most 6,000 characters) three times each. The other "
        "models translated the 18 items shared with Gemini (3 per dataset), three times each. GPT-6.1 Sol and GPT-6 Luna were stopped part-way (0 successes) and "
        "are left out of this report. Expressivity (back-translation) covers the Gemini models and o4-mini: "
        "the back-translator sees only the BrainCode, and the scores compare the original item text with the "
        "reconstructed text only.", "",
        "Translations that carry natural language instead of encoding it (claimed successes with needs marked "
        "opaque, or any translation with a quoted string of 8+ words outside names/titles; spec §13) are counted as errors and left out of the "
        "determinism, expressivity and qualitative analyses. o4-mini, where this happened 3 times, translated those "
        "3 items again with the corrected success check; like the other models it has 3 runs per shared item "
        "(54), 3 of them the rejected ones. Expressivity uses one back-translation per model and item (its "
        "first usable run).", "",
        *rows])


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--results", default="main-cov-det")
    p.add_argument("--out", default="evaluation_report.docx")
    args = p.parse_args(argv)
    pandoc = shutil.which("pandoc")
    if not pandoc:
        sys.exit("export_report: pandoc not found")
    d = EVAL_DIR / "results" / args.results
    summary = json.loads((d / "summary.json").read_text(encoding="utf-8"))
    parts = ["---", "title: BrainCode language evaluation", "subtitle: Coverage, determinism and expressivity",
             "---", "", overview(summary)]
    for title, name, figures in SECTIONS:
        f = d / name
        if not f.exists():
            continue
        parts += ["", f"## {title}", "", body_of(f.read_text(encoding="utf-8"))]
        for fig, caption in figures:
            if (d / fig).exists():
                parts += ["", f"![{caption}]({fig}){{width=16cm}}"]
    md = d / "evaluation_report.md"
    md.write_text("\n".join(parts) + "\n", encoding="utf-8")
    out = d / args.out
    subprocess.run([pandoc, str(md), "-o", str(out), "--resource-path", str(d), "--toc",
                    "--shift-heading-level-by=-1"], check=True)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
