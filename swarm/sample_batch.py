#!/usr/bin/env python3
"""Draw a batch file for spawn_batch.py from normalized trajectory data.

Every run needs the same three things — a random sample, a few filters, and the
guarantee that nothing already processed comes round again — and each session
that rebuilt them by hand got the exclusion half subtly wrong. So this is the
one place that knows how to do it.

It assumes only what the pipeline itself assumes: JSONL, one object per line,
with a string `content` holding the trajectory. `id` is used when present but
not required. Nothing here knows where the data came from.

    python3 sample_batch.py -n 30 --max-chars 20000 --latin-only

Writes `batches/batch-NN.jsonl`, taking the next free number, and prints why
records were rejected — a run that samples 3 of a requested 30 has usually hit
a filter, not the end of the data.

Standard library only, deliberately: this runs before anything is installed.
"""
import argparse
import glob as globlib
import hashlib
import json
import random
import sys
import unicodedata
from collections import Counter
from pathlib import Path

SELF_DIR = Path(__file__).resolve().parent

# What a record must have to be worth spending a container on. Turn tags are
# the pipeline's own contract (see tasks/discovery.md), not a property of any
# one source, so they're checked by default.
TURN_TAGS = ("<|user|>", "<|assistant|>")


def content_hash(line: str) -> str:
    """Same identity spawn_batch.py uses: sha256 of the raw record line. Must
    stay in step with utils.content_hash, and is duplicated rather than
    imported so this script keeps working with no dependencies installed."""
    return hashlib.sha256(line.encode()).hexdigest()


def is_latin(text: str) -> bool:
    """True when the text is writable in the Latin script plus ordinary
    punctuation. A filter for keeping early corpora simple to read, not a
    judgment about the data: CJK and RTL trajectories translate fine, but a
    reviewer who can't read the source can't check the translation.
    """
    for ch in text:
        code = ord(ch)
        if code < 0x0250:                                    # Latin + Latin-1 + Ext-A/B
            continue
        if 0x2000 <= code <= 0x206F:                         # – — “ ” …
            continue
        if 0x20A0 <= code <= 0x20BF:                         # currency
            continue
        if code in (0x2122, 0x00B0):                         # ™ °
            continue
        if unicodedata.category(ch) in ("Zs", "Cf"):         # spacing, formatting
            continue
        return False
    return True


def resolve_sources(patterns) -> list:
    """Expand each argument as a file, a directory (recursively, *.jsonl), or a
    glob. Accepting all three means callers don't have to know how a source
    happens to be laid out on disk."""
    paths = []
    for pattern in patterns:
        path = Path(pattern)
        if path.is_dir():
            paths.extend(sorted(path.rglob("*.jsonl")))
        elif path.is_file():
            paths.append(path)
        else:
            matched = sorted(Path(p) for p in globlib.glob(pattern, recursive=True))
            paths.extend(p for p in matched if p.is_file())
    seen, unique = set(), []
    for path in paths:
        resolved = path.resolve()
        if resolved not in seen:
            seen.add(resolved)
            unique.append(path)
    return unique


def collect_seen(out_dir: Path, batches_dir: Path) -> tuple:
    """Every record already spoken for, by content hash and by `id`.

    Both keys matter and neither subsumes the other. A hash catches a record
    re-offered byte-identically; an `id` catches the same trajectory arriving
    with a re-serialized or re-annotated line, which a hash misses entirely.
    Three places are read, because a record can be spoken for in three ways:

    - `output/*/metadata.json` — succeeded (that file is written only on success).
    - `failures/*/` — attempted and failed. Excluded too: a batch file is the
      way to retry, so re-sampling a failed record would silently duplicate
      work that already has a home. Re-run its own batch file instead.
    - `batches/*.jsonl` — already drawn, whether or not it has been run. This is
      what stops two batches sampled in one session from overlapping.
    """
    hashes, ids = set(), set()

    def note_record_line(line: str):
        line = line.strip()
        if not line:
            return
        hashes.add(content_hash(line))
        try:
            record = json.loads(line)
        except ValueError:
            return
        if isinstance(record, dict) and record.get("id") is not None:
            ids.add(str(record["id"]))

    for path in sorted(batches_dir.glob("*.jsonl")) if batches_dir.is_dir() else []:
        with path.open(encoding="utf-8") as fh:
            for line in fh:
                note_record_line(line)

    failures = out_dir.parent / "failures"
    for base in (out_dir, failures):
        if not base.is_dir():
            continue
        for entry in sorted(base.iterdir()):
            if not entry.is_dir():
                continue
            source = entry / "source.json"
            if source.is_file():
                note_record_line(source.read_text(encoding="utf-8", errors="replace"))
            for name in ("metadata.json", "failure.json"):
                meta_path = entry / name
                if not meta_path.is_file():
                    continue
                try:
                    meta = json.loads(meta_path.read_text())
                except (ValueError, OSError):
                    continue
                if meta.get("hash"):
                    hashes.add(meta["hash"])

    return hashes, ids


def next_batch_path(batches_dir: Path) -> Path:
    """The first `batch-NN.jsonl` not taken, two-digit and then wider."""
    used = set()
    for path in batches_dir.glob("batch-*.jsonl"):
        stem = path.stem[len("batch-"):]
        if stem.isdigit():
            used.add(int(stem))
    n = 1
    while n in used:
        n += 1
    return batches_dir / f"batch-{n:02d}.jsonl"


