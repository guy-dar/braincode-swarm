#!/usr/bin/env python3
"""Charts of the loop's progress, saved to graphs/:

  suggestions_<type>_by_class.png    suggestions of one type (add / refine) written per batch,
                                     closed-class vs open-class datasets (color)
  suggestions_<type>_by_dataset.png  the same, one line per dataset (color = class, marker = dataset)
  accepted_<type>_by_class.png       the same two charts for the suggestions the migrator accepted
  accepted_<type>_by_dataset.png     (carried into an applied glossary op)
  success_rate.png            % of the batch's translators that produced a successful translation
  glossary_size.png           live glossary records after each batch's migration, from the
                              initial import (reconstructed from glossary-provenance.jsonl)
  glossary_size_by_kind.png   the same per record kind (value, operation, composite, ...),
                              one small panel per kind with its own scale
  glossary_size_by_kind.csv   the numbers behind it
  summary.csv                 the numbers behind the other charts (table view)

Data: translator_suggestions/suggestion_counts.csv (the inspector's CSV) and
reference/glossary-provenance.jsonl (via inspector.py).

    python plot_inspector.py
"""
import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.ticker import MaxNLocator, PercentFormatter  # noqa: E402

import inspector  # noqa: E402
import loop_files as lf  # noqa: E402

GRAPHS_DIR = lf.SELF_DIR / "graphs"

CLOSED = ("mind2web", "alfred", "swebench")
OPEN = ("prism", "paths", "thoughttrace")
LABELS = {"mind2web": "Mind2Web", "alfred": "ALFRED", "swebench": "SWE-bench",
          "prism": "PRISM", "paths": "PATHs", "thoughttrace": "ThoughtTrace"}
MARKERS = {"mind2web": "o", "alfred": "s", "swebench": "^", "prism": "D", "paths": "v", "thoughttrace": "P"}

# Validated categorical slots 1-2 (blue / orange) of the reference palette; text in ink tokens.
COLORS = {"closed": "#2a78d6", "open": "#eb6834"}
SURFACE = "#fcfcfb"
INK = "#0b0b0b"
INK_2 = "#52514e"
GRID = "#e4e2dc"


def style():
    plt.rcParams.update({
        "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE,
        "axes.edgecolor": GRID, "axes.labelcolor": INK_2, "axes.titlecolor": INK,
        "axes.titlesize": 12, "axes.titleweight": "bold", "axes.labelsize": 10,
        "xtick.color": INK_2, "ytick.color": INK_2, "xtick.labelsize": 9, "ytick.labelsize": 9,
        "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.8, "axes.axisbelow": True,
        "axes.spines.top": False, "axes.spines.right": False,
        "legend.frameon": False, "legend.fontsize": 9, "legend.labelcolor": INK_2,
        "lines.linewidth": 2, "lines.markersize": 6.5, "font.size": 10,
    })


def load_counts() -> list:
    if not lf.COUNTS_CSV.exists():
        raise SystemExit(f"no inspector CSV at {lf.COUNTS_CSV}")
    with lf.COUNTS_CSV.open(newline="", encoding="utf-8") as fh:
        rows = sorted(csv.DictReader(fh), key=lambda r: int(r["batch"]))
    missing = [r["batch"] for r in rows if not r.get("accepted_add_total")]
    if missing:
        raise SystemExit(f"batches {missing} have no accepted counts; run: python inspector.py --batches "
                         f"{rows[0]['batch']}-{rows[-1]['batch']}")
    for r in rows:
        for k, v in list(r.items()):
            if k == "batch" or k.startswith(("add_", "refine_", "accepted_add_", "accepted_refine_",
                                             "translators_", "successful_", "failed_")):
                r[k] = int(float(v)) if v not in (None, "") else 0
    return rows


def glossary_sizes(batches: list) -> list:
    """[(label, x, live_records)]: the initial import (x=0), then the size after
    each batch's migration (inspector.glossary_sizes, from the provenance log)."""
    initial, after = inspector.glossary_sizes(inspector.load_provenance())
    return [("initial", 0, initial)] + [(f"batch {b}", b, after[b]) for b in batches if b in after]


def _label_end(ax, x, y, text, color):
    ax.annotate(text, (x, y), xytext=(6, 0), textcoords="offset points", va="center",
                fontsize=9, color=INK_2)


def _axes(ax, ylabel):
    ax.set_xlabel("Batch")
    ax.set_ylabel(ylabel)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_ylim(bottom=0)


def _what(accepted: bool) -> str:
    return "accepted by the migrator" if accepted else "written by translators"


