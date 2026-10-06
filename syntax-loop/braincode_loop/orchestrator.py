"""The small-group syntax-creation loop, run as a sequence of Agile sprints.

**Sprint 0 (bootstrap)** runs once, automatically, the first time the loop is pointed at an
empty docs/language-spec.md: Searcher gathers reference material on the inspiration languages
(config.yaml -> run.bootstrap.inspiration_languages), Shaper proposes an entire initial syntax
basis, the Critic simulates it on sampled dataset items and judges every pre-KPI, and the
Documenter initializes docs/language-spec.md. It does not count against budget.max_iterations
but its LLM calls do count against the $ budget like any other sprint.

**Steady state (sprints 1..N)**: Searcher grounds a candidate task -> Shaper proposes a *set* of
changes -> doc-hygiene script -> sampled simulation items (+ optional cross-provider translations)
-> Critic assesses -> decision -> Documenter records. A sent-back attempt is retried within the
same sprint (run.sprint.max_attempts) with the Critic's required changes fed to the Shaper.

**Steering sprints**: while steering/notes.md (config.yaml -> run.steering) has an open
fundamental note, a sprint is focused on that note instead of a sampled seed task — the Shaper
revises the existing language to realize it (optionally several Shapers propose competing
positions and the Critic picks one), may rebut the Critic's required changes on rework, and the
Critic judges every note each attempt. Notes are passed to every role in every sprint. Start from
an existing product instead of Sprint 0 with `run.py --from [dir]` (reset.py::import_baseline);
sprint numbering continues from the baseline (LanguageState.last_sprint_number).

The loop stops the moment either the budget or the iteration cap is hit (config.yaml -> budget).
"""
from __future__ import annotations

import logging
import os
import random

from . import doc_hygiene, run_lock, simulation, steering
from .budget import BudgetExceeded, BudgetTracker, add_to_total_spent, format_burndown, read_total_spend_data
from .decision import append_history, build_history_record, decide, regressed_hard_notes, violated_hard_notes
from .reset import snapshot_docs
from .roles import Critic, Documenter, Searcher, Shaper
from .roles.base_role import LLMCallFailed
from .state import LanguageState
from .transcript import TranscriptLogger
from .utils import format_attempt_label

logger = logging.getLogger("braincode_loop")


