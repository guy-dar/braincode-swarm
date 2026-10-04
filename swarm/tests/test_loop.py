"""Plan sampling, translator ids, the suggestion contract, output
validation/routing documents, and the inspector."""
import csv
import json

import pytest

import inspector
import loop
import loop_files as lf
from translate_batch import validate_output


@pytest.fixture
def loop_dirs(tmp_path, monkeypatch):
    """Point every loop path at a temp tree."""
    for name, rel in (("TRANSLATIONS_DIR", "translations"), ("SUCCESS_DIR", "translations/successful"),
                      ("FAILED_DIR", "translations/failed"), ("SUGGESTIONS_DIR", "translator_suggestions"),
                      ("COUNTS_CSV", "translator_suggestions/suggestion_counts.csv"), ("RUNS_DIR", "runs"),
                      ("PLAN_PATH", "runs/plan.jsonl")):
        monkeypatch.setattr(lf, name, tmp_path / rel)
    return tmp_path


def make_data(root, sizes):
    for ds, n in sizes.items():
        d = root / ds
        d.mkdir(parents=True)
        (d / "train.jsonl").write_text("".join(json.dumps({"id": f"{ds}-{i}", "content": f"<|user|>item {i}"}) + "\n"
                                               for i in range(n)), encoding="utf-8")


class TestPlan:
    def test_per_dataset_sample_with_fallback(self, tmp_path):
        make_data(tmp_path, {"a": 50, "b": 7})
        rows, summary = loop.build_plan(10, 4, 1, data_dir=tmp_path, datasets=("a", "b"))
        taken = {s["dataset"]: s["taken"] for s in summary}
        assert taken == {"a": 10, "b": 7}
        assert "fallback" in next(s for s in summary if s["dataset"] == "b")["note"]
        assert len(rows) == 17

    def test_translator_ids_are_batch_dash_tnum(self, tmp_path):
        make_data(tmp_path, {"a": 9})
        rows, _ = loop.build_plan(9, 4, 1, data_dir=tmp_path, datasets=("a",))
        # 9 items, batches of at most 4 -> 3 batches, dealt evenly (3 each).
        assert [r["translator_id"] for r in rows] == ["1-1", "1-2", "1-3", "2-1", "2-2", "2-3", "3-1", "3-2", "3-3"]
        assert all(r["translator_id"] == f"{r['batch_id']}-{r['tnum']}" for r in rows)

    def test_every_batch_has_the_same_count_per_dataset(self, tmp_path):
        from collections import Counter
        make_data(tmp_path, {"a": 50, "b": 50, "c": 50})
        rows, _ = loop.build_plan(20, 6, 3, data_dir=tmp_path, datasets=("a", "b", "c"))
        batches = lf.plan_batches(rows)
        assert len(batches) == 10
        assert all(Counter(r["dataset"] for r in b) == {"a": 2, "b": 2, "c": 2} for b in batches.values())

    def test_short_dataset_is_spread_evenly(self, tmp_path):
        from collections import Counter
        make_data(tmp_path, {"a": 50, "b": 5})
        rows, _ = loop.build_plan(20, 5, 3, data_dir=tmp_path, datasets=("a", "b"))
        per_batch_b = [Counter(r["dataset"] for r in b)["b"] for b in lf.plan_batches(rows).values()]
        assert sum(per_batch_b) == 5 and max(per_batch_b) - min(per_batch_b) <= 1

    def test_sampling_is_seeded_and_unique(self, tmp_path):
        make_data(tmp_path, {"a": 100})
        r1, _ = loop.build_plan(30, 30, 7, data_dir=tmp_path, datasets=("a",))
        r2, _ = loop.build_plan(30, 30, 7, data_dir=tmp_path, datasets=("a",))
        assert [r["record_line"] for r in r1] == [r["record_line"] for r in r2]
        assert len({r["record_line"] for r in r1}) == 30


