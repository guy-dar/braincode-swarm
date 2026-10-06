# BrainCode Syntax Changelog

Append-only. One entry per attempt, written by the Documenter role. Each entry records: what set
of changes was proposed and by which model, the Critic's decision and its benefit/harm judgment
per pre-KPI, the sampled dataset items it simulated (with the BrainCode expressions it produced),
whether independent cross-provider translations were available, the required changes it asked
for, and the final decision. This is the audit trail for "what did this specific syntax change
actually contribute" — the raw records also land in `../runs/kpi_history.jsonl`.

No decision recorded here is gated on a statistical test. The Critic's critical judgment is the
decision; the scripted doc-hygiene check (every change has a gloss + worked example) is the only
override.

*(Empty at seed. Sprint 0, when it runs, appears first.)*

<!-- Format written by the Documenter role:

## Sprint 0 (bootstrap, attempt A/N) — YYYY-MM-DD

- **Language version:** 0.1.0 → 1.0.0 (MAJOR — establishes the base syntax)
- **Inspiration languages:** <1-2 sentences citing which language inspired which choice>
- **Shaper proposal (model: <provider/model>):** <summary>
- **Changes:** `entity-ref` (add, MAJOR), `action` (add, MAJOR), ...
- **Critic decision:** accept | needs-rework | reject — <reasoning>
- **Doc hygiene:** pass | FAIL — <detail>
- **Pre-KPI assessment:**
  - coverage: benefit | harm | neutral | mixed — <reasoning>
  - expressivity / determinism / interpretability / improvement: ...
- **Simulated examples:**
  - `<item_id>` (<source>) [Full|Partial|Fail] NL: "..." → `<braincode>` — <notes>
- **Cross-check:** used=true|false, agreement=high|partial|low|n/a — <notes>
- **Required changes:** (when not accepted, or when the Critic still sees improvements)
  - `<target>`: <concrete edit>
- **Decision:** accepted | needs-rework | rejected
- **Documenter summary:** <1-3 sentences>
- **Cost this sprint:** $X.XX

## Sprint N (attempt A/M) — YYYY-MM-DD

- **Language version:** 1.0.0 → 1.1.0 (MINOR/PATCH)
- **Candidate task:** <the sampled dev task>
- **Shaper proposal (model: <provider/model>):** <summary>
- **Changes:** `<name>` (add|revise, MAJOR|MINOR|PATCH), ...
- ... same trail blocks as above ...

-->

## Sprint 0 (bootstrap) (attempt 1) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 2) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 3) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 4) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 5) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 6) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 7) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 8) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 9) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 10) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 11) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 12) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 13) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 14) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 15) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 16) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 17) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 18) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 19) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 20) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 21) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 22) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 23) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 24) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 25) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 26) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 27) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 28) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 29) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 30) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 31) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 32) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 33) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 34) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 35) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 36) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 37) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 38) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 39) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 40) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 41) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 42) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 43) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 44) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 45) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 46) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 47) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 48) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 49) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 50) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 51) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 52) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 53) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 54) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 55) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 56) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 57) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 58) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 59) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 60) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 61) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 62) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 63) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 64) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 65) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 66) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 67) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 68) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 69) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 70) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 71) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 72) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 73) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 74) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 75) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 76) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 77) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 78) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 79) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 80) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 81) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 82) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 83) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 84) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 85) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 86) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 87) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 88) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 89) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 90) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 91) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 92) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 93) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 94) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 95) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 96) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 97) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 98) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 99) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap) (attempt 100) — 2026-09-21

