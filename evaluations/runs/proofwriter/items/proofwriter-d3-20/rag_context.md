# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 35 needs (decomposition: llm), 172 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | speech_act | t1:s1 | introduce a set of premises or theory | `respond`, `propose`, `subject`, `inform`, `ask`, `supports`, `example_of`, `confirm`, `express_interest`, `in_front_of`, `conjunction`, `topic_school_work_routine` |
| n2 | claim | t1:s2 | Bob is cold | `state_cold`*, `state_dirty`, `motivated_by`, `statement`, `enables`, `chill`, `leads_to`, `outcome`, `important`, `causes`, `state_warm`, `constrained_by` |
| n3 | object | t1:s2, t1:s3, t1:s4, t1:s5, t1:s6 | Bob | `resource_sink`, `bread`, `in_front_of`, `role_professor`, `behind`, `right_of`, `on`, `left_of`, `pencil`, `topic_spider_man_2`, `bowtie`, `resource_chiller` |
| n4 | object | t1:s2, t1:s10, t1:s12, t1:s17 | cold | `state_cold`*, `resource_chiller`, `chill`, `heat`, `unit_fahrenheit`, `bread`, `state_warm`, `state_dirty`, `cinnamon`, `mittens`, `ice_cream`, `weather_condition` |
| n5 | claim | t1:s3 | Bob is nice | `style_catchy`, `enables`, `tone_silly`, `tone_polite`, `leads_to`, `outcome`, `statement`, `role_professor`, `important`, `condition_perfect`, `motivated_by`, `comfortable` |
| n6 | object | t1:s3, t1:s14, t1:s15 | nice | `style_catchy`, `tone_polite`, `condition_perfect`, `tone_silly`, `tone_empathetic`, `resource_chiller`, `resource_sink`, `well_wishes`, `state_clean`, `comfortable`, `tone_urgent`, `resource_heater` |
| n7 | claim | t1:s4 | Bob is quiet | `unaware`, `enables`, `outcome`, `tone_silly`, `leads_to`, `tone_neutral`, `statement`, `occurred_recently`, `motivated_by`, `grape_thompson_seedless`, `comfortable`, `important` |
| n8 | object | t1:s4, t1:s14, t1:s16, t1:s18 | quiet | `chill`, `tone_polite`, `tone_silly`, `state_cold`, `tone_neutral`, `tone_empathetic`, `tone_urgent`, `resource_chiller`, `tone_casual`, `unaware`, `resource_sink`, `format_plain_text` |
| n9 | claim | t1:s5 | Bob is round | `shape_round`*, `in_front_of`, `shape_oval`, `enables`, `topic_baldurs_gate_3`, `leads_to`, `motivated_by`, `statement`, `important`, `shape_triangular`, `rule_category_shape_value`, `behind` |
| n10 | object | t1:s5, t1:s9, t1:s13, t1:s15, t1:s17, t1:s20 | round | `shape_round`*, `rule_category_shape_value`, `shape_oval`, `shape_square`, `shape_triangular`, `shape_rectangular`, `left_of`, `corner`, `between`, `unit_day`, `turn`, `resource_chiller` |
| n11 | claim | t1:s6 | Bob is white | `enables`, `unit_word`, `outcome`, `role_professor`, `leads_to`, `in_front_of`, `statement`, `state_dirty`, `motivated_by`, `occurred_recently`, `pencil`, `important` |
| n12 | object | t1:s6, t1:s12, t1:s13, t1:s16 | white → `color_label::<key>` | `color_label`*, `sultana`, `unit_word`, `state_dirty`, `on`, `dulce_de_leche`, `gender_unisex`, `resource_sink`, `under`, `wall`, `state_clean`, `dulce_de_nata` |
| n13 | claim | t1:s7 | Fiona is rough | `state_dirty`, `character_trait`, `style_catchy`, `enables`, `outcome`, `leads_to`, `tone_empathetic`, `statement`, `occurred_recently`, `important`, `recommended`, `spoon` |
| n14 | object | t1:s7, t1:s8, t1:s20 | Fiona | `chill`, `style_catchy`, `event_sadie_adler_unmasking`, `on`, `right_of`, `yarn`, `role_sister`, `role_mother`, `bowtie`, `next_to`, `art_story`, `role_agent` |
| n15 | object | t1:s7, t1:s14, t1:s16, t1:s18 | rough | `mattress`, `state_dirty`, `tone_empathetic`, `shape_oval`, `tone_silly`, `shape_round`, `pencil`, `behind`, `spatula`, `resource_chiller`, `spoon`, `resource_sink` |
| n16 | claim | t1:s8 | Fiona is smart | `style_catchy`, `enables`, `style_persuasive`, `outcome`, `leads_to`, `test_condition`, `statement`, `recommended`, `important`, `motivated_by`, `comfortable`, `occurred_recently` |
| n17 | object | t1:s8, t1:s11 | smart | `style_catchy`, `tone_polite`, `state_clean`, `tone_urgent`, `role_colleague`, `tone_silly`, `resource_chiller`, `resource_sink`, `role_user`, `art_plan`, `constitutional_ai`, `resource_heater` |
| n18 | claim | t1:s9 | Gary is round | `shape_round`*, `enables`, `topic_baldurs_gate_3`, `shape_oval`, `leads_to`, `in_front_of`, `rule_category_shape_value`, `shape_square`, `on`, `motivated_by`, `statement`, `important` |
| n19 | object | t1:s9 | Gary | `chill`, `right_of`, `in_front_of`, `topic_baldurs_gate_3`, `on`, `left_of`, `next_to`, `state_dirty`, `topic_greatest_cricketer_of_all_time`, `topic_politics`, `subject`, `resource_sink` |
| n20 | claim | t1:s10 | Harry is cold | `state_cold`*, `cinnamon`, `statement`, `motivated_by`, `chill`, `enables`, `leads_to`, `important`, `outcome`, `constrained_by`, `causes`, `recommended` |
| n21 | object | t1:s10, t1:s11 | Harry | `topic_spider_man_2`, `united_kingdom`, `on`, `right_of`, `art_story`, `new_york_university`, `role_friend`, `resource_chiller`, `dom_safari`, `resource_sink`, `path_ipython_core_magics_basic_py`, `coffee_maker` |
| n22 | claim | t1:s11 | Harry is smart | `important`, `style_catchy`, `style_persuasive`, `enables`, `comfortable`, `motivated_by`, `leads_to`, `statement`, `test_condition`, `outcome`, `role_colleague`, `recommended` |
| n23 | reasoning | t1:s12 | if someone is white, then they are cold | `state_cold`*, `then`*, `rejects`, `stereotype`, `supports`, `color_label`, `state_dirty`, `unit_word`, `contrast`, `gender_unisex`, `cinnamon`, `state_warm` |
| n24 | reasoning | t1:s13 | if someone is round, then they are white | `shape_round`*, `rule_category_shape_value`, `then`*, `rejects`, `supports`, `shape_oval`, `unit_word`, `color_label`, `shape_square`, `in_front_of`, `contrast`, `left_of` |
| n25 | reasoning | t1:s14 | if someone is rough and quiet, then they are nice | `then`*, `comfortable`, `tone_polite`, `rejects`, `tone_silly`, `supports`, `tone_empathetic`, `style_catchy`, `topic_profanity`, `style_persuasive`, `contrast`, `constraint_respectful` |
| n26 | reasoning | t1:s15 | if someone is nice, then they are round | `shape_round`*, `rule_category_shape_value`, `then`*, `comfortable`, `style_catchy`, `tone_polite`, `tone_silly`, `supports`, `style_persuasive`, `rejects`, `contrast`, `constraint_respectful` |
| n27 | reasoning | t1:s16 | if someone is rough and white, then they are quiet | `then`*, `comfortable`, `rejects`, `unaware`, `supports`, `tone_empathetic`, `tone_polite`, `tone_silly`, `topic_profanity`, `style_catchy`, `contrast`, `unit_word` |
| n28 | reasoning | t1:s17 | if someone is cold, then they are round | `state_cold`*, `shape_round`*, `then`*, `rejects`, `supports`, `in_front_of`, `shape_oval`, `event_camper_in_sludge_pit`, `rule_category_shape_value`, `contrast`, `left_of`, `shape_square` |
| n29 | reasoning | t1:s18 | if someone is rough, then they are quiet | `then`*, `comfortable`, `rejects`, `tone_silly`, `supports`, `tone_empathetic`, `tone_polite`, `unaware`, `topic_profanity`, `style_catchy`, `contrast`, `style_persuasive` |
| n30 | speech_act | t1:s19 | ask a question about the truth value of a statement | `ask`*, `statement`*, `respond`, `confirm`, `failure`, `supports`, `inform`, `motivated_by`, `personal_values`, `propose`, `rejects`, `contrast` |
| n31 | action | t1:s19 | evaluate the truth value of a statement | `statement`*, `failure`, `test_condition`, `run_tests`, `supports`, `assert_multinomial_scorer`, `decision`, `considered`, `motivated_by`, `calculation`, `rejects`, `confirm` |
| n32 | constraint | t1:s19 | base the evaluation only on the provided theory | `subject`, `supports`, `test_condition`, `constraint_budget_limited`, `constraint_respectful`, `regression_case`, `constraint_realistic`, `decision`, `considered`, `constraint_exclude_flowery_language`, `constraint_include_character_attribute_list`, `constraint_beginner` |
| n33 | constraint | t1:s19 | answer must be True, False, or Unknown | `constraint_realistic`, `constraint_respectful`, `right_of`, `in_front_of`, `failure`, `rejects`, `metric_order_late`, `constraint_budget_limited`, `constraint_exclude_flowery_language`, `respond`*, `unaware`, `confirm` |
| n34 | claim | t1:s20 | Fiona is not round | `shape_round`*, `enables`, `shape_triangular`, `leads_to`, `rule_category_shape_value`, `topic_baldurs_gate_3`, `shape_rectangular`, `motivated_by`, `shape_oval`, `shape_square`, `outcome`, `event_sadie_adler_unmasking` |
| n35 | negation | t1:s20 | Fiona is not round | `shape_round`*, `rule_category_shape_value`, `constraint_exclude_flowery_language`, `test_condition`, `negation`, `shape_triangular`, `topic_baldurs_gate_3`, `shape_rectangular`, `shape_oval`, `shape_square`, `event_sadie_adler_unmasking`, `assert_multinomial_scorer` |

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
- heat.destination → object_label
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