class Orchestrator:
    def __init__(self, config: dict, base_dir: str, log_dir: str | None = None):
        self.config = config
        self.base_dir = base_dir
        self.log_dir = log_dir  # runs/logs/run_<timestamp>/ — holds transcript.log; see run.py
        run_cfg = config["run"]
        self.dry_run = run_cfg.get("dry_run", False)
        random_seed = run_cfg.get("random_seed", 42)

        self.docs_dir = os.path.join(base_dir, run_cfg["docs_dir"])
        self.runs_dir = os.path.join(base_dir, run_cfg["runs_dir"])
        self.total_spend_path = os.path.join(self.runs_dir, "total_spend.json")
        seed_tasks_path = os.path.join(base_dir, run_cfg["seed_tasks_path"])
        sources_path = os.path.join(base_dir, run_cfg.get("sources_path", "sources/previous_work.md"))
        self.sources_path = sources_path
        self.inspiration_languages = run_cfg.get("bootstrap", {}).get(
            "inspiration_languages", ["python", "html", "english"]
        )
        self.bootstrap_max_attempts = run_cfg.get("bootstrap", {}).get("max_attempts", 3)
        self.sprint_max_attempts = run_cfg.get("sprint", {}).get("max_attempts", 2)
        steering_cfg = run_cfg.get("steering", {})
        notes_path = steering_cfg.get("notes_path")
        self.notes = steering.load_notes(os.path.join(base_dir, notes_path) if notes_path else None)
        self.note_status = steering.NoteStatus(self.docs_dir)
        self.hard_note_ids = {n.id for n in self.notes if n.kind == "hard"}
        self.max_sprints_per_note = int(steering_cfg.get("max_sprints_per_note", 2))
        self.positions = max(1, int(steering_cfg.get("positions", 1)))
        self.max_changes = int(steering_cfg.get("max_changes", 12))
        self.fallback_to_tasks = steering_cfg.get("fallback_to_tasks", True)
        self.sprint_offset = 0  # set in _run_inner once the starting point (seed/bootstrap/baseline) is known

        self.budget = BudgetTracker(
            max_budget_usd=config["budget"]["max_budget_usd"],
            max_iterations=config["budget"]["max_iterations"],
        )
        self.state = LanguageState(self.docs_dir, seed_tasks_path, sources_path=sources_path, random_seed=random_seed)

        transcript_path = os.path.join(log_dir, "transcript.log") if log_dir else None
        self.transcript = TranscriptLogger(transcript_path)

        pricing = config["pricing_usd_per_1m_tokens"]
        self.pricing = pricing
        roles_cfg = config["roles"]
        llm_cfg = config.get("llm", {})
        self.llm_cfg = llm_cfg
        self.searcher = Searcher(roles_cfg["searcher"], pricing, self.budget, self.dry_run, random_seed=random_seed, llm_cfg=llm_cfg, transcript=self.transcript)
        self.shaper = Shaper(roles_cfg["shaper"], pricing, self.budget, self.dry_run, llm_cfg=llm_cfg, transcript=self.transcript)
        self.critic = Critic(roles_cfg["critic"], pricing, self.budget, self.dry_run, llm_cfg=llm_cfg, transcript=self.transcript)
        self.documenter = Documenter(roles_cfg["documenter"], pricing, self.budget, self.dry_run, llm_cfg=llm_cfg, transcript=self.transcript)

        eval_cfg = config.get("evaluation", {})
        sim_cfg = eval_cfg.get("simulation", {})
        self.closed_sources = sim_cfg.get("closed_sources", ["seed_tasks", "mind2web", "alfred", "swebench"])
        self.open_sources = sim_cfg.get("open_sources", ["prism", "paths", "thoughttrace"])
        self.items_per_dataset_closed = int(sim_cfg.get("items_per_dataset_closed", 2))
        self.items_per_dataset_open = int(sim_cfg.get("items_per_dataset_open", 4))
        self.cross_check_cfg = eval_cfg.get("cross_check", {})
        # Separate RNG stream from task sampling / searcher mode so simulation picks don't perturb them.
        self.sim_rng = random.Random(random_seed + 2)
        self.sim_pool = simulation.load_pool(base_dir, self.closed_sources + self.open_sources, self.state)
        logger.info("Simulation pool: %s", {k: len(v) for k, v in self.sim_pool.items()})

    def run(self) -> None:
        # Raises run_lock.RunAlreadyActive (uncaught here, on purpose) if another run.py
        # invocation already holds this runs_dir — see run_lock.py for why this exists.
        run_lock.acquire(self.runs_dir)
        try:
            if not self.dry_run:
                prior = read_total_spend_data(self.total_spend_path)
                logger.info(
                    "Budget burndown (before this run):\n%s",
                    format_burndown(prior, max_budget_usd=self.budget.max_budget_usd),
                )
            logger.info("Starting BrainCode syntax loop: max_budget=$%.2f max_iterations=%d dry_run=%s",
                         self.budget.max_budget_usd, self.budget.max_iterations, self.dry_run)
            try:
                self._run_inner()
            finally:
                # Always write the cost log — real money may have been spent before any crash.
                os.makedirs(self.runs_dir, exist_ok=True)
                # runs/budget_log.json is "the latest run" and gets replaced each run, so every
                # run's own copy is also kept next to its logs (runs/logs/<run_id>/), never overwritten.
                self.budget.write_log(os.path.join(self.runs_dir, "budget_log.json"))
                if self.log_dir:
                    self.budget.write_log(os.path.join(self.log_dir, "budget_log.json"))
                if self.log_dir:
                    # Same run_id as runs/logs/run_<run_id>/, so a run's logs and its produced
                    # docs/ snapshot are correlated by name — see reset.py::snapshot_docs.
                    run_id = os.path.basename(self.log_dir)
                    snapshot_dest = snapshot_docs(self.base_dir, self.config["run"]["docs_dir"], run_id)
                    if snapshot_dest:
                        logger.info("Snapshotted this run's docs/ to %s", snapshot_dest)
                if not self.dry_run:
                    by_provider = self.budget.spent_by_provider()
                    updated = add_to_total_spent(self.total_spend_path, self.budget.spent_usd, by_provider)
                    logger.info(
                        "Budget burndown (after this run, +$%.4f):\n%s",
                        self.budget.spent_usd, format_burndown(updated, max_budget_usd=self.budget.max_budget_usd),
                    )
        finally:
            run_lock.release(self.runs_dir)

    def _run_inner(self) -> None:
        if self.notes:
            self.note_status.sync(self.notes)
            logger.info(
                "Fundamental notes: %s",
                ", ".join(f"{n.id}[{n.kind}]={self.note_status.status_of(n.id)}" for n in self.notes),
            )
        if not self.state.is_bootstrapped():
            try:
                bootstrap_ok = self.run_bootstrap_sprint()
            except BudgetExceeded as e:
                logger.warning("Sprint 0 (bootstrap) cut short by budget: %s. No steady-state sprints ran.", e)
                return
            if not bootstrap_ok:
                logger.error(
                    "Sprint 0 (bootstrap) was not accepted by the Critic — halting before steady-state "
                    "sprints. Inspect docs/changelog.md's Sprint 0 entries (required changes are listed), "
                    "adjust, run `python run.py --reset`, and rerun."
                )
                return
        else:
            logger.info("Sprint 0 already bootstrapped (docs/language-spec.md has constructs) — skipping.")

        self.sprint_offset = self.state.last_sprint_number()
        if self.sprint_offset:
            logger.info("Continuing sprint numbering after sprint %d.", self.sprint_offset)

        stop_reason = "completed_normally"
        while True:
            ok, reason = self.budget.status()
            if not ok:
                stop_reason = reason
                break
            if not self.fallback_to_tasks and self.notes and self._next_note() is None:
                stop_reason = "all_fundamental_notes_settled (run.steering.fallback_to_tasks: false)"
                break
            sprint = self.sprint_offset + self.budget.iteration + 1
            try:
                self.run_sprint(sprint)
            except BudgetExceeded as e:
                stop_reason = f"budget_exceeded_mid_sprint: {e}"
                logger.warning("Sprint %d cut short: %s", sprint, e)
                break
            self.budget.complete_sprint()

        logger.info("Loop stopped: %s | %s", stop_reason, self.budget.summary())

    # ------------------------------------------------------------------ attempts
    def _log_malformed_attempt(self, *, sprint: int, attempt: int, max_attempts: int, bootstrap: bool, exc: Exception) -> None:
        """No proposal dict exists for this attempt — either the Shaper's response never parsed
        as JSON, or the LLM call itself failed before returning a response at all (LLMCallFailed;
        `exc`'s own message says which) — so there's nothing for doc_hygiene/Critic/Documenter to
        work with. Write a minimal, LLM-free changelog entry directly so the attempt is still
        visible in the audit trail."""
        label = "Sprint 0 (bootstrap)" if bootstrap else f"Sprint {sprint}"
        attempt_label = format_attempt_label(attempt, max_attempts)
        header = f"## {label}" + (f" {attempt_label}" if attempt_label else "") + f" — {self.state.today()}"
        self.state.append_changelog_entry(
            f"\n{header}\n\n"
            f"- **Shaper failed to produce a usable proposal:** {exc}\n"
            f"- **Decision:** needs-rework (no proposal to assess)\n"
        )

    def _run_attempt(
        self, *, sprint: int, attempt: int, max_attempts: int, proposal: dict, bootstrap: bool,
        task, searcher_notes: dict, spent_before: float, previous_attempt: dict | None = None,
        force_accept: bool = False, focus_note=None, positions: list[dict] | None = None,
    ) -> tuple[str, dict, dict]:
        """Returns (decision, critique, proposal). `positions` (multi-position steering attempt):
        several competing proposals; the Critic picks one, and that one is the returned
        `proposal` (the `proposal` argument is then just positions[0])."""
        spec_text = _read(self.state.spec_path)
        glossary_text = _read(self.state.glossary_path)
        existing_names = self.state.spec_construct_names()
        existing_vocab = self.state.vocabulary_names()
        notes_text = self._notes_text(focus_note)
        if positions and len(positions) < 2:
            proposal, positions = positions[0], None
        for p in positions or [proposal]:
            changes_summary = ", ".join(
                f"{c.get('construct_name', '?')}({c.get('op', 'add')})" for c in p.get("changes") or []
            ) or "(none)"
            logger.info(
                "Sprint %d attempt %d: Shaper (%s/%s) proposed: %s%s",
                sprint, attempt, p.get("_provider_used", "?"), p.get("_model_used", "?"), changes_summary,
                f" | rebuttals: {len(p['rebuttals'])}" if p.get("rebuttals") else "",
            )

        for p in positions or [proposal]:
            _normalize_revise_of_missing(p, existing_names, existing_vocab, sprint=sprint, attempt=attempt)
        position_hygiene = [doc_hygiene.check(p, existing_names, existing_vocab) for p in positions] if positions else None
        hygiene = doc_hygiene.check(proposal, existing_names, existing_vocab)
        if not hygiene.ok and not positions:
            logger.warning("Sprint %d attempt %d: %s", sprint, attempt, hygiene.describe())

        items = simulation.sample_items(
            self.sim_pool, closed_sources=self.closed_sources, open_sources=self.open_sources,
            per_closed=self.items_per_dataset_closed, per_open=self.items_per_dataset_open, rng=self.sim_rng,
        )
        providers = [p for p in self.cross_check_cfg.get("providers", ["anthropic", "gemini"]) if p != self.critic.cfg.get("provider")]
        xcheck_items = simulation.pick_cross_check_items(items, self.cross_check_cfg.get("max_items"))
        if positions:
            ok, note = False, "skipped — multi-position attempt (the Critic compares the positions instead)"
        else:
            ok, note = simulation.should_cross_check(
                mode=self.cross_check_cfg.get("mode", "auto"), changes=proposal.get("changes") or [],
                spec_construct_count=len(existing_names), budget=self.budget,
                n_items=len(xcheck_items), n_providers=len(providers),
            )
            if ok and len(xcheck_items) < len(items):
                note += f" ({len(xcheck_items)} of {len(items)} items cross-checked)"
        translations: dict = {}
        if ok:
            translations = simulation.cross_translate(
                items=xcheck_items, spec_text=spec_text, proposal=proposal, providers=providers,
                max_tokens=int(self.cross_check_cfg.get("max_tokens", 3000)),
                effort=self.cross_check_cfg.get("effort"),
                models_map=self.shaper.models, sprint=sprint, budget=self.budget,
                pricing_table=self.pricing, dry_run=self.dry_run, llm_cfg=self.llm_cfg,
                transcript=self.transcript, attempt=attempt, notes_text=notes_text,
                # Only the Vocabulary section: construct glossary entries duplicate the spec, and
                # this prompt is sent once per item per provider.
                glossary_text=self.state.vocabulary_section(),
            )
            if not translations:
                note = "attempted, but fewer than 2 providers returned usable translations — Critic simulates alone"
        logger.info("Sprint %d attempt %d: %d simulation items, cross-check: %s", sprint, attempt, len(items), note)

        try:
            critique = self.critic.assess(
                sprint=sprint, attempt=attempt, proposal=proposal, spec_text=spec_text, glossary_text=glossary_text,
                simulation_items=items, cross_translations=translations, cross_check_note=note,
                hygiene=hygiene, bootstrap=bootstrap, notes_text=notes_text, focus_note=focus_note,
                previous_attempt=previous_attempt, positions=positions, position_hygiene=position_hygiene,
            )
        except (ValueError, LLMCallFailed) as exc:
            logger.error("Sprint %d attempt %d: Critic call failed: %s", sprint, attempt, exc)
            critique = _carry_forward_critique(exc, (previous_attempt or {}).get("critique"))
        if positions:
            chosen = _chosen_index(critique.get("chosen_position"), len(positions), position_hygiene)
            proposal, hygiene = positions[chosen], position_hygiene[chosen]
            logger.info(
                "Sprint %d attempt %d: Critic chose position %d (%s) of %d.",
                sprint, attempt, chosen, proposal.get("_provider_used", "?"), len(positions),
            )
            if not hygiene.ok:
                logger.warning("Sprint %d attempt %d: %s", sprint, attempt, hygiene.describe())
        changes = proposal.get("changes") or []
        if not hygiene.ok:
            # The Shaper only sees the critique on rework — put the scripted failures in it
            # verbatim, so it can't miss e.g. a remove/revise that names a nonexistent entry.
            critique = dict(critique)
            critique["required_changes"] = [
                {"target": "doc hygiene (scripted — blocks acceptance)", "change": hygiene.describe()}
            ] + list(critique.get("required_changes") or [])
        decision = decide(hygiene, critique, self.hard_note_ids)
        violated = violated_hard_notes(critique, self.hard_note_ids)
        regressed = regressed_hard_notes(critique, self.hard_note_ids)
        if violated:
            logger.info("Sprint %d attempt %d: hard note(s) still violated after the changes (not blocking): %s", sprint, attempt, ", ".join(violated))
        if regressed:
            logger.warning("Sprint %d attempt %d: Critic reports hard note(s) REGRESSED (blocks acceptance): %s", sprint, attempt, ", ".join(regressed))
        if force_accept and decision == "needs-rework" and hygiene.ok and not regressed:
            # hygiene.ok is checked explicitly and separately from `decision` — decide() returns
            # "needs-rework" both for a genuine Critic verdict AND for a doc-hygiene failure, and
            # those two cases must not be treated the same here (see comment below).
            # Deliberately narrow: only overrides a genuine "needs-rework" (per critic_system.md,
            # this means "the core idea is sound but specific issues must be fixed first") — never
            # an explicit `reject` (the Critic judged the shape fundamentally wrong, which
            # force-accept must not paper over), and never a doc-hygiene failure (missing
            # glossary_gloss/worked_example would corrupt upsert_construct_in_spec/
            # upsert_glossary_entry, which index into those fields directly). This is the last
            # attempt in the sprint — instead of retrying forever or ending with nothing
            # documented, accept as-is and carry the Critic's required_changes forward as visible,
            # on-the-record known issues (they stay in the changelog/backlog either way, since
            # decide()/`_trail_blocks` already print required_changes whenever present, accepted
            # or not) rather than silently ending the sprint/bootstrap empty-handed.
            logger.warning(
                "Sprint %d attempt %d/%d: last attempt still needs-rework — force-accepting with "
                "known issues carried forward (config.yaml -> run.%s.max_attempts).",
                sprint, attempt, max_attempts, "bootstrap" if bootstrap else "sprint",
            )
            critique = dict(critique)
            critique["reasoning"] = (
                f"[Forced acceptance after {max_attempts} attempt(s) without a clean accept — "
                f"the required changes below are known issues carried forward for a future sprint "
                f"to address, not resolved.] {critique.get('reasoning', '')}"
            )
            decision = "accepted"
        applied_names: list[str] | None = None
        if decision == "needs-rework" and not bootstrap:
            applied_names = self._partial_subset(
                proposal, critique, existing_names, existing_vocab, sprint=sprint, attempt=attempt,
            )
            if applied_names:
                decision = "partially-accepted"
        self.transcript.log_iteration_summary(
            sprint=sprint, attempt=attempt, max_attempts=max_attempts, bootstrap=bootstrap,
            decision=decision, critique=critique, cost_usd=self.budget.spent_usd - spent_before,
        )
        reason_snippet = " ".join((critique.get("reasoning") or "").split())
        if len(reason_snippet) > 180:
            reason_snippet = reason_snippet[:177] + "..."
        logger.info("Sprint %d attempt %d: Critic (%s): %s", sprint, attempt, decision, reason_snippet or "(no reasoning given)")
        append_history(self.runs_dir, build_history_record(
            sprint=sprint, attempt=attempt, proposal=proposal, hygiene=hygiene, critique=critique,
            decision=decision, cross_check_note=note, focus_note=focus_note.id if focus_note else None,
        ))

        cost_so_far = self.budget.spent_usd - spent_before
        if bootstrap:
            self.documenter.initialize_documentation(
                sprint=0, basis=proposal, searcher_notes=searcher_notes, critique=critique, hygiene=hygiene,
                decision=decision, state=self.state, cost_this_sprint=cost_so_far,
                attempt=attempt, max_attempts=max_attempts,
            )
        else:
            self.documenter.record_sprint(
                sprint=sprint, task=task, searcher_notes=searcher_notes, proposal=proposal, critique=critique,
                hygiene=hygiene, decision=decision, state=self.state, cost_this_sprint=cost_so_far,
                attempt=attempt, max_attempts=max_attempts, focus_note=focus_note,
                applied_names=applied_names,
            )
        # The Documenter's own call isn't in the figure it was just given — patch the entry it wrote.
        true_cost = self.budget.spent_usd - spent_before
        self.state.update_last_cost(true_cost)
        logger.info(
            "Sprint %d attempt %d/%d done: decision=%s hygiene=%s changes=%d cost=$%.4f cumulative=$%.4f",
            sprint, attempt, max_attempts, decision, "pass" if hygiene.ok else "FAIL", len(changes),
            true_cost, self.budget.spent_usd,
        )
        if applied_names:
            # The rework that follows sees what landed and what is still pending.
            critique = dict(critique)
            critique["_applied_changes"] = applied_names
        return decision, critique, proposal

    def _partial_subset(self, proposal: dict, critique: dict, existing_names: set[str], existing_vocab: set[str],
                        *, sprint: int, attempt: int) -> list[str] | None:
        """Partial acceptance: when the Critic sends a bundle back but names, in `accept_changes`,
        a subset that is sound on its own and regresses no note, apply just that subset instead of
        discarding it with the rest. Applied only if the subset passes doc hygiene by itself; the
        Critic's judgment is what vouches for its no-regression and self-containment."""
        wanted = [str(n) for n in (critique.get("accept_changes") or []) if n]
        if not wanted:
            return None
        subset = [c for c in proposal.get("changes") or [] if c.get("construct_name") in wanted]
        if not subset:
            return None
        sub_hygiene = doc_hygiene.check({"changes": subset}, existing_names, existing_vocab)
        if not sub_hygiene.ok:
            logger.warning(
                "Sprint %d attempt %d: Critic's accept_changes subset fails doc hygiene — not applied: %s",
                sprint, attempt, sub_hygiene.describe(),
            )
            return None
        names = [c.get("construct_name") for c in subset]
        logger.info(
            "Sprint %d attempt %d: PARTIAL ACCEPTANCE — applying %d of %d changes: %s",
            sprint, attempt, len(subset), len(proposal.get("changes") or []), ", ".join(names),
        )
        return names

    # ------------------------------------------------------------------ steering
    def _next_note(self):
        return steering.next_note(self.notes, self.note_status)

    def _notes_text(self, focus_note=None) -> str:
        return steering.notes_block(self.notes, self.note_status, focus=focus_note)

    def run_bootstrap_sprint(self) -> bool:
        """True once the Critic accepts a basis; False if every attempt was sent back. Grounding
        runs once per Sprint 0 (the reference material doesn't change between attempts)."""
        max_attempts = self.bootstrap_max_attempts
        logger.info("--- Sprint 0 (bootstrap) --- (up to %d attempt(s))", max_attempts)
        spent_before = self.budget.spent_usd
        try:
            searcher_notes = self.searcher.ground_basis(
                sprint=0, sources_text=_read(self.sources_path),
                inspiration_languages=self.inspiration_languages, state=self.state,
            )
        except (ValueError, LLMCallFailed) as exc:
            logger.error("Sprint 0 (bootstrap): Searcher call failed: %s", exc)
            searcher_notes = _fallback_searcher_notes(exc)

        previous_attempt = None
        for attempt in range(1, max_attempts + 1):
            try:
                basis = self.shaper.propose_basis(
                    sprint=0, searcher_notes=searcher_notes, inspiration_languages=self.inspiration_languages,
                    previous_attempt=previous_attempt, attempt=attempt, notes_text=self._notes_text(),
                )
            except (ValueError, LLMCallFailed) as exc:
                logger.error("Sprint 0 (bootstrap) attempt %d/%d: Shaper call failed: %s", attempt, max_attempts, exc)
                self._log_malformed_attempt(sprint=0, attempt=attempt, max_attempts=max_attempts, bootstrap=True, exc=exc)
                previous_attempt = _malformed_response_feedback(exc, previous_attempt)
                spent_before = self.budget.spent_usd
                continue
            decision, critique, _ = self._run_attempt(
                sprint=0, attempt=attempt, max_attempts=max_attempts, proposal=basis, bootstrap=True,
                task=None, searcher_notes=searcher_notes, spent_before=spent_before,
                previous_attempt=previous_attempt, force_accept=(attempt == max_attempts),
            )
            if decision == "accepted":
                return True
            previous_attempt = {"changes": basis.get("changes", []), "critique": critique}
            spent_before = self.budget.spent_usd

        # Only reachable if the last attempt was `rejected` outright, or `needs-rework` with
        # failing doc hygiene (force_accept deliberately never overrides either — see
        # _run_attempt) — a genuine `needs-rework` on the last attempt gets force-accepted above
        # and returns True before this point.
        logger.error(
            "Sprint 0 (bootstrap) still not accepted after %d attempt(s) — the last attempt was "
            "either `rejected` outright, or `needs-rework` with failing doc hygiene (force-accept "
            "never overrides either of those). Inspect docs/changelog.md's Sprint 0 entries for "
            "what keeps getting sent back.",
            max_attempts,
        )
        return False

    def run_sprint(self, sprint: int) -> None:
        """Steering sprint on the next open fundamental note if there is one, else a task sprint."""
        note = self._next_note()
        if note is not None:
            self.run_steering_sprint(sprint, note)
        else:
            self.run_task_sprint(sprint)

    def run_steering_sprint(self, sprint: int, note) -> None:
        max_attempts = self.sprint_max_attempts
        logger.info("--- Sprint %d (steering: %s [%s]) --- (up to %d attempt(s))", sprint, note.id, note.kind, max_attempts)
        spent_before = self.budget.spent_usd
        try:
            searcher_notes = self.searcher.ground_note(
                sprint=sprint, note=note, notes_text=self._notes_text(note),
                spec_text=_read(self.state.spec_path), sources_text=_read(self.sources_path), state=self.state,
            )
        except (ValueError, LLMCallFailed) as exc:
            logger.error("Sprint %d: Searcher call failed: %s", sprint, exc)
            searcher_notes = _fallback_searcher_notes(exc)

        # A note carried over from an earlier sprint resumes that sprint's discussion.
        previous_attempt = self.note_status.last_attempt(note.id)
        if previous_attempt:
            logger.info("Sprint %d: resuming %s's discussion (%s).", sprint, note.id, previous_attempt.get("origin"))
        chosen_provider = None
        decision, critique, last_proposal = "needs-rework", {}, None
        for attempt in range(1, max_attempts + 1):
            # Attempt 1 may gather several competing positions; reworks continue with the chosen one's provider.
            if attempt == 1 and self.positions > 1:
                rotation = self.shaper.rotation
                start = sprint % len(rotation)
                providers = [rotation[(start + i) % len(rotation)] for i in range(min(self.positions, len(rotation)))]
            else:
                providers = [chosen_provider]
            positions = []
            last_exc = None
            for provider in providers:
                try:
                    positions.append(self.shaper.propose_steering(
                        sprint=sprint, note=note, notes_text=self._notes_text(note), searcher_notes=searcher_notes,
                        spec_text=_read(self.state.spec_path), glossary_text=_read(self.state.glossary_path),
                        previous_attempt=previous_attempt, attempt=attempt, provider=provider,
                        max_changes=self.max_changes,
                    ))
                except (ValueError, LLMCallFailed) as exc:
                    logger.error("Sprint %d attempt %d/%d: Shaper (%s) call failed: %s", sprint, attempt, max_attempts, provider or "rotation", exc)
                    last_exc = exc
            if not positions:
                self._log_malformed_attempt(sprint=sprint, attempt=attempt, max_attempts=max_attempts, bootstrap=False, exc=last_exc)
                previous_attempt = _malformed_response_feedback(last_exc, previous_attempt)
                spent_before = self.budget.spent_usd
                continue
            decision, critique, proposal = self._run_attempt(
                sprint=sprint, attempt=attempt, max_attempts=max_attempts, proposal=positions[0], bootstrap=False,
                task=None, searcher_notes=searcher_notes, spent_before=spent_before,
                previous_attempt=previous_attempt, force_accept=(attempt == max_attempts),
                focus_note=note, positions=positions if len(positions) > 1 else None,
            )
            chosen_provider = proposal.get("_provider_used")
            last_proposal = proposal
            previous_attempt = _next_previous_attempt(proposal, critique, decision)
            if decision not in ("needs-rework", "partially-accepted"):
                break
            spent_before = self.budget.spent_usd

        assessment = (critique.get("notes_assessment") or {}).get(note.id)
        sprints_spent = len((self.note_status.data.get(note.id) or {}).get("sprints", [])) + 1
        status = steering.resolve_status(
            note=note, decision=decision, assessment=assessment,
            sprints_spent=sprints_spent, max_sprints=self.max_sprints_per_note,
        )
        self.note_status.record(
            note, sprint=sprint, status=status, assessment=assessment,
            last_attempt=previous_attempt if last_proposal else None,
        )
        self.documenter.record_note_outcome(sprint=sprint, note=note, status=status, assessment=assessment, state=self.state)
        logger.info("Sprint %d: note %s -> %s", sprint, note.id, status)

    def run_task_sprint(self, sprint: int) -> None:
        max_attempts = self.sprint_max_attempts
        logger.info("--- Sprint %d --- (up to %d attempt(s))", sprint, max_attempts)
        spent_before = self.budget.spent_usd

        task = self.state.sample_task("dev")
        try:
            searcher_notes = self.searcher.ground_candidate(
                sprint=sprint, task=task, sources_text=_read(self.sources_path), state=self.state,
            )
        except (ValueError, LLMCallFailed) as exc:
            logger.error("Sprint %d: Searcher call failed: %s", sprint, exc)
            searcher_notes = _fallback_searcher_notes(exc)

        previous_attempt = None
        for attempt in range(1, max_attempts + 1):
            try:
                proposal = self.shaper.propose(
                    sprint=sprint, task=task, searcher_notes=searcher_notes,
                    spec_text=_read(self.state.spec_path), glossary_text=_read(self.state.glossary_path),
                    previous_attempt=previous_attempt, attempt=attempt, notes_text=self._notes_text(),
                )
            except (ValueError, LLMCallFailed) as exc:
                logger.error("Sprint %d attempt %d/%d: Shaper call failed: %s", sprint, attempt, max_attempts, exc)
                self._log_malformed_attempt(sprint=sprint, attempt=attempt, max_attempts=max_attempts, bootstrap=False, exc=exc)
                previous_attempt = _malformed_response_feedback(exc, previous_attempt)
                spent_before = self.budget.spent_usd
                continue
            decision, critique, proposal = self._run_attempt(
                sprint=sprint, attempt=attempt, max_attempts=max_attempts, proposal=proposal, bootstrap=False,
                task=task, searcher_notes=searcher_notes, spent_before=spent_before,
                previous_attempt=previous_attempt, force_accept=(attempt == max_attempts),
            )
            if decision not in ("needs-rework", "partially-accepted"):
                return
            previous_attempt = _next_previous_attempt(proposal, critique, decision)
            spent_before = self.budget.spent_usd


