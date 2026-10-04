import sys
from collections import Counter
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import metrics  # noqa: E402

KINDS = {"pick_up": "operation", "place": "operation", "measure": "constructor", "outcome": "claim_relation",
         "MODE": "structural", "rule_x": "rule"}
DOC = """Status: success

## BrainCode

```braincode
MODE REQUEST
ENTRYPOINT Mug
TASK Mug {
  ACTION pick_up(target=object_label::mug) -> mug_ref : REF[STRING]  # pick_up again in a comment
  ACTION place(target=mug_ref, destination=object_label::sink, note="pick_up literal")
  TERM measure(amount=5, unit=currency::ZAR) -> m : TERM
}
```
"""


def test_symbol_counts_skip_comments_literals_and_structural():
    symbols, types = metrics.symbol_counts(DOC, KINDS)
    assert symbols == Counter({"pick_up": 1, "place": 1, "measure": 1, "object_label::mug": 1,
                               "object_label::sink": 1, "currency::ZAR": 1})
    assert types == Counter({"operation": 2, "constructor": 1, "group_value": 3})


def test_js_divergence_properties():
    a, b = Counter({"x": 2, "y": 2}), Counter({"z": 1})
    assert metrics.js_divergence(a, a) == 0.0
    assert metrics.js_divergence(a, b) == pytest.approx(1.0)
    c = Counter({"x": 3, "y": 1})
    assert metrics.js_divergence(a, c) == pytest.approx(metrics.js_divergence(c, a))
    assert 0 < metrics.js_divergence(a, c) < 1
    assert metrics.js_divergence(Counter(), Counter()) == 0.0
    assert metrics.js_divergence(Counter(), a) == 1.0


def test_mean_pairwise_js():
    a = Counter({"x": 1})
    mean, identical = metrics.mean_pairwise_js([a, a, Counter({"y": 1})])
    assert mean == pytest.approx(2 / 3) and identical == pytest.approx(1 / 3)
    assert metrics.mean_pairwise_js([a]) == (None, None)


def test_word_levenshtein():
    assert metrics.levenshtein(["a", "b", "c"], ["a", "x", "c", "d"]) == 2
    assert metrics.word_levenshtein_similarity("Put the mug away", "put the mug away") == 1.0
    assert metrics.word_levenshtein_similarity("<|user|>a b c d", "a b") == pytest.approx(0.5)


def test_bleu_and_rouge_are_oriented_higher_is_better():
    ref = "put the clean mug in the sink and turn on the light"
    assert metrics.bleu(ref, ref) == pytest.approx(1.0)
    assert metrics.rouge_l(ref, ref) == pytest.approx(1.0)
    worse = "open the window"
    assert metrics.bleu(ref, worse) < metrics.bleu(ref, "put the clean mug in the sink")
    assert metrics.rouge_l(ref, worse) < metrics.rouge_l(ref, "put the clean mug in the sink")
