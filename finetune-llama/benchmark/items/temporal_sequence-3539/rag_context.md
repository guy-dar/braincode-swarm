# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 18 needs (decomposition: llm), 113 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | action | t1:s2 | Schedule a meeting for Isabella, Sarah, Ava, Charlotte, and Sophia. | `minimum_per_period`, `entity_assembly_tips`, `entity_recipes`, `entity_grocery_list`, `obligation`, `search_travel`, `entity_appetizers`, `sequence`, `calculation`, `group_size`, `propose`, `format_numbered_list` |
| n2 | constraint | t1:s1 | Standard working hours are 9:00 to 17:00 local time on weekdays. | `unit_hour`*, `daytime`, `unit_day`, `unit_week`, `unit_minute`, `clock`, `unit_month`, `nighttime`, `topic_school_work_routine`, `cat_limited_time_offers`, `metric_uptime`, `time_point` |
| n3 | temporal | t1:s2 | The meeting must be scheduled within the current week. | `unit_week`*, `unit_day`, `unit_month`, `prep_time`, `unit_hour`, `time_point`, `daytime`, `cat_limited_time_offers`, `nighttime`, `duration`, `metric_order_late`, `rule_category_duration_unit_value` |
| n4 | constraint | t1:s3, t1:s4, t1:s5, t1:s6, t1:s7, t1:s8 | Respect Isabella's weekly schedule of free and booked times. | `cat_limited_time_offers`, `prep_time`, `unit_week`, `unit_day`, `unit_hour`, `daytime`, `unit_month`, `time_point`, `metric_uptime`, `clock`, `example_b_preserve_the_class_and_amount_of_an_itinerary_constraint`, `topic_school_work_routine` |
| n5 | constraint | t1:s9, t1:s10, t1:s11, t1:s12, t1:s13, t1:s14 | Respect Sarah's weekly schedule of free and booked times. | `cat_limited_time_offers`, `prep_time`, `unit_week`, `unit_day`, `unit_hour`, `daytime`, `unit_minute`, `clock`, `metric_uptime`, `time_point`, `metric_response_time`, `unit_month` |
| n6 | constraint | t1:s15, t1:s16, t1:s17, t1:s18, t1:s19, t1:s20 | Respect Ava's weekly schedule of free and booked times. | `cat_limited_time_offers`, `prep_time`, `unit_week`, `unit_day`, `unit_hour`, `unit_month`, `metric_uptime`, `metric_response_time`, `unit_minute`, `daytime`, `clock`, `rule_category_duration_unit_value` |
| n7 | constraint | t1:s21, t1:s22, t1:s23, t1:s24, t1:s25, t1:s26 | Respect Charlotte's weekly schedule of free and booked times. | `cat_limited_time_offers`, `prep_time`, `unit_week`, `daytime`, `unit_day`, `clock`, `unit_hour`, `time_point`, `valet`, `nighttime`, `metric_uptime`, `constraint_budget_limited` |
| n8 | constraint | t1:s27, t1:s28, t1:s29, t1:s30, t1:s31, t1:s32 | Respect Sophia's weekly schedule of free and booked times. | `cat_limited_time_offers`, `prep_time`, `unit_week`, `unit_day`, `daytime`, `unit_hour`, `metric_uptime`, `clock`, `unit_month`, `metric_response_time`, `unit_minute`, `constraint_budget_limited` |
| n9 | constraint | t1:s33 | Isabella can clear her morning schedule from 9:00 to 9:45 if needed. | `daytime`, `unit_hour`, `nighttime`, `clock`, `unit_day`, `time_point`, `unit_week`, `prep_time`, `unit_minute`, `constraint_exclude_flowery_language`, `event_sadie_adler_unmasking`, `constraint_budget_limited` |
| n10 | constraint | t1:s34 | Sarah only accepts meetings on Mondays and Thursdays if they are at most 1 hour long. | `unit_hour`*, `at_most`*, `unit_week`, `unit_day`, `unit_minute`, `cat_limited_time_offers`, `daytime`, `topic_school_work_routine`, `entity_grocery_list`, `format_newsletter`, `example_b_preserve_the_class_and_amount_of_an_itinerary_constraint`, `wait` |
| n11 | constraint | t1:s35 | Ava can stay until 18:00 to accommodate the meeting. | `minimum_per_period`, `unit_hour`, `unit_minute`, `metric_response_time`, `rule_category_duration_unit_value`, `clock`, `prep_time`, `constraint_budget_limited`, `works_best`, `night_stand`, `constraint_exclude_flowery_language`, `constraint_include_character_attribute_list` |
| n12 | constraint | t1:s36 | Charlotte needs a lunch break on Wednesday from 12:30 to 13:00. | `cuisine_mediterranean`, `night_stand`, `nighttime`, `cuisine_pizza`, `constraint_budget_limited`, `restaurant`, `clock`, `constraint_include_character_attribute_list`, `time_point`, `eastern_cape`, `bread`, `cat_limited_time_offers` |
| n13 | constraint | t1:s37 | Sophia can miss the last 10 minutes of the meeting. | `unit_minute`*, `metric_order_late`, `metric_response_time`, `nighttime`, `wait`, `rule_category_duration_unit_value`, `time_horizon`, `event_sadie_adler_unmasking`, `temporal_context`, `constraint_exclude_flowery_language`, `unit_sentence`, `constraint_budget_limited` |
| n14 | constraint | t1:s38 | The meeting must start on the hour or half hour. | `unit_hour`*, `clock`, `unit_week`, `unit_minute`, `unit_day`, `minimum_per_period`, `daytime`, `time_point`, `unit_month`, `prep_time`, `example_b_preserve_the_class_and_amount_of_an_itinerary_constraint`, `wait` |
| n15 | action | t1:s38 | Compute X, the length of the longest possible meeting in minutes. | `unit_minute`*, `example_b_preserve_the_class_and_amount_of_an_itinerary_constraint`, `wait`, `duration`, `minimum_per_period`, `unit_hour`, `unit_week`, `maximum_between_stops`, `rule_category_duration_unit_value`, `unit_day`, `prep_time`, `cat_limited_time_offers` |
| n16 | action | t1:s39 | Compute Y, the number of possible options for such longest meetings. | `wait`, `minimum_per_period`, `duration`, `unit_week`, `unit_hour`, `rule_category_duration_unit_value`, `unit_minute`, `maximum_between_stops`, `prep_time`, `cat_limited_time_offers`, `metric_response_time`, `calculation` |
| n17 | constraint | t1:s40 | Report X and Y separated by a comma. | `format_structured_report`*, `sequence`, `unit_sentence`, `format_numbered_list`, `unit_paragraph`, `constraint_budget_limited`, `constraint_exclude_flowery_language`, `in_front_of`, `left_of`, `constraint_exclude_liberation_theme`, `respond`, `constraint_include_character_attribute_list` |
| n18 | constraint | t1:s41 | If X is 0, report 0, 0. | `extract`, `format_structured_report`*, `constraint_budget_limited`, `unit_second`, `unit_item`, `constraint_exclude_flowery_language`, `calculation`, `measure`, `tone_neutral`, `constraint_exclude_liberation_theme`, `negation`, `unit_gram` |

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

