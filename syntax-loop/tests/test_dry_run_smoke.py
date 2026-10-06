"""End-to-end offline run: bootstrap + two steady-state sprints against a temp copy of the
workspace, $0 cost, no API keys."""
import json
import os
import shutil

import yaml

from braincode_loop.orchestrator import Orchestrator
from braincode_loop.reset import reset_workspace

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def _ignore_generated_artifacts(directory, contents):
    """shutil.copytree ignore callback: skip runtime-generated content that must never leak into
    a test's isolated tmp_path — (1) real fetched dataset samples (datasets/samples/<name>.jsonl,
    as opposed to the small committed <name>.seed.jsonl fallbacks): these can be large (real runs
    fetch up to 1000 rows each) and copying them into every test both slows the suite down and
    means tests would depend on however much real data happens to be fetched on this machine,
    instead of the small, deterministic seed fixtures they're meant to use; (2) accumulated
    braincode_loop/seed_docs/runs/<run_id>/ doc snapshots from real runs — copying these in would
    make "no snapshot exists yet" tests fail depending on what real runs happened to precede them
    on this machine, a real test-isolation bug caught by test_no_log_dir_means_no_snapshot."""
    ignored = {name for name in contents if name.endswith(".jsonl") and not name.endswith(".seed.jsonl")}
    if directory.replace("\\", "/").rstrip("/").endswith("seed_docs") and "runs" in contents:
        # Must be excluded one level up (here), not from inside seed_docs/runs itself — by the
        # time copytree would call this ignore function *on* seed_docs/runs, it has already
        # created that directory, leaving an empty (but existing) runs/ folder in the copy.
        ignored.add("runs")
    return ignored


def _workspace(tmp_path):
    for sub in ("braincode_loop", "datasets", "sources"):
        shutil.copytree(os.path.join(BASE_DIR, sub), tmp_path / sub, ignore=_ignore_generated_artifacts)
    (tmp_path / "docs").mkdir()
    (tmp_path / "runs").mkdir()
    reset_workspace(str(tmp_path))
    with open(os.path.join(BASE_DIR, "config", "config.yaml"), "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    config["run"]["dry_run"] = True
    config["budget"]["max_iterations"] = 2
    return config


def test_dry_run_end_to_end(tmp_path):
    config = _workspace(tmp_path)
    Orchestrator(config, base_dir=str(tmp_path)).run()

    spec = (tmp_path / "docs" / "language-spec.md").read_text(encoding="utf-8")
    assert "**Status:** bootstrapped" in spec
    assert "### `entity-ref`" in spec and "### `cond-branch`" in spec
    assert spec.count("### `seq`") == 1  # bootstrap add + steady-state revise -> one section
    assert "zero steps is a no-op" in spec  # the revise landed
    assert "empty list does nothing" in (tmp_path / "docs" / "glossary.md").read_text(encoding="utf-8")
    assert "**Version:** 1.2.0" in spec  # 1.0.0 (bootstrap) -> 1.1.0 -> 1.2.0: MINOR wins over PATCH each sprint

    changelog = (tmp_path / "docs" / "changelog.md").read_text(encoding="utf-8")
    assert "## Sprint 0 (bootstrap, attempt 1/3)" in changelog
    assert "## Sprint 1 (attempt 1/3)" in changelog and "## Sprint 2 (attempt 1/3)" in changelog
    assert "**Pre-KPI assessment:**" in changelog and "**Simulated examples:**" in changelog
    assert "→ `" in changelog  # a simulated braincode expression was written out
    assert "$0.0000" not in changelog or "Cost this sprint" in changelog

    backlog = (tmp_path / "docs" / "backlog.md").read_text(encoding="utf-8")
    assert "| 0 | `entity-ref` | accepted |" in backlog
    assert "| 1 | `cond-branch` | accepted |" in backlog and "| 1 | `seq` | accepted |" in backlog

    with open(tmp_path / "runs" / "kpi_history.jsonl", "r", encoding="utf-8") as f:
        records = [json.loads(line) for line in f if line.strip()]
    assert [r["sprint"] for r in records] == [0, 1, 2]
    assert all(r["simulations"] and r["kpi_assessment"]["coverage"]["impact"] for r in records)
    assert records[0]["cross_check"]["script_note"].startswith("run")

    with open(tmp_path / "runs" / "budget_log.json", "r", encoding="utf-8") as f:
        log = json.load(f)
    roles = {c["role"] for c in log["calls"]}
    assert roles == {"searcher", "shaper", "critic", "documenter", "cross_check_translator"}
    assert log["summary"]["sprints_completed"] == 2


def test_reset_restores_seed_state(tmp_path):
    config = _workspace(tmp_path)
    Orchestrator(config, base_dir=str(tmp_path)).run()
    assert (tmp_path / "runs" / "kpi_history.jsonl").exists()
    reset_workspace(str(tmp_path))
    assert not (tmp_path / "runs" / "kpi_history.jsonl").exists()
    assert not (tmp_path / "runs" / "budget_log.json").exists()
    spec = (tmp_path / "docs" / "language-spec.md").read_text(encoding="utf-8")
    assert "**Version:** 0.1.0" in spec and "not yet bootstrapped" in spec
    assert "*(Empty at seed.)*" in (tmp_path / "sources" / "previous_work.md").read_text(encoding="utf-8")
