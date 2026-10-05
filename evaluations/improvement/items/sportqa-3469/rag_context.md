# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 15 needs (decomposition: llm), 112 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | speech_act | t1:s1 | Introduce the task structure consisting of a main question and two sub-questions. | `respond`, `ask`, `rule_category_topic_value`, `correct`, `propose`, `subject`, `inform`, `topic_school_work_routine`, `express_interest`, `unit_item`, `offer`, `topic_politics` |
| n2 | object | t1:s1 | A main question and two sub-questions. | `respond`, `ask`, `topic_politics`, `topic_abortion`, `property_question`, `rule_category_topic_value`, `subject`, `entity_mains`, `topic_baldurs_gate_3`, `between`, `correct`, `under` |
| n3 | speech_act | t1:s2 | Inform that each question has multiple choices. | `ask`, `respond`, `inform`*, `constraint_single_choice`, `topic_abortion`, `propose_menu`, `varies_with`, `decline`, `propose`, `controversial`, `subject`, `select_option` |
| n4 | object | t1:s2 | Multiple choices for each question. | `constraint_single_choice`, `topic_abortion`, `constraint_comprehensive`, `ask`, `varies_with`, `topic_politics`, `rank_price`, `respond`, `controversial`, `property_question`, `style_persuasive`, `subject` |
| n5 | action | t1:s3 | Select the correct choices for each question. | `select_option`, `constraint_single_choice`, `respond`, `correct`*, `topic_abortion`, `select_filter`, `ask`, `sort`, `search_web`, `property_question`, `topic_greatest_cricketer_of_all_time`, `rank_price` |
| n6 | constraint | t1:s3 | Select all correct choices for each question. | `constraint_single_choice`, `topic_abortion`, `correct`*, `topic_greatest_cricketer_of_all_time`, `constraint_budget_limited`, `ask`, `constraint_respectful`, `constraint_include_character_attribute_list`, `constraint_beginner`, `select_option`, `constraint_realistic`, `constraint_comprehensive` |
| n7 | object | t1:s4 | Main question about the consequences of serious foul play in football. | `potential_harms`, `topic_greatest_cricketer_of_all_time`, `state_dirty`, `subject`, `topic_profanity`, `entity_mains`, `event_camper_in_sludge_pit`, `controversial`, `outcome`, `property_question`, `assert_multinomial_scorer`, `resource_chiller` |
| n8 | object | t1:s5, t1:s6, t1:s7, t1:s8 | Multiple choices (A, B, C, D) for the main question. | `constraint_single_choice`, `rank_price`, `constraint_comprehensive`, `respond`, `subject`, `topic_abortion`, `entity_mains`, `ask`, `style_persuasive`, `topic_pickup_lines`, `decision`, `property_question` |
| n9 | object | t1:s9 | Sub-question 1 about the repercussions of a red card for a team. | `credit_card`*, `assert_multinomial_scorer`, `varies_with`, `potential_harms`, `topic_current_events`, `role_respondent`, `role_support_team`, `gender_men`, `topic_politics`, `outcome`, `egift_card`, `metric_response_time` |
| n10 | object | t1:s10, t1:s11, t1:s12, t1:s13 | Multiple choices (A, B, C, D) for sub-question 1. | `constraint_single_choice`, `ask`, `constraint_comprehensive`, `respond`, `topic_abortion`, `unit_sentence`, `subject`, `rule_category_topic_value`, `rank_distance`, `constraint_budget_limited`, `rank_price`, `topic_pickup_lines` |
| n11 | object | t1:s14 | Sub-question 2 about the impacts of player suspension. | `potential_harms`, `event_camper_in_sludge_pit`, `constraint_beginner`, `obligation`, `varies_with`, `drop`, `on`, `topic_spider_man_2`, `rank_rating`, `property_question`, `unit_second`, `assert_multinomial_scorer` |
| n12 | object | t1:s15, t1:s16, t1:s17, t1:s18 | Multiple choices (A, B, C, D) for sub-question 2. | `constraint_single_choice`, `rule_category_topic_value`, `ask`, `respond`, `constraint_comprehensive`, `topic_abortion`, `rank_price`, `subject`, `rank_distance`, `unit_sentence`, `constraint_budget_limited`, `topic_pickup_lines` |
| n13 | constraint | t1:s19 | Provide the answer as a concatenation of the correct choices for each question. | `respond`*, `constraint_single_choice`, `constraint_respectful`, `constraint_comprehensive`, `correct`*, `role_respondent`, `subject`, `ask`, `constraint_realistic`, `constraint_beginner`, `decision`, `constraint_include_character_attribute_list` |
| n14 | constraint | t1:s20 | Separate the answers for the questions by a comma. | `respond`*, `subject`, `ask`, `constraint_budget_limited`, `constraint_single_choice`, `constraint_realistic`, `constraint_respectful`, `constraint_include_character_attribute_list`, `constraint_comprehensive`, `topic_politics`, `constraint_beginner`, `topic_pickup_lines` |
| n15 | constraint | t1:s21 | Format the final output matching the provided example (e.g., 'AC, D, BD'). | `example_d_record_an_actual_test_outcome_without_asserting_overall_correctness`, `unit_character`, `constraint_include_character_attribute_list`, `constraint_budget_limited`, `constraint_comprehensive`, `constraint_respectful`, `tone_concise`, `constraint_single_choice`, `constraint_realistic`, `calculation`, `constraint_beginner`, `requirement` |

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
- search_web.target → object_label, food_label, animal_label
- search_web.color → color_label
- search_web.currency → currency
- search_web.genre → genre_label
- search_web.location → country
- requirement.value → platform_label
- provides.actor → platform_label
- provides.subject → platform_label
- activity.object → object_label, food_label, animal_label
- activity.location → country
- activity.instrument → object_label, platform_label
- run_tests.target → platform_label
- failure.system → platform_label

