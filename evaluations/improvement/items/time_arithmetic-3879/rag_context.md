# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 29 needs (decomposition: llm), 134 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | action | t1:s1 | Define variables X, Y, and Z as components of the answer to Question 1. | `respond`*, `calculation`, `ask`, `conjunction`, `conditional`, `at_most`, `at_least`, `constraint_17_plus`, `subject`, `extract`, `property_question`, `offer_help` |
| n2 | claim | t1:s2 | The match was moved forward by 18 weeks. | `unit_week`*, `ongoing`, `unit_month`, `metric_response_time`, `occurred_recently`, `prep_time`, `outcome`, `rule_category_duration_unit_value`, `works_best`, `escalation`, `constraint_17_plus`, `metric_order_late` |
| n3 | temporal | t1:s2 | Duration of 18 weeks. | `unit_week`*, `duration`*, `unit_month`, `unit_year`, `unit_minute`, `rule_category_duration_unit_value`, `unit_hour`, `unit_day`, `prep_time`, `metric_response_time`, `constraint_17_plus`, `cat_limited_time_offers` |
| n4 | claim | t1:s3 | The original date for the match was 25-12-2021. | `occurred_recently`, `outcome`, `unit_year`, `unit_month`, `prep_time`, `metric_response_time`, `rule_category_duration_unit_value`, `constraint_17_plus`, `topic_macbook_pro_2017`, `ongoing`, `leads_to`, `occurred` |
| n5 | temporal | t1:s3 | Original date of 25-12-2021. | `unit_month`, `unit_year`, `unit_day`, `unit_week`, `time_point`, `rule_category_duration_unit_value`, `aesthetic`, `metric_response_time`, `daytime`, `constraint_17_plus`, `topic_macbook_pro_2017`, `topic_current_events` |
| n6 | action | t1:s3 | Calculate the new date of the match. | `time_point`, `topic_current_events`*, `unit_month`, `unit_year`, `metric_response_time`, `wait`, `rule_category_duration_unit_value`, `unit_week`, `outcome`, `unit_minute`, `minimum_per_period`, `unit_day` |
| n7 | constraint | t1:s4 | Format the date answer as mm/dd/yyyy. | `unit_month`, `metric_response_time`, `unit_year`, `rule_category_duration_unit_value`, `unit_week`, `respond`*, `unit_minute`, `clock`, `time_point`, `constraint_budget_limited`, `format_numbered_list`, `unit_day` |
| n8 | action | t1:s5 | Define X' as X plus 26. | `at_least`*, `constraint_17_plus`, `calculation`, `wait`, `conditional`, `measure`, `at_most`, `unit_character`, `lexical_label`, `obligation`, `example_c_existing_constraint_symbol_becomes_a_typed_construction`, `code_entity` |
| n9 | action | t1:s6 | Define variable P as the answer to Question 2. | `respond`*, `calculation`, `ask`, `property_question`, `metric_response_time`, `conditional`, `test_condition`, `subject`, `offer_help`, `unit_second`, `constraint_realistic`, `role_respondent` |
| n10 | claim | t1:s7 | Today is Monday. | `unit_day`, `occurred_recently`, `unit_week`, `daytime`, `outcome`, `topic_current_events`, `ongoing`, `wait`, `leads_to`, `topic_school_work_routine`, `enables`, `tone_urgent` |
| n11 | action | t1:s7 | Calculate the day of the week X' days before Monday. | `unit_week`*, `unit_day`*, `daytime`*, `time_point`, `nighttime`, `unit_month`, `wait`, `rule_category_duration_unit_value`, `prep_time`, `unit_year`, `metric_response_time`, `unit_hour` |
| n12 | temporal | t1:s7 | X' days before Monday. | `unit_day`*, `daytime`*, `unit_month`, `unit_week`, `unit_year`, `nighttime`, `prep_time`, `unit_hour`, `rule_category_duration_unit_value`, `time_point`, `wait`, `cat_limited_time_offers` |
| n13 | constraint | t1:s8 | Format the answer as a day of the week. | `unit_week`*, `unit_day`*, `daytime`*, `respond`*, `unit_month`, `unit_year`, `unit_hour`, `unit_minute`, `rule_category_duration_unit_value`, `cat_limited_time_offers`, `nighttime`, `unit_sentence` |
| n14 | action | t1:s9 | Define Y' as Y minus 9. | `calculation`, `at_least`, `measure`, `negation`, `at_most`, `wait`, `constraint_17_plus`, `under`, `unit_sentence`, `block_evaluation`, `obligation`, `indicator` |
| n15 | action | t1:s9 | Define P' as the day of the week 24 days after P. | `unit_day`*, `unit_week`*, `daytime`*, `time_point`, `nighttime`, `unit_month`, `wait`, `rule_category_duration_unit_value`, `unit_hour`, `unit_year`, `unit_minute`, `prep_time` |
| n16 | temporal | t1:s9 | 24 days after P. | `unit_day`*, `unit_month`, `unit_week`, `unit_year`, `daytime`*, `rule_category_duration_unit_value`, `unit_hour`, `duration`, `example_b_preserve_the_class_and_amount_of_an_itinerary_constraint`, `metric_response_time`, `unit_minute`, `time_point` |
| n17 | action | t1:s10 | Define variable Q as the answer to Question 3. | `respond`*, `calculation`, `ask`, `property_question`, `example_c_existing_constraint_symbol_becomes_a_typed_construction`, `metric_response_time`, `test_condition`, `conditional`, `subject`, `offer_help`, `assert_multinomial_scorer`, `dialogue` |
| n18 | claim | t1:s11 | The current time is 10:26 AM on P'. | `prep_time`, `occurred_recently`, `metric_response_time`, `time_point`, `outcome`, `unit_minute`, `daytime`, `clock`, `unit_day`, `unit_hour`, `wait`, `nighttime` |
| n19 | action | t1:s11 | Calculate the day of the week Y' hours from 10:26 AM on P'. | `unit_week`*, `unit_day`*, `unit_hour`*, `daytime`*, `nighttime`, `clock`, `unit_month`, `time_point`, `rule_category_duration_unit_value`, `unit_minute`, `wait`, `metric_response_time` |
| n20 | temporal | t1:s11 | Y' hours from 10:26 AM on P'. | `unit_hour`*, `unit_day`, `daytime`, `unit_month`, `nighttime`, `time_point`, `unit_week`, `clock`, `rule_category_duration_unit_value`, `prep_time`, `metric_response_time`, `unit_minute` |
| n21 | constraint | t1:s12 | Reply with 'unanswerable' if information is insufficient or multiple answers exist. | `respond`*, `ask`, `constraint_realistic`, `rule_category_constraint_value`, `assert_multinomial_scorer`, `constraint_budget_limited`, `test_condition`, `constraint_exclude_flowery_language`, `failure`, `at_least`, `at_most`, `constraint_beginner` |
| n22 | action | t1:s13 | Define Z' as Z minus 1990. | `calculation`, `locale_zh`, `negation`, `wait`, `weather_condition`, `at_least`, `currency`, `measure`, `eastern_cape`, `tone_neutral`, `unit_second`, `block_evaluation` |
| n23 | action | t1:s13 | Define Q' as the day of the week 49 days after Q. | `unit_day`*, `unit_week`*, `daytime`*, `time_point`, `nighttime`, `unit_month`, `rule_category_duration_unit_value`, `wait`, `unit_hour`, `unit_minute`, `metric_response_time`, `greeting` |
| n24 | temporal | t1:s13 | 49 days after Q. | `unit_day`*, `unit_month`, `unit_week`, `unit_year`, `daytime`*, `unit_hour`, `duration`, `rule_category_duration_unit_value`, `metric_response_time`, `unit_minute`, `time_point`, `wait` |
| n25 | action | t1:s14 | Solve Question 4 using the calculated values. | `respond`, `calculation`, `metric_response_time`, `minimum_per_period`, `assert_multinomial_scorer`, `unit_year`, `test_condition`, `outcome`, `constraint_17_plus`, `at_most`, `at_least`, `quantity` |
| n26 | claim | t1:s15 | A text was received before noon on Q' stating the deadline is in Z' hours. | `unit_hour`*, `prep_time`, `metric_response_time`, `unit_month`, `occurred_recently`, `outcome`, `wait`, `clock`, `daytime`, `unit_minute`, `unit_week`, `time_point` |
| n27 | temporal | t1:s15 | Before noon on Q', and a duration of Z' hours. | `unit_hour`*, `daytime`, `unit_day`, `unit_month`, `unit_week`, `clock`, `duration`*, `unit_year`, `nighttime`, `time_point`, `rule_category_duration_unit_value`, `prep_time` |
| n28 | action | t1:s16 | Calculate the possible days of the week for the deadline. | `unit_week`*, `unit_day`*, `daytime`*, `time_point`, `unit_month`, `wait`, `rule_category_duration_unit_value`, `metric_response_time`, `unit_minute`, `prep_time`, `unit_year`, `unit_hour` |
| n29 | constraint | t1:s17 | Format the answer as an alphabetically ordered list. | `format_numbered_list`, `respond`*, `sort`, `extract`, `format_bullet_list`, `metric_order_late`, `sequence`, `entity_order_vs_assemble_plan`, `entity_condensed_grocery_list`, `constraint_budget_limited`, `format_table`, `constraint_exclude_flowery_language` |

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
- measure.unit → currency
- lexical_label.value → object_label, genre_label, food_label, animal_label, color_label
- code_entity.project → platform_label
- failure.system → platform_label
- weather_condition.location → country
- activity.object → object_label, food_label, animal_label
- activity.location → country
- activity.instrument → object_label, platform_label
- requirement.value → platform_label

