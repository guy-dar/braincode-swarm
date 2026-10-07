# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 35 needs (decomposition: llm), 150 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | speech_act | t1:s1 | introduces a logical theory or set of premises | `respond`, `supports`, `subject`, `propose`, `ask`, `inform`, `conditional`, `failure`, `motivated_by`, `correct`, `rule_structural_constructs`, `confirm` |
| n2 | claim | t1:s2 | Bob is white | `enables`, `outcome`, `unit_word`, `leads_to`, `role_professor`, `in_front_of`, `statement`, `state_dirty`, `causes`, `motivated_by`, `important`, `occurred_recently` |
| n3 | object | t1:s2 | Bob | `resource_sink`, `bread`, `in_front_of`, `role_professor`, `right_of`, `behind`, `on`, `topic_spider_man_2`, `left_of`, `bowtie`, `resource_chiller`, `resource_heater` |
| n4 | constraint | t1:s2 | white color → `color_label::<key>` | `color_label`*, `color_pink`, `outshines`, `unit_word`, `visual_contrast`, `constraint_exclude_flowery_language`, `illuminates`, `sultana`, `constraint_respectful`, `gender_unisex`, `rule_category_product_attribute_value`, `constraint_include_character_attribute_list` |
| n5 | claim | t1:s3 | Fiona is cold | `state_cold`*, `enables`, `event_sadie_adler_unmasking`, `outcome`, `state_dirty`, `leads_to`, `cinnamon`, `yarn`, `statement`, `causes`, `motivated_by`, `chill` |
| n6 | object | t1:s3 | Fiona | `chill`, `yarn`, `event_sadie_adler_unmasking`, `style_catchy`, `on`, `role_sister`, `right_of`, `art_story`, `bowtie`, `role_mother`, `resource_sink`, `next_to` |
| n7 | claim | t1:s4 | Fiona is rough | `state_dirty`, `character_trait`, `enables`, `outcome`, `style_catchy`, `leads_to`, `yarn`, `statement`, `important`, `recommended`, `event_sadie_adler_unmasking`, `tone_empathetic` |
| n8 | claim | t1:s5 | Gary is big | `important`, `enables`, `leads_to`, `outcome`, `statement`, `causes`, `size_large`, `motivated_by`, `topic_greatest_cricketer_of_all_time`, `comfortable`, `size_tall`, `recommended` |
| n9 | object | t1:s5 | Gary | `chill`, `right_of`, `in_front_of`, `on`, `topic_baldurs_gate_3`, `next_to`, `left_of`, `state_dirty`, `resource_sink`, `topic_politics`, `topic_greatest_cricketer_of_all_time`, `resource_chiller` |
| n10 | claim | t1:s6 | Gary is rough | `state_dirty`, `enables`, `outcome`, `leads_to`, `topic_greatest_cricketer_of_all_time`, `statement`, `tone_empathetic`, `cinnamon`, `important`, `topic_baldurs_gate_3`, `on`, `recommended` |
| n11 | claim | t1:s7 | Gary is white | `enables`, `outcome`, `color_label`, `leads_to`, `on`, `unit_word`, `color_pink`, `gender_unisex`, `statement`, `causes`, `motivated_by`, `important` |
| n12 | constraint | t1:s7 | white color → `color_label::<key>` | `color_label`*, `color_pink`, `outshines`, `unit_word`, `visual_contrast`, `constraint_exclude_flowery_language`, `illuminates`, `sultana`, `constraint_respectful`, `gender_unisex`, `rule_category_product_attribute_value`, `constraint_include_character_attribute_list` |
| n13 | claim | t1:s8 | Harry is nice | `comfortable`, `enables`, `style_catchy`, `style_persuasive`, `important`, `leads_to`, `outcome`, `statement`, `motivated_by`, `causes`, `recommended`, `role_friend` |
| n14 | object | t1:s8 | Harry | `topic_spider_man_2`, `united_kingdom`, `on`, `art_story`, `right_of`, `new_york_university`, `dom_safari`, `resource_chiller`, `resource_sink`, `role_friend`, `path_ipython_core_magics_basic_py`, `resource_heater` |
| n15 | reasoning | t1:s9 | rule: if something is white and cold, then it is blue | `state_cold`*, `color_label`, `then`*, `sultana`, `supports`, `in_front_of`, `rejects`, `right_of`, `contrast`, `prohibited`, `rule_category_state_value`, `state_warm` |
| n16 | constraint | t1:s9 | white color → `color_label::<key>` | `color_label`*, `color_pink`, `outshines`, `unit_word`, `visual_contrast`, `constraint_exclude_flowery_language`, `illuminates`, `sultana`, `constraint_respectful`, `gender_unisex`, `rule_category_product_attribute_value`, `constraint_include_character_attribute_list` |
| n17 | constraint | t1:s9 | blue color → `color_label::<key>` | `color_label`*, `color_pink`, `yakuza`, `grape_merlot`, `sultana`, `constraint_respectful`, `lettuce`, `constraint_exclude_flowery_language`, `dried_fruit`, `grape_sauvignon_blanc`, `grape_pinot_noir`, `constraint_exclude_liberation_theme` |
| n18 | reasoning | t1:s10 | rule: if Bob is nice, then Bob is furry | `then`*, `comfortable`, `style_catchy`, `supports`, `rejects`, `constraint_respectful`, `in_front_of`, `contrast`, `subject`, `tone_silly`, `tone_polite`, `associated_with` |
| n19 | reasoning | t1:s11 | rule: if something is big and cold, then it is blue | `state_cold`*, `color_label`, `then`*, `supports`, `rejects`, `in_front_of`, `style_catchy`, `right_of`, `contrast`, `outshines`, `metric_order_late`, `size_small` |
| n20 | constraint | t1:s11 | blue color → `color_label::<key>` | `color_label`*, `color_pink`, `yakuza`, `grape_merlot`, `sultana`, `constraint_respectful`, `lettuce`, `constraint_exclude_flowery_language`, `dried_fruit`, `grape_sauvignon_blanc`, `grape_pinot_noir`, `constraint_exclude_liberation_theme` |
| n21 | reasoning | t1:s12 | rule: if Fiona is furry, then Fiona is white | `then`*, `char_female`, `stereotype`, `yarn`, `event_sadie_adler_unmasking`, `color_pink`, `sym_pandas_testing_assert_almost_equal`, `supports`, `style_catchy`, `rejects`, `rule_category_product_attribute_value`, `color_label` |
| n22 | constraint | t1:s12 | white color → `color_label::<key>` | `color_label`*, `color_pink`, `outshines`, `unit_word`, `visual_contrast`, `constraint_exclude_flowery_language`, `illuminates`, `sultana`, `constraint_respectful`, `gender_unisex`, `rule_category_product_attribute_value`, `constraint_include_character_attribute_list` |
| n23 | reasoning | t1:s13 | rule: if something is big, then it is cold | `state_cold`*, `then`*, `unit_fahrenheit`, `supports`, `rejects`, `style_catchy`, `contrast`, `size_small`, `state_warm`, `size_large`, `size_tall`, `weather_condition` |
| n24 | reasoning | t1:s14 | rule: if Bob is blue and nice, then Bob is cold | `state_cold`*, `then`*, `style_catchy`, `in_front_of`, `supports`, `color_label`, `constraint_respectful`, `right_of`, `contrast`, `rejects`, `rule_category_state_value`, `state_dirty` |
| n25 | constraint | t1:s14 | blue color → `color_label::<key>` | `color_label`*, `color_pink`, `yakuza`, `grape_merlot`, `sultana`, `constraint_respectful`, `lettuce`, `constraint_exclude_flowery_language`, `dried_fruit`, `grape_sauvignon_blanc`, `grape_pinot_noir`, `constraint_exclude_liberation_theme` |
| n26 | reasoning | t1:s15 | rule: if something is blue and cold, then it is nice | `state_cold`*, `color_label`, `then`*, `style_catchy`, `condition_perfect`, `supports`, `rejects`, `comfortable`, `contrast`, `constraint_respectful`, `right_of`, `rule_category_state_value` |
| n27 | constraint | t1:s15 | blue color → `color_label::<key>` | `color_label`*, `color_pink`, `yakuza`, `grape_merlot`, `sultana`, `constraint_respectful`, `lettuce`, `constraint_exclude_flowery_language`, `dried_fruit`, `grape_sauvignon_blanc`, `grape_pinot_noir`, `constraint_exclude_liberation_theme` |
| n28 | reasoning | t1:s16 | rule: if something is white, then it is big | `then`*, `color_label`, `rejects`, `supports`, `unit_word`, `outshines`, `contrast`, `unit_sentence`, `size_small`, `size_large`, `size_queen`, `revises` |
| n29 | constraint | t1:s16 | white color → `color_label::<key>` | `color_label`*, `color_pink`, `outshines`, `unit_word`, `visual_contrast`, `constraint_exclude_flowery_language`, `illuminates`, `sultana`, `constraint_respectful`, `gender_unisex`, `rule_category_product_attribute_value`, `constraint_include_character_attribute_list` |
| n30 | speech_act | t1:s17 | asks to evaluate the truth value of a statement | `ask`*, `statement`*, `respond`, `confirm`, `failure`, `supports`, `test_condition`, `inform`, `assert_multinomial_scorer`, `considered`, `motivated_by`, `propose` |
| n31 | constraint | t1:s17 | rely only on the provided theory | `constraint_realistic`, `subject`, `constraint_respectful`, `constraint_budget_limited`, `constraint_exclude_flowery_language`, `supports`, `constraint_include_character_attribute_list`, `regression_case`, `failure`, `rejects`, `constraint_exclude_liberation_theme`, `constraint_beginner` |
| n32 | constraint | t1:s17 | answer must be True, False, or Unknown | `constraint_realistic`, `right_of`, `constraint_respectful`, `in_front_of`, `constraint_exclude_flowery_language`, `constraint_budget_limited`, `failure`, `rejects`, `metric_order_late`, `constraint_include_character_attribute_list`, `respond`*, `constraint_beginner` |
| n33 | claim | t1:s18 | statement to evaluate: Bob is not blue | `enables`, `statement`*, `outcome`, `causes`, `failure`, `color_label`, `test_condition`, `leads_to`, `recommended`, `assert_multinomial_scorer`, `motivated_by`, `important` |
| n34 | negation | t1:s18 | Bob is not blue | `color_label`, `negation`, `topic_spider_man_2`, `grape_thompson_seedless`, `rejects`, `state_dirty`, `constraint_exclude_flowery_language`, `grape_merlot`, `sultana`, `exclude`, `decline`, `mug` |
| n35 | constraint | t1:s18 | blue color → `color_label::<key>` | `color_label`*, `color_pink`, `yakuza`, `grape_merlot`, `sultana`, `constraint_respectful`, `lettuce`, `constraint_exclude_flowery_language`, `dried_fruit`, `grape_sauvignon_blanc`, `grape_pinot_noir`, `constraint_exclude_liberation_theme` |

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
- failure.system → platform_label
- chill.destination → object_label
- weather_condition.location → country
- heat.destination → object_label
- run_tests.target → platform_label
- regression_case.framework → platform_label
- requirement.value → platform_label
- activity.object → object_label, food_label, animal_label
- activity.location → country
- activity.instrument → object_label, platform_label
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

