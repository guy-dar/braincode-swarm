# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 13 needs (decomposition: llm), 128 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | claim | t1:s1 | The user has a table with 30 rows and 18 columns. | `table`*, `format_table`, `transform_preserve_first_column`, `night_stand`, `format_numbered_list`, `desk`, `format_structured_report`, `user_practice`, `unit_paragraph`, `minimum_per_period`, `request`, `rule_category_location_name` |
| n2 | claim | t1:s2 | The table was converted to markdown format. | `table`*, `format_table`, `format_markdown`, `format_xlsx`, `night_stand`, `transform_preserve_first_column`, `desk`, `format_structured_report`, `format_numbered_list`, `rule_category_location_name`, `format_bullet_list`, `occurred_recently` |
| n3 | object | t1:s3, t1:s4, t1:s5, t1:s6, t1:s7, t1:s8, t1:s9, t1:s10, t1:s11, t1:s12, t1:s13, t1:s14, t1:s15, t1:s16, t1:s17, t1:s18, t1:s19, t1:s20, t1:s21, t1:s22, t1:s23, t1:s24, t1:s25, t1:s26, t1:s27, t1:s28, t1:s29, t1:s30, t1:s31, t1:s32, t1:s33 | The markdown table containing data with some ERROR and null values. | `table`*, `format_markdown`, `format_table`, `raises_exception`, `format_structured_report`, `format_numbered_list`, `unit_item`, `night_stand`, `issue`, `assert_multinomial_scorer`, `warning`, `rule_category_location_name` |
| n4 | claim | t1:s34 | The conversion code was buggy and replaced some values with ERROR. | `raises_exception`, `currency`, `rule_category_code_value`, `sym_pandas_testing_assert_almost_equal`, `issue`, `sym_log_reg_scoring_path`, `outcome`, `warning`, `chg_modify_code`, `transform_remove_br`, `modify_code`, `prep_time` |
| n5 | object | t1:s35 | A list of replacement values for the ERROR cells in column-order. | `transform_preserve_first_column`, `format_numbered_list`, `sort`, `format_table`, `table`, `unit_item`, `metric_order_late`, `format_bullet_list`, `assert_multinomial_scorer`, `pick_up`, `rule_examples_general`, `entity_order_vs_assemble_plan` |
| n6 | action | t1:s34, t1:s35 | Replace the ERROR values in the table with the provided list of values in column-order. | `table`*, `transform_preserve_first_column`, `format_table`, `format_numbered_list`, `sort`, `add_to_cart`, `calculation`, `pick_up`, `format_bullet_list`, `modify_code`, `extract`, `metric_order_late` |
| n7 | action | t1:s36 | Compute the absolute difference between the sum of music_listening_minutes and study_minutes. | `unit_minute`*, `between`*, `rule_category_duration_unit_value`, `rate`, `minimum_per_period`, `unit_hour`, `maximum_between_stops`, `unit_second`, `metric_response_time`, `unit_sentence`, `unit_week`, `unit_day` |
| n8 | constraint | t1:s36 | Only consider days where the number of calls was greater than 2. | `unit_day`*, `daytime`*, `unit_week`, `unit_minute`, `unit_hour`, `unit_sentence`, `unit_month`, `unit_second`, `rule_category_duration_unit_value`, `cat_limited_time_offers`, `unit_year`, `wait` |
| n9 | constraint | t1:s36 | Only consider days where the sleep minutes was greater than 350. | `unit_minute`*, `unit_day`*, `daytime`*, `unit_hour`, `nighttime`, `unit_week`, `metric_response_time`, `size_queen`, `unit_month`, `time_point`, `rule_category_duration_unit_value`, `minimum_per_period` |
| n10 | constraint | t1:s37 | Round the final result to 2 decimal places. | `shape_round`*, `format_numbered_list`, `metric_response_time`, `unit_second`, `shape_square`, `shape_rectangular`, `calculation`, `assert_multinomial_scorer`, `maximum_between_stops`, `shape_triangular`, `shape_oval`, `rank_distance` |
| n11 | constraint | t1:s38 | Assume the condition is not satisfied if it cannot be determined due to null values. | `constraint_single_choice`, `rule_category_constraint_value`, `assert_multinomial_scorer`, `test_condition`, `constraint_budget_limited`, `medical_condition`*, `conditional`, `at_least`, `raises_exception`, `constraint_include_character_attribute_list`, `rule_category_reservation_status_value`, `constraint_comprehensive` |
| n12 | constraint | t1:s39 | Ignore null values from the computations. | `extract`, `calculation`, `maximum_between_stops`, `tone_neutral`, `constraint_budget_limited`, `raises_exception`, `pick_up`, `rule_category_capacity_unit_value`, `constraint_include_character_attribute_list`, `wait`, `constraint_exclude_flowery_language`, `exclude` |
| n13 | constraint | t1:s40 | Output 0 if any of the sums cannot be computed due to no values. | `constraint_budget_limited`, `calculation`, `measure`, `assert_multinomial_scorer`, `state_empty`, `tone_neutral`, `test_condition`, `at_most`, `extract`, `pick_up`, `at_least`, `quantity` |

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

