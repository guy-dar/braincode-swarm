"""braincode_loop/reset.py::snapshot_docs archives a run's produced docs/ into
<base_dir>/braincode_loop/seed_docs/runs/<run_id>/ at the end of Orchestrator.run(), so a run's
documentation output survives a later --reset or a later run overwriting docs/ further."""
import os

from test_dry_run_smoke import _workspace

from braincode_loop.orchestrator import Orchestrator


def test_run_snapshots_docs_into_seed_docs_runs(tmp_path):
    config = _workspace(tmp_path)
    log_dir = os.path.join(str(tmp_path), "runs", "logs", "run_test123")
    os.makedirs(log_dir, exist_ok=True)

    Orchestrator(config, base_dir=str(tmp_path), log_dir=log_dir).run()

    snapshot_dir = os.path.join(str(tmp_path), "braincode_loop", "seed_docs", "runs", "run_test123")
    assert os.path.isdir(snapshot_dir)
    for name in ("language-spec.md", "glossary.md", "backlog.md", "changelog.md"):
        snap_path = os.path.join(snapshot_dir, name)
        live_path = os.path.join(str(tmp_path), "docs", name)
        assert os.path.exists(snap_path)
        with open(snap_path, encoding="utf-8") as f:
            snap_content = f.read()
        with open(live_path, encoding="utf-8") as f:
            live_content = f.read()
        assert snap_content == live_content


def test_no_log_dir_means_no_snapshot(tmp_path):
    config = _workspace(tmp_path)
    Orchestrator(config, base_dir=str(tmp_path)).run()  # log_dir defaults to None
    seed_docs_runs = os.path.join(str(tmp_path), "braincode_loop", "seed_docs", "runs")
    assert not os.path.isdir(seed_docs_runs)


def test_snapshot_never_touches_the_real_repos_seed_docs(tmp_path):
    """Regression test: snapshot_docs's destination must be resolved from `base_dir`, never from
    this module's own __file__ (the real installed package) — an earlier version of this function
    did the latter, which would have silently written every test's run snapshot into the live
    repo's braincode_loop/seed_docs/runs/ regardless of which project instance was running."""
    import braincode_loop

    real_seed_docs_runs = os.path.join(os.path.dirname(braincode_loop.__file__), "seed_docs", "runs")
    before = set(os.listdir(real_seed_docs_runs)) if os.path.isdir(real_seed_docs_runs) else None

    config = _workspace(tmp_path)
    log_dir = os.path.join(str(tmp_path), "runs", "logs", "run_isolation_check")
    os.makedirs(log_dir, exist_ok=True)
    Orchestrator(config, base_dir=str(tmp_path), log_dir=log_dir).run()

    after = set(os.listdir(real_seed_docs_runs)) if os.path.isdir(real_seed_docs_runs) else None
    assert after == before, (
        "snapshot_docs wrote into the real repo's seed_docs/runs/ instead of the test's isolated tmp_path"
    )