**rule_attributes_and_generate** (v19/rule/attributes-and-generate; rule governing art_story)

Attribute entries name arguments; legality/types come from each operation, not global membership. GENERATE uses the spec's core fields; retained artifact profiles return STRING. Numeric/list results need explicit profiles. Legacy itinerary fields expand to TERM constraints: duration/duration_unit → duration(amount,unit); stop_min_per_day/stop_requirement → minimum_per_period(class,count,period=unit_day), never an inferred temple class; max_walk_duration/unit → maximum_between_stops(activity="walk",amount,unit). No legacy shorthand is enabled. Old events/character_properties/transformations become explicitly scoped TERM constraints. Message purpose is TERM, not send_email.content: GENERATE exact STRING content, then send. Report opaque fallback separately.

**rule_category_artifact_value** (v19/rule/category/artifact-value; rule governing art_story)

STRING artifact class for GENERATE.target. art_story says what kind of artifact to produce, not what occurs in its plot.

**rule_category_character_property_value** (v19/rule/category/character-property-value; rule governing char_female)

TERM-described trait/style. Use constraints and explicit inclusion/scope; do not use an ungoverned character_properties attribute.

**rule_category_code_value** (v19/rule/category/code-value; rule governing path_ipython_core_magics_basic_py)

path_/sym_ remain STRING identities; migrated chg_/assert_ are TERM constructors. Do not recover an exact file path by guessing from underscores.