class TestIds:
    def test_batch_file_pattern_does_not_cross_batches(self):
        pattern = lf.batch_file_re(1)
        assert pattern.match("1-12.md") and not pattern.match("10-12.md") and not pattern.match("1-x.md")

    def test_parse_translator_id(self):
        assert lf.parse_translator_id("7-23") == (7, 23)
        assert lf.parse_translator_id("7_23") is None


GOOD_SUGGESTIONS = """### S1 | type: add | dimension: constructor | symbol: group_size
- Needs: n2
### S2 | type: refine | dimension: refine-entry | target: v19/composite/constraint_17_plus
- Before: x
"""


class TestSuggestionContract:
    def test_parse(self):
        parsed = lf.parse_suggestions(GOOD_SUGGESTIONS)
        assert [(s["type"], s["dimension"], s["value"]) for s in parsed] == [
            ("add", "constructor", "group_size"), ("refine", "refine-entry", "v19/composite/constraint_17_plus")]
        assert lf.suggestion_problems(GOOD_SUGGESTIONS) == []

    def test_wrong_dimension_for_type(self):
        text = "### S1 | type: add | dimension: refine-entry | symbol: x\n"
        assert any("not valid for type add" in p for p in lf.suggestion_problems(text))

    def test_malformed_heading_is_flagged(self):
        text = GOOD_SUGGESTIONS + "### S3 type add vocabulary-member foo\n"
        assert any("malformed" in p for p in lf.suggestion_problems(text))

    def test_empty_is_flagged(self):
        assert lf.suggestion_problems("no suggestions here")


class TestValidateOutput:
    def write(self, d, translation=None, suggestions=None):
        if translation is not None:
            (d / "translation.md").write_text(translation, encoding="utf-8")
        if suggestions is not None:
            (d / "suggestions.md").write_text(suggestions, encoding="utf-8")

    def test_success(self, tmp_path):
        self.write(tmp_path, "Status: success\n```braincode\nMODE REQUEST\n```\n")
        assert validate_output(tmp_path)[0::3] == ("success", None)

    def test_failed_requires_suggestions(self, tmp_path):
        self.write(tmp_path, "Status: failed\n```braincode\nMODE TRACE\n```\n")
        assert "without" in validate_output(tmp_path)[3]
        self.write(tmp_path, suggestions=GOOD_SUGGESTIONS)
        assert validate_output(tmp_path)[3] is None

    def test_missing_status_and_file(self, tmp_path):
        assert "no /output/translation.md" in validate_output(tmp_path)[3]
        self.write(tmp_path, "Here is my translation\n```braincode\n```\n")
        assert "Status" in validate_output(tmp_path)[3]


class TestCompose:
    META = {"translator_id": "3-4", "batch_id": 3, "dataset": "prism", "item_id": "prism-c1", "status": "failed",
            "glossary_version": "19.0.0-draft.1+g2", "glossary_sha": "ab" * 32, "model": "m", "needs_count": 5,
            "needs_method": "llm"}

    def test_translation_doc_has_header_item_and_body(self):
        doc = lf.compose_translation(self.META, "t1:s1 [USER] ```code```", "Status: failed\nbody")
        assert doc.startswith("# Translation 3-4 — failed")
        assert "- Dataset: prism" in doc and "````text" in doc and doc.rstrip().endswith("body")

    def test_suggestions_header_is_parseable(self):
        doc = lf.compose_suggestions(self.META, GOOD_SUGGESTIONS)
        assert lf.header_field(doc, "Dataset") == "prism"
        assert len(lf.parse_suggestions(doc)) == 2


def write_suggestion(tid, dataset, body):
    meta = dict(TestCompose.META, translator_id=tid, dataset=dataset)
    lf.SUGGESTIONS_DIR.mkdir(parents=True, exist_ok=True)
    lf.suggestions_path(tid).write_text(lf.compose_suggestions(meta, body), encoding="utf-8")
    path = lf.failed_path(dataset, tid)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("x", encoding="utf-8")


