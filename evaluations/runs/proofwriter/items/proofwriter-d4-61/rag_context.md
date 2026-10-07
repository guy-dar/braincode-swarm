# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 37 needs (decomposition: llm), 157 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | speech_act | t1:s1 | introduce a set of logical premises | `respond`, `supports`, `propose`, `inform`, `subject`, `conditional`, `ask`, `topic_school_work_routine`, `rule_structural_constructs`, `conjunction`, `confirm`, `correct` |
| n2 | claim | t1:s2 | Dave is green | `lettuce`, `color_label`, `outshines`, `enables`, `leads_to`, `grape_thompson_seedless`, `motivated_by`, `outcome`, `apple`, `statement`, `important`, `recommended` |
| n3 | object | t1:s2 | Dave | `resource_chiller`, `chill`, `on`, `yarn`, `bowtie`, `liberal_onsen`, `decision`, `candle`, `resource_sink`, `resource_heater`, `coffee_maker`, `locale_de` |
| n4 | constraint | t1:s2 | green → `color_label::<key>` | `color_label`*, `outshines`, `lettuce`, `apple`, `grape_thompson_seedless`, `constraint_exclude_flowery_language`, `right_of`, `left_of`, `constraint_respectful`, `constraint_exclude_liberation_theme`, `constraint_budget_limited`, `constraint_realistic` |
| n5 | claim | t1:s3 | Dave is quiet | `unaware`, `grape_thompson_seedless`, `enables`, `leads_to`, `outcome`, `tone_neutral`, `occurred_recently`, `statement`, `tone_silly`, `recommended`, `motivated_by`, `important` |
| n6 | object | t1:s3 | Dave | `resource_chiller`, `chill`, `on`, `yarn`, `bowtie`, `liberal_onsen`, `decision`, `candle`, `resource_sink`, `resource_heater`, `coffee_maker`, `locale_de` |
| n7 | constraint | t1:s3 | quiet | `tone_neutral`, `constraint_exclude_flowery_language`, `tone_polite`, `constraint_budget_limited`, `tone_urgent`, `state_cold`, `tone_silly`, `constraint_exclude_liberation_theme`, `tone_empathetic`, `constraint_respectful`, `constraint_realistic`, `tone_casual` |
| n8 | claim | t1:s4 | Dave is young | `enables`, `leads_to`, `topic_profanity`, `constraint_17_plus`, `outcome`, `occurred_recently`, `rule_support_primitives_general`, `statement`, `recommended`, `size_small`, `motivated_by`, `important` |
| n9 | object | t1:s4 | Dave | `resource_chiller`, `chill`, `on`, `yarn`, `bowtie`, `liberal_onsen`, `decision`, `candle`, `resource_sink`, `resource_heater`, `coffee_maker`, `locale_de` |
| n10 | constraint | t1:s4 | young | `constraint_budget_limited`, `topic_profanity`, `constraint_17_plus`, `constraint_exclude_flowery_language`, `size_small`, `under`, `role_kids`, `constraint_respectful`, `constraint_realistic`, `constraint_exclude_liberation_theme`, `unit_sentence`, `tone_silly` |
| n11 | claim | t1:s5 | Erin is blue | `color_label`, `enables`, `outcome`, `leads_to`, `recommended`, `statement`, `occurred_recently`, `color_pink`, `motivated_by`, `role_sister`, `event_sadie_adler_unmasking`, `important` |
| n12 | object | t1:s5 | Erin | `event_sadie_adler_unmasking`, `resource_chiller`, `yarn`, `art_short_text`, `right_of`, `constitutional_ai`, `art_story`, `art_plan`, `resource_heater`, `resource_sink`, `art_social_post`, `potential_harms` |
| n13 | constraint | t1:s5 | blue → `color_label::<key>` | `color_label`*, `lettuce`, `constraint_exclude_flowery_language`, `right_of`, `yakuza`, `constraint_respectful`, `constraint_exclude_liberation_theme`, `sultana`, `on`, `constraint_realistic`, `constraint_budget_limited`, `dried_fruit` |
| n14 | claim | t1:s6 | Erin is white | `enables`, `outcome`, `leads_to`, `gender_unisex`, `unit_word`, `statement`, `occurred_recently`, `recommended`, `motivated_by`, `important`, `comfortable`, `causes` |
| n15 | object | t1:s6 | Erin | `event_sadie_adler_unmasking`, `resource_chiller`, `yarn`, `art_short_text`, `right_of`, `constitutional_ai`, `art_story`, `art_plan`, `resource_heater`, `resource_sink`, `art_social_post`, `potential_harms` |
| n16 | constraint | t1:s6 | white → `color_label::<key>` | `color_label`*, `unit_word`, `constraint_exclude_flowery_language`, `dulce_de_leche`, `on`, `sultana`, `constraint_respectful`, `gender_unisex`, `constraint_exclude_liberation_theme`, `constraint_budget_limited`, `state_dirty`, `constraint_realistic` |
| n17 | claim | t1:s7 | Gary is quiet | `enables`, `unaware`, `outcome`, `leads_to`, `occurred_recently`, `tone_neutral`, `statement`, `recommended`, `motivated_by`, `important`, `cinnamon`, `comfortable` |
| n18 | object | t1:s7 | Gary | `chill`, `right_of`, `in_front_of`, `on`, `topic_baldurs_gate_3`, `left_of`, `next_to`, `resource_chiller`, `topic_politics`, `state_dirty`, `resource_sink`, `topic_greatest_cricketer_of_all_time` |
| n19 | constraint | t1:s7 | quiet | `tone_neutral`, `constraint_exclude_flowery_language`, `tone_polite`, `constraint_budget_limited`, `tone_urgent`, `state_cold`, `tone_silly`, `constraint_exclude_liberation_theme`, `tone_empathetic`, `constraint_respectful`, `constraint_realistic`, `tone_casual` |
| n20 | claim | t1:s8 | Harry is blue | `enables`, `leads_to`, `color_label`, `outcome`, `topic_spider_man_2`, `statement`, `occurred_recently`, `motivated_by`, `recommended`, `important`, `ginger`, `comfortable` |
| n21 | object | t1:s8 | Harry | `topic_spider_man_2`, `on`, `resource_chiller`, `united_kingdom`, `right_of`, `path_ipython_core_magics_basic_py`, `art_story`, `resource_heater`, `new_york_university`, `role_friend`, `resource_sink`, `coffee_maker` |
| n22 | constraint | t1:s8 | blue → `color_label::<key>` | `color_label`*, `lettuce`, `constraint_exclude_flowery_language`, `right_of`, `yakuza`, `constraint_respectful`, `constraint_exclude_liberation_theme`, `sultana`, `on`, `constraint_realistic`, `constraint_budget_limited`, `dried_fruit` |
| n23 | claim | t1:s9 | if something is cold and green then it is kind | `state_cold`*, `lettuce`, `enables`, `outshines`, `style_catchy`, `right_of`, `motivated_by`, `leads_to`, `recommended`, `important`, `color_label`, `causes` |
| n24 | claim | t1:s10 | all quiet things are green | `lettuce`, `grape_thompson_seedless`, `unaware`, `outshines`, `enables`, `color_label`, `comfortable`, `leads_to`, `tone_neutral`, `outcome`, `motivated_by`, `important` |
| n25 | claim | t1:s11 | if something is cold then it is kind | `state_cold`*, `comfortable`, `enables`, `style_catchy`, `reason_for`, `motivated_by`, `right_of`, `recommended`, `leads_to`, `important`, `weather_condition`, `causes` |
| n26 | claim | t1:s12 | if something is quiet and kind then it is white | `comfortable`, `enables`, `outshines`, `leads_to`, `recommended`, `motivated_by`, `style_catchy`, `tone_polite`, `outcome`, `unit_word`, `important`, `statement` |
| n27 | claim | t1:s13 | if something is cold then it is quiet | `state_cold`*, `comfortable`, `enables`, `weather_condition`, `motivated_by`, `leads_to`, `outcome`, `recommended`, `state_warm`, `statement`, `important`, `occurred_recently` |
| n28 | claim | t1:s14 | if Dave is cold then Dave is kind | `state_cold`*, `comfortable`, `enables`, `style_catchy`, `recommended`, `leads_to`, `motivated_by`, `mod_mixed_case`, `right_of`, `important`, `causes`, `yarn` |
| n29 | claim | t1:s15 | all green things are cold | `state_cold`*, `lettuce`, `grape_thompson_seedless`, `weather_condition`, `enables`, `color_label`, `leads_to`, `motivated_by`, `outcome`, `statement`, `causes`, `cinnamon` |
| n30 | claim | t1:s16 | all cold, white things are young | `state_cold`*, `enables`, `leads_to`, `motivated_by`, `topic_profanity`, `outcome`, `statement`, `causes`, `important`, `recommended`, `occurred_recently`, `weather_condition` |
| n31 | speech_act | t1:s17 | ask to evaluate the truth value of a statement | `ask`*, `statement`*, `respond`, `confirm`, `failure`, `inform`, `supports`, `test_condition`, `assert_multinomial_scorer`, `motivated_by`, `considered`, `run_tests` |
| n32 | constraint | t1:s17 | base the evaluation only on the provided theory | `subject`, `supports`, `test_condition`, `decision`, `regression_case`, `constraint_exclude_flowery_language`, `constraint_budget_limited`, `constraint_respectful`, `constraint_exclude_liberation_theme`, `constraint_realistic`, `considered`, `constraint_include_character_attribute_list` |
| n33 | constraint | t1:s17 | respond with True, False, or Unknown | `respond`*, `constraint_exclude_flowery_language`, `failure`, `assert_multinomial_scorer`, `unaware`, `constraint_respectful`, `constraint_realistic`, `constraint_budget_limited`, `constraint_exclude_liberation_theme`, `constraint_comprehensive`, `role_respondent`, `rejects` |
| n34 | claim | t1:s18 | Harry is not kind | `comfortable`, `enables`, `style_persuasive`, `leads_to`, `motivated_by`, `perceived_as`, `important`, `statement`, `recommended`, `has_attribute`, `causes`, `outcome` |
| n35 | negation | t1:s18 | not kind | `negation`, `topic_profanity`, `comfortable`, `style_catchy`, `character_trait`, `constraint_exclude_flowery_language`, `style_persuasive`, `exclude`, `well_wishes`, `tone_polite`, `rejects`, `decline` |
| n36 | object | t1:s18 | Harry | `topic_spider_man_2`, `on`, `resource_chiller`, `united_kingdom`, `right_of`, `path_ipython_core_magics_basic_py`, `art_story`, `resource_heater`, `new_york_university`, `role_friend`, `resource_sink`, `coffee_maker` |
| n37 | constraint | t1:s18 | kind | `style_catchy`, `right_of`, `constraint_exclude_flowery_language`, `well_wishes`, `tone_polite`, `similarity`, `style_persuasive`, `constraint_respectful`, `constraint_budget_limited`, `comfortable`, `constraint_exclude_liberation_theme`, `next_to` |