- search_travel.location → country
- measure.unit → currency
- activity.object → object_label, food_label, animal_label
- activity.location → country
- activity.instrument → object_label, platform_label
- subject.qualifier → platform_label
- subject.location → country
- requirement.value → platform_label
- failure.system → platform_label

## Retrieved records

### Shared rules that govern the records below (full text)

**rule_lexical_groups** (v19/rule/lexical-groups; rule governing platform_label)

Section 3.1 defines value groups: `group::key` values of type ATOM[group]. Open groups admit any key of their form (examples are not whitelists); standard groups admit the codes of their bundled standard (ISO 3166-1 alpha-2 for country, ISO 4217 for currency). Leaf values are never glossary entries. Consumer signatures alone decide where a group may appear. Retired bare symbols are invalid.

**rule_reading_guide** (v19/rule/reading-guide; core)

The spec governs syntax/types; this glossary defines vocabulary. Signature notation: ? optional, A / B explicit alternatives, void no result. Omitted optional arguments are unspecified. Value entries are category-refined STRING primitives; complex meanings require composition. Aliases are contextual hints, not unconditional equivalences. Report ambiguity. IDs use v19/<category>/<symbol>, v19/support/<symbol> or v19/composite/<symbol>. Statuses apply to this candidate: Retained preserves meaning; Adapted uses the stated contract; Composite requires TERM (bare STRING deprecated); Structural is syntax/argument vocabulary; Needs clarification is unusable until resolved; Deprecated is historical; Accepted is usable within this candidate.

