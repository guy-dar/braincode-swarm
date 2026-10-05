#!/usr/bin/env python3
"""Tables and figures for a finished evaluation run -> results/<run>/.

    python analyze.py --run main

Coverage      coverage.md/.csv, coverage_radar_shared.png (all models, the
              shared items), coverage_radar_gemini.png (Gemini, all items)
Determinism   determinism.md/.csv, js_heatmap_symbols.png, js_heatmap_types.png,
              self_divergence.png, self_divergence_by_dataset.png,
              symbol_type_mix.png, determinism_vs_coverage.png
Expressivity  expressivity.md/.csv, expressivity.png (Gemini models and o4-mini)
summary.json  everything above as numbers (qualitative.py reads it)

Every figure has a table view (the .md/.csv next to it). Color = company
(blue Gemini, orange Claude, aqua OpenAI: the reference palette's first three
slots, which validate all-pairs); tier is a second encoding (strong = solid
line / filled marker, weak = dashed / hollow).
"""
import argparse
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

EVAL_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(EVAL_DIR))
import metrics  # noqa: E402

DATASETS = ("mind2web", "alfred", "swebench", "prism", "paths", "thoughttrace")
DS_LABELS = {"mind2web": "Mind2Web", "alfred": "ALFRED", "swebench": "SWE-bench", "prism": "PRISM",
             "paths": "PATHs", "thoughttrace": "ThoughtTrace"}
COMPANIES = ("Gemini", "Claude", "OpenAI")
COMPANY_COLOR = {"Gemini": "#2a78d6", "Claude": "#eb6834", "OpenAI": "#1baf7a"}
SURFACE, INK, INK_2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e2dc"
BLUES = ["#f0f6fe", "#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95", "#0d366b"]
PROPOSED_RE = re.compile(r"#\s*PROPOSED:\s*(S\d+)")


# Companies left out of every figure (tables keep them); set by --plot-hide-companies.
PLOT_HIDE_COMPANIES = set()


def plotted(models: list) -> list:
    return [m for m in models if m["company"] not in PLOT_HIDE_COMPANIES]


def style():
    plt.rcParams.update({
        "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE,
        "axes.edgecolor": GRID, "axes.labelcolor": INK_2, "axes.titlecolor": INK, "axes.titlesize": 11,
        "axes.titleweight": "bold", "xtick.color": INK_2, "ytick.color": INK_2, "axes.grid": True,
        "grid.color": GRID, "grid.linewidth": 0.8, "axes.axisbelow": True, "axes.spines.top": False,
        "axes.spines.right": False, "legend.frameon": False, "legend.fontsize": 8.5, "legend.labelcolor": INK_2,
        "lines.linewidth": 2, "font.size": 9.5,
    })


def line_style(model: dict) -> dict:
    strong = model["tier"] == "strong"
    return {"color": COMPANY_COLOR[model["company"]], "linestyle": "-" if strong else (0, (4, 2)),
            "marker": "o", "markerfacecolor": COMPANY_COLOR[model["company"]] if strong else SURFACE,
            "markeredgecolor": COMPANY_COLOR[model["company"]], "markersize": 5}


def save(fig, path: Path):
    """Save a figure; a PNG held open by a viewer (Windows locks it) is retried,
    then reported instead of aborting the whole analysis."""
    import time
    try:
        for attempt in range(5):
            try:
                fig.savefig(path, dpi=150, bbox_inches="tight")
                return
            except OSError:
                time.sleep(1.5)
        print(f"WARNING: could not write {path.name} (open in a viewer?) - close it and rerun", file=sys.stderr)
    finally:
        plt.close(fig)


# ---------------------------------------------------------------------- loading

