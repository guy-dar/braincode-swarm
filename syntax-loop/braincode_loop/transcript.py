"""Full prompt/response transcript logging — a separate, much larger and more detailed log than
runs/logs/<run>/orchestration.log, meant to answer "what did the agents actually say to each
other" (previously not persisted anywhere at all). Opt-out via --no-log-file, same as the
orchestration log. Not truncated or compressed by design — that would defeat the purpose; the
accepted tradeoff is a log file that can grow large on a long run, since the full spec/glossary/
critique JSON gets re-sent every attempt.
"""
from __future__ import annotations

import datetime

_BAR = "=" * 80


class TranscriptLogger:
    """Constructed with a file path, or None to be a no-op (mirrors --no-log-file)."""

    def __init__(self, path: str | None):
        self.path = path

    def _write(self, block: str) -> None:
        if not self.path:
            return
        with open(self.path, "a", encoding="utf-8") as f:
            f.write(block)

    @staticmethod
    def _label(sprint: int, attempt: int, bootstrap: bool) -> str:
        label = "Sprint 0 (bootstrap)" if bootstrap else f"Sprint {sprint}"
        return f"{label} attempt {attempt}"

    def log_call(
        self, *, sprint: int, attempt: int, bootstrap: bool, role: str, provider: str, model: str,
        system_prompt: str, user_prompt: str, response_text: str, cost_usd: float,
        parse_error: str | None = None,
    ) -> None:
        if not self.path:
            return
        ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        header = f"{self._label(sprint, attempt, bootstrap)} — {role} ({provider}/{model}) — {ts}"
        block = (
            f"{_BAR}\n{header}\n{_BAR}\n"
            f"--- SYSTEM ---\n{system_prompt}\n\n"
            f"--- USER ---\n{user_prompt}\n\n"
            f"--- RESPONSE ---\n{response_text}\n\n"
        )
        if parse_error:
            block += f"PARSE ERROR: {parse_error}\n\n"
        block += f"Cost: ${cost_usd:.4f}\n\n"
        self._write(block)

    def log_iteration_summary(
        self, *, sprint: int, attempt: int, max_attempts: int, bootstrap: bool, decision: str,
        critique: dict, cost_usd: float,
    ) -> None:
        if not self.path:
            return
        ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        header = f"{self._label(sprint, attempt, bootstrap)}/{max_attempts} — ITERATION SUMMARY — {ts}"
        kpi = critique.get("kpi_assessment") or {}
        reqs = critique.get("required_changes") or []
        req_lines = "".join(f"  - {r.get('target', '?')}: {r.get('change', '')}\n" for r in reqs) or "  (none)\n"
        block = (
            f"{_BAR}\n{header}\n{_BAR}\n"
            f"Decision: {decision}\n"
            f"Critic reasoning: {critique.get('reasoning', '')}\n"
            f"Required changes:\n{req_lines}"
            f"KPI assessment: {kpi}\n"
            f"Cost this attempt: ${cost_usd:.4f}\n\n"
        )
        self._write(block)