def plan_rows(batch, datasets):
    return [{"translator_id": f"{batch}-{i}", "batch_id": batch, "tnum": i, "dataset": ds}
            for i, ds in enumerate(datasets, 1)]


class TestInspector:
    def test_counts_by_type_and_dataset_and_ignores_other_batches(self, loop_dirs):
        rows = plan_rows(1, ["prism", "alfred", "alfred"])
        write_suggestion("1-1", "prism", GOOD_SUGGESTIONS)
        write_suggestion("1-2", "alfred", "### S1 | type: add | dimension: vocabulary-member | symbol: sponge\n")
        write_suggestion("10-1", "alfred", GOOD_SUGGESTIONS)   # another batch: must not count
        s = lf.success_path("alfred", "1-3")
        s.parent.mkdir(parents=True, exist_ok=True)
        s.write_text("x")
        row = inspector.count_batch(1, rows)
        assert (row["add_total"], row["refine_total"]) == (2, 1)
        assert (row["add_prism"], row["refine_prism"], row["add_alfred"]) == (1, 1, 1)
        assert (row["translators_finished"], row["failed_translations"], row["successful_translations"]) == (3, 2, 1)

    def test_stop_rule_thresholds_are_inclusive(self):
        base = {"translators_planned": 30, "translators_finished": 30}
        assert inspector.decide({**base, "add_total": 2, "refine_total": 5})[0] == "stop"
        assert inspector.decide({**base, "add_total": 3, "refine_total": 0})[0] == "continue"
        assert inspector.decide({**base, "add_total": 0, "refine_total": 6})[0] == "continue"

    def test_completion_guard_blocks_stop(self):
        decision, reason = inspector.decide({"translators_planned": 30, "translators_finished": 20,
                                             "add_total": 0, "refine_total": 0})
        assert decision == "continue" and "20/30" in reason

    def test_csv_upserts_one_row_per_batch(self, loop_dirs):
        rows = plan_rows(1, ["prism"])
        inspector.inspect(1, rows, log=lambda m: None)
        inspector.inspect(1, rows, log=lambda m: None)
        inspector.inspect(2, plan_rows(2, ["prism"]), log=lambda m: None)
        with lf.COUNTS_CSV.open(encoding="utf-8") as fh:
            data = list(csv.DictReader(fh))
        assert [d["batch"] for d in data] == ["1", "2"]
        assert {"add_prism", "refine_thoughttrace", "decision"} <= set(data[0])


class TestDockerCmd:
    def test_extra_mounts_are_read_only_and_output_stays_the_only_writable(self):
        import utils
        cmd = utils.build_docker_cmd(None, None, "m", "/ref", "/t.txt", "/p.md", "/scratch", "img",
                                     extra_mounts=[("/kit", "/kit")], extra_env={"TRANSLATOR_ID": "1-2"},
                                     add_host=True)
        mounts = [cmd[i + 1] for i, a in enumerate(cmd) if a == "-v"]
        assert "/kit:/kit:ro" in mounts
        assert [m for m in mounts if not m.endswith(":ro")] == ["/scratch:/output"]
        assert "--user" not in cmd
        assert "host.docker.internal:host-gateway" in cmd
        assert "TRANSLATOR_ID=1-2" in cmd and cmd[-1] == "img"