def load(run: str, exclude=()) -> dict:
    d = EVAL_DIR / "runs" / run
    models = {m["name"]: m for m in json.loads((EVAL_DIR / "models.json").read_text(encoding="utf-8"))["models"]}
    items = {json.loads(l)["item_key"]: json.loads(l) for l in
             (d / "items.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()}
    kinds = metrics.glossary_kinds(d / "reference" / "glossary.jsonl")
    runs = []
    for p in sorted(d.glob("*/*/r*/result.json")):
        r = json.loads(p.read_text(encoding="utf-8"))
        if r["model"] not in models or r["model"] in exclude or r["status"] == "skipped":
            continue
        r["dir"] = p.parent
        r["shared"] = items[r["item"]]["all_models"]
        doc = p.parent / "translation.md"
        r["symbols"], r["types"] = (metrics.symbol_counts(doc.read_text(encoding="utf-8"), kinds)
                                    if doc.exists() else (Counter(), Counter()))
        r["missing"] = missing_symbols(p.parent) if r["status"] == "failed" else None
        back = p.parent / "back" / "reconstruction.md"
        if back.exists():
            original = (d / "items" / r["item"] / "item_raw.txt").read_text(encoding="utf-8")
            recon = back.read_text(encoding="utf-8")
            r["back"] = {"bleu": metrics.bleu(original, recon), "rouge_l": metrics.rouge_l(original, recon),
                         "word_lev_sim": metrics.word_levenshtein_similarity(original, recon),
                         "original": original, "reconstruction": recon}
        runs.append(r)
    present = [m for m in models.values() if any(r["model"] == m["name"] for r in runs)]
    present.sort(key=lambda m: (COMPANIES.index(m["company"]), m["tier"] != "strong"))
    return {"dir": d, "models": present, "items": items, "runs": runs}


def missing_symbols(run_dir: Path) -> int:
    """Distinct symbols a failed translation needed and the glossary lacks:
    its `add` suggestions, or else its distinct `# PROPOSED: S<k>` markers."""
    sugg = run_dir / "suggestions.md"
    adds = set()
    if sugg.exists():
        import loop_files as lf
        adds = {s["value"] for s in lf.parse_suggestions(sugg.read_text(encoding="utf-8")) if s["type"] == "add"}
    if adds:
        return len(adds)
    doc = run_dir / "translation.md"
    return len(set(PROPOSED_RE.findall(doc.read_text(encoding="utf-8")))) if doc.exists() else 0


def rate(runs: list, status="success"):
    return sum(r["status"] == status for r in runs) / len(runs) if runs else float("nan")


def fmt(x, digits=2):
    return "—" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{x:.{digits}f}"


# ---------------------------------------------------------------------- coverage

def coverage(data: dict, out: Path) -> dict:
    rows = []
    for m in data["models"]:
        for scope in ("shared", "all"):
            if scope == "all" and m["sample"] != "all":
                continue
            rs = [r for r in data["runs"] if r["model"] == m["name"] and (scope == "all" or r["shared"])]
            failed = [r["missing"] for r in rs if r["status"] == "failed"]
            costs = [r.get("cost_usd") for r in rs if r.get("cost_usd") is not None]
            rows.append({
                "company": m["company"], "model": m["label"], "tier": m["tier"], "items": scope,
                "runs": len(rs), "success_rate": rate(rs), "failed_rate": rate(rs, "failed"),
                "error_rate": rate(rs, "error"),
                "rejected_successes": sum(bool(r.get("regated")) for r in rs),
                "missing_symbols_per_failed": float(np.mean(failed)) if failed else None,
                "mean_minutes": float(np.mean([r.get("duration_s", 0) for r in rs])) / 60 if rs else None,
                "cost_usd": sum(costs) if costs else None,
                **{f"success_{ds}": rate([r for r in rs if r["dataset"] == ds]) for ds in DATASETS},
            })
    write_csv(out / "coverage.csv", rows)
    lines = ["# Coverage: translating unseen test items", "",
             "Success rate (higher is better) and mean number of missing glossary symbols per failed translation "
             "(the distinct symbols its suggestions add). `shared` = the items every model translated; `all` = the "
             "full sample (Gemini models).", "",
             "`rejected` = claimed successes and declared failures counted as errors because they carry source text instead of encoding it "
             "(needs marked opaque, or quoted strings of 8+ words outside names/titles; spec §13). They are included in "
             "`error` and left out of the determinism and expressivity analyses.", "",
             "| company | model | tier | items | runs | success | failed | error | rejected | missing symbols / failed | "
             "min / run | cost $ |", "|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for r in rows:
        lines.append(f"| {r['company']} | {r['model']} | {r['tier']} | {r['items']} | {r['runs']} | "
                     f"{fmt(r['success_rate'])} | {fmt(r['failed_rate'])} | {fmt(r['error_rate'])} | {r['rejected_successes']} | "
                     f"{fmt(r['missing_symbols_per_failed'], 1)} | {fmt(r['mean_minutes'], 1)} | "
                     f"{fmt(r['cost_usd'])} |")
    lines += ["", "Success rate per dataset:", "",
              "| model | items | " + " | ".join(DS_LABELS[d] for d in DATASETS) + " |",
              "|---|---|" + "---:|" * len(DATASETS)]
    for r in rows:
        lines.append(f"| {r['model']} | {r['items']} | " + " | ".join(fmt(r[f'success_{d}']) for d in DATASETS) + " |")
    (out / "coverage.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    radar(data, plotted(data["models"]), "shared", out / "coverage_radar_shared.png",
          "Translation success rate per dataset (items shared by all models)")
    gem = [m for m in data["models"] if m["sample"] == "all"]
    if gem:
        radar(data, gem, "all", out / "coverage_radar_gemini.png",
              "Translation success rate per dataset (Gemini models, full sample)")
    return {"rows": rows}


def radar(data: dict, models: list, scope: str, path: Path, title: str):
    companies = [c for c in COMPANIES if any(m["company"] == c for m in models)]
    angles = np.linspace(0, 2 * np.pi, len(DATASETS), endpoint=False).tolist()
    fig, axes = plt.subplots(1, len(companies), figsize=(4.6 * len(companies), 4.9),
                             subplot_kw={"projection": "polar"}, squeeze=False)
    fig.suptitle(title, x=0.02, ha="left", fontsize=12, fontweight="bold", color=INK)
    for ax, company in zip(axes[0], companies):
        for m in [m for m in models if m["company"] == company]:
            rs = [r for r in data["runs"] if r["model"] == m["name"] and (scope == "all" or r["shared"])]
            vals = [rate([r for r in rs if r["dataset"] == ds]) for ds in DATASETS]
            vals = [0.0 if np.isnan(v) else v for v in vals]
            st = line_style(m)
            ax.plot(angles + angles[:1], vals + vals[:1], label=f"{m['label']} ({m['tier']})", **st)
            ax.fill(angles + angles[:1], vals + vals[:1], color=st["color"], alpha=0.10 if m["tier"] == "strong" else 0.04)
        ax.set_theta_offset(np.pi / 2)    # first dataset at the top, clockwise: no labels at 3 and 9 o'clock
        ax.set_theta_direction(-1)
        ax.set_xticks(angles)
        ax.set_xticklabels([DS_LABELS[d] for d in DATASETS], color=INK_2, fontsize=8.5)
        ax.tick_params(axis="x", pad=6)
        ax.set_ylim(0, 1)
        ax.set_yticks([0.25, 0.5, 0.75, 1.0])
        ax.set_yticklabels(["25%", "50%", "75%", "100%"], fontsize=7, color=INK_2)
        ax.set_title(company, pad=14)
        ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.08), ncol=1)
    fig.subplots_adjust(wspace=0.45)
    save(fig, path)


# ---------------------------------------------------------------------- determinism

def determinism(data: dict, out: Path) -> dict:
    models = data["models"]
    shared = [r for r in data["runs"] if r["shared"] and r["status"] in ("success", "failed")]
    pooled = {m["name"]: (sum((r["symbols"] for r in shared if r["model"] == m["name"]), Counter()),
                          sum((r["types"] for r in shared if r["model"] == m["name"]), Counter())) for m in models}
    names = [m["name"] for m in models]
    js_sym = np.array([[metrics.js_divergence(pooled[a][0], pooled[b][0]) for b in names] for a in names])
    js_typ = np.array([[metrics.js_divergence(pooled[a][1], pooled[b][1]) for b in names] for a in names])
    by_name = {m["name"]: m for m in models}
    pairs = []
    for a, b in combinations(names, 2):
        ma, mb = by_name[a], by_name[b]
        if ma["company"] == mb["company"]:
            kind = "weak vs strong, same company"
        elif ma["tier"] == mb["tier"]:
            kind = f"{ma['tier']} vs {mb['tier']}, different companies"
        else:
            kind = "other"
        pairs.append({"model_a": ma["label"], "model_b": mb["label"], "pair": kind,
                      "js_symbols": js_sym[names.index(a), names.index(b)],
                      "js_types": js_typ[names.index(a), names.index(b)]})
    self_rows = []
    for m in models:
        for scope in ("shared", "all"):
            if scope == "all" and m["sample"] != "all":
                continue
            rs = [r for r in data["runs"] if r["model"] == m["name"] and r["status"] in ("success", "failed")
                  and (scope == "all" or r["shared"])]
            per_item = defaultdict(list)
            for r in rs:
                per_item[r["item"]].append(r)
            sym_vals, typ_vals, same, by_ds = [], [], [], defaultdict(list)
            for item, runs in per_item.items():
                v, ident = metrics.mean_pairwise_js([r["symbols"] for r in runs])
                vt, _ = metrics.mean_pairwise_js([r["types"] for r in runs])
                if v is None:
                    continue
                sym_vals.append(v)
                typ_vals.append(vt)
                same.append(ident)
                by_ds[data["items"][item]["dataset"]].append(v)
            self_rows.append({"company": m["company"], "model": m["label"], "name": m["name"], "tier": m["tier"],
                              "items": scope, "items_with_2plus_runs": len(sym_vals),
                              "self_js_symbols": float(np.mean(sym_vals)) if sym_vals else None,
                              "self_js_symbols_sd": float(np.std(sym_vals)) if sym_vals else None,
                              "self_js_types": float(np.mean(typ_vals)) if typ_vals else None,
                              "identical_pair_share": float(np.mean(same)) if same else None,
                              **{f"self_js_{d}": (float(np.mean(by_ds[d])) if by_ds[d] else None) for d in DATASETS}})
    write_csv(out / "determinism_pairs.csv", pairs)
    write_csv(out / "determinism_self.csv", self_rows)
    lines = ["# Determinism", "",
             "Jensen-Shannon divergence (base 2, 0 = identical symbol use, 1 = disjoint; lower = more alike) between "
             "the symbol distributions P(symbol | model) and P(symbol type | model), pooled over every translation of "
             "the shared items. Same-model divergence: for each item, the mean JS over its pairs of runs; then the "
             "mean over items.", "", "## Model pairs", "",
             "| pair | model A | model B | JS symbols | JS types |", "|---|---|---|---:|---:|"]
    for p in sorted(pairs, key=lambda p: p["pair"]):
        if p["pair"] != "other":
            lines.append(f"| {p['pair']} | {p['model_a']} | {p['model_b']} | {fmt(p['js_symbols'], 3)} | "
                         f"{fmt(p['js_types'], 3)} |")
    lines += ["", "## Same model, repeated runs", "",
              "| model | items | items with ≥2 runs | JS symbols (mean ± sd) | JS types | identical run pairs |",
              "|---|---|---:|---:|---:|---:|"]
    for r in self_rows:
        lines.append(f"| {r['model']} | {r['items']} | {r['items_with_2plus_runs']} | "
                     f"{fmt(r['self_js_symbols'], 3)} ± {fmt(r['self_js_symbols_sd'], 3)} | "
                     f"{fmt(r['self_js_types'], 3)} | {fmt(r['identical_pair_share'])} |")
    (out / "determinism.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    shown = plotted(models)
    idx = [models.index(m) for m in shown]
    labels = [m["label"] for m in shown]
    heatmap(js_sym[np.ix_(idx, idx)], labels, out / "js_heatmap_symbols.png",
            "JS divergence between models: symbols used")
    heatmap(js_typ[np.ix_(idx, idx)], labels, out / "js_heatmap_types.png",
            "JS divergence between models: symbol types used")
    shown_rows = [r for r in self_rows if any(m["name"] == r["name"] for m in shown)]
    self_bars(shown_rows, shown, out / "self_divergence.png")
    self_by_dataset(shown_rows, shown, out / "self_divergence_by_dataset.png")
    type_mix(pooled, models, out / "symbol_type_mix.png")   # every model, OpenAI included
    return {"pairs": pairs, "self": self_rows,
            "pooled_top_symbols": {by_name[n]["label"]: pooled[n][0].most_common(25) for n in names},
            "pooled_types": {by_name[n]["label"]: dict(pooled[n][1]) for n in names}}


def heatmap(matrix, labels, path, title):
    fig, ax = plt.subplots(figsize=(1.0 * len(labels) + 2.6, 0.85 * len(labels) + 1.6))
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("blues", BLUES)
    im = ax.imshow(matrix, cmap=cmap, vmin=0, vmax=max(0.05, float(matrix.max())))
    ax.set_xticks(range(len(labels)), labels, rotation=30, ha="right")
    ax.set_yticks(range(len(labels)), labels)
    ax.grid(False)
    for i in range(len(labels)):
        for j in range(len(labels)):
            v = matrix[i, j]
            ax.text(j, i, f"{v:.2f}", ha="center", va="center", fontsize=8.5,
                    color="#ffffff" if v > 0.6 * matrix.max() else INK)
    ax.set_title(title, loc="left")
    cb = fig.colorbar(im, ax=ax, fraction=0.045)
    cb.set_label("JS divergence (lower = more alike)", color=INK_2)
    save(fig, path)


def self_bars(rows, models, path):
    shared = [r for r in rows if r["items"] == "shared" and r["self_js_symbols"] is not None]
    if not shared:
        return
    fig, ax = plt.subplots(figsize=(8, 4.2))
    xs = np.arange(len(shared))
    for x, r in zip(xs, shared):
        m = next(m for m in models if m["name"] == r["name"])
        c = COMPANY_COLOR[m["company"]]
        ax.bar(x, r["self_js_symbols"], width=0.6, color=c if m["tier"] == "strong" else SURFACE, edgecolor=c,
               linewidth=2, hatch=None if m["tier"] == "strong" else "///")
        ax.errorbar(x, r["self_js_symbols"], yerr=r["self_js_symbols_sd"], color=INK_2, capsize=3, linewidth=1)
        ax.annotate(f"{r['self_js_symbols']:.2f}", (x, r["self_js_symbols"]), xytext=(0, 4),
                    textcoords="offset points", ha="center", fontsize=8.5, color=INK_2)
    ax.set_xticks(xs, [r["model"] for r in shared], rotation=20, ha="right")
    ax.set_ylabel("JS divergence between runs (lower = more deterministic)")
    ax.set_title("Same-model divergence over 3 runs per item (shared items; bar = mean, whisker = sd)", loc="left")
    ax.set_ylim(bottom=0)
    save(fig, path)


def self_by_dataset(rows, models, path):
    shared = [r for r in rows if r["items"] == "shared"]
    if not shared:
        return
    fig, ax = plt.subplots(figsize=(9, 4.4))
    width = 0.8 / max(1, len(shared))
    for i, r in enumerate(shared):
        m = next(m for m in models if m["name"] == r["name"])
        c = COMPANY_COLOR[m["company"]]
        vals = [r[f"self_js_{d}"] if r[f"self_js_{d}"] is not None else np.nan for d in DATASETS]
        ax.bar(np.arange(len(DATASETS)) + (i - (len(shared) - 1) / 2) * width, vals, width=width * 0.92,
               color=c if m["tier"] == "strong" else SURFACE, edgecolor=c, linewidth=1.5,
               hatch=None if m["tier"] == "strong" else "///", label=r["model"])
    ax.set_xticks(range(len(DATASETS)), [DS_LABELS[d] for d in DATASETS])
    ax.set_ylabel("JS divergence between runs (lower = more deterministic)")
    ax.set_title("Same-model divergence by dataset (shared items)", loc="left")
    ax.legend(ncol=3, loc="upper left", bbox_to_anchor=(0, -0.12))
    ax.set_ylim(bottom=0)
    save(fig, path)


def type_mix(pooled, models, path):
    kinds = Counter()
    for m in models:
        kinds.update(pooled[m["name"]][1])
    top = [k for k, _ in kinds.most_common(7)]
    fig, ax = plt.subplots(figsize=(9, 0.55 * len(models) + 1.8))
    seq = ["#0d366b", "#184f95", "#2a78d6", "#6da7ec", "#9ec5f4", "#cde2fb", "#f0f6fe", "#d9d7d0"]
    for i, m in enumerate(models):
        counts = pooled[m["name"]][1]
        total = sum(counts.values()) or 1
        left = 0.0
        for j, k in enumerate(top + ["other"]):
            v = (counts.get(k, 0) if k != "other" else total - sum(counts.get(t, 0) for t in top)) / total
            ax.barh(i, v, left=left, color=seq[j], edgecolor=SURFACE, linewidth=1.5,
                    label=k.replace("_", " ") if i == 0 else None)
            if v >= 0.08:
                ax.text(left + v / 2, i, f"{v:.0%}", ha="center", va="center", fontsize=7.5,
                        color="#ffffff" if j < 3 else INK)
            left += v
    ax.set_yticks(range(len(models)), [m["label"] for m in models])
    ax.invert_yaxis()
    ax.set_xlim(0, 1)
    ax.xaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0))
    ax.set_title("Share of symbol types used (shared items, all runs)", loc="left")
    ax.legend(ncol=4, loc="upper left", bbox_to_anchor=(0, -0.08))
    ax.grid(axis="y", visible=False)
    save(fig, path)


