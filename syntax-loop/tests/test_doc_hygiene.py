from braincode_loop import doc_hygiene


def _change(**overrides):
    base = {
        "op": "add",
        "construct_name": "foo",
        "grammar": "FOO(<x>)",
        "semantics": "does foo",
        "glossary_gloss": "does foo things",
        "worked_example": {"nl": "x", "braincode": "y"},
    }
    base.update(overrides)
    return base


def test_fails_on_missing_gloss():
    result = doc_hygiene.check({"changes": [_change(glossary_gloss="")]})
    assert not result.ok
    assert result.failures[0]["construct_name"] == "foo"
    assert "glossary_gloss" in result.failures[0]["missing_fields"]


def test_fails_on_incomplete_example():
    result = doc_hygiene.check({"changes": [_change(worked_example={"nl": "x"})]})
    assert not result.ok
    assert "worked_example.nl/braincode" in result.failures[0]["missing_fields"]


def test_passes_when_every_change_complete():
    result = doc_hygiene.check({"changes": [_change(), _change(construct_name="bar", op="revise")]})
    assert result.ok and result.failures == []


def test_fails_on_empty_proposal():
    assert not doc_hygiene.check({"changes": []}).ok
    assert not doc_hygiene.check({}).ok
