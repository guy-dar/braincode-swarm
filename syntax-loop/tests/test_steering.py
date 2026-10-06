"""Steering: baseline import (`run.py --from`), fundamental notes (steering/notes.md), note-driven
sprints, `op: remove`, and the hard-note guard in decide()."""
import json
import os
import shutil

from braincode_loop import steering
from braincode_loop.decision import decide
from braincode_loop.doc_hygiene import HygieneResult, check
from braincode_loop.orchestrator import Orchestrator
from braincode_loop.reset import import_baseline, reset_workspace
from braincode_loop.state import LanguageState

from test_dry_run_smoke import _workspace

NOTES = """# notes
<!--
## N9 [hard] commented-out example, must be ignored
-->
## N1 [direction] Drop ENTITY in favour of plain arguments.
Referents are just arguments.

## N2 [hard] Every composition goes through a named Bind.
"""


def test_parse_notes_ignores_comments_and_reads_bodies():
    notes = steering.parse_notes(NOTES)
    assert [(n.id, n.kind) for n in notes] == [("N1", "direction"), ("N2", "hard")]
    assert notes[0].body == "Referents are just arguments."
    assert notes[1].body == ""


def test_project_notes_file_parses():
    """steering/notes.md is user-owned; only check it's well-formed (ids unique, kinds valid)."""
    base = os.path.join(os.path.dirname(__file__), "..", "steering", "notes.md")
    notes = steering.load_notes(base)
    assert len({n.id for n in notes}) == len(notes)
    assert all(n.kind in steering.NOTE_KINDS and n.title for n in notes)


def test_next_note_hard_first_then_reopen_on_edit(tmp_path):
    notes = steering.parse_notes(NOTES)
    status = steering.NoteStatus(str(tmp_path))
    status.sync(notes)
    assert steering.next_note(notes, status).id == "N2"  # hard before direction
    status.record(notes[1], sprint=5, status="resolved", assessment={"status": "upheld"})
    assert steering.next_note(notes, status).id == "N1"
    status.record(notes[0], sprint=6, status="resolved", assessment={"status": "satisfied"})
    assert steering.next_note(notes, status) is None

    # Persisted, and editing a note's text reopens it.
    reloaded = steering.NoteStatus(str(tmp_path))
    edited = steering.parse_notes(NOTES.replace("plain arguments.", "plain positional arguments."))
    reloaded.sync(edited)
    assert reloaded.status_of("N1") == "open" and reloaded.status_of("N2") == "resolved"


def test_resolve_status():
    direction = steering.Note("N1", "direction", "x")
    hard = steering.Note("N2", "hard", "y")
    kw = dict(sprints_spent=1, max_sprints=2)
    assert steering.resolve_status(note=direction, decision="accepted", assessment={"status": "satisfied"}, **kw) == "resolved"
    assert steering.resolve_status(note=direction, decision="accepted", assessment={"status": "contested"}, **kw) == "declined"
    assert steering.resolve_status(note=hard, decision="accepted", assessment={"status": "contested"}, **kw) == "open"
    assert steering.resolve_status(note=direction, decision="rejected", assessment=None, **kw) == "open"
    assert steering.resolve_status(note=direction, decision="rejected", assessment=None, sprints_spent=2, max_sprints=2) == "stalled"


def test_decide_gates_on_hard_note_regression_not_preexisting_violation():
    ok = HygieneResult(ok=True)
    # Still violated but no worse than the current spec: its own sprint will fix it — not blocking.
    still_violated = {"decision": "accept", "notes_assessment": {"N2": {"status": "violated", "trend": "unchanged"}}}
    assert decide(ok, still_violated, {"N2"}) == "accepted"
    regressed = {"decision": "accept", "notes_assessment": {"N2": {"status": "violated", "trend": "regressed"},
                                                            "N1": {"status": "partial", "trend": "regressed"}}}
    assert decide(ok, regressed, {"N2"}) == "needs-rework"
    assert decide(ok, regressed, set()) == "accepted"  # N1 isn't hard — only hard notes gate
    assert decide(ok, regressed) == "accepted"


