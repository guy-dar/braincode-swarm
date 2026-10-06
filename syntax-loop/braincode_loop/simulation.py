"""Simulation inputs for the Critic: a random sample of prompt/trajectory/conversation items each
attempt, plus optional independent cross-provider translations of those items as Determinism
evidence.

Pool sources (config.yaml -> evaluation.simulation.closed_sources / open_sources — see
datasets/README.md for the closed/open split):
- `seed_tasks`  — braincode_loop/seed_tasks.json (both splits)
- everything else (`mind2web`, `alfred`, `swebench`, `prism`, `paths`, `thoughttrace`) —
  datasets/samples/<name>.jsonl if scripts/fetch_dataset_samples.py has been run, otherwise the
  committed illustrative datasets/samples/<name>.seed.jsonl.

Sampling draws a fixed number of items from *each* source in each class (not a flat total split
round-robin) — `items_per_dataset_closed` from every closed source, `items_per_dataset_open` from
every open source — so a config + seed reproduces the same items every attempt.
"""
from __future__ import annotations

import json
import logging
import os
import random
from dataclasses import dataclass, field

from .budget import BudgetTracker
from .llm import generate_resilient
from .llm.pricing import estimate_cost_usd
from .state import LanguageState
from .utils import parse_json_response

logger = logging.getLogger("braincode_loop")

# Measured 2026-09-30 with notes + vocabulary in the prompt: ~$0.11/call for claude-sonnet-5
# (which uses its whole output cap), ~$0.03 for gemini-3.1-pro-preview. Was 0.02 — ~5x too low,
# so the budget gate never skipped a cross-check it couldn't afford.
EST_TRANSLATOR_CALL_USD = 0.10

_TRANSLATOR_SYSTEM = (
    "You are an independent translator for the BrainCode syntax. Given the current language spec, "
    "any proposed changes available for this translation, and one natural-language task, produce "
    "the BrainCode expression for the task. Use only constructs and glossary symbols defined in the "
    "spec, the glossary, or the proposed changes. If something cannot be expressed with them, do "
    "not invent syntax and do not smuggle in natural-language text: write GAP(\"<what is missing>\") "
    "at that point, so the gap is explicit evidence. If fundamental notes are listed, they "
    "override these defaults. Do not explain your reasoning, verify the "
    "grammar step by step, or show your work — go straight to the answer. Respond with only a JSON "
    'object and nothing else: {"braincode": "<expression>"}'
)


@dataclass
class SimItem:
    id: str
    nl: str
    source: str
    domain: str = ""
    steps: list[str] = field(default_factory=list)

    def as_prompt_dict(self) -> dict:
        d = {"item_id": self.id, "source": self.source, "domain": self.domain, "nl": self.nl}
        if self.steps:
            d["trajectory_steps"] = self.steps[:12]
        return d


def _read_jsonl(path: str, source: str) -> list[SimItem]:
    items = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            if not row.get("nl"):
                continue
            steps = row.get("steps") or []
            items.append(
                SimItem(
                    id=str(row.get("id") or f"{source}-{len(items)+1}"),
                    nl=row["nl"],
                    source=row.get("source") or source,
                    domain=str(row.get("domain") or row.get("task_type") or ""),
                    steps=[str(s) for s in steps],
                )
            )
    return items


def resolve_dataset_path(base_dir: str, name: str) -> str | None:
    samples_dir = os.path.join(base_dir, "datasets", "samples")
    for candidate in (f"{name}.jsonl", f"{name}.seed.jsonl"):
        path = os.path.join(samples_dir, candidate)
        if os.path.exists(path):
            return path
    return None


def load_pool(base_dir: str, sources: list[str], state: LanguageState) -> dict[str, list[SimItem]]:
    pool: dict[str, list[SimItem]] = {}
    for src in sources:
        if src == "seed_tasks":
            items = [
                SimItem(id=t.id, nl=t.nl, source="seed_tasks", domain=f"{t.domain} ({t.split})")
                for split_items in state.tasks_by_split.values()
                for t in split_items
            ]
        else:
            path = resolve_dataset_path(base_dir, src)
            if not path:
                logger.warning("Simulation source %r has no datasets/samples/%s(.seed).jsonl — skipping.", src, src)
                continue
            items = _read_jsonl(path, src)
            logger.info("Simulation pool: %s -> %d items from %s", src, len(items), os.path.basename(path))
        if items:
            pool[src] = items
    return pool


def sample_items(
    pool: dict[str, list[SimItem]], *, closed_sources: list[str], open_sources: list[str],
    per_closed: int, per_open: int, rng: random.Random,
) -> list[SimItem]:
    """Exactly `per_closed` items from each closed source and `per_open` from each open source,
    capped at what's available per source (e.g. seed_tasks' small pool is fine at per_closed=2; a
    missing/unfetched source is silently skipped, same as today)."""
    picked: list[SimItem] = []
    for sources, per in ((closed_sources, per_closed), (open_sources, per_open)):
        for src in sources:
            items = pool.get(src)
            if items:
                picked.extend(rng.sample(items, min(per, len(items))))
    return picked


def changes_digest(proposal: dict) -> str:
    lines = []
    for c in proposal.get("changes") or []:
        op, name = c.get("op", "add"), c.get("construct_name")
        vocab = str(c.get("kind", "construct")).lower() == "vocabulary"
        if op == "remove":
            lines.append(f"- [remove{' vocabulary' if vocab else ''}] {name}: no longer part of the language — do not use it")
        elif vocab:
            members = ", ".join(str(m.get("symbol")) for m in c.get("members") or [] if isinstance(m, dict)) or "(see rule)"
            rule = f"; membership rule: {c['membership_rule']}" if c.get("membership_rule") else ""
            lines.append(
                f"- [{op} vocabulary] {name} ({'closed' if c.get('closed', True) else 'open'}): "
                f"{c.get('glossary_gloss')} Members: {members}{rule}"
            )
        else:
            lines.append(f"- [{op}] {name}: grammar `{c.get('grammar')}` — {c.get('semantics')}")
    return "\n".join(lines) or "(no changes)"