(* = exact name/alias match; → = the value group the need's noun/value belongs to)

## Value groups (all of them)

Leaf values are written `group::key` and have no glossary entry: any admissible key is valid (open groups: a lower-case word; country and currency: the ISO code, `country::JP`, `currency::ZAR`). Use a group only in a slot whose signature accepts `ATOM[group]`.

- `animal_label::<key>` — open label, lower_word — A source-supplied animal-kind label; denotes that labeled animal kind, without inferred taxonomy, behavior or capabilities. e.g. animal_label::cat, animal_label::tuna | slots: search_web.target, activity.object, lexical_label.value
- `color_label::<key>` — open label, lower_word — A source-supplied color-name qualifier; no numeric color coordinates, shade equivalence or color-space conversion is implied. e.g. color_label::red, color_label::blue | slots: search_web.color, pick_up.color, lexical_label.value
- `country::<key>` — ISO 3166-1 alpha-2 codes (249), upper_code — A country identified by its ISO 3166-1 alpha-2 code (country::JP is Japan). The code names the country only; no language, currency or region membership is implied. e.g. country::JP, country::DE | slots: search_travel.location, search_transit.location, search_web.location, check_reservation_availability.location, activity.location, subject.location, weather_condition.location
- `currency::<key>` — ISO 4217 codes (178), upper_code — A currency identified by its ISO 4217 code (currency::ZAR is the South African rand); no exchange rate or implicit conversion. e.g. currency::USD, currency::EUR | slots: search_web.currency, check_reservation_availability.currency, measure.unit
- `food_label::<key>` — open label, lower_word — A source-supplied food-kind label; denotes that labeled food kind, without inferred ingredients, preparation, nutrition or biology. e.g. food_label::tomato, food_label::egg | slots: search_web.target, pick_up.target, activity.object, lexical_label.value
- `genre_label::<key>` — open label, lower_word — An explicitly supplied genre label, without inferred genre taxonomy. e.g. genre_label::comedy, genre_label::shoegaze | slots: search_web.genre, lexical_label.value
- `object_label::<key>` — open label, lower_word — An explicitly supplied label of an object kind; no inferred physical properties or English sense. e.g. object_label::thimble, object_label::pillow | slots: search_web.target, pick_up.target, pick_up.source, place.destination, place.location, rinse.destination, heat.destination, chill.destination …
- `platform_label::<key>` — open label, lower_identifier — A source-supplied name of a software platform, service, framework, library, package, build tool or operating system (platform_label::django, platform_label::windows). Denotes that named system only; no version, vendor, capability or relation between systems is implied. e.g. platform_label::django, platform_label::windows, platform_label::pytorch_lightning | slots: modify_code.target, run_tests.target, requirement.value, activity.instrument, subject.qualifier, regression_case.framework, failure.system, attribute_claim.subject …

## Slots of the retrieved records that take value groups

- subject.qualifier → platform_label
- subject.location → country
- chill.destination → object_label
- weather_condition.location → country
- failure.system → platform_label
- run_tests.target → platform_label
- regression_case.framework → platform_label
- activity.object → object_label, food_label, animal_label
- activity.location → country
- activity.instrument → object_label, platform_label
- requirement.value → platform_label
- attribute_claim.subject → platform_label
- attribute_claim.value → platform_label
- walk.destination → object_label

## Retrieved records

### Shared rules that govern the records below (full text)

**rule_lexical_groups** (v19/rule/lexical-groups; rule governing platform_label)

Section 3.1 defines value groups: `group::key` values of type ATOM[group]. Open groups admit any key of their form (examples are not whitelists); standard groups admit the codes of their bundled standard (ISO 3166-1 alpha-2 for country, ISO 4217 for currency). Leaf values are never glossary entries. Consumer signatures alone decide where a group may appear. Retired bare symbols are invalid.

**rule_reading_guide** (v19/rule/reading-guide; core)

The spec governs syntax/types; this glossary defines vocabulary. Signature notation: ? optional, A / B explicit alternatives, void no result. Omitted optional arguments are unspecified. Value entries are category-refined STRING primitives; complex meanings require composition. Aliases are contextual hints, not unconditional equivalences. Report ambiguity. IDs use v19/<category>/<symbol>, v19/support/<symbol> or v19/composite/<symbol>. Statuses apply to this candidate: Retained preserves meaning; Adapted uses the stated contract; Composite requires TERM (bare STRING deprecated); Structural is syntax/argument vocabulary; Needs clarification is unusable until resolved; Deprecated is historical; Accepted is usable within this candidate.

**rule_recording_signatures** (v19/rule/recording-signatures; rule governing chill)

RECORD ACTION uses the operation signature with REF[STRING] → TERM and LIST[REF[STRING]] → LIST[TERM]; other types/categories stay unchanged. Return EVENT, never the runtime result. Record actual outputs as attributed CLAIMs. Do not infer missing resources.

**rule_speech_acts_general** (v19/rule/speech-acts-general; rule governing respond)

UTTER-only, void, with the spec's speech attributes and LIST[TERM] constraints. No result binding. Literal content cannot replace required semantic arguments for structured coverage.

**rule_structural_constructs** (v19/rule/structural-constructs; candidate)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; rule governing supports)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_attributes_and_generate** (v19/rule/attributes-and-generate; rule governing art_short_text)