**rule_category_constraint_value** (v19/rule/category/constraint-value; rule governing constraint_exclude_flowery_language)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_descriptive_value** (v19/rule/category/descriptive-value; rule governing dom_safari)

STRING modifier/domain label; never a free-form proposition. dom_sgi needs its intended referent established before semantically dependent use.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; rule governing unit_word)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing resource_sink)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_event_value** (v19/rule/category/event-value; rule governing event_sadie_adler_unmasking)

TERM-described narrative event, not a recorded EVENT. Require inclusion explicitly when generating a story.

**rule_category_location_name** (v19/rule/category/location-name; rule governing united_kingdom)

STRING location descriptor. A `table` surface is not the generated artifact category art_table.

**rule_category_metric_value** (v19/rule/category/metric-value; rule governing metric_order_late)

STRING metric identity, not a Boolean value. Uptime and response time need numeric observations with units; order-late is Boolean-valued. Do not type every metric as BOOL.

**rule_category_product_attribute_value** (v19/rule/category/product-attribute-value; candidate)

STRING color/size/product-market facets. gender_women describes a product category, not an assertion about a person's gender.

**rule_category_recipient_value** (v19/rule/category/recipient-value; rule governing role_professor)

STRING roles or explicit named recipients. A role is not an exact person's identity. Keep an explicit name where substituting a role loses information.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing in_front_of)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_state_value** (v19/rule/category/state-value; candidate)