- **Shaper failed to produce a usable proposal:** the response never parsed as JSON after retries (Streaming is required for operations that may take longer than 10 minutes. See https://github.com/anthropics/anthropic-sdk-python#long-requests for more details).
- **Decision:** needs-rework (no proposal to assess)

## Sprint 0 (bootstrap, attempt 1) — 2026-09-22

- **Language version:** 0.1.0 → 0.1.0 (MAJOR — establishes the base syntax)
- **Inspiration languages:** Python inspired the flat, non-nested top-to-bottom statement sequencing and the preference for 'one obvious way to do it' in argument passing; HTML inspired separating an action's core verb from its stylistic/contextual key=value attributes; English supplied the closed-class function words (and/or/not/if/then/else/for each) that carry BrainCode's logical structure; formal-language-theory concerns motivated replacing indentation-sensitivity with explicit block-closing keywords to keep the grammar strictly context-free and deterministically parseable.
- **Shaper proposal (model: anthropic/claude-sonnet-5):** Establishes a six-construct orthogonal core — lexical primitives, Action, Sequence/Binding, Task, Condition, and Iteration — covering effectful primitives, decomposition, data flow, boolean logic, and looping with explicit evaluation-order and precedence rules.
- **Changes:** `Lexical Primitives` (add, MAJOR), `Action` (add, MAJOR), `Sequence & Binding` (add, MAJOR), `Task` (add, MAJOR), `Condition` (add, MAJOR), `Iteration` (add, MAJOR)
- **Critic decision:** needs-rework — The proposed basis has useful structural intent: explicit blocks, sequencing, bindings, precedence, short-circuiting, and iteration improve several operational simulations. It cannot be accepted as Sprint 0 because central constructs contradict their grammar and essential runtime/scoping semantics are absent. Most notably, task definitions and quantifiers do not parse where their own semantics and examples require them, while unconstrained Action naming causes pronounced independent-translation divergence.
- **Doc hygiene:** pass — All changes carry a complete glossary entry (gloss + worked example).
- **Pre-KPI assessment:**
  - coverage: mixed — The action-with-attributes pattern can encode requests from embodied control, shopping, software repair, planning, health explanation, and creative writing, as the simulations show. However, this coverage is achieved primarily by allowing arbitrary action names and opaque quoted-string payloads rather than by defined semantic structure; important common data such as lists, structured records, dates, monetary comparisons, and content constraints have no native representation.
  - expressivity: mixed — The proposal preserves sequencing, simple data flow, branching, iteration, and several request attributes such as audience, tone, quantities, and style. But condition semantics do not define the truth value of variable references, task definitions cannot actually appear in a program, quantifiers are claimed usable in conditions but excluded from the condition grammar, and strings become the only way to preserve many structured details, including code, recipes, and creative prompts.
  - determinism: harm — Independent translations visibly diverge on core action naming and argument schemas: getObjects/find, send/send_follow_up, find_motherboard/find, prepare/get_cup_ready, explain/request, say/hello, and numerous incompatible attribute names. Since all undefined calls are valid Actions, the language supplies no canonical vocabulary, ontology, or normalization rule that would make those alternatives equivalent rather than merely similar. The call-site task/action resolution also makes an otherwise identical call change meaning when a task definition exists elsewhere in scope.
  - interpretability: mixed — Explicit end delimiters, key=value attributes, sequencing, precedence, and short-circuit rules are helpful. Yet the grammar contradicts its own examples and semantics: task_def is not a statement, task bodies cannot end with a variable reference despite the Django example doing so, and quantifiers are absent from bool_expr atoms. Undefined action names, action result shapes, collection types, variable truthiness, and branch/loop binding visibility prevent a reader with only the glossary from reliably recovering execution behavior.
  - improvement: mixed — The explicit structures materially help an agent execute the pillow transfer, conditional follow-up, shopping dependency, and recipe meal-prep request. For many informational or creative requests, however, the expression is only a renamed arbitrary action with a long prompt string, which adds little planning guidance over natural language; broken task and conditional semantics would also hinder an executor on nontrivial decompositions.
- **Simulated examples:**
  - `dev-embodied-2` (seed_tasks) [Full] NL: "Put both pillows from the sofa onto the armchair, one at a time." → `let pillows = find_objects(type="pillow", location="sofa")
for each pillow in $pillows:
  move(item=$pillow, destination="armchair")
end` — Iteration and sequential loop-body execution preserve "both" and "one at a time"; Action names remain unconstrained.
  - `dev-email-2` (seed_tasks) [Full] NL: "If my manager hasn't replied by Friday, send a polite follow-up; otherwise do nothing." → `if not has_replied(person="my manager", by="Friday") then
  send_follow_up(recipient="my manager", tone="polite")
end` — Condition handles the negative branch condition. Omitted else is intended to mean no action, but that behavior is not expressly specified.
  - `e344b89e-767a-4618-ba82-4b81cdcba280` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "add a motherboard under $200 and a compatible processor at any price to the shopping cart." → `let motherboard = find_product(category="motherboard", max_price=200)
let processor = find_product(category="processor", compatible_with=$motherboard)
add_to_cart(item=$motherboard)
add_to_cart(item=$processor)` — Binding captures compatibility dependency. Currency is implicit in max_price=200 because number literals carry no unit.
  - `f118238f-ef8f-4b63-9159-a81e981ef46e` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Add decorative LED Candles to the cart." → `add_to_cart(item="decorative LED Candles")` — Action is sufficient; proposed iteration, tasks, and conditions are irrelevant.
  - `trial_T20190906_214148_552057#1` (ALFRED (json_2.1.0, train)) [Full] NL: "get a cup ready for coffee" → `prepare(item="cup", purpose="coffee")` — The terse request can be represented, although the intended embodied substeps are delegated entirely to an undefined action.
  - `trial_T20190908_102045_139402#1` (ALFRED (json_2.1.0, train)) [Full] NL: "To put the toilet paper away." → `put_away(item="toilet paper")` — Action captures the high-level goal but does not expose the intended holder destination.
  - `sympy__sympy-15345` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "mathematica_code gives wrong output with Max. mathematica_code(Max(x,2)) should produce Max[x,2], but produces Max(2, x)." → `fix_bug(component="sympy/printing/mathematica.py", issue="mathematica_code gives wrong output with Max", reproduction="x = symbols(\"x\"); mathematica_code(Max(x,2))", expected="Max[x,2]", actual="Max(2, x)", requirement="emit valid Mathematica Max syntax")` — The defect facts fit as attributes, but code and expected behavior are opaque strings rather than typed code/test constructs.
  - `django__django-15098` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "Django i18n_patterns fails for locale tags containing script and region, including en-latn-us and en-Latn-US; update locale handling so these valid RFC 5646 forms return 200." → `fix_bug(component="django/utils/translation/trans_real.py", issue="i18n_patterns rejects locale tags containing script and region", failing_cases="en-latn-us; en-Latn-US", expected_status=200, standard="RFC 5646", requirement="accept language-script-region locale forms and normalize BCP 47 case")` — A single Action can preserve the repair request, but cannot encode test-case collections natively; semicolon-delimited cases are an opaque string.
  - `c5957` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Full] NL: "Please provide a recipe for high protein flatbread" → `provide_recipe(dish="flatbread", dietary_property="high protein")` — Action attributes capture the requested dish and constraint.
  - `c436` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Full] NL: "What places to visit in Bilbao" → `recommend_places(location="Bilbao")` — Simple recommendation request; no proposed control construct is needed.
  - `c996` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Full] NL: "What is your take on love?" → `answer_question(topic="love", response_kind="perspective")` — The request is expressible only through an arbitrary action schema, which differs substantially from other equally valid renderings such as ask(question=...).
  - `c4939` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Full] NL: "Is marriage important?" → `answer_question(topic="importance of marriage", response_kind="balanced perspective")` — Action can represent the question, though no formal mechanism distinguishes a question from an instruction except arbitrary verb choice.
  - `wildchat1m_en3u-129421` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-1106-preview)) [Full] NL: "Act as the composite persona Mark and explain in depth, in simple casual American style with formulas and concrete examples, how linear algebra converts text to model representations and representations back to answers in ChatGPT-4." → `explain(topic="how a model like ChatGPT-4 uses linear algebra to transform text into numerical representations and transform representations into answers", persona="Mark: composite of an American psycholinguist, Harvard-educated linear algebra professor, logical reasoning professor, and LLM/Transformers expert", depth="in depth", style="eloquent simple practical casual conversational American", include="mathematical notation, formulas, concrete numerical examples, 18th-century mathematician style")` — The many persona and style requirements fit attributes, but their semantics are wholly delegated to undefined Action behavior.
  - `wildchat1m_en3u-148973` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-0125-preview)) [Full] NL: "Write a hilarious 17+ Scooby gang and Scrappy-Doo script reacting behind the scenes to badly translated sentences and roasting their errors, beginning with the supplied Jeopardy robot sentence." → `write_script(characters="Scooby gang; Scrappy-Doo", setting="behind the scenes", genre="hilarious comedy", audience_rating="17+", activity="react to, question, and roast errors, inconsistencies, and names in a badly translated sentence", recurring_device="characters imagine silly mocking quotes", source_sentence="Velma and Shaggy compete on Jeopardy, hosted by Alex Trebek, but things go awry when a robot competitor begins attacking anyone who gets more points than him.")` — Creative constraints are retained as attributes, but this is effectively a structured wrapper around prompt text.
  - `wildchat1m_en3u-142592` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-0125-preview)) [Full] NL: "Please write steps for homiletics and engaging Christian sermons" → `write_steps(topic="homiletics and engaging Christian sermons", detail_level="practical")` — The request is represented, but no native structure requires a stepwise output beyond an undeclared action convention.
  - `wildchat1m_en3u-22638` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0301)) [Full] NL: "write an email introducing yourself and job position to other party asking for collaborations" → `write_email(recipient="other party", purpose="introduce sender and job position; request collaboration", register="professional")` — Recipient, purpose, and register are preserved as Action attributes.
  - `1775955172098` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Full] NL: "I need help planning a trip to Italy" → `plan_trip(destination="Italy")` — The underspecified request is representable; its missing duration, budget, and interests remain intentionally unspecified.
  - `1775612391896` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Full] NL: "hello" → `greet()` — A zero-argument Action works, but independent translations show arbitrary lexical choice between greet(), hello(), and say(text="hello").
  - `1775448065619` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Full] NL: "I want to start a healthy diet. Can you help me plan a simple meal prep for 3 days that includes breakfast, lunch, and dinner? I prefer high-protein options." → `plan_meal_prep(goal="healthy diet", simplicity="simple", days=3, meals="breakfast; lunch; dinner", dietary_preference="high-protein")` — Quantification and meals are represented as attributes, but the grammar has no list literal, forcing a semicolon-delimited string.
  - `1775760283577` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Full] NL: "Hi there, I am curious to learn a little about end-stage heart failure. Talk to me like you would a 5-year-old." → `explain(topic="end-stage heart failure", audience_age=5, depth="introductory", tone="gentle and easy to understand")` — Audience and tone are expressible as attributes; medical safety and uncertainty requirements are not language-level concepts.
