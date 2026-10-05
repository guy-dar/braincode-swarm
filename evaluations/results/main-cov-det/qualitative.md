# Qualitative analysis (written by claude-opus-5-5)

# BrainCode translator comparison: symbol use, avoidance, structure and divergences

## 1. Parts of speech, constructs and symbol types used more by particular models

**Symbol-type shares.** These are computed from `type_counts` and are shares of each model's typed symbol tokens.

| type | Gem-High | Gem-Flash | Sonnet | Haiku | o4-mini |
|---|---|---|---|---|---|
| constructor | 34.9% | 32.8% | 37.6% | 35.5% | 17.5% |
| value | 16.2% | 15.8% | 14.7% | 11.4% | 4.7% |
| attribute | 13.8% | 15.1% | 15.2% | 16.5% | 21.2% |
| group_value | 11.0% | 11.5% | 9.2% | 9.4% | 15.5% |
| claim_relation | 10.7% | 10.4% | 9.9% | 10.9% | 1.4% |
| speech_act | 6.0% | 6.6% | 8.8% | 10.0% | 27.7% |
| operation | 6.2% | 6.6% | 3.6% | 5.1% | 12.0% |
| total tokens | 3748 | 3529 | 4395 | 3545 | 491 |

**Speech acts vs. operations by company.**
- The two Claude models lean toward speech acts: 8.8% and 10.0%, against about 6% for Gemini.
- The two Gemini models lean toward operations: 6.2% and 6.6%, against 3.6% for Sonnet and 5.1% for Haiku.
- At the symbol level, Claude uses `inform` (Sonnet 83, Haiku 66) and `include` (95 and 67), both of which Gemini rarely uses (see Q2).

**Type-distribution distance.** Overall the type mixes of the four main models are nearly identical:
- js_types is 0.0007 for Gemini-High vs Gemini-Flash.
- js_types is 0.003 to 0.008 for the other pairs among the four main models.
- The differences above are therefore real but small.

**o4-mini is the clear outlier.**
- Speech acts are 27.7% of its tokens and claim relations only 1.4%.
- js_types against every other model is 0.118 to 0.150.

**Statement heads per translation.**
- **TERM:** Sonnet writes far more TERM statements (27.93) than Gemini (18.24 for Flash, 20.89 for High) or Haiku (12.55).
- **Length:** Sonnet also produces the longest translations, at 57.3 lines against 42 to 47 for the others.
- **UTTER:** Claude models use more UTTER (Haiku 6.66, Sonnet 7.17) than Gemini (about 4.2 to 4.3).
- **ACTION:** Gemini uses bare `ACTION` most (about 2.43 per translation). Haiku has no plain ACTION at all but the most `RECORD ACTION` (3.43, against 1.65 to 1.87 for the others).
- **LET:** Only Haiku (0.23) and o4-mini (0.27) use LET.
- **TASK:** Only Gemini (0.15 to 0.17) uses TASK in non-trivial amounts.

**Opaque `content=` fallbacks.** These separate the models sharply:
- Gemini: 0.00
- Sonnet: 0.33
- Haiku: 0.49
- o4-mini: 7.33 per translation

## 2. Symbol groups and families that certain models avoid

**Gemini avoids the Claude-favoured relations.**
- `include`: 0.1% vs 1.3% (Flash) and 0.1% vs 1.4% (High).
- `constrained_by`: 0.0% and 0.1% vs 0.5%.
- `inform` is avoided by Gemini-High (0.5% vs 2.1%).
- In place of these, Gemini packages content as `CLAIM statement(fact=...)`. Statement counts are 73 and 65 for Gemini, against 33 for Haiku.

**Claude avoids a Gemini-favoured family.**
- Both Claude models avoid `lexical_label` (0.0% vs 0.5%) and `provides` (0.1% vs 0.5 to 0.6%).
- Haiku also avoids `property_question` (0.0% vs 0.6%) and `conjunction` (0.2% vs 0.8%).
- Sonnet, by contrast, uses `conjunction` 48 times.
- Gemini-High uses `property_question` 38 times and `lexical_label` 38 times.

**Sonnet avoids embodied and code-edit symbols.**
- `walk`: 0.2% vs 0.8%.
- `chg_modify_code`: 0.2% vs 0.8%.
- This probably reflects its low success on ALFRED (0.33) rather than a stylistic preference. If failed runs contribute fewer symbols, avoidance is confounded with failure. The evidence does not say whether failed runs are counted.

**Value groups.**
- No main model is flagged as avoiding a specific `group::` family.
- Group values are 9 to 12% for all four main models.
- `platform_label::zuora` appears about 28 to 30 times in every main model's top 25 lists.
- `country::IT` (Haiku 32) and `document_section` (Haiku 57) look item-specific, so this is too thin to call a preference.

**o4-mini** avoids almost the whole semantic layer:
- `activity`: 2.4% vs 11.7%.
- `role_agent`: 1.6% vs 7.4%.
- Zero uses of `statement`, `character`, `recommended`, `conjunction`, `supports` and `platform_label::zuora`.
- Its group values are concentrated in `object_label::*` and `platform_label::*` inside ALFRED and SWE-bench actions, for example `object_label::lettuce` (7) and `platform_label::transformers` (7).