def _carry_forward_critique(exc: Exception, fallback_critique: dict | None) -> dict:
    """Best-effort critique to hand the Shaper when a role's call failed this attempt. If a real
    critique from an earlier attempt in this same sprint is already on hand, keep it intact (its
    required_changes/logic_issues are still exactly what the next attempt needs to fix — the
    proposal that earned them hasn't been superseded by a new judgment) and just add a note about
    this attempt's failure on top. Otherwise a failure would silently erase all of the Critic's
    substantive feedback and the following attempt would effectively restart from scratch instead
    of revising. Only when there is no earlier real critique to fall back on (e.g. attempt 1
    itself failed) do we fall back to generic guidance.

    `exc` may be a genuine JSON-parse failure (ValueError from parse_json_response — a formatting
    problem, worth telling the model to fix) or an LLMCallFailed (the call itself never returned a
    response — an infrastructure problem, where "fix your JSON formatting" would be actively wrong
    advice since content was never even the issue)."""
    if isinstance(exc, LLMCallFailed):
        note = {
            "target": "infrastructure",
            "change": "(no content change needed — the previous attempt's LLM call itself failed "
                      "before producing a response; retry as-is.)",
        }
    elif "cut off at the output limit" in str(exc):
        note = {
            "target": "proposal size",
            "change": f"{exc}. Carry the essentials forward; leave the rest for the next sprint.",
        }
    else:
        note = {
            "target": "response format",
            "change": "Return only a single valid JSON object matching the schema exactly — "
                       "no prose outside it, no unescaped quotes inside string values, no "
                       "trailing commas, no markdown code fences.",
        }
    if fallback_critique:
        critique = dict(fallback_critique)
        critique["reasoning"] = (
            f"(A more recent attempt failed: {exc}. The required changes below are carried "
            f"forward from the last successfully judged attempt and still apply.) "
            f"{critique.get('reasoning', '')}"
        )
        critique["required_changes"] = [note] + list(critique.get("required_changes") or [])
        return critique
    return {
        "decision": "needs-rework",
        "reasoning": f"Attempt failed: {exc}",
        "required_changes": [note],
        "logic_issues": [],
        "kpi_assessment": {},
        "simulations": [],
    }


