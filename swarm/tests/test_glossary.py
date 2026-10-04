"""Glossary records: the legacy import, the render/import round trip, and
applying migration operations with validation."""
import copy

import pytest

from glossary import import_legacy, import_md, records, render, schema
from glossary.records import OpError, apply_ops, validate

LEGACY = records.REF_DIR / "history" / "legacy" / "glossary.legacy.md"


@pytest.fixture(scope="module")
def legacy_records():
    return import_legacy.convert(LEGACY.read_text(encoding="utf-8"))


@pytest.fixture
def recs(legacy_records):
    return copy.deepcopy(legacy_records)


def by_symbol(recs, sym):
    return next(r for r in recs if r["symbol"] == sym)


class TestLegacyImport:
    def test_every_inventory_member_is_a_record(self, legacy_records):
        text = LEGACY.read_text(encoding="utf-8")
        inventory = [line.split("|")[1].strip().strip("`") for line in text.splitlines()
                     if line.startswith("| `") and line.rstrip().endswith(("| Adapted |", "| Retained |", "| Composite |",
                                                                          "| Structural |", "| Needs clarification |"))]
        symbols = {r["symbol"] for r in legacy_records}
        assert len(inventory) == 252
        assert set(inventory) <= symbols

    def test_supplemental_and_support_entries_present(self, legacy_records):
        symbols = {r["symbol"] for r in legacy_records}
        assert {"pillow", "sofa", "armchair", "coffee_maker", "art_itinerary", "extract"} <= symbols
        assert {"requirement", "property_question", "outcome", "supports", "revises"} <= symbols

    def test_imported_glossary_is_valid(self, legacy_records):
        assert validate(legacy_records) == []

    def test_composite_depends_on_its_expansion(self, recs):
        assert "v19/support/subject" in by_symbol(recs, "content_kyoto_itinerary")["dependencies"]

    def test_members_link_their_category_rule(self, recs):
        assert "v19/rule/category/entity-name" in by_symbol(recs, "mug")["shared_rules"]
        assert "v19/rule/search-web-attributes" in by_symbol(recs, "search_web")["shared_rules"]

    def test_operation_signature_and_aliases_are_joined(self, recs):
        pick_up = by_symbol(recs, "pick_up")
        assert pick_up["signature"].startswith("(target: STRING")
        assert "grab" in pick_up["aliases"]

    def test_speech_acts_and_relations_are_typed(self, recs):
        assert by_symbol(recs, "ask")["kind"] == "speech_act"
        assert by_symbol(recs, "supports")["kind"] == "link"
        assert by_symbol(recs, "outcome")["kind"] == "claim_relation"


class TestRenderRoundTrip:
    def test_md_round_trip_is_exact(self, recs):
        recs = [schema.normalize(r) for r in recs]
        out, changed = import_md.merge_edits(recs, import_md.parse_md(render.render_md(recs, "test")))
        assert changed == []
        assert {r["id"]: r for r in out} == {r["id"]: r for r in recs}

    def test_md_has_one_row_per_live_record(self, recs):
        rows = import_md.parse_md(render.render_md(recs))
        assert len(rows) == len(recs)

    def test_manual_edit_bumps_version(self, recs):
        recs = [schema.normalize(r) for r in recs]
        out, changed = import_md.merge_edits(recs, [{"symbol": "mug", "definition": "A drinking cup with a handle."}])
        assert changed == ["v19/entity-name/mug"]
        assert by_symbol(out, "mug")["version"] == 2

    def test_new_row_gets_id_and_rules(self, recs):
        recs = [schema.normalize(r) for r in recs]
        out, changed = import_md.merge_edits(recs, [{"symbol": "kettle", "kind": "value", "category": "entity-name",
                                                     "definition": "A water-boiling vessel."}])
        kettle = by_symbol(out, "kettle")
        assert kettle["id"] == "v19/entity-name/kettle" == changed[0]
        assert kettle["shared_rules"] == ["v19/rule/category/entity-name"]
        assert validate(out, previous=recs) == []


NEW_CONSTRUCTOR = {"id": "v19/support/group_size", "symbol": "group_size", "kind": "constructor",
                   "status": "Accepted", "signature": "TERM group_size(group: STRING / TERM, count: NUMBER) -> TERM",
                   "definition": "The number of members of the described group.",
                   "shared_rules": ["v19/rule/support-primitives-general"]}