## 3. Repetitive structural patterns in complex texts

**Gemini: "bind-then-assert" pairs.**
- Nearly every fact becomes a TERM followed by `CLAIM statement(fact=…)`.
- In swebench-3, Gemini-High repeats this nine times for the dependency list: `TERM software_version(project=platform_label::pytest, version="3.9.1") -> software_version_10` followed by `CLAIM statement(fact=software_version_10)`.
- In paths-3 it uses the same pattern for characters: `TERM character(name="Lady Elyria")` … `CLAIM statement(fact=character_2)`.
- Gemini always binds sub-terms before use, rather than nesting them.
- Gemini names variables mechanically (`subject_2`, `activity_3`).
- Gemini appears to order arguments alphabetically: `activity(actor=…, object=…, purpose=…, verb=…)`.

**Haiku: hub-and-spoke claims around one anchor.**
- prism-2 chains `CLAIM constrained_by(activity=mow_activity, constraint=…)` for every equipment item and step.
- prism-1 repeats `CLAIM enables(condition=…, outcome=activity(…))` four times.
- Haiku nests constructors inline, e.g. `constraint=requirement(property="equipment_needed", value=…)`.
- Haiku puts `verb=` first and uses semantic names (`equipment_gloves`, `remove_debris`).
- On long narrative, Haiku can collapse the whole reply into one opaque `UTTER respond(target=t1.inception_source, content="Title: Dreamcrafter…")` (paths-3).

**o4-mini: one `UTTER inform(content="…")` per source sentence.**
- This holds even where the source repeats itself: prism-1 t4 duplicates the `confirm`/`inform` block verbatim.
- In swebench-3 it emits malformed `UTTER content="…"` lines and comments (`# We fall back to literal UTTER content…`).
- It also produces a self-nested `modify_code(... revision=chg_modify_code(... revision=cli_command(...)))`.

**Sonnet:** no Sonnet translation appears among the divergent examples, so its structural habits cannot be described beyond the counts. Those counts are many TERMs, `conjunction` 48 and `attribute_claim` 52.

## 4. Common examples of translation differences

**Structured semantics vs. verbatim text.**
- This is by far the most common difference. 5 of the 6 most divergent pairs involve o4-mini, with JS of 0.751 to 0.955.
- Example (prism-3, Gemini-Flash vs o4-mini): Gemini-Flash writes `CLAIM considered(subject=obligation_2) … LINK contrast(first=considered_2, second=controversial_2)`, while o4-mini writes `UTTER inform(content="The government has considered requiring…")`.

**Granularity of narrative.**
- paths-3 shows the contrast within the main models (JS 0.815).
- Gemini-High decomposes the plot into `character`, `obligation`, `decision` and `temporal_context` terms.
- Haiku keeps the reply as one quoted string.

**Choice of relation for the same content.**
- Equipment and steps: Haiku uses `constrained_by` (prism-2), where Gemini habitually uses `statement`, `provides` or `enables`.
- Speculative consequences: Haiku marks them with `STATUS hypothesized` (prism-1, `user_practice`), while Gemini uses `asserted`, `reported` or `inferred`.

**Invented or concatenated values.**
- Haiku: `object_label::gardeninggloves`, `object_label::protectiveeyewear`.
- Gemini-High: bare values `art_story`, `style_narrative`, `cat_game`.
- o4-mini: a raw string in a target slot, `UTTER offer(target="I hope this helps!…")`.

**Cross-turn reference style.**
- Gemini: `t1.conjunction_2`, `t1.activity_3`.
- Haiku: `REPLY_TO t1` and `t1.inception_source`.
- o4-mini: none.

**Distances between models.**
- Same-company distances are smallest: Gemini pair js_symbols 0.020, Claude pair 0.067.
- Cross-company distances among main models are 0.086 to 0.096.
- Every pair with o4-mini is 0.31 to 0.33.

## Caveats

- **o4-mini sample:** o4-mini ran once per item (18 runs) with a success rate of 0.17 and an error rate of 0.17. It has no self-consistency data, and its profile mostly reflects fallback behaviour.
- **Sonnet failures:** Sonnet succeeded on only 46% of shared runs (paths 0.11, alfred 0.33). Its symbol profile, and apparent "avoidance" of `walk` and `chg_modify_code`, may be failure artefacts. It also contributes no divergent examples.
- **Within-model variation:** Self-JS for the main models (0.098 to 0.183) is at least as large as pooled cross-model JS. This is not directly comparable, because it is per-item vs pooled, but it signals substantial run-to-run variation. Haiku is noisiest, at 0.183 and 0.31 on paths.
- **Small samples:** Some top symbols (`country::IT`, `document_section`) likely come from one or two items.
- **Truncated examples:** The divergent examples are truncated and selected for maximal divergence, so they illustrate extremes rather than typical output.
