"""Budget and iteration guardrails for the syntax-creation loop.

Every LLM call in the loop must go through BudgetTracker.record_call(); every role call checks
BudgetTracker.check() (or ensure_available(), which raises) before spending anything. Whichever
limit is hit first — dollars or sprints — stops the run. Checked before every individual LLM
call, not just at sprint boundaries, so a run never overshoots either cap mid-sprint.
"""
from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass, field
from datetime import datetime

_EMPTY_TOTALS = {"total_usd": 0.0, "by_provider": {}, "runs": []}


def read_total_spend_data(path: str) -> dict:
    """Full persisted cross-run structure — `{total_usd, by_provider, runs}`. `runs` is
    append-only, oldest-to-newest (new entries pushed to the end; a "last N" print is
    `data["runs"][-N:]`). Separate from `budget_log.json`, which is one run's own detail and gets
    overwritten every invocation. Missing/corrupt file reads as empty, not an error — this is for
    visibility, not authoritative billing data."""
    if not os.path.exists(path):
        return dict(_EMPTY_TOTALS, by_provider={}, runs=[])
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return {
            "total_usd": float(data.get("total_usd", 0.0)),
            "by_provider": {k: float(v) for k, v in (data.get("by_provider") or {}).items()},
            "runs": list(data.get("runs") or []),
        }
    except (json.JSONDecodeError, OSError, ValueError, TypeError):
        return dict(_EMPTY_TOTALS, by_provider={}, runs=[])


def read_total_spent(path: str) -> float:
    """Thin convenience wrapper for callers that only need the scalar total."""
    return read_total_spend_data(path)["total_usd"]


def add_to_total_spent(path: str, run_spent_usd: float, by_provider: dict[str, float]) -> dict:
    """Adds this run's spend (overall + per-provider) to the persisted cross-run total and
    appends one `runs` entry with a timestamp. Returns the full updated structure. Callers must
    only call this for real spend — never for a dry run's fabricated costs."""
    data = read_total_spend_data(path)
    data["total_usd"] = round(data["total_usd"] + run_spent_usd, 4)
    for provider, cost in by_provider.items():
        data["by_provider"][provider] = round(data["by_provider"].get(provider, 0.0) + cost, 4)
    data["runs"].append({
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "spent_usd": round(run_spent_usd, 4),
        "by_provider": {k: round(v, 4) for k, v in by_provider.items()},
    })
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    return data


def format_burndown(data: dict, *, max_budget_usd: float, run_cap: int = 10) -> str:
    """Multi-line block: total + this run's cap, per-provider breakdown, last `run_cap` runs
    (oldest first) — the file keeps full history regardless of this display cap, which exists so
    the log line doesn't grow unbounded over months of runs."""
    lines = [f"  Total spent across all real runs: ${data['total_usd']:.4f} (this run's cap: ${max_budget_usd:.2f})"]
    lines.append("  By provider:")
    for provider, cost in sorted(data.get("by_provider", {}).items()):
        lines.append(f"    - {provider}: ${cost:.4f}")
    runs = data.get("runs", [])[-run_cap:]
    lines.append(f"  Last {len(runs)} run(s) (oldest first):")
    for r in runs:
        per = ", ".join(f"{p}=${c:.4f}" for p, c in sorted((r.get("by_provider") or {}).items()))
        lines.append(f"    - {r.get('timestamp', '?')}  ${r.get('spent_usd', 0):.4f}  ({per})")
    return "\n".join(lines)


class BudgetExceeded(Exception):
    """Raised when an LLM call would be attempted after a limit has already been reached."""


@dataclass
class CallRecord:
    sprint: int
    role: str
    provider: str
    model: str
    input_tokens: int
    output_tokens: int
    cost_usd: float
    timestamp: float = field(default_factory=time.time)


class BudgetTracker:
    def __init__(self, max_budget_usd: float = 20.0, max_iterations: int = 40):
        if max_budget_usd <= 0:
            raise ValueError("max_budget_usd must be positive")
        if max_iterations <= 0:
            raise ValueError("max_iterations must be positive")
        self.max_budget_usd = float(max_budget_usd)
        self.max_iterations = int(max_iterations)
        self.spent_usd = 0.0
        self.iteration = 0  # completed sprints
        self.calls: list[CallRecord] = []

    def status(self) -> tuple[bool, str | None]:
        """Return (ok, reason). ok=False means the run must stop before doing more work."""
        if self.spent_usd >= self.max_budget_usd:
            return False, (
                f"budget_exhausted (${self.spent_usd:.2f} spent >= "
                f"${self.max_budget_usd:.2f} max)"
            )
        if self.iteration >= self.max_iterations:
            return False, (
                f"max_iterations_reached ({self.iteration} sprints >= "
                f"{self.max_iterations} max)"
            )
        return True, None

    def ensure_available(self) -> None:
        ok, reason = self.status()
        if not ok:
            raise BudgetExceeded(reason)

    def remaining_budget_usd(self) -> float:
        return max(0.0, self.max_budget_usd - self.spent_usd)

    def remaining_iterations(self) -> int:
        return max(0, self.max_iterations - self.iteration)

    def record_call(
        self,
        *,
        sprint: int,
        role: str,
        provider: str,
        model: str,
        input_tokens: int,
        output_tokens: int,
        cost_usd: float,
    ) -> None:
        self.spent_usd += cost_usd
        self.calls.append(
            CallRecord(
                sprint=sprint,
                role=role,
                provider=provider,
                model=model,
                input_tokens=input_tokens,
                output_tokens=output_tokens,
                cost_usd=cost_usd,
            )
        )

    def spent_by_provider(self) -> dict[str, float]:
        out: dict[str, float] = {}
        for call in self.calls:
            out[call.provider] = round(out.get(call.provider, 0.0) + call.cost_usd, 4)
        return out

    def complete_sprint(self) -> None:
        self.iteration += 1

    def summary(self) -> dict:
        return {
            "spent_usd": round(self.spent_usd, 4),
            "max_budget_usd": self.max_budget_usd,
            "sprints_completed": self.iteration,
            "max_iterations": self.max_iterations,
            "num_calls": len(self.calls),
        }

    def write_log(self, path: str) -> None:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "summary": self.summary(),
                    "calls": [c.__dict__ for c in self.calls],
                },
                f,
                indent=2,
            )