Attribute entries name arguments; legality/types come from each operation, not global membership. GENERATE uses the spec's core fields; retained artifact profiles return STRING. Numeric/list results need explicit profiles. Legacy itinerary fields expand to TERM constraints: duration/duration_unit → duration(amount,unit); stop_min_per_day/stop_requirement → minimum_per_period(class,count,period=unit_day), never an inferred temple class; max_walk_duration/unit → maximum_between_stops(activity="walk",amount,unit). No legacy shorthand is enabled. Old events/character_properties/transformations become explicitly scoped TERM constraints. Message purpose is TERM, not send_email.content: GENERATE exact STRING content, then send. Report opaque fallback separately.

**rule_category_artifact_value** (v19/rule/category/artifact-value; rule governing art_short_text)

STRING artifact class for GENERATE.target. art_story says what kind of artifact to produce, not what occurs in its plot.

**rule_category_code_value** (v19/rule/category/code-value; rule governing path_ipython_core_magics_basic_py)

path_/sym_ remain STRING identities; migrated chg_/assert_ are TERM constructors. Do not recover an exact file path by guessing from underscores.

**rule_category_constraint_value** (v19/rule/category/constraint-value; rule governing constraint_exclude_flowery_language)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_descriptive_value** (v19/rule/category/descriptive-value; rule governing constitutional_ai)

