# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 41 needs (decomposition: llm), 164 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | speech_act | t1:s1 | Introduce a set of logical premises or theory | `respond`, `supports`, `propose`, `subject`, `ask`, `conditional`, `inform`, `constraint_realistic`, `topic_school_work_routine`, `failure`, `rule_structural_constructs`, `motivated_by` |
| n2 | object | t1:s2 | Anne | `on`, `right_of`, `role_mother`, `next_to`, `art_story`, `resource_sink`, `role_sister`, `role_daughter`, `art_plan`, `in_front_of`, `left_of`, `resource_chiller` |
| n3 | claim | t1:s2 | Anne is nice | `style_catchy`, `tone_polite`, `enables`, `tone_silly`, `recommended`, `well_wishes`, `important`, `occurred_recently`, `leads_to`, `comfortable`, `color_pink`, `outcome` |
| n4 | negation | t1:s2 | Anne is not nice | `constraint_exclude_flowery_language`, `negation`, `topic_profanity`, `tone_silly`, `topic_ai_earning_methods`, `event_sadie_adler_unmasking`, `char_female`, `potential_harms`, `exclude`, `style_catchy`, `opposes`, `object_label` |
| n5 | claim | t1:s3 | Anne is round | `shape_round`*, `shape_triangular`, `rule_category_shape_value`, `enables`, `recommended`, `shape_oval`, `on`, `topic_baldurs_gate_3`, `important`, `shape_rectangular`, `apple`, `leads_to` |
| n6 | claim | t1:s4 | Anne is white | `char_female`, `enables`, `gender_unisex`, `color_pink`, `unit_word`, `recommended`, `leads_to`, `occurred_recently`, `outcome`, `important`, `gender_women`, `color_label` |
| n7 | negation | t1:s4 | Anne is not white | `constraint_exclude_flowery_language`, `sultana`, `color_label`, `negation`, `color_pink`, `char_female`, `gender_unisex`, `rule_category_product_attribute_value`, `grape_thompson_seedless`, `exclude`, `event_sadie_adler_unmasking`, `gender_identity` |
| n8 | constraint | t1:s4 | white → `color_label::<key>` | `color_label`*, `unit_word`, `constraint_exclude_flowery_language`, `constraint_respectful`, `gender_unisex`, `sultana`, `art_short_text`, `on`, `state_dirty`, `constraint_budget_limited`, `constraint_realistic`, `dulce_de_nata` |
| n9 | claim | t1:s5 | Anne is young | `topic_profanity`, `enables`, `constraint_17_plus`, `recommended`, `art_short_text`, `occurred_recently`, `leads_to`, `role_sister`, `rule_support_primitives_general`, `role_daughter`, `outcome`, `important` |
| n10 | object | t1:s6 | Erin | `event_sadie_adler_unmasking`, `art_story`, `art_short_text`, `constitutional_ai`, `art_plan`, `potential_harms`, `art_social_post`, `resource_sink`, `role_sister`, `yarn`, `right_of`, `gender_unisex` |
| n11 | claim | t1:s6 | Erin is round | `shape_round`*, `shape_triangular`, `enables`, `recommended`, `rule_category_shape_value`, `topic_ai_earning_methods`, `event_sadie_adler_unmasking`, `topic_baldurs_gate_3`, `constitutional_ai`, `shape_oval`, `on`, `important` |
| n12 | object | t1:s7 | Fiona | `chill`, `event_sadie_adler_unmasking`, `style_catchy`, `role_sister`, `yarn`, `role_mother`, `on`, `art_story`, `bowtie`, `right_of`, `role_daughter`, `next_to` |
| n13 | claim | t1:s7 | Fiona is blue | `color_label`, `enables`, `recommended`, `color_pink`, `event_sadie_adler_unmasking`, `yarn`, `role_sister`, `outcome`, `leads_to`, `occurred_recently`, `role_mother`, `important` |
| n14 | constraint | t1:s7 | blue → `color_label::<key>` | `color_label`*, `constraint_respectful`, `constraint_exclude_flowery_language`, `sultana`, `dried_fruit`, `right_of`, `lettuce`, `on`, `grape_merlot`, `constraint_budget_limited`, `constraint_realistic`, `yakuza` |
| n15 | object | t1:s8 | Gary | `chill`, `right_of`, `on`, `topic_baldurs_gate_3`, `next_to`, `left_of`, `in_front_of`, `state_dirty`, `topic_politics`, `resource_sink`, `unit_sentence`, `resource_chiller` |
| n16 | claim | t1:s8 | Gary is young | `leads_to`, `topic_profanity`, `enables`, `constraint_17_plus`, `recommended`, `size_small`, `rule_support_primitives_general`, `occurred_recently`, `comfortable`, `important`, `on`, `outcome` |
| n17 | reasoning | t1:s9 | All nice people are not quiet | `tone_polite`, `tone_silly`, `comfortable`, `supports`, `tone_empathetic`, `rejects`, `revises`, `style_persuasive`, `well_wishes`, `style_catchy`, `contrast`, `foreigners` |
| n18 | negation | t1:s9 | Nice people are not quiet | `tone_polite`, `tone_silly`, `negation`, `well_wishes`, `tone_empathetic`, `style_persuasive`, `constraint_exclude_flowery_language`, `greeting`, `exclude`, `style_catchy`, `comfortable`, `decline` |
| n19 | reasoning | t1:s10 | All round people are quiet | `shape_round`*, `unaware`, `tone_silly`, `tone_polite`, `supports`, `rejects`, `rule_category_shape_value`, `tone_neutral`, `grape_thompson_seedless`, `rule_lexical_groups`, `revises`, `associated_with` |
| n20 | reasoning | t1:s11 | If Anne is nice then Anne is white | `then`*, `color_pink`, `char_female`, `supports`, `tone_polite`, `color_label`, `style_catchy`, `rule_category_product_attribute_value`, `tone_silly`, `rejects`, `revises`, `contrast` |
| n21 | constraint | t1:s11 | white → `color_label::<key>` | `color_label`*, `unit_word`, `constraint_exclude_flowery_language`, `constraint_respectful`, `gender_unisex`, `sultana`, `art_short_text`, `on`, `state_dirty`, `constraint_budget_limited`, `constraint_realistic`, `dulce_de_nata` |
| n22 | reasoning | t1:s12 | If someone is quiet then they are blue | `color_label`, `then`*, `unaware`, `tone_polite`, `tone_silly`, `supports`, `rejects`, `tone_empathetic`, `in_front_of`, `revises`, `contrast`, `outshines` |
| n23 | constraint | t1:s12 | blue → `color_label::<key>` | `color_label`*, `constraint_respectful`, `constraint_exclude_flowery_language`, `sultana`, `dried_fruit`, `right_of`, `lettuce`, `on`, `grape_merlot`, `constraint_budget_limited`, `constraint_realistic`, `yakuza` |
| n24 | reasoning | t1:s13 | If Fiona is white then Fiona is blue | `color_label`, `then`*, `sultana`, `color_pink`, `char_female`, `event_sadie_adler_unmasking`, `supports`, `rule_category_product_attribute_value`, `rejects`, `outshines`, `contrast`, `sym_pandas_testing_assert_almost_equal` |
| n25 | constraint | t1:s13 | white → `color_label::<key>` | `color_label`*, `unit_word`, `constraint_exclude_flowery_language`, `constraint_respectful`, `gender_unisex`, `sultana`, `art_short_text`, `on`, `state_dirty`, `constraint_budget_limited`, `constraint_realistic`, `dulce_de_nata` |
| n26 | constraint | t1:s13 | blue → `color_label::<key>` | `color_label`*, `constraint_respectful`, `constraint_exclude_flowery_language`, `sultana`, `dried_fruit`, `right_of`, `lettuce`, `on`, `grape_merlot`, `constraint_budget_limited`, `constraint_realistic`, `yakuza` |
| n27 | reasoning | t1:s14 | If someone is rough then they are young | `then`*, `topic_profanity`, `tone_silly`, `constraint_17_plus`, `supports`, `rejects`, `character_trait`, `tone_empathetic`, `style_catchy`, `state_dirty`, `tone_polite`, `associated_with` |
| n28 | reasoning | t1:s15 | If someone is nice and not blue then they are not rough | `color_label`, `then`*, `comfortable`, `tone_polite`, `constraint_respectful`, `style_catchy`, `supports`, `tone_silly`, `tone_empathetic`, `rejects`, `style_persuasive`, `topic_profanity` |
| n29 | negation | t1:s15 | Not blue | `color_label`, `negation`, `color_pink`, `grape_thompson_seedless`, `constraint_exclude_flowery_language`, `exclude`, `dried_fruit`, `art_short_text`, `sultana`, `decline`, `gender_unisex`, `raisin` |
| n30 | negation | t1:s15 | Not rough | `negation`, `style_catchy`, `state_dirty`, `constraint_exclude_flowery_language`, `exclude`, `rule_category_shape_value`, `weather_condition`, `decline`, `shape_oval`, `tone_casual`, `tone_polite`, `rejects` |
| n31 | constraint | t1:s15 | blue → `color_label::<key>` | `color_label`*, `constraint_respectful`, `constraint_exclude_flowery_language`, `sultana`, `dried_fruit`, `right_of`, `lettuce`, `on`, `grape_merlot`, `constraint_budget_limited`, `constraint_realistic`, `yakuza` |
| n32 | reasoning | t1:s16 | If someone is blue then they are rough | `color_label`, `then`*, `tone_silly`, `topic_profanity`, `supports`, `rejects`, `state_dirty`, `possesses`, `tone_empathetic`, `revises`, `contrast`, `associated_with` |
| n33 | constraint | t1:s16 | blue → `color_label::<key>` | `color_label`*, `constraint_respectful`, `constraint_exclude_flowery_language`, `sultana`, `dried_fruit`, `right_of`, `lettuce`, `on`, `grape_merlot`, `constraint_budget_limited`, `constraint_realistic`, `yakuza` |
| n34 | reasoning | t1:s17 | If Erin is young then Erin is white | `then`*, `color_pink`, `outshines`, `gender_unisex`, `supports`, `char_female`, `rejects`, `event_sadie_adler_unmasking`, `constraint_exclude_flowery_language`, `unit_word`, `revises`, `contrast` |
| n35 | constraint | t1:s17 | white → `color_label::<key>` | `color_label`*, `unit_word`, `constraint_exclude_flowery_language`, `constraint_respectful`, `gender_unisex`, `sultana`, `art_short_text`, `on`, `state_dirty`, `constraint_budget_limited`, `constraint_realistic`, `dulce_de_nata` |
| n36 | speech_act | t1:s18 | Ask a question about the truth value of a statement | `ask`*, `statement`*, `respond`, `confirm`, `failure`, `supports`, `inform`, `personal_values`, `acknowledge`, `constraint_realistic`, `contrast`, `motivated_by` |
| n37 | constraint | t1:s18 | Base the answer only on the provided theory | `respond`*, `extract`, `subject`, `constraint_exclude_flowery_language`, `topic_baldurs_gate_3`, `constraint_respectful`, `constraint_realistic`, `constraint_budget_limited`, `supports`, `constraint_beginner`, `constraint_comprehensive`, `failure` |
| n38 | constraint | t1:s18 | Answer must be True, False, or Unknown | `constraint_realistic`, `constraint_respectful`, `constraint_exclude_flowery_language`, `right_of`, `metric_order_late`, `unaware`, `constraint_budget_limited`, `failure`, `entity_flowers`, `constraint_comprehensive`, `respond`*, `constraint_beginner` |
| n39 | action | t1:s18 | Determine the truth value of a statement | `statement`*, `failure`, `test_condition`, `run_tests`, `assert_multinomial_scorer`, `supports`, `decision`, `considered`, `obligation`, `validates_parameter`, `has_style`, `motivated_by` |
| n40 | claim | t1:s19 | Erin is rough | `state_dirty`, `enables`, `style_catchy`, `potential_harms`, `recommended`, `event_sadie_adler_unmasking`, `occurred_recently`, `outcome`, `leads_to`, `tone_empathetic`, `important`, `genre_electronic` |
| n41 | negation | t1:s19 | Erin is not rough | `negation`, `constraint_exclude_flowery_language`, `character_trait`, `style_catchy`, `comfortable`, `event_sadie_adler_unmasking`, `gender_unisex`, `style_persuasive`, `exclude`, `rule_category_locale_value`, `rule_category_character_property_value`, `metric_compatibility` |

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
- run_tests.target → platform_label
- requirement.value → platform_label
- activity.object → object_label, food_label, animal_label
- activity.location → country
- activity.instrument → object_label, platform_label
- walk.destination → object_label
- attribute_claim.subject → platform_label
- attribute_claim.value → platform_label