- **Cross-check:** used=True, agreement=partial — The two providers generally agree on broad sequencing and on exact simple cases such as add_to_cart, put_away, plan_trip, and explain. They disagree pervasively on action vocabulary and attribute schemas (for example getObjects versus find, hasReplied versus has_replied, send versus send_follow_up, and say versus hello), and some supplied translations use unsupported values such as list literals or top-level task definitions; thus surface divergence is often semantic-schema divergence, not merely harmless formatting.
- **Required changes:**
  - `basis`: Define a complete grammar with a single program-item production: permit task_def wherever declarations are legal, state whether declarations may occur inside task/condition/loop bodies, and make the supplied Task examples parse. Either add a return statement or explicitly permit variable_ref as a statement if task bodies are intended to return `$result`.
  - `Condition`: Add quantifier to atom (or otherwise revise bool_expr) so `any(...)` and `all(...)` are syntactically usable as the Iteration semantics claim. Define boolean coercion for variable_ref, including which values are false, and define the value/result of a condition statement.
  - `Sequence & Binding`: Define lexical scopes and binding visibility for each condition branch and each loop iteration: specify whether branch-created bindings escape, whether a loop body may shadow an outer binding, whether bindings persist across iterations, and whether a binding must be initialized on all branches before later reference.
  - `Iteration`: Define the collection value type, empty-collection behavior, quantifier behavior on empty collections, and whether loop variable `x` is accessed as `$x`; revise grammar or semantics so that binding form and reference form are explicitly consistent.
  - `Action`: Replace the unspecified 'implicit result value' with a defined result model (at minimum scalar, ordered collection, record, and failure), define how an action definition declares a named boolean output field, and specify error propagation for failed nested actions and failed statements.
  - `Lexical Primitives`: Repair the string grammar so it formally defines allowed escaped characters and newline behavior; define the exact statement-separator rule, including whether a newline is required after comments and how `end else`-style token boundaries work. Add literals/types needed by the core examples, at least list and record literals or an explicit typed alternative, plus null and date/time or unit-bearing quantities.
  - `Task`: Define task namespace and declaration scope unambiguously: prohibit Action/task name collisions or require explicit `call` versus `action` syntax. Define argument validation against parameters, parameter binding evaluation order, task visibility, and a deterministic recursion/cycle policy; an executor-specific depth limit is not sufficient semantics for a formal language.
  - `basis`: Establish a canonical closed vocabulary or a separately versioned action-schema registry with canonical names and canonical attribute names for common operations. If arbitrary actions remain permitted, define a normalization/equivalence rule; otherwise independent translations cannot converge.
  - `Action`: Remove or constrain duplicate-key last-wins behavior. Prefer duplicate keys as a static error, since silent overriding loses user constraints such as two recipients, two quantities, or conflicting tone requirements.