def test_hard_focus_note_resolves_when_upheld():
    hard = steering.Note("N2", "hard", "y")
    kw = dict(sprints_spent=1, max_sprints=2)
    assert steering.resolve_status(note=hard, decision="accepted", assessment={"status": "upheld"}, **kw) == "resolved"
    assert steering.resolve_status(note=hard, decision="accepted", assessment={"status": "violated", "trend": "improved"}, **kw) == "open"


def test_hygiene_for_remove_and_revise_targets():
    remove_ok = {"op": "remove", "construct_name": "seq", "rationale": "merged"}
    assert check({"changes": [remove_ok]}, {"seq"}).ok
    assert not check({"changes": [remove_ok]}, {"other"}).ok  # removing something that doesn't exist
    assert not check({"changes": [{"op": "remove", "construct_name": "seq"}]}, {"seq"}).ok  # no rationale
    revise = {"op": "revise", "construct_name": "ghost", "grammar": "g", "semantics": "s",
              "glossary_gloss": "x", "worked_example": {"nl": "a", "braincode": "b"}}
    assert check({"changes": [revise]}).ok  # no existing_names -> schema check only
    assert not check({"changes": [revise]}, {"seq"}).ok


def _bootstrapped_products(tmp_path):
    """Bootstrap + 1 dry-run sprint, then copy the resulting spec/glossary out as a 'product'."""
    config = _workspace(tmp_path)
    config["budget"]["max_iterations"] = 1
    Orchestrator(config, base_dir=str(tmp_path)).run()
    products = tmp_path / "products"
    products.mkdir()
    for name in ("language-spec.md", "glossary.md"):
        shutil.copyfile(tmp_path / "docs" / name, products / name)
    return config, products


def test_import_baseline_and_remove_construct(tmp_path):
    _, products = _bootstrapped_products(tmp_path)
    import_baseline(str(tmp_path), str(products))

    docs = tmp_path / "docs"
    assert (docs / "language-spec.md").read_text(encoding="utf-8") == (products / "language-spec.md").read_text(encoding="utf-8")
    changelog = (docs / "changelog.md").read_text(encoding="utf-8")
    assert "## Baseline — imported v1.1.0" in changelog and "**Continues from sprint:** 1" in changelog
    assert "## Sprint 0 (bootstrap, attempt 1/3)" not in changelog  # fresh changelog, old history not carried
    assert not (tmp_path / "runs" / "kpi_history.jsonl").exists()

    state = LanguageState(str(docs), str(tmp_path / "braincode_loop" / "seed_tasks.json"))
    assert state.is_bootstrapped()
    assert state.last_sprint_number() == 1
    assert state.remove_construct("entity-ref")
    assert "entity-ref" not in state.spec_construct_names() and "entity-ref" not in state.glossary_terms()
    assert {"seq", "cond-branch", "action"} <= state.spec_construct_names()


def _write_notes(tmp_path, config, text):
    (tmp_path / "steering").mkdir(exist_ok=True)
    (tmp_path / "steering" / "notes.md").write_text(text, encoding="utf-8")
    config["run"]["steering"]["notes_path"] = "steering/notes.md"