- issue.project → platform_label
- chg_modify_code.target → platform_label
- modify_code.target → platform_label
- pick_up.target → object_label, food_label
- pick_up.source → object_label
- pick_up.color → color_label
- place.destination → object_label
- place.location → object_label
- measure.unit → currency
- activity.object → object_label, food_label, animal_label
- activity.location → country
- activity.instrument → object_label, platform_label
- requirement.value → platform_label
- subject.qualifier → platform_label
- subject.location → country
- pull_request.project → platform_label
- failure.system → platform_label

## Retrieved records

### Shared rules that govern the records below (full text)

**rule_lexical_groups** (v19/rule/lexical-groups; rule governing platform_label)

Section 3.1 defines value groups: `group::key` values of type ATOM[group]. Open groups admit any key of their form (examples are not whitelists); standard groups admit the codes of their bundled standard (ISO 3166-1 alpha-2 for country, ISO 4217 for currency). Leaf values are never glossary entries. Consumer signatures alone decide where a group may appear. Retired bare symbols are invalid.

**rule_reading_guide** (v19/rule/reading-guide; core)

The spec governs syntax/types; this glossary defines vocabulary. Signature notation: ? optional, A / B explicit alternatives, void no result. Omitted optional arguments are unspecified. Value entries are category-refined STRING primitives; complex meanings require composition. Aliases are contextual hints, not unconditional equivalences. Report ambiguity. IDs use v19/<category>/<symbol>, v19/support/<symbol> or v19/composite/<symbol>. Statuses apply to this candidate: Retained preserves meaning; Adapted uses the stated contract; Composite requires TERM (bare STRING deprecated); Structural is syntax/argument vocabulary; Needs clarification is unusable until resolved; Deprecated is historical; Accepted is usable within this candidate.

**rule_recording_signatures** (v19/rule/recording-signatures; rule governing modify_code)

RECORD ACTION uses the operation signature with REF[STRING] → TERM and LIST[REF[STRING]] → LIST[TERM]; other types/categories stay unchanged. Return EVENT, never the runtime result. Record actual outputs as attributed CLAIMs. Do not infer missing resources.

**rule_speech_acts_general** (v19/rule/speech-acts-general; core)

UTTER-only, void, with the spec's speech attributes and LIST[TERM] constraints. No result binding. Literal content cannot replace required semantic arguments for structured coverage.

**rule_structural_constructs** (v19/rule/structural-constructs; core)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; rule governing user_practice)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_attributes_and_generate** (v19/rule/attributes-and-generate; rule governing quantity)

Attribute entries name arguments; legality/types come from each operation, not global membership. GENERATE uses the spec's core fields; retained artifact profiles return STRING. Numeric/list results need explicit profiles. Legacy itinerary fields expand to TERM constraints: duration/duration_unit → duration(amount,unit); stop_min_per_day/stop_requirement → minimum_per_period(class,count,period=unit_day), never an inferred temple class; max_walk_duration/unit → maximum_between_stops(activity="walk",amount,unit). No legacy shorthand is enabled. Old events/character_properties/transformations become explicitly scoped TERM constraints. Message purpose is TERM, not send_email.content: GENERATE exact STRING content, then send. Report opaque fallback separately.

