"""The cross-run cumulative spend tracker (braincode_loop/budget.py::read_total_spend_data /
add_to_total_spent, wired into orchestrator.py::Orchestrator.run()) must accumulate real spend
(overall and per-provider) across separate invocations, print a "Budget burndown" block with a
per-provider breakdown and a per-run history table at start and end, survive `--reset`, and never
count a dry run's fabricated costs as real money.

IMPORTANT: every test here builds its Orchestrator with the config's `dry_run` left at
_workspace()'s safe default (True) and NEVER flips it — some provider API keys are ambient OS
environment variables on this machine (not just .env-scoped), so a test that set
`config["run"]["dry_run"] = False` once made real, billable API calls before it could be caught.
A later attempt to work around that by flipping `orch.dry_run` back to False *after*
construction was ALSO unsafe: `Orchestrator._run_attempt` passes `dry_run=self.dry_run` straight
through to `simulation.cross_translate` by reading the live attribute at call time, not a value
captured once at role construction, so that too could reach a real provider. Tests that need to
exercise the orchestrator's "this was a real run" bookkeeping instead stub out `_run_inner`
entirely (the sole entry point into all pipeline/role code) with a fake that records calls
directly on `orch.budget` — zero pipeline code executes, so there is no path to any network call
at all, regardless of what's ambient in the environment."""
import os

from test_dry_run_smoke import _workspace

from braincode_loop.budget import add_to_total_spent, read_total_spend_data, read_total_spent
from braincode_loop.orchestrator import Orchestrator
from braincode_loop.reset import reset_workspace


def _total_spend_path(tmp_path) -> str:
    return os.path.join(str(tmp_path), "runs", "total_spend.json")


def _fake_real_orchestrator(config, tmp_path, spend_usd=0.5):
    """dry_run stays True at the LLM-client level (see module docstring) — only
    Orchestrator.run()'s own "was this real" bookkeeping is exercised, and `_run_inner` is fully
    replaced so no role/network code ever runs regardless. Uses budget.record_call() directly
    (with two different providers) so per-provider aggregation has real data to sum, still
    entirely offline."""
    orch = Orchestrator(config, base_dir=str(tmp_path))
    orch.dry_run = False

    def fake_run_inner():
        orch.budget.record_call(
            sprint=0, role="shaper", provider="anthropic", model="m",
            input_tokens=100, output_tokens=100, cost_usd=round(spend_usd * 0.6, 4),
        )
        orch.budget.record_call(
            sprint=0, role="critic", provider="openai", model="m",
            input_tokens=100, output_tokens=100, cost_usd=round(spend_usd * 0.4, 4),
        )

    orch._run_inner = fake_run_inner
    return orch


def test_read_total_spent_defaults_to_zero_when_missing(tmp_path):
    assert read_total_spent(_total_spend_path(tmp_path)) == 0.0
    data = read_total_spend_data(_total_spend_path(tmp_path))
    assert data == {"total_usd": 0.0, "by_provider": {}, "runs": []}


def test_add_to_total_spent_accumulates_across_calls(tmp_path):
    path = _total_spend_path(tmp_path)
    os.makedirs(os.path.dirname(path), exist_ok=True)

    result = add_to_total_spent(path, 0.50, {"anthropic": 0.50})
    assert result["total_usd"] == 0.50
    assert result["by_provider"] == {"anthropic": 0.50}
    assert len(result["runs"]) == 1

    result = add_to_total_spent(path, 0.25, {"anthropic": 0.20, "openai": 0.05})
    assert result["total_usd"] == 0.75
    assert result["by_provider"] == {"anthropic": 0.70, "openai": 0.05}
    assert len(result["runs"]) == 2
    # append-only, oldest-to-newest
    assert result["runs"][0]["spent_usd"] == 0.50
    assert result["runs"][1]["spent_usd"] == 0.25
    assert read_total_spent(path) == 0.75


def test_a_run_updates_the_persisted_total(tmp_path, caplog):
    caplog.set_level("INFO", logger="braincode_loop")
    config = _workspace(tmp_path)
    orch = _fake_real_orchestrator(config, tmp_path)
    orch.run()

    data = read_total_spend_data(_total_spend_path(tmp_path))
    assert data["total_usd"] > 0
    assert data["total_usd"] == round(orch.budget.spent_usd, 4)
    assert set(data["by_provider"]) == {"anthropic", "openai"}
    assert "Budget burndown" in caplog.text
    assert "anthropic:" in caplog.text and "openai:" in caplog.text


def test_a_second_run_sees_the_first_runs_total_as_its_starting_point(tmp_path, caplog):
    caplog.set_level("INFO", logger="braincode_loop")
    config = _workspace(tmp_path)

    orch1 = _fake_real_orchestrator(config, tmp_path)
    orch1.run()
    first_total = read_total_spent(_total_spend_path(tmp_path))

    caplog.clear()
    orch2 = _fake_real_orchestrator(config, tmp_path)
    orch2.run()

    assert f"${first_total:.4f}" in caplog.text
    final = read_total_spend_data(_total_spend_path(tmp_path))
    assert final["total_usd"] == round(first_total + orch2.budget.spent_usd, 4)
    assert len(final["runs"]) == 2


def test_dry_run_does_not_affect_the_persisted_total(tmp_path):
    config = _workspace(tmp_path)  # dry_run stays True here — this is the case under test
    orch = Orchestrator(config, base_dir=str(tmp_path))
    orch.run()
    assert not os.path.exists(_total_spend_path(tmp_path))


def test_reset_does_not_remove_total_spend(tmp_path):
    config = _workspace(tmp_path)
    orch = _fake_real_orchestrator(config, tmp_path)
    orch.run()
    path = _total_spend_path(tmp_path)
    assert os.path.exists(path)
    data_before_reset = read_total_spend_data(path)

    reset_workspace(str(tmp_path))

    assert os.path.exists(path)  # --reset must not erase real cumulative spend history
    assert read_total_spend_data(path) == data_before_reset