def test_steering_run_from_baseline_end_to_end(tmp_path):
    config, products = _bootstrapped_products(tmp_path)
    import_baseline(str(tmp_path), str(products))
    _write_notes(tmp_path, config, "## N1 [direction] Drop ENTITY in favour of plain arguments.\n")
    config["budget"]["max_iterations"] = 2
    Orchestrator(config, base_dir=str(tmp_path)).run()

    docs = tmp_path / "docs"
    spec = (docs / "language-spec.md").read_text(encoding="utf-8")
    assert "### `entity-ref`" not in spec  # the steering sprint's remove landed
    assert "entity-ref" not in (docs / "glossary.md").read_text(encoding="utf-8")
    assert "**Version:** 2.1.0" in spec  # 1.1.0 baseline -> 2.0.0 (remove = MAJOR) -> 2.1.0 (task sprint)

    changelog = (docs / "changelog.md").read_text(encoding="utf-8")
    # Numbering continues after the baseline's sprint 1: Sprint 2 is steering, Sprint 3 falls back to a task.
    s2 = changelog[changelog.index("## Sprint 2"):changelog.index("## Sprint 3")]
    assert "**Steering note:** N1 [direction]" in s2 and "**Fundamental notes:**" in s2 and "N1: satisfied" in s2
    assert "`entity-ref` (remove, MAJOR)" in s2 and "`seq` (revise, MINOR)" in s2
    assert "`tone-value` (add vocabulary, MINOR)" in s2
    glossary = (docs / "glossary.md").read_text(encoding="utf-8")
    assert "### `tone-value` (vocabulary)" in glossary and "`polite`" in glossary
    assert "**Shaper's position on the note:** comply" in s2
    assert "**Candidate task:**" in changelog[changelog.index("## Sprint 3"):]

    status = json.loads((docs / "notes-status.json").read_text(encoding="utf-8"))
    assert status["N1"]["status"] == "resolved" and status["N1"]["sprints"] == [2]
    assert "| 2 | note N1 [direction] | resolved |" in (docs / "backlog.md").read_text(encoding="utf-8")

    with open(tmp_path / "runs" / "kpi_history.jsonl", "r", encoding="utf-8") as f:
        records = [json.loads(line) for line in f if line.strip()]
    assert [(r["sprint"], r["focus_note"]) for r in records] == [(2, "N1"), (3, None)]


def test_multi_position_steering_attempt(tmp_path):
    config, products = _bootstrapped_products(tmp_path)
    import_baseline(str(tmp_path), str(products))
    _write_notes(tmp_path, config, "## N1 [direction] Drop ENTITY in favour of plain arguments.\n")
    config["run"]["steering"]["positions"] = 3
    config["budget"]["max_iterations"] = 1
    Orchestrator(config, base_dir=str(tmp_path)).run()

    with open(tmp_path / "runs" / "budget_log.json", "r", encoding="utf-8") as f:
        calls = json.load(f)["calls"]
    shaper_providers = [c["provider"] for c in calls if c["role"] == "shaper"]
    assert len(shaper_providers) == 3  # one position per provider in attempt 1
    assert not [c for c in calls if c["role"] == "cross_check_translator"]  # skipped for multi-position
    assert "### `entity-ref`" not in (tmp_path / "docs" / "language-spec.md").read_text(encoding="utf-8")


def test_reset_clears_notes_status(tmp_path):
    config, products = _bootstrapped_products(tmp_path)
    import_baseline(str(tmp_path), str(products))
    _write_notes(tmp_path, config, "## N1 [direction] Drop ENTITY.\n")
    config["budget"]["max_iterations"] = 1
    Orchestrator(config, base_dir=str(tmp_path)).run()
    assert (tmp_path / "docs" / "notes-status.json").exists()
    reset_workspace(str(tmp_path))
    assert not (tmp_path / "docs" / "notes-status.json").exists()


def test_revise_of_missing_entry_becomes_add():
    from braincode_loop.orchestrator import _normalize_revise_of_missing
    p = {"changes": [
        {"op": "revise", "construct_name": "seq"},
        {"op": "revise", "construct_name": "new-thing"},
        {"op": "revise", "kind": "vocabulary", "construct_name": "tone-value"},
        {"op": "remove", "construct_name": "ghost"},
    ]}
    _normalize_revise_of_missing(p, {"seq"}, set(), sprint=1, attempt=2)
    assert [(c["op"], c["construct_name"]) for c in p["changes"]] == [
        ("revise", "seq"), ("add", "new-thing"), ("add", "tone-value")]  # remove of missing dropped