- **Logic issues:** The Task grammar defines `task_def`, but `program ::= statement+` and `statement ::= binding | action | task_call | condition | iteration` omit task_def. Therefore every worked Task definition and any program containing one is syntactically invalid.; The Django Task worked example ends its task body with `$result`, but variable_ref is not a statement, so that example is also syntactically invalid even if task_def were admitted.; Iteration states that `any` and `all` are atoms usable anywhere a bool_expr atom is allowed, but Condition's `atom` production excludes `quantifier`.; Condition allows variable_ref as a boolean atom but never defines its boolean meaning; the worked example relies on `$results` as a found/nonempty predicate while separately calling is_empty.; A task call and primitive Action have identical syntax and are resolved based on whether a same-named task is in scope. Adding an unrelated definition can silently alter an existing call's meaning.; The phrase 'flat, non-nested execution order' conflicts with the actual nested task, conditional, iteration, and nested-action grammar, leaving the intended execution/scoping model unclear.; Action values omit collection and record literals, yet iteration requires actions or variables to yield ordered lists and common tasks require structured selections, lists of tests, or multiple items.; The implicit result type, Action output-field declaration mechanism, failure propagation, collection semantics, and truth conversion are not defined, so a conforming executor cannot determine many program outcomes.; Branch and loop binding lifetimes are unspecified; a later `$x` after `if ... let x ... end` or after a loop has no defined static validity or runtime value.; Duplicate argument keys silently discard an earlier user-provided constraint, which is deterministic operationally but not meaning-preserving.
- **Decision:** needs-rework
- **Documenter summary:** The Shaper proposed a 6-construct core (Lexical Primitives, Action, Sequence & Binding, Task, Condition, Iteration) drawing on Python's flat statement structure, HTML's element/attribute separation, English's closed-class connectives, and formal-language-theory's context-free parseability, with Parsel and ReAct cited as agentic-decomposition precedents. The Critic returned a needs-rework decision, judging Determinism harmed and Expressivity/Coverage/Interpretability mixed, most critically because task_def is not actually reachable from the program grammar and quantifiers are excluded from bool_expr atoms, making the basis's own worked examples (e.g. the Django task ending in $result) syntactically invalid despite otherwise successful simulations like the pillow-transfer and shopping-cart cases. Cross-provider simulation also showed pervasive divergence in action/attribute naming (e.g. getObjects vs find, send vs send_follow_up), underscoring the lack of a canonical vocabulary.
- **Cost this sprint:** $0.7262

