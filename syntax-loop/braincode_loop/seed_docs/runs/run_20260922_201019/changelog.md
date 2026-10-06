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

## Sprint 0 (bootstrap, attempt 1) — 2026-09-22

- **Language version:** 0.1.0 → 0.1.0 (MAJOR — establishes the base syntax)
- **Inspiration languages:** Python inspired the flat indentation-delimited Task/Step sequencing, call-style Actions, and Let-bindings; HTML inspired splitting an Action's operational Args from its attribute-like Modifiers; English inspired the closed-class If/Else/And/Or/Not control-flow keywords; formal language theory inspired the fixed-precedence, short-circuit, context-free design used to keep every construct deterministically parseable.
- **Shaper proposal (model: anthropic/claude-sonnet-5):** Establishes a five-construct orthogonal core (Action, Task, Condition/BoolExpr, Binding, ForEach) covering effectful calls, sequential decomposition, deterministic short-circuit control flow, single-assignment data flow, and ordered iteration.
- **Changes:** `Action` (add, MAJOR), `Task` (add, MAJOR), `Condition` (add, MAJOR), `Binding` (add, MAJOR), `ForEach` (add, MAJOR)
- **Critic decision:** needs-rework — This is a promising core: ordered Tasks, bindings, fixed-precedence conditions, and sequential iteration provide useful structure for several sampled closed tasks. It cannot be accepted because its own examples contain grammar/reference errors and fundamental execution, scoping, document, collection, task-call, and effect-in-condition semantics remain unresolved. The open-vocabulary strategy also yields low translation convergence and turns many closed-task plans into opaque labels rather than reliably interpretable agent instructions.
- **Doc hygiene:** pass — All changes carry a complete glossary entry (gloss + worked example).
- **Pre-KPI assessment:**
  - coverage: mixed — The open Action vocabulary, sequencing, bindings, conditions, and iteration cover many sampled web, household, and planning tasks. However, closed-task coverage is weakened by missing collection-valued Action arguments, no defined document/top-level form, no task parameters or returns, and no way to represent structured code edits, test assertions, or persistent state updates without hiding their actionable core in arbitrary verb names and strings.
  - expressivity: mixed — The proposal preserves ordering, simple branches, priority/tone modifiers, and loop order in several samples. It loses or leaves underspecified important meanings: explicit no-op behavior, task inputs/outputs, selection cardinality such as both/exactly one, compatibility-selection policy, quantification, conversational turns and revisions, and whether a modifier is a descriptive attribute or an execution guard.
  - determinism: harm — The syntax parses some boolean expressions deterministically, but translation is highly unconstrained because all domain semantics reside in arbitrary Action names and arbitrary modifier keys. The independent translations diverge substantially between Find/Search, PutAway/Prepare, Ask/Answer, monolithic versus decomposed plans, and whether to emit an Else no-op; the specification supplies no normalization rule to resolve these choices.
  - interpretability: mixed — Indentation, fixed boolean precedence, lexical binding scope, and sequential loop semantics are readable. But an expression such as Prepare("cup", [purpose="coffee"]) is not legal under this grammar, and otherwise a reader cannot infer the operational contract of open verbs such as FixLocaleMatching, Find, Say, or SendFollowUp from the glossary; the glossary only defines Action generally, not the vocabulary used in an expression.
  - improvement: mixed — Explicit order, data flow, branch execution, and iteration can improve planning for the embodied, shopping, email, and meal-prep tasks. The improvement is undermined where a supposedly structured plan merely replaces prose with opaque action labels or strings, and where effectful Actions are allowed inside predicates and modifiers, making an evaluator potentially perform unintended effects while deciding what to do.
