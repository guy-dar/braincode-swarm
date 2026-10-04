"""Value groups (spec §3.1, the lexical-groups release): the group contract,
the retire op, the markdown round trip, retrieval (catalog, slots, group
tags) and the host check of `group::key` atoms."""
import copy
import json
import re
from pathlib import Path

import pytest

from glossary import groups, import_md, records, render, schema
from glossary.records import OpError, apply_ops, validate
from rag import needs as needs_mod
from rag.retrieve import Retriever, render_check, render_context

SWARM = Path(__file__).resolve().parent.parent


@pytest.fixture(scope="module")
def live():
    return records.load()


@pytest.fixture
def recs(live):
    return copy.deepcopy(live)


@pytest.fixture(scope="module")
def retriever(tmp_path_factory):
    return Retriever(dense=False, use_llm=False, index_dir=tmp_path_factory.mktemp("index"))


def group_record(**group):
    return {"id": "v19/lexical-group/plant_label", "version": 1, "symbol": "plant_label", "kind": "lexical_group",
            "status": "Accepted", "definition": "A source-supplied plant-kind label.", "group": group}


# ---------------------------------------------------------------------- glossary

class TestInstalledRelease:
    def test_groups_present_and_no_leaf_rows(self, live):
        gs = groups.groups_by_symbol(live)
        assert set(gs) == {"object_label", "food_label", "animal_label", "color_label", "genre_label", "platform_label",
                           "country", "currency"}
        assert groups.contract(gs["object_label"])["admission"] == "open_label"
        for sym, std in (("country", "iso3166-1-alpha2"), ("currency", "iso4217")):
            c = groups.contract(gs[sym])
            assert (c["admission"], c["standard"], c["members"]) == ("standard", std, {})
        symbols = {r["symbol"] for r in live}
        assert not {"pillow", "curr_zar", "japan", "color_red", "genre_comedy"} & symbols
        assert validate(live) == []

    def test_atom_signatures_depend_on_their_groups(self, live):
        pick_up = next(r for r in live if r["symbol"] == "pick_up")
        assert "v19/lexical-group/object_label" in pick_up["dependencies"]
        assert ("pick_up", "target") in groups.consumers(live)["object_label"]

    def test_standard_code_lists_are_bundled(self):
        assert groups.standard_codes("iso4217")["ZAR"]
        assert groups.standard_codes("iso3166-1-alpha2")["JP"] == "Japan"


class TestContract:
    def test_valid_open_group(self):
        assert groups.contract_errors(group_record(examples=["plant_label::fern"])) == []

    @pytest.mark.parametrize("group, fragment", [
        ({"examples": ["plant_label::fern"], "members": {"fern": {"sense_id": "x", "definition": "d"}}}, "no members"),
        ({"examples": ["plant_label::Fern"]}, "does not match lower_word"),
        ({"examples": []}, "1-3 illustrative examples"),
        ({"examples": ["plant_label::fern"], "key_aliases": {"ferns": "fern", "fernz": "ferns"}}, "no chains"),
        ({"admission": "standard", "key_form": "upper_code", "examples": ["plant_label::AB"]}, "names its `standard`"),
        ({"admission": "standard", "standard": "iso9999", "key_form": "upper_code", "examples": ["plant_label::AB"]},
         "no bundled code list"),
        ({"examples": ["plant_label::fern"], "colour": "x"}, "unknown group field"),
    ])
    def test_contract_errors(self, group, fragment):
        errors = groups.contract_errors(group_record(**group))
        assert any(fragment in e for e in errors), errors

    def test_schema_routes_groups_through_the_contract(self):
        rec = group_record(examples=["plant_label::Fern"])
        assert any("lower_word" in e for e in schema.record_errors(rec))
        assert schema.derive_id({"symbol": "plant_label", "kind": "lexical_group"}) == "v19/lexical-group/plant_label"

    def test_atom_checks(self, live):
        gs = groups.groups_by_symbol(live)
        assert groups.check_atom(gs, "object_label", "thimble")[0] == "ok"
        assert groups.check_atom(gs, "currency", "ZAR")[0] == "ok"
        assert groups.check_atom(gs, "currency", "ZZZ")[0] == "not_in_standard"
        assert groups.check_atom(gs, "color_label", "Red")[0] == "bad_key"
        assert groups.check_atom(gs, "colour", "red")[0] == "unknown_group"
        assert groups.check_atom(gs, "color_label", "gray") == ("alias", "color_label::gray: write the canonical "
                                                                         "color_label::grey")