## Retrieved records

### Shared rules that govern the records below (full text)

**rule_lexical_groups** (v19/rule/lexical-groups; candidate)

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

**rule_category_character_property_value** (v19/rule/category/character-property-value; candidate)

TERM-described trait/style. Use constraints and explicit inclusion/scope; do not use an ungoverned character_properties attribute.

**rule_category_code_value** (v19/rule/category/code-value; rule governing sym_pandas_testing_assert_almost_equal)

path_/sym_ remain STRING identities; migrated chg_/assert_ are TERM constructors. Do not recover an exact file path by guessing from underscores.

**rule_category_constraint_value** (v19/rule/category/constraint-value; rule governing constraint_realistic)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_descriptive_value** (v19/rule/category/descriptive-value; rule governing potential_harms)

STRING modifier/domain label; never a free-form proposition. dom_sgi needs its intended referent established before semantically dependent use.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; rule governing unit_word)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing resource_sink)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_event_value** (v19/rule/category/event-value; rule governing event_sadie_adler_unmasking)

TERM-described narrative event, not a recorded EVENT. Require inclusion explicitly when generating a story.

**rule_category_locale_value** (v19/rule/category/locale-value; candidate)

STRING locale. “English” alone does not always mean locale_en_us; preserve ambiguity.

**rule_category_metric_value** (v19/rule/category/metric-value; rule governing metric_order_late)