## Retrieved records

### Shared rules that govern the records below (full text)

**rule_lexical_groups** (v19/rule/lexical-groups; rule governing lexical_label)

Section 3.1 defines value groups: `group::key` values of type ATOM[group]. Open groups admit any key of their form (examples are not whitelists); standard groups admit the codes of their bundled standard (ISO 3166-1 alpha-2 for country, ISO 4217 for currency). Leaf values are never glossary entries. Consumer signatures alone decide where a group may appear. Retired bare symbols are invalid.

**rule_reading_guide** (v19/rule/reading-guide; core)

The spec governs syntax/types; this glossary defines vocabulary. Signature notation: ? optional, A / B explicit alternatives, void no result. Omitted optional arguments are unspecified. Value entries are category-refined STRING primitives; complex meanings require composition. Aliases are contextual hints, not unconditional equivalences. Report ambiguity. IDs use v19/<category>/<symbol>, v19/support/<symbol> or v19/composite/<symbol>. Statuses apply to this candidate: Retained preserves meaning; Adapted uses the stated contract; Composite requires TERM (bare STRING deprecated); Structural is syntax/argument vocabulary; Needs clarification is unusable until resolved; Deprecated is historical; Accepted is usable within this candidate.

**rule_recording_signatures** (v19/rule/recording-signatures; rule governing extract)