def det_vs_cov(cov, det, models, path):
    fig, ax = plt.subplots(figsize=(6.4, 4.6))
    for m in models:
        c = next((r for r in cov["rows"] if r["model"] == m["label"] and r["items"] == "shared"), None)
        s = next((r for r in det["self"] if r["name"] == m["name"] and r["items"] == "shared"), None)
        if not c:
            continue
        st = line_style(m)
        if not s or s["self_js_symbols"] is None:
            # no item with 2+ usable runs (e.g. a 1-run probe): no y value, so a
            # vertical line at its success rate rather than an invented point
            ax.axvline(c["success_rate"], color=st["color"], linestyle=(0, (4, 2)), linewidth=1.5, zorder=2)
            ax.annotate(f"{m['label']}: no same-model value\n(1 usable run per item)", (c["success_rate"], 0.98),
                        xycoords=("data", "axes fraction"), xytext=(6, 0), textcoords="offset points",
                        va="top", fontsize=8.5, color=INK_2)
            continue
        ax.scatter(c["success_rate"], s["self_js_symbols"], s=70, color=st["markerfacecolor"],
                   edgecolors=st["color"], linewidths=2, zorder=3)
        ax.annotate(m["label"], (c["success_rate"], s["self_js_symbols"]), xytext=(6, 4), textcoords="offset points",
                    fontsize=8.5, color=INK_2)
    ax.set_xlabel("Success rate (higher = better)")
    ax.set_ylabel("Same-model JS divergence (lower = more deterministic)")
    ax.set_title("Coverage vs determinism (shared items)", loc="left")
    ax.xaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0))
    save(fig, path)