STRING metric identity, not a Boolean value. Uptime and response time need numeric observations with units; order-late is Boolean-valued. Do not type every metric as BOOL.

**rule_category_product_attribute_value** (v19/rule/category/product-attribute-value; candidate)

STRING color/size/product-market facets. gender_women describes a product category, not an assertion about a person's gender.

**rule_category_recipient_value** (v19/rule/category/recipient-value; rule governing role_mother)

STRING roles or explicit named recipients. A role is not an exact person's identity. Keep an explicit name where substituting a role loses information.

**rule_category_search_value** (v19/rule/category/search-value; rule governing genre_electronic)

STRING refinements rank_ / dir_ / cat_ / avail_ / genre_ are separate. rank_rating may fill rank_field; genre_label::comedy may not. “Cheapest” usually requires both rank_price and dir_asc, not rank_price alone.

**rule_category_shape_value** (v19/rule/category/shape-value; candidate)

STRING geometry. shape_round may select a circular object; it does not imply color or dimensions.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing on)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_state_value** (v19/rule/category/state-value; rule governing state_dirty)

STRING condition used in selection. state_warm does not command heat; “hot” is not automatically synonymous with “warm.”

**rule_category_style_value** (v19/rule/category/style-value; rule governing style_catchy)

STRING production style. style_narrative does not establish that described events occurred.