RECORD ACTION uses the operation signature with REF[STRING] → TERM and LIST[REF[STRING]] → LIST[TERM]; other types/categories stay unchanged. Return EVENT, never the runtime result. Record actual outputs as attributed CLAIMs. Do not infer missing resources.

**rule_speech_acts_general** (v19/rule/speech-acts-general; rule governing respond)

UTTER-only, void, with the spec's speech attributes and LIST[TERM] constraints. No result binding. Literal content cannot replace required semantic arguments for structured coverage.

**rule_structural_constructs** (v19/rule/structural-constructs; core)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; rule governing ongoing)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_attributes_and_generate** (v19/rule/attributes-and-generate; rule governing quantity)

Attribute entries name arguments; legality/types come from each operation, not global membership. GENERATE uses the spec's core fields; retained artifact profiles return STRING. Numeric/list results need explicit profiles. Legacy itinerary fields expand to TERM constraints: duration/duration_unit → duration(amount,unit); stop_min_per_day/stop_requirement → minimum_per_period(class,count,period=unit_day), never an inferred temple class; max_walk_duration/unit → maximum_between_stops(activity="walk",amount,unit). No legacy shorthand is enabled. Old events/character_properties/transformations become explicitly scoped TERM constraints. Message purpose is TERM, not send_email.content: GENERATE exact STRING content, then send. Report opaque fallback separately.

**rule_category_artifact_value** (v19/rule/category/artifact-value; rule governing art_itinerary)

STRING artifact class for GENERATE.target. art_story says what kind of artifact to produce, not what occurs in its plot.

**rule_category_code_value** (v19/rule/category/code-value; rule governing assert_multinomial_scorer)

path_/sym_ remain STRING identities; migrated chg_/assert_ are TERM constructors. Do not recover an exact file path by guessing from underscores.