def _malformed_response_feedback(exc: Exception, previous_attempt: dict | None = None) -> dict:
    """`previous_attempt` for the next Shaper call after the Shaper's own call failed this
    attempt (parse failure or LLMCallFailed) — see _carry_forward_critique for how prior
    substantive feedback survives and how the two failure classes are distinguished."""
    prior_critique = (previous_attempt or {}).get("critique")
    return {
        "changes": (previous_attempt or {}).get("changes", []),
        "critique": _carry_forward_critique(exc, prior_critique),
    }


def _normalize_revise_of_missing(proposal: dict, existing_names: set[str], existing_vocab: set[str], *, sprint: int, attempt: int) -> None:
    """On rework the Shaper naturally refers to what it *proposed* last attempt — but a rejected
    attempt never entered the docs, so those entries don't exist yet. A `revise` of such an entry
    is really an add (the upsert writes it either way), and a `remove` of one just means "drop it
    from my proposal" — nothing to delete. Normalize both instead of failing doc hygiene."""
    kept = []
    for change in proposal.get("changes") or []:
        existing = existing_vocab if doc_hygiene.is_vocabulary(change) else existing_names
        missing = change.get("construct_name") not in existing
        if change.get("op") == "revise" and missing:
            change["op"] = "add"
            logger.info(
                "Sprint %d attempt %d: `%s` is marked revise but isn't in the docs yet — treating it as add.",
                sprint, attempt, change.get("construct_name"),
            )
        elif change.get("op") == "remove" and missing:
            logger.info(
                "Sprint %d attempt %d: `%s` is marked remove but isn't in the docs — dropping that change (nothing to remove).",
                sprint, attempt, change.get("construct_name"),
            )
            continue
        kept.append(change)
    if "changes" in proposal:
        proposal["changes"] = kept