# ---------------------------------------------------------------------- expressivity

def quoted_share(run: dict) -> float:
    """Share of the BrainCode's characters inside quoted string literals: text
    carried verbatim rather than encoded in symbols (a round trip of it is a copy)."""
    code = metrics.braincode_code((run["dir"] / "translation.md").read_text(encoding="utf-8"))
    code = "\n".join(line.split("#", 1)[0] for line in code.splitlines())
    return sum(len(q) for q in metrics.QUOTED_RE.findall(code)) / max(1, len(code))


def expressivity(data: dict, out: Path) -> dict:
    rows = []
    for m in data["models"]:
        # errors (incl. successes the gate rejected on re-check) are left out
        rs = [r for r in data["runs"] if r["model"] == m["name"] and r.get("back")
              and r["status"] in ("success", "failed")]
        if not rs:
            continue
        own = "all" if m["sample"] == "all" else "shared"
        scopes = [(own, ds) for ds in (None, *DATASETS)] + ([("shared", None)] if own == "all" else [])
        for scope, ds in scopes:
            sub = [r for r in rs if (ds is None or r["dataset"] == ds) and (scope == "all" or r["shared"])]
            if not sub:
                continue
            rows.append({"model": m["label"], "items": scope, "dataset": DS_LABELS[ds] if ds else "all",
                         "pairs": len(sub),
                         "bleu": float(np.mean([r["back"]["bleu"] for r in sub])),
                         "corpus_bleu": metrics.corpus_bleu([r["back"]["original"] for r in sub],
                                                            [r["back"]["reconstruction"] for r in sub]),
                         "rouge_l": float(np.mean([r["back"]["rouge_l"] for r in sub])),
                         "word_lev_sim": float(np.mean([r["back"]["word_lev_sim"] for r in sub])),
                         "quoted_share": float(np.mean([quoted_share(r) for r in sub])),
                         "from_success": sum(r["status"] == "success" for r in sub)})
    if not rows:
        return {"rows": []}
    write_csv(out / "expressivity.csv", rows)
    lines = ["# Expressivity: round trip natural language → BrainCode → natural language", "",
             "**Every score is in [0, 1] and higher = input and output more similar = better.** BLEU = mean sentence "
             "BLEU (and corpus BLEU); ROUGE-L = longest-common-subsequence F1; word-Levenshtein similarity = "
             "1 − word edit distance / longer length. One forward translation per item (its first usable run) is back-translated by the same model "
             "without seeing the original: the back-translator gets only the BrainCode block of the translation (not "
             "the translation report), and the scores compare only the original item text (input) with the "
             "reconstructed text (output), turn markers removed.", "",
             "`items`: `all` = the model's full sample (Gemini: 48 items); `shared` = the 18 items every model "
             "translated (use these rows to compare models; o4-mini has back-translations only where its forward "
             "run produced a usable translation). Per-dataset rows and the figure use each model's full sample.", "",
             "`quoted` = share of the BrainCode's characters inside quoted string literals (`content=\"…\"` and "
             "other literals). Text carried verbatim in strings comes back almost unchanged, so a high score with a "
             "high quoted share measures copying, not how much meaning the symbols encode.", "",
             "| model | items | dataset | pairs | BLEU ↑ | corpus BLEU ↑ | ROUGE-L ↑ | word-Levenshtein similarity ↑ | quoted |",
             "|---|---|---|---:|---:|---:|---:|---:|---:|"]
    for r in sorted(rows, key=lambda r: (r["dataset"] != "all", r["items"] != "shared")):
        lines.append(f"| {r['model']} | {r['items']} | {r['dataset']} | {r['pairs']} | {fmt(r['bleu'], 3)} | "
                     f"{fmt(r['corpus_bleu'], 3)} | {fmt(r['rouge_l'], 3)} | {fmt(r['word_lev_sim'], 3)} | "
                     f"{fmt(r['quoted_share'])} |")
    (out / "expressivity.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    fig, axes = plt.subplots(1, 3, figsize=(13, 4.3), sharey=True)
    fig.suptitle("Round-trip similarity per dataset (higher = more similar = better)", x=0.02, ha="left",
                 fontsize=12, fontweight="bold", color=INK)
    models = [m for m in plotted(data["models"]) if any(r["model"] == m["label"] for r in rows)]
    width = 0.8 / max(1, len(models))
    for ax, key, title in zip(axes, ("bleu", "rouge_l", "word_lev_sim"),
                              ("BLEU", "ROUGE-L", "Word-Levenshtein similarity")):
        for i, m in enumerate(models):
            vals = [next((r[key] for r in rows if r["model"] == m["label"] and r["dataset"] == DS_LABELS[d]), np.nan)
                    for d in DATASETS]
            c = COMPANY_COLOR[m["company"]]
            ax.bar(np.arange(len(DATASETS)) + (i - (len(models) - 1) / 2) * width, vals, width=width * 0.92,
                   color=c if m["tier"] == "strong" else SURFACE, edgecolor=c, linewidth=1.5,
                   hatch=None if m["tier"] == "strong" else "///", label=m["label"])
        ax.set_xticks(range(len(DATASETS)), [DS_LABELS[d] for d in DATASETS], rotation=30, ha="right")
        ax.set_title(title, loc="left")
        ax.set_ylim(0, 1)
    axes[0].set_ylabel("Score (0-1, higher = better)")
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=len(labels), bbox_to_anchor=(0.5, -0.16))
    save(fig, out / "expressivity.png")
    return {"rows": rows}