**rule_category_capacity_unit_value** (v19/rule/category/capacity-unit-value; candidate)

Preserve original binary-unit definitions for audit, but mark Needs clarification: GB/TB aliases conflate decimal and binary units. No silent change to scale.

**rule_category_code_value** (v19/rule/category/code-value; candidate)

path_/sym_ remain STRING identities; migrated chg_/assert_ are TERM constructors. Do not recover an exact file path by guessing from underscores.

**rule_category_constraint_value** (v19/rule/category/constraint-value; candidate)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; candidate)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing desk)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_format_value** (v19/rule/category/format-value; rule governing format_table)

STRING format. format_email is layout, not the action send_email.

**rule_category_location_name** (v19/rule/category/location-name; candidate)

STRING location descriptor. A `table` surface is not the generated artifact category art_table.

**rule_category_metric_value** (v19/rule/category/metric-value; candidate)

STRING metric identity, not a Boolean value. Uptime and response time need numeric observations with units; order-late is Boolean-valued. Do not type every metric as BOOL.

**rule_category_product_attribute_value** (v19/rule/category/product-attribute-value; rule governing size_queen)

STRING color/size/product-market facets. gender_women describes a product category, not an assertion about a person's gender.

**rule_category_reservation_status_value** (v19/rule/category/reservation-status-value; candidate)

STRING filter states; neither is a BOOL result binding. check_reservation_availability returns a BOOL with a distinct handle.

**rule_category_search_value** (v19/rule/category/search-value; rule governing cat_limited_time_offers)

STRING refinements rank_ / dir_ / cat_ / avail_ / genre_ are separate. rank_rating may fill rank_field; genre_label::comedy may not. “Cheapest” usually requires both rank_price and dir_asc, not rank_price alone.

**rule_category_shape_value** (v19/rule/category/shape-value; rule governing shape_round)

STRING geometry. shape_round may select a circular object; it does not imply color or dimensions.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing between)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_state_value** (v19/rule/category/state-value; rule governing state_empty)

STRING condition used in selection. state_warm does not command heat; “hot” is not automatically synonymous with “warm.”

**rule_category_tone_value** (v19/rule/category/tone-value; rule governing tone_concise)

STRING register. tone_urgent describes urgency, not a concrete deadline.

**rule_category_transformation_value** (v19/rule/category/transformation-value; rule governing transform_preserve_first_column)

TERM-described transformation. Pass it through constraints; no ungoverned transformations attribute.

**rule_composites_general** (v19/rule/composites-general; rule governing transform_preserve_first_column)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_examples_general** (v19/rule/examples-general; candidate)

Examples use this glossary's contracts. They have not been verified by an implemented BrainCode parser.

**rule_operations_general** (v19/rule/operations-general; rule governing modify_code)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_search_web_attributes** (v19/rule/search-web-attributes; rule governing sort)

Optional filters: availability, category, color, cuisine, currency, gender, genre, location, platform, ram_unit, reservation_availability, shape, size (category-refined STRING); max_price, min_ram, min_rating (NUMBER); trending (BOOL). Explicit signature alternatives additionally admit atoms. Price requires currency; RAM requires a capacity unit; no default scale/source. rank is invalid: use sort, whose rank_field accepts rank_* and rank_direction accepts dir_*. Category/genre/availability accept only their own subfamilies.