class TestRetireAndValidate:
    def test_retire_removes_and_validates_with_retired(self, recs):
        target = next(r for r in recs if r["kind"] == "value" and not any(
            r["id"] in (o.get("dependencies") or []) + (o.get("related") or []) for o in recs))
        new, report = apply_ops(recs, [{"op": "retire", "id": target["id"], "reason": "a group covers it",
                                        "replacement": "object_label::x"}])
        assert target["id"] not in {r["id"] for r in new}
        assert report[0]["op"] == "retire" and "object_label::x" in report[0]["outcome"]
        assert validate(new, previous=recs) != []   # a plain removal is still an error
        assert validate(new, previous=recs, retired=records.retired_ids(report)) == []

    def test_retire_blocked_while_referenced(self, recs):
        pick_up = next(r for r in recs if r["symbol"] == "pick_up")
        dep = pick_up["dependencies"][0]
        with pytest.raises(OpError, match="still referenced"):
            apply_ops(recs, [{"op": "retire", "id": dep, "reason": "x"}])

    def test_standard_group_cannot_change_standard(self, recs):
        new, _ = apply_ops(recs, [{"op": "update", "id": "v19/lexical-group/currency",
                                   "set": {"group": {"admission": "standard", "standard": "iso3166-1-alpha2",
                                                     "key_form": "upper_code", "examples": ["currency::JP"]}}}])
        assert any("needs a migration" in e for e in validate(new, previous=recs))


class TestMarkdown:
    def test_round_trip_keeps_group_contracts(self, recs):
        rows = import_md.parse_md(render.render_md(recs, "x"))
        merged, changed = import_md.merge_edits(recs, rows)
        assert changed == []
        food = next(r for r in merged if r["symbol"] == "food_label")
        assert food["group"]["key_aliases"]["spud"] == "potato" and food["group"]["recognition"]

    def test_compact_line_shows_contract_and_slots(self, live):
        cur = next(r for r in live if r["symbol"] == "currency")
        line = render.compact_line(cur, [("measure", "unit")])
        assert "ISO 4217" in line and "currency::USD" in line and "measure.unit" in line


@pytest.mark.parametrize("path", [
    "reference/language-spec.compact.md", "reference/glossary.md", "kit/README.md", "kit/needs_prompt.md",
    "tasks/translator.md", "doc_formats/successful_translation.md", "doc_formats/failed_translation.md",
    "doc_formats/suggestions.md",
])
def test_attached_files_have_no_run_command_pattern(path):
    # Model-facing files: the proxy's firewall blocked request bodies containing "run `python -m …`"
    # (it 403-ed every drafter in batch 2). `node /kit/rag.mjs` commands have been sent in every
    # translator request since batch 3 without a block, so only interpreter/shell commands are banned.
    text = (SWARM / path).read_text(encoding="utf-8")
    assert not re.search(r"\brun\s+`(python|py |pip|bash|sh |curl|wget|powershell)", text, re.I), path
    assert "python -m" not in text, path


# ---------------------------------------------------------------------- retrieval

class TestRetrieval:
    NEEDS = [{"kind": "action", "text": "pick up the thimble", "source": ["t1:s1"]},
             {"kind": "object", "text": "a thimble", "source": ["t1:s1"], "group": "object_label"}]

    def test_catalog_slots_and_group_tag(self, retriever):
        res = retriever.retrieve("<|user|>Pick up the thimble.", needs=copy.deepcopy(self.NEEDS))
        ctx = render_context(res, retriever, "g")
        catalog = ctx.split("## Value groups (all of them)", 1)[1].split("##", 1)[0]
        for g in ("object_label", "food_label", "animal_label", "color_label", "genre_label", "platform_label", "country",
                  "currency"):
            assert f"`{g}::<key>`" in catalog
        assert {"symbol": "pick_up", "param": "target", "groups": ["object_label", "food_label"]} in res["slots"]
        assert "pick_up.target → object_label, food_label" in ctx
        tagged = res["needs"][1]["candidates"][0]
        assert tagged["symbol"] == "object_label" and "group-tag" in tagged["reasons"]
        assert "→ `object_label::<key>`" in ctx

    def test_catalog_present_even_without_group_needs(self, retriever):
        res = retriever.retrieve("<|user|>Say hello.", needs=[{"kind": "speech_act", "text": "greet the user",
                                                               "source": ["t1:s1"]}])
        assert "`currency::<key>`" in render_context(res, retriever, "g")

    def test_widen_offers_groups_of_accepting_slots(self, retriever):
        out = retriever.widen("pick up the thimble from the shelf", kind="action")
        reasons = {c["symbol"]: c["reasons"] for c in out["candidates"]}
        assert "object_label" in reasons

    def test_entry_resolves_atoms(self, retriever):
        assert retriever.entry("currency::ZAR")["atom"]["status"] == "ok"
        assert retriever.entry("country::XX")["atom"]["status"] == "not_in_standard"
        assert retriever.entry("object_label")["slots"]

    def test_needs_parse_keeps_known_group_only(self, monkeypatch):
        reply = json.dumps({"needs": [{"kind": "object", "text": "a pear", "source": "t1:s1", "group": "food_label"},
                                      {"kind": "object", "text": "a fern", "source": "t1:s1", "group": "plant_label"},
                                      {"kind": "object", "text": "rand", "source": "t1:s1", "group": "`currency::ZAR`"}]})

        class Msg:
            content = reply

        class Choice:
            message = Msg()

        class Resp:
            choices = [Choice()]

        import litellm
        monkeypatch.setattr(litellm, "completion", lambda **kw: Resp())
        monkeypatch.setattr(needs_mod, "_llm_settings", lambda: ("m", "key", "http://x"))
        out = needs_mod.llm_needs(needs_mod.segment("A pear, a fern and rand."))
        assert [n.get("group") for n in out] == ["food_label", None, "currency"]