STRING condition used in selection. state_warm does not command heat; “hot” is not automatically synonymous with “warm.”

**rule_category_style_value** (v19/rule/category/style-value; rule governing style_catchy)

STRING production style. style_narrative does not establish that described events occurred.

**rule_category_tone_value** (v19/rule/category/tone-value; rule governing tone_empathetic)

STRING register. tone_urgent describes urgency, not a concrete deadline.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_spider_man_2)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_composites_general** (v19/rule/composites-general; rule governing constraint_exclude_flowery_language)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_operations_general** (v19/rule/operations-general; rule governing chill)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_support_primitives_general** (v19/rule/support-primitives-general; rule governing subject)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- chill | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Chill using the stated resource; same identity.  ⟵ candidate
- heat | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Heat using the stated resource; same identity. Selecting a warm object does not imply heating it.  ⟵ candidate
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

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ dependency of event_sadie_adler_unmasking
- character_trait | constructor | TERM character_trait(property: STRING, value: STRING / NUMBER) -> TERM | A character attribute | not: Not a claim about a real person  ⟵ candidate
- conditional | constructor | TERM conditional(condition: TERM, consequence: TERM) -> TERM | Constructs a structured conditional proposition term connecting a condition and consequence. descriptive logic structure. | aliases: if_then  ⟵ candidate
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ candidate
- illuminates | constructor | TERM illuminates(target: STRING / TERM, source: STRING / TERM) -> TERM | Constructs a description of directional illumination where a light source casts light onto a target body. | not: an ambient color state or reflection (use reflects_light) | aliases: illuminates, shines on, shining towards  ⟵ candidate
- include | constructor | TERM include(item: STRING / TERM) -> TERM | Require the identified content/item | not: Not permission to invent an instance in a recorded trace  ⟵ dependency of constraint_include_character_attribute_list
- negation | constructor | TERM negation(target: TERM) -> TERM | Constructs a descriptive semantic negation of a target descriptive proposition or condition term. | not: Check's runtime Boolean operator NOT or a speech-act decline | aliases: not, does not, negation, absence of  ⟵ candidate
- outshines | constructor | TERM outshines(brighter: STRING / TERM, dimmer: STRING / TERM) -> TERM | Constructs a description of relative visual brightness where a brighter light source overpowers the perceived brightness of a dimmer object. | not: an absolute numeric brightness measurement | aliases: outshines, overpowers brightness, drowns out light  ⟵ candidate
- regression_case | constructor | TERM regression_case(framework: STRING / ATOM[platform_label], modifier: STRING, relation: STRING) -> TERM | A regression scenario specifying affected framework, condition and relation | not: Does not invent a passing test or exact implementation  ⟵ candidate
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ dependency of constraint_respectful
- sequence | constructor | TERM sequence(items: LIST[TERM]) -> TERM | Ordered described activities/content | not: Not unordered conjunction  ⟵ dependency of event_sadie_adler_unmasking
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ candidate
- test_condition | constructor | TERM test_condition(condition: STRING, expected: BOOL) -> TERM | A testable condition with the expected Boolean outcome | not: Expected outcome is not an observed result  ⟵ candidate
- visual_contrast | constructor | TERM visual_contrast(background: STRING / TERM, foreground: STRING / TERM) -> TERM | Constructs a descriptive term representing the optical contrast between a foreground object and its surrounding background environment. | not: a rhetorical claim link (use LINK contrast) | aliases: visual contrast, contrast against, contrast with background  ⟵ candidate
- weather_condition | constructor | TERM weather_condition(condition: STRING, location?: STRING / TERM / ATOM[country], severity?: STRING) -> TERM | A structured descriptor of atmospheric or weather phenomena such as wind, rain, or storm at an optional location; asserts nothing. | not: state_cold or state_warm (thermal states of physical objects) or occurred (past factual occurrence assertion) | aliases: weather, storm_condition, atmospheric_condition  ⟵ candidate