**rule_supplemental_general** (v19/rule/supplemental-general; rule governing extract)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; rule governing minimum_per_period)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- add_to_cart | operation | operation-vocabulary | (target: LIST[REF[STRING]]) -> void | Add the explicitly selected items. Does not pay or place an order.  ⟵ candidate
- extract | operation | operation-vocabulary | (target: LIST[REF[STRING]], limit: NUMBER) -> LIST[REF[STRING]] | First limit results, preserving order and identity; limit is a nonnegative integer; limit=1 is still a list  ⟵ candidate
- modify_code | operation | operation-vocabulary | (target: STRING / ATOM[platform_label], file: STRING, revision: TERM, method?: STRING) -> void | Apply the structured change to the indicated code. A method name alone does not specify the change. | aliases: fix, reduce, optimize  ⟵ candidate
- pick_up | operation | operation-vocabulary | (target: STRING / ATOM[object_label] / ATOM[food_label], quantity?: NUMBER, source?: STRING / ATOM[object_label], color?: STRING / ATOM[color_label], shape?: STRING, state?: STRING) -> REF[STRING] or LIST[REF[STRING]] | Select/acquire objects. Missing quantity or literal 1 returns REF; integer literal greater than 1 returns LIST[REF]. Other values are invalid for this profile. | aliases: grab, take, retrieve  ⟵ candidate
- place | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label], location?: STRING / ATOM[object_label], relation?: STRING) -> void | Place an already acquired object. Spatial relation must be explicit if the source distinguishes it. | aliases: put, insert  ⟵ candidate
- sort | operation | operation-vocabulary | (target: LIST[REF[STRING]], rank_direction: STRING, rank_field: STRING) -> LIST[REF[STRING]] | Request ordering of selected results. Preserve member identity; this is not a claim that order was observed. | aliases: rank, order by  ⟵ candidate
- wait | operation | operation-vocabulary | (duration?: NUMBER) -> void | Pause execution for a duration or cycle. duration in seconds or ticks. | aliases: idle, pause  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ dependency of user_practice
- at_least | constructor | TERM at_least(measure: TERM) -> TERM | A lower bound: the constrained value is greater than or equal to the given measure (or number term). Use inside requirement(value=...). | not: an exact value; a strict 'more than' only when the source says so explicitly | aliases: at least, minimum, or more, no less than, plus  ⟵ candidate
- at_most | constructor | TERM at_most(measure: TERM) -> TERM | An upper bound: the constrained value is less than or equal to the given measure (or number term). Use inside requirement(value=...). | not: an exact value or a target to aim for | aliases: at most, maximum, up to, no more than, under  ⟵ candidate
- calculation | constructor | TERM calculation(inputs: LIST[TERM], operation: STRING, result?: TERM) -> TERM | Constructs a descriptive representation of an arithmetic or algorithmic calculation step with inputs, operation identifier, and optional resulting value. | not: an executed runtime action or factual claim of outcome | aliases: math_operation, compute_step  ⟵ candidate
- chg_modify_code | constructor | TERM chg_modify_code(target: STRING / ATOM[platform_label], file: STRING / TERM, revision: TERM) -> TERM | Constructs a structured change specification describing code file modifications. software engineering revision term. | aliases: modify_source_code  ⟵ candidate
- conditional | constructor | TERM conditional(condition: TERM, consequence: TERM) -> TERM | Constructs a structured conditional proposition term connecting a condition and consequence. descriptive logic structure. | aliases: if_then  ⟵ candidate
- distinguish | constructor | TERM distinguish(first: TERM, second: TERM, criterion?: STRING / TERM) -> TERM | Constructs a descriptive representation of discerning or differentiating between two entities, conditions, or behaviors along an optional criterion. | not: visual_contrast (optical contrast) or LINK contrast (rhetorical opposition between claims) | aliases: tell the difference, differentiate, distinguish between  ⟵ candidate
- duration | constructor | TERM duration(amount: NUMBER, unit: STRING) -> TERM | Requested elapsed/calendar extent | not: Word/item counts are not time  ⟵ dependency of wait
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ candidate
- group_size | constructor | TERM group_size(count: NUMBER, group?: STRING / TERM) -> TERM | The headcount or number of members in a specified group or party; count is a nonnegative integer. | not: minimum_per_period (a per-period minimum bound) or measure (measured quantities with units) | aliases: party_size, party of, number of guests, guest_count  ⟵ candidate
- include | constructor | TERM include(item: STRING / TERM) -> TERM | Require the identified content/item | not: Not permission to invent an instance in a recorded trace  ⟵ dependency of constraint_include_character_attribute_list
- issue | constructor | TERM issue(project: STRING / ATOM[platform_label], number: NUMBER) -> TERM | Constructs an issue tracker ticket reference. issue tracker descriptor. | aliases: issue_ticket, bug_report  ⟵ candidate
- maximum_between_stops | constructor | TERM maximum_between_stops(activity: STRING, amount: NUMBER, unit: STRING) -> TERM | Upper bound on the stated activity between successive stops | not: Not a limit on total daily duration  ⟵ candidate
- measure | constructor | TERM measure(amount: NUMBER, unit: STRING / ATOM[currency]) -> TERM | A measured amount: a number with its unit symbol (a unit-category value such as unit_minute, cap_gb or currency::USD). Describes the amount only; asserts nothing. ATOM[currency] is also accepted and supplies the pinned currency identity; no exchange rate or conversion is implicit. | not: a symbol with the number baked in (char_age_18, size_16gb); a unitless count (use the quantity argument) | aliases: amount of, size of, measured in  ⟵ candidate
- medical_condition | constructor | TERM medical_condition(condition: STRING, patient: STRING / TERM, severity?: STRING) -> TERM | Constructs a descriptive representation of a medical condition, pathology, or symptom profile. | not: an asserted factual attribution (use attribute_claim) or executed treatment | aliases: condition, symptom, pathology, diagnosis  ⟵ candidate
- minimum_per_period | constructor | TERM minimum_per_period(class: STRING, count: NUMBER, period: STRING) -> TERM | At least count members of class in each period | not: Not a minimum total over the whole artifact  ⟵ candidate
- preserve | constructor | TERM preserve(component: STRING, index: NUMBER) -> TERM | Keep the indexed component unchanged, using one-based indexing | not: Not preserve all components  ⟵ dependency of transform_preserve_first_column
- pull_request | constructor | TERM pull_request(project: STRING / ATOM[platform_label], number: NUMBER) -> TERM | Constructs a repository pull request reference. software repository reference. | aliases: pr  ⟵ related to chg_modify_code
- rate | constructor | TERM rate(denominator: TERM, numerator: TERM) -> TERM | Constructs a structured proportional rate or frequency relating a numerator measured quantity to a denominator reference quantity. | not: an asserted factual attribution (use attribute_claim) or bound constraint (use requirement) | aliases: per_unit, ratio  ⟵ candidate
- remove_literal | constructor | TERM remove_literal(text: STRING) -> TERM | Remove occurrences of that exact literal in the stated artifact | not: Not remove similar markup unless specified  ⟵ dependency of transform_remove_br
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ dependency of constraint_budget_limited
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ dependency of considered
- test_condition | constructor | TERM test_condition(condition: STRING, expected: BOOL) -> TERM | A testable condition with the expected Boolean outcome | not: Expected outcome is not an observed result  ⟵ candidate
- time_point | constructor | TERM time_point(date?: STRING, time?: STRING, timezone?: STRING) -> TERM | Constructs a structured representation of a specific calendar date, time of day, or scheduled timestamp. | not: an elapsed time duration (use duration) | aliases: timestamp, datetime, scheduled_time  ⟵ candidate

