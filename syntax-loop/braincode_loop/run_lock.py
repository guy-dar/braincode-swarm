"""Stops two `run.py` invocations from racing on the same shared docs_dir/runs_dir at once.

This isn't hypothetical: a real incident happened where two `python run.py` processes ended up
running concurrently against the same live workspace, each independently spending real API money
and both writing to the same files (docs/language-spec.md, runs/kpi_history.jsonl, etc.) with no
coordination. A simple lock file closes that gap.

This deliberately does NOT use the classic POSIX "is this PID alive" check
(`os.kill(pid, 0)` raises if the process is gone). On Windows, `os.kill(pid, sig)` doesn't have a
signal-0 special case the way POSIX does — passing 0 goes through `TerminateProcess(handle, 0)`,
which would actually kill whatever process currently happens to hold that PID. Since this project
runs on Windows, a PID-liveness check is not safe to use here.

Instead the lock's age decides staleness: a process that finishes normally (or crashes, since
`orchestrator.py::Orchestrator.run()` releases it from a `finally`) removes its own lock. A lock
older than `_STALE_AFTER_SECONDS` is assumed to be left over from a process that was killed hard
enough to skip that `finally` (e.g. `Stop-Process -Force`) and is safe to reclaim; real runs so
far finish in minutes, so the threshold is set far above any expected run length.
"""
from __future__ import annotations

import os
import time

_STALE_AFTER_SECONDS = 6 * 3600  # generous: real runs so far finish in minutes, not hours


class RunAlreadyActive(Exception):
    """Another run.py invocation appears to already be active against this runs_dir."""


def _lock_path(runs_dir: str) -> str:
    return os.path.join(runs_dir, ".run.lock")


def acquire(runs_dir: str) -> None:
    os.makedirs(runs_dir, exist_ok=True)
    path = _lock_path(runs_dir)
    if os.path.exists(path):
        age_seconds = time.time() - os.path.getmtime(path)
        if age_seconds < _STALE_AFTER_SECONDS:
            with open(path, "r", encoding="utf-8") as f:
                held_by = f.read().strip() or "unknown process"
            raise RunAlreadyActive(
                f"Another run appears to already be active against {runs_dir!r} "
                f"(lock held by {held_by}, created {age_seconds:.0f}s ago). Two runs sharing the "
                f"same docs/runs directories will race on the same files and can double real "
                f"spend. If you're sure no other run is actually active (e.g. it crashed without "
                f"cleaning up), delete {path!r} and try again."
            )
        # Older than the staleness ceiling — almost certainly abandoned by a process that was
        # killed before it could reach its own `finally` block. Safe to reclaim.
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"pid={os.getpid()} started={time.strftime('%Y-%m-%d %H:%M:%S')}\n")


def release(runs_dir: str) -> None:
    path = _lock_path(runs_dir)
    try:
        os.remove(path)
    except FileNotFoundError:
        pass
