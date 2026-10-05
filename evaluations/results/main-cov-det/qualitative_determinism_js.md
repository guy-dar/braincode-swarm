# Qualitative analysis: determinism (JS divergence of symbol use), written by claude-opus-5-5

# BrainCode Translation Evaluation: Model Differences in Symbol Use, Structure and Translation Choices

Type shares below are my own computations from `type_counts`: count divided by that model's total typed symbols. Raw counts are not comparable across models because volume differs, especially for o4-mini. In every model, the `attribute` type count almost exactly equals the count of the symbol `target` (e.g. Gemini high 483/483, Sonnet 662/661, o4-mini 361/358). So "attribute" effectively measures use of the `target=` argument.

## 1. Constructs and symbol types that particular models over-use

**Type-level profile (share of typed symbols)**

| Type | Gemini high | Gemini Flash | Sonnet 5.5 | Haiku 4.5 | o4-mini |
|---|---|---|---|---|---|
| constructor | 35.4% | 33.3% | **38.1%** | 35.5% | 24.7% |
| value | **16.4%** | 15.9% | 14.3% | 12.8% | 6.1% |
| attribute (`target`) | 13.9% | 14.9% | 15.5% | 16.4% | **22.0%** |
| claim_relation | 10.5% | 10.2% | 9.8% | 11.0% | **4.4%** |
| group_value | 10.0% | 10.7% | 9.1% | 8.6% | **17.0%** |
| speech_act | 6.2% | 6.6% | 8.5% | 9.7% | **12.5%** |
| operation | 6.4% | 7.2% | 3.8% | 4.8% | **11.8%** |

**The four strong-performing models share one type profile.**
- Type-level JS among the two Gemini and two Claude models is tiny, between 0.0007 and 0.007.
- o4-mini is the clear outlier. Its JS against every other model is 0.050–0.062.
- o4-mini's profile has:
  - half the constructor-heavy content of the others;
  - less than half their claim relations;
  - much more of the "thin" types: `target`, speech acts, operations and group values.

**Statement heads (per translation) show stable company signatures.**

- **Gemini uses ACTION more.**
  - Gemini models use about 2.6 `ACTION` per translation (2.64 / 2.57).
  - Claude uses 0.74 (Haiku) and 1.3 (Sonnet).
  - Gemini also uses `TASK` blocks (0.16–0.18), which Haiku never does and Sonnet almost never does (0.02).
  - The alfred example shows the cause. Gemini high switches to `MODE REQUEST … TASK Keys { ACTION turn(direction="left") … }`, while Haiku stays in `MODE TRACE` with `CONVO`/`TURN`.
- **Claude uses UTTER more.**
  - Claude models use about 6.8 `UTTER` per translation.
  - Gemini uses about 4.2.
  - This matches Claude's higher speech-act share (8.5–9.7% vs 6.2–6.6%) and Gemini high's avoidance of `inform` (see Q2).
- **Sonnet writes the most TERMs.**
  - Sonnet averages 27.52 `TERM` per translation, about double Haiku's 13.94.
  - It also has the longest translations (56.48 lines) and the highest constructor share.
- **Haiku records more past actions.**
  - Haiku has more `RECORD ACTION` (2.63 vs Sonnet 1.65).
  - It is the only strong-coverage model using `LET` (0.15).
- **o4-mini makes very few claims.**
  - It averages 1.2 `CLAIM` per translation, against 5.7–8.0 for the others.
  - It has the most opaque `content=` fallbacks (0.48).
  - It uses rare heads such as `GENERATE` and `RETURN`.
  - Sonnet is the only other model with fallbacks (0.37). Both Gemini models and Haiku have 0.0.

**Part-of-speech-like tendencies (from top symbols)**
- Claude models lean on speech-act and communicative symbols:
  - Sonnet: `propose` 125, `include` 94, `inform` 71, `request` 50.
  - Haiku: `propose` 115, `ask` 110, `inform` 70.
- Gemini leans more on concrete operations and labels:
  - `walk` (34 / 31), `turn`, `lexical_label` (Gemini high 38).

## 2. Symbol groups and families that certain models avoid

**Gemini avoids specific relations and constructors.**
- Both Gemini models avoid:
  - `include` (0.1% vs 1.2% in the others);
  - `constrained_by` (0.0–0.1% vs 0.5%);
  - `software_version` (0.0% vs 0.5%).