### composites

- assert_multinomial_scorer | composite | code-value | TERM assert_multinomial_scorer() -> TERM | Assertion that multinomial probabilistic scoring succeeds. | = test_condition(condition="multinomial_probabilistic_scoring", expected=TRUE)  ⟵ candidate
- constraint_budget_limited | composite | constraint-value | TERM constraint_budget_limited() -> TERM | Limited budget. | = requirement(property="budget_limited", value=TRUE)  ⟵ candidate
- constraint_comprehensive | composite | constraint-value | TERM constraint_comprehensive() -> TERM | Must be comprehensive. | = requirement(property="comprehensive", value=TRUE)  ⟵ candidate
- constraint_exclude_flowery_language | composite | constraint-value | TERM constraint_exclude_flowery_language() -> TERM | Avoid flowery language. | = exclude(item="flowery_language")  ⟵ candidate
- constraint_include_character_attribute_list | composite | constraint-value | TERM constraint_include_character_attribute_list() -> TERM | Include character attributes. | = include(item="character_attribute_list")  ⟵ candidate
- constraint_respectful | composite | constraint-value | TERM constraint_respectful() -> TERM | Must be respectful. | = requirement(property="respectful", value=TRUE)  ⟵ candidate
- constraint_single_choice | composite | constraint-value | TERM constraint_single_choice() -> TERM | Must pick a single choice. | = requirement(property="choice_count", value=1)  ⟵ candidate
- transform_preserve_first_column | composite | transformation-value | TERM transform_preserve_first_column() -> TERM | Preserve the first column of a table. | = preserve(component="column", index=1)  ⟵ candidate
- transform_remove_br | composite | transformation-value | TERM transform_remove_br() -> TERM | Remove <br /> tags. | = remove_literal(text="<br />")  ⟵ candidate