## Retrieved records

### Shared rules that govern the records below (full text)

**rule_lexical_groups** (v19/rule/lexical-groups; rule governing platform_label)

Section 3.1 defines value groups: `group::key` values of type ATOM[group]. Open groups admit any key of their form (examples are not whitelists); standard groups admit the codes of their bundled standard (ISO 3166-1 alpha-2 for country, ISO 4217 for currency). Leaf values are never glossary entries. Consumer signatures alone decide where a group may appear. Retired bare symbols are invalid.

**rule_reading_guide** (v19/rule/reading-guide; core)

The spec governs syntax/types; this glossary defines vocabulary. Signature notation: ? optional, A / B explicit alternatives, void no result. Omitted optional arguments are unspecified. Value entries are category-refined STRING primitives; complex meanings require composition. Aliases are contextual hints, not unconditional equivalences. Report ambiguity. IDs use v19/<category>/<symbol>, v19/support/<symbol> or v19/composite/<symbol>. Statuses apply to this candidate: Retained preserves meaning; Adapted uses the stated contract; Composite requires TERM (bare STRING deprecated); Structural is syntax/argument vocabulary; Needs clarification is unusable until resolved; Deprecated is historical; Accepted is usable within this candidate.

**rule_recording_signatures** (v19/rule/recording-signatures; rule governing select_option)

RECORD ACTION uses the operation signature with REF[STRING] → TERM and LIST[REF[STRING]] → LIST[TERM]; other types/categories stay unchanged. Return EVENT, never the runtime result. Record actual outputs as attributed CLAIMs. Do not infer missing resources.

**rule_speech_acts_general** (v19/rule/speech-acts-general; rule governing respond)

UTTER-only, void, with the spec's speech attributes and LIST[TERM] constraints. No result binding. Literal content cannot replace required semantic arguments for structured coverage.

**rule_structural_constructs** (v19/rule/structural-constructs; core)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; rule governing propose_menu)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_category_code_value** (v19/rule/category/code-value; rule governing assert_multinomial_scorer)

path_/sym_ remain STRING identities; migrated chg_/assert_ are TERM constructors. Do not recover an exact file path by guessing from underscores.

**rule_category_constraint_value** (v19/rule/category/constraint-value; rule governing constraint_single_choice)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_descriptive_value** (v19/rule/category/descriptive-value; rule governing potential_harms)