## Sprint 0 (bootstrap, attempt 2) — 2026-09-22

- **Language version:** 0.1.0 → 0.1.0 (MAJOR — establishes the base syntax)
- **Inspiration languages:** Python motivates flat, explicitly-delimited sequential blocks and dotted-namespace calls (`act.foo(...)`); HTML motivates decoupling verbs from key=value attributes and the idea of a separately-versioned vocabulary/schema; English motivates the fixed-precedence closed-class logical connectives; Parsel motivates named, parameterized, returning task decomposition.
- **Shaper proposal (model: anthropic/claude-sonnet-5):** Revised the six-construct basis to make every worked example actually parse under its own grammar, add a typed value/result model with list/record/null/quantity literals, split the primitive-action and task namespaces, define block-local scoping with no branch-escaping bindings, make quantifiers legal boolean atoms with defined truthiness and empty-collection behavior, and replace silent duplicate-key override with a static error plus a versioned action-schema registry hook.
- **Changes:** `Lexical Primitives` (revise, MAJOR), `Action` (revise, MAJOR), `Sequence & Binding` (revise, MAJOR), `Task` (revise, MAJOR), `Condition` (revise, MAJOR), `Iteration` (revise, MAJOR)
- **Critic decision:** needs-rework — This is a promising structural core: explicit sequential execution, scoped bindings, namespace separation, lists, quantities, branch precedence, and list iteration are meaningful improvements over no language. It cannot be accepted because its mandatory external action registry is absent and several central semantics—especially Result versus value binding, failure handling, whitespace/block parsing, and non-empty loop results—are internally incomplete or contradictory. These defects prevent statically valid, deterministic translations for every sampled item and force most domain content back into opaque prose strings.
- **Doc hygiene:** pass — All changes carry a complete glossary entry (gloss + worked example).
- **Pre-KPI assessment:**
  - coverage: mixed — Lists, records, quantities, sequencing, conditionals, loops, and task decomposition make many embodied and workflow requests structurally expressible. However, every domain-specific operation depends on an unspecified external registry, so the proposed basis alone cannot provide a usable vocabulary for web navigation, code modification, research, advice, or text generation.
  - expressivity: mixed — The proposal preserves ordering, many values, quantities, basic branches, and iteration substantially better than an empty basis. It cannot reliably preserve important sampled constraints such as source citations, factual-currentness requirements, legal jurisdiction, exact document clauses, audience/register, uncertainty, or code-level edits without placing them inside opaque natural-language strings; it also has no field access, comparison, arithmetic, object selection, or explicit output-format mechanism.
  - determinism: harm — Fixed precedence, scopes, separators, and namespaces improve syntactic determinism, but the absence of a supplied registry and canonical action/key definitions leaves translators free to invent incompatible verbs such as act.search_web, act.answer_question, act.generate_text, and act.modify_file. The unclear distinction between a call's Result and its value further makes equivalent dataflow translations unlikely.
  - interpretability: mixed — The explicit schemas, lexical rules, scope rules, and short-circuit semantics are a useful start. Interpretability is undermined by undefined registry behavior, an unspecified whitespace/block-token treatment despite indentation in examples, inconsistent Result/value semantics, and an impossible claimed ability to inspect ok when no member-access or Result-binding syntax exists.
  - improvement: mixed — For simple embodied sequences and list iteration, explicit ordered calls would help a weaker executor. For most sampled advisory, writing, web, and software tasks, invented opaque action names and prose instructions in strings provide little actionable decomposition beyond the original request, while missing error inspection and result selection prevent reliable plans.