**rule_structural_constructs** (v19/rule/structural-constructs; core)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; rule governing supports)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_attributes_and_generate** (v19/rule/attributes-and-generate; rule governing art_story)

Attribute entries name arguments; legality/types come from each operation, not global membership. GENERATE uses the spec's core fields; retained artifact profiles return STRING. Numeric/list results need explicit profiles. Legacy itinerary fields expand to TERM constraints: duration/duration_unit → duration(amount,unit); stop_min_per_day/stop_requirement → minimum_per_period(class,count,period=unit_day), never an inferred temple class; max_walk_duration/unit → maximum_between_stops(activity="walk",amount,unit). No legacy shorthand is enabled. Old events/character_properties/transformations become explicitly scoped TERM constraints. Message purpose is TERM, not send_email.content: GENERATE exact STRING content, then send. Report opaque fallback separately.

**rule_category_artifact_value** (v19/rule/category/artifact-value; rule governing art_story)

STRING artifact class for GENERATE.target. art_story says what kind of artifact to produce, not what occurs in its plot.

**rule_category_code_value** (v19/rule/category/code-value; rule governing path_ipython_core_magics_basic_py)

path_/sym_ remain STRING identities; migrated chg_/assert_ are TERM constructors. Do not recover an exact file path by guessing from underscores.