- Gemini high additionally avoids `inform` (0.4% vs 1.7%).
- Gemini Flash vs Gemini high has a symbol JS of 0.020. This is the most similar pair by far, so these avoidances look like a company or model-family trait rather than an effort-level one.

**Claude avoids `lexical_label` (both models 0.0% vs 0.5%).**
- This is tied to how the two families treat `object_label`/`color_label` values.
- Gemini high in alfred-1 builds `TERM lexical_label(value=color_label::black)`, `lexical_label(value=object_label::table)`, and so on.
- Haiku on the same item uses bare strings: `activity(verb="place", object="keys", location="ottoman")`.
- Haiku also avoids `property_question` entirely (0.0% vs 0.7%).
- Sonnet does use `property_question` heavily in thoughttrace-2. So this is a model-specific avoidance, not a Claude-wide one.

**Sonnet avoids several symbols.**
- `walk` (0.2% vs 0.9%).
- `country::IT` (0.1% vs 0.6%).
- `provides`, `duration`, `art_story`, `lexical_label`.
- The `country::IT` gap is visible in thoughttrace-2:
  - Sonnet writes `location="Rome"` as a string.
  - Haiku attaches `location=country::IT` to every activity (`country::IT` is 32 occurrences in Haiku's top list).
- This contrast comes largely from one item, so it is weak evidence of a general aversion to `country::` values.

**o4-mini avoids the claim-relation family as a whole.**
- `supports`, `attribute_claim`, `provides` and `leads_to` are all at 0.0% (vs 0.4–0.6% in the others).
- `statement`, `recommended`, `acknowledge` and `user_practice` are at 0.1–0.2%.
- It also avoids `character`, `document_section` and `lexical_label`.
- Its use of `object_label::*` values is relatively high: `counter` 20, `lawn` 16, `table` 14.
  - Its group_value share (17.0%) is the highest of all models.
  - Its "missing" content is relational and discourse-level, not lexical.

**Value groups in general.** Beyond the observations above, the evidence cannot establish group-level avoidance.
- `symbols_avoided` lists individual symbols, not whole `group::` families.
- Group-value shares in the four strong-coverage models sit in a narrow band (8.6–10.7%).
- Top-25 lists show item-driven values such as `platform_label::zuora` (Gemini, Sonnet), `country::JP` and `platform_label::pandas` (Gemini Flash). These reflect specific source texts more than model preferences.

## 3. Repetitive structural patterns in complex texts

- **Sonnet: one TERM per fact, then a CLAIM wrapper.**
  - In thoughttrace-2, each user preference becomes `TERM requirement(property=…, value=…)` followed by `CLAIM desires(target=requirement_N) BY user …`. This repeats five or more times.
  - In mind2web-1, the same habit appears as seven consecutive `requirement(property=…)` TERMs plus 15 `web_element(label=…, tag=…)` TERMs.
  - This pattern explains its 27.5 TERMs per translation.
- **Sonnet and Haiku: TERM + UTTER pairs.**
  - Sonnet: `TERM property_question(...) -> property_question_2` then `UTTER ask(target=property_question_2)`, repeated per question.
  - Haiku (alfred-1): `TERM activity(verb="turn") -> turn_1` … `UTTER propose(target=turn_1)` for every step.
  - Both drive Claude's higher UTTER counts.
- **Haiku: flat, repetitive lists with copied arguments.**
  - In thoughttrace-2, ten consecutive lines take the form `TERM activity(verb="kayaking", location=country::IT)`.
  - Activity names are stuffed into `verb` ("e-bike tour", "truffle hunting").
  - Elsewhere it uses raw strings in speech acts: `UTTER ask(topic="Where do you want to go?")`.
- **Gemini high: a narrative "statement" scaffold.**
  - In paths-3, nearly every sentence is wrapped as `CLAIM statement(fact=X) BY role_agent STATUS reported`.
  - Named entities are introduced as `character(name=…)`.
  - This is consistent with `statement` 47 and `character` 54 in its top list.
  - Its alfred translation spawns many `spatial_constraint` and `lexical_label` TERMs. Several, such as `spatial_constraint_3`, are never referenced again.
- **Gemini Flash: a CLAIM + LINK argument chain.**
  - In prism-3 it links claims explicitly: `LINK contrast(first=considered_2, second=controversial_2)` and `LINK supports(conclusion=important_2, premise=controversial_2)`.
  - This is a discourse-structure pattern o4-mini never produces (`supports` 0.0%).
- **o4-mini: three distinct habits.**
  - It lists web actions as `RECORD ACTION click(target="Flights") STATUS succeeded SOURCE …` and repeats this for all steps. Sonnet instead declares the elements as TERMs.
  - It nests constructors inline inside `UTTER`, e.g. `UTTER propose(target=flight_search_request(origin=…, …))`.
  - It abandons whole turns with comments: `# Content of t2:s1–t2:s5 not encoded due to missing constructors/relations`.
  - It also leans heavily on `# PROPOSED: Sn` tags for invented constructors (`reason_question`, `problem_question`, `naming_pattern`).

**Consistency.** Self-consistency mirrors these patterns.
- o4-mini's self-JS is 0.330 (SD 0.163), roughly 2–3.6× the others (0.092–0.173). It reaches 0.456 on swebench.
- Gemini high is the most self-consistent (0.092).
- Haiku is notably variable on paths (0.265), the narrative dataset.

## 4. Common translation differences

- **Granularity and dropped detail.**
  - In alfred-1, Haiku omits "white vase", "purple", "black" and "cell phone".
  - Gemini high encodes all of them, down to `ACTION place(…, location=object_label::phone, relation=left_of)`.
  - Item JS for this pair is 0.893, the highest of all items.
- **Speech-act choice for the same utterance.**
  - "planning a trip" becomes `UTTER ask(topic="planning a trip")` in Haiku.
  - Sonnet renders it as `CLAIM ongoing(...)` plus `UTTER inform`.
  - Alfred commands become `UTTER propose` (Haiku) vs bare `ACTION` in a `TASK` (Gemini).
- **Literal vs normalized values.**
  - In mind2web-1, Sonnet normalizes "San Francisco" and encodes nonstop as `value=0`.
  - o4-mini keeps `text="SAN FRANSISCO"`, which is faithful to the typed text, and writes `stops="nonstop"`.
  - Both map "morning" to `daytime`.
  - Group values also split: `group=role_senior` (o4-mini) vs `group="senior"` (Sonnet).
- **Resolving underspecified facts.**
  - Haiku dates the trip `"early July 2025"`, while Sonnet writes `"early_july_current_year"`.
  - Haiku encodes travelling with parents as `group_size(count=3, group="parents")`. This conflates the user with the parents.
- **Content invention or misattribution (o4-mini).**
  - paths-3 is about Inception, yet o4-mini's output references `topic_baldurs_gate_3` and `topic_spider_man_2`, which appear nowhere in the source excerpt.
  - In prism-3 it emits `UTTER inform(target=policy_summary)` with no definition for `policy_summary`.
- **Redundant or mismatched arguments.**
  - Gemini Flash writes `attribute_claim(…, subject=subject_3, value="marginalized_communities")`, where the subject is already the marginalized communities.
  - Gemini high passes a character as `purpose=character_5`.

## Caveats

- **Coverage differs enormously on the shared items.** Success rates are:
  - Haiku 0.93, Gemini high 0.91, Gemini Flash 0.85;
  - Sonnet 0.44;
  - o4-mini 0.07.
  - It is unclear whether symbol counts include failed or partial translations.
  - o4-mini's profile (and partly Sonnet's) may therefore reflect failure modes rather than stylistic preference. Its type profile is consistent with mostly incomplete output.
- **The sample is small.** Shared items give 54 runs per model (16–18 items with two or more runs).
  - Many "avoided" gaps are 0.4–1 percentage point and could be driven by one or two items, e.g. `country::IT` and `art_story`.
- **Only Gemini has all-items data.** All-items figures (144 runs) exist only for the Gemini models, so cross-company comparisons rest on the shared subset.
- **Excerpts are truncated.** The divergent examples are cut off and were selected for maximal divergence. They illustrate patterns but are not representative frequencies.
- **The type taxonomy is uneven.** "Attribute" is essentially one symbol (`target`), so that row measures argument style, not a broad part of speech.
