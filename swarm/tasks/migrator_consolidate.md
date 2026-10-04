# Migrator: consolidate

You are the migrator for **batch {{BATCH_ID}}**, step 1 of 2. Translators failed on items the glossary couldn't express and wrote suggestions. Pre-migrators merged them in groups into **{{N_MERGED}} merged suggestion files**, which are attached to this message. Each pre-migrator saw only its own group, so the same concept often appears in several files under different names, and some patterns only show up across groups.

**Your job now: write one consolidated suggestion file.** Drafters will then turn it into glossary operations in parallel, and you'll review their drafts in step 2. You don't touch the glossary in this step.

**Attached:**
- the merged files (`M1.md`…)
- the consolidated-file format (`merged_suggestions.md`)
- the suggestion format
- the purpose
- the language spec

The glossary is at `/reference/glossary.md` (one table row per symbol) if you need to check whether a name exists.

## Do

1. **Merge across groups.** Find suggestions that mean the same thing in different files and give each one block. Its `Sources` names every merged suggestion it covers (`M2#S1, M4#S3`).
2. **Generalize patterns.** When several suggestions are instances of one pattern, propose one general constructor or member family, not one symbol per phrase. Say so in `Merge notes`.
3. **Keep real distinctions.** Negation, quantity, time, holder and epistemic status stay separate.
4. **Be compact.** One line per field, and the proposed record holds only the authored fields (`symbol`, `kind`, `category`, `signature`, `definition`, `not`, `aliases`, `expansion`). The drafters add detail.
5. **Account for everything.** Every merged suggestion appears in exactly one block's `Sources`, or in "Not carried forward" with a reason.

**No values baked into symbols.** Never propose or accept a symbol whose name carries a specific number, size, age, amount or other value (`char_age_18`, `ram_16gb`, `max_5_items`). Build it from constructors with arguments instead: `measure(amount, unit)`, `at_least(...)` / `at_most(...)`, `character_trait(property, value)`, `requirement(property, value)`. Proper names that contain digits (`topic_spider_man_2`) are fine.

Write `/output/consolidated_suggestions.md`, with header `# Consolidated suggestions — batch {{BATCH_ID}}` and blocks `### S1 | type: … | dimension: … | symbol|target: …`. Finish by writing it.