**rule_category_constraint_value** (v19/rule/category/constraint-value; candidate)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_content_value** (v19/rule/category/content-value; rule governing content_kyoto_itinerary)

Existing compounds become the constructors in Section 5. Their outputs go in topic/target/constraints as appropriate, not content, whose spec type remains STRING.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; candidate)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing clock)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_format_value** (v19/rule/category/format-value; rule governing format_numbered_list)

STRING format. format_email is layout, not the action send_email.

**rule_category_locale_value** (v19/rule/category/locale-value; rule governing locale_zh)

STRING locale. “English” alone does not always mean locale_en_us; preserve ambiguity.

**rule_category_location_name** (v19/rule/category/location-name; rule governing eastern_cape)

STRING location descriptor. A `table` surface is not the generated artifact category art_table.

**rule_category_metric_value** (v19/rule/category/metric-value; rule governing metric_response_time)

STRING metric identity, not a Boolean value. Uptime and response time need numeric observations with units; order-late is Boolean-valued. Do not type every metric as BOOL.

**rule_category_recipient_value** (v19/rule/category/recipient-value; rule governing role_respondent)

STRING roles or explicit named recipients. A role is not an exact person's identity. Keep an explicit name where substituting a role loses information.

**rule_category_search_value** (v19/rule/category/search-value; rule governing cat_limited_time_offers)

STRING refinements rank_ / dir_ / cat_ / avail_ / genre_ are separate. rank_rating may fill rank_field; genre_label::comedy may not. “Cheapest” usually requires both rank_price and dir_asc, not rank_price alone.

**rule_category_semantic_category_value** (v19/rule/category/semantic-category-value; rule governing class_temple)

STRING class label used by typed constraints. class_temple describes a class, not an acquired physical temple reference.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing under)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_tone_value** (v19/rule/category/tone-value; candidate)

STRING register. tone_urgent describes urgency, not a concrete deadline.

**rule_category_topic_value** (v19/rule/category/topic-value; candidate)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_category_transformation_value** (v19/rule/category/transformation-value; rule governing transform_preserve_first_column)

TERM-described transformation. Pass it through constraints; no ungoverned transformations attribute.

**rule_composites_general** (v19/rule/composites-general; rule governing transform_preserve_first_column)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_examples_general** (v19/rule/examples-general; rule governing example_c_existing_constraint_symbol_becomes_a_typed_construction)

Examples use this glossary's contracts. They have not been verified by an implemented BrainCode parser.

**rule_operations_general** (v19/rule/operations-general; rule governing extract)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_search_web_attributes** (v19/rule/search-web-attributes; rule governing sort)

Optional filters: availability, category, color, cuisine, currency, gender, genre, location, platform, ram_unit, reservation_availability, shape, size (category-refined STRING); max_price, min_ram, min_rating (NUMBER); trending (BOOL). Explicit signature alternatives additionally admit atoms. Price requires currency; RAM requires a capacity unit; no default scale/source. rank is invalid: use sort, whose rank_field accepts rank_* and rank_direction accepts dir_*. Category/genre/availability accept only their own subfamilies.

**rule_supplemental_general** (v19/rule/supplemental-general; rule governing extract)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; rule governing calculation)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- extract | operation | operation-vocabulary | (target: LIST[REF[STRING]], limit: NUMBER) -> LIST[REF[STRING]] | First limit results, preserving order and identity; limit is a nonnegative integer; limit=1 is still a list  ⟵ candidate
- send_message | operation | operation-vocabulary | (recipient: STRING, content: STRING, tone?: STRING) -> void | Send supplied exact content through the specified message context. If the channel is unresolved, report it. | aliases: text  ⟵ candidate
- sort | operation | operation-vocabulary | (target: LIST[REF[STRING]], rank_direction: STRING, rank_field: STRING) -> LIST[REF[STRING]] | Request ordering of selected results. Preserve member identity; this is not a claim that order was observed. | aliases: rank, order by  ⟵ candidate
- wait | operation | operation-vocabulary | (duration?: NUMBER) -> void | Pause execution for a duration or cycle. duration in seconds or ticks. | aliases: idle, pause  ⟵ candidate

### speech acts

