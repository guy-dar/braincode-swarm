"""Two `run.py` invocations must never race on the same shared docs_dir/runs_dir — a real
incident happened where that produced double real spend and a risk of corrupted, interleaved
writes. See braincode_loop/run_lock.py and orchestrator.py::Orchestrator.run()."""
import os
import time

import pytest
from test_dry_run_smoke import _workspace

from braincode_loop import run_lock
from braincode_loop.orchestrator import Orchestrator


def test_second_run_refuses_while_a_lock_is_active(tmp_path):
    config = _workspace(tmp_path)
    runs_dir = os.path.join(str(tmp_path), "runs")
    run_lock.acquire(runs_dir)
    try:
        orch = Orchestrator(config, base_dir=str(tmp_path))
        with pytest.raises(run_lock.RunAlreadyActive):
            orch.run()
    finally:
        run_lock.release(runs_dir)


def test_lock_is_released_after_a_normal_run(tmp_path):
    config = _workspace(tmp_path)
    orch = Orchestrator(config, base_dir=str(tmp_path))
    orch.run()
    assert not os.path.exists(os.path.join(str(tmp_path), "runs", ".run.lock"))


def test_lock_is_released_even_if_the_run_crashes(tmp_path):
    config = _workspace(tmp_path)
    orch = Orchestrator(config, base_dir=str(tmp_path))

    def boom(*args, **kwargs):
        raise RuntimeError("simulated crash")

    orch.searcher.ground_basis = boom  # not a ValueError, so nothing catches it — must still unlock

    with pytest.raises(RuntimeError):
        orch.run()
    assert not os.path.exists(os.path.join(str(tmp_path), "runs", ".run.lock"))


def test_a_stale_lock_is_reclaimed_instead_of_blocking_forever(tmp_path):
    """A process killed hard enough to skip its own `finally` (e.g. Stop-Process -Force, which is
    exactly what happened in the real incident this guards against) leaves its lock behind
    forever otherwise — it must age out rather than block every future run permanently."""
    config = _workspace(tmp_path)
    runs_dir = os.path.join(str(tmp_path), "runs")
    run_lock.acquire(runs_dir)
    lock_path = os.path.join(runs_dir, ".run.lock")
    stale_time = time.time() - run_lock._STALE_AFTER_SECONDS - 10
    os.utime(lock_path, (stale_time, stale_time))

    orch = Orchestrator(config, base_dir=str(tmp_path))
    orch.run()  # must not raise — the stale lock should be reclaimed, not treated as active

    assert not os.path.exists(lock_path)  # released normally once this run finished