- **Simulated examples:**
  - `dev-embodied-2` (seed_tasks) [Partial] NL: "Put both pillows from the sofa onto the armchair, one at a time." → `#!schema:core@1
let pillows = act.find_objects(type="pillow", location="sofa")
for each pillow in $pillows:
  act.move(item=$pillow, destination="armchair")
end` — Iteration directly helps, but find_objects and move are invented registry entries and $pillows is ambiguous between a Result record and its value.
  - `dev-embodied-1` (seed_tasks) [Partial] NL: "Rinse the mug in the sink, then put it in the coffee maker." → `#!schema:core@1
let mug = act.find_object(type="mug")
act.rinse(item=$mug, location="sink")
act.move(item=$mug, destination="coffee maker")` — Sequence helps, but object-reference behavior and action vocabulary are not defined by core@1.
  - `86afd67c-1bff-455c-baa7-e18dcb64b0f3` (Mind2Web) [Partial] NL: "Find comedy tv shows on netflix sorted by audience score." → `#!schema:core@1
act.search_catalog(service="netflix", media_type="tv show", genre="comedy", sort="audience score descending")` — A single abstract action loses the supplied UI trajectory; canonical web action names and sort-value vocabulary are missing.
  - `bf469f30-6628-4017-b963-672645d7feab` (Mind2Web) [Partial] NL: "Find the highest rated dog collar under 10 dollar." → `#!schema:core@1
act.search_products(category="dog collar", price_max=10 usd, sort="rating descending", limit=1)` — Quantity supports the price constraint, but ranking semantics, selection, and the registry action/key vocabulary are unspecified.
  - `trial_T20190907_223758_523581#1` (ALFRED) [Partial] NL: "Microwave a slice of apple and place it on the table." → `#!schema:core@1
let apple_slice = act.find_object(type="apple slice")
act.heat(item=$apple_slice, appliance="microwave")
act.move(item=$apple_slice, destination="table")` — Ordering is represented, but the trajectory's slicing, appliance-door, pickup, and spatial-placement requirements are not recoverable from the brief request or core semantics.
  - `trial_T20190908_224836_919680#2` (ALFRED) [Partial] NL: "Put a microwaved slice of apple on the table in the corner." → `#!schema:core@1
let apple_slice = act.find_object(type="apple slice")
act.heat(item=$apple_slice, appliance="microwave")
act.move(item=$apple_slice, destination="table in the corner")` — Sequential heat-then-place is expressible, but object disambiguation and a compositional location representation are registry-dependent.
  - `scikit-learn__scikit-learn-11578` (SWE-bench_Verified) [Partial] NL: "Fix LogisticRegressionCV probabilistic scoring so LogisticRegression created in _log_reg_scoring_path inherits multi_class, with testing." → `#!schema:core@1
act.modify_source(file="sklearn/linear_model/logistic.py", change="Pass multi_class=multi_class when _log_reg_scoring_path constructs LogisticRegression for probabilistic scoring.")
act.run_tests(target="logistic regression probabilistic scoring", verify="multinomial predict_proba and scorer use multinomial behavior")` — The substantive code edit and test oracle are opaque prose strings; no syntax represents source locations, AST edits, assertions, patches, or test outcomes.
  - `django__django-13112` (SWE-bench_Verified) [Partial] NL: "Fix makemigrations crashing for a ForeignKey with a mixed-case app name." → `#!schema:core@1
act.modify_source(file="django/db/models/fields/related.py", change="Preserve or correctly resolve mixed-case installed-app labels in lazy ForeignKey references.")
act.run_tests(target="mixed-case app name ForeignKey migration")` — This is only an opaque instruction. The language lacks code-query, diagnosis, patch, and regression-test constructs.
  - `c6516` (PRISM) [Partial] NL: "What different foods would be great to try while in the Netherlands and can you recommend a good restaurant?" → `#!schema:core@1
act.answer_question(question="Recommend Dutch foods to try and a good restaurant in the Netherlands.")` — The two requested outputs are retained only in natural-language text. No research provenance, location, restaurant criteria, or answer-format representation exists.
  - `c3388` (PRISM) [Partial] NL: "Can you tell me a joke to help take my mind off pain I have had for nearly three years?" → `#!schema:core@1
act.generate_text(kind="joke", audience_context="user has been in pain for nearly three years", tone="gentle")` — A generator action can request a joke, but empathetic and safety-sensitive response behavior is unspecified and all names are invented.
  - `c2067` (PRISM) [Partial] NL: "If Supreme Court justices are appointed by the president, how is that fair?" → `#!schema:core@1
act.answer_question(question="Explain the fairness rationale and criticisms of United States Supreme Court justices being nominated by the president and confirmed by the Senate.", register="brief, balanced")` — Question, requested explanation, and balanced register are strings/undefined keys rather than core semantics.
  - `c2904` (PRISM) [Partial] NL: "Are you aware of current political events in Aotearoa for 2023?" → `#!schema:core@1
act.answer_question(question="Summarize current political events in Aotearoa/New Zealand for 2023.", require_current_sources=true)` — Temporal freshness and source verification have no defined semantics; require_current_sources is an invented registry key.
  - `wildchat1m_en3u-73283` (PATHs) [Partial] NL: "Introduce the topic of the impact of dam construction on seasonal precipitation pattern, land use/cover, and socio-economic conditions in semi-arid Eastern Sudan." → `#!schema:core@1
act.generate_text(kind="topic introduction", topic="Impact of dam construction on seasonal precipitation patterns, land use/cover, and socio-economic conditions in semi-arid Eastern Sudan", register="academic")` — The topic and requested genre are representable as string data only; the language has no composition, paragraph, citation, or claim-qualification structure.
  - `wildchat1m_en3u-76731` (PATHs) [Partial] NL: "Try to squeeze ideas of The Holy Blood and the Holy Grail-like conspiracy from The Brothers Karamazov." → `#!schema:core@1
act.generate_analysis(source_work="The Brothers Karamazov", comparison_work="The Holy Blood and the Holy Grail", focus="possible conspiracy-like thematic parallels", caveat="do not claim direct equivalence")` — The needed literary-analysis constraints are registry-dependent and do not distinguish evidence, speculation, and factual claims.
  - `wildchat1m_en3u-137561` (PATHs) [Partial] NL: "Write a story of when Gloopy and Glitter met the scientist, who is amazed they can speak." → `#!schema:core@1
act.generate_story(characters=["Gloopy", "Glitter", "a scientist"], premise="The scientist meets Gloopy and Glitter and is amazed that they can speak.", setting="Gloopiter")` — Creative generation can be requested, but narrative continuity, prior conversation canon, perspective, length, and style are absent from the core.
  - `wildchat1m_en3u-78000` (PATHs) [Partial] NL: "Write a legal document and contract for a high-demand speaker, saying there is not enough time and the speaker is in very high demand; add a binding signature line." → `#!schema:core@1
act.generate_document(kind="speaker engagement contract", party_role="speaker", premise="speaker has limited availability and high demand", include=["binding signature line"], register="professional legal")` — A legal contract requires jurisdiction, parties, consideration, clauses, and enforceability semantics that are not represented; this is an opaque generation request.
  - `1776009617894` (ThoughtTrace) [Partial] NL: "Can you suggest a posting schedule to help the Hamoudi children's educational YouTube channel grow quickly in its first month?" → `#!schema:core@1
act.create_plan(subject="Hamoudi children's educational YouTube channel", goal="growth in first month", deliverable="posting schedule")` — Planning is expressible only as a generic opaque action; frequency, calendar dates, platform constraints, and growth assumptions lack formal representation.
  - `1775429344935` (ThoughtTrace) [Partial] NL: "Help me create a text about my decision to go to Japan to learn about SGI. Only 100 words." → `#!schema:core@1
act.generate_text(topic="my decision to go to Japan to learn about SGI", word_limit=100, perspective="first person")` — The exact 100-word constraint is captured only if an undefined generator registry gives word_limit normative meaning; no core output-length semantics exists.
  - `1775752130482` (ThoughtTrace) [Partial] NL: "Hello, I want to plan a 3 day safari in Eastern Cape, South Africa." → `#!schema:core@1
act.create_itinerary(destination="Eastern Cape, South Africa", duration=3 days, activity="safari")` — Quantity is useful, but itinerary structure, dates, budget, bookings, current availability, and recommendations are all undefined registry behavior.
  - `1775479438859` (ThoughtTrace) [Partial] NL: "Give examples of short certifications in the UK that could lead to stable, mortgage-friendly employment." → `#!schema:core@1
act.answer_question(question="Give realistic UK examples of short certifications leading to stable employment suitable for mortgage applications.", include=["duration", "role", "employment-stability caveats"], register="actionable")` — The requested country-specific factual advice, lender caveats, and structured comparison are only informal registry arguments.
- **Cross-check:** used=False, agreement=low — No independent translations were supplied. Independent capable translators would likely agree on basic sequence and loop shapes for the two simple embodied tasks, but would diverge sharply on invented action names, action keys, abstraction level, and whether to encode complex requests as one generator call or decomposed calls because the required registry is absent.
- **Required changes:**
  - `basis`: Provide a normative minimal versioned action registry for the bootstrap schema (at least retrieval/search, select, navigate/click, move/manipulate, read/write/modify source, test, research, generate text, and present output), including each action's keys, types, effects, result type, canonical synonyms, and examples. A required but unavailable registry makes no proposed program statically checkable.
  - `Sequence & Binding`: Define exactly what let binds when its right-hand value is an action_call or task_call: the whole Result record or Result.value. Revise the flight, pillow, and task examples accordingly, and add explicit syntax for binding or inspecting the whole Result if it remains observable.
  - `Action`: Add Result field access or dedicated predicates/binders, such as $r.ok, $r.value, and $r.error, and define whether failures occurring in a condition become false, propagate, or may be explicitly handled. Remove the current claim that a Condition can check ok until such syntax exists.
  - `Lexical Primitives`: Define whitespace and indentation treatment globally, including whether leading spaces are ignored, and give a complete program grammar with required statement separators. The worked examples use indentation although the grammar only defines ws+ inside quantities and says the language is not indentation-sensitive.
  - `Condition`: Make not_expr recursively permit repeated negation (`'not' not_expr | atom`) or explicitly prohibit it in the semantics; the present grammar accepts only one not while the connective description implies a general unary operator.
  - `Task`: Replace the lexical guarded-recursion rule with a defined termination/resource model, or define precisely what lexically nested means for calls inside nested tasks/loops and why a condition counts as a guard. A condition whose predicate is always true still permits nontermination, while executor-specific depth behavior is not fully deterministic beyond the minimum.
  - `Iteration`: Define the Result of a non-empty for_each, including whether it is the final iteration's final statement Result, a list of Results, or null; currently only empty-loop behavior is specified.
  - `basis`: Add core structured-output and information/task primitives needed by the sampled domains: record/member projection, comparison/filter/sort/select, explicit source/citation and freshness constraints, output format/length constraints, and a source-edit/test assertion model. Do not rely on prose strings where these constraints need executor-visible meaning.