### composites

- char_female | composite | character-property-value | TERM char_female() -> TERM | Female gender. | = character_trait(property="gender", value="female") | aliases: female  ⟵ candidate
- assert_multinomial_scorer | composite | code-value | TERM assert_multinomial_scorer() -> TERM | Assertion that multinomial probabilistic scoring succeeds. | = test_condition(condition="multinomial_probabilistic_scoring", expected=TRUE)  ⟵ candidate
- constraint_beginner | composite | constraint-value | TERM constraint_beginner() -> TERM | Targeted at beginners. | = requirement(property="audience_expertise", value="beginner")  ⟵ candidate
- constraint_budget_limited | composite | constraint-value | TERM constraint_budget_limited() -> TERM | Limited budget. | = requirement(property="budget_limited", value=TRUE)  ⟵ candidate
- constraint_comprehensive | composite | constraint-value | TERM constraint_comprehensive() -> TERM | Must be comprehensive. | = requirement(property="comprehensive", value=TRUE)  ⟵ candidate
- constraint_exclude_flowery_language | composite | constraint-value | TERM constraint_exclude_flowery_language() -> TERM | Avoid flowery language. | = exclude(item="flowery_language")  ⟵ candidate
- constraint_exclude_liberation_theme | composite | constraint-value | TERM constraint_exclude_liberation_theme() -> TERM | Avoid liberation theme. | = exclude(item="liberation_theme")  ⟵ candidate
- constraint_include_character_attribute_list | composite | constraint-value | TERM constraint_include_character_attribute_list() -> TERM | Include character attributes. | = include(item="character_attribute_list")  ⟵ candidate
- constraint_realistic | composite | constraint-value | TERM constraint_realistic() -> TERM | Must be realistic. | = requirement(property="realistic", value=TRUE)  ⟵ candidate
- constraint_respectful | composite | constraint-value | TERM constraint_respectful() -> TERM | Must be respectful. | = requirement(property="respectful", value=TRUE)  ⟵ candidate
- event_sadie_adler_unmasking | composite | event-value | TERM event_sadie_adler_unmasking() -> TERM | Sadie Adler taking off her hat and peeling skin. | = sequence(items=[activity(verb="remove", actor="Sadie Adler", object="hat"), activity(verb="peel", actor="Sadie Adler", object="skin")])  ⟵ candidate
- topic_greatest_cricketer_of_all_time | composite | topic-value | TERM topic_greatest_cricketer_of_all_time() -> TERM | Greatest cricketer of all time. | = subject(kind="cricketer", qualifier=requirement(property="rank_by_greatness", value=1), time="all_time")  ⟵ candidate

