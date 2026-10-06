"""Small shared helpers: JSON extraction from LLM text, expression canonicalization.

LLM JSON output fails to parse for a handful of recurring, well-understood reasons — this module
handles each one explicitly rather than just retrying and hoping, since every failed parse costs a
real retried API call (see roles/base_role.py's retry loop) or, worse, an entire wasted attempt
(see orchestrator.py's malformed-response handling) if retries are exhausted:

- prose or a ```json fence wrapped around the object
- a trailing comma before `}`/`]` (a common LLM slip, invalid in strict JSON)
- a literal, unescaped newline/tab inside a string value (very common in fields like `grammar` or
  `semantics` that legitimately contain multi-line content) — Python's `json` module rejects this
  under `strict=True` (the default) but accepts it under `strict=False`
- the response being cut off mid-object (hit a token/length limit, or a transport-level
  truncation) — recovered on a best-effort basis by auto-closing whatever strings/brackets were
  still open, optionally trimming a final incomplete trailing member first
"""
from __future__ import annotations

import json
import logging
import re

logger = logging.getLogger("braincode_loop")

_FENCE_RE = re.compile(r"```(?:json)?\s*(.*?)\s*```", re.DOTALL | re.IGNORECASE)
_TRAILING_COMMA_RE = re.compile(r",(\s*[}\]])")
_CLOSERS = {'"': '"', "{": "}", "[": "]"}


def _strip_code_fence(text: str) -> str | None:
    match = _FENCE_RE.search(text)
    return match.group(1) if match else None


def _remove_trailing_commas(candidate: str) -> str:
    return _TRAILING_COMMA_RE.sub(r"\1", candidate)


def _scan_balanced_or_truncated(text: str, start: int) -> tuple[str | None, list[str]]:
    """Scan a JSON object/array starting at `start` (text[start] is '{' or '['), tracking
    string/escape state so braces inside quoted values don't throw off the boundary. Returns
    `(candidate, [])` if it closes cleanly (candidate = text[start:end+1]), or `(None, stack)`
    with the still-open bracket/string markers (innermost last) if the text runs out first."""
    stack: list[str] = []
    in_string = False
    escape = False
    for i in range(start, len(text)):
        ch = text[i]
        if in_string:
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == '"':
                in_string = False
            continue
        if ch == '"':
            in_string = True
        elif ch in "{[":
            stack.append(ch)
        elif ch in "}]":
            if stack:
                stack.pop()
            if not stack:
                return text[start : i + 1], []
    if in_string:
        stack.append('"')  # closed first on repair, since it's the innermost open thing
    return None, stack


def _extract_first_json_object(text: str) -> str | None:
    start = text.find("{")
    if start == -1:
        return None
    candidate, _ = _scan_balanced_or_truncated(text, start)
    return candidate


def _repair_truncated_json(text: str, max_lines_to_trim: int = 20) -> str | None:
    """Best-effort recovery when the response was cut off mid-object: close whatever strings and
    brackets were still open at EOF. If that alone doesn't yield valid JSON (e.g. truncation left
    a dangling `"key":` with no value), progressively drop the last line and retry — a bounded,
    cheap way to fall back to the last point the response was actually complete, rather than
    discarding the whole (possibly mostly-good) response."""
    start = text.find("{")
    if start == -1:
        return None
    working = text
    for _ in range(max_lines_to_trim + 1):
        candidate, stack = _scan_balanced_or_truncated(working, start)
        if candidate is not None:
            return None  # it closes cleanly — not actually truncated, nothing to repair
        if not stack:
            return None  # no content at all after `start` — nothing to recover
        repaired = working[start:] + "".join(_CLOSERS[tok] for tok in reversed(stack))
        for attempt in (repaired, _remove_trailing_commas(repaired)):
            try:
                json.loads(attempt, strict=False)
                return attempt
            except json.JSONDecodeError:
                continue
        # Didn't parse even after closing brackets — the last line likely ends mid-value
        # (e.g. `"key": ` with nothing after the colon). Drop it and try again.
        trimmed = working.rstrip().rsplit("\n", 1)
        if len(trimmed) < 2:
            return None
        working = trimmed[0]
    return None


def parse_json_response(text: str) -> dict:
    """Best-effort JSON extraction from raw LLM output — see module docstring for the specific
    failure modes this recovers from."""
    candidates = [text.strip()]
    fenced = _strip_code_fence(text)
    if fenced is not None:
        candidates.append(fenced.strip())

    for candidate in candidates:
        try:
            return json.loads(candidate, strict=False)
        except json.JSONDecodeError:
            pass

    for source in candidates:
        balanced = _extract_first_json_object(source)
        if not balanced:
            continue
        for attempt in (balanced, _remove_trailing_commas(balanced)):
            try:
                return json.loads(attempt, strict=False)
            except json.JSONDecodeError:
                continue

    for source in candidates:
        repaired = _repair_truncated_json(source)
        if repaired:
            try:
                result = json.loads(repaired, strict=False)
            except json.JSONDecodeError:
                continue
            logger.warning(
                "Recovered a likely-truncated JSON response by auto-closing open strings/"
                "brackets (and possibly trimming an incomplete trailing line) — some trailing "
                "content may be missing from the result."
            )
            if isinstance(result, dict):
                result["_truncated"] = True  # callers that need a complete answer can reject it
            return result

    raise ValueError(
        f"Could not parse JSON from model response (first/last 200 chars shown): "
        f"{text[:200]!r} ... {text[-200:]!r}"
    )


def format_attempt_label(attempt: int, max_attempts: int, *, large_threshold: int = 20) -> str:
    """'(attempt N/M)' when M is a meaningful ceiling, else just '(attempt N)' — 'attempt 4/100'
    reads like 100 is an expected number of tries, when it's really a practically-unbounded safety
    cap (see config.yaml -> run.bootstrap.max_attempts)."""
    if max_attempts <= 1:
        return ""
    if max_attempts > large_threshold:
        return f"(attempt {attempt})"
    return f"(attempt {attempt}/{max_attempts})"


def canonicalize_expression(expr: str) -> str:
    """Cheap canonical form for comparing two BrainCode expressions: collapse whitespace,
    lowercase, strip trailing punctuation. Not a real parser — only catches trivial formatting
    differences."""
    s = expr.strip().lower()
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"\s*[.,;]+$", "", s)
    return s.strip()
