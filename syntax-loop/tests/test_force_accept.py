"""On the LAST attempt of a sprint (bootstrap or steady-state), a genuine `needs-rework` verdict
is force-accepted with the Critic's still-open required_changes carried forward as visible known
issues, instead of retrying forever (previously up to 100 bootstrap attempts) or ending the
sprint with nothing documented. See orchestrator.py::_run_attempt's `force_accept` param and
config.yaml's run.bootstrap.max_attempts / run.sprint.max_attempts (both 3).

Deliberately narrow: force-accept must NEVER override an explicit `reject` (the Critic judged the
shape fundamentally wrong) or a doc-hygiene failure (missing glossary_gloss/worked_example would
corrupt the actual spec/glossary write)."""
from test_dry_run_smoke import _workspace

from braincode_loop.orchestrator import Orchestrator


def test_force_accepts_last_bootstrap_attempt_with_known_issues(tmp_path):
    config = _workspace(tmp_path)
    orch = Orchestrator(config, base_dir=str(tmp_path))
    assert orch.bootstrap_max_attempts == 3

    real_assess = orch.critic.assess
    calls = {"n": 0}

    def always_needs_rework(**kwargs):
        calls["n"] += 1
        result = dict(real_assess(**kwargs))
        result["decision"] = "needs-rework"
        result["required_changes"] = [{"target": "basis", "change": "KNOWN_ISSUE_MARKER"}]
        return result

    orch.critic.assess = always_needs_rework

    accepted = orch.run_bootstrap_sprint()  # must not raise

    assert accepted is True
    assert calls["n"] == 3  # all 3 attempts genuinely ran; the 3rd was force-accepted

    spec = (tmp_path / "docs" / "language-spec.md").read_text(encoding="utf-8")
    assert "**Status:** bootstrapped" in spec  # the state actually changed, not just logged

    changelog = (tmp_path / "docs" / "changelog.md").read_text(encoding="utf-8")
    assert "Forced acceptance after 3 attempt(s)" in changelog
    assert "KNOWN_ISSUE_MARKER" in changelog  # the known issue is on the record, not hidden
    assert "**Decision:** accepted" in changelog

    backlog = (tmp_path / "docs" / "backlog.md").read_text(encoding="utf-8")
    assert "| accepted |" in backlog


def test_does_not_force_accept_an_explicit_reject(tmp_path):
    config = _workspace(tmp_path)
    orch = Orchestrator(config, base_dir=str(tmp_path))

    real_assess = orch.critic.assess

    def always_reject(**kwargs):
        result = dict(real_assess(**kwargs))
        result["decision"] = "reject"
        return result

    orch.critic.assess = always_reject

    accepted = orch.run_bootstrap_sprint()  # must not raise

    assert accepted is False
    spec = (tmp_path / "docs" / "language-spec.md").read_text(encoding="utf-8")
    assert "not yet bootstrapped" in spec  # nothing was written


def test_does_not_force_accept_a_hygiene_failure(tmp_path):
    config = _workspace(tmp_path)
    orch = Orchestrator(config, base_dir=str(tmp_path))

    # Force every attempt to needs-rework via the Critic too — otherwise the canned dry-run
    # Critic's default "accept" would land on attempt 1 (a complete, valid proposal) before the
    # loop ever reaches the last attempt, where this test needs the hygiene failure to occur.
    real_assess = orch.critic.assess

    def always_needs_rework(**kwargs):
        result = dict(real_assess(**kwargs))
        result["decision"] = "needs-rework"
        return result

    orch.critic.assess = always_needs_rework

    real_propose_basis = orch.shaper.propose_basis

    def incomplete_last_attempt(**kwargs):
        result = real_propose_basis(**kwargs)
        if kwargs.get("attempt") == orch.bootstrap_max_attempts:
            # Strip a required field so doc_hygiene.check() fails on the final attempt.
            result = dict(result)
            result["changes"] = [dict(c) for c in result["changes"]]
            result["changes"][0].pop("glossary_gloss", None)
        return result

    orch.shaper.propose_basis = incomplete_last_attempt

    accepted = orch.run_bootstrap_sprint()  # must not raise

    assert accepted is False
    spec = (tmp_path / "docs" / "language-spec.md").read_text(encoding="utf-8")
    assert "not yet bootstrapped" in spec  # nothing was written — hygiene failure is never force-accepted


def test_force_accepts_last_steady_state_attempt(tmp_path):
    config = _workspace(tmp_path)
    orch = Orchestrator(config, base_dir=str(tmp_path))
    assert orch.sprint_max_attempts == 3
    assert orch.run_bootstrap_sprint() is True  # get to steady state first

    real_assess = orch.critic.assess
    calls = {"n": 0}

    def always_needs_rework(**kwargs):
        calls["n"] += 1
        result = dict(real_assess(**kwargs))
        result["decision"] = "needs-rework"
        result["required_changes"] = [{"target": "seq", "change": "STEADY_STATE_KNOWN_ISSUE"}]
        return result

    orch.critic.assess = always_needs_rework

    orch.run_sprint(1)  # must not raise

    assert calls["n"] == 3
    changelog = (tmp_path / "docs" / "changelog.md").read_text(encoding="utf-8")
    assert "Forced acceptance after 3 attempt(s)" in changelog
    assert "STEADY_STATE_KNOWN_ISSUE" in changelog