def test_truncated_steering_proposal_is_rejected():
    import pytest
    from braincode_loop.roles.shaper import _reject_truncated
    from braincode_loop.utils import parse_json_response
    cut = '{\n  "summary": "s",\n  "changes": [\n    {"op": "add", "construct_name": "a"},\n    {"op": "add", "construct_name": "b", "sem'
    result = parse_json_response(cut)
    assert result.get("_truncated")
    with pytest.raises(ValueError, match="cut off"):
        _reject_truncated(result, 12)
    _reject_truncated(parse_json_response('{"changes": []}'), 12)  # complete answers pass


def test_critic_sees_rebuttals_on_rework(tmp_path):
    from braincode_loop.roles.critic import Critic

    config = _workspace(tmp_path)
    orch = Orchestrator(config, base_dir=str(tmp_path))
    captured = {}

    def fake_call(**kwargs):
        captured.update(kwargs)
        return {"decision": "accept"}

    critic: Critic = orch.critic
    critic.call = fake_call
    note = steering.Note("N1", "direction", "Drop ENTITY.")
    critic.assess(
        sprint=4, attempt=2,
        proposal={"changes": [], "rebuttals": [{"target": "seq", "change": "rename it", "argument": "SEQ is idiomatic"}]},
        spec_text="", glossary_text="", simulation_items=[], cross_translations={}, cross_check_note="n/a",
        hygiene=HygieneResult(ok=True), notes_text="FUNDAMENTAL NOTES ...", focus_note=note,
        previous_attempt={"critique": {"required_changes": [{"target": "seq", "change": "rename it"}]}},
    )
    prompt = captured["user_prompt"]
    assert captured["role_marker"] == "critic_steering"
    assert "STEERING SPRINT focused on note N1" in prompt and "FUNDAMENTAL NOTES" in prompt
    assert "REBUTS" in prompt and "SEQ is idiomatic" in prompt


def test_vocabulary_entries_live_in_their_own_glossary_section(tmp_path):
    config, products = _bootstrapped_products(tmp_path)
    import_baseline(str(tmp_path), str(products))
    state = LanguageState(str(tmp_path / "docs"), str(tmp_path / "braincode_loop" / "seed_tasks.json"))
    vocab = {"construct_name": "seq", "glossary_gloss": "g", "closed": False, "sprint": 5,
             "members": [{"symbol": "a", "gloss": "first", "nl_synonyms": ["one"]}], "membership_rule": "one token",
             "worked_example": {"nl": "x", "braincode": "y"}}
    state.upsert_vocabulary_entry(vocab)  # same name as a construct — must not collide
    state.upsert_glossary_entry({**vocab, "construct_name": "later", "sprint": 6})  # construct added afterwards
    glossary = (tmp_path / "docs" / "glossary.md").read_text(encoding="utf-8")
    assert glossary.index("### `later`") < glossary.index("## Vocabulary") < glossary.index("### `seq` (vocabulary)")
    assert "- `a` — first (natural-language synonyms: one)" in glossary and "**Membership rule:** one token" in glossary
    assert state.vocabulary_names() == {"seq"} and "seq" in state.glossary_terms()
    assert "(vocabulary)" not in (tmp_path / "docs" / "language-spec.md").read_text(encoding="utf-8")

    state.upsert_vocabulary_entry({**vocab, "glossary_gloss": "revised"})
    assert (tmp_path / "docs" / "glossary.md").read_text(encoding="utf-8").count("### `seq` (vocabulary)") == 1
    assert state.remove_vocabulary_entry("seq") and state.vocabulary_names() == set()
    assert "seq" in state.glossary_terms()  # the construct entry survived


def test_hygiene_for_vocabulary():
    v = {"op": "add", "kind": "vocabulary", "construct_name": "tone-value", "glossary_gloss": "g",
         "worked_example": {"nl": "a", "braincode": "b"}}
    assert not check({"changes": [v]}).ok  # neither members nor membership_rule
    assert check({"changes": [{**v, "members": [{"symbol": "x"}]}]}).ok  # no grammar/semantics needed
    assert not check({"changes": [{**v, "op": "revise", "members": [{"symbol": "x"}]}]}, set(), set()).ok
    assert check({"changes": [{"op": "remove", "kind": "vocabulary", "construct_name": "tone-value", "rationale": "r"}]},
                 {"tone-value"} - {"tone-value"}, {"tone-value"}).ok  # checked against vocab, not constructs


