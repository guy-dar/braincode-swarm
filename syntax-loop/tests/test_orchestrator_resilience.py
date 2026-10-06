"""A Shaper response that never parses as JSON (base_role.py exhausts its retries and raises
ValueError) must fail only that one attempt, not crash the whole run — see orchestrator.py's
run_bootstrap_sprint/run_sprint try/except around the Shaper call."""
import json

from test_dry_run_smoke import _workspace

from braincode_loop.orchestrator import Orchestrator
from braincode_loop.roles.base_role import LLMCallFailed


def test_malformed_shaper_response_does_not_crash_bootstrap(tmp_path):
    config = _workspace(tmp_path)
    orch = Orchestrator(config, base_dir=str(tmp_path))

    real_propose_basis = orch.shaper.propose_basis
    calls = {"n": 0}

    def flaky_propose_basis(**kwargs):
        calls["n"] += 1
        if calls["n"] == 1:
            raise ValueError("Could not parse JSON from model response (simulated)")
        return real_propose_basis(**kwargs)

    orch.shaper.propose_basis = flaky_propose_basis

    accepted = orch.run_bootstrap_sprint()  # must not raise

    assert accepted is True
    assert calls["n"] == 2  # attempt 1 failed to parse, attempt 2 (the canned dry-run response) succeeded
    changelog = (tmp_path / "docs" / "changelog.md").read_text(encoding="utf-8")
    assert "Shaper failed to produce a usable proposal" in changelog
    assert "attempt 1" in changelog and "attempt 2" in changelog
    spec = (tmp_path / "docs" / "language-spec.md").read_text(encoding="utf-8")
    assert "**Status:** bootstrapped" in spec


def test_malformed_shaper_response_does_not_crash_steady_state(tmp_path):
    config = _workspace(tmp_path)
    config["run"]["docs_dir"] = "docs"
    orch = Orchestrator(config, base_dir=str(tmp_path))
    assert orch.run_bootstrap_sprint() is True  # get to steady state first

    real_propose = orch.shaper.propose
    calls = {"n": 0}

    def flaky_propose(**kwargs):
        calls["n"] += 1
        if calls["n"] == 1:
            raise ValueError("Could not parse JSON from model response (simulated)")
        return real_propose(**kwargs)

    orch.shaper.propose = flaky_propose

    orch.run_sprint(1)  # must not raise

    assert calls["n"] == 2
    changelog = (tmp_path / "docs" / "changelog.md").read_text(encoding="utf-8")
    assert "Shaper failed to produce a usable proposal" in changelog


def test_real_critique_survives_a_malformed_attempt_in_between(tmp_path):
    """Regression test for a real failure seen in production: attempt 1 gets a real
    needs-rework critique with concrete required_changes; attempt 2's Shaper JSON fails to
    parse; attempt 3 must still receive attempt 1's real required_changes, not just the
    generic "fix your JSON formatting" note the malformed-response handler manufactures —
    otherwise a mid-run parse failure silently erases all of the Critic's substantive
    feedback and the next attempt effectively restarts from scratch instead of revising."""
    config = _workspace(tmp_path)
    orch = Orchestrator(config, base_dir=str(tmp_path))

    real_assess = orch.critic.assess
    assess_calls = {"n": 0}

    def flaky_assess(**kwargs):
        assess_calls["n"] += 1
        result = real_assess(**kwargs)
        if assess_calls["n"] == 1:
            result = dict(result)
            result["decision"] = "needs-rework"
            result["required_changes"] = [{"target": "basis", "change": "SPECIFIC_MARKER_DEFINE_ITERATION"}]
        return result

    orch.critic.assess = flaky_assess

    real_propose_basis = orch.shaper.propose_basis
    seen_previous_attempts = []
    calls = {"n": 0}

    def flaky_propose_basis(**kwargs):
        calls["n"] += 1
        seen_previous_attempts.append(kwargs.get("previous_attempt"))
        if calls["n"] == 2:
            raise ValueError("Could not parse JSON from model response (simulated)")
        return real_propose_basis(**kwargs)

    orch.shaper.propose_basis = flaky_propose_basis

    orch.run_bootstrap_sprint()

    assert calls["n"] == 3
    attempt_3_previous = seen_previous_attempts[2]
    assert "SPECIFIC_MARKER_DEFINE_ITERATION" in json.dumps(attempt_3_previous), (
        "attempt 3 lost attempt 1's real required_changes after attempt 2's JSON parse failure"
    )