def _next_previous_attempt(proposal: dict, critique: dict, decision: str = "needs-rework") -> dict:
    """What the next attempt revises (or, carried over, what the next sprint on this note starts
    from). After a partial acceptance only the changes that were NOT applied are pending; after a
    full (or forced) acceptance nothing is pending — everything is in the docs now, and only the
    Critic's required changes (known issues) remain. Say which is which."""
    if decision == "accepted":
        applied = [c.get("construct_name") for c in proposal.get("changes") or []]
    else:
        applied = critique.get("_applied_changes") or []
    pending = [c for c in proposal.get("changes") or [] if c.get("construct_name") not in applied]
    out = {"changes": pending, "critique": critique}
    if applied:
        out["applied"] = applied
    return out


def _chosen_index(raw, n: int, hygiene: list) -> int:
    """The Critic's `chosen_position`, validated. Falls back to the first position that passes
    doc hygiene (else 0) when it's missing or out of range."""
    try:
        idx = int(raw)
        if 0 <= idx < n:
            return idx
    except (TypeError, ValueError):
        pass
    return next((i for i, h in enumerate(hygiene or []) if h.ok), 0)


def _fallback_searcher_notes(exc: Exception) -> dict:
    """Searcher runs once per sprint, ahead of the Shaper/Critic attempt loop — if its call fails
    (a JSON-parse failure after retries, or an LLMCallFailed infrastructure failure), the sprint
    should still proceed on a minimal, honest note rather than crash the whole run over a
    grounding-notes failure. The Shaper/Critic system prompts already treat sparse searcher_notes
    as normal (folder-mode sprints can be thin)."""
    return {
        "notes": f"(Searcher call failed this sprint: {exc} — proceeding without grounding notes.)",
        "relevant_precedents": [],
        "new_source_suggestion": None,
    }


def _read(path: str) -> str:
    if not os.path.exists(path):
        return ""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