**rule_category_tone_value** (v19/rule/category/tone-value; rule governing tone_polite)

STRING register. tone_urgent describes urgency, not a concrete deadline.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_school_work_routine)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_composites_general** (v19/rule/composites-general; rule governing constraint_realistic)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_operations_general** (v19/rule/operations-general; rule governing chill)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_supplemental_general** (v19/rule/supplemental-general; rule governing extract)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; candidate)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- chill | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Chill using the stated resource; same identity.  ⟵ candidate
- extract | operation | operation-vocabulary | (target: LIST[REF[STRING]], limit: NUMBER) -> LIST[REF[STRING]] | First limit results, preserving order and identity; limit is a nonnegative integer; limit=1 is still a list  ⟵ candidate
- run_tests | operation | operation-vocabulary | (target: STRING / ATOM[platform_label], assertion?: TERM) -> BOOL | Run the selected project's tests, optionally checking the specified assertion. TRUE means the declared test condition passed, not overall software correctness.  ⟵ candidate
- turn | operation | operation-vocabulary | (direction: STRING) -> void | Rotate agent body/view orientation. direction is typically left, right, or angle. | aliases: rotate, turn_around  ⟵ related to then
- walk | operation | operation-vocabulary | (destination: STRING / TERM / ATOM[object_label], relation?: STRING) -> void | Locomote towards a target destination or landmark. destination must identify a valid entity or location. | aliases: move_to, go_to, navigate_to  ⟵ related to then

### speech acts