- **Simulated examples:**
  - `dev-embodied-2` (seed_tasks) [Full] NL: "Put both pillows from the sofa onto the armchair, one at a time." → `Task MovePillows:
    Let pillows = FindItems(item="pillow", location="sofa", count=2)
    ForEach pillow In pillows:
        Move(item=pillow, source="sofa", destination="armchair")` — ForEach supplies ordered one-at-a-time iteration and Binding supplies the collection. The exact interpretation of "both" depends on an undeclared FindItems/count action contract.
  - `dev-email-2` (seed_tasks) [Full] NL: "If my manager hasn't replied by Friday, send a polite follow-up; otherwise do nothing." → `Task FollowUpManager:
    If Not HasReplied(person="manager", deadline="Friday"):
        SendFollowUp(recipient="manager")[tone="polite"]
    Else:
        NoOp()` — Condition and modifier capture the branch and polite register. NoOp is only an arbitrary open Action; its no-effect contract is not defined by the basis.
  - `e344b89e-767a-4618-ba82-4b81cdcba280` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "add a motherboard under $200 and a compatible processor at any price to the shopping cart." → `Task AddCompatibleParts:
    Let motherboard = FindProduct(category="motherboard", max_price=200)
    Let processor = FindProduct(category="processor", compatible_with=motherboard)
    AddToCart(item=motherboard)
    AddToCart(item=processor)` — Binding makes compatibility data flow explicit. The task still has no defined selection policy when multiple qualifying products exist.
  - `f118238f-ef8f-4b63-9159-a81e981ef46e` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Add decorative LED Candles to the cart." → `Task AddLedCandles:
    AddToCart(item="decorative LED Candles")` — Action and Task are sufficient for the requested outcome; no proposed control-flow feature is needed.
  - `trial_T20190906_214148_552057#1` (ALFRED (json_2.1.0, train)) [Full] NL: "get a cup ready for coffee" → `Task PrepareCupForCoffee:
    Let cup = GetItem(item="cup", location="fridge")
    Heat(item=cup, appliance="microwave")
    Place(item=cup, location="under coffee maker spout")` — Sequential Task and Binding expose the implied embodied sequence. The source request itself under-specifies the heating operation, so different translators can reasonably emit a single PrepareCup action instead.
  - `trial_T20190908_102045_139402#1` (ALFRED (json_2.1.0, train)) [Full] NL: "To put the toilet paper away." → `Task PutToiletPaperAway:
    Let paper = GetItem(item="toilet paper", location="on toilet")
    Place(item=paper, location="wall holder")` — The Task structure expresses the trajectory-level pickup and placement. The natural-language instruction alone does not specify the holder, so this decomposition depends on environment context.
  - `sympy__sympy-15345` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Partial] NL: "mathematica_code gives wrong output with Max
If I run the code

```
x = symbols('x')
mathematica_code(Max(x,2))
```

then I would expect the output `'Max[x,2]'` which is valid Mathematica code but instead I get `'Max(2, x)'` which is not valid Mathematica code.
" → `Task FixMathematicaMax:
    Reproduce(command="x = symbols('x'); mathematica_code(Max(x,2))", expected="Max[x,2]", actual="Max(2, x)")
    EditFile(path="sympy/printing/mathematica.py", change="emit Mathematica Max with square brackets and preserve argument order")
    RunTests(target="mathematica printer Max")` — Task ordering helps, but the substantive code transformation and test oracle remain opaque natural-language strings. There is no code, patch, assertion, or structured test construct.
  - `django__django-15098` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Partial] NL: "Internationalisation didn't support language locale containing both script and region." → `Task FixLocaleScriptRegion:
    ReproduceLocaleRouting(locale="en-Latn-US", expected_status=200, actual_status=404)
    EditFile(path="django/utils/translation/trans_real.py", change="accept locale tags containing language, optional script, and optional region")
    VerifyLocaleRouting(locales="en-latn-us,en-Latn-US", expected_status=200)` — The high-level reproduce-fix-verify sequence is represented, but the RFC rule, precise regex/code patch, and test cases are opaque strings. The basis has no structured representation for file changes or test assertions.
  - `c5957` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Please provide a recipe for high protein flatbread" → `Task ProvideFlatbreadRecipe:
    ProvideRecipe(dish="flatbread")[nutrition_focus="high protein"]` — The request act and dietary constraint are represented; the recipe prose is correctly retained as generation content. The later trajectory revisions and nutrition follow-up cannot be linked as turns.
  - `c436` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "What places to visit in Bilbao" → `Task RecommendBilbaoPlaces:
    RecommendPlaces(city="Bilbao")` — The recommendation request and destination are represented; recommended-place prose is an opaque generation payload. The subsequent opening-hours, rain-plan, and nearby-town follow-ups have no conversation-thread construct.
  - `c996` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "What is your take on love?" → `Task GiveViewOnLove:
    GiveOpinion(topic="love")` — The opinion speech act and topic are captured, while the opinion itself is appropriately generated prose. The later question about AI experience is not representable as a linked turn.
  - `c4939` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Is marriage important?" → `Task ExplainMarriageImportance:
    Explain(topic="importance of marriage")` — The question is captured as an explanatory response request; its substantive argument remains prose. The historical follow-up and feedback cannot be represented as a threaded interaction.
  - `wildchat1m_en3u-129421` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-1106-preview)) [Partial] NL: "ISA, act as a collective of a hypothetical persona, Mark, who is a literal combination of four expert personas, then explain in depth how linear algebra transforms text into numbers for ChatGPT-4 and back into answers, using concrete examples." → `Task ExplainLinearAlgebraAsMark:
    Explain(topic="how ChatGPT-4 uses linear algebra to encode text and generate answers", persona="Mark: literal collective of psycholinguist, linear-algebra professor, logical-reasoning professor, and LLM practitioner", examples="concrete", depth="in depth")[register="eloquent simple casual conversational American"]` — The explanation act, persona, depth, examples, and register are represented, with technical exposition as payload. The repeated "continue" requests in the trajectory cannot be modeled as revisions of the same response.
  - `wildchat1m_en3u-148973` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-0125-preview)) [Partial] NL: "Write a hilarious 17+ Scooby gang and Scrappy-Doo behind-the-scenes script reacting to badly translated sentences and roasting their errors." → `Task WriteTranslationRoastScript:
    WriteScript(subject="Scooby gang and Scrappy-Doo react behind the scenes to a badly translated Jeopardy-and-robot premise", humor="hilarious roasting", rating="17+", include="occasional mocking quotes")[genre="comedy", audience="adult"]` — The requested format, characters, premise, tone, rating, and stylistic constraint are captured; the script remains content payload. The multi-turn sequence of additional translations and continuity constraints is not modeled.
  - `wildchat1m_en3u-142592` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-0125-preview)) [Partial] NL: "Please write steps for homiletics and engaging Christian sermons" → `Task WriteHomileticsSteps:
    WriteGuide(topic="homiletics and engaging Christian sermons", format="steps", audience="Christian sermon writers")` — The guide-generation act, topic, format, and audience are represented. The later request to expand every step and give examples is a revision operation not supported by the basis.
  - `wildchat1m_en3u-22638` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0301)) [Partial] NL: "write an email introducing yourself and job position to other party asking for collaborations" → `Task WriteCollaborationEmail:
    WriteEmail(purpose="introduce sender and job position and request collaboration", recipient="other party")[register="professional"]` — The communication format, recipient, purpose, and inferred register are captured; email wording is correctly content payload. The subsequent request for the recipient's response lacks a reply/thread primitive.
  - `1775955172098` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "I need help planning a trip to Italy" → `Task PlanItalyTrip:
    PlanTrip(destination="Italy")` — The planning intent and destination are represented, but the later one-week architecture preference, Chilean origin, and one-million-CLP budget are unrepresentable as successive refinements of this plan.
  - `1775612391896` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Full] NL: "hello" → `Task Greet:
    Greet()` — The greeting is directly representable. The later CRUD-app ideation and modal-versus-page decision are a separate, unthreaded conversational task.
  - `1775448065619` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Full] NL: "I want to start a healthy diet. Can you help me plan a simple meal prep for 3 days that includes breakfast, lunch, and dinner? I prefer high-protein options." → `Task PlanHighProteinMealPrep:
    ForEach day In [1, 2, 3]:
        PlanMeal(day=day, meal="breakfast")[diet="healthy", protein="high", complexity="simple"]
        PlanMeal(day=day, meal="lunch")[diet="healthy", protein="high", complexity="simple"]
        PlanMeal(day=day, meal="dinner")[diet="healthy", protein="high", complexity="simple"]` — ForEach captures three days and ordered meals; modifiers capture explicit dietary constraints. The later request to optimize for time is a missing revision/refinement relation.
  - `1775760283577` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "Hi there, I am curious to learn a little about end-stage heart failure. Talk to me like you would a 5-year-old." → `Task ExplainHeartFailure:
    Explain(topic="end-stage heart failure", depth="a little")[audience="5-year-old", register="simple compassionate"]` — The explanation act, topic, requested depth, audience, and register are represented; medical explanation content remains prose. The prognosis question and later reassurance are not linked conversational turns.
- **Cross-check:** used=True, agreement=low — Independent translations agree only loosely on a few simple intents such as PlanTrip(destination="Italy") and Say("hello"). They differ in decomposition level, action names, capitalization, positional versus keyword arguments, whether to represent an Else no-op, and even speech-act direction (for example Ask versus Answer). Several supplied translations also expose grammar failures: ForEach email In UnreadEmails() violates the proposed ForEach source grammar, and Prepare("cup", [purpose="coffee"]) treats modifiers as an Action argument.
- **Required changes:**
  - `basis`: Add a complete document grammar defining whether a document contains one or more Tasks, whether top-level Steps are legal, newline/comment handling, and the parse rule for INDENT/DEDENT. State every reserved word, including Task, Let, ForEach, Else, True, and False.
  - `Action`: Make Action argument rules unambiguous: specify whether positional arguments may follow keyword arguments, whether duplicate keyword arguments are legal, and reject duplicates rather than silently using last-occurrence-wins for constraints. Define a closed distinction between modifier categories such as execution guard, presentation/register, and priority, or remove the claim that arbitrary modifiers express conditions.
  - `Action`: Either prohibit effectful Actions in BoolExpr and Modifiers or introduce a distinct pure query/predicate form with declared return types. If effectful predicates remain allowed, define their failure/error behavior and document that short-circuiting can suppress effects.
  - `Action`: Add ListLiteral to Value, or explicitly define a separate collection-value grammar available in Action arguments and bindings. As written, Action(list=[...]) is impossible and the only worked ForEach example is syntactically invalid because UnreadEmails() is neither an Identifier nor a ListLiteral.
  - `Task`: Define Task signatures, argument binding, return values, and invocation semantics, or prohibit Task invocation. The current claim that a Task can be called with ordinary Action syntax has no grammar for declared parameters or a returned value.
  - `Binding`: Resolve the contradiction between Python-like scoping and the stated block-lexical scope, define shadowing of an outer binding and collision between loop identifiers and Lets, and state whether an unbound Identifier in an Action argument/modifier is always a static error.
  - `Action`: Correct the BookFlight worked example to use priority="high" or define enum literals. Under the stated Value grammar, high is an Identifier, and under Binding it is unbound.
  - `Condition`: Define the value domain and comparison semantics for strings, numbers, booleans, lists, null/missing values, and incomparable operands; define failures from nested Actions. Add tests for precedence, nested If/Else attachment, and short-circuit behavior.
  - `basis`: Add a minimal canonicalization policy for action names, keyword casing, positional-versus-keyword arguments, decomposition granularity, explicit no-op branches, and modifier placement. Without it, the open Action vocabulary makes equivalent translations non-convergent.
  - `basis`: Add a conversation/revision construct before claiming broad conversational coverage, with turn order, reference to a prior response/plan, and operations such as refine, continue, correct, and answer-follow-up.
  - `basis`: Add at least a generic structured artifact/change/assertion mechanism for code and web tasks (for example FileEdit, Patch, Test/Assert with typed fields), so closed SWE-style requests do not rely solely on opaque prose in change strings.
- **Logic issues:** The ForEach worked example is invalid: its grammar permits only Identifier or ListLiteral after In, but UnreadEmails() is an Action.; The Action worked example is invalid or has undefined reference resolution: priority=high uses high as an unbound Identifier rather than a String or defined enum.; The foundations say If/Else/And/Or/Not/In are reserved, but omit Task, Let, ForEach, True, and False from the reserved-word rule despite using them as grammar terminals.; Task claims flat sequential control flow while its Step grammar permits nested Condition and ForEach blocks; this is not inherently wrong, but the description is contradictory and obscures nesting/evaluation rules.; Task invocation is asserted semantically but no Task parameter grammar, argument-to-parameter binding, or task result/return semantics exists.; Last-occurrence-wins for duplicate action/modifier keys silently discards constraints, such as conflicting recipients, deadlines, audiences, or safety settings; this harms faithful round-trip meaning.; Actions are effectful by default yet may occur in comparisons and modifiers. Consequently, evaluating a condition or a qualifier can mutate the world; no failure, retry, rollback, or idempotency semantics are given.; Comparison semantics are undefined for heterogeneous values, list values, null/missing action returns, and failed actions.; The sole data-flow claim is false for loop state and aggregation: single-assignment Let has no mutation, accumulator, reduction, or return semantics, so the stated ForEach-plus-Let workaround for quantification cannot actually track a result.; No grammar or semantics defines a root document, multiple tasks, top-level actions, comments/newlines, or the lexical treatment of whitespace and indentation errors.; Open Action identifiers and arbitrary modifier keys make the formal surface parseable but leave the meaning of nearly every domain operation unspecified, producing both redundancy and divergent translations.
- **Decision:** needs-rework
- **Documenter summary:** The Shaper proposed a 5-construct foundational basis (Action, Task, Condition, Binding, ForEach) built on Python's flat indentation-scoped blocks, HTML's content/attribute separation for Action args vs. modifiers, and English's closed-class control-flow keywords, aiming for a context-free deterministic core. The Critic returned a needs-rework verdict: despite full coverage on several simulated web/household/planning items (e.g. shopping cart, meal-prep, pillow-moving tasks), low-agreement cross-checked translations and internal grammar errors surfaced—most notably the ForEach worked example (`ForEach email In UnreadEmails()`) violating its own grammar and the `priority=high` Action example using an undefined, unbound identifier—alongside unresolved gaps in document structure, task invocation/return semantics, effectful actions inside conditions, and collection-valued arguments. No basis was ratified this attempt; required changes were specified for resubmission.
- **Cost this sprint:** $0.7409

## Sprint 0 (bootstrap, attempt 2) — 2026-09-22

- **Language version:** 0.1.0 → 0.1.0 (MAJOR — establishes the base syntax)
- **Inspiration languages:** Python's indentation-delimited, flat statement blocks shape Document/Task/Condition/ForEach sequencing and scoping; HTML's content/attribute separation shapes Action's Args-vs-Modifiers split; English's closed-class function words shape the small reserved keyword set (If/And/Or/Not/Query/Let/Set) that keeps control flow deterministic while domain vocabulary stays open.
- **Shaper proposal (model: anthropic/claude-sonnet-5):** This revision adds an explicit Document/lexical layer and a Dialogue construct, and substantially rewrites Action, Task, Condition, Binding, and ForEach to fix every grammar error, close the pure/effectful and scoping ambiguities, add data-flow mutation, structured code-edit primitives, and a canonicalization policy the Critic required.
- **Changes:** `Document` (add, MAJOR), `Action` (revise, MAJOR), `Task` (revise, MAJOR), `Condition` (revise, MAJOR), `Binding` (revise, ?)
- **Critic decision:** needs-rework — This is a promising direction: explicit indentation, entry-point rules, ordered evaluation, pure Query predicates, strict comparison behavior, and the Edit/Assert/Verify core address real bootstrap gaps. It nevertheless cannot be accepted because doc hygiene failed and the submitted foundation is incomplete: Binding is truncated, while essential referenced constructs for iteration and conversation are absent. These omissions materially harm interpretability and leave common sampled task structures without defined behavior, so the Shaper should complete the basis before resubmission.
- **Doc hygiene:** FAIL — Doc hygiene FAILED — `Binding` missing glossary_gloss, worked_example, worked_example.nl/braincode
- **Pre-KPI assessment:**
  - coverage: mixed — Action calls and ordered blocks cover many simple embodied, browsing, and code-edit requests, and the proposed Edit primitive helps SWE-style work. However, the submitted basis omits the promised ForEach and Dialogue constructs entirely, leaves Binding incomplete, and has no completed way to express iteration, conversational turns, revisions, or structured multi-step data flow.
  - expressivity: mixed — The Action Args/Modifiers distinction, typed comparisons, and explicit ordering preserve useful constraints such as priority, audience, and conditions. But the missing Dialogue syntax loses follow-up and correction structure in PRISM and ThoughtTrace items; missing ForEach loses the explicit one-at-a-time constraint; and several closed code tasks require opaque issue strings rather than fully structured diagnosis, edit, and test plans.
  - determinism: mixed — Reserved keywords, indentation rules, positional-before-keyword arguments, duplicate rejection, precedence, and canonical naming are meaningful improvements. Determinism remains weak because arbitrary open-vocabulary actions have no action catalog or argument schema, equivalent translations can choose substantially different verbs and parameter names, and the absent Binding/ForEach/Dialogue definitions force translators to improvise or flatten structure.
  - interpretability: harm — The document is not a usable complete basis: Binding is truncated and lacks its required glossary/example, while Document and Action reference undefined Turn, TurnRef, Dialogue, and ForEach semantics. The Task worked example is also an ambiguous-entry program under the stated entry-point rule, so a reader cannot reliably determine whether the example is executable.
  - improvement: mixed — Explicit sequencing, guards, pure Query calls, assertions, verification, and exact Edit operations would improve an agent's planning over raw simple requests. The benefit is blocked for iterative, conversational, and revision-oriented tasks because their central control structures are absent, and opaque generic Actions provide little more guidance than a natural-language instruction.
- **Simulated examples:**
  - `dev-embodied-2` (seed_tasks) [Full] NL: "Put both pillows from the sofa onto the armchair, one at a time." → `PickUp(item="first pillow", source="sofa")