- ask | speech_act | operation-vocabulary | UTTER ask(target: TERM, or a sufficiently precise topic: STRING / TERM) | Request information/advice; not an assertion of an answer. | aliases: ask, how should  ⟵ candidate
- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ dependency of occurred
- aesthetic | constructor | TERM aesthetic(period: STRING, style: STRING) -> TERM | A stylistic description with an explicit period | not: Not a character's age or production date  ⟵ candidate
- at_least | constructor | TERM at_least(measure: TERM) -> TERM | A lower bound: the constrained value is greater than or equal to the given measure (or number term). Use inside requirement(value=...). | not: an exact value; a strict 'more than' only when the source says so explicitly | aliases: at least, minimum, or more, no less than, plus  ⟵ candidate
- at_most | constructor | TERM at_most(measure: TERM) -> TERM | An upper bound: the constrained value is less than or equal to the given measure (or number term). Use inside requirement(value=...). | not: an exact value or a target to aim for | aliases: at most, maximum, up to, no more than, under  ⟵ candidate
- block_evaluation | constructor | TERM block_evaluation(block: STRING / TERM, maturity?: STRING, potential?: STRING, quality?: STRING, rank?: NUMBER, traps?: STRING) -> TERM | Constructs a structured evaluation, categorization, or ranking descriptor for a geological exploration block. | not: an external execution action or generic list sorting operation (use sort) | aliases: block assessment, block ranking, block rating, block categorization  ⟵ candidate
- calculation | constructor | TERM calculation(inputs: LIST[TERM], operation: STRING, result?: TERM) -> TERM | Constructs a descriptive representation of an arithmetic or algorithmic calculation step with inputs, operation identifier, and optional resulting value. | not: an executed runtime action or factual claim of outcome | aliases: math_operation, compute_step  ⟵ candidate
- code_entity | constructor | TERM code_entity(file?: STRING / TERM, kind: STRING, name: STRING, project?: STRING / ATOM[platform_label]) -> TERM | Constructs a structured descriptor for a source code entity such as a function, method, class, module, or source file within a project. | not: an executed runtime call or file system operation | aliases: code_function, source_file, code_symbol  ⟵ candidate
- conditional | constructor | TERM conditional(condition: TERM, consequence: TERM) -> TERM | Constructs a structured conditional proposition term connecting a condition and consequence. descriptive logic structure. | aliases: if_then  ⟵ candidate
- conjunction | constructor | TERM conjunction(items: LIST[TERM]) -> TERM | All described components apply | not: Does not imply temporal order  ⟵ candidate
- dialogue | constructor | TERM dialogue(style: STRING) -> TERM | Constructs a description of conversational dialogue adhering to a style. descriptive conversational term. | aliases: conversation_style  ⟵ candidate
- duration | constructor | TERM duration(amount: NUMBER, unit: STRING) -> TERM | Requested elapsed/calendar extent | not: Word/item counts are not time  ⟵ candidate
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ dependency of constraint_exclude_flowery_language
- greeting | constructor | TERM greeting(recipient: STRING) -> TERM | Constructs a conversational salutation greeting descriptor. conversational discourse term. | aliases: salutation  ⟵ candidate
- indicator | constructor | TERM indicator(condition: STRING / TERM, indicator_type?: STRING) -> TERM | Constructs a descriptive term representing a warning sign, behavioral marker, or red flag indicating an underlying condition or risk. | not: warning (a system alert claim relation) or color_label::red (a product color) | aliases: red flag, warning sign, behavioral marker, signal  ⟵ candidate
- lexical_label | constructor | TERM lexical_label(value: ATOM[object_label] / ATOM[genre_label] / ATOM[food_label] / ATOM[animal_label] / ATOM[color_label]) -> TERM | Describe a domain-qualified leaf label using the atom group contract. Adds no inferred properties, relation, assertion or English-sense resolution. A downstream TERM consumer must permit this description role; TERM typing alone never turns a label into a condition or proposition. | not: Inferring that cork is waterproof, or using a label as a complete claim.  ⟵ candidate
- maximum_between_stops | constructor | TERM maximum_between_stops(activity: STRING, amount: NUMBER, unit: STRING) -> TERM | Upper bound on the stated activity between successive stops | not: Not a limit on total daily duration  ⟵ dependency of example_b_preserve_the_class_and_amount_of_an_itinerary_constraint
- measure | constructor | TERM measure(amount: NUMBER, unit: STRING / ATOM[currency]) -> TERM | A measured amount: a number with its unit symbol (a unit-category value such as unit_minute, cap_gb or currency::USD). Describes the amount only; asserts nothing. ATOM[currency] is also accepted and supplies the pinned currency identity; no exchange rate or conversion is implicit. | not: a symbol with the number baked in (char_age_18, size_16gb); a unitless count (use the quantity argument) | aliases: amount of, size of, measured in  ⟵ candidate
- minimum_per_period | constructor | TERM minimum_per_period(class: STRING, count: NUMBER, period: STRING) -> TERM | At least count members of class in each period | not: Not a minimum total over the whole artifact  ⟵ candidate
- negation | constructor | TERM negation(target: TERM) -> TERM | Constructs a descriptive semantic negation of a target descriptive proposition or condition term. | not: Check's runtime Boolean operator NOT or a speech-act decline | aliases: not, does not, negation, absence of  ⟵ candidate
- obligation | constructor | TERM obligation(actor: STRING / TERM, activity: TERM) -> TERM | Constructs a deontic obligation description requiring an actor to perform an activity. actor and activity specified. | aliases: duty, mandatory_activity  ⟵ candidate
- offer_help | constructor | TERM offer_help() -> TERM | Constructs a conversational proffer of assistance or support. conversational discourse term. | aliases: help_offer  ⟵ candidate
- preserve | constructor | TERM preserve(component: STRING, index: NUMBER) -> TERM | Keep the indexed component unchanged, using one-based indexing | not: Not preserve all components  ⟵ dependency of transform_preserve_first_column
- property_question | constructor | TERM property_question(property: STRING, subject: STRING / TERM) -> TERM | An open request for a property of a subject | not: Does not supply the property's value  ⟵ candidate
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ dependency of constraint_budget_limited
- sequence | constructor | TERM sequence(items: LIST[TERM]) -> TERM | Ordered described activities/content | not: Not unordered conjunction  ⟵ candidate
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ candidate
- test_condition | constructor | TERM test_condition(condition: STRING, expected: BOOL) -> TERM | A testable condition with the expected Boolean outcome | not: Expected outcome is not an observed result  ⟵ candidate
- time_point | constructor | TERM time_point(date?: STRING, time?: STRING, timezone?: STRING) -> TERM | Constructs a structured representation of a specific calendar date, time of day, or scheduled timestamp. | not: an elapsed time duration (use duration) | aliases: timestamp, datetime, scheduled_time  ⟵ candidate
- weather_condition | constructor | TERM weather_condition(condition: STRING, location?: STRING / TERM / ATOM[country], severity?: STRING) -> TERM | A structured descriptor of atmospheric or weather phenomena such as wind, rain, or storm at an optional location; asserts nothing. | not: state_cold or state_warm (thermal states of physical objects) or occurred (past factual occurrence assertion) | aliases: weather, storm_condition, atmospheric_condition  ⟵ candidate