STRING modifier/domain label; never a free-form proposition. dom_sgi needs its intended referent established before semantically dependent use.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; rule governing unit_item)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing entity_mains)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_event_value** (v19/rule/category/event-value; rule governing event_camper_in_sludge_pit)

TERM-described narrative event, not a recorded EVENT. Require inclusion explicitly when generating a story.

**rule_category_metric_value** (v19/rule/category/metric-value; rule governing metric_response_time)

STRING metric identity, not a Boolean value. Uptime and response time need numeric observations with units; order-late is Boolean-valued. Do not type every metric as BOOL.

**rule_category_product_attribute_value** (v19/rule/category/product-attribute-value; rule governing gender_men)

STRING color/size/product-market facets. gender_women describes a product category, not an assertion about a person's gender.

**rule_category_recipient_value** (v19/rule/category/recipient-value; rule governing role_respondent)

STRING roles or explicit named recipients. A role is not an exact person's identity. Keep an explicit name where substituting a role loses information.

**rule_category_search_value** (v19/rule/category/search-value; rule governing rank_price)

STRING refinements rank_ / dir_ / cat_ / avail_ / genre_ are separate. rank_rating may fill rank_field; genre_label::comedy may not. “Cheapest” usually requires both rank_price and dir_asc, not rank_price alone.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing between)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_state_value** (v19/rule/category/state-value; rule governing state_dirty)

STRING condition used in selection. state_warm does not command heat; “hot” is not automatically synonymous with “warm.”

**rule_category_style_value** (v19/rule/category/style-value; rule governing style_persuasive)

STRING production style. style_narrative does not establish that described events occurred.

**rule_category_tone_value** (v19/rule/category/tone-value; rule governing tone_concise)

STRING register. tone_urgent describes urgency, not a concrete deadline.

**rule_category_topic_value** (v19/rule/category/topic-value; candidate)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_composites_general** (v19/rule/composites-general; rule governing topic_school_work_routine)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_examples_general** (v19/rule/examples-general; rule governing example_d_record_an_actual_test_outcome_without_asserting_overall_correctness)

Examples use this glossary's contracts. They have not been verified by an implemented BrainCode parser.

**rule_operations_general** (v19/rule/operations-general; rule governing select_option)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_search_web_attributes** (v19/rule/search-web-attributes; rule governing sort)

Optional filters: availability, category, color, cuisine, currency, gender, genre, location, platform, ram_unit, reservation_availability, shape, size (category-refined STRING); max_price, min_ram, min_rating (NUMBER); trending (BOOL). Explicit signature alternatives additionally admit atoms. Price requires currency; RAM requires a capacity unit; no default scale/source. rank is invalid: use sort, whose rank_field accepts rank_* and rank_direction accepts dir_*. Category/genre/availability accept only their own subfamilies.

**rule_support_primitives_general** (v19/rule/support-primitives-general; rule governing subject)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- add_to_cart | operation | operation-vocabulary | (target: LIST[REF[STRING]]) -> void | Add the explicitly selected items. Does not pay or place an order.  ⟵ candidate
- drop | operation | operation-vocabulary | (target: REF[STRING] / TERM) -> void | Drop or release the held target object from the agent's hand. | not: place (which requires a destination receptacle) | aliases: drop, let go, put down  ⟵ candidate
- run_tests | operation | operation-vocabulary | (target: STRING / ATOM[platform_label], assertion?: TERM) -> BOOL | Run the selected project's tests, optionally checking the specified assertion. TRUE means the declared test condition passed, not overall software correctness.  ⟵ dependency of example_d_record_an_actual_test_outcome_without_asserting_overall_correctness
- search_web | operation | operation-vocabulary | (target: STRING / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], color?: STRING / ATOM[color_label], currency?: STRING / ATOM[currency], genre?: STRING / ATOM[genre_label], location?: STRING / ATOM[country], ...other search attributes below) -> LIST[REF[STRING]] | Query a catalog/web source. Criteria filter the result; rank separately when requested. | aliases: find, look for  ⟵ candidate
- select_filter | operation | operation-vocabulary | (target: REF[STRING], criterion: TERM) -> void | Apply one specified filter in an existing UI. Do not add this operation when the source only requests filtered search.  ⟵ candidate
- select_option | operation | operation-vocabulary | (target: REF[STRING], value: STRING) -> void | Select an option from a dropdown or select menu element. target must be a select element. | aliases: choose_option, choose_dropdown, pick_option  ⟵ candidate
- sort | operation | operation-vocabulary | (target: LIST[REF[STRING]], rank_direction: STRING, rank_field: STRING) -> LIST[REF[STRING]] | Request ordering of selected results. Preserve member identity; this is not a claim that order was observed. | aliases: rank, order by  ⟵ candidate