STRING modifier/domain label; never a free-form proposition. dom_sgi needs its intended referent established before semantically dependent use.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; rule governing unit_sentence)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing lettuce)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_event_value** (v19/rule/category/event-value; rule governing event_sadie_adler_unmasking)

TERM-described narrative event, not a recorded EVENT. Require inclusion explicitly when generating a story.

**rule_category_locale_value** (v19/rule/category/locale-value; rule governing locale_de)

STRING locale. “English” alone does not always mean locale_en_us; preserve ambiguity.

**rule_category_location_name** (v19/rule/category/location-name; rule governing liberal_onsen)

STRING location descriptor. A `table` surface is not the generated artifact category art_table.

**rule_category_product_attribute_value** (v19/rule/category/product-attribute-value; rule governing size_small)

STRING color/size/product-market facets. gender_women describes a product category, not an assertion about a person's gender.

**rule_category_recipient_value** (v19/rule/category/recipient-value; rule governing role_kids)

STRING roles or explicit named recipients. A role is not an exact person's identity. Keep an explicit name where substituting a role loses information.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing on)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_state_value** (v19/rule/category/state-value; rule governing state_cold)

STRING condition used in selection. state_warm does not command heat; “hot” is not automatically synonymous with “warm.”

**rule_category_style_value** (v19/rule/category/style-value; rule governing style_catchy)

STRING production style. style_narrative does not establish that described events occurred.

**rule_category_tone_value** (v19/rule/category/tone-value; rule governing tone_neutral)

STRING register. tone_urgent describes urgency, not a concrete deadline.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_school_work_routine)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_composites_general** (v19/rule/composites-general; rule governing topic_school_work_routine)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_operations_general** (v19/rule/operations-general; rule governing chill)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_supplemental_general** (v19/rule/supplemental-general; rule governing coffee_maker)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; candidate)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- chill | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Chill using the stated resource; same identity.  ⟵ candidate
- run_tests | operation | operation-vocabulary | (target: STRING / ATOM[platform_label], assertion?: TERM) -> BOOL | Run the selected project's tests, optionally checking the specified assertion. TRUE means the declared test condition passed, not overall software correctness.  ⟵ candidate
- turn | operation | operation-vocabulary | (direction: STRING) -> void | Rotate agent body/view orientation. direction is typically left, right, or angle. | aliases: rotate, turn_around  ⟵ related to then
- walk | operation | operation-vocabulary | (destination: STRING / TERM / ATOM[object_label], relation?: STRING) -> void | Locomote towards a target destination or landmark. destination must identify a valid entity or location. | aliases: move_to, go_to, navigate_to  ⟵ related to then