def sample(args) -> int:
    sources = resolve_sources(args.data)
    if not sources:
        print(f"sample_batch: no .jsonl files found in {args.data}", file=sys.stderr)
        return 1

    out_dir = Path(args.output_dir)
    batches_dir = Path(args.batches_dir)
    batches_dir.mkdir(parents=True, exist_ok=True)
    out_path = Path(args.out) if args.out else next_batch_path(batches_dir)

    if args.no_exclude:
        seen_hashes, seen_ids = set(), set()
    else:
        seen_hashes, seen_ids = collect_seen(out_dir, batches_dir)

    # Seeded from the destination filename by default, so a batch is
    # reproducible and two batches never draw the same sample — the failure
    # mode of a fixed default seed.
    seed = args.seed if args.seed is not None else int(content_hash(out_path.name)[:12], 16)
    rnd = random.Random(seed)

    stats = Counter()
    reservoir, eligible = [], 0
    drawn_hashes = set()

    for path in sources:
        with path.open(encoding="utf-8", errors="replace") as fh:
            for line in fh:
                line = line.rstrip("\n")
                if not line.strip():
                    continue
                stats["read"] += 1
                try:
                    record = json.loads(line)
                except ValueError:
                    stats["unparseable"] += 1
                    continue
                if not isinstance(record, dict):
                    stats["unparseable"] += 1
                    continue
                content = record.get("content")
                if not isinstance(content, str) or not content.strip():
                    stats["no_content"] += 1
                    continue
                if len(content) < args.min_chars:
                    stats["too_short"] += 1
                    continue
                if args.max_chars and len(content) > args.max_chars:
                    stats["too_long"] += 1
                    continue
                if args.latin_only and not is_latin(content):
                    stats["non_latin"] += 1
                    continue
                if args.require_turns and not all(t in content for t in TURN_TAGS):
                    stats["no_turns"] += 1
                    continue
                if record.get("id") is not None and str(record["id"]) in seen_ids:
                    stats["already_done_id"] += 1
                    continue
                line_hash = content_hash(line)
                if line_hash in seen_hashes:
                    stats["already_done_hash"] += 1
                    continue
                if line_hash in drawn_hashes:
                    stats["duplicate_in_source"] += 1
                    continue
                drawn_hashes.add(line_hash)

                # Reservoir sample: one pass, memory bounded by -n, and every
                # eligible record equally likely regardless of how large the
                # source turns out to be. Shuffling the whole corpus first
                # would mean holding all of it.
                stats["eligible"] += 1
                eligible += 1
                if len(reservoir) < args.count:
                    reservoir.append(line)
                else:
                    j = rnd.randrange(eligible)
                    if j < args.count:
                        reservoir[j] = line

    rnd.shuffle(reservoir)
    with out_path.open("w", encoding="utf-8") as fh:
        for line in reservoir:
            fh.write(line + "\n")

    lengths = sorted(len(json.loads(l)["content"]) for l in reservoir) or [0]
    print(f"sample_batch: {len(sources)} source file(s), {stats['read']} records read")
    print(f"  excluded as already done: {len(seen_hashes)} hashes / {len(seen_ids)} ids known")
    for key in ("unparseable", "no_content", "too_short", "too_long", "non_latin",
                "no_turns", "already_done_id", "already_done_hash",
                "duplicate_in_source"):
        if stats[key]:
            print(f"  rejected {key}: {stats[key]}")
    print(f"  eligible: {stats['eligible']}")
    print(f"wrote {len(reservoir)} records (seed {seed}) -> {out_path}")
    print(f"  content chars: min={lengths[0]} median={lengths[len(lengths) // 2]} max={lengths[-1]}")
    if len(reservoir) < args.count:
        print(f"  NOTE: asked for {args.count}; the pool of eligible records was "
              f"{stats['eligible']}", file=sys.stderr)
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Sample a batch file for spawn_batch.py, excluding everything already processed.")
    parser.add_argument("-n", "--count", type=int, default=20,
                        help="records to draw (default 20)")
    parser.add_argument("-o", "--out", default=None,
                        help="output path (default: the next free batches/batch-NN.jsonl)")
    parser.add_argument("--data", nargs="+", default=[str(SELF_DIR / "data")],
                        help="source files, directories, or globs (default: data/)")
    parser.add_argument("--min-chars", type=int, default=0,
                        help="skip trajectories shorter than this")
    parser.add_argument("--max-chars", type=int, default=0,
                        help="skip trajectories longer than this (0 = no limit)")
    parser.add_argument("--latin-only", action="store_true",
                        help="skip trajectories using non-Latin scripts")
    parser.add_argument("--no-require-turns", dest="require_turns",
                        action="store_false",
                        help="keep records without <|user|>/<|assistant|> tags")
    parser.add_argument("--no-exclude", action="store_true",
                        help="don't exclude already-processed records (rarely what you want)")
    parser.add_argument("--seed", type=int, default=None,
                        help="RNG seed (default: derived from the output filename)")
    parser.add_argument("--output-dir", default=str(SELF_DIR / "output"),
                        help="the swarm output dir to read exclusions from (default: output/)")
    parser.add_argument("--batches-dir", default=str(SELF_DIR / "batches"),
                        help="where batch files live (default: batches/)")
    return sample(parser.parse_args(argv))


if __name__ == "__main__":
    sys.exit(main())