**rule_category_constraint_value** (v19/rule/category/constraint-value; rule governing constraint_respectful)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_descriptive_value** (v19/rule/category/descriptive-value; rule governing constitutional_ai)

STRING modifier/domain label; never a free-form proposition. dom_sgi needs its intended referent established before semantically dependent use.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; rule governing unit_day)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing resource_sink)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_event_value** (v19/rule/category/event-value; rule governing event_sadie_adler_unmasking)

TERM-described narrative event, not a recorded EVENT. Require inclusion explicitly when generating a story.

**rule_category_format_value** (v19/rule/category/format-value; rule governing format_plain_text)

STRING format. format_email is layout, not the action send_email.

**rule_category_location_name** (v19/rule/category/location-name; rule governing corner)

STRING location descriptor. A `table` surface is not the generated artifact category art_table.

**rule_category_metric_value** (v19/rule/category/metric-value; rule governing metric_order_late)

STRING metric identity, not a Boolean value. Uptime and response time need numeric observations with units; order-late is Boolean-valued. Do not type every metric as BOOL.

**rule_category_product_attribute_value** (v19/rule/category/product-attribute-value; rule governing condition_perfect)

STRING color/size/product-market facets. gender_women describes a product category, not an assertion about a person's gender.

**rule_category_recipient_value** (v19/rule/category/recipient-value; rule governing role_professor)