class TestCheck:
    TRANSLATION = """```braincode
MODE REQUEST
ENTRYPOINT ObjectLabelThimble
TASK ObjectLabelThimble {
  ACTION pick_up(target=object_label::thimble, source=pillow, color=color_label::gray) -> object_label_thimble_ref : REF[STRING]
  TERM measure(amount=5, unit=currency::ZAR) -> m : TERM
  TERM measure(amount=5, unit=currency::ZZZ) -> m2 : TERM
  LET fish = colour::red
  LET broken = currency:: + ::x
}
```"""

    def test_atoms_retired_and_label_preserved(self, retriever):
        needs = [{"id": "n1", "kind": "object", "text": "a thimble", "group": "object_label",
                  "candidates": [{"symbol": "object_label"}]},
                 {"id": "n2", "kind": "constraint", "text": "price in rand", "group": "currency",
                  "candidates": [{"symbol": "currency"}]}]
        rep = retriever.check(self.TRANSLATION, needs)
        assert any("currency::ZZZ" in e for e in rep["atom_errors"])
        assert any("colour::red" in e for e in rep["atom_errors"])
        assert not any("ZAR" in e or "thimble" in e for e in rep["atom_errors"])
        assert any("grey" in w for w in rep["atom_warnings"])
        assert rep["retired_symbols_used"] == ["pillow (write object_label::pillow)"]   # `fish` is a bound name
        assert rep["label_preserved"] == ["n1"]
        assert [n["status"] for n in rep["needs"]] == ["label-preserved", "covered"]
        text = render_check(rep)
        assert "[LABEL] n1" in text and "Invalid value-group atoms" in text

    def test_success_gate_blocks_hard_atom_errors_only(self, retriever):
        from translate_batch import success_gate_problems
        rep = retriever.check(self.TRANSLATION, [])
        problems = success_gate_problems(rep)
        assert any("invalid value-group atoms" in p for p in problems)
        assert any("retired bare symbols" in p for p in problems)
        ok = retriever.check("```braincode\nMODE REQUEST\nENTRYPOINT A\nTASK A {\n"
                             "  ACTION pick_up(target=object_label::cup, color=color_label::gray) -> r : REF[STRING]\n"
                             "}\n```", [])
        assert success_gate_problems(ok) == []   # a non-canonical alias is only advisory


def test_quoted_double_colon_is_not_an_atom(retriever):
    rep = retriever.check('```braincode\nMODE REQUEST\nENTRYPOINT A\nTASK A {\n'
                          '  LET lib : STRING = "cpprestsdk::cpprest"\n}\n```', [])
    assert rep["atom_errors"] == []


def test_consolidation_folds_a_family_into_a_group(recs):
    from glossary import consolidate
    spec = {"group": {"symbol": "zz_tool_label", "definition": "A source-supplied tool name.",
                      "group": {"key_form": "lower_identifier", "examples": ["zz_tool_label::hammer"]}},
            "slots": {"pick_up": ["target"]},
            "retire": {}}
    vals = [r for r in recs if r["kind"] == "value" and not any(
        r["id"] in (o.get("dependencies") or []) + (o.get("related") or []) + (o.get("mentions") or []) for o in recs)][:2]
    spec["retire"] = {v["symbol"]: None for v in vals}
    new, report, retired = consolidate.build(spec, recs)
    assert validate(new, previous=recs, retired=records.retired_ids(report)) == []
    assert "ATOM[zz_tool_label]" in next(r for r in new if r["symbol"] == "pick_up")["signature"]
    assert set(retired) == {v["symbol"] for v in vals}
    assert all(e["replacement"].startswith("zz_tool_label::") for e in retired.values())


def test_rewrite_text_keeps_literals_and_argument_names():
    from glossary import consolidate
    out = consolidate.rewrite_text('run_tests(target=sklearn, django="django") django', {"sklearn": "scikit_learn",
                                                                                         "django": "django"}, "p")
    assert out == 'run_tests(target=p::scikit_learn, django="django") p::django'
