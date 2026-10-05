"""The scorer must agree with BBEH's own examples (bbeh/evaluate.py)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import improve  # noqa: E402

OFFICIAL = [
    ("Ok The final answer is: \\boxed{4}.", "4", True),
    ("[Reasoning] The final answer is: \\boxed{4}.", "3", False),
    ("Alright! The final answer is: 2, 3, 4", "2,3,4", True),
    ("blah blah The final answer is: 2, 3, 4", "2,3,5", False),
    ("Ok The answer is: (A)", "a", True),
    ("Ok The answer is: (A)", "b", False),
    ("Ok The answer is: **25**\nHere's why.", "25.0", True),
    ("Ok The answer is: **25**\nHere's why.", "26.0", False),
]


def test_scorer_matches_official_examples():
    for sample, reference, expected in OFFICIAL:
        assert improve.evaluate_correctness(sample, reference) is expected, (sample, reference)