### speech acts

- ask | speech_act | operation-vocabulary | UTTER ask(target: TERM, or a sufficiently precise topic: STRING / TERM) | Request information/advice; not an assertion of an answer. | aliases: ask, how should  ⟵ candidate
- confirm | speech_act | operation-vocabulary | UTTER confirm(target: CLAIM) | Confirm the proposition; its evidence/status remains explicit.  ⟵ candidate
- correct | speech_act | operation-vocabulary | UTTER correct(target: CLAIM) | Offer corrected content. Actual supersession requires the Conversation revision rules.  ⟵ candidate
- decline | speech_act | operation-vocabulary | UTTER decline(target: TERM) | Decline the represented request/proposal; not negate every proposition within it.  ⟵ candidate
- inform | speech_act | operation-vocabulary | UTTER inform(target: CLAIM) | Present the proposition; preserve its holder/status.  ⟵ candidate
- propose | speech_act | operation-vocabulary | UTTER propose(target: TERM) | Suggest an action/idea; does not record it as performed.  ⟵ candidate
- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ dependency of decision
- character_trait | constructor | TERM character_trait(property: STRING, value: STRING / NUMBER) -> TERM | A character attribute | not: Not a claim about a real person  ⟵ candidate
- conditional | constructor | TERM conditional(condition: TERM, consequence: TERM) -> TERM | Constructs a structured conditional proposition term connecting a condition and consequence. descriptive logic structure. | aliases: if_then  ⟵ candidate
- conjunction | constructor | TERM conjunction(items: LIST[TERM]) -> TERM | All described components apply | not: Does not imply temporal order  ⟵ candidate
- decision | constructor | TERM decision(activity: TERM) -> TERM | A decision whose content is the described activity | not: Not proof it was carried out  ⟵ candidate
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ candidate
- include | constructor | TERM include(item: STRING / TERM) -> TERM | Require the identified content/item | not: Not permission to invent an instance in a recorded trace  ⟵ dependency of constraint_include_character_attribute_list
- negation | constructor | TERM negation(target: TERM) -> TERM | Constructs a descriptive semantic negation of a target descriptive proposition or condition term. | not: Check's runtime Boolean operator NOT or a speech-act decline | aliases: not, does not, negation, absence of  ⟵ candidate
- outshines | constructor | TERM outshines(brighter: STRING / TERM, dimmer: STRING / TERM) -> TERM | Constructs a description of relative visual brightness where a brighter light source overpowers the perceived brightness of a dimmer object. | not: an absolute numeric brightness measurement | aliases: outshines, overpowers brightness, drowns out light  ⟵ candidate
- regression_case | constructor | TERM regression_case(framework: STRING / ATOM[platform_label], modifier: STRING, relation: STRING) -> TERM | A regression scenario specifying affected framework, condition and relation | not: Does not invent a passing test or exact implementation  ⟵ candidate
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ dependency of constraint_respectful
- sequence | constructor | TERM sequence(items: LIST[TERM]) -> TERM | Ordered described activities/content | not: Not unordered conjunction  ⟵ dependency of event_sadie_adler_unmasking
- similarity | constructor | TERM similarity(target: STRING / TERM, dimension?: STRING / TERM) -> TERM | Constructs a descriptor representing comparative closeness or similarity to a target along a given dimension. | not: spatial proximity (use rank_distance or next_to) or an assertion of exact identity (use identity) | aliases: closest_to, similar_to, resembles  ⟵ candidate
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ candidate
- test_condition | constructor | TERM test_condition(condition: STRING, expected: BOOL) -> TERM | A testable condition with the expected Boolean outcome | not: Expected outcome is not an observed result  ⟵ candidate
- weather_condition | constructor | TERM weather_condition(condition: STRING, location?: STRING / TERM / ATOM[country], severity?: STRING) -> TERM | A structured descriptor of atmospheric or weather phenomena such as wind, rain, or storm at an optional location; asserts nothing. | not: state_cold or state_warm (thermal states of physical objects) or occurred (past factual occurrence assertion) | aliases: weather, storm_condition, atmospheric_condition  ⟵ candidate
- well_wishes | constructor | TERM well_wishes(recipient?: STRING / TERM, sentiment?: STRING) -> TERM | Constructs a conversational discourse term representing well-wishes, good luck expressions, or parting encouragement. | not: a salutation greeting (use greeting) or apology (use apologize) | aliases: good_luck, best_wishes, encouragement  ⟵ candidate

### composites