### claim relations

- considered | claim_relation | CLAIM considered(subject: TERM) | Asserts that an agent or speaker evaluated or entertained a specific candidate term or concept. subject is the evaluated term. | aliases: evaluated, weighed  ⟵ candidate
- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ core
- occurred_recently | claim_relation | CLAIM occurred_recently(target: CLAIM) | Asserts temporal recency of an asserted occurrence or claim. temporal recency qualifier. | aliases: recently_happened  ⟵ candidate
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ candidate
- prep_time | claim_relation | CLAIM prep_time(value: TERM) | Asserts an estimated preparation or assembly time duration. time requirement assertion. | aliases: preparation_duration  ⟵ candidate
- raises_exception | claim_relation | CLAIM raises_exception(target?: TERM, exception_type: STRING, message?: STRING) | Asserts that an unhandled runtime error or exception was raised with the specified exception type, message, and target entity. | not: warning (a non-fatal library warning or deprecation notice) or failure (a general system failure hypothesis) | aliases: raises, exception, throws_error, type_error  ⟵ candidate
- request | claim_relation | CLAIM request(target: TERM / STRING) | Represents an active communicative request or constraint state in conversation tracking. target is the requested action or topic. | aliases: user_request  ⟵ candidate
- user_practice | claim_relation | CLAIM user_practice(activity: TERM) | Asserts a habitual, workflow, or recurring practice of a user. workflow practice. | aliases: habitual_activity  ⟵ candidate
- warning | claim_relation | CLAIM warning(message: STRING, target?: TERM) | Asserts a recorded library warning, deprecation notice, or advisory alert. system alert claim. | aliases: alert, deprecation_warning  ⟵ candidate

### links

- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ core
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ core
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ core

### values