Place(item="first pillow", destination="armchair")
PickUp(item="second pillow", source="sofa")
Place(item="second pillow", destination="armchair")` — Flattening preserves the two-item and one-at-a-time ordering for this concrete request. The omitted ForEach construct would be needed for a general collection-valued formulation.
  - `dev-embodied-1` (seed_tasks) [Full] NL: "Rinse the mug in the sink, then put it in the coffee maker." → `Rinse(item="mug", location="sink")
Place(item="mug", destination="coffee maker")` — Action sequencing captures the actionable core; proposed Binding and missing constructs are irrelevant.
  - `86afd67c-1bff-455c-baa7-e18dcb64b0f3` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Find comedy tv shows on netflix sorted by audience score." → `OpenSite(site="Netflix")
Navigate(section="TV Shows")
Filter(category="Genre", value="comedy")
Sort(field="audience score", order="descending")
ShowResults()` — The ordered web interaction and requested sort are expressible through open Actions, although arbitrary action names reduce convergence.
  - `bf469f30-6628-4017-b963-672645d7feab` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Find the highest rated dog collar under 10 dollar." → `OpenShop()
Navigate(category="Pet")
Filter(petType="dog")
Filter(category="collars and leashes")
Filter(price="under 10 dollars")
Sort(field="rating", order="descending")
ShowResults()` — The finite selection and ordering constraints are represented. No proposed typed shopping primitive constrains whether translators use Filter, Search, or Navigate.
  - `trial_T20190907_223758_523581#1` (ALFRED (json_2.1.0, train)) [Full] NL: "Microwave a slice of apple and place it on the table." → `Slice(item="apple")