def test_versioned_products_folder_is_resolved_and_never_modified(tmp_path):
    from braincode_loop.reset import resolve_baseline_dir
    _, products = _bootstrapped_products(tmp_path)
    fav = tmp_path / "favourite-products"
    for v in ("v1", "v2", "v10"):
        shutil.copytree(products, fav / v)
    (fav / "v11").mkdir()  # incomplete version folder is ignored
    (fav / "notes.txt").write_text("unrelated", encoding="utf-8")
    assert resolve_baseline_dir(str(fav)) == str(fav / "v10")
    assert resolve_baseline_dir(str(fav / "v1")) == str(fav / "v1")

    before = {p: p.read_bytes() for p in fav.rglob("*") if p.is_file()}
    mtimes = {p: p.stat().st_mtime_ns for p in before}
    import_baseline(str(tmp_path), str(fav))
    assert "v10" in (tmp_path / "docs" / "changelog.md").read_text(encoding="utf-8")
    after = {p: p.read_bytes() for p in fav.rglob("*") if p.is_file()}
    assert after == before and {p: p.stat().st_mtime_ns for p in after} == mtimes


def test_reset_archives_instead_of_deleting(tmp_path):
    config = _workspace(tmp_path)
    config["budget"]["max_iterations"] = 1
    Orchestrator(config, base_dir=str(tmp_path)).run()
    (tmp_path / "runs" / "logs" / "run_old").mkdir(parents=True)
    (tmp_path / "runs" / "logs" / "run_old" / "orchestration.log").write_text("old run", encoding="utf-8")
    kpi_before = (tmp_path / "runs" / "kpi_history.jsonl").read_text(encoding="utf-8")
    spec_before = (tmp_path / "docs" / "language-spec.md").read_text(encoding="utf-8")

    reset_workspace(str(tmp_path))
    archives = [a for a in (tmp_path / "runs" / "archive").iterdir() if (a / "runs" / "kpi_history.jsonl").exists()]
    assert len(archives) == 1
    latest = archives[0]
    assert (latest / "runs" / "kpi_history.jsonl").read_text(encoding="utf-8") == kpi_before
    assert (latest / "runs" / "budget_log.json").exists()
    assert (latest / "docs" / "language-spec.md").read_text(encoding="utf-8") == spec_before
    assert (tmp_path / "runs" / "logs" / "run_old" / "orchestration.log").read_text(encoding="utf-8") == "old run"


def test_each_run_keeps_its_own_budget_log(tmp_path):
    config = _workspace(tmp_path)
    config["budget"]["max_iterations"] = 1
    for run_id in ("run_a", "run_b"):
        log_dir = tmp_path / "runs" / "logs" / run_id
        log_dir.mkdir(parents=True)
        Orchestrator(config, base_dir=str(tmp_path), log_dir=str(log_dir)).run()
    assert (tmp_path / "runs" / "logs" / "run_a" / "budget_log.json").exists()
    assert (tmp_path / "runs" / "logs" / "run_b" / "budget_log.json").exists()


def test_rework_prompt_says_previous_attempt_was_not_applied():
    from braincode_loop.roles.shaper import _rework_block
    block = _rework_block({"changes": [{"op": "add", "construct_name": "x"}], "critique": {}, "origin": "carried over from sprint 10"})
    assert "NOT applied" in block and "COMPLETE set" in block and "carried over from sprint 10" in block


