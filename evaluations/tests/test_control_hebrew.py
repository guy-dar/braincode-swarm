import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import control_hebrew as ch  # noqa: E402

ORIGINAL = "<|user|>Book a table for two.<|assistant|>1. Open opentable.com\n2. Search for dinner"
HEBREW = "<|user|>הזמן שולחן לשניים.<|assistant|>1. פתח את opentable.com\n2. חפש ארוחת ערב"


def test_hebrew_share_ignores_urls_and_code():
    assert ch.hebrew_share(HEBREW) == 1.0
    assert ch.hebrew_share("<|user|>Book a table for two.") == 0.0
    assert ch.hebrew_share("הרץ `pip install foo` עכשיו") == 1.0


def test_latin_word_share_counts_words_left_in_latin_script():
    assert ch.latin_word_share("שלום world") == pytest.approx(0.5)
    assert ch.latin_word_share("<|user|>שלום") == 0.0


def test_output_problems():
    assert ch.output_problems("forward", ORIGINAL, HEBREW) == []
    assert ch.output_problems("forward", ORIGINAL, "") == ["empty output"]
    untranslated = ch.output_problems("forward", ORIGINAL, ORIGINAL)
    assert len(untranslated) == 1 and "Hebrew" in untranslated[0]
    assert "turn markers" in ch.output_problems("back", ORIGINAL, "<|user|>Book a table for two.")[0]
    assert ch.output_problems("back", ORIGINAL, ORIGINAL) == []        # back step: no Hebrew check


def _row(method, item, ds, score, copied=0.1):
    return {"method": method, "model": "m", "item": item, "dataset": ds, "bleu": score, "rouge_l": score,
            "word_lev_sim": score, "copied": copied, "original": "a b c", "reconstruction": "a b c"}


def test_paired_keeps_items_with_both_round_trips():
    rows = [_row("braincode", "i1", "alfred", 0.2), _row("hebrew", "i1", "alfred", 0.6),
            _row("braincode", "i2", "alfred", 0.3)]
    assert {r["item"] for r in ch.paired(rows)} == {"i1"}


def test_comparison_and_tests_tables():
    rows = [_row("braincode", "i1", "alfred", 0.2), _row("hebrew", "i1", "alfred", 0.6),
            _row("braincode", "i2", "prism", 0.4), _row("hebrew", "i2", "prism", 0.5)]
    lines, out = ch.comparison_table(rows, {"m": "Model"}, {"alfred": "ALFRED", "prism": "PRISM"})
    overall = next(r for r in out if r["dataset"] == "all")
    assert overall["pairs"] == 2
    assert overall["rouge_l_braincode"] == pytest.approx(0.3)
    assert overall["rouge_l_hebrew"] == pytest.approx(0.55)
    assert {r["dataset"] for r in out} == {"all", "ALFRED", "PRISM"}
    t = ch.tests_table(rows, {"m": "Model"})
    assert any("ROUGE-L" in line and "-0.250" in line and "0 of 2" in line for line in t)