### composites

- assert_multinomial_scorer | composite | code-value | TERM assert_multinomial_scorer() -> TERM | Assertion that multinomial probabilistic scoring succeeds. | = test_condition(condition="multinomial_probabilistic_scoring", expected=TRUE)  ⟵ candidate
- constraint_beginner | composite | constraint-value | TERM constraint_beginner() -> TERM | Targeted at beginners. | = requirement(property="audience_expertise", value="beginner")  ⟵ candidate
- constraint_budget_limited | composite | constraint-value | TERM constraint_budget_limited() -> TERM | Limited budget. | = requirement(property="budget_limited", value=TRUE)  ⟵ candidate
- constraint_exclude_flowery_language | composite | constraint-value | TERM constraint_exclude_flowery_language() -> TERM | Avoid flowery language. | = exclude(item="flowery_language")  ⟵ candidate
- constraint_realistic | composite | constraint-value | TERM constraint_realistic() -> TERM | Must be realistic. | = requirement(property="realistic", value=TRUE)  ⟵ candidate
- content_kyoto_itinerary | composite | content-value | TERM content_kyoto_itinerary() -> TERM | A Kyoto itinerary subject. | = subject(kind="itinerary", location="Kyoto")  ⟵ dependency of example_b_preserve_the_class_and_amount_of_an_itinerary_constraint
- topic_school_work_routine | composite | topic-value | TERM topic_school_work_routine() -> TERM | School and work routine. | = subject(kind="routine", qualifier=conjunction(items=[subject(kind="school"), subject(kind="work")]))  ⟵ candidate
- transform_preserve_first_column | composite | transformation-value | TERM transform_preserve_first_column() -> TERM | Preserve the first column of a table. | = preserve(component="column", index=1)  ⟵ candidate

