import pytest

from braincode_loop.utils import canonicalize_expression, parse_json_response


def test_json_extraction_handles_markdown_fence():
    text = "Sure, here you go:\n```json\n{\"a\": 1}\n```"
    assert parse_json_response(text) == {"a": 1}


def test_json_extraction_ignores_prose_before_and_after():
    text = 'Here is the object:\n{"a": 1, "b": [1, 2]}\nLet me know if you need anything else!'
    assert parse_json_response(text) == {"a": 1, "b": [1, 2]}


def test_json_extraction_tolerates_trailing_commas():
    text = '{"a": 1, "b": [1, 2, 3,],\n"c": "x",\n}'
    assert parse_json_response(text) == {"a": 1, "b": [1, 2, 3], "c": "x"}


def test_json_extraction_tolerates_literal_newlines_in_strings():
    # A raw, unescaped newline inside a string value is invalid under strict JSON but common in
    # LLM output for multi-line fields (e.g. a `grammar` or `semantics` field) — must still parse.
    text = '{"grammar": "line one\nline two"}'
    assert parse_json_response(text) == {"grammar": "line one\nline two"}


def test_json_extraction_recovers_from_truncation_mid_string(caplog):
    # Cut off mid-value, as happens when a response is truncated by a token/length limit.
    text = '{"a": 1, "changes": [{"name": "Task"}, {"name": "Action", "grammar": "some text that got cut'
    result = parse_json_response(text)
    assert result["a"] == 1
    assert result["changes"][0]["name"] == "Task"
    assert "Recovered a likely-truncated JSON response" in caplog.text


def test_json_extraction_recovers_from_truncation_after_dangling_key(caplog):
    # Truncated right after a key's colon, with no value at all yet — closing brackets alone
    # can't fix this; the incomplete trailing member must be trimmed.
    text = '{\n  "a": 1,\n  "changes": [{"name": "Task"}],\n  "rationale":'
    result = parse_json_response(text)
    assert result["a"] == 1
    assert result["changes"] == [{"name": "Task"}]
    assert "rationale" not in result


def test_json_extraction_raises_on_pure_garbage():
    with pytest.raises(ValueError):
        parse_json_response("Sorry, I can't help with that request.")


def test_canonicalize_collapses_whitespace_and_case():
    assert canonicalize_expression("  Foo(  Bar )  .") == "foo( bar )"