- assert_multinomial_scorer | composite | code-value | TERM assert_multinomial_scorer() -> TERM | Assertion that multinomial probabilistic scoring succeeds. | = test_condition(condition="multinomial_probabilistic_scoring", expected=TRUE)  ⟵ candidate
- constraint_budget_limited | composite | constraint-value | TERM constraint_budget_limited() -> TERM | Limited budget. | = requirement(property="budget_limited", value=TRUE)  ⟵ candidate
- constraint_comprehensive | composite | constraint-value | TERM constraint_comprehensive() -> TERM | Must be comprehensive. | = requirement(property="comprehensive", value=TRUE)  ⟵ candidate
- constraint_exclude_flowery_language | composite | constraint-value | TERM constraint_exclude_flowery_language() -> TERM | Avoid flowery language. | = exclude(item="flowery_language")  ⟵ candidate
- constraint_exclude_liberation_theme | composite | constraint-value | TERM constraint_exclude_liberation_theme() -> TERM | Avoid liberation theme. | = exclude(item="liberation_theme")  ⟵ candidate
- constraint_include_character_attribute_list | composite | constraint-value | TERM constraint_include_character_attribute_list() -> TERM | Include character attributes. | = include(item="character_attribute_list")  ⟵ candidate
- constraint_realistic | composite | constraint-value | TERM constraint_realistic() -> TERM | Must be realistic. | = requirement(property="realistic", value=TRUE)  ⟵ candidate
- constraint_respectful | composite | constraint-value | TERM constraint_respectful() -> TERM | Must be respectful. | = requirement(property="respectful", value=TRUE)  ⟵ candidate
- event_sadie_adler_unmasking | composite | event-value | TERM event_sadie_adler_unmasking() -> TERM | Sadie Adler taking off her hat and peeling skin. | = sequence(items=[activity(verb="remove", actor="Sadie Adler", object="hat"), activity(verb="peel", actor="Sadie Adler", object="skin")])  ⟵ candidate
- topic_greatest_cricketer_of_all_time | composite | topic-value | TERM topic_greatest_cricketer_of_all_time() -> TERM | Greatest cricketer of all time. | = subject(kind="cricketer", qualifier=requirement(property="rank_by_greatness", value=1), time="all_time")  ⟵ candidate
- topic_profanity | composite | topic-value | TERM topic_profanity() -> TERM | A composite term representing the topic of profanity. | = subject(kind="profanity") | not: potential_harms (which is generic) | aliases: profanity  ⟵ candidate
- topic_school_work_routine | composite | topic-value | TERM topic_school_work_routine() -> TERM | School and work routine. | = subject(kind="routine", qualifier=conjunction(items=[subject(kind="school"), subject(kind="work")]))  ⟵ candidate

### claim relations

- attribute_claim | claim_relation | CLAIM attribute_claim(subject: STRING / TERM / ATOM[platform_label], property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) | Asserts that a subject possesses a named property evaluated to a specific primitive or structured value. general property attribution claim. | aliases: property_value, word_property, has_property, property attribution  ⟵ related to statement
- causes | claim_relation | CLAIM causes(cause: CLAIM / TERM, effect: CLAIM) | Asserts a direct causal relationship producing an effect proposition. causal assertion. | aliases: produces  ⟵ candidate
- comfortable | claim_relation | CLAIM comfortable(person: TERM, value: BOOL) | Asserts whether a person or animal is comfortable in a situation. affective/state claim. | aliases: is_comfortable  ⟵ candidate
- considered | claim_relation | CLAIM considered(subject: TERM) | Asserts that an agent or speaker evaluated or entertained a specific candidate term or concept. subject is the evaluated term. | aliases: evaluated, weighed  ⟵ candidate
- enables | claim_relation | CLAIM enables(condition: TERM / CLAIM, outcome: TERM / CLAIM) | Asserts that an enabling condition or capability facilitates an outcome. enabling condition. | aliases: facilitates, allows  ⟵ candidate
- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ candidate
- has_attribute | claim_relation | CLAIM has_attribute(subject: STRING / TERM, attribute: STRING / TERM) | Asserts that an entity, group, or person possesses a stated characteristic or attribute. general characteristic attribution. | aliases: possesses_attribute  ⟵ candidate
- has_state | claim_relation | CLAIM has_state(subject: TERM, state: STRING) | Asserts that an entity is currently in a physical, thermal, or operational state. state must be a valid state descriptor string. | aliases: in_state, state_is  ⟵ related to statement
- important | claim_relation | CLAIM important(target: TERM) | Asserts that a concept, activity, or condition is important or significant. evaluative importance claim. | aliases: significant  ⟵ candidate
- leads_to | claim_relation | CLAIM leads_to(cause: TERM, effect: TERM) | Asserts a conceptual consequence or progression from cause to effect. progression relation. | aliases: results_in  ⟵ candidate
- motivated_by | claim_relation | CLAIM motivated_by(claim: CLAIM, motive: STRING / TERM) | Asserts that an action, rule, or claim is motivated by an underlying motive or goal. motive explanation. | aliases: rationale_is  ⟵ candidate
- occurred_recently | claim_relation | CLAIM occurred_recently(target: CLAIM) | Asserts temporal recency of an asserted occurrence or claim. temporal recency qualifier. | aliases: recently_happened  ⟵ candidate
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ candidate
- perceived_as | claim_relation | CLAIM perceived_as(subject: STRING / TERM, concept: STRING / TERM) | Asserts public perception attributing a quality, reputation, or image to a subject. perception attribution. | aliases: regarded_as  ⟵ candidate
- reason_for | claim_relation | CLAIM reason_for(subject: CLAIM / TERM, reason: STRING / TERM) | Asserts an explanatory reason for a policy, belief, or state of affairs. explanatory reason. | aliases: basis_for  ⟵ candidate
- recommended | claim_relation | CLAIM recommended(target: TERM / CLAIM) | Asserts an advisory recommendation that an activity or measure is advisable. advisory normative claim. | aliases: advisable  ⟵ candidate
- spatial_state | claim_relation | CLAIM spatial_state(relation: STRING, object: TERM, reference: TERM) | Asserts an observed spatial configuration between an object and a reference landmark. relation must specify spatial configuration. | aliases: placed_at, located_at  ⟵ related to statement
- statement | claim_relation | CLAIM statement(fact: TERM) | Foundational claim relation converting any descriptive TERM into an attributed, truth-evaluated assertion. universal fact assertion. | aliases: assert_fact, fact_claim, claim_statement  ⟵ candidate
- unaware | claim_relation | CLAIM unaware(person: STRING / TERM, topic: STRING / TERM) | Asserts epistemic lack of awareness regarding a topic, fact, or event. epistemic state. | aliases: ignorant_of  ⟵ candidate
- validates_parameter | claim_relation | CLAIM validates_parameter(condition: STRING, entity: TERM, parameter: STRING) | Asserts that a code entity inspects or validates parameter names or types for a specified condition. | not: a runtime assertion test | aliases: inspects_parameter, checks_parameter, validates_parameter_names  ⟵ candidate