def test_open_note_carries_last_attempt_into_next_sprint(tmp_path):
    config, products = _bootstrapped_products(tmp_path)
    import_baseline(str(tmp_path), str(products))
    _write_notes(tmp_path, config, "## N1 [direction] Drop ENTITY.\n")
    config["run"]["steering"]["max_sprints_per_note"] = 5
    orch = Orchestrator(config, base_dir=str(tmp_path))
    real_assess = orch.critic.assess
    seen_previous = []

    def partial_assess(**kwargs):  # keep N1 open: needs-rework on every attempt
        seen_previous.append(kwargs.get("previous_attempt"))
        result = dict(real_assess(**kwargs))
        result["decision"] = "reject"
        result["notes_assessment"] = {"N1": {"status": "partial", "reasoning": "not yet"}}
        return result

    orch.critic.assess = partial_assess
    orch.note_status.sync(orch.notes)
    orch.run_sprint(2)
    stored = orch.note_status.last_attempt("N1")
    assert stored and stored["origin"] == "carried over from sprint 2" and stored["changes"]
    orch.run_sprint(3)
    assert seen_previous[0] is None and seen_previous[-1]["origin"] == "carried over from sprint 2"


def test_partial_acceptance_applies_only_the_named_subset(tmp_path):
    config, products = _bootstrapped_products(tmp_path)
    import_baseline(str(tmp_path), str(products))
    _write_notes(tmp_path, config, "## N1 [direction] Drop ENTITY.\n")
    config["run"]["sprint"]["max_attempts"] = 2
    orch = Orchestrator(config, base_dir=str(tmp_path))
    real_assess = orch.critic.assess
    seen_previous = []

    def partial_assess(**kwargs):
        seen_previous.append(kwargs.get("previous_attempt"))
        result = dict(real_assess(**kwargs))
        result["notes_assessment"] = {"N1": {"status": "partial", "trend": "improved"}}
        if len(seen_previous) == 1:
            result["decision"] = "needs-rework"
            result["accept_changes"] = ["tone-value"]  # vocabulary only; the remove/revise are sent back
        else:  # reject the final attempt so force-accept doesn't land the rest
            result["decision"] = "reject"
            result["accept_changes"] = []
        return result

    orch.critic.assess = partial_assess
    orch.note_status.sync(orch.notes)
    orch.run_sprint(2)

    docs = tmp_path / "docs"
    glossary = (docs / "glossary.md").read_text(encoding="utf-8")
    spec = (docs / "language-spec.md").read_text(encoding="utf-8")
    assert "### `tone-value` (vocabulary)" in glossary  # the accepted subset landed
    assert "### `entity-ref`" in spec  # the rest did not
    changelog = (docs / "changelog.md").read_text(encoding="utf-8")
    assert "**Partial acceptance:** applied 1 of 3 changes (`tone-value`)" in changelog
    backlog = (docs / "backlog.md").read_text(encoding="utf-8")
    assert "| 2 | `tone-value` | accepted |" in backlog and "| 2 | `entity-ref` | needs-rework |" in backlog
    # Attempt 2 was told what landed and only sees the pending changes.
    prev = seen_previous[1]
    assert prev["applied"] == ["tone-value"]
    assert [c["construct_name"] for c in prev["changes"]] == ["seq", "entity-ref"]
    from braincode_loop.roles.shaper import _rework_block
    assert "PARTIALLY ACCEPTED" in _rework_block(prev)


def test_carry_over_after_acceptance_marks_everything_applied():
    from braincode_loop.orchestrator import _next_previous_attempt
    from braincode_loop.roles.shaper import _rework_block
    proposal = {"changes": [{"construct_name": "a"}, {"construct_name": "b"}]}
    accepted = _next_previous_attempt(proposal, {"required_changes": [{"target": "a", "change": "x"}]}, "accepted")
    assert accepted["applied"] == ["a", "b"] and accepted["changes"] == []
    block = _rework_block(accepted)
    assert "ACCEPTED WITH KNOWN ISSUES" in block and "NOT applied" not in block
    partial = _next_previous_attempt(proposal, {"_applied_changes": ["a"]}, "partially-accepted")
    assert partial["applied"] == ["a"] and [c["construct_name"] for c in partial["changes"]] == ["b"]
    rework = _next_previous_attempt(proposal, {}, "needs-rework")
    assert "applied" not in rework and len(rework["changes"]) == 2