def chart_by_class(rows: list, kind: str, accepted: bool, path: Path):
    """One suggestion type (add or refine), closed-class vs open-class datasets."""
    prefix = f"accepted_{kind}" if accepted else kind
    xs = [r["batch"] for r in rows]
    fig, ax = plt.subplots(figsize=(8, 4.4))
    ax.set_title(f"{kind.capitalize()} suggestions {_what(accepted)}, by dataset class", loc="left")
    for cls, sets in (("closed", CLOSED), ("open", OPEN)):
        ys = [sum(r[f"{prefix}_{ds}"] for ds in sets) for r in rows]
        name = ("Closed-class (Mind2Web, ALFRED, SWE-bench)" if cls == "closed"
                else "Open-class (PRISM, PATHs, ThoughtTrace)")
        ax.plot(xs, ys, color=COLORS[cls], marker="o", label=name, markeredgecolor=SURFACE, markeredgewidth=1.5)
        _label_end(ax, xs[-1], ys[-1], f"{ys[-1]}", COLORS[cls])
    _axes(ax, "Accepted suggestions" if accepted else "Suggestions")
    ax.legend(loc="upper right")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def chart_by_dataset(rows: list, kind: str, accepted: bool, path: Path):
    """One suggestion type, one line per dataset (color = class, marker = dataset)."""
    prefix = f"accepted_{kind}" if accepted else kind
    xs = [r["batch"] for r in rows]
    fig, ax = plt.subplots(figsize=(8, 4.8))
    fig.suptitle(f"{kind.capitalize()} suggestions {_what(accepted)}, by dataset", x=0.01, ha="left",
                 fontsize=12, fontweight="bold", color=INK)
    fig.text(0.01, 0.905, "blue solid = closed-class, orange dashed = open-class", ha="left", fontsize=9,
             color=INK_2)
    for ds in CLOSED + OPEN:
        cls = "closed" if ds in CLOSED else "open"
        ys = [r[f"{prefix}_{ds}"] for r in rows]
        ax.plot(xs, ys, color=COLORS[cls], marker=MARKERS[ds], label=LABELS[ds],
                linestyle="-" if cls == "closed" else (0, (4, 2)),
                markeredgecolor=SURFACE, markeredgewidth=1.2, alpha=0.95)
    _axes(ax, "Accepted suggestions" if accepted else "Suggestions")
    handles, labels = ax.get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper left", ncol=6, bbox_to_anchor=(0.005, 0.89))
    fig.tight_layout(rect=(0, 0, 1, 0.83))
    fig.savefig(path, dpi=150)
    plt.close(fig)


def chart_success(rows: list, path: Path):
    xs = [r["batch"] for r in rows]
    ys = [100 * r["successful_translations"] / r["translators_planned"] if r["translators_planned"] else 0
          for r in rows]
    fig, ax = plt.subplots(figsize=(8, 4.2))
    ax.plot(xs, ys, color=COLORS["closed"], marker="o", markeredgecolor=SURFACE, markeredgewidth=1.5)
    for i, (dx, dy, ha) in ((0, (8, -14, "left")), (len(xs) - 1, (0, 10, "right"))):
        r = rows[i]
        ax.annotate(f"{ys[i]:.0f}% ({r['successful_translations']}/{r['translators_planned']})", (xs[i], ys[i]),
                    xytext=(dx, dy), textcoords="offset points", ha=ha, fontsize=9, color=INK_2)
    ax.set_title("Successful translations per batch", loc="left")
    ax.set_xlabel("Batch")
    ax.set_ylabel("Share of the batch's translators")
    ax.set_ylim(0, 105)
    ax.yaxis.set_major_formatter(PercentFormatter())
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def chart_glossary(sizes: list, path: Path):
    xs = [x for _, x, _ in sizes]
    ys = [y for _, _, y in sizes]
    fig, ax = plt.subplots(figsize=(8, 4.2))
    ax.plot(xs, ys, color=COLORS["closed"], marker="o", markeredgecolor=SURFACE, markeredgewidth=1.5)
    for i in {0, len(xs) - 1}:
        ax.annotate(f"{ys[i]}", (xs[i], ys[i]), xytext=(0, 9), textcoords="offset points", ha="center",
                    fontsize=9, color=INK_2)
    ax.set_title("Glossary size after each batch's migration (live records)", loc="left")
    ax.set_xlabel("Batch (0 = initial import)")
    ax.set_ylabel("Live glossary records")
    ax.set_ylim(bottom=0)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def glossary_sizes_by_kind(batches: list) -> tuple:
    """(xs, {kind: [live records of that kind at each x]}): x=0 is the initial
    import, then each batch's post-migration glossary. Kinds come from the
    current glossary.jsonl, which keeps every record ever created (records are
    deprecated, never removed)."""
    import json
    kind_of = {}
    for line in (lf.REFERENCE_DIR / "glossary.jsonl").read_text(encoding="utf-8").splitlines():
        if line.strip():
            r = json.loads(line)
            kind_of[r.get("id")] = r.get("kind") or "unknown"
    initial, after = inspector.glossary_live_sets(inspector.load_provenance())
    points = [(0, initial)] + [(b, after[b]) for b in batches if b in after]
    kinds = sorted({kind_of.get(i, "unknown") for _, ids in points for i in ids})
    series = {k: [sum(kind_of.get(i, "unknown") == k for i in ids) for _, ids in points] for k in kinds}
    # largest kinds first (by current size)
    series = dict(sorted(series.items(), key=lambda kv: -kv[1][-1]))
    return [x for x, _ in points], series