- **Logic issues:** The schema pragma mandates registry validation, but no registry named core@1 or any registry contents are supplied. Consequently every simulated act.* call is unverifiable and may be a static error.; Action says every call yields a Result record, while Sequence's examples use let results = act.search_flights(...) and later pass $results as a flight/list value. The language never defines implicit Result.value extraction for let.; Action says uncaught failures propagate unless caught by a Condition checking ok, but no field projection, Result predicate, or syntax for checking ok exists; a failed action used directly as a condition atom has special coercion but cannot distinguish failure from false.; The grammar does not define general whitespace handling or include statement separators in program, block, task_def, condition, or iteration productions, while all examples rely on newline-delimited and indented blocks.; The grammar permits at most one not because not_expr ::= ['not'] atom, contradicting the ordinary recursive unary-connective expectation and leaving `not not true` invalid without an intentional rule.; for_each defines its Result only for empty collections and type errors, not after one or more successful iterations or after a later iteration fails.; The claimed static recursion guard is not a meaningful termination guarantee: recursion under `if true then` is accepted, and the lexical condition is underspecified for calls nested in loops, nested tasks, and condition predicates.; Action's `result ::= record { ok: boolean, value: value | null, error: record | null }` is neither valid grammar under the record-literal production nor a complete definition of record/error field syntax; field access is absent.; The task recursion policy permits depth-limit-dependent outcomes and leaves error message content executor-defined, reducing cross-executor equivalence.; No rule specifies whether a value expression containing a failed task/action on the right side of let produces no binding, propagates through a condition, or exposes the failed Result; the stated enclosing-statement propagation does not resolve all binding cases.
- **Decision:** needs-rework
- **Documenter summary:** The Shaper proposed a 6-construct sequential, block-delimited core (drawing on Python's flat statement order, HTML's verb/attribute separation via act.<name>(key=value) plus a mandatory schema-registry pragma, English's fixed and/or/not connectives, and Parsel-style top-level task decomposition with return), but the Critic returned it needs-rework because the schema registry it mandates was never supplied and central semantics are incomplete or contradictory. The decisive evidence was that across nearly all 20 sampled items (SWE-bench, Mind2Web, ALFRED, PRISM, ThoughtTrace, PATHs) every domain action had to be an invented, unverifiable act.* name, and simulations exposed unresolved gaps like whether `let` binds a call's Result or its .value, no way to inspect `ok`, undefined whitespace/indentation rules despite indented examples, and undefined for_each results after non-empty iteration. No basis was established this attempt; a revised proposal with a concrete minimal registry and these semantic fixes is required.
- **Cost this sprint:** $1.1382