**rule_recording_signatures** (v19/rule/recording-signatures; rule governing search_travel)

RECORD ACTION uses the operation signature with REF[STRING] → TERM and LIST[REF[STRING]] → LIST[TERM]; other types/categories stay unchanged. Return EVENT, never the runtime result. Record actual outputs as attributed CLAIMs. Do not infer missing resources.

**rule_speech_acts_general** (v19/rule/speech-acts-general; rule governing propose)

UTTER-only, void, with the spec's speech attributes and LIST[TERM] constraints. No result binding. Literal content cannot replace required semantic arguments for structured coverage.

**rule_structural_constructs** (v19/rule/structural-constructs; core)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; rule governing prep_time)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_attributes_and_generate** (v19/rule/attributes-and-generate; rule governing art_itinerary)

Attribute entries name arguments; legality/types come from each operation, not global membership. GENERATE uses the spec's core fields; retained artifact profiles return STRING. Numeric/list results need explicit profiles. Legacy itinerary fields expand to TERM constraints: duration/duration_unit → duration(amount,unit); stop_min_per_day/stop_requirement → minimum_per_period(class,count,period=unit_day), never an inferred temple class; max_walk_duration/unit → maximum_between_stops(activity="walk",amount,unit). No legacy shorthand is enabled. Old events/character_properties/transformations become explicitly scoped TERM constraints. Message purpose is TERM, not send_email.content: GENERATE exact STRING content, then send. Report opaque fallback separately.

**rule_category_artifact_value** (v19/rule/category/artifact-value; rule governing art_itinerary)

STRING artifact class for GENERATE.target. art_story says what kind of artifact to produce, not what occurs in its plot.

**rule_category_constraint_value** (v19/rule/category/constraint-value; rule governing constraint_budget_limited)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_content_value** (v19/rule/category/content-value; rule governing content_kyoto_itinerary)

Existing compounds become the constructors in Section 5. Their outputs go in topic/target/constraints as appropriate, not content, whose spec type remains STRING.

**rule_category_cuisine_value** (v19/rule/category/cuisine-value; rule governing cuisine_mediterranean)

STRING cuisine class; cuisine_indian is a cuisine filter, not the location India.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; candidate)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing entity_assembly_tips)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_event_value** (v19/rule/category/event-value; rule governing event_sadie_adler_unmasking)

TERM-described narrative event, not a recorded EVENT. Require inclusion explicitly when generating a story.

**rule_category_format_value** (v19/rule/category/format-value; rule governing format_numbered_list)

STRING format. format_email is layout, not the action send_email.

**rule_category_location_name** (v19/rule/category/location-name; rule governing night_stand)

STRING location descriptor. A `table` surface is not the generated artifact category art_table.

**rule_category_metric_value** (v19/rule/category/metric-value; rule governing metric_uptime)

STRING metric identity, not a Boolean value. Uptime and response time need numeric observations with units; order-late is Boolean-valued. Do not type every metric as BOOL.

**rule_category_product_attribute_value** (v19/rule/category/product-attribute-value; rule governing valet)

STRING color/size/product-market facets. gender_women describes a product category, not an assertion about a person's gender.

**rule_category_search_value** (v19/rule/category/search-value; rule governing cat_limited_time_offers)

STRING refinements rank_ / dir_ / cat_ / avail_ / genre_ are separate. rank_rating may fill rank_field; genre_label::comedy may not. “Cheapest” usually requires both rank_price and dir_asc, not rank_price alone.

**rule_category_semantic_category_value** (v19/rule/category/semantic-category-value; rule governing class_temple)

STRING class label used by typed constraints. class_temple describes a class, not an acquired physical temple reference.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing in_front_of)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_tone_value** (v19/rule/category/tone-value; rule governing tone_neutral)

STRING register. tone_urgent describes urgency, not a concrete deadline.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_school_work_routine)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_composites_general** (v19/rule/composites-general; rule governing topic_school_work_routine)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_examples_general** (v19/rule/examples-general; rule governing example_b_preserve_the_class_and_amount_of_an_itinerary_constraint)