STRING roles or explicit named recipients. A role is not an exact person's identity. Keep an explicit name where substituting a role loses information.

**rule_category_shape_value** (v19/rule/category/shape-value; candidate)

STRING geometry. shape_round may select a circular object; it does not imply color or dimensions.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing in_front_of)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_state_value** (v19/rule/category/state-value; rule governing state_cold)

STRING condition used in selection. state_warm does not command heat; “hot” is not automatically synonymous with “warm.”

**rule_category_style_value** (v19/rule/category/style-value; rule governing style_catchy)

STRING production style. style_narrative does not establish that described events occurred.

**rule_category_tone_value** (v19/rule/category/tone-value; rule governing tone_silly)

STRING register. tone_urgent describes urgency, not a concrete deadline.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_school_work_routine)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_composites_general** (v19/rule/composites-general; rule governing topic_school_work_routine)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_operations_general** (v19/rule/operations-general; rule governing chill)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_supplemental_general** (v19/rule/supplemental-general; rule governing coffee_maker)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; rule governing subject)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- chill | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Chill using the stated resource; same identity.  ⟵ candidate
- heat | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Heat using the stated resource; same identity. Selecting a warm object does not imply heating it.  ⟵ candidate
- run_tests | operation | operation-vocabulary | (target: STRING / ATOM[platform_label], assertion?: TERM) -> BOOL | Run the selected project's tests, optionally checking the specified assertion. TRUE means the declared test condition passed, not overall software correctness.  ⟵ candidate
- turn | operation | operation-vocabulary | (direction: STRING) -> void | Rotate agent body/view orientation. direction is typically left, right, or angle. | aliases: rotate, turn_around  ⟵ candidate
- walk | operation | operation-vocabulary | (destination: STRING / TERM / ATOM[object_label], relation?: STRING) -> void | Locomote towards a target destination or landmark. destination must identify a valid entity or location. | aliases: move_to, go_to, navigate_to  ⟵ related to then

### speech acts

- acknowledge | speech_act | operation-vocabulary | UTTER acknowledge(target: CLAIM / TERM) | Acknowledge receipt/awareness; does not imply agreement.  ⟵ candidate
- ask | speech_act | operation-vocabulary | UTTER ask(target: TERM, or a sufficiently precise topic: STRING / TERM) | Request information/advice; not an assertion of an answer. | aliases: ask, how should  ⟵ candidate
- confirm | speech_act | operation-vocabulary | UTTER confirm(target: CLAIM) | Confirm the proposition; its evidence/status remains explicit.  ⟵ candidate
- express_interest | speech_act | operation-vocabulary | UTTER express_interest(target: STRING / TERM) | Speech act expressing conversational interest or engagement in a topic. speech act in dialogic traces. | aliases: show_interest  ⟵ candidate
- inform | speech_act | operation-vocabulary | UTTER inform(target: CLAIM) | Present the proposition; preserve its holder/status.  ⟵ candidate
- propose | speech_act | operation-vocabulary | UTTER propose(target: TERM) | Suggest an action/idea; does not record it as performed.  ⟵ candidate
- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ dependency of constrained_by
- calculation | constructor | TERM calculation(inputs: LIST[TERM], operation: STRING, result?: TERM) -> TERM | Constructs a descriptive representation of an arithmetic or algorithmic calculation step with inputs, operation identifier, and optional resulting value. | not: an executed runtime action or factual claim of outcome | aliases: math_operation, compute_step  ⟵ candidate
- character_trait | constructor | TERM character_trait(property: STRING, value: STRING / NUMBER) -> TERM | A character attribute | not: Not a claim about a real person  ⟵ candidate
- conjunction | constructor | TERM conjunction(items: LIST[TERM]) -> TERM | All described components apply | not: Does not imply temporal order  ⟵ candidate
- decision | constructor | TERM decision(activity: TERM) -> TERM | A decision whose content is the described activity | not: Not proof it was carried out  ⟵ candidate
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ dependency of constraint_exclude_flowery_language
- include | constructor | TERM include(item: STRING / TERM) -> TERM | Require the identified content/item | not: Not permission to invent an instance in a recorded trace  ⟵ dependency of constraint_include_character_attribute_list
- negation | constructor | TERM negation(target: TERM) -> TERM | Constructs a descriptive semantic negation of a target descriptive proposition or condition term. | not: Check's runtime Boolean operator NOT or a speech-act decline | aliases: not, does not, negation, absence of  ⟵ candidate
- regression_case | constructor | TERM regression_case(framework: STRING / ATOM[platform_label], modifier: STRING, relation: STRING) -> TERM | A regression scenario specifying affected framework, condition and relation | not: Does not invent a passing test or exact implementation  ⟵ candidate
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ dependency of topic_greatest_cricketer_of_all_time
- sequence | constructor | TERM sequence(items: LIST[TERM]) -> TERM | Ordered described activities/content | not: Not unordered conjunction  ⟵ dependency of event_sadie_adler_unmasking
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ candidate
- test_condition | constructor | TERM test_condition(condition: STRING, expected: BOOL) -> TERM | A testable condition with the expected Boolean outcome | not: Expected outcome is not an observed result  ⟵ candidate
- weather_condition | constructor | TERM weather_condition(condition: STRING, location?: STRING / TERM / ATOM[country], severity?: STRING) -> TERM | A structured descriptor of atmospheric or weather phenomena such as wind, rain, or storm at an optional location; asserts nothing. | not: state_cold or state_warm (thermal states of physical objects) or occurred (past factual occurrence assertion) | aliases: weather, storm_condition, atmospheric_condition  ⟵ candidate
- well_wishes | constructor | TERM well_wishes(recipient?: STRING / TERM, sentiment?: STRING) -> TERM | Constructs a conversational discourse term representing well-wishes, good luck expressions, or parting encouragement. | not: a salutation greeting (use greeting) or apology (use apologize) | aliases: good_luck, best_wishes, encouragement  ⟵ candidate