- sym_log_reg_scoring_path | value | code-value | The _log_reg_scoring_path program symbol.  ⟵ candidate
- sym_pandas_testing_assert_almost_equal | value | code-value | Source code file path or exported symbol in scientific Python: sym_pandas_testing_assert_almost_equal. | aliases: sym_pandas_testing_assert_almost_equal  ⟵ candidate
- unit_character | value | duration-unit-value | One Unicode scalar value in the final rendered artifact; line endings are normalized to LF before counting. | aliases: characters, chars  ⟵ candidate
- unit_day | value | duration-unit-value | Day. | aliases: days  ⟵ candidate
- unit_hour | value | duration-unit-value | Hour. | aliases: hours  ⟵ candidate
- unit_item | value | duration-unit-value | Top-level generated list or report item. | aliases: items, entries  ⟵ candidate
- unit_minute | value | duration-unit-value | Minute. | aliases: minutes, min  ⟵ candidate
- unit_month | value | duration-unit-value | Month. | aliases: months  ⟵ candidate
- unit_paragraph | value | duration-unit-value | Paragraph of text. | aliases: paragraphs, paragraph  ⟵ candidate
- unit_second | value | duration-unit-value | Second. | aliases: seconds, sec  ⟵ candidate
- unit_sentence | value | duration-unit-value | One grammatical sentence in text generation or constraint counting. | not: unit_paragraph (paragraph block) or unit_word (individual word) | aliases: sentence, sentences  ⟵ candidate
- unit_week | value | duration-unit-value | Week. | aliases: weeks  ⟵ candidate
- unit_year | value | duration-unit-value | Year. | aliases: years  ⟵ candidate
- desk | value | entity-name | A work desk furniture surface. | aliases: desk  ⟵ candidate
- entity_order_vs_assemble_plan | value | entity-name | Event planning item or menu category: entity_order_vs_assemble_plan. | aliases: entity_order_vs_assemble_plan  ⟵ candidate
- format_bullet_list | value | format-value | Bulleted list. | aliases: bullet points  ⟵ candidate
- format_markdown | value | format-value | Markdown layout. | aliases: in markdown  ⟵ candidate
- format_numbered_list | value | format-value | Numbered list. | aliases: numbered steps  ⟵ candidate
- format_structured_report | value | format-value | Headed structured report layout. | aliases: structured report, report  ⟵ candidate
- format_table | value | format-value | Tabular layout. | aliases: as a table  ⟵ candidate
- format_xlsx | value | format-value | Microsoft Excel OpenXML spreadsheet document format (.xlsx). | not: format_table (general tabular display layout) or format_pdf | aliases: XLSX, Excel 2010, Excel files, xlsx  ⟵ candidate
- night_stand | value | location-name | A small bedside table or nightstand furniture surface. | not: a chest of drawers (use dresser) or a general table surface (use table) | aliases: nightstand, bedside table  ⟵ candidate
- table | value | location-name | A table surface.  ⟵ candidate
- metric_order_late | value | metric-value | Whether an order is late. | aliases: order is late, delayed  ⟵ candidate
- metric_response_time | value | metric-value | Support response time. | aliases: response time  ⟵ candidate
- size_queen | value | product-attribute-value | Queen-size dimension classification for beds, mattresses, and bedding. | not: size_large (generic large apparel/goods size) or size_king | aliases: queen, queen size, Queen  ⟵ candidate
- cat_limited_time_offers | value | search-value | Category: time-limited deals.  ⟵ candidate
- rank_distance | value | search-value | Rank field: proximity. | aliases: nearest, closest  ⟵ candidate
- shape_oval | value | shape-value | Oval. | aliases: oval  ⟵ candidate
- shape_rectangular | value | shape-value | Rectangular. | aliases: rectangular, rectangle  ⟵ candidate
- shape_round | value | shape-value | Circular/round. | aliases: round, circular  ⟵ candidate
- shape_square | value | shape-value | Square. | aliases: square  ⟵ candidate
- shape_triangular | value | shape-value | Triangular. | aliases: triangular, triangle  ⟵ candidate
- between | value | spatial-relation | Positioned between or in the middle of reference entities. | not: next_to or in_front_of | aliases: between, in the middle of, middle of, center of  ⟵ candidate
- state_empty | value | state-value | Contains no intended material or usable remaining amount. | aliases: empty, used up  ⟵ candidate
- daytime | value | time-of-day-value | The period of natural daylight between sunrise and sunset in the diurnal cycle. | not: unit_day (a 24-hour elapsed duration unit) or clock time timestamps | aliases: daytime, day, day time, daylight hours  ⟵ candidate
- nighttime | value | time-of-day-value | The period of darkness between sunset and sunrise in the diurnal cycle. | not: night_stand (a piece of furniture) or clock time timestamps | aliases: nighttime, night, night time, darkness  ⟵ candidate
- tone_concise | value | tone-value | Brief, to-the-point register. | aliases: briefly, concisely  ⟵ candidate
- tone_neutral | value | tone-value | Plain, unmarked register.  ⟵ candidate

### attributes

- quantity | attribute | attribute-name | Explicit count as NUMBER.  ⟵ candidate