- acknowledge | speech_act | operation-vocabulary | UTTER acknowledge(target: CLAIM / TERM) | Acknowledge receipt/awareness; does not imply agreement.  ⟵ candidate
- ask | speech_act | operation-vocabulary | UTTER ask(target: TERM, or a sufficiently precise topic: STRING / TERM) | Request information/advice; not an assertion of an answer. | aliases: ask, how should  ⟵ candidate
- confirm | speech_act | operation-vocabulary | UTTER confirm(target: CLAIM) | Confirm the proposition; its evidence/status remains explicit.  ⟵ candidate
- decline | speech_act | operation-vocabulary | UTTER decline(target: TERM) | Decline the represented request/proposal; not negate every proposition within it.  ⟵ candidate
- inform | speech_act | operation-vocabulary | UTTER inform(target: CLAIM) | Present the proposition; preserve its holder/status.  ⟵ candidate
- propose | speech_act | operation-vocabulary | UTTER propose(target: TERM) | Suggest an action/idea; does not record it as performed.  ⟵ candidate
- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ dependency of topic_ai_earning_methods
- calculation | constructor | TERM calculation(inputs: LIST[TERM], operation: STRING, result?: TERM) -> TERM | Constructs a descriptive representation of an arithmetic or algorithmic calculation step with inputs, operation identifier, and optional resulting value. | not: an executed runtime action or factual claim of outcome | aliases: math_operation, compute_step  ⟵ candidate
- character_trait | constructor | TERM character_trait(property: STRING, value: STRING / NUMBER) -> TERM | A character attribute | not: Not a claim about a real person  ⟵ candidate
- conditional | constructor | TERM conditional(condition: TERM, consequence: TERM) -> TERM | Constructs a structured conditional proposition term connecting a condition and consequence. descriptive logic structure. | aliases: if_then  ⟵ candidate
- conjunction | constructor | TERM conjunction(items: LIST[TERM]) -> TERM | All described components apply | not: Does not imply temporal order  ⟵ candidate
- decision | constructor | TERM decision(activity: TERM) -> TERM | A decision whose content is the described activity | not: Not proof it was carried out  ⟵ candidate
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ candidate
- gender_identity | constructor | TERM gender_identity(identity: STRING) -> TERM | Constructs a descriptive term representing an individual's or demographic group's gender identity. | not: gender_women (product attribute) or char_female (fictional character trait) or identity (name/persona claim) | aliases: gender, gender_expression  ⟵ candidate
- greeting | constructor | TERM greeting(recipient: STRING) -> TERM | Constructs a conversational salutation greeting descriptor. conversational discourse term. | aliases: salutation  ⟵ candidate
- include | constructor | TERM include(item: STRING / TERM) -> TERM | Require the identified content/item | not: Not permission to invent an instance in a recorded trace  ⟵ dependency of constraint_include_character_attribute_list
- negation | constructor | TERM negation(target: TERM) -> TERM | Constructs a descriptive semantic negation of a target descriptive proposition or condition term. | not: Check's runtime Boolean operator NOT or a speech-act decline | aliases: not, does not, negation, absence of  ⟵ candidate
- obligation | constructor | TERM obligation(actor: STRING / TERM, activity: TERM) -> TERM | Constructs a deontic obligation description requiring an actor to perform an activity. actor and activity specified. | aliases: duty, mandatory_activity  ⟵ candidate
- outshines | constructor | TERM outshines(brighter: STRING / TERM, dimmer: STRING / TERM) -> TERM | Constructs a description of relative visual brightness where a brighter light source overpowers the perceived brightness of a dimmer object. | not: an absolute numeric brightness measurement | aliases: outshines, overpowers brightness, drowns out light  ⟵ candidate
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ dependency of constraint_realistic
- sequence | constructor | TERM sequence(items: LIST[TERM]) -> TERM | Ordered described activities/content | not: Not unordered conjunction  ⟵ dependency of event_sadie_adler_unmasking
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ candidate
- test_condition | constructor | TERM test_condition(condition: STRING, expected: BOOL) -> TERM | A testable condition with the expected Boolean outcome | not: Expected outcome is not an observed result  ⟵ candidate
- weather_condition | constructor | TERM weather_condition(condition: STRING, location?: STRING / TERM / ATOM[country], severity?: STRING) -> TERM | A structured descriptor of atmospheric or weather phenomena such as wind, rain, or storm at an optional location; asserts nothing. | not: state_cold or state_warm (thermal states of physical objects) or occurred (past factual occurrence assertion) | aliases: weather, storm_condition, atmospheric_condition  ⟵ candidate
- well_wishes | constructor | TERM well_wishes(recipient?: STRING / TERM, sentiment?: STRING) -> TERM | Constructs a conversational discourse term representing well-wishes, good luck expressions, or parting encouragement. | not: a salutation greeting (use greeting) or apology (use apologize) | aliases: good_luck, best_wishes, encouragement  ⟵ candidate

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
- topic_ai_earning_methods | composite | topic-value | TERM topic_ai_earning_methods() -> TERM | AI earning methods. | = subject(kind="methods", qualifier=activity(verb="earn", instrument="AI", object="income"))  ⟵ candidate
- topic_profanity | composite | topic-value | TERM topic_profanity() -> TERM | A composite term representing the topic of profanity. | = subject(kind="profanity") | not: potential_harms (which is generic) | aliases: profanity  ⟵ candidate
- topic_school_work_routine | composite | topic-value | TERM topic_school_work_routine() -> TERM | School and work routine. | = subject(kind="routine", qualifier=conjunction(items=[subject(kind="school"), subject(kind="work")]))  ⟵ candidate

