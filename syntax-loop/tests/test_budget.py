import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from braincode_loop.budget import BudgetExceeded, BudgetTracker


def test_default_budget_matches_spec():
    b = BudgetTracker()
    assert b.max_budget_usd == 20.0


def test_stops_on_budget_exhaustion():
    b = BudgetTracker(max_budget_usd=1.0, max_iterations=100)
    b.record_call(sprint=1, role="x", provider="p", model="m", input_tokens=1, output_tokens=1, cost_usd=1.0)
    ok, reason = b.status()
    assert not ok
    assert "budget_exhausted" in reason


def test_stops_on_iteration_cap():
    b = BudgetTracker(max_budget_usd=1000.0, max_iterations=2)
    b.complete_sprint()
    b.complete_sprint()
    ok, reason = b.status()
    assert not ok
    assert "max_iterations_reached" in reason


def test_ensure_available_raises_when_exceeded():
    b = BudgetTracker(max_budget_usd=1.0, max_iterations=100)
    b.record_call(sprint=1, role="x", provider="p", model="m", input_tokens=1, output_tokens=1, cost_usd=1.0)
    try:
        b.ensure_available()
        assert False, "expected BudgetExceeded"
    except BudgetExceeded:
        pass


def test_whichever_limit_hits_first_stops():
    b = BudgetTracker(max_budget_usd=20.0, max_iterations=3)
    b.complete_sprint()
    b.complete_sprint()
    b.complete_sprint()
    ok, reason = b.status()
    assert not ok and "max_iterations_reached" in reason
    assert b.spent_usd == 0.0  # budget itself untouched — confirms iteration cap fired, not budget


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print(f"ok: {name}")