PickUp(item="apple slice")
Heat(item="apple slice", appliance="microwave")
Place(item="apple slice", destination="table")` — The requested preparation, heating, and final placement are sequenced. Incidental navigation-tool trajectories are not part of the user-request core.
  - `trial_T20190908_224836_919680#2` (ALFRED (json_2.1.0, train)) [Full] NL: "Put a microwaved slice of apple on the table in the corner." → `Slice(item="apple")
PickUp(item="apple slice")
Heat(item="apple slice", appliance="microwave")
Place(item="apple slice", destination="table in the corner")` — The required heated state and destination are represented by ordered Actions.
  - `scikit-learn__scikit-learn-11578` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Partial] NL: "For probabilistic scorers, LogisticRegressionCV(multi_class='multinomial') uses OvR to calculate scores; pass multi_class into the LogisticRegression constructor in _log_reg_scoring_path and test the fix." → `Edit(path="sklearn/linear_model/logistic.py", target="log_reg = LogisticRegression(fit_intercept=fit_intercept)", replacement="log_reg = LogisticRegression(fit_intercept=fit_intercept, multi_class=multi_class)")
Verify(command="run targeted LogisticRegressionCV multinomial probabilistic-scoring regression test", expected=True)` — Edit helps materially and captures the identified source replacement. The required regression-test command and complete behavioral conditions remain opaque because Verify.command is only an uninterpreted string.
  - `django__django-13112` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Partial] NL: "makemigrations crashes for ForeignKey with mixed-case app name." → `InvestigateAndFix(path="django/db/models/fields/related.py", issue="mixed-case installed app names are incorrectly lowercased when resolving lazy ForeignKey references")
