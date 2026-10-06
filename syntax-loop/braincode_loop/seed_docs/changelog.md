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
