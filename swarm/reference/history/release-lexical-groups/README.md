# Language release 19.0.0-draft.1 (glossary g14), before the lexical-groups release

The complete reference set as it was immediately before `python -m glossary.adopt_release` installed
`19.0.0-draft.2-lexical-groups` (glossary g15). Translations and suggestions from batches 1-10 were
made against these files (their headers name the glossary version).

| File | What it is |
|---|---|
| `language-spec.md` | Spec 19.0.0-draft.1, canonical (with §17, the v18 change log) |
| `language-spec.compact.md` | The compact spec translators received in batches 1-10 |
| `glossary.jsonl` / `glossary.md` | Glossary g14: 687 records, including the 34 leaf values the new release retired (`pillow`, `curr_zar`, `japan`, `color_red`, …) |
| `glossary-provenance.jsonl` | Provenance log up to g14 |
| `examples.jsonl` | Worked examples (the §13 pillow example with bare symbols) |
| `reference-manifest.json` | Versions and hashes of the above |

The design of the new release, and the map from each retired symbol to its group value, are in
`reference/proposed-lexical-groups/` (unchanged) and `reference/retired-symbols.json`.

To go back to this release, copy these files over `reference/` (keep `history/`), delete
`reference/standards/` and `reference/retired-symbols.json`, and restart the loop (it rebuilds the
RAG index). The code stays compatible: it reads both releases.
