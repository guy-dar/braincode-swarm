"""Offline stand-in for any provider. Returns deterministic, schema-valid canned JSON so the
whole orchestrator/budget/state pipeline can be smoke-tested with zero API calls and $0 cost.
Enable via config.yaml -> run.dry_run: true.

Every role's user prompt starts with a `# ROLE: <name>` marker line (see
roles/base_role.py::BaseRole.call, simulation.py::cross_translate) — this client reads that
marker to decide which canned shape to return. Token counts are fabricated from text length so
budget math still has something plausible to chew on. `use_search_grounding` is accepted but has
no effect here.
"""
from __future__ import annotations

import json
import re

from .base import LLMClient, LLMResponse


def _construct(name, grammar, semantics, nl, braincode, gloss, change_type, rationale, source, op="add"):
    return {
        "op": op,
        "construct_name": name,
        "grammar": grammar,
        "semantics": semantics,
        "worked_example": {"nl": nl, "braincode": braincode},
        "glossary_gloss": gloss,
        "change_type": change_type,
        "rationale": rationale,
        "cites_source": source,
    }


def _critique(decision, reasoning, sims, bootstrap=False, notes_assessment=None):
    return {
        "notes_assessment": notes_assessment or {},
        "rebuttal_rulings": [],
        "decision": decision,
        "kpi_assessment": {
            "coverage": {"impact": "benefit", "reasoning": "[dry-run] Sampled web/household/chat items express in full with the proposed constructs."},
            "expressivity": {"impact": "benefit", "reasoning": "[dry-run] Conditions, ordering, and recipients survive the round trip."},
            "determinism": {"impact": "neutral", "reasoning": "[dry-run] Cross-provider translations agree after canonicalization; naming of args still free-form."},
            "interpretability": {"impact": "benefit", "reasoning": "[dry-run] Every construct has a gloss; no overlap with existing constructs."},
            "improvement": {"impact": "neutral", "reasoning": "[dry-run] No evidence either way at this scale."},
        },
        "simulations": sims,
        "cross_check": {"used": True, "agreement": "high", "notes": "[dry-run] both providers produced the same canned expression."},
        "required_changes": [] if decision == "accept" else [{"target": "basis", "change": "[dry-run] define iteration"}],
        "logic_issues": [],
        "reasoning": reasoning + (" (bootstrap)" if bootstrap else ""),
    }