def chart_glossary_by_kind(xs: list, series: dict, path: Path):
    """Small multiples, one panel per record kind with its own y-scale: kinds
    range from a handful of records to hundreds, so one shared axis would
    flatten the small ones. One hue: the panel title names the kind."""
    n = len(series)
    cols = 4
    rows_n = -(-n // cols)
    fig, axes = plt.subplots(rows_n, cols, figsize=(13, 2.6 * rows_n + 0.8), sharex=True, squeeze=False)
    fig.suptitle("Glossary size by record kind after each batch's migration (live records)", x=0.01, ha="left",
                 fontsize=13, fontweight="bold", color=INK)
    fig.text(0.01, 1 - 0.55 / (2.6 * rows_n + 0.8), "batch 0 = initial import; each panel has its own scale",
             ha="left", fontsize=9, color=INK_2)
    for ax, (kind, ys) in zip(axes.flat, series.items()):
        ax.plot(xs, ys, color=COLORS["closed"], marker="o", markersize=4, markeredgecolor=SURFACE,
                markeredgewidth=1)
        grew = ys[-1] - ys[0]
        ax.set_title(f"{kind}  {ys[0]} → {ys[-1]}" + (f" (+{grew})" if grew > 0 else ""), loc="left", fontsize=10)
        lo, hi = min(ys), max(ys)
        pad = max(1, (hi - lo) * 0.15)
        ax.set_ylim(max(0, lo - pad), hi + pad)
        ax.yaxis.set_major_locator(MaxNLocator(integer=True, nbins=4))
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    for ax in list(axes.flat)[n:]:
        ax.set_visible(False)
    for ax in axes[-1]:
        ax.set_xlabel("Batch")
    fig.tight_layout(rect=(0, 0, 1, 1 - 0.75 / (2.6 * rows_n + 0.8)))
    fig.savefig(path, dpi=150)
    plt.close(fig)


def write_glossary_by_kind(xs: list, series: dict, path: Path):
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["batch", *series, "total"])
        for i, x in enumerate(xs):
            vals = [ys[i] for ys in series.values()]
            w.writerow([x, *vals, sum(vals)])


def write_summary(rows: list, sizes: list, path: Path):
    size_by_batch = {x: y for _, x, y in sizes}
    prefixes = ("add", "refine", "accepted_add", "accepted_refine")
    per_ds = [f"{p}_{d}" for p in prefixes for d in CLOSED + OPEN]
    by_class = [f"{p}_{c}" for p in prefixes for c in ("closed", "open")]
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["batch", "translators", "successful", "success_pct", *by_class, *per_ds,
                    "glossary_live_records_after"])
        w.writerow([0, "", "", "", *[""] * (len(by_class) + len(per_ds)), size_by_batch.get(0, "")])
        for r in rows:
            t = r["translators_planned"]
            classes = [sum(r[f"{p}_{d}"] for d in sets) for p in prefixes for sets in (CLOSED, OPEN)]
            w.writerow([r["batch"], t, r["successful_translations"],
                        round(100 * r["successful_translations"] / t, 1) if t else "",
                        *classes, *[r[k] for k in per_ds], size_by_batch.get(r["batch"], "")])


# replaced by the per-type charts
OBSOLETE = ("suggestions_by_class.png", "suggestions_by_dataset.png")


def main():
    style()
    GRAPHS_DIR.mkdir(exist_ok=True)
    for name in OBSOLETE:
        (GRAPHS_DIR / name).unlink(missing_ok=True)
    rows = load_counts()
    sizes = glossary_sizes([r["batch"] for r in rows])
    for accepted in (False, True):
        for kind in ("add", "refine"):
            stem = f"{'accepted' if accepted else 'suggestions'}_{kind}"
            chart_by_class(rows, kind, accepted, GRAPHS_DIR / f"{stem}_by_class.png")
            chart_by_dataset(rows, kind, accepted, GRAPHS_DIR / f"{stem}_by_dataset.png")
    chart_success(rows, GRAPHS_DIR / "success_rate.png")
    chart_glossary(sizes, GRAPHS_DIR / "glossary_size.png")
    xs, by_kind = glossary_sizes_by_kind([r["batch"] for r in rows])
    chart_glossary_by_kind(xs, by_kind, GRAPHS_DIR / "glossary_size_by_kind.png")
    write_glossary_by_kind(xs, by_kind, GRAPHS_DIR / "glossary_size_by_kind.csv")
    write_summary(rows, sizes, GRAPHS_DIR / "summary.csv")
    print(f"{len(rows)} batches; glossary sizes {[(lbl, n) for lbl, _, n in sizes]}")
    print(f"wrote {', '.join(p.name for p in sorted(GRAPHS_DIR.iterdir()))} to {GRAPHS_DIR}")


if __name__ == "__main__":
    main()