def pick_cross_check_items(items: list[SimItem], max_items: int | None) -> list[SimItem]:
    """The subset of this attempt's sampled items that also get independent translations
    (config.yaml -> evaluation.cross_check.max_items; None/0 = all). Taken round-robin across
    sources in sample order, so the subset spans closed and open items instead of the first few
    sources only. The Critic still simulates every sampled item."""
    if not max_items or max_items >= len(items):
        return list(items)
    by_source: dict[str, list[SimItem]] = {}
    for item in items:
        by_source.setdefault(item.source, []).append(item)
    queues = list(by_source.values())
    picked: list[SimItem] = []
    while len(picked) < max_items:
        for q in queues:
            if q and len(picked) < max_items:
                picked.append(q.pop(0))
    return picked


def should_cross_check(
    *, mode: str, changes: list[dict], spec_construct_count: int, budget: BudgetTracker,
    n_items: int, n_providers: int,
) -> tuple[bool, str]:
    """`auto` decides whether independent translations would mean anything this attempt."""
    mode = (mode or "auto").lower()
    if mode == "never":
        return False, "cross-check disabled (evaluation.cross_check.mode=never)"
    if n_providers < 2 or n_items == 0:
        return False, "cross-check needs at least 2 providers and 1 sampled item"
    if mode == "always":
        return True, "cross-check forced (mode=always)"
    adds = [c for c in changes if c.get("op", "add") == "add"]
    if spec_construct_count == 0 and len(adds) < 2:
        return False, "skipped: no constructs in the spec yet and fewer than 2 proposed — nothing to translate with"
    if changes and all(str(c.get("change_type", "")).upper() == "PATCH" for c in changes):
        return False, "skipped: every change is PATCH (documentation-only), translations would not differ"
    needed = n_items * n_providers * EST_TRANSLATOR_CALL_USD
    if budget.remaining_budget_usd() < 2 * needed:
        return False, f"skipped: remaining budget ${budget.remaining_budget_usd():.2f} too low for ~${needed:.2f} of translations"
    return True, "run: proposal is substantive and budget allows"


def cross_translate(
    *, items: list[SimItem], spec_text: str, proposal: dict, providers: list[str], models_map: dict,
    sprint: int, budget: BudgetTracker, pricing_table: dict, dry_run: bool, llm_cfg: dict | None = None,
    transcript=None, attempt: int = 1, glossary_text: str = "", notes_text: str = "",
    max_tokens: int = 3000, effort: str | None = None,
) -> dict[str, dict[str, str]]:
    """Independent translations of every sampled item by each provider. Any single failure is
    logged and skipped; items with fewer than two successful translations are dropped, and an
    empty dict means the Critic should simulate Determinism on its own."""
    digest = changes_digest(proposal)
    out: dict[str, dict[str, str]] = {}
    for item in items:
        per_provider: dict[str, str] = {}
        for provider in providers:
            model = models_map.get(provider)
            if not model:
                continue
            user = (
                f"# ROLE: translator\n\n"
                + (f"{notes_text}\n" if notes_text else "")
                + f"Language spec:\n{spec_text}\n\n"
                + (f"Glossary:\n{glossary_text}\n\n" if glossary_text else "")
                + f"Proposed changes available for this translation:\n{digest}\n\n"
                f"Task: \"{item.nl}\"\n\nReturn JSON: {{\"braincode\": \"...\"}}"
            )
            try:
                budget.ensure_available()
                response, model_used = generate_resilient(
                    provider=provider, model=model, system=_TRANSLATOR_SYSTEM, user=user,
                    # Generous headroom, not because the answer is long: "thinking"-capable models
                    # (e.g. gemini-3.1-pro-preview) spend part of max_output_tokens reasoning
                    # before the visible answer — worse on long, technical items (e.g. a full
                    # SWE-bench issue body) where step-by-step grammar verification can run long
                    # despite _TRANSLATOR_SYSTEM telling it not to. A tight budget here truncates
                    # the JSON mid-string, or in the worst case eats the whole budget before any
                    # JSON is emitted at all — seen in practice on exactly this kind of item.
                    max_tokens=max_tokens, effort=effort, temperature=0.2, dry_run=dry_run, llm_cfg=llm_cfg,
                    log_prefix="[cross_check_translator] ",
                )
                cost = estimate_cost_usd(pricing_table, model_used, response.input_tokens, response.output_tokens)
                budget.record_call(
                    sprint=sprint, role="cross_check_translator", provider=provider, model=model_used,
                    input_tokens=response.input_tokens, output_tokens=response.output_tokens, cost_usd=cost,
                )
                if transcript:
                    transcript.log_call(
                        sprint=sprint, attempt=attempt, bootstrap=False, role="cross_check_translator",
                        provider=provider, model=model_used, system_prompt=_TRANSLATOR_SYSTEM,
                        user_prompt=user, response_text=response.text, cost_usd=cost,
                    )
                text = parse_json_response(response.text).get("braincode", "")
                if text:
                    per_provider[provider] = str(text).strip()
            except Exception as exc:  # noqa: BLE001 - evidence only; never fail the sprint over it
                logger.warning("cross-check translation failed (%s, item %s): %s", provider, item.id, exc)
        if len(per_provider) >= 2:
            out[item.id] = per_provider
    return out