### speech acts

- ask | speech_act | operation-vocabulary | UTTER ask(target: TERM, or a sufficiently precise topic: STRING / TERM) | Request information/advice; not an assertion of an answer. | aliases: ask, how should  ⟵ candidate
- correct | speech_act | operation-vocabulary | UTTER correct(target: CLAIM) | Offer corrected content. Actual supersession requires the Conversation revision rules.  ⟵ candidate
- decline | speech_act | operation-vocabulary | UTTER decline(target: TERM) | Decline the represented request/proposal; not negate every proposition within it.  ⟵ candidate
- express_interest | speech_act | operation-vocabulary | UTTER express_interest(target: STRING / TERM) | Speech act expressing conversational interest or engagement in a topic. speech act in dialogic traces. | aliases: show_interest  ⟵ candidate
- inform | speech_act | operation-vocabulary | UTTER inform(target: CLAIM) | Present the proposition; preserve its holder/status.  ⟵ candidate
- offer | speech_act | operation-vocabulary | UTTER offer(target: STRING / TERM) | Speech act offering assistance, service, or items to a conversation partner. speech act in dialogic traces. | aliases: proffer  ⟵ candidate
- propose | speech_act | operation-vocabulary | UTTER propose(target: TERM) | Suggest an action/idea; does not record it as performed.  ⟵ candidate
- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ dependency of event_camper_in_sludge_pit
- calculation | constructor | TERM calculation(inputs: LIST[TERM], operation: STRING, result?: TERM) -> TERM | Constructs a descriptive representation of an arithmetic or algorithmic calculation step with inputs, operation identifier, and optional resulting value. | not: an executed runtime action or factual claim of outcome | aliases: math_operation, compute_step  ⟵ candidate
- conjunction | constructor | TERM conjunction(items: LIST[TERM]) -> TERM | All described components apply | not: Does not imply temporal order  ⟵ dependency of topic_school_work_routine
- decision | constructor | TERM decision(activity: TERM) -> TERM | A decision whose content is the described activity | not: Not proof it was carried out  ⟵ candidate
- include | constructor | TERM include(item: STRING / TERM) -> TERM | Require the identified content/item | not: Not permission to invent an instance in a recorded trace  ⟵ dependency of constraint_include_character_attribute_list
- obligation | constructor | TERM obligation(actor: STRING / TERM, activity: TERM) -> TERM | Constructs a deontic obligation description requiring an actor to perform an activity. actor and activity specified. | aliases: duty, mandatory_activity  ⟵ candidate
- property_question | constructor | TERM property_question(property: STRING, subject: STRING / TERM) -> TERM | An open request for a property of a subject | not: Does not supply the property's value  ⟵ candidate
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ candidate
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ candidate
- test_condition | constructor | TERM test_condition(condition: STRING, expected: BOOL) -> TERM | A testable condition with the expected Boolean outcome | not: Expected outcome is not an observed result  ⟵ dependency of assert_multinomial_scorer

### composites