_CANNED = {
    "searcher": {
        "search_mode": "folder",
        "relevant_precedents": ["Parsel (arxiv.org/abs/2212.10561)"],
        "phenomena_present": ["conditional", "multi-step-dependency"],
        "kpi_fit": {"Parsel (arxiv.org/abs/2212.10561)": "[dry-run] Strong on expressivity for decomposition/dependency; not evaluated for determinism across independent authors."},
        "comparable_expression": {
            "precedent": "Parsel (arxiv.org/abs/2212.10561)",
            "nl": "[dry-run candidate task]",
            "rendering": "[dry-run] Parsel-style: define a `follow_up()` function guarded by a `reply_received` precondition, composed into the parent plan.",
        },
        "notes": "[dry-run] candidate task exercises a conditional branch and a follow-up action; Parsel's decomposition style is the closest precedent.",
        "new_source_suggestion": None,
    },
    "searcher_bootstrap": {
        "search_mode": "folder",
        "python_notes": "[dry-run] Python favors composable, indentation-scoped statements over deeply nested syntax; good precedent for a construct's grammar staying flat and readable.",
        "html_notes": "[dry-run] HTML separates content from attributes (style/context) via tags — precedent for BrainCode carrying context/register as attributes rather than inline prose.",
        "english_notes": "[dry-run] English marks conditionals, negation, and recipients with closed function-word classes, not open vocabulary — precedent for keeping BrainCode's core grammar small.",
        "formal_language_notes": "[dry-run] Chomsky-hierarchy framing: aim for a context-free core (composable, parseable) with a small set of primitives rather than a context-sensitive grammar.",
        "relevant_precedents": ["Parsel (arxiv.org/abs/2212.10561)", "Automatic Textbook Formalization (arxiv.org/abs/2604.03071)"],
        "new_source_suggestion": None,
    },
    "shaper": {
        "summary": "[dry-run] Add a conditional branch and revise SEQ to allow an empty else-path.",
        "changes": [
            _construct(
                "cond-branch", "COND(<condition>) -> THEN(<action>) [ELSE(<action>)]",
                "Evaluates <condition> against task state; executes THEN branch if true, ELSE branch (if present) otherwise. No implicit fallthrough.",
                "[dry-run candidate task]", "COND(reply_received == false) -> THEN(send(follow_up))",
                "A conditional branch: run one action if a condition holds, otherwise an optional alternate action.",
                "MINOR", "[dry-run] Task requires expressing an if/else without natural-language fallback.", "Parsel",
            ),
            _construct(
                "seq", "SEQ(<step>, <step>, ...)",
                "Executes steps in the given order; no implicit reordering or parallelism. A SEQ with zero steps is a no-op.",
                "first draft it, then send it", "SEQ(ACTION(draft, [it]), ACTION(send, [it]))",
                "Runs a list of steps in the exact order given; an empty list does nothing.",
                "PATCH", "[dry-run] Clarify the empty case so COND's ELSE can be an empty SEQ.", "Python (statement lists)",
                op="revise",
            ),
        ],
    },
    "shaper_bootstrap": {
        "foundations_overview": "[dry-run] Core grammar: ENTITY(name, attrs) for referents, ACTION(verb, args) for operations, SEQ(...) for ordering. Inspired by Python's flat composability, HTML's content/attribute separation, and English's closed-class function words.",
        "inspiration_summary": "[dry-run] Draws structural composability from Python, context/attribute separation from HTML, and closed-class function words from English.",
        "summary": "[dry-run] Three orthogonal primitives: referents, operations, ordering.",
        "changes": [
            _construct(
                "entity-ref", "ENTITY(<name>, <attrs>)",
                "References a person/object/resource with a name and a set of context attributes (e.g. register, relationship) — analogous to an HTML tag with attributes.",
                "my professor", "ENTITY(professor, {register: formal})",
                "Names a person, object, or resource, tagged with context attributes like formality or relationship.",
                "MAJOR", "[dry-run] Foundational primitive: nearly every task references some entity with implicit style/context.", "HTML (attributes)",
            ),
            _construct(
                "action", "ACTION(<verb>, <args>)",
                "A single operation with a verb and argument list — the atomic unit of agentic execution.",
                "send a message", "ACTION(send, [message])",
                "One concrete operation: a verb plus its arguments.",
                "MAJOR", "[dry-run] Foundational primitive: composable operation unit, akin to a Python function call.", "Python (function calls)",
            ),
            _construct(
                "seq", "SEQ(<step>, <step>, ...)",
                "Executes steps in the given order; no implicit reordering or parallelism.",
                "first draft it, then send it", "SEQ(ACTION(draft, [it]), ACTION(send, [it]))",
                "Runs a list of steps in the exact order given.",
                "MAJOR", "[dry-run] Foundational primitive: temporal ordering, a core reasoning phenomenon.", "English (temporal connectives)",
            ),
        ],
    },
    "critic": _critique(
        "accept",
        "[dry-run] The changes express every sampled item without prose fallback and introduce no ambiguity.",
        [
            {"item_id": "dev-email-2", "source": "seed_tasks", "nl": "If my manager hasn't replied by Friday, send a polite follow-up; otherwise do nothing.",
             "braincode": "COND(replied(ENTITY(manager), by=friday) == false) -> THEN(ACTION(send, [follow_up, {tone: polite}])) ELSE(SEQ())",
             "coverage": "Full", "notes": "[dry-run] cond-branch carries the conditional; revised SEQ covers 'do nothing'."},
            {"item_id": "m2w-seed-1", "source": "mind2web", "nl": "Find the cheapest one-way flight from New York to Chicago on March 3.",
             "braincode": "SEQ(ACTION(search, [flights, {from: NYC, to: CHI, date: 03-03, oneway: true}]), ACTION(select, [cheapest]))",
             "coverage": "Full", "notes": "[dry-run] plain sequence; no new construct needed."},
        ],
    ),
    "critic_bootstrap": _critique(
        "accept",
        "[dry-run] Basis is internally consistent — no cross-construct overlap; simulated items express fully.",
        [
            {"item_id": "alfred-seed-1", "source": "alfred", "nl": "Put a clean mug in the coffee maker.",
             "braincode": "SEQ(ACTION(pick, [ENTITY(mug)]), ACTION(clean, [ENTITY(mug)]), ACTION(place, [ENTITY(mug), ENTITY(coffee_maker)]))",
             "coverage": "Full", "notes": "[dry-run] ordering + entities suffice."},
            {"item_id": "dev-email-1", "source": "seed_tasks", "nl": "Draft a reply to my professor asking for a two-day extension on the assignment, and keep it formal.",
             "braincode": "ACTION(draft_reply, [ENTITY(professor, {register: formal}), {topic: extension, days: 2}])",
             "coverage": "Full", "notes": "[dry-run] register carried as an attribute."},
        ],
        bootstrap=True,
    ),
    # Steering sprint (focus note N1 in the tests): revise `seq`, remove `entity-ref`.
    "shaper_steering": {
        "summary": "[dry-run] Realize N1: drop ENTITY in favour of plain arguments and let SEQ own ordering.",
        "note_position": "comply",
        "note_argument": "[dry-run] entity-ref is removed; seq's revised example no longer needs it.",
        "foundations_overview": None,
        "rebuttals": [],
        "changes": [
            {**_construct(
                "seq", "SEQ(<step>, <step>, ...)",
                "Executes steps in the given order; steps take plain arguments (no ENTITY wrapper).",
                "first draft it, then send it", "SEQ(ACTION(draft, [it]), ACTION(send, [it]))",
                "Runs a list of steps in the exact order given, with plain arguments.",
                "MINOR", "[dry-run] Revised per N1.", None, op="revise",
            ), "addresses_note": "N1"},
            {"op": "remove", "construct_name": "entity-ref", "change_type": "MAJOR", "addresses_note": "N1",
             "rationale": "[dry-run] N1 makes ENTITY redundant with plain arguments."},
            {"op": "add", "kind": "vocabulary", "construct_name": "tone-value", "closed": True,
             "glossary_gloss": "The tones a message can be written in.",
             "members": [{"symbol": "formal", "gloss": "Professional register.", "nl_synonyms": ["professional"]},
                         {"symbol": "polite", "gloss": "Courteous, softened requests.", "nl_synonyms": ["nice", "courteous"]}],
             "membership_rule": None,
             "worked_example": {"nl": "politely ask for an extension", "braincode": "ACTION(request, [extension, {tone: polite}])"},
             "change_type": "MINOR", "rationale": "[dry-run] tone values must be glossary symbols.", "addresses_note": "N1"},
        ],
    },
    "critic_steering": _critique(
        "accept",
        "[dry-run] N1 is realized: entity-ref is gone and every sampled item still expresses.",
        [
            {"item_id": "m2w-seed-1", "source": "mind2web", "nl": "Find the cheapest one-way flight from New York to Chicago on March 3.",
             "braincode": "SEQ(ACTION(search, [flights, {from: NYC, to: CHI}]), ACTION(select, [cheapest]))",
             "coverage": "Full", "notes": "[dry-run] no ENTITY needed."},
        ],
        notes_assessment={"N1": {"status": "satisfied", "trend": "improved", "reasoning": "[dry-run] entity-ref removed as the note asks."}},
    ),
    "translator": {"braincode": "SEQ(ACTION(search, [flights, {from: TLV, to: BER}]), ACTION(list, [cheapest, 3]))"},
    "documenter": {
        "summary": "[dry-run] Recorded sprint: cond-branch added and seq revised; Critic accepted on full coverage of the sampled items.",
    },
    "documenter_bootstrap": {
        "summary": "[dry-run] Recorded Sprint 0: base syntax established (entity-ref, action, seq), inspired by Python/HTML/English; Critic accepted after simulating sampled items in full.",
    },
}

_ALIASES = {"searcher_steering": "searcher"}  # same response shape as the aliased role

_ROLE_RE = re.compile(r"#\s*ROLE:\s*([a-zA-Z_]+)", re.IGNORECASE)


class DryRunClient(LLMClient):
    provider = "dry_run"

    def __init__(self, model: str = "dry-run"):
        super().__init__(model)

    def generate(
        self,
        *,
        system: str,
        user: str,
        max_tokens: int = 1500,
        temperature: float = 0.4,
        use_search_grounding: bool = False,
        effort: str | None = None,
    ) -> LLMResponse:
        match = _ROLE_RE.search(user) or _ROLE_RE.search(system)
        role_key = match.group(1).lower() if match else "documenter"
        payload = _CANNED.get(role_key) or _CANNED.get(_ALIASES.get(role_key, ""), {"notes": f"[dry-run] no canned response for role={role_key}"})
        text = json.dumps(payload)
        return LLMResponse(
            text=text,
            input_tokens=max(1, len(system + user) // 4),
            output_tokens=max(1, len(text) // 4),
            provider=self.provider,
            model=self.model,
            used_search_grounding=False,
        )