class TestMigratorEvaluate:
    REFS = [{"ref": "C#S1", "type": "add"}, {"ref": "C#S2", "type": "refine"}]

    def run(self, ops, hints=None):
        import migrate
        from glossary import records
        return migrate.evaluate_ops(ops, records.load(), self.REFS, batch_id=1, hints=hints)

    def add_op(self):
        return {"op": "add", "suggestions": ["C#S1"], "record": {
            "symbol": "group_size", "kind": "constructor",
            "signature": "TERM group_size(group: STRING, count: NUMBER) -> TERM", "definition": "Group size."}}

    def test_valid_ops_and_hints(self):
        result = self.run([self.add_op(), {"op": "reject", "suggestions": ["C#S2"], "reason": "fine as is"}],
                          hints={"aliases": {"v19/support/group_size": ["how many"]},
                                 "related": {"v19/support/group_size": ["v19/support/requirement"]}})
        assert result["ok"] and not result["soft"]
        rec = next(r for r in result["new_records"] if r["symbol"] == "group_size")
        assert rec["aliases"] == ["how many"] and rec["related"] == ["v19/support/requirement"]
        assert rec["shared_rules"] == ["v19/rule/support-primitives-general"]

    def test_unaddressed_suggestion_is_soft(self):
        result = self.run([self.add_op()])
        assert result["ok"] and "C#S2" in result["soft"][0]

    def test_invalid_record_is_an_error(self):
        bad = self.add_op()
        bad["record"]["signature"] = ""
        result = self.run([bad])
        assert not result["ok"] and any("requires a signature" in e for e in result["errors"])

    def test_removal_is_impossible_through_ops(self):
        result = self.run([{"op": "delete", "id": "v19/entity-name/mug"}])
        assert not result["ok"] and any("unknown op" in e for e in result["errors"])


class TestReview:
    def test_assemble_applies_decisions_and_keeps_unreviewed(self):
        import migrate
        numbered = {"D1": {"op": "add", "suggestions": ["C#S1"], "record": {"symbol": "a"}},
                    "D2": {"op": "add", "suggestions": ["C#S2"], "record": {"symbol": "b"}},
                    "D3": {"op": "reject", "suggestions": ["C#S3"], "reason": "x"},
                    "D4": {"op": "reject", "suggestions": ["C#S4"], "reason": "y"}}
        review = "\n".join(json.dumps(d) for d in [
            {"draft": "D1", "decision": "approve", "reason": "ok"},
            {"draft": "D2", "decision": "replace", "op": {"op": "add", "suggestions": ["C#S2"], "record": {"symbol": "b2"}},
             "reason": "rename"},
            {"draft": "D3", "decision": "drop", "reason": "dup"},
            {"decision": "add", "op": {"op": "reject", "suggestions": ["C#S5"], "reason": "z"}, "reason": "missing"},
            {"draft": "D9", "decision": "approve"}])
        final, rows, errors = migrate.assemble(review, numbered)
        assert [o.get("record", {}).get("symbol") or o["suggestions"][0] for o in final] == ["a", "b2", "C#S5", "C#S4"]
        assert any("unknown draft D9" in e for e in errors)
        assert "kept D4 (not reviewed)" in [r[1] for r in rows]

    def test_drafts_document_notes_validation(self):
        import migrate
        from glossary import records
        drafts = [{"drafter": "D1", "status": "drafted", "ops": [
            {"op": "add", "suggestions": ["C#S1"], "record": {"symbol": "mug", "kind": "value", "category": "entity-name",
                                                             "definition": "dup"}}]}]
        numbered, text = migrate.drafts_document(drafts, records.load())
        assert list(numbered) == ["D1"] and "## C#S1" in text and "add of existing id" in text

    def test_c_refs_chain_back_to_translators(self):
        import migrate
        m = migrate.source_map({"M1": MERGED_OK})
        c = migrate.source_map({"C": "### S1 | type: add | dimension: constructor | symbol: g\n- Sources: M1#S1\n"})
        assert migrate.chain_sources(c, m) == {"C#S1": ["1-1#S1", "1-2#S1"]}


def test_unclosed_braincode_block_is_malformed(tmp_path):
    (tmp_path / "translation.md").write_text("Status: success\n```braincode\nMODE REQUEST\n\n## Needs coverage\n")
    assert "never closed" in validate_output(tmp_path)[3]