def test_malformed_critic_response_does_not_crash_bootstrap(tmp_path):
    """Same failure class as the Shaper crash bug, one role deeper: base_role.py's JSON-parse
    retry loop can exhaust for ANY role's call, not just the Shaper's. Critic.assess() is the
    largest, most complex prompt/schema of the four roles, so it is at least as likely to hit
    this in production — it must fail only the one attempt, not crash the run."""
    config = _workspace(tmp_path)
    orch = Orchestrator(config, base_dir=str(tmp_path))

    real_assess = orch.critic.assess
    calls = {"n": 0}

    def flaky_assess(**kwargs):
        calls["n"] += 1
        if calls["n"] == 1:
            raise ValueError("Could not parse JSON from model response (simulated)")
        return real_assess(**kwargs)

    orch.critic.assess = flaky_assess

    accepted = orch.run_bootstrap_sprint()  # must not raise

    assert accepted is True
    assert calls["n"] == 2
    changelog = (tmp_path / "docs" / "changelog.md").read_text(encoding="utf-8")
    assert "attempt 1" in changelog and "attempt 2" in changelog


def test_critic_failure_carries_forward_prior_required_changes(tmp_path):
    """Mirrors test_real_critique_survives_a_malformed_attempt_in_between but for a Critic
    parse failure instead of a Shaper one: attempt 1 gets a real needs-rework critique with
    concrete required_changes; attempt 2's Critic JSON fails to parse; attempt 3's Shaper must
    still see attempt 1's real required_changes, not a bare "couldn't parse" note."""
    config = _workspace(tmp_path)
    orch = Orchestrator(config, base_dir=str(tmp_path))

    real_assess = orch.critic.assess
    assess_calls = {"n": 0}

    def flaky_assess(**kwargs):
        assess_calls["n"] += 1
        if assess_calls["n"] == 1:
            result = dict(real_assess(**kwargs))
            result["decision"] = "needs-rework"
            result["required_changes"] = [{"target": "basis", "change": "SPECIFIC_MARKER_DEFINE_ITERATION"}]
            return result
        if assess_calls["n"] == 2:
            raise ValueError("Could not parse JSON from model response (simulated)")
        return real_assess(**kwargs)

    orch.critic.assess = flaky_assess

    real_propose_basis = orch.shaper.propose_basis
    seen_previous_attempts = []

    def recording_propose_basis(**kwargs):
        seen_previous_attempts.append(kwargs.get("previous_attempt"))
        return real_propose_basis(**kwargs)

    orch.shaper.propose_basis = recording_propose_basis

    orch.run_bootstrap_sprint()  # must not raise

    assert assess_calls["n"] == 3
    attempt_3_previous = seen_previous_attempts[2]
    assert "SPECIFIC_MARKER_DEFINE_ITERATION" in json.dumps(attempt_3_previous), (
        "attempt 3 lost attempt 1's real required_changes after attempt 2's Critic parse failure"
    )


def test_malformed_documenter_response_does_not_crash_and_still_applies_acceptance(tmp_path):
    """If the Documenter's own summary call fails to parse after retries, the accepted changes
    it was about to record must still be written to docs/ (that's real, already-approved,
    already-paid-for content) — the run must not crash and must not silently drop the
    acceptance because of an unrelated prose-summary failure."""
    config = _workspace(tmp_path)
    orch = Orchestrator(config, base_dir=str(tmp_path))

    real_call = orch.documenter.call
    calls = {"n": 0}

    def flaky_call(*args, **kwargs):
        calls["n"] += 1
        if calls["n"] == 1:
            raise ValueError("Could not parse JSON from model response (simulated)")
        return real_call(*args, **kwargs)

    orch.documenter.call = flaky_call

    accepted = orch.run_bootstrap_sprint()  # must not raise

    assert accepted is True
    spec = (tmp_path / "docs" / "language-spec.md").read_text(encoding="utf-8")
    assert "**Status:** bootstrapped" in spec
    assert "### `entity-ref`" in spec  # the accepted construct was still written despite the summary failure