- assert_multinomial_scorer | composite | code-value | TERM assert_multinomial_scorer() -> TERM | Assertion that multinomial probabilistic scoring succeeds. | = test_condition(condition="multinomial_probabilistic_scoring", expected=TRUE)  ⟵ candidate
- constraint_beginner | composite | constraint-value | TERM constraint_beginner() -> TERM | Targeted at beginners. | = requirement(property="audience_expertise", value="beginner")  ⟵ candidate
- constraint_budget_limited | composite | constraint-value | TERM constraint_budget_limited() -> TERM | Limited budget. | = requirement(property="budget_limited", value=TRUE)  ⟵ candidate
- constraint_comprehensive | composite | constraint-value | TERM constraint_comprehensive() -> TERM | Must be comprehensive. | = requirement(property="comprehensive", value=TRUE)  ⟵ candidate
- constraint_include_character_attribute_list | composite | constraint-value | TERM constraint_include_character_attribute_list() -> TERM | Include character attributes. | = include(item="character_attribute_list")  ⟵ candidate
- constraint_realistic | composite | constraint-value | TERM constraint_realistic() -> TERM | Must be realistic. | = requirement(property="realistic", value=TRUE)  ⟵ candidate
- constraint_respectful | composite | constraint-value | TERM constraint_respectful() -> TERM | Must be respectful. | = requirement(property="respectful", value=TRUE)  ⟵ candidate
- constraint_single_choice | composite | constraint-value | TERM constraint_single_choice() -> TERM | Must pick a single choice. | = requirement(property="choice_count", value=1)  ⟵ candidate
- event_camper_in_sludge_pit | composite | event-value | TERM event_camper_in_sludge_pit() -> TERM | Campers interacting in a sludge pit. | = activity(verb="interact", actor="campers", location="sludge_pit")  ⟵ candidate
- topic_greatest_cricketer_of_all_time | composite | topic-value | TERM topic_greatest_cricketer_of_all_time() -> TERM | Greatest cricketer of all time. | = subject(kind="cricketer", qualifier=requirement(property="rank_by_greatness", value=1), time="all_time")  ⟵ candidate
- topic_profanity | composite | topic-value | TERM topic_profanity() -> TERM | A composite term representing the topic of profanity. | = subject(kind="profanity") | not: potential_harms (which is generic) | aliases: profanity  ⟵ candidate
- topic_school_work_routine | composite | topic-value | TERM topic_school_work_routine() -> TERM | School and work routine. | = subject(kind="routine", qualifier=conjunction(items=[subject(kind="school"), subject(kind="work")]))  ⟵ candidate

### claim relations

- controversial | claim_relation | CLAIM controversial(subject: STRING / TERM) | Asserts that a topic, policy, or practice is the subject of public debate or controversy. evaluative debate claim. | aliases: debated, disputed  ⟵ candidate
- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ core
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ candidate
- prohibited | claim_relation | CLAIM prohibited(subject: STRING / TERM, location: STRING / TERM, condition?: STRING / TERM) | Asserts that a subject is prohibited from a location or activity under specified conditions. deontic prohibition claim. | aliases: forbidden, banned_from  ⟵ related to obligation
- propose_menu | claim_relation | CLAIM propose_menu(menu: TERM) | Asserts the proposal of a comprehensive menu plan. planning proposal. | aliases: suggest_menu  ⟵ candidate
- proposed_policy | claim_relation | CLAIM proposed_policy(policy: TERM, requirements: LIST[TERM]) | Asserts that a proposed policy framework comprises the specified requirement terms. policy must be a policy term. | aliases: policy_proposal  ⟵ related to obligation
- provides | claim_relation | CLAIM provides(actor: STRING / TERM / ATOM[platform_label], subject: STRING / TERM / ATOM[platform_label]) | Asserts that an establishment, organization, or provider supplies a specified item or service. provision claim. | aliases: supplies  ⟵ candidate
- varies_with | claim_relation | CLAIM varies_with(target: CLAIM / TERM, condition: STRING / TERM) | Asserts that a target claim or term varies contingently depending on specified conditions, external factors, or behavioral habits. | not: geographic variation only (use varies_by_location) | aliases: depends_on, contingent_on  ⟵ candidate

### links

- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ core
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ core
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ core

### values