### links

- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ candidate
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ core
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ candidate
- then | link | LINK then(previous: EVENT, next: EVENT) | Represents temporal sequence and succession between two events where next follows previous. previous and next must be event terms. | aliases: followed_by, after_which  ⟵ candidate

### values

- art_plan | value | artifact-value | Actionable plan.  ⟵ candidate
- art_short_text | value | artifact-value | Short free text.  ⟵ candidate
- art_social_post | value | artifact-value | A short social media post or microblogging message. | not: art_short_text (general unstructured short prose) or art_story (narrative fiction) | aliases: tweet, tweets, social_media_post, microblog_post  ⟵ candidate
- art_story | value | artifact-value | Narrative story.  ⟵ candidate
- path_ipython_core_magics_basic_py | value | code-value | File path to the IPython basic magics module. | not: an individual command line script or general config file | aliases: IPython/core/magics/basic.py, ipython_core_magics_basic_py  ⟵ candidate
- constraint_17_plus | value | constraint-value | Rated 17+ or mature.  ⟵ candidate
- constitutional_ai | value | descriptive-value | Concept of rule-based constitutional training and self-critique principles in AI alignment. | aliases: constitutional_ai  ⟵ candidate
- mod_mixed_case | value | descriptive-value | Mixed-case modifier. | aliases: mixed case  ⟵ candidate
- potential_harms | value | descriptive-value | Concept of potential safety hazards, adverse outcomes, or risks in AI interaction. | aliases: potential_harms  ⟵ candidate
- yakuza | value | descriptive-value | Descriptive concept of yakuza in cultural and social contexts. | aliases: yakuza  ⟵ candidate
- unit_sentence | value | duration-unit-value | One grammatical sentence in text generation or constraint counting. | not: unit_paragraph (paragraph block) or unit_word (individual word) | aliases: sentence, sentences  ⟵ candidate
- unit_word | value | duration-unit-value | Rendered whitespace-delimited word. | aliases: words  ⟵ candidate
- apple | value | entity-name | An apple fruit item, typically an ingredient or interactive food object. | not: food_label::tomato or other fruits/vegetables | aliases: apple, apples, red apple, green apple, apple slice  ⟵ candidate
- bowtie | value | entity-name | Item or prop in joke/creative context: bowtie. | aliases: bowtie  ⟵ candidate
- candle | value | entity-name | A candle light source made of wax with a wick. | not: lamp (an electric light appliance or fixture) | aliases: candle, wax candle  ⟵ candidate
- cinnamon | value | entity-name | Ground or whole cinnamon culinary spice from Cinnamomum tree bark. | not: nutmeg, cloves, or other distinct spice varieties | aliases: cinnamon, ground cinnamon, cinnamon spice, cinnamon stick  ⟵ candidate
- coffee_maker | value | entity-name | A coffee-making appliance; not automatically a heating resource  ⟵ candidate
- dried_fruit | value | entity-name | Generic dried fruit food item. | not: fresh fruit or specific dried varieties like raisin or sultana | aliases: dried fruit, dried fruits  ⟵ candidate
- dulce_de_leche | value | entity-name | Sweet caramelized milk confection or dessert spread: dulce de leche. | not: cheese or dulce_de_nata | aliases: dulce de leche, dulce_de_leche  ⟵ candidate
- dulce_de_nata | value | entity-name | Clotted cream milk confection or dessert item: dulce de nata. | not: dulce_de_leche or cheese | aliases: dulce de nata, dulce_de_nata  ⟵ candidate
- fridge | value | entity-name | A refrigerator cooling appliance. | aliases: fridge  ⟵ candidate
- ginger | value | entity-name | Pungent aromatic spice root from Zingiber officinale used in cooking and baking. | not: cinnamon, cardamom, or other distinct spice varieties | aliases: ginger, ground ginger, fresh ginger, ginger root  ⟵ candidate
- grape_thompson_seedless | value | entity-name | Thompson Seedless grape variety. | not: wine grape cultivars like grape_merlot or grape_chardonnay | aliases: Thompson Seedless, thompson seedless grape, sultana grape  ⟵ candidate
- lettuce | value | entity-name | A head of lettuce or leafy green vegetable food item. | not: food_label::tomato or food_label::potato (other vegetable items) | aliases: lettuce, head of lettuce, salad greens  ⟵ candidate
- resource_chiller | value | entity-name | Canonical abstract chilling resource when no particular appliance is named.  ⟵ candidate
- resource_heater | value | entity-name | Canonical abstract heating resource when no particular appliance is named.  ⟵ candidate
- resource_sink | value | entity-name | Canonical abstract washing resource when no particular sink is named.  ⟵ candidate
- sultana | value | entity-name | Dried white seedless grape food product. | not: raisin (dark dried grape) or wine_grape | aliases: sultana, sultanas, golden raisin  ⟵ candidate
- yarn | value | entity-name | Item or prop in joke/creative context: yarn. | aliases: yarn  ⟵ candidate
- locale_de | value | locale-value | German language or locale descriptor. | not: other language locales (such as locale_en_us or locale_fr) or country entity (country::DE) | aliases: German, german, Deutsch, de, de-DE  ⟵ candidate
- liberal_onsen | value | location-name | Traditional Japanese establishment or hospitality venue: liberal_onsen. | aliases: liberal_onsen  ⟵ candidate
- new_york_university | value | location-name | New York University institution or campus grounds. | aliases: nyu  ⟵ candidate
- united_kingdom | value | location-name | Geopolitical nation or sovereign state: United Kingdom (Great Britain). | not: locale_en_gb (a language/locale code, not a location) | aliases: United Kingdom, UK, Great Britain, Britain  ⟵ candidate
- color_pink | value | product-attribute-value | Pink visual color qualifier. | not: color_label::red, color_label::purple, or other distinct color shades | aliases: pink, color_pink, blush pink, rose pink, pastel pink  ⟵ candidate
- gender_unisex | value | product-attribute-value | Unisex. | aliases: unisex  ⟵ candidate
- size_small | value | product-attribute-value | Small size. | aliases: small, S  ⟵ candidate
- role_friend | value | recipient-value | A friend of the user. | aliases: my friend  ⟵ candidate
- role_kids | value | recipient-value | Children/kids participant group in event context. | aliases: kids, children  ⟵ candidate
- role_respondent | value | recipient-value | A respondent, survey participant, or interviewee providing primary research data. | not: role_customer (the user's client) or role_user (the conversational user) | aliases: respondent, respondents, survey respondent, study participant  ⟵ candidate
- role_sister | value | recipient-value | Sister participant role in family/event context. | aliases: sister  ⟵ candidate
- in_front_of | value | spatial-relation | Positioned in front of. | aliases: in front of  ⟵ candidate
- left_of | value | spatial-relation | To the left of. | aliases: left of  ⟵ candidate
- next_to | value | spatial-relation | Adjacent to. | aliases: beside  ⟵ candidate
- on | value | spatial-relation | Resting atop. | aliases: on top of  ⟵ candidate
- right_of | value | spatial-relation | To the right of. | aliases: right of  ⟵ candidate
- under | value | spatial-relation | Beneath. | aliases: below  ⟵ candidate
- state_cold | value | state-value | Cold or chilled condition. | aliases: cold, chilled  ⟵ candidate
- state_dirty | value | state-value | Dirty condition. | aliases: dirty  ⟵ candidate
- state_warm | value | state-value | Warm or heated condition. | aliases: warm, hot  ⟵ candidate
- style_catchy | value | style-value | Catchy, attention-grabbing style. | aliases: catchy  ⟵ candidate
- style_persuasive | value | style-value | Persuasive/argumentative style. | aliases: persuasive  ⟵ candidate
- tone_casual | value | tone-value | Informal register. | aliases: casually  ⟵ candidate
- tone_empathetic | value | tone-value | Conveys empathy/understanding. | aliases: sympathetically  ⟵ candidate
- tone_neutral | value | tone-value | Plain, unmarked register.  ⟵ candidate
- tone_polite | value | tone-value | Courteous, respectful register. | aliases: politely, kindly  ⟵ candidate
- tone_silly | value | tone-value | Playful, lighthearted, or silly conversational tone. | aliases: silly  ⟵ candidate
- tone_urgent | value | tone-value | Conveys urgency. | aliases: urgently, ASAP  ⟵ candidate
- topic_baldurs_gate_3 | value | topic-value | Baldur's Gate 3.  ⟵ candidate
- topic_politics | value | topic-value | Politics.  ⟵ candidate
- topic_spider_man_2 | value | topic-value | Marvel's Spider-Man 2.  ⟵ candidate
