# Format: merged suggestions (pre-migrator output) and consolidated suggestions (migrator)

Migration happens in two stages:

1. **Pre-migrators** (up to 5 in parallel, translator-class model). Each one receives up to 6 translator suggestion files and merges them with each other into **one merged suggestion file**. They don't look at the glossary: their job is to deduplicate, unify naming, and generalize across their group only.
2. **The migrator** (stronger model). It merges the up to 5 merged files into **one consolidated suggestion file**, then migrates that file into the glossary (`migration_ops.md`).

Both files use the same suggestion block format as `suggestions.md`, with one extra required field: **`Sources`**.

## Merged file — written by a pre-migrator as `/output/merged.md`

````markdown
# Merged suggestions M2 — batch 7

- Group: M2
- Source files: 7-4, 7-9, 7-15, 7-18, 7-21, 7-28

### S1 | type: add | dimension: constructor | symbol: group_size
- Sources: 7-4#S1, 7-9#S2, 7-21#S3
- Needs: 7-4 n2 (t1:s1); 7-9 n5 (t2:s1); 7-21 n3 (t1:s2)
- Typed parameters: …
- Interpretation: …
- Restrictions: …
- Examples: …
- Merge notes: 7-9 called it `member_count` and 7-21 `how_many`; same meaning (a count of members of a described group), unified under one constructor.
- Proposed record:
```json
{…}
```

### S2 | type: refine | dimension: refine-entry | target: v19/composite/constraint_17_plus
- Sources: 7-15#S2
- …

## Not carried forward

| source | reason |
|---|---|
| 7-28#S4 | Same concept as S1 (group_size), which covers it |
| 7-18#S1 | Translator's own note says the existing `place` covers it; withdrawn |
````

## Consolidated file — written by the migrator as `/output/consolidated_suggestions.md`

The format is the same, titled `# Consolidated suggestions — batch 7`. Its `Sources` name **merged** suggestions (`M2#S1`, `M4#S3`), and its "Not carried forward" table lists any merged suggestion dropped while consolidating. Drafters and the review refer to its blocks as `C#S<k>`.

## Rules (validated by the host)

- **Headings.** They use the exact `### S<k> | type: … | dimension: … | symbol|target: …` format from `suggestions.md`, numbered from S1 within the file.
- **Every input is accounted for.** Every suggestion in the input (`<translator_id>#S<k>` for a pre-migrator, `M<g>#S<k>` for the migrator) appears in exactly one place: in the `Sources` of one block, or in the "Not carried forward" table with a reason. Nothing is silently dropped.
- **Merge when the meaning is the same.** Two suggestions are merged when they mean the same thing, even under different names or dimensions. Several one-off suggestions that are instances of one pattern become one general constructor or family (with `Merge notes` saying so). Suggestions that merely look alike but differ in meaning (negation, quantity, time, holder, epistemic status) stay separate.
- **Merged evidence.** A merged block carries the union of its sources' `Needs` and evidence, and the most complete version of each field.
- **Proposed record.** One JSON line with only the authored fields (`symbol`, `kind`, `category`, `signature`, `definition`, `not`, `aliases`, `expansion`); see `suggestions.md`.