Examples use this glossary's contracts. They have not been verified by an implemented BrainCode parser.

**rule_operations_general** (v19/rule/operations-general; rule governing search_travel)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_supplemental_general** (v19/rule/supplemental-general; rule governing extract)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; rule governing minimum_per_period)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- extract | operation | operation-vocabulary | (target: LIST[REF[STRING]], limit: NUMBER) -> LIST[REF[STRING]] | First limit results, preserving order and identity; limit is a nonnegative integer; limit=1 is still a list  ⟵ candidate
- search_travel | operation | operation-vocabulary | (target: STRING, constraints?: LIST[TERM], location?: STRING / ATOM[country]) -> LIST[REF[STRING]] | Query travel options meeting supplied constraints. Does not book them.  ⟵ candidate
- wait | operation | operation-vocabulary | (duration?: NUMBER) -> void | Pause execution for a duration or cycle. duration in seconds or ticks. | aliases: idle, pause  ⟵ candidate

### speech acts

- propose | speech_act | operation-vocabulary | UTTER propose(target: TERM) | Suggest an action/idea; does not record it as performed.  ⟵ candidate
- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ dependency of obligation
- at_most | constructor | TERM at_most(measure: TERM) -> TERM | An upper bound: the constrained value is less than or equal to the given measure (or number term). Use inside requirement(value=...). | not: an exact value or a target to aim for | aliases: at most, maximum, up to, no more than, under  ⟵ candidate
- calculation | constructor | TERM calculation(inputs: LIST[TERM], operation: STRING, result?: TERM) -> TERM | Constructs a descriptive representation of an arithmetic or algorithmic calculation step with inputs, operation identifier, and optional resulting value. | not: an executed runtime action or factual claim of outcome | aliases: math_operation, compute_step  ⟵ candidate
- conjunction | constructor | TERM conjunction(items: LIST[TERM]) -> TERM | All described components apply | not: Does not imply temporal order  ⟵ dependency of topic_school_work_routine
- document_section | constructor | TERM document_section(title: STRING, items?: LIST[TERM]) -> TERM | Constructs a structural document section descriptor with a section title and optional content items. | not: a complete document artifact class (use art_structured_report) | aliases: section, report_section, article_section  ⟵ candidate
- duration | constructor | TERM duration(amount: NUMBER, unit: STRING) -> TERM | Requested elapsed/calendar extent | not: Word/item counts are not time  ⟵ candidate
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ dependency of constraint_exclude_flowery_language
- group_size | constructor | TERM group_size(count: NUMBER, group?: STRING / TERM) -> TERM | The headcount or number of members in a specified group or party; count is a nonnegative integer. | not: minimum_per_period (a per-period minimum bound) or measure (measured quantities with units) | aliases: party_size, party of, number of guests, guest_count  ⟵ candidate
- include | constructor | TERM include(item: STRING / TERM) -> TERM | Require the identified content/item | not: Not permission to invent an instance in a recorded trace  ⟵ dependency of constraint_include_character_attribute_list
- maximum_between_stops | constructor | TERM maximum_between_stops(activity: STRING, amount: NUMBER, unit: STRING) -> TERM | Upper bound on the stated activity between successive stops | not: Not a limit on total daily duration  ⟵ candidate
- measure | constructor | TERM measure(amount: NUMBER, unit: STRING / ATOM[currency]) -> TERM | A measured amount: a number with its unit symbol (a unit-category value such as unit_minute, cap_gb or currency::USD). Describes the amount only; asserts nothing. ATOM[currency] is also accepted and supplies the pinned currency identity; no exchange rate or conversion is implicit. | not: a symbol with the number baked in (char_age_18, size_16gb); a unitless count (use the quantity argument) | aliases: amount of, size of, measured in  ⟵ candidate
- minimum_per_period | constructor | TERM minimum_per_period(class: STRING, count: NUMBER, period: STRING) -> TERM | At least count members of class in each period | not: Not a minimum total over the whole artifact  ⟵ candidate
- negation | constructor | TERM negation(target: TERM) -> TERM | Constructs a descriptive semantic negation of a target descriptive proposition or condition term. | not: Check's runtime Boolean operator NOT or a speech-act decline | aliases: not, does not, negation, absence of  ⟵ candidate
- obligation | constructor | TERM obligation(actor: STRING / TERM, activity: TERM) -> TERM | Constructs a deontic obligation description requiring an actor to perform an activity. actor and activity specified. | aliases: duty, mandatory_activity  ⟵ candidate
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ dependency of constraint_budget_limited
- sequence | constructor | TERM sequence(items: LIST[TERM]) -> TERM | Ordered described activities/content | not: Not unordered conjunction  ⟵ candidate
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ dependency of topic_school_work_routine
- temporal_context | constructor | TERM temporal_context(activity: STRING / TERM, period?: STRING) -> TERM | Constructs a temporal or situational context descriptor specifying an ongoing process, evaluation phase, or historical timeframe. | not: time_point (a specific timestamp/date) or duration (an elapsed numerical duration) | aliases: while, during, in past relationships, timeframe  ⟵ candidate
- time_horizon | constructor | TERM time_horizon(horizon: STRING) -> TERM | Constructs a temporal horizon or prospective timeframe descriptor indicating relative temporal distance into the future. | not: a specific calendar timestamp (use time_point) or an elapsed numerical duration (use duration). | aliases: future, future timeframe, time horizon, far off in the future, far future  ⟵ candidate
- time_point | constructor | TERM time_point(date?: STRING, time?: STRING, timezone?: STRING) -> TERM | Constructs a structured representation of a specific calendar date, time of day, or scheduled timestamp. | not: an elapsed time duration (use duration) | aliases: timestamp, datetime, scheduled_time  ⟵ candidate