### claim relations

- associated_with | claim_relation | CLAIM associated_with(subject: STRING / TERM, concept: STRING / TERM) | Asserts a cultural, semantic, or historical association between a subject and concept. association claim. | aliases: linked_to, correlated_with  ⟵ candidate
- attribute_claim | claim_relation | CLAIM attribute_claim(subject: STRING / TERM / ATOM[platform_label], property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) | Asserts that a subject possesses a named property evaluated to a specific primitive or structured value. general property attribution claim. | aliases: property_value, word_property, has_property, property attribution  ⟵ related to statement
- comfortable | claim_relation | CLAIM comfortable(person: TERM, value: BOOL) | Asserts whether a person or animal is comfortable in a situation. affective/state claim. | aliases: is_comfortable  ⟵ candidate
- considered | claim_relation | CLAIM considered(subject: TERM) | Asserts that an agent or speaker evaluated or entertained a specific candidate term or concept. subject is the evaluated term. | aliases: evaluated, weighed  ⟵ candidate
- enables | claim_relation | CLAIM enables(condition: TERM / CLAIM, outcome: TERM / CLAIM) | Asserts that an enabling condition or capability facilitates an outcome. enabling condition. | aliases: facilitates, allows  ⟵ candidate
- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ candidate
- has_state | claim_relation | CLAIM has_state(subject: TERM, state: STRING) | Asserts that an entity is currently in a physical, thermal, or operational state. state must be a valid state descriptor string. | aliases: in_state, state_is  ⟵ related to statement
- has_style | claim_relation | CLAIM has_style(target: CLAIM / EVENT / TERM, value: TERM / STRING) | Asserts that an artifact, utterance, or action possesses a designated style. style qualifier. | aliases: style_is  ⟵ candidate
- identity | claim_relation | CLAIM identity(subject: STRING / TERM, name: STRING) | Asserts the identified name or persona of an agent or entity. identity assertion. | aliases: agent_name  ⟵ dependency of gender_identity
- important | claim_relation | CLAIM important(target: TERM) | Asserts that a concept, activity, or condition is important or significant. evaluative importance claim. | aliases: significant  ⟵ candidate
- leads_to | claim_relation | CLAIM leads_to(cause: TERM, effect: TERM) | Asserts a conceptual consequence or progression from cause to effect. progression relation. | aliases: results_in  ⟵ candidate
- motivated_by | claim_relation | CLAIM motivated_by(claim: CLAIM, motive: STRING / TERM) | Asserts that an action, rule, or claim is motivated by an underlying motive or goal. motive explanation. | aliases: rationale_is  ⟵ candidate
- occurred_recently | claim_relation | CLAIM occurred_recently(target: CLAIM) | Asserts temporal recency of an asserted occurrence or claim. temporal recency qualifier. | aliases: recently_happened  ⟵ candidate
- opposes | claim_relation | CLAIM opposes(actor: STRING / TERM, subject: STRING / TERM) | Asserts that an actor opposes or objects to a practice, entity, or policy. opposition stance. | aliases: objects_to, against  ⟵ candidate
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ candidate
- possesses | claim_relation | CLAIM possesses(subject: STRING / TERM, item: TERM, value: BOOL) | Asserts whether a subject possesses or lacks a stated property, capability, or entity. possession assertion with boolean polarity. | aliases: holds_property  ⟵ candidate
- prohibited | claim_relation | CLAIM prohibited(subject: STRING / TERM, location: STRING / TERM, condition?: STRING / TERM) | Asserts that a subject is prohibited from a location or activity under specified conditions. deontic prohibition claim. | aliases: forbidden, banned_from  ⟵ related to obligation
- proposed_policy | claim_relation | CLAIM proposed_policy(policy: TERM, requirements: LIST[TERM]) | Asserts that a proposed policy framework comprises the specified requirement terms. policy must be a policy term. | aliases: policy_proposal  ⟵ related to obligation
- recommended | claim_relation | CLAIM recommended(target: TERM / CLAIM) | Asserts an advisory recommendation that an activity or measure is advisable. advisory normative claim. | aliases: advisable  ⟵ candidate
- spatial_state | claim_relation | CLAIM spatial_state(relation: STRING, object: TERM, reference: TERM) | Asserts an observed spatial configuration between an object and a reference landmark. relation must specify spatial configuration. | aliases: placed_at, located_at  ⟵ related to statement
- statement | claim_relation | CLAIM statement(fact: TERM) | Foundational claim relation converting any descriptive TERM into an attributed, truth-evaluated assertion. universal fact assertion. | aliases: assert_fact, fact_claim, claim_statement  ⟵ candidate
- unaware | claim_relation | CLAIM unaware(person: STRING / TERM, topic: STRING / TERM) | Asserts epistemic lack of awareness regarding a topic, fact, or event. epistemic state. | aliases: ignorant_of  ⟵ candidate
- validates_parameter | claim_relation | CLAIM validates_parameter(condition: STRING, entity: TERM, parameter: STRING) | Asserts that a code entity inspects or validates parameter names or types for a specified condition. | not: a runtime assertion test | aliases: inspects_parameter, checks_parameter, validates_parameter_names  ⟵ candidate