Verify(command="run regression test for ForeignKey lazy reference with mixed-case app name", expected=True)` — The requested file, defect, and test intent are present, but no defined structured diagnostic/change primitive can state the exact implementation. InvestigateAndFix is an unconstrained open Action.
  - `c6516` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "What kind of different foods would be great to try while in the Netherlands and can you recommend a good restaurant?" → `Respond(prompt="Recommend Dutch foods to try and a good restaurant in the Netherlands", context="User previously asked for places to visit in the Netherlands")[audience="user", tone="enthusiastic"]` — The two requested answer components and audience/tone are represented; substantive recommendations appropriately remain payload prose. The prior-turn relationship cannot be formally represented because Dialogue and Turn are absent.
  - `c3388` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "yeah being in pain sucks, i have been in pain for nearly 3 years, can you tell me a joke to help take my mind off the pain" → `Respond(prompt="Acknowledge the user's long-term pain empathetically, then tell a gentle joke intended as distraction")[audience="user", tone="supportive"]` — Speech act, recipient, purpose, and supportive register are captured; the actual empathetic wording and joke are legitimate generative payload. Dialogue context and safe conversational follow-up are undefined.
  - `c2067` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "If they are appointed by the president how is that fair?" → `Respond(prompt="Explain, in the context of the prior Supreme Court discussion, how appointment by the president is intended to be fair")[audience="user", tone="clear"]` — The follow-up question and explanatory intent are captured, but its dependency on prior turns is only opaque prose because Turn/AnswerFollowUp semantics were not actually supplied.
  - `c2904` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "But the information you provided is old news, are you aware of the current political events in Aotearoa for 2023?" → `Respond(prompt="Correct the stale earlier answer and state whether current 2023 political events in Aotearoa/New Zealand are available; provide current information only if supported")[audience="user", tone="candid"]` — This is a correction of a prior answer, but the promised Correct/Dialogue construct has no supplied grammar or semantics. A generic response loses formal correction sequencing.
  - `wildchat1m_en3u-73283` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "Introduce the topic of the impact of dam construction on seasonal precipitation pattern, land use/cover, and socio-economic conditions in the semi-arid region of Eastern Sudan." → `GenerateIntroduction(topic="impact of dam construction on seasonal precipitation patterns, land use/cover, and socio-economic conditions in semi-arid Eastern Sudan")[register="academic", audience="general reader"]` — The generation act, topic, audience, and register are represented; the requested introduction's prose substance is correctly left to generation.
  - `wildchat1m_en3u-76731` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "try to squeeze some ideas of “The Holy Blood and the Holy Grail”-alike conspiracy from “The Brothers Karamazov”" → `GenerateAnalysis(sourceWork="The Brothers Karamazov", comparisonWork="The Holy Blood and the Holy Grail", focus="possible conspiracy-like thematic parallels", constraint="do not claim direct equivalence")` — The comparative creative-analysis request and its source works are represented. The analysis itself is an appropriate opaque payload.
  - `wildchat1m_en3u-137561` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-1106-preview)) [Partial] NL: "Write a story of when Gloopy and Glitter met the scientist, who is amazed they can speak." → `GenerateStory(characters=["Gloopy", "Glitter", "scientist"], premise="The scientist first meets Gloopy and Glitter on Gloopiter and is amazed that they can speak", continuity="Gloopy is a teal blob and Glitter is a sparkling fuchsia blob")` — The final request's narrative goal and necessary continuity are represented. The lengthy preceding story is conversational context that should be modeled by missing Dialogue/Turn structures rather than flattened into an Action.
  - `wildchat1m_en3u-78000` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "Add a binding signature line to the speaker-facing high-demand speaking-engagement contract." → `ReviseDocument(document="speaker-facing high-demand speaking-engagement contract", change="add an acceptance section with client name, date, and binding signature line")[register="professional"]` — The revision operation, target document, role orientation, and requested addition are retained. It is a follow-up revision, but Refine/Continue/Correct have no defined Dialogue semantics.
  - `1776009617894` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "Can you suggest a posting schedule to help the Hamoudi children's educational YouTube channel grow quickly in its first month?" → `GeneratePlan(subject="first-month posting schedule", project="Hamoudi children's educational YouTube channel", objective="grow quickly", context="beginner deciding between real-life, 2D, or hybrid production")` — The requested plan, project, objective, and relevant context are captured; schedule content remains generative. The multi-turn dependency is opaque without Dialogue.
  - `1775429344935` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "Help me to create a text about my decision to go to Japan to learn about SGI. Only 100 words." → `GenerateText(topic="my decision to go to Japan to learn about SGI", wordCount=100, perspective="first person")` — Intent, topic, strict quantity, and perspective are captured. The requested prose is appropriately a generated payload.
  - `1775752130482` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "hello, i want to plan a 3 day safari in eastern cape south africa" → `GenerateItinerary(destination="Eastern Cape, South Africa", durationDays=3, activity="safari")` — The planning speech act, destination, duration, and activity are explicit. The itinerary's recommendations remain prose payload.
  - `1775479438859` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "Gain a short certification if it opens a stable field: examples in UK context?" → `Respond(prompt="Give realistic examples of short UK certifications that can lead to stable employment, with mortgage-friendly employment considerations", context="User seeks a job contract to access mortgage products")[audience="user", tone="practical"]` — The requested UK-specific examples, stability criterion, and mortgage context are retained. The response is a context-dependent follow-up that cannot be represented as a formal turn.
- **Cross-check:** used=False, agreement=low — No independent translations were supplied. Capable translators would likely agree on simple linear embodied sequences, but are unlikely to converge on open Action names and schemas such as Respond versus Answer, Filter versus Search, or InvestigateAndFix versus DiagnoseAndFix; the incomplete control-flow basis increases divergence.
- **Required changes:**
  - `Binding`: Submit the complete Binding grammar and semantics, including Let initialization, Set resolution and mutation rules, assignment type behavior, shadowing, block/task scope, undefined-name errors, and a required glossary gloss and NL-to-BrainCode worked example.
  - `ForEach`: Add the promised ForEach construct with complete grammar, iterable value rules, loop-variable scope, deterministic iteration order, empty-list behavior, interaction with Return/branching, and a worked example.
  - `Dialogue`: Add Turn and Dialogue grammar and semantics before reserving or referencing Turn, TurnRef, Refine, Continue, Correct, and AnswerFollowUp. Define turn ordering, participant/recipient representation, reference resolution, corrections/follow-ups, and whether dialogue Actions are effects or response-generation requests.
  - `Document`: Remove references to undefined Step, Turn, Dialogue, and TurnRef until they are supplied, or define them in this submission. Clarify whether a top-level QueryCall is a legal Step and give a complete top-level Step production.
  - `Task`: Fix the worked example's entry-point error by adding bare Main steps, naming one Task Main, or changing the example so there is exactly one declared Task. Define whether task invocation is legal as a standalone Step independently of Action and specify its return behavior when nested in Args.
  - `Condition`: Either remove `In` from the reserved-word claim or add membership grammar and semantics. Add parenthesized BoolExpr grouping and repeated negation grammar, such as `NotExpr := "Not" NotExpr | Primary` and a parenthesized boolean primary, so complex conditions are expressible without ambiguity.
  - `Document`: Define EscapeSeq, newline handling inside String, and the exact lexical boundary rule separating Identifier from EnumWord. State whether EnumWord values such as `high` are lexed contextually rather than as Identifiers.
  - `basis`: Add a small canonical core vocabulary or domain-neutral operation schema for common retrieval, navigation, selection, response-generation, and object manipulation actions, or explicitly state that semantic equivalence of synonymous open Actions is not guaranteed. The present naming convention alone cannot make open Action translations converge.
- **Logic issues:** Doc hygiene failed: Binding has neither glossary_gloss nor worked_example, so the attempt cannot be accepted.; The proposal is truncated in Binding semantics and omits the promised ForEach and Dialogue changes entirely.; Document and Action refer to undefined Turn, TurnRef, Dialogue, and ForEach constructs, making the grammar/reference graph incomplete.; The Task worked example declares two Tasks, has no bare steps or Turn sequence, and neither Task is named Main; Document therefore makes it a static ambiguous-entry error.; Condition states that In is reserved but does not include an In comparison operator or membership semantics.; Condition has no grammar for parenthesized BoolExpr grouping and permits only one Not token, despite presenting a general logical-expression language.; String relies on undefined EscapeSeq and does not state whether literal newlines are legal, so source text and code-edit payload parsing is incomplete.; Open-vocabulary Actions with arbitrary keyword schemas make semantically equivalent translations non-canonical despite the stated naming policy.; Task says call-position precedence first treats a bound name as a variable reference and never callable, but no grammar/semantics define callable values or diagnose `x()` clearly when x is bound.; The claimed strict pure/effectful separation is syntactic only for QueryCall; arbitrary open Actions may return values and nested Actions execute effects inside argument evaluation, making apparently atomic outer calls operationally multi-effect.
- **Decision:** needs-rework
- **Documenter summary:** Sprint 0 attempt 2 proposed a 5-construct basis (Document, Action, Task, Condition, Binding) drawing on Python's flat indentation, HTML's content/attribute separation, and English's closed function-word class, but was sent back needs-rework because Binding was left truncated (failing doc hygiene) and the promised ForEach and Dialogue constructs were never submitted despite being referenced elsewhere. The Critic's simulations showed Full coverage on simple linear embodied tasks (e.g. pillow-moving, mug-rinsing) but only Partial coverage on nearly every PRISM, ThoughtTrace, and SWE-bench item, since conversational follow-ups/corrections and structured code-diagnosis had no formal construct to represent them, most tellingly the Task worked example itself violating the basis's own entry-point rule.
- **Cost this sprint:** $0.7103