class TestApplyOps:
    def test_add_stamps_provenance(self, recs):
        out, report = apply_ops(recs, [{"op": "add", "record": NEW_CONSTRUCTOR, "suggestions": ["3-7#S1"]}], batch=3)
        rec = by_symbol(out, "group_size")
        assert rec["version"] == 1 and "provenance" not in rec
        assert report[0]["translator_ids"] == ["3-7"] and report[0]["outcome"] == "added"
        assert validate(out, previous=recs) == []

    def test_add_without_id_or_rules_is_completed_by_host(self, recs):
        bare = {"symbol": "walk_to", "kind": "operation", "signature": "(destination: STRING) -> void",
                "definition": "Move to the destination.", "shared_rules": ["v19/rule/category/operation-vocabulary"]}
        out, _ = apply_ops(recs, [{"op": "add", "record": bare, "suggestions": []}])
        rec = by_symbol(out, "walk_to")
        assert rec["id"] == "v19/operation-vocabulary/walk_to"
        assert rec["shared_rules"] == ["v19/rule/operations-general", "v19/rule/recording-signatures"]
        assert validate(out, previous=recs) == []

    def test_add_composite_derives_dependencies(self, recs):
        comp = {"id": "v19/composite/constraint_short", "symbol": "constraint_short", "kind": "composite",
                "status": "Accepted", "category": "constraint-value", "signature": "TERM constraint_short() -> TERM",
                "expansion": 'requirement(property="length", value="short")', "definition": "Must be short."}
        out, _ = apply_ops(recs, [{"op": "add", "record": comp, "suggestions": ["1-1#S1"]}])
        assert "v19/support/requirement" in by_symbol(out, "constraint_short")["dependencies"]

    def test_update_bumps_version(self, recs):
        out, _ = apply_ops(recs, [{"op": "update", "id": "v19/entity-name/mug", "set": {"definition": "Cup."},
                                   "reason": "clarify", "suggestions": ["2-1#S1"]}], batch=2)
        mug = by_symbol(out, "mug")
        assert mug["version"] == 2 and mug["definition"] == "Cup."

    def test_update_cannot_touch_id(self, recs):
        with pytest.raises(OpError):
            apply_ops(recs, [{"op": "update", "id": "v19/entity-name/mug", "set": {"id": "v19/x/y"}}])

    def test_merge_deprecates_and_repoints(self, recs):
        out, _ = apply_ops(recs, [{"op": "merge", "into": "v19/entity-name/sink", "from": ["v19/entity-name/resource_sink"],
                                   "notes": "same resource", "suggestions": ["1-2#S1"]}])
        old = by_symbol(out, "resource_sink")
        assert old["status"] == "Deprecated" and old["superseded_by"] == ["v19/entity-name/sink"]
        assert "resource sink" in by_symbol(out, "sink")["aliases"]
        assert validate(out, previous=recs) == []

    def test_split_adds_and_deprecates(self, recs):
        a = {"id": "v19/capacity-unit-value/cap_gb_decimal", "symbol": "cap_gb_decimal", "kind": "value",
             "category": "capacity-unit-value", "definition": "10^9 bytes."}
        b = {"id": "v19/capacity-unit-value/cap_gib", "symbol": "cap_gib", "kind": "value",
             "category": "capacity-unit-value", "definition": "2^30 bytes."}
        out, _ = apply_ops(recs, [{"op": "split", "id": "v19/capacity-unit-value/cap_gb", "into": [a, b],
                                   "notes": "decimal vs binary", "suggestions": ["1-3#S1"]}])
        assert by_symbol(out, "cap_gb")["superseded_by"] == [a["id"], b["id"]]
        assert validate(out, previous=recs) == []

    def test_reject_changes_nothing(self, recs):
        out, report = apply_ops(recs, [{"op": "reject", "suggestions": ["1-4#S1"], "reason": "exists"}])
        assert out == recs and report[0]["op"] == "reject"

    def test_unknown_op_and_missing_target_raise(self, recs):
        with pytest.raises(OpError):
            apply_ops(recs, [{"op": "rename"}])
        with pytest.raises(OpError):
            apply_ops(recs, [{"op": "deprecate", "id": "v19/nope/nothing", "reason": "x"}])


class TestValidate:
    def test_removed_record_is_an_error(self, recs):
        shorter = [r for r in recs if r["symbol"] != "mug"]
        assert any("was removed" in e for e in validate(shorter, previous=recs))

    def test_dangling_dependency_is_an_error(self, recs):
        by_symbol(recs, "mug")["dependencies"] = ["v19/nope/missing"]
        assert any("does not resolve" in e for e in validate(recs))

    def test_cycle_is_an_error(self, recs):
        a, b = by_symbol(recs, "constraint_realistic"), by_symbol(recs, "requirement")
        b["dependencies"] = [a["id"]]
        assert any("cycle" in e for e in validate(recs))

    def test_duplicate_symbol_is_an_error(self, recs):
        dup = copy.deepcopy(by_symbol(recs, "mug"))
        dup["id"] = "v19/entity-name/mug2"
        recs.append(dup)
        assert any("duplicate symbol" in e for e in validate(recs))

    def test_composite_without_expansion_is_an_error(self, recs):
        by_symbol(recs, "constraint_realistic")["expansion"] = ""
        assert any("requires an expansion" in e for e in validate(recs))

    def test_shared_rule_must_be_a_rule(self, recs):
        by_symbol(recs, "mug")["shared_rules"] = ["v19/entity-name/sink"]
        assert any("not a rule" in e for e in validate(recs))


def test_rendered_header_has_no_shell_commands(recs):
    # glossary.md is attached to model requests; the proxy's firewall blocks bodies containing
    # "run `<command>`" as suspected command injection (it 403-ed every drafter in batch 2).
    head = render.render_md(recs, "x").split("## ", 1)[0]
    assert "python -m" not in head and "run `" not in head