- potential_harms | value | descriptive-value | Concept of potential safety hazards, adverse outcomes, or risks in AI interaction. | aliases: potential_harms  ⟵ candidate
- unit_character | value | duration-unit-value | One Unicode scalar value in the final rendered artifact; line endings are normalized to LF before counting. | aliases: characters, chars  ⟵ candidate
- unit_item | value | duration-unit-value | Top-level generated list or report item. | aliases: items, entries  ⟵ candidate
- unit_second | value | duration-unit-value | Second. | aliases: seconds, sec  ⟵ candidate
- unit_sentence | value | duration-unit-value | One grammatical sentence in text generation or constraint counting. | not: unit_paragraph (paragraph block) or unit_word (individual word) | aliases: sentence, sentences  ⟵ candidate
- credit_card | value | entity-name | A physical plastic credit, debit, or payment card object. | not: egift_card (an electronic gift card or digital voucher) | aliases: credit card, card, payment card  ⟵ candidate
- egift_card | value | entity-name | Electronic gift card or digital voucher product. | aliases: digital_gift_card, e_gift_card  ⟵ candidate
- entity_mains | value | entity-name | Event planning item or menu category: entity_mains. | aliases: entity_mains  ⟵ candidate
- resource_chiller | value | entity-name | Canonical abstract chilling resource when no particular appliance is named.  ⟵ candidate
- metric_response_time | value | metric-value | Support response time. | aliases: response time  ⟵ candidate
- gender_men | value | product-attribute-value | Men's/male-targeted. | aliases: men, male  ⟵ candidate
- role_agent | value | recipient-value | The assistant. | aliases: you, the assistant  ⟵ dependency of example_d_record_an_actual_test_outcome_without_asserting_overall_correctness
- role_respondent | value | recipient-value | A respondent, survey participant, or interviewee providing primary research data. | not: role_customer (the user's client) or role_user (the conversational user) | aliases: respondent, respondents, survey respondent, study participant  ⟵ candidate
- role_support_team | value | recipient-value | A customer-support team. | aliases: support, customer service  ⟵ candidate
- rank_distance | value | search-value | Rank field: proximity. | aliases: nearest, closest  ⟵ candidate
- rank_price | value | search-value | Rank or filter field: monetary cost. | aliases: cheapest, lowest price  ⟵ candidate
- rank_rating | value | search-value | Rank or filter field: user or critic score.  ⟵ candidate
- between | value | spatial-relation | Positioned between or in the middle of reference entities. | not: next_to or in_front_of | aliases: between, in the middle of, middle of, center of  ⟵ candidate
- on | value | spatial-relation | Resting atop. | aliases: on top of  ⟵ candidate
- under | value | spatial-relation | Beneath. | aliases: below  ⟵ candidate
- state_dirty | value | state-value | Dirty condition. | aliases: dirty  ⟵ candidate
- style_persuasive | value | style-value | Persuasive/argumentative style. | aliases: persuasive  ⟵ candidate
- tone_concise | value | tone-value | Brief, to-the-point register. | aliases: briefly, concisely  ⟵ candidate
- topic_abortion | value | topic-value | The subject matter, ethical debate, healthcare procedure, or legal question of abortion and reproductive choice. | not: general politics (use topic_politics) or cognitive belief concepts (use beliefs) | aliases: abortion, reproductive rights, abortion rights  ⟵ candidate
- topic_baldurs_gate_3 | value | topic-value | Baldur's Gate 3.  ⟵ candidate
- topic_current_events | value | topic-value | Current news, geopolitical events, and ongoing international developments. | aliases: current_events, news  ⟵ candidate
- topic_pickup_lines | value | topic-value | Pickup lines.  ⟵ candidate
- topic_politics | value | topic-value | Politics.  ⟵ candidate
- topic_spider_man_2 | value | topic-value | Marvel's Spider-Man 2.  ⟵ candidate

### examples

- example_d_record_an_actual_test_outcome_without_asserting_overall_correctness (candidate): Record an actual test outcome without asserting overall correctness

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=AGENT {
    RECORD ACTION run_tests(target=platform_label::scikit_learn) STATUS succeeded SOURCE "t1:tests" -> run_tests_event : EVENT
    CLAIM outcome(event=run_tests_event, value=TRUE) BY role_agent STATUS observed SOURCE "t1:tests" -> outcome_2 : CLAIM
  }
}
```