### claim relations

- associated_with | claim_relation | CLAIM associated_with(subject: STRING / TERM, concept: STRING / TERM) | Asserts a cultural, semantic, or historical association between a subject and concept. association claim. | aliases: linked_to, correlated_with  ⟵ candidate
- attribute_claim | claim_relation | CLAIM attribute_claim(subject: STRING / TERM / ATOM[platform_label], property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) | Asserts that a subject possesses a named property evaluated to a specific primitive or structured value. general property attribution claim. | aliases: property_value, word_property, has_property, property attribution  ⟵ related to statement
- causes | claim_relation | CLAIM causes(cause: CLAIM / TERM, effect: CLAIM) | Asserts a direct causal relationship producing an effect proposition. causal assertion. | aliases: produces  ⟵ candidate
- comfortable | claim_relation | CLAIM comfortable(person: TERM, value: BOOL) | Asserts whether a person or animal is comfortable in a situation. affective/state claim. | aliases: is_comfortable  ⟵ candidate
- considered | claim_relation | CLAIM considered(subject: TERM) | Asserts that an agent or speaker evaluated or entertained a specific candidate term or concept. subject is the evaluated term. | aliases: evaluated, weighed  ⟵ candidate
- enables | claim_relation | CLAIM enables(condition: TERM / CLAIM, outcome: TERM / CLAIM) | Asserts that an enabling condition or capability facilitates an outcome. enabling condition. | aliases: facilitates, allows  ⟵ candidate
- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ candidate
- has_state | claim_relation | CLAIM has_state(subject: TERM, state: STRING) | Asserts that an entity is currently in a physical, thermal, or operational state. state must be a valid state descriptor string. | aliases: in_state, state_is  ⟵ related to statement
- important | claim_relation | CLAIM important(target: TERM) | Asserts that a concept, activity, or condition is important or significant. evaluative importance claim. | aliases: significant  ⟵ candidate
- leads_to | claim_relation | CLAIM leads_to(cause: TERM, effect: TERM) | Asserts a conceptual consequence or progression from cause to effect. progression relation. | aliases: results_in  ⟵ candidate
- motivated_by | claim_relation | CLAIM motivated_by(claim: CLAIM, motive: STRING / TERM) | Asserts that an action, rule, or claim is motivated by an underlying motive or goal. motive explanation. | aliases: rationale_is  ⟵ candidate
- occurred_recently | claim_relation | CLAIM occurred_recently(target: CLAIM) | Asserts temporal recency of an asserted occurrence or claim. temporal recency qualifier. | aliases: recently_happened  ⟵ candidate
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ candidate
- prohibited | claim_relation | CLAIM prohibited(subject: STRING / TERM, location: STRING / TERM, condition?: STRING / TERM) | Asserts that a subject is prohibited from a location or activity under specified conditions. deontic prohibition claim. | aliases: forbidden, banned_from  ⟵ candidate
- recommended | claim_relation | CLAIM recommended(target: TERM / CLAIM) | Asserts an advisory recommendation that an activity or measure is advisable. advisory normative claim. | aliases: advisable  ⟵ candidate
- spatial_state | claim_relation | CLAIM spatial_state(relation: STRING, object: TERM, reference: TERM) | Asserts an observed spatial configuration between an object and a reference landmark. relation must specify spatial configuration. | aliases: placed_at, located_at  ⟵ related to statement
- statement | claim_relation | CLAIM statement(fact: TERM) | Foundational claim relation converting any descriptive TERM into an attributed, truth-evaluated assertion. universal fact assertion. | aliases: assert_fact, fact_claim, claim_statement  ⟵ candidate
- stereotype | claim_relation | CLAIM stereotype(target: STRING / TERM, trait: STRING / TERM) | Asserts that an attributed trait, generalization, or assumption about a demographic group or social category is a stereotype. | not: an individual character trait or verified fact | aliases: social_stereotype, generalization, bias  ⟵ candidate

### links