### composites

- assert_multinomial_scorer | composite | code-value | TERM assert_multinomial_scorer() -> TERM | Assertion that multinomial probabilistic scoring succeeds. | = test_condition(condition="multinomial_probabilistic_scoring", expected=TRUE)  ⟵ candidate
- constraint_beginner | composite | constraint-value | TERM constraint_beginner() -> TERM | Targeted at beginners. | = requirement(property="audience_expertise", value="beginner")  ⟵ candidate
- constraint_budget_limited | composite | constraint-value | TERM constraint_budget_limited() -> TERM | Limited budget. | = requirement(property="budget_limited", value=TRUE)  ⟵ candidate
- constraint_exclude_flowery_language | composite | constraint-value | TERM constraint_exclude_flowery_language() -> TERM | Avoid flowery language. | = exclude(item="flowery_language")  ⟵ candidate
- constraint_include_character_attribute_list | composite | constraint-value | TERM constraint_include_character_attribute_list() -> TERM | Include character attributes. | = include(item="character_attribute_list")  ⟵ candidate
- constraint_realistic | composite | constraint-value | TERM constraint_realistic() -> TERM | Must be realistic. | = requirement(property="realistic", value=TRUE)  ⟵ candidate
- constraint_respectful | composite | constraint-value | TERM constraint_respectful() -> TERM | Must be respectful. | = requirement(property="respectful", value=TRUE)  ⟵ candidate
- event_camper_in_sludge_pit | composite | event-value | TERM event_camper_in_sludge_pit() -> TERM | Campers interacting in a sludge pit. | = activity(verb="interact", actor="campers", location="sludge_pit")  ⟵ candidate
- event_sadie_adler_unmasking | composite | event-value | TERM event_sadie_adler_unmasking() -> TERM | Sadie Adler taking off her hat and peeling skin. | = sequence(items=[activity(verb="remove", actor="Sadie Adler", object="hat"), activity(verb="peel", actor="Sadie Adler", object="skin")])  ⟵ candidate
- topic_greatest_cricketer_of_all_time | composite | topic-value | TERM topic_greatest_cricketer_of_all_time() -> TERM | Greatest cricketer of all time. | = subject(kind="cricketer", qualifier=requirement(property="rank_by_greatness", value=1), time="all_time")  ⟵ candidate
- topic_profanity | composite | topic-value | TERM topic_profanity() -> TERM | A composite term representing the topic of profanity. | = subject(kind="profanity") | not: potential_harms (which is generic) | aliases: profanity  ⟵ candidate
- topic_school_work_routine | composite | topic-value | TERM topic_school_work_routine() -> TERM | School and work routine. | = subject(kind="routine", qualifier=conjunction(items=[subject(kind="school"), subject(kind="work")]))  ⟵ candidate