### links

- contrast | link | LINK contrast(first: CLAIM, second: CLAIM) | Expresses rhetorical qualification, opposition, or contrast between two claims. link between claims. | aliases: qualification, however  ⟵ candidate
- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ candidate
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ candidate
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ candidate
- then | link | LINK then(previous: EVENT, next: EVENT) | Represents temporal sequence and succession between two events where next follows previous. previous and next must be event terms. | aliases: followed_by, after_which  ⟵ candidate

### values

- art_plan | value | artifact-value | Actionable plan.  ⟵ candidate
- art_short_text | value | artifact-value | Short free text.  ⟵ candidate
- art_social_post | value | artifact-value | A short social media post or microblogging message. | not: art_short_text (general unstructured short prose) or art_story (narrative fiction) | aliases: tweet, tweets, social_media_post, microblog_post  ⟵ candidate
- art_story | value | artifact-value | Narrative story.  ⟵ candidate
- sym_pandas_testing_assert_almost_equal | value | code-value | Source code file path or exported symbol in scientific Python: sym_pandas_testing_assert_almost_equal. | aliases: sym_pandas_testing_assert_almost_equal  ⟵ candidate
- constraint_17_plus | value | constraint-value | Rated 17+ or mature.  ⟵ candidate
- constitutional_ai | value | descriptive-value | Concept of rule-based constitutional training and self-critique principles in AI alignment. | aliases: constitutional_ai  ⟵ candidate
- personal_values | value | descriptive-value | Concept of personal moral beliefs and subjective ethical commitments. | aliases: personal_values  ⟵ candidate
- potential_harms | value | descriptive-value | Concept of potential safety hazards, adverse outcomes, or risks in AI interaction. | aliases: potential_harms  ⟵ candidate
- yakuza | value | descriptive-value | Descriptive concept of yakuza in cultural and social contexts. | aliases: yakuza  ⟵ candidate
- unit_sentence | value | duration-unit-value | One grammatical sentence in text generation or constraint counting. | not: unit_paragraph (paragraph block) or unit_word (individual word) | aliases: sentence, sentences  ⟵ candidate
- unit_word | value | duration-unit-value | Rendered whitespace-delimited word. | aliases: words  ⟵ candidate
- apple | value | entity-name | An apple fruit item, typically an ingredient or interactive food object. | not: food_label::tomato or other fruits/vegetables | aliases: apple, apples, red apple, green apple, apple slice  ⟵ candidate
- bowtie | value | entity-name | Item or prop in joke/creative context: bowtie. | aliases: bowtie  ⟵ candidate
- dried_fruit | value | entity-name | Generic dried fruit food item. | not: fresh fruit or specific dried varieties like raisin or sultana | aliases: dried fruit, dried fruits  ⟵ candidate
- dulce_de_nata | value | entity-name | Clotted cream milk confection or dessert item: dulce de nata. | not: dulce_de_leche or cheese | aliases: dulce de nata, dulce_de_nata  ⟵ candidate
- entity_flowers | value | entity-name | Flowers, blossoms, or floral design elements. | not: constraint_exclude_flowery_language (a prose style constraint) or agricultural food items | aliases: flowers, floral, flower, floral decorations  ⟵ candidate
- grape_merlot | value | entity-name | Merlot wine grape variety. | not: other red grape varieties such as grape_cabernet_sauvignon or grape_pinot_noir | aliases: Merlot, merlot grape  ⟵ candidate
- grape_thompson_seedless | value | entity-name | Thompson Seedless grape variety. | not: wine grape cultivars like grape_merlot or grape_chardonnay | aliases: Thompson Seedless, thompson seedless grape, sultana grape  ⟵ candidate
- lettuce | value | entity-name | A head of lettuce or leafy green vegetable food item. | not: food_label::tomato or food_label::potato (other vegetable items) | aliases: lettuce, head of lettuce, salad greens  ⟵ candidate
- raisin | value | entity-name | Dried grape food item. | not: sultana (specifically dried white grape) or fresh wine_grape | aliases: raisin, raisins, dried grape  ⟵ candidate
- resource_chiller | value | entity-name | Canonical abstract chilling resource when no particular appliance is named.  ⟵ candidate
- resource_sink | value | entity-name | Canonical abstract washing resource when no particular sink is named.  ⟵ candidate
- sultana | value | entity-name | Dried white seedless grape food product. | not: raisin (dark dried grape) or wine_grape | aliases: sultana, sultanas, golden raisin  ⟵ candidate
- yarn | value | entity-name | Item or prop in joke/creative context: yarn. | aliases: yarn  ⟵ candidate
- metric_compatibility | value | metric-value | Compatibility status. | aliases: compatible  ⟵ candidate
- metric_order_late | value | metric-value | Whether an order is late. | aliases: order is late, delayed  ⟵ candidate
- color_pink | value | product-attribute-value | Pink visual color qualifier. | not: color_label::red, color_label::purple, or other distinct color shades | aliases: pink, color_pink, blush pink, rose pink, pastel pink  ⟵ candidate
- gender_unisex | value | product-attribute-value | Unisex. | aliases: unisex  ⟵ candidate
- gender_women | value | product-attribute-value | Women's/female-targeted. | aliases: women, female  ⟵ candidate
- size_small | value | product-attribute-value | Small size. | aliases: small, S  ⟵ candidate
- foreigners | value | recipient-value | Social, demographic, or institutional group: foreigners. | aliases: foreigners  ⟵ candidate
- role_daughter | value | recipient-value | Daughter participant role in family or travel context. | not: role_sister, role_mother, or generic role_kids | aliases: daughter, my daughter  ⟵ candidate
- role_mother | value | recipient-value | The mother of the user. | not: role_sister or role_kids | aliases: my mom, mother, mom  ⟵ candidate
- role_sister | value | recipient-value | Sister participant role in family/event context. | aliases: sister  ⟵ candidate
- genre_electronic | value | search-value | Music genre refinement: electronic music. | not: genre_pop_rock or general style descriptors | aliases: electronic, electronic music, EDM  ⟵ candidate
- shape_oval | value | shape-value | Oval. | aliases: oval  ⟵ candidate
- shape_rectangular | value | shape-value | Rectangular. | aliases: rectangular, rectangle  ⟵ candidate
- shape_round | value | shape-value | Circular/round. | aliases: round, circular  ⟵ candidate
- shape_triangular | value | shape-value | Triangular. | aliases: triangular, triangle  ⟵ candidate
- in_front_of | value | spatial-relation | Positioned in front of. | aliases: in front of  ⟵ candidate
- left_of | value | spatial-relation | To the left of. | aliases: left of  ⟵ candidate
- next_to | value | spatial-relation | Adjacent to. | aliases: beside  ⟵ candidate
- on | value | spatial-relation | Resting atop. | aliases: on top of  ⟵ candidate
- right_of | value | spatial-relation | To the right of. | aliases: right of  ⟵ candidate
- state_dirty | value | state-value | Dirty condition. | aliases: dirty  ⟵ candidate
- style_catchy | value | style-value | Catchy, attention-grabbing style. | aliases: catchy  ⟵ candidate
- style_persuasive | value | style-value | Persuasive/argumentative style. | aliases: persuasive  ⟵ candidate
- tone_casual | value | tone-value | Informal register. | aliases: casually  ⟵ candidate
- tone_empathetic | value | tone-value | Conveys empathy/understanding. | aliases: sympathetically  ⟵ candidate
- tone_neutral | value | tone-value | Plain, unmarked register.  ⟵ candidate
- tone_polite | value | tone-value | Courteous, respectful register. | aliases: politely, kindly  ⟵ candidate
- tone_silly | value | tone-value | Playful, lighthearted, or silly conversational tone. | aliases: silly  ⟵ candidate
- topic_baldurs_gate_3 | value | topic-value | Baldur's Gate 3.  ⟵ candidate
- topic_politics | value | topic-value | Politics.  ⟵ candidate