- contrast | link | LINK contrast(first: CLAIM, second: CLAIM) | Expresses rhetorical qualification, opposition, or contrast between two claims. link between claims. | aliases: qualification, however  ⟵ candidate
- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ candidate
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ candidate
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ candidate
- then | link | LINK then(previous: EVENT, next: EVENT) | Represents temporal sequence and succession between two events where next follows previous. previous and next must be event terms. | aliases: followed_by, after_which  ⟵ candidate

### values

- art_story | value | artifact-value | Narrative story.  ⟵ candidate
- path_ipython_core_magics_basic_py | value | code-value | File path to the IPython basic magics module. | not: an individual command line script or general config file | aliases: IPython/core/magics/basic.py, ipython_core_magics_basic_py  ⟵ candidate
- sym_pandas_testing_assert_almost_equal | value | code-value | Source code file path or exported symbol in scientific Python: sym_pandas_testing_assert_almost_equal. | aliases: sym_pandas_testing_assert_almost_equal  ⟵ candidate
- dom_safari | value | descriptive-value | Safari domain concept. | aliases: safari  ⟵ candidate
- yakuza | value | descriptive-value | Descriptive concept of yakuza in cultural and social contexts. | aliases: yakuza  ⟵ candidate
- unit_sentence | value | duration-unit-value | One grammatical sentence in text generation or constraint counting. | not: unit_paragraph (paragraph block) or unit_word (individual word) | aliases: sentence, sentences  ⟵ candidate
- unit_word | value | duration-unit-value | Rendered whitespace-delimited word. | aliases: words  ⟵ candidate
- bowtie | value | entity-name | Item or prop in joke/creative context: bowtie. | aliases: bowtie  ⟵ candidate
- bread | value | entity-name | A bread loaf or slice food object. | aliases: bread  ⟵ candidate
- cinnamon | value | entity-name | Ground or whole cinnamon culinary spice from Cinnamomum tree bark. | not: nutmeg, cloves, or other distinct spice varieties | aliases: cinnamon, ground cinnamon, cinnamon spice, cinnamon stick  ⟵ candidate
- dried_fruit | value | entity-name | Generic dried fruit food item. | not: fresh fruit or specific dried varieties like raisin or sultana | aliases: dried fruit, dried fruits  ⟵ candidate
- grape_merlot | value | entity-name | Merlot wine grape variety. | not: other red grape varieties such as grape_cabernet_sauvignon or grape_pinot_noir | aliases: Merlot, merlot grape  ⟵ candidate
- grape_pinot_noir | value | entity-name | Pinot Noir wine grape variety. | not: other red grape varieties such as grape_cabernet_sauvignon or grape_merlot | aliases: Pinot Noir, pinot noir grape  ⟵ candidate
- grape_sauvignon_blanc | value | entity-name | Sauvignon Blanc wine grape variety. | not: other white grape varieties such as grape_chardonnay | aliases: Sauvignon Blanc, sauvignon blanc grape  ⟵ candidate
- grape_thompson_seedless | value | entity-name | Thompson Seedless grape variety. | not: wine grape cultivars like grape_merlot or grape_chardonnay | aliases: Thompson Seedless, thompson seedless grape, sultana grape  ⟵ candidate
- lettuce | value | entity-name | A head of lettuce or leafy green vegetable food item. | not: food_label::tomato or food_label::potato (other vegetable items) | aliases: lettuce, head of lettuce, salad greens  ⟵ candidate
- mug | value | entity-name | Drinking cup. | aliases: mug  ⟵ candidate
- resource_chiller | value | entity-name | Canonical abstract chilling resource when no particular appliance is named.  ⟵ candidate
- resource_heater | value | entity-name | Canonical abstract heating resource when no particular appliance is named.  ⟵ candidate
- resource_sink | value | entity-name | Canonical abstract washing resource when no particular sink is named.  ⟵ candidate
- sultana | value | entity-name | Dried white seedless grape food product. | not: raisin (dark dried grape) or wine_grape | aliases: sultana, sultanas, golden raisin  ⟵ candidate
- yarn | value | entity-name | Item or prop in joke/creative context: yarn. | aliases: yarn  ⟵ candidate
- new_york_university | value | location-name | New York University institution or campus grounds. | aliases: nyu  ⟵ candidate
- united_kingdom | value | location-name | Geopolitical nation or sovereign state: United Kingdom (Great Britain). | not: locale_en_gb (a language/locale code, not a location) | aliases: United Kingdom, UK, Great Britain, Britain  ⟵ candidate
- metric_order_late | value | metric-value | Whether an order is late. | aliases: order is late, delayed  ⟵ candidate
- color_pink | value | product-attribute-value | Pink visual color qualifier. | not: color_label::red, color_label::purple, or other distinct color shades | aliases: pink, color_pink, blush pink, rose pink, pastel pink  ⟵ candidate
- condition_perfect | value | product-attribute-value | Product condition rating: perfect or mint physical and operational condition. | not: test_condition (software testing) or state_dirty (physical environmental state) | aliases: perfect, mint, pristine, flawless, like new  ⟵ candidate
- gender_unisex | value | product-attribute-value | Unisex. | aliases: unisex  ⟵ candidate
- size_large | value | product-attribute-value | Large size. | aliases: large, L  ⟵ candidate
- size_queen | value | product-attribute-value | Queen-size dimension classification for beds, mattresses, and bedding. | not: size_large (generic large apparel/goods size) or size_king | aliases: queen, queen size, Queen  ⟵ candidate
- size_small | value | product-attribute-value | Small size. | aliases: small, S  ⟵ candidate
- size_tall | value | product-attribute-value | Tall relative vertical dimension qualifier. | aliases: size_tall  ⟵ candidate
- role_friend | value | recipient-value | A friend of the user. | aliases: my friend  ⟵ candidate
- role_mother | value | recipient-value | The mother of the user. | not: role_sister or role_kids | aliases: my mom, mother, mom  ⟵ candidate
- role_professor | value | recipient-value | The user's professor/instructor. | aliases: my professor, teacher  ⟵ candidate
- role_sister | value | recipient-value | Sister participant role in family/event context. | aliases: sister  ⟵ candidate
- behind | value | spatial-relation | Positioned behind.  ⟵ candidate
- in_front_of | value | spatial-relation | Positioned in front of. | aliases: in front of  ⟵ candidate
- left_of | value | spatial-relation | To the left of. | aliases: left of  ⟵ candidate
- next_to | value | spatial-relation | Adjacent to. | aliases: beside  ⟵ candidate
- on | value | spatial-relation | Resting atop. | aliases: on top of  ⟵ candidate
- right_of | value | spatial-relation | To the right of. | aliases: right of  ⟵ candidate
- state_clean | value | state-value | Clean condition. | aliases: clean  ⟵ candidate
- state_cold | value | state-value | Cold or chilled condition. | aliases: cold, chilled  ⟵ candidate
- state_dirty | value | state-value | Dirty condition. | aliases: dirty  ⟵ candidate
- state_warm | value | state-value | Warm or heated condition. | aliases: warm, hot  ⟵ candidate
- style_catchy | value | style-value | Catchy, attention-grabbing style. | aliases: catchy  ⟵ candidate
- style_persuasive | value | style-value | Persuasive/argumentative style. | aliases: persuasive  ⟵ candidate
- tone_empathetic | value | tone-value | Conveys empathy/understanding. | aliases: sympathetically  ⟵ candidate
- tone_polite | value | tone-value | Courteous, respectful register. | aliases: politely, kindly  ⟵ candidate
- tone_silly | value | tone-value | Playful, lighthearted, or silly conversational tone. | aliases: silly  ⟵ candidate
- topic_baldurs_gate_3 | value | topic-value | Baldur's Gate 3.  ⟵ candidate
- topic_politics | value | topic-value | Politics.  ⟵ candidate
- topic_spider_man_2 | value | topic-value | Marvel's Spider-Man 2.  ⟵ candidate
- unit_fahrenheit | value | unit-value | Standard unit of temperature measurement on the Fahrenheit scale. | not: qualitative thermal states (use state_warm or state_cold) or duration units (use unit_minute, etc.) | aliases: Fahrenheit, deg F, degrees Fahrenheit, degrees F, F  ⟵ candidate