### claim relations

- associated_with | claim_relation | CLAIM associated_with(subject: STRING / TERM, concept: STRING / TERM) | Asserts a cultural, semantic, or historical association between a subject and concept. association claim. | aliases: linked_to, correlated_with  ⟵ candidate
- attribute_claim | claim_relation | CLAIM attribute_claim(subject: STRING / TERM / ATOM[platform_label], property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) | Asserts that a subject possesses a named property evaluated to a specific primitive or structured value. general property attribution claim. | aliases: property_value, word_property, has_property, property attribution  ⟵ related to statement
- causes | claim_relation | CLAIM causes(cause: CLAIM / TERM, effect: CLAIM) | Asserts a direct causal relationship producing an effect proposition. causal assertion. | aliases: produces  ⟵ candidate
- comfortable | claim_relation | CLAIM comfortable(person: TERM, value: BOOL) | Asserts whether a person or animal is comfortable in a situation. affective/state claim. | aliases: is_comfortable  ⟵ candidate
- considered | claim_relation | CLAIM considered(subject: TERM) | Asserts that an agent or speaker evaluated or entertained a specific candidate term or concept. subject is the evaluated term. | aliases: evaluated, weighed  ⟵ candidate
- constrained_by | claim_relation | CLAIM constrained_by(activity: TERM, constraint: TERM) | Asserts that an activity or operation is governed or restricted by a constraint. governance/constraint claim. | aliases: restricted_by  ⟵ candidate
- enables | claim_relation | CLAIM enables(condition: TERM / CLAIM, outcome: TERM / CLAIM) | Asserts that an enabling condition or capability facilitates an outcome. enabling condition. | aliases: facilitates, allows  ⟵ candidate
- example_of | claim_relation | CLAIM example_of(example: TERM, concept: TERM) | Asserts that an instance or term exemplifies a general concept, pattern, or category. example and concept are descriptive terms. | aliases: exemplifies, instance_of  ⟵ candidate
- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ candidate
- has_state | claim_relation | CLAIM has_state(subject: TERM, state: STRING) | Asserts that an entity is currently in a physical, thermal, or operational state. state must be a valid state descriptor string. | aliases: in_state, state_is  ⟵ related to statement
- important | claim_relation | CLAIM important(target: TERM) | Asserts that a concept, activity, or condition is important or significant. evaluative importance claim. | aliases: significant  ⟵ candidate
- leads_to | claim_relation | CLAIM leads_to(cause: TERM, effect: TERM) | Asserts a conceptual consequence or progression from cause to effect. progression relation. | aliases: results_in  ⟵ candidate
- motivated_by | claim_relation | CLAIM motivated_by(claim: CLAIM, motive: STRING / TERM) | Asserts that an action, rule, or claim is motivated by an underlying motive or goal. motive explanation. | aliases: rationale_is  ⟵ candidate
- occurred_recently | claim_relation | CLAIM occurred_recently(target: CLAIM) | Asserts temporal recency of an asserted occurrence or claim. temporal recency qualifier. | aliases: recently_happened  ⟵ candidate
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ candidate
- reason_for | claim_relation | CLAIM reason_for(subject: CLAIM / TERM, reason: STRING / TERM) | Asserts an explanatory reason for a policy, belief, or state of affairs. explanatory reason. | aliases: basis_for  ⟵ candidate
- recommended | claim_relation | CLAIM recommended(target: TERM / CLAIM) | Asserts an advisory recommendation that an activity or measure is advisable. advisory normative claim. | aliases: advisable  ⟵ candidate
- spatial_state | claim_relation | CLAIM spatial_state(relation: STRING, object: TERM, reference: TERM) | Asserts an observed spatial configuration between an object and a reference landmark. relation must specify spatial configuration. | aliases: placed_at, located_at  ⟵ related to statement
- statement | claim_relation | CLAIM statement(fact: TERM) | Foundational claim relation converting any descriptive TERM into an attributed, truth-evaluated assertion. universal fact assertion. | aliases: assert_fact, fact_claim, claim_statement  ⟵ candidate
- stereotype | claim_relation | CLAIM stereotype(target: STRING / TERM, trait: STRING / TERM) | Asserts that an attributed trait, generalization, or assumption about a demographic group or social category is a stereotype. | not: an individual character trait or verified fact | aliases: social_stereotype, generalization, bias  ⟵ candidate
- unaware | claim_relation | CLAIM unaware(person: STRING / TERM, topic: STRING / TERM) | Asserts epistemic lack of awareness regarding a topic, fact, or event. epistemic state. | aliases: ignorant_of  ⟵ candidate