### claim relations

- considered | claim_relation | CLAIM considered(subject: TERM) | Asserts that an agent or speaker evaluated or entertained a specific candidate term or concept. subject is the evaluated term. | aliases: evaluated, weighed  ⟵ candidate
- enables | claim_relation | CLAIM enables(condition: TERM / CLAIM, outcome: TERM / CLAIM) | Asserts that an enabling condition or capability facilitates an outcome. enabling condition. | aliases: facilitates, allows  ⟵ candidate
- escalation | claim_relation | CLAIM escalation(cause: CLAIM, conflict: TERM) | Asserts an escalation in intensity or scale of a conflict triggered by an event. conflict dynamics. | aliases: conflict_escalation  ⟵ candidate
- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ candidate
- leads_to | claim_relation | CLAIM leads_to(cause: TERM, effect: TERM) | Asserts a conceptual consequence or progression from cause to effect. progression relation. | aliases: results_in  ⟵ candidate
- occurred | claim_relation | CLAIM occurred(activity: TERM) | Asserts that an event, action, or activity took place in the past. past occurrence claim. | aliases: happened  ⟵ candidate
- occurred_recently | claim_relation | CLAIM occurred_recently(target: CLAIM) | Asserts temporal recency of an asserted occurrence or claim. temporal recency qualifier. | aliases: recently_happened  ⟵ candidate
- ongoing | claim_relation | CLAIM ongoing(target: TERM) | Asserts that a conflict, process, or initiative is actively ongoing. temporal aspect claim. | aliases: in_progress  ⟵ candidate
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ candidate
- prep_time | claim_relation | CLAIM prep_time(value: TERM) | Asserts an estimated preparation or assembly time duration. time requirement assertion. | aliases: preparation_duration  ⟵ candidate
- prohibited | claim_relation | CLAIM prohibited(subject: STRING / TERM, location: STRING / TERM, condition?: STRING / TERM) | Asserts that a subject is prohibited from a location or activity under specified conditions. deontic prohibition claim. | aliases: forbidden, banned_from  ⟵ related to obligation
- proposed_policy | claim_relation | CLAIM proposed_policy(policy: TERM, requirements: LIST[TERM]) | Asserts that a proposed policy framework comprises the specified requirement terms. policy must be a policy term. | aliases: policy_proposal  ⟵ related to obligation
- works_best | claim_relation | CLAIM works_best(style: STRING, count: NUMBER, purpose: STRING) | Asserts an advisory evaluation of optimal event style and participant capacity. planning evaluation. | aliases: optimal_format  ⟵ candidate

### links

- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ core
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ core
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ core

### values