### composites

- constraint_budget_limited | composite | constraint-value | TERM constraint_budget_limited() -> TERM | Limited budget. | = requirement(property="budget_limited", value=TRUE)  ⟵ candidate
- constraint_exclude_flowery_language | composite | constraint-value | TERM constraint_exclude_flowery_language() -> TERM | Avoid flowery language. | = exclude(item="flowery_language")  ⟵ candidate
- constraint_exclude_liberation_theme | composite | constraint-value | TERM constraint_exclude_liberation_theme() -> TERM | Avoid liberation theme. | = exclude(item="liberation_theme")  ⟵ candidate
- constraint_include_character_attribute_list | composite | constraint-value | TERM constraint_include_character_attribute_list() -> TERM | Include character attributes. | = include(item="character_attribute_list")  ⟵ candidate
- content_kyoto_itinerary | composite | content-value | TERM content_kyoto_itinerary() -> TERM | A Kyoto itinerary subject. | = subject(kind="itinerary", location="Kyoto")  ⟵ dependency of example_b_preserve_the_class_and_amount_of_an_itinerary_constraint
- event_sadie_adler_unmasking | composite | event-value | TERM event_sadie_adler_unmasking() -> TERM | Sadie Adler taking off her hat and peeling skin. | = sequence(items=[activity(verb="remove", actor="Sadie Adler", object="hat"), activity(verb="peel", actor="Sadie Adler", object="skin")])  ⟵ candidate
- topic_school_work_routine | composite | topic-value | TERM topic_school_work_routine() -> TERM | School and work routine. | = subject(kind="routine", qualifier=conjunction(items=[subject(kind="school"), subject(kind="work")]))  ⟵ candidate

### claim relations

- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ core
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ core
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
- cuisine_mediterranean | value | cuisine-value | Mediterranean culinary cuisine style. | aliases: mediterranean  ⟵ candidate
- cuisine_pizza | value | cuisine-value | Pizza culinary cuisine style and food category. | not: cuisine_italian (broader regional/national cuisine) | aliases: pizza, pizzeria, pizza cuisine  ⟵ candidate
- unit_day | value | duration-unit-value | Day. | aliases: days  ⟵ candidate
- unit_hour | value | duration-unit-value | Hour. | aliases: hours  ⟵ candidate
- unit_item | value | duration-unit-value | Top-level generated list or report item. | aliases: items, entries  ⟵ candidate
- unit_minute | value | duration-unit-value | Minute. | aliases: minutes, min  ⟵ candidate
- unit_month | value | duration-unit-value | Month. | aliases: months  ⟵ candidate
- unit_paragraph | value | duration-unit-value | Paragraph of text. | aliases: paragraphs, paragraph  ⟵ candidate
- unit_second | value | duration-unit-value | Second. | aliases: seconds, sec  ⟵ candidate
- unit_sentence | value | duration-unit-value | One grammatical sentence in text generation or constraint counting. | not: unit_paragraph (paragraph block) or unit_word (individual word) | aliases: sentence, sentences  ⟵ candidate
- unit_week | value | duration-unit-value | Week. | aliases: weeks  ⟵ candidate
- bread | value | entity-name | A bread loaf or slice food object. | aliases: bread  ⟵ candidate
- clock | value | entity-name | A clock timepiece appliance. | not: duration units like unit_hour | aliases: clock, timer  ⟵ candidate
- entity_appetizers | value | entity-name | Event planning item or menu category: entity_appetizers. | aliases: entity_appetizers  ⟵ candidate
- entity_assembly_tips | value | entity-name | Event planning item or menu category: entity_assembly_tips. | aliases: entity_assembly_tips  ⟵ candidate
- entity_grocery_list | value | entity-name | Event planning item or menu category: entity_grocery_list. | aliases: entity_grocery_list  ⟵ candidate
- entity_recipes | value | entity-name | Event planning item or menu category: entity_recipes. | aliases: entity_recipes  ⟵ candidate
- restaurant | value | entity-name | A commercial restaurant, eatery, or dining establishment where meals are prepared and served. | not: ryokan or onsen (specific traditional hospitality establishments) | aliases: restaurant, eatery, dining establishment, restaurants  ⟵ candidate
- textbook | value | entity-name | A textbook or instructional book used as an educational resource. | not: style_academic (which is a stylistic mode) or art_short_text (which is a brief generated text artifact) | aliases: textbook, book, coursebook, textbooks  ⟵ candidate
- format_newsletter | value | format-value | Newsletter layout. | aliases: newsletter  ⟵ candidate
- format_numbered_list | value | format-value | Numbered list. | aliases: numbered steps  ⟵ candidate
- format_structured_report | value | format-value | Headed structured report layout. | aliases: structured report, report  ⟵ candidate
- eastern_cape | value | location-name | Eastern Cape region.  ⟵ candidate
- night_stand | value | location-name | A small bedside table or nightstand furniture surface. | not: a chest of drawers (use dresser) or a general table surface (use table) | aliases: nightstand, bedside table  ⟵ candidate
- metric_order_late | value | metric-value | Whether an order is late. | aliases: order is late, delayed  ⟵ candidate
- metric_response_time | value | metric-value | Support response time. | aliases: response time  ⟵ candidate
- metric_uptime | value | metric-value | Service uptime status. | aliases: uptime, is up  ⟵ candidate
- valet | value | product-attribute-value | Valet parking or dedicated vehicle attendant service. | aliases: valet_parking  ⟵ candidate
- cat_limited_time_offers | value | search-value | Category: time-limited deals.  ⟵ candidate
- class_temple | value | semantic-category-value | The abstract class of temples. | aliases: temple, temples  ⟵ dependency of example_b_preserve_the_class_and_amount_of_an_itinerary_constraint
- in_front_of | value | spatial-relation | Positioned in front of. | aliases: in front of  ⟵ candidate
- left_of | value | spatial-relation | To the left of. | aliases: left of  ⟵ candidate
- daytime | value | time-of-day-value | The period of natural daylight between sunrise and sunset in the diurnal cycle. | not: unit_day (a 24-hour elapsed duration unit) or clock time timestamps | aliases: daytime, day, day time, daylight hours  ⟵ candidate
- nighttime | value | time-of-day-value | The period of darkness between sunset and sunrise in the diurnal cycle. | not: night_stand (a piece of furniture) or clock time timestamps | aliases: nighttime, night, night time, darkness  ⟵ candidate
- tone_neutral | value | tone-value | Plain, unmarked register.  ⟵ candidate
- unit_gram | value | unit-value | Standard metric measurement unit of mass equal to 1/1,000 of a kilogram (0.001 kg). | not: digital capacity units (like cap_gb) or temporal duration units | aliases: g, gram, grams  ⟵ candidate

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

