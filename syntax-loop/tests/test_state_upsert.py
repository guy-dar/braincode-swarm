import os
import shutil

from braincode_loop.reset import SEED_DOCS_DIR
from braincode_loop.state import LanguageState

SEED_TASKS = os.path.join(os.path.dirname(__file__), "..", "braincode_loop", "seed_tasks.json")


def _state(tmp_path):
    for name in ("language-spec.md", "glossary.md"):
        shutil.copyfile(os.path.join(SEED_DOCS_DIR, name), tmp_path / name)
    return LanguageState(str(tmp_path), SEED_TASKS)


def _construct(name, semantics="v1", sprint=1):
    return {
        "construct_name": name, "grammar": f"{name.upper()}(<x>)", "semantics": semantics,
        "worked_example": {"nl": "n", "braincode": "b"}, "glossary_gloss": f"gloss {semantics}", "sprint": sprint,
    }


def test_add_then_revise_replaces_single_section(tmp_path):
    state = _state(tmp_path)
    assert not state.is_bootstrapped()
    state.upsert_construct_in_spec(_construct("seq"))
    state.upsert_glossary_entry(_construct("seq"))
    state.upsert_construct_in_spec(_construct("cond", semantics="cond-v1"))
    state.upsert_glossary_entry(_construct("cond", semantics="cond-v1"))
    state.upsert_construct_in_spec(_construct("seq", semantics="v2", sprint=2))
    state.upsert_glossary_entry(_construct("seq", semantics="v2", sprint=2))

    spec = (tmp_path / "language-spec.md").read_text(encoding="utf-8")
    glossary = (tmp_path / "glossary.md").read_text(encoding="utf-8")
    assert spec.count("### `seq`") == 1 and spec.count("### `cond`") == 1
    assert "**Semantics:** v2" in spec and "**Semantics:** v1" not in spec and "**Semantics:** cond-v1" in spec
    assert "*\n\n### `cond`" in spec  # blank line between sections survives a replace
    assert "No constructs accepted yet" not in spec
    assert glossary.count("### `seq`") == 1 and "gloss v2" in glossary and "gloss v1" not in glossary
    assert "Empty — no constructs" not in glossary
    assert state.spec_construct_names() == {"seq", "cond"}
    assert state.is_bootstrapped()


def test_revise_keeps_following_section_intact(tmp_path):
    state = _state(tmp_path)
    state.upsert_construct_in_spec(_construct("a"))
    state.upsert_construct_in_spec(_construct("b"))
    state.upsert_construct_in_spec(_construct("a", semantics="v2"))
    spec = (tmp_path / "language-spec.md").read_text(encoding="utf-8")
    assert spec.index("### `a`") < spec.index("### `b`")
    assert "**Grammar:** `B(<x>)`" in spec


def test_bump_version_for_picks_strongest(tmp_path):
    state = _state(tmp_path)
    assert state.bump_version_for(["PATCH", "MINOR", "PATCH"]) == "0.2.0"
    assert state.bump_version_for(["patch"]) == "0.2.1"
    assert state.bump_version_for(["MINOR", "MAJOR"]) == "1.0.0"
    assert state.bump_version_for([]) == "1.0.1"
    assert "**Version:** 1.0.1" in (tmp_path / "language-spec.md").read_text(encoding="utf-8")


def test_set_and_replace_foundations(tmp_path):
    state = _state(tmp_path)
    state.set_foundations("first overview\n")
    state.replace_foundations("second overview")
    spec = (tmp_path / "language-spec.md").read_text(encoding="utf-8")
    assert "second overview" in spec and "first overview" not in spec
    assert "## Constructs" in spec