### links

- contrast | link | LINK contrast(first: CLAIM, second: CLAIM) | Expresses rhetorical qualification, opposition, or contrast between two claims. link between claims. | aliases: qualification, however  ⟵ candidate
- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ candidate
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ core
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ candidate
- then | link | LINK then(previous: EVENT, next: EVENT) | Represents temporal sequence and succession between two events where next follows previous. previous and next must be event terms. | aliases: followed_by, after_which  ⟵ candidate

### values

- art_plan | value | artifact-value | Actionable plan.  ⟵ candidate
- art_story | value | artifact-value | Narrative story.  ⟵ candidate
- path_ipython_core_magics_basic_py | value | code-value | File path to the IPython basic magics module. | not: an individual command line script or general config file | aliases: IPython/core/magics/basic.py, ipython_core_magics_basic_py  ⟵ candidate
- constitutional_ai | value | descriptive-value | Concept of rule-based constitutional training and self-critique principles in AI alignment. | aliases: constitutional_ai  ⟵ candidate
- dom_safari | value | descriptive-value | Safari domain concept. | aliases: safari  ⟵ candidate
- personal_values | value | descriptive-value | Concept of personal moral beliefs and subjective ethical commitments. | aliases: personal_values  ⟵ candidate
- unit_day | value | duration-unit-value | Day. | aliases: days  ⟵ candidate
- unit_word | value | duration-unit-value | Rendered whitespace-delimited word. | aliases: words  ⟵ candidate
- bowtie | value | entity-name | Item or prop in joke/creative context: bowtie. | aliases: bowtie  ⟵ candidate
- bread | value | entity-name | A bread loaf or slice food object. | aliases: bread  ⟵ candidate
- cinnamon | value | entity-name | Ground or whole cinnamon culinary spice from Cinnamomum tree bark. | not: nutmeg, cloves, or other distinct spice varieties | aliases: cinnamon, ground cinnamon, cinnamon spice, cinnamon stick  ⟵ candidate
- coffee_maker | value | entity-name | A coffee-making appliance; not automatically a heating resource  ⟵ candidate
- dulce_de_leche | value | entity-name | Sweet caramelized milk confection or dessert spread: dulce de leche. | not: cheese or dulce_de_nata | aliases: dulce de leche, dulce_de_leche  ⟵ candidate
- dulce_de_nata | value | entity-name | Clotted cream milk confection or dessert item: dulce de nata. | not: dulce_de_leche or cheese | aliases: dulce de nata, dulce_de_nata  ⟵ candidate
- grape_thompson_seedless | value | entity-name | Thompson Seedless grape variety. | not: wine grape cultivars like grape_merlot or grape_chardonnay | aliases: Thompson Seedless, thompson seedless grape, sultana grape  ⟵ candidate
- ice_cream | value | entity-name | Frozen dessert food item: ice cream. | not: entity_desserts or entity_sweet_food (generic menu categories) | aliases: ice cream, ice_cream  ⟵ candidate
- mattress | value | entity-name | A mattress cushion or sleeping surface object. | not: bed (a bed furniture surface or frame) or object_label::pillow | aliases: mattress, mattresses  ⟵ candidate
- mittens | value | entity-name | Item or prop in joke/creative context: mittens. | aliases: mittens  ⟵ candidate
- pencil | value | entity-name | A pencil writing instrument. | aliases: pencil  ⟵ candidate
- resource_chiller | value | entity-name | Canonical abstract chilling resource when no particular appliance is named.  ⟵ candidate
- resource_heater | value | entity-name | Canonical abstract heating resource when no particular appliance is named.  ⟵ candidate
- resource_sink | value | entity-name | Canonical abstract washing resource when no particular sink is named.  ⟵ candidate
- spatula | value | entity-name | A kitchen utensil with a broad, flat, and flexible blade used for lifting, flipping, or spreading food. | not: knife (cutting utensil) or spoon (scooping utensil) | aliases: spatula, turner, flipper  ⟵ candidate
- spoon | value | entity-name | An eating or cooking utensil. | aliases: spoon  ⟵ candidate
- sultana | value | entity-name | Dried white seedless grape food product. | not: raisin (dark dried grape) or wine_grape | aliases: sultana, sultanas, golden raisin  ⟵ candidate
- yarn | value | entity-name | Item or prop in joke/creative context: yarn. | aliases: yarn  ⟵ candidate
- format_plain_text | value | format-value | Unstructured prose text. | aliases: plain text  ⟵ candidate
- corner | value | location-name | A corner area.  ⟵ candidate
- new_york_university | value | location-name | New York University institution or campus grounds. | aliases: nyu  ⟵ candidate
- united_kingdom | value | location-name | Geopolitical nation or sovereign state: United Kingdom (Great Britain). | not: locale_en_gb (a language/locale code, not a location) | aliases: United Kingdom, UK, Great Britain, Britain  ⟵ candidate
- wall | value | location-name | A room boundary wall surface. | aliases: wall  ⟵ candidate
- metric_order_late | value | metric-value | Whether an order is late. | aliases: order is late, delayed  ⟵ candidate
- color_pink | value | product-attribute-value | Pink visual color qualifier. | not: color_label::red, color_label::purple, or other distinct color shades | aliases: pink, color_pink, blush pink, rose pink, pastel pink  ⟵ candidate
- condition_perfect | value | product-attribute-value | Product condition rating: perfect or mint physical and operational condition. | not: test_condition (software testing) or state_dirty (physical environmental state) | aliases: perfect, mint, pristine, flawless, like new  ⟵ candidate
- gender_unisex | value | product-attribute-value | Unisex. | aliases: unisex  ⟵ candidate
- role_agent | value | recipient-value | The assistant. | aliases: you, the assistant  ⟵ candidate
- role_colleague | value | recipient-value | A coworker of the user. | aliases: my colleague, coworker  ⟵ candidate
- role_friend | value | recipient-value | A friend of the user. | aliases: my friend  ⟵ candidate
- role_mother | value | recipient-value | The mother of the user. | not: role_sister or role_kids | aliases: my mom, mother, mom  ⟵ candidate
- role_professor | value | recipient-value | The user's professor/instructor. | aliases: my professor, teacher  ⟵ candidate
- role_sister | value | recipient-value | Sister participant role in family/event context. | aliases: sister  ⟵ candidate
- role_user | value | recipient-value | The requesting human. | aliases: me, I  ⟵ candidate
- shape_oval | value | shape-value | Oval. | aliases: oval  ⟵ candidate
- shape_rectangular | value | shape-value | Rectangular. | aliases: rectangular, rectangle  ⟵ candidate
- shape_round | value | shape-value | Circular/round. | aliases: round, circular  ⟵ candidate
- shape_square | value | shape-value | Square. | aliases: square  ⟵ candidate
- shape_triangular | value | shape-value | Triangular. | aliases: triangular, triangle  ⟵ candidate
- behind | value | spatial-relation | Positioned behind.  ⟵ candidate
- between | value | spatial-relation | Positioned between or in the middle of reference entities. | not: next_to or in_front_of | aliases: between, in the middle of, middle of, center of  ⟵ candidate
- in_front_of | value | spatial-relation | Positioned in front of. | aliases: in front of  ⟵ candidate
- left_of | value | spatial-relation | To the left of. | aliases: left of  ⟵ candidate
- next_to | value | spatial-relation | Adjacent to. | aliases: beside  ⟵ candidate
- on | value | spatial-relation | Resting atop. | aliases: on top of  ⟵ candidate
- right_of | value | spatial-relation | To the right of. | aliases: right of  ⟵ candidate
- under | value | spatial-relation | Beneath. | aliases: below  ⟵ candidate
- state_clean | value | state-value | Clean condition. | aliases: clean  ⟵ candidate
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
- topic_pickup_lines | value | topic-value | Pickup lines.  ⟵ candidate
- topic_politics | value | topic-value | Politics.  ⟵ candidate
- topic_spider_man_2 | value | topic-value | Marvel's Spider-Man 2.  ⟵ candidate
- unit_fahrenheit | value | unit-value | Standard unit of temperature measurement on the Fahrenheit scale. | not: qualitative thermal states (use state_warm or state_cold) or duration units (use unit_minute, etc.) | aliases: Fahrenheit, deg F, degrees Fahrenheit, degrees F, F  ⟵ candidate