class TestStratifiedSample:
    def test_sample_keeps_the_feature_mix(self):
        import random
        lines = ([json.dumps({"k": "big"})] * 600 + [json.dumps({"k": "mid"})] * 300
                 + [json.dumps({"k": "small"})] * 100)
        chosen = loop.stratified_sample(lines, 50, "k", random.Random(1))
        counts = {s: sum(json.loads(l)["k"] == s for l in chosen) for s in ("big", "mid", "small")}
        assert counts == {"big": 30, "mid": 15, "small": 5}

    def test_consecutive_items_cycle_strata(self):
        import random
        lines = [json.dumps({"k": s, "i": i}) for s in "abc" for i in range(10)]
        order = [json.loads(l)["k"] for l in loop.interleave_strata(lines, "k", random.Random(2))]
        assert all(len(set(order[i:i + 3])) >= 2 for i in range(0, 30, 3))


class TestSuccessGate:
    def test_clean_report_passes(self):
        from translate_batch import success_gate_problems
        assert success_gate_problems({"unresolved": [], "unknown_symbols_in_head_position": [],
                                      "claimed_but_absent": {}, "string_literals_as_operation_arguments": ['x="y"']}) == []

    def test_unresolved_invented_and_claimed_absent_fail(self):
        from translate_batch import success_gate_problems
        problems = success_gate_problems({"unresolved": ["n1", "n2"], "unknown_symbols_in_head_position": ["foo"],
                                          "claimed_but_absent": {"right_of": ["n3"]}})
        assert len(problems) == 3 and "n1" in problems[0]

    def test_proxy_errors_are_recognised(self):
        from translate_batch import is_proxy_error
        assert is_proxy_error("HTTP 429 (Cloudflare challenge)") and is_proxy_error("HTTP 503")
        assert not is_proxy_error("timed out after 1200s and was killed.") and not is_proxy_error("")


MERGED_OK = """# Merged suggestions M1 — batch 1

- Group: M1
- Source files: 1-1, 1-2

### S1 | type: add | dimension: constructor | symbol: group_size
- Sources: 1-1#S1, 1-2#S1
- Merge notes: same concept

## Not carried forward

| source | reason |
|---|---|
| 1-2#S2 | duplicate |
"""


class TestTwoStageMigration:
    def test_groups_are_at_most_five_of_at_most_six(self, loop_dirs):
        import migrate
        lf.SUGGESTIONS_DIR.mkdir(parents=True)
        for i in range(1, 26):
            write_suggestion(f"1-{i}", lf.DATASETS[i % 6], GOOD_SUGGESTIONS)
        groups = migrate.group_files(lf.batch_suggestion_files(1))
        assert len(groups) == 5 and max(map(len, groups)) <= 6 and sum(map(len, groups)) == 25
        assert len(migrate.group_files(lf.batch_suggestion_files(1)[:7])) == 2

    def test_accounting_accepts_merged_and_dropped(self):
        import migrate
        assert migrate.accounting_problems(MERGED_OK, ["1-1#S1", "1-2#S1", "1-2#S2"]) == []

    def test_accounting_flags_missing_and_unknown(self):
        import migrate
        problems = migrate.accounting_problems(MERGED_OK, ["1-1#S1", "1-2#S1", "1-2#S2", "1-3#S1"])
        assert any("1-3#S1" in p and "not accounted" in p for p in problems)
        problems = migrate.accounting_problems(MERGED_OK.replace("1-1#S1", "9-9#S9"), ["1-1#S1", "1-2#S1", "1-2#S2"])
        assert any("unknown source 9-9#S9" in p for p in problems)

    def test_passthrough_keeps_every_suggestion(self, loop_dirs):
        import migrate
        write_suggestion("1-1", "prism", GOOD_SUGGESTIONS)
        path = lf.batch_suggestion_files(1)[0]
        blocks = [(f"{path.stem}#S{b['n']}", b) for b in migrate.blocks_of(path.read_text(encoding="utf-8"))]
        text = migrate.passthrough("# Merged suggestions M1 — batch 1", blocks)
        assert migrate.accounting_problems(text, ["1-1#S1", "1-1#S2"]) == []

    def test_provenance_maps_refs_to_translators(self):
        import migrate
        from glossary import records
        sources = migrate.source_map({"M1": MERGED_OK})
        op = {"op": "add", "suggestions": ["M1#S1"], "record": {
            "symbol": "group_size", "kind": "constructor",
            "signature": "TERM group_size(count: NUMBER) -> TERM", "definition": "Group size."}}
        result = migrate.evaluate_ops([op], records.load(), [{"ref": "M1#S1", "type": "add"}], 1, sources=sources)
        assert result["ok"] and not result["soft"]
        entry = next(e for e in result["report"] if e["target"] == "v19/support/group_size")
        assert entry["translator_ids"] == ["1-1", "1-2"]


