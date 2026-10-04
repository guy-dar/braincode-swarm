# Compact atomic-group proposal

Only this suggestion folder is edited. The original reference release is unchanged. The candidate glossary has **661 records versus 687**: 34 leaf rows and one empty category rule removed, nine supporting records added. Five open groups use examples and sparse aliases; two registered groups retain 13 identity definitions. Translators can propose new groups with consuming signatures as glossary changes, without editing the spec.

The combined required specification and glossary is now smaller than the original for every choice of views. No registered definitions have been moved outside that input. Spec-only size still includes the cost of the new mechanism; the reduction comes from the package as a whole.

| File | Original bytes | Previous suggestion | Current bytes | vs original |
|---|---:|---:|---:|---:|
| language-spec.md | 37,701 | 51,352 | 40,529 | +7.5% |
| language-spec.compact.md | 34,197 | 46,948 | 39,273 | +14.8% |
| glossary.md | 139,055 | 144,612 | 132,426 | -4.8% |
| glossary.jsonl | 260,970 | 261,078 | 249,938 | -4.2% |

| Required input pair | Original bytes | Current bytes | Change |
|---|---:|---:|---:|
| full readable | 176,756 | 172,955 | -2.2% |
| compact readable | 173,252 | 171,699 | -0.9% |
| full machine | 298,671 | 290,467 | -2.7% |
| compact machine | 295,167 | 289,211 | -2.0% |

Read one spec variant and one complete glossary view. The JSONL remains the source of truth; Markdown includes all normative group and registry data in readable tables. Shared defaults replace duplicated group fields, signatures alone define consumers, and glossary rules no longer repeat the spec. Historical/adoption prose is in design-notes.md.

## Files

- language-spec.md / language-spec.compact.md: normative rules, with the group mechanism in Section 3.1.
- glossary.jsonl / glossary.md: reduced active vocabulary and complete registries.
- glossary-impact.md: removals, retained exceptions and semantic migration limits.
- translator-group-proposals.md: proposed agent workflow; examples use the compact record schema.
- examples-and-validation.md: positive and negative design cases.
- migration-map.json: offline audit, never a value-admission whitelist.
- design-notes.md: rationale and historical adoption notes; not required for translating fresh documents.
- size-comparison.json / size-before-compaction.json: byte accounting.
- source-baseline.json / proposal-manifest.json: original hashes and candidate validation results.

An open label supplies deterministic identity and a source-supported role, not guessed English meaning. Unresolved sense requirements still make a translation partial. This remains an unimplemented design proposal; Accepted statuses apply only inside the candidate. Historical translations require semantic/type review.
