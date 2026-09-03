---
name: miner
description: Context for finding, mining, or sourcing trajectory data for the discovery swarm in this repo. Use when asked to find data sources, gather conversation logs, or source trajectories to translate — background for the judgment calls involved, not a procedure.
---

# Miner

Background for finding *datasets* of trajectory data — collections of many real
trajectories, sourced from the web (public research/benchmark releases, dataset
hubs, anywhere agent traces get published) and other sources (session logs,
internal exports, other agent tools' history, wherever real usage already
happened) — to feed this repo's swarm pipeline (see `.claude/skills/orchestrator`
for how sourced data actually gets run through it). This is about sourcing at the
scale of a dataset, not hand-picking a few examples: the goal is volume of *real*
trajectories, filtered by the judgment calls below, not a curated handful.

This is context, not a checklist — the judgment calls matter more than any fixed
procedure, and there's no single right way to go find data.

## What we're actually trying to do

The swarm's discovery task translates real trajectories into BrainCode (see
`swarm/reference/DESIGN_DOC.md`) — a language for encoding human/AI trajectories, built as a
research artifact for interpretability, cross-model comparison, and related uses.
Its value depends entirely on the trajectories being real: the language's fidelity
contract (`swarm/reference/DESIGN_DOC.md`'s "Fidelity")
explicitly forbids inventing reasoning that wasn't evidenced — feeding the pipeline
synthetic or fabricated "trajectories" written to look plausible defeats the whole
purpose, even if they're structurally valid JSONL. A trajectory manufactured to be
easy to translate is worse than no trajectory at all.

## What counts as a good trajectory

Per `swarm/reference/DESIGN_DOC.md`'s opening: "the arc of one task, from the
human's intent through the agent's reasoning and action to completion." In
practice that favors:

- Visible reasoning and action, not just a final answer — a bare Q&A pair with no
  trace of what the agent did to get there gives discovery nothing to translate.
- One complete arc — a fragment cut off mid-task is worth less than a short but
  complete one.
- Genuine variety *within* the volume — the swarm is also trying to grow
  BrainCode's vocabulary through what recurs across many different trajectories
  (canonization — see `swarm/reference/DESIGN_DOC.md`), which needs real
  scale to work at all. The failure mode to watch for isn't a dataset being
  large — a large dataset is the point — it's a large dataset that's actually
  the same handful of tasks repeated thousands of times, which teaches the
  swarm less than a smaller dataset spanning genuinely different tasks and
  domains would. When choosing between candidate sources, prefer the one with
  more genuine variety, not the one with the highest raw count.

## Where this kind of data actually lives

No fixed list — the search itself is judgment, not lookup — but the shape of what
to look for: agent/coding-assistant session transcripts and released trajectory
corpora, wherever they exist. That includes public web sources (dataset hubs,
benchmark suites for coding/tool-use agents, research papers that release the
traces their evaluation ran on, anywhere a project has published real session
logs) and non-web sources already reachable from here (other agent tools' own
session/history storage, internal logs or exports, anywhere real usage already
happened and left a record). A dataset explicitly built for something else
(a benchmark's held-out test set, a QA dataset with no agent in the loop at all)
is worth a second look before assuming it fits — see "what counts as a good
trajectory" above for the actual bar.

## Where to put what you find

The batching format itself belongs to `.claude/skills/orchestrator` — the short
version: one JSON object per line, `content` (`<|user|>`/`<|assistant|>` turns);
an `id` field is optional and not required for uniqueness — the pipeline names
each record's output folder from its content, not from `id`, so records from
different sources never collide there regardless of what ids they do or don't
carry. If you're staging raw material before it's normalized into that shape,
keep it under `swarm/data/<source-name>/` (one folder per source, created only
once there's something to put in it) rather than dropping it loose in `swarm/`.
This repo doesn't assume one static dataset — sourced material accumulating from
several places over time is the expected shape, not an edge case.

## Where this job ends

Mining ends at producing staged, normalized data under `swarm/data/<source-name>/`
— content-only JSONL records, ready for batching. Splitting that into
`swarm/batches/batch-NN.jsonl` files and actually calling `spawn_batch.py`
(which spins up Docker containers against the model API — a real, costed
action) is `.claude/skills/orchestrator`'s job, not this one. After staging
data, propose running it through the orchestrator rather than doing it
yourself.

## Preserve evidenced reasoning, don't discard it

When a source carries a field that's genuine evidenced reasoning distinct from
the final response (e.g. a `thinking`/`reasoning` column separate from the
reply text), fold it into the trajectory rather than dropping it — per
`swarm/reference/DESIGN_DOC.md`'s fidelity contract, reasoning is never invented, but
reasoning that *was* recorded by the source is exactly what discovery needs and
should be kept, not thrown away for being inconvenient to format.

## Flag size before pulling

Before downloading a candidate source, check its size (dataset card, API
metadata, a HEAD request — whatever's available before committing to the
pull). Flag it to the user before proceeding if the total is more than a few
gigabytes (as a rule of thumb, >4GB) or if it looks large relative to
available disk space — sourcing at dataset scale can mean multi-gigabyte pulls
without warning, and that's a cost worth surfacing rather than a surprise.
