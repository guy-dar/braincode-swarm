"""Retrieval over the real glossary, keyword+exact channels only (no
embedding model download in unit tests; dense retrieval is exercised by
`python -m rag.cli retrieve`)."""
import pytest

from rag import needs as needs_mod
from rag.retrieve import Retriever, render_check, render_context


@pytest.fixture(scope="module")
def retriever(tmp_path_factory):
    return Retriever(dense=False, use_llm=False, index_dir=tmp_path_factory.mktemp("index"))


def symbols(cands):
    return [c["symbol"] for c in cands]


class TestSegmentation:
    def test_conversation_turns_and_sentences(self):
        segs = needs_mod.segment("<|user|>Hi there. Book a table?<|assistant|>Sure. Which day?")
        assert [s["loc"] for s in segs] == ["t1:s1", "t1:s2", "t2:s1", "t2:s2"]
        assert segs[2]["speaker"] == "AGENT"

    def test_bare_prompt_is_one_user_turn(self):
        segs = needs_mod.segment("Put the mug in the sink.")
        assert segs == [{"loc": "t1:s1", "turn": 1, "speaker": "USER", "text": "Put the mug in the sink."}]

    def test_numbered_text_matches_locators(self):
        text = needs_mod.numbered_text(needs_mod.segment("<|user|>A.<|assistant|>B."))
        assert text.splitlines() == ["t1:s1 [USER] A.", "", "t2:s1 [AGENT] B."]

    def test_heuristic_needs_type_negation_and_questions(self):
        segs = needs_mod.segment("<|user|>Do not use flowery language. What is the capital of France?")
        kinds = [n["kind"] for n in needs_mod.heuristic_needs(segs)]
        assert kinds == ["negation", "speech_act"]


class TestSearch:
    def test_alfred_need_finds_operations_and_entities(self, retriever):
        found = symbols(retriever.search_need("rinse the mug in the sink and put it in the coffee maker", kind="action"))
        assert {"rinse", "mug", "sink", "coffee_maker", "place"} <= set(found)

    def test_alias_finds_symbol(self, retriever):
        assert "rank_price" in symbols(retriever.search_need("the cheapest one", kind="constraint"))

    def test_exact_matches_survive_a_tiny_keep(self, retriever):
        found = retriever.search_need("grab the mug and wash it", keep=0)
        assert {"pick_up", "mug", "rinse"} <= set(symbols(found))
        assert all("exact" in c["reasons"] for c in found)

    def test_widen_returns_more_than_search(self, retriever):
        text = "walking at most twenty minutes between stops"
        assert len(retriever.widen(text)["candidates"]) > len(retriever.search_need(text))


class TestRetrieve:
    def test_supplied_needs_expand_to_rules_and_dependencies(self, retriever):
        result = retriever.retrieve("Make a three-day Kyoto itinerary.",
                                    needs=[{"kind": "object", "text": "Kyoto itinerary", "source": ["t1:s1"]}])
        ids = {r["id"] for r in result["records"]}
        assert "v19/composite/content_kyoto_itinerary" in ids
        assert "v19/support/subject" in ids                       # dependency
        assert "v19/rule/composites-general" in ids               # shared rule
        assert "v19/rule/reading-guide" in ids                    # core

    def test_context_renders_needs_table(self, retriever):
        result = retriever.retrieve("Put the mug in the sink.", use_llm=False)
        text = render_context(result, retriever, "test")
        assert "| n1 |" in text and "`mug`" in text


class TestCheck:
    def test_reports_coverage_and_invented_symbols(self, retriever):
        needs = [{"id": "n1", "kind": "action", "text": "rinse mug",
                  "candidates": [{"symbol": "rinse"}, {"symbol": "mug"}]},
                 {"id": "n2", "kind": "constraint", "text": "politely", "candidates": [{"symbol": "tone_polite"}]}]
        translation = """Status: success
```braincode
MODE REQUEST
ENTRYPOINT Mug
TASK Mug {
  ACTION pick_up(target=mug) -> mug_ref : REF[STRING]
  ACTION rinse(target=mug_ref, destination=sink) -> mug_ref_2 : REF[STRING]
  ACTION scrub_hard(target=mug_ref_2, tool=sponge_thing)
}
```
"""
        report = retriever.check(translation, needs)
        assert [n["status"] for n in report["needs"]] == ["covered", "unresolved"]
        assert report["unknown_symbols_in_head_position"] == ["scrub_hard"]
        assert "sponge_thing" in report["unbound_attribute_values"]
        assert "mug_ref" not in report["unbound_attribute_values"]
        assert "MISS" in render_check(report)

    def test_flags_string_entities_claimed_absent_and_unclosed_blocks(self, retriever):
        translation = """Status: success
```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=AGENT {
    RECORD ACTION pick_up(target="knife", source=table) STATUS succeeded SOURCE "t1:s1" -> e : EVENT
  }
}

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | pick_up, right_of | covered |
"""
        report = retriever.check(translation, [])
        assert report["string_literals_as_operation_arguments"] == ['target="knife"']
        assert report["claimed_but_absent"] == {"right_of": ["n1"]}
        assert report["unknown_symbols_in_head_position"] == []   # RECORD/TERM on later lines aren't heads
