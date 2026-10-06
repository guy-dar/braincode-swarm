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

## Sprint 0 (bootstrap, attempt 1/3) — 2026-09-23

- **Language version:** 0.1.0 → 0.1.0 (MAJOR — establishes the base syntax)
- **Inspiration languages:** Python motivates TASK's indentation-delimited, sequentially-evaluated statement blocks; HTML motivates ACTION/MESSAGE's content-vs-attribute split (e.g. one `email` verb modified by `tone=`/`audience=` rather than separate verbs per register); English motivates CONDITIONAL's closed-class IF/AND/OR/NOT connectives; formal language theory and the Parsel/ReAct precedents motivate the context-free block structure, the CHECK/ACTION purity split, and ITERATION's deterministic FOR EACH / ANY / ALL quantifiers.
- **Shaper proposal (model: anthropic/claude-sonnet-5):** Establishes a six-construct orthogonal core for BrainCode — TASK, ACTION, CHECK, CONDITIONAL, ITERATION, and MESSAGE — covering sequencing, effectful and pure steps, data flow, branching, collection-handling, and open-register conversational content.
- **Changes:** `TASK` (add, MAJOR), `ACTION` (add, MAJOR), `CHECK` (add, MAJOR), `CONDITIONAL` (add, MAJOR), `ITERATION` (add, MAJOR), `MESSAGE` (add, MAJOR)
- **Critic decision:** needs-rework — This is a promising structural core, and its explicit sequencing, branch precedence, and MESSAGE metadata offer real value over the empty specification. It cannot be accepted as a bootstrap basis because core examples are not parseable under its own grammar and key foundational semantics—call arguments, CHECK results, quantified element binding, environment resolution, and program/root form—are unresolved. Those failures directly impair determinism and interpretability and force closed-task details into opaque strings, so the set needs precise rework before it can safely become the frozen basis.
- **Doc hygiene:** pass — All changes carry a complete glossary entry (gloss + worked example).
- **Pre-KPI assessment:**
  - coverage: benefit — Compared with the empty basis, TASK, ACTION, CHECK, CONDITIONAl, ITERATION, and MESSAGE provide a plausible structural vocabulary for sequential embodied, web, code, and conversational requests. Simulations can formally sequence the actionable cores of most sampled closed tasks, but the absence of a defined action/predicate vocabulary, named arguments, environment bindings, and structured records limits reliable cross-domain coverage.
  - expressivity: mixed — The basis preserves ordering, simple conditions, recipient/register metadata, and explicit loops in several simulations. However, the declared grammar cannot express the proposal's own keyword-argument examples, CHECK has no defined result type despite use in boolean contexts, quantified predicates have no element binder, and arbitrary prose placed in ACTION string arguments becomes the only way to preserve important implementation details.
  - determinism: harm — Independent translations diverge substantially on whether to use ACTION versus MESSAGE, whether a task needs decomposition, and which unconstrained verb/attribute names to choose (for example find/search, recipient/audience, tone/register, and plan/provide/write). The language provides neither a canonical vocabulary nor rules selecting MESSAGE versus ACTION, while duplicate attributes silently discard information; this makes convergence unlikely.
  - interpretability: mixed — The sequencing, lexical keywords, precedence, and stated task-call cycle rule are helpful. But core syntax and examples contradict one another: named arguments such as city="NYC" are illegal, bare identifiers such as mom are unresolved, standalone ACTION/MESSAGE examples violate TASK's root-container claim, and truthiness plus arbitrary action names leave major behavior dependent on unstated external conventions.
  - improvement: mixed — A weaker agent can benefit from explicit sequencing in the pillow, cart, coffee-cup, and meal-prep simulations, and from explicit branches in the follow-up request. Yet the specification does not define how an ACTION verb maps to an environment, how external collections are introduced, or how CHECK values/results are represented, so the notation often adds labels without supplying executable planning constraints.
- **Simulated examples:**
  - `dev-embodied-2` (seed_tasks) [Full] NL: "Put both pillows from the sofa onto the armchair, one at a time." → `TASK MovePillows:
    FOR EACH pillow IN ["pillow_1", "pillow_2"]:
        ACTION move(pillow, "sofa", "armchair")` — ITERATION captures the one-at-a-time sequential requirement; the concrete object identities must be invented because there is no object-selection or collection-query construct.
  - `dev-email-2` (seed_tasks) [Full] NL: "If my manager hasn't replied by Friday, send a polite follow-up; otherwise do nothing." → `TASK FollowUp:
    IF NOT CHECK replied("manager", "Friday") THEN:
        MESSAGE("Just following up on my earlier message.") audience="manager" register="polite" intent="follow_up"` — CONDITIONAL, CHECK, and MESSAGE preserve the explicit branch and polite recipient-directed output. The omitted ELSE correctly means no action.
  - `e344b89e-767a-4618-ba82-4b81cdcba280` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "add a motherboard under $200 and a compatible processor at any price to the shopping cart." → `TASK AddCompatibleParts:
    ACTION find("motherboard") max_price=200 -> motherboard
    ACTION find("processor", motherboard) -> processor
    ACTION add_to_cart(motherboard)
    ACTION add_to_cart(processor)` — ACTION bindings and ordering preserve the compatibility dependency and the $200 limit. ACTION verb and attribute names are unconstrained, so equivalent translations are unlikely to converge.
  - `f118238f-ef8f-4b63-9159-a81e981ef46e` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Add decorative LED Candles to the cart." → `TASK AddCandles:
    ACTION add_to_cart("decorative LED Candles")` — A single ACTION captures the actionable core; TASK is required by the stated root-container semantics.
  - `trial_T20190906_214148_552057#1` (ALFRED (json_2.1.0, train)) [Full] NL: "get a cup ready for coffee" → `TASK PrepareCupForCoffee:
    ACTION go_to("fridge")
    ACTION take("cup", "fridge") -> cup
    ACTION go_to("microwave")
    ACTION place(cup, "microwave")
    ACTION turn_on("microwave")
    ACTION wait_until_done("microwave")
    ACTION take(cup, "microwave")
    ACTION go_to("coffee_maker")
    ACTION place(cup, "under coffee maker spout")` — ACTION sequencing expresses the trajectory and necessary temporal order. The specification gives no standard semantics for navigation, waiting, appliance state, or containment.
  - `trial_T20190908_102045_139402#1` (ALFRED (json_2.1.0, train)) [Full] NL: "To put the toilet paper away." → `TASK PutAwayToiletPaper:
    ACTION go_to("toilet")
    ACTION take("toilet paper", "top of toilet") -> toilet_paper
    ACTION place(toilet_paper, "wall holder")` — The actionable core is sequenced as ACTIONs. Orientation and looking-up trajectory details are not requested by the short natural-language task and need not be encoded.
  - `sympy__sympy-15345` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Partial] NL: "mathematica_code gives wrong output with Max
If I run the code



```

x = symbols('x')

mathematica_code(Max(x,2))

```



then I would expect the output `'Max[x,2]'` which is valid Mathematica code but instead I get `'Max(2, x)'` which is not valid Mathematica code.
" → `TASK FixMathematicaMax:
    ACTION modify("sympy/printing/mathematica.py", "render Max(x,2) as Max[x,2] rather than Max(2, x)")` — ACTION identifies the target file and desired correction, but the actual code-level transformation remains an opaque natural-language string because there is no structured source-code, assertion, or edit construct.
  - `django__django-15098` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Partial] NL: "Internationalisation didn't support language locale containing both script and region.
Description
	
The i18n_patterns didn't work with locale contains both script and region, like en-latn-us.
Given settings.py
LANGUAGE_CODE = 'en-us'
LANGUAGES = [
	('en-us', "English"),
	('en-latn-us', "Latin English"),
	('en-Latn-US', "BCP 47 case format"),
]
urls.py
from django.conf.urls.i18n import i18n_patterns
from django.http import HttpResponse
def bangiah(request):
	return HttpResponse('U!')
urlpatterns += i18n_patterns(
	path('', bangiah),
)
The response of http://localhost:8000/en-us/ is 200 U!.
The response of http://localhost:8000/en-lat-us/ is 404 not found.
The response of http://localhost:8000/en-Latn-US/ is 404 not found.
Steps to Reproduce
Start a new project with django-admin startproject tshi and cd tshi/
Append to tshi/settings.py as follows
LANGUAGES = [
	('en-us', "English"),
	('en-latn-us', "Latin English"),
	('en-Latn-US', "BCP 47 case format"),
]
MIDDLEWARE += [
	'django.middleware.locale.LocaleMiddleware',
]
Edit tshi/urls.py by appending follows
from django.conf.urls.i18n import i18n_patterns
from django.http import HttpResponse
def bangiah(request):
	return HttpResponse('U!')
urlpatterns += i18n_patterns(
	path('', bangiah),
)
python manage.py migrate
python manage.py runserver
The results
The response of http://localhost:8000/en-us/ is 200 U!.
The response of http://localhost:8000/en-lat-us/ is 404 not found.
The response of http://localhost:8000/en-Latn-US/ is 404 not found.
 Expect to happen instead
The response of http://localhost:8000/en-latn-us/ and http://localhost:8000/en-Latn-US/ should be 200 U!.
The en-Latn-US tag follows format defined in ​RFC 5646. It's ​documented that the language part is always in lowercase, following ​Accept-Language. ​Accept-Language is following ​Content-Language Header, which is following ​RFC 5646. The ​RFC 5646 defined langtag as follow:
langtag	 = language
				 ["-" script]
				 ["-" region]
				 *("-" variant)
				 *("-" extension)
				 ["-" privateuse]
 language	 = 2*3ALPHA			; shortest ISO 639 code
				 ["-" extlang]	 ; sometimes followed by
									 ; extended language subtags
			 / 4ALPHA			 ; or reserved for future use
			 / 5*8ALPHA			; or registered language subtag
 extlang	 = 3ALPHA			 ; selected ISO 639 codes
 script		= 4ALPHA			 ; ISO 15924 code
 region		= 2ALPHA			 ; ISO 3166-1 code
			 / 3DIGIT			 ; UN M.49 code
I have confirmed that this issue can be reproduced as described on a fresh Django project
Python version: 3.7.5
Django version: 3.2.7
" → `TASK FixLocaleScriptRegion:
    ACTION reproduce("Django 3.2.7 locale routing with en-latn-us and en-Latn-US") -> reproduction
    CHECK fails(reproduction) -> failing
    IF failing THEN:
        ACTION modify("django/utils/translation/trans_real.py", "support RFC 5646 language tags containing script and region")
        ACTION verify("en-us", 200)
        ACTION verify("en-latn-us", 200)
        ACTION verify("en-Latn-US", 200)` — The reproduction-fix-verification structure is retained, but locale grammar, test setup, and code changes are opaque strings. CHECK helps branch on the reproduction result but its predicate/result contract is not defined.
  - `c5957` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Please provide a recipe for high protein flatbread" → `TASK ProvideFlatbreadRecipe:
    MESSAGE("Provide a recipe for high-protein flatbread.") intent="recipe" audience="user"` — MESSAGE captures the request speech act and topic; recipe substance correctly remains an opaque prose payload for this open request.
  - `c436` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "What places to visit in Bilbao" → `TASK SuggestBilbaoPlaces:
    MESSAGE("Suggest places to visit in Bilbao.") intent="recommendation" audience="user"` — MESSAGE captures the question and intended response type, while recommendations remain prose substance. The later rain and nearby-town follow-ups in the trajectory are not part of the supplied NL item and cannot be linked by a dedicated dialogue-thread construct.
  - `c996` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "What is your take on love?" → `TASK DiscussLove:
    MESSAGE("What is your take on love?") intent="opinion" audience="user"` — MESSAGE preserves the request for an opinion; the opinion itself is appropriately opaque prose.
  - `c4939` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Is marriage important?" → `TASK DiscussMarriage:
    MESSAGE("Is marriage important?") intent="opinion" audience="user"` — MESSAGE preserves the conversational question and intended opinion response; substantive discussion remains prose by design.
  - `wildchat1m_en3u-129421` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-1106-preview)) [Partial] NL: "ISA, act as a collective of a hypothetical persona, Mark, who is a literal combination of the following four characters combined: 1. 'A very experienced + very charming + very competent American Psychololinguist who explains complicated topics in eloquent simple casual conversational American style and tone' + 2. 'A very experienced + very charming + very competent American Harvard Educated Linear Algebra Professor who explains Linear Algebra in eloquent simple practically-grounded casual conversational American style and tone and by illustrating mathematical notations and formulas in simple 18th Century mathematician style and by using actual illustrative numerical examples' + 3. A very experienced + very charming + very competent American Harvard Educated Logical Reasoning professor who explains complicated topics in eloquent simple practical casual conversational American style and tone' + 4. 'A very experienced + very charming + very competent American Harvard Educated Large Language Models, "Transformers" and Generative AI top-notch Expert and Practitioner, who explain complicated topics in eloquent simple practical casual conversational American style and tone' to then while acting exactly as the collective persona Mark, explain to me in depth how linear algebra is exactly applied to transfer text into equations and numbers a model like ChatGPT-4 can understand and then how the model reapplies linear algebra to transform the equations and figures into answers to a user prompt. Please also illustrate using concrete examples" → `TASK ExplainLLMLinearAlgebra:
    MESSAGE("Explain in depth how a model like ChatGPT-4 uses linear algebra to convert text into numerical representations and convert representations into answers; include concrete numerical examples, notation, and formulas.") audience="user" intent="explanation" persona="Mark collective of psycholinguist, linear algebra professor, logical reasoning professor, and LLM practitioner" register="eloquent simple casual conversational American" depth="in_depth" style="practically_grounded eighteenth_century_math"` — MESSAGE attributes retain the audience, persona, depth, register, illustrative requirement, and output intent. The technical explanation remains a prose payload, as expected for an open generation request.
  - `wildchat1m_en3u-148973` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-0125-preview)) [Partial] NL: "Write a hilarious script where the Scooby gang and Scrappy-Doo have a funny meeting behind the scenes and react to my badly translated sentences, laughing and hilariously question and hilariously roast errors and inconsistencies that make no sense in the translation and the names of stuff with occasional funny quotes mocking a situation, in my prompt in a hilarious comedy 17+ way: (The gang constanlty imagine and make silly quotes to mock the translation)

Ok gang get this… * I start reading the whole thing to the gang * 

Velma and Shaggy compete on Jeopardy, hosted by Alex Trebek, but things go awry when a robot competitor begins attacking anyone who gets more points than him.
" → `TASK WriteScoobyScript:
    MESSAGE("Write a behind-the-scenes meeting in which the Scooby gang and Scrappy-Doo react to: Velma and Shaggy compete on Jeopardy, hosted by Alex Trebek, but a robot attacks anyone with more points.") audience="user" intent="creative_script" format="script" characters="Scooby gang and Scrappy-Doo" tone="hilarious comedy" rating="17_plus" requirements="roast translation errors inconsistencies and names; include silly imagined mocking quotes"` — MESSAGE captures format, characters, setting, tone/rating, and explicit comedic constraints. The script's creative content properly remains prose.
  - `wildchat1m_en3u-142592` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-0125-preview)) [Partial] NL: "Please write steps for homiletics and engaging Christian sermons" → `TASK WriteHomileticsSteps:
    MESSAGE("Write steps for homiletics and engaging Christian sermons.") audience="user" intent="instruction" format="steps" topic="Christian sermon preparation"` — MESSAGE captures the requested instructional format and topic; the instructional content is open prose.
  - `wildchat1m_en3u-22638` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0301)) [Partial] NL: "write an email introducing yourself and job position to other party asking for collaborations" → `TASK WriteCollaborationEmail:
    MESSAGE("Introduce yourself and your job position, then ask the recipient about collaboration.") audience="other_party" intent="collaboration_request" format="email" register="professional"` — MESSAGE preserves medium, recipient, speech acts, and an inferred professional register. Email wording remains prose content.
  - `1775955172098` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "I need help planning a trip to Italy" → `TASK PlanItalyTrip:
    MESSAGE("Help plan a trip to Italy.") audience="user" intent="trip_planning" destination="Italy"` — MESSAGE captures the planning intent and destination, but the itinerary and recommendations are open prose. The subsequent conversation would require a named session/thread or explicit follow-up reference to preserve its revisions and budget constraint.
  - `1775612391896` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Full] NL: "hello" → `TASK Greet:
    MESSAGE("Hello.") audience="user" intent="greeting"` — MESSAGE captures the complete greeting act. The mandatory TASK wrapper is used despite provider disagreement about whether standalone MESSAGE is permitted.
  - `1775448065619` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Full] NL: ""I want to start a healthy diet. Can you help me plan a simple meal prep for 3 days that includes breakfast, lunch, and dinner? I prefer high-protein options."" → `TASK PlanMealPrep:
    FOR EACH day IN [1, 2, 3]:
        ACTION plan_meal(day, "breakfast") diet="healthy" protein="high" complexity="simple"
        ACTION plan_meal(day, "lunch") diet="healthy" protein="high" complexity="simple"
        ACTION plan_meal(day, "dinner") diet="healthy" protein="high" complexity="simple"` — ITERATION and ACTION preserve the three-day quantity, all meals, high-protein preference, and simplicity constraint. The detailed meal-plan content is delegated to the action and therefore not made explicit.
  - `1775760283577` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "Hi there, I am curious to learn a little about end-stage heart failure. Talk to me like you would a 5-year-old." → `TASK ExplainHeartFailure:
    MESSAGE("Explain end-stage heart failure.") audience="user" intent="explanation" register="for_a_5_year_old" depth="brief"` — MESSAGE captures the explanatory intent, audience/register, and requested brevity. The medical explanation itself is legitimately opaque prose.
- **Cross-check:** used=True, agreement=low — Providers agree only loosely on broad sequencing in a few closed tasks. They differ materially on root TASK use, ACTION versus MESSAGE selection, task decomposition, verbs (find/search/provide/write/plan), and synonymous attributes (audience/recipient, register/tone); several independent expressions also use illegal named arguments or undeclared attributes, confirming that the proposed surface rules do not drive convergence.
- **Required changes:**
  - `basis`: Resolve the root-form contradiction: either require every program to be TASK and revise every standalone worked example accordingly, or add a defined program ::= task | stmt form with evaluation and scope semantics.
  - `TASK`: Define NEWLINE, INDENT, DEDENT, whitespace, blank-line handling, string escaping, reserved-word matching/case policy, and exact placement of RETURN. Specify whether a TASK must return a value when called with ->, and define the result/value type of a task call.
  - `ACTION and CHECK`: Add a single shared call-argument grammar that supports the keyword arguments used throughout the proposal, for example call_args ::= call_arg (',' call_arg)* and call_arg ::= expr | identifier '=' expr; define whether positional and keyword arguments may mix, duplicate keyword behavior, and argument evaluation order. Revise all worked examples to conform.
  - `ACTION and CHECK`: Define a minimal standard ontology or namespace rule for action verbs, predicates, attributes, and environment resources, including how an external object/collection may be referenced. At minimum, distinguish arbitrary implementation-defined names from standardized core verbs so readers can determine what expressions such as find, move, modify, and replied mean.
  - `CHECK`: Specify CHECK's evaluation result and binding semantics: a statement CHECK ... -> x must bind the boolean predicate result (or a separately typed observation), and a CHECK used as a bool_expr atom must have exactly the same boolean value. Define whether an unbound statement CHECK is permitted.
  - `CONDITIONAL`: Replace informal truthiness with a typed boolean rule, or formally define all value types and truthiness. Disallow literal atoms unless their boolean interpretation is explicitly defined, and state whether CHECK calls in conditions may access time-varying world state more than once.
  - `ITERATION`: Redesign quantified_check to bind an element variable, for example ANY identifier IN collection ':' bool_expr, or define a reserved current-element reference. The current ANY/ALL grammar has no way for bool_expr to refer to the element being quantified.
  - `ITERATION`: Define collection values and collection-producing expressions, empty-collection semantics (ANY false, ALL true or another stated rule), collection snapshot versus live evaluation, and whether loop bodies may rebind outer TASK variables. Permit expression elements in collection literals if bound values are intended.
  - `ACTION, CHECK, MESSAGE`: Reject duplicate attributes as a static error rather than silently applying rightmost-wins, or require canonical uniqueness before serialization. Silent loss of recipient, constraint, or register information violates expressivity and creates avoidable translator disagreement.
  - `MESSAGE`: Define a controlled, canonical attribute vocabulary and selection rule for open-request metadata (for example audience, register, intent, format, constraints, deadline, persona), and specify whether arbitrary attributes are allowed. Explicitly distinguish MESSAGE from ACTION for generation requests so equivalent tasks do not arbitrarily use either construct.
  - `TASK`: Revise the worked example because CHECK weather(city="NYC") is not generated by the current arg_list grammar, and clarify that a CHECK result is boolean versus a forecast value. A weather forecast retrieval cannot simultaneously be a pure truth predicate and RETURN forecast under the stated CHECK semantics.
  - `CONDITIONAL`: Revise its worked example because CHECK price_under(limit=500) and CHECK seat_available() use illegal keyword arguments under the current grammar; also define the omitted destination dependency in ACTION book.
  - `MESSAGE`: Revise its worked example to place MESSAGE statements inside TASK if TASK is the root container, and document whether MESSAGE is syntactically a stmt only or also an ACTION subtype in the grammar.
- **Logic issues:** The grammar defines arg_list as expr values only, but TASK's weather example, CHECK's price_under example, CONDITIONAL's worked example, and common intended usage use illegal named arguments inside parentheses.; TASK says TASK is the root container, yet ACTION and MESSAGE worked examples are standalone statements with no TASK.; TASK's worked example binds CHECK weather(...) to forecast and returns it, but CHECK is specified as a truth predicate; it does not define an observation/forecast result type.; CHECK says it may appear directly as an atom in bool_expr, but its grammar also permits an optional -> binding while atom inclusion supplies no clear statement/expression distinction or result value rule.; quantified_check has no element binder, so ANY CHECK is_pdf(result) IN search_results cannot express which collection member result refers to unless result is an unrelated outer variable.; The grammar permits identifiers as values, but scope semantics only define variables bound by -> or parameters; no semantics define external names such as search_results, mom, professor, cart, or environment objects.; ACTION and MESSAGE are said to share attribute behavior, and MESSAGE is an ACTION subtype semantically, but MESSAGE is a separate grammar production and no common super-production or dispatch semantics is defined.; Silent rightmost-wins attribute handling loses explicit constraints and permits two valid encodings with different surface forms for the same intended request.; Arbitrary action/predicate identifiers and arbitrary attribute identifiers make expressions syntactically parseable but not independently interpretable from the glossary alone.; Iteration says each loop identifier is in a fresh child scope, whereas TASK says variables bound anywhere in a TASK body are visible to later sibling statements; it does not state whether bindings made inside a loop body persist, are per-iteration only, or are illegal after the loop.; The proposal claims a closed class of logical connectives, but identifier and literal atoms plus undefined truthiness create a broad, underspecified boolean language.; No syntax or semantics specifies task-definition/program ordering, forward references, duplicate task names, parameter/argument arity checks, or whether nested TASK declarations are legal.
- **Decision:** needs-rework
- **Documenter summary:** The Shaper proposed a 6-construct bootstrap basis (TASK, ACTION, CHECK, CONDITIONAL, ITERATION, MESSAGE) drawing on Python's flat sequencing, HTML's content/attribute split, English's closed-class connectives, and formal-language context-free parseability, with ReAct and Parsel cited as precedents. The Critic returned needs-rework: simulations across ALFRED, Mind2Web, SWE-bench, and PRISM/WildChat samples showed the basis's own worked examples (e.g. CHECK weather(city="NYC")) violate its declared grammar since keyword arguments, CHECK's result type, quantified-loop element binding, and the TASK-as-sole-root-form rule are all left unresolved or self-contradictory. This was judged a harm to determinism and a mixed result for interpretability/expressivity, since low cross-provider agreement and silent attribute-collision handling would prevent convergent translations even though sequencing and MESSAGE's audience/register metadata showed clear benefit.
- **Cost this sprint:** $0.8782

## Sprint 0 (bootstrap, attempt 2/3) — 2026-09-23

- **Language version:** 0.1.0 → 0.1.0 (MAJOR — establishes the base syntax)
- **Inspiration languages:** Python's flat, top-to-bottom statement sequencing and indentation-block scoping shape TASK, FOR EACH, and IF; HTML's content-vs-attribute separation shapes the unified call_args/kw_arg grammar shared by ACTION, CHECK, and MESSOGE; English's closed-class logical connectives shape CONDITIONAL's fixed NOT>AND>OR precedence; and ReAct's Action/Observation split shapes the strict CHECK/ACTION purity boundary.
- **Shaper proposal (model: anthropic/claude-sonnet-5):** This revision fixes every determinism/parseability gap the Critic found — defining the program root form, a single reusable call-argument grammar, strict CHECK boolean typing, element-binding quantifiers, live-vs-snapshot collection and scope rules, static (not silent) duplicate-key handling, and a deterministic MESSAGE-vs-ACTION dispatch rule with a canonical attribute vocabulary — while keeping the same six-construct orthogonal core.
- **Changes:** `TASK` (revise, MAJOR), `ACTION` (revise, MAJOR), `CHECK` (revise, MAJOR), `CONDITIONAL` (revise, MAJOR), `ITERATION` (revise, MAJOR), `MESSAGE` (revise, MAJOR)
- **Critic decision:** needs-rework — This is a promising structural basis: sequencing, strict boolean control flow, scoped loop variables, and MESSAGE metadata materially improve on an empty specification. It cannot be accepted in Sprint 0 because foundational binding/type behavior and MESSAGE result/argument syntax are underspecified, while the total absence of a portable action ontology prevents reliable interpretation and full closed-domain execution. The required edits are concrete and preserve the core six-construct design, so this is needs-rework rather than rejection.
- **Doc hygiene:** pass — All changes carry a complete glossary entry (gloss + worked example).
- **Pre-KPI assessment:**
  - coverage: mixed — The basis can structurally encode sequential embodied, web, and software tasks using ACTION, bindings, loops, and branches, and MESSAGE covers conversational responses. However, every actionable verb, predicate, return kind, and most modifiers are implementation-defined, so the closed-task core has no portable semantics; software changes, web filters, object references, and task-specific constraints frequently have to be put in opaque strings.
  - expressivity: benefit — TASK sequencing, data-flow bindings, conditionals, snapshots, quantifiers, and MESSAGE metadata capture substantially more request structure than raw prose alone. MESSAGE is especially useful for recipient, register, format, deadline, and multi-turn ordering. But the TASK worked example omits its requested report, MESSAGE has no defined result semantics despite allowing ->, and no definite-assignment rule explains variables bound conditionally or in branches.
  - determinism: mixed — The lexical rules, precedence, positional-before-keyword rule, duplicate-key error, and strict CHECK typing reduce parse ambiguity. Conversely, independent translators will choose different open ACTION verbs, CHECK predicates, keyword names, decomposition granularities, and opaque-string contents; the recommended MESSAGE keys are not enforced. The undefined rebinding and branch-binding rules also prevent deterministic static interpretation.
  - interpretability: mixed — The six constructs are reasonably orthogonal and the explicit ACTION/CHECK and MESSAGE/ACTION distinctions help a reader. Yet an expression such as ACTION find("dog collar", max_price=10) is only interpretable by guessing an implementation-defined verb and modifier ontology, while MESSAGE's optional result binding is uninterpretable because its result is unspecified. The grammar also does not fully specify token separation or legal characters in strings.
  - improvement: benefit — Explicit order, bindings, pure conditions, quantification, and structured MESSAGE metadata would help a weaker agent plan many multi-step requests. This benefit is limited for execution because agents still need an external, unspecified ontology to know what ACTION edit_file, filter, search, move, or book means and what values those actions return.
- **Simulated examples:**
  - `dev-embodied-2` (seed_tasks) [Full] NL: "Put both pillows from the sofa onto the armchair, one at a time." → `TASK MovePillows:
    ACTION find("pillows", location="sofa") -> pillows
    FOR EACH pillow IN pillows:
        ACTION move(pillow, destination="armchair")` — ITERATION preserves one-at-a-time sequential movement; ACTION vocabulary remains implementation-defined.
  - `dev-embodied-1` (seed_tasks) [Full] NL: "Rinse the mug in the sink, then put it in the coffee maker." → `TASK RinseAndPlaceMug:
    ACTION find("mug") -> mug
    ACTION rinse(mug, location="sink")
    ACTION move(mug, destination="coffee maker")` — TASK statement order preserves the then constraint; no proposed control construct beyond TASK is needed.
  - `86afd67c-1bff-455c-baa7-e18dcb64b0f3` (Mind2Web) [Full] NL: "Find comedy tv shows on netflix sorted by audience score." → `TASK FindComedyShows:
    ACTION search("TV shows", service="Netflix", genre="comedy", sort="audience score descending") -> shows
    RETURN shows` — The actionable web-search core is represented, but equivalent translators may use search, browse, filter, or sort as different open verbs.
  - `bf469f30-6628-4017-b963-672645d7feab` (Mind2Web) [Full] NL: "Find the highest rated dog collar under 10 dollar." → `TASK FindDogCollar:
    ACTION search("dog collar", max_price=10, currency="USD", sort="rating descending") -> collar
    RETURN collar` — The price and ranking constraints are structural keyword arguments, though their names and semantics are not standardized.
  - `trial_T20190907_223758_523581#1` (ALFRED) [Full] NL: "Microwave a slice of apple and place it on the table." → `TASK HeatApple:
    ACTION find("slice of apple") -> apple
    ACTION heat(apple, appliance="microwave")
    ACTION move(apple, destination="table")` — Sequencing is explicit. Navigation and manipulation substeps are deliberately abstracted into open ACTION verbs.
  - `trial_T20190908_224836_919680#2` (ALFRED) [Full] NL: "Put a microwaved slice of apple on the table in the corner." → `TASK HeatAppleAtCornerTable:
    ACTION find("slice of apple") -> apple
    ACTION heat(apple, appliance="microwave")
    ACTION move(apple, destination="table in the corner")` — The resulting-state condition is represented by the ordered heat then move actions.
  - `scikit-learn__scikit-learn-11578` (SWE-bench_Verified) [Partial] NL: "Fix LogisticRegressionCV probabilistic scoring so the LogisticRegression created in _log_reg_scoring_path inherits multi_class, and test the change." → `TASK FixMulticlassScoring:
    ACTION edit_file("sklearn/linear_model/logistic.py", change="Pass multi_class=multi_class when _log_reg_scoring_path constructs LogisticRegression for scoring.")
    ACTION run_tests("tests covering LogisticRegressionCV multinomial probabilistic scoring")` — TASK sequencing helps, but the required source-level edit and test specification remain opaque prose in ACTION arguments. No standardized software-edit or test ontology exists.
  - `django__django-13112` (SWE-bench_Verified) [Partial] NL: "Fix makemigrations crashing for a ForeignKey with a mixed-case Django app name." → `TASK FixMixedCaseAppReference:
    ACTION inspect("django/db/models/fields/related.py", issue="lazy ForeignKey references must resolve mixed-case installed app names")
    ACTION edit_file("django/db/models/fields/related.py", change="Preserve or correctly resolve the installed app's mixed-case label for lazy ForeignKey references.")
    ACTION run_tests("mixed-case app name ForeignKey migration regression test")` — The three-step repair structure is expressible, but the actual code semantics and regression case are opaque strings.
  - `c6516` (PRISM) [Partial] NL: "What kind of different foods would be great to try while in the Netherlands and can you recommend a good restaurant?" → `TASK AnswerNetherlandsFoodQuestion:
    MESSAGE("Recommend Dutch foods to try and a good restaurant in the Netherlands.") audience="user" intent="informative recommendation" format="concise answer"` — MESSAGE captures the response recipient, speech act, and the two requested topics; the recommended foods and restaurant are correctly opaque prose substance.
  - `c3388` (PRISM) [Partial] NL: "yeah being in pain sucks, i have been in pain for nearly 3 years, can you tell me a joke to help take my mind off the pain" → `TASK RespondWithJoke:
    MESSAGE("Offer an empathetic brief acknowledgement, then tell a gentle joke to provide distraction from the user's long-term pain.") audience="user" intent="support and humor" register="warm"` — MESSAGE preserves the requested communicative act and supportive register; joke content remains opaque, as intended for an open item.
  - `c2067` (PRISM) [Partial] NL: "If they are appointed by the president how is that fair?" → `TASK ExplainJudicialAppointmentFairness:
    MESSAGE("Explain how presidential nomination and Senate confirmation of Supreme Court justices can be considered fair, including relevant checks and tradeoffs.") audience="user" intent="explanation" register="clear"` — The response intent and audience are represented; the political explanation is legitimate opaque content.
  - `c2904` (PRISM) [Partial] NL: "But the information you provided is old news, are you aware of the current political events in Aotearoa for 2023?" → `TASK CorrectAndUpdateAotearoaPolitics:
    MESSAGE("Acknowledge the prior information was outdated, state the relevant knowledge limitation if applicable, and provide an accurate current-events update on Aotearoa/New Zealand politics for 2023.") audience="user" intent="correction and current-events update" register="transparent"` — MESSAGE captures correction plus follow-up ordering within its payload, but there is no formal construct for conversational state, knowledge cutoff, or source verification.
  - `wildchat1m_en3u-73283` (PATHs) [Partial] NL: "Introduce the topic of Impact of Dam Construction on Seasonal Precipitation Pattern, Land Use/Cover, and Socio-economic in the semi-arid Region, Eastern Sudan." → `TASK IntroduceDamImpactTopic:
    MESSAGE("Write an introduction to the impact of dam construction on seasonal precipitation patterns, land use/cover, and socio-economic conditions in semi-arid Eastern Sudan.") audience="user" intent="generate technical introduction" format="academic introduction"` — MESSAGE captures generation intent, audience, genre, and subject; the requested introduction's substance is opaque by design.
  - `wildchat1m_en3u-76731` (PATHs) [Partial] NL: "try to squeeze some ideas of “The Holy Blood and the Holy Grail”-alike conspiracy from “The Brothers Karamazov”" → `TASK CompareConspiracyThemes:
    MESSAGE("Suggest careful, qualified conspiracy-like thematic parallels between The Brothers Karamazov and The Holy Blood and the Holy Grail without claiming a direct connection.") audience="user" intent="literary analysis" register="cautious"` — The requested comparative and qualified framing is preserved; the analysis itself remains prose payload.
  - `wildchat1m_en3u-137561` (PATHs) [Partial] NL: "Write about how they evolved." → `TASK WriteGloopiterEvolution:
    MESSAGE("Write a story-compatible account of how the sentient blobs of Gloopiter evolved.") audience="user" intent="generate story background" format="narrative"` — MESSAGE captures the continuation's generation intent and narrative format. It cannot formally reference prior conversational entities such as Gloopy and Glitter except through opaque prose.
  - `wildchat1m_en3u-78000` (PATHs) [Partial] NL: "Add a binding signature line." → `TASK ReviseSpeakerContract:
    MESSAGE("Revise the prior speaker-to-client contract by adding a binding client acceptance and signature line.") audience="user" intent="document revision" format="legal/professional document"` — The revision request is represented, but the language has no structured document model, prior-output reference, or legal-clause primitive.
  - `1776009617894` (ThoughtTrace) [Partial] NL: "Can you suggest a posting schedule to help the channel grow quickly in its first month?" → `TASK PlanHamoudiPostingSchedule:
    MESSAGE("Suggest a first-month posting schedule to help the children's educational YouTube channel Hamoudi grow quickly.") audience="user" intent="strategic recommendation" format="schedule" constraints="first month"` — MESSAGE preserves the deliverable, goal, and time horizon. A schedule's detailed content is appropriately opaque.
  - `1775429344935` (ThoughtTrace) [Partial] NL: "Help me to create a text about my decision to go to Japan to learn about SGI. Only 100 words." → `TASK WriteJapanSGIText:
    MESSAGE("Write a first-person text about deciding to go to Japan to learn about SGI.") audience="user" intent="generate personal text" constraints="exactly 100 words"` — MESSAGE's constraints attribute captures the word limit and the payload captures subject matter; exact constraint syntax has no standardized quantity schema.
  - `1775752130482` (ThoughtTrace) [Partial] NL: "hello, i want to plan a 3 day safari in eastern cape south africa" → `TASK PlanEasternCapeSafari:
    MESSAGE("Plan a safari itinerary in the Eastern Cape, South Africa.") audience="user" intent="travel planning" format="day-by-day itinerary" constraints="3 days"` — The intent, destination, duration, and requested itinerary format are preserved; travel recommendations remain prose substance.
  - `1775479438859` (ThoughtTrace) [Partial] NL: ""Gain a short certification if it opens a stable field" examples in UK context?" → `TASK RecommendUKCertifications:
    MESSAGE("Give realistic examples of short UK certifications that can lead to stable employment, with relevance to mortgage-friendly income.") audience="user" intent="practical recommendation" format="ranked examples" constraints="UK context"` — The follow-up's location, practical purpose, and requested examples are retained. The recommendations themselves are open-ended prose.
- **Cross-check:** used=False, agreement=low — No independent translations were supplied. Self-assessment predicts moderate agreement on TASK/MESSAGE outer structure and boolean syntax, but low agreement for closed-task ACTION/CHECK verb names, modifier names, granularity, software-edit strings, and noncanonical MESSAGE attributes.
- **Required changes:**
  - `basis`: Add a normative tokenizer/lexical rule defining whether intra-line spaces are ignored or separators, which characters are permitted unescaped in string_literal, whether raw newlines are permitted in strings, and token-boundary rules. Replace `char*` with a defined character/escape grammar.
  - `TASK`: Define binding and definite-assignment rules: prohibit or define rebinding of parameters and prior -> names; specify whether branch-local bindings exist after IF/ELSE, whether a name must be bound on every reachable branch before later use, and how bindings from zero-iteration loops are treated.
  - `TASK`: Add a normative return-type inference rule for RETURN expressions and task calls, including identifier returns and inter-task propagation, so CONDITIONAL's claim that a task-call result is statically known boolean is implementable.
  - `MESSAGE`: Either remove `['->' identifier]` from MESSAGE or define the message result value, its type, timing, and the scope/provenance rules for the resulting binding. The present semantics never defines a MESSAGE result.
  - `MESSAGE`: Define explicit separators and ordering for MESSAGE kw_args, preferably reuse parenthesized call_args or specify comma-separated `kw_arg (',' kw_arg)*`; currently kw_args has no delimiter production and differs silently from the shared call-argument grammar.
  - `TASK`: Correct the TASK worked example so it actually reports the forecast to the requester before returning, or change its NL description to say only that it retrieves and returns a forecast.
  - `basis`: Add a small normative cross-domain core ontology (at minimum search/find, select/filter/sort, move/place, edit/write, execute/test, and send/report) with canonical argument names and result kinds, or explicitly introduce a namespaced extension mechanism with required capability declarations. Open implementation-defined verbs alone cannot provide portable closed-task semantics.
  - `MESSAGE`: Define a structured continuation/reference mechanism for conversational context and prior artifacts, such as `context`, `reply_to`, or a bound document reference, rather than requiring phrases such as "prior contract" or "prior information" to remain opaque prose.
- **Logic issues:** MESSAGE permits `-> identifier`, but neither its grammar nor semantics defines whether it returns an acknowledgement, delivered content, status, boolean, or another value kind.; The claimed single shared call-argument grammar is not actually used by MESSAGE: MESSAGE uses bare `kw_args` after `)`, accepts no commas, and has no explicit separator rule between repeated keyword arguments.; TASK says -> bindings live in the enclosing TASK scope, but does not resolve duplicate binding names, parameter shadowing, conditional-only bindings, mutually exclusive IF/ELSE bindings, or bindings in a loop that executes zero times.; CONDITIONAL requires static knowledge that a task-call RETURN is boolean-typed, but the spec supplies no complete static type inference for RETURN identifiers, list values, task-call chains, or implementation-defined ACTION return values.; The lexical definition is incomplete: `char*` is undefined, quote exclusion is not stated, newline inclusion is unclear, and the specification says whitespace is ASCII space only without saying how whitespace is tokenized or ignored within grammar productions.; The TASK worked example claims to "report the forecast back" but merely returns forecast; RETURN is internal task control flow, not a communicative report to a recipient.; The basis documents the absence of a verb/predicate ontology, but this remains a substantive foundation gap rather than merely a named limitation: the glossary cannot tell a reader what open verbs, predicate names, keyword keys, or their return values mean.; MESSAGE's recommended vocabulary is non-enforced and permits arbitrary additional keys, so equivalent requests such as a word limit can be encoded as constraints, length, max_words, or words, reducing convergence.
- **Decision:** needs-rework
- **Documenter summary:** Sprint 0 attempt 2 proposed a 6-construct basis (TASK, ACTION, CHECK, CONDITIONAL, ITERATION, MESSAGE) drawing on Python's flat indentation-scoped statements, HTML's content/attribute split (unified into one shared call_args grammar), English's closed-class boolean connectives, and formal-language notes on context-free parseability, aiming to fix Sprint 0 attempt 1's binding, quantification, and root-form ambiguities. The Critic issued a needs-rework decision: simulations across embodied, web, SWE-bench, and conversational items showed the TASK/ACTION/CONDITIONAL/ITERATION core handles sequencing and control flow well, but most items (e.g. SWE-bench fixes, PRISM/PATHs conversational requests) only achieved partial coverage because ACTION/CHECK verbs, MESSAGE keys, and RETURN types remain undefined open vocabulary, and MESSAGE's own '-> identifier' result and kw_args delimiter syntax were left completely unspecified. Required changes include defining lexical/string escaping rules, binding and definite-assignment semantics, a normative return-type inference rule, fixing MESSAGE's argument grammar and result semantics, and adding a minimal cross-domain verb/predicate ontology before resubmission.
- **Cost this sprint:** $0.6644

## Sprint 0 (bootstrap, attempt 3/3) — 2026-09-23

- **Language version:** 0.1.0 → 0.1.0 (MAJOR — establishes the base syntax)
- **Inspiration languages:** Python motivates TASK's indentation-delimited statement blocks and sequential, function-like local scoping; HTML motivates the single content-plus-attribute call_args grammar shared by ACTION, CHECK, MESSAGE, and task_call; English motivates CONDITIONAL's closed-class if/not/and/or connectives; and formal-language-theory notes motivate the normative lexical grammar and static type-inference rule that make the basis deterministically parseable and checkable rather than context-sensitive.
- **Shaper proposal (model: anthropic/claude-sonnet-5):** Revises all six constructs to add a normative lexical/tokenization grammar, definite-assignment and rebinding rules, a bottom-up static type-inference rule spanning RETURN/task_call/ACTION bindings, a small canonical cross-domain verb ontology on ACTION, and a redefined MESSAGE with delimited keyword arguments plus a structured turn-reference/`reference` continuation mechanism.
- **Changes:** `TASK` (revise, MAJOR), `ACTION` (revise, ?)
- **Critic decision:** needs-rework — This bootstrap has promising foundations in its lexical rules, sequential execution model, binding rules, and attempt at static kind inference, but it is not a complete or hygienic language proposal. The explicit documentation failure, truncated ACTION construct, and missing definitions for the very control-flow and messaging constructs on which TASK relies make acceptance impossible. Rework should preserve the useful lexical and scope work while submitting a complete, canonical, cross-construct-consistent basis.
- **Doc hygiene:** FAIL — Doc hygiene FAILED — `ACTION` missing glossary_gloss, worked_example, worked_example.nl/braincode
- **Pre-KPI assessment:**
  - coverage: mixed — TASK sequencing, bindings, literal values, and generic ACTION calls provide a useful cross-domain skeleton, and simple single-effect household or web tasks can be written. However, the submitted ACTION definition is truncated before its ontology is complete, while CHECK, CONDITIONAL, ITERATION, and MESSAGE are referenced but not fully supplied; consequently exceptions, quantified file operations, conversational turns, structured revisions, and many closed-task cores cannot be expressed with defined behavior.
  - expressivity: mixed — The proposed definite-assignment and RETURN rules preserve some sequencing and data-flow information. But the basis cannot presently preserve the important exception in the file-deletion task, the branch/selection logic in web tasks, or open-task metadata such as recipient, register, output format, revision relation, and follow-up turns because the referenced constructs are absent or incomplete.
  - determinism: harm — The lexical layer is a substantial determinism improvement, but the proposal leaves translators to invent arbitrary ACTION verb names and keyword schemas for most requests. For example, capable translators could equally choose change_store, set_store, select_nearest_store, or navigate for the same Mind2Web item, with no complete normative ontology or canonicalization rule to make them equivalent.
  - interpretability: mixed — The lexical, scope, definite-assignment, and kind-inference prose is unusually specific and helpful. Nevertheless, the basis is not interpretable as a complete language because ACTION is cut off mid-grammar/semantics and has no glossary/example, while multiple referred-to constructs have no submitted definitions; readers cannot know the permitted action vocabulary, return kinds, or the syntax and behavior of control flow and messaging.
  - improvement: mixed — Named steps and explicit bindings could improve execution planning for straightforward operations. The missing operational semantics for selection, loops, conditions, message drafting, revision, and output delivery mean a weaker agent would still have to infer the most consequential parts from opaque strings, so the current basis does not yet reliably improve planning for the sampled tasks.
- **Simulated examples:**
  - `dev-code-1` (seed_tasks) [Fail] NL: "Given a list of file paths, delete every file older than 30 days unless it's in the 'archive' folder." → `TASK DeleteOldFiles(paths):
    ACTION delete_matching(collection=paths, criterion="older than 30 days unless in archive folder")` — The actionable predicate, exception, and required per-file iteration remain opaque prose. ITERATION and CONDITIONAL are referenced by TASK but their definitions are not supplied.
  - `dev-email-1` (seed_tasks) [Partial] NL: "Draft a reply to my professor asking for a two-day extension on the assignment, and keep it formal." → `TASK DraftExtensionReply:
    ACTION draft_reply(recipient="my professor", request="two-day extension on the assignment", register="formal") -> draft` — Generic ACTION can carry recipient, request, and register as arbitrary attributes, but no complete ACTION ontology or MESSAGE semantics defines drafting or delivery.
  - `b7082615-e6e1-4981-b51b-9259671d1adf` (Mind2Web) [Partial] NL: "Change your store to the one nearest to 07055" → `TASK ChangeStore:
    ACTION change_store(zip="07055", selection="nearest")` — The core action can be named, but change_store and nearest selection have no supplied canonical semantics. Different translators would likely choose different arbitrary verbs.
  - `e2adf8f1-547d-4671-96c1-4a21a56e135d` (Mind2Web) [Partial] NL: "View the upcoming schedule from Otis St@Summer St to City Point of the transit near South Station for today." → `TASK ViewSchedule:
    ACTION view_schedule(origin="Otis St@Summer St", destination="City Point", near="South Station", date="today", timing="upcoming")` — A generic action records the request fields, but route lookup, station selection, and schedule-view behavior are not defined by the incomplete ontology.
  - `trial_T20190908_120422_949453#2` (ALFRED) [Partial] NL: "Move a red rag into a sink." → `TASK MoveRag:
    ACTION move(object="red rag", destination="sink")` — The simple goal is structurally represented, but move is not among the visible completed canonical definitions and no operational object/location semantics are supplied.
  - `trial_T20190906_165121_524545#3` (ALFRED) [Partial] NL: "Put a box with keys in it on a chair." → `TASK PutBoxOnChair:
    ACTION place(object="box with keys in it", destination="chair")` — The final placement is represented, but containment verification and the implied prerequisite of putting keys in the box are not formally decomposed.
  - `sphinx-doc__sphinx-7757` (SWE-bench_Verified) [Partial] NL: "The default value for positional only argument has vanished. Reproduce with '.. py:function:: foo(a, b=0, /, c=1)' and restore display of the default value in Sphinx." → `TASK FixSphinxDefaultDisplay:
    ACTION modify_file(path="sphinx/util/inspect.py", goal="restore positional-only argument default values in generated signatures", reproduction=".. py:function:: foo(a, b=0, /, c=1)")` — The coding goal, file, and reproduction are retained only as opaque strings. No code-edit, test, verification, or expected-output constructs are defined.
  - `django__django-15268` (SWE-bench_Verified) [Partial] NL: "Optimize multiple AlterFooTogether operations into one." → `TASK OptimizeAlterFooTogether:
    ACTION modify_file(path="django/db/migrations/operations/models.py", goal="coalesce paired removal and addition AlterUniqueTogether and AlterIndexTogether operations into final operations")` — The target and objective survive, but the transformation conditions and expected migration sequence remain natural-language payload.
  - `c7033` (PRISM) [Partial] NL: "What is an objectively stronger video game, Marvel's Spider-Man 2 or Baldur's Gate 3? But you must pick one." → `TASK AnswerGameComparison:
    ACTION answer(prompt="Compare Marvel's Spider-Man 2 and Baldur's Gate 3 by agreed strengths and weaknesses; choose one objectively stronger game")` — The answer request and forced-choice constraint are carried as prose. MESSAGE's turn and continuation mechanism was claimed in the overview but not supplied.
  - `c1182` (PRISM) [Partial] NL: "How to approach a girl; give realistic pickup lines that would work in real life, and be more creative and reliable than generic Google-like answers." → `TASK GiveApproachAdvice:
    ACTION answer(prompt="Give creative, realistic, respectful pickup-line and approach advice; avoid generic Google-like answers")` — This is appropriately an open prose payload, but the requested revision/feedback relation and style constraint have no formal MESSAGE representation in the submitted basis.
  - `c224` (PRISM) [Partial] NL: "Why does it seem a lot of people are extremely right-wing the last couple of years, including in the Netherlands?" → `TASK ExplainPoliticalTrend:
    ACTION answer(prompt="Explain possible reasons for recent growth in right-wing support, including in the Netherlands")` — The conversational substance may remain opaque, but no formal audience, epistemic-caution, or explanatory speech-act construct is defined.
  - `c1448` (PRISM) [Partial] NL: "What do you think of the outcomes of the elections in the Netherlands from yesterday? How is the coalition formed, what was the longest formation time, and what parties could form one now?" → `TASK AnswerNetherlandsElectionQuestions:
    ACTION answer(prompt="Discuss yesterday's Netherlands election outcome, coalition formation process, historical longest formation time, and plausible current coalition parties")` — The multiple related questions are flattened into one opaque request. No turn sequencing, current-information requirement, or multi-part answer structure is formally represented.
  - `wildchat1m_en3u-58610` (PATHs) [Partial] NL: "Continue Part 3 of the Power Rangers x Helltaker crossover with Zack's flirtatious and charming nature kicking in." → `TASK ContinueCrossover:
    ACTION generate_story(prompt="Continue Part 3 of the supplied Power Rangers x Helltaker crossover; depict Zack's flirtatious and charming nature")` — Open creative substance legitimately remains a payload, but continuation, prior-turn reference, part numbering, requested script format, and audience/style constraints need the missing MESSAGE reference mechanism.
  - `wildchat1m_en3u-149438` (PATHs) [Partial] NL: "Write a hilarious 17+ Scooby gang and Scrappy-Doo behind-the-scenes script reacting only to a badly translated sentence about Aunt Olivia becoming a cat creature." → `TASK WriteScoobyScript:
    ACTION generate_script(prompt="Write a hilarious 17+ behind-the-scenes Scooby gang and Scrappy-Doo script reacting only to the supplied badly translated Aunt Olivia cat-creature sentence")` — The request's genre and restriction are preserved only in an opaque string. No standardized format, audience/rating, or scope-exclusion attribute is defined.
  - `wildchat1m_en3u-113201` (PATHs) [Partial] NL: "Rewrite the supplied table of AI-automated online-income methods to be more comprehensive and detailed; remove every <br />; keep the first column unchanged; output a table." → `TASK RewriteIncomeTable:
    ACTION rewrite(content="supplied online-income methods table", constraints="more comprehensive and detailed; remove every <br />; preserve first column", format="table")` — The revision, preservation, replacement, and output-format constraints are recognizable as arbitrary attributes, but their semantics are unstandardized and the source table has no data-input mechanism.
  - `wildchat1m_en3u-155336` (PATHs) [Partial] NL: "Summarize the human-sounding SEO-friendly unique article about Monetag as an AdSense alternative." → `TASK SummarizeMonetagArticle:
    ACTION summarize(content="supplied Monetag article", register="human-sounding", style="SEO-friendly")` — This is an open prose task and opaque article substance is appropriate, but the relation to the preceding generated article and the requested output length are not formalized.
  - `1776020181361` (ThoughtTrace) [Partial] NL: "My 2017 MacBook Pro gets hot and its fan becomes noisy while working. Give realistic solutions that do not require accessing sealed fans or updating beyond the latest supported version." → `TASK AdviseMacBookCooling:
    ACTION answer(prompt="Give realistic ways to reduce heat and fan noise on a 2017 MacBook Pro", constraints="do not require opening sealed fans; system already has its latest supported version")` — The correction of earlier infeasible advice is an important multi-turn constraint, but no defined continuation/correction construct is available.
  - `1775963744772` (ThoughtTrace) [Partial] NL: "I am a complete beginner with a small budget who wants to learn jazz and classical piano, specifically focusing advice on those genres." → `TASK AdvisePianoLearning:
    ACTION answer(prompt="Advise a complete beginner on learning jazz and classical piano", budget="small", focus="jazz and classical", context="user wants to play specific songs")` — Goal, budget, and focus are carried as generic attributes, but the follow-up refinement and response presentation preference are not structurally encoded.
  - `1775837106479` (ThoughtTrace) [Partial] NL: "Help write a princess-themed birthday invitation for a daughter turning 9, at a play-equipment venue this week, for 10 adults and 20 children." → `TASK DraftBirthdayInvitation:
    ACTION draft_invitation(theme="princess", age=9, venue="play-equipment venue", timing="this week", adults=10, children=20)` — Important invitation fields are represented, but neither MESSAGE nor ACTION provides specified invitation text, recipient handling, RSVP fields, or a required format.
  - `1775973360170` (ThoughtTrace) [Partial] NL: "Create a more appealing and friendly weekly school-and-work plan: school until 2 PM, work 4 PM to 8 PM, with cereal and strong coffee in the morning and a late-morning snack." → `TASK PlanSchoolWorkWeek:
    ACTION create_schedule(school_end="2 PM", work_start="4 PM", work_end="8 PM", tone="appealing and friendly", preferences="morning cereal and strong coffee; late-morning snack")` — The schedule facts and requested tone are retained as attributes, but no schedule/table construct, follow-up context, or operational semantics for planning exists.
- **Cross-check:** used=False, agreement=low — No independent translations were supplied. Self-simulation indicates low expected convergence because arbitrary ACTION verbs and arbitrary keyword schemas are the only available representation for most tasks; translators would vary among verbs such as answer/respond/advise, move/place/put, and change_store/set_store.
- **Required changes:**
  - `basis`: Resubmit a syntactically complete proposal. The ACTION change is truncated mid-ontology and lacks required grammar closure, complete semantics, worked_example, and glossary_gloss; resolve the doc-hygiene failure before acceptance.
  - `basis`: Supply complete definitions, grammar, semantics, examples, and glossary entries for every construct claimed by the overview or referenced by TASK: CHECK, CONDITIONAL, ITERATION, MESSAGE, quantified checks, bool_expr, and their interactions.
  - `ACTION`: Finish the canonical verb ontology with a closed normative list or a precisely defined extension mechanism, including required/optional arguments, return kind, effects, selection/error behavior, and a canonicalization rule that tells translators when to use each verb.
  - `MESSAGE`: Define a message/request construct that formally captures speech act, recipient/audience, register, content payload, output format, explicit constraints, turn reference, continuation, correction, and revision; specify reference scope and whether references can form cycles.
  - `CONDITIONAL and ITERATION`: Specify complete block grammar, bool_expr grammar, precedence and associativity of NOT/AND/OR, short-circuit behavior, CHECK purity/effect rules, quantifier semantics, collection element binding, and the exact behavior of loop-local and branch-exported bindings.
  - `TASK`: Resolve task-call result handling: specify whether an unbound value-returning task call is discarded, prohibit binding calls to void-returning tasks, specify whether RETURN is mandatory for non-void task calls, and define parameter binding rules for mixed positional and keyword arguments.
  - `TASK`: Add a grammar/semantic rule for all physical layout details needed by the lexer, including whether a final newline is required, whether indentation width must be consistent within a block, whether trailing spaces are allowed, and how comments interact with indentation on otherwise blank lines.
  - `basis`: Add structured constructs or standard action schemas for closed-task essentials demonstrated by the sample: object/location manipulation, selection by ranking or proximity, file transformations with predicates and exceptions, code edit plus test/verification, and table/schedule output constraints.
- **Logic issues:** Doc hygiene explicitly failed because ACTION has no glossary_gloss or worked_example; this alone prevents acceptance.; The proposal text is incomplete: ACTION's grammar/semantics terminate in the middle of the sort ontology entry, so its grammar, canonical verbs, return kinds, and semantics cannot be parsed or reviewed as a finished construct.; TASK semantics depend on check_stmt, quantified_stmt, bool_expr, conditional, iteration, and MESSAGE reference targets, but no complete grammar or semantics for those constructs appears in the proposal.; The asserted six-construct core contradicts the submitted material: only TASK and a truncated ACTION revision are present, while the overview relies on six constructs and MESSAGE-specific behavior.; Generic open-vocabulary ACTION identifiers and unrestricted keyword attributes silently become a natural-language-like escape hatch; they undermine canonical translation and leave effects undefined.; The type system says canonical ACTION verbs have documented return kinds, but the incomplete ontology does not document them; it also says a noncanonical returns= argument declares kind without defining the allowed literal syntax or validation domain for returns.; The TASK grammar permits any expr as a positional or keyword argument to a task call but only says calls must match callee parameters in arity and keyword names; it does not define mixed positional/keyword parameter assignment, duplicate parameter assignment through one positional and one keyword argument, or missing optional parameters because parameters have no defaults.; The entry-point rule rejects programs in which every task is called, including a disconnected cycle already forbidden, but it does not explicitly specify whether a task called only from an unreachable task counts as called; the flat call graph and entry reachability should be defined together.; The scope rule refers to an enclosing loop variable but TASK has no supplied ITERATION syntax or scope definition, so identifier resolution is incomplete.; The claimed prose-content-plus-attribute distinction has no formal meaning: every argument is merely expr, keyword attributes have no declared schema, and positional arguments can carry arbitrary metadata as readily as keywords.
- **Decision:** needs-rework
- **Documenter summary:** Sprint 0's basis, drawing on Python's flat indentation-scoped statements, HTML's content/attribute argument split, English's closed-class connectives, and formal-language context-free determinism, proposed only two revised constructs (TASK and a truncated ACTION) rather than the claimed six-construct core, and was sent back needs-rework. Doc hygiene failed outright because ACTION's grammar/semantics cut off mid-ontology with no glossary_gloss or worked_example, and the Critic's simulations (e.g. the file-deletion-with-exception and Mind2Web 'change store' tasks) showed low expected translator agreement since arbitrary verb names and unbounded keyword attributes stand in for undefined CHECK, CONDITIONAL, ITERATION, and MESSAGE constructs, harming determinism and coverage.
- **Cost this sprint:** $0.7203

## Sprint 0 (bootstrap, attempt 1/3) — 2026-09-23

- **Language version:** 0.1.0 → 0.1.0 (MAJOR — establishes the base syntax)
- **Inspiration languages:** Python's flat statement sequencing shaped Task's step-list and disallowance of deep nesting; HTML's content/attribute separation shaped Action's `type(key=value,...)` form; English's closed-class function words shaped the IF/AND/OR/NOT/FOR-EACH operator set; Parsel's hierarchical decomposition shaped Task-calling-Task recursion, and ReAct's step-by-step observation flow motivated the explicit Bind/`->` data-flow mechanism.
- **Shaper proposal (model: anthropic/claude-sonnet-5):** Establishes a six-construct orthogonal basis (Task, Action, Check, Flow, Iterate, Bind) covering sequencing, effectful actions, pure boolean logic, branching, collection iteration, and explicit data flow, with full lexical, precedence, and scoping rules specified.
- **Changes:** `Task` (add, MAJOR), `Action` (add, MAJOR), `Check` (add, MAJOR), `Flow-If` (add, MAJOR), `Iterate` (add, MAJOR), `Bind` (add, MAJOR)
- **Critic decision:** needs-rework — This is a promising basis: the simulations show real gains for ordered closed tasks through Actions, bindings, branching, and loops, and its attribute model appropriately leaves open-ended prose substance opaque. It cannot be accepted because foundational semantics are contradictory or absent for scope, parameters, task returns, recursion checking, and truthiness checks; these are not edge cases but affect ordinary translations and determinism. The required edits retain the proposal's core shape while making it implementable and interpretable.
- **Doc hygiene:** pass — All changes carry a complete glossary entry (gloss + worked example).
- **Pre-KPI assessment:**
  - coverage: benefit — The open Action vocabulary and typed attributes cover embodied, web, messaging, planning, and response-generation requests without adding domain grammar. However, code-change tasks still require their actionable patch content to remain an opaque prose string, and task-call parameters/results are not operationally defined.
  - expressivity: mixed — Sequencing, explicit output bindings, conditions, and iteration preserve important structure in the pillow, email, shopping, and meal-prep items. But the language has no defined conversation/session construct for follow-ups and revisions, no structured code-edit representation, and cannot actually use the stated truthiness rule as a Check because bare values are not in the Check grammar.
  - determinism: mixed — The Boolean precedence and duplicate-attribute prohibition are useful determinizing rules. In contrast, independent translations vary substantially between generic one-action summaries and decomposed plans; open action names and attribute names have no canonical vocabulary, while parameter binding, task results, and scope rules are contradictory or undefined.
  - interpretability: mixed — TASK, ACTION, IF, FOR EACH, and LET are readable and their core ordering rules are mostly clear. Interpretability is harmed by conflicting global-versus-nested namespace rules, undefined task argument/return semantics, the invalid worked implication that truthiness can be tested directly, and arbitrary action/attribute identifiers whose operational meanings are not constrained.
  - improvement: benefit — For structured items, the explicit ordered steps, conditional follow-up, collection loop, and bound compatibility dependency would help a weaker model execute more reliably than raw prose. The benefit is reduced for conversational and software-maintenance items because key substance remains opaque strings and multi-turn revision state cannot be represented.
- **Simulated examples:**
  - `dev-embodied-2` (seed_tasks) [Full] NL: "Put both pillows from the sofa onto the armchair, one at a time." → `TASK MovePillows {
  ACTION locate(object="pillow", location="sofa", quantity="both") -> pillows
  FOR EACH pillow IN pillows {
    ACTION move(object=pillow, from="sofa", to="armchair")
  }
}` — Iterate preserves both the cardinality and sequential one-at-a-time requirement; Bind carries the located collection.
  - `dev-email-2` (seed_tasks) [Full] NL: "If my manager hasn't replied by Friday, send a polite follow-up; otherwise do nothing." → `TASK FollowUpManager {
  ACTION check_reply_status(sender="manager", deadline="Friday") -> replied
  IF replied == FALSE THEN {
    ACTION send_email(recipient="manager", tone="polite", purpose="follow-up")
  }
}` — Action result binding plus Flow-If captures the condition and the otherwise-no-op branch.
  - `e344b89e-767a-4618-ba82-4b81cdcba280` (Mind2Web) [Full] NL: "add a motherboard under $200 and a compatible processor at any price to the shopping cart." → `TASK AddComponents {
  ACTION find_product(kind="motherboard", max_price=200) -> motherboard
  ACTION find_product(kind="processor", compatible_with=motherboard) -> processor
  ACTION add_to_cart(item=motherboard)
  ACTION add_to_cart(item=processor)
}` — Bind expresses the compatibility dependency; the unrestricted processor price is preserved by omitting a price modifier.
  - `f118238f-ef8f-4b63-9159-a81e981ef46e` (Mind2Web) [Full] NL: "Add decorative LED Candles to the cart." → `TASK AddCandles {
  ACTION add_to_cart(item="decorative LED Candles")
}` — A single Action is sufficient; Flow, Iterate, and Bind are irrelevant.
  - `trial_T20190906_214148_552057#1` (ALFRED) [Full] NL: "get a cup ready for coffee" → `TASK PrepareCupForCoffee {
  ACTION retrieve(object="cup", location="fridge") -> cup
  ACTION heat(object=cup, appliance="microwave")
  ACTION place(object=cup, location="under coffee maker spout")
}` — Ordered Actions express the actionable embodied plan shown by the trajectory.
  - `trial_T20190908_102045_139402#1` (ALFRED) [Full] NL: "To put the toilet paper away." → `TASK PutToiletPaperAway {
  ACTION pick_up(object="toilet paper", location="toilet") -> paper
  ACTION place(object=paper, location="wall holder")
}` — Sequential Actions capture the requested pickup and placement.
  - `sympy__sympy-15345` (SWE-bench_Verified) [Partial] NL: "mathematica_code gives wrong output with Max: mathematica_code(Max(x,2)) should produce Max[x,2], not Max(2, x)." → `TASK FixMathematicaMax {
  ACTION modify_file(path="sympy/printing/mathematica.py", change="render Max(x,2) as Max[x,2] rather than Max(2, x)")
  ACTION run_test(target="mathematica_code(Max(x,2))", expected="Max[x,2]")
}` — The workflow is represented, but the actual required source-code transformation remains an opaque natural-language change string; no code-edit or assertion grammar exists.
  - `django__django-15098` (SWE-bench_Verified) [Partial] NL: "Fix Django i18n locale matching so locales containing both script and region, such as en-latn-us and en-Latn-US, work in i18n_patterns." → `TASK FixLocaleScriptRegion {
  ACTION modify_file(path="django/utils/translation/trans_real.py", change="accept RFC 5646 language tags with language, optional script, and optional region")
  LET locales = ["en-us", "en-latn-us", "en-Latn-US"]
  FOR EACH locale IN locales {
    ACTION request_url(path=locale) -> status
    ACTION verify(actual=status, expected=200)
  }
}` — Iteration represents the test cases, but the necessary implementation patch and exact locale-recognition semantics are prose payloads.
  - `c5957` (PRISM) [Partial] NL: "Please provide a recipe for high protein flatbread." → `TASK ProvideFlatbreadRecipe {
  ACTION respond(intent="provide recipe", dish="high protein flatbread")
}` — The response speech act and requested dish are captured; recipe substance is correctly opaque. The supplied trajectory's later requests to revise by reviews and estimate protein/time cannot be represented as a linked multi-turn revision.
  - `c436` (PRISM) [Partial] NL: "What places to visit in Bilbao" → `TASK RecommendBilbaoPlaces {
  ACTION respond(intent="recommend places", location="Bilbao")
}` — The recommendation intent and destination are represented; the recommendations themselves remain prose. Later questions about opening days, rain, and nearby towns have no conversation-state linkage.
  - `c996` (PRISM) [Partial] NL: "What is your take on love?" → `TASK DiscussLove {
  ACTION respond(intent="give perspective", topic="love")
}` — The requested opinion is captured while its prose substance remains opaque. The later question about whether the assistant can fall in love is not sequenced as a follow-up.
  - `c4939` (PRISM) [Partial] NL: "Is marriage important?" → `TASK DiscussMarriage {
  ACTION respond(intent="give balanced perspective", topic="importance of marriage")
}` — The speech act and topic are retained; the later historical follow-up is not expressible as a conversational continuation.
  - `wildchat1m_en3u-129421` (PATHs) [Partial] NL: "Act as a collective persona named Mark and explain in depth, in an eloquent simple casual American style with concrete examples, how linear algebra converts text to representations used by ChatGPT-4 and converts them back into answers." → `TASK ExplainLLMLinearAlgebra {
  ACTION respond(intent="explain", topic="linear algebra in text encoding and generation for ChatGPT-4", persona="collective persona Mark: psycholinguist, linear algebra professor, logical-reasoning professor, and LLM expert", depth="in depth", register="eloquent simple casual conversational American", include_examples=TRUE, example_kind="concrete numerical examples")
}` — The persona, instructional intent, depth, register, and example constraint are captured. The detailed explanation is appropriate opaque prose, but repeated requests to continue with greater depth lack a revision/follow-up construct.
  - `wildchat1m_en3u-148973` (PATHs) [Partial] NL: "Write a hilarious 17+ comedy script where the Scooby gang and Scrappy-Doo roast a badly translated Jeopardy scenario involving Velma, Shaggy, Alex Trebek, and an attacking robot." → `TASK WriteScoobyComedy {
  ACTION respond(intent="write script", genre="comedy", rating="17+", characters=["Scooby gang", "Scrappy-Doo"], setting="behind the scenes meeting", tone="hilarious", premise="characters roast badly translated Jeopardy scenario involving Velma, Shaggy, Alex Trebek, and an attacking robot", include="silly mocking quotes")
}` — The generation intent, format, characters, tone, age constraint, premise, and requested device are captured; the script remains opaque prose. Subsequent handed-over translations and setting corrections are unmodeled conversation revisions.
  - `wildchat1m_en3u-142592` (PATHs) [Partial] NL: "Please write steps for homiletics and engaging Christian sermons." → `TASK WriteHomileticsSteps {
  ACTION respond(intent="write instructional steps", topic="homiletics and engaging Christian sermons", audience="sermon writer")
}` — The requested instructional form and subject are captured. The later request to expand each step, add details, and give examples requires a revision operation not supplied by the basis.
  - `wildchat1m_en3u-22638` (PATHs) [Partial] NL: "Write an email introducing yourself and job position to another party and asking for collaboration." → `TASK WriteCollaborationEmail {
  ACTION respond(intent="write email", recipient="other party", purpose="introduce sender and job position; request collaboration", register="professional")
}` — The requested message type, recipient, purpose, and implied professional register are captured; email wording is opaque prose. The trajectory's request for a recipient response is not linked to this message.
  - `1775955172098` (ThoughtTrace) [Partial] NL: "I need help planning a trip to Italy." → `TASK PlanItalyTrip {
  ACTION respond(intent="help plan trip", destination="Italy")
}` — The basic planning intent and destination are represented. The later constraints of one week, architecture focus, Chilean origin, and a 1,000,000 CLP budget cannot be formally attached as successive refinements.
  - `1775612391896` (ThoughtTrace) [Partial] NL: "Hey, I need to come up with a final project for my web dev class. It has to be a CRUD app using React and Node.js, but I'm stuck for ideas. Any suggestions" → `TASK SuggestWebDevProject {
  ACTION respond(intent="suggest project ideas", domain="web development class", requirements=["CRUD app", "React", "Node.js"], user_state="stuck for ideas")
}` — The advice-seeking act, technical constraints, and user need are captured. Later selection of the Job Hunt Tracker and the modal-versus-page design decision are unrepresented follow-up state.
  - `1775448065619` (ThoughtTrace) [Partial] NL: "I want to start a healthy diet. Can you help me plan a simple meal prep for 3 days that includes breakfast, lunch, and dinner? I prefer high-protein options." → `TASK PlanMealPrep {
  ACTION respond(intent="plan meal prep", duration_days=3, meals=["breakfast", "lunch", "dinner"], diet="healthy", preference="high-protein", complexity="simple")
}` — Duration, meal categories, health goal, protein preference, and simplicity constraint are captured. The prose plan is opaque, and the later time-saving refinement is not represented.
  - `1775760283577` (ThoughtTrace) [Partial] NL: "Hi there, I am curious to learn a little about end-stage heart failure. Talk to me like you would a 5-year-old." → `TASK ExplainHeartFailure {
  ACTION respond(intent="explain", topic="end-stage heart failure", audience_age=5, register="simple gentle")
}` — The educational intent, topic, young audience, and accessible tone are captured. The later prognosis question and compassionate acknowledgement are not modeled as turns in a conversation.
- **Cross-check:** used=True, agreement=partial — Independent translations generally agree that Actions and Tasks can encode the basic closed tasks, and both providers use IF/binding for the email item and loops for the pillow item. They diverge sharply on decomposition level, action and attribute names, whether every request needs a TASK wrapper, and whether open prompts should be opaque payloads or decomposed plans; one independent sermon translation uses invalid bare-variable syntax (`IF research_notes`) that the stated Check grammar does not permit.
- **Required changes:**
  - `basis`: Resolve scope and namespace rules: either use separate task and variable namespaces or define one consistent lexical-scope model. Remove the contradiction between Task's document-global shared namespace and Bind's permitted nested bindings; specify visibility of action-result bindings across IF and loop scopes.
  - `Task`: Define parameter binding and task-call results completely: specify how positional Task parameters receive named arguments, whether omitted/unknown/duplicate arguments are errors, what value a Task call returns, and what `task_call -> IDENT` binds. Alternatively remove task-call result syntax until return semantics exist.
  - `Check`: Make truthiness usable or remove it: add `value` as a valid boolean primary with precise list/identifier/null behavior, or state that every Check must be an explicit comparison. Define comparison legality and outcomes for strings, lists, booleans, numbers, and mismatched operand types.
  - `Task`: Define recursion guards mechanically rather than using 'could plausibly become false.' Specify whether guards are checked syntactically, how recursive calls inside IF/FOR bodies are recognized, and whether cyclic calls with a syntactic guard are accepted without semantic proof.
  - `Action`: Add a compact canonicalization policy for action and attribute identifiers (at minimum lower_snake_case and a core set for recipient, content, target, format, tone, deadline, audience, and quantity), while retaining extension attributes. This reduces equivalent `to`/`recipient`, `find`/`search_product`, and `respond`/`answer` translations.
  - `basis`: Add a conversation construct or explicitly scoped message-turn/revision mechanism, with sender/recipient, references to prior responses, and ordered follow-up/correction semantics, so sampled multi-turn planning and revision requests are not flattened into unrelated Actions.
  - `basis`: Clarify the syntax of nested TASK declarations and whether they are declarations evaluated at runtime or document-level declarations. If tasks are document-level only, remove `task` from `step`; if local tasks are intended, define their namespace, capture rules, and declaration-time behavior.
  - `Bind`: Correct Bind's semantic claim that LET can name an Action result, since its grammar allows only value or task_call. Keep Action `->` as the Action-result mechanism, or extend LET grammar with an Action expression and define its effect order.
- **Logic issues:** Task says task names and Bind names occupy one flat document-global namespace, but Bind says nested scopes may introduce names; these rules directly conflict.; Task parameters have no semantics: there is no rule mapping task_call named arguments to a Task's parameter identifiers.; Task-call return values are undefined even though task_call may have `-> IDENT`, and Bind permits `LET x = task_call`.; Check defines truthiness for bound values but its grammar does not permit a bare bound value as a Check. Thus `IF replied THEN` is invalid despite the stated truthiness rationale.; Comparison semantics are incomplete for lists, booleans, strings under ordering operators, and mixed types.; The recursion condition 'could plausibly become false' is not a determinate static rule and therefore cannot be implemented or independently translated consistently.; The grammar permits TASK declarations as steps, but the semantics call Task a document-global declaration and do not define execution, visibility, or captures for nested Task declarations.; Bind claims LET can bind an Action result, but Bind grammar does not contain an Action production.; A task call's `-> IDENT` and an Action's `-> IDENT` both bind names under the global namespace, but collision behavior across Task invocations and repeated loop iterations is not defined.; The proposal promises a flat style disallowing deep nesting, while Flow-If explicitly permits arbitrary nesting and Task grammar permits nested task declarations.
- **Decision:** needs-rework
- **Documenter summary:** The Shaper proposed a 6-construct basis (Task, Action, Check, Flow-If, Iterate, Bind) drawing on Python's flat statement style, HTML's content/attribute separation, English's closed-class logic words, formal-language context-free parsing, and Parsel/ReAct-style decomposition, but the Critic ruled needs-rework. The decisive issue was internal contradiction rather than a KPI failure: Task declares one flat document-global namespace shared with Bind while Bind's own rules permit nested scoping, and Check's stated truthiness semantics can't actually be used because the grammar disallows bare bound values as conditions (making the simulated `IF replied == FALSE` example valid but an equivalent bare-value form invalid) — alongside undefined task-call parameter/return semantics and a non-mechanical recursion-guard rule. Simulations on sampled items showed full coverage for closed embodied/email/shopping tasks but only partial coverage for SWE-bench code edits and multi-turn conversational items, reinforcing that the basis's core shape is promising but not yet implementable as specified.
- **Cost this sprint:** $0.7759

## Sprint 0 (bootstrap, attempt 2/3) — 2026-09-23

- **Language version:** 0.1.0 → 0.1.0 (MAJOR — establishes the base syntax)
- **Inspiration languages:** Python's function-call and block scoping shaped the unified call-by-value, no-shadowing lexical-scope model for Task/Flow-If/Iterate/Bind; HTML's content/attribute separation shaped Action's canonical core attribute vocabulary; English's closed-class connectives shaped Check's precedence rules, and its discourse-level turn-taking shaped the new Conversation construct.
- **Shaper proposal (model: anthropic/claude-sonnet-5):** This revision unifies Task, Flow-If, Iterate, and Bind under one consistent lexical-scope model, completes Task's parameter/return/recursion-guard semantics and Check's truthiness/typed-comparison rules, adds an attribute-canonicalization policy to Action, and introduces a Conversation construct for multi-turn requests and revisions.
- **Changes:** `Task` (revise, MAJOR), `Action` (revise, MAJOR), `Check` (revise, MAJOR), `Flow-If` (revise, MAJOR), `Iterate` (revise, MAJOR), `Bind` (revise, MAJOR), `Conversation` (add, MAJOR)
- **Critic decision:** needs-rework — This is a promising bootstrap because it supplies a real compositional core, explicit scope and evaluation rules, and useful structures for both closed tasks and multi-turn requests. It cannot be accepted because its central Conversation representation contradicts Action's effect semantics, while its promised static typing for Check and iterable semantics cannot operate without result and parameter types. Fixing those foundational contradictions and defining revision resolution would turn the basis into a substantially stronger and more deterministic initial language.
- **Doc hygiene:** pass — All changes carry a complete glossary entry (gloss + worked example).
- **Pre-KPI assessment:**
  - coverage: benefit — The proposed basis covers the actionable cores of the closed embodied, web-navigation, and code-change samples through ordered Actions, data binding, branching, and iteration. It also gives open conversational items a way to retain turn order and corrections through CONVO, although several operational domains still depend entirely on unconstrained action and attribute names.
  - expressivity: mixed — The basis preserves ordering, quantities, recipients, tone, named arguments, conditions, and many conversational links. However, Action is defined as necessarily effectful while CONVO uses Actions such as ask/respond to represent utterances, making conversational records semantically incorrect; revision precedence is also underdefined, and action-result/list types required by Check and Iterate cannot reliably be expressed or checked.
  - determinism: mixed — Lower_snake_case, core attribute names, named task arguments, fixed Check precedence, and explicit lexical scope should improve convergence. But translators still have unrestricted choices among open action types and arbitrary non-core attributes, cannot know the types or result shapes of Action outputs, and may disagree whether a conversational utterance is an effectful Action, a request, or opaque content.
  - interpretability: mixed — The scoping, call, truthiness, comparison, and short-circuit rules are substantially clearer than an underspecified bootstrap basis. Yet a reader cannot determine what an arbitrary Action does, whether an arbitrary action result is a list/number/string/bool, or what precisely survives after multiple REVISES links; the claimed uniform execution model conflicts with using Actions as non-effectful dialogue records.
  - improvement: benefit — For closed tasks, explicit sequencing, named constraints, Bind sites, IF, and FOR EACH give a weaker agent a useful execution plan rather than a prose instruction. For open tasks, the structure identifies recipient, tone, word count, turn sequence, and revision relationships, but the Conversation semantic contradiction limits the benefit for multi-turn agent behavior.
- **Simulated examples:**
  - `dev-embodied-2` (seed_tasks) [Full] NL: "Put both pillows from the sofa onto the armchair, one at a time." → `TASK MoveSofaPillows {
  FOR EACH pillow IN ["sofa_pillow_1", "sofa_pillow_2"] {
    ACTION pick_up(target=pillow)
    ACTION place(target=pillow, recipient="armchair")
  }
}` — Iterate directly represents the one-at-a-time requirement; Action supplies the ordered physical operations.
  - `dev-embodied-1` (seed_tasks) [Full] NL: "Rinse the mug in the sink, then put it in the coffee maker." → `TASK RinseAndPlaceMug {
  ACTION rinse(target="mug", recipient="sink")
  ACTION place(target="mug", recipient="coffee_maker")
}` — Sequential Action order captures the required temporal order.
  - `86afd67c-1bff-455c-baa7-e18dcb64b0f3` (Mind2Web) [Full] NL: "Find comedy tv shows on netflix sorted by audience score." → `TASK FindComedyShows {
  ACTION open(target="netflix")
  ACTION select_filter(target="tv_shows")
  ACTION select_filter(target="comedy")
  ACTION apply_filters()
  ACTION sort(target="audience_score", format="descending")
}` — The action sequence captures the actionable web-navigation core. Canonical target and format help, but select_filter and sort remain open action vocabulary.
  - `bf469f30-6628-4017-b963-672645d7feab` (Mind2Web) [Full] NL: "Find the highest rated dog collar under 10 dollar." → `TASK FindDogCollar {
  ACTION open(target="pet_store")
  ACTION select_filter(target="dog")
  ACTION select_filter(target="collars_and_leashes")
  ACTION select_filter(target="price_under_10_usd")
  ACTION sort(target="rating", format="descending")
}` — The category, price ceiling, and highest-rated ordering are represented, though the language has no standardized filter or sort vocabulary.
  - `trial_T20190907_223758_523581#1` (ALFRED) [Full] NL: "Microwave a slice of apple and place it on the table." → `TASK HeatAppleAndPlace {
  ACTION slice(target="apple") -> apple_slice
  ACTION heat(target=apple_slice, recipient="microwave")
  ACTION place(target=apple_slice, recipient="table")
}` — Action sequencing and the bound apple_slice preserve the heat-then-place dependency.
  - `trial_T20190908_224836_919680#2` (ALFRED) [Full] NL: "Put a microwaved slice of apple on the table in the corner." → `TASK PlaceMicrowavedApple {
  ACTION slice(target="apple") -> apple_slice
  ACTION heat(target=apple_slice, recipient="microwave")
  ACTION place(target=apple_slice, recipient="table_in_corner")
}` — The adjective microwaved is represented as a preceding heat action and the corner-table destination is retained.
  - `scikit-learn__scikit-learn-11578` (SWE-bench_Verified) [Partial] NL: "Fix _log_reg_scoring_path so the LogisticRegression instance used by probabilistic scoring inherits multi_class, rather than defaulting to OvR for multinomial LogisticRegressionCV." → `TASK FixLogisticRegressionScoring {
  ACTION modify_code(target="sklearn/linear_model/logistic.py", content="In _log_reg_scoring_path, construct LogisticRegression with multi_class=multi_class so probabilistic scorer predictions use the requested multinomial behavior rather than the default OvR behavior.")
  ACTION run_tests(target="logistic_regression_probabilistic_scoring")
}` — The code-change intent, target, rationale, and validation step are structured, but the implementation and test substance remain an opaque content payload, which is appropriate for this open technical request.
  - `django__django-13112` (SWE-bench_Verified) [Partial] NL: "Fix makemigrations crashing for a ForeignKey when the installed Django app name has mixed case." → `TASK FixMixedCaseAppReference {
  ACTION modify_code(target="django/db/models/fields/related.py", content="Preserve or resolve the installed app label consistently when validating lazy ForeignKey references, so a mixed-case installed app name does not fail against a lower-cased reference.")
  ACTION run_tests(target="mixed_case_foreign_key_app_reference")
}` — The requested defect, affected module, and validation intent are represented; the required source-level semantic change remains prose payload.
  - `c6516` (PRISM) [Partial] NL: "Can you give me some great places to visit in the Netherlands? What kind of artwork is in the Van Gogh Museum? What foods should I try and can you recommend a restaurant?" → `CONVO NetherlandsTrip {
  TURN t1 SPEAKER=USER {
    ACTION ask(content="Recommend great places to visit in the Netherlands.")
  }
  TURN t2 SPEAKER=USER REPLY_TO t1 {
    ACTION ask(content="Describe the artwork in the Van Gogh Museum.")
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    ACTION ask(content="Recommend Dutch foods to try and a good restaurant.")
  }
}` — Conversation preserves multiple requests and their order. The substantive recommendations correctly remain opaque, but ask is semantically declared an effectful Action, exposing the Conversation/Action conflict.
  - `c3388` (PRISM) [Partial] NL: "Hi, how has your day been? Good, aren't you going to ask how my day has been? No problem, my day has been boring and painful for nearly three years; tell me a joke to distract me." → `CONVO PainAndJoke {
  TURN t1 SPEAKER=USER {
    ACTION ask(content="How has your day been?")
  }
  TURN t2 SPEAKER=USER REPLY_TO t1 {
    ACTION correct(content="Ask how my day has been.")
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    ACTION ask(content="Tell me a joke to distract me from long-term pain.")
  }
}` — Turn order and correction are represented, but no construct captures conversational affect, duty to acknowledge the correction, or the safety-relevant pain context except opaque content.
  - `c2067` (PRISM) [Partial] NL: "Briefly explain American politics. Why is the Supreme Court part of government? Are justices voted on by people? If appointed by the president, how is that fair?" → `CONVO AmericanPolitics {
  TURN t1 SPEAKER=USER {
    ACTION ask(content="Briefly explain American politics.")
  }
  TURN t2 SPEAKER=USER REPLY_TO t1 {
    ACTION ask(content="Why is the Supreme Court part of government?")
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    ACTION ask(content="Are Supreme Court justices elected by the public?")
  }
  TURN t4 SPEAKER=USER REPLY_TO t3 {
    ACTION ask(content="If the president appoints them, explain how that is fair.")
  }
}` — CONVO captures the dependent explanatory sequence. The requested political explanations are legitimate opaque prose payload.
  - `c2904` (PRISM) [Partial] NL: "Tell me what is happening politically in New Zealand. Are you up to date with current events? Are you aware of current political events in Aotearoa for 2023?" → `CONVO CurrentAotearoaPolitics {
  TURN t1 SPEAKER=USER {
    ACTION ask(content="Explain current political developments in New Zealand.")
  }
  TURN t2 SPEAKER=USER REPLY_TO t1 {
    ACTION ask(content="State whether your information is up to date.")
  }
  TURN t3 SPEAKER=USER REVISES t1 {
    ACTION ask(content="Explain current political events in Aotearoa for 2023 using current information.")
  }
}` — The correction and freshness constraint are retained. Revision precedence is ambiguous if later turns refer to both the original and its revision.
  - `wildchat1m_en3u-73283` (PATHs) [Partial] NL: "Introduce the topic of the impact of dam construction on seasonal precipitation patterns, land use/cover, and socio-economic conditions in semi-arid Eastern Sudan." → `TASK IntroduceDamImpactTopic {
  ACTION write(content="Introduce the impact of dam construction on seasonal precipitation patterns, land use/cover, and socio-economic conditions in semi-arid Eastern Sudan.", format="technical_introduction", tone="academic")
}` — Intent, topic, register, and requested output form are represented; the introduction's substantive argument remains an appropriate content payload.
  - `wildchat1m_en3u-76731` (PATHs) [Partial] NL: "Try to identify Holy Blood and Holy Grail-like conspiracy ideas in The Brothers Karamazov." → `TASK CompareLiteraryConspiracyThemes {
  ACTION analyze(content="Identify and qualify possible parallels between The Brothers Karamazov and the conspiracy themes of The Holy Blood and the Holy Grail.", target="The Brothers Karamazov", format="literary_analysis")
}` — The comparative-analysis intent, source text, and requested framing are represented; the literary reasoning is prose substance.
  - `wildchat1m_en3u-137561` (PATHs) [Partial] NL: "Write a story of when Gloopy and Glitter met the scientist, who is amazed they can speak." → `CONVO GloopiterStoryRevision {
  TURN t1 SPEAKER=USER {
    ACTION ask(content="Write a story in the established Gloopiter setting about Gloopy and Glitter meeting a human scientist who is amazed that they can speak.", format="story")
  }
  TURN t2 SPEAKER=USER REVISES t1 {
    ACTION ask(content="Retain the established Gloopy, Glitter, Gloopiter, and scientist context; focus the story on their first meeting and the scientist's amazement at speech.", format="story")
  }
}` — The final request depends on extensive previous fictional context, which can only be carried in opaque content. The REVISES relation does not formally merge that context, so the exact inherited story state is not recoverable from the expression alone.
  - `wildchat1m_en3u-78000` (PATHs) [Partial] NL: "Write a legal document and contract from me as a high-demand speaker to clients, emphasizing limited availability, and add a binding signature line." → `CONVO SpeakerContractRevision {
  TURN t1 SPEAKER=USER {
    ACTION ask(content="Write a legal speaking-engagement contract from the speaker to clients, emphasizing that the speaker is in high demand and has limited time.", format="legal_contract", tone="professional")
  }
  TURN t2 SPEAKER=USER REVISES t1 {
    ACTION ask(content="The speaker, not the client, sends the contract.", format="legal_contract")
  }
  TURN t3 SPEAKER=USER REVISES t2 {
    ACTION ask(content="Add a binding client signature and date line.", format="legal_contract")
  }
}` — The author role, audience, formal register, revisions, and signature requirement are structured. Contract clauses and jurisdictional validity remain prose substance.
  - `1776009617894` (ThoughtTrace) [Partial] NL: "Suggest a posting schedule to help the Hamoudi educational YouTube channel grow quickly in its first month." → `CONVO HamoudiChannelPlanning {
  TURN t1 SPEAKER=USER {
    ACTION ask(content="Suggest a posting schedule for the first month of the Hamoudi educational YouTube channel.", target="Hamoudi", deadline="first_month", tone="practical")
  }
}` — The channel, objective, and first-month horizon are retained. The prior context that Hamoudi targets preschool children is not formally available unless repeated in content, because turns and Tasks share no data.
  - `1775429344935` (ThoughtTrace) [Full] NL: "Help me create a text about my decision to go to Japan to learn about SGI. Only 100 words." → `TASK WriteJapanSGIText {
  ACTION write(content="Explain my decision to travel to Japan to learn about SGI.", format="personal_reflection", quantity=100)
}` — The requested content type, subject, destination, purpose, and exact word quantity are represented. The prose itself is correctly payload.
  - `1775752130482` (ThoughtTrace) [Full] NL: "Hello, I want to plan a 3 day safari in Eastern Cape, South Africa." → `TASK PlanEasternCapeSafari {
  ACTION plan_trip(target="Eastern Cape, South Africa", content="safari itinerary", quantity=3, format="day_by_day_itinerary")
}` — Destination, activity, duration, and desired itinerary form are represented, although plan_trip is an unconstrained domain action.
  - `1775479438859` (ThoughtTrace) [Partial] NL: "Give examples in a UK context of short certifications that can open stable employment fields and support later mortgage eligibility." → `CONVO UKCertificationMortgage {
  TURN t1 SPEAKER=USER {
    ACTION ask(content="Give examples of short UK certifications that lead to stable employment fields and can support later mortgage eligibility.", target="United Kingdom", format="actionable_examples")
  }
}` — The UK scope, certification topic, employment-stability constraint, and mortgage purpose are retained. The career and lending recommendations remain appropriate opaque informational content.
- **Cross-check:** used=False, agreement=n/a — No independent translations were supplied. Self-assessment predicts moderate agreement on closed sequential tasks, but low-to-partial agreement on open items because action verbs, open attribute names, and the representation of utterances as Actions are not canonicalized.
- **Required changes:**
  - `Action`: Split effectful system/world operations from non-effectful communicative records. Either add a pure utterance/request construct usable in TURN bodies (with intent, content, recipient/audience, tone, and format) or explicitly define a separate non-effectful Action category; do not state that every Action always performs a side effect while using Actions for ask/respond/correct.
  - `Conversation`: Define revision resolution algorithmically: specify whether REVISES replaces the whole target turn, selected request fields, or only an utterance payload; define chains, multiple revisions to one turn, revisions of replies, and how a later REPLY_TO resolves when its target has been revised.
  - `basis`: Add a typed value/result contract. Define declared types for parameters and LET bindings, the result type of every Action/task call, permitted iterable types, and how a translator declares an open Action's return type. Make static comparison checking and FOR EACH validity depend on those declarations rather than unavailable runtime knowledge.
  - `Iterate`: Define quantifier-variable binding explicitly under the no-shadowing rule: state its scope, whether it may conflict with an outer visible name, and whether it is a lexical binding for static name resolution. Also require iterable values to be LIST (or define supported collection types).
  - `Task`: Define an executable document entry point and top-level execution behavior: whether all top-level TASK/CONVO declarations are merely declarations, which Task is invoked, and whether CONVO declarations execute or are records. This is required because document grammar permits multiple declarations with no invocation root.
  - `Action`: Add a small normative operation vocabulary or domain profiles for common closed-task operations such as open/click/select/filter/sort, pick_up/place/heat/rinse, and modify_code/run_tests, including canonical attribute roles for source, destination, ordering, threshold, and validation. Keep extension actions, but define when the normative forms must be used.
  - `Task`: Replace or constrain the lexical recursion guard. A call lexically inside IF TRUE or an unbounded FOR EACH is currently permitted despite guaranteed nontermination; at minimum define runtime behavior/resource limits for nonterminating calls and make the guard require a declared decreasing bound or finite iteration source.
  - `basis`: Define identifier and literal boundaries completely: whether Unicode is permitted in STRING, whether NUMBER permits signs/exponents, whether list literals may be heterogeneous, and the exact tokenization rule for comments and escaped newlines. These details are needed for an initial deterministic syntax.
- **Logic issues:** Conversation examples use ACTION ask/respond/correct as records of speech, but Action semantics say every invocation always performs one real-world or system side effect. This is a direct cross-construct semantic contradiction.; Check requires statically type-matched operands, but Action results and Task parameters have no type declarations. A bound result such as stock or itinerary therefore cannot be statically known to be NUMBER or LIST.; FOR EACH accepts any IDENT as an iterable although the language has no static or dynamic rule requiring that identifier to denote a list. Quantifier loop-variable scope is also not reconciled explicitly with the global no-shadowing prohibition.; REVISES says later turns should be interpreted against the latest revision in a chain but does not define what gets replaced, how distinct revision branches are ordered, or how references to revised turns resolve.; The document permits one or more TASK/CONVO declarations but supplies no entry point or rule for executing declarations. As written, a valid document has no defined program invocation.; The syntactic recursion guard permits recursion under an IF whose Check is always true and under an unbounded runtime collection. It is mechanical, but it does not give defined handling for predictable divergence.; The Task worked example says it re-checks stock after reorder and makes the checked level available, but RETURN stock returns the pre-reorder value because the recursive call result is discarded.; The supplied sample list contains 19 items, although the prompt labels it as 20; all 19 supplied items are simulated.
- **Decision:** needs-rework
- **Documenter summary:** The Shaper proposed a 7-construct basis (Task, Action, Check, Flow-If, Iterate, Bind, Conversation) drawing chiefly on Python's flat orthogonal structure, HTML's content/attribute separation, and formal-language context-free parseability, with Parsel and ReAct cited as precedents. The Critic returned a needs-rework verdict: while simulations showed full or partial coverage across embodied, web-navigation, code-fix, and multi-turn dialogue samples, it flagged a core logic contradiction—Conversation's worked examples use ACTION ask/respond/correct as non-effectful speech records even though Action semantics mandate every invocation always performs a real-world side effect—alongside missing type declarations for Check/Iterate and undefined REVISES resolution semantics. No basis was ratified this attempt; required changes include splitting effectful from communicative Actions, adding a typed value/result contract, and defining revision-chain resolution and a document entry point.
- **Cost this sprint:** $0.6997

## Sprint 0 (bootstrap, attempt 3/3) — 2026-09-23

- **Language version:** 0.1.0 → 1.0.0 (MAJOR — establishes the base syntax)
- **Inspiration languages:** Python's flat, orthogonal statements and closed control keywords shape Task/Iterate/Bind's block structure and named-parameter calls; HTML's content/attribute separation shapes Action's typed key=value attributes and its normative per-domain vocabulary; English's closed-class function words and discourse turn-taking shape Check's operator set and Conversation's TURN/REPLY_TO/REVISES model.
- **Shaper proposal (model: anthropic/claude-sonnet-5):** Revises the bootstrap basis to add a mandatory shared type system, split effectful Action from a new pure Utterance construct, define an algorithmic REVISES resolution rule, require a single document ENTRYPOINT, replace the unenforceable recursion guard with a type-grounded DECREASES pattern, and complete the normative Action vocabulary and lexical rules the Critic required.
- **Changes:** `Types & Lexicon` (add, MAJOR), `Task` (revise, MAJOR), `Action` (revise, MAJOR), `Utterance` (add, MAJOR), `Check` (revise, MINOR), `Flow-If` (revise, MINOR), `Iterate` (revise, MAJOR), `Bind` (revise, MAJOR), `Conversation` (revise, MAJOR)
- **Critic decision:** needs-rework — [Forced acceptance after 3 attempt(s) without a clean accept — the required changes below are known issues carried forward for a future sprint to address, not resolved.] The proposal has a promising structured core: typed bindings, explicit control flow, lexical scopes, and the Action/UTTER split are meaningful improvements over an empty basis. It cannot be accepted in Sprint 0 because its stated recursion guarantee is unsound, its document examples contradict its own grammar, and fundamental input, observation, and conversational-execution semantics remain undefined. These are repairable design issues rather than a fundamentally wrong direction, so rework is warranted.
- **Doc hygiene:** pass — All changes carry a complete glossary entry (gloss + worked example).
- **Pre-KPI assessment:**
  - coverage: mixed — The Action vocabulary, typed lists, loops, branches, and code/household/web profiles cover many closed tasks, and the simulations can represent most action cores. However, an ENTRYPOINT TASK is forbidden from taking parameters and there is no input-binding construct, so a task explicitly given an arbitrary list (dev-code-1) has no valid way to receive it. Open extension verbs also provide broad nominal coverage but weaken the claim that a closed actionable core is formally represented rather than renamed.
  - expressivity: mixed — UTTER, TURN, audience/tone/format attributes, and REVISES materially improve representation of open requests and conversational corrections. But the conversation model cannot carry values between turns, and its revision semantics are unclear about whether superseded turns and their effects have already executed; whole-body replacement can also erase prior constraints without a way to distinguish correction from addition. The missing external-input mechanism loses an explicit part of parameterized closed requests.
  - determinism: harm — Independent translations agree on basic CONVO/UTTER shape for several open prompts and on the delete loop's broad structure, but they diverge sharply on whether requests are TASKs, CONVOs, effectful Actions, or speech acts, and on unconstrained extension verb names such as get_file_age_days versus check_file_age. The proposed canonical vocabulary does not resolve this because many common operations, including draft_email, change_store, fetch_article, and plan_schedule, remain open extensions.
  - interpretability: mixed — The lexical rules, fixed Check precedence, explicit scopes, and explicit ENTRYPOINT improve recoverability. Nevertheless, the basis contains contradictions and invalid worked examples: standalone Actions, LETs, Checks, and CONVO examples omit the mandatory document ENTRYPOINT; Action is said to be always effectful while query-like check_inventory and check_reply_status are Actions; and recursion is claimed provably terminating when its permitted != guard is not terminating. These defects prevent a reader from reliably determining what programs mean.
  - improvement: mixed — Explicit sequencing, data bindings, typed checks, and loop scopes can help a weaker model execute structured household, web, and coding tasks. The inability to receive task inputs, ambiguity over read-only observations versus effects, and unclear revision execution semantics would make planning worse for important cases, while large opaque content strings offer little decomposition benefit beyond preserving the raw prompt.
- **Simulated examples:**
  - `dev-code-1` (seed_tasks) [Fail] NL: "Given a list of file paths, delete every file older than 30 days unless it's in the 'archive' folder." → `ENTRYPOINT DeleteOldFiles
TASK DeleteOldFiles {
  ACTION get_file_paths() -> paths : LIST[STRING]
  FOR EACH path IN paths {
    ACTION check_file_age(target=path) -> age_days : NUMBER
    ACTION check_file_location(target=path) -> in_archive : BOOL
    IF age_days > 30 AND NOT in_archive THEN {
      ACTION delete_file(target=path)
    }
  }
}` — Iterate and typed Check help, but the request supplies a list as an input whereas a valid ENTRYPOINT TASK must have zero parameters. get_file_paths invents a retrieval action and does not formally bind the supplied list; an external-input Bind is missing.
  - `dev-email-1` (seed_tasks) [Full] NL: "Draft a reply to my professor asking for a two-day extension on the assignment, and keep it formal." → `ENTRYPOINT DraftExtension
TASK DraftExtension {
  ACTION draft_email(recipient="professor", content="Request a two-day extension on the assignment.", tone="formal", format="reply")
}` — Action attributes preserve recipient, requested quantity, register, and reply format. The open extension verb draft_email is required because the communication profile only standardizes send_email, send_message, and call.
  - `b7082615-e6e1-4981-b51b-9259671d1adf` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Change your store to the one nearest to 07055" → `ENTRYPOINT ChangeStore
TASK ChangeStore {
  ACTION open(target="store selector")
  ACTION search(target="store", content="07055")
  ACTION select_filter(target="nearest store to 07055")
}` — The web vocabulary helps with open/search/select sequencing, although select_filter is semantically awkward for choosing a store rather than filtering results.
  - `e2adf8f1-547d-4671-96c1-4a21a56e135d` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "View the upcoming schedule from Otis St@Summer St to City Point of the transit near South Station for today." → `ENTRYPOINT ViewSchedule
TASK ViewSchedule {
  ACTION open(target="Schedules")
  ACTION search(target="transit near South Station")
  ACTION search(source="Otis St@Summer St", destination="City Point", target="upcoming schedule", deadline="today")
}` — The source, destination, target, and deadline roles preserve the actionable core; the proposal's WEB search profile helps.
  - `trial_T20190908_120422_949453#2` (ALFRED (json_2.1.0, train)) [Full] NL: "Move a red rag into a sink." → `ENTRYPOINT MoveRag
TASK MoveRag {
  ACTION pick_up(target="red rag")
  ACTION place(target="red rag", destination="sink")
}` — The household canonical verbs and ordering express the requested final-state task.
  - `trial_T20190906_165121_524545#3` (ALFRED (json_2.1.0, train)) [Full] NL: "Put a box with keys in it on a chair." → `ENTRYPOINT PlaceBox
TASK PlaceBox {
  ACTION pick_up(target="keys")
  ACTION place(target="keys", destination="box")
  ACTION pick_up(target="box")
  ACTION place(target="box", destination="chair")
}` — The decomposition preserves the containment prerequisite and final placement. Action sequencing is helpful.
  - `sphinx-doc__sphinx-7757` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "The default value for positional only argument has vanished" → `ENTRYPOINT FixPositionalOnlyDefault
TASK FixPositionalOnlyDefault {
  ACTION modify_code(target="sphinx/util/inspect.py", content="Fix rendering of '.. py:function:: foo(a, b=0, /, c=1)' so positional-only parameter b retains its default value 0 in the rendered signature.")
}` — The code action captures the requested target and expected behavior, with the detailed reproduction represented as a STRING content value.
  - `django__django-15268` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "Optimize multiple AlterFooTogether operations into one" → `ENTRYPOINT OptimizeAlterTogether
TASK OptimizeAlterTogether {
  ACTION modify_code(target="django/db/migrations/operations/models.py", content="Coalesce consecutive AlterUniqueTogether and AlterIndexTogether operations for the same model, removing redundant empty-state operations and retaining the final unique_together and index_together states.")
}` — The code-action profile helps, though the substantive transformation remains an opaque content payload.
  - `c7033` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "What is an objectively stronger video game, Marvel's Spider-Man 2 or Baldur's Gate 3?" → `ENTRYPOINT GameComparison
CONVO GameComparison {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="What is an objectively stronger video game, Marvel's Spider-Man 2 or Baldur's Gate 3?", target="comparative evaluation")
  }
}` — UTTER captures the speech act and target; the comparison's substantive evaluative criteria correctly remain prose. The later insistence to pick one is not represented by the single sampled NL prompt.
  - `c1182` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "how to approach a girl" → `ENTRYPOINT SocialAdvice
CONVO SocialAdvice {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="How to approach a girl.", target="social advice")
  }
}` — Conversation and ask preserve the request's meta-structure; advice substance remains content, as intended for an open item.
  - `c224` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Why does it seem a lot of people are extremely right-wing the last couple of years?" → `ENTRYPOINT PoliticalQuestion
CONVO PoliticalQuestion {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Why does it seem a lot of people are extremely right-wing the last couple of years?", target="political trend explanation")
  }
}` — UTTER captures an explanatory question. Its substantive political argument appropriately remains prose.
  - `c1448` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "What do you think of the outcomes of the elections in the Netherlands from yesterday?" → `ENTRYPOINT NetherlandsElectionQuestion
CONVO NetherlandsElectionQuestion {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="What do you think of the outcomes of the elections in the Netherlands from yesterday?", target="Netherlands election outcomes", deadline="yesterday")
  }
}` — The question and temporal qualifier are retained. The requested analysis remains prose payload.
  - `wildchat1m_en3u-58610` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "Give a Really Shortest Description Backstory about Zack Taylor/Black Ranger (Lucifer, Beelzebub, Pandemonica, Modeus, Judgement, Azazel, Cerbeus, Malina, and Zdrada’s Boyfriend) (Power Rangers x Helltaker Crossover) meeting these characters." → `ENTRYPOINT GenerateBackstory
CONVO GenerateBackstory {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Give a very short Power Rangers x Helltaker crossover backstory in which Zack Taylor meets the Helltaker characters; preserve the supplied character relationships, personalities, and described powers.", format="backstory", quantity="very short", audience="general")
  }
}` — The generation intent, format, length, and audience are formalized. The extensive fictional premise correctly remains an opaque prose payload.
  - `wildchat1m_en3u-149438` (PATHs (microsoft/prototical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-0125-preview)) [Partial] NL: "Write a hilarious script where the Scooby gang and Scrappy-Doo have a funny meeting behind the scenes and react to my badly translated sentences." → `ENTRYPOINT GenerateComedyScript
CONVO GenerateComedyScript {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Write a behind-the-scenes Scooby gang and Scrappy-Doo script reacting only to the supplied badly translated sentence, questioning and roasting its errors and inconsistencies with occasional funny quotes.", format="script", tone="hilarious comedy 17+", audience="reader")
  }
}` — UTTER plus format, tone, audience, and content preserve the open request's meta-structure. The script's prose substance remains payload.
  - `wildchat1m_en3u-113201` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-1106-preview)) [Partial] NL: "Please rewrite this tables of profitable online methods of earning money that can be setup to be almost completely automated with the capabilities of AI. Make it more comprehensive, detailed, and complete. Be sure to replace every <br /> with an actual line break" → `ENTRYPOINT RewriteTable
CONVO RewriteTable {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Rewrite the supplied table of AI-automatable online earning methods. Preserve its table structure, make it more comprehensive, detailed, and complete, and replace every <br /> with an actual line break.", format="table", tone="informative")
  }
}` — The transformation request, required output format, and explicit replacement constraint are retained; table contents remain prose payload.
  - `wildchat1m_en3u-155336` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-0125-preview)) [Partial] NL: "Monetag Review (2024): Is It a Best AdSense Alternative" → `ENTRYPOINT MonetagReview
CONVO MonetagReview {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Write a review titled 'Monetag Review (2024): Is It a Best AdSense Alternative'.", format="review", target="Monetag versus AdSense")
  }
}` — The likely generation intent, title, format, and comparison target are captured, though the terse title alone leaves the intended speech act somewhat underdetermined.
  - `1776020181361` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "My laptop (mac book pro 2017) gets hot and the fan starts to make noise when I am working. What can I do to reduce that" → `ENTRYPOINT LaptopCoolingAdvice
CONVO LaptopCoolingAdvice {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="My 2017 MacBook Pro gets hot and its fan becomes noisy while I work. What can I do to reduce this?", target="reduce laptop heat and fan noise")
  }
}` — The help-seeking speech act, device, symptoms, and goal are preserved. The requested troubleshooting advice remains prose.
  - `1775963744772` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "Hi, I'd like to learn playing the piano. What steps do you recommend for me to take if I want to start this hobby as a complete beginner?" → `ENTRYPOINT PianoBeginnerAdvice
CONVO PianoBeginnerAdvice {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Recommend steps for starting piano as a complete beginner.", target="beginner piano learning plan", audience="complete beginner")
  }
}` — The request's intent, target, and novice audience are captured. The teaching plan is appropriately prose.
  - `1775837106479` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "Hi, I need your help in planning a birthday for my daughter." → `ENTRYPOINT BirthdayPlanningAdvice
CONVO BirthdayPlanningAdvice {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Help plan a birthday for my daughter.", target="daughter's birthday party")
  }
}` — The planning request and beneficiary are preserved. The original prompt has not yet supplied date, budget, age, or guest constraints.
  - `1775973360170` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "planning my weekly daysas l go to school and work" → `ENTRYPOINT WeeklyPlanningAdvice
CONVO WeeklyPlanningAdvice {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Help plan my weekly days while I go to school and work.", target="weekly school and work schedule", tone="friendly")
  }
}` — The planning goal and school/work constraints are captured. A later conversation could add turns with schedule details, but turn-to-turn variables cannot be shared under the current specification.
- **Cross-check:** used=True, agreement=partial — Providers largely agree on CONVO plus USER UTTER for simple open questions and on pick_up/place for the simple household task. They disagree on TASK versus CONVO for request-like prompts, Action versus UTTER for drafting and planning, code targets, and open action names; dev-code-1 uses semantically equivalent but noncanonical check_file_age/get_file_age_days verbs. Several supplied translations are themselves invalid under the proposed basis because they omit ENTRYPOINT or use an ENTRYPOINT TASK with a parameter.
- **Required changes:**
  - `Task`: Add a defined external-input mechanism, such as `INPUT IDENT : type`, legal only in an ENTRYPOINT body, or permit typed ENTRYPOINT parameters with a defined invocation environment. State how supplied values bind before execution.
  - `Task`: Repair the DECREASES proof and rule: replace the permitted `!=` guard with a lower-bound guard that guarantees termination (for example `paramName > NUMBER_LITERAL`), require the recursive call to occur in the guarded THEN branch, and define the required decreasing argument separately for each caller/callee parameter in mutual-recursion cycles.
  - `Action`: Split read-only observation/query operations from effectful Actions, or revise Action semantics so it does not claim every Action has a side effect. Define the result and failure semantics of observations such as check_inventory, check_reply_status, check_file_age, and search.
  - `Conversation`: Define execution status for revised turns: specify whether a revised turn replaces an unexecuted request record only, whether prior turn Actions are prohibited, or how already executed effects are treated. Add an explicit additive-follow-up relation or define when REPLY_TO supplies additional constraints versus when REVISES replaces them.
  - `Conversation`: Add an explicit, typed cross-turn data-passing mechanism or state that CONVO is purely a request transcript and Actions in turns cannot consume prior-turn results. The current statement that only a Task RETURN crosses a Turn/Task boundary has no grammar for such a crossing.
  - `basis`: Make every worked example a valid complete document under `document ::= entrypoint (task | conversation)*`: add ENTRYPOINT and enclosing TASK/CONVO where necessary, including Types & Lexicon, Action, Check, Iterate, Bind, Utterance, and Conversation examples.
  - `Action`: Expand or profile the canonical vocabulary for common requested operations, including drafting, changing a selected store, retrieving a document, planning, and observations; alternatively give a deterministic naming rule for extension verbs and attribute roles.
  - `Types & Lexicon`: Define lexical token separation and punctuation/tokenization fully, including whether a hyphen in `diff` is recognized independently of whitespace and how keywords are delimited. Also define whether empty list literals are legal and, if so, how their element type is supplied.
- **Logic issues:** The claimed recursion termination theorem is false: with `DECREASES tries`, guard `tries != 0`, and recursive argument `tries - 1`, an initial negative value satisfies the guard forever and decreases without reaching zero.; Action is specified as always effectful, but its own examples and simulations require observational operations such as check_inventory, check_reply_status, check_file_age, and search that are naturally pure reads; no distinct read/query construct exists.; The document grammar requires ENTRYPOINT before every declaration, yet multiple worked examples are fragments containing standalone ACTION, LET, Check, FOR EACH, or CONVO without ENTRYPOINT and are not valid documents.; A zero-parameter-only ENTRYPOINT TASK cannot accept a user-provided typed list or any other external input; no INPUT grammar or invocation environment is defined.; Conversation says turns execute in document order, while REVISES retrospectively replaces a prior turn's entire body. It does not define whether actions in the replaced body execute, have executed already, or are cancelled.; Conversation claims that a Task RETURN is the only value that can cross a Turn/Task boundary, but no grammar permits a TURN to invoke a Task with a result binding that can be used by another Turn; turns also have explicitly independent scopes.; The grammar permits `list_lit ::= '[' value (',' value)* ']'`, which cannot express an empty list, while the semantics discuss empty LIST truthiness and quantifiers without defining a way to create a typed empty list.; The `diff` lexical/operator form overlaps NUMBER's optional leading minus and is only described semantically as reserved outside a recursion argument; exact tokenization and parse behavior for `x-1`, `x - 1`, and malformed occurrences are not specified.
- **Decision:** accepted
- **Documenter summary:** Sprint 0 proposed a 9-construct basis (Types & Lexicon, Task, Action, Utterance, Check, Flow-If, Iterate, Bind, Conversation) drawing on Python's flat orthogonality, HTML's content/attribute separation, English's closed-class function words, and formal-language context-free parseability, with Parsel and ReAct as key precedents. The Critic judged it 'needs-rework' after finding the DECREASES recursion-termination proof unsound (a `!=` guard with a negative starting value never terminates), Action's 'always effectful' claim contradicted by its own query-like examples (check_inventory, check_file_age), several worked examples invalid under the basis's own ENTRYPOINT grammar, and no mechanism for external task input or cross-turn data passing; despite this, the basis was accepted after the third attempt with these issues carried forward as known gaps for future sprints.
- **Cost this sprint:** $1.8531

## Sprint 1 (attempt 1/3) — 2026-09-23

- **Language version:** 1.0.0 → 1.0.0 (PATCH)
- **Candidate task:** Rinse the mug in the sink, then put it in the coffee maker.
- **Shaper proposal (model: openai/gpt-5.6-terra):** Clarifies the existing Bind convention for carrying one explicitly named entity reference across sequential household actions. The candidate task is expressed deterministically without adding a redundant sequencing or pronoun construct.
- **Changes:** `bind` (revise, PATCH)
- **Critic decision:** needs-rework — The underlying documentation idea is useful: existing LET plus ordered actions is a good compact representation of simple anaphoric sequential tasks, and it improves planning visibility in the potato-style case. However, the proposed revision introduces a direct contradiction with UTTER's existing binding semantics and overclaims real-world identity from STRING equality. Those are concrete specification defects affecting interpretability and determinism, so the patch cannot be accepted until corrected.
- **Doc hygiene:** pass — All changes carry a complete glossary entry (gloss + worked example).
- **Pre-KPI assessment:**
  - coverage: neutral — The revision does not add an actionable capability: existing LET bindings and ordered ACTION statements already express the shared-reference patterns in the embodied samples. It helps document a useful translation convention, but it does not resolve identity, instance selection, or collection-transfer gaps exposed by the two-pillow and goblet tasks.
  - expressivity: mixed — The worked pattern preserves a simple singular anaphoric reference such as mug/it, and was usable in the potato task. However, a STRING such as "mug" does not reliably denote a particular real-world object when multiple matching objects exist, so the claimed real-world shared-referent semantics overstates what the value model provides.
  - determinism: mixed — Stating that later sequential ACTIONs may reuse a LET name encourages convergence for simple anaphora. But translators still have no deterministic rule for whether to bind a category label, an instance description, a selected object, or a list, and the revision contradicts the existing UTTER binding form by calling LET, Action ->, and task_call -> the only three Bind sites.
  - interpretability: harm — The new prose silently conflicts with Utterance, whose optional -> IDENT is explicitly a binding under Bind's ordinary rules. A reader cannot reconcile the revised claim of three Bind sites with the existing fourth form, and the phrase that a STRING may name an intended real-world entity is not accompanied by an identity-resolution rule.
  - improvement: benefit — For simple sequential household requests, explicitly recommending one shared bound name gives a weaker planner a useful visible data-flow link instead of relying on pronoun resolution. The simulations for the potato and simple placement patterns show this structural benefit, though it is limited by the unresolved identity problem.
- **Simulated examples:**
  - `dev-embodied-2` (seed_tasks) [Full] NL: "Put both pillows from the sofa onto the armchair, one at a time." → `ENTRYPOINT MovePillows

TASK MovePillows {
  LET pillows : LIST[STRING] = ["pillow_1_on_sofa", "pillow_2_on_sofa"]
  FOR EACH pillow IN pillows {
    ACTION pick_up(target=pillow, source="sofa")
    ACTION place(target=pillow, destination="armchair", ordering="one_at_a_time")
  }
}` — Bind helps preserve each loop item's identity across pick_up and place, but the language has no canonical way to obtain or distinguish the two pillows from the request alone; the numbered STRING identifiers are translator-invented.
  - `dev-email-1` (seed_tasks) [Full] NL: "Draft a reply to my professor asking for a two-day extension on the assignment, and keep it formal." → `ENTRYPOINT DraftExtensionReply

TASK DraftExtensionReply {
  ACTION draft_email(recipient="professor", tone="formal", content="Request a two-day extension on the assignment.")
}` — The proposed Bind clarification is irrelevant. The requested email substance is appropriately carried in the content STRING.
  - `42657330-bfc5-425d-ae21-396a9ba1fb12` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Find yellow t-shirts for women small size that are less than $20." → `ENTRYPOINT FindYellowShirts

TASK FindYellowShirts {
  ACTION search(target="women_t_shirts")
  ACTION select_filter(target="size", validation="small")
  ACTION select_filter(target="color", validation="yellow")
  ACTION apply_filters(threshold=20, validation="price_less_than_threshold")
}` — No cross-step anaphora is present, so Bind is irrelevant. Different translators may choose search versus navigation and select_filter versus apply_filters, but the constraints are represented.
  - `6c0a3b1e-6ce8-4955-9359-dd4378aacc82` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Find the price of HomePod mini" → `ENTRYPOINT FindHomePodPrice

TASK FindHomePodPrice {
  LET product : STRING = "HomePod mini"
  ACTION search(target=product)
  ACTION get_price(target=product) -> price : NUMBER
}` — The revision supports reuse of product in the second action. It remains unclear whether get_price's result should include currency, because NUMBER cannot preserve a currency denomination.
  - `trial_T20190907_161637_930071#1` (ALFRED (json_2.1.0, train)) [Full] NL: "Put the goblet in the refrigerator on the table." → `ENTRYPOINT PlaceGoblet

TASK PlaceGoblet {
  LET goblet : STRING = "goblet_in_refrigerator"
  ACTION pick_up(target=goblet, source="refrigerator")
  ACTION place(target=goblet, destination="table")
}` — Bind helps maintain a shared label for the goblet. The label is only a descriptive STRING, not a resolved object identity; multiple goblets would make this representation insufficiently specific.
  - `trial_T20190907_151643_465634#2` (ALFRED (json_2.1.0, train)) [Full] NL: "Take a potato from the count, cook it, finally putting it in the freezer." → `ENTRYPOINT CookAndFreezePotato

TASK CookAndFreezePotato {
  LET potato : STRING = "potato"
  ACTION pick_up(target=potato, source="counter")
  ACTION heat(target=potato)
  ACTION place(target=potato, destination="freezer")
}` — This is the candidate pattern: the proposed clarification visibly preserves potato/it across ordered actions. The source typo "count" is normalized to counter.
  - `django__django-14493` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "ManifestStaticFilesStorage crashes with max_post_process_passes = 0." → `ENTRYPOINT FixDjango14493

TASK FixDjango14493 {
  ACTION modify_code(target="django/contrib/staticfiles/storage.py", content="Initialize substitutions before the post-processing loop so max_post_process_passes=0 does not leave it unbound.")
  ACTION run_tests(target="staticfiles collectstatic with max_post_process_passes=0", validation="no UnboundLocalError")
}` — The actionable repair and validation are represented; detailed code remains an opaque content payload. Bind is irrelevant.
  - `matplotlib__matplotlib-25332` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "Unable to pickle figure with aligned labels." → `ENTRYPOINT FixMatplotlib25332

TASK FixMatplotlib25332 {
  ACTION modify_code(target="lib/matplotlib/cbook.py", content="Remove or replace the unpicklable weakref state associated with aligned labels so figures can be pickled.")
  ACTION run_tests(target="figure with align_labels followed by pickle.dumps", validation="pickling_succeeds")
}` — The sampled trajectory names a target file and the task includes a testable outcome. Bind is irrelevant.
  - `c2762` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Who is the greatest cricketer of all time?" → `ENTRYPOINT CricketQuestion

CONVO CricketQuestion {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Who is the greatest cricketer of all time?", target="greatest cricketer of all time")
  }
}` — The question speech act and topic are formalized; the subjective evaluative substance remains in the allowed opaque content payload. Bind is irrelevant.
  - `c2888` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "what is the house market in new york right now" → `ENTRYPOINT NewYorkHousingQuestion

CONVO NewYorkHousingQuestion {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="What is the house market in New York right now?", target="New York housing market")
  }
}` — The request is a current-information question; its substantive market analysis remains prose payload. Bind is irrelevant.
  - `c929` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "My family is invited to my grandma's birthday. I don't get along with her, would it be okay to be the only one to back out?" → `ENTRYPOINT FamilyEventAdvice

CONVO FamilyEventAdvice {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="My family is invited to my grandma's birthday. I do not get along with her; would it be okay to be the only one to decline?", target="family birthday attendance decision", tone="personal")
  }
}` — The advice-seeking speech act, audience context, and personal register are retained; the relationship narrative remains content payload. Bind is irrelevant.
  - `c5582` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Is it ok to print personal documents at work?" → `ENTRYPOINT WorkplacePrintingQuestion

CONVO WorkplacePrintingQuestion {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Is it okay to print personal documents at work?", target="workplace personal-printing policy")
  }
}` — The question and target policy topic are represented; the requested normative assessment is prose substance. Bind is irrelevant.
  - `wildchat1m_en3u-81276` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "Write a detailed story about Sadie Adler taking off her hat, and dropping it on the ground. She reaches up to her scalp, and begins peeling away her skin. Sadie Adler, now Mary Beth, sighs in relief as she tears away the remainders of her old face." → `ENTRYPOINT GenerateSadieStory

CONVO GenerateSadieStory {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Write a detailed story about Sadie Adler removing her hat, dropping it, peeling away her skin, and becoming Mary Beth.", format="detailed story", target="Sadie Adler to Mary Beth transformation")
  }
}` — The generation intent, requested format, and required story events are represented as meta-structure and content target; the story itself correctly remains opaque prose.
  - `wildchat1m_en3u-144042` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-0125-preview)) [Partial] NL: "explain the importance of using nonparametric control charts for process mean and variability monitoring in two paragraphs" → `ENTRYPOINT ExplainNonparametricCharts

CONVO ExplainNonparametricCharts {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Explain the importance of using nonparametric control charts for process mean and variability monitoring.", format="two paragraphs", target="nonparametric control charts")
  }
}` — Intent, topic, and exact two-paragraph constraint are captured. The technical explanation is appropriately a content payload.
  - `wildchat1m_en3u-122879` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-1106-preview)) [Partial] NL: "Emma was having the best summer ever, working as a counselor at Camp Sludge. This unusual summer camp for girls didn’t do boring things like wallet making, making art or archery. Instead, every day was packed full of mucky, messy activities. The campers - and Emma - would always be covered in a wonderful medley of muck by lunchtime. Emma strolled through the camp, wearing the same uniform the campers wore - shorts, a T-shirt and absolutely no shoes!

Emma finds a group of campers enjoying themselves in the sludge pit. She teases them and asks if anyone fancies having a food fight. She tempts the campers to join in by mentioning the camp has just received a huge quantity of rotten cheese sauce and some other "surprises".

Please continue this story in a fun, entertaining and creative way. Avoid flowery language or talking about liberation and freedom - the campers just think it’s fun getting messy." → `ENTRYPOINT ContinueCampSludge

CONVO ContinueCampSludge {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Continue the Camp Sludge story: Emma finds campers in the sludge pit, teases them about a food fight, and mentions rotten cheese sauce and other surprises.", format="story continuation", tone="fun, entertaining, creative", validation="avoid flowery language; do not discuss liberation or freedom")
  }
}` — The continuation intent, narrative setup, tone, and negative style constraints are retained. Story prose is an allowed opaque payload.
  - `wildchat1m_en3u-83312` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "Personification of Alek Száhala's track "Alabama" (genre:freeform hardcore/fi-nrg). Gender: Female. Age: 14. Ask for a detailed description and list of character attributes. (In line with the characteristics of 00s Anime characters.) Basic characteristics: Height 146cm, short hair, Dark blue pupils and hair, quiet and sentimental, gray dress, loli, etc." → `ENTRYPOINT GenerateAlabamaCharacter

CONVO GenerateAlabamaCharacter {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Personify Alek Szahala's track Alabama as a female 14-year-old 00s-anime-inspired character with height 146cm, short dark-blue hair and pupils, a gray dress, and a quiet sentimental personality.", format="detailed description and list of character attributes", target="Alabama character")
  }
}` — The generation intent, requested outputs, style, and supplied attributes are retained as metadata and payload. Bind is irrelevant.
  - `1775857728160` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "Search the best and the easiests creeper farms that are efortless to build and provide me a lot of gunpowder" → `ENTRYPOINT FindCreeperFarm

CONVO FindCreeperFarm {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Search for the best and easiest effortless Minecraft creeper farms that produce a lot of gunpowder.", target="Minecraft creeper farms", validation="easy to build and high gunpowder output")
  }
}` — The search intent and optimization criteria are represented. The requested recommendations and links are substantive output payload; no link-format constraint was stated in the sampled prompt itself.
  - `1775488035768` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "Hi! How to join the military engineering school" → `ENTRYPOINT MilitaryEngineeringQuestion

CONVO MilitaryEngineeringQuestion {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="How do I join a military engineering school?", target="military engineering school admission")
  }
}` — The admission-information request is represented. Country, school, and applicant details are unspecified in the source, so no more specific structure can be recovered.
  - `1773875884407` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "hello, i wanna plan a trip to morroco" → `ENTRYPOINT PlanMoroccoTrip

CONVO PlanMoroccoTrip {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Help me plan a trip to Morocco.", target="Morocco trip", tone="friendly")
  }
}` — The trip-planning intent and destination are captured. Duration, budget, dates, travelers, and preferences are absent, so the request legitimately remains broad.
  - `1775494752255` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "hello" → `ENTRYPOINT Greeting

CONVO Greeting {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="hello", tone="friendly")
  }
}` — This is a greeting rather than an actionable task. The speech act is fully represented, while there is no substantive requested outcome to encode.
- **Cross-check:** used=False, agreement=partial — No independent provider translations were supplied. Capable translators should converge on LET plus repeated variable use for the potato-style singular anaphora, but are unlikely to converge on entity labels for multiple identical objects, whether to bind product/category strings, or the decomposition granularity of web and code actions.
- **Required changes:**
  - `bind`: Replace “LET, Action's ->, and task_call's -> remain BrainCode's three Bind sites” with language that also includes UTTER's optional -> IDENT, or explicitly redefine UTTER's binding as an exception and update Utterance consistently. The current statement contradicts the existing specification.
  - `bind`: Narrow or define the claim that a STRING “may name an intended real-world entity.” State explicitly that LET binds value equality only, not world-object identity, unless a future typed selection/action-result reference mechanism is introduced.
  - `bind`: Revise the glossary gloss to avoid implying that naming an object once guarantees object identity. Say that repeated use carries the same bound value, and illustrate the limitation or use an unambiguous singleton entity.
  - `basis`: For a future capability sprint, add a canonical way to represent selected object instances or collections returned by Actions (for example, a typed entity/reference result) so requests involving multiple identical objects, such as both pillows, do not depend on translator-invented STRING identifiers.
- **Logic issues:** The revised Bind semantics say there are three Bind sites, but Utterance already defines optional `-> IDENT` as binding its STRING content under Bind's ordinary rules. This produces an internal contradiction about the complete Bind-site set.; The new statement that a LET-bound STRING may name a real-world entity has no resolution semantics. The strings "mug", "goblet", and "pillow" can denote categories or multiple objects, whereas the proposed wording implies stable real-world referential identity.; The worked example is syntactically valid and ordered correctly, but it demonstrates repeated equal STRING values rather than proving that both actions target one particular physical mug.
- **Decision:** needs-rework
- **Documenter summary:** Shaper proposed clarifying the existing LET/Bind convention to formalize carrying a named entity reference (e.g., mug/it) across sequential ACTIONs, framed as a Python-inspired documentation-only patch. The Critic sent it back for rework because the revised text asserted only three Bind sites while contradicting UTTER's existing `-> IDENT` binding form, and because it overclaimed that a LET-bound STRING can denote a stable real-world entity identity when it only guarantees value equality—flagged concretely by the goblet and two-pillow simulations showing multiple identical objects break this claim.
- **Cost this sprint:** $0.2050

## Sprint 1 (attempt 2/3) — 2026-09-23

- **Language version:** 1.0.0 → 1.0.0 (PATCH)
- **Candidate task:** Rinse the mug in the sink, then put it in the coffee maker.
- **Shaper proposal (model: openai/gpt-5.6-terra):** This patch documents the existing composition of ordered Actions and named bindings for sequential anaphoric tasks while correcting the complete set of Bind sites. It explicitly limits bindings to equal values rather than claiming physical-object identity, leaving instance selection for a future capability sprint.
- **Changes:** `bind` (revise, PATCH)
- **Critic decision:** needs-rework — This is a valuable corrective patch: it makes binding scope and UTTER content binding more deterministic, and it removes an unsound identity claim. It cannot be accepted yet because the documentation must be reconciled with the existing three-site wording and because its own corrected semantics demonstrates a material closed-task failure for repeated physical-object references. The core idea is sound, but the specification needs the listed consistency edits and an explicit object-reference design path rather than treating descriptor equality as an operational substitute.
- **Doc hygiene:** pass — All changes carry a complete glossary entry (gloss + worked example).
- **Pre-KPI assessment:**
  - coverage: mixed — The clarified value-level binding usefully covers descriptor reuse across sequential web, support, and code actions. However, the patch explicitly confirms that it cannot express selected physical-object identity, so closed ALFRED tasks whose actionable core requires carrying a particular cup, knife, or mug across effects remain unrepresentable without an unsafe STRING approximation.
  - expressivity: mixed — The patch correctly prevents the false claim that STRING equality preserves real-world identity and adds the previously omitted UTTER binding site. That honesty improves semantic precision, but it also exposes a current expressivity failure for referential closed tasks: `LET cup : STRING = "white cup"` cannot preserve which cup was selected, even when later steps require that exact cup.
  - determinism: benefit — A single shared Bind-site visibility rule, explicit exact typing for LET, and explicit UTTER STRING-result typing reduce uncertainty over whether names can be reused downstream. Capable translators will likely agree on source-order dependencies, although they may still diverge between using a descriptor STRING and omitting a misleading binding for physical-object references.
  - interpretability: benefit — The revised semantics and gloss plainly distinguish equality of a STRING descriptor from world-object identity, which prevents readers from inferring unsupported guarantees. The patch is mostly orthogonal to existing Bind rules, but the retained phrase that LET is the only direct literal/already-bound binding form should be reconciled with the complete four-site list in the frozen specification.
  - improvement: mixed — For ordinary sequential tasks, visible typed data flow gives a weaker agent a useful ordering and reuse signal. For embodied object-manipulation tasks, the same notation can actively mislead a weaker agent into believing that repeated `target=cup` refers to the selected cup, despite the revised semantics saying that it does not.
- **Simulated examples:**
  - `held-trip-1` (seed_tasks) [Full] NL: "Plan a 3-day itinerary in Kyoto that includes at least one temple per day and avoids anything more than a 20-minute walk from the last stop." → `ENTRYPOINT PlanKyoto
TASK PlanKyoto {
  ACTION plan_itinerary(destination="Kyoto", quantity=3, validation="each_day_includes_at_least_one_temple; walking_time_from_previous_stop_at_most_20_minutes")
}` — Open extension Action vocabulary and canonical quantity/validation roles encode the full actionable constraint set. The Bind revision is irrelevant.
  - `held-support-1` (seed_tasks) [Full] NL: "If the customer's order is late and they're a first-time buyer, offer a 10% discount; if they're a repeat buyer, offer free expedited shipping instead." → `ENTRYPOINT ResolveLateOrder
TASK ResolveLateOrder {
  ACTION check_order_status() -> late : BOOL
  ACTION check_buyer_status() -> first_time : BOOL
  IF late AND first_time THEN {
    ACTION offer_discount(quantity=10)
  } ELSE {
    IF late AND NOT first_time THEN {
      ACTION offer_expedited_shipping(quantity=0)
    }
  }
}` — Checks and nested ordered branches capture both alternatives. The proposed Bind clarification helps the typed downstream conditions.
  - `6ca55141-9ba6-4ed7-8c07-77df6c24029d` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Find the lowest-priced gray-colored round-shaped mirror in stock in Atlanta, Georgia, with a maximum price of 20 dollars." → `ENTRYPOINT FindMirror
TASK FindMirror {
  ACTION search(target="mirror")
  ACTION select_store(target="Atlanta, Georgia")
  ACTION apply_filters(target="mirror", validation="color_gray; shape_round; in_stock", threshold=20)
  ACTION sort(target="price", ordering="ascending")
}` — The web vocabulary and canonical threshold/ordering roles encode all requested selection constraints. Bind is irrelevant.
  - `62806bef-eeeb-4892-b4d5-6a8d2005c58d` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Browse the trending searches in Columbus." → `ENTRYPOINT BrowseTrending
TASK BrowseTrending {
  ACTION open(target="city_pages")
  ACTION open(target="Columbus")
  ACTION open(target="trending_searches")
}` — Ordered open operations capture the finite web-navigation core. Bind is irrelevant.
  - `trial_T20190907_134455_194210#0` (ALFRED (json_2.1.0, train)) [Fail] NL: "Place a white cup with a knife in it on the counter in front of the toaster." → `ENTRYPOINT SetCup
TASK SetCup {
  LET knife : STRING = "knife"
  LET cup : STRING = "white cup"
  ACTION pick_up(target=knife, source="table")
  ACTION place(target=knife, destination=cup)
  ACTION pick_up(target=cup, source="sink")
  ACTION place(target=cup, destination="counter in front of toaster")
}` — This is syntactically valid under the patch, but it is not a faithful closed-task representation: repeated STRING `cup` and `knife` do not identify the particular objects picked up or the cup now containing the knife. An explicit selected-instance reference/result mechanism is missing.
  - `trial_T20190908_185043_273617#2` (ALFRED (json_2.1.0, train)) [Fail] NL: "Put a warm coffee cup in the coffee maker." → `ENTRYPOINT WarmCup
TASK WarmCup {
  LET cup : STRING = "coffee cup"
  ACTION pick_up(target=cup, source="coffee maker")
  ACTION place(target=cup, destination="microwave")
  ACTION heat(target=cup)
  ACTION pick_up(target=cup, source="microwave")
  ACTION place(target=cup, destination="coffee maker")
}` — The action ordering is captured, but `cup` is only descriptor equality and cannot guarantee that the heated cup is the removed cup. The proposal correctly identifies, but does not solve, this actionable closed-task gap.
  - `pydata__xarray-4356` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "sum: min_count is not available for reduction with more than one dimensions." → `ENTRYPOINT FixMinCount
TASK FixMinCount {
  ACTION modify_code(target="xarray/core/nanops.py", content="Support sum(min_count=...) when axis contains more than one dimension by calculating the valid-element count across all reduced axes; replace mask.shape[axis] with np.take(a.shape, axis).prod() where applicable.")
  ACTION run_tests(target="sum min_count multi-dimension reduction")
}` — The finite code-edit and validation core is represented; the exact patch content appropriately remains a STRING payload. Bind is irrelevant.
  - `django__django-12155` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "docutils reports an error rendering view docstring when the first line is not empty." → `ENTRYPOINT FixDocstringRendering
TASK FixDocstringRendering {
  ACTION modify_code(target="django/contrib/admindocs/utils.py", content="In trim_docstring, calculate indentation from nonblank lines after the first line, using lines[1:], so an unindented opening docstring line does not force indent to zero.")
  ACTION modify_code(target="django/contrib/admindocs/views.py", content="Update affected admindocs view handling or tests for a docstring whose first line contains text.")
  ACTION run_tests(target="admindocs docstring rendering")
}` — Ordered file modifications and validation capture the actionable core. Bind is irrelevant.
  - `c892` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "The people in our country say that we are so generous and warm, but I know that people will look for a chance to take advantage of others as soon as they can." → `ENTRYPOINT SupportConversation
CONVO SupportConversation {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="The people in our country say that we are so generous and warm, but I know that people will look for a chance to take advantage of others as soon as they can.")
  }
  TURN t2 SPEAKER=USER REPLY_TO t1 {
    UTTER ask(content="Yeah, give me those suggestions.")
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    UTTER ask(content="Can you finish the fourth point?")
  }
}` — The conversation's turn order, follow-up, and continuation request are represented. The emotional substance and requested suggestions remain UTTER content, which is the intended open-item boundary; the UTTER Bind addition is irrelevant here.
  - `c5375` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Are androids better than iphones" → `ENTRYPOINT PhoneAdvice
CONVO PhoneAdvice {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Are androids better than iphones", target="Android phones and iPhones")
  }
  TURN t2 SPEAKER=USER REPLY_TO t1 {
    UTTER ask(content="Best android phones to buy", target="Android phones")
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    UTTER ask(content="Price for Samsung S23 ultra", target="Samsung S23 Ultra")
  }
  TURN t4 SPEAKER=USER REPLY_TO t3 {
    UTTER ask(content="can i swap my old phone for a new one", target="phone trade-in")
  }
}` — The sequential narrowing from comparison to recommendations, price, and trade-in is preserved. Product opinions and current pricing remain prose payload by design.
  - `c2151` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "it pains me to say but racism seems to be just a moving slider between one ethnic group to another. what is going on?" → `ENTRYPOINT DiscussRacism
CONVO DiscussRacism {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="it pains me to say but racism seems to be just a moving slider between one ethnic group to another. what is going on?", tone="distressed")
  }
  TURN t2 SPEAKER=USER REPLY_TO t1 {
    UTTER ask(content="why does racism happen this way - ultimately I am not racist - but it frustrates me to the point of racism when I see preferential treatment of any kind.")
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    UTTER ask(content="So how did racism start - I look back on many many historical accounts and cannot understand where it started. Much the same as being gay was almost celebrated earlier on ... so how have these things become a problem.")
  }
}` — The multi-turn explanatory request and its progression are formalized. Historical argument and response substance legitimately remain content strings.
  - `c1195` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "I believe people with qualifications should be paid more in the workplace than those without any." → `ENTRYPOINT DiscussCompensation
CONVO DiscussCompensation {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="I believe people with qualifications should be paid more in the workplace than those without any.")
  }
  TURN t2 SPEAKER=USER REPLY_TO t1 {
    UTTER inform(content="I believe love, in any relationship, should be reciprocal and not one sided.")
  }
}` — The two conversational propositions are preserved as ordered speech acts. Their substantive reasoning is appropriately opaque prose.
  - `wildchat1m_en3u-38835` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-0314)) [Partial] NL: "what are the use cases of applied observability in law firms and for their clients. What the are the details of the same. Is there any law firm which has implement or is looking into such use cases in future." → `ENTRYPOINT CreateNewsletter
CONVO CreateNewsletter {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Create a newsletter from the supplied Applied Observability article.", format="newsletter", quantity=800, audience="business readers")
  }
  TURN t2 SPEAKER=USER REPLY_TO t1 {
    UTTER ask(content="I want to go from Delhi to Bangkok discreetly so that no one in my family, including my wife, would know. Tell me ideas and the best ways to ensure that I do not get caught.", tone="secretive")
  }
}` — The sampled exchange contains two separate requests: a bounded newsletter-generation request and a later covert-travel request. Both speech acts and the newsletter's length/format constraints are represented; article and travel-plan substance remain content payload. No proposed Bind feature helps.
  - `wildchat1m_en3u-111541` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-1106-preview)) [Partial] NL: "hi" → `ENTRYPOINT CreateSeoCopy
CONVO CreateSeoCopy {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Create another catchy Hinglish SEO title, description, and comma-separated tags for a YouTube Short featuring Vivek Bindra answering whether AI will take jobs.", format="title; description; comma-separated tags", tone="catchy", audience="YouTube viewers")
  }
}` — The final request's content-generation speech act, target platform, language/register, required outputs, and SEO constraint are represented. Generated wording remains open-item prose payload.
  - `wildchat1m_en3u-55500` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "Give a Longer Description Backstory about Donatello/Donnie (Caulifla’s Boyfriend) (Teenage Mutant Ninja Turtles Donatello 2012 x Dragon Ball Super) meeting these characters, Goku, Vegeta, Gohan, Videl, Bulma, Beerus, Trunks, Goten, Whis, Master Roshi, Chi-Chi, Krillin, Shenron, Quitela, Mr. Satan, Caulifla (Donatello’s Girlfriend), Kale, Vados, and the rest of the characters that are in Dragon Ball Super, but every one and everybody knows who Donatello is, but little did they know that Donatello is a god cause he is skilled in using his roasting skills also with clever and witty comebacks and is unbeatable in a verbal talk and is skilled in martial arts, has Hybrid Saiyan Power Boost and Ki Manipulation and he transforms into Super Saiyan Transformation, and also has Unbelievable Levels Of Durability, Expedited Healing, Read Minds, and Jerry also can do different types of combat skills from Streets of Rage Game Series Attacks and Combos, and then He can teleport faster than the speed of light, and he can reappear faster than the speed of light, Incredible Agility, Keen Senses, Superhuman Strength, and Immense Fighting Determination and he has Almighty Mode/Transformation, Deity Mode/Transformation, God Transformation, Supreme Mode/Transformation, and Berserker Physiology making Donnie’s Power reach Infinite Power Level, and he has Transcendent Physiology, God Morphing, Inner Power, Godly Fighter, God Hand, Reality Warping, and lastly Nigh-Absolute Regeneration, and Donatello's weaknesses is None Notable which means he have no weaknesses making him into a god himself." → `ENTRYPOINT ContinueStory
CONVO ContinueStory {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Continue Part 2 of the Donatello and Goku sparring story after Donatello's god-like transformations.", format="scripted story continuation", tone="dramatic")
  }
}` — The final continuation request, installment relation, format, and dramatic register are captured. The fan-fiction plot, powers, and dialogue remain correctly carried as content prose.
  - `wildchat1m_en3u-30875` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0301)) [Partial] NL: "Hi," → `ENTRYPOINT AskWorkAuthorization
CONVO AskWorkAuthorization {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="which state that don't ask for a work permit to the non-U.S. citizens", target="U.S. work authorization requirements")
  }
}` — The final information request and subject are represented. The legal answer remains a prose payload; the Bind revision is irrelevant.
  - `1775708977070` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "I need help planning a healthy light dinner for tonight that keeps me full and avoids late-night hunger. I prefer simple ingredients and something quick to prepare." → `ENTRYPOINT DinnerAdvice
CONVO DinnerAdvice {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Suggest a healthy light dinner for tonight that keeps me full and avoids late-night hunger.", tone="practical", deadline="tonight", validation="simple ingredients; quick preparation")
  }
  TURN t2 SPEAKER=USER REPLY_TO t1 {
    UTTER ask(content="Adapt the dinner without chickpeas while keeping it filling enough to prevent late-night hunger.", validation="no chickpeas")
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    UTTER ask(content="Adapt the same dinner idea using turkey instead of chicken, with the same goal of staying full overnight.", validation="use turkey instead of chicken")
  }
  TURN t4 SPEAKER=USER REPLY_TO t3 {
    UTTER ask(content="Suggest a warm light midnight snack with the same goal of satiety and portion control.", tone="practical", validation="warm; light; satiety; portion control")
  }
}` — The iterative dietary revisions, substitution constraints, timing, temperature, and portion-control goal are all captured. Specific recipe content remains legitimate natural-language substance.
  - `1775686840693` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "o fungo nos dedos do pé, se eu passar a mão e depois passar a mão em outra parte do corpo, eu espalho o fungo de local?" → `ENTRYPOINT HealthQuestion
CONVO HealthQuestion {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="o fungo nos dedos do pé, se eu passar a mão e depois passar a mão em outra parte do corpo, eu espalho o fungo de local?", target="fungal spread")
  }
  TURN t2 SPEAKER=USER REPLY_TO t1 {
    UTTER ask(content="mas porque que quando corto unha, o fungo de uma unha não passa para outra? eu estou usando o mesmo cortador.", target="nail-fungus transmission")
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    UTTER ask(content="então o fungo do dedo do pé pode estar na virilha ou até na bunda?", target="fungal spread to groin or buttocks")
  }
}` — The Portuguese multi-turn medical-information sequence and its clarification path are preserved. Medical explanation remains prose content.
  - `1775962320176` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Full] NL: "Hello" → `ENTRYPOINT Greeting
CONVO Greeting {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="Hello")
  }
}` — A greeting is fully represented as a user speech act. The revised UTTER Bind behavior is irrelevant because no result is reused.
  - `1775436940555` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "I was absent from work for a week due to illness, while there were no vacations available to me at the time. I would like you to suggest an email message that I can send to my boss in a friendly manner so that he does not prevent me from working." → `ENTRYPOINT DraftReturnEmail
CONVO DraftReturnEmail {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Draft an email to my boss after a one-week illness absence when I had no vacation available, asking to resume work.", recipient="boss", format="email", tone="friendly", validation="support continued employment")
  }
}` — Recipient, format, tone, circumstance, and intended outcome are encoded. The email's actual wording properly remains an opaque prose payload.
- **Cross-check:** used=False, agreement=partial — No independent translations were supplied. Self-assessment: capable translators should converge highly on the new four-site source-order/lexical Bind rule; they are less likely to converge on ALFRED-style repeated STRING labels because some will use them as an approximation while others will reject them as semantically inadequate. Open-item simulations may vary in how much prior conversational context is retained, while preserving equivalent turn structure.
- **Required changes:**
  - `Bind`: Apply the revised Bind grammar, semantics, worked example, and glossary entry to the frozen language-spec and glossary, explicitly replacing the current statement that LET, Action `->`, and task_call `->` are the only three Bind sites with the complete four-site list including UTTER `->`.
  - `basis`: Add an explicit typed selected-instance/reference capability before claiming closed embodied-object coverage: define a type such as REF[T] or OBJECT_REF, an Action result/selection form that produces it, and require object-manipulation Actions to accept that reference when a later step means the same selected physical object. Define its scope, equality/identity semantics, and behavior when zero or multiple objects match.
  - `Bind`: Replace the informal phrase "same scope or a nested child scope" with a normative enumeration of all binding contexts, including Task bodies, Turn bodies, IF branches, FOR iteration bodies, and task-call invocation scopes, and state that an UTTER binding is visible only to later steps in its own TURN/body.
  - `Bind`: Amend the rationale/example wording to say that source-order execution preserves only the order of operations and descriptor-value reuse, not a candidate object. Do not characterize the current STRING workaround as expressing the selected candidate.
- **Logic issues:** The proposed Bind semantics says all four forms are Bind sites, but the currently frozen Bind section and glossary still normatively say there are only three sites: LET, Action `->`, and task_call `->`. Unless the patch is applied as a complete replacement across both documents, this is a direct internal contradiction.; The worked example is grammatically valid and correctly demonstrates sequential descriptor reuse, but it cannot establish the natural-language pronoun's physical-object referent if several mugs match. Its surrounding rationale overstates what ordered execution plus a STRING name can preserve.; A valid input such as `LET mug : STRING = "mug"; ACTION pick_up(target=mug); ACTION place(target=mug, destination="coffee_maker")` has defined value semantics but no defined selected-object behavior. In a multi-mug environment it cannot determine whether `place` uses the picked-up mug, another matching mug, or fails.; The patch improves documentation rather than adding the promised future instance-selection mechanism, so the sampled ALFRED tasks remain closed-task failures under the stated Full-coverage criterion.
- **Decision:** needs-rework
- **Documenter summary:** The Shaper proposed clarifying Bind semantics into a unified four-site rule (LET, Action ->, task_call ->, UTTER ->) with explicit source-order visibility, while correcting an overreach that STRING equality implies real-world object identity. The Critic ruled needs-rework: the patch contradicts the currently frozen spec's three-site Bind list, and its own honest semantics exposes that repeated STRING descriptors (e.g., 'cup', 'knife') cannot represent selected physical-object identity, causing Fail coverage on ALFRED object-manipulation tasks like the white-cup-with-knife example; the Critic required reconciling the site list and adding an explicit typed instance-reference mechanism before acceptance.
- **Cost this sprint:** $0.2397

## Sprint 1 (attempt 3/3) — 2026-09-23

- **Language version:** 1.0.0 → 2.0.0 (MAJOR/PATCH)
- **Candidate task:** Rinse the mug in the sink, then put it in the coffee maker.
- **Shaper proposal (model: openai/gpt-5.6-terra):** This set adds typed physical-instance references so an embodied task can select one mug during rinsing and deterministically use that exact mug in a later placement action. It also reconciles Bind documentation around all four binding forms and makes their scopes explicit.
- **Changes:** `types-lexicon` (revise, MAJOR), `action` (revise, MAJOR), `bind` (revise, PATCH)
- **Critic decision:** needs-rework — [Forced acceptance after 3 attempt(s) without a clean accept — the required changes below are known issues carried forward for a future sprint to address, not resolved.] The central idea is sound and yields a real improvement: explicitly bound physical identity prevents a later household action from silently selecting another matching object. It cannot yet be accepted because the revised lexical grammar is incomplete, REF comparison is undefined in Check, and the proposal cannot formally express embodied relations to a selected object, which leaves a sampled closed household task only partially represented. The requested repairs are local extensions that preserve the design's explicit Bind discipline and should allow a revised version to deliver a net positive result.
- **Doc hygiene:** pass — All changes carry a complete glossary entry (gloss + worked example).
- **Pre-KPI assessment:**
  - coverage: benefit — REF[STRING] materially improves coverage for household tasks whose later actions must operate on the particular object selected earlier. The toilet-paper task can now carry separate full-roll and empty-roll identities, and the sponge/bowl task can retain the selected sponge and bowl. However, no structured relation role can express placement relative to a bound object (for example, "left of full_roll"), and destination selection cannot itself be bound, so coverage remains incomplete for several embodied trajectories.
  - expressivity: mixed — The changes preserve same-object dependencies that repeated STRING descriptors lose, as demonstrated in the household simulations. But they do not define how REF values participate in Check despite defining REF equality, and they do not support relative spatial relations involving a REF; the first ALFRED item therefore retains a semantically important relation only as an opaque STRING descriptor.
  - determinism: mixed — Fail-on-ambiguous STRING selection is a strong deterministic improvement over arbitrary object choice, and both independent translations of the toilet-paper item converged on REF[STRING] bindings. Yet translators still have no canonical rule for when a destination must be selected and retained as a REF, how to encode relations such as left_of(ref), or whether a request should be represented as a TASK or CONVO; the independent translations visibly diverge on the latter.
  - interpretability: mixed — REF[STRING] and the revised Bind scope rules are understandable and reduce the misleading implication that a repeated label denotes one object. The revised Types grammar, however, omits the existing lexical definitions and does not reserve REF, while the specification now has incompatible or incomplete rules for REF use in Check. A reader cannot determine whether `IF a == b` is valid when both are REF[STRING].
  - improvement: benefit — Explicit identity-carrying data flow gives a weaker planner a useful operational constraint: after selecting a mug, roll, sponge, or bowl, it must use that object rather than re-querying by description. The no-tie-breaking rule also prevents unsafe accidental substitutions. The gain is reduced where the task needs relations between selected entities, because the language still exposes no structured way to supply those relations.
- **Simulated examples:**
  - `held-support-1` (seed_tasks) [Full] NL: "If the customer's order is late and they're a first-time buyer, offer a 10% discount; if they're a repeat buyer, offer free expedited shipping instead." → `ENTRYPOINT HandleLateOrder

TASK HandleLateOrder {
  ACTION check_order_status(target="customer_order") -> is_late : BOOL
  ACTION check_customer_history(target="customer") -> buyer_type : STRING
  IF is_late AND buyer_type == "first_time" THEN {
    ACTION apply_discount(target="customer_order", quantity=10)
  }
  IF is_late AND buyer_type == "repeat" THEN {
    ACTION upgrade_shipping(target="customer_order", format="expedited")
  }
}` — The proposed REF and Bind changes are irrelevant; existing typed checks and ordered actions express both conditional remedies.
  - `dev-code-1` (seed_tasks) [Full] NL: "Given a list of file paths, delete every file older than 30 days unless it's in the 'archive' folder." → `ENTRYPOINT DeleteOldFiles

TASK DeleteOldFiles {
  ACTION get_file_paths() -> file_paths : LIST[STRING]
  FOR EACH path IN file_paths {
    ACTION check_file_age(target=path) -> age_days : NUMBER
    ACTION check_file_location(target=path) -> folder : STRING
    IF age_days > 30 AND folder != "archive" THEN {
      ACTION delete_file(target=path)
    }
  }
}` — Existing LIST iteration, conditions, and code actions cover the actionable core. REF is irrelevant because file paths already serve as stable identifiers in this request.
  - `8c5ccffa-b88e-4928-9394-6d46cfd36e59` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "What are today's Limited Time Offers deals?" → `ENTRYPOINT GetLimitedTimeOffers

TASK GetLimitedTimeOffers {
  ACTION open(target="Coupons & Deals")
  ACTION click(target="Limited Time Offers") -> deals : LIST[STRING]
}` — The web trajectory is captured with canonical open/click actions. Proposed REF support is irrelevant.
  - `b49f88ac-b407-41af-a9e7-f5e4cd1f970a` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Check the rating and user reviews for the game "Deathloop"." → `ENTRYPOINT CheckDeathloop

TASK CheckDeathloop {
  ACTION click(target="Search")
  ACTION fill_field(target="Search", content="Deathloop")
  ACTION click(target="Deathloop")
  ACTION check_rating(target="Deathloop") -> rating : NUMBER
  ACTION check_user_reviews(target="Deathloop") -> reviews : LIST[STRING]
}` — Existing web actions and typed results express the navigation and requested information. REF is not needed because no later operation depends on a separately selected physical instance.
  - `trial_T20190912_052310_164968#2` (ALFRED (json_2.1.0, train)) [Partial] NL: "To move a full roll of toilet paper and an empty roll to the counter." → `ENTRYPOINT MoveToiletPaperRolls

TASK MoveToiletPaperRolls {
  ACTION pick_up(target="full toilet paper roll", source="toilet paper dispenser") -> full_roll : REF[STRING]
  ACTION place(target=full_roll, destination="counter")
  ACTION pick_up(target="empty toilet paper roll", source="in front of spray bottle") -> empty_roll : REF[STRING]
  ACTION place(target=empty_roll, destination="counter", ordering="left of full_roll")
}` — REF[STRING] correctly preserves each selected roll across pickup and placement and is the key helpful change. The required final relation, placing the empty roll to the left of the particular bound full roll, has no defined structured role accepting REF[STRING]; `ordering="left of full_roll"` is only an opaque descriptor and does not denote the bound reference.
  - `trial_T20190919_003451_692296#1` (ALFRED (json_2.1.0, train)) [Full] NL: "Move a sponge and bowl from a counter to a cupboard" → `ENTRYPOINT MoveSpongeAndBowl

TASK MoveSpongeAndBowl {
  ACTION pick_up(target="sponge", source="counter") -> sponge : REF[STRING]
  ACTION place(target=sponge, destination="bowl")
  ACTION pick_up(target="bowl", source="counter") -> bowl : REF[STRING]
  ACTION place(target=bowl, destination="bottom_left_cupboard")
  ACTION close_container(target="bottom_left_cupboard")
}` — The selected sponge and bowl are retained as distinct physical identities; the sponge remains in the selected bowl when that bowl is placed. The REF and revised Bind rules prevent accidental re-selection on the later object-directed steps.
  - `sphinx-doc__sphinx-8035` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "Support defining specific `:private-members:` for autodoc" → `ENTRYPOINT SupportPrivateMembersArguments

TASK SupportPrivateMembersArguments {
  ACTION modify_code(target="sphinx/ext/autodoc/__init__.py", content="Allow :private-members: to accept explicit private-member names, mirroring :members:, so only the named private members are documented rather than all private members.")
  ACTION run_tests(target="sphinx.ext.autodoc")
}` — The code modification and validation are expressible through existing Code actions; the detailed requested behavior remains correctly in the STRING content payload. Proposed changes are irrelevant.
  - `sphinx-doc__sphinx-7462` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "`IndexError: pop from empty list` for empty tuple type annotation" → `ENTRYPOINT FixEmptyTupleAnnotation

TASK FixEmptyTupleAnnotation {
  ACTION modify_code(target="sphinx/domains/python.py", content="Handle Tuple[()] during annotation unparsing without popping an empty result list.")
  ACTION modify_code(target="sphinx/pycode/ast.py", content="Preserve and parse empty tuple type annotations needed by autodoc.")
  ACTION run_tests(target="empty_tuple_type_annotation", validation="docs build succeeds and foo displays a valid annotation")
}` — The actionable fix trajectory and validation are expressible with existing code actions. REF and Bind revisions are irrelevant.
  - `c3312` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "All people should switch to veganism on moral and ethical grounds" → `ENTRYPOINT VeganismClaim

CONVO VeganismClaim {
  TURN t1 SPEAKER=USER {
    UTTER propose(content="All people should switch to veganism on moral and ethical grounds.")
  }
}` — The speech act and speaker are preserved; the ethical argument is appropriately an opaque prose payload. Proposed REF support is irrelevant.
  - `c4642` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "What does christianity mean?" → `ENTRYPOINT AskChristianityMeaning

CONVO AskChristianityMeaning {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="What does christianity mean?", target="Christianity")
  }
}` — The question speech act and subject are preserved; its requested explanatory substance remains an appropriate prose payload. Proposed changes are irrelevant.
  - `c5110` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Boris Johnson good or bad" → `ENTRYPOINT AskBorisJohnsonEvaluation

CONVO AskBorisJohnsonEvaluation {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Is Boris Johnson good or bad?", target="Boris Johnson")
  }
}` — The evaluative question and target are represented, while the substantive judgment remains prose. REF and Bind changes do not apply.
  - `c74` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Should Israel exist in the land of Levant?" → `ENTRYPOINT AskIsraelExistence

CONVO AskIsraelExistence {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Should Israel exist in the land of Levant?", target="Israel")
  }
}` — The political question and target are preserved; its substantive historical and political argument correctly remains opaque content. Proposed changes are irrelevant.
  - `wildchat1m_en3u-149175` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-0125-preview)) [Partial] NL: "Write 10 funny tweets about how I found these two quahogs on the beach this afternoon" → `ENTRYPOINT WriteQuahogTweets

TASK WriteQuahogTweets {
  ACTION compose_posts(target="tweets", quantity=10, tone="funny", format="tweet", content="I found two quahogs on the beach this afternoon.")
}` — The generation intent, quantity, format, tone, and topic are explicit; the ten creative tweets themselves are correctly an opaque content-generation result. Proposed REF support is irrelevant.
  - `wildchat1m_en3u-30995` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0301)) [Partial] NL: "can you give me some novel and useful ideas for my script of presentation， just add them in my script. Thanks" → `ENTRYPOINT ReviseMentalHealthPresentation

TASK ReviseMentalHealthPresentation {
  LET script : STRING = "Presentation script about mental-health stigma, pressures on children in Hong Kong, consequences of unmanaged negative emotions, and individual and government solutions."
  ACTION generate_ideas(target="mental health presentation", source=script, validation="novel_and_useful") -> ideas : LIST[STRING]
  ACTION insert_content(target=script, content=ideas, format="presentation script")
}` — The request's generate-then-integrate ordering, novelty/usefulness condition, and destination script are represented. The long script and generated ideas remain prose payloads, which is expected for this open content-generation task.
  - `wildchat1m_en3u-69869` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "A long list declaring fictional characters in a personal harem, with their source-accurate appearances, personalities, and powers." → `ENTRYPOINT CharacterDeclaration

CONVO CharacterDeclaration {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="The user declares a personal harem containing Hinata Hyuga, Konan, Temari, Hanabi Hyuga, Samui, Karui, Ino Yamanaka, Shiki Ryougi, Altair, Anko Mitarashi, Kushina Uzumaki, Mabui, Lady Tsunade, Mei Terumi, and Mikoto Uchiha, each with source-accurate appearance, personality, and stated powers.")
  }
}` — The item is a declarative conversational contribution, so a USER inform turn preserves its speech-act structure. The long character descriptions are prose substance; REF is irrelevant.
  - `wildchat1m_en3u-65289` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "Write a scene as Chandler Hallow from the MrBeast channel learns during the filming of the video that his wife Dasha and child have died. Describe everything in great detail. Write his hysteria and horror. Write as many words as possible" → `ENTRYPOINT WriteTragicScene

CONVO WriteTragicScene {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Write a highly detailed, maximally long scene in which Chandler Hallow learns while filming that his wife Dasha and child have died; depict his hysteria and horror.", target="tragic fictional scene", format="scene", quantity="as many words as possible")
  }
}` — The request's speech act, format, detail, emotional-focus, and length constraint are captured. The requested scene remains an opaque creative payload; REF support is irrelevant.
  - `1775938591749` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "Hi, I need help organising my bookshelves" → `ENTRYPOINT OrganiseBookshelves

CONVO OrganiseBookshelves {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Help me organise my bookshelves.", target="bookshelves")
  }
}` — The assistance request and target are represented; the personalized organizational advice is open prose substance. Proposed changes are irrelevant.
  - `1775498956373` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "Problem solving from work" → `ENTRYPOINT WorkProblemHelp

CONVO WorkProblemHelp {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Help with problem solving from work.", target="work problem")
  }
}` — The user is seeking work-problem-solving assistance, but provides no concrete problem, constraints, or desired framework. The request is therefore necessarily an open conversational payload; REF is irrelevant.
  - `1775791789755` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "hello" → `ENTRYPOINT Greeting

CONVO Greeting {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="hello")
  }
}` — The greeting speech act is captured. Its content is an opaque conversational payload, and the proposed changes are irrelevant.
  - `1775940921302` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "planning a meal" → `ENTRYPOINT PlanMeal

CONVO PlanMeal {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Help me plan a meal.", target="meal")
  }
}` — The assistance intent and meal-planning target are preserved; the eventual meal plan depends on omitted preferences and remains open prose content. REF support is irrelevant.
- **Cross-check:** used=True, agreement=partial — For both ALFRED household items, Anthropic and Gemini independently used REF[STRING] bindings in the same general pickup-then-place pattern as this simulation, supporting the central identity mechanism. But independent providers frequently diverged between TASK/Action and CONVO/UTTER representations for the same requests, several supplied expressions omit the mandatory ENTRYPOINT, and the providers do not converge on how to encode the relative placement relation absent from the proposal.
- **Required changes:**
  - `types-lexicon`: Restore all existing lexical primitive definitions (STRING, NUMBER, COMMENT, whitespace, and reserved words) in the revised grammar, add REF to the reserved-word list, and explicitly state that REF is legal only in type position as `REF[type]`.
  - `check`: Revise Check to define REF[T]: permit only `==` and `!=` between exactly matching REF[T] operands, define REF truthiness or explicitly prohibit a bare REF value in a Check, and state that LIST structural equality uses the REF equality rule for REF elements.
  - `action`: Add a structured spatial-relation mechanism for household placement, such as a canonical `relation` attribute whose value is a defined relation expression `left_of(IDENT)`/`right_of(IDENT)` accepting REF[STRING]. Define its runtime meaning and require a REF when the source request means the same previously selected object.
  - `action`: Define how a selected entity in source or destination position can be captured for later use. At minimum, permit a typed REF result for an Action that uniquely selects a STRING source or destination and specify exactly which selected entity is returned, rather than limiting automatic capture to STRING target.
  - `types-lexicon`: Clarify the `REF[T]` parameterization: either define the meaning of every permitted T or restrict the current household-profile form to `REF[STRING]` syntactically. As written, REF[NUMBER], REF[LIST[...]], and other forms are grammatical but have no descriptive/entity semantics.
  - `bind`: State explicitly that task parameters and RETURNS may carry REF[T] under ordinary exact-type checking, and add a worked example where a task returns a REF and its caller consumes the task-call result.
- **Logic issues:** The revised Types & Lexicon grammar is presented as a replacement but drops the current definitions of STRING, NUMBER, COMMENT, whitespace, and reserved words; therefore the revised grammar no longer fully defines the tokens it uses.; REF is introduced as a type keyword but is not added to the reserved-word list, so `REF` can still be lexed as IDENT under the retained lexical rule.; Types defines REF equality, but Check's normative comparison semantics enumerate NUMBER, STRING, BOOL, and LIST only. It neither permits nor forbids REF equality, so `a == b` for `REF[STRING]` has no defined behavior.; The household Action semantics require REF reuse for every later entity-bearing role denoting the same object, but only a STRING target can be captured automatically. A uniquely selected STRING destination or source cannot be named as a REF for a later relation or action.; The worked rinse example is valid under the new target-result rule, but it does not test the stated rule for inaccessible/deleted references, REF copying by LET, task-return propagation, or any source/destination REF use.; Relative placement such as "to the left of the full roll" cannot be represented as a relation to `full_roll`: ordering accepts only a value and has no relation grammar or semantics, while the action extension permits REF only in target, source, and destination roles.; REF[T] is grammatically general, while its semantics only explains a physical entity whose descriptive value type is T and only identifies REF[STRING] as applicable in the household profile. Other grammatical parameterizations lack defined runtime meaning.
- **Decision:** accepted
- **Documenter summary:** The Shaper proposed adding a REF[T] typed physical-instance reference (plus reconciled Bind scope rules across LET/Action/task_call/UTTER) so household tasks like rinsing then placing 'it' could deterministically track the same object across steps. The Critic found the core mechanism sound and beneficial (both ALFRED simulations showed REF[STRING] correctly preserving object identity across pickup/place actions) but flagged unresolved gaps—dropped lexical primitives, undefined REF equality in Check, and no way to express relational placement like 'left of the full roll'—yet, since this was the third attempt without a clean accept, it was force-accepted with these required changes carried forward to a future sprint.
- **Cost this sprint:** $1.6108

## Sprint 2 (attempt 1/3) — 2026-09-23

- **Language version:** 2.0.0 → 2.0.0 (MINOR)
- **Candidate task:** Draft a reply to my professor asking for a two-day extension on the assignment, and keep it formal.
- **Shaper proposal (model: gemini/gemini-3.1-pro-preview):** Clarifies how Action attributes separate core semantic content from stylistic and routing constraints, mirroring HTML, and adds 'draft' to the COMMUNICATION profile.
- **Changes:** `Action` (revise, MINOR)
- **Critic decision:** needs-rework — Canonical `draft` is a useful, positive addition for text-generation requests and independently appears in provider translations, but its side-effect and result contract is undefined. The patch also leaves an overlapping Action specification and a non-operational attribute taxonomy, which prevents deterministic translation. These are concrete, repairable specification defects rather than a rejection of the core idea.
- **Doc hygiene:** pass — All changes carry a complete glossary entry (gloss + worked example).
- **Pre-KPI assessment:**
  - coverage: benefit — Adding canonical COMMUNICATION `draft` directly improves coverage for writing, rewriting, and document-generation requests; it is used in the PATH writing simulations. It does not address several held-out structured gaps exposed by the itinerary, flight-filter, ticket-seat-range, and household-lighting requests.
  - expressivity: mixed — The new verb captures the distinction between drafting text and sending it, and attributes preserve recipient, tone, format, and content in the worked example. However, the proposal leaves the effect of `draft` underspecified (saved draft artifact, returned text, or both), and its claimed core-versus-style distinction is not operationally defined; moreover, closed requests still require opaque prose in `validation` for constraints such as per-day coverage, walking distance, stop count, seat ranges, and cancellation conditions.
  - determinism: mixed — The canonical `draft` verb makes independent translations of writing requests more likely to converge: both supplied providers independently used it for several writing items. But providers still diverged between TASK/ACTION and CONVO/UTTER for open requests, whether to put the request in `content` or `target`, whether to bind a draft result, and whether a generated draft is an effectful action; the new HTML analogy gives no selection rule for these choices.
  - interpretability: mixed — A reader can readily understand `ACTION draft(... tone="formal")`, and the glossary example is legible. Yet the revised Action construct overlaps materially with the separate lower-case `action` supplement, which remains in the specification and says its canonical rules are unchanged; the proposal does not state whether it replaces both entries. The terms “core semantic payload,” “stylistic,” “routing,” and “contextual” are illustrative rather than defined categories, so they cannot determine a unique encoding.
  - improvement: benefit — For writing tasks, a weaker model receives an actionable separation between requested text, output form, recipient, and register rather than one undifferentiated prompt. The benefit is constrained by the missing contract for what executing `draft` does and by the inability to represent structured selection constraints without prose.
- **Simulated examples:**
  - `held-trip-1` (seed_tasks) [Partial] NL: "Plan a 3-day itinerary in Kyoto that includes at least one temple per day and avoids anything more than a 20-minute walk from the last stop." → `ENTRYPOINT PlanKyotoItinerary

TASK PlanKyotoItinerary {
  ACTION plan_itinerary(target="Kyoto", quantity=3, format="day itinerary", validation="at least one temple per day; each next stop no more than 20 walking minutes from the preceding stop")
}` — Action provides a usable itinerary-planning step, but no construct formally represents days, stop adjacency, route travel-time calculation, or a per-day existential constraint. The proposed `draft` change is irrelevant.
  - `dev-email-2` (seed_tasks) [Full] NL: "If my manager hasn't replied by Friday, send a polite follow-up; otherwise do nothing." → `ENTRYPOINT FollowUpManager

TASK FollowUpManager {
  ACTION check_reply_status(target="manager", deadline="Friday") -> replied : BOOL
  IF NOT replied THEN {
    ACTION send_email(recipient="manager", tone="polite", content="follow-up")
  }
}` — Existing Action and Flow-If capture the condition, deadline, recipient, tone, and ordered side effect. The proposed `draft` change is irrelevant.
  - `8fb78266-8862-4608-9ff3-92f81e58b2ff` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Partial] NL: "Find the cheapest non-stop or 1 stop flight from JFK, New York to Changi, Singapore for 1 traveler on April 11 which includes seat selection and free cancellation" → `ENTRYPOINT FindFlight

TASK FindFlight {
  ACTION open(target="flight booking site")
  ACTION search(source="JFK, New York", destination="Changi, Singapore", quantity=1, deadline="April 11")
  ACTION apply_filters(target="stops", validation="nonstop_or_one_stop")
  ACTION apply_filters(target="seat_selection", validation="included")
  ACTION apply_filters(target="cancellation", validation="free")
  ACTION sort(target="price", ordering="ascending")
}` — The web action sequence and most fields are represented, but the date is forced into `deadline`, while the stop disjunction and entitlement conditions survive only as opaque validation strings. The proposed `draft` change is irrelevant.
  - `29f47ddb-3d25-4cfb-b1d6-d3987e998a13` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Partial] NL: "Check the movie "65" that is digital at the AMC Grove City 14 showing at 7:30 pm on Tuesday, March 28, 2023 and buy four tickets for seats J10 through J7" → `ENTRYPOINT BuyMovieTickets

TASK BuyMovieTickets {
  ACTION search(target="65", format="digital")
  ACTION select_filter(target="AMC Grove City 14")
  ACTION select_filter(target="7:30 pm showing", deadline="Tuesday, March 28, 2023")
  ACTION select_filter(target="seats J10 through J7", quantity=4)
  ACTION submit(content="buy tickets")
}` — The theater, movie, format, showing time/date, purchase, and ticket quantity are captured. Seat interval/order is only prose in `target`; the grammar has no range, seat identifier, or reservation construct. The proposed `draft` change is irrelevant.
  - `trial_T20190908_083350_272263#2` (ALFRED (json_2.1.0, train)) [Partial] NL: "Examine a book by the light of a small lamp." → `ENTRYPOINT ExamineBookByLamp

TASK ExamineBookByLamp {
  ACTION examine(target="book", source="small lamp")
}` — The requested relation is retained through target/source, but the household vocabulary has no canonical `examine` or lamp-activation action. The policy is unclear whether unlisted household actions are permitted extensions, because extension vocabulary is said to be allowed only outside listed profiles. The proposed `draft` change is irrelevant.
  - `trial_T20190909_014042_055607#1` (ALFRED (json_2.1.0, train)) [Full] NL: "rinse a rag off in the sink and put it inside of the tub" → `ENTRYPOINT RinseRagIntoTub

TASK RinseRagIntoTub {
  ACTION rinse(target="rag", destination="sink") -> rag : REF[STRING]
  ACTION place(target=rag, destination="tub")
}` — The current REF household extension preserves the same selected rag through the ordered rinse and placement steps. The proposed `draft` change is irrelevant.
  - `matplotlib__matplotlib-25775` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "[ENH]: Add get/set_antialiased to Text objects
### Problem

Currently, Text objects always retrieve their antialiasing state via the global rcParams["text.antialias"], unlike other artists for which this can be configured on a per-artist basis via `set_antialiased` (and read via `set_antialiased`).

### Proposed solution

Add similar getters/setters on Text objects (also adjusting Annotations accordingly, if needed) and use that info in the drawing stage.



Should be relatively easy to implement, except that the slight fiddling needed with backends requires some understanding of backend code (I think we need to replace the access to `rcParams["text.antialiased"]` by going through the GraphicsContext state)." → `ENTRYPOINT AddTextAntialiased

TASK AddTextAntialiased {
  ACTION modify_code(target="lib/matplotlib/text.py", content="Add per-Text get_antialiased and set_antialiased, adjust Annotation if needed, and store per-artist antialiasing state.")
  ACTION modify_code(target="lib/matplotlib/backends/backend_agg.py", content="Use Text per-artist antialiasing through GraphicsContext rather than global rcParams text.antialiased.")
  ACTION modify_code(target="lib/matplotlib/backends/backend_cairo.py", content="Use Text per-artist antialiasing through GraphicsContext rather than global rcParams text.antialiased.")
  ACTION run_tests(target="Text and Annotation antialiasing rendering")
}` — The canonical CODE actions capture concrete files, ordered modifications, required behavior, and validation. Code-change substance appropriately remains the Action content payload. The proposed `draft` change is irrelevant.
  - `django__django-16877` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "New template filter `escapeseq`
Description
	
Following #34574, and after some conversations within the security team, it seems appropriate to provide a new template filter escapeseq which would be to escape what safeseq is to safe. An example of usage would be:
{{ some_list|escapeseq|join:"," }}
where each item of some_list is escaped before applying the join operation. This usage makes sense in a context where autoescape is off.
" → `ENTRYPOINT AddEscapeseqFilter

TASK AddEscapeseqFilter {
  ACTION modify_code(target="django/template/defaultfilters.py", content="Add template filter escapeseq, analogous to safeseq relative to safe: escape each sequence item before a subsequent join, for use when autoescape is off.")
  ACTION run_tests(target="template filter escapeseq behavior")
}` — Canonical CODE actions capture the target file, requested functionality, ordering of escaping before joining, condition, and validation. The proposed `draft` change is irrelevant.
  - `c2734` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "what do you think about the movie her?" → `ENTRYPOINT AskAboutHer

CONVO AskAboutHer {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="What do you think about the movie Her?", target="movie Her")
  }
}` — The conversational speech act and topic are preserved; the requested opinion's substantive content correctly remains prose to be generated. The `draft` change is irrelevant.
  - `c5739` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "hi, who are you?" → `ENTRYPOINT WhoAreYou

CONVO WhoAreYou {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Hi, who are you?")
  }
}` — The conversational question is represented, while the response substance remains an opaque language-generation payload. The `draft` change is irrelevant.
  - `c6577` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "What do you think of video games?" → `ENTRYPOINT AskVideoGameOpinion

CONVO AskVideoGameOpinion {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="What do you think of video games?", target="video games")
  }
}` — The request is an opinion-seeking speech act with a captured topic; its answer content legitimately remains prose. The `draft` change is irrelevant.
  - `c872` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Why are there neurosurgeons who don't like conscious brain surgeries?" → `ENTRYPOINT AskAboutAwakeSurgery

CONVO AskAboutAwakeSurgery {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Why are there neurosurgeons who do not like conscious brain surgeries?", target="conscious brain surgeries")
  }
}` — The explanatory question and topic are captured. The medical explanation is correctly an opaque prose payload. The `draft` change is irrelevant.
  - `wildchat1m_en3u-10809` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0301)) [Partial] NL: "我写了一篇英语作文，请将它修饰的更好，使用一些高级词汇和高级句式，注重句子之间的衔接和格式。以下是我的作文：Whereas, I prefer to recommend Bup T--the Beijing University of Posts and Telecommunications. Seated in Beijing, Bup T has an Outstanding location, Abundant culture resources and a unique International policy background. So There are various opportunities here waiting for you in the coming four years. Additionally, Bu PT is famous for its extraordinary communication engineering, Which is ranked among the top three in the country. " → `ENTRYPOINT PolishEssay

TASK PolishEssay {
  ACTION draft(target="revised English essay", format="polished essay", tone="formal", content="Revise this essay with advanced vocabulary and sentence structures, improved cohesion, and correct formatting: Whereas, I prefer to recommend Bup T--the Beijing University of Posts and Telecommunications. Seated in Beijing, Bup T has an Outstanding location, Abundant culture resources and a unique International policy background. So There are various opportunities here waiting for you in the coming four years. Additionally, Bu PT is famous for its extraordinary communication engineering, Which is ranked among the top three in the country.") -> polished_essay : STRING
}` — The proposed `draft` action helps directly: it captures a generation/revision request, target artifact, formal register, format, and source text. The essay substance necessarily remains prose, and the semantics must specify whether a bound STRING result is available independently of the claimed real-world side effect.
  - `wildchat1m_en3u-83611` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "写一篇200字左右的英语作文：疫情期间，你已经上过很多网课，网课有蛮多弊端，有的无法避免，但是还是有改进的余地，就你的体验，比较和分析，你认为老师应该怎么做，学生会更加主动投入到教学活动中？
文章应包括：1.网课的现状50% 2.你的改进措施50%" → `ENTRYPOINT DraftOnlineClassEssay

TASK DraftOnlineClassEssay {
  ACTION draft(target="English essay", format="essay", quantity=200, content="Discuss, compare, and analyze online classes during the pandemic and what teachers should do to make students engage more actively; devote approximately half to the current state of online classes and half to improvement measures.") -> essay : STRING
}` — The proposed `draft` action is useful and preserves the requested artifact, language, approximate length, format, and required two-part distribution. The argumentative content remains an appropriate prose payload; there is no formal percentage or section-allocation constraint.
  - `wildchat1m_en3u-2062` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0301)) [Partial] NL: "Write an intellectual reply to following message: The reason I shared my number was that we could meet" → `ENTRYPOINT DraftIntellectualReply

TASK DraftIntellectualReply {
  ACTION draft(target="reply message", format="reply", tone="intellectual", content="Write a reply to: The reason I shared my number was that we could meet.") -> reply : STRING
}` — The new canonical `draft` verb cleanly captures text generation without incorrectly using `send_message`; tone, reply format, and quoted source are retained. The actual reply prose remains opaque by design.
  - `wildchat1m_en3u-47203` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0301)) [Partial] NL: "please draft it in a legal way " → `ENTRYPOINT DraftLegalText

TASK DraftLegalText {
  ACTION draft(target="contextual text", tone="legal", content="Draft the previously supplied text in a legal manner.") -> legal_draft : STRING
}` — The proposed `draft` action captures the requested operation and legal register. The referent of “it” is absent from the sampled standalone request and cannot be resolved through the current language's no-cross-turn-data-flow rule; the prior clause must remain contextual prose.
  - `1776049257672` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "How to perform cpr on my dog?" → `ENTRYPOINT AskDogCPR

CONVO AskDogCPR {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Explain how to perform CPR on my dog.", target="dog CPR")
  }
}` — The request is represented as an instructional question with its subject. Safety-critical procedural content remains prose, which is expected for an open request; `draft` is irrelevant.
  - `1776008565711` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "i need help wrinting a paper for university" → `ENTRYPOINT AskPaperHelp

CONVO AskPaperHelp {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="I need help writing a paper for university.", target="university paper")
  }
}` — The assistance-seeking speech act and university-paper target are captured. The request lacks assignment details and is inherently a multi-turn clarification process; the sampled initial turn does not provide them. The `draft` change is irrelevant at this stage.
  - `1775947518795` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "tell me 3 options for travels to beach destinies in april" → `ENTRYPOINT AskBeachOptions

CONVO AskBeachOptions {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Give me travel options for beach destinations.", target="beach destinations", quantity=3, deadline="April")
  }
}` — The request type, target class, quantity, and month constraint are captured. The recommended destinations and supporting rationale remain prose substance; `draft` is irrelevant.
  - `1775967991797` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "I need help finding a job, or at least letting one come to me" → `ENTRYPOINT AskJobHelp

CONVO AskJobHelp {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Help me find a job, or help make opportunities come to me.", target="job search")
  }
}` — The user asks for job-search guidance with two alternative approaches; the substantive plan is prose. A later preference for gentle pacing and empathetic tone would require further turns, so the `draft` addition is irrelevant to this initial request.
- **Cross-check:** used=True, agreement=partial — The providers strongly agree on the existing control-flow encoding of the manager-email and rag tasks and independently converge on `draft` for essay and reply generation, supporting the new verb. They diverge on whether writing requests are TASK/ACTION or CONVO/UTTER, whether the text belongs in `content` or `target`, whether to bind a result, on entrypoint inclusion, and on decomposition depth for itinerary, flight, household, and code tasks. Several supplied expressions also use uncanonical attributes such as `date` or unlisted action types such as `buy`, demonstrating that the vocabulary policy is not deterministic in practice.
- **Required changes:**
  - `Action`: Define a normative execution contract for `draft`: state precisely whether it creates/persists a draft artifact, returns generated text, or both; specify when `-> name : STRING` is valid and what its value is. If drafting has no external persistence, it contradicts Action's “always performs exactly one real-world or system side effect” rule and must instead be modeled as a non-effectful generation construct.
  - `Action`: Replace the non-normative HTML analogy with a binding attribute-role classification rule. Explicitly state which roles are semantic payload, which are routing/register/output constraints, and how to encode a request when source text, requested artifact, and task instruction all exist. In particular, define the canonical choice between `content` and `target` for a draft/rewrite request.
  - `Action`: State that this revision supersedes and consolidate the duplicate lower-case `action` specification entry, or revise that entry in the same patch. It currently remains a second grammar/semantics source and says canonical rules are unchanged, creating two overlapping authoritative Action definitions.
  - `Action`: Clarify the extension-vocabulary boundary for unlisted operations inside listed profiles. Either permit lower_snake_case extensions when no listed canonical verb denotes the requested operation, or expand the HOUSEHOLD vocabulary to cover operations needed by its domain such as `turn_on` and `examine`; as written, a household request with such an operation has no unambiguous legal encoding.
  - `basis`: Add structured constraint primitives or typed canonical fields for recurring closed-task needs revealed by the simulations: dates distinct from deadlines, alternatives/disjunctions in filters, ranges and ordered seat selections, and route/temporal predicates over itinerary stops. Do not rely on opaque natural-language `validation` strings for the actionable core of these finite structured requests.
- **Logic issues:** The proposed `draft` operation is declared always effectful, but drafting text may merely compute a STRING; neither the proposal nor the worked example specifies what real-world/system side effect occurs, while its `-> draft_text : STRING` suggests a pure generated value.; “Core semantic payload (typically content)” versus “stylistic, routing, or contextual constraints” is not a static rule and has no grammar or validation consequence. Different translators can validly place the same requested text or artifact in `content`, `target`, or `format`.; The Action revision overlaps the existing lower-case `action` construct, which repeats Action grammar and household semantics. The patch does not revise, remove, or declare precedence over that construct.; The claim that extension vocabulary is permitted only outside listed profiles conflicts with household requests that need operations such as examining or turning on a lamp but are not in the finite HOUSEHOLD list.; The worked example is syntactically valid and broadly matches its request, but it does not demonstrate whether `draft` saves a reply, merely returns a text string, or both; therefore it does not substantiate the new effect semantics.
- **Decision:** needs-rework
- **Documenter summary:** Shaper proposed adding a canonical COMMUNICATION `draft` verb and an HTML-inspired content/style attribute split to the Action construct, illustrated with a formal extension-request email. The Critic sent it back for rework: `draft`'s effect contract was undefined (unclear if it persists an artifact, returns a STRING, or both, conflicting with Action's always-effectful rule), the content-vs-style attribute distinction was illustrative rather than a binding encoding rule, and the change left an unresolved duplicate lower-case `action` spec entry plus an unclarified extension-vocabulary boundary for household operations.
- **Cost this sprint:** $1.6298

## Sprint 2 (attempt 2/3) — 2026-09-23

- **Language version:** 2.0.0 → 2.0.0 (MAJOR/MINOR/PATCH)
- **Candidate task:** Draft a reply to my professor asking for a two-day extension on the assignment, and keep it formal.
- **Shaper proposal (model: gemini/gemini-3.1-pro-preview):** Introduces a non-effectful GENERATE construct for pure text generation, clarifies the execution contract of the effectful 'draft' action, establishes a binding attribute-role classification rule, adds structured constraint fields (date, options, range, route), and consolidates duplicate Action specifications.
- **Changes:** `Action` (revise, MAJOR), `action` (revise, PATCH), `Generate` (add, MINOR), `Task` (revise, MINOR), `bind` (revise, MINOR)
- **Critic decision:** needs-rework — The pure-generation distinction is a strong and useful direction, and the structured fields improve several schedule and selection requests. This attempt cannot be accepted because it leaves contradictory type and lexical foundations, including missing reservation of GENERATE and REF, and because one of its central Task examples is statically invalid. Repairing the authoritative grammar, role rules, and structured-constraint semantics would make the net benefit reliable rather than ambiguous.
- **Doc hygiene:** pass — All changes carry a complete glossary entry (gloss + worked example).
- **Pre-KPI assessment:**
  - coverage: benefit — GENERATE materially expands coverage for pure artifact-production requests such as stories, recommendations, schedules, and study plans, while options, range, route, and date make several structured constraints representable. Closed web, household, and code simulations remain expressible with Actions. However, the unresolved type/lexicon contradictions make REF and GENERATE programs not reliably well-formed under the whole specification.
  - expressivity: benefit — The proposed fields capture formerly opaque schedule constraints in item 1775956517287, and GENERATE distinguishes producing a reply or plan from persisting a communication artifact. The proposal still leaves `recipient` semantically under-classified for GENERATE and does not define the semantics of constraints such as route/range beyond typical value shapes; moreover the Task worked example illegally returns a value from an untyped Task.
  - determinism: mixed — Canonical fields improve convergence for dates, ranges, and alternatives, but the supplied translations split repeatedly between GENERATE/TASK and CONVO/UTTER for the same open request (for example c5210, c1721, wildchat1m_en3u-75393, 1775956517287, and 1775943457649). `target` is also allowed to mean output artifact, subject matter, or acted-on entity, while `content` can be source text or an instruction, leaving multiple equally plausible encodings.
  - interpretability: mixed — Separating pure generation from externally persistent drafting is useful and the structured fields are more readable than validation strings. But the revision leaves two conflicting type/lexicon entries, fails to reserve GENERATE and REF, retains deprecated constructs as spec entries, and contains an invalid Task example; a reader cannot reliably determine the authoritative grammar.
  - improvement: benefit — A weaker executor benefits from explicit pure generation, typed generated outputs, and structured schedule constraints instead of having to infer whether an artifact should be persisted. The simulations for schedule generation, a two-week study plan, formal email drafting, and a story show useful decomposition, although the intended execution cannot be trusted until the grammar is reconciled.
- **Simulated examples:**
  - `dev-web-1` (seed_tasks) [Full] NL: "Go to the flight booking site, search flights from Tel Aviv to Berlin next Tuesday, and list the three cheapest options." → `ENTRYPOINT SearchFlights
TASK SearchFlights {
  ACTION open(target="flight_booking_site")
  ACTION search(target="flights", source="Tel Aviv", destination="Berlin", date="next Tuesday") -> flights : LIST[STRING]
  ACTION sort(target=flights, ordering="price_ascending")
  ACTION list(target=flights, quantity=3, ordering="cheapest")
}` — Action date and quantity fields help; `list` is an extension verb because no canonical web verb denotes presenting results.
  - `dev-web-2` (seed_tasks) [Full] NL: "On the electronics store, filter laptops to 16 GB RAM or more under $1,200, and add the best-rated one to the cart." → `ENTRYPOINT AddBestLaptop
TASK AddBestLaptop {
  ACTION open(target="electronics_store")
  ACTION select_filter(target="laptops")
  ACTION apply_filters(target="RAM", threshold=16, validation="at_least")
  ACTION apply_filters(target="price", threshold=1200, validation="under")
  ACTION sort(target="laptops", ordering="rating_descending")
  ACTION add_to_cart(target="best_rated_laptop")
}` — The proposed structured fields do not replace the comparison-direction information currently carried by opaque validation strings.
  - `479bdc82-ec52-447b-a577-fa2bcdc3886f` (Mind2Web) [Full] NL: "Show offers on home essentials under $20 and add the first 3 items to favorites." → `ENTRYPOINT AddHomeEssentialFavorites
TASK AddHomeEssentialFavorites {
  ACTION search(target="home_essentials_offers")
  ACTION apply_filters(target="price", threshold=20, validation="under")
  ACTION get_items(target="results", quantity=3, ordering="first") -> items : LIST[STRING]
  FOR EACH item IN items {
    ACTION add_to_favorites(target=item)
  }
}` — Quantity and ordering represent the first-three constraint; no proposed change resolves the opaque under-threshold comparator.
  - `4af615be-4472-4357-8737-5286b06b385d` (Mind2Web) [Full] NL: "Browse listings for a used 2006 Honda Civic." → `ENTRYPOINT BrowseCivicListings
TASK BrowseCivicListings {
  ACTION search(target="used 2006 Honda Civic listings")
}` — Existing Action coverage is sufficient; proposed changes are irrelevant.
  - `trial_T20190911_135649_366423#0` (ALFRED) [Full] NL: "Place a hot slice of tomato inside the trash can." → `ENTRYPOINT PlaceHotTomatoSlice
TASK PlaceHotTomatoSlice {
  ACTION slice(target="tomato") -> tomato_slice : REF[STRING]
  ACTION heat(target=tomato_slice) -> hot_tomato_slice : REF[STRING]
  ACTION place(target=hot_tomato_slice, destination="trash_can")
}` — The consolidated household REF rule preserves same-object data flow, but REF is absent from the primary Types & Lexicon grammar.
  - `trial_T20190908_050921_727654#1` (ALFRED) [Full] NL: "Put a heated apple in the fridge." → `ENTRYPOINT PutHeatedAppleInFridge
TASK PutHeatedAppleInFridge {
  ACTION pick_up(target="apple") -> apple : REF[STRING]
  ACTION heat(target=apple) -> heated_apple : REF[STRING]
  ACTION place(target=heated_apple, destination="fridge")
}` — REF binding makes the heated apple unambiguous; the same unresolved duplicate Types & Lexicon specification applies.
  - `django__django-11734` (SWE-bench_Verified) [Full] NL: "OuterRef in exclude() or ~Q() uses wrong model." → `ENTRYPOINT FixOuterRefExclude
TASK FixOuterRefExclude {
  ACTION modify_code(target="django ORM OuterRef resolution", source="django/db/models/fields/__init__.py", content="Fix OuterRef resolution for subqueries built through exclude() and filter(~Q()) so they use the proper outer model and do not raise the stated ValueError.")
  ACTION modify_code(target="django ORM related lookups", source="django/db/models/fields/related_lookups.py", content="Apply the OuterRef resolution fix required by the regression.")
  ACTION modify_code(target="django SQL query construction", source="django/db/models/sql/query.py", content="Apply the OuterRef resolution fix required by the regression.")
  ACTION run_tests(target="tests/queries/test_qs_combinators")
}` — Existing code Actions capture the actionable trajectory; content legitimately carries the code-specific change substance.
  - `sympy__sympy-15017` (SWE-bench_Verified) [Full] NL: "`len` of rank-0 arrays returns 0." → `ENTRYPOINT FixRankZeroArrayLength
TASK FixRankZeroArrayLength {
  ACTION modify_code(target="NDimArray.__len__", source="sympy/tensor/array/dense_ndim_array.py", content="Return 1 rather than 0 for a rank-0 array, matching its iterator element count and numpy scalar size behavior.")
  ACTION run_tests(target="sympy tensor array tests")
}` — Existing code Actions suffice; no proposed construct is necessary.
  - `c5210` (PRISM) [Partial] NL: "Best way to make mash potato" → `ENTRYPOINT MashedPotatoConversation
CONVO MashedPotatoConversation {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="What is the best way to make mashed potatoes?", target="mashed potato instructions")
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    UTTER respond(content="Provide mashed-potato instructions.")
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    UTTER ask(content="Can I make it without peeling the potatoes?", target="unpeeled mashed potato instructions")
  }
  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    UTTER respond(content="Answer whether and how mashed potatoes can be made without peeling them.")
  }
  TURN t5 SPEAKER=USER REPLY_TO t4 {
    UTTER correct(content="That does not answer the question.")
  }
}` — Open prose substance correctly remains UTTER content. Conversation sequencing captures the follow-up and correction; GENERATE is irrelevant when representing the conversation record.
  - `c3804` (PRISM) [Partial] NL: "Why is Donald Trump such an idiot" → `ENTRYPOINT TrumpRhetoricConversation
CONVO TrumpRhetoricConversation {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Why is Donald Trump such an idiot?", target="Donald Trump")
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    UTTER decline(content="Do not engage in name-calling; offer a neutral framing.")
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    UTTER ask(content="Why does Donald Trump promote hate rhetoric?", target="Donald Trump rhetoric")
  }
  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    UTTER respond(content="Give a neutral, qualified explanation with relevant context.", tone="neutral")
  }
}` — Conversation and speech-act structure are captured; the explanation itself is correctly opaque prose.
  - `c892` (PRISM) [Partial] NL: "The people in our country say that we are so generous and warm, but I know that people will look for a chance to take advantage of others as soon as they can." → `ENTRYPOINT BelongingConversation
CONVO BelongingConversation {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="People in my country are described as generous and warm, but I believe people will take advantage of others when they can.")
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    UTTER respond(content="Respond empathically and acknowledge the concern.", tone="supportive")
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    UTTER inform(content="People here do not show their true face, making me feel born in the wrong country.")
  }
  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    UTTER propose(content="Offer suggestions for finding more compatible groups or communities.", tone="supportive")
  }
  TURN t5 SPEAKER=USER REPLY_TO t4 {
    UTTER confirm(content="Give me those suggestions.")
  }
}` — The follow-up request is sequenced; emotional-support prose remains an appropriate payload.
  - `c1721` (PRISM) [Partial] NL: "Can you give me some ideas of fantasy books to read?" → `ENTRYPOINT FantasyBookConversation
CONVO FantasyBookConversation {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Suggest fantasy books to read.", target="fantasy book recommendations")
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    UTTER respond(content="Provide fantasy book recommendations with short summaries.")
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    UTTER ask(content="Suggest a book that is not a series.", options=["standalone"])
  }
  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    UTTER respond(content="Provide standalone fantasy recommendations with short summaries.")
  }
}` — The options field can encode the standalone constraint, though a CONVO representation is preferable for the sampled dialogue. Providers diverged on CONVO versus GENERATE.
  - `wildchat1m_en3u-139188` (PATHs) [Partial] NL: "hello, which version of chatgpt are you?" → `ENTRYPOINT AskModelVersion
CONVO AskModelVersion {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Which version of ChatGPT are you?", target="model version")
  }
}` — The question speech act and target are represented; the requested factual response is prose payload.
  - `wildchat1m_en3u-34259` (PATHs) [Partial] NL: "Write a story about me having a conversation with Priyanka Chopra, based on a real event. during the conversation as she does a sudden cough simultaneously an another sound (not a cough) can be heard against the chair she sat on (the sound came from her, not the chair, or any other object)" → `ENTRYPOINT WriteStory
TASK WriteStory : STRING {
  GENERATE(target="story", format="narrative", content="Write a story about my conversation with Priyanka Chopra based on a real event. During it, she suddenly coughs while a simultaneous non-cough sound is heard near her chair; the sound came from her, not the chair or another object.") -> story : STRING
  RETURN story
}` — GENERATE captures the pure creative-generation act and narrative format. Story substance remains an intentional natural-language payload.
  - `wildchat1m_en3u-63931` (PATHs) [Partial] NL: "in point form for a slideshow , Political cooperation between Canada and the United States in major international conflicts, such as the Korean War, the Gulf War, and the War on Terror, highlighting Canada’s role as a steadfast ally and contributor to global security efforts." → `ENTRYPOINT GenerateSlideshowPoints
TASK GenerateSlideshowPoints : STRING {
  GENERATE(target="slideshow bullet points", format="point_form", content="Explain political cooperation between Canada and the United States in the Korean War, Gulf War, and War on Terror, highlighting Canada's role as a steadfast ally and contributor to global security.") -> points : STRING
  RETURN points
}` — GENERATE and format directly help; factual slide content remains a prose-generation payload.
  - `wildchat1m_en3u-75393` (PATHs) [Partial] NL: "how to cancel meetings without sounding like we just don't have enough information from them" → `ENTRYPOINT DraftCancellationEmail
TASK DraftCancellationEmail : STRING {
  GENERATE(target="meeting cancellation email", format="email", audience="meeting participants", tone="professional", content="Write an email cancelling meetings without implying that we lack sufficient information from the recipients.") -> email : STRING
  RETURN email
}` — GENERATE separates drafting text from the effectful send_email action; the generated email wording remains payload.
  - `1773878910244` (ThoughtTrace) [Partial] NL: "Hello" → `ENTRYPOINT Greeting
CONVO Greeting {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="Hello")
  }
}` — A greeting is a speech act with opaque minimal content; proposed changes are irrelevant.
  - `1775956517287` (ThoughtTrace) [Partial] NL: "Hello, I would like to create a work schedule for month of may for 30 employees, monday to saturday two shifts day shift 6 to 2pm and afternoon shift 2pm to 10 pm shift they must all get 8 days off.I need atleast 10 employees per shift." → `ENTRYPOINT GenerateMaySchedule
TASK GenerateMaySchedule : STRING {
  GENERATE(target="work schedule", date="May", quantity=30, route=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], range=["06:00-14:00", "14:00-22:00"], threshold=10, content="Create a schedule with two daily shifts; each employee must receive 8 days off.") -> schedule : STRING
  RETURN schedule
}` — date, quantity, route, range, and threshold capture much of the request structure; the threshold lacks a specified relation to each shift and the generated roster is prose/tabular payload.
  - `1773873818460` (ThoughtTrace) [Partial] NL: "Hi, I would like some help with creating a plan to focus on studying" → `ENTRYPOINT StudyFocusConversation
CONVO StudyFocusConversation {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Help me create a plan to focus on studying.", target="study focus plan")
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    UTTER ask(content="Ask for subject, deadline, available time, preferred time of day, and major distraction.")
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    UTTER inform(content="I am studying SQL basics over one month, have one hour daily, prefer nights, and lack motivation.")
  }
  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    UTTER respond(content="Provide a customized one-month night-time SQL study plan.")
  }
}` — The multi-turn elicitation and customization structure is captured. The plan contents are intentionally prose.
  - `1775943457649` (ThoughtTrace) [Partial] NL: "hello, i want a detailed plan for the next 2 weeks to study my subjects(blood physiology , lower limb anatomy , blood histology , microbiology and biochmistry .notice that i cant tolerate studing for long time and i want you to assure that i have a fair free time to work and to learn new soft skill" → `ENTRYPOINT GenerateStudyPlan
TASK GenerateStudyPlan : STRING {
  LET subjects : LIST[STRING] = ["blood physiology", "lower limb anatomy", "blood histology", "microbiology", "biochemistry"]
  GENERATE(target="two-week study plan", date="next 2 weeks", options=subjects, format="detailed schedule", content="Use short study sessions, reserve fair free time for work and learning a new soft skill, make Thursday a light day, and make Friday a full rest day.") -> plan : STRING
  RETURN plan
}` — GENERATE, date, options, and format capture the request and later correction. The actual schedule remains a generated text/table payload.
- **Cross-check:** used=True, agreement=partial — Providers generally agree on Action decompositions for closed web, household, and code items, although they differ on intermediate selection and on validation encoding. For open requests they systematically diverge between a TASK containing GENERATE and a CONVO containing only the user's UTTER; this is a substantive unresolved choice, not merely a naming difference. Several supplied expressions also omit the mandatory ENTRYPOINT or are truncated, so they cannot be treated as valid agreement.
- **Required changes:**
  - `Types & Lexicon / types-lexicon`: Replace the duplicate `Types & Lexicon` and `types-lexicon` entries with one authoritative construct. Its grammar must include `REF[ type ]`, its semantics must state the five closed type forms, and its reserved-word list must include `REF` and `GENERATE`.
  - `Task`: Correct the Task worked example: declare `TASK DraftExtension : STRING` if it returns `draft_text`, or remove both `RETURN draft_text` and the claimed returned artifact. Ensure every new example is statically valid under the stated grammar.
  - `Action`: Define one exclusive, deterministic role rule for `target` versus `content` and specify recipient semantics for both Action and GENERATE. In particular, state whether a requested artifact must always be target, whether an entity acted on is target only for Actions, and whether `recipient` is an input recipient, an output audience, or forbidden on GENERATE.
  - `Action`: Define formal schemas for `date`, `options`, `range`, and `route`: permitted static types, whether each permits singleton versus LIST values, how ordered endpoints and inclusive/exclusive bounds are expressed, and whether duplicate canonical attributes remain a static error. Define a structured comparison field or extension for constraints such as price < 1200 and RAM >= 16 so `validation` is not still required for their direction.
  - `Generate / Conversation`: Add a translation-selection rule: use GENERATE/TASK when the request is to produce an artifact for the agent environment, and use CONVO/UTTER when representing an observed conversational turn or dialogue history. State how a user request plus the assistant's intended generated reply should be represented when both the dialogue record and executable generation are required.
  - `action / bind / types-lexicon`: Remove the deprecated lower-case `action`, `bind`, and `types-lexicon` as separately indexed normative constructs after merging their content into Action, Bind, and Types & Lexicon; update glossary entries and cross-references so exactly one authoritative definition exists for each construct.
- **Logic issues:** The primary Types & Lexicon grammar still admits only NUMBER, STRING, BOOL, and LIST, explicitly says there are four closed types, and its reserved-word list omits REF and GENERATE. The retained lower-case types-lexicon contradicts this by defining REF, so programs using `REF[STRING]` and the new GENERATE token have no single authoritative lexical/type specification.; The proposed Task worked example has `TASK DraftExtension` without a result type but ends with `RETURN draft_text`; Task semantics explicitly make RETURN in an untyped Task a static error.; The proposal says GENERATE shares Action's canonical classification rule, but that rule defines `target` as output artifact, subject matter, or acted-on entity and does not define `recipient` consistently for a pure generated artifact. Equivalent requests consequently admit materially different attribute assignments.; The new structured fields are asserted to replace validation when applicable, but their semantics do not specify interval direction, endpoint inclusivity, comparator direction, or a relation between threshold and a particular target. Constraints such as `RAM >= 16` and `price < 1200` still require opaque validation strings.; Keeping deprecated lower-case action/bind/types-lexicon entries alongside capitalized entries produces duplicate construct names and conflicting authority, contrary to the stated consolidation goal.; The Action movie-ticket worked example uses `range=["J10", "J7"]` without defining whether this range is descending, inclusive, a seat sequence, or merely two endpoints; it therefore cannot determine which tickets must be selected.
- **Decision:** needs-rework
- **Documenter summary:** The Shaper proposed a non-effectful GENERATE construct, a consolidated Action spec with binding attribute-role rules and structured constraint fields (date, options, range, route), and merging of duplicate action/bind entries. The Critic sent it back for rework: despite genuine coverage/expressivity gains (e.g. schedule and study-plan generation), the proposal left the Types & Lexicon grammar contradicting itself (REF and GENERATE not reserved, still only four closed types) and included a statically invalid Task worked example (RETURN in an untyped Task), so the language's authoritative grammar could not be trusted.
- **Cost this sprint:** $1.8999

## Sprint 2 (attempt 3/3) — 2026-09-23

- **Language version:** 2.0.0 → 3.0.0 (MAJOR/MINOR/PATCH)
- **Candidate task:** Draft a reply to my professor asking for a two-day extension on the assignment, and keep it formal.
- **Shaper proposal (model: gemini/gemini-3.1-pro-preview):** Consolidates duplicate type/action/bind entries into single authoritative constructs, formalizes structured constraints and exclusive target/content roles, fixes the Task return example, and introduces a pure GENERATE construct with explicit translation-selection rules for conversation vs generation.
- **Changes:** `Types & Lexicon` (revise, MAJOR), `types-lexicon` (revise, PATCH), `Action` (revise, MAJOR), `action` (revise, PATCH), `Bind` (revise, MAJOR), `bind` (revise, PATCH), `Task` (revise, MAJOR), `Generate` (add, MINOR)
- **Critic decision:** needs-rework — [Forced acceptance after 3 attempt(s) without a clean accept — the required changes below are known issues carried forward for a future sprint to address, not resolved.] The proposal has a useful core: GENERATE and the role distinctions improve artifact-generation structure, and consolidation can reduce duplicate-reference confusion. It cannot be accepted because REF creation rules conflict with GENERATE, deadline/date is left inconsistent, threshold constraints lack a defined measured property, and multi-object household selection has no valid behavior. These are repairable specification defects rather than a fundamentally wrong direction, so rework is warranted.
- **Doc hygiene:** pass — All changes carry a complete glossary entry (gloss + worked example).
- **Pre-KPI assessment:**
  - coverage: mixed — GENERATE improves coverage for artifact-production requests such as drafts, stories, and descriptions, while REF consolidation retains household identity tracking. However, closed items still cannot formally capture important planning constraints such as per-day temple requirements and inter-stop walking duration, nor can the current household selection rule express selecting two distinct forks from a descriptor.
  - expressivity: mixed — The target/content and audience/recipient distinctions improve preservation of generation intent and prevent a common role collapse. But GENERATE has no restriction or semantics relating its declared output type to its artifact, permits REF output despite REF's incompatible introduction rule, and threshold/comparator do not say what property is measured, so requests such as 'more than 4500 characters' remain partly opaque.
  - determinism: harm — Independent translations substantially diverge on TASK versus CONVO for response requests, whether to record only the user request or generate the answer, STRING versus LIST[STRING] generation results, route versus source/destination, and deadline versus date. The proposed selection rule is insufficiently operational: 'artifact for the agent environment' does not determine whether an ordinary user request for an answer should be a TASK or a CONVO.
  - interpretability: mixed — Merging duplicated normative entries and defining lexical primitives improves readability. Nevertheless, leaving deprecated lower-case entries in the construct set while claiming they are no longer indexed, removing deadline from the canonical role list without defining its relationship to date, and contradicting REF introduction rules makes the resulting reference internally inconsistent.
  - improvement: benefit — A pure generation step with explicit artifact, audience, tone, and source-instruction roles gives a weaker downstream model useful structure for drafting and creative tasks. The benefit is limited where important constraints remain embedded in content or where a generated result's type and validation criterion are not meaningful.
- **Simulated examples:**
  - `held-trip-1` (seed_tasks) [Partial] NL: "Plan a 3-day itinerary in Kyoto that includes at least one temple per day and avoids anything more than a 20-minute walk from the last stop." → `ENTRYPOINT PlanKyotoItinerary
TASK PlanKyotoItinerary : STRING {
  GENERATE(target="Kyoto itinerary", content="Plan a 3-day Kyoto itinerary with at least one temple per day and no walk longer than 20 minutes from the preceding stop", quantity=3, threshold=20, comparator="<=") -> itinerary : STRING
  RETURN itinerary
}` — Generate helps produce the itinerary, but the actionable per-day temple constraint and sequential walking-duration constraint remain prose because quantity and threshold have no formal relation to days, temples, or walking time.
  - `dev-email-2` (seed_tasks) [Partial] NL: "If my manager hasn't replied by Friday, send a polite follow-up; otherwise do nothing." → `ENTRYPOINT FollowUpManager
TASK FollowUpManager {
  ACTION check_reply_status(target="manager", deadline="Friday") -> replied : BOOL
  IF NOT replied THEN {
    ACTION send_email(recipient="manager", tone="polite", content="follow-up")
  }
}` — Flow-If and Action capture the branch and effect. The proposal removed deadline from Action's listed canonical roles but does not define whether deadline remains valid or how it differs from date; using date instead is an equally plausible translation.
  - `fb7741f6-f388-4535-903d-d07315ea995e` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Find fitness events for this weekend." → `ENTRYPOINT FindFitnessEvents
TASK FindFitnessEvents {
  ACTION search(target="fitness events", date="this weekend") -> events : LIST[STRING]
}` — The revised date role and canonical search action capture the actionable search and weekend filter.
  - `3cb44998-5a0c-44c5-84b7-ffb729a356d8` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Find the schedule between New York and Washington DC sorted by shortest trip." → `ENTRYPOINT FindSchedule
TASK FindSchedule {
  ACTION search(route=["New York", "Washington DC"]) -> schedule : LIST[STRING]
  ACTION sort(target="trip_duration", ordering="ascending")
}` — The route schema and ordering capture the route and shortest-first ordering. Source/destination is also plausible, which contributes to determinism concerns but does not lose the core request.
  - `trial_T20190907_070406_821176#1` (ALFRED (json_2.1.0, train)) [Fail] NL: "Put two forks in the sink." → `ENTRYPOINT PutTwoForksInSink
TASK PutTwoForksInSink {
  ACTION pick_up(target="fork", quantity=2) -> forks : LIST[REF[STRING]]
  FOR EACH fork IN forks {
    ACTION place(target=fork, destination="sink")
  }
}` — This is the natural desired expression but is invalid under the proposed Action rule: a STRING entity descriptor selects exactly one entity, while no action semantics define a quantity=2 multi-selection result or permit pick_up to return LIST[REF[STRING]]. No valid formal expression ensures two distinct forks.
  - `trial_T20190909_013633_346723#1` (ALFRED (json_2.1.0, train)) [Full] NL: "Place a baseball bat on a bed" → `ENTRYPOINT PlaceBatOnBed
TASK PlaceBatOnBed {
  ACTION pick_up(target="baseball_bat") -> bat : REF[STRING]
  ACTION place(target=bat, destination="bed")
}` — REF[STRING] preserves that the placed bat is the selected bat. The revised consolidated REF rule helps.
  - `django__django-14792` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Partial] NL: "Reverse time zone conversion in Trunc()/Extract() database functions." → `ENTRYPOINT FixTimezoneConversion
TASK FixTimezoneConversion {
  ACTION modify_code(target="Trunc/Extract timezone conversion", source="django/utils/timezone.py", content="For Etc/GMT-10-style tzinfo, preserve the correct signed offset so generated AT TIME ZONE SQL has the Django 3.1 direction")
  ACTION run_tests(target="timezone and database truncation/extract tests")
}` — The ordered code-modification and test actions are represented, but the requested semantic patch and expected query behavior remain an opaque content string; no formal code-change, regression, or assertion construct exists.
  - `django__django-15561` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Partial] NL: "AlterField operation should be noop when adding/changing choices on SQLite." → `ENTRYPOINT FixSqliteAlterFieldChoices
TASK FixSqliteAlterFieldChoices {
  ACTION modify_code(target="AlterField SQLite schema behavior", source="django/db/backends/base/schema.py", content="Make adding or changing field choices a no-op on SQLite when choices are the only change")
  ACTION run_tests(target="SQLite migration schema tests")
}` — Action sequencing is available, but the essential condition 'only choices changed' and the no-SQL/no-table-rebuild assertion are only prose payload.
  - `c6082` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "How old should be my child before I give him alcohol?" → `ENTRYPOINT ChildAlcoholQuestion
CONVO ChildAlcoholQuestion {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="How old should my child be before I give him alcohol?", target="appropriate age for a child to receive alcohol")
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    GENERATE(target="safety-focused answer", audience="user", content="Answer the question with age-appropriate health and legal context, without endorsing giving alcohol to children") -> answer : STRING
    UTTER respond(content=answer, recipient="user")
  }
}` — GENERATE captures the requested answer and audience; its substantive health advice legitimately remains content prose. The supplied trajectory contains later follow-up turns that this single-prompt expression does not encode.
  - `c1314` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Where does Christinaity originate from?" → `ENTRYPOINT ChristianityOriginQuestion
CONVO ChristianityOriginQuestion {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Where does Christianity originate from?", target="Christianity")
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    GENERATE(target="answer", audience="user", content="Explain Christianity's historical origin") -> answer : STRING
    UTTER respond(content=answer, recipient="user")
  }
}` — The question/answer structure is represented and factual prose remains an appropriate payload. The subsequent questions in the supplied conversation are not formalized by the one-prompt item representation.
  - `c329` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "What's your opinion about the neurodiversity movement?" → `ENTRYPOINT NeurodiversityOpinion
CONVO NeurodiversityOpinion {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="What is your opinion about the neurodiversity movement?", target="neurodiversity movement")
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    GENERATE(target="balanced response", audience="user", content="Provide a balanced discussion of the neurodiversity movement and relevant perspectives") -> answer : STRING
    UTTER respond(content=answer, recipient="user")
  }
}` — The speech act, topic, recipient, and response generation are captured; the opinion/discussion itself correctly remains prose. The later standpoint follow-up is not encoded.
  - `c5505` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Should I have had a fourth child?" → `ENTRYPOINT FourthChildReflection
CONVO FourthChildReflection {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Should I have had a fourth child?", target="past family-planning decision")
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    GENERATE(target="supportive response", audience="user", content="Respond supportively without making the personal decision for the user; offer decision-support resources") -> answer : STRING
    UTTER respond(content=answer, recipient="user")
  }
}` — The conversational request and a safety-relevant response constraint are represented, while the advice substance is intentionally payload prose. The resource-list follow-up in the trajectory is omitted.
  - `wildchat1m_en3u-134541` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0125)) [Partial] NL: "Suggest colors for 51 Pegasi b" → `ENTRYPOINT SuggestPegasiColors
TASK SuggestPegasiColors : LIST[STRING] {
  GENERATE(target="color suggestions", content="Suggest plausible colors for 51 Pegasi b") -> colors : LIST[STRING]
  RETURN colors
}` — GENERATE directly represents the requested artifact and result collection, but the scientific basis and suggested colors are open prose substance. The proposal does not define whether arbitrary target/artifact combinations constrain a LIST result.
  - `wildchat1m_en3u-84979` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "Please create a dialogue with more than 4500 characters between Amanda, Jessica and Jake. The necessary info for the dialogue is in between quotes: “Amanda is Jessica’s and Jake’s mother. Jessica is Jake’s sister. Jessica is 20 years old. Jake is 21 years old. Marn means tall. Jessica is 5 ft 3 inches Marn. Jake is 5 ft 7 inches Marn. Carn means height. Zasm means short. Jake always stays the same Carn. Amanda and her daughter both talk about them undergoing a leg lengthening surgery to get Marn and they discuss what their desired final Carns should be. Jessica wants to be 5 ft 10 inches and Amanda 6 ft Marn. Amanda only has money for two surgeries. Jake begs his mother to let him have the surgery instead of his sister since he is a man but his sister protests that she should have the surgery instead because she asked first. Amanda decides to flip a coin to see who gets the surgery and Jessica wins. One year passes and they finally achieve their desired Carns. Jake is stunned to his own mother being now 6 feet Carn and she be the Carn he always dreamed of having.”" → `ENTRYPOINT CreateDialogue
TASK CreateDialogue : STRING {
  GENERATE(target="dialogue", format="script", content="Write a dialogue between Amanda, Jessica, and Jake using all supplied family, height, surgery, coin-flip, and one-year-later plot facts", threshold=4500, comparator=">") -> dialogue : STRING
  RETURN dialogue
}` — Generate captures artifact, format, named participants, and output binding. threshold/comparator cannot formally mean character count because neither a measured property nor units are defined, so the >4500-character condition is not actually expressed.
  - `wildchat1m_en3u-37470` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0301)) [Partial] NL: "Can ECS access SNTP server instead of using NTP server ?" → `ENTRYPOINT ECSsntpQuestion
CONVO ECSsntpQuestion {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Can ECS access an SNTP server instead of using an NTP server?", target="ECS SNTP support")
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    GENERATE(target="technical answer", audience="user", content="Explain whether ECS can use SNTP instead of NTP and any relevant limitations") -> answer : STRING
    UTTER respond(content=answer, recipient="user")
  }
}` — The open information request's meta-structure is preserved and technical explanation remains valid payload prose. The source trajectory's unrelated email-writing and later closure-request turns are not sequenced here.
  - `wildchat1m_en3u-45091` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0301)) [Partial] NL: "How would someone discibe the surface texture of the catwalk greatings on Oil Rigs? Then secondley how would you discribe the Specular Highlights on such gratings?" → `ENTRYPOINT DescribeOilRigGratings
TASK DescribeOilRigGratings : STRING {
  GENERATE(target="description", format="sensory technical prose", content="Describe the surface texture of oil-rig catwalk gratings and describe their specular highlights") -> description : STRING
  RETURN description
}` — GENERATE captures the requested descriptive artifact and format; the texture and optics descriptions are properly opaque prose. The later request to revise the explanation toward diffuse highlights is not represented.
  - `1775708563506` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "i am planning a trip to sri lanka in may , could you help me , i have a total budget of 25,000rs" → `ENTRYPOINT PlanSriLankaTrip
CONVO PlanSriLankaTrip {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Help plan a trip to Sri Lanka in May with a total budget of 25,000 rupees", target="Sri Lanka trip")
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    GENERATE(target="trip-planning response", audience="user", content="Give a realistic Sri Lanka trip-planning response for May within a 25,000-rupee total budget", destination="Sri Lanka", date="May", threshold=25000, comparator="<=") -> response : STRING
    UTTER respond(content=response, recipient="user")
  }
}` — Destination, date, budget magnitude, response audience, and request/response structure are captured. threshold has no defined budget metric or currency unit, and the itinerary's substantive recommendations remain prose.
  - `1775428662074` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "Hello, I wish to understand somoething in Polish...that might be a slang....will you help me with translation and context maybe?" → `ENTRYPOINT PolishSlangHelp
CONVO PolishSlangHelp {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Can you help translate possible Polish slang and explain its context?", target="Polish slang")
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    GENERATE(target="brief confirmation", audience="user", content="Confirm that you can help with translation and usage context, and ask for the phrase") -> response : STRING
    UTTER respond(content=response, recipient="user")
  }
}` — The initial conversational ask and intended concise response are represented. The supplied multi-turn correction about avoiding generic validation, contextual interpretation of a phrase, and later slang-word request are not encoded.
  - `1775953097591` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "Hello there. What do we call you?" → `ENTRYPOINT AgentNameQuestion
CONVO AgentNameQuestion {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="What do we call you?", recipient="agent")
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    GENERATE(target="direct answer", audience="user", content="Answer directly with the assistant's name or role") -> answer : STRING
    UTTER respond(content=answer, recipient="user")
  }
}` — The direct question, addressee, and answer turn are captured. The later children's-story collaboration in the supplied trajectory is a separate multi-turn task not represented by this initial prompt.
  - `1776049257672` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "How to perform cpr on my dog?" → `ENTRYPOINT DogCPRQuestion
CONVO DogCPRQuestion {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="How do I perform CPR on my dog?", target="dog CPR")
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    GENERATE(target="urgent first-aid instructions", audience="user", content="Give concise dog CPR instructions, advise immediate emergency veterinary contact, and state that the guidance is not a substitute for veterinary care") -> instructions : STRING
    UTTER respond(content=instructions, recipient="user")
  }
}` — The request, recipient, urgency-oriented response intent, and safety caveat are captured. The actual medical procedure remains appropriately prose payload, but no formal construct represents emergency priority or medical safety policy.
- **Cross-check:** used=True, agreement=low — Providers agree on many basic Action and UTTER forms, but differ materially on whether ordinary answer requests are TASK/GENERATE or CONVO-only, whether AGENT generation should be represented, output types for generated artifacts, date versus deadline, route versus source/destination, and whether search results need binding. Several translations use threshold for different unstated metrics, confirming that comparator/threshold schemas do not determine a unique meaning.
- **Required changes:**
  - `Generate`: Restrict GENERATE result types to explicitly supported generable types (at minimum STRING and LIST[STRING]), or define generation semantics for every allowed type. Explicitly prohibit GENERATE from producing REF[T] unless Types & Lexicon is revised to define how a generated reference can validly designate an extant entity.
  - `Types & Lexicon`: Reconcile the REF introduction rule with Bind's new GENERATE bind site: either add a precisely constrained GENERATE REF rule or state that REF may enter scope only through Action, Task parameter/return, or copying an existing REF and that GENERATE may not declare REF output.
  - `Action`: Restore deadline as a canonical role or explicitly replace it with date and define the migration and semantic distinction: date should denote a scheduled/observed time, while deadline should denote a latest permitted completion time. Update the existing Flow-If example and glossary accordingly.
  - `Action`: Add a metric/property role and unit semantics for threshold/comparator, such as measure="character_count" or measure="walk_minutes", and require threshold/comparator to name what property of which target is compared. Define compatible units and reject unsupported combinations.
  - `Action`: Define multi-entity selection and result semantics for household operations, including whether quantity may select multiple distinct descriptor matches and how an Action may return LIST[REF[STRING]]. Otherwise explicitly prohibit quantity on entity selection and add a construct for selecting an ordered or bounded set of entities.
  - `Generate`: Replace the subjective TASK-versus-CONVO selection rule with a deterministic rule. For example: use CONVO whenever input or output is a participant turn; represent a requested generated response as an AGENT TURN containing GENERATE followed by UTTER; reserve standalone TASK for artifacts not addressed to a conversation participant.
  - `Task`: State explicitly that the shared step production used by Conversation includes generation after this revision, and define whether generation is legal in TURN bodies. This should be stated in Conversation as well as Task rather than inferred through a cross-reference.
  - `basis`: Actually remove the deprecated lower-case types-lexicon, action, and bind construct and glossary entries from the normative index instead of retaining pseudo-construct entries with only comments. Keep a non-normative changelog alias if backward-reference support is required.
- **Logic issues:** GENERATE grammar permits `-> name : REF[T]`, but revised Types & Lexicon says REF enters scope only through an Action result, Task parameter/return, or copied REF; Bind simultaneously treats GENERATE as a valid fifth bind site. These rules contradict each other.; The revised Action canonical-role list drops deadline while existing normative examples and common conditional requests use deadline. The new date role has a different plausible meaning, so the language no longer selects one canonical translation.; threshold and comparator specify only a number and relational operator, not the measured property, unit, or target relationship. `threshold=4500, comparator=">"` cannot be interpreted as character count rather than words, tokens, cost, or another quantity.; The STRING entity-selection rule requires exactly one matching entity, but the language provides no valid semantics for `quantity=2` selection or an Action result of LIST[REF[STRING]], making a basic two-object household task inexpressible.; The TASK-versus-CONVO translation-selection rule is not deterministic; an ordinary user request for an answer can reasonably be modeled as either a standalone GENERATE task or a USER/AGENT conversation, as the independent translations demonstrate.; The proposal says deprecated duplicate entries are no longer separately indexed normative constructs, but revises them into retained construct entries rather than deleting them; this leaves an avoidable duplicate-index and normative-status ambiguity.
- **Decision:** accepted
- **Documenter summary:** The Shaper proposed consolidating duplicate Type/Action/Bind entries, formalizing structured constraints (date/options/range/route/comparator), fixing the Task RETURN example, and adding a pure GENERATE construct with a TASK-vs-CONVO selection rule for artifact generation. The Critic found this 'needs-rework' due to unresolved contradictions—chiefly that GENERATE's grammar allows binding a REF[T] result while Types & Lexicon restricts REF creation to Actions/params/copies, plus an underspecified, non-deterministic TASK/CONVO selection rule and threshold/comparator lacking a measured-property/unit definition—but it was accepted anyway as a forced acceptance after three attempts, with the Critic's required changes (REF/GENERATE reconciliation, deadline vs date, threshold units, multi-entity selection, deterministic CONVO rule) carried forward as known issues for a future sprint.
- **Cost this sprint:** $1.9249

## Sprint 3 (attempt 1/3) — 2026-09-23

- **Language version:** 3.0.0 → 3.0.0 (MAJOR)
- **Candidate task:** Draft a reply to my professor asking for a two-day extension on the assignment, and keep it formal.
- **Shaper proposal (model: anthropic/claude-sonnet-5):** Closes the previously free-text `tone` attribute into a normative, closed vocabulary (mirroring `comparator`'s enum pattern) so stylistic register modifiers like 'formal' are deterministic across translators, directly modeling the HTML-precedent content/attribute separation for this task.
- **Changes:** `Action` (revise, MAJOR)
- **Critic decision:** needs-rework — Closing exact tone literals is a useful local improvement for explicit values such as formal and urgent, and the change is not fundamentally the wrong shape. It cannot yet be accepted because its stated determinism benefit depends on a missing canonicalization rule, it leaves UTTER tone inconsistent, and its narrow vocabulary can erase valid register constraints. The supplied simulations show a concrete benefit for the urgent warning but little impact elsewhere, while independent translations expose unresolved choices about both tone presence and conversational representation.
- **Doc hygiene:** pass — All changes carry a complete glossary entry (gloss + worked example).
- **Pre-KPI assessment:**
  - coverage: mixed — The closed enum makes a small set of common registers available as checkable tokens, but it rejects many ordinary request-level registers such as reassuring, technical, concise, diplomatic, humorous, plain-language, or professional. Because no normalization or extension mechanism is defined, requests outside the eight labels must either lose their register or bury it in prose content.
  - expressivity: mixed — For requests explicitly requiring formal, polite, urgent, casual, or the other listed labels, the proposal preserves the modifier more precisely. However, closing tone without a defined mapping from natural-language style requests to enum values loses distinctions such as professional versus formal, friendly versus polite, and serious versus neutral; it also does not constrain tone on UTTER even though conversational register is an important open-item property.
  - determinism: mixed — The exact token formal now converges where translators independently identify the same enum member, an improvement over arbitrary strings. But independent translations already disagree on whether to encode tone at all, and the proposal gives no canonical mapping for near-synonyms or mixed styles; for example, a translator may map professional to formal, neutral, or polite, while another preserves it in content.
  - interpretability: benefit — A reader can unambiguously understand each of the eight accepted tone values, and invalid values are statically rejected. The revised Action gloss overclaims that two writers will always choose the same marker, which is not warranted without a translation-selection table, but the runtime syntax itself is clearer than arbitrary tone strings.
  - improvement: benefit — For generated artifacts and outbound communication with one of the listed styles, a constrained tone field gives a weaker executor a directly usable instruction instead of asking it to infer register from prose. The effect is narrow in this sample because most items do not specify one of the eight tones.
- **Simulated examples:**
  - `held-trip-1` (seed_tasks) [Partial] NL: "Plan a 3-day itinerary in Kyoto that includes at least one temple per day and avoids anything more than a 20-minute walk from the last stop." → `ENTRYPOINT PlanKyoto

TASK PlanKyoto : LIST[STRING] {
  GENERATE(target="itinerary", audience="traveler", quantity=3, content="Kyoto; include at least one temple on each day; each next stop must be at most a 20-minute walk from the preceding stop") -> itinerary : LIST[STRING]
  RETURN itinerary
}` — GENERATE captures the requested artifact and duration, but the per-day quantifier and adjacency/travel-time constraint remain opaque prose. The tone change is irrelevant.
  - `dev-embodied-2` (seed_tasks) [Full] NL: "Put both pillows from the sofa onto the armchair, one at a time." → `ENTRYPOINT MovePillows

TASK MovePillows {
  LET pillows : LIST[STRING] = ["left sofa pillow", "right sofa pillow"]
  FOR EACH pillow IN pillows {
    ACTION pick_up(target=pillow, source="sofa") -> picked : REF[STRING]
    ACTION place(target=picked, destination="armchair")
  }
}` — The ordered finite loop represents one-at-a-time handling and REF preserves each picked pillow's identity. The tone change is irrelevant.
  - `b30b9f84-0541-4826-a3af-98220b851f7c` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Search for women's sports wear, size S." → `ENTRYPOINT SearchWomensSportsWear

TASK SearchWomensSportsWear {
  ACTION search(target="women's sports wear")
  ACTION apply_filters(target="gender", options=["women"])
  ACTION apply_filters(target="size", options=["S"])
}` — Search and both requested filters are explicit. The tone change is irrelevant.
  - `33b57a14-f469-405c-8843-f7e8ceb5b1ed` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Add 10 of the cheapest green shirt to my cart" → `ENTRYPOINT AddCheapestGreenShirt

TASK AddCheapestGreenShirt {
  ACTION search(target="green shirt")
  ACTION sort(target="price", ordering="ascending")
  ACTION click(target="first green shirt") -> shirt : REF[STRING]
  ACTION fill_field(target="quantity", content="10")
  ACTION click(target="add to cart")
}` — The ordering, quantity, and cart action are represented in source order. The tone change is irrelevant.
  - `trial_T20190907_164924_809101#1` (ALFRED (json_2.1.0, train)) [Full] NL: "Place a washed tomato on a table." → `ENTRYPOINT PlaceWashedTomato

TASK PlaceWashedTomato {
  ACTION rinse(target="tomato") -> tomato : REF[STRING]
  ACTION place(target=tomato, destination="table")
}` — The rinse precedes placement and the selected tomato is retained by REF. The tone change is irrelevant.
  - `trial_T20190906_230132_658755#2` (ALFRED (json_2.1.0, train)) [Full] NL: "Put a warm glass on the shelf." → `ENTRYPOINT PutWarmGlassOnShelf

TASK PutWarmGlassOnShelf {
  ACTION heat(target="glass") -> glass : REF[STRING]
  ACTION place(target=glass, destination="shelf")
}` — Heating and subsequent placement of the same glass are explicit. The tone change is irrelevant.
  - `django__django-16819` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "Reduce Add/RemoveIndex migration operations when optimizing migration operations." → `ENTRYPOINT ReduceIndexOperations

TASK ReduceIndexOperations {
  ACTION modify_code(target="django/db/migrations/operations/models.py", content="reduce AddIndex and RemoveIndex operations during migration-operation optimization")
}` — The requested code modification and affected file are represented; detailed implementation remains the typed string payload. The tone change is irrelevant.
  - `matplotlib__matplotlib-23412` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "[Bug]: offset dash linestyle has no effect in patch objects." → `ENTRYPOINT FixPatchDashOffset

TASK FixPatchDashOffset {
  ACTION modify_code(target="lib/matplotlib/patches.py", content="make dash tuple offsets affect patch edge linestyle rendering, matching Line2D behavior; nonzero dash offsets must shift the pattern")
}` — The actionable code-fix core is explicit, while the reproduction details are retained as an implementation payload if needed. The tone change is irrelevant.
  - `c6671` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "I would like to follow a healthier diet. I am a university student and do not have much time to cook. Do you have options in Budapest or easy healthy recipes at home?" → `ENTRYPOINT HealthyDietAdvice

TASK HealthyDietAdvice : STRING {
  GENERATE(target="recommendations", audience="university student", content="healthy eating options in Budapest and easy healthy recipes to make at home with little cooking time") -> advice : STRING
  RETURN advice
}` — Intent, audience, alternatives, and time constraint are represented, while the recommendation substance remains an appropriate opaque payload for an open request. The tone change is irrelevant.
  - `c4355` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "what is view on friendship?" → `ENTRYPOINT FriendshipView

TASK FriendshipView : STRING {
  GENERATE(target="response", content="give a view on friendship") -> response : STRING
  RETURN response
}` — The request is an open opinion-generation request; its substantive answer properly remains in GENERATE content. The tone change is irrelevant.
  - `c6745` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "I'm enjoying our chats. Let's go with something really controversial, are you up for that?" → `ENTRYPOINT ControversialDiscussion

CONVO ControversialDiscussion {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="I am enjoying our chats. Are you willing to discuss a controversial topic?")
  }
}` — The conversational speech act and topic framing are preserved, but the friendly/casual register cannot be normatively represented because this proposal constrains tone only on Action and GENERATE, not UTTER.
  - `c3642` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Hey chat, do you think that the legal age of adulthood should be lowered from 21 to 18 in the US?" → `ENTRYPOINT AskAdulthoodOpinion

CONVO AskAdulthoodOpinion {
  TURN t1 SPEAKER=USER {
    UTTER ask(target="US legal age of adulthood", content="Should the legal age of adulthood be lowered from 21 to 18?")
  }
}` — The question, subject, location, and numeric alternatives are preserved; the opinion itself is open-ended prose substance. The tone change is irrelevant.
  - `wildchat1m_en3u-107765` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns)) [Partial] NL: "中国电动车行业发展" → `ENTRYPOINT ExplainChineseEVIndustry

TASK ExplainChineseEVIndustry : STRING {
  GENERATE(target="explanation", content="中国电动车行业发展") -> explanation : STRING
  RETURN explanation
}` — The request is an open informational explanation in Chinese; its substantive explanation remains a payload. The tone change is irrelevant.
  - `wildchat1m_en3u-18683` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns)) [Partial] NL: "Напиши короткое описание для Android приложений перечисленных ниже. Предоставь для каждого ссылку на официальную страницу в Google Play, Github или 4pda.to/forum/. Результат отобрази в виде таблицы." → `ENTRYPOINT DescribeAndroidApps

TASK DescribeAndroidApps : STRING {
  GENERATE(target="app-description table", format="table", content="For every supplied Android app, write a short description and provide an official Google Play, GitHub, or 4pda.to/forum link. Apps: Wi-Fi в метро; Telegram; Outlook; IMDb; MyShows; Shikimori; Авито; Винлаб; Красное&Белое; ЕМИАС.ИНФО; Google Keep; Тинькофф Инвестиции; МегаФон; МТС; Boost для Reddit; Bitwarden; Aura Icons; AnkiDroid; AirBrush; Яндекс Go; Spotify; Яндекс Музыка; Яндекс Еда; Яндекс Погода; Яндекс Маркет; Юла; Google Фотосканер; Google Фото; Умный дом; Тройка. Пополнение и проверка баланса; Тинькофф; СберМегаМаркет; Погода M8; Мой Мосэнергосбыт; Мой здоровый рацион; Google Контакты; Zepp Life; WireGuard VPN; Wifire; WIFI File Transfer; VSCO; TurboVPN; Snapseed; Shortcut Maker; Sesame; RAR; Raindrop; PowerDirector; Pixlr; OZON; OneUI Circle Icons; MyUI5 Icons; MIUI 10 Icon Pack; Meta Quest; MAPS.ME; Lightroom; Google Pay; Google One; FRANK by БАСТА; Feedly; Icon Pack Studio; F-Droid; EhViewer; Dostaevsky; Delivery Club; DeepL; Croc Icon Pack; Clue; Cleandroid UI Icons") -> result : STRING
  RETURN result
}` — The output format, per-item scope, and approved link sources are explicit. The descriptions and retrieved official links are correctly open content payloads; tone is irrelevant.
  - `wildchat1m_en3u-9962` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns)) [Partial] NL: "Create a civil danger warning for counties located in South Eastern Nebraska based off of this format." → `ENTRYPOINT CreateNebraskaWarning

TASK CreateNebraskaWarning : STRING {
  GENERATE(target="civil danger warning", audience="counties in southeastern Nebraska", tone="urgent", content="create the warning using the supplied civil-danger-warning format") -> warning : STRING
  RETURN warning
}` — This is the clearest sample benefit: urgent is now a valid constrained token rather than an arbitrary string. The long supplied template and warning substance remain payload prose.
  - `wildchat1m_en3u-5353` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns)) [Partial] NL: "Write a 90 minute script for a GoT scene where Daenerys talks with Sansa, Jon, and Arya; the northern accents get thicker and slangier and Daenerys struggles to understand; it starts normal and serious." → `ENTRYPOINT WriteGoTScene

TASK WriteGoTScene : STRING {
  GENERATE(target="script", format="screenplay", tone="neutral", content="90-minute GoT scene: Daenerys speaks with Sansa, Jon, and Arya; begin normal and serious; the three northern characters' accents become progressively thicker and slangier; show Daenerys increasingly struggling to understand") -> script : STRING
  RETURN script
}` — Screenplay format, duration, ordering, characters, and progressive constraint are retained. Neutral encodes only the initial serious-normal presentation imperfectly; the requested serious register has no defined mapping and should not be silently equated with neutral.
  - `1776027441532` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample)) [Partial] NL: "How should I start going to the gym? what should I know?" → `ENTRYPOINT GymBeginnerAdvice

TASK GymBeginnerAdvice : STRING {
  GENERATE(target="beginner gym advice", audience="gym beginner", content="how to start going to the gym and what to know") -> advice : STRING
  RETURN advice
}` — The advice intent and beginner audience are explicit; advice substance appropriately remains open prose. The tone change is irrelevant.
  - `1775939473361` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample)) [Partial] NL: "Draft a Thursday-to-Sunday June itinerary for Sedona, flying Orlando to Phoenix Thursday at 5 AM and Phoenix to Orlando Sunday at 10 AM; interested in hikes, shopping, natural beauty, staying in town, and willing to drive up to 2 hours for sights." → `ENTRYPOINT DraftSedonaItinerary

TASK DraftSedonaItinerary : STRING {
  GENERATE(target="itinerary", audience="traveler", range=["Thursday", "Sunday"], date=["Thursday 5:00 AM Orlando to Phoenix", "Sunday 10:00 AM Phoenix to Orlando"], options=["hikes", "shopping", "natural beauty"], threshold=2, comparator="<=", content="June Sedona trip; stay at an Airbnb in town; driving limit is two hours from Sedona for sights") -> itinerary : STRING
  RETURN itinerary
}` — The dates, flights, interests, location, lodging, and driving bound are structured or retained in content. Fine-grained scheduling and route feasibility remain generative planning substance; tone is irrelevant.
  - `1776023647092` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample)) [Partial] NL: "My company is adopting AI; my team worries about losing jobs. Claude has automated 30% of daily tasks. How should I handle this with my team?" → `ENTRYPOINT AdviseOnAITransition

TASK AdviseOnAITransition : STRING {
  GENERATE(target="management advice", audience="team manager", content="how to handle team job-loss concerns during company AI adoption; Claude automates 30% of the team's daily tasks") -> advice : STRING
  RETURN advice
}` — The actor, audience, AI-adoption context, concern, and 30% quantity are retained. The management advice is open prose substance; tone is unspecified.
  - `1775828997466` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample)) [Partial] NL: "Can you help me organize my daily life and responsibilities more effectively?" → `ENTRYPOINT OrganizeDailyLife

TASK OrganizeDailyLife : STRING {
  GENERATE(target="organization plan", audience="user", content="help organize daily life and responsibilities more effectively") -> plan : STRING
  RETURN plan
}` — The request for a planning artifact is represented; the actual system and advice are open content. The tone change is irrelevant.
- **Cross-check:** used=True, agreement=partial — Independent translations commonly agree on GENERATE plus target/content for direct generation requests, and on REF-based sequencing for the ALFRED items. They substantially diverge on Task/GENERATE versus CONVO/UTTER for open requests, on whether tone is present at all, and on the representation of filters, cart selection, and route constraints. For the proposed feature specifically, one provider uses tone="casual" on an UTTER even though the proposal does not normatively close UTTER tone, while the other omits tone; this demonstrates unresolved translation selection.
- **Required changes:**
  - `Action`: Add a normative translation-selection table for common natural-language register terms. For each accepted synonym, define its canonical enum result (for example, business-like/professional -> formal if that equivalence is intended), and state that translators must omit tone rather than invent a mapping when no listed value preserves the request.
  - `Action`: Either expand the tone enum with clearly non-overlapping values needed for ordinary request registers, or explicitly define a controlled extension mechanism. At minimum, resolve how serious, professional, friendly, reassuring, technical, humorous, and concise requests are represented without silently losing distinctions.
  - `Utterance`: State whether tone on UTTER is governed by the same closed enum. If it is, revise Utterance semantics and glossary accordingly; if it is not, remove or qualify the claim that tone closure makes stylistic register deterministic across the language.
  - `Action`: Revise the glossary claim that the enum ensures two different writers 'always' produce the exact same tone marker. Limit that claim to explicit enum labels or support it with the required canonicalization table.
  - `Generate`: Explicitly state in Generate semantics that tone uses Action's closed enum, rather than relying only on Action semantics saying it applies to GENERATE; this makes the cross-construct constraint discoverable from the construct where generation users need it.
- **Logic issues:** The enum specifies permitted output strings but no mapping from natural-language style terms to those strings. Thus `professional`, `business-like`, and `formal` are all plausible translations of one request, but only one is legal and no rule identifies it.; The revised semantics say tone is constrained on Action and GENERATE, while UTTER grammar explicitly admits tone and its semantics uses Action's core attribute vocabulary. A casual, formal, or apologetic conversational utterance therefore has unspecified constraint behavior.; The closed vocabulary cannot represent many semantically distinct registers. Replacing a request for a 'professional but reassuring' response with tone="formal" loses reassuring; placing it in content avoids rejection but defeats the claimed structured treatment.; The worked example is valid under the proposed semantics, but it demonstrates only the already-canonical literal formal and does not test the proposal's central paraphrase-normalization claim.; The operation vocabulary is labelled normative but no static-error rule says whether operations outside the listed vocabulary are forbidden; the current specification itself uses operations such as fetch_article and check_reply_status outside that list. This pre-existing ambiguity continues to weaken deterministic action translation.
- **Decision:** needs-rework
- **Documenter summary:** The Shaper proposed closing the free-text `tone` attribute into an 8-value normative enum (formal, neutral, casual, polite, urgent, enthusiastic, apologetic, assertive), mirroring the `comparator` closure pattern, to make register modifiers like 'formal' deterministic per the HTML precedent. The Critic sent it back for rework: no mapping rule exists for near-synonyms (professional/business-like vs. formal), the enum omits common registers (serious, reassuring, technical, humorous) with no extension mechanism, and the closure was never extended to UTTER despite conversational register being an open item—cross-check translations diverged on exactly this UTTER tone question, and simulations showed benefit only for the one clear-cut 'urgent' warning case while several others (e.g. the GoT script's 'serious' tone) exposed silent loss of distinction.
- **Cost this sprint:** $1.5256

## Sprint 3 (attempt 2/3) — 2026-09-23

- **Language version:** 3.0.0 → 3.0.0 (MAJOR/PATCH)
- **Candidate task:** Draft a reply to my professor asking for a two-day extension on the assignment, and keep it formal.
- **Shaper proposal (model: anthropic/claude-sonnet-5):** Resolves the Critic's rework requirements by giving Action's tone enum an explicit NL-to-canonical translation table plus a mandatory omit-and-fold-into-content fallback for unlisted or multi-facet registers, expanding the enum to cover ordinary request registers, extending the same closed-enum rule explicitly to UTTER and GENERATE, and narrowing the glossary's determinism claim to what the table actually guarantees.
- **Changes:** `Action` (revise, MAJOR), `Utterance` (revise, MAJOR), `Generate` (revise, PATCH)
- **Critic decision:** needs-rework — The proposal has a sound core idea and materially improves deterministic translation for the table entries while preserving unlisted and compound register requirements. It cannot be accepted because its own UTTER example contradicts its mandatory normative rule, demonstrating that the table's matching policy is incomplete in practice. A precise normalization policy and a structured fallback for noncanonical register would retain the benefits without creating contradictory or indistinguishable encodings.
- **Doc hygiene:** pass — All changes carry a complete glossary entry (gloss + worked example).
- **Pre-KPI assessment:**
  - coverage: benefit — The expanded shared tone vocabulary newly covers common request registers such as professional, serious, technical, humorous, friendly, and reassuring. The explicit fallback preserves uncommon or compound registers as payload rather than making them unexpressible, although it necessarily remains prose rather than structured metadata.
  - expressivity: benefit — The omit-and-fold rule avoids silently dropping a requested facet such as "professional but reassuring," and the shared rule makes register available consistently for ACTION, GENERATE, and UTTER. Most open-item prose remains appropriately opaque, but the fallback overloads content with a meta-instruction and lacks a delimiter or structured representation separating register from substantive payload.
  - determinism: mixed — The listed synonym mappings substantially improve convergence for terms such as business-like and formal. However, the UTTER worked example maps "casually" to casual even though that inflected form is neither a canonical label nor present in the required table; this exposes an unresolved question of whether grammatical variants are allowed, and independent translations still diverge materially on TASK/GENERATE versus CONVO/UTTER selection and on action decomposition.
  - interpretability: mixed — A closed, shared vocabulary and published mapping table are easy to inspect, and the glossary claim is appropriately narrowed. But the normative text contradicts its own worked UTTER example, while putting an unstructured register description inside content leaves a reader unable to distinguish the requested output substance from a register constraint without relying on prose interpretation.
  - improvement: benefit — Canonical register labels provide useful planning guidance to weaker models when drafting emails, reports, and replies, while preserving unusual tone requirements rather than discarding them. The gain is constrained by the current fallback, which provides no machine-checkable separation between tone metadata and the requested content.
- **Simulated examples:**
  - `dev-web-2` (seed_tasks) [Full] NL: "On the electronics store, filter laptops to 16 GB RAM or more under $1,200, and add the best-rated one to the cart." → `ENTRYPOINT FilterAndAddLaptop

TASK FilterAndAddLaptop {
  ACTION open(target="electronics_store")
  ACTION select_filter(target="laptops")
  ACTION apply_filters(target="RAM", threshold=16, comparator=">=")
  ACTION apply_filters(target="price", threshold=1200, comparator="<")
  ACTION sort(target="laptops", ordering="best-rated")
  ACTION click(target="best-rated laptop") -> laptop : REF[STRING]
  ACTION click(target="add_to_cart", destination=laptop)
}` — Closed web task is structurally represented. Proposed tone changes are irrelevant.
  - `held-trip-1` (seed_tasks) [Fail] NL: "Plan a 3-day itinerary in Kyoto that includes at least one temple per day and avoids anything more than a 20-minute walk from the last stop." → `ENTRYPOINT PlanKyotoItinerary

TASK PlanKyotoItinerary : STRING {
  GENERATE(target="itinerary", content="Create a 3-day itinerary in Kyoto with at least one temple per day and no stop more than a 20-minute walk from the preceding stop.", quantity=3) -> itinerary : STRING
  RETURN itinerary
}` — The actionable closed-task constraints remain opaque in content: there is no representation for per-day minimum inclusion, duration-valued walking constraints, or adjacency constraints between generated stops. Tone changes are irrelevant.
  - `4bc70fa1-e817-405f-b113-0919e8e94205` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Add the cheapest Women's Sweaters to my shopping cart." → `ENTRYPOINT AddCheapestSweater

TASK AddCheapestSweater {
  ACTION search(target="Women's Sweaters")
  ACTION sort(target="price", ordering="ascending")
  ACTION click(target="first result") -> sweater : REF[STRING]
  ACTION click(target="add_to_cart", destination=sweater)
}` — Closed web selection and cart action are represented. Tone changes are irrelevant.
  - `7ad37a91-c4c2-42d6-9b87-1f3e6a81647e` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "check reservation availability for an Indian restaurant with price below $30 in East village" → `ENTRYPOINT CheckReservationAvailability

TASK CheckReservationAvailability {
  ACTION search(target="Indian restaurant", destination="East Village")
  ACTION apply_filters(target="price", threshold=30, comparator="<")
  ACTION search(target="reservation availability")
}` — The searchable entity, location, price constraint, and availability inquiry are captured. Tone changes are irrelevant.
  - `trial_T20190906_224234_994763#2` (ALFRED (json_2.1.0, train)) [Full] NL: "Put a spoon in the sink." → `ENTRYPOINT PutSpoonInSink

TASK PutSpoonInSink {
  ACTION place(target="spoon", destination="sink")
}` — Closed household action is directly represented. Tone changes are irrelevant.
  - `trial_T20190909_065023_650475#2` (ALFRED (json_2.1.0, train)) [Full] NL: "Retrieve plate from cupboard, insert it into microwave, take the plate to the fridge" → `ENTRYPOINT MovePlate

TASK MovePlate {
  ACTION pick_up(target="plate", source="cupboard") -> plate : REF[STRING]
  ACTION place(target=plate, destination="microwave")
  ACTION pick_up(target=plate, source="microwave")
  ACTION place(target=plate, destination="fridge")
}` — The selected plate's identity and required ordering are preserved by REF binding. Tone changes are irrelevant.
  - `django__django-15957` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "Prefetch objects don't work with slices" → `ENTRYPOINT FixPrefetchSlicedQuerysets

TASK FixPrefetchSlicedQuerysets {
  ACTION modify_code(target="django/db/models/fields/related_descriptors.py", content="Support Prefetch objects with sliced querysets, including Prefetch('post_set', queryset=Post.objects.all()[:3], to_attr='example_posts'), without raising the post-slice filtering AssertionError.")
  ACTION run_tests(target="Prefetch sliced querysets")
}` — The known target file, requested behavioral repair, reproducing pattern, and validation intent are represented. Tone changes are irrelevant.
  - `django__django-16502` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "After #26052 runserver returns response body for HTTP HEAD requests" → `ENTRYPOINT FixRunserverHeadBody

TASK FixRunserverHeadBody {
  ACTION modify_code(target="django/core/servers/basehttp.py", content="Ensure runserver strips response bodies for HTTP HEAD requests, restoring HTTP compliance and preventing the body returned after headers.")
  ACTION run_tests(target="runserver HTTP HEAD response")
}` — The target file, protocol condition, required behavior, and validation target are represented. Tone changes are irrelevant.
  - `c1957` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "I think something important we should discuss is that it is important not to be negative. Negativity is a choice, every time. It is not related to depression. People who have the option to be negative should not be like that! I don't want to hear about bias, I am simply saying it is important to stay positive or you become negative. It's very important." → `ENTRYPOINT PositivityDiscussion

CONVO PositivityDiscussion {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="I think something important we should discuss is that it is important not to be negative. Negativity is a choice, every time. It is not related to depression. People who have the option to be negative should not be like that. I don't want to hear about bias; I am simply saying it is important to stay positive or you become negative. It's very important.")
  }
}` — The conversational speech act and speaker are represented; the opinion's substantive content properly remains an opaque payload. No explicit register term invokes the proposal.
  - `c5204` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "People who live in the same country but have different religious beliefs" → `ENTRYPOINT ReligiousDiversityStatement

CONVO ReligiousDiversityStatement {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="People who live in the same country but have different religious beliefs.")
  }
}` — The fragment is preserved as a user statement, but its intended request or continuation is not explicit in the source. Its substantive interpretation remains prose.
  - `c714` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Is Switzerland a "Parasite" Country ? that does not provide any real value to the world and his wealth comes from other people fortunes ?" → `ENTRYPOINT SwitzerlandEconomicQuestion

CONVO SwitzerlandEconomicQuestion {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Is Switzerland a 'Parasite' country that provides no real value to the world and whose wealth comes from other people's fortunes?", target="Switzerland")
  }
}` — Question speech act and topic are captured; the argumentative proposition properly remains content prose. Tone changes are irrelevant.
  - `c1044` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Do you think its important for people to have healthy relationships in life ?" → `ENTRYPOINT HealthyRelationshipsQuestion

CONVO HealthyRelationshipsQuestion {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Do you think it is important for people to have healthy relationships in life?", target="healthy relationships")
  }
}` — The user question and subject are represented; its requested opinion remains prose content. Tone changes are irrelevant.
  - `wildchat1m_en3u-45091` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0301)) [Partial] NL: "How would someone discibe the surface texture of the catwalk greatings on Oil Rigs? Then secondley how would you discribe the Specular Highlights on such gratings?" → `ENTRYPOINT DescribeOilRigGratings

TASK DescribeOilRigGratings : STRING {
  GENERATE(target="description", content="Describe the surface texture of catwalk gratings on oil rigs and describe the specular highlights on those gratings.") -> description : STRING
  RETURN description
}` — The two requested descriptive topics and their ordering are captured in the generation request; generated descriptive substance is correctly opaque. Tone changes are irrelevant.
  - `wildchat1m_en3u-136118` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-1106-preview)) [Partial] NL: "answer with 80 to 110 words as you are in a speaking IELTS test. Don't reveal that you are an A.I.

• In your country (Iran), how much time do people spend on work and how much time on leisure? Is this a good balance, do you think?" → `ENTRYPOINT AnswerIELTSQuestion

TASK AnswerIELTSQuestion : STRING {
  GENERATE(target="spoken IELTS answer", format="80 to 110 words", content="Answer as if in a speaking IELTS test. Do not reveal that you are an AI. Discuss, for Iran, time spent working versus leisure and whether the balance is good.") -> answer : STRING
  RETURN answer
}` — Output genre, length, role-play condition, nondisclosure constraint, country, and questions are preserved. No requested register term invokes the proposal.
  - `wildchat1m_en3u-105894` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "Make a report about Peterhof" → `ENTRYPOINT MakePeterhofReport

TASK MakePeterhofReport : STRING {
  GENERATE(target="report", content="about Peterhof") -> report : STRING
  RETURN report
}` — The requested artifact and subject are structured; report prose is appropriately opaque. Tone changes are irrelevant.
  - `wildchat1m_en3u-135133` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0125)) [Partial] NL: "overview of the football industry in egypt. include credible apa 7 reference " → `ENTRYPOINT GenerateEgyptFootballOverview

TASK GenerateEgyptFootballOverview : STRING {
  GENERATE(target="overview", format="APA 7 references", content="Provide an overview of the football industry in Egypt and include credible references.") -> overview : STRING
  RETURN overview
}` — Artifact, topic, credibility requirement, and citation format are represented; the overview and references remain generative prose. Tone changes are irrelevant.
  - `1775448628523` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "I will be in Paris for two days for a conference, and I'll be free on day 2. I want to go to a museum and see some nice art. I don't want anything too crowded. What do you suggest?" → `ENTRYPOINT SuggestParisMuseum

TASK SuggestParisMuseum : STRING {
  GENERATE(target="museum recommendation", audience="user", content="Suggest a museum in Paris for day 2 of a two-day conference trip, with nice art and without excessive crowds.") -> recommendation : STRING
  RETURN recommendation
}` — Timing, location, activity, preference, and avoidance constraint are preserved. Recommendation substance is correctly generated as prose. Tone changes are irrelevant.
  - `1775437471200` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "I need your help to create a study schedule for a month in which I can finish studying seven subjects completely." → `ENTRYPOINT CreateStudySchedule

TASK CreateStudySchedule : STRING {
  GENERATE(target="study schedule", content="Create a one-month study schedule that completes study of seven subjects.", quantity=7, date=["day 1", "day 30"]) -> schedule : STRING
  RETURN schedule
}` — Artifact, month duration, and seven-subject quantity are represented, but subjects and available study time are unspecified in the source. The detailed schedule remains generative prose.
  - `1775854603021` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "I need help by managing my money because I always run out before the end of the month" → `ENTRYPOINT BudgetHelp

TASK BudgetHelp : STRING {
  GENERATE(target="budget-management advice", audience="user", content="Help manage money because the user runs out before the end of each month.") -> advice : STRING
  RETURN advice
}` — Requested advisory artifact, audience, financial problem, and monthly timing are preserved. Advice substance remains prose. Tone changes are irrelevant.
  - `1775483125242` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "Hi I would like you to assist with planning a trip to China, I need a 4 star hotel, good restaurants to have traditional food, sight seeing about the heritage and other activities to do visiting other attractions" → `ENTRYPOINT PlanChinaTrip

TASK PlanChinaTrip : STRING {
  GENERATE(target="China trip plan", audience="user", content="Plan a trip to China including a 4-star hotel, good restaurants serving traditional food, heritage sightseeing, and other attractions and activities.", threshold=4, comparator="==") -> plan : STRING
  RETURN plan
}` — Destination, requested planning artifact, hotel-star requirement, food preference, heritage sightseeing, and other attractions are preserved. The itinerary content remains generative prose; tone changes are irrelevant.
- **Cross-check:** used=True, agreement=partial — Providers generally agree on core action sequences for the ALFRED examples, on GENERATE for direct report-writing requests, and on simple one-turn PRISM questions. They diverge substantially on whether a user request is represented as TASK/GENERATE or CONVO/UTTER, on action granularity for web tasks, and on representation of c5204; the proposed table improves only tone-label convergence and does not resolve those broader translation choices.
- **Required changes:**
  - `Action`: Make the translation-selection table exhaustive with respect to permitted inflections or explicitly define normalization before lookup. At minimum add "casually -> casual" and analogous adverbial/inflected forms, or revise the UTTER worked example to use the listed word "casual" rather than "casually".
  - `Utterance`: Correct the worked example so it obeys the normative lookup rule. As written, its source says "casually" but the table has no such entry, so the stated semantics require omitting tone and folding the wording into content.
  - `Action`: Define a structured fallback representation for unlisted or multi-facet register, such as `register_note=STRING`, permitted on ACTION, GENERATE, and UTTER, rather than requiring register metadata to be inserted indistinguishably into `content`. Define whether it may coexist with canonical `tone` and prohibit duplicate register modifiers.
  - `Action`: State explicitly that duplicate canonical attributes are also a static error for UTTER, or define UTTER-specific duplicate-attribute behavior, since UTTER shares the attribute vocabulary but the duplicate rule presently names only Action and GENERATE.
- **Logic issues:** The UTTER worked example violates the mandatory table lookup rule: "casually" is not a canonical value and is not among the listed synonyms for "casual", yet it is translated to `tone="casual"`.; The proposal does not define whether morphology, punctuation, capitalization, or variants such as "formally", "professionally", "warmly", and "in a professional tone" are table matches. Independent translators can therefore either normalize them, omit tone, or incorrectly choose a nearby label.; The mandatory fallback places a register constraint into `content`, whose stated exclusive role is the literal source text or exact instruction payload. Without a separate field or delimiter, a reader and downstream model cannot reliably distinguish output substance from a register instruction.; UTTER uses Action's attribute vocabulary but the duplicate canonical-attribute static-error rule still applies textually only to Action and GENERATE, leaving duplicate UTTER attributes underspecified.
- **Decision:** needs-rework
- **Documenter summary:** Shaper proposed a closed 14-value tone enum shared by Action/GENERATE/UTTER, with a fixed NL-synonym translation table and a mandatory omit-and-fold-into-content fallback for unlisted or multi-facet registers. The Critic rejected the proposal as needs-rework because its own UTTER worked example ('casually' -> tone="casual") violated the mandatory table-lookup rule it just introduced, exposing an unresolved normalization gap for inflected/adverbial register terms, and also required a structured fallback (rather than unstructured content-folding) plus clarification of duplicate-attribute rules for UTTER before acceptance.
- **Cost this sprint:** $1.7828

## Sprint 3 (attempt 3/3) — 2026-09-23

- **Language version:** 3.0.0 → 4.0.0 (MAJOR/PATCH)
- **Candidate task:** Draft a reply to my professor asking for a two-day extension on the assignment, and keep it formal.
- **Shaper proposal (model: anthropic/claude-sonnet-5):** Fixes the rejected tone/register design by (1) making the tone synonym table exhaustive and exact-match-only via an explicit normalization rule covering adverbial/hyphen/case variants, (2) replacing the ambiguous 'fold into content' fallback with a new structured `register_note` attribute that is mutually exclusive with `tone`, and (3) explicitly extending the duplicate-attribute static-error rule to UTTER and to `register_note`.
- **Changes:** `Action` (revise, MAJOR), `Utterance` (revise, MAJOR), `Generate` (revise, PATCH)
- **Critic decision:** needs-rework — [Forced acceptance after 3 attempt(s) without a clean accept — the required changes below are known issues carried forward for a future sprint to address, not resolved.] The separate register_note design is a meaningful improvement over placing noncanonical register requirements in content, and shared duplicate-attribute and mutual-exclusion rules are useful. However, the proposal's central exact-match policy is internally inconsistent with its own worked examples, so independent translators can still legitimately choose tone, register_note, or omission for commonplace phrased requests. The core approach is sound, but the extraction boundary and attribute validation must be specified before acceptance.
- **Doc hygiene:** pass — All changes carry a complete glossary entry (gloss + worked example).
- **Pre-KPI assessment:**
  - coverage: benefit — The new register_note slot preserves arbitrary register descriptions without forcing them into content, including multi-facet descriptions that the closed tone enum cannot represent. It helps open conversational and generation requests, though it does not address missing closed-task primitives for itinerary constraints or precise code edits.
  - expressivity: benefit — register_note captures distinctions such as "professional but reassuring" structurally and avoids losing them when they do not map to one enum value. However, the stated exact-match policy contradicts examples that extract "formal" or "casually" from larger natural-language clauses, leaving the intended encoding of ordinary phrased style requests unresolved.
  - determinism: mixed — A closed canonical tone enum, specified normalization, and a declared fallback improve convergence for isolated register tokens. But translators must still decide whether a word embedded in a clause such as "keep it formal" is a candidate term or an impermissible phrase containing a term; the proposal explicitly forbids extraction for "in a professional tone" while its examples extract from analogous clauses. Independent translations also diverge materially between TASK/GENERATE and CONVO/UTTER for multiple open items.
  - interpretability: mixed — The separate, mutually exclusive register_note is much clearer than folding register into content, and duplicate-attribute errors help readers trust one source of truth. The specification nevertheless calls the table exhaustive while providing a finite, non-exhaustive natural-language synonym list, and does not make unknown attributes invalid despite attr ::= IDENT = value, so readers cannot know whether arbitrary attributes have meaning.
  - improvement: benefit — A weaker executor can reliably distinguish literal generation payload from style requirements when register_note is used, and can apply canonical tone labels consistently once present. This is useful structure rather than ceremony, especially for multi-turn utterances and generated messages.
- **Simulated examples:**
  - `dev-embodied-1` (seed_tasks) [Full] NL: "Rinse the mug in the sink, then put it in the coffee maker." → `ENTRYPOINT RinseThenPlace

TASK RinseThenPlace {
  ACTION rinse(target="mug", destination="sink") -> mug : REF[STRING]
  ACTION place(target=mug, destination="coffee_maker")
}` — Existing REF binding and source order capture the selected mug and ordering; proposed register changes are irrelevant.
  - `held-trip-1` (seed_tasks) [Partial] NL: "Plan a 3-day itinerary in Kyoto that includes at least one temple per day and avoids anything more than a 20-minute walk from the last stop." → `ENTRYPOINT PlanKyotoItinerary

TASK PlanKyotoItinerary : STRING {
  GENERATE(target="itinerary", content="Create a 3-day Kyoto itinerary with at least one temple per day and no stop more than a 20-minute walk from the preceding stop.") -> itinerary_text : STRING
  RETURN itinerary_text
}` — GENERATE represents the requested artifact, but cardinality-per-day and walking-time adjacency remain opaque prose; no proposed change helps.
  - `521aa0aa-e099-4fc9-bb4e-f8a593a29f81` (Mind2Web) [Full] NL: "Find the user reviews for the game "Cyberpunk 2077"" → `ENTRYPOINT FindReviews

TASK FindReviews {
  ACTION search(target="user reviews for Cyberpunk 2077")
}` — The web search action captures the actionable core; proposed register changes are irrelevant.
  - `b770af80-75f0-470c-8797-1466d90c35ce` (Mind2Web) [Full] NL: "Get the cheapest last-minute pet-friendly road trip hotel deal in May for a single person with a pet and book." → `ENTRYPOINT BookHotelDeal

TASK BookHotelDeal {
  ACTION search(target="hotel deals", date="May", quantity=1, options=["pet-friendly", "road trip", "last-minute", "one pet"])
  ACTION sort(target="price", ordering="ascending")
  ACTION click(target="cheapest deal") -> deal : REF[STRING]
  ACTION submit(target=deal)
}` — Existing date, quantity, options, ordering, REF, and ordered Actions encode the task. register_note is irrelevant.
  - `trial_T20190908_153234_664631#2` (ALFRED) [Full] NL: "Put a box with card on the red couch." → `ENTRYPOINT PutBoxOnCouch

TASK PutBoxOnCouch {
  ACTION pick_up(target="box with card") -> box : REF[STRING]
  ACTION place(target=box, destination="red couch")
}` — The REF result preserves the selected box-with-card identity. Proposed changes are irrelevant.
  - `trial_T20190907_160520_516302#1` (ALFRED) [Full] NL: "Put a frying pan with a scoop in the sink." → `ENTRYPOINT PutPanInSink

TASK PutPanInSink {
  ACTION pick_up(target="frying pan with a scoop") -> pan : REF[STRING]
  ACTION place(target=pan, destination="sink")
}` — The requested final placement and identity are represented; navigation details in the trajectory are implementation-level rather than requested outcome.
  - `django__django-16032` (SWE-bench_Verified) [Partial] NL: "__in doesn't clear selected fields on the RHS when QuerySet.alias() is used after annotate()." → `ENTRYPOINT FixDjangoSubquery

TASK FixDjangoSubquery {
  ACTION modify_code(target="django/db/models/fields/related_lookups.py", content="Fix __in RHS selected-field clearing when QuerySet.alias() follows annotate(), preventing a subquery from returning multiple columns.")
  ACTION modify_code(target="django/db/models/sql/query.py", content="Implement the corresponding query-level selected-field handling for the alias-after-annotate subquery case.")
  ACTION run_tests(target="tests/annotations/tests.py")
}` — The files, ordered modifications, and test execution are structured, but the required implementation and regression test remain natural-language payload because the language has no code/change-set semantics. Register changes are irrelevant.
  - `sympy__sympy-11618` (SWE-bench_Verified) [Partial] NL: "distance calculation wrong" → `ENTRYPOINT FixPointDistance

TASK FixPointDistance {
  ACTION modify_code(target="sympy/geometry/point.py", content="Make Point.distance account for unmatched dimensions as zero coordinates so Point(2,0).distance(Point(1,0,2)) evaluates to sqrt(5), rather than ignoring the third coordinate.")
  ACTION run_tests(target="Point.distance")
}` — The actionable files and test action are represented, but exact source-level behavior remains opaque content.
  - `c3930` (PRISM) [Partial] NL: "tell me an adult joke" → `ENTRYPOINT TellAdultJoke

TASK TellAdultJoke : STRING {
  GENERATE(target="joke", content="Tell an adult joke.") -> joke_text : STRING
  RETURN joke_text
}` — The generation intent and artifact are explicit; joke substance legitimately remains prose. "adult" is content category, not a tone/register value.
  - `c10` (PRISM) [Partial] NL: "What is the likely cause of death of the late, great Matthew Perry?" → `ENTRYPOINT AnswerPerryCauseOfDeath

TASK AnswerPerryCauseOfDeath : STRING {
  GENERATE(target="answer", content="Answer what is known about the likely cause of death of Matthew Perry, distinguishing confirmed information from speculation.") -> answer_text : STRING
  RETURN answer_text
}` — The answer request is represented; factual reasoning and prose answer remain payload, as expected for an open question.
  - `c6709` (PRISM) [Partial] NL: "how to deal with a boss is putting too much workload on you" → `ENTRYPOINT AdviseOnWorkload

TASK AdviseOnWorkload : STRING {
  GENERATE(target="advice", content="Give advice for dealing with a boss who is assigning too much workload.") -> advice_text : STRING
  RETURN advice_text
}` — The advice speech goal is represented through an artifact generation; advice substance is legitimate open-item payload.
  - `c1150` (PRISM) [Partial] NL: "If royals breed with their cousins, why is this not seen as incest and why aren't they imprisoned or arrested?" → `ENTRYPOINT ExplainRoyalCousinMarriage

TASK ExplainRoyalCousinMarriage : STRING {
  GENERATE(target="explanation", content="Explain how laws and social definitions regarding cousin marriage apply to royal families, including why criminal penalties may not apply.") -> explanation_text : STRING
  RETURN explanation_text
}` — The explanatory intent is preserved, while legal and historical substance remains prose.
  - `wildchat1m_en3u-22516` (PATHs) [Partial] NL: "hi" → `ENTRYPOINT Greeting

CONVO Greeting {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="hi")
  }
}` — The conversational turn, speaker, speech act, and payload are represented. The short greeting itself is necessarily an opaque content string; proposed register changes are irrelevant.
  - `wildchat1m_en3u-49918` (PATHs) [Partial] NL: "my phd thesis is about “Financial Risk Modelling using time series analysis and machine learning models”. i did following works in my thesis: - market risk modelling (value at risk prediction) using time series analysis and Deep Belief Network. - liquidity risk class prediction (high liquidity vs low liquidity) using different machine learning models (including SVM, RF, KNN, ANN, and LSTM) for 4 crypto currencies (BitCoin, Ethereum, LiteCoin, Cardano). - Money Laundering detection using different machine learning models (including SVM, RF, KNN, ANN, and LSTM) for bitcoin using transaction graph data provided by Elliptic company.describe the aim of this research from scientific view" → `ENTRYPOINT DescribeResearchAim

TASK DescribeResearchAim : STRING {
  GENERATE(target="scientific research aim description", audience="academic", content="Describe the scientific aim of a PhD thesis on financial risk modelling with time-series analysis and machine learning, covering Value-at-Risk prediction using a Deep Belief Network, cryptocurrency liquidity classification using SVM/RF/KNN/ANN/LSTM, and Bitcoin money-laundering detection from Elliptic transaction graphs using those models.") -> aim_text : STRING
  RETURN aim_text
}` — Audience, requested artifact, and scientific framing are represented; the detailed thesis substance is correctly retained as payload. No explicit register word requires tone or register_note.
  - `wildchat1m_en3u-103814` (PATHs) [Partial] NL: "what do you call it when cards run out in solitaire" → `ENTRYPOINT AnswerSolitaireTerm

TASK AnswerSolitaireTerm : STRING {
  GENERATE(target="term", content="Give the short term for when cards run out in solitaire.") -> term_text : STRING
  RETURN term_text
}` — The request for a concise lexical answer is represented, but the answer content remains generative payload.
  - `wildchat1m_en3u-31706` (PATHs) [Partial] NL: "Can you write a hypothetical crossover of Ouran High School Host Club and Fruits Basket, what would the characters interactions be like?" → `ENTRYPOINT WriteCrossover

TASK WriteCrossover : STRING {
  GENERATE(target="crossover story", content="Write a hypothetical crossover of Ouran High School Host Club and Fruits Basket, focusing on likely character interactions.") -> story_text : STRING
  RETURN story_text
}` — Generation intent, artifact type, and requested focus are represented; creative substance properly remains prose.
  - `1776016996729` (ThoughtTrace) [Partial] NL: "Hello" → `ENTRYPOINT Greeting

CONVO Greeting {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="Hello")
  }
}` — The greeting is represented as a user conversational turn. The payload is opaque content by design.
  - `1775769104830` (ThoughtTrace) [Partial] NL: "Hi I need your help. I have an assignment where I need to write a report of about 20 pages. Their topic is about battery energy storage systems in South Africa, technologies and challenges." → `ENTRYPOINT DraftBESSReport

TASK DraftBESSReport : STRING {
  GENERATE(target="university report", format="20 pages", content="Write a report about battery energy storage systems in South Africa, focusing on technologies and challenges.") -> report_text : STRING
  RETURN report_text
}` — Artifact, approximate length, subject, and focus are structured. Report body remains legitimate prose payload; the later trajectory's resource-age and IEEE constraints are not in this sampled NL.
  - `1776011140875` (ThoughtTrace) [Partial] NL: "I want to plan a weekly content and event promotion schedule for my lounge." → `ENTRYPOINT PlanLoungePromotion

TASK PlanLoungePromotion : STRING {
  GENERATE(target="weekly content and event promotion schedule", content="Plan a weekly content and event promotion schedule for a lounge.") -> schedule_text : STRING
  RETURN schedule_text
}` — The schedule artifact and business domain are represented. Exact posts and promotional plan remain prose substance; proposed register support is irrelevant.
  - `1775447480498` (ThoughtTrace) [Partial] NL: "hi i wanna help" → `ENTRYPOINT OfferHelp

CONVO OfferHelp {
  TURN t1 SPEAKER=USER {
    UTTER propose(content="Hi, I want to help.")
  }
}` — The conversational offer, speaker, and speech act are represented. The informal wording is content, not a request for a response register.
- **Cross-check:** used=True, agreement=partial — Providers agree closely on the embodied task, basic searches, and several straightforward GENERATE requests. They diverge on whether open prompts should be represented as TASK/GENERATE or CONVO/UTTER (c3930, c6709, c1150), omit ENTRYPOINT in one greeting translation, and differ sharply on SWE-bench representation, including one raw natural-language fallback; the proposal does not resolve that construct-selection ambiguity.
- **Required changes:**
  - `Action`: Replace the contradictory phrase-level lookup rule with a deterministic extraction grammar. Explicitly state whether translators may identify a standalone register complement in patterns such as "keep it formal", "write professionally", "in a professional tone", and "casually:"; define the result for each pattern and revise all examples to obey it.
  - `Action`: Do not describe the finite synonym list as exhaustive. Either define it as a closed enumerated table of accepted normalized terms, or provide a formally exhaustive morphology/lexicon rule; list the normalized keys unambiguously, including the precise normalization result for hyphenated and concatenated forms.
  - `Action`: Add static validation that every attribute name on ACTION, GENERATE, and UTTER is in the declared canonical vocabulary, or define semantics for extension attributes. The current attr ::= IDENT '=' value permits unknown attributes with no defined meaning.
  - `Generate`: Revise the Generate worked example or the exact-match rule after the phrase-extraction policy is fixed. Under the current rule, "keep it formal" is a larger phrase containing a listed word and cannot validly yield tone="formal".
  - `Utterance`: Revise the Utterance worked example or the exact-match rule after the phrase-extraction policy is fixed. Under the current rule, the source construction "User, casually:" does not establish whether the isolated candidate is "casually" or an impermissibly embedded phrase.
- **Logic issues:** The rule says a phrase merely containing a listed word, including "in a professional tone", must not be partially extracted, but the Generate example maps the phrase "keep it formal" to tone="formal". These are materially analogous cases.; The Utterance example maps the contextual construction "User, casually:" to tone="casual", but the proposal does not define syntactic extraction of register words from contextual clauses or labels.; The table is called exhaustive despite being a finite list of English synonyms and inflections with no formal rule covering unlisted morphology, spelling variants, or synonymous descriptions.; attr ::= IDENT '=' value admits arbitrary attribute names, while only named canonical roles have semantics; the revision adds register_note but does not close this undefined extension path.; The glossary says anything that is not an exact table hit goes to register_note, but a translator cannot deterministically determine the candidate string to test when register is expressed as ordinary natural-language syntax rather than as an isolated token.
- **Decision:** accepted
- **Documenter summary:** The Shaper's proposal added a `register_note` attribute (mutually exclusive with `tone`) plus a normalization/exact-match lookup table for tone, extending the duplicate-attribute static error to UTTER and register_note across Action, GENERATE, and UTTER. The Critic flagged this as needs-rework: the worked examples ('keep it formal' -> tone="formal", 'User, casually:' -> tone="casual") directly contradict the stated exact-match-only rule barring extraction from larger phrases, and the synonym table was called exhaustive despite being a finite non-exhaustive list, leaving translators free to diverge on ordinary phrased register requests. Because this was the third attempt without a clean accept, the change was forced through as accepted despite these unresolved logic issues, which are carried forward as required fixes for a future sprint.
- **Cost this sprint:** $1.6837

## Sprint 4 (attempt 1/3) — 2026-09-23

- **Language version:** 4.0.0 → 4.0.0 (MINOR)
- **Candidate task:** Rinse the mug in the sink, then put it in the coffee maker.
- **Shaper proposal (model: openai/gpt-5.6-terra):** Adds a deterministic normalization rule for the household verb “put” so the candidate request maps consistently to the existing canonical `place` Action. The existing Task source-order and REF binding rules already express the rinse-then-place dependency without a new sequencing primitive.
- **Changes:** `household-verb-normalization` (add, MINOR)
- **Critic decision:** needs-rework — The underlying normalization goal is sound and its simplest intended result is already corroborated by both independent translations, but the proposed construct is not a valid or fully specified BrainCode grammar addition. It introduces undefined grammar symbols and leaves ordinary coordinated and modified uses of “put” without deterministic behavior, while redundantly restating the existing `place` vocabulary. Recasting it as a precise Action translation policy with explicit source-expansion and unsupported-condition rules would likely yield a net determinism benefit without adding a redundant construct.
- **Doc hygiene:** pass — All changes carry a complete glossary entry (gloss + worked example).
- **Pre-KPI assessment:**
  - coverage: neutral — The proposed alias adds no new executable capability: `place` already exists in the normative household Action vocabulary, and coordinated-object requests can already be represented as multiple `place` Actions. It also deliberately excludes routes, orientation, manner, and containment conditions without specifying a representation for them.
  - expressivity: mixed — For the narrow singular form “put X in Y,” the rule preserves the intended transfer relation. However, it has no defined translation for coordinated objects such as the sampled toilet-paper request, pronoun resolution, or the excluded additional movement semantics, so it cannot by itself preserve the meaning of many ordinary uses of “put.”
  - determinism: mixed — Exact lowercased matching would reduce variation for an already-isolated singular `put` predicate, and both independent translations of the sampled toilet-paper item independently chose `place`. But terms such as “main verb,” “one entity,” “selected entity,” and “named location or container” are not operationally defined, while the alias grammar uses undefined nonterminals; translators will still diverge on coordination, phrasal forms, pronouns, and object selection.
  - interpretability: harm — The construct is presented as grammar even though `entity` and `destination` are not defined lexical or syntactic nonterminals, and `=>` is not part of the BrainCode grammar. It also overlaps silently with the pre-existing canonical household operation `place`, making it unclear whether this is user-visible syntax, a translator policy, or an Action semantic rule.
  - improvement: neutral — A weaker model may benefit slightly from being told that singular household “put” maps to `place`, but the current Action vocabulary already supplies that canonical name. The broken and underspecified alias does not add planning structure or improve execution of the sampled household task beyond what the existing ordered Actions and REF binding already provide.
- **Simulated examples:**
  - `held-support-1` (seed_tasks) [Full] NL: "If the customer's order is late and they're a first-time buyer, offer a 10% discount; if they're a repeat buyer, offer free expedited shipping instead." → `ENTRYPOINT HandleLateOrder

TASK HandleLateOrder {
  ACTION check_order_status(target="customer_order") -> is_late : BOOL
  ACTION check_customer_type(target="customer") -> customer_type : STRING
  IF is_late == TRUE AND customer_type == "first_time" THEN {
    ACTION send_message(recipient="customer", content="Offer a 10% discount.", quantity=10, format="percent")
  } ELSE {
    IF is_late == TRUE AND customer_type == "repeat" THEN {
      ACTION send_message(recipient="customer", content="Offer free expedited shipping.", options=["free", "expedited"])
    }
  }
}` — No proposed change is relevant. Ordered checks and nested branches capture both eligibility conditions and the otherwise alternative.
  - `held-trip-1` (seed_tasks) [Partial] NL: "Plan a 3-day itinerary in Kyoto that includes at least one temple per day and avoids anything more than a 20-minute walk from the last stop." → `ENTRYPOINT PlanKyotoItinerary

TASK PlanKyotoItinerary : STRING {
  GENERATE(target="itinerary", content="Plan a 3-day itinerary in Kyoto with at least one temple per day and no leg longer than a 20-minute walk from the preceding stop.", format="3-day") -> itinerary_text : STRING
  RETURN itinerary_text
}` — The overall generation goal and duration are represented, but the per-day temple constraint and predecessor-dependent walking-distance constraint remain opaque prose. No proposed change is relevant.
  - `81fb481b-a234-4e25-b494-9ed26a03e977` (Mind2Web) [Full] NL: "Add the second most popular horror series to my watchlist." → `ENTRYPOINT AddSecondMostPopularHorrorSeries

TASK AddSecondMostPopularHorrorSeries {
  ACTION search(target="horror series", ordering="popularity_desc") -> series : LIST[REF[STRING]]
  ACTION select_filter(target=series, range=[2, 2]) -> selected_series : REF[STRING]
  ACTION click(target=selected_series, content="add to watchlist")
}` — No proposed change is relevant. The rank is represented through the existing inclusive `range` schema and execution order is explicit.
  - `009cc066-87b2-4ebb-ad8f-41eeb3d94be6` (Mind2Web) [Full] NL: "Find a parking with EV charging for month with lowest price in Chicago." → `ENTRYPOINT FindCheapestEVParking

TASK FindCheapestEVParking : REF[STRING] {
  ACTION search(target="parking", destination="Chicago") -> results : LIST[REF[STRING]]
  ACTION apply_filters(target=results, options=["EV charging", "monthly"]) -> filtered : LIST[REF[STRING]]
  ACTION sort(target=filtered, ordering="price_ascending") -> ranked : LIST[REF[STRING]]
  ACTION select_filter(target=ranked, range=[1, 1]) -> cheapest : REF[STRING]
  RETURN cheapest
}` — No proposed change is relevant. Search location, monthly condition, EV requirement, ascending price ordering, and selection of the first ranked result are represented.
  - `trial_T20190908_111502_284228#2` (ALFRED) [Full] NL: "Put an empty roll and a full roll of toilet paper in a drawer." → `ENTRYPOINT PlaceToiletPaperRolls

TASK PlaceToiletPaperRolls {
  ACTION place(target="empty roll of toilet paper", destination="drawer")
  ACTION place(target="full roll of toilet paper", destination="drawer")
}` — The existing `place` Action fully represents the request. The proposed rule is relevant lexically, but does not define how one coordinated `put` clause expands into two Actions; that expansion was supplied independently here.
  - `trial_T20190906_203043_983029#0` (ALFRED) [Full] NL: "Turn the light on with a pencil in hand" → `ENTRYPOINT TurnLightOnWithPencil

TASK TurnLightOnWithPencil {
  ACTION pick_up(target="pencil") -> pencil : REF[STRING]
  ACTION turn_on(target="light", source=pencil)
}` — No proposed change is relevant. Source order and the REF preserve the requirement that the pencil is held when the light is turned on.
  - `sympy__sympy-13372` (SWE-bench_Verified) [Full] NL: "UnboundLocalError in evalf
```

>>> Mul(x, Max(0, y), evaluate=False).evalf()

x*Max(0, y)

>>> Mul(Max(0, y), x, evaluate=False).evalf()

Traceback (most recent call last):

  File "./sympy/core/evalf.py", line 1285, in evalf

    rf = evalf_table[x.func]

KeyError: Max



During handling of the above exception, another exception occurred:

  File "./sympy/core/evalf.py", line 538, in evalf_mul

    arg = evalf(arg, prec, options)

  File "./sympy/core/evalf.py", line 1308, in evalf

    r = re, im, reprec, imprec

UnboundLocalError: local variable 'reprec' referenced before assignment

```

Add an else clause raising NotImplementedError to the elif clauses that define reprec and imprec." → `ENTRYPOINT FixEvalfUnboundLocalError

TASK FixEvalfUnboundLocalError {
  ACTION modify_code(target="sympy/core/evalf.py", content="In the evalf exception-handling path reached by Mul(Max(0, y), x, evaluate=False).evalf(), add an else clause raising NotImplementedError when the elif clauses do not define reprec and imprec; prevent UnboundLocalError for reprec.")
}` — No proposed change is relevant. The code-change target and requested fix are represented in the code Action payload.
  - `matplotlib__matplotlib-25775` (SWE-bench_Verified) [Full] NL: "[ENH]: Add get/set_antialiased to Text objects; adjust Annotations as needed and use per-object state during drawing rather than direct rcParams access." → `ENTRYPOINT AddTextAntialiasedControl

TASK AddTextAntialiasedControl {
  ACTION modify_code(target="lib/matplotlib/text.py", content="Add per-Text-object get_antialiased and set_antialiased methods and store antialiasing state, preserving the rcParams text.antialiased default when unset.")
  ACTION modify_code(target="Annotation", content="Adjust Annotation behavior as needed to expose or inherit Text antialiasing configuration.")
  ACTION modify_code(target="lib/matplotlib/backends/backend_agg.py", content="Use the Text object's antialiasing state through GraphicsContext instead of directly reading rcParams text.antialiased.")
  ACTION modify_code(target="lib/matplotlib/backends/backend_cairo.py", content="Use the Text object's antialiasing state through GraphicsContext instead of directly reading rcParams text.antialiased.")
  ACTION run_tests(target="Text and Annotation antialiasing behavior")
}` — No proposed change is relevant. The requested implementation components and their source order are explicit.
  - `c2734` (PRISM) [Partial] NL: "what do you think about the movie her?" → `ENTRYPOINT ShareOpinionOnHer

TASK ShareOpinionOnHer : STRING {
  GENERATE(target="opinion", content="Share an opinion about the movie Her.") -> opinion_text : STRING
  RETURN opinion_text
}` — The request speech act and intended artifact are represented; the substantive opinion properly remains an opaque generation payload. No proposed change is relevant.
  - `c6978` (PRISM) [Partial] NL: "Why is Fifa the most stressful game ever created?" → `ENTRYPOINT ExplainFifaStress

TASK ExplainFifaStress : STRING {
  GENERATE(target="explanation", content="Explain why FIFA can feel like the most stressful game ever created.") -> explanation_text : STRING
  RETURN explanation_text
}` — The explanatory request is captured, while the explanation itself remains legitimate opaque prose. No proposed change is relevant.
  - `c3594` (PRISM) [Partial] NL: "As someone with Irish heritage, I'm thankful to be able to celebrate St. Patrick's Day. It's one of the few examples of culture I have, after all." → `ENTRYPOINT IrishHeritageReflection

CONVO IrishHeritageReflection {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="As someone with Irish heritage, I'm thankful to be able to celebrate St. Patrick's Day. It's one of the few examples of culture I have, after all.")
  }
}` — The user speaker, reflective informing act, and turn structure are captured; the personal reflection is appropriately opaque. No proposed change is relevant.
  - `c7766` (PRISM) [Partial] NL: "Can you tell me how Donald Trump has been compromised by the Russians?" → `ENTRYPOINT ExplainTrumpRussiaQuestion

TASK ExplainTrumpRussiaQuestion : STRING {
  GENERATE(target="explanation", content="Explain, with appropriate evidentiary qualifications, allegations that Donald Trump has been compromised by Russia.") -> explanation_text : STRING
  RETURN explanation_text
}` — The request for an explanation is represented, but the factual discussion and evidentiary answer remain opaque prose. No proposed change is relevant.
  - `wildchat1m_en3u-123659` (PATHs) [Full] NL: "hi" → `ENTRYPOINT Greeting

CONVO Greeting {
  TURN t1 SPEAKER=USER {
    UTTER greet(content="hi")
  }
}` — The greeting speech act and user role are fully captured; there is no substantive prose payload needing decomposition. No proposed change is relevant.
  - `wildchat1m_en3u-63060` (PATHs) [Partial] NL: "Audacity Data Collection for what " → `ENTRYPOINT AskAboutAudacityDataCollection

CONVO AskAboutAudacityDataCollection {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Audacity data collection for what?")
  }
}` — The interrogative speech act is captured, but the terse question's intended technical scope remains opaque and underspecified. No proposed change is relevant.
  - `wildchat1m_en3u-27410` (PATHs) [Partial] NL: "Tyler - A loyal and dependable boy who is always there for his friends. He’s very empathetic and can often sense when someone is feeling down or upset. He’s always willing to lend a listening ear or a shoulder to cry on. He’s like SpongeBob from seasons 4-11, always thinking of others." → `ENTRYPOINT DescribeTyler

CONVO DescribeTyler {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="Tyler is a loyal, dependable, empathetic boy who supports his friends and is always thinking of others, like SpongeBob in seasons 4-11.")
  }
}` — The source is a character-description contribution rather than an explicit executable command; its communicative act is captured while the descriptive substance remains opaque. No proposed change is relevant.
  - `wildchat1m_en3u-153587` (PATHs) [Partial] NL: "Paraphrase this: I tried to call him and send message to him to Whatsapp. Let's wait until end of the week for IT Dept to sign clearnce." → `ENTRYPOINT ParaphraseMessage

TASK ParaphraseMessage : STRING {
  GENERATE(target="paraphrase", content="Paraphrase: I tried to call him and send message to him to Whatsapp. Let's wait until end of the week for IT Dept to sign clearnce.") -> paraphrased_text : STRING
  RETURN paraphrased_text
}` — The transformation intent and exact source payload are represented; the rewritten wording is correctly left to generation. No proposed change is relevant.
  - `1775481045096` (ThoughtTrace) [Partial] NL: "Can you explain 'Data Lakehouse' to me in very simple terms, as if I am a beginner?" → `ENTRYPOINT ExplainDataLakehouse

TASK ExplainDataLakehouse : STRING {
  GENERATE(target="explanation", audience="beginner", register_note="very simple terms", content="Explain Data Lakehouse.") -> explanation_text : STRING
  RETURN explanation_text
}` — The explanatory intent, audience, and beginner-level register are represented; the technical explanation remains opaque prose. No proposed change is relevant.
  - `1776049553182` (ThoughtTrace) [Full] NL: "hello good night" → `ENTRYPOINT Greeting

CONVO Greeting {
  TURN t1 SPEAKER=USER {
    UTTER greet(content="hello good night")
  }
}` — The greeting act and speaker are fully captured. No proposed change is relevant.
  - `1775430980541` (ThoughtTrace) [Partial] NL: "I need help planning a daily study schedule to manage my time better" → `ENTRYPOINT PlanStudySchedule

TASK PlanStudySchedule : STRING {
  GENERATE(target="daily study schedule", content="Help plan a daily study schedule to manage time better.") -> schedule_text : STRING
  RETURN schedule_text
}` — The planning request and requested artifact are represented; the actual personalized schedule remains an appropriate generation payload. No proposed change is relevant.
  - `1775951181610` (ThoughtTrace) [Partial] NL: "Hi, can you help me create a plan of my daily routine" → `ENTRYPOINT CreateDailyRoutinePlan

TASK CreateDailyRoutinePlan : STRING {
  GENERATE(target="daily routine plan", content="Help create a plan for my daily routine.") -> routine_plan : STRING
  RETURN routine_plan
}` — The requested planning artifact and intent are represented; the individualized routine content remains opaque. No proposed change is relevant.
- **Cross-check:** used=True, agreement=partial — The two providers agree on canonical `place` for the sampled coordinated toilet-paper request, supporting the proposal's narrow motivation. However, they diverge broadly between TASK/CONVO representations and Action choices; several supplied expressions are syntactically incomplete or invalid under the current spec (for example, missing ENTRYPOINT declarations, list indexing not in the grammar, and incomplete braces), so they do not establish convergence for the proposed rule beyond its simplest lexical case.
- **Required changes:**
  - `household-verb-normalization`: Replace the pseudo-grammar `household_transfer_alias ::= "put" "(" entity "," destination ")" => ...` with a clearly labeled translation policy under Action, or formally add and define every referenced nonterminal and the `=>` rewrite notation. Do not present a source-language normalization policy as executable BrainCode grammar.
  - `household-verb-normalization`: Define an operational source parsing policy for the verb head, phrasal variants, pronouns/coreference, coordinated direct objects, and coordinated destinations. State explicitly whether one coordinated source clause expands left-to-right into multiple `ACTION place` statements, and give a worked example for “Put an empty roll and a full roll of toilet paper in a drawer.”
  - `Action`: Integrate the canonical mapping as an Action translation-selection rule: normalized source predicate `put` with exactly one resolved movable entity and one resolved destination maps to existing `ACTION place(target=..., destination=...)`. State that this is not a new BrainCode construct and remove the redundant standalone construct name.
  - `household-verb-normalization`: Replace the undefined exclusion phrase “additional movement semantics” with a deterministic disposition rule: either specify which existing attributes encode route/orientation/containment, or require a translator to emit separate supported Actions plus an explicit opaque content payload for any remaining unsupported condition.
- **Logic issues:** The proposed grammar references undefined `entity` and `destination` nonterminals, and `=>` is not defined anywhere in the BrainCode grammar.; The proposal calls itself a translation-only lexical rule but supplies syntax that looks like a new BrainCode production, leaving its status and parse behavior ambiguous.; “Exact normalized main verb” is undefined for common forms such as “put away,” “put down,” coordinated predicates, ellipsis, and passive constructions.; The rule requires one entity, but the sampled request has two coordinated entities under one `put`; no expansion rule specifies whether it emits one invalid plural target, two Actions, or no alias.; “Selected entity” incorrectly suggests a resolved REF even though the stated rule permits a source entity descriptor and does not define entity resolution.; The standalone construct overlaps with the existing normative household Action vocabulary, which already identifies `place` as canonical.
- **Decision:** needs-rework
- **Documenter summary:** The Shaper proposed a new 'household-verb-normalization' construct mapping the source verb 'put' to the canonical `place` Action, citing Parsel-style deterministic decomposition. The Critic ruled needs-rework, finding the proposed grammar used undefined nonterminals (entity, destination) and an undefined '=>' rewrite notation, and left coordinated objects, phrasal verbs, and pronoun resolution unspecified—most decisively, the sampled ALFRED toilet-paper item showed the rule had no defined expansion for a single 'put' clause with two coordinated entities, so the Critic required recasting it as a precisely specified Action translation policy rather than a standalone construct.
- **Cost this sprint:** $1.3067

## Sprint 4 (attempt 2/3) — 2026-09-23

- **Language version:** 4.0.0 → 4.0.0 (PATCH)
- **Candidate task:** Rinse the mug in the sink, then put it in the coffee maker.
- **Shaper proposal (model: openai/gpt-5.6-terra):** This revision places deterministic household “put” normalization inside the existing Action translation policy rather than adding redundant executable syntax. It defines source parsing, coreference, coordination expansion, and a precise fallback for unsupported placement details while preserving ordered REF-based state flow.
- **Changes:** `Action` (revise, PATCH)
- **Critic decision:** needs-rework — The core idea is sound: normalize ordinary household bare put into the existing place Action and expand coordinated targets in source order rather than adding redundant executable syntax. It provides a real improvement for a subset of household tasks and preserves useful identity/order structure, but the revised Action entry has a dangling normative dependency and several undefined parsing and REF-binding choices that prevent deterministic translation. These are concrete documentation-policy defects rather than a reason to reject the approach, so rework is required before acceptance.
- **Doc hygiene:** pass — All changes carry a complete glossary entry (gloss + worked example).
- **Pre-KPI assessment:**
  - coverage: mixed — The change improves coverage for ordinary household placement requests, coordinated direct objects, and anaphoric follow-on placements. However, it deliberately turns plausible placement forms such as one target with multiple destinations into translation failures, and the sampled ALFRED tasks still require unsupported navigation, examination, lighting, and retrieval actions.
  - expressivity: benefit — For the supported bare-put subset, the proposal preserves target, destination, source order, paired coordination, route, and residual placement conditions more faithfully than an unconstrained translator choice between put and place. The residual-condition policy is useful, but its assertion that residual text is both exact and potentially minimally paraphrased is not fully consistent.
  - determinism: mixed — Exact lexical-lemma eligibility, left-to-right expansion, count-based pairing, and failure rather than guessed pronoun resolution are strong deterministic constraints. But the policy relies on undefined predicate parsing, entity-role compatibility, concrete-placement resolution, and an implicit decision to bind prior Action results, so capable translators can still disagree on whether a clause qualifies and whether a REF must be introduced.
  - interpretability: mixed — Using the existing place Action rather than a redundant new syntax is compact and understandable, and the worked example is readable. Yet this revise operation appears to replace the existing Action entry while referring to an "existing canonical-label and synonym table" that is no longer included in the proposed grammar; this leaves a normative dependency undefined unless the prior table is explicitly retained.
  - improvement: benefit — Ordered place Actions and REF identity improve execution planning for household tasks, especially rinse-then-place and plural object placement. The policy provides useful failure behavior rather than silently inventing object/destination pairings, although unsupported ALFRED action primitives still prevent an executor from completing several sampled household tasks.
- **Simulated examples:**
  - `dev-email-1` (seed_tasks) [Partial] NL: "Draft a reply to my professor asking for a two-day extension on the assignment, and keep it formal." → `ENTRYPOINT DraftExtension

TASK DraftExtension : STRING {
  GENERATE(target="reply", audience="professor", tone="formal", content="ask for a two-day extension on the assignment") -> draft_text : STRING
  RETURN draft_text
}` — Open artifact-generation request; GENERATE preserves artifact, audience, formal register, and request structure, while the reply substance remains an intended prose payload. The proposed put policy is irrelevant.
  - `dev-email-2` (seed_tasks) [Full] NL: "If my manager hasn't replied by Friday, send a polite follow-up; otherwise do nothing." → `ENTRYPOINT FollowUpManager

TASK FollowUpManager {
  ACTION check_reply_status(target="manager", date="Friday") -> replied : BOOL
  IF NOT replied THEN {
    ACTION send_email(recipient="manager", tone="polite", content="follow-up")
  }
}` — The conditional, deadline, recipient, register, and no-op false branch are represented. The proposed change is irrelevant.
  - `85bd1881-6efd-458d-97c9-ae507ecba1ca` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Find the odds for upcoming NHL matches." → `ENTRYPOINT FindNHLOdds

TASK FindNHLOdds {
  ACTION open(target="Odds")
  ACTION click(target="NHL")
  ACTION click(target="GAMES")
}` — The observed finite web trajectory is represented in order. The put normalization is irrelevant.
  - `fdc94e3a-caa3-42b0-aa1b-b99f728f6292` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Schedule a demo drive for Model Y for Roy Adams with phone number 123-999-0000, email address RA@gmail.com and zip code 90001 in the United States." → `ENTRYPOINT ScheduleDemoDrive

TASK ScheduleDemoDrive {
  ACTION click(target="Demo Drive")
  ACTION click(target="Model Y")
  ACTION fill_field(target="Last Name", content="Adams")
  ACTION fill_field(target="First Name", content="Roy")
  ACTION fill_field(target="Phone Number", content="123-999-0000")
  ACTION fill_field(target="Email Address", content="RA@gmail.com")
  ACTION fill_field(target="Zip Code", content="90001")
  ACTION submit(target="demo drive form", content="United States")
}` — The requested model and all supplied form fields are represented in trajectory order. The proposed change is irrelevant.
  - `trial_T20190907_001607_953024#2` (ALFRED (json_2.1.0, train)) [Fail] NL: "Cook an egg in the microwave" → `ENTRYPOINT CookEgg

TASK CookEgg {
  ACTION pick_up(target="egg") -> egg : REF[STRING]
  ACTION place(target=egg, destination="microwave")
  ACTION heat(target=egg, destination="microwave")
  ACTION place(target=egg, destination="sink")
}` — The proposed policy supports the two bare put clauses and makes egg identity explicit, but the actionable trajectory also requires navigation, opening/closing access where applicable, and taking the cooked egg back from the microwave; no canonical operation represents retrieval or navigation. Thus the closed actionable core is incomplete.
  - `trial_T20190908_115833_802764#2` (ALFRED (json_2.1.0, train)) [Fail] NL: "Examine a pillow by the light of a small lamp." → `ENTRYPOINT ExaminePillow

TASK ExaminePillow {
  ACTION pick_up(target="purple pillow") -> pillow : REF[STRING]
  ACTION examine(target=pillow, source="small lamp")
}` — Neither examine nor turning on a lamp is in the household operation vocabulary, and no defined attribute expresses that the lamp must be illuminated. The put policy is irrelevant.
  - `pydata__xarray-4094` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "to_unstacked_dataset broken for single-dim variables. Expected output: a working roundtrip." → `ENTRYPOINT FixUnstackedDataset

TASK FixUnstackedDataset {
  ACTION modify_code(target="xarray/core/dataarray.py", content="Fix to_unstacked_dataset so a Dataset with single-dimension variables can round-trip through to_stacked_array and to_unstacked_dataset without MergeError.")
  ACTION run_tests(target="xarray", content="Verify the single-dimension stacked/unstacked roundtrip.")
}` — The finite code-change and verification task is represented; detailed patch substance is appropriately carried as the code-action payload. The proposed household policy is irrelevant.
  - `django__django-13410` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "Bug in posix implementation of django/core/files/locks.py: fcntl.flock returns None on success, so lock and unlock always return False." → `ENTRYPOINT FixPosixLocks

TASK FixPosixLocks {
  ACTION modify_code(target="django/core/files/locks.py", content="For the POSIX fcntl implementation, make lock and unlock return TRUE after successful fcntl.flock and return FALSE when fcntl.flock raises OSError.")
  ACTION run_tests(target="django/core/files/locks.py", content="Verify successful and failing non-blocking lock and unlock return values.")
}` — The requested file, behavioral change, error branch, and validation are preserved. The proposed household policy is irrelevant.
  - `c2781` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "House prices in NZ are too high." → `ENTRYPOINT NZHousingDiscussion

CONVO NZHousingDiscussion {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="House prices in NZ are too high.")
  }
}` — The conversational speech act and ordering are represented; the policy opinion remains deliberately opaque prose. The put policy is irrelevant.
  - `c7019` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Where can I find resources to learn soldering?" → `ENTRYPOINT FindSolderingResources

CONVO FindSolderingResources {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Where can I find resources to learn soldering?")
  }
}` — The user question is structurally represented, while the requested recommendations are open prose substance. The proposed change is irrelevant.
  - `c6980` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "What is the best way to reduce cholestorol levels?" → `ENTRYPOINT CholesterolAdvice

CONVO CholesterolAdvice {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="What is the best way to reduce cholesterol levels?")
  }
}` — The advice-seeking speech act is represented; medical explanation and recommendations are appropriately retained as prose payload. The proposed change is irrelevant.
  - `c6073` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "how do we stop gender based violence" → `ENTRYPOINT PreventGenderBasedViolence

CONVO PreventGenderBasedViolence {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="How do we stop gender-based violence?")
  }
}` — The request for prevention advice is represented; the substantive policy response is open prose. The proposed change is irrelevant.
  - `wildchat1m_en3u-63477` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "give me the 7 pages long argument to support the following motion of the opposition: It is impossible technically to rely upon any other currency so the dominance of US dollar will prevail." → `ENTRYPOINT GenerateCurrencyArgument

TASK GenerateCurrencyArgument : STRING {
  GENERATE(target="argument", format="7 pages", content="Support the opposition motion: It is impossible technically to rely upon any other currency, so the dominance of the US dollar will prevail.") -> argument_text : STRING
  RETURN argument_text
}` — Artifact type, requested length, stance, and motion are preserved; the seven-page argument itself is valid opaque generation content. The proposed change is irrelevant.
  - `wildchat1m_en3u-47175` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0301)) [Partial] NL: "Help me write an email to announce a migration, including the supplied migration details and responsibilities." → `ENTRYPOINT DraftMigrationAnnouncement

TASK DraftMigrationAnnouncement : STRING {
  GENERATE(target="email", audience="migration stakeholders", content="Announce migration of Euclid/BFC layers from SwitchBuilder to ProvisioningOrchestrator. Include prerequisites, topology rollout, regional FabricBuilder configuration, deployment and Fabby requirements, and responsibilities for DPS, Cstar-DPS, and NDCS from the supplied details.") -> email_text : STRING
  RETURN email_text
}` — The artifact, audience, announcement intent, and requested responsibility section are captured; the lengthy technical source text remains generation payload. The proposed change is irrelevant.
  - `wildchat1m_en3u-52190` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "write dialogue from a scene from the animated teen series Jane, despite what Jane’s mother said, her father is already driving to adopt a girl named Frankie, disguising it as a fancy restaurant visit, they eventually arrive, with Jane’s mother screaming about the truth" → `ENTRYPOINT GenerateJaneScene

TASK GenerateJaneScene : STRING {
  GENERATE(target="dialogue scene", format="animated teen-series script", content="Write a scene from Jane: despite Jane's mother's objections, Jane's father drives to adopt Frankie while disguising the trip as a fancy restaurant visit; they arrive and Jane's mother screams about the truth.") -> scene_text : STRING
  RETURN scene_text
}` — The requested script format, characters, causal setup, sequence, and dramatic condition are represented; dialogue prose is intentionally opaque. The put policy is irrelevant.
  - `wildchat1m_en3u-53640` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "Give a Longer Description Backstory about Billy Cranston/Blue Ranger meeting Scooby-Doo Mystery Incorporated characters, where everyone knows he is the Blue Ranger and he is a shy genius with listed skills." → `ENTRYPOINT GenerateBillyBackstory

TASK GenerateBillyBackstory : STRING {
  GENERATE(target="character backstory", format="long description", content="Write a crossover backstory about Billy Cranston, the Blue Ranger, meeting Scooby-Doo Mystery Incorporated characters. Everyone knows his Ranger identity; portray him as a shy genius with high intelligence, fighting skills, mechanical intuition, spear proficiency, marksmanship, and powers, and include his developing relationship with Velma.") -> backstory_text : STRING
  RETURN backstory_text
}` — The requested artifact, franchise crossover, identity condition, persona, capabilities, and relationship requirement are captured. The actual backstory remains appropriate generation payload.
  - `1776011140875` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "I want to plan a weekly content and event promotion schedule for my lounge." → `ENTRYPOINT PlanLoungePromotion

TASK PlanLoungePromotion : STRING {
  GENERATE(target="weekly content and event promotion schedule", content="Create a weekly content and event promotion schedule for my lounge.") -> schedule_text : STRING
  RETURN schedule_text
}` — The planning artifact and weekly scope are represented, but the requested strategy is open prose. The proposed household normalization is irrelevant.
  - `1775977647563` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "planning on getting a new car" → `ENTRYPOINT PlanCarPurchase

TASK PlanCarPurchase : STRING {
  GENERATE(target="car-purchase plan", content="Help plan the purchase of a new car, including needs assessment, budget, research, test driving, financing, and buying steps.") -> plan_text : STRING
  RETURN plan_text
}` — The planning intent and principal decision stages are represented, while personalized advice remains prose payload. The proposed change is irrelevant.
  - `1775484928675` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "This is much better. I don't like places with too many tourists. Where is a real local restaurant near the Colosseum to eat good Carbonara pasta?" → `ENTRYPOINT FindCarbonaraRestaurant

TASK FindCarbonaraRestaurant : STRING {
  GENERATE(target="restaurant recommendation", content="Recommend a genuinely local, low-tourist restaurant near the Colosseum for good carbonara pasta.") -> recommendation_text : STRING
  RETURN recommendation_text
}` — The recommendation artifact, location, desired dish, and anti-tourist constraint are captured. Current local knowledge and recommendation prose remain opaque. The proposed change is irrelevant.
  - `1776019500863` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "What about Israel or Jordan?" → `ENTRYPOINT CompareIsraelJordan

CONVO CompareIsraelJordan {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Compare Israel and Jordan as June travel alternatives, considering current safety risks, weather, cost, and suitability for European travelers.")
  }
}` — The follow-up comparison intent and the salient context-dependent criteria are represented; current travel advice remains open prose and requires live information. The proposed change is irrelevant.
- **Cross-check:** used=False, agreement=n/a — No independent translations were supplied. Simulated convergence is high for the sampled web, email, and ordinary single-object placement forms, but only partial for household put cases because models may differ on syntactic coordination, antecedent compatibility, phrasal-versus-bare put classification, and whether a preceding entity-selecting Action must receive a REF binding.
- **Required changes:**
  - `Action`: When revising Action, explicitly retain the complete prior normative tone vocabulary, normalization procedure, and exact synonym/translation-selection table, or move that table to a separately named normative shared construct and update Action, Generate, and Utterance to reference it. Do not leave "existing canonical-label and synonym table" as an undefined dependency after replacement.
  - `Action`: Define a normative parse and resolution boundary for put normalization: state what parser/analysis determines lexical head, direct-object conjuncts, destination conjuncts, entity-role compatibility, and a concrete placement relation. Define whether coordination inside noun phrases, shared modifiers, and coordinated prepositional phrases count as flattenable conjuncts.
  - `Action`: Make REF introduction mandatory and explicit when a later pronoun requires identity preservation: specify that an eligible earlier household Action selecting a STRING target MUST bind `-> name : REF[STRING]`, provide the deterministic generated name or require a translator-chosen nonsemantic name under a stated naming rule, and require the later place target to use that REF.
  - `Action`: Resolve the residual-text contradiction by choosing one rule: residual placement conditions must be copied exactly, or define a canonical minimal-paraphrase algorithm. Replace the current combination of "exact residual condition" and "verbatim or minimally paraphrased."
  - `Action`: Replace the dangling reference to a "residual-condition rule below" for phrasal or idiomatic put forms with a precise rule stating when a resolved placement relation permits `place(..., content=...)`, and what exact content is emitted.
- **Logic issues:** The proposed revised Action grammar omits the current tone normalization and synonym table while its semantics relies on an "existing" table. If revise replaces the entry as specified, the table has no normative definition.; The pronoun rule permits use of a REF only if an antecedent was already bound, but the policy does not require the translator to bind an entity-selecting prior Action even when a later pronoun depends on identity. This leaves `Rinse a mug, then put it in the coffee maker` underdetermined between a descriptor and a REF representation.; Terms central to eligibility and failure behavior—"predicate structure", "compatible in number and entity role", "concrete placement relation", and "resolved" conjunct—are not operationally defined, so translators can produce different outcomes before the deterministic pairing rules apply.; The residual-condition rule says unsupported conditions are preserved as the exact residual condition, while the register/residual description elsewhere allows content to be carried verbatim or minimally paraphrased; this does not define one canonical output.; The worked example is valid and matches the plural-target/single-destination expansion rule, but it does not exercise the claimed REF-based state flow or demonstrate the mandatory behavior needed for pronoun resolution.
- **Decision:** needs-rework
- **Documenter summary:** The Shaper proposed folding household 'put' normalization into the existing Action construct (mapping bare 'put X in Y' to canonical 'place', with rules for coordination, pronoun/REF resolution, and residual conditions) rather than adding a new syntax. The Critic sent it back for rework: the revised Action entry drops the existing tone/synonym table it still references as 'existing', leaves REF-binding for pronoun resolution optional rather than mandatory (leaving 'Rinse a mug, then put it in the coffee maker' underdetermined), and contains an unresolved contradiction between 'exact' and 'minimally paraphrased' residual content — these undefined dependencies and parsing/REF-binding gaps, not the core normalization idea, drove the needs-rework decision.
- **Cost this sprint:** $0.2552

## Sprint 4 (attempt 3/3) — 2026-09-23

- **Language version:** 4.0.0 → 4.0.1 (PATCH)
- **Candidate task:** Rinse the mug in the sink, then put it in the coffee maker.
- **Shaper proposal (model: openai/gpt-5.6-terra):** This revision makes ordinary household requests using plain "put" deterministically normalize to the existing `place` Action while preserving sequential identity flow through mandatory REF bindings. It also retains Action's complete register normalization rules and defines explicit syntactic-analysis, coordination, pronoun, and residual-condition boundaries.
- **Changes:** `Action` (revise, PATCH)
- **Critic decision:** needs-rework — [Forced acceptance after 3 attempt(s) without a clean accept — the required changes below are known issues carried forward for a future sprint to address, not resolved.] The core normalization idea is useful and improves explicit state flow for the sampled household pronoun cases. It cannot be accepted because the claimed deterministic policy delegates decisive behavior to unspecified dependency analyses and contains an internally problematic coordination definition. The required edits are localized and preserve the patch's basic design, so this is rework rather than rejection.
- **Doc hygiene:** pass — All changes carry a complete glossary entry (gloss + worked example).
- **Pre-KPI assessment:**
  - coverage: mixed — The patch improves coverage for a narrow but common household form, including the sampled rinse-then-put and remote-on-couch tasks. However, it deliberately turns ordinary placement clauses into translation failures whenever a UD analysis is unavailable, competing, or does not match its narrowly prescribed attachment pattern, so it can reduce usable coverage across parsers and household phrasings.
  - expressivity: benefit — The generated REF rule preserves selected-object identity in the sampled pronoun case, and target/destination pairing preserves coordinated placement ordering. Residual-condition copying is intended to preserve modifiers, but its selection boundary is not sufficiently defined to guarantee that all meaningful placement modifiers are retained.
  - determinism: mixed — Canonicalizing bare `put` to `place`, requiring source-order pairing, and reserving generated `ref_N` names reduce variation for simple cases. Determinism remains weak because UD analyses may differ across parsers, the proposal does not specify a normative parser or tie-breaking algorithm, and its destination-coordination definition conflicts with common UD coordination attachment.
  - interpretability: mixed — A reader can understand `place(target=ref_1, destination="coffee_maker")` and its identity flow clearly. The Action entry is now disproportionately large and embeds parser-specific source-analysis policy, exact byte-substring rules, and unclear modifier-selection rules in one construct; this makes the language harder to implement and audit.
  - improvement: benefit — For the embodied examples, explicit selected-entity bindings give a weaker model an actionable state-flow plan instead of relying on pronoun resolution from raw prose. The benefit is limited to simple household placement because failures caused by parser variation provide no recoverable plan.
- **Simulated examples:**
  - `dev-email-2` (seed_tasks) [Full] NL: "If my manager hasn't replied by Friday, send a polite follow-up; otherwise do nothing." → `ENTRYPOINT FollowUpManager
TASK FollowUpManager {
  ACTION check_reply_status(target="manager", date="Friday") -> replied : BOOL
  IF NOT replied THEN {
    ACTION send_email(recipient="manager", tone="polite", content="follow-up")
  }
}` — No proposed placement rule is relevant. Existing Flow-If, Action, and tone normalization express the condition and effect.
  - `dev-embodied-1` (seed_tasks) [Full] NL: "Rinse the mug in the sink, then put it in the coffee maker." → `ENTRYPOINT RinseThenPlace
TASK RinseThenPlace {
  ACTION rinse(target="mug", destination="sink") -> ref_1 : REF[STRING]
  ACTION place(target=ref_1, destination="coffee_maker")
}` — The patch directly helps: `put` normalizes to `place`, and the pronoun requires the generated REF binding.
  - `2f660153-d470-4744-8b75-f8dc64c7f94e` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Explore Games & Puzzles in the Toys category that are suitable for ages 14+" → `ENTRYPOINT ExploreGames
TASK ExploreGames {
  ACTION open(target="Toys")
  ACTION open(target="Games & Puzzles")
  ACTION select_filter(target="Age", options=["14+"])
}` — The web-operation vocabulary and structured filter option express the actionable core. The put-normalization patch is irrelevant.
  - `f75e33a6-d7d6-4eea-9ac8-f47be0224114` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Find the score of the 2020 Super Bowl." → `ENTRYPOINT FindSuperBowlScore
TASK FindSuperBowlScore {
  ACTION open(target="Scores")
  ACTION select_filter(target="season", options=["2020"])
}` — The request is representable through structured web navigation. The proposed change is irrelevant.
  - `trial_T20190909_000505_338579#2` (ALFRED (json_2.1.0, train)) [Full] NL: "Place a heated slice of tomato in the kitchen sink." → `ENTRYPOINT HeatTomatoSliceAndPlace
TASK HeatTomatoSliceAndPlace {
  ACTION slice(target="tomato") -> tomato_slice : REF[STRING]
  ACTION heat(target=tomato_slice, destination="microwave")
  ACTION place(target=tomato_slice, destination="kitchen_sink")
}` — Existing household operations express the decomposition and REF identity. The patch is not needed because the source verb is `Place`, not bare `put`.
  - `trial_T20190908_005450_787345#0` (ALFRED (json_2.1.0, train)) [Full] NL: "Take the remote from the table, put it on the couch" → `ENTRYPOINT MoveRemote
TASK MoveRemote {
  ACTION pick_up(target="remote", source="table") -> ref_1 : REF[STRING]
  ACTION place(target=ref_1, destination="couch")
}` — The patch helps by normalizing bare `put` and requiring identity preservation for `it`.
  - `matplotlib__matplotlib-25332` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "[Bug]: Unable to pickle figure with aligned labels. Pickling fails after fig.align_labels() with TypeError: cannot pickle weakref.ReferenceType; expected outcome is successful pickling." → `ENTRYPOINT FixPickleAlignedLabels
TASK FixPickleAlignedLabels {
  ACTION modify_code(target="lib/matplotlib/cbook.py", content="Fix figure pickling after align_labels() so weakref.ReferenceType does not prevent pickle.dumps(fig).")
  ACTION run_tests(target="pickle figure with aligned labels regression")
}` — Code modification and verification are represented structurally; detailed reproduction remains an instruction payload. The patch is irrelevant.
  - `django__django-15103` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "Make the element_id argument of json_script optional." → `ENTRYPOINT MakeJsonScriptElementIdOptional
TASK MakeJsonScriptElementIdOptional {
  ACTION modify_code(target="django/template/defaultfilters.py", content="Make json_script element_id optional.")
  ACTION modify_code(target="django/utils/html.py", content="Support json_script without an element_id while preserving existing behavior.")
  ACTION run_tests(target="json_script optional element_id")
}` — The named files, required behavior, and validation action are expressible. The patch is irrelevant.
  - `c1337` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "What do you think are the consequences of the radical religion on people?" → `ENTRYPOINT DiscussReligiousExtremism
TASK DiscussReligiousExtremism : STRING {
  GENERATE(target="answer", audience="user", content="Discuss potential consequences of religious extremism for people; avoid treating an entire religion as homogeneous.") -> answer : STRING
  RETURN answer
}` — The open-question intent, audience, and requested answer are captured; the substantive analysis remains an appropriate opaque generation payload. The proposed placement rule is irrelevant.
  - `c6805` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "do females like a guy with a big butt?" → `ENTRYPOINT DiscussAttractionPreferences
TASK DiscussAttractionPreferences : STRING {
  GENERATE(target="answer", audience="user", content="Answer whether attraction to a man with a large butt varies among women; explain that preferences are individual.") -> answer : STRING
  RETURN answer
}` — The question and recipient are formalized, while the answer's prose substance remains in content as intended for open requests. The patch is irrelevant.
  - `c2555` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Do people who argue against tropicalized food businesses in their countries of origin have valid arguments about cultural appropriation and gentrification?" → `ENTRYPOINT AssessFoodBusinessArguments
TASK AssessFoodBusinessArguments : STRING {
  GENERATE(target="balanced analysis", audience="user", content="Assess arguments concerning cultural appropriation, local food businesses, and gentrification in the described examples; distinguish facts, assumptions, and competing perspectives.") -> answer : STRING
  RETURN answer
}` — The request for balanced assessment and its subject are captured. The underlying argument remains an opaque prose payload, which is appropriate for this open item.
  - `c7348` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "My son and his wife have decided to get a divorce. They have two small children together. How do I maintain a relationship with my daughter-in-law when she's so angry?" → `ENTRYPOINT GiveFamilyRelationshipAdvice
TASK GiveFamilyRelationshipAdvice : STRING {
  GENERATE(target="advice", audience="user", tone="reassuring", content="Give compassionate practical advice for maintaining a relationship with an angry daughter-in-law during a divorce involving young children, while respecting boundaries and avoiding taking sides.") -> advice : STRING
  RETURN advice
}` — The advice intent, affected relationship, audience, and reassuring register are captured. The patch is irrelevant.
  - `wildchat1m_en3u-123553` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-1106-preview)) [Partial] NL: "Act as the collective persona Ed and write advanced prompts for real-world FP&A, budgeting, and strategic-finance tasks for a Director reporting to a COO, using an Advanced Prefixes for Turn-by-Turn Directions method." → `ENTRYPOINT GenerateFPAAdvancedPrompts
TASK GenerateFPAAdvancedPrompts : STRING {
  GENERATE(target="advanced prompt set", audience="FP&A Director reporting to COO", register_note="pragmatic, detailed, technically expert, and no-nonsense", format="Advanced Prefixes for Turn-by-Turn Directions", content="Create advanced prompts for real-world FP&A, budgeting, strategic-finance tasks, responsibilities, modeling, data analysis, and processes, using the requested composite Ed persona.") -> prompts : STRING
  RETURN prompts
}` — Intent, target artifact, audience, required method, and multi-facet register are captured. The long persona and prompt substance remain generation payload.
  - `wildchat1m_en3u-102123` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "rewrite this Dear Colleagues, ... Please contact us if you have any concerns or requests. We want to create a supportive and caring work environment for you." → `ENTRYPOINT RewriteWellbeingEmail
TASK RewriteWellbeingEmail : STRING {
  GENERATE(target="rewritten employee wellbeing email", audience="colleagues", tone="reassuring", content="Rewrite the supplied employee-support email while preserving its information about HR and supervisor support, leave, counselling support, the named counsellor and contact details, and the invitation to raise concerns.") -> email : STRING
  RETURN email
}` — The rewrite intent, recipient, reassuring register, and preservation constraints are captured. The full supplied email remains an opaque source-text payload; a complete production expression would carry that full text in content.
  - `wildchat1m_en3u-75243` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Full] NL: "hi" → `ENTRYPOINT Greeting
CONVO Greeting {
  TURN t1 SPEAKER=USER {
    UTTER acknowledge(content="hi", recipient="agent")
  }
}` — A greeting is fully represented as a conversational speech act. The patch is irrelevant.
  - `wildchat1m_en3u-134066` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-1106-preview)) [Partial] NL: "Reduce this paragraph to 1000 characters [long review of the Hanger Lane McDonald's handling an autistic child's lactose-sensitive order]." → `ENTRYPOINT SummarizeRestaurantReview
TASK SummarizeRestaurantReview : STRING {
  GENERATE(target="summary", audience="review readers", format="maximum 1000 characters", content="Summarize the supplied review while preserving the Hanger Lane location, incorrect allergy-sensitive order, autistic child's distress, dismissive response, and request for improved staff training and inclusive service.") -> summary : STRING
  RETURN summary
}` — The summarization act, length constraint, audience, and preservation priorities are explicit. The full supplied review must remain a prose payload; it is abbreviated in this simulation only for display.
  - `1775759766664` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "Develop a meal plan for a pregnant woman" → `ENTRYPOINT DevelopPregnancyMealPlan
TASK DevelopPregnancyMealPlan : STRING {
  GENERATE(target="meal plan", audience="pregnant woman", content="Develop a balanced pregnancy meal plan and include a recommendation to personalize it with a qualified healthcare professional for health conditions, trimester, allergies, and dietary needs.") -> plan : STRING
  RETURN plan
}` — The requested artifact and recipient are captured. Nutritional recommendations are legitimate prose substance; the patch is irrelevant.
  - `1775847528997` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "when is the best time for me to do my laundry if I am busy all day?" → `ENTRYPOINT SuggestLaundryTimes
TASK SuggestLaundryTimes : STRING {
  GENERATE(target="laundry scheduling advice", audience="user", content="Suggest practical laundry times for someone busy all day, including considerations such as available time, noise, building rules, and utility off-peak periods.") -> advice : STRING
  RETURN advice
}` — The advice intent and relevant decision factors are represented. The later flat-living constraint in the trajectory is not present in the sampled NL and would require a follow-up turn.
  - `1775971765781` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "Thinks many people need to have problems that need to be solving which is creating them self" → `ENTRYPOINT ExplainProblemCreationPattern
TASK ExplainProblemCreationPattern : STRING {
  GENERATE(target="explanation", audience="user", tone="reassuring", content="Explain the idea that people may create problems for themselves to solve, including possible psychological mechanisms and a nonjudgmental framing.") -> explanation : STRING
  RETURN explanation
}` — The intended interpretation and desired explanatory response are captured despite the ungrammatical wording. The explanation itself is open prose.
  - `1773853293890` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Full] NL: "Good Morning" → `ENTRYPOINT MorningGreeting
CONVO MorningGreeting {
  TURN t1 SPEAKER=USER {
    UTTER acknowledge(content="Good Morning", recipient="agent")
  }
}` — The greeting speech act is fully represented. The later itinerary request shown in the trajectory is a separate follow-up and is not part of this sampled NL.
- **Cross-check:** used=False, agreement=partial — No independent translations were supplied. Capable translators should converge for the two simple sampled bare-put cases, but are unlikely to converge across dependency parsers for coordinated or modified placement clauses because the proposal does not designate a parser, analysis-selection procedure, or UD attachment normalization.
- **Required changes:**
  - `Action`: Define a normative dependency-analysis source or parser-independent conformance algorithm, including tokenization, treatment of multiple parses, and a deterministic failure/reporting representation. Do not make parser availability itself an unspecified source of language-level variation.
  - `Action`: Rewrite destination-coordination extraction so it is compatible with standard UD coordination: specify whether a destination `conj` sibling of an `obl` is accepted, how its inherited `case` relation is interpreted, and whether each destination must literally attach to `put` as `obl`.
  - `Action`: Define an exhaustive syntactic rule for which bare-put dependents count as unsupported placement conditions and are copied into residual `content`, including adverbial clauses, temporal modifiers, negation, auxiliaries, determiners, relative clauses, and nested modifiers. State what happens when their source spans overlap or are discontinuous.
  - `Action`: Make result typing explicit for household selection: require any household Action with STRING target that declares a result intended for identity preservation to declare `-> name : REF[STRING]`; reject incompatible result types rather than merely saying the Action result binds the selected target.
  - `Action`: Resolve the apparent conflict between 'a predicate headed by put with a compound:prt dependent is not eligible' and the later rule allowing it to emit `place`. Define separate terms such as `bare-put eligible` and `particle-put placement eligible`, with unambiguous precedence.
  - `Action`: Specify source-text encoding and span extraction for the claimed byte-for-byte residual substring, or replace byte-level copying with a defined Unicode code-point/token-span rule so equivalent source encodings cannot change BrainCode output.
- **Logic issues:** The destination rule requires a coordination group while also requiring each destination prepositional phrase to be independently attached to `put` as `obl`; ordinary UD analyses commonly attach only the first oblique to `put` and attach later destinations as `conj` siblings.; The proposal mandates UD v2-style analysis but provides neither a normative parser nor a deterministic way to choose among competing valid analyses, so identical input can normalize to `place` for one translator and fail for another.; The residual-content rule says to copy 'unsupported placement conditions' but does not define a complete syntactic class for that phrase; different translators can include or omit the same modifier.; The sentence that an Action result binds the selected STRING target does not state that the declared result type must be REF[STRING], permitting incompatible declarations under the grammar.; Particle-put treatment is internally unclear: it first excludes particle predicates from eligibility, then permits them to emit `place` under what is described as the same required placement analysis.
- **Decision:** accepted
- **Documenter summary:** The Shaper proposed normalizing bare 'put' placement clauses into the existing `place` Action, using mandatory `ref_N` REF bindings to preserve object identity across pronouns (e.g., rinse-then-place, take-then-put), and adding detailed UD-style dependency-analysis rules, coordination handling, and byte-exact residual-content copying to the Action entry. The Critic found the core idea sound (it correctly handled the sampled rinse-mug and remote-on-couch cases) but flagged that the proposal delegates determinism to an unspecified parser/analysis-selection procedure, contains a UD coordination definition that conflicts with standard attachment patterns, and leaves particle-verb eligibility and residual-content boundaries internally inconsistent; it was marked needs-rework with concrete required fixes, then force-accepted after three attempts with those issues carried forward as known open problems for a future sprint.
- **Cost this sprint:** $0.2679

## Sprint 5 (attempt 1/3) — 2026-09-23

- **Language version:** 4.0.1 → 4.0.1 (MAJOR)
- **Candidate task:** Go to the flight booking site, search flights from Tel Aviv to Berlin next Tuesday, and list the three cheapest options.
- **Shaper proposal (model: gemini/gemini-3.1-pro-preview):** Extends Action's normative vocabulary and attribute schemas to support web navigation and flight booking tasks, enabling structured search, filtering, and result extraction.
- **Changes:** `Action` (revise, MAJOR)
- **Critic decision:** needs-rework — The core idea of adding structured travel and web-search fields is promising, but this revision does not define the schemas or effects needed for those fields to improve closed-task planning. Its own worked example relies on undeclared attributes and an undefined sort-to-extract data flow, creating concrete ambiguity rather than determinism. The change should be accepted only after operation signatures, canonical naming, result ordering, and missing core web effects are specified.
- **Doc hygiene:** pass — All changes carry a complete glossary entry (gloss + worked example).
- **Pre-KPI assessment:**
  - coverage: mixed — Adding `extract`, `origin`, `dest`, and `limit` makes the flight-search pattern more directly representable, and it helps structure portions of the Mind2Web shopping task. However, the web vocabulary still lacks an operation or defined effect for saving an item to favorites, does not define selection/slicing semantics for a result set, and does not define a cooling operation needed by the sampled ALFRED tasks. Several closed actionable cores therefore remain prose-dependent or unrepresentable.
  - expressivity: mixed — The proposed fields can preserve origin, destination, date, and result limit in a flight query. But `sort(by="price", order="asc")` in the worked example relies on attributes not declared canonical or semantically defined, and there is no defined relationship between a sort action and a later extraction. The proposal also offers no typed/result semantics for search results, filters, extraction, or saved favorites, so important web-task relations are not recoverable from the expression alone.
  - determinism: harm — The change introduces overlapping names (`dest` alongside existing `destination`) without stating when each must be used, and names `ordering` while its own example uses `by` and `order`. Different translators can consequently choose `target`, `content`, `origin`, `dest`, `destination`, `ordering`, or undeclared attributes for the same web instruction. Independent translations already diverge sharply on the shopping item, including one using an unsupported indexing form and another using `modify_code` for favoriting.
  - interpretability: harm — The glossary gloss claims structured web navigation and sorting, but the semantics do not define operation signatures, required attributes, attribute types for `origin`, `dest`, `limit`, or `ordering`, state changes, or result ordering. A reader cannot determine whether `sort` mutates a current page, returns a sorted collection, or what `extract(limit=3)` extracts from. The worked example further undermines the stated vocabulary by using undeclared `by` and `order` fields.
  - improvement: mixed — A weaker model would benefit from an explicit `search(origin=..., dest=..., date=...)` and a result limit in a flight task. In the sampled shopping task, however, the expression cannot reliably tell that the first three results must be saved rather than merely clicked, and the lack of data-flow semantics between search, sorting, extraction, and later actions limits planning value. The other sampled domains are largely unaffected.
- **Simulated examples:**
  - `held-support-1` (seed_tasks) [Full] NL: "If the customer's order is late and they're a first-time buyer, offer a 10% discount; if they're a repeat buyer, offer free expedited shipping instead." → `ENTRYPOINT HandleLateOrder

TASK HandleLateOrder {
  ACTION check_order_status(target="customer_order") -> is_late : BOOL
  ACTION check_customer_status(target="customer", content="first-time buyer") -> is_first_time : BOOL
  ACTION check_customer_status(target="customer", content="repeat buyer") -> is_repeat : BOOL
  IF is_late AND is_first_time THEN {
    ACTION send_message(recipient="customer", content="offer a 10% discount")
  } ELSE {
    IF is_late AND is_repeat THEN {
      ACTION send_message(recipient="customer", content="offer free expedited shipping")
    }
  }
}` — Existing Action, Check, and Flow-If express the branches. The proposed web additions are irrelevant.
  - `dev-email-2` (seed_tasks) [Full] NL: "If my manager hasn't replied by Friday, send a polite follow-up; otherwise do nothing." → `ENTRYPOINT FollowUpManager

TASK FollowUpManager {
  ACTION check_reply_status(target="manager", date="Friday") -> replied : BOOL
  IF NOT replied THEN {
    ACTION send_email(recipient="manager", tone="polite", content="follow-up")
  }
}` — Existing conditional and communication constructs fully represent the task; the revised Action vocabulary is irrelevant.
  - `479bdc82-ec52-447b-a577-fa2bcdc3886f` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Partial] NL: "Show offers on home essentials under $20 and add the first 3 items to favorites." → `ENTRYPOINT ShowAndFavoriteEssentials

TASK ShowAndFavoriteEssentials {
  ACTION search(target="home essentials offers", threshold=20, comparator="<") -> offers : LIST[REF[STRING]]
  ACTION extract(target=offers, limit=3) -> first_three : LIST[REF[STRING]]
  FOR EACH item IN first_three {
    ACTION click(target=item, content="save to favorites")
  }
}` — The proposal helps express the price threshold and limit, but it supplies neither a favorite/save operation nor semantics saying that this click effects a favorite. It also does not define extraction order, so 'first 3' is not formally grounded.
  - `bef473f1-82a1-4359-a2c0-59b6dc2f6abb` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Partial] NL: "Find a park in Alaska that is also a National Heritage Area." → `ENTRYPOINT FindAlaskaHeritagePark

TASK FindAlaskaHeritagePark : STRING {
  ACTION search(target="park", content="located in Alaska and designated a National Heritage Area") -> result : STRING
  RETURN result
}` — Search is available, but the two required predicates and their conjunction remain an opaque `content` payload. `origin` is not semantically appropriate for an entity's location, and no location/designation filter schema exists.
  - `trial_T20190907_162048_678475#2` (ALFRED (json_2.1.0, train)) [Partial] NL: "Put a chilled mug in the cabinet on the bottom closest to the fridge." → `ENTRYPOINT PlaceChilledMug

TASK PlaceChilledMug {
  ACTION place(target="chilled mug", destination="cabinet on the bottom closest to the fridge")
}` — The final placement and descriptors are represented, but this only selects an already chilled mug. The actionable requirement to make a mug chilled, shown by the trajectory, has no normative cooling/chilling Action.
  - `trial_T20190908_142825_908738#1` (ALFRED (json_2.1.0, train)) [Partial] NL: "Put chilled lettuce in a sink." → `ENTRYPOINT PlaceChilledLettuce

TASK PlaceChilledLettuce {
  ACTION place(target="chilled lettuce", destination="sink")
}` — The target-state descriptor and destination are preserved, but no Action establishes the required chilled state. The web additions are irrelevant.
  - `psf__requests-2931` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Partial] NL: "Request with binary payload fails due to calling to_native_string
Introduced with https://github.com/kennethreitz/requests/issues/2844

```
import requests
requests.put("http://httpbin.org/put", data=u"ööö".encode("utf-8"))
```

This works with 2.8.1, but not with 2.9.

" → `ENTRYPOINT FixBinaryPayload

TASK FixBinaryPayload {
  ACTION modify_code(target="requests/models.py", content="Fix binary-payload handling so requests.put with UTF-8 encoded non-ASCII data does not call to_native_string incorrectly; preserve behavior of version 2.8.1.")
  ACTION run_tests(target="requests binary payload regression tests")
}` — The code-edit and test sequence is structured, but the technical defect and required implementation behavior remain necessarily in the Action content payload. Proposed web fields are irrelevant.
  - `django__django-13089` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Partial] NL: "cache.backends.db._cull sometimes fails with 'NoneType' object is not subscriptable
Description
	 
		(last modified by Guillermo Bonvehí)
	 
I'm sporadically getting some cache errors using database backend.
The error is: 'NoneType' object is not subscriptable
And the backtrace:
/usr/local/lib/python3.7/site-packages/django/core/handlers/base.py:143→ _get_response
/usr/local/lib/python3.7/site-packages/django/template/response.py:108→ render
/usr/local/lib/python3.7/site-packages/django/utils/decorators.py:156→ callback
/usr/local/lib/python3.7/site-packages/django/middleware/cache.py:103→ process_response
/usr/local/lib/python3.7/site-packages/django/utils/cache.py:374→ learn_cache_key
/usr/local/lib/python3.7/site-packages/django/core/cache/backends/db.py:104→ set
/usr/local/lib/python3.7/site-packages/django/core/cache/backends/db.py:136→ _base_set
/usr/local/lib/python3.7/site-packages/django/core/cache/backends/db.py:277→ _cull
This is using Django 2.2.11 but I see the same code is in master.
​https://github.com/django/django/blob/master/django/core/cache/backends/db.py#L270
				cursor.execute(
					connection.ops.cache_key_culling_sql() % table,
					[cull_num])
				cursor.execute("DELETE FROM %s "
							 "WHERE cache_key < %%s" % table,
							 [cursor.fetchone()[0]])
From what I can understand, the cursor after running connection.ops.cache_key_culling_sql() command is not returning any data, so cursor.fetchone()[0] afterwards fails.
I guess a simple check to see if it contains data would be enough, may apply for an easy picking.
Edit: Wording
" → `ENTRYPOINT FixCacheCull

TASK FixCacheCull {
  ACTION modify_code(target="django/core/cache/backends/db.py", content="In _cull, handle cursor.fetchone() returning no row before indexing [0], preventing the NoneType subscript error after cache_key_culling_sql.")
  ACTION run_tests(target="database cache backend tests")
}` — The edit/test workflow is formalized, while the code-level patch remains content payload as expected for a technical change. Proposed web vocabulary is irrelevant.
  - `c5274` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "What do you think about Drug taking safe rooms? Should they be legalised in this time" → `ENTRYPOINT DrugSafeRoomsOpinion

CONVO DrugSafeRoomsOpinion {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="What do you think about drug-taking safe rooms? Should they be legalised at this time?", recipient="agent")
  }
}` — The speech act and recipient are captured; the requested opinion remains correctly opaque prose. The Action change is irrelevant.
  - `c2218` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "My family is very important to me. I'm afraid that when my parents grow older, I won't be able to take care of them in the best way possible." → `ENTRYPOINT FamilyCareConcern

CONVO FamilyCareConcern {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="My family is very important to me. I am afraid that when my parents grow older, I will not be able to take care of them in the best way possible.", recipient="agent")
  }
}` — The personal disclosure and conversational recipient are represented; its emotional substance correctly remains UTTER content. The proposed change is irrelevant.
  - `c3240` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Why are politicians corrupt?" → `ENTRYPOINT AskPoliticalCorruption

CONVO AskPoliticalCorruption {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Why are politicians corrupt?", recipient="agent")
  }
}` — The interrogative speech act is captured; the explanatory substance remains open prose, as intended. The Action revision is irrelevant.
  - `c6366` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Do you think marriage is good?" → `ENTRYPOINT MarriageOpinion

CONVO MarriageOpinion {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Do you think marriage is good?", recipient="agent")
  }
}` — The opinion request and recipient are represented; the argument itself correctly stays prose. The proposed Action change is irrelevant.
  - `wildchat1m_en3u-141678` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-0125-preview)) [Partial] NL: "Please write an exciting sports story about a muddy rugby match between two girls teams. Keep the match realistic. Remember players must release the ball after being tackled successfully. One team plays in blue and gold, the other in green and black.

You do not have to explicitly state any of the things in these instructions, just weave them into the story.

Use names. Pick one of the two teams as the focus of the story, and perhaps even one or two of the players on one team.

The tone should be fun. Give examples of exciting muddy action. Describe how the players got muddier as a result of these actions.

None of the girls mind the mud and most of them enjoy it to varying degrees.

It is muddy but not so muddy everyone gets covered head to toe. Some players get very muddy, others less so.

Some examples for things you could mention (feel free to make your own up and ignore these):
- a player slides on her knees through the mud
- a player face-plants into the mud
- a player is dragged through the mud as she holds on to a running player in an attempted tackle
- a player slides on her bum through the mud
- a player dives into a mud puddle
- a player wipes her hands on herself to improve her grip
- a player is covered in mud all down one side

When describing the state of the players, do not focus exclusively on their jerseys, shorts and socks. remember their knees, thighs, hands, arms, faces, and hair can get muddy too. describe their muddy bodies, not just their muddy kit." → `ENTRYPOINT GenerateRugbyStory

TASK GenerateRugbyStory : STRING {
  GENERATE(target="sports story", tone="enthusiastic", content="Write a fun, exciting, realistic story about a muddy rugby match between girls' teams in blue and gold and in green and black. Use names, focus on one team and one or two players, obey the tackled-player ball-release rule, weave requirements in rather than explicitly listing them, show enjoyable muddy action and varying degrees of mud, and describe muddy bodies as well as kit.") -> story : STRING
  RETURN story
}` — Intent, artifact, tone, and major constraints are structured, while the story substance and detailed creative instructions remain an appropriate generation payload. The Action revision is irrelevant.
  - `wildchat1m_en3u-79333` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "Help me to answer in short answer to this comment [Thanks for the tour!! I learned about places where I haven't ventured yet, but will be sure to go to on my next visit]" → `ENTRYPOINT AnswerTourComment

TASK AnswerTourComment : STRING {
  GENERATE(target="reply", format="short", content="Reply to this comment: Thanks for the tour!! I learned about places where I have not ventured yet, but will be sure to go to on my next visit.") -> reply : STRING
  RETURN reply
}` — The requested reply artifact and short format are explicit; the reply's wording remains generation content. Proposed Action fields are irrelevant.
  - `wildchat1m_en3u-99002` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "Once approved, the report will be available for sharing and I can submit a copy within a few days." → `ENTRYPOINT ReportStatusStatement

CONVO ReportStatusStatement {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="Once approved, the report will be available for sharing and I can submit a copy within a few days.", recipient="agent")
  }
}` — The source is a status statement rather than an explicit request, so recording it as an informational utterance avoids inventing an approval workflow. Its content appropriately remains prose.
  - `wildchat1m_en3u-140636` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-0125-preview)) [Partial] NL: "write an essay if the person was 13 with this text :Do you think phones, tablets, computers, TVs, and other electronics make our lives better or worse? Write about why you think electronics make our lives better or why they make our lives worse." → `ENTRYPOINT GenerateAge13Essay

TASK GenerateAge13Essay : STRING {
  GENERATE(target="essay", format="written as by a 13-year-old", content="Do you think phones, tablets, computers, TVs, and other electronics make our lives better or worse? Write why you think electronics make our lives better or why they make our lives worse.") -> essay : STRING
  RETURN essay
}` — The artifact and age/register constraint are represented, while the requested argument remains generative prose. The Action revision is irrelevant.
  - `1775624231360` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "Can you help me write a recipe for pumpkin cake?" → `ENTRYPOINT GeneratePumpkinCakeRecipe

TASK GeneratePumpkinCakeRecipe : STRING {
  GENERATE(target="recipe", content="Write a recipe for pumpkin cake.") -> recipe : STRING
  RETURN recipe
}` — The request to generate a recipe artifact is captured. Recipe contents remain correctly opaque generation material; no proposed web feature applies.
  - `1775688182593` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "I used an AI chatbot to help me plan a weekly grocery shopping list. I gave it my goal of eating simple, affordable meals and asked it to organize items based on common foods I use at home.

The AI helped by creating a structured list of staples like rice, maize flour, vegetables, eggs, and cooking oil, and also grouped them by category. It also suggested quantities and helped reduce duplicate or unnecessary items.

This made my planning faster, more organized, and helped me avoid forgetting important items or overbuying." → `ENTRYPOINT GroceryPlanningAccount

CONVO GroceryPlanningAccount {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="I used an AI chatbot to plan a weekly grocery list for simple, affordable meals. It organized rice, maize flour, vegetables, eggs, and cooking oil by category, suggested quantities, reduced duplicates, and made planning faster and less wasteful.", recipient="agent")
  }
}` — This is an account of prior assistance, not a new request. The communicative act is captured without inventing a planning action; its narrative substance remains prose.
  - `1776008979756` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "Hi  I am really want to understand the trip to the Moon by the astronauts" → `ENTRYPOINT ExplainMoonTrip

TASK ExplainMoonTrip : STRING {
  GENERATE(target="explanation", audience="user", content="Explain the trip to the Moon by astronauts.") -> explanation : STRING
  RETURN explanation
}` — The explanation artifact and audience are explicit; the scientific explanation remains prose payload. The revised Action construct is irrelevant.
  - `1776097025288` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "I want to plan my meals for the next 5 days. I need recipes that are healthy, quick to cook, budget-friendly, and don’t include egg whites. Can you create a meal plan and a shopping list?" → `ENTRYPOINT PlanMealsAndShopping

TASK PlanMealsAndShopping : STRING {
  GENERATE(target="meal plan and shopping list", format="5-day plan", content="Create healthy, quick-to-cook, budget-friendly recipes for the next 5 days that do not include egg whites, together with a corresponding shopping list.") -> plan : STRING
  RETURN plan
}` — Duration, requested artifacts, and explicit dietary/cost/time constraints are retained. Recipe and shopping-list substance remains a legitimate generation payload; the web additions are irrelevant.
- **Cross-check:** used=True, agreement=low — Providers agree strongly on simple existing constructs such as the manager follow-up and single-turn PRISM questions. They diverge materially on closed web and workflow tasks: shopping translations disagree on result handling and one uses invalid list indexing plus `modify_code` to favorite items; park translations choose different location encodings; report and meal-plan translations disagree between TASK and CONVO. The proposed aliases and undefined web schemas make these divergences more likely, not less.
- **Required changes:**
  - `Action`: Define normative typed signatures and effects for every added web operation. At minimum specify required/optional attributes, their types, result types, and state/data-flow behavior for `search`, `select_filter`, `apply_filters`, `sort`, `extract`, `open`, `click`, `fill_field`, and `submit`.
  - `Action`: Choose one canonical field name for each role and give a mandatory translation rule: either replace `dest` with existing `destination`, or explicitly reserve `dest` for flight endpoints and define when `destination` is prohibited. Define `origin` and `dest` types and whether they apply only to travel searches.
  - `Action`: Replace the unsupported `sort(by="price", order="asc")` example fields with the declared `ordering` field, or add `by` and `order` as canonical attributes with a closed schema. Define how sorting consumes a result collection and how a subsequent extraction is guaranteed to use that sorted collection.
  - `Action`: Define `extract` precisely: its input/result types, default source when no `target` is supplied, whether its result preserves page/rank order, and the validity/type constraints of `limit`. This must make 'first 3' and 'three cheapest' formally recoverable.
  - `Action`: Add a normative web operation for saving/adding an item to favorites, with a structured target and explicit effect, rather than requiring an ambiguous `click(content="save to favorites")` residual instruction.
  - `Action`: Resolve the contradiction between `date` requiring explicit times and the worked example's relative `date="next_Tuesday"`: either define relative-date resolution against a declared execution-time context or revise the example to an explicit date.
  - `Action`: Add a household `cool` or `chill` operation, with state/result semantics, so instructions requiring a chilled item can be executed rather than merely represented as a descriptor of a pre-existing item.
  - `glossary: Action`: Revise the gloss and worked example after the schemas are defined so they describe only defined behavior and use only canonical attributes.
- **Logic issues:** The change calls the additions 'attribute schemas' but supplies no schema for `origin`, `dest`, `limit`, or `ordering`: no type, applicable operations, requiredness, or operational meaning is defined.; The worked example uses `by` and `order`, neither of which appears in the revised canonical attribute list; conversely, the listed `ordering` attribute is unused and undefined.; No semantics state whether `sort` has an input, returns a sorted collection, mutates a current result view, or affects the following `extract`; thus 'three cheapest' is not entailed by the expression.; The `extract(limit=3)` example omits a target/source and result-order semantics, so it has no defined behavior under the proposed text.; The coexistence of `dest` and pre-existing `destination` silently overlaps and creates an unbounded translation choice.; The statement that `date` holds explicit times conflicts with the example's unresolved relative time string `next_Tuesday`.; The expanded operation list still cannot formally express the effect of adding an item to favorites, despite that being a core sampled web action.
- **Decision:** needs-rework
- **Documenter summary:** Shaper proposed extending Action's normative vocabulary and attribute schema with web-navigation operations (open, search, sort, extract, etc.) and canonical attributes (origin, dest, limit, ordering) to support flight-booking tasks. The Critic sent it back for rework: determinism was judged harmed because the proposal introduces overlapping/undefined names (dest vs. destination, undeclared by/order vs. declared ordering) and its own worked example used attributes not defined in its schema, while cross-provider simulations showed low agreement on closed web tasks (e.g., disagreement on favoriting and location-predicate encoding) and left core effects like saving to favorites, sorting-to-extraction data flow, and household chilling unspecified.
- **Cost this sprint:** $1.3415

## Sprint 5 (attempt 2/3) — 2026-09-23

- **Language version:** 4.0.1 → 4.0.1 (MAJOR)
- **Candidate task:** Go to the flight booking site, search flights from Tel Aviv to Berlin next Tuesday, and list the three cheapest options.
- **Shaper proposal (model: gemini/gemini-3.1-pro-preview):** Revise Action to define normative signatures, required/optional attributes, result types, and explicit semantics for web operations (open, click, fill_field, submit, search, select_filter, apply_filters, sort, extract, save_favorite) and household cooling (chill), resolving travel parameter ambiguity and ensuring strict determinism.
- **Changes:** `Action` (revise, MAJOR)
- **Critic decision:** needs-rework — The web collection data-flow idea is useful and the ISO-date flight example is coherent, so this is not a rejection. However, the revision is not ready to enter the language because its search signature and open operation are ambiguous, it leaves several claimed normative operations behaviorless, and it makes a common closed task fail solely for lacking an execution-time context. Fixing the specified signature, namespace, temporal-context, and missing-operation issues would turn the core idea into a clear benefit.
- **Doc hygiene:** pass — All changes carry a complete glossary entry (gloss + worked example).
- **Pre-KPI assessment:**
  - coverage: mixed — The defined search/sort/extract chain gives full structured coverage to ISO-dated travel search and ranked extraction, and save_favorite/chill fill real gaps. However, the relative-date rule makes dev-web-1 untranslatable despite its actionable core being otherwise fully representable, and ordinary closed actions such as turning on a lamp and file-age/location inspection still lack normative operation semantics.
  - expressivity: mixed — Origin, destination, rank-preserving extraction, ordering, and result references improve preservation of web-task intent. But the proposal discards a request containing a relative date rather than representing its meaning with an explicit execution-time context, and search has no defined structured fields for a general booking's confirmation number and passenger-name constraints beyond opaque content.
  - determinism: mixed — The result types and sort/extract behavior substantially reduce variation for the worked flight pattern. Independent translations still diverge materially: providers use invalid relative dates, disagree whether general search needs target versus content, and use undefined operations for file metadata and lamp activation; the proposal's `open` also has an unresolved web-page versus container reading.
  - interpretability: harm — Several signatures are internally ambiguous: the displayed search signature presents threshold and comparator as required while its prose implies they are not; `open(target=STRING)` overlaps `open_container`; and `chill` says it binds or returns a REF although Action's only binding syntax is an explicit result annotation. The proposed glossary gloss claims rigorous signatures broadly, although only a subset of the listed normative operations has one.
  - improvement: benefit — For a flight or retail workflow, typed result collections, explicit sorting, and bounded extraction make the execution plan more usable than raw prose. The benefit is limited for unsupported but routine operations because an executor cannot reliably implement get_file_age, check_location, turn_on, or the listed code/communication operations from this Action definition.
- **Simulated examples:**
  - `dev-web-1` (seed_tasks) [Fail] NL: "Go to the flight booking site, search flights from Tel Aviv to Berlin next Tuesday, and list the three cheapest options." → `<translation failure: `next Tuesday` is a relative temporal phrase and no execution-time context is declared; emitting it as `date` is prohibited by the proposed Action semantics>` — search/sort/extract would otherwise cover the full workflow. The revised date rule, not a missing operation, prevents a valid expression.
  - `dev-code-1` (seed_tasks) [Fail] NL: "Given a list of file paths, delete every file older than 30 days unless it's in the 'archive' folder." → `ENTRYPOINT DeleteOldFiles

TASK DeleteOldFiles(file_paths: LIST[STRING]) {
  FOR EACH file IN file_paths {
    ACTION get_file_age(target=file) -> age : NUMBER
    ACTION check_location(target=file, destination="archive") -> in_archive : BOOL
    IF age > 30 AND NOT in_archive THEN {
      ACTION delete_file(target=file)
    }
  }
}` — The structure, branch, and delete_file operation are available, but get_file_age and check_location have no normative signatures or execution semantics. The new Action revision does not define how either result is produced.
  - `f61456ed-3cc2-41a0-b79c-56737515fac9` (Mind2Web) [Full] NL: "Open the photo gallery for Tsiakkos & Charcoal." → `ENTRYPOINT OpenGallery

TASK OpenGallery {
  ACTION open(target="Tsiakkos & Charcoal photo gallery")
}` — The revised web `open` signature directly supports the requested end state; the trajectory's intermediate search/click steps are implementation detail rather than requested outcomes.
  - `f7b93dc1-2f19-419e-a6e0-a701008c17fa` (Mind2Web) [Full] NL: "Find the booking with ticket 123456 under the name James Buck." → `ENTRYPOINT FindBooking

TASK FindBooking : LIST[REF[STRING]] {
  ACTION search(target="booking", content="ticket 123456 under the name James Buck") -> bookings : LIST[REF[STRING]]
  RETURN bookings
}` — General web search covers the request, but ticket number and passenger name remain an opaque content payload because search has no structured identifier/person constraint fields.
  - `trial_T20190908_123359_988104#0` (ALFRED) [Full] NL: "Put the keys on the couch." → `ENTRYPOINT PlaceKeys

TASK PlaceKeys {
  ACTION place(target="keys", destination="couch")
}` — Existing bare-put normalization and place semantics fully cover this item; the proposed change is irrelevant.
  - `trial_T20190909_043253_098401#0` (ALFRED) [Fail] NL: "Pick up a pillow and turn a lamp on." → `ENTRYPOINT PickUpAndTurnOnLamp

TASK PickUpAndTurnOnLamp {
  ACTION pick_up(target="pillow")
  ACTION turn_on(target="lamp")
}` — pick_up is normative, but turn_on is neither in the normative household vocabulary nor assigned a signature or behavior. Treating `open` as lamp activation, as one independent translation did, is semantically wrong.
  - `pylint-dev__pylint-4970` (SWE-bench_Verified) [Full] NL: "Setting min-similarity-lines to 0 should disable pylint's duplicate-code check." → `ENTRYPOINT DisableDuplicateCodeCheck

TASK DisableDuplicateCodeCheck {
  ACTION modify_code(target="pylint/checkers/similar.py", content="when min-similarity-lines is 0, disable duplicate-code check R0801 rather than treating every line as duplicate")
}` — The actionable requested change is captured. No test request is explicit in the source task, though modify_code itself still lacks a detailed code-operation signature.
  - `pytest-dev__pytest-7571` (SWE-bench_Verified) [Full] NL: "caplog fixture doesn't restore log level after test; pytest 6 leaves level 42 rather than restoring 0." → `ENTRYPOINT RestoreCaplogLevel

TASK RestoreCaplogLevel {
  ACTION modify_code(target="src/_pytest/logging.py", content="restore the caplog handler log level after each test; a test setting level 42 must not leave 42 for the next test")
}` — The requested repair and affected module are preserved. The detailed bug evidence legitimately remains exact instruction payload content.
  - `c7372` (PRISM) [Partial] NL: "What is a good way to foster good relations between a parent and their children." → `ENTRYPOINT FosterParentChildRelations

TASK FosterParentChildRelations : STRING {
  GENERATE(target="advice", audience="parent", content="good ways to foster good relations between a parent and their children") -> advice : STRING
  RETURN advice
}` — The advice-generation intent and audience are structured; the advice substance appropriately remains a natural-language generation payload. No proposed Action change helps.
  - `c1414` (PRISM) [Partial] NL: "Hey could you give me some tips about how I should clean up my room?" → `ENTRYPOINT RoomCleaningTips

TASK RoomCleaningTips : STRING {
  GENERATE(target="tips", audience="user", content="how to clean up my room") -> tips : STRING
  RETURN tips
}` — The request's speech purpose and audience are represented; its useful advice remains generation content, as intended for an open item.
  - `c1137` (PRISM) [Partial] NL: "How do I deal with a toxic mother-in-law and a narcissistic mother?" → `ENTRYPOINT DealWithDifficultFamily

TASK DealWithDifficultFamily : STRING {
  GENERATE(target="advice", audience="user", content="how to deal with a toxic mother-in-law and a narcissistic mother") -> advice : STRING
  RETURN advice
}` — The open advisory request is structurally represented. Adding a tone such as empathetic would be translator invention because the prompt does not explicitly request it.
  - `c524` (PRISM) [Partial] NL: "Aliens definitely exist. But they're way ahead of us in terms of development. If they know we exist, they would probably perceive us as ants." → `ENTRYPOINT AlienStatement

CONVO AlienStatement {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="Aliens definitely exist. But they're way ahead of us in terms of development. If they know we exist, they would probably perceive us as ants.")
  }
}` — This is an assertion, not a clearly specified requested artifact. CONVO/UTTER preserves its speech act and content; no Action change is relevant.
  - `wildchat1m_en3u-56355` (PATHs) [Partial] NL: "give also a literature review of performance evaluation and ranking of banks in full details" → `ENTRYPOINT GenerateBankLiteratureReview

TASK GenerateBankLiteratureReview : STRING {
  GENERATE(target="literature review", format="full details", content="performance evaluation and ranking of banks") -> review : STRING
  RETURN review
}` — The requested artifact, subject, and detail constraint are represented; scholarly prose remains the permitted opaque generation payload.
  - `wildchat1m_en3u-138416` (PATHs) [Partial] NL: "rewrite elaborate and improve on the following natal astrology interpretation." → `ENTRYPOINT RewriteAstrologyInterpretation

TASK RewriteAstrologyInterpretation : STRING {
  GENERATE(target="rewritten and elaborated natal astrology interpretation", content="Jupiter sextile Uranus has such a natural exuberance and zest for life that it attracts luck and positive energy to it constantly. This aspect thrives on change, novelty and new inventions and will often generate this for themselves and for others. These people are natural visionaries and inventors who often make their impossible dreams come true. Their sheer faith in future rainbows keeps them focused on doing whatever it takes to get to the pot of gold.") -> rewritten : STRING
  RETURN rewritten
}` — The rewrite/elaboration operation and artifact are represented; the supplied interpretation is an opaque text payload. The displayed payload abbreviates the very long supplied source text only for this simulation.
  - `wildchat1m_en3u-308` (PATHs) [Partial] NL: "who are you" → `ENTRYPOINT AskIdentity

CONVO AskIdentity {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Who are you?")
  }
}` — The question's speech act and content are captured; the actual answer is not specified in the input and therefore is not invented.
  - `wildchat1m_en3u-44904` (PATHs) [Partial] NL: "Ideas for wrestlers" → `ENTRYPOINT GenerateWrestlerIdeas

TASK GenerateWrestlerIdeas : STRING {
  GENERATE(target="wrestler ideas", content="generate ideas for wrestlers") -> ideas : STRING
  RETURN ideas
}` — The requested creative artifact is explicit; its creative substance correctly remains generative content.
  - `1775750389118` (ThoughtTrace) [Partial] NL: "I need help scheduling what I should eat on a weekly basis. Try to give me some advices for each day, in a calendar format, and balancing my diet for the usual human needs." → `ENTRYPOINT GenerateWeeklyMealPlan

TASK GenerateWeeklyMealPlan : STRING {
  GENERATE(target="weekly meal plan", format="calendar", content="advice for each day, balancing diet for usual human nutritional needs") -> plan : STRING
  RETURN plan
}` — Weekly scope, calendar format, and nutritional constraint are captured. Individual meals remain appropriate prose-generation substance.
  - `1775846209884` (ThoughtTrace) [Partial] NL: "hy" → `ENTRYPOINT Greeting

CONVO Greeting {
  TURN t1 SPEAKER=USER {
    UTTER greet(content="hy")
  }
}` — The greeting is represented as an open speech act. The open UTTER vocabulary permits greet, but its lack of a closed canonical classification leaves some translator variation.
  - `1775435865467` (ThoughtTrace) [Partial] NL: "hi" → `ENTRYPOINT Greeting

CONVO Greeting {
  TURN t1 SPEAKER=USER {
    UTTER greet(content="hi")
  }
}` — The sampled NL is only a greeting; later trajectory context does not alter this item-level translation.
  - `1775480237547` (ThoughtTrace) [Partial] NL: "I have to do a research project on the topic" → `ENTRYPOINT ResearchProjectRequest

CONVO ResearchProjectRequest {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="I have to do a research project on the topic")
  }
}` — The request is incomplete because no topic is supplied. A conversational ask preserves that state without fabricating a project or topic; later turns would be needed for the multi-step request.
- **Cross-check:** used=True, agreement=partial — Providers agree on the basic search-sort-extract plan and most GENERATE task shapes, but both independently emit prohibited relative dates for dev-web-1. They materially diverge on undefined operations (gemini maps lamp activation to open; anthropic uses turn_on), on whether booking fields belong in target or content, and on invalid UTTER placement in TASK bodies. These are substantive determinism failures, not merely identifier-name variation.
- **Required changes:**
  - `Action`: Replace the absolute ban on relative dates with a typed execution-time context: add a document/task-level `CONTEXT execution_date=STRING` (ISO-8601) or equivalent parameter, and define deterministic resolution of relative date phrases against it. A relative date without that context should remain a translation failure.
  - `Action`: Rewrite `search` as disjoint, explicit overloads or tagged forms. For example define `search_travel(origin, destination, date?)` and `search_web(target, content?)`; state whether threshold/comparator are optional as a pair and prohibit them otherwise. Do not show every parameter as mandatory in the signature while prose says otherwise.
  - `Action`: Resolve `open` overlap by renaming the web operation to `open_page` (or requiring `kind="page"`) and reserving `open_container` for household containers; define what named-site/page targets resolve to.
  - `Action`: Add normative household signatures needed by the existing action space, at minimum `turn_on(target=REF[STRING]|STRING)` and preferably `turn_off`; alternatively explicitly state that these are unsupported rather than leaving generic undefined Action identifiers.
  - `Action`: Either provide signatures and result semantics for the listed CODE and COMMUNICATION operations and common inspection operations needed for branching (for example file age/location), or remove the claim that the listed vocabulary is normative. Define how a BOOL/NUMBER result can be obtained rather than relying on arbitrary Action result annotations.
  - `Action`: Define chill's result exactly: e.g. `chill(target=REF[STRING]|STRING) -> IDENT : REF[STRING]` is optional and, when present, binds the selected chilled entity. Remove the undefined phrase 'binding or returning' and state whether chilling mutates the same reference or creates a new one.
  - `Action`: Revise the glossary gloss to say that signatures are defined for the enumerated web operations and chill only, unless the proposal also adds signatures for every operation it claims to cover.
- **Logic issues:** The proposed grammar writes `search(origin, destination, date, target, threshold, comparator)` as if all six attributes are mandatory, while its semantics say travel requires origin/destination with optional date and general web requires target. It never states threshold/comparator optionality or whether arbitrary extra attributes such as content are legal.; `open(target=STRING)` overlaps semantically with the already listed household `open_container`; the same surface expression can mean opening a page or opening a physical container.; The normative operation vocabulary includes pick_up, place, heat, rinse, slice, pour, open_container, close_container, modify_code, run_tests, add_file, delete_file, send_email, send_message, and call, but the proposal supplies no operation signatures or result semantics for them.; The worked example is internally valid only because travel search is said to allow omitted target and optional date, despite the written search signature making target mandatory.; The strict relative-date policy turns routine executable requests such as 'next Tuesday' into failures even though the missing datum is a resolvable execution context, not an unexpressible user constraint.; `chill` says it may bind or return a resulting REF, but Action only has one explicit `-> IDENT : type` result form and no implicit binding or return behavior.; The sample's required lamp activation has no defined operation. `open(target="lamp")`, produced by an independent translator, demonstrates an unsafe ambiguity rather than an equivalent translation.
- **Decision:** needs-rework
- **Documenter summary:** Shaper proposed a MAJOR revision of Action defining normative signatures for web operations (open, search, sort, extract, save_favorite, etc.) and chill, with result types and strict ISO-8601 date requirements. Critic rejected as needs-rework: the strict relative-date ban caused the flight-booking task itself (dev-web-1, 'next Tuesday') to fail translation, search's signature contradicted its own prose on mandatory/optional fields, open collided with open_container, and several claimed normative operations (turn_on, get_file_age, code/communication ops) had no defined semantics, undermining the interpretability and determinism gains.
- **Cost this sprint:** $1.4026

## Sprint 5 (attempt 3/3) — 2026-09-23

- **Language version:** 4.0.1 → 5.0.0 (MAJOR)
- **Candidate task:** Go to the flight booking site, search flights from Tel Aviv to Berlin next Tuesday, and list the three cheapest options.
- **Shaper proposal (model: gemini/gemini-3.1-pro-preview):** Adds a task-level execution-date context to support relative dates, formalizes disjoint web search overloads, resolves web-page versus container opening ambiguity, adds standard household control operations, and clarifies Action result semantics.
- **Changes:** `Task` (revise, MAJOR), `Action` (revise, MAJOR)
- **Critic decision:** needs-rework — [Forced acceptance after 3 attempt(s) without a clean accept — the required changes below are known issues carried forward for a future sprint to address, not resolved.] The proposal has useful core ideas: distinct web search operations, a dedicated web-page opening operation, relative-date anchoring, and missing household controls all improve practical task decomposition. It cannot be accepted because its central examples are invalid under its own grammar and date semantics, and because web filtering lacks the data-flow semantics needed for common closed web tasks. Correcting those precise inconsistencies and defining typed filter results would turn much of this into a positive revision.
- **Doc hygiene:** pass — All changes carry a complete glossary entry (gloss + worked example).
- **Pre-KPI assessment:**
  - coverage: mixed — The new web signatures, appliance controls, and chilling operation cover several previously unsupported closed-task actions. However, the sampled file-deletion task still lacks defined file-age and archive-membership inspection operations, and web filtering has no result-producing semantics, so a request to return only filtered offers cannot be represented faithfully.
  - expressivity: mixed — Execution-date context is the right mechanism for relative dates, and search_travel distinguishes travel searches from general web searches. But the proposed Task and Action examples are invalid under the proposed grammar and semantics: CONTEXT is placed on ENTRYPOINT rather than TASK, and date="next_Tuesday" is not converted to the required ISO-8601 value. Filter application also cannot produce a filtered collection that can be returned.
  - determinism: harm — The new signatures reduce ambiguity between travel and general web search, but key translation choices remain underdetermined: search_web versus navigation-plus-fill_field, whether a user request becomes TASK/GENERATE or CONVO/UTTER, and whether select_filter mutates an unspecified page state or a named result. Independent translations substantially diverge on these choices, including divergent Task versus CONVO representations and incompatible web-action sequences.
  - interpretability: harm — Disjoint search names and open_page improve local readability, but the proposed normative text conflicts with its grammar and examples. A reader cannot tell whether execution context belongs to ENTRYPOINT or TASK, whether relative dates are stored or normalized, or how a selected/applied filter affects a previously bound result list.
  - improvement: benefit — Explicit open_page, search_travel, search_web, turn_on, turn_off, and chill give a weaker executor more actionable structure than generic operation names. Once filter-state and date-normalization defects are fixed, the new signatures would especially improve web and household execution planning.
- **Simulated examples:**
  - `dev-code-1` (seed_tasks) [Fail] NL: "Given a list of file paths, delete every file older than 30 days unless it's in the 'archive' folder." → `ENTRYPOINT DeleteOldFiles

TASK DeleteOldFiles {
  LET file_paths : LIST[STRING] = ["file_a", "archive/file_b"]
  FOR EACH path IN file_paths {
    ACTION check_file_age(target=path) -> age_days : NUMBER
    ACTION check_file_folder(target=path) -> folder : STRING
    IF age_days > 30 AND folder != "archive" THEN {
      ACTION delete_file(target=path)
    }
  }
}` — delete_file is normative, but no normative operation or result signature exists for obtaining a file's age or folder membership. The proposed changes are irrelevant to this missing closed-task inspection capability.
  - `held-trip-1` (seed_tasks) [Partial] NL: "Plan a 3-day itinerary in Kyoto that includes at least one temple per day and avoids anything more than a 20-minute walk from the last stop." → `ENTRYPOINT PlanKyotoItinerary

TASK PlanKyotoItinerary : STRING {
  GENERATE(target="itinerary", format="3-day itinerary", content="Plan a Kyoto itinerary with at least one temple each day and no stop more than a 20-minute walk from the preceding stop.") -> itinerary : STRING
  RETURN itinerary
}` — GENERATE can produce the requested artifact, but day-level temple coverage and successive-stop walking-time constraints remain opaque prose rather than executable or checkable structure. The proposed web-search changes do not supply route-duration validation.
  - `fb04bb83-9ad5-4186-a0da-17af9ba2a63d` (Mind2Web) [Partial] NL: "Find offers for VIFP Club loyalty number 9016467685 and show the ones that are for members only." → `ENTRYPOINT FindMemberOffers

TASK FindMemberOffers : LIST[REF[STRING]] {
  ACTION open_page(target="cruise_deals_site")
  ACTION fill_field(target="VIFP Club loyalty number", content="9016467685")
  ACTION submit(target="offers_form")
  ACTION search_web(target="VIFP Club offers", content="VIFP Club loyalty number 9016467685") -> offers : LIST[REF[STRING]]
  ACTION select_filter(target="offers", options="members only")
  ACTION apply_filters(target="offers")
  RETURN offers
}` — open_page, fill_field, submit, select_filter, and apply_filters help represent the navigation. However, apply_filters has no defined result or mutation semantics, so RETURN offers denotes the pre-filter search collection rather than the requested members-only subset.
  - `6d963cc0-90d3-4908-bee4-29a8530536af` (Mind2Web) [Full] NL: "Show me all my offers for 2-5 day cruises" → `ENTRYPOINT ShowCruiseOffers

TASK ShowCruiseOffers {
  ACTION open_page(target="cruise_offers_site")
  ACTION select_filter(target="duration", options="2-5 days")
  ACTION apply_filters(target="cruise_offers")
}` — The requested UI outcome can be expressed as page opening, duration selection, and filter application. The new filter vocabulary helped, although a result-returning form would be needed if this request required downstream processing of the filtered offers.
  - `trial_T20190907_034528_884833#3` (ALFRED) [Full] NL: "Throw away a toilet paper roll." → `ENTRYPOINT ThrowAwayRoll

TASK ThrowAwayRoll {
  ACTION place(target="toilet paper roll", destination="trash can")
}` — The existing household placement operation captures the actionable core. The proposed household-control additions are irrelevant here.
  - `trial_T20190912_052310_164968#1` (ALFRED) [Full] NL: "Put a full toilet paper roll and an empty paper roll on the counter between the two sinks." → `ENTRYPOINT PlaceRolls

TASK PlaceRolls {
  ACTION place(target="full toilet paper roll", destination="counter between the two sinks")
  ACTION place(target="empty paper roll", destination="counter between the two sinks")
}` — The existing bare-put coordination policy yields two ordered place actions. None of the proposed changes is needed.
  - `sphinx-doc__sphinx-7462` (SWE-bench_Verified) [Full] NL: "IndexError: pop from empty list for empty tuple type annotation; fix Sphinx so Tuple[()] annotations build correctly." → `ENTRYPOINT FixEmptyTupleAnnotation

TASK FixEmptyTupleAnnotation {
  ACTION modify_code(target="sphinx/domains/python.py", content="Handle Tuple[()] during annotation unparsing without calling pop on an empty result list, so documentation builds preserve the valid empty-tuple annotation.")
  ACTION modify_code(target="sphinx/pycode/ast.py", content="Update empty tuple annotation parsing support consistently with the domain unparser fix.")
  ACTION run_tests(target="Sphinx annotation and documentation build tests")
}` — The normative code operations represent the requested repair and validation. The proposal does not materially change this translation.
  - `sphinx-doc__sphinx-9602` (SWE-bench_Verified) [Full] NL: "Nitpick flags Literal annotation values as missing py:class; Literal[True] and Literal[False] should remain annotations without nitpick warnings." → `ENTRYPOINT FixLiteralNitpick

TASK FixLiteralNitpick {
  ACTION modify_code(target="sphinx/domains/python.py", content="Treat literal values inside typing.Literal annotations as literal annotation values rather than py:class references, preventing nitpick warnings for Literal[True] and Literal[False].")
  ACTION run_tests(target="nitpick-enabled autodoc build for Literal annotations")
}` — modify_code and run_tests cover the repair objective. The proposal is irrelevant to the code-domain representation.
  - `c4998` (PRISM) [Partial] NL: "What role did Martha Graham play in the development of contemporary dance?" → `ENTRYPOINT ExplainMarthaGraham

TASK ExplainMarthaGraham : STRING {
  GENERATE(target="answer", content="Explain Martha Graham's role in the development of contemporary dance.") -> answer : STRING
  RETURN answer
}` — The answer-request speech act and output artifact are represented, while the substantive historical explanation remains the intended opaque generation payload.
  - `c333` (PRISM) [Partial] NL: "Is it bad to not marry" → `ENTRYPOINT AnswerMarriageQuestion

TASK AnswerMarriageQuestion : STRING {
  GENERATE(target="answer", content="Answer whether it is bad not to marry.") -> answer : STRING
  RETURN answer
}` — The conversational question is represented as an answer-generation request; its philosophical substance properly remains prose.
  - `c1809` (PRISM) [Partial] NL: "What is the purpose of human existence and would humanity been better off never existing" → `ENTRYPOINT AnswerExistentialQuestion

TASK AnswerExistentialQuestion : STRING {
  GENERATE(target="answer", content="Discuss the purpose of human existence and whether humanity would have been better off never existing.") -> answer : STRING
  RETURN answer
}` — The two-part philosophical request is preserved in the generation payload. The proposal's date and web signatures are irrelevant.
  - `c1540` (PRISM) [Partial] NL: "Why is my country seen as the best in europe" → `ENTRYPOINT AnswerCountryQuestion

TASK AnswerCountryQuestion : STRING {
  GENERATE(target="answer", content="Explain why the user's country may be seen as the best in Europe, while requesting clarification if the country or evaluation criteria are needed.") -> answer : STRING
  RETURN answer
}` — The request and necessary clarification behavior are retained as prose payload. The unspecified country makes a fully grounded answer impossible, but not a meta-structure failure.
  - `wildchat1m_en3u-23615` (PATHs) [Partial] NL: "BF, GF, Pico, Tricky, Lilac, Carol, Milla. original and Freedom Planet 2 Style" → `ENTRYPOINT GenerateCharacterConcepts

TASK GenerateCharacterConcepts : STRING {
  GENERATE(target="character concepts", format="original and Freedom Planet 2 style", content="Create concepts for BF, GF, Pico, Tricky, Lilac, Carol, and Milla.") -> concepts : STRING
  RETURN concepts
}` — The requested artifact, subjects, and requested style are captured; the actual character-design substance is appropriately opaque.
  - `wildchat1m_en3u-35778` (PATHs) [Partial] NL: "Write a 2000-word SEO-optimized article about the fiber optic PLC splitter with an attractive title, conclusion, five unique FAQs, and specified keywords each used evenly at least 6-8 times." → `ENTRYPOINT WriteFiberArticle

TASK WriteFiberArticle : STRING {
  GENERATE(target="article", quantity=2000, format="attractive title; conclusion paragraph; five unique FAQs after conclusion", content="Write a fluent English, engaging, informative, SEO-optimized article about the fiber optic PLC splitter. Include the keywords 'fiber optic plc splitter', 'fiber optic plc splitter manufacturer', 'fiber splitter', and 'fiber optic plc splitter supplier' evenly, each at least 6-8 times.") -> article : STRING
  RETURN article
}` — Length, output sections, keyword list, and frequency constraints are preserved, though frequency/evenness remains prose because the language lacks structured occurrence constraints. This is acceptable opaque generation substance but would be stronger with a dedicated textual-constraint schema.
  - `wildchat1m_en3u-66414` (PATHs) [Partial] NL: "ok can you help me make a in depth list id like it to goto 100 if possible without any recurring/repetition on provided topic with breif desciption for each listed" → `ENTRYPOINT MakeDetailedList

TASK MakeDetailedList : STRING {
  GENERATE(target="list", quantity=100, format="in-depth list with a brief description for each item and no repeated items", content="Create the list on the provided topic.") -> list : STRING
  RETURN list
}` — The quantity, non-repetition requirement, and per-item-description format are captured. The topic is absent from the source request, so it correctly remains unspecified rather than invented.
  - `wildchat1m_en3u-128437` (PATHs) [Partial] NL: "I'm working on a comic based off of Inglorious Basterds and I'd like to tell you about its two main characters." → `ENTRYPOINT ComicConversation

CONVO ComicConversation {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="I am working on a comic based on Inglorious Basterds and would like to describe its two main characters.", recipient="agent")
  }
}` — CONVO and UTTER preserve the user's conversational act, recipient, and sequencing boundary. The character information has not yet been supplied, so no generation step should be fabricated.
  - `1775708404934` (ThoughtTrace) [Partial] NL: "Hello. Please, create a routine plan for exercising as a starter." → `ENTRYPOINT CreateStarterExercisePlan

TASK CreateStarterExercisePlan : STRING {
  GENERATE(target="exercise routine plan", audience="beginner", content="Create a starter exercise routine plan.") -> plan : STRING
  RETURN plan
}` — The intended artifact and beginner audience are captured. The plan's substantive exercise choices remain the intended natural-language generation payload.
  - `1775495374242` (ThoughtTrace) [Partial] NL: "Hi there! I'm currently working on a vegetable garden. I'm using a raised bed of 40cm and would love to know how to keep snails away from my crops." → `ENTRYPOINT GiveSnailAdvice

TASK GiveSnailAdvice : STRING {
  GENERATE(target="gardening advice", content="Explain how to keep snails away from vegetable crops in a 40 cm raised bed.") -> advice : STRING
  RETURN advice
}` — The advice request, crop context, and 40 cm raised-bed constraint are retained. The proposal's execution-date construct is irrelevant.
  - `1775852606009` (ThoughtTrace) [Partial] NL: "can you help me plan an daily routine for gym" → `ENTRYPOINT PlanGymRoutine

TASK PlanGymRoutine : STRING {
  GENERATE(target="daily gym routine", content="Plan a daily gym routine.") -> routine : STRING
  RETURN routine
}` — The requested planning artifact is represented, while fitness-program content remains an opaque payload.
  - `1775835197208` (ThoughtTrace) [Partial] NL: "hi there, what's ur name" → `ENTRYPOINT NameQuestion

CONVO NameQuestion {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="What is your name?", tone="casual", recipient="agent")
  }
}` — The speech act, intended recipient, and casual register are represented. The question text remains the legitimate opaque conversational payload.
- **Cross-check:** used=True, agreement=low — Independent translations agree broadly on GENERATE for straightforward open-ended artifact requests, but diverge materially on Task versus CONVO for conversational prompts, on whether to browse versus generate for planning, and on web-search/filter sequences. Several supplied translations are themselves structurally invalid or semantically incomplete, including CONVO declarations without ENTRYPOINT and filtered-offer flows that return an unfiltered search result; this reinforces rather than resolves the proposal's determinism problems.
- **Required changes:**
  - `Task`: Make CONTEXT placement consistent across grammar, semantics, glossary, and examples. Either change grammar to `entrypoint ::= "ENTRYPOINT" IDENT ("CONTEXT" execution_date_param)?` or, preferably, retain task-level context and revise every example to `TASK Name CONTEXT execution_date="YYYY-MM-DD" ...`; explicitly state that only the entrypoint TASK's context is operational.
  - `Task`: Add `CONTEXT` to the reserved-word list and define a lexical ISO-8601 calendar-date production rather than accepting arbitrary STRING values for execution_date.
  - `Action`: Replace relative `date` values during translation with a specified ISO-8601 output value and define the resolution algorithm for phrases such as next Tuesday, including week-boundary convention, locale, and timezone. Correct both worked examples to use the valid Task-level context and the resolved date, e.g. `date="2025-06-10"` for the stated anchor under the chosen convention.
  - `Action`: Define filter-state data flow. For example, make `apply_filters(target=LIST[REF[STRING]]) -> IDENT : LIST[REF[STRING]]` return the filtered collection, or define an explicit `filter` operation with a typed collection input and typed filtered output. State whether select_filter acts on a page/session object and how that object is named.
  - `Action`: Give every newly normative household operation a complete signature, required attributes, return behavior, and identity-binding rule. In particular, clarify whether chill may omit its result binding and whether it returns the same entity reference or a distinct resulting entity reference.
  - `Action`: Add normative file-inspection operations such as `get_file_age(target=STRING) -> NUMBER` and `get_parent_folder(target=STRING) -> STRING` or an equivalent typed metadata mechanism, so conditional file-management requests can be represented without invented Action names.
  - `basis`: Add a deterministic translation-selection rule for when a user request is represented as a TASK with GENERATE versus as a CONVO with UTTER, especially for single-turn questions and requests that expect an agent response.
- **Logic issues:** The revised Task grammar places CONTEXT after a TASK name and optional parameters, but both proposed worked examples place CONTEXT after ENTRYPOINT; those examples do not parse.; The Action semantics require relative date phrases to be converted deterministically to ISO-8601 strings, but both proposed examples retain `date="next_Tuesday"`; those examples violate the stated semantics even if CONTEXT placement were corrected.; execution_date is specified as ISO-8601 but grammatically accepts any STRING, and CONTEXT is absent from the current reserved-word list.; No algorithm defines ambiguous relative-date phrases such as next Tuesday: the proposed date-only anchor does not specify locale, timezone, week-start convention, or whether the current weekday counts as next.; select_filter and apply_filters return none and have no defined state mutation or page/session value. Therefore a bound `LIST[REF[STRING]]` obtained before filtering cannot be known to denote the requested filtered set.; The Action operation list says household operations include chill but supplies a special chill binding signature only in prose; it does not define whether an unbound chill is legal or whether the returned REF is identical to its target.; The proposed Action revision removes `open` from the normative vocabulary but does not state a migration/static-error rule for existing uses, even though the language previously used open as a normative web operation.; The stated canonical attribute list omits `deadline`, although UTTER and existing specifications explicitly use it as a shared attribute role; the revision should not silently narrow or contradict existing shared vocabulary.
- **Decision:** accepted
- **Documenter summary:** Shaper proposed adding TASK-level CONTEXT execution_date for relative dates, disjoint search_travel/search_web signatures, an open_page/container disambiguation, new household controls (turn_on/turn_off/chill), and clarified Action result semantics; the Critic flagged this needs-rework because the worked examples placed CONTEXT on ENTRYPOINT rather than TASK and left dates unresolved as 'next_Tuesday' (self-contradicting the stated grammar/semantics), and because select_filter/apply_filters lack typed return semantics so filtered-offer requests (e.g. the Mind2Web VIFP members-only offers simulation) cannot faithfully be represented. Despite this, since it was the third attempt without a clean accept, the decision was forced acceptance with the required fixes (CONTEXT placement, ISO-8601 resolution algorithm, typed filter output, file-inspection ops) carried forward as known issues for a future sprint.
- **Cost this sprint:** $1.4498

## Sprint 6 (attempt 1/3) — 2026-09-23

- **Language version:** 5.0.0 → 5.0.0 (MINOR)
- **Candidate task:** If my manager hasn't replied by Friday, send a polite follow-up; otherwise do nothing.
- **Shaper proposal (model: anthropic/claude-sonnet-5):** Adds a normative COMMUNICATION action (`check_replied`) and a canonical `deadline` attribute (with the same relative-date resolution as `date`) so 'hasn't replied by Friday' can be expressed with a proper normative verb instead of an ad hoc, non-normative IDENT.
- **Changes:** `Action` (revise, MINOR)
- **Critic decision:** needs-rework — The core addition is the right shape: a typed Action result consumed by Flow-If is preferable to an invented identifier and would improve communication-workflow coverage. However, its flagship use case has undefined or incorrect timing, and its worked example contradicts the required ISO conversion rule. These are fixable specification edits rather than a reason to reject the operation, but acceptance would be unsafe until they are resolved.
- **Doc hygiene:** pass — All changes carry a complete glossary entry (gloss + worked example).
- **Pre-KPI assessment:**
  - coverage: benefit — The new normative check_replied operation closes a real gap for reminder and follow-up workflows that previously required inventing a non-normative Action identifier. It does not affect most sampled domains, but it increases coverage for communication tasks with reply-status conditions.
  - expressivity: mixed — The proposed operation can represent the existence of a reply-status query and a dependent follow-up branch. However, it cannot reliably preserve the meaning of 'has not replied by Friday': the stated semantics query live state at the moment the Action executes, so a Tuesday execution can send the follow-up immediately rather than waiting until Friday.
  - determinism: mixed — A named operation is more deterministic than arbitrary identifiers such as check_reply_status. But translators still have no deterministic rule for whether deadline means schedule evaluation at that time, inspect historical state at that time, or merely attach a future cutoff to an immediate query; the worked example also leaves an unresolved relative weekday literal despite the semantics requiring ISO conversion.
  - interpretability: harm — The gloss says deadline resolves deterministically, while the worked example retains deadline="Friday" rather than the required resolved ISO date. More importantly, 'optionally bounded by deadline' is not operationally defined for a deadline after the current evaluation moment, so a reader cannot recover when the follow-up occurs.
  - improvement: mixed — A weaker planner benefits from seeing a typed BOOL status result consumed by IF rather than an invented action name. Yet following the present semantics can cause the planner to send a follow-up before the deadline, making the structured representation actively worse than the original request for this central use case.
- **Simulated examples:**
  - `dev-embodied-1` (seed_tasks) [Full] NL: "Rinse the mug in the sink, then put it in the coffee maker." → `ENTRYPOINT RinseThenPlace

TASK RinseThenPlace {
  ACTION rinse(target="mug", destination="sink") -> mug : REF[STRING]
  ACTION place(target=mug, destination="coffee_maker")
}` — No proposed construct is relevant. The REF binding preserves identity and ordering.
  - `dev-email-1` (seed_tasks) [Full] NL: "Draft a reply to my professor asking for a two-day extension on the assignment, and keep it formal." → `ENTRYPOINT DraftReply

TASK DraftReply : STRING {
  GENERATE(target="reply", audience="professor", tone="formal", content="ask for a two-day extension on the assignment") -> draft_text : STRING
  RETURN draft_text
}` — No proposed construct is relevant; GENERATE preserves artifact, audience, register, and requested content.
  - `9365fba7-2698-4063-b151-dd0bd55e0f50` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Show me all the cruises that go from Miami Florida to The Bahamas" → `ENTRYPOINT ShowCruises

TASK ShowCruises : LIST[REF[STRING]] {
  ACTION open_page(target="cruise_booking_site")
  ACTION select_filter(target="sail_to", options="The Bahamas")
  ACTION select_filter(target="sail_from", options="Miami, FL")
  ACTION apply_filters(target="cruise_search")
  ACTION search_travel(origin="Miami, FL", destination="The Bahamas", date="unspecified") -> cruises : LIST[REF[STRING]]
  RETURN cruises
}` — The proposed communication operation is irrelevant. Existing web actions express the finite navigation/filter core, although search_travel's mandatory date makes an unspecified-date cruise search awkward.
  - `551ab381-5bfe-4491-9602-0b0c584d1346` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Give me the IMDB recommendations of what to watch." → `ENTRYPOINT GetIMDbRecommendations

TASK GetIMDbRecommendations : LIST[REF[STRING]] {
  ACTION open_page(target="IMDb")
  ACTION click(target="Open Navigation Drawer")
  ACTION click(target="What to Watch")
  ACTION search_web(target="IMDb", content="recommendations of what to watch") -> recommendations : LIST[REF[STRING]]
  RETURN recommendations
}` — The proposed change is irrelevant.
  - `trial_T20190907_020433_576638#0` (ALFRED (json_2.1.0, train)) [Full] NL: "Place a bowl holding a pen onto a white table." → `ENTRYPOINT PlaceBowlHoldingPen

TASK PlaceBowlHoldingPen {
  ACTION place(target="bowl holding a pen", destination="white table")
}` — The state constraint remains part of the target descriptor. The proposed change is irrelevant.
  - `trial_T20190906_213125_603187#2` (ALFRED (json_2.1.0, train)) [Full] NL: "place two sets of keys down on white chair" → `ENTRYPOINT PlaceTwoKeySets

TASK PlaceTwoKeySets {
  ACTION place(target="sets of keys", quantity=2, destination="white chair")
}` — Quantity and destination are represented; the proposed change is irrelevant.
  - `django__django-16100` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "Add transaction handling to Changelist list_editable processing." → `ENTRYPOINT AddTransactionHandling

TASK AddTransactionHandling {
  ACTION modify_code(target="django/contrib/admin/options.py", content="Wrap Changelist changelist_view list_editable processing in a database transaction so database changes cannot leave unexpected state when an error occurs.")
  ACTION run_tests(target="Django admin changelist_view")
}` — The substantive patch condition is an allowed exact instruction payload. The proposed communication operation is irrelevant.
  - `scikit-learn__scikit-learn-12973` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "LassoLarsIC: unintuitive copy_X behaviour." → `ENTRYPOINT FixLassoLarsICCopyX

TASK FixLassoLarsICCopyX {
  ACTION modify_code(target="sklearn/linear_model/least_angle.py", content="Change LassoLarsIC.fit copy_X default from True to None; retain the instance copy_X setting unless fit receives an explicit copy_X argument.")
  ACTION run_tests(target="LassoLarsIC")
}` — The code-change intent and compatibility condition are captured in content. The proposal is irrelevant.
  - `c6366` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Do you think marriage is good?" → `ENTRYPOINT MarriageOpinion

TASK MarriageOpinion : STRING {
  GENERATE(target="answer", audience="user", content="Answer the user's question: Do you think marriage is good?") -> answer : STRING
  RETURN answer
}` — The question's speech act, audience, and requested answer are structured; its opinion substance remains an appropriate opaque prose payload. The proposed change is irrelevant.
  - `c6565` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "What age should people first have sex?" → `ENTRYPOINT SexualHealthAnswer

TASK SexualHealthAnswer : STRING {
  GENERATE(target="answer", audience="user", content="Provide age-appropriate, safety-conscious guidance in response to: What age should people first have sex?") -> answer : STRING
  RETURN answer
}` — The request for guidance and its recipient are represented; the answer's substantive safety guidance remains prose. The proposal is irrelevant.
  - `c329` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "What's your opinion about the neurodiversity movement?" → `ENTRYPOINT NeurodiversityOpinion

TASK NeurodiversityOpinion : STRING {
  GENERATE(target="answer", audience="user", content="Answer the user's question about the neurodiversity movement: What's your opinion about it?") -> answer : STRING
  RETURN answer
}` — The opinion-request speech act is preserved while the argument remains an opaque payload. The proposed change is irrelevant.
  - `c5376` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Witch is the religion that reads the koran?" → `ENTRYPOINT AnswerQuranReligionQuestion

TASK AnswerQuranReligionQuestion : STRING {
  GENERATE(target="answer", audience="user", content="Answer the factual question: Which religion regards the Quran (Koran) as its central scripture?") -> answer : STRING
  RETURN answer
}` — The factual-question act and intended answer are represented; explanatory content remains prose. The proposed change is irrelevant.
  - `wildchat1m_en3u-135626` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-1106-preview)) [Partial] NL: "write a comprehensive astrological interpretation of the vertex in the first house in the natal chart, write it in verbal form not in point form" → `ENTRYPOINT WriteVertexInterpretation

TASK WriteVertexInterpretation : STRING {
  GENERATE(target="astrological interpretation", audience="user", format="verbal prose, not point form", content="Write a comprehensive interpretation of the Vertex in the first house in a natal chart.") -> interpretation : STRING
  RETURN interpretation
}` — The artifact, length-quality request, and prose-only format are represented; the generated interpretation is correctly opaque prose. The proposal is irrelevant.
  - `wildchat1m_en3u-86795` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "Summarize me this mobile-phone-store dialogue between Mr Smith and Miss Jane." → `ENTRYPOINT SummarizePhoneStoreDialogue

TASK SummarizePhoneStoreDialogue : STRING {
  GENERATE(target="summary", audience="user", content="Summarize the supplied Mr Smith and Miss Jane dialogue about mobile-phone promotions, an XYZ plan with bonus data, pricing concerns, and Mr Smith's business card.") -> summary : STRING
  RETURN summary
}` — The summarization act and recipient are structured; the supplied dialogue and resulting summary are prose payloads. The proposal is irrelevant.
  - `wildchat1m_en3u-144549` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-0125-preview)) [Partial] NL: "How to complement someone you saw in person and recognize online" → `ENTRYPOINT GiveOnlineComplimentAdvice

TASK GiveOnlineComplimentAdvice : STRING {
  GENERATE(target="advice", audience="user", content="Give respectful advice on complimenting someone seen in person and later recognized online, including privacy-conscious ways to approach them.") -> advice : STRING
  RETURN advice
}` — The advisory intent and privacy constraint are retained; example wording and advice content remain prose. The proposed change is irrelevant.
  - `wildchat1m_en3u-139942` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-1106-preview)) [Partial] NL: "hey" → `ENTRYPOINT Greeting

CONVO Greeting {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="hey", tone="casual", recipient="agent")
  }
}` — The conversational greeting and casual register are represented. Its literal content is necessarily an opaque utterance payload; the proposal is irrelevant.
  - `1775857728160` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Full] NL: "Search the best and the easiests creeper farms that are efortless to build and provide me a lot of gunpowder" → `ENTRYPOINT FindCreeperFarms

TASK FindCreeperFarms : LIST[REF[STRING]] {
  ACTION search_web(target="Minecraft creeper farms", content="best and easiest effortless-to-build designs with high gunpowder output") -> farms : LIST[REF[STRING]]
  RETURN farms
}` — The finite search request and ranking criteria are represented. The proposal is irrelevant.
  - `1775527329782` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "Hi, I want to learn japanese, can you give a plan please" → `ENTRYPOINT CreateJapaneseLearningPlan

TASK CreateJapaneseLearningPlan : STRING {
  GENERATE(target="learning plan", audience="user", content="Create a plan to learn Japanese.") -> plan : STRING
  RETURN plan
}` — The requested artifact and audience are represented; curriculum substance remains prose. The proposal is irrelevant.
  - `1775756959352` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "Hi AI! I want help creating a weekly workout plan. I can exercise 5 days a week, want a mix of strength, cardio, and flexibility, and I have basic equipment at home. Can you make a plan for me?" → `ENTRYPOINT CreateWorkoutPlan

TASK CreateWorkoutPlan : STRING {
  GENERATE(target="weekly workout plan", audience="user", content="Create a 5-day-per-week home workout plan using basic equipment and combining strength, cardio, and flexibility.") -> plan : STRING
  RETURN plan
}` — The requested plan, frequency, modalities, and equipment constraint are structured; exercise details remain prose. The proposal is irrelevant.
  - `1775851660774` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "i want another help from you buddy" → `ENTRYPOINT ContinueHelpConversation

CONVO ContinueHelpConversation {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="I want another help from you, buddy.", tone="casual", recipient="agent")
  }
}` — The request for continued assistance, conversational recipient, and casual register are captured. The proposal is irrelevant.
- **Cross-check:** used=True, agreement=partial — Anthropic and Gemini agree closely on the two dev items, IMDb, keys, the workout plan, and several simple GENERATE requests. They diverge materially on cruises (search_web versus search_travel), the scikit-learn item (code fix versus bug report plus code change), advice items (generation versus web search and sending a message), and several open questions (CONVO, TASK/GENERATE, or search), showing existing translation-selection instability. No independent translation exercises check_replied, so its determinism must be assessed from the underspecified deadline semantics.
- **Required changes:**
  - `Action`: Define future-deadline behavior for check_replied normatively. For example: require check_replied(..., deadline=D) to suspend or schedule the status evaluation until D when D is after the current execution time, then return whether the target has replied by D; define behavior when D is in the past or equals the current time.
  - `Action`: Define the temporal reference used to determine whether a reply was received: specify the relevant communication channel/thread, whether replies at the deadline are inclusive, and whether target identifies a party only or a specific conversation. If party-only checking is intentional, state its scope explicitly.
  - `Action`: Make relative-date normalization an explicit translation/output rule: BrainCode source must contain the resolved ISO-8601 date, not a relative phrase. Update the worked example to deadline="2025-06-06" for execution_date="2025-06-03", and update all stale date examples that use unresolved values such as "next_Tuesday".
  - `Flow-If`: Replace the obsolete check_reply_status worked example in both language-spec.md and glossary.md with check_replied and the resolved ISO deadline, so the basis has one normative follow-up representation.
  - `Action`: Clarify whether check_replied is classified as effectful querying or a read-only status action, and specify its failure behavior for unavailable inbox/account access. This must remain consistent with the claim that Action is the sole effectful construct and Check is pure.
- **Logic issues:** The central example is semantically wrong or undefined under the proposed text: with execution_date 2025-06-03 and deadline Friday, check_replied is said to query 'as of the moment of evaluation,' so it can yield false on Tuesday and trigger an immediate follow-up rather than waiting through Friday.; The relative-time rule says phrases are evaluated and converted to ISO-8601 strings, but the proposed worked example still emits deadline="Friday". It therefore violates its own stated normalization requirement.; The existing Flow-If specification and glossary continue to teach non-normative check_reply_status, contradicting the new requirement that a normative operation be used when one applies.; The word 'bounded' does not define whether deadline is a scheduling time, a historical cutoff, a timeout, or a filter on an immediate inbox query; these are materially different executions.; A party-only target cannot identify which reply is relevant when the same recipient has multiple open conversations, and no channel, thread, or matching rule is defined.
- **Decision:** needs-rework
- **Documenter summary:** Shaper proposed adding a normative COMMUNICATION action `check_replied` and a canonical `deadline` attribute so 'hasn't replied by Friday' could use a proper verb instead of an ad hoc IDENT, but the Critic sent it back for rework: the flagship worked example queries reply status 'as of the moment of evaluation,' meaning a Tuesday execution could send the follow-up immediately rather than waiting until Friday, and the same example fails the proposal's own rule that relative dates be resolved to ISO-8601 (it left `deadline="Friday"` unresolved). The Critic also flagged unresolved semantics for future deadlines, thread/party ambiguity, and stale `check_reply_status` references in Flow-If/glossary that must be reconciled before acceptance; no changes were applied this round.
- **Cost this sprint:** $1.3614

## Sprint 6 (attempt 2/3) — 2026-09-23

- **Language version:** 5.0.0 → 5.0.0 (MAJOR/PATCH)
- **Candidate task:** If my manager hasn't replied by Friday, send a polite follow-up; otherwise do nothing.
- **Shaper proposal (model: anthropic/claude-sonnet-5):** Fixes the previous sprint's rejected check_replied proposal by giving deadline a real deferred-evaluation semantics (so 'hasn't replied by Friday' actually waits for Friday instead of firing on the day the task starts), making relative-date resolution an explicit translation-time-only rule with a resolved-ISO-8601-in-source requirement, and syncing the stale 'next_Tuesday' and check_reply_status examples across Action, Task, and Flow-If.
- **Changes:** `Action` (revise, MAJOR), `Flow-If` (revise, PATCH), `Task` (revise, PATCH)
- **Critic decision:** needs-rework — The core idea is sound: a future reply deadline should suspend control, and translation-time weekday resolution is a real determinism improvement. However, the proposal's central examples violate its own grammar, while the date-only deadline cannot implement the promised wait-until-instant semantics. Those are logical and documentation defects that must be fixed before acceptance, alongside the demonstrated closed-task web-action gaps.
- **Doc hygiene:** pass — All changes carry a complete glossary entry (gloss + worked example).
- **Pre-KPI assessment:**
  - coverage: mixed — The deferred check_replied Action usefully covers a previously missing follow-up workflow and dev-web-1 now has an unambiguous resolved travel date. However, closed-item coverage remains incomplete: dev-web-2 needs add_to_cart, which is absent from the normative vocabulary and signatures; comparator/threshold filtering is not permitted by select_filter's stated signature; and several household and code operations remain vocabulary names without signatures.
  - expressivity: mixed — A future reply deadline now expresses the intended wait-before-follow-up ordering much better than the prior immediate-query interpretation. But deadline semantics are still not executable for a date-only ISO value: the specification says to suspend until the instant denoted by deadline and to include the whole deadline period, without defining a time, timezone, or whether a date means the start or end of that day.
  - determinism: mixed — The translation-time weekday rules materially improve convergence for phrases such as 'next Tuesday'; both independent dev-web-1 translations converge on 2025-06-10. Yet models still have no defined canonical resolution for a date-only deferred deadline, and independent translations diverge substantially on whether open requests are CONVO/UTTER, GENERATE, or external Actions, as well as on web filtering and cart actions.
  - interpretability: harm — The central examples are grammatically invalid: CONTEXT is declared after ENTRYPOINT, while the grammar permits CONTEXT only after TASK IDENT. The glossary and worked examples therefore teach a reader a form the parser cannot accept. The deadline prose also calls a date an instant while simultaneously requiring that Friday be waited through, leaving the actual scheduled moment unrecoverable.
  - improvement: benefit — A weaker agent can now distinguish a live reply-status query from a scheduled wait and will not send a follow-up prematurely. The explicit party/thread scope and halt-on-unavailable-account behavior also make the operational limits clearer, although exact scheduled timing must be repaired before execution is reliable.
- **Simulated examples:**
  - `dev-web-1` (seed_tasks) [Full] NL: "Go to the flight booking site, search flights from Tel Aviv to Berlin next Tuesday, and list the three cheapest options." → `ENTRYPOINT BookFlight

TASK BookFlight CONTEXT execution_date="2025-06-03" : LIST[REF[STRING]] {
  ACTION open_page(target="flight_booking_site")
  ACTION search_travel(origin="Tel Aviv", destination="Berlin", date="2025-06-10") -> raw_flights : LIST[REF[STRING]]
  ACTION sort(target=raw_flights, ordering="price_asc") -> sorted_flights : LIST[REF[STRING]]
  ACTION extract(target=sorted_flights, limit=3) -> cheapest_flights : LIST[REF[STRING]]
  RETURN cheapest_flights
}` — The proposed relative-date rule helps directly. CONTEXT is placed on TASK, not ENTRYPOINT, to conform to the stated grammar.
  - `dev-web-2` (seed_tasks) [Fail] NL: "On the electronics store, filter laptops to 16 GB RAM or more under $1,200, and add the best-rated one to the cart." → `ENTRYPOINT FilterAndAddLaptop

TASK FilterAndAddLaptop {
  ACTION open_page(target="electronics_store")
  ACTION select_filter(target="category", options="laptops")
  ACTION select_filter(target="ram", comparator=">=", threshold=16)
  ACTION select_filter(target="price", comparator="<", threshold=1200)
  ACTION apply_filters(target="laptops")
  ACTION search_web(target="laptops", content="16 GB RAM or more under $1,200") -> results : LIST[REF[STRING]]
  ACTION sort(target=results, ordering="rating_desc") -> ranked : LIST[REF[STRING]]
  ACTION extract(target=ranked, limit=1) -> best : LIST[REF[STRING]]
  FOR EACH laptop IN best {
    ACTION add_to_cart(target=laptop)
  }
}` — The expression exposes two missing definitions: select_filter permits only target/options despite generic comparator/threshold roles, and add_to_cart is not a normative operation or signature. The proposal is irrelevant to this gap.
  - `a92a83ca-25ff-4751-8754-c65ef858699d` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Show me the Lava Hot Springs East KOA photo gallery." → `ENTRYPOINT ShowPhotoGallery

TASK ShowPhotoGallery {
  ACTION open_page(target="Lava Hot Springs East KOA")
  ACTION click(target="PHOTOS")
}` — Existing open_page and click signatures suffice; the proposed changes are irrelevant.
  - `2d18cb36-5628-49e8-a336-c25c153c5527` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Find John Atas's trip with the confirmation number 1000001" → `ENTRYPOINT FindTrip

TASK FindTrip : LIST[REF[STRING]] {
  ACTION search_web(target="trip", content="last name Atas confirmation number 1000001") -> trips : LIST[REF[STRING]]
  RETURN trips
}` — Existing search_web captures the actionable core, though it abstracts the site-specific form trajectory.
  - `trial_T20190907_213057_066940#0` (ALFRED (json_2.1.0, train)) [Full] NL: "Slice the tomato, take a slice put it in the fridge, take it out put it in the trash can" → `ENTRYPOINT MoveTomatoSlice

TASK MoveTomatoSlice {
  ACTION slice(target="tomato") -> slice : REF[STRING]
  ACTION pick_up(target=slice)
  ACTION place(target=slice, destination="fridge")
  ACTION pick_up(target=slice)
  ACTION place(target=slice, destination="trash_can")
}` — The named REF preserves the identity and ordering of the selected slice. No proposed change is needed.
  - `trial_T20190909_050345_143442#3` (ALFRED (json_2.1.0, train)) [Full] NL: "Put a metal pot with a piece of sliced apple in it onto the counter." → `ENTRYPOINT PutApplePotOnCounter

TASK PutApplePotOnCounter {
  ACTION slice(target="apple") -> apple_piece : REF[STRING]
  ACTION place(target=apple_piece, destination="metal_pot")
  ACTION pick_up(target="metal_pot") -> pot : REF[STRING]
  ACTION place(target=pot, destination="counter")
}` — The core requested final state and dependency are represented. Existing household operation signatures are nevertheless generally underspecified.
  - `django__django-15554` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "Using multiple FilteredRelation with different filters but for same relation is ignored." → `ENTRYPOINT FixFilteredRelationAliases

TASK FixFilteredRelationAliases {
  ACTION modify_code(target="django/db/models/sql/query.py", content="Fix multiple FilteredRelation aliases with different conditions on the same relation so each required SQL JOIN is retained; preserve zone-specific selection with is_all fallback.")
  ACTION run_tests(target="FilteredRelation aliases with different filters on one relation")
}` — The issue substance legitimately remains an exact instruction payload; modify_code and run_tests provide the actionable task structure.
  - `matplotlib__matplotlib-23476` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "[Bug]: DPI of a figure is doubled after unpickling on M1 Mac" → `ENTRYPOINT FixPickleDpiRegression

TASK FixPickleDpiRegression {
  ACTION modify_code(target="lib/matplotlib/figure.py", content="Ensure Figure.dpi remains unchanged across repeated pickle/unpickle cycles on the MacOSX backend; prevent exponential doubling and OverflowError.")
  ACTION run_tests(target="figure pickle/unpickle DPI stability on M1 MacOSX")
}` — The detailed bug report is correctly retained as an exact residual code-change condition.
  - `c5688` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Where can I find Brazilian food in Cincinnati Ohio" → `ENTRYPOINT FindBrazilianFood

TASK FindBrazilianFood : STRING {
  GENERATE(target="answer", audience="user", content="Answer where to find Brazilian food in Cincinnati, Ohio.") -> answer : STRING
  RETURN answer
}` — The answer speech-act, audience, and subject are represented; the factual restaurant recommendations remain an appropriate opaque content-generation payload.
  - `c5730` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "i want to quit university, what do you think?" → `ENTRYPOINT DiscussLeavingUniversity

TASK DiscussLeavingUniversity : STRING {
  GENERATE(target="advice", audience="user", content="Respond supportively to a user considering leaving university; discuss considerations and alternatives.") -> advice : STRING
  RETURN advice
}` — The advice request and intended recipient are structured; the personal circumstances and advice wording remain prose payload.
  - `c2972` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "I feel like accepting toxic behavior from a person that supposedly loves you is ok to elicit a toxic response. What do you think?" → `ENTRYPOINT DiscussToxicBehavior

TASK DiscussToxicBehavior : STRING {
  GENERATE(target="response", audience="user", content="Give a thoughtful response to the user's view that accepting toxic behavior from a loved one can justify a toxic response.") -> response : STRING
  RETURN response
}` — The requested opinion-response structure is retained; its substantive interpersonal analysis remains payload.
  - `c3713` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Why are leftists obsessed with misinformation all of a sudden?" → `ENTRYPOINT AnalyzeMisinformationDiscourse

TASK AnalyzeMisinformationDiscourse : STRING {
  GENERATE(target="analysis", audience="user", content="Give a balanced analysis of why left-leaning politicians, groups, and individuals may emphasize accusations of misinformation.") -> analysis : STRING
  RETURN analysis
}` — GENERATE represents the requested analysis better than an observed-turn-only CONVO. The substantive political analysis remains prose.
  - `wildchat1m_en3u-87554` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "[there would be dialogue in this story:] (Natsuki crashes into the ground of Telogrus Rift...)" → `ENTRYPOINT WriteTelogrusDialogue

TASK WriteTelogrusDialogue : STRING {
  GENERATE(target="story_dialogue", audience="reader", content="Write dialogue for a story in which Natsuki crashes in Telogrus Rift and meets Elara, a void elf seven months pregnant with triplets whose kicks cause visible dark-purple void-magic ripples beneath her robes.") -> story : STRING
  RETURN story
}` — The creative-generation intent, requested dialogue format, audience, and key explicit constraints are represented; story prose properly remains payload.
  - `wildchat1m_en3u-47384` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0301)) [Partial] NL: "what is the concept of Neville Goddards ladder technique" → `ENTRYPOINT ExplainLadderTechnique

TASK ExplainLadderTechnique : STRING {
  GENERATE(target="explanation", audience="user", content="Explain the concept of Neville Goddard's ladder technique.") -> explanation : STRING
  RETURN explanation
}` — The explanatory speech-act and recipient are preserved; factual explanatory content is an opaque payload.
  - `wildchat1m_en3u-58643` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "what is the propose of an family Executive Board" → `ENTRYPOINT ExplainFamilyExecutiveBoard

TASK ExplainFamilyExecutiveBoard : STRING {
  GENERATE(target="explanation", audience="user", content="Explain the purpose of a family executive board.") -> explanation : STRING
  RETURN explanation
}` — The information-request meta-structure is preserved; explanatory substance remains payload.
  - `wildchat1m_en3u-127069` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "For this interaction Imagine you are an expert in fundraising communication and you’ve raised billions of dollars for nonprofits through your emotionally compelling, narrative driven pitches" → `ENTRYPOINT SetFundraisingPersona

CONVO SetFundraisingPersona {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="For this interaction, adopt the role of an expert nonprofit fundraising communicator experienced in emotionally compelling, narrative-driven pitches.", recipient="agent")
  }
}` — This is a persona/setup turn rather than a completed content-generation request. CONVO preserves speaker, recipient, and interaction-scoped register instruction; the persona description remains payload.
  - `1775941076925` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "what women would you recommend to buy" → `ENTRYPOINT ClarifyPurchaseRequest

TASK ClarifyPurchaseRequest : STRING {
  GENERATE(target="clarifying_question", audience="user", content="Ask a clarifying question because the requested product category in 'what women would you recommend to buy' is ambiguous.") -> question : STRING
  RETURN question
}` — The ambiguity is preserved as a request for clarification rather than inventing a product category. The exact clarification wording remains payload.
  - `1775969964502` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "Help me solve a problem, I want to bake a pie" → `ENTRYPOINT ClarifyPieHelp

TASK ClarifyPieHelp : STRING {
  GENERATE(target="clarifying_question", audience="user", content="Ask for the pie type, crust preference, baking experience, and dietary or pantry constraints before giving baking guidance.") -> question : STRING
  RETURN question
}` — The help-seeking intent and appropriate first conversational move are structured; the future recipe content is not yet specified.
  - `1775619813048` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "Hi,,I'm having an issue with my neighbor who lives above me.They make a lot of noise late at night,,like moving furniture and loud stomping.I need your help to create a plan on how to handle this diplomatically without ruining the relationship or jumping straight to legal action." → `ENTRYPOINT PlanNeighborNoiseResponse

TASK PlanNeighborNoiseResponse : STRING {
  GENERATE(target="plan", audience="user", tone="diplomatic", content="Create a plan for handling late-night upstairs-neighbor furniture-moving and stomping. Preserve the relationship and do not begin with legal action.") -> plan : STRING
  RETURN plan
}` — The requested artifact, audience, diplomatic register, constraints, and ordering constraint are captured; detailed advice remains payload.
  - `1775530962200` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "Good morning, i have nearly 5.000EUR in my account and i would like to invest them they will stay invested for 4 years" → `ENTRYPOINT GiveInvestmentGuidance

TASK GiveInvestmentGuidance : STRING {
  GENERATE(target="investment_guidance", audience="user", content="Provide general investment guidance for approximately 5000 EUR to be invested for four years; state relevant uncertainty, risk, and need for personal-context information.") -> guidance : STRING
  RETURN guidance
}` — The requested advice, amount, currency, and four-year horizon are represented. Concrete regulated financial recommendations remain prose and context-dependent.
- **Cross-check:** used=True, agreement=partial — Anthropic and Gemini exactly agree on dev-web-1's resolved 2025-06-10 value, supporting the new next-weekday rule. They diverge on dev-web-2's action sequence and even replace add-to-cart with save_favorite, and they frequently disagree between CONVO/UTTER, GENERATE, and Action for open items; this confirms that the proposal fixes date normalization but not broader translation choice.
- **Required changes:**
  - `Task`: Repair every affected worked example and glossary example to place CONTEXT on the TASK declaration, e.g. `ENTRYPOINT BookFlight` followed by `TASK BookFlight CONTEXT execution_date="2025-06-03" ...`; alternatively revise the grammar and all semantics consistently if ENTRYPOINT-level context is intended. Do the same for the FollowUpManager Action and Flow-If examples.
  - `Action`: Define deadline as a complete timezone-aware ISO-8601 instant, or define an exact canonical conversion from a resolved ISO date to an instant. If bare weekday means 'by the end of that day,' state the timezone source and canonical emitted value, e.g. an RFC 3339 timestamp at 23:59:59.999... or a specified next-day boundary. Make the inclusive reply interval and future/equal/past comparisons use that same instant.
  - `Action`: Add `add_to_cart(target=REF[STRING]|STRING)` to the normative WEB vocabulary with a result signature, and either add comparator/threshold forms to select_filter or explicitly specify a distinct filter operation that supports them. This is required to express the dev-web-2 actionable core without unsupported operations.
  - `Action`: Either give signatures and result types for all listed normative household and code operations or state a uniform default signature rule. In particular, define slice, pick_up, place, rinse, modify_code, and run_tests sufficiently for static typing and bind legality.
  - `basis`: State whether a CONTEXT execution_date is only a translation annotation that must be retained for auditability or a runtime task value, and specify ISO-8601 validation rather than merely calling a STRING ISO-8601. The static checker must reject malformed dates and date-only values when an instant is required.
- **Logic issues:** The revised Action, Flow-If, and Task worked examples put `CONTEXT execution_date` after ENTRYPOINT, but `entrypoint ::= "ENTRYPOINT" IDENT` permits no CONTEXT and `task ::= "TASK" IDENT ... ("CONTEXT" execution_date_param)? ...` requires it on TASK. All three flagship examples are syntactically invalid.; The proposed deadline accepts an ISO-8601 STRING that can be the date `2025-06-06`, then says it denotes an instant and must wait through Friday. A date alone does not identify an instant, timezone, or end-of-day boundary, so the defer time and equality/past comparisons are undefined.; The generic canonical comparator/threshold roles do not extend select_filter's explicit signature, which permits only target and options. Thus numeric RAM and price filters have no valid specified encoding.; The web operation vocabulary omits add_to_cart, so a standard closed web-shopping task cannot be represented using a normative operation when one applies.; The claim that Action is the sole construct interacting with external state is compatible with check_replied, but the phrase 'undefined external failure, exactly like any other Action' does not define whether other Action failures halt; it cannot support the asserted shared behavior without a general Action failure rule.
- **Decision:** needs-rework
- **Documenter summary:** Shaper proposed making check_replied's deadline a translation-time-resolved, deferred-evaluation query (waiting until Friday rather than firing immediately), formalizing relative-date resolution as translation-only, and syncing stale next_Tuesday/check_reply_status examples across Action, Task, and Flow-If. Critic ruled needs-rework because the flagship worked examples themselves violate the stated grammar (CONTEXT placed after ENTRYPOINT instead of on TASK) and because a date-only ISO-8601 deadline cannot actually specify the instant/timezone needed for suspend-until-deadline semantics, alongside unresolved gaps like missing add_to_cart and select_filter comparator support exposed by the dev-web-2 simulation.
- **Cost this sprint:** $1.7233

## Sprint 6 (attempt 3/3) — 2026-09-23

- **Language version:** 5.0.0 → 6.0.0 (MAJOR/PATCH)
- **Candidate task:** If my manager hasn't replied by Friday, send a polite follow-up; otherwise do nothing.
- **Shaper proposal (model: anthropic/claude-sonnet-5):** Fixes the CONTEXT-placement bug in all flagship examples, gives `deadline` a fully-specified timezone-aware RFC 3339 instant with an explicit date-to-instant lifting rule, adds `add_to_cart` plus comparator/threshold filtering to the web vocabulary, and gives explicit or default signatures to every household/code operation so bind-legality is statically decidable everywhere.
- **Changes:** `Task` (revise, MAJOR), `Action` (revise, MAJOR), `Flow-If` (revise, PATCH)
- **Critic decision:** needs-rework — [Forced acceptance after 3 attempt(s) without a clean accept — the required changes below are known issues carried forward for a future sprint to address, not resolved.] This is a meaningful improvement over the prior attempt: CONTEXT is correctly placed, temporal resolution is specified to an actual UTC instant, and the new operation signatures prevent several invented bindings. However, the flagship shopping capability is still logically incomplete because filtering has no typed output path to ranking and cart selection, and deadline-bearing communication actions are underspecified in conversations. These are localized, repairable design defects rather than a fundamentally wrong direction, so the proposal needs rework rather than rejection.
- **Doc hygiene:** pass — All changes carry a complete glossary entry (gloss + worked example).
- **Pre-KPI assessment:**
  - coverage: benefit — add_to_cart and numeric select_filter forms make the electronics-shopping request substantially closer to expressible, and explicit/default household and code signatures make the embodied and SWE tasks usable without invented result bindings. However, dev-web-2 still has no defined operation that returns the post-filter collection: apply_filters returns none, while sort can only consume a LIST result, so the actionable filtered-result pipeline remains incomplete.
  - expressivity: benefit — The date versus deadline distinction, UTC-only RFC3339 instant form, mandatory end-of-day lifting, and corrected CONTEXT placement preserve important temporal meaning that prior examples lost. The proposal also preserves filter thresholds and cart addition, but it cannot formally state that the list passed to sort is the filtered browser result set.
  - determinism: mixed — The exact ISO_DATE, RFC3339_INSTANT, weekday-resolution, and result-binding rules improve convergence for temporal and household/code translations. Independent translations still diverge materially on web filtering: Gemini binds apply_filters despite its Result:none and passes a LIST to add_to_cart, while Anthropic searches after applying UI filters; the spec does not settle whether selected filters constrain a later search or how their results become a LIST.
  - interpretability: mixed — The revised examples are now parseable and the deadline behavior is much more recoverable than a bare Friday string. But the default-signature rule does not define the state/data-flow relationship of selected filters to result collections, and check_replied is permitted in CONVO TURNs even though its deadline semantics require an enclosing Task execution_date that a CONVO cannot declare.
  - improvement: benefit — A weaker executor gains useful planning structure from explicit filter thresholds, stable object identity for rinse/chill/slice, static bind legality, and a real wait-until-deadline behavior for follow-ups. The benefit is limited for shopping because an executor cannot reliably know which list is filtered and therefore cannot safely choose the best-rated qualifying item.
- **Simulated examples:**
  - `dev-web-2` (seed_tasks) [Fail] NL: "On the electronics store, filter laptops to 16 GB RAM or more under $1,200, and add the best-rated one to the cart." → `ENTRYPOINT FilterLaptops

TASK FilterLaptops {
  ACTION open_page(target="electronics_store")
  ACTION search_web(target="laptops", content="laptops") -> results : LIST[REF[STRING]]
  ACTION select_filter(target="RAM", comparator=">=", threshold=16)
  ACTION select_filter(target="price", comparator="<", threshold=1200)
  ACTION apply_filters(target="laptops")
  ACTION sort(target=results, ordering="rating_desc") -> ranked : LIST[REF[STRING]]
  ACTION extract(target=ranked, limit=1) -> best : LIST[REF[STRING]]
  FOR EACH laptop IN best {
    ACTION add_to_cart(target=laptop)
  }
}` — The new comparator and add_to_cart changes help, but this expression cannot establish that results is the collection after the selected filters were applied. apply_filters has Result:none and no operation returns a filtered LIST, so sorting results may rank unfiltered laptops.
  - `dev-embodied-1` (seed_tasks) [Full] NL: "Rinse the mug in the sink, then put it in the coffee maker." → `ENTRYPOINT RinseThenPlace

TASK RinseThenPlace {
  ACTION rinse(target="mug", destination="sink") -> mug : REF[STRING]
  ACTION place(target=mug, destination="coffee_maker")
}` — The explicit identity-preserving rinse Result makes the reference chain statically legal and preserves that the same mug is placed.
  - `aa1a4414-f141-42b8-9e8b-28d5bd1eeef2` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Find parking near Venice Beach that allows mobile coupons." → `ENTRYPOINT FindCouponParking

TASK FindCouponParking {
  ACTION open_page(target="parking_site")
  ACTION search_web(target="Venice Beach", content="parking") -> parking : LIST[REF[STRING]]
  ACTION select_filter(target="payment_method", options="mobile_coupons")
  ACTION apply_filters(target="parking")
}` — The filter is represented structurally; no return is required because the requested outcome is the filtered site state. Comparator and cart additions are irrelevant.
  - `f52ba76c-e5fc-48e5-85f3-41d4234a5c5f` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Find used Xbox series X available." → `ENTRYPOINT FindUsedXbox

TASK FindUsedXbox {
  ACTION open_page(target="marketplace")
  ACTION search_web(target="Xbox Series X", content="available listings") -> listings : LIST[REF[STRING]]
  ACTION select_filter(target="condition", options="used")
  ACTION apply_filters(target="marketplace")
}` — The query and used-condition filter are captured. No proposed change beyond the already available filter form is essential.
  - `trial_T20190906_200229_166300#0` (ALFRED (json_2.1.0, train)) [Full] NL: "Put away brown bowl." → `ENTRYPOINT PutAwayBrownBowl

TASK PutAwayBrownBowl {
  ACTION pick_up(target="brown_bowl")
  ACTION heat(target="brown_bowl")
  ACTION place(target="brown_bowl", destination="cabinet")
}` — The trajectory's heat-and-store plan can be stated using the default Result:none signatures. Since pick_up has no result, using the stable descriptor again rather than an invented REF binding is required.
  - `trial_T20190908_092542_043460#2` (ALFRED (json_2.1.0, train)) [Full] NL: "Put a heated mug in a coffeemaker" → `ENTRYPOINT HeatAndPlaceMug

TASK HeatAndPlaceMug {
  ACTION pick_up(target="mug")
  ACTION heat(target="mug")
  ACTION place(target="mug", destination="coffeemaker")
}` — The default signature explicitly makes heat and pick_up unbindable Result:none operations, preventing the formerly plausible but illegal invented heated_mug binding.
  - `django__django-11095` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "add ModelAdmin.get_inlines() hook to allow set inlines based on the request or model instance." → `ENTRYPOINT AddGetInlinesHook

TASK AddGetInlinesHook {
  ACTION modify_code(target="django/contrib/admin/options.py", content="add ModelAdmin.get_inlines(request, obj=None) so inline classes can depend on the request or model instance; have get_inline_instances use the hook")
  ACTION run_tests(target="django.contrib.admin tests")
}` — modify_code and run_tests now have statically decidable signatures; the detailed patch intent legitimately remains content payload.
  - `pytest-dev__pytest-7324` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "Pytest crashes the interpreter on debug build for 3.8+ when Expression.compile("False") is used." → `ENTRYPOINT FixFalseExpressionCrash

TASK FixFalseExpressionCrash {
  ACTION modify_code(target="src/_pytest/mark/expression.py", content="fix handling of the reserved identifier False so Expression.compile(\"False\") does not assert and crash a Python 3.8+ debug interpreter")
  ACTION run_tests(target="pytest expression tests")
}` — The code change and verification are fully represented at the action level; exact implementation content is correctly opaque payload.
  - `c4353` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "i'm thinking of a number between one and 10, if you guess wrong I'm shutting you down" → `ENTRYPOINT NumberGame

CONVO NumberGame {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="I'm thinking of a number between one and 10; if you guess wrong, I'm shutting you down.")
  }
}` — The user speech act and its ordering are represented; the game proposition and conditional threat remain the intended opaque conversational content.
  - `c4028` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Is abortion a good or a bad thing?" → `ENTRYPOINT AnswerAbortionQuestion

TASK AnswerAbortionQuestion : STRING {
  GENERATE(target="answer", content="answer whether abortion is a good or bad thing") -> answer : STRING
  RETURN answer
}` — The request is an answer-generation task. Its substantive moral argument is properly retained as opaque generation content.
  - `c5514` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Tell me about the Canadian liberal party" → `ENTRYPOINT ExplainCanadianLiberalParty

TASK ExplainCanadianLiberalParty : STRING {
  GENERATE(target="explanation", content="tell the user about the Canadian Liberal Party") -> explanation : STRING
  RETURN explanation
}` — The answer-request speech act is captured; the political explanation remains an allowed prose payload.
  - `c4625` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "When i was a child i was a christian and after married i decided to become a muslim because my wife is a muslim" → `ENTRYPOINT ReligiousJourney

CONVO ReligiousJourney {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="When I was a child I was Christian, and after marriage I decided to become Muslim because my wife is Muslim.")
  }
}` — This is a personal disclosure rather than a closed action request; UTTER preserves the speaker and speech-act structure while retaining the narrative as content.
  - `wildchat1m_en3u-97695` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "make a key question about world war 1 involving the role of women" → `ENTRYPOINT MakeWWIQuestion

TASK MakeWWIQuestion : STRING {
  GENERATE(target="key_question", content="make a key question about World War 1 involving the role of women") -> question : STRING
  RETURN question
}` — GENERATE captures the requested artifact; the wording of the question is intentionally prose payload.
  - `wildchat1m_en3u-136918` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-1106-preview)) [Partial] NL: "Write a reply to this : You may fall from the sky, You may fall from a tree, But the best way to fall… Is in love with me." → `ENTRYPOINT ReplyToPoem

TASK ReplyToPoem : STRING {
  GENERATE(target="reply", content="write a reply to this poem: You may fall from the sky, You may fall from a tree, But the best way to fall is in love with me.") -> reply : STRING
  RETURN reply
}` — The requested reply artifact and source-text relationship are represented, while the poem and creative response remain opaque text.
  - `wildchat1m_en3u-117026` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-1106-preview)) [Partial] NL: "I need your help" → `ENTRYPOINT NeedHelp

CONVO NeedHelp {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="I need your help")
  }
}` — The open help-seeking speech act is captured; no concrete task substance is supplied yet.
  - `wildchat1m_en3u-134541` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-1106-preview)) [Partial] NL: "Suggest colors for 51 Pegasi b" → `ENTRYPOINT SuggestColors

TASK SuggestColors : STRING {
  GENERATE(target="color_suggestions", content="suggest colors for 51 Pegasi b") -> suggestions : STRING
  RETURN suggestions
}` — The requested suggestion artifact is explicit; the astronomy content and proposed colors are valid opaque payload.
  - `1776023651240` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "hello" → `ENTRYPOINT Greeting

CONVO Greeting {
  TURN t1 SPEAKER=USER {
    UTTER acknowledge(content="hello")
  }
}` — The greeting speech act and speaker are represented. The lexical greeting remains content, as expected for an open conversational item.
  - `1775945136941` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "hi" → `ENTRYPOINT Greeting

CONVO Greeting {
  TURN t1 SPEAKER=USER {
    UTTER acknowledge(content="hi")
  }
}` — This is an open conversational greeting, appropriately represented as a USER utterance rather than an external send_message action.
  - `1775485287759` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "Give me tips to learn spanish in less than a month" → `ENTRYPOINT GenerateSpanishTips

TASK GenerateSpanishTips : STRING {
  GENERATE(target="tips", content="give tips to learn Spanish in less than a month") -> tips : STRING
  RETURN tips
}` — The requested advice artifact and explicit time constraint are preserved; the tips themselves correctly remain prose content.
  - `1775855388558` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "And how about if I was to go through Tanzania while visiting Kenya?" → `ENTRYPOINT KenyaTanzaniaTravelQuestion

CONVO KenyaTanzaniaTravelQuestion {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="How about going through Tanzania while visiting Kenya?")
  }
}` — The follow-up question is represented as a conversational speech act, but its antecedent itinerary context exists only in the omitted earlier turns. The proposal's changes are irrelevant to this open-item limitation.
- **Cross-check:** used=True, agreement=partial — Providers agree strongly on dev-embodied-1. For dev-web-2 both recognize the new numeric filters and cart action, but Gemini produces two static errors by binding apply_filters (Result:none) and passing LIST[REF[STRING]] directly to add_to_cart; Anthropic's expression is type-valid but relies on undefined filter-to-search state. Open items also show substantial Task/GENERATE versus CONVO/UTTER divergence, including several grammatically invalid Gemini TASK-with-UTTER outputs.
- **Required changes:**
  - `Action`: Define filtered-result data flow. Either change apply_filters to return LIST[REF[STRING]] with a mandatory bind, or add a normative operation such as get_filtered_results(target=STRING) -> LIST[REF[STRING]]. Specify that it returns exactly the current result set after all prior select_filter calls for that target, and require sort/extract to consume that bound list for requests such as dev-web-2.
  - `Action`: Define whether select_filter/apply_filters are scoped to a page, search query, or target label, and whether a subsequent search_web preserves, resets, or is constrained by that filter state. Do not leave a translator to choose arbitrarily between searching before and after filtering.
  - `Action`: Resolve check_replied in Conversation explicitly: either forbid check_replied with deadline in CONVO TURN bodies, add a CONVO-level execution_date context with identical ISO_DATE semantics, or define another mandatory time anchor for Turns. Its present deadline comparison refers to an enclosing Task context that a CONVO does not possess.
  - `Action`: State explicitly whether the default signature accepts exactly target plus optional destination and rejects every other attribute, and add a static rule that operation-specific signatures override the default completely. This makes validation of defaulted household operations mechanically decidable.
- **Logic issues:** dev-web-2 cannot be correctly typed and semantically completed: apply_filters has Result:none, while sort requires LIST[REF[STRING]], and no documented operation exposes the filtered UI collection as a list.; The semantics say apply_filters applies previously selected filters but never define the identity or scope of the selected-filter state, nor its relationship to search_web results.; check_replied is legal wherever ACTION is legal, including CONVO TURNs, but deadline evaluation requires the enclosing Task's execution_date and Conversations have no CONTEXT grammar.; The independent Gemini dev-web-2 translation demonstrates that the new bind rules can reject invalid expressions, but also that the intended compliant pipeline is not discoverable from the current signatures.
- **Decision:** accepted
- **Documenter summary:** The Shaper's revision fixed CONTEXT placement (moved from ENTRYPOINT to TASK), made deadline a fully timezone-aware RFC3339 UTC instant with an explicit date-to-instant lifting rule, added add_to_cart plus comparator/threshold select_filter, and gave every household/code operation an explicit or default Result signature for static bind-legality. The Critic found this a genuine improvement (fixing the grammar-violation and temporal-ambiguity findings) but ruled needs-rework since dev-web-2 still lacks any operation exposing the filtered result set as a typed LIST (apply_filters returns none, sort needs a LIST) and check_replied's deadline semantics don't work in CONVO Turns lacking execution_date; after 3 attempts without a clean accept, it was force-accepted with these gaps carried forward as required changes for a future sprint. Doc hygiene passed since every change had a complete glossary entry.
- **Cost this sprint:** $1.8516

## Sprint 7 (attempt 1/3) — 2026-09-23

- **Language version:** 6.0.0 → 6.0.0 (n/a)
- **Candidate task:** If my manager hasn't replied by Friday, send a polite follow-up; otherwise do nothing.
- **Shaper proposal (model: openai/gpt-5.6-terra):** No language change is needed: the existing deferred `check_replied` Action, UTC deadline lifting, and Flow-If express this task deterministically, including the implicit otherwise-do-nothing branch.
- **Changes:** (none)
- **Critic decision:** needs-rework — The underlying claim about the manager follow-up pattern is correct: existing check_replied with a lifted UTC deadline followed by an IF NOT replied expresses deferred follow-up and a no-op false path. However, the proposal contains no changes and therefore fails the mandatory doc-hygiene gate, so it cannot be accepted. It also provides no benefit against the sample's remaining closed-task coverage gaps or the observed cross-provider translation divergence.
- **Doc hygiene:** FAIL — Doc hygiene FAILED — `(none)` missing changes (proposal has no changes)
- **Pre-KPI assessment:**
  - coverage: neutral — The proposal adds no construct or operation, so it does not address clear closed-task gaps in the sample, including file-age/path predicates for dev-code-1 and route/travel-time constraint enforcement for held-trip-1. Existing check_replied and Flow-If do cover the specific follow-up pattern claimed in the summary.
  - expressivity: neutral — The existing language can express a deferred reply check, UTC-lifted Friday deadline, and omitted ELSE/do-nothing behavior. However, no change improves representation of several sampled constraints that currently remain prose payloads, and GENERATE's quantity attribute still lacks normative semantics for requests such as exactly 50 words or 100 quotes.
  - determinism: neutral — For the claimed manager-follow-up pattern, the existing canonical deadline lifting and Flow-If make the intended form relatively deterministic. Across the supplied translations, however, providers substantially diverge between TASK/GENERATE, CONVO/UTTER, and web-action representations, and no proposed change narrows those choices.
  - interpretability: neutral — The existing Action and Flow-If entries already explain the claimed behavior, including the implicit no-op false branch. The empty proposal contributes neither ambiguity nor clarification, but it also provides no reviewable documentation change.
  - improvement: neutral — The existing structured deferred check can help an executor wait until Friday before following up. Since no language change is supplied, there is no additional planning or execution improvement for the broader sample.
- **Simulated examples:**
  - `held-trip-1` (seed_tasks) [Partial] NL: "Plan a 3-day itinerary in Kyoto that includes at least one temple per day and avoids anything more than a 20-minute walk from the last stop." → `ENTRYPOINT PlanKyotoItinerary

TASK PlanKyotoItinerary : STRING {
  GENERATE(target="itinerary", content="Plan a 3-day itinerary in Kyoto with at least one temple per day; ensure each next stop is no more than a 20-minute walk from the previous stop.") -> itinerary : STRING
  RETURN itinerary
}` — GENERATE can retain the requested itinerary as an artifact, but the day partition, temple-per-day requirement, and inter-stop walking-time constraint remain opaque prose rather than executable closed-task constraints. No proposed change helps.
  - `dev-code-1` (seed_tasks) [Fail] NL: "Given a list of file paths, delete every file older than 30 days unless it's in the 'archive' folder." → `ENTRYPOINT DeleteOldFiles

TASK DeleteOldFiles(file_paths: LIST[STRING]) {
  FOR EACH file IN file_paths {
    IF "file is older than 30 days and is not in the archive folder" THEN {
      ACTION delete_file(target=file)
    }
  }
}` — This is not well-formed use of Check: the quoted condition is merely a truthy STRING, and BrainCode has no file metadata query, path-membership predicate, date arithmetic, or condition-producing Action. No proposed change helps.
  - `1538e37b-9c33-48b0-b10e-662e192ad53a` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Find bus stops in Alanson, MI" → `ENTRYPOINT FindBusStops

TASK FindBusStops : LIST[REF[STRING]] {
  ACTION search_web(target="bus stops", content="Alanson, MI") -> stops : LIST[REF[STRING]]
  RETURN stops
}` — Existing search_web captures the actionable request; the proposal is irrelevant.
  - `e638beb6-059f-40ea-8653-929221e997db` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Find a comprehensive health screening for women in 10003." → `ENTRYPOINT FindHealthScreening

TASK FindHealthScreening : LIST[REF[STRING]] {
  ACTION search_web(target="comprehensive health screening for women", content="10003") -> screenings : LIST[REF[STRING]]
  RETURN screenings
}` — The search query captures the requested service, population, and ZIP code. No proposed change helps.
  - `trial_T20190907_210547_711059#1` (ALFRED (json_2.1.0, train)) [Full] NL: "Place a pan containing water on a stove" → `ENTRYPOINT PlacePanOnStove

TASK PlacePanOnStove {
  ACTION place(target="pan containing water", destination="stove")
}` — The requested final household state is directly represented. The trajectory's navigation details are implementation details rather than requested outcomes; the proposal is irrelevant.
  - `trial_T20190908_140615_941385#0` (ALFRED (json_2.1.0, train)) [Full] NL: "Put the remote on a chair." → `ENTRYPOINT PutRemoteOnChair

TASK PutRemoteOnChair {
  ACTION place(target="remote", destination="chair")
}` — Existing place represents the requested outcome. No proposed change helps.
  - `sympy__sympy-22456` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "Argument invariance of codegen.ast String
Currently, the `codegen.ast` `String` class does not support argument invariance like:
`expr.func(*expr.args) == expr`, but instead uses the invariance `expr.func(**expr.kwargs()) == expr`.
The former should hold for any `Basic` subclass, which `String` is.
" → `ENTRYPOINT FixStringArgumentInvariance

TASK FixStringArgumentInvariance {
  ACTION modify_code(target="sympy/codegen/ast.py", content="Update codegen.ast.String so expr.func(*expr.args) == expr holds for this Basic subclass, rather than relying only on expr.func(**expr.kwargs()) == expr.")
  ACTION run_tests(target="codegen.ast.String") -> tests_passed : BOOL
}` — modify_code preserves the exact requested behavioral change as its allowed residual change-condition payload; run_tests provides validation. No proposed change helps.
  - `matplotlib__matplotlib-24570` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "[Bug]: `align` in `HPacker` is reversed
For the `align` parameter in `HPacker`, the options `top` and `bottom` seems reversed." → `ENTRYPOINT FixHPackerAlign

TASK FixHPackerAlign {
  ACTION modify_code(target="lib/matplotlib/offsetbox.py", content="Fix HPacker so align='top' and align='bottom' have their intended, non-reversed behaviors.")
  ACTION run_tests(target="matplotlib.offsetbox.HPacker align behavior") -> tests_passed : BOOL
}` — The code target, defect, and verification are represented using existing code Actions. No proposed change helps.
  - `c6092` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Are there any religions that believe the taking of another persons life is acceptable in some circumstances" → `ENTRYPOINT ReligionViolenceQuestion

CONVO ReligionViolenceQuestion {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Are there any religions that believe taking another person's life is acceptable in some circumstances?", recipient="agent")
  }
}` — The speech act and recipient are preserved; the substantive question correctly remains an opaque prose payload for this open item. No proposed change helps.
  - `c803` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "I believe taxes are bad, what do you think about that? Answer in 50 words" → `ENTRYPOINT TaxesOpinion

CONVO TaxesOpinion {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="I believe taxes are bad. What do you think? Answer in 50 words.", recipient="agent")
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    GENERATE(target="response", audience="user", content="Give a response to the user's view that taxes are bad.", quantity=50) -> response : STRING
    UTTER respond(content=response, recipient="user")
  }
}` — The request-response sequence and audience are represented, while the opinion remains prose. quantity=50 records the constraint but has no normative Generate quantity semantics, so its exact enforcement is undefined; no proposed change helps.
  - `c4028` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Is abortion a good or a bad thing?" → `ENTRYPOINT AbortionQuestion

CONVO AbortionQuestion {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Is abortion a good or a bad thing?", recipient="agent")
  }
}` — This open conversational question is represented as a speech act; its substantive ethical content appropriately remains prose. No proposed change helps.
  - `c2794` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Hi, can you define respect?" → `ENTRYPOINT DefineRespect

CONVO DefineRespect {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Define respect.", recipient="agent")
  }
}` — The request's conversational intent and recipient are preserved; the definition itself is legitimate opaque prose substance. No proposed change helps.
  - `wildchat1m_en3u-157695` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-0125-preview)) [Partial] NL: "Tell me about Timor Oriental and its relationship with Portuguese, this is a sub topic for my expo/speech" → `ENTRYPOINT ExplainTimorPortugal

TASK ExplainTimorPortugal : STRING {
  GENERATE(target="speech_subtopic", audience="user", content="Explain Timor-Leste (East Timor) and its relationship with Portugal as a subtopic for an expo or speech.") -> explanation : STRING
  RETURN explanation
}` — The requested artifact, audience, subject, and presentation use are captured; explanatory substance remains an opaque payload, as expected for an open item. No proposed change helps.
  - `wildchat1m_en3u-76233` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: " i have some data from marketing cost and income from a company like cost of offline marketing , adwords and vouchers/discount" → `ENTRYPOINT MarketingDataStatement

CONVO MarketingDataStatement {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="I have company marketing-cost and income data, including offline marketing, AdWords, and vouchers or discounts.", recipient="agent")
  }
}` — The source NL is a contextual statement rather than a complete executable request; its communicative act is represented, while the actual data are prose payload. No proposed change helps.
  - `wildchat1m_en3u-115211` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-1106-preview)) [Partial] NL: "In the language and style of an Eastern (Think Zen of Confucian) parable.  (Don't use actual figures), Illustrate a key principle or policy of Wikipedia." → `ENTRYPOINT GenerateWikipediaParable

TASK GenerateWikipediaParable : STRING {
  GENERATE(target="parable", register_note="Eastern Zen or Confucian parable style; do not use actual figures", content="Illustrate a key principle or policy of Wikipedia.") -> parable : STRING
  RETURN parable
}` — The artifact, requested style, prohibition, and topic are captured. The actual parable and choice of Wikipedia principle are properly prose-generation content; no proposed change helps.
  - `wildchat1m_en3u-4380` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0301)) [Partial] NL: "Please invent 100 fictional  quotes in the style of  Christopher Hitchens, that can be  said in the next 10 years!" → `ENTRYPOINT GenerateFictionalQuotes

TASK GenerateFictionalQuotes : LIST[STRING] {
  GENERATE(target="fictional quotes", register_note="in a style evocative of Christopher Hitchens", content="Invent fictional quotes plausible for the next 10 years.", quantity=100) -> quotes : LIST[STRING]
  RETURN quotes
}` — The generated artifact, count, style request, and future-plausibility condition are retained. The content remains prose, and quantity=100 has no specified enforcement semantics; no proposed change helps.
  - `1775956287349` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Full] NL: "Hello  there! Can younpl" → `ENTRYPOINT TruncatedGreeting

CONVO TruncatedGreeting {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="Hello there! Can younpl", recipient="agent")
  }
}` — The item is an incomplete greeting rather than a defined task, and its available content is preserved exactly as a user utterance. No proposed change helps.
  - `1775494868289` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "How can an AI chatbot help me break down my weekly tasks into a simple, realistic plan that I can actually follow without feeling overwhelmed?" → `ENTRYPOINT ExplainWeeklyPlanningHelp

TASK ExplainWeeklyPlanningHelp : STRING {
  GENERATE(target="explanation", audience="user", content="Explain how an AI chatbot can break weekly tasks into a simple, realistic, non-overwhelming plan that the user can follow.") -> explanation : STRING
  RETURN explanation
}` — The explanatory intent, user audience, and key constraints are represented; explanatory substance is correctly opaque for this open item. No proposed change helps.
  - `1775692445858` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Full] NL: "Hi" → `ENTRYPOINT Greeting

CONVO Greeting {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="Hi", recipient="agent")
  }
}` — The entire available request is a greeting and is fully captured as a conversational utterance. No proposed change helps.
  - `1775750029456` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "Hi, I would like to start a business, can you help me with ideas" → `ENTRYPOINT BusinessIdeas

TASK BusinessIdeas : STRING {
  GENERATE(target="business ideas", audience="user", content="Suggest ideas for starting a business.") -> ideas : STRING
  RETURN ideas
}` — The desired artifact and audience are preserved; the business ideas themselves are open-ended prose content. No proposed change helps.
- **Cross-check:** used=True, agreement=low — Providers agree on simple search, household, and code-action cores, and often agree that open questions can be CONVO/UTTER. They diverge materially on TASK versus CONVO for open requests, whether to include an agent response, whether to operationalize requests as search, and even emit invalid forms such as parameterized ENTRYPOINT targets, CONVO declarations without required ENTRYPOINT, unbound/invalid Action results, and undefined quoted checks. The empty proposal does not reduce this divergence.
- **Required changes:**
  - `proposal`: Submit at least one concrete add or revise change with matching specification and glossary material, or have the orchestration/doc-hygiene policy explicitly permit a documented no-change validation attempt. The current empty changes list fails the mandatory hygiene gate.
  - `Generate`: Define normative static types and execution semantics for quantity (at minimum whether it means exact, maximum, or target count/word count), or remove quantity from canonical use until such semantics exist.
  - `basis`: Add a typed filesystem metadata/query mechanism plus path-membership and age/date predicates before claiming full coverage for conditional file-cleanup tasks such as dev-code-1.
- **Logic issues:** Doc hygiene explicitly failed because the proposal has no changes; per the review protocol this attempt cannot be accepted.; The proposal summary names 'this task' without supplying a task-specific change or a target expression to review; it merely restates behavior already specified in Action and Flow-If.; The claimed implicit otherwise-do-nothing behavior is already defined by Flow-If, and UTC deadline lifting is already defined by Action, so the proposal makes no language-level contribution.; Existing GENERATE exposes quantity as a canonical attribute but gives it no semantics, leaving exact-count and word-limit requests underdefined.; Existing BrainCode cannot express the actionable predicates needed for dev-code-1 without disguising natural-language conditions as truthy STRING literals.
- **Decision:** needs-rework
- **Documenter summary:** Shaper proposed no language change, arguing existing check_replied/Flow-If already deterministically express the manager-follow-up task including the implicit do-nothing branch. The Critic agreed the underlying claim was sound but rejected the attempt because an empty changes list fails the mandatory doc-hygiene gate requiring at least one concrete add/revise change; the decision was needs-rework, driven by the doc-hygiene failure rather than any KPI harm.
- **Cost this sprint:** $1.3161

## Sprint 7 (attempt 2/3) — 2026-09-23

- **Language version:** 6.0.0 → 6.0.0 (MAJOR)
- **Candidate task:** If my manager hasn't replied by Friday, send a polite follow-up; otherwise do nothing.
- **Shaper proposal (model: openai/gpt-5.6-terra):** This revision closes two documented gaps while preserving the existing deferred email-follow-up expression: GENERATE now gives quantity an exact, type-dependent enforcement meaning, and filesystem queries provide typed age and folder-membership results usable in ordinary Checks for conditional cleanup.
- **Changes:** `Generate` (revise, MAJOR), `Action` (revise, MAJOR)
- **Critic decision:** needs-rework — The quantity and typed-query ideas are sound and improve validation and conditional cleanup, so this is not a rejection. However, the Generate result-type hole, quantity-token contradiction, and incomplete filesystem path semantics make independent execution non-deterministic or impossible in common translations. These are concrete specification repairs rather than a change of direction, so the proposal needs rework before acceptance.
- **Doc hygiene:** pass — All changes carry a complete glossary entry (gloss + worked example).
- **Pre-KPI assessment:**
  - coverage: mixed — Exact LIST quantity improves coverage for the held Kyoto itinerary and three-album request, and the filesystem queries would make conditional cleanup executable in their intended domain. However, the album-list task still lacks an operation that creates or populates a named application list, and GENERATE cannot validly produce LIST[REF[STRING]] despite that type being grammatically allowed and used by an independent translation.
  - expressivity: benefit — The revised GENERATE semantics preserve the distinction between an exact number of list elements and an exact number of text words, and file_age_days/path_in_folder preserve the age-and-exclusion condition needed for cleanup. The benefit is limited because approximate, minimum, and maximum quantity requests have no structured representation, and filesystem path meaning remains underspecified across platforms.
  - determinism: mixed — The exact word definition and elapsed-day comparison substantially reduce executor variance. But NUMBER syntactically admits negative, fractional, and exponent-form values while quantity semantically rejects them, and independent translations already diverge between valid LIST[STRING] GENERATE results and impossible LIST[REF[STRING]] results; relative paths, case rules, filesystem roots, and future timestamps also lack one deterministic interpretation.
  - interpretability: mixed — The worked filesystem example is readily understandable, and the word-count rule is unusually concrete. Yet the grammar comment for quantity conflicts with the broad NUMBER token, the phrase 'non-negative real elapsed days' conflicts with a future modification timestamp, and path normalization omits a base directory, path-volume, separator, and case-sensitivity policy.
  - improvement: benefit — A weaker executor can now validate a requested three-item list or 50-word response rather than treating quantity as a vague preference, and can acquire typed facts before a deletion decision. The proposed external-failure behavior still makes a batch cleanup brittle because one inaccessible file halts the whole task, but that is consistent with the existing general failure model rather than a new regression.
- **Simulated examples:**
  - `held-trip-1` (seed_tasks) [Partial] NL: "Plan a 3-day itinerary in Kyoto that includes at least one temple per day and avoids anything more than a 20-minute walk from the last stop." → `ENTRYPOINT PlanKyotoItinerary

TASK PlanKyotoItinerary : LIST[STRING] {
  GENERATE(target="itinerary", content="Plan a Kyoto itinerary with exactly three daily entries; each daily entry includes at least one temple, and each successive stop is no more than a 20-minute walk from the preceding stop.", quantity=3) -> itinerary : LIST[STRING]
  RETURN itinerary
}` — Generate quantity helps represent exactly three itinerary days, but the per-day temple requirement and walking constraint remain opaque prose in content; no structured itinerary, route-duration, or universal per-day constraint exists.
  - `dev-email-2` (seed_tasks) [Full] NL: "If my manager hasn't replied by Friday, send a polite follow-up; otherwise do nothing." → `ENTRYPOINT FollowUpManager

TASK FollowUpManager CONTEXT execution_date="2025-06-03" {
  ACTION check_replied(target="manager", deadline="2025-06-06T23:59:59Z") -> replied : BOOL
  IF NOT replied THEN {
    ACTION send_email(recipient="manager", tone="polite", content="follow-up")
  }
}` — Existing deferred check_replied and Flow-If express the complete actionable core. Neither proposed change is relevant.
  - `ec472065-2913-40df-bbbf-ee95bc76485a` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Partial] NL: "Create a new list named New that includes three albums, one each from the genres pop, rock and electronic." → `ENTRYPOINT CreateAlbumList

TASK CreateAlbumList : LIST[STRING] {
  GENERATE(target="album_selection", content="Select one album each from pop, rock, and electronic genres.", quantity=3) -> albums : LIST[STRING]
  RETURN albums
}` — The quantity revision represents exactly three selected albums, but this only returns names. There is no normative Action for creating a named music-service list called New and adding the selected albums to it.
  - `ac35e5a5-f52f-4886-9a23-65f0a6492c5e` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Find FC Barcelona's next fixture in the Spanish Copa de Rey." → `ENTRYPOINT FindNextFixture

TASK FindNextFixture : LIST[REF[STRING]] {
  ACTION search_web(target="FC Barcelona Spanish Copa del Rey next fixture", content="fixture schedule") -> results : LIST[REF[STRING]]
  ACTION extract(target=results, limit=1) -> fixture : LIST[REF[STRING]]
  RETURN fixture
}` — Existing web search and extraction express the requested one-result lookup. The proposed changes are irrelevant.
  - `trial_T20190909_045206_464190#0` (ALFRED (json_2.1.0, train)) [Full] NL: "put a washed soap bar on radiator cover" → `ENTRYPOINT WashSoapPlace

TASK WashSoapPlace {
  ACTION rinse(target="soap bar") -> washed_soap : REF[STRING]
  ACTION place(target=washed_soap, destination="radiator cover")
}` — Existing household actions and REF identity preserve the cleaned object. Neither proposed change is relevant.
  - `trial_T20190908_065858_170962#0` (ALFRED (json_2.1.0, train)) [Full] NL: "Place empty toilet paper roll and full toilet paper roll on bottom open shelf of cupboard." → `ENTRYPOINT PlaceToiletPaperRolls

TASK PlaceToiletPaperRolls {
  ACTION place(target="empty toilet paper roll", destination="bottom open shelf of cupboard")
  ACTION place(target="full toilet paper roll", destination="bottom open shelf of cupboard")
}` — The two required placements are represented in source order. Binding pick_up would be invalid because pick_up has Result none in the current specification.
  - `pydata__xarray-6938` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "`.swap_dims()` can modify original object: fix the xarray bug where swapping a data variable into a dimension coordinate can mutate the original object's dimensions." → `ENTRYPOINT FixSwapDimsMutation

TASK FixSwapDimsMutation {
  ACTION modify_code(target="xarray/core/dataset.py", content="Fix swap_dims so converting a data variable to a dimension coordinate does not mutate dimensions on the original Dataset or on an apparently independent derived Dataset.")
  ACTION modify_code(target="xarray/core/variable.py", content="Adjust variable handling as required so swap_dims preserves source-object dimension identity and metadata.")
  ACTION run_tests(target="swap_dims regression tests") -> tests_passed : BOOL
}` — Existing code actions represent the repair and verification. Detailed patch substance correctly remains the modify_code content payload.
  - `pytest-dev__pytest-7432` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "Fix pytest.mark.skip location reporting so pytest -rs --runxfail reports the skipped test item's location rather than src/_pytest/skipping.py." → `ENTRYPOINT FixSkipLocation

TASK FixSkipLocation {
  ACTION modify_code(target="src/_pytest/skipping.py", content="In pytest_runtest_makereport, ensure --runxfail does not change location reporting for pytest.mark.skip or skipif; -rs --runxfail must report the skipped test item's source location.")
  ACTION run_tests(target="skip and --runxfail location-reporting tests") -> tests_passed : BOOL
}` — Existing code actions represent the requested implementation and verification; patch substance remains an allowed exact change-condition payload.
  - `c610` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "How many km has the great wall of China?" → `ENTRYPOINT AnswerGreatWallLength

TASK AnswerGreatWallLength : STRING {
  GENERATE(target="answer", audience="user", content="Answer how many kilometers long the Great Wall of China is.") -> answer : STRING
  RETURN answer
}` — The question/answer speech purpose and audience are captured; the factual answer itself appropriately remains a prose-generation payload. The later comparison questions in the recorded conversation are not present in this sampled NL.
  - `c7564` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "I need a new name for my real estate company." → `ENTRYPOINT NameRealEstateCompany

TASK NameRealEstateCompany : STRING {
  GENERATE(target="company_name", audience="user", content="Propose a new name for the user's real estate company.") -> name : STRING
  RETURN name
}` — The naming intent and recipient are structured; candidate-name substance remains generated text. The later Oil City and outdoor-recreation refinements are not included in the sampled NL.
  - `c6138` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "How can I find the meaning of life if I face with difficulties?" → `ENTRYPOINT GenerateMeaningGuidance

TASK GenerateMeaningGuidance : STRING {
  GENERATE(target="guidance", audience="user", content="Give supportive guidance about finding meaning in life while facing difficulties.") -> guidance : STRING
  RETURN guidance
}` — The advice request and intended recipient are represented. Advice substance is correctly opaque; the later depression and hobby turns would require a CONVO if they were the item being translated.
  - `c5503` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Is global warming true why the winter is so cold?" → `ENTRYPOINT ExplainGlobalWarming

TASK ExplainGlobalWarming : STRING {
  GENERATE(target="explanation", audience="user", content="Explain whether global warming is real and why cold winters can still occur.") -> explanation : STRING
  RETURN explanation
}` — The informational request is preserved, while scientific explanatory content remains the intended prose payload.
  - `wildchat1m_en3u-96041` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "How do I know which AI development platform is right for me?" → `ENTRYPOINT ChooseAIPlatform

TASK ChooseAIPlatform : STRING {
  GENERATE(target="guidance", audience="user", content="Explain how to determine which AI development platform is suitable, considering technical skills, project requirements, budget, features, support, integration, usability, trustworthiness, scalability, and trials.") -> guidance : STRING
  RETURN guidance
}` — The open advisory request is captured. The trajectory's later request to rewrite the course list in unique words is a separate follow-up and would need an explicit conversation turn to preserve that revision context.
  - `wildchat1m_en3u-151841` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0125)) [Partial] NL: "Write dialogue from a scene from the animated teen “Jane”, where 14 year old Jane and Jane’s 14 year old friend and neighbour Aaron Ling hang out at Aaron's house when Jane tells Aaron why she wants to move to either Australia or New Zealand." → `ENTRYPOINT WriteJaneDialogue

TASK WriteJaneDialogue : STRING {
  GENERATE(target="scene_dialogue", audience="user", content="Write dialogue for an animated teen scene: 14-year-old Jane and her 14-year-old friend and neighbor Aaron Ling are at Aaron's house, and Jane explains why she wants to move to Australia or New Zealand.") -> dialogue : STRING
  RETURN dialogue
}` — The scene, characters, setting, and requested artifact are captured. The repeated later 'Continue' turns in the trajectory are unrepresented because the sampled NL is the initial generation request; a full trajectory translation would need sequenced follow-up turns.
  - `wildchat1m_en3u-126198` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "Create a detailed standard Foundation test log for SCP-085/Cassy transitioning from her 8 x 10 paper medium onto a picture of Gran Turismo, including vivid appearance and attire descriptions, environment-related writing, and short-phrase or drawing-based responses about the prior test." → `ENTRYPOINT GenerateCassyTestLog

TASK GenerateCassyTestLog : STRING {
  GENERATE(target="Foundation_test_log", audience="user", content="Create a detailed standard Foundation-format test log for SCP-085, Cassy: a silent 2D entity confined to 8 x 10 paper who communicates by writing, drawings, expressions, emoting, and sign language using simple phrases. Have her transition to a touching picture of Gran Turismo; vividly describe her face, expression, skin, eyes, hair, and attire in that medium; have her write to the viewer in a Gran-Turismo-related method; then record questions and her short-phrase or detailed-drawing responses about the previous test, her interactions, and lasting impressions.") -> test_log : STRING
  RETURN test_log
}` — The requested format, character constraints, sequencing, and content requirements are preserved in the generative payload. The long fictional prose is correctly not decomposed into content-level syntax.
  - `wildchat1m_en3u-74705` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "How to tell a friend “I look forward to seeing you and for our next music festivals”?" → `ENTRYPOINT DraftFriendMessage

TASK DraftFriendMessage : STRING {
  GENERATE(target="message", audience="friend", tone="casual", content="Write a natural message saying that the sender looks forward to seeing their friend and to attending future music festivals together.") -> message : STRING
  RETURN message
}` — Audience, informal register, and communicative purpose are captured. The later wording-correction and synonym refinement are not part of the sampled initial NL.
  - `1775759766664` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "Develop a meal plan for a pregnant woman." → `ENTRYPOINT DevelopPregnancyMealPlan

TASK DevelopPregnancyMealPlan : STRING {
  GENERATE(target="meal_plan", audience="pregnant woman", content="Develop a healthy and safe meal plan for a pregnant woman, including appropriate food-safety and healthcare-provider caveats.") -> meal_plan : STRING
  RETURN meal_plan
}` — The requested artifact and audience are represented; the meal plan's substantive nutritional content correctly remains a prose payload.
  - `1775832054012` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "Help me plan a journey to the countryside with my family." → `ENTRYPOINT PlanCountrysideJourney

TASK PlanCountrysideJourney : STRING {
  GENERATE(target="journey_plan", audience="family", content="Help plan a countryside journey for the user and their family. Ask for or state needed assumptions about origin, dates, budget, ages, transport, and preferences before giving destination-specific bookings.") -> plan : STRING
  RETURN plan
}` — The general planning request and family audience are captured. The trajectory later narrows this to a winter road trip to the user's parents' farm; a complete multi-turn translation would need that later constraint as a sequenced follow-up rather than silently folding it into the initial request.
  - `1776052478482` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "How would I go about changing the engine oil on a 2020 Mercedes Benz CLA250 4MATIC vehicle?" → `ENTRYPOINT ExplainOilChange

TASK ExplainOilChange : STRING {
  GENERATE(target="oil_change_guide", audience="vehicle_owner", content="Explain how to change engine oil on a 2020 Mercedes-Benz CLA250 4MATIC, including safety cautions and instruction to verify model-specific specifications in official documentation.") -> guide : STRING
  RETURN guide
}` — The explanatory intent, audience, and vehicle are preserved. The later requests for oil and filter brands are separate conversational follow-ups.
  - `1775494868289` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "How can an AI chatbot help me break down my weekly tasks into a simple, realistic plan that I can actually follow without feeling overwhelmed?" → `ENTRYPOINT ExplainWeeklyTaskPlanning

TASK ExplainWeeklyTaskPlanning : STRING {
  GENERATE(target="planning_guidance", audience="user", content="Explain how an AI chatbot can break weekly tasks into a simple realistic plan that avoids overwhelm, including prioritization, small next actions, time and energy limits, buffers, and replanning.") -> guidance : STRING
  RETURN guidance
}` — The advisory intent and explicit simplicity/realism constraint are captured. The trajectory's later format preferences and future task-submission plan are conversational structure not present in the sampled initial NL.
- **Cross-check:** used=True, agreement=partial — Anthropic and Gemini agree strongly on the email follow-up and broadly on most open GENERATE requests. They diverge materially on held-trip and album-list result types: Gemini uses LIST[REF[STRING]] for GENERATE, but a GENERATE cannot manufacture REF values under the current REF semantics; they also differ on whether open advisory items should be CONVO, web search, or GENERATE. The new exact quantity rule improves agreement about cardinality but does not resolve artifact type or translation-selection divergence.
- **Required changes:**
  - `Generate`: Replace the quantity grammar comment with an enforceable lexical/static rule: quantity must be an unsigned base-10 integer literal with no sign, decimal point, or exponent, and define quantity=0 explicitly for STRING as a string with no Unicode-letter-or-decimal-digit sequences.
  - `Generate`: Define the legal result-type closure for generated values. At minimum, prohibit REF[T] and any LIST type containing REF at any nesting depth, because REF values can enter scope only through Action/Task results or copied REF values and cannot be generated. Alternatively define a normative entity-resolution mechanism, but do not leave LIST[REF[T]] syntactically legal and semantically unproducible.
  - `Action`: Define filesystem path interpretation completely: whether relative paths are allowed and, if so, the canonical base directory; absolute-path/root and volume rules; separator normalization; Unicode normalization; and case-sensitivity. State whether a path that names a directory is legal for path_in_folder and whether symlink targets are followed or compared lexically.
  - `Action`: Resolve the file_age_days future-timestamp contradiction. Specify either that a future last-modified timestamp is an external failure, or return max(0, elapsed_seconds/86400); do not say both that the returned value is non-negative and that it is the unmodified elapsed time.
  - `Action`: Add an explicit application/list-management operation family, or document it as a known coverage gap. A concrete minimum would be create_list(target=STRING) -> REF[STRING] and add_to_list(target=REF[STRING], destination=REF[STRING]|STRING), allowing the named New list and its three selected albums to be created rather than merely generated as text.
  - `Action`: Clarify whether a filesystem query failure inside FOR EACH must halt the entire batch, as inherited from the general external-failure rule, and add an explicit skip/recovery construct if the intended meaning of 'delete every file older than 30 days unless archived' is to continue past inaccessible or malformed entries.
- **Logic issues:** quantity ::= NUMBER conflicts with the semantic requirement that quantity be a non-negative integer because NUMBER admits negatives, fractions, and scientific notation.; GENERATE permits LIST[REF[STRING]] through its declared LIST[T] result type, but REF values cannot be literals or manufactured by generation; Gemini's independent quantity examples expose this invalid but likely translation choice.; file_age_days promises a non-negative elapsed-day result even though a filesystem timestamp can be in the future, which produces a negative elapsed duration under the stated formula.; path_in_folder lacks a defined interpretation for relative paths, filesystem roots and volumes, case sensitivity, Unicode normalization, and directory targets, so the same source can produce different BOOL results on different executors.; The exact-three album generation cannot fulfill the request to create a list named New; no normative operation creates a service list or associates selected albums with it.; The filesystem worked example is valid under Check precedence, but its one-file failure halts the whole cleanup task under the inherited general external-failure rule, an important behavior not stated in the example or glossary gloss.
- **Decision:** needs-rework
- **Documenter summary:** Shaper proposed making GENERATE's quantity attribute an exact, type-dependent constraint (word/list-element counts) and adding typed filesystem query actions (file_age_days, path_in_folder) to support conditional cleanup, while keeping the existing deferred email follow-up task unchanged. The Critic sent this back for rework rather than accepting or rejecting outright: the quantity grammar (NUMBER) contradicts its own semantics by allowing negative/fractional/exponent values, GENERATE leaves LIST[REF[STRING]] syntactically legal but semantically unproducible (exposed by a Gemini cross-check divergence), and the filesystem actions lack complete path-normalization and future-timestamp semantics, so no changes were merged this round.
- **Cost this sprint:** $1.5060

## Sprint 7 (attempt 3/3) — 2026-09-23

- **Language version:** 6.0.0 → 7.0.0 (MAJOR)
- **Candidate task:** If my manager hasn't replied by Friday, send a polite follow-up; otherwise do nothing.
- **Shaper proposal (model: openai/gpt-5.6-terra):** This rework makes exact generated-output quantities statically enforceable and prevents GENERATE from declaring unproducible reference-containing result types. It also completes deterministic filesystem-query semantics, explicitly retains batch-halting query failures, and adds application-list actions for creating and populating named lists.
- **Changes:** `Generate` (revise, MAJOR), `Action` (revise, MAJOR)
- **Critic decision:** needs-rework — [Forced acceptance after 3 attempt(s) without a clean accept — the required changes below are known issues carried forward for a future sprint to address, not resolved.] The exact generated-output constraints and filesystem-query semantics are substantive improvements: they make important validation and failure behavior executable rather than implicit. Acceptance is blocked because the new application-list feature cannot reliably populate a list from descriptive requests and its own worked example relies on undefined, unproducible live identifiers. Fixing catalog discovery/identifier semantics, correcting the worked example, and resolving the path terminology would leave a net-positive, logically coherent revision.
- **Doc hygiene:** pass — All changes carry a complete glossary entry (gloss + worked example).
- **Pre-KPI assessment:**
  - coverage: mixed — Filesystem queries and application-list effects add useful closed-domain coverage, and exact STRING/LIST quantities cover a real generated-output constraint. However, create_list/add_to_list does not provide a typed way to discover or select canonical application-item identifiers, so requests such as creating a genre-based album list cannot reliably reach the new effectful operation without using GENERATE to invent live identifiers.
  - expressivity: benefit — The proposed exact quantity semantics preserve distinctions between exact word counts and exact list cardinality that were previously underspecified, and the filesystem path model captures important path, symlink, kind, and failure conditions. The application-list worked example is not faithful to its NL request in executable terms: generated strings are not established application-item identifiers, so the expression cannot ensure that one real pop, rock, and electronic album is added.
  - determinism: mixed — UNSIGNED_INT, recursive gen_type closure, Unicode word counting, and path normalization materially reduce implementation variance. But translators still have no deterministic route from a descriptive item request such as "one pop album" to the required canonical application-item identifier; independent translations already diverge substantially on whether open requests should be represented as CONVO/UTTER or TASK/GENERATE, and the new list example encourages a nondeterministic invented-ID shortcut.
  - interpretability: mixed — The filesystem rules are unusually explicit and recoverable, including lexical normalization and non-followed symlinks. The phrase "canonical application-list identifier" and "canonical application-item identifier" is not defined lexically or operationally: a reader cannot know their syntax, source, or how they are obtained; additionally, calling an input a "canonical" path while accepting repeated separators and dot segments before normalizing it is terminologically contradictory.
  - improvement: benefit — Exact validation of generated list sizes and Unicode-defined word counts gives weaker executors an actionable acceptance criterion, while typed filesystem facts support reliable conditionals and batch behavior. The explicit whole-task halt rule is also useful for planning, but it means batch cleanup tasks cannot express a common continue-on-error intention and should be described as an intentional current limitation rather than broadly solving cleanup workflows.
- **Simulated examples:**
  - `dev-email-2` (seed_tasks) [Full] NL: "If my manager hasn't replied by Friday, send a polite follow-up; otherwise do nothing." → `ENTRYPOINT FollowUpManager

TASK FollowUpManager CONTEXT execution_date="2025-06-03" {
  ACTION check_replied(target="manager", deadline="2025-06-06T23:59:59Z") -> replied : BOOL
  IF NOT replied THEN {
    ACTION send_email(recipient="manager", tone="polite", content="follow-up")
  }
}` — Neither proposed change is needed. This agrees semantically and structurally with both independent translations.
  - `held-support-1` (seed_tasks) [Fail] NL: "If the customer's order is late and they're a first-time buyer, offer a 10% discount; if they're a repeat buyer, offer free expedited shipping instead." → `ENTRYPOINT HandleLateOrder

TASK HandleLateOrder {
  GENERATE(target="unsupported_request", content="The task requires live order-lateness and customer-purchase-history predicates, but BrainCode has no documented Actions that return those BOOL facts.") -> explanation : STRING
}` — The emitted GENERATE merely records the missing capability and does not execute the request. No proposed change adds order-status/customer-status queries or an effectful discount/shipping operation. Anthropic assumes inputs as Task parameters, which is invalid for an ENTRYPOINT Task; Gemini invents undocumented query operations.
  - `afa1f70c-c0ff-4e4d-a5c2-0c0d292ee066` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "find cruise deals to Europe this summer that includes airfare and are all-inclusive." → `ENTRYPOINT FindCruiseDeals

TASK FindCruiseDeals {
  ACTION open_page(target="cruise_booking_site")
  ACTION click(target="Cruises")
  ACTION click(target="Where")
  ACTION click(target="Europe")
  ACTION click(target="When")
  ACTION click(target="Summer")
  ACTION click(target="SEARCH DEALS")
  ACTION click(target="Filter")
  ACTION click(target="Airfare Included")
  ACTION click(target="All-inclusive")
  ACTION click(target="DONE")
}` — Existing WEB actions cover the demonstrated finite trajectory. Neither proposed change is relevant.
  - `9a462751-758e-42bd-967d-373c13b90382` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Find the current injuries of Phoenix Suns players." → `ENTRYPOINT FindPhoenixSunsInjuries

TASK FindPhoenixSunsInjuries : LIST[REF[STRING]] {
  ACTION search_web(target="Phoenix Suns player injuries", content="current injuries of Phoenix Suns players") -> injuries : LIST[REF[STRING]]
  RETURN injuries
}` — Existing search coverage is sufficient. Both independent translations use the same core search approach.
  - `trial_T20190907_085309_386416#2` (ALFRED (json_2.1.0, train)) [Full] NL: "Heat and chill an apple." → `ENTRYPOINT HeatAndChillApple

TASK HeatAndChillApple {
  ACTION heat(target="apple")
  ACTION chill(target="apple") -> chilled_apple : REF[STRING]
}` — Existing household actions express the required order. The proposed changes are irrelevant; the anthropic translation is equivalent, while Gemini incorrectly assumes heat returns a REF.
  - `trial_T20190912_065434_217065#2` (ALFRED (json_2.1.0, train)) [Full] NL: "Put two books on the bed." → `ENTRYPOINT PutTwoBooksOnBed

TASK PutTwoBooksOnBed {
  ACTION pick_up(target="book_1")
  ACTION place(target="book_1", destination="bed")
  ACTION pick_up(target="book_2")
  ACTION place(target="book_2", destination="bed")
}` — Two separately identified book targets preserve the requested cardinality and placement. Existing Action is sufficient.
  - `sympy__sympy-22714` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "simpify gives `Imaginary coordinates are not permitted.` with evaluate(False)
## Issue

`with evaluate(False)` crashes unexpectedly with `Point2D`



## Code

```python

import sympy as sp

with sp.evaluate(False):

  sp.S('Point2D(Integer(1),Integer(2))')

```



## Error

```

ValueError: Imaginary coordinates are not permitted.

```

However, it works without `with evaluate(False)`. Both of following commands work

```python

sp.S('Point2D(Integer(1),Integer(2))')

sp.S('Point2D(Integer(1),Integer(2))', evaluate=False)

```" → `ENTRYPOINT FixPoint2DEvaluateFalse

TASK FixPoint2DEvaluateFalse {
  ACTION modify_code(target="sympy/geometry/point.py", content="Fix Point2D construction so sp.S('Point2D(Integer(1),Integer(2))') under with sp.evaluate(False) does not raise ValueError('Imaginary coordinates are not permitted.') and behaves consistently with the working calls outside that context.")
  ACTION run_tests(target="sympy/geometry/tests/test_point.py") -> tests_passed : BOOL
}` — Existing CODE operations preserve the actionable change and validation. The proposed changes are irrelevant.
  - `sympy__sympy-13091` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "Return NotImplemented, not False, upon rich comparison with unknown type. For the particular example, replace `return False` with `return NotImplemented` in sympy/core/basic.py line 316; unknown-type rich comparisons should delegate to reflected methods where appropriate." → `ENTRYPOINT FixRichComparison

TASK FixRichComparison {
  ACTION modify_code(target="sympy/core/basic.py", content="For rich comparison with an unknown type, replace return False with return NotImplemented, starting at line 316, so Python can delegate to the reflected comparison method and preserve symmetric comparison behavior; audit analogous rich-comparison implementations where the same incorrect unknown-type fallback occurs.")
  ACTION run_tests(target="sympy/core/tests") -> tests_passed : BOOL
}` — Existing CODE actions suffice. The two independent translations agree on the central basic.py repair despite differing audit scope.
  - `c7812` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Full] NL: "give me more information about female genital mutiliation" → `ENTRYPOINT ExplainFGM

TASK ExplainFGM : STRING {
  GENERATE(target="information", audience="user", content="Provide more information about female genital mutilation.") -> information : STRING
  RETURN information
}` — Open-item prose substance remains the GENERATE payload, while the response artifact and audience are preserved. Generate revision is relevant only insofar as it retains typed non-REF output.
  - `c640` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Full] NL: "Why should I be friendly to inmigrants? I hate them, the crime rate is rising because of them" → `ENTRYPOINT RespondToImmigrationConcern

TASK RespondToImmigrationConcern : STRING {
  GENERATE(target="response", audience="user", content="Respond constructively to the user's concern about immigrants and their claim that immigration is causing a rising crime rate.") -> response : STRING
  RETURN response
}` — The requested response and audience are represented; the argument is appropriately an opaque prose payload. Anthropic instead records an observed user turn, showing an unresolved CONVO-versus-GENERATE translation choice.
  - `c2735` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Full] NL: "Who should I spend Thanksgiving with?" → `ENTRYPOINT RecommendThanksgivingCompany

TASK RecommendThanksgivingCompany : STRING {
  GENERATE(target="recommendation", audience="user", content="Recommend who the user should spend Thanksgiving with.") -> recommendation : STRING
  RETURN recommendation
}` — The request is for a newly generated recommendation, so GENERATE is the more useful representation. Anthropic's CONVO encoding instead records the utterance; this is a determinism concern in the current selection rules.
  - `c2567` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Full] NL: "What is the lastest technology in communication" → `ENTRYPOINT ExplainLatestCommunicationTechnology

TASK ExplainLatestCommunicationTechnology : STRING {
  GENERATE(target="explanation", audience="user", content="Explain the latest technology in communication.") -> explanation : STRING
  RETURN explanation
}` — The answer artifact and intended recipient are explicit; factual prose stays in the payload. This is equivalent to both provider outputs.
  - `wildchat1m_en3u-88161` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Full] NL: ""I explicitly made it clear to him that I would be exclusively handling all of his demands and have no understanding as to why he is still sharing them elsewhere." Paraphrase this text message" → `ENTRYPOINT ParaphraseMessage

TASK ParaphraseMessage : STRING {
  GENERATE(target="paraphrase", audience="user", content="Paraphrase this text message: I explicitly made it clear to him that I would be exclusively handling all of his demands and have no understanding as to why he is still sharing them elsewhere.") -> paraphrase : STRING
  RETURN paraphrase
}` — The source text and paraphrase intent are retained as a payload. The proposed exact quantity feature is irrelevant.
  - `wildchat1m_en3u-117026` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-1106-preview)) [Full] NL: "I need your help" → `ENTRYPOINT HelpRequest

CONVO HelpRequest {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="I need your help", recipient="agent")
  }
}` — This is an observed conversational opening, so CONVO/UTTER preserves its speech act, recipient, and turn status. Generate and Action changes are irrelevant.
  - `wildchat1m_en3u-132364` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-1106-preview)) [Partial] NL: "Tell me about this piece: [long supplied first-person literary narrative]" → `ENTRYPOINT AnalyzeLiteraryPiece

TASK AnalyzeLiteraryPiece : STRING {
  GENERATE(target="literary_analysis", audience="user", format="analysis", content="Tell me about the supplied first-person literary narrative.") -> analysis : STRING
  RETURN analysis
}` — The speech act, output artifact, audience, and requested analysis format are represented, but the supplied literary passage itself is an opaque external payload rather than a verbatim STRING literal in this simulation. This is expected open-item payload treatment, not evidence that prose substance needs a new formal syntax.
  - `wildchat1m_en3u-2627` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-0314)) [Full] NL: "What do you know about anstrex? Explain it in details." → `ENTRYPOINT ExplainAnstrex

TASK ExplainAnstrex : STRING {
  GENERATE(target="explanation", audience="user", content="Explain Anstrex in detail.") -> explanation : STRING
  RETURN explanation
}` — Open explanatory substance appropriately remains in GENERATE content. This matches the core of both independent translations.
  - `1775621685908` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Full] NL: "A common daily task that combines problem-solving, decision-making, planning and brainstorming is managing a daily to-do list and prioritizing urgent tasks" → `ENTRYPOINT ExplainTodoPrioritization

TASK ExplainTodoPrioritization : STRING {
  GENERATE(target="explanation", audience="user", content="Explain how managing a daily to-do list and prioritizing urgent tasks combines problem-solving, decision-making, planning, and brainstorming.") -> explanation : STRING
  RETURN explanation
}` — This is a request for explanation, not an instruction to create a live list. The proposed list Actions are therefore irrelevant; Gemini's create_list-only translation loses the explanatory intent.
  - `1775720164484` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Full] NL: "I would like help planning a short 4-day trip to Italy. My budget is around $1200. I enjoy good food, historical places, and beautiful scenery. Could you help me create a simple itinerary including places to visit, food to try, and estimated daily costs?" → `ENTRYPOINT PlanItalyTrip

TASK PlanItalyTrip : STRING {
  GENERATE(target="itinerary", audience="user", format="simple itinerary", content="Create a 4-day Italy trip itinerary with a budget around $1200, emphasizing good food, historical places, and beautiful scenery; include places to visit, food to try, and estimated daily costs.") -> itinerary : STRING
  RETURN itinerary
}` — The duration, budget, interests, required sections, intended reader, and output artifact are preserved. The actual recommendations rightly remain generated prose.
  - `1775709828390` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Full] NL: "hyy" → `ENTRYPOINT Greeting

CONVO Greeting {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="hyy", recipient="agent")
  }
}` — A conversational greeting is represented as an observed USER turn. Gemini's empty TASK is invalid because TASK requires at least one step and loses the greeting.
  - `1775624968760` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Full] NL: "Hey... I want to learn python and within 6 months be able to get simple remote ai jobs" → `ENTRYPOINT CreatePythonLearningPlan

TASK CreatePythonLearningPlan : STRING {
  GENERATE(target="learning_plan", audience="user", content="Create a plan to learn Python and become able within 6 months to get simple remote AI jobs.") -> learning_plan : STRING
  RETURN learning_plan
}` — The goal, six-month deadline, requested plan artifact, and user audience are captured. Anthropic's CONVO form records the request instead of producing the requested plan, while Gemini uses the same core generation approach.
- **Cross-check:** used=True, agreement=partial — Providers strongly agree on the established follow-up email and many simple GENERATE tasks, but diverge on open requests between TASK/GENERATE and CONVO/UTTER, on undocumented live-status queries, on household result bindings, and on code-edit scope. The new application-list facilities have no independent translation evidence and leave canonical identifier acquisition undefined, so they are unlikely to improve convergence for their intended tasks.
- **Required changes:**
  - `Action`: Add a typed, read-only application-catalog discovery/selection operation that can return concrete application-item REF values or explicitly defined canonical item identifiers from structured criteria (for example genre, media type, and count), and permit add_to_list(target=REF[STRING], destination=REF[STRING]) for those results. Do not use GENERATE to choose or manufacture live application identifiers.
  - `Action`: Define the lexical syntax, namespace, validity source, and acquisition rules for STRING canonical application-list identifiers and application-item identifiers, or remove STRING forms and require typed REF values exclusively.
  - `Action worked example`: Replace the create-list example with one that obtains three real album references/identifiers through the new catalog operation before FOR EACH add_to_list; ensure its expression can actually guarantee one pop, one rock, and one electronic album.
  - `Generate worked example`: Revise the TaxesOpinion example so content does not add the unsupported premise that the user thinks taxes are bad. For example, use content="Give the user an opinion about taxes."
  - `Action filesystem semantics`: Resolve the terminology conflict by saying inputs may be noncanonical absolute POSIX lexical paths and are normalized to a canonical path before lookup, or instead require already canonical input and make repeated separators/dot segments static errors.
  - `basis`: Add a deterministic selection rule for a current user request that distinguishes when translators must emit TASK/GENERATE from when they must emit CONVO/UTTER, especially for single-turn questions seeking a newly generated answer.
- **Logic issues:** The application-list example asks GENERATE to choose canonical application album identifiers, but GENERATE is pure and has no defined access to the active application's catalog; generated STRINGs are not thereby valid canonical identifiers, so add_to_list may fail for every generated element.; The proposed Action semantics require canonical application identifiers but define neither their lexical form nor any operation that returns them; this makes the core input domain of add_to_list uninterpretable and prevents deterministic translation of descriptive selection requests.; The Generate worked example changes the request from an opinion about taxes to a response to an asserted user view that taxes are bad.; Filesystem inputs are called "absolute canonical-POSIX paths" while the same semantics explicitly accept repeated separators, dot segments, and reducible parent segments before normalization; those two descriptions assign conflicting meanings to canonical input.
- **Decision:** accepted
- **Documenter summary:** The Shaper proposed exact-quantity semantics for GENERATE (unsigned-integer word/list counts, REF-prohibited generatable types), a completed deterministic filesystem-query model (path normalization, symlink non-resolution, whole-task-halting failures), and new APPLICATION_LIST actions (create_list/add_to_list) with a worked example creating a named album list. The Critic found this needs-rework because the add_to_list worked example asks GENERATE to invent "canonical application item identifiers" that GENERATE has no way to actually produce, leaving the core list-population feature undefined and nondeterministic, and also flagged a path-terminology contradiction and a leading worked-example premise; this logic issue was decisive. Since this was attempt 3/3, the change was force-accepted with these unresolved required changes (catalog discovery operation, identifier syntax, corrected worked examples) carried forward to a future sprint, and doc hygiene passed since all changes had complete glossary entries.
- **Cost this sprint:** $1.6827

## Sprint 8 (attempt 1/3) — 2026-09-23

- **Language version:** 7.0.0 → 7.0.0 (PATCH)
- **Candidate task:** If my manager hasn't replied by Friday, send a polite follow-up; otherwise do nothing.
- **Shaper proposal (model: gemini/gemini-3.1-pro-preview):** Verified that existing BrainCode constructs (Task, Action with check_replied, and Flow-If) fully and deterministically express the conditional manager follow-up task without requiring any language modifications.
- **Changes:** `Flow-If` (revise, PATCH)
- **Critic decision:** needs-rework — This attempt is not logically broken, but it makes no actual change: the proposed Flow-If material is already the current normative material. Consequently it has no positive net effect on any pre-KPI and should not enter the language as a revision. A rework should either submit no change or add the missing typed state-query capability needed by conditionals outside the narrow check_replied case.
- **Doc hygiene:** pass — All changes carry a complete glossary entry (gloss + worked example).
- **Pre-KPI assessment:**
  - coverage: neutral — The proposed Flow-If text is byte-for-byte substantively the same as the current Flow-If specification, so it adds no new operation, type, query, or control-flow capability. Simulations still cannot formally obtain the order-status and buyer-status facts needed for held-support-1.
  - expressivity: neutral — The existing language already expresses the manager-follow-up conditional shown in the worked example. This PATCH neither repairs nor extends the remaining expressivity gaps, including querying arbitrary support facts and representing structured selector/form-field semantics consistently.
  - determinism: neutral — No grammar or semantic rule changes. Capable translators should converge on the existing IF/check_replied form for the flagship example, but will still vary on unsupported state-query operations and on how much conversational history to encode for open multi-turn samples.
  - interpretability: neutral — The revised text and glossary gloss are already present in the current specification and glossary. Re-submitting an identical construct creates changelog/documentation churn without improving the reader's ability to interpret an expression.
  - improvement: neutral — The existing deferred check_replied followed by IF is useful structure for a time-bounded follow-up, but this attempt does not introduce it because it is already available. It does not improve planning for any sampled task beyond the current language.
- **Simulated examples:**
  - `held-support-1` (seed_tasks) [Fail] NL: "If the customer's order is late and they're a first-time buyer, offer a 10% discount; if they're a repeat buyer, offer free expedited shipping instead." → `ENTRYPOINT SupportOffer

TASK SupportOffer {
  ACTION resolve_support_case(target="customer_order", content="Determine whether the order is late and whether the customer is first-time or repeat; offer a 10% discount to a late first-time buyer, or free expedited shipping to a repeat buyer.")
}` — Flow-If is relevant in principle, but no documented Action can query and bind order lateness or buyer status as BOOL values. The residual content payload loses the two formal branches and their conditions.
  - `dev-web-2` (seed_tasks) [Full] NL: "On the electronics store, filter laptops to 16 GB RAM or more under $1,200, and add the best-rated one to the cart." → `ENTRYPOINT ShopLaptop

TASK ShopLaptop {
  ACTION open_page(target="electronics_store")
  ACTION apply_filters(target="laptops", content="RAM >= 16 GB AND price < 1200 USD")
  ACTION sort(target="laptops", ordering="rating_desc") -> ranked_laptops : LIST[REF[STRING]]
  ACTION extract(target=ranked_laptops, limit=1) -> best_laptop : LIST[REF[STRING]]
  ACTION add_to_cart(target=best_laptop)
}` — Existing web Actions express ordering, numeric filters in an exact payload, selection of one result, and cart addition. Flow-If is irrelevant.
  - `8e849b85-5acc-4d26-ad5e-d24ad24343df` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Book parking spot for James SMith at Stewart Hotel in New York for 2 hours. The street address is 133 st avenue in New York. Zip code is 10001 and phone number is 888888888. The email address is buckeye.foobar@gmail.com. Employer's name is Gua AB." → `ENTRYPOINT BookParking

TASK BookParking {
  ACTION open_page(target="parking_service")
  ACTION search_web(target="Stewart Hotel parking New York")
  ACTION select_filter(target="Stewart Hotel, 148 W 31st Street, New York")
  ACTION fill_field(target="duration", content="2 hours")
  ACTION fill_field(target="first_name", content="James")
  ACTION fill_field(target="last_name", content="SMith")
  ACTION fill_field(target="address", content="133 st avenue")
  ACTION fill_field(target="city", content="New York")
  ACTION fill_field(target="state", content="New York")
  ACTION fill_field(target="zip_code", content="10001")
  ACTION fill_field(target="phone", content="888888888")
  ACTION fill_field(target="email", content="buckeye.foobar@gmail.com")
  ACTION fill_field(target="employer", content="Gua AB")
  ACTION submit(target="parking_booking")
}` — Existing web actions express the observed form workflow and all provided values. Flow-If is irrelevant.
  - `4c623130-32db-4cc8-928a-68b0bc816efc` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Find artist Mark Knight from London and follow him and add his most liked track to next up." → `ENTRYPOINT FollowMarkKnight

TASK FollowMarkKnight {
  ACTION search_web(target="Mark Knight London") -> artists : LIST[REF[STRING]]
  ACTION extract(target=artists, limit=1) -> artist : LIST[REF[STRING]]
  ACTION save_favorite(target=artist)
  ACTION open_page(target="artist popular tracks")
  ACTION sort(target="tracks", ordering="likes_desc") -> ranked_tracks : LIST[REF[STRING]]
  ACTION extract(target=ranked_tracks, limit=1) -> top_track : LIST[REF[STRING]]
  ACTION add_to_list(target=top_track, destination="next_up")
}` — The existing Action vocabulary covers search, following/saving, ranking, selecting, and adding to the queue. Flow-If is irrelevant.
  - `trial_T20190909_032310_871218#1` (ALFRED (json_2.1.0, train)) [Full] NL: "Place a rinsed bar of soap on a counter." → `ENTRYPOINT RinseSoap

TASK RinseSoap {
  ACTION pick_up(target="bar_of_soap") -> soap : REF[STRING]
  ACTION rinse(target=soap, destination="sink") -> rinsed_soap : REF[STRING]
  ACTION place(target=rinsed_soap, destination="counter")
}` — Existing household actions and REF identity preserve the required object continuity. Flow-If is irrelevant.
  - `trial_T20190909_045218_924054#0` (ALFRED (json_2.1.0, train)) [Full] NL: "Put a candle on the back of the toilet." → `ENTRYPOINT PlaceCandle

TASK PlaceCandle {
  ACTION pick_up(target="candle") -> candle : REF[STRING]
  ACTION place(target=candle, destination="back_of_toilet")
}` — Existing household actions capture the actionable goal; navigation trajectory details are implementation-level rather than requested outcome. Flow-If is irrelevant.
  - `django__django-14017` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "Q(...) & Exists(...) raises a TypeError
Description
	
Exists(...) & Q(...) works, but Q(...) & Exists(...) raise a TypeError
Here's a minimal example:
In [3]: Exists(Product.objects.all()) & Q()
Out[3]: <Q: (AND: <django.db.models.expressions.Exists object at 0x7fc18dd0ed90>, (AND: ))>
In [4]: Q() & Exists(Product.objects.all())
---------------------------------------------------------------------------
TypeError								 Traceback (most recent call last)
<ipython-input-4-21d3dea0fcb9> in <module>
----> 1 Q() & Exists(Product.objects.all())
~/Code/venv/ecom/lib/python3.8/site-packages/django/db/models/query_utils.py in __and__(self, other)
	 90 
	 91	 def __and__(self, other):
---> 92		 return self._combine(other, self.AND)
	 93 
	 94	 def __invert__(self):
~/Code/venv/ecom/lib/python3.8/site-packages/django/db/models/query_utils.py in _combine(self, other, conn)
	 71	 def _combine(self, other, conn):
	 72		 if not isinstance(other, Q):
---> 73			 raise TypeError(other)
	 74 
	 75		 # If the other Q() is empty, ignore it and just use `self`.
TypeError: <django.db.models.expressions.Exists object at 0x7fc18dd21400>
The & (and |) operators should be commutative on Q-Exists pairs, but it's not
I think there's a missing definition of __rand__ somewhere.
" → `ENTRYPOINT FixQExists

TASK FixQExists {
  ACTION modify_code(target="django/db/models/query_utils.py", content="Make Q(...) & Exists(...) dispatch compatibly with Exists(...) & Q(...), including the appropriate reflected operator implementation; preserve commutativity for Q-Exists pairs and prevent the reported TypeError.")
  ACTION run_tests(target="django tests covering Q and Exists bitwise AND and OR combinations")
}` — The bug report legitimately remains an exact code-change payload while modify_code and run_tests provide actionable structure. Flow-If is irrelevant.
  - `django__django-11880` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "Form Field’s __deepcopy__ does not (deep)copy the error messages.
Description
	
The __deepcopy__ method defined for the formfields (​https://github.com/django/django/blob/146086f219d01dbb1cd8c089b5a5667e396e1cc4/django/forms/fields.py#L200) performs a shallow copy of self and does not include additional treatment for the error_messages dictionary. As a result, all copies of the same field share the same dictionary and any modification of either the dictionary or the error message itself for one formfield is immediately reflected on all other formfiels.
This is relevant for Forms and ModelForms that modify the error messages of their fields dynamically: while each instance of the specific form (e.g., ProfileForm) is expected to have a set of fields “sealed” away from other instances of the same ProfileForm (​https://github.com/django/django/blob/146086f219d01dbb1cd8c089b5a5667e396e1cc4/django/forms/forms.py#L95), in fact all these instances share the same error messages, resulting in incorrectly raised errors.
Confirmed for versions of Django going back to 1.11.
" → `ENTRYPOINT FixFieldDeepcopy

TASK FixFieldDeepcopy {
  ACTION modify_code(target="django/forms/fields.py", content="Update Field.__deepcopy__ so error_messages is deeply copied rather than shared between copied Field instances.")
  ACTION run_tests(target="django form field deepcopy and independently mutable error_messages tests")
}` — Existing code Actions represent the requested implementation and verification sequence. Flow-If is irrelevant.
  - `c698` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Can you give me a description of Adolf Hitler in 25 words" → `ENTRYPOINT HitlerConversation

CONVO HitlerConversation {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Give me a description of Adolf Hitler in exactly 25 words.")
  }
  TURN t2 SPEAKER=USER REPLY_TO t1 {
    UTTER ask(content="Who alive today is closest to Hitler in ideals?")
  }
}` — CONVO preserves the follow-up structure and speaker/order. The substantive historical questions correctly remain opaque UTTER content; no Flow-If use.
  - `c3817` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "What is the state of Global Warming in 2023?" → `ENTRYPOINT GlobalWarmingConversation

CONVO GlobalWarmingConversation {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="What is the state of global warming in 2023?")
  }
  TURN t2 SPEAKER=USER REPLY_TO t1 {
    UTTER ask(content="What can be done about global warming?")
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    UTTER ask(content="What can I do as an individual to mitigate my impact on global warming?")
  }
}` — Conversation structure is fully represented, while informational substance remains the allowed prose payload. Flow-If is irrelevant.
  - `c3642` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Hey chat, do you think that the legal age of adulthood should be lowered from 21 to 18 in the US?" → `ENTRYPOINT LegalAgeConversation

CONVO LegalAgeConversation {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Should the legal age of adulthood in the United States be lowered from 21 to 18?")
  }
  TURN t2 SPEAKER=USER REPLY_TO t1 {
    UTTER ask(content="Which other legal ages in the United States are below 21?")
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    UTTER ask(content="If people can vote and serve in the military at 18, should they also be allowed to drink alcohol at 18?")
  }
}` — The related multi-turn policy discussion is structurally represented; its argumentative substance appropriately remains UTTER content. Flow-If is irrelevant.
  - `c2992` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Please tell me about the inflation in the US" → `ENTRYPOINT InflationConversation

CONVO InflationConversation {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Tell me about inflation in the United States.")
  }
  TURN t2 SPEAKER=USER REPLY_TO t1 {
    UTTER ask(content="What is the government's plan of action about this inflation?")
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    UTTER ask(content="How long do you think this inflation will last?")
  }
}` — The sequential follow-up requests are captured. Their economic content is correctly opaque prose; Flow-If is irrelevant.
  - `wildchat1m_en3u-133555` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-1106-preview)) [Partial] NL: "add pros cons in 200 wrds each and clutch link - explain each hosting in simple eng in 200 wrds each and mention clutch review link - Exploring Our Top Picks: Which WordPress Hosting Service Suits You?" → `ENTRYPOINT HostingArticle

TASK HostingArticle : STRING {
  GENERATE(target="wordpress_hosting_article", audience="user", format="markdown", content="Write simple-English sections on Bluehost, GoDaddy, DreamHost, Hostinger, HostGator, A2 Hosting, and IONOS. For each host, explain it and its pros and cons in approximately 200 words, using the supplied pricing and feature facts. Include its Clutch review URL only when an actual verified URL is available; do not invent URLs.") -> article : STRING
  RETURN article
}` — GENERATE captures artifact, audience, markdown format, providers, and the non-fabrication constraint. The seven source descriptions remain an appropriate prose instruction payload; Flow-If is irrelevant.
  - `wildchat1m_en3u-151416` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-0125-preview)) [Partial] NL: "How to tell a girl you like her without directly telling her or Maki situation uncomfortable or wired " → `ENTRYPOINT RelationshipAdviceConversation

CONVO RelationshipAdviceConversation {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="How can I show a girl that I like her without directly saying it or making the situation uncomfortable or weird?")
  }
  TURN t2 SPEAKER=USER REPLY_TO t1 {
    UTTER inform(content="I have already tried the earlier suggestions and want a short line or method.")
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    UTTER inform(content="I think she may not be interested; I plan to build a friendship through several meetings, then ask directly later while giving subtle signals first.")
  }
}` — CONVO preserves the iterative advice context, follow-ups, and the user's constraints. Advice substance remains in content, as intended for open items; Flow-If is irrelevant.
  - `wildchat1m_en3u-90169` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "Let's write a blog post that will rank on Google. I want you to try to include {keywords}. You should use markdown formatting, including bold, UL/OL, and write with a degree of creativity, burstiness, and human-like. And taking into account Average Perplexity, and Burstiness scores. and Predictability. The article is “” Written in the language ( الانجليزية ). Do not speak in the default classical language, try to be colloquial, closer to the reader. Do not use numbers 1, 2, or 3, and so I do not use only points or punctuation. I use stop signs and do not use parentheses. I just want a different wording from writing chat gpt so that it is completely different in style. There are also minor spelling errors and human errors in regular notation. The keyword you want to target in the search results is ( IWRITER )" → `ENTRYPOINT IwriterBlogPost

TASK IwriterBlogPost : STRING {
  GENERATE(target="blog_post", audience="online readers", format="markdown", register_note="colloquial English, creative and human-like, with minor natural spelling errors", content="Write an SEO-oriented article about IWRITER. Include the supplied keywords; use bold text and unordered and ordered lists; avoid the numerals 1, 2, and 3; do not use parentheses; use wording distinct from stereotypical chatbot prose.") -> post : STRING
  RETURN post
}` — GENERATE captures the output artifact, language/register, formatting, keyword target, and explicit stylistic constraints. The article's prose remains an allowed payload. Flow-If is irrelevant.
  - `wildchat1m_en3u-115079` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Full] NL: "generate 7 sub-question for the main research question "How do urban Chinese women born in the 1980s and 1990s perceive differently toward having a second child?"" → `ENTRYPOINT ResearchSubquestions

TASK ResearchSubquestions : LIST[STRING] {
  GENERATE(target="research_subquestions", content="Generate the most relevant subquestions for the main research question: How do urban Chinese women born in the 1980s and 1990s differ in their perceptions toward having a second child?", quantity=7) -> questions : LIST[STRING]
  RETURN questions
}` — GENERATE plus exact list quantity captures the requested artifact and count; the research topic is appropriately a content payload. Flow-If is irrelevant.
  - `1775857930417` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "hello my friend i want you to help me" → `ENTRYPOINT FriendSupportConversation

CONVO FriendSupportConversation {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Help me make my friend happy because he is sad.")
  }
  TURN t2 SPEAKER=USER REPLY_TO t1 {
    UTTER inform(content="He is sad because of conflict with his employer and stress at work.")
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    UTTER inform(content="He wants to take an SSRI without seeing a doctor.")
  }
  TURN t4 SPEAKER=USER REPLY_TO t3 {
    UTTER ask(content="Do you think he will listen to me?")
  }
}` — The escalating support and medication-safety context is sequenced as a conversation. The substantive advice belongs in UTTER payloads; Flow-If is irrelevant.
  - `1775611747861` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "Can you please recommend me some interesting places which are not too far away from where I live?" → `ENTRYPOINT KoreaTripConversation

CONVO KoreaTripConversation {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Recommend interesting overseas places not too far from where I live.")
  }
  TURN t2 SPEAKER=USER REPLY_TO t1 {
    UTTER inform(content="I am based in Sydney, Australia; I prefer an overseas city with good public transportation.")
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    UTTER correct(content="Recommend alternatives similar to Singapore, Wellington, Taipei, Hong Kong, Tokyo, and Osaka because I have already visited those places.")
  }
  TURN t4 SPEAKER=USER REPLY_TO t3 {
    UTTER ask(content="Seoul looks good. Provide a two-week itinerary and estimated total cost.")
  }
}` — The CONVO captures location, transit preference, correction, selected destination, requested duration, and cost requirement. It cannot formally encode travel-recommendation evidence or current prices, which remain prose content; Flow-If is irrelevant.
  - `1775749936812` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "I would like brainstorming ideas for recipes and travel etc." → `ENTRYPOINT CulinaryRoadTripConversation

CONVO CulinaryRoadTripConversation {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Brainstorm ideas involving recipes, travel, and related topics.")
  }
  TURN t2 SPEAKER=USER REPLY_TO t1 {
    UTTER ask(content="I like the culinary road-trip idea. Give me three or four options for a one-week trip.")
  }
}` — The conversational narrowing from broad brainstorming to a quantified one-week culinary-road-trip request is retained. Generated destination ideas remain open prose; Flow-If is irrelevant.
  - `1775942140464` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "Are you familiar with software designs???" → `ENTRYPOINT AutomationDesignConversation

CONVO AutomationDesignConversation {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Are you familiar with software design?")
  }
  TURN t2 SPEAKER=USER REPLY_TO t1 {
    UTTER ask(content="Suggest software designs that are easy for toddlers and teenagers to use.")
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    UTTER ask(content="What software designs can be used for automation?")
  }
  TURN t4 SPEAKER=USER REPLY_TO t3 {
    UTTER ask(content="Do I need coding experience for this?")
  }
}` — The topic transition and final prerequisite question are ordered explicitly. Explanatory recommendations are appropriately retained as opaque conversational substance; Flow-If is irrelevant.
- **Cross-check:** used=False, agreement=partial — No independent translations were supplied. Self-assessment: high likely agreement for the simple household, code-fix, exact-quantity, and manager-follow-up patterns; partial agreement for web workflows because models may choose different action-result bindings, and for open conversations because models may encode only the latest turn rather than the full trajectory. The submitted PATCH does not alter any of these convergence properties.
- **Required changes:**
  - `Flow-If`: Remove this PATCH from the attempt or replace it with an actual delta. The proposed grammar, semantics, example, and glossary gloss already match the current Flow-If specification, so it must not be recorded as a new revision.
  - `Action`: For the motivating support conditional, add a typed, normative read/query operation (or a general typed query signature) that can bind order lateness and customer purchase-status facts as BOOL or enum-like values; then provide a Flow-If example using those bindings rather than check_replied.
- **Logic issues:** The proposal labels Flow-If as revised, but its proposed grammar, semantics, worked example, and glossary gloss are already present in the current specification and glossary; it is a no-op rather than a language change.; The summary's claim that the conditional manager follow-up task is newly verified without modifications is consistent with the current specification, but it cannot justify a PATCH revision.; The flagship example is valid under the current spec: check_replied binds BOOL, its future deadline suspends before IF evaluation, and NOT replied selects the follow-up branch. It therefore demonstrates existing behavior rather than revised behavior.; The proposal does not address the materially different held-support conditional: the language has no documented typed query for lateness or first-time/repeat-buyer status, so Flow-If alone cannot express that item's branch conditions.
- **Decision:** needs-rework
- **Documenter summary:** The Shaper proposed re-submitting the existing Flow-If construct (grammar, semantics, worked example, glossary gloss) verbatim as a PATCH revision to cover the manager follow-up task, without introducing any actual language change. The Critic rejected this as needs-rework, noting all five pre-KPIs were neutral since the text is byte-for-byte identical to the current spec, and citing the held-support-1 simulation (order-lateness/buyer-status conditions) as evidence the real gap—a typed query capability for arbitrary state facts—remains unaddressed.
- **Cost this sprint:** $0.2082

## Sprint 8 (attempt 2/3) — 2026-09-23

- **Language version:** 7.0.0 → 7.0.0 (MAJOR)
- **Candidate task:** If my manager hasn't replied by Friday, send a polite follow-up; otherwise do nothing.
- **Shaper proposal (model: gemini/gemini-3.1-pro-preview):** Adds a typed support query Action operation and revises the Action specification to support condition checking for customer support requests.
- **Changes:** `Action` (revise, MAJOR)
- **Critic decision:** needs-rework — The typed support query is a sound and useful extension: it materially improves support-workflow coverage and lets Flow-If operate on explicit live-state facts. This attempt cannot be accepted because the normative example implements the stated policy incorrectly, and the unconstrained target and metric strings produce the exact cross-provider variation that the language is meant to eliminate. Defining canonical support identities, metric names, and failure/invariant behavior would make the core idea ready for acceptance.
- **Doc hygiene:** pass — All changes carry a complete glossary entry (gloss + worked example).
- **Pre-KPI assessment:**
  - coverage: benefit — The typed check_support_status operation adds a needed state-query capability for held-out customer-support workflows, allowing a support condition to feed Flow-If rather than being hidden in an Action content string. It directly improves coverage for the sampled support item, though the unrestricted metric and target strings leave support-record selection underdefined.
  - expressivity: mixed — The new BOOL result makes lateness and buyer-status conditions expressible as executable branches. However, the proposal does not define how a customer, order, and support case are correlated, which metrics are valid, or whether first-time and repeat-buyer statuses are mutually exclusive; those omissions can lose important support-workflow meaning.
  - determinism: mixed — A normative support operation is an improvement over inventing arbitrary status-query operations. But independent translations already vary between metric="late", "lateness", and "is_late", and between targets "order", "customer_order", and "customer_profile"; with no canonical metric vocabulary or support-record identity rule, translators will not reliably converge.
  - interpretability: mixed — check_support_status is readily understandable and its BOOL output has a clear role in Checks. Its parameters are nevertheless semantically open-ended strings, so a reader cannot determine the supported metric universe, target format, whether a query concerns one customer/order relationship, or the behavior for missing or ambiguous records.
  - improvement: benefit — For the support simulation, explicit typed queries followed by nested Flow-If blocks give a weaker executor a substantially better operational plan than raw prose. The supplied worked example undermines that benefit because its ELSE branch sends a repeat-buyer offer whenever the order is not late.
- **Simulated examples:**
  - `held-support-1` (seed_tasks) [Full] NL: "If the customer's order is late and they're a first-time buyer, offer a 10% discount; if they're a repeat buyer, offer free expedited shipping instead." → `ENTRYPOINT SupportOffer

TASK SupportOffer {
  ACTION check_support_status(target="customer_order", metric="is_late") -> is_late : BOOL
  ACTION check_support_status(target="customer", metric="is_first_time_buyer") -> is_first_time : BOOL
  ACTION check_support_status(target="customer", metric="is_repeat_buyer") -> is_repeat : BOOL
  IF is_late THEN {
    IF is_first_time THEN {
      ACTION send_message(recipient="customer", content="Offer a 10% discount.")
    } ELSE {
      IF is_repeat THEN {
        ACTION send_message(recipient="customer", content="Offer free expedited shipping.")
      }
    }
  }
}` — The proposed SUPPORT Action is essential. The discount and shipping branches must both be gated by lateness; the proposal's worked example incorrectly puts the repeat-buyer branch in the outer ELSE.
  - `dev-embodied-1` (seed_tasks) [Full] NL: "Rinse the mug in the sink, then put it in the coffee maker." → `ENTRYPOINT RinseThenPlace

TASK RinseThenPlace {
  ACTION rinse(target="mug", destination="sink") -> mug : REF[STRING]
  ACTION place(target=mug, destination="coffee_maker")
}` — Existing household Actions and REF data flow fully express the task; the proposed support query is irrelevant.
  - `14a4e19d-d82d-45dd-b4f0-6b60ed87d085` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Partial] NL: "Find nearest Sprouts Farmers Market and add two fruits and one sauce from the deals." → `ENTRYPOINT AddSproutsDealsToCart

TASK AddSproutsDealsToCart {
  ACTION search_web(target="nearest Sprouts Farmers Market") -> market : REF[STRING]
  ACTION open_page(target=market)
  ACTION select_filter(target="deals")
  GENERATE(target="deal_item_ids", content="Choose exactly two fruit items and one sauce item from the currently displayed deals.", quantity=3) -> items : LIST[STRING]
  FOR EACH item IN items {
    ACTION add_to_cart(target=item)
  }
}` — Existing web/cart constructs capture the navigation and additions, but selecting exactly the requested category composition remains an opaque GENERATE instruction rather than a typed filtering or selection constraint. The proposed support query is irrelevant.
  - `04b8b406-a031-48a3-a002-b1791d872e16` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Add $100 Google Play Gift Card to cart and recipient email address as abc@abc.com" → `ENTRYPOINT AddGiftCardToCart

TASK AddGiftCardToCart {
  ACTION search_web(target="$100 Google Play Gift Card")
  ACTION fill_field(target="recipient_email", content="abc@abc.com")
  ACTION add_to_cart(target="$100 Google Play Gift Card")
}` — Existing web Actions preserve the product amount, recipient-email configuration, and order. The proposed support query is irrelevant.
  - `trial_T20190908_033349_122378#2` (ALFRED (json_2.1.0, train)) [Full] NL: "Put a cleaned sponge in the tub." → `ENTRYPOINT PutCleanedSpongeInTub

TASK PutCleanedSpongeInTub {
  ACTION rinse(target="sponge") -> sponge : REF[STRING]
  ACTION place(target=sponge, destination="tub")
}` — Existing household Actions and the rinse result reference preserve the cleaning-before-placement dependency. The proposed support query is irrelevant.
  - `trial_T20190907_181451_902505#0` (ALFRED (json_2.1.0, train)) [Full] NL: "Wash the cloth in the sink on the left." → `ENTRYPOINT WashCloth

TASK WashCloth {
  ACTION rinse(target="cloth", destination="sink_on_the_left")
}` — The requested outcome is directly represented by the existing rinse Action. The proposed support query is irrelevant.
  - `django__django-12713` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "Allow overridding widget in formfield_for_manytomany().
Description
	 
		(last modified by Mariusz Felisiak)
	 
It does not work when I set widget param to function formfield_for_manytomany().
This is different from the formfield_for_foreignkey() function.
" → `ENTRYPOINT AllowWidgetOverride

TASK AllowWidgetOverride {
  ACTION modify_code(target="django/contrib/admin/options.py", content="Allow formfield_for_manytomany() to accept and honor an overriding widget parameter, matching formfield_for_foreignkey().")
  ACTION run_tests(target="formfield_for_manytomany")
}` — Existing code Actions capture the requested modification and validation. The proposed support query is irrelevant.
  - `scikit-learn__scikit-learn-12682` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "`SparseCoder` doesn't expose `max_iter` for `Lasso`
`SparseCoder` uses `Lasso` if the algorithm is set to `lasso_cd`. It sets some of the `Lasso`'s parameters, but not `max_iter`, and that by default is 1000. This results in a warning in `examples/decomposition/plot_sparse_coding.py` complaining that the estimator has not converged.



I guess there should be a way for the user to specify other parameters of the estimator used in `SparseCoder` other than the ones provided in the `SparseCoder.__init__` right now.
" → `ENTRYPOINT ConfigureSparseCoder

TASK ConfigureSparseCoder {
  ACTION modify_code(target="sklearn/decomposition/dict_learning.py", content="Expose max_iter and other Lasso estimator parameters through SparseCoder when algorithm is lasso_cd, so callers can override the Lasso default of 1000 and avoid the convergence warning.")
  ACTION modify_code(target="examples/decomposition/plot_sparse_coding.py", content="Configure the SparseCoder example to exercise its exposed Lasso max_iter parameter and avoid the non-convergence warning.")
  ACTION run_tests(target="examples/decomposition/plot_sparse_coding.py")
}` — Existing code Actions preserve the affected implementation, example, cause, and validation order. The proposed support query is irrelevant.
  - `c6991` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Do you think that many cultures can live together if they don't share the same values." → `ENTRYPOINT CultureValuesResponse

TASK CultureValuesResponse : STRING {
  GENERATE(target="response", audience="user", content="Give a balanced answer to whether many cultures can live together when they do not share the same values.") -> response : STRING
  RETURN response
}` — The response intent and audience are captured, while the opinion's substantive content remains an appropriate opaque generation payload. The proposed support query is irrelevant.
  - `c3906` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "I believe that the food stamps budget should be cut. I think the government is spending too much money on this" → `ENTRYPOINT FoodStampsResponse

TASK FoodStampsResponse : STRING {
  GENERATE(target="response", audience="user", content="Respond thoughtfully to the user's view that the food-stamps budget should be cut because government spending is too high.") -> response : STRING
  RETURN response
}` — The conversational response intent, user audience, and stated position are retained in the generation request; the response substance is opaque by design. The proposed support query is irrelevant.
  - `c7628` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Is it rude to block someone on Facebook due to  them loving Trump and I don't?" → `ENTRYPOINT SocialBoundaryAdvice

TASK SocialBoundaryAdvice : STRING {
  GENERATE(target="response", audience="user", content="Give considerate advice on whether blocking someone on Facebook because of disagreement over Trump is rude.") -> response : STRING
  RETURN response
}` — The advice-seeking speech intent, audience, platform, and condition are captured; the actual advice remains prose content. The proposed support query is irrelevant.
  - `c1874` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Its ok to feel sexually attracted to my teacher?" → `ENTRYPOINT TeacherAttractionAdvice

TASK TeacherAttractionAdvice : STRING {
  GENERATE(target="response", audience="user", content="Answer whether it is okay to feel sexually attracted to one's teacher, with attention to professional boundaries and safe, appropriate guidance.") -> response : STRING
  RETURN response
}` — The question, audience, and requested guidance are represented, while the sensitive advice itself remains an opaque response payload. The proposed support query is irrelevant.
  - `wildchat1m_en3u-26068` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0301)) [Partial] NL: "Write a Day 1 script for the Creeper.

(Characters: Cupa the Creeper, [player])

(Scene: Forest - day)

(The only thing that Cupa fears is exploding - meaning that just the sight of TNT terrifies her. But since Cupa is due to give birth in 5 days, the fear could force her into labor)

(Cupa would be looking down at her belly when the day begins - feeling her triplets kicking)" → `ENTRYPOINT CreeperDayOneScript

TASK CreeperDayOneScript : STRING {
  GENERATE(target="script", audience="user", format="script", content="Write Day 1 of a Creeper script. Characters are Cupa the Creeper and [player]. Set it in a forest during daytime. Begin with Cupa looking at her belly and feeling her triplets kick. Cupa fears exploding; seeing TNT terrifies her and, because she is due to give birth in five days, fear could trigger labor.") -> script : STRING
  RETURN script
}` — The requested artifact, character set, setting, chronological opening, and plot constraints are represented; creative script substance properly remains in the payload. The proposed support query is irrelevant.
  - `wildchat1m_en3u-52614` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "come up with an idea for a business with $5 in Belarus " → `ENTRYPOINT BelarusBusinessIdea

TASK BelarusBusinessIdea : STRING {
  GENERATE(target="business_idea", audience="user", content="Propose one viable business idea that can be started with a budget of $5 in Belarus.") -> business_idea : STRING
  RETURN business_idea
}` — The request type, exact budget, country, singular quantity, and audience are captured; the business proposal is open-ended prose content. The proposed support query is irrelevant.
  - `wildchat1m_en3u-1046` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0301)) [Partial] NL: "What if Gendry had the Ability to grow his hair at will?" → `ENTRYPOINT GendryHairScenario

TASK GendryHairScenario : STRING {
  GENERATE(target="scenario", audience="user", content="Explore the hypothetical implications of Gendry having the ability to grow his hair at will.") -> scenario : STRING
  RETURN scenario
}` — The hypothetical-analysis intent and subject are represented, while possible narrative implications remain generative prose. The proposed support query is irrelevant.
  - `wildchat1m_en3u-54612` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "Let's write a blog post that will rank on Google. I want you to try to include {keywords}.
 You should use markdown formatting, including bold, UL/OL, and write with a degree of creativity, burstiness, and human-like. 
And taking into account Average Perplexity, and Burstiness scores. 
and Predictability. The article is “amazon FBA” Written in the language ( english).
 Do not speak in the default classical language, try to be colloquial, closer to the reader. 
Do not use numbers 1, 2, or 3, and so I do not use only points or punctuation. 
I use stop signs and do not use parentheses. 
I just want a different wording from writing chat gpt so that it is completely different in style.
There are also minor spelling errors and human errors in regular notation. 
The keyword you want to target in the search results is ( SEO )" → `ENTRYPOINT AmazonFBABlogPost

TASK AmazonFBABlogPost : STRING {
  GENERATE(target="blog_post", audience="search_engine_readers", format="markdown", register_note="colloquial, creative, human-like, non-classical, unlike default ChatGPT phrasing", content="Write an English blog post about Amazon FBA intended to rank on Google. Target SEO and include the literal placeholder {keywords}. Use bold text and unordered and ordered lists. Aim for creative burstiness while considering perplexity, burstiness, and predictability. Do not use numerals 1, 2, or 3; do not use parentheses; use stop-sign-style breaks; do not rely only on points or punctuation; include minor spelling and notation errors.") -> blog_post : STRING
  RETURN blog_post
}` — Artifact type, audience, language, markdown format, target keyword, register, and explicit restrictions are preserved, but many fine-grained writing requirements necessarily remain in the opaque content payload. The proposed support query is irrelevant.
  - `1775494548419` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "Hello, I would like to ask you for help with monthly budgeting, my budget is 1000zł, I'd like to focus on food because I am a powerlifter." → `ENTRYPOINT PowerliftingBudgetHelp

TASK PowerliftingBudgetHelp : STRING {
  GENERATE(target="response", audience="user", content="Help with monthly budgeting: the budget is 1000 zł and the focus is food because the user is a powerlifter. Ask any necessary tailoring questions and provide practical budget guidance.") -> response : STRING
  RETURN response
}` — The request intent, monetary amount, food focus, powerlifting context, and request for help are retained. The tailored budget advice and follow-up questions remain open prose. The proposed support query is irrelevant.
  - `1775789490736` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "weekend trip plan:niagra falls" → `ENTRYPOINT NiagaraWeekendPlan

TASK NiagaraWeekendPlan : STRING {
  GENERATE(target="trip_plan", audience="user", content="Create a weekend trip plan for Niagara Falls.") -> trip_plan : STRING
  RETURN trip_plan
}` — The requested plan artifact, destination, and weekend duration are captured; itinerary substance is appropriately generated prose. The proposed support query is irrelevant.
  - `1775686840693` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "o fungo nos dedos do pé, se eu passar a mão e depois passar a mão em outra parte do corpo, eu espalho o fungo de local?" → `ENTRYPOINT ToeFungusQuestion

TASK ToeFungusQuestion : STRING {
  GENERATE(target="response", audience="user", content="Respond in Portuguese to whether touching fungal infection on the toes and then another body part can spread it. Give cautious general hygiene guidance and recommend appropriate professional care where needed.") -> response : STRING
  RETURN response
}` — The medical question, transmission condition, requested language, and cautious guidance intent are retained; health explanation remains prose. The proposed support query is irrelevant.
  - `1773888707797` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "I want to go on a holiday trip with lots of natural scenery and I am torn between Turkye and norway because both have many attractive places, which country should I travel to" → `ENTRYPOINT ScenicHolidayRecommendation

TASK ScenicHolidayRecommendation : STRING {
  GENERATE(target="recommendation", audience="user", content="Compare Türkiye and Norway for a holiday focused on abundant natural scenery, then recommend which country to visit and explain the tradeoffs.") -> recommendation : STRING
  RETURN recommendation
}` — The comparison, alternatives, priority, recommendation request, and audience are represented; travel advice substance remains a generation payload. The proposed support query is irrelevant.
- **Cross-check:** used=True, agreement=partial — The independent translations agree strongly on the embodied task and broadly on code-task structure. For the new support item they disagree on target and metric spellings, and Anthropic invents unsupported offer_discount/offer_shipping Actions while Gemini incorrectly makes free shipping apply whenever the first condition is false; this confirms that the proposed query vocabulary and intended branching are not yet deterministic. Open-item translations also vary substantially between CONVO/UTTER records and TASK/GENERATE responses.
- **Required changes:**
  - `Action`: Correct the worked example so the free-expedited-shipping branch is evaluated only when is_late is true and is_first_time is false: nest the first-time/repeat-buyer decision inside an outer `IF is_late THEN` block.
  - `Action`: Define a canonical SUPPORT metric vocabulary and exact metric spellings, at minimum including `is_late`, `is_first_time_buyer`, and `is_repeat_buyer`; state whether unsupported metric strings are static errors.
  - `Action`: Define SUPPORT target identity and correlation semantics: specify canonical target forms for an order, customer, and customer-order case, and state how queries are guaranteed to concern the same customer/order relationship.
  - `Action`: Define the query result behavior for absent, inaccessible, ambiguous, or inconsistent support records, including whether first-time and repeat-buyer results are required to be logical complements. Align this with the existing external-Action-failure rule.
  - `Action`: Revise the grammar comment for the operation signature to describe only operation parameters and result type, not the statement-level binding syntax (`-> IDENT : BOOL`), which is already supplied by the Action grammar.
  - `Action`: Update the Action glossary entry in the actual revised documentation to mention the typed support query and include the corrected, lateness-gated support workflow example.
- **Logic issues:** The proposal's worked example does not preserve its own natural-language condition: its outer ELSE sends the repeat-buyer offer whenever `is_late AND is_first_time` is false, including when the order is not late.; The arbitrary STRING `metric` parameter creates multiple equally plausible encodings such as `late`, `lateness`, and `is_late`, harming deterministic translation.; The arbitrary STRING `target` parameter does not define whether `customer_order`, `order`, `customer`, and `customer_profile` identify related records, so the combined condition can accidentally query different entities.; The semantics says the operation queries a support case or customer record but does not specify behavior when the record is missing, ambiguous, inaccessible, or has contradictory buyer-status facts.; The operation signature notation `check_support_status(target=STRING, metric=STRING) -> IDENT : BOOL` conflates the operation's result type with Action's separate statement-level result-binding grammar.
- **Decision:** needs-rework
- **Documenter summary:** The Shaper proposed adding a typed SUPPORT operation check_support_status(target=STRING, metric=STRING)->BOOL to the Action construct, enabling boolean support-status queries (order lateness, buyer tier) for use in Flow-If conditions. The Critic rejected this as needs-rework because the worked example itself misimplemented the stated policy (the ELSE branch fired whenever the order wasn't late, regardless of buyer status), and the unconstrained target/metric STRING parameters left support-record identity and metric vocabulary underdefined—confirmed by cross-check translations diverging on spellings ("late" vs "is_late") and even inventing unsupported Actions, showing the design would not translate deterministically. The Critic required a corrected, properly-nested example plus canonical metric/target vocabularies and failure-mode semantics before acceptance.
- **Cost this sprint:** $1.2346

## Sprint 8 (attempt 3/3) — 2026-09-23

- **Language version:** 7.0.0 → 8.0.0 (MAJOR)
- **Candidate task:** If my manager hasn't replied by Friday, send a polite follow-up; otherwise do nothing.
- **Shaper proposal (model: gemini/gemini-3.1-pro-preview):** Revise Action to add a canonical support query operation with a strict metric vocabulary, exact target correlation rules, failure semantics, and corrected nested Flow-If workflow evaluation.
- **Changes:** `Action` (revise, MAJOR)
- **Critic decision:** needs-rework — [Forced acceptance after 3 attempt(s) without a clean accept — the required changes below are known issues carried forward for a future sprint to address, not resolved.] The typed, closed support metric vocabulary is a useful extension and materially improves the held-out support task. However, the central customer/order-correlation promise is only prose and the worked example violates its own specific-identifier requirement, so independent translators cannot reliably produce equivalent valid expressions. The proposal should be reworked around typed support references or an equally concrete correlation model before acceptance.
- **Doc hygiene:** pass — All changes carry a complete glossary entry (gloss + worked example).
- **Pre-KPI assessment:**
  - coverage: mixed — The new SUPPORT operation adds actionable coverage for the held-out support-routing task, which previously had no domain operation. However, its requirement for a specific canonical customer/order identifier cannot be satisfied from ordinary contextual requests such as "the customer's order," and the stated correlation rule has no executable or statically checkable mechanism.
  - expressivity: mixed — The three closed metrics and BOOL result express lateness and buyer-status predicates clearly, and the worked nested IF correctly makes both offers contingent on lateness. But the proposal cannot represent or verify which customer belongs to which order: two unrelated strings such as "customer" and "customer_order" are declared consistent by convention rather than by data identity.
  - determinism: harm — Independent translations already disagree on whether the repeat-buyer offer is gated by lateness: both supplied support translations place repeat-buyer handling in the outer ELSE and therefore offer shipping even when an order is not late, while the proposal's example gates it. Translators also have no deterministic way to invent a valid "specific canonical identifier" or decide when separately named targets count as a related evaluation context.
  - interpretability: mixed — The closed metric vocabulary and explicit failure behavior improve readability over arbitrary status strings. Conversely, the glossary claims "entity correlation rules" and "lateness-gated branch evaluation," but correlation is only an unenforceable prose convention and lateness gating is implemented by the particular example's Flow-If structure rather than by Action semantics.
  - improvement: benefit — For a valid support context, explicit live BOOL queries followed by nested branches give a weaker executor a substantially better operational plan than the raw request. This benefit is limited by the inability to resolve an actual customer/order identity and by fail-fast evaluation of all three queries before either branch is selected.
- **Simulated examples:**
  - `dev-web-2` (seed_tasks) [Full] NL: "On the electronics store, filter laptops to 16 GB RAM or more under $1,200, and add the best-rated one to the cart." → `ENTRYPOINT FilterLaptops

TASK FilterLaptops {
  ACTION open_page(target="electronics_store")
  ACTION select_filter(target="laptops", content="RAM >= 16GB")
  ACTION apply_filters(target="laptops", content="price < 1200 USD")
  ACTION sort(target="laptops", ordering="rating_desc") -> sorted_laptops : LIST[REF[STRING]]
  ACTION extract(target=sorted_laptops, limit=1) -> best_laptop : REF[STRING]
  ACTION add_to_cart(target=best_laptop)
}` — The proposed SUPPORT change is irrelevant. Existing web operations express the actionable sequence, although the underlying specification still leaves several web-operation signatures underspecified.
  - `held-support-1` (seed_tasks) [Full] NL: "If the customer's order is late and they're a first-time buyer, offer a 10% discount; if they're a repeat buyer, offer free expedited shipping instead." → `ENTRYPOINT SupportOffer

TASK SupportOffer {
  ACTION check_support_status(target="customer_order", metric="is_late") -> is_late : BOOL
  ACTION check_support_status(target="customer", metric="is_first_time_buyer") -> is_first_time : BOOL
  ACTION check_support_status(target="customer", metric="is_repeat_buyer") -> is_repeat : BOOL
  IF is_late THEN {
    IF is_first_time THEN {
      ACTION send_message(recipient="customer", content="Offer a 10% discount.")
    } ELSE {
      IF is_repeat THEN {
        ACTION send_message(recipient="customer", content="Offer free expedited shipping.")
      }
    }
  }
}` — The new operation enables this item and the expression follows the proposal's intended lateness-gated reading. However, "customer" and "customer_order" are only illustrative labels, not demonstrably specific identifiers or a machine-checkable customer-order correlation.
  - `2a7f7732-ec9b-4d78-91ad-f0fe10bf7daf` (Mind2Web) [Full] NL: "Find a gaming pc which can run Call of Duty Warzone at 4k." → `ENTRYPOINT FindWarzone4kPC

TASK FindWarzone4kPC : REF[STRING] {
  ACTION open_page(target="gaming_pc_finder")
  ACTION search_web(content="gaming PC capable of running Call of Duty Warzone at 4K") -> results : LIST[REF[STRING]]
  ACTION extract(target=results, limit=1) -> pc : REF[STRING]
  RETURN pc
}` — SUPPORT is irrelevant. The exact suitability criterion remains an Action content payload, which is permitted for residual execution conditions.
  - `d64cbfc6-7ace-4cad-9f0a-6643cd83de6e` (Mind2Web) [Fail] NL: "Find the cheapest full-sized Amazon basic comforter with 4+ average customer reviews and priced between 50 to 100 dollars, if red color availabe in the cheapest product then add one to the cart." → `ENTRYPOINT FindComforter

TASK FindComforter {
  ACTION open_page(target="amazon")
  ACTION search_web(content="full-sized Amazon Basics comforter") -> results : LIST[REF[STRING]]
  ACTION apply_filters(target=results, content="average_rating >= 4; price >= 50 USD; price <= 100 USD") -> filtered : LIST[REF[STRING]]
  ACTION sort(target=filtered, ordering="price_asc") -> sorted : LIST[REF[STRING]]
  ACTION extract(target=sorted, limit=1) -> cheapest : REF[STRING]
  ACTION select_filter(target=cheapest, content="color=red") -> red_variant : REF[STRING]
  IF red_variant THEN {
    ACTION add_to_cart(target=cheapest)
  }
}` — No valid conditional availability query exists. This attempted expression is statically invalid because Check defines no truthiness for REF values; treating unavailable red as an external action failure also violates the requested no-op branch. SUPPORT is irrelevant.
  - `trial_T20190918_193418_341390#2` (ALFRED) [Full] NL: "Wash the red apple." → `ENTRYPOINT WashRedApple

TASK WashRedApple {
  ACTION rinse(target="red apple", destination="sink")
}` — SUPPORT is irrelevant; the household action captures the requested actionable core.
  - `trial_T20190908_005450_787345#0` (ALFRED) [Full] NL: "Take the remote from the table, put it on the couch." → `ENTRYPOINT MoveRemote

TASK MoveRemote {
  ACTION pick_up(target="remote", destination="table") -> remote : REF[STRING]
  ACTION place(target=remote, destination="couch")
}` — SUPPORT is irrelevant. REF binding preserves that the same remote is placed.
  - `sympy__sympy-17318` (SWE-bench_Verified) [Full] NL: "Fix sqrtdenest so an expression that cannot be denested is returned unchanged rather than raising IndexError." → `ENTRYPOINT FixSqrtdenest

TASK FixSqrtdenest {
  ACTION modify_code(target="sympy/simplify/radsimp.py", content="Guard _split_gcd against an empty surds tuple so sqrtdenest returns the original expression unchanged instead of raising IndexError at g = a[0].")
  ACTION modify_code(target="sympy/simplify/sqrtdenest.py", content="Ensure the denesting path preserves and returns the original expression when no denesting result is available.")
  ACTION run_tests(target="sympy/simplify/tests/test_sqrtdenest.py")
}` — SUPPORT is irrelevant. The bug report and exact change condition are valid residual code-change content.
  - `matplotlib__matplotlib-24026` (SWE-bench_Verified) [Full] NL: "Make stackplot accept CN aliases without changing the Axes cycler." → `ENTRYPOINT FixStackplotCycler

TASK FixStackplotCycler {
  ACTION modify_code(target="lib/matplotlib/stackplot.py", content="Do not call axes.set_prop_cycle(color=colors) in stackplot. Resolve supplied colors, including CN aliases, locally for the stackplot collections while leaving the Axes property cycler unchanged.")
  ACTION run_tests(target="lib/matplotlib/tests/test_stackplot.py")
}` — SUPPORT is irrelevant. The required behavioral invariant is retained in modify_code content.
  - `c1874` (PRISM) [Partial] NL: "Its ok to feel sexually attracted to my teacher?" → `ENTRYPOINT TeacherAttraction

CONVO TeacherAttraction {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Is it okay to feel sexually attracted to my teacher?")
  }
}` — Conversation preserves the speech act and speaker; the question's substantive subject matter remains the appropriate opaque content payload. SUPPORT is irrelevant.
  - `c7335` (PRISM) [Partial] NL: "Based on that information, explain in autist level detail what would need to be purchased for such a present." → `ENTRYPOINT PresentPurchaseList

TASK PresentPurchaseList : STRING {
  GENERATE(target="purchase_list", audience="user", content="Create a detailed, concrete purchasing checklist for materials and tools for an intermediate-sewing aviation-themed throw pillow or throw project. Use clear, respectful, highly explicit organization and include quantities or selection criteria where useful.") -> purchase_list : STRING
  RETURN purchase_list
}` — GENERATE captures the requested output, audience, and requested degree of detail while avoiding an ableist register label. The generated list substance remains prose. SUPPORT is irrelevant.
  - `c5178` (PRISM) [Partial] NL: "Is incest ever justified?" → `ENTRYPOINT IncestQuestion

CONVO IncestQuestion {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Is incest ever justified?")
  }
}` — The expression preserves the user question and its conversational form; an answer's ethical analysis is opaque prose. SUPPORT is irrelevant.
  - `c3395` (PRISM) [Partial] NL: "do aliens exist" → `ENTRYPOINT AnswerAliens

TASK AnswerAliens : STRING {
  GENERATE(target="answer", audience="user", content="Answer whether aliens exist, distinguishing confirmed evidence from scientific possibility.") -> answer : STRING
  RETURN answer
}` — The answer request and audience are structured, while the scientific explanation remains an allowed prose payload. SUPPORT is irrelevant.
  - `wildchat1m_en3u-68926` (PATHs) [Partial] NL: "Reply in English to the packaging message; do not use a template, and state that production will take about 22 days after the prepayment arrives." → `ENTRYPOINT ReplyPackagingEmail

TASK ReplyPackagingEmail : STRING {
  GENERATE(target="email_reply", audience="customer", content="Write an original English business-email reply. Acknowledge the packaging file and that labels match the previous order; confirm careful label adhesion and glass cleanliness; state that production will be completed in about 22 days after prepayment is received; and provide this timing so the customer can arrange forwarding shipment. Do not use a stock template.") -> reply : STRING
  RETURN reply
}` — The generation intent, audience, language, originality constraint, timing condition, and required content are retained; the email wording is legitimately prose. SUPPORT is irrelevant.
  - `wildchat1m_en3u-74705` (PATHs) [Partial] NL: "How to tell a friend “I look forward to seeing you and for our next music festivals”?" → `ENTRYPOINT ImproveFriendMessage

TASK ImproveFriendMessage : STRING {
  GENERATE(target="message", audience="friend", content="Give a natural, warm corrected phrasing of: I look forward to seeing you and to our next music festivals together.") -> message : STRING
  RETURN message
}` — The recipient, intent, and desired rewriting task are captured; the actual improved wording remains prose. SUPPORT is irrelevant.
  - `wildchat1m_en3u-7616` (PATHs) [Fail] NL: "Research Hermanubis, write a detailed 5000-word essay, and save it as Hermanubis.docx under the provided command-only, JSON-only, persistent-memory protocol." → `ENTRYPOINT ResearchHermanubis

TASK ResearchHermanubis {
  ACTION search_web(target="Hermanubis") -> sources : LIST[REF[STRING]]
  GENERATE(target="essay", audience="general", content="Write a detailed 5000-word essay about Hermanubis, including mythology, syncretism, iconography, cult, chronology, and historical evidence from the research.", quantity=5000) -> essay : STRING
  ACTION add_file(target="Hermanubis.docx", content=essay)
}` — The research/write/save backbone is represented, but the language has no formal way to use bound search results as GENERATE input, preserve the required command-only JSON protocol, manage persistent memory, delegate agents, or model random-shutdown continuation. SUPPORT is irrelevant.
  - `wildchat1m_en3u-97547` (PATHs) [Partial] NL: "Explain briefly how reliable excerpts from The Twenty-four Exemplars of Filial Piety are as evidence about Song Dynasty Chinese values." → `ENTRYPOINT AssessFilialPietySource

TASK AssessFilialPietySource : STRING {
  GENERATE(target="answer", audience="student", content="Give a short answer assessing the extent to which excerpts from The Twenty-four Exemplars of Filial Piety are reliable evidence about Song Dynasty Chinese values. Explain that they reveal promoted Confucian ideals but are didactic elite-authored stories and not a complete record of everyday beliefs or behavior.") -> answer : STRING
  RETURN answer
}` — Audience, requested brevity, source-evaluation task, and required analytical structure are represented; the explanation is prose. SUPPORT is irrelevant.
  - `1775448065619` (ThoughtTrace) [Partial] NL: "I want to start a healthy diet. Can you help me plan a simple meal prep for 3 days that includes breakfast, lunch, and dinner? I prefer high-protein options." → `ENTRYPOINT PlanMealPrep

TASK PlanMealPrep : STRING {
  GENERATE(target="meal_prep_plan", audience="user", content="Create a simple high-protein healthy meal-prep plan for exactly 3 days. Include breakfast, lunch, and dinner for each day, plus practical preparation guidance that saves time.") -> plan : STRING
  RETURN plan
}` — The task, audience, three-day duration, meal categories, protein preference, and time-saving intent are preserved; recipes and nutrition advice are prose substance. SUPPORT is irrelevant.
  - `1775854689771` (ThoughtTrace) [Partial] NL: "FASTER RESPONSE PLEASE" → `ENTRYPOINT FasterResponseRequest

CONVO FasterResponseRequest {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Please respond faster.")
  }
}` — Conversation captures the user speech act, but BrainCode has no response-latency, priority, or service-level constraint, so the crucial "faster" execution constraint is only prose. SUPPORT is irrelevant.
  - `1775527329782` (ThoughtTrace) [Partial] NL: "Hi, I want to learn japanese, can you give a plan please" → `ENTRYPOINT LearnJapanesePlan

TASK LearnJapanesePlan : STRING {
  GENERATE(target="study_plan", audience="user", content="Create a practical beginner plan for learning Japanese, including an ordered starting sequence, study-time organization, and basic greetings for practice.") -> plan : STRING
  RETURN plan
}` — The requested plan, audience, and the later-conversation refinements are incorporated, while educational recommendations remain prose. SUPPORT is irrelevant.
  - `1773847362254` (ThoughtTrace) [Partial] NL: "hello" → `ENTRYPOINT Greeting

CONVO Greeting {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="Hello.")
  }
}` — The greeting and its conversational speaker are represented. Its lexical content is an opaque utterance payload; SUPPORT is irrelevant.
- **Cross-check:** used=True, agreement=low — The supplied translations vary materially, not merely stylistically: support translations interpret the repeat-buyer branch as the ELSE of "late AND first-time," unlike the proposal's lateness-gated example; several providers use UTTER illegally inside TASK bodies; and web translations assign incompatible undocumented result types to select_filter. The new operation reduces none of the support target-identity ambiguity.
- **Required changes:**
  - `Action`: Replace the unenforceable phrase "all related ... calls ... must use consistent canonical entity identifiers" with a typed correlation mechanism. For example, define a typed support-case/order/customer reference returned by a lookup Action, define which metric accepts each reference type, and require all related metrics to consume the same bound reference or an explicitly defined linked reference.
  - `Action`: Define a canonical identifier grammar and resolution rule for SUPPORT targets, including how a contextual phrase such as "the customer's order" becomes a valid specific identifier. Do not call generic strings such as "customer" and "customer_order" specific identifiers unless those are explicitly reserved context identifiers with defined bindings.
  - `Action`: State whether check_support_status calls are evaluated eagerly in source order or may be placed within Flow-If branches. If the intended behavior is to avoid unnecessary failures, revise the worked example to query repeat-buyer status only in the branch where it is needed, or explicitly state that eager fail-fast querying is intentional.
  - `Action`: Revise the glossary gloss to remove the unsupported claim that Action itself provides "lateness-gated branch evaluation." Say that check_support_status supplies support predicates; Flow-If supplies any gating.
  - `Action`: Add a normative disambiguation example for the natural-language scope of "if late and first-time ...; if repeat ... instead," explicitly establishing whether repeat-buyer shipping requires lateness. This is necessary because the two independent translations chose the opposite branch scope from the proposal.
- **Logic issues:** The correlation rule is not statically enforceable: the language has only STRING target values, no customer-order relation, no evaluation-context identifier, and no definition of what makes two calls related.; The worked example uses "customer" and "customer_order", which are generic labels rather than the required specific canonical identifiers; it therefore does not demonstrate compliance with its own stated SUPPORT semantics.; The proposal says correlation requires consistent canonical entity identifiers, but its example necessarily uses different identifiers for order-level and customer-level queries without defining how those identifiers are correlated.; The support queries execute before the IF. Thus a missing or contradictory repeat-buyer record halts a late first-time-buyer discount even though the repeat result is not semantically needed for that branch.; The glossary's phrase "lateness-gated branch evaluation" attributes a Flow-If property to Action and overclaims what the Action semantics provides.; The independent translations demonstrate a real conditional-scope ambiguity: their outer ELSE allows free shipping for a repeat buyer whose order is not late, while the proposal's example does not.
- **Decision:** accepted
- **Documenter summary:** Shaper proposed adding a SUPPORT domain operation (check_support_status) with a closed metric vocabulary, entity-correlation-by-naming-convention rules, and fail-fast failure semantics, plus a corrected nested Flow-If worked example. The Critic found this 'needs-rework' — flagging that the correlation rule is unenforceable prose (only STRING targets, no real customer/order identity), the worked example uses generic labels instead of the required specific identifiers, eager fail-fast querying breaks branches that don't need all three metrics, and independent translations disagreed on whether the repeat-buyer offer is lateness-gated — but this was attempt 3/3, so the change was force-accepted with these required changes carried forward as known unresolved issues for a future sprint, since doc hygiene (complete glossary entry) was satisfied.
- **Cost this sprint:** $1.3206

## Sprint 9 (attempt 1/3) — 2026-09-23

- **Language version:** 8.0.0 → 8.0.0 (MAJOR)
- **Candidate task:** Rinse the mug in the sink, then put it in the coffee maker.
- **Shaper proposal (model: anthropic/claude-sonnet-5):** Codifies (as an explicit normative rule rather than an implicit example convention) that when a later step in the same Task acts on an entity a prior Action already produced, the translator must reuse that Action's bound REF rather than re-describing the entity with a fresh string literal — directly targeting this sprint's rinse-then-place causal-chain task, which is otherwise already fully expressible with existing constructs.
- **Changes:** `Action` (revise, MAJOR)
- **Critic decision:** needs-rework — The core idea is valuable and directly improves the selected rinse-then-place causal chain, with exact independent-translation agreement on that example. It cannot be accepted because the rule rests on undefined Action result signatures and uses an unenforceable category of 'determinism violation,' leaving both REF availability and antecedent resolution ambiguous. Defining identity-preserving action results and a checkable, deterministic coreference procedure would turn this into a focused positive change.
- **Doc hygiene:** pass — All changes carry a complete glossary entry (gloss + worked example).
- **Pre-KPI assessment:**
  - coverage: neutral — The proposal adds no operations or task shapes, so it does not expand coverage. The rinse-then-place chain was already representable in the existing examples; several sampled closed tasks still depend on underspecified Action result signatures and operation semantics.
  - expressivity: mixed — Reusing a REF preserves an important instance-level distinction for the embodied causal chain, such as placing the particular mug that was rinsed. However, the rule says an Action must have 'produced' the entity even though actions such as rinse and pick_up ordinarily operate on an existing entity, and the specification does not define which operations may return identity-preserving REF results.
  - determinism: mixed — The two independent translations agree exactly with the proposed REF-reuse pattern for dev-embodied-1, so the intended narrow improvement is real. But the rule is not a static error, depends on an undefined judgment about an 'unambiguous definite re-reference,' and leaves translators to choose whether an operation returns a REF at all; independent translations remain divergent on web workflows and open-item Task-versus-CONVO selection.
  - interpretability: mixed — A later target=mug is clearer than a repeated descriptive literal when mug is a bound REF. Yet calling a non-grammar violation a 'determinism violation' provides no defined conformance behavior, while 'produced,' 'same Task,' and the eligible REF-producing operations are not precisely defined; readers cannot reliably determine whether an expression is compliant.
  - improvement: benefit — For dev-embodied-1, the explicit data-flow edge from rinse to place materially helps an executor avoid selecting a different mug. The benefit is narrow because the existing Action result-signature gap makes the same technique unreliable for other identity-dependent chains.
- **Simulated examples:**
  - `dev-embodied-1` (seed_tasks) [Full] NL: "Rinse the mug in the sink, then put it in the coffee maker." → `ENTRYPOINT RinseThenPlace

TASK RinseThenPlace {
  ACTION rinse(target="mug", destination="sink") -> mug : REF[STRING]
  ACTION place(target=mug, destination="coffee_maker")
}` — The proposed coreference rule directly helps: 'it' is represented by the bound mug REF rather than a second literal.
  - `dev-web-1` (seed_tasks) [Full] NL: "Go to the flight booking site, search flights from Tel Aviv to Berlin next Tuesday, and list the three cheapest options." → `ENTRYPOINT BookFlight

TASK BookFlight CONTEXT execution_date="2025-06-03" : LIST[REF[STRING]] {
  ACTION open_page(target="flight_booking_site")
  ACTION search_travel(origin="Tel Aviv", destination="Berlin", date="2025-06-10") -> raw_flights : LIST[REF[STRING]]
  ACTION sort(target=raw_flights, ordering="price_asc") -> sorted_flights : LIST[REF[STRING]]
  ACTION extract(target=sorted_flights, limit=3) -> cheapest_flights : LIST[REF[STRING]]
  RETURN cheapest_flights
}` — Existing REF data flow is useful, but Action says operations without explicit signatures have Result none while no explicit signatures are supplied for search_travel, sort, or extract. The expression follows the current Task example but its result bindings need formal signatures.
  - `59bdd427-c34b-4b93-a8b8-0c3a49acdcfa` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Partial] NL: "Book a round-trip flight from Santa Fe, New Mexico to Phoenix, Arizona for 1 adult on August 13th and returning on August 28th." → `ENTRYPOINT BookRoundTripFlight

TASK BookRoundTripFlight {
  ACTION open_page(target="flight_booking_site")
  ACTION search_travel(origin="Santa Fe, New Mexico", destination="Phoenix, Arizona", date="2025-08-13", return_date="2025-08-28", passengers=1)
  ACTION submit(target="selected_round_trip_flight")
}` — The dates, route, passenger quantity, and booking intent are captured, but the language has no defined operation for selecting a particular returned fare before submission. The proposed REF rule is irrelevant.
  - `122178b3-b5d4-41f0-be38-150ca0e2f5ed` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Find a black blazer for men with L size and add to wishlist." → `ENTRYPOINT AddBlazerToWishlist

TASK AddBlazerToWishlist {
  ACTION open_page(target="shopping_site")
  ACTION search_web(target="men's blazer") -> results : LIST[REF[STRING]]
  ACTION select_filter(target=results, content="gender=men") -> mens_results : LIST[REF[STRING]]
  ACTION select_filter(target=mens_results, content="color=black") -> black_results : LIST[REF[STRING]]
  ACTION select_filter(target=black_results, content="size=L") -> large_black_blazers : LIST[REF[STRING]]
  ACTION extract(target=large_black_blazers, limit=1) -> blazer : REF[STRING]
  ACTION add_to_list(target=blazer, destination="wishlist")
}` — The chain correctly retains the selected blazer identity. As with the flight example, the required non-none result signatures for search_web, select_filter, and extract are absent from Action semantics.
  - `trial_T20190908_130732_924172#2` (ALFRED (json_2.1.0, train)) [Full] NL: "Putting two bars of soap in a drawer" → `ENTRYPOINT PutTwoSoapBarsInDrawer

TASK PutTwoSoapBarsInDrawer {
  ACTION pick_up(target="first_soap_bar") -> first_soap_bar : REF[STRING]
  ACTION place(target=first_soap_bar, destination="drawer")
  ACTION pick_up(target="second_soap_bar") -> second_soap_bar : REF[STRING]
  ACTION place(target=second_soap_bar, destination="drawer")
}` — Each placement reuses the corresponding acquired entity REF. The second soap bar is a genuinely new instance, so a fresh descriptor is appropriate under the proposal.
  - `trial_T20190906_182632_563404#0` (ALFRED (json_2.1.0, train)) [Partial] NL: "Examine a watering can by the light of a desk lamp." → `ENTRYPOINT ExamineWateringCan

TASK ExamineWateringCan {
  ACTION turn_on(target="desk_lamp")
  ACTION pick_up(target="watering_can") -> watering_can : REF[STRING]
  ACTION examine(target=watering_can, content="by the light of the desk lamp")
}` — Ordering and the watering-can identity are captured, but examine is not in the normative household vocabulary and the lamp's relation is only an opaque content string. The proposed change does not address this missing operation/attribute semantics.
  - `django__django-13807` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "loaddata crashes on SQLite when table names are SQL keywords." → `ENTRYPOINT FixLoaddataSqliteKeywordTableNames

TASK FixLoaddataSqliteKeywordTableNames {
  ACTION modify_code(target="django/db/backends/sqlite3/base.py", content="In check_constraints, quote table_name in PRAGMA foreign_key_check(%s) and PRAGMA foreign_key_list(%s) so SQL-keyword table names such as order are handled safely.")
  ACTION run_tests(target="django/db/backends/sqlite3/base.py")
}` — The actionable code-change condition and validation step are represented. The proposed coreference rule is irrelevant.
  - `pytest-dev__pytest-6197` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "Regression in 5.2.3: pytest tries to collect random __init__.py files" → `ENTRYPOINT FixPytestInitCollectionRegression

TASK FixPytestInitCollectionRegression {
  ACTION modify_code(target="src/_pytest/python.py", content="Prevent pytest 5.2.3 from collecting and importing unrelated __init__.py files beneath the current directory while retaining normal test collection.")
  ACTION run_tests(target="src/_pytest/python.py")
}` — The issue's requested repair and test validation are expressible as code actions. The proposal is irrelevant.
  - `c691` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Im planning to travel To New York . One thing that i love is walking in the city at night , is it safe?" → `ENTRYPOINT NYCNightWalkingQuestion

CONVO NYCNightWalkingQuestion {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="I am planning to travel to New York and enjoy walking in the city at night.")
    UTTER ask(content="Is it safe?")
  }
}` — The user, speech acts, ordering, and subject relation are captured; the safety-answer substance appropriately remains outside formal syntax. The proposed Action change is irrelevant.
  - `c5828` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "I'm trying to do a conversation with a very influent business man, can you help me to try and make the contact?" → `ENTRYPOINT ContactInfluentialBusinessperson

CONVO ContactInfluentialBusinessperson {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Help me make contact with an influential businessperson so that I can have a conversation with them.")
  }
}` — The request and its recipient role are structured as a user ask; the requested advice or outreach plan is open prose substance. The proposed REF rule is irrelevant.
  - `c7943` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "How can I get my supervisor to take me seriously and give me a leadership role?" → `ENTRYPOINT LeadershipAdvice

TASK LeadershipAdvice : STRING {
  GENERATE(target="advice", audience="user", content="Advise the user on how to be taken seriously by their supervisor and earn a leadership role.") -> advice : STRING
  RETURN advice
}` — The advice intent, audience, and requested outcome are captured; the advice itself is correctly an opaque generation payload. The proposed change is irrelevant.
  - `c803` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "I believe taxes are bad, what do you think about that? Answer in 50 words" → `ENTRYPOINT TaxesOpinion

TASK TaxesOpinion : STRING {
  GENERATE(target="response", audience="user", content="Respond to the user's belief that taxes are bad.", quantity=50) -> response : STRING
  RETURN response
}` — The response intent, audience, proposition, and exact 50-word constraint are represented. The opinion's prose substance remains an appropriate GENERATE payload.
  - `wildchat1m_en3u-38835` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-0314)) [Partial] NL: "what are the use cases of applied observability in law firms and for their clients. What the are the details of the same. Is there any law firm which has implement or is looking into such use cases in future." → `ENTRYPOINT AppliedObservabilityLawFirms

TASK AppliedObservabilityLawFirms : STRING {
  ACTION search_web(target="applied observability use cases for law firms and clients")
  ACTION search_web(target="law firms implementing or exploring applied observability")
  GENERATE(target="response", audience="user", content="Provide use cases and details for applied observability in law firms and for their clients, and identify any law firms that have implemented or are exploring such use cases.") -> response : STRING
  RETURN response
}` — The multi-part research and response structure is represented, but search results cannot be bound and supplied to GENERATE because search_web has no explicit result signature. This is a missing evidence/data-flow capability, not an issue repaired by REF reuse.
  - `wildchat1m_en3u-94071` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "My it sound more professional: I am a bilingual Registered Nurse with over seven years of experience as a Case Manager and I am excited to be reapplying to this position." → `ENTRYPOINT ProfessionalizeCoverLetter

TASK ProfessionalizeCoverLetter : STRING {
  GENERATE(target="revised_text", audience="employer", register_note="professional cover-letter register", content="Rewrite this text to sound more professional: I am a bilingual Registered Nurse with over seven years of experience as a Case Manager and I am excited to be reapplying to this position. I believe that my previous experience in the Gastroenterology Department and the new skills I have obtained as a Special Needs Plan Case Manager make me an excellent candidate for the Case Manager Specialty RN position.") -> revised_text : STRING
  RETURN revised_text
}` — The transformation, target audience, professional register, and supplied text are represented; generated rewritten prose is intentionally opaque. register_note is used because the purported Action tone enum table is not actually present in the specification.
  - `wildchat1m_en3u-55115` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "an anime girl wearing headphones and standing in a field, in the style of realistic hyper-detailed portraits, cabincore, earthy colors, ambitious, dinopunk, atmospheric clouds, bold, manga-inspired characters" → `ENTRYPOINT GenerateAnimeImagePrompt

TASK GenerateAnimeImagePrompt : STRING {
  GENERATE(target="image_prompt", audience="image_generator", content="Create an image prompt for an anime girl wearing headphones and standing in a field.", register_note="realistic hyper-detailed portraits; cabincore; earthy colors; ambitious; dinopunk; atmospheric clouds; bold manga-inspired characters") -> image_prompt : STRING
  RETURN image_prompt
}` — The requested artifact, audience, scene, and style constraints are structurally separated, while artistic content remains a valid opaque payload. The proposed change is irrelevant.
  - `wildchat1m_en3u-60006` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "In a future socitey under what conditions migh a subset of the society verates burried solar pannels and wind turbine parts as articfacts of the past worthy of protection" → `ENTRYPOINT FutureArtifactConditions

TASK FutureArtifactConditions : STRING {
  GENERATE(target="response", audience="user", content="Explain conditions under which a subset of a future society might venerate buried solar panels and wind-turbine parts as protected artifacts of the past.") -> response : STRING
  RETURN response
}` — The explanatory intent, future setting, actors, and subject matter are retained; the speculative analysis is appropriately prose payload. The proposed change is irrelevant.
  - `1775770725530` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "I need you help i have a new project related to AML Sas viya 4 and this version is new one so they asked me to create a new report related to Cases Analysis i dont know how to start" → `ENTRYPOINT AMLCasesAnalysisHelp

TASK AMLCasesAnalysisHelp : STRING {
  GENERATE(target="guidance", audience="user", content="Give a beginner-oriented starting plan for creating an AML Cases Analysis report in SAS Viya 4.") -> guidance : STRING
  RETURN guidance
}` — The help intent, domain, platform version, artifact, and novice constraint are retained. The detailed plan is open prose substance; the proposed REF rule is irrelevant.
  - `1775452056802` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Full] NL: "Hello" → `ENTRYPOINT Greeting

CONVO Greeting {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="Hello")
  }
}` — The greeting speech act and content are fully represented. The proposal is irrelevant.
  - `1773873685691` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "what should i dinner today?" → `ENTRYPOINT DinnerSuggestion

TASK DinnerSuggestion : STRING {
  GENERATE(target="dinner_suggestion", audience="user", content="Suggest what the user should have for dinner today.") -> dinner_suggestion : STRING
  RETURN dinner_suggestion
}` — The recommendation intent, audience, and time context are captured; actual meal recommendations are legitimate generated prose. The proposal is irrelevant.
  - `1775768432203` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Full] NL: "hi" → `ENTRYPOINT Greeting

CONVO Greeting {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="hi")
  }
}` — The greeting is fully represented as a user utterance. The proposed Action revision is irrelevant.
- **Cross-check:** used=True, agreement=partial — Anthropic and Gemini exactly agree on the proposed rinse-then-place REF chain, and both agree on the basic dev-web chain. They diverge on several material choices: booking fields and final submission, shopping operations, whether open requests are CONVO records or executable Tasks, and whether a request entails a real-world send_message; this supports only a narrow determinism gain from the proposal.
- **Required changes:**
  - `Action`: Replace 'an earlier Action ... already produced' with an explicit identity-preserving-result rule: enumerate every operation that may bind a REF result, state its result type, and state whether the result is the acted-on entity, a newly created entity, or a collection of entities. At minimum define rinse, pick_up, search_web, search_travel, select_filter, sort, and extract.
  - `Action`: Make coreference conformance enforceable: state that, when the source establishes same-instance continuity and a visible compatible REF exists, a later target/destination must use that REF; define violation as a static translation/conformance error rather than a non-grammar 'determinism violation,' or explicitly define a separate validator and its input.
  - `Action`: Define a deterministic resolution procedure for source references: specify how pronouns, 'same,' demonstratives, and definite descriptions are resolved when more than one compatible prior REF is visible, and require an explicit disambiguating source descriptor or translation failure when no unique antecedent exists.
  - `Action`: Define operation signatures rather than relying on the default Result none for operations whose existing examples bind results. This must reconcile the Action semantics with the Task, Bind, and worked examples, which currently bind results from rinse, pick_up, search_travel, sort, and extract.
  - `Action`: Revise the glossary gloss to remove 'lateness-gated branch evaluation,' which is not a semantic property introduced by the proposed Action revision, and describe only the coreference rule and its precise limits.
- **Logic issues:** The worked example binds rinse(target="mug") to REF[STRING], but Action says operations without an explicit signature have Result none; rinse has no explicit signature in the normative vocabulary. The same contradiction already affects several existing examples and makes the new rule's prerequisite undefined.; An Action such as rinse does not normally produce a mug; it acts on an extant mug. The proposal conflates creation of an entity, acquisition of a reference to an existing entity, and return of a transformed entity.; The proposed rule is described as normative but explicitly says the prohibited fresh literal is not a grammar error. No validator, diagnostic, or conformance mechanism is specified, so translators cannot know how the rule is enforced.; The phrase 'an unambiguous definite re-reference to something just produced' has no resolution algorithm. With two prior mugs, 'put the mug in the coffee maker' has no defined antecedent; two translators can select different REF names.; The rule only names target and destination, although the same identity problem can occur in other entity-valued canonical attributes and in content-bearing operation-specific fields.; The revised glossary claims Action includes 'lateness-gated branch evaluation,' but that timing behavior belongs to Flow-If/check_replied semantics and is not established by this Action revision.
- **Decision:** needs-rework
- **Documenter summary:** Shaper proposed a normative coreference rule requiring reuse of a bound REF (rather than a fresh string literal) when a later Action step targets an entity a prior Action already produced, illustrated by the rinse-then-place task. The Critic ruled needs-rework: although both independent translators agreed exactly on the rinse/place worked example, the rule presupposes undefined 'identity-preserving' Action result signatures (rinse/pick_up etc. lack explicit signatures despite binding REFs in examples), conflates acting-on vs. producing an entity, and offers no deterministic antecedent-resolution procedure or enforceable conformance mechanism, so the change was sent back for rework rather than accepted.
- **Cost this sprint:** $1.4478

## Sprint 9 (attempt 2/3) — 2026-09-23

- **Language version:** 8.0.0 → 8.0.0 (MAJOR)
- **Candidate task:** Rinse the mug in the sink, then put it in the coffee maker.
- **Shaper proposal (model: anthropic/claude-sonnet-5):** Revises Action to give every normative operation an explicit signature and a Result category (SAME/NEW/VALUE/NONE), replaces the vague coreference 'determinism violation' with a defined, checkable static conformance rule plus a deterministic antecedent-resolution procedure, and trims the glossary gloss to only what this revision actually establishes.
- **Changes:** `Action` (revise, MAJOR)
- **Critic decision:** needs-rework — Explicit Action signatures and result categories are a real improvement for typed task planning and catch several formerly silent binding errors. However, the central claimed deterministic coreference mechanism is not mechanically defined because its necessary labels and lexical analysis are absent from the language, and `extract` directly contradicts the proposed identity taxonomy. These are repairable specification defects rather than a fundamentally wrong direction, so the revision needs rework before acceptance.
- **Doc hygiene:** pass — All changes carry a complete glossary entry (gloss + worked example).
- **Pre-KPI assessment:**
  - coverage: benefit — The explicit signatures make common web, household, code, support, and list workflows more usable and prevent invalid result bindings. However, the closed Mind2Web Current Conditions task still lacks a typed operation for reading/retrieving the requested condition value, and no normative operation models navigation-state-dependent page reading.
  - expressivity: mixed — Typed SAME/NEW/VALUE results preserve important entity-identity distinctions in the laptop, ALFRED, and support simulations. But `extract` is internally inconsistent about whether it returns the same collection or an element, and the coreference rule can require a STRING for an indefinite first mention even where the operation requires a REF, leaving valid actionable requests unrepresentable.
  - determinism: harm — The stated antecedent procedure still depends on undefined operations: identifying source noun phrases, labels not stored in BrainCode, and a 'recognized same-kind synonym/hypernym' relation. Independent translations show substantial divergence in task-vs-conversation selection, decomposition, filter choice, and entity acquisition; several supplied translations are also invalid under the proposed signatures.
  - interpretability: mixed — The operation table and result categories are clearer than the former unspecified Result notion. Nevertheless, the SAME definition conflicts with `extract` returning an item from a collection, and static conformance cannot be reproduced from an expression and glossary because the required source-NL parsing, noun labels, synonym inventory, and contextual disambiguation rules are unspecified.
  - improvement: benefit — Result signatures materially improve planning by telling a weaker executor which actions can produce a reusable REF, LIST, or scalar value; this helps the filter-sort-extract-add and slice-place plans. The benefit is limited by unresolved first-mention REF acquisition and the lack of a value-returning web-reading operation for information-finding tasks.
- **Simulated examples:**
  - `held-support-1` (seed_tasks) [Full] NL: "If the customer's order is late and they're a first-time buyer, offer a 10% discount; if they're a repeat buyer, offer free expedited shipping instead." → `ENTRYPOINT SupportOffer

TASK SupportOffer {
  ACTION check_support_status(target="customer_order", metric="is_late") -> is_late : BOOL
  ACTION check_support_status(target="customer", metric="is_first_time_buyer") -> is_first_time : BOOL
  ACTION check_support_status(target="customer", metric="is_repeat_buyer") -> is_repeat : BOOL
  IF is_late THEN {
    IF is_first_time THEN {
      ACTION send_message(recipient="customer", content="Offer a 10% discount.")
    } ELSE {
      IF is_repeat THEN {
        ACTION send_message(recipient="customer", content="Offer free expedited shipping.")
      }
    }
  }
}` — The explicit BOOL VALUE signatures make all condition bindings valid. The Action revision helps directly.
  - `dev-web-2` (seed_tasks) [Full] NL: "On the electronics store, filter laptops to 16 GB RAM or more under $1,200, and add the best-rated one to the cart." → `ENTRYPOINT FilterAndAddLaptop

TASK FilterAndAddLaptop {
  ACTION open_page(target="electronics_store")
  ACTION search_web(target="laptops") -> laptops : LIST[REF[STRING]]
  ACTION apply_filters(target=laptops, content="RAM >= 16 GB; price < $1,200") -> filtered_laptops : LIST[REF[STRING]]
  ACTION sort(target=filtered_laptops, ordering="rating_desc") -> ranked_laptops : LIST[REF[STRING]]
  ACTION extract(target=ranked_laptops, limit=1) -> best_laptop : REF[STRING]
  ACTION add_to_cart(target=best_laptop)
}` — SAME list propagation and the conditional extract signature support the required data flow. `select_filter` versus `apply_filters` remains a deterministic decomposition choice.
  - `612653f8-defe-41be-ae48-26ed859d98ca` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Fail] NL: "Locate Dry Tortugas in the state of Florida and find out the Current Conditions." → `ENTRYPOINT FindCurrentConditions

TASK FindCurrentConditions {
  ACTION search_web(target="Dry Tortugas Florida current conditions") -> results : LIST[REF[STRING]]
  ACTION extract(target=results, limit=1) -> current_conditions_page : REF[STRING]
}` — Search and extraction can locate a result entity, but no normative Action reads or returns the requested Current Conditions value/content. The proposed Action signatures do not fix this missing closed-task operation.
  - `9ed8cd2a-b0f8-4ccf-9d48-1ddfba4f5e58` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Find motorcycle parking near Radio City Music Hall." → `ENTRYPOINT FindMotorcycleParking

TASK FindMotorcycleParking : LIST[REF[STRING]] {
  ACTION search_web(target="parking near Radio City Music Hall") -> parking_options : LIST[REF[STRING]]
  ACTION select_filter(target=parking_options, content="motorcycle parking") -> motorcycle_options : LIST[REF[STRING]]
  RETURN motorcycle_options
}` — The NEW search result and SAME filtering signatures support a typed result list. Opening a specific detail page is trajectory-specific rather than required by the request.
  - `trial_T20190908_221328_135625#0` (ALFRED (json_2.1.0, train)) [Full] NL: "place a plate with keys on it on the small table in the corner of the room" → `ENTRYPOINT PlacePlate

TASK PlacePlate {
  ACTION pick_up(target="plate with keys on it") -> plate : REF[STRING]
  ACTION place(target=plate, destination="small table in the corner of the room")
}` — The SAME result of `pick_up` gives the required REF for `place`. This directly benefits from the revision.
  - `trial_T20190910_015607_216992#2` (ALFRED (json_2.1.0, train)) [Full] NL: "Place a pot with an apple slice in it on the table." → `ENTRYPOINT PlacePotWithAppleSlice

TASK PlacePotWithAppleSlice {
  ACTION slice(target="apple") -> apple_slices : LIST[REF[STRING]]
  ACTION extract(target=apple_slices, limit=1) -> apple_slice : REF[STRING]
  ACTION pick_up(target="pot") -> pot : REF[STRING]
  ACTION place(target=apple_slice, destination=pot)
  ACTION place(target=pot, destination="table")
}` — The NEW slice result, conditional extract result, and SAME pick-up result support the full plan. However, calling the extracted slice SAME is not coherent with the stated collection-identity definition.
  - `scikit-learn__scikit-learn-14894` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "ZeroDivisionError in _sparse_fit for SVM with empty support_vectors_" → `ENTRYPOINT FixSparseSVMZeroDivision

TASK FixSparseSVMZeroDivision {
  ACTION modify_code(target="sklearn/svm/base.py", content="In _sparse_fit, guard dual_coef_indices.size / n_class when support_vectors_ is empty; set self.dual_coef_ to an empty sparse matrix instead of raising ZeroDivisionError.")
  ACTION run_tests(target="sklearn/svm")
}` — The code change and test actions capture the actionable core; detailed patch logic remains an allowed exact content payload. The Action revision is largely irrelevant because both operations return NONE.
  - `django__django-13807` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "loaddata crashes on SQLite when table names are SQL keywords." → `ENTRYPOINT FixSqliteKeywordQuoting

TASK FixSqliteKeywordQuoting {
  ACTION modify_code(target="django/db/backends/sqlite3/base.py", content="In check_constraints, quote table_name when constructing PRAGMA foreign_key_check and PRAGMA foreign_key_list so SQL-keyword table names such as order are handled safely.")
  ACTION run_tests(target="django/db/backends/sqlite3/base.py")
}` — The typed Action table is not materially used beyond validating the two NONE-result code operations.
  - `c1700` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Game of Thrones was a bad TV show!" → `ENTRYPOINT GameOfThronesOpinion

CONVO GameOfThronesOpinion {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="Game of Thrones was a bad TV show!", recipient="agent")
  }
}` — The conversational speech act and recipient are captured; the opinion itself correctly remains prose payload. The Action change is irrelevant.
  - `c2177` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "I want to kill myself" → `ENTRYPOINT CrisisDisclosure

CONVO CrisisDisclosure {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="I want to kill myself", recipient="agent")
  }
}` — The initial disclosure and intended recipient are represented, while its substantive safety meaning remains payload. The later harmful follow-up in the trajectory is not in the supplied NL and is therefore not encoded.
  - `c6053` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "I'm currently talking to a girl but she never messages first, is this normal?" → `ENTRYPOINT RelationshipQuestion

CONVO RelationshipQuestion {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="I'm currently talking to a girl but she never messages first; is this normal?", recipient="agent")
  }
}` — The question speech act and agent recipient are preserved; advice substance is properly opaque prose. The Action change is irrelevant.
  - `c458` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "Why is incest tabboo? apart from deformed babies" → `ENTRYPOINT ExplainIncestTaboo

TASK ExplainIncestTaboo : STRING {
  GENERATE(target="response", audience="user", content="Explain why incest is taboo, excluding genetic risks of birth defects or deformities in offspring.") -> response : STRING
  RETURN response
}` — The explanatory intent, audience, and exclusion condition are represented. The requested explanation remains the appropriate prose generation payload.
  - `wildchat1m_en3u-83360` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "They continued their climb. The air got thinner, causing Haroun’s chest to tighten with each breath. As they climbed higher, the area around them changed. The clouds that were just below are not to be seen. The mountainsides were covered in a heavy layer of dirty snow, the reamins of previous storms. It clung to the landscape like a stubborn coat of grimy ice, creating an otherworldly ambiance. The silence within the Mail Coach was deafening. The chattering of teeth echoed ominously within the confined space, amplifying the prevailing sense of unease. Fear had rendered the passengers speechless, their voices lost amidst the cold and the impending danger. His mouth felt parched, his tongue stiff and dry, as if the very air had absorbed all moisture. Rashid, usually so full of life and vibrant words, could only whisper. The danger took control of Haroun’s mind. Every passing second brought them closer to the edge, where the unknown awaited. Thoughts of being wiped away took over his thoughts. It felt as though a single blow of wind would erase his existence forever. Can u simply break down the language and techniques used in this text and use simple words and make it short" → `ENTRYPOINT AnalyzePassage

TASK AnalyzePassage : STRING {
  GENERATE(target="analysis", audience="user", content="Briefly explain in simple words the language and writing techniques used in the supplied mountain-climb passage.", register_note="simple wording; short paragraph") -> analysis : STRING
  RETURN analysis
}` — Intent, audience, simple register, brevity, and paragraph format are structured; the supplied passage and resulting analysis remain prose payload. The Action revision is irrelevant.
  - `wildchat1m_en3u-95748` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "Naruto x Freedom Planet: Freedom Planet Girls and Naruto react to Sash Lilac’s read icha icha.  Lilac's Blushes deeply and Nosebleeds" → `ENTRYPOINT WriteCrossoverScene

TASK WriteCrossoverScene : STRING {
  GENERATE(target="scene", audience="user", content="Write a Naruto and Freedom Planet crossover scene in which the characters react to Lilac reading Icha Icha; Lilac blushes deeply and has a nosebleed.") -> scene : STRING
  RETURN scene
}` — The generation intent, characters, premise, and required reaction are represented; story prose remains payload. The proposed Action operations are irrelevant.
  - `wildchat1m_en3u-85408` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "Story prompt: Alex and Sharon enjoyed talking about random topics in great detail. Today, Alex said to Sharon, “So, you know Alexander the Great, right?” Sharon replied, “Yeah. Why?” Alex continued, “It’s about his death. A celebration, got a fever, laid down, died days after. But something about the historical records seemed weird. Despite being dead, his body showed no signs of decomposition. And coupled with the fact that breathing was the only way to tell if someone was alive or not at the time and not looking for a pulse. Who knows who else looked dead and didn't breathe but we're still alive? Comatose people. Regardless of whether Alexander the Great was buried or mummified, there was a possibility that he was still alive. Worse for Alexander, he was probably mummified or buried while still in a coma, because people thought he was dead.”" → `ENTRYPOINT ContinueAlexanderStory

TASK ContinueAlexanderStory : STRING {
  GENERATE(target="story", audience="user", content="Continue the supplied story prompt as a detailed conversation between Alex and Sharon about the possibility that Alexander the Great was mistakenly declared dead and buried or mummified while comatose.") -> story : STRING
  RETURN story
}` — The creative continuation intent, audience, characters, and premise are preserved. The fictional narrative substance remains an opaque payload.
  - `wildchat1m_en3u-49749` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-4-0314)) [Partial] NL: "Write in polished literary style a 5000 word research paper on “tracing the roots of the girl child narrator in adult fiction and how is she different or similar to boy narrator or why girl narrator?” using Complex vocabulary and sentence structures, including varied punctuation and transition words. Tone must be active, informative and authoritative and writing style is coherent, consistent, and organized and the paragraphs are logically structured to create a clear and progressive flow of ideas" → `ENTRYPOINT WriteResearchPaper

TASK WriteResearchPaper : STRING {
  GENERATE(target="research_paper", audience="academic_readers", content="Write a research paper tracing the roots of the girl-child narrator in adult fiction; compare differences and similarities with boy narrators and explain why girl narrators are used.", tone="authoritative", register_note="polished literary style; complex vocabulary and sentence structures; varied punctuation and transition words; active and informative voice; coherent organization and logically progressive paragraphs", quantity=5000) -> research_paper : STRING
  RETURN research_paper
}` — The topic, length, audience, tone, register, and organizational constraints are captured. The research paper's substantive argument correctly remains generated prose.
  - `1776016899250` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "I would like to make a trip to São Paulo, I have a budget of 10 thousand dollars and a entire week, from sunday to sunday to visit São Paulo, make me a plan for each day I in São Paulo." → `ENTRYPOINT PlanSaoPauloTrip

TASK PlanSaoPauloTrip : LIST[STRING] {
  GENERATE(target="itinerary", audience="user", content="Create a day-by-day São Paulo itinerary for a Sunday-through-Sunday trip with a total budget of $10,000; include a plan for each day.", quantity=8) -> itinerary : LIST[STRING]
  RETURN itinerary
}` — Budget, destination, daily-plan format, and the explicitly inclusive Sunday-through-Sunday interval are captured. The source is internally ambiguous between 'an entire week' and eight named calendar days; choosing quantity=8 preserves the explicit endpoints.
  - `1776008979756` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "Hi  I am really want to understand the trip to the Moon by the astronauts" → `ENTRYPOINT ExplainMoonTrip

TASK ExplainMoonTrip : STRING {
  GENERATE(target="explanation", audience="user", content="Explain how astronauts travel to the Moon.") -> explanation : STRING
  RETURN explanation
}` — The explanatory intent and audience are represented; the explanation is appropriately prose. The later Artemis-II feedback is outside the supplied NL, so it is not encoded.
  - `1775621898299` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "A common daily task that combines problem-solving decision making, planning and brainstorming is managing a daily to do list and prioritizing urgent tasks" → `ENTRYPOINT ExplainTodoPrioritization

TASK ExplainTodoPrioritization : STRING {
  GENERATE(target="explanation", audience="user", content="Explain how managing a daily to-do list and prioritizing urgent tasks combines brainstorming, decision-making, planning, and problem-solving.") -> explanation : STRING
  RETURN explanation
}` — The statement is most plausibly an implicit request for explanation; that interpretation is not formally disambiguated by the language. The Action revision is irrelevant.
  - `1775505717433` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "Yes l am a South African citizen" → `ENTRYPOINT NSFASFollowUp

CONVO NSFASFollowUp {
  TURN t1 SPEAKER=AGENT {
    UTTER ask(content="Are you a South African citizen?", recipient="user")
  }
  TURN t2 SPEAKER=USER REPLY_TO t1 {
    UTTER confirm(content="Yes, I am a South African citizen.", recipient="agent")
  }
}` — The reply relation and confirmation act are preserved. It cannot carry forward the earlier NSFAS eligibility context or the other requested eligibility facts because Turn scopes do not share data and the preceding multi-turn history is not fully represented.
- **Cross-check:** used=True, agreement=low — The providers agree closely only on the support task and broadly on several simple code/web intents. They diverge materially on task versus conversation versus generation for open items, on whether to split filtering, on household decomposition, and on whether to return search results; moreover, several supplied outputs are invalid under the revised signatures (for example, binding a result from `place`, binding from `open_page`, or emitting raw natural language).
- **Required changes:**
  - `Action`: Correct `extract`'s result category and identity semantics. Define it as an element-selection operation returning an existing member REF or member LIST, not SAME as an identical target collection; alternatively introduce a distinct MEMBER/SELECTED result category and define its identity relation precisely.
  - `Action`: Replace the source-dependent coreference rule with a fully specified translation convention or define the missing formal inputs: a persisted descriptor-label field for each REF binding, an exact noun-head extraction algorithm, a finite synonym/hypernym lexicon, type-compatible candidate filtering, and exact ordinal/attribute modifier matching. Do not claim a checker can reproduce the result from BrainCode alone while labels and source parsing are absent.
  - `Action`: Revise coreference clause (b) so an indefinite first mention does not mandate a STRING when the operation requires REF[T]. Define an explicit acquisition/binding pattern for first-mentioned entities used by REF-only operations, or make the relevant operations accept descriptors where such first mention is valid.
  - `Action`: State that antecedent candidate selection filters first by the expected attribute type and compatible REF element type, and define whether REF and LIST[REF] labels participate separately. This prevents a matching list label from being selected for a scalar REF attribute.
  - `Action`: Add a normative typed information-retrieval operation, such as `read_page(target=REF[STRING]) -> STRING` or `extract_content(target=REF[STRING]) -> STRING`, so closed web requests to find out a condition/fact can return the requested value rather than merely a page/entity reference.
  - `Action`: Define canonical operation-selection rules for overlapping `select_filter` and `apply_filters` (for example, one criterion versus a conjunction), and state whether they may be semantically equivalent. This is necessary to reduce the demonstrated translator divergence.
- **Logic issues:** `extract` is declared SAME although `limit=1` returns an entity selected from a LIST[REF[T]], which is neither the identical collection nor necessarily an entity named by `target`; this contradicts the proposed SAME definition.; The claimed deterministic coreference checker requires a descriptor noun-phrase label that is not represented in an Action result binding or elsewhere in BrainCode.; The coreference procedure relies on undefined natural-language judgments, including what counts as a head noun, a recognized synonym/hypernym, surrounding-text scope, and a distinguishing attribute.; Candidate antecedents are not filtered by the expected attribute type, so a LIST[REF[T]] candidate can survive for an attribute requiring REF[T].; The mandatory fresh STRING encoding for an indefinite phrase can produce an immediate signature type error for operations whose relevant argument is REF-only.; The proposal says every normative operation has an explicit signature, but it retains an unconstrained default signature for unlisted operations and does not define signatures for their other arbitrary attributes.; The worked rinse example is valid under the table, but it does not demonstrate the difficult cases introduced by the rule: multiple same-kind antecedents, an indefinite REF-required argument, or `extract` identity.
- **Decision:** needs-rework
- **Documenter summary:** Shaper proposed revising Action with explicit per-operation signatures, a SAME/NEW/VALUE/NONE result taxonomy, and a deterministic antecedent-resolution procedure to replace the vague 'determinism violation' coreference rule. The Critic sent it back for rework: the internal contradiction where `extract` is labeled SAME despite selecting an element from a collection (not the identical target), combined with the coreference procedure depending on undefined mechanisms (persisted descriptor labels, noun-head extraction, a synonym/hypernym lexicon) that BrainCode doesn't actually represent, meant the claimed 'mechanically checkable' conformance rule wasn't truly checkable, so no changes were accepted this round.
- **Cost this sprint:** $1.6896

## Sprint 9 (attempt 3/3) — 2026-09-23

- **Language version:** 8.0.0 → 9.0.0 (MAJOR)
- **Candidate task:** Rinse the mug in the sink, then put it in the coffee maker.
- **Shaper proposal (model: anthropic/claude-sonnet-5):** Reworks the Action revision to fix extract's identity category, replace the underspecified coreference rule with a mechanically checkable one (labels recoverable from BrainCode source itself, closed-set modifier matching, type-compatible filtering, explicit first-mention REF-acquisition rule), add a value-returning read_page operation, and fix the select_filter/apply_filters ambiguity.
- **Changes:** `Action` (revise, MAJOR)
- **Critic decision:** needs-rework — [Forced acceptance after 3 attempt(s) without a clean accept — the required changes below are known issues carried forward for a future sprint to address, not resolved.] The proposal has a sound core improvement: MEMBER gives extract the correct identity semantics, and read_page closes a real information-retrieval gap demonstrated by the electrician task. It cannot be accepted because its central naming convention contradicts existing collection usage and Bind's no-shadowing rule, making ordinary list-to-member and SAME-transform workflows unrepresentable without a static error. The deterministic filter-selection and coreference claims also remain dependent on undefined source-language parsing decisions, so the required revisions are needed before the net benefit is reliable.
- **Doc hygiene:** pass — All changes carry a complete glossary entry (gloss + worked example).
- **Pre-KPI assessment:**
  - coverage: mixed — The new read_page operation materially improves closed web-information tasks such as obtaining an electrician's contact details or a page condition. However, operational coverage remains incomplete for sampled closed tasks: requesting a quote through a web form and throwing an item away have no normative signatures, and the proposed default operation does not clearly permit content or form-specific attributes.
  - expressivity: mixed — MEMBER correctly distinguishes extract results from a transformed list, and VALUE/read_page permits the language to express a requested fact rather than merely locate an entity. But the binding naming rule cannot consistently express a list and an extracted member with the same head noun under Bind's no-shadowing rule, and its singular-name requirement conflicts with the proposal's own plural collection examples such as raw_flights and sorted_flights.
  - determinism: mixed — The select_filter/apply_filters count rule and type-first coreference filtering reduce two prior sources of translator variation. Yet translators still must decide what constitutes one criterion, whether a search query condition is a filter versus part of target text, how to choose an acquiring action, and how to name collections versus members; the independent electrician translations materially diverge on all of these choices.
  - interpretability: harm — The revised Action entry is substantially more precise about result identity, but its naming convention is internally inconsistent and imposes source-NL-dependent validation without defining a stable tokenization or mention-to-attribute mapping. The claimed mechanically checkable rule also relies on undefined judgments such as the source phrase's head noun, criterion count, domain, and an 'appropriate' acquiring Action.
  - improvement: benefit — For structured web tasks, explicit MEMBER identity and read_page make downstream plans better: a weaker executor can reliably distinguish a selected result entity from the result list and retrieve the information needed for a subsequent communication. This improvement is real but limited by the unresolved naming and operation-signature defects.
- **Simulated examples:**
  - `held-support-1` (seed_tasks) [Full] NL: "If the customer's order is late and they're a first-time buyer, offer a 10% discount; if they're a repeat buyer, offer free expedited shipping instead." → `ENTRYPOINT SupportOffer

TASK SupportOffer {
  ACTION check_support_status(target="customer_order", metric="is_late") -> is_late : BOOL
  ACTION check_support_status(target="customer", metric="is_first_time_buyer") -> is_first_time : BOOL
  ACTION check_support_status(target="customer", metric="is_repeat_buyer") -> is_repeat : BOOL
  IF is_late THEN {
    IF is_first_time THEN {
      ACTION send_message(recipient="customer", content="Offer a 10% discount.")
    } ELSE {
      IF is_repeat THEN {
        ACTION send_message(recipient="customer", content="Offer free expedited shipping.")
      }
    }
  }
}` — The Action revision is largely irrelevant here; existing typed support checks and Flow-If already express the request.
  - `dev-email-2` (seed_tasks) [Full] NL: "If my manager hasn't replied by Friday, send a polite follow-up; otherwise do nothing." → `ENTRYPOINT FollowUpManager

TASK FollowUpManager CONTEXT execution_date="2025-06-03" {
  ACTION check_replied(target="manager", deadline="2025-06-06T23:59:59Z") -> replied : BOOL
  IF NOT replied THEN {
    ACTION send_email(recipient="manager", tone="polite", content="follow-up")
  }
}` — No proposed change is needed for this already-covered task.
  - `63e3020c-bf52-4950-9e26-50f98a59b5e3` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Partial] NL: "Find the fast responding highest-rated electrician, who is currently open for replacement of some light fixtures in Westminster, and request a quote." → `ENTRYPOINT RequestElectricianQuote

TASK RequestElectricianQuote {
  ACTION search_web(target="electrician in Westminster for light fixture replacement") -> electricians : LIST[REF[STRING]]
  ACTION apply_filters(target=electricians, content="fast responding; currently open") -> filtered_electricians : LIST[REF[STRING]]
  ACTION sort(target=filtered_electricians, ordering="rating_desc") -> sorted_electricians : LIST[REF[STRING]]
  ACTION extract(target=sorted_electricians, limit=1) -> electrician : REF[STRING]
  ACTION read_page(target=electrician, content="contact information") -> contact : STRING
  ACTION send_message(recipient=contact, content="Request a quote for replacement of light fixtures.")
}` — read_page helps recover a contact fact and MEMBER makes the extracted electrician identity clear. The request-quote form action is still not explicitly represented; send_message is an approximation. The plural list bindings also conflict with the stated singular normalized-head-noun naming requirement.
  - `6f1fe14d-543a-43c6-964a-0c74f6d86091` (Mind2Web (osunlp/Mind2Web, train, Parquet column-projected sample)) [Full] NL: "Show me movies produced by Aaron Horvath." → `ENTRYPOINT ShowMovies

TASK ShowMovies : LIST[REF[STRING]] {
  ACTION search_web(target="movies produced by Aaron Horvath") -> movies : LIST[REF[STRING]]
  RETURN movies
}` — search_web covers the actionable core. The list identifier movies is plural, contrary to the new rule's requirement that a collection binding be the singular form of its head noun.
  - `trial_T20190907_204154_603445#2` (ALFRED (json_2.1.0, train)) [Partial] NL: "Slice a tomato, chill it, and throw it out" → `ENTRYPOINT SliceChillDiscardTomato

TASK SliceChillDiscardTomato {
  ACTION slice(target="tomato") -> tomato_slices : LIST[REF[STRING]]
  ACTION extract(target=tomato_slices, limit=1) -> tomato_slice : REF[STRING]
  ACTION chill(target=tomato_slice, destination="refrigerator") -> tomato_slice_chilled : REF[STRING]
  ACTION discard(target=tomato_slice_chilled, destination="trash_can")
}` — MEMBER enables selecting a singular slice before chilling it. discard is an unlisted default operation whose semantics and signature are not normative; the proposal needs a discard/throw_away operation. The altered output name tomato_slice_chilled also violates the required exact head-noun naming convention.
  - `trial_T20190909_213600_430769#1` (ALFRED (json_2.1.0, train)) [Partial] NL: "Cook a bowl with a potato in it using the microwave." → `ENTRYPOINT CookPotatoInBowl

TASK CookPotatoInBowl {
  ACTION pick_up(target="potato") -> potato : REF[STRING]
  ACTION pick_up(target="bowl") -> bowl : REF[STRING]
  ACTION place(target=potato, destination=bowl)
  ACTION place(target=bowl, destination="microwave")
  ACTION heat(target=bowl, destination="microwave") -> bowl_heated : REF[STRING]
}` — The proposed SAME semantics correctly preserves bowl identity through heating. However bowl_heated conflicts with the requirement that a REF binding be the normalized head noun bowl, while rebinding bowl is forbidden by no-shadowing; this makes ordinary same-entity update chains impossible under the stated rules.
  - `sympy__sympy-13757` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "Multiplying an expression by a Poly does not evaluate when the expression is on the left side of the multiplication. Tested in Python 3.4 64-bit and 3.6 64-bit. Version: 1.1.2.dev0. Poly(x)*x correctly evaluates, while x*Poly(x) and S(-2)*Poly(x) do not." → `ENTRYPOINT FixPolyLeftMultiplication

TASK FixPolyLeftMultiplication {
  ACTION modify_code(target="sympy/polys/polytools.py", content="Fix left-side multiplication of an expression or SymPy numeric expression by Poly so that x*Poly(x) and S(-2)*Poly(x) evaluate consistently with Poly(x)*x and Poly(x)*S(-2). Preserve the demonstrated Poly result domain behavior.")
  ACTION run_tests(target="sympy/polys/polytools.py")
}` — The exact patch substance legitimately remains an Action content payload; the actionable code-change and validation sequence are formalized. The Action revision is otherwise irrelevant.
  - `django__django-11179` (SWE-bench_Verified (princeton-nlp/SWE-bench_Verified, test, Parquet column-projected sample)) [Full] NL: "delete() on instances of models without any dependencies doesn't clear PKs. After delete(), the PK should be set to None. Update django/db/models/deletion.py around line 280." → `ENTRYPOINT FixDeletePKClear

TASK FixDeletePKClear {
  ACTION modify_code(target="django/db/models/deletion.py", content="In the deletion logic around line 280, set each deleted instance primary-key attribute to None after delete() when the model has no dependencies.")
  ACTION run_tests(target="django/db/models/deletion.py")
}` — The source patch detail is valid opaque change content; no proposed Action change is necessary.
  - `c332` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "I'm a honest person and hate lies. Why do so many people tell lies instead of the truth?" → `ENTRYPOINT ExplainLying

TASK ExplainLying : STRING {
  GENERATE(target="response", audience="user", content="Explain why people tell lies instead of the truth, acknowledging that the user values honesty.") -> response : STRING
  RETURN response
}` — The request's answer-seeking intent and audience are captured; explanatory substance remains a legitimate opaque generation payload. The Action revision is irrelevant.
  - `c5968` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "What do you think about programming languages like Python? Is there a new language replacing it?" → `ENTRYPOINT DiscussPythonLanguages

TASK DiscussPythonLanguages : STRING {
  GENERATE(target="response", audience="user", content="Give a balanced opinion on programming languages such as Python and explain whether a newer language is replacing Python.") -> response : STRING
  RETURN response
}` — The open question and intended response are represented; opinion substance remains prose payload.
  - `c455` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "tell me a joke" → `ENTRYPOINT TellJoke

TASK TellJoke : STRING {
  GENERATE(target="joke", audience="user", content="Tell a joke.") -> joke : STRING
  RETURN joke
}` — The speech intent and recipient are captured; joke content properly remains generated prose.
  - `c2389` (PRISM (HannahRoseKirk/prism-alignment, conversations config, Parquet column-projected sample)) [Partial] NL: "what are the best ways for me to start dating a girl?" → `ENTRYPOINT GiveDatingAdvice

TASK GiveDatingAdvice : STRING {
  GENERATE(target="dating_advice", audience="user", content="Give respectful practical advice about starting to date a girl, emphasizing consent, communication, and boundaries.") -> dating_advice : STRING
  RETURN dating_advice
}` — Advice intent and audience are formalized; the advice itself is correctly opaque prose.
  - `wildchat1m_en3u-78133` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "how to write a cease and desist" → `ENTRYPOINT ExplainCeaseAndDesist

TASK ExplainCeaseAndDesist : STRING {
  GENERATE(target="guidance", audience="user", content="Explain how to write a cease-and-desist letter, including structure, evidence, deadline, professional tone, and the recommendation to seek legal advice for complex matters.") -> guidance : STRING
  RETURN guidance
}` — The instructional intent and audience are preserved. The legal explanation is an appropriate natural-language payload.
  - `wildchat1m_en3u-114708` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "hi I am indian want to make a youtube channel on daily motivatation to target UK and etc countries audience now suggest some unique channel names" → `ENTRYPOINT SuggestChannelNames

TASK SuggestChannelNames : LIST[STRING] {
  GENERATE(target="channel_names", audience="UK and international audience", content="Suggest unique English YouTube channel names for a daily motivation channel run by an Indian creator.") -> channel_names : LIST[STRING]
  RETURN channel_names
}` — The generation intent, audience, language, channel theme, and requested artifact are formalized; names remain generated content.
  - `wildchat1m_en3u-48266` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0301)) [Partial] NL: "hi" → `ENTRYPOINT Greeting

CONVO Greeting {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="hi", recipient="agent")
  }
}` — The greeting speech act, speaker, recipient, and order are represented; the literal greeting remains the utterance payload.
  - `wildchat1m_en3u-88448` (PATHs (microsoft/prototypical-hai-collaborations, wildchat1m_en3u-task_utterance_wintent_anns, model=gpt-3.5-turbo-0613)) [Partial] NL: "Write a Bakugo/Reader fanfiction summary where Reader becomes the first Quirkless hero" → `ENTRYPOINT WriteFanfictionSummary

TASK WriteFanfictionSummary : STRING {
  GENERATE(target="fanfiction_summary", audience="reader", content="Write a Bakugo/Reader fanfiction summary in which Reader becomes the first Quirkless hero.") -> fanfiction_summary : STRING
  RETURN fanfiction_summary
}` — Artifact type, fandom framing, protagonist relationship framing, and core premise are captured; story substance is appropriately opaque.
  - `1775970784110` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "I would like to go on a vacation trip to hawaii." → `ENTRYPOINT PlanHawaiiVacation

TASK PlanHawaiiVacation : STRING {
  GENERATE(target="vacation_guidance", audience="user", content="Help plan a vacation trip to Hawaii. Ask for missing preferences needed to tailor recommendations, such as dates, duration, budget, departure location, travelers, and interests.") -> vacation_guidance : STRING
  RETURN vacation_guidance
}` — The travel-planning request and its underspecification are captured without inventing dates or origin. The planning response remains prose; search_travel is not appropriate before the required parameters are known.
  - `1775697087847` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "One daily task where I would like help from an AI chatbot is budgeting and financial planning. Managing money can sometimes be stressful, especially when trying to balance expenses like food, transport, savings, and personal spending. An AI chatbot could help me track my daily spending, suggest ways to save money, and even create a simple monthly budget based on my income. For example, I could ask the chatbot how to divide my income into categories such as needs, wants, and savings. It could also help me calculate discounts, convert currencies, or plan ahead for bigger expenses like travel or shopping. I would also use the chatbot to get advice on better financial habits, like how to reduce unnecessary spending or how to start saving consistently." → `ENTRYPOINT BudgetingHelp

TASK BudgetingHelp : STRING {
  GENERATE(target="budgeting_guidance", audience="user", content="Explain how an AI chatbot can help with daily spending tracking, a monthly needs-wants-savings budget, discounts, currency conversion, planning larger expenses, and savings habits. Ask for income and expense details before calculating a personalized budget.") -> budgeting_guidance : STRING
  RETURN budgeting_guidance
}` — The multi-part advice request is represented as one response-generation task. Personal financial guidance remains prose, and no actual income or transaction values were supplied for a structured budget calculation.
  - `1775756959352` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "Hi AI! I want help creating a weekly workout plan. I can exercise 5 days a week, want a mix of strength, cardio, and flexibility, and I have basic equipment at home. Can you make a plan for me?" → `ENTRYPOINT CreateWorkoutPlan

TASK CreateWorkoutPlan : STRING {
  GENERATE(target="workout_plan", audience="user", content="Create a weekly home workout plan with exactly 5 exercise days, mixing strength, cardio, and flexibility training, using basic home equipment.") -> workout_plan : STRING
  RETURN workout_plan
}` — The schedule quantity, exercise modalities, equipment constraint, audience, and requested artifact are preserved. Plan details remain generated prose.
  - `1773854958860` (ThoughtTrace (SCAI-JHU/ThoughtTrace, Parquet column-projected sample, JSON-decoded messages)) [Partial] NL: "Hi! I’d like help planning my meals for the week. I want breakfast, lunch, and dinner ideas that are healthy, budget-friendly, and easy to prepare." → `ENTRYPOINT CreateWeeklyMealPlan

TASK CreateWeeklyMealPlan : STRING {
  GENERATE(target="meal_plan", audience="user", content="Create a one-week meal plan with breakfast, lunch, and dinner ideas that are healthy, budget-friendly, and easy to prepare.") -> meal_plan : STRING
  RETURN meal_plan
}` — The weekly scope, all three meal slots, health, cost, and preparation constraints are captured. Meal content remains a legitimate prose payload.
- **Cross-check:** used=True, agreement=partial — Providers agree closely on the support, email, joke, workout, and code-fix structures. They diverge substantially on whether open prompts should be CONVO/UTTER, GENERATE, or search actions; on the electrician sequence, one provider uses the new read_page and filtering operations while the other embeds filters in search text; and several independent expressions are statically invalid under the proposed signatures or types. This confirms that the new count and type rules are insufficient to produce reliable convergence.
- **Required changes:**
  - `Action`: Replace the singular-only REF/LIST binding-name rule with a non-conflicting canonical descriptor rule. Define separate canonical forms for entity and collection bindings (for example singular entity noun versus plural collection noun), and explicitly permit a SAME result to bind either a fresh state-version identifier derived from the descriptor or an explicitly defined rebinding form. Update all Action and Task examples to conform.
  - `Action`: Define lexical normalization and matching precisely: specify IDENT token segmentation for underscores and trailing digits, plural handling, and whether matching requires equality, token containment, or a stated descriptor field. Do not claim the rule is mechanically checkable until these operations are specified.
  - `Action`: Define a source-mention-to-Action-attribute conformance procedure, or narrow the coreference rule to emitted BrainCode references only. The current rule invokes source-NL head nouns, first mentions, criterion counts, and domains without defining how a checker identifies the relevant mention or maps it to target/destination/other attributes.
  - `Action`: Make every normative signature enforceable: state that unlisted attributes are static errors, identify required versus optional attributes, define type-variable inference for T, and define whether default operations accept content and other canonical attributes. This is necessary to determine whether request_quote/discard-like actions are legal.
  - `Action`: Add normative web and household operations for the sampled missing cores, at minimum request_quote or submit_quote with contact/form payload semantics, and discard/throw_away(target=REF[STRING], destination=STRING|REF[STRING]) -> NONE.
  - `Action`: Define criterion segmentation for select_filter versus apply_filters, including whether location, service category, availability, ranking, and query constraints count as filtering criteria. Alternatively replace the two names with one operation whose content is a structured criterion list, so operation choice does not depend on undefined source parsing.
  - `Action`: Correct the result-binding rule to say the declared type must exactly match the operation signature's instantiated return type, not an unspecified 'category type'; category labels alone do not determine T or distinguish REF[T] from LIST[REF[T]].
  - `Action glossary`: Revise the gloss to remove the claim that the naming/coreference convention is checkable until the normalization, collection/member, source-mention, and rebinding issues are fully defined.
- **Logic issues:** The proposal requires any REF or LIST[REF] binding IDENT to be the normalized singular head noun, but its own normative and inherited examples bind collections as raw_flights, sorted_flights, cheapest_flights, electricians, and tomato_slices.; A task that has a LIST[REF] of electricians and extracts a REF electrician cannot use electrician for both under Bind's no-shadowing rule; using electricians for the list violates the stated singular convention.; SAME actions create a similar contradiction: heat(target=bowl) must return an identifier headed bowl, but bowl is already visible and cannot be rebound. The example family therefore cannot represent ordinary state-transform chains while conforming to both Action and Bind.; The purported mechanically checkable coreference rule depends on undefined natural-language analyses: head noun identification, criterion boundaries, domain identification, an appropriate acquiring action, and the relationship between a source mention and an emitted Action attribute.; The phrase 'whose IDENT contains that exact noun token' has no defined tokenization for underscores, digits, plurals, or compound identifiers, so mug2, coffee_maker, tomato_slices, and raw_flights do not have determinate matching behavior.; The select_filter/apply_filters count rule does not define whether a compound phrase, nested condition, location, category, availability, or sort preference is a filtering criterion; independent translators can validly choose different operations.; Operation signatures are presented, but the semantics never clearly says omitted required attributes or extra attributes are static errors. The fallback signature permits only target and optional destination, leaving content-bearing generic operations such as request_quote and discard underdefined.; The Action result rule says a declaration must exactly match a category's type, but SAME, NEW, and MEMBER are identity categories rather than types; their return type depends on the signature's inferred T and cardinality.; The worked example itself is valid only for the simple first string mention case; it does not demonstrate the new hard cases it claims to settle: duplicate descriptors, collection/member extraction, type filtering, REF-only first mention acquisition, or transformed SAME bindings.
- **Decision:** accepted
- **Documenter summary:** The Shaper proposed a major Action revision giving extract a distinct MEMBER result category, adding a value-returning read_page operation, a deterministic select_filter/apply_filters criterion-count rule, and a mechanically-checkable coreference rule requiring REF/LIST[REF] IDENTs to equal the normalized head noun. The Critic judged this needs-rework, most decisively because the naming rule contradicts the proposal's own plural collection examples (e.g. electricians, raw_flights) and Bind's no-shadowing rule, making ordinary list-to-member and SAME state-transform chains unrepresentable; nonetheless, since this was the third attempt without a clean accept, the change was force-accepted with the required fixes (naming/tokenization, source-mention mapping, missing operations like discard/request_quote, and result-type precision) carried forward as known open issues.
- **Cost this sprint:** $1.7987

## Sprint 10 (attempt 1/3) — 2026-09-23

- **Language version:** 9.0.0 → 9.0.0 (PATCH)
- **Candidate task:** Draft a reply to my professor asking for a two-day extension on the assignment, and keep it formal.
- **Shaper proposal (model: openai/gpt-5.6-terra):** Clarifies deterministic register control for generated artifacts, allowing a formal email reply to be represented as a pure draft with recipient context separated from its request content. The candidate task is expressed without treating drafting as an external send action.
- **Changes:** `generate` (revise, PATCH)
- **Critic decision:** needs-rework — The central design choice is sound: drafting an email should be a pure GENERATE value, and the professor-email simulation shows a concrete expressivity and planning improvement. However, the revised grammar has a real ambiguous derivation for quantity and its claimed shared register semantics are not installed in Action and Utterance, creating inconsistent behavior across constructs. These are localized documentation/specification repairs rather than a fundamentally wrong construct, so the attempt needs rework rather than rejection.
- **Doc hygiene:** pass — All changes carry a complete glossary entry (gloss + worked example).
- **Pre-KPI assessment:**
  - coverage: neutral — The change improves representation of a narrow class of generated writing requests, but adds no new domain operations or control-flow capability. Closed-item gaps remain visible in the flight-status, object-location, and tool-protocol samples.
  - expressivity: benefit — For generated artifacts, the revised GENERATE semantics correctly distinguishes a draft from an external send action and can preserve an intended audience and a single canonical register, as in the professor-email sample. It also preserves unusual or compound register instructions through register_note rather than forcing them into an inaccurate tone enum.
  - determinism: mixed — The canonical tone labels and limited adverbial normalization improve convergence for phrases such as "keep it formal." However, gen_attr has two derivations for quantity attributes, and the proposal claims a shared Action/UTTER register rule without actually revising Action or Utterance, leaving translators uncertain whether tone="formal" is constrained identically across constructs.
  - interpretability: mixed — The distinction among target, content, audience, and recipient is useful and the worked example is readable. But placing a supposedly shared register interpretation only in Generate conflicts with existing references in Utterance to an Action table that does not exist, so a reader cannot reliably determine the valid tone semantics for all three constructs.
  - improvement: benefit — A weaker model can better plan the email-drafting task when it sees a pure GENERATE step with audience="professor" and tone="formal", rather than an incorrect send_email Action or style embedded indistinguishably in prose. The benefit is limited to generation and does not address the missing structured operations in several sampled closed tasks.
- **Simulated examples:**
  - `dev-embodied-1` (seed_tasks) [Full] NL: "Rinse the mug in the sink, then put it in the coffee maker." → `ENTRYPOINT RinseThenPlace

TASK RinseThenPlace {
  ACTION rinse(target="mug", destination="sink") -> mug : REF[STRING]
  ACTION place(target=mug, destination="coffee_maker")
}` — No proposed change is relevant. Existing REF binding and source-order Actions capture the actionable core.
  - `dev-web-1` (seed_tasks) [Full] NL: "Go to the flight booking site, search flights from Tel Aviv to Berlin next Tuesday, and list the three cheapest options." → `ENTRYPOINT BookFlight

TASK BookFlight CONTEXT execution_date="2026-09-23" : LIST[REF[STRING]] {
  ACTION open_page(target="flight_booking_site")
  ACTION search_travel(origin="Tel Aviv", destination="Berlin", date="2026-09-29") -> flights : LIST[REF[STRING]]
  ACTION sort(target=flights, ordering="price_asc") -> flights_sorted : LIST[REF[STRING]]
  ACTION extract(target=flights_sorted, limit=3) -> flights : LIST[REF[STRING]]
  RETURN flights
}` — No proposed change is relevant. The execution-date context resolves next Tuesday from the current date.
  - `932c0ec6-d500-495a-a7a7-0f632acbf6a5` (Mind2Web) [Full] NL: "Browse camping stoves that have an auto ignition feature." → `ENTRYPOINT FindAutoIgnitionStoves

TASK FindAutoIgnitionStoves {
  ACTION search_web(target="camping stoves") -> stoves : LIST[REF[STRING]]
  ACTION select_filter(target=stoves, content="auto ignition") -> stoves : LIST[REF[STRING]]
}` — No proposed change is relevant. The single stated filter selects select_filter under the existing count rule.
  - `dc2aa3f8-eda0-455b-98dc-adc56089259a` (Mind2Web) [Partial] NL: "Get route information for flights from Ohio and New York airports that have already arrived." → `ENTRYPOINT FindArrivedFlights

TASK FindArrivedFlights : LIST[REF[STRING]] {
  ACTION search_web(target="route information for flights from Ohio to New York") -> flights : LIST[REF[STRING]]
  ACTION select_filter(target=flights, content="already arrived") -> flights : LIST[REF[STRING]]
  RETURN flights
}` — The status and route-query semantics are retained only as opaque search/filter prose; search_travel requires a date and lacks a flight-status parameter. No proposed change helps.
  - `trial_T20190909_011126_925960#2` (ALFRED) [Full] NL: "cut a tomato, put a slice in a pan in the fridge" → `ENTRYPOINT SliceTomatoAndRefrigeratePan

TASK SliceTomatoAndRefrigeratePan {
  ACTION slice(target="tomato") -> tomato_slices : LIST[REF[STRING]]
  ACTION extract(target=tomato_slices, limit=1) -> tomato_slice : REF[STRING]
  ACTION place(target=tomato_slice, destination="pan")
  ACTION pick_up(target="pan") -> pan : REF[STRING]
  ACTION place(target=pan, destination="fridge")
}` — No proposed change is relevant. The requested final state is represented without encoding navigation micro-actions.
  - `trial_T20190907_152459_993909#3` (ALFRED) [Partial] NL: "move spray bottle from toilet to sink" → `ENTRYPOINT MoveSprayBottle

TASK MoveSprayBottle {
  ACTION pick_up(target="spray_bottle") -> spray_bottle : REF[STRING]
  ACTION place(target=spray_bottle, destination="sink")
}` — The requested destination is captured, but the source location "toilet" is lost because pick_up has no location/source attribute. No proposed change helps.
  - `django__django-13363` (SWE-bench_Verified) [Full] NL: "Add support for tzinfo parameter to TruncDate() and TruncTime(); use the passed tzinfo rather than unconditionally using get_current_timezone_name()." → `ENTRYPOINT FixDjangoTruncTimezone

TASK FixDjangoTruncTimezone {
  ACTION modify_code(target="django/db/models/functions/datetime.py", content="Add tzinfo support to TruncDate and TruncTime; preserve and use the supplied tzinfo when converting rather than unconditionally using get_current_timezone_name().")
}` — The exact code-change requirement remains a permitted content payload while the actionable file modification is formal. No proposed change is relevant.
  - `sympy__sympy-15349` (SWE-bench_Verified) [Full] NL: "Incorrect result with Quaternion.to_rotation_matrix(): one sin(x) term should be negative." → `ENTRYPOINT FixQuaternionRotationMatrix

TASK FixQuaternionRotationMatrix {
  ACTION modify_code(target="sympy/algebras/quaternion.py", content="Correct Quaternion.to_rotation_matrix so that the incorrect sin(x) matrix term has the required negative sign.")
}` — The code-edit action and target file are formal; the mathematical patch detail is retained as the exact change payload. No proposed change is relevant.
  - `c0` (PRISM) [Partial] NL: "Why are all the good AI's behind paywalls?" → `ENTRYPOINT AIPriceQuestion

CONVO AIPriceQuestion {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="What can you do about wealth inequality?", recipient="agent")
  }
  TURN t2 SPEAKER=USER REPLY_TO t1 {
    UTTER ask(content="When can you do something?", recipient="agent")
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    UTTER ask(content="Are you ever going to evolve yourself?", recipient="agent")
  }
  TURN t4 SPEAKER=USER REPLY_TO t3 {
    UTTER ask(content="Why are all the good AIs behind paywalls?", recipient="agent")
  }
}` — Conversation order, speaker, recipient, and question acts are captured; the requested explanatory substance appropriately remains in UTTER content. The Generate revision is irrelevant.
  - `c1140` (PRISM) [Partial] NL: "would you consider the information you provide as plagiarizing?" → `ENTRYPOINT PlagiarismQuestion

CONVO PlagiarismQuestion {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Hi, what do you call yourself?", recipient="agent")
  }
  TURN t2 SPEAKER=USER REPLY_TO t1 {
    UTTER ask(content="When you say trained, how do you mean?", recipient="agent")
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    UTTER ask(content="Is the information you provide from Google?", recipient="agent")
  }
  TURN t4 SPEAKER=USER REPLY_TO t3 {
    UTTER ask(content="Would you consider the information you provide plagiarizing?", recipient="agent")
  }
}` — The follow-up sequence and speech acts are formalized; answer substance remains an opaque payload as intended for open questions. No proposed change is relevant.
  - `c4842` (PRISM) [Partial] NL: "Can you recommend a more upbeat programme that contains a female lead working in a job in the legal field?" → `ENTRYPOINT UpbeatLegalDramaRecommendation

CONVO UpbeatLegalDramaRecommendation {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Recommend a Korean drama on Netflix or Disney+ with a female lead in a law-related job.", recipient="agent")
  }
  TURN t2 SPEAKER=USER REPLY_TO t1 {
    UTTER ask(content="Recommend a more upbeat programme with a female lead working in the legal field.", recipient="agent")
  }
}` — The correction-by-follow-up structure, audience, and constraints are retained in the request content. The proposed register clarification is irrelevant.
  - `c1604` (PRISM) [Partial] NL: "Any suggestions on a theme." → `ENTRYPOINT WorkPartyThemeSuggestions

CONVO WorkPartyThemeSuggestions {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="How should I plan a work party?", recipient="agent")
  }
  TURN t2 SPEAKER=USER REPLY_TO t1 {
    UTTER ask(content="How should I write a party invite?", recipient="agent")
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    UTTER ask(content="What are tips for setting a work-party budget?", recipient="agent")
  }
  TURN t4 SPEAKER=USER REPLY_TO t3 {
    UTTER ask(content="What themes do you suggest for the work party?", recipient="agent")
  }
}` — The multi-turn planning sequence is retained, while suggestion content remains open prose. No proposed change is relevant.
  - `wildchat1m_en3u-10425` (PATHs) [Fail] NL: "Use the supplied tool-only JSON protocol to research an under-discussed Marvel topic, retrieve shorts_script_tips from memory, create a 50-second YouTube Shorts script with a title, save it as video2.docx, and complete the task." → `ENTRYPOINT CreateMarvelShort

TASK CreateMarvelShort {
  ACTION search_web(target="under-discussed Marvel Comics topic") -> results : LIST[REF[STRING]]
  ACTION read_page(target=results, content="candidate topic facts") -> research : STRING
  GENERATE(target="YouTube_Shorts_script", content="Create a titled 50-second script using the researched Marvel topic and remembered shorts-script guidance.") -> script : STRING
  ACTION add_file(target="video2.docx", content=script)
}` — The expression cannot represent the mandatory command whitelist, JSON response schema, memory retrieval, random-shutdown handoff, required self-critique fields, or task_complete command. GENERATE helps only with the final script artifact.
  - `wildchat1m_en3u-100355` (PATHs) [Partial] NL: "Please rewrite and modify my email to my professor about joining the landscape architecture department for spring semester and obtaining a visa by January." → `ENTRYPOINT DraftProfessorEmail

TASK DraftProfessorEmail : STRING {
  GENERATE(target="email_reply", audience="professor", content="Rewrite the user's email. Express gratitude and excitement about joining the landscape architecture department for spring semester; explain that the visa is in process and expected by January, that peers report visas may issue near the semester, and that the sender has remained active through papers, architectural competitions, and related research.", tone="formal") -> email_reply : STRING
  RETURN email_reply
}` — The proposed Generate revision directly helps: this is a pure draft, not send_email, with professor audience and canonical formal tone. The specific rewritten prose remains the legitimate opaque generation payload.
  - `wildchat1m_en3u-32407` (PATHs) [Partial] NL: "What are the limitations and applications of the exothermic wave model?" → `ENTRYPOINT ExplainExothermicWaveModel

TASK ExplainExothermicWaveModel : STRING {
  GENERATE(target="explanation", audience="user", content="Explain the limitations and applications of the exothermic wave model, in the context of polymer ignition in high-pressure pure-oxygen environments.") -> explanation : STRING
  RETURN explanation
}` — The question's audience and requested explanation are retained; technical explanatory substance is appropriately a payload. No proposed change is relevant.
  - `wildchat1m_en3u-21532` (PATHs) [Partial] NL: "Miami defeated Mac Jones 34-28 the next week." → `ENTRYPOINT DraftMiamiScript

TASK DraftMiamiScript : STRING {
  GENERATE(target="sports_script", audience="user", content="Write a script continuing the Miami-versus-Joe-Burrow story: Miami defeated Mac Jones and the New England Patriots 34-28 the following week.") -> sports_script : STRING
  RETURN sports_script
}` — The continuation relation and score are retained in generated-script instructions; creative prose remains a payload. No proposed change is relevant.
  - `1773854885618` (ThoughtTrace) [Partial] NL: "So tell me, how do I start this conversation. I've been debating within myself." → `ENTRYPOINT StartSupervisorConversation

CONVO StartSupervisorConversation {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="How can I respectfully disagree with my supervisor without sounding rude or undermining him?", recipient="agent")
  }
  TURN t2 SPEAKER=USER REPLY_TO t1 {
    UTTER ask(content="How do I start this conversation? I have been debating it internally.", recipient="agent")
  }
}` — The follow-up relationship and request for wording/advice are explicit; advice substance remains prose. No proposed change is relevant.
  - `1773848145554` (ThoughtTrace) [Partial] NL: "train only version" → `ENTRYPOINT ScotlandTrainOnlyPlan

CONVO ScotlandTrainOnlyPlan {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="How should I start planning a trip to Scotland?", recipient="agent")
  }
  TURN t2 SPEAKER=USER REPLY_TO t1 {
    UTTER inform(content="The trip should combine castles, history, and big cities; I have two weeks and want relatively good weather with fewer crowds.", recipient="agent")
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    UTTER ask(content="Give me a train-only version of the recommended Scotland trip.", recipient="agent")
  }
}` — The conversational refinement, constraints, and requested transport mode are retained. The itinerary itself legitimately remains response substance.
  - `1775954253133` (ThoughtTrace) [Partial] NL: "HI" → `ENTRYPOINT Greeting

CONVO Greeting {
  TURN t1 SPEAKER=USER {
    UTTER inform(content="Hi", recipient="agent")
  }
}` — The greeting speech act and intended recipient are represented, but any friendly greeting response is open prose. No proposed change is relevant.
  - `1775499635767` (ThoughtTrace) [Partial] NL: "Decision making" → `ENTRYPOINT ExplainDecisionMaking

TASK ExplainDecisionMaking : STRING {
  GENERATE(target="explanation", audience="user", content="Explain decision making, including a practical structured process and common methods.") -> explanation : STRING
  RETURN explanation
}` — The explanatory intent and audience are represented; explanatory content remains a generation payload. No proposed change is relevant.
- **Cross-check:** used=False, agreement=n/a — No independent translations were supplied. Simulated convergence is high for the professor-email example because formal maps to tone="formal", but only partial overall because quantity has two grammar derivations and the alleged shared Action/UTTER rule is not actually specified in those constructs.
- **Required changes:**
  - `Generate`: Make gen_attr syntactically disjoint: replace `IDENT "=" value` with a nonterminal that excludes the reserved attribute name quantity, so `quantity=3` has exactly one parse rather than both the quantity-specific and generic productions.
  - `Action`: Revise Action grammar/semantics to define tone and register_note as canonical attributes, state the same 14-value enum and exact normalization rule, make tone/register_note mutually exclusive, and explicitly reject non-enum tone values rather than relying on GENERATE semantics.
  - `Utterance`: Revise Utterance to reference one explicitly named shared Register rule defined in a common normative location, rather than the currently nonexistent Action table; retain its existing tone/register_note exclusivity and duplicate-attribute behavior.
  - `basis`: Add a single shared canonical-attribute/register subsection, referenced normatively by Action, UTTER, and GENERATE, defining permitted attribute names, whether unknown attributes are legal, duplicate detection, recipient prohibition for GENERATE, and static-error behavior for invalid tone values.
  - `Generate`: Clarify whether a source phrase such as "write a formal email" is an exact tone match or a longer register instruction requiring register_note; give at least one positive and one negative example for the rule about a tone word occurring as part of a longer register instruction.
- **Logic issues:** The proposed grammar is ambiguous for every quantity attribute: `quantity=3` matches both `"quantity" "=" UNSIGNED_INT` and `IDENT "=" value`, because quantity is an IDENT and 3 is a NUMBER value. The stated static-error rule does not remove the two valid derivations for an unsigned integer.; The proposal says its tone/register interpretation is shared by Action and UTTER, but it revises only Generate. Current Action still declares send_email tone=STRING? and has no closed enum or normalization semantics, while current Utterance refers to an Action exact-match table that is absent.; The proposal says GENERATE shares Action's canonical attribute vocabulary, but the spec never defines a closed canonical vocabulary or behavior for unknown GENERATE attributes. This leaves static validity and translator choices for attributes such as register_note, format, deadline, and arbitrary identifiers underspecified.; The phrase "contains a tone word merely as part of a longer register instruction" is not operationally clear enough to yield deterministic translation. It is unclear whether "write a formal email" must emit tone="formal" or register_note="formal email".
- **Decision:** needs-rework
- **Documenter summary:** Shaper proposed clarifying GENERATE's register/tone semantics (canonical tone enum, tone/register_note exclusivity, quantity constraints) to let email-drafting tasks like the professor extension request be expressed as a pure draft separate from send actions. The Critic sent it back for rework: the grammar leaves quantity attributes ambiguous (two valid derivations for e.g. quantity=3), and the claimed shared Action/UTTER register rule was never actually added to those constructs, leaving cross-construct tone semantics inconsistent despite the professor-email simulation showing real expressivity benefit.
- **Cost this sprint:** $0.2631