class TestSpeedups:
    def test_attachments_are_built_in_order(self, tmp_path):
        import translate_batch
        ref = tmp_path / "ref"
        ref.mkdir()
        (ref / "language-spec.compact.md").write_text("spec")
        (tmp_path / "rag_context.md").write_text("ctx")
        out = translate_batch.build_attachments(tmp_path / "attach", ref, tmp_path)
        names = sorted(p.name for p in out.iterdir())
        assert names[:2] == ["1-language-spec.md", "2-rag_context.md"] and len(names) == 6

    def test_needs_cache_round_trip_and_content_check(self, loop_dirs, monkeypatch):
        import translate_batch
        from rag import needs as needs_mod
        monkeypatch.setattr(translate_batch, "NEEDS_CACHE_DIR", loop_dirs / "runs" / "needs_cache")
        calls = []
        monkeypatch.setattr(needs_mod, "extract_needs",
                            lambda content, use_llm=True: calls.append(content) or
                            ([], [{"id": "n1", "kind": "action", "text": "x", "source": ["t1:s1"], "context": "c"}], "llm"))
        row = {"translator_id": "2-1", "batch_id": 2, "tnum": 1, "dataset": "alfred",
               "record_line": json.dumps({"id": "a", "content": "<|user|>Put the mug in the sink."})}
        assert translate_batch.prefetch_needs([row], workers=1)["cached"] == 1
        cached = translate_batch.load_cached_needs("2-1", "<|user|>Put the mug in the sink.")
        assert cached["method"] == "llm" and cached["needs"] == [{"kind": "action", "text": "x", "source": ["t1:s1"]}]
        assert translate_batch.load_cached_needs("2-1", "different item") is None
        assert translate_batch.prefetch_needs([row], workers=1)["skipped"] == 1 and len(calls) == 1

    def test_heuristic_fallback_is_not_cached(self, loop_dirs, monkeypatch):
        import translate_batch
        from rag import needs as needs_mod
        monkeypatch.setattr(translate_batch, "NEEDS_CACHE_DIR", loop_dirs / "runs" / "needs_cache")
        monkeypatch.setattr(needs_mod, "extract_needs", lambda content, use_llm=True: ([], [{"text": "x"}], "heuristic"))
        row = {"translator_id": "2-2", "batch_id": 2, "tnum": 2, "dataset": "alfred",
               "record_line": json.dumps({"id": "b", "content": "hi"})}
        assert translate_batch.prefetch_needs([row], workers=1)["fallback"] == 1
        assert translate_batch.load_cached_needs("2-2", "hi") is None

    def test_compact_spec_keeps_rules_and_drops_history(self):
        import spec_compact
        src = (lf.REFERENCE_DIR / "language-spec.md").read_text(encoding="utf-8")
        out = spec_compact.build(src)
        assert "v18" not in out and "## 17." not in out
        for heading in [l for l in src.replace("\r\n", "\n").splitlines() if l.startswith("## ") and "17." not in l]:
            assert heading in out
        assert "```ebnf" in out and out.count("```braincode") == src.count("```braincode")