def test_malformed_searcher_response_does_not_crash_bootstrap(tmp_path):
    """Same failure class again, one role earlier: the Searcher runs once per sprint, before the
    Shaper/Critic attempt loop even starts. If its JSON response fails to parse after retries,
    the sprint must still proceed with a fallback grounding note, not crash the whole run."""
    config = _workspace(tmp_path)
    orch = Orchestrator(config, base_dir=str(tmp_path))

    real_ground_basis = orch.searcher.ground_basis
    calls = {"n": 0}

    def flaky_ground_basis(**kwargs):
        calls["n"] += 1
        if calls["n"] == 1:
            raise ValueError("Could not parse JSON from model response (simulated)")
        return real_ground_basis(**kwargs)

    orch.searcher.ground_basis = flaky_ground_basis

    accepted = orch.run_bootstrap_sprint()  # must not raise

    assert accepted is True
    assert calls["n"] == 1  # Searcher runs once per sprint, not once per attempt — no retry loop here


def test_llm_call_failure_is_not_mislabeled_as_a_json_parse_failure(tmp_path):
    """Regression test for a real production incident: an Anthropic SDK pre-flight rejection
    ("Streaming is required for operations that may take longer than 10 minutes" — raised
    client-side before any network request, entirely unrelated to JSON) got caught by a bare
    `except ValueError` and logged as "Shaper never produced parseable JSON" for all 100 bootstrap
    attempts. LLMCallFailed (roles/base_role.py) is deliberately NOT a ValueError so this class of
    failure can never be confused with parse_json_response's ValueError again — verify the
    orchestrator still handles it gracefully (no crash) AND the changelog entry it writes
    describes the real failure, not a fabricated JSON complaint."""
    config = _workspace(tmp_path)
    orch = Orchestrator(config, base_dir=str(tmp_path))

    real_propose_basis = orch.shaper.propose_basis
    calls = {"n": 0}

    def flaky_propose_basis(**kwargs):
        calls["n"] += 1
        if calls["n"] == 1:
            raise LLMCallFailed(
                "[shaper_bootstrap] LLM call failed before returning a response: Streaming is "
                "required for operations that may take longer than 10 minutes."
            )
        return real_propose_basis(**kwargs)

    orch.shaper.propose_basis = flaky_propose_basis

    accepted = orch.run_bootstrap_sprint()  # must not raise

    assert accepted is True
    assert calls["n"] == 2
    changelog = (tmp_path / "docs" / "changelog.md").read_text(encoding="utf-8")
    assert "Shaper failed to produce a usable proposal" in changelog
    assert "Streaming is required" in changelog
    assert "never parsed as JSON" not in changelog
    assert "parseable JSON" not in changelog


def test_llm_call_failure_carries_forward_prior_required_changes_without_blaming_formatting(tmp_path):
    """Mirrors test_real_critique_survives_a_malformed_attempt_in_between, but for an
    LLMCallFailed instead of a JSON-parse failure: attempt 1 gets a real needs-rework critique
    with concrete required_changes; attempt 2's Shaper call fails at the infrastructure level.
    Attempt 3 must still see attempt 1's real required_changes, AND the carried-forward critique
    must not tell the Shaper to "fix your JSON formatting" — the previous attempt's content was
    never the problem."""
    config = _workspace(tmp_path)
    orch = Orchestrator(config, base_dir=str(tmp_path))

    real_assess = orch.critic.assess
    assess_calls = {"n": 0}

    def flaky_assess(**kwargs):
        assess_calls["n"] += 1
        if assess_calls["n"] == 1:
            result = dict(real_assess(**kwargs))
            result["decision"] = "needs-rework"
            result["required_changes"] = [{"target": "basis", "change": "SPECIFIC_MARKER_DEFINE_ITERATION"}]
            return result
        return real_assess(**kwargs)

    orch.critic.assess = flaky_assess

    real_propose_basis = orch.shaper.propose_basis
    seen_previous_attempts = []
    calls = {"n": 0}

    def flaky_propose_basis(**kwargs):
        calls["n"] += 1
        seen_previous_attempts.append(kwargs.get("previous_attempt"))
        if calls["n"] == 2:
            raise LLMCallFailed("[shaper_bootstrap] LLM call failed before returning a response: connection reset")
        return real_propose_basis(**kwargs)

    orch.shaper.propose_basis = flaky_propose_basis

    orch.run_bootstrap_sprint()  # must not raise

    assert calls["n"] == 3
    attempt_3_previous = seen_previous_attempts[2]
    dumped = json.dumps(attempt_3_previous)
    assert "SPECIFIC_MARKER_DEFINE_ITERATION" in dumped, (
        "attempt 3 lost attempt 1's real required_changes after attempt 2's LLMCallFailed"
    )
    assert "Return only a single valid JSON object" not in dumped, (
        "an infrastructure failure must not be blamed on the Shaper's JSON formatting"
    )
    assert "no content change needed" in dumped