- art_itinerary | value | artifact-value | An ordered travel plan; GENERATE returns STRING, not booked travel  ⟵ dependency of example_b_preserve_the_class_and_amount_of_an_itinerary_constraint
- constraint_17_plus | value | constraint-value | Rated 17+ or mature.  ⟵ candidate
- unit_character | value | duration-unit-value | One Unicode scalar value in the final rendered artifact; line endings are normalized to LF before counting. | aliases: characters, chars  ⟵ candidate
- unit_day | value | duration-unit-value | Day. | aliases: days  ⟵ candidate
- unit_hour | value | duration-unit-value | Hour. | aliases: hours  ⟵ candidate
- unit_minute | value | duration-unit-value | Minute. | aliases: minutes, min  ⟵ candidate
- unit_month | value | duration-unit-value | Month. | aliases: months  ⟵ candidate
- unit_second | value | duration-unit-value | Second. | aliases: seconds, sec  ⟵ candidate
- unit_sentence | value | duration-unit-value | One grammatical sentence in text generation or constraint counting. | not: unit_paragraph (paragraph block) or unit_word (individual word) | aliases: sentence, sentences  ⟵ candidate
- unit_week | value | duration-unit-value | Week. | aliases: weeks  ⟵ candidate
- unit_year | value | duration-unit-value | Year. | aliases: years  ⟵ candidate
- clock | value | entity-name | A clock timepiece appliance. | not: duration units like unit_hour | aliases: clock, timer  ⟵ candidate
- entity_condensed_grocery_list | value | entity-name | Event planning item or menu category: entity_condensed_grocery_list. | aliases: entity_condensed_grocery_list  ⟵ candidate
- entity_order_vs_assemble_plan | value | entity-name | Event planning item or menu category: entity_order_vs_assemble_plan. | aliases: entity_order_vs_assemble_plan  ⟵ candidate
- format_bullet_list | value | format-value | Bulleted list. | aliases: bullet points  ⟵ candidate
- format_newsletter | value | format-value | Newsletter layout. | aliases: newsletter  ⟵ candidate
- format_numbered_list | value | format-value | Numbered list. | aliases: numbered steps  ⟵ candidate
- format_pdf | value | format-value | PDF document. | aliases: as a pdf  ⟵ candidate
- format_table | value | format-value | Tabular layout. | aliases: as a table  ⟵ candidate
- locale_zh | value | locale-value | Chinese language locale (Simplified and Traditional Chinese). | not: a specific geographical region or nationality (use location-name) | aliases: chinese, zh, zh-cn, zh-tw, mandarin  ⟵ candidate
- eastern_cape | value | location-name | Eastern Cape region.  ⟵ candidate
- metric_order_late | value | metric-value | Whether an order is late. | aliases: order is late, delayed  ⟵ candidate
- metric_response_time | value | metric-value | Support response time. | aliases: response time  ⟵ candidate
- role_respondent | value | recipient-value | A respondent, survey participant, or interviewee providing primary research data. | not: role_customer (the user's client) or role_user (the conversational user) | aliases: respondent, respondents, survey respondent, study participant  ⟵ candidate
- cat_limited_time_offers | value | search-value | Category: time-limited deals.  ⟵ candidate
- class_temple | value | semantic-category-value | The abstract class of temples. | aliases: temple, temples  ⟵ dependency of example_b_preserve_the_class_and_amount_of_an_itinerary_constraint
- under | value | spatial-relation | Beneath. | aliases: below  ⟵ candidate
- daytime | value | time-of-day-value | The period of natural daylight between sunrise and sunset in the diurnal cycle. | not: unit_day (a 24-hour elapsed duration unit) or clock time timestamps | aliases: daytime, day, day time, daylight hours  ⟵ candidate
- nighttime | value | time-of-day-value | The period of darkness between sunset and sunrise in the diurnal cycle. | not: night_stand (a piece of furniture) or clock time timestamps | aliases: nighttime, night, night time, darkness  ⟵ candidate
- tone_neutral | value | tone-value | Plain, unmarked register.  ⟵ candidate
- tone_urgent | value | tone-value | Conveys urgency. | aliases: urgently, ASAP  ⟵ candidate
- topic_current_events | value | topic-value | Current news, geopolitical events, and ongoing international developments. | aliases: current_events, news  ⟵ candidate
- topic_macbook_pro_2017 | value | topic-value | MacBook Pro 2017.  ⟵ candidate
- topic_pickup_lines | value | topic-value | Pickup lines.  ⟵ candidate

### attributes

- quantity | attribute | attribute-name | Explicit count as NUMBER.  ⟵ candidate

### examples

- example_b_preserve_the_class_and_amount_of_an_itinerary_constraint (candidate): Preserve the class and amount of an itinerary constraint

```braincode
MODE REQUEST
ENTRYPOINT Itinerary
TASK Itinerary : STRING {
  TERM content_kyoto_itinerary() -> content_kyoto_itinerary_2 : TERM
  TERM duration(amount=3, unit=unit_day) -> duration_2 : TERM
  TERM minimum_per_period(class=class_temple, count=1, period=unit_day) -> minimum_per_period_2 : TERM
  TERM maximum_between_stops(activity="walk", amount=20, unit=unit_minute) -> maximum_between_stops_2 : TERM
  GENERATE(target=art_itinerary, constraints=[duration_2, minimum_per_period_2, maximum_between_stops_2], topic=content_kyoto_itinerary_2) -> itinerary : STRING
  RETURN itinerary
}
```

- example_c_existing_constraint_symbol_becomes_a_typed_construction (candidate): Existing constraint symbol becomes a typed construction

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM constraint_realistic() -> constraint_realistic_2 : TERM
    UTTER ask(constraints=[constraint_realistic_2], topic=topic_pickup_lines)
  }
}
```