def failures(data: dict, out: Path) -> dict:
    """failures.md: every failed translation with the terms it would add or
    refine (its own documentation, from result.json / suggestions.md), and the
    terms most often missing per model."""
    rows, per_model = [], defaultdict(Counter)
    for r in sorted(data["runs"], key=lambda r: (r["model"], r["item"], r["run"])):
        if r["status"] != "failed":
            continue
        res = json.loads((r["dir"] / "result.json").read_text(encoding="utf-8"))
        f = res.get("failure") or {}
        adds = [a["term"] for a in f.get("would_add") or []]
        refines = [x["target"] for x in f.get("would_refine") or []]
        per_model[r["model"]].update(adds)
        rows.append({"model": r["model"], "item": r["item"], "dataset": r["dataset"], "run": r["run"],
                     "add_count": len(set(adds)), "would_add": ", ".join(adds),
                     "refine_count": len(set(refines)), "would_refine": ", ".join(refines),
                     "documented": f.get("documented", False)})
    write_csv(out / "failures.csv", rows)
    labels = {m["name"]: m["label"] for m in data["models"]}
    lines = ["# Failed translations and what they were missing", "",
             "Every failed run, with the terms its translator documented as missing from the glossary "
             "(`add`) or needing a change (`refine`), from its suggestions.", "",
             "| model | item | run | adds | terms it would add | refines | targets |", "|---|---|---:|---:|---|---:|---|"]
    for r in rows:
        lines.append(f"| {labels.get(r['model'], r['model'])} | {r['item']} | r{r['run']} | {r['add_count']} | "
                     f"{r['would_add'] or '—'} | {r['refine_count']} | {r['would_refine'] or '—'} |")
    lines += ["", "## Most frequent missing terms per model", ""]
    for m, c in per_model.items():
        lines.append(f"- **{labels.get(m, m)}**: " + ", ".join(f"{t} ({n})" for t, n in c.most_common(15)))
    (out / "failures.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"rows": rows}


def write_csv(path: Path, rows: list):
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--run", default="main")
    p.add_argument("--exclude", default="", help="comma-separated model names to leave out")
    p.add_argument("--only", default="coverage,determinism,expressivity,failures",
                   help="comma-separated analyses to run (summary.json only when all run)")
    p.add_argument("--out", default=None, help="results subfolder (default: the run id)")
    p.add_argument("--plot-hide-companies", default="",
                   help="comma-separated companies left out of every figure (tables keep them)")
    args = p.parse_args(argv)
    PLOT_HIDE_COMPANIES.update(filter(None, args.plot_hide_companies.split(",")))
    only = set(args.only.split(","))
    sys.path.insert(0, str(EVAL_DIR.parent / "swarm"))
    style()
    data = load(args.run, exclude=set(filter(None, args.exclude.split(","))))
    out = EVAL_DIR / "results" / (args.out or args.run)
    out.mkdir(parents=True, exist_ok=True)
    cov = coverage(data, out) if {"coverage", "determinism"} & only else None
    det = determinism(data, out) if "determinism" in only else None
    if cov and det:
        det_vs_cov(cov, det, plotted(data["models"]), out / "determinism_vs_coverage.png")
    exp = expressivity(data, out) if "expressivity" in only else None
    fails = failures(data, out) if "failures" in only else None
    if not (cov and det and exp and fails):
        print(f"wrote {', '.join(sorted(p.name for p in out.iterdir()))} to {out}")
        return
    summary = {"run": args.run, "models": [{k: m[k] for k in ("name", "label", "company", "tier")} for m in
                                           data["models"]],
               "coverage": cov["rows"], "determinism_pairs": det["pairs"], "determinism_self": det["self"],
               "top_symbols": det["pooled_top_symbols"], "type_counts": det["pooled_types"],
               "expressivity": exp["rows"], "failures": fails["rows"]}
    (out / "summary.json").write_text(json.dumps(summary, indent=1, default=float), encoding="utf-8")
    print(f"wrote {', '.join(sorted(p.name for p in out.iterdir()))} to {out}")


if __name__ == "__main__":
    main()
