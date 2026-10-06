"""Critic: the merged Reviewer + Examiner. One adversarial, KPI-aware judgment per attempt —
does this set of changes benefit or harm each pre-KPI, what must change to maximize benefit, and
what do the sampled dataset items look like when actually expressed with the proposal.
"""
from __future__ import annotations

import json

from ..doc_hygiene import HygieneResult
from ..simulation import SimItem
from .base_role import BaseRole


class Critic(BaseRole):
    role_name = "critic"
    prompt_file = "critic_system.md"

    def assess(
        self,
        *,
        sprint: int,
        attempt: int,
        proposal: dict,
        spec_text: str,
        glossary_text: str,
        simulation_items: list[SimItem],
        cross_translations: dict[str, dict[str, str]],
        cross_check_note: str,
        hygiene: HygieneResult,
        bootstrap: bool = False,
        notes_text: str = "",
        focus_note=None,
        previous_attempt: dict | None = None,
        positions: list[dict] | None = None,
        position_hygiene: list[HygieneResult] | None = None,
    ) -> dict:
        """`positions` (multi-position steering attempt): several Shapers' competing proposals —
        the Critic picks one (`chosen_position`) and assesses it; `proposal` is then ignored.
        `previous_attempt` carries the last attempt's critique so the Critic can rule on the
        Shaper's `rebuttals` against its own earlier required changes."""
        items_block = json.dumps([i.as_prompt_dict() for i in simulation_items], indent=1, ensure_ascii=False)
        if cross_translations:
            xlat_block = (
                "Independent translations of the sampled items by other providers (evidence for the "
                "Determinism pre-KPI — compare them to each other and to your own simulation):\n"
                + json.dumps(cross_translations, indent=1, ensure_ascii=False)
            )
        else:
            xlat_block = (
                f"No independent cross-provider translations are available this attempt "
                f"({cross_check_note}). Simulate Determinism yourself: for each sampled item, judge how "
                f"likely two different capable models would produce equivalent BrainCode."
            )
        if bootstrap:
            header = (
                "This is Sprint 0 (bootstrap): the proposal is the entire initial syntax basis, so judge it "
                "holistically — cross-construct consistency, redundancy, and the foundational-gap checklist.\n\n"
            )
        elif focus_note is not None:
            header = (
                f"Sprint {sprint}, attempt {attempt} — STEERING SPRINT focused on note {focus_note.id} "
                f"[{focus_note.kind}]: {focus_note.title}. Judge whether the changes realize that note "
                f"(or, for a direction note the Shaper contests, whether its evidence holds), without "
                f"regressing the pre-KPIs or making any note worse than the current spec. Gating is "
                f"no-regression: progress on the focus note is acceptable even if it isn't fully "
                f"realized yet, and pre-existing violations of other notes don't block.\n\n"
            )
        else:
            header = f"Sprint {sprint}, attempt {attempt}: the proposal is a set of changes against the current spec.\n\n"
        if positions:
            hyg = position_hygiene or [None] * len(positions)
            proposal_block = (
                f"COMPETING POSITIONS ({len(positions)} Shapers proposed independently). Compare them, "
                f"pick the one that best serves the note and the pre-KPIs as `chosen_position` "
                f"(0-based index), explain the comparison in `position_comparison`, and give the rest "
                f"of your assessment (simulations, required_changes, decision) for the chosen one. "
                f"Your required_changes may borrow good ideas from the others.\n\n"
                + "\n\n".join(
                    f"Position {i} ({p.get('_provider_used', '?')}) — doc hygiene: "
                    f"{h.describe() if h else 'n/a'}\n{json.dumps(_public(p), indent=1, ensure_ascii=False)}"
                    for i, (p, h) in enumerate(zip(positions, hyg))
                )
                + "\n\n"
            )
            hygiene_line = ""
        else:
            proposal_block = f"Proposal (summary + all changes):\n{json.dumps(proposal, indent=1, ensure_ascii=False)}\n\n"
            hygiene_line = f"Doc-hygiene check (scripted, structural): {hygiene.describe()}\n\n"
        debate_block = ""
        rebuttals = (proposal or {}).get("rebuttals") if not positions else None
        if previous_attempt and previous_attempt.get("critique"):
            prev = previous_attempt["critique"]
            debate_block = (
                f"Your previous critique's required changes: {json.dumps(prev.get('required_changes', []), ensure_ascii=False)}\n"
                + (
                    f"The Shaper REBUTS some of them instead of complying — rule on each in "
                    f"`rebuttal_rulings` (upheld = the change is dropped; overruled = still required):\n"
                    f"{json.dumps(rebuttals, indent=1, ensure_ascii=False)}\n\n"
                    if rebuttals
                    else "The Shaper did not rebut any of them — check each was actually made.\n\n"
                )
            )
        prompt = (
            header
            + (f"{notes_text}\n" if notes_text else "")
            + proposal_block
            + debate_block
            + f"Current language-spec.md:\n{spec_text or '(empty — no constructs yet)'}\n\n"
            + f"Current glossary.md:\n{glossary_text or '(empty)'}\n\n"
            + hygiene_line
            + f"Sampled dataset items to simulate ({len(simulation_items)}):\n{items_block}\n\n"
            + xlat_block
            + "\n\nReturn only the JSON object specified in your instructions; include one `simulations` "
            "entry per sampled item."
        )
        if bootstrap:
            marker = "critic_bootstrap"
        elif focus_note is not None:
            marker = "critic_steering"
        else:
            marker = "critic"
        return self.call(sprint=sprint, user_prompt=prompt, role_marker=marker, bootstrap=bootstrap, attempt=attempt)


def _public(proposal: dict) -> dict:
    """A proposal without the loop's internal `_provider_used`/`_model_used` bookkeeping keys."""
    return {k: v for k, v in proposal.items() if not k.startswith("_")}
