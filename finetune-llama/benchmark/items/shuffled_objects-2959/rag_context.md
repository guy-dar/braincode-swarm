# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 28 needs (decomposition: llm), 188 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | action | t1:s1 | play a game | `cat_game`, `obligation`, `propose`, `drop`, `event_camper_in_sludge_pit`, `activity`, `opposes`, `calculation`, `entity_appetizers`, `add_to_cart`, `target`, `click` |
| n2 | object | t1:s1 | Alice | `entity_flowers`, `event_sadie_adler_unmasking`, `art_story`, `role_sister`, `constitutional_ai`, `art_plan`, `topic_ai_earning_methods`, `art_short_text`, `resource_sink`, `art_technical_explanation`, `example_a_select_two_pillows_and_move_those_objects`, `class_temple` |
| n3 | object | t1:s1 | Bob | `resource_sink`, `bread`, `role_professor`, `bowtie`, `in_front_of`, `pencil`, `example_a_select_two_pillows_and_move_those_objects`, `mattress`, `coffee_maker`, `mug`, `on`, `target` |
| n4 | object | t1:s1 | Claire | `role_sister`, `role_daughter`, `role_mother`, `art_story`, `art_short_text`, `char_female`, `role_user`, `resource_sink`, `pencil`, `on`, `example_a_select_two_pillows_and_move_those_objects`, `unit_sentence` |
| n5 | object | t1:s1 | Dave | `resource_chiller`, `chill`, `yarn`, `bowtie`, `on`, `resource_sink`, `example_a_select_two_pillows_and_move_those_objects`, `mattress`, `candle`, `coffee_maker`, `topic_jazz_piano`, `cd` |
| n6 | object | t1:s1 | Eve | `mattress`, `entity_flowers`, `size_queen`, `gender_unisex`, `bed`, `art_story`, `class_temple`, `nighttime`, `moon`, `example_a_select_two_pillows_and_move_those_objects`, `resource_sink`, `night_stand` |
| n7 | object | t1:s1 | Fred | `art_story`, `mug`, `in_front_of`, `role_professor`, `resource_sink`, `unit_sentence`, `on`, `example_a_select_two_pillows_and_move_those_objects`, `coffee_maker`, `art_social_post`, `resource_chiller`, `resource_heater` |
| n8 | object | t1:s1 | Gertrude | `entity_flowers`, `mug`, `art_story`, `role_sister`, `vase`, `resource_sink`, `grape_pinot_noir`, `gender_unisex`, `example_a_select_two_pillows_and_move_those_objects`, `coffee_maker`, `grape_sauvignon_blanc`, `resource_chiller` |
| n9 | temporal | t1:s2 | at the start of the game | `cat_game`, `topic_baldurs_gate_3`, `entity_sides`, `wall`, `unit_day`, `on`, `daytime`, `in_front_of`, `counter`, `nighttime`, `mug`, `target` |
| n10 | object | t1:s2 | ball → `object_label::<key>` | `mattress`, `bread`, `shape_oval`, `topic_greatest_cricketer_of_all_time`, `object_label`*, `bowl`, `topic_politics`, `shape_square`, `table`, `metric_order_late`, `example_a_select_two_pillows_and_move_those_objects`, `resource_sink` |
| n11 | constraint | t1:s2 | pink color → `color_label::<key>` | `color_pink`*, `color_label`*, `entity_flowers`, `constraint_exclude_flowery_language`, `dulce_de_leche`, `dulce_de_nata`, `style_catchy`, `sym_pandas_testing_assert_almost_equal`, `mug`, `ice_cream`, `ginger`, `fruit_juice` |
| n12 | constraint | t1:s2 | white color → `color_label::<key>` | `color_label`*, `color_pink`, `entity_flowers`, `art_short_text`, `unit_word`, `constraint_exclude_flowery_language`, `gender_unisex`, `illuminates`, `sultana`, `wall`, `constraint_include_character_attribute_list`, `constraint_exclude_liberation_theme` |
| n13 | constraint | t1:s2 | brown color → `color_label::<key>` | `color_label`*, `color_pink`, `entity_flowers`, `constraint_exclude_flowery_language`, `art_character_profile`, `constraint_include_character_attribute_list`, `style_catchy`, `unit_character`, `constraint_exclude_liberation_theme`, `constraint_budget_limited`, `mug`, `illuminates` |
| n14 | constraint | t1:s2 | blue color → `color_label::<key>` | `color_label`*, `color_pink`, `entity_flowers`, `constraint_exclude_flowery_language`, `grape_sauvignon_blanc`, `sultana`, `dried_fruit`, `grape_merlot`, `lettuce`, `grape_pinot_noir`, `mug`, `constraint_include_character_attribute_list` |
| n15 | constraint | t1:s2 | yellow color → `color_label::<key>` | `color_label`*, `color_pink`, `entity_flowers`, `shape_oval`, `shape_triangular`, `shape_round`, `constraint_exclude_flowery_language`, `rule_category_shape_value`, `illuminates`, `constraint_include_character_attribute_list`, `ginger`, `constraint_budget_limited` |
| n16 | constraint | t1:s2 | black color → `color_label::<key>` | `color_label`*, `color_pink`, `entity_flowers`, `gender_unisex`, `constraint_exclude_flowery_language`, `wall`, `constraint_include_character_attribute_list`, `illuminates`, `constraint_exclude_liberation_theme`, `style_catchy`, `constraint_budget_limited`, `constraint_beginner` |
| n17 | constraint | t1:s2 | purple color → `color_label::<key>` | `color_pink`, `color_label`*, `constraint_exclude_liberation_theme`, `entity_flowers`, `mug`, `constraint_exclude_flowery_language`, `gender_unisex`, `ginger`, `constraint_include_character_attribute_list`, `fridge`, `constraint_budget_limited`, `lamp` |
| n18 | constraint | t1:s2 | initial assignment of balls to players | `constraint_beginner`, `entity_flowers`, `subject`, `sequence`, `obligation`, `topic_greatest_cricketer_of_all_time`, `mittens`, `constraint_exclude_flowery_language`, `format_bullet_list`, `topic_ai_earning_methods`, `constraint_include_character_attribute_list`, `property_question` |
| n19 | temporal | t1:s3 | as the game progresses | `cat_game`, `unit_day`, `art_plan`, `topic_baldurs_gate_3`, `event_camper_in_sludge_pit`, `daytime`, `nighttime`, `activity`, `drop`, `on`, `target`, `topic_spider_man_2` |
| n20 | action | t1:s3 | swap balls between players | `between`*, `drop`, `example_a_select_two_pillows_and_move_those_objects`, `pick_up`, `obligation`, `shape_round`, `event_camper_in_sludge_pit`, `shape_oval`, `substitute`, `topic_greatest_cricketer_of_all_time`, `calculation`, `shape_rectangular` |
| n21 | temporal | t1:s4, t1:s5, t1:s348 | sequential order of actions | `sequence`, `sort`, `metric_order_late`, `in_front_of`, `entity_order_vs_assemble_plan`, `unit_day`, `daytime`, `decision`, `then`, `nighttime`, `add_to_cart`, `wait` |
| n22 | action | t1:s5 | nothing happens (no-op) | `occurred`*, `wait`, `negation`, `obligation`, `search_transit`, `chill`, `rule_support_primitives_general`, `decline`, `calculation`, `click`, `ask`, `state_empty` |
| n23 | object | t1:s5 | named action identifier | `target`, `entity_appetizers`, `identity`, `obligation`, `resource_sink`, `role`, `resource_heater`, `example_a_select_two_pillows_and_move_those_objects`, `entity_checklist`, `click`, `coffee_maker`, `resource_chiller` |
| n24 | action | t1:s22 | discuss something | `propose`, `obligation`, `subject`, `offer_help`, `dialogue`, `topic_politics`, `calculation`, `ask`, `respond`, `add_to_cart`, `decision`, `greeting` |
| n25 | action | t1:s26 | repeat a previous action | `occurred`, `metric_repeat_buyer`, `then`, `propose`, `rule_recording_signatures`, `revises`, `sequence`, `drop`, `pick_up`, `obligation`, `wait`, `substitute` |
| n26 | temporal | t1:s349 | at the end of the game | `cat_game`, `activity`, `unit_day`, `nighttime`, `daytime`, `on`, `drop`, `topic_baldurs_gate_3`, `unit_character`, `wall`, `maximum_between_stops`, `unit_hour` |
| n27 | speech_act | t1:s349 | ask which ball Claire has | `ask`*, `entity_flowers`, `respond`, `topic_greatest_cricketer_of_all_time`, `size_queen`, `char_female`, `express_interest`, `moon`, `role_sister`, `mattress`, `inform`, `propose` |
| n28 | constraint | t1:s350 | multiple choice options | `constraint_single_choice`, `select_option`, `constraint_comprehensive`, `search_travel`, `entity_flowers`, `entity_order_vs_assemble_plan`, `constraint_exclude_flowery_language`, `constraint_include_character_attribute_list`, `constraint_budget_limited`, `example_a_select_two_pillows_and_move_those_objects`, `constraint_beginner`, `constraint_exclude_liberation_theme` |

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

- activity.object → object_label, food_label, animal_label
- activity.location → country
- activity.instrument → object_label, platform_label
- chill.destination → object_label
- subject.qualifier → platform_label
- subject.location → country
- pick_up.target → object_label, food_label
- pick_up.source → object_label
- pick_up.color → color_label
- search_transit.location → country
- search_travel.location → country
- place.destination → object_label
- place.location → object_label
- requirement.value → platform_label
- walk.destination → object_label
- failure.system → platform_label

## Retrieved records

### Shared rules that govern the records below (full text)

**rule_lexical_groups** (v19/rule/lexical-groups; rule governing platform_label)

Section 3.1 defines value groups: `group::key` values of type ATOM[group]. Open groups admit any key of their form (examples are not whitelists); standard groups admit the codes of their bundled standard (ISO 3166-1 alpha-2 for country, ISO 4217 for currency). Leaf values are never glossary entries. Consumer signatures alone decide where a group may appear. Retired bare symbols are invalid.

**rule_reading_guide** (v19/rule/reading-guide; core)

The spec governs syntax/types; this glossary defines vocabulary. Signature notation: ? optional, A / B explicit alternatives, void no result. Omitted optional arguments are unspecified. Value entries are category-refined STRING primitives; complex meanings require composition. Aliases are contextual hints, not unconditional equivalences. Report ambiguity. IDs use v19/<category>/<symbol>, v19/support/<symbol> or v19/composite/<symbol>. Statuses apply to this candidate: Retained preserves meaning; Adapted uses the stated contract; Composite requires TERM (bare STRING deprecated); Structural is syntax/argument vocabulary; Needs clarification is unusable until resolved; Deprecated is historical; Accepted is usable within this candidate.

**rule_recording_signatures** (v19/rule/recording-signatures; candidate)

RECORD ACTION uses the operation signature with REF[STRING] → TERM and LIST[REF[STRING]] → LIST[TERM]; other types/categories stay unchanged. Return EVENT, never the runtime result. Record actual outputs as attributed CLAIMs. Do not infer missing resources.

**rule_speech_acts_general** (v19/rule/speech-acts-general; rule governing propose)

UTTER-only, void, with the spec's speech attributes and LIST[TERM] constraints. No result binding. Literal content cannot replace required semantic arguments for structured coverage.

**rule_structural_constructs** (v19/rule/structural-constructs; core)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; rule governing opposes)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_attributes_and_generate** (v19/rule/attributes-and-generate; rule governing target)

Attribute entries name arguments; legality/types come from each operation, not global membership. GENERATE uses the spec's core fields; retained artifact profiles return STRING. Numeric/list results need explicit profiles. Legacy itinerary fields expand to TERM constraints: duration/duration_unit → duration(amount,unit); stop_min_per_day/stop_requirement → minimum_per_period(class,count,period=unit_day), never an inferred temple class; max_walk_duration/unit → maximum_between_stops(activity="walk",amount,unit). No legacy shorthand is enabled. Old events/character_properties/transformations become explicitly scoped TERM constraints. Message purpose is TERM, not send_email.content: GENERATE exact STRING content, then send. Report opaque fallback separately.

**rule_category_artifact_value** (v19/rule/category/artifact-value; rule governing art_story)

STRING artifact class for GENERATE.target. art_story says what kind of artifact to produce, not what occurs in its plot.

**rule_category_character_property_value** (v19/rule/category/character-property-value; rule governing char_female)

TERM-described trait/style. Use constraints and explicit inclusion/scope; do not use an ungoverned character_properties attribute.

**rule_category_code_value** (v19/rule/category/code-value; rule governing sym_pandas_testing_assert_almost_equal)

path_/sym_ remain STRING identities; migrated chg_/assert_ are TERM constructors. Do not recover an exact file path by guessing from underscores.

**rule_category_constraint_value** (v19/rule/category/constraint-value; rule governing constraint_exclude_flowery_language)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_descriptive_value** (v19/rule/category/descriptive-value; rule governing constitutional_ai)

STRING modifier/domain label; never a free-form proposition. dom_sgi needs its intended referent established before semantically dependent use.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; rule governing unit_sentence)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing entity_appetizers)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_event_value** (v19/rule/category/event-value; rule governing event_camper_in_sludge_pit)

TERM-described narrative event, not a recorded EVENT. Require inclusion explicitly when generating a story.

**rule_category_format_value** (v19/rule/category/format-value; rule governing format_bullet_list)

STRING format. format_email is layout, not the action send_email.

**rule_category_location_name** (v19/rule/category/location-name; rule governing night_stand)

STRING location descriptor. A `table` surface is not the generated artifact category art_table.

**rule_category_metric_value** (v19/rule/category/metric-value; rule governing metric_order_late)

STRING metric identity, not a Boolean value. Uptime and response time need numeric observations with units; order-late is Boolean-valued. Do not type every metric as BOOL.

**rule_category_product_attribute_value** (v19/rule/category/product-attribute-value; candidate)

STRING color/size/product-market facets. gender_women describes a product category, not an assertion about a person's gender.

**rule_category_recipient_value** (v19/rule/category/recipient-value; rule governing role_sister)

STRING roles or explicit named recipients. A role is not an exact person's identity. Keep an explicit name where substituting a role loses information.

**rule_category_search_value** (v19/rule/category/search-value; rule governing cat_game)

STRING refinements rank_ / dir_ / cat_ / avail_ / genre_ are separate. rank_rating may fill rank_field; genre_label::comedy may not. “Cheapest” usually requires both rank_price and dir_asc, not rank_price alone.

**rule_category_semantic_category_value** (v19/rule/category/semantic-category-value; rule governing class_temple)

STRING class label used by typed constraints. class_temple describes a class, not an acquired physical temple reference.

**rule_category_shape_value** (v19/rule/category/shape-value; candidate)

STRING geometry. shape_round may select a circular object; it does not imply color or dimensions.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing in_front_of)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_state_value** (v19/rule/category/state-value; rule governing state_empty)

STRING condition used in selection. state_warm does not command heat; “hot” is not automatically synonymous with “warm.”

**rule_category_style_value** (v19/rule/category/style-value; rule governing style_catchy)

STRING production style. style_narrative does not establish that described events occurred.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_ai_earning_methods)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_composites_general** (v19/rule/composites-general; rule governing event_camper_in_sludge_pit)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_examples_general** (v19/rule/examples-general; rule governing example_a_select_two_pillows_and_move_those_objects)

Examples use this glossary's contracts. They have not been verified by an implemented BrainCode parser.

**rule_operations_general** (v19/rule/operations-general; rule governing drop)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_search_web_attributes** (v19/rule/search-web-attributes; rule governing sort)

Optional filters: availability, category, color, cuisine, currency, gender, genre, location, platform, ram_unit, reservation_availability, shape, size (category-refined STRING); max_price, min_ram, min_rating (NUMBER); trending (BOOL). Explicit signature alternatives additionally admit atoms. Price requires currency; RAM requires a capacity unit; no default scale/source. rank is invalid: use sort, whose rank_field accepts rank_* and rank_direction accepts dir_*. Category/genre/availability accept only their own subfamilies.

**rule_supplemental_general** (v19/rule/supplemental-general; rule governing coffee_maker)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; candidate)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- add_to_cart | operation | operation-vocabulary | (target: LIST[REF[STRING]]) -> void | Add the explicitly selected items. Does not pay or place an order.  ⟵ candidate
- chill | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Chill using the stated resource; same identity.  ⟵ candidate
- click | operation | operation-vocabulary | (target: REF[STRING]) -> void | Activate the selected UI element. Requires its identity, not an invented selector.  ⟵ candidate
- drop | operation | operation-vocabulary | (target: REF[STRING] / TERM) -> void | Drop or release the held target object from the agent's hand. | not: place (which requires a destination receptacle) | aliases: drop, let go, put down  ⟵ candidate
- pick_up | operation | operation-vocabulary | (target: STRING / ATOM[object_label] / ATOM[food_label], quantity?: NUMBER, source?: STRING / ATOM[object_label], color?: STRING / ATOM[color_label], shape?: STRING, state?: STRING) -> REF[STRING] or LIST[REF[STRING]] | Select/acquire objects. Missing quantity or literal 1 returns REF; integer literal greater than 1 returns LIST[REF]. Other values are invalid for this profile. | aliases: grab, take, retrieve  ⟵ candidate
- place | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label], location?: STRING / ATOM[object_label], relation?: STRING) -> void | Place an already acquired object. Spatial relation must be explicit if the source distinguishes it. | aliases: put, insert  ⟵ dependency of example_a_select_two_pillows_and_move_those_objects
- search_transit | operation | operation-vocabulary | (target: STRING, constraints?: LIST[TERM], location?: STRING / ATOM[country]) -> LIST[REF[STRING]] | Query transit options. Does not buy tickets.  ⟵ candidate
- search_travel | operation | operation-vocabulary | (target: STRING, constraints?: LIST[TERM], location?: STRING / ATOM[country]) -> LIST[REF[STRING]] | Query travel options meeting supplied constraints. Does not book them.  ⟵ candidate
- select_option | operation | operation-vocabulary | (target: REF[STRING], value: STRING) -> void | Select an option from a dropdown or select menu element. target must be a select element. | aliases: choose_option, choose_dropdown, pick_option  ⟵ candidate
- sort | operation | operation-vocabulary | (target: LIST[REF[STRING]], rank_direction: STRING, rank_field: STRING) -> LIST[REF[STRING]] | Request ordering of selected results. Preserve member identity; this is not a claim that order was observed. | aliases: rank, order by  ⟵ candidate
- turn | operation | operation-vocabulary | (direction: STRING) -> void | Rotate agent body/view orientation. direction is typically left, right, or angle. | aliases: rotate, turn_around  ⟵ related to then
- wait | operation | operation-vocabulary | (duration?: NUMBER) -> void | Pause execution for a duration or cycle. duration in seconds or ticks. | aliases: idle, pause  ⟵ candidate
- walk | operation | operation-vocabulary | (destination: STRING / TERM / ATOM[object_label], relation?: STRING) -> void | Locomote towards a target destination or landmark. destination must identify a valid entity or location. | aliases: move_to, go_to, navigate_to  ⟵ related to then

### speech acts

- ask | speech_act | operation-vocabulary | UTTER ask(target: TERM, or a sufficiently precise topic: STRING / TERM) | Request information/advice; not an assertion of an answer. | aliases: ask, how should  ⟵ candidate
- decline | speech_act | operation-vocabulary | UTTER decline(target: TERM) | Decline the represented request/proposal; not negate every proposition within it.  ⟵ candidate
- express_interest | speech_act | operation-vocabulary | UTTER express_interest(target: STRING / TERM) | Speech act expressing conversational interest or engagement in a topic. speech act in dialogic traces. | aliases: show_interest  ⟵ candidate
- inform | speech_act | operation-vocabulary | UTTER inform(target: CLAIM) | Present the proposition; preserve its holder/status.  ⟵ candidate
- propose | speech_act | operation-vocabulary | UTTER propose(target: TERM) | Suggest an action/idea; does not record it as performed.  ⟵ candidate
- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ candidate
- calculation | constructor | TERM calculation(inputs: LIST[TERM], operation: STRING, result?: TERM) -> TERM | Constructs a descriptive representation of an arithmetic or algorithmic calculation step with inputs, operation identifier, and optional resulting value. | not: an executed runtime action or factual claim of outcome | aliases: math_operation, compute_step  ⟵ candidate
- character_trait | constructor | TERM character_trait(property: STRING, value: STRING / NUMBER) -> TERM | A character attribute | not: Not a claim about a real person  ⟵ dependency of char_female
- decision | constructor | TERM decision(activity: TERM) -> TERM | A decision whose content is the described activity | not: Not proof it was carried out  ⟵ candidate
- dialogue | constructor | TERM dialogue(style: STRING) -> TERM | Constructs a description of conversational dialogue adhering to a style. descriptive conversational term. | aliases: conversation_style  ⟵ candidate
- duration | constructor | TERM duration(amount: NUMBER, unit: STRING) -> TERM | Requested elapsed/calendar extent | not: Word/item counts are not time  ⟵ dependency of wait
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ dependency of constraint_exclude_flowery_language
- greeting | constructor | TERM greeting(recipient: STRING) -> TERM | Constructs a conversational salutation greeting descriptor. conversational discourse term. | aliases: salutation  ⟵ candidate
- illuminates | constructor | TERM illuminates(target: STRING / TERM, source: STRING / TERM) -> TERM | Constructs a description of directional illumination where a light source casts light onto a target body. | not: an ambient color state or reflection (use reflects_light) | aliases: illuminates, shines on, shining towards  ⟵ candidate
- include | constructor | TERM include(item: STRING / TERM) -> TERM | Require the identified content/item | not: Not permission to invent an instance in a recorded trace  ⟵ dependency of constraint_include_character_attribute_list
- maximum_between_stops | constructor | TERM maximum_between_stops(activity: STRING, amount: NUMBER, unit: STRING) -> TERM | Upper bound on the stated activity between successive stops | not: Not a limit on total daily duration  ⟵ candidate
- negation | constructor | TERM negation(target: TERM) -> TERM | Constructs a descriptive semantic negation of a target descriptive proposition or condition term. | not: Check's runtime Boolean operator NOT or a speech-act decline | aliases: not, does not, negation, absence of  ⟵ candidate
- obligation | constructor | TERM obligation(actor: STRING / TERM, activity: TERM) -> TERM | Constructs a deontic obligation description requiring an actor to perform an activity. actor and activity specified. | aliases: duty, mandatory_activity  ⟵ candidate
- offer_help | constructor | TERM offer_help() -> TERM | Constructs a conversational proffer of assistance or support. conversational discourse term. | aliases: help_offer  ⟵ candidate
- outshines | constructor | TERM outshines(brighter: STRING / TERM, dimmer: STRING / TERM) -> TERM | Constructs a description of relative visual brightness where a brighter light source overpowers the perceived brightness of a dimmer object. | not: an absolute numeric brightness measurement | aliases: outshines, overpowers brightness, drowns out light  ⟵ candidate
- property_question | constructor | TERM property_question(property: STRING, subject: STRING / TERM) -> TERM | An open request for a property of a subject | not: Does not supply the property's value  ⟵ candidate
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ dependency of topic_greatest_cricketer_of_all_time
- sequence | constructor | TERM sequence(items: LIST[TERM]) -> TERM | Ordered described activities/content | not: Not unordered conjunction  ⟵ candidate
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ candidate
- substitute | constructor | TERM substitute(original: STRING / TERM, replacement: STRING / TERM, purpose?: STRING / TERM) -> TERM | Constructs a descriptive representation of substituting an original entity or ingredient with a replacement alternative. | not: an executed change or runtime revision (use LINK revises) | aliases: substitute, substitution, alternative for, replace with  ⟵ candidate

### composites

- char_female | composite | character-property-value | TERM char_female() -> TERM | Female gender. | = character_trait(property="gender", value="female") | aliases: female  ⟵ candidate
- constraint_beginner | composite | constraint-value | TERM constraint_beginner() -> TERM | Targeted at beginners. | = requirement(property="audience_expertise", value="beginner")  ⟵ candidate
- constraint_budget_limited | composite | constraint-value | TERM constraint_budget_limited() -> TERM | Limited budget. | = requirement(property="budget_limited", value=TRUE)  ⟵ candidate
- constraint_comprehensive | composite | constraint-value | TERM constraint_comprehensive() -> TERM | Must be comprehensive. | = requirement(property="comprehensive", value=TRUE)  ⟵ candidate
- constraint_exclude_flowery_language | composite | constraint-value | TERM constraint_exclude_flowery_language() -> TERM | Avoid flowery language. | = exclude(item="flowery_language")  ⟵ candidate
- constraint_exclude_liberation_theme | composite | constraint-value | TERM constraint_exclude_liberation_theme() -> TERM | Avoid liberation theme. | = exclude(item="liberation_theme")  ⟵ candidate
- constraint_include_character_attribute_list | composite | constraint-value | TERM constraint_include_character_attribute_list() -> TERM | Include character attributes. | = include(item="character_attribute_list")  ⟵ candidate
- constraint_single_choice | composite | constraint-value | TERM constraint_single_choice() -> TERM | Must pick a single choice. | = requirement(property="choice_count", value=1)  ⟵ candidate
- event_camper_in_sludge_pit | composite | event-value | TERM event_camper_in_sludge_pit() -> TERM | Campers interacting in a sludge pit. | = activity(verb="interact", actor="campers", location="sludge_pit")  ⟵ candidate
- event_sadie_adler_unmasking | composite | event-value | TERM event_sadie_adler_unmasking() -> TERM | Sadie Adler taking off her hat and peeling skin. | = sequence(items=[activity(verb="remove", actor="Sadie Adler", object="hat"), activity(verb="peel", actor="Sadie Adler", object="skin")])  ⟵ candidate
- topic_ai_earning_methods | composite | topic-value | TERM topic_ai_earning_methods() -> TERM | AI earning methods. | = subject(kind="methods", qualifier=activity(verb="earn", instrument="AI", object="income"))  ⟵ candidate
- topic_greatest_cricketer_of_all_time | composite | topic-value | TERM topic_greatest_cricketer_of_all_time() -> TERM | Greatest cricketer of all time. | = subject(kind="cricketer", qualifier=requirement(property="rank_by_greatness", value=1), time="all_time")  ⟵ candidate

### claim relations

- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ core
- identity | claim_relation | CLAIM identity(subject: STRING / TERM, name: STRING) | Asserts the identified name or persona of an agent or entity. identity assertion. | aliases: agent_name  ⟵ candidate
- occurred | claim_relation | CLAIM occurred(activity: TERM) | Asserts that an event, action, or activity took place in the past. past occurrence claim. | aliases: happened  ⟵ candidate
- opposes | claim_relation | CLAIM opposes(actor: STRING / TERM, subject: STRING / TERM) | Asserts that an actor opposes or objects to a practice, entity, or policy. opposition stance. | aliases: objects_to, against  ⟵ candidate
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ core
- prohibited | claim_relation | CLAIM prohibited(subject: STRING / TERM, location: STRING / TERM, condition?: STRING / TERM) | Asserts that a subject is prohibited from a location or activity under specified conditions. deontic prohibition claim. | aliases: forbidden, banned_from  ⟵ related to obligation
- proposed_policy | claim_relation | CLAIM proposed_policy(policy: TERM, requirements: LIST[TERM]) | Asserts that a proposed policy framework comprises the specified requirement terms. policy must be a policy term. | aliases: policy_proposal  ⟵ related to obligation
- role | claim_relation | CLAIM role(subject: STRING / TERM, role_type: STRING) | Asserts the functional role or capacity of an agent or entity. role assertion. | aliases: agent_role  ⟵ candidate

### links

- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ core
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ candidate
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ core
- then | link | LINK then(previous: EVENT, next: EVENT) | Represents temporal sequence and succession between two events where next follows previous. previous and next must be event terms. | aliases: followed_by, after_which  ⟵ candidate

### values

- art_character_profile | value | artifact-value | Descriptive character profile.  ⟵ candidate
- art_plan | value | artifact-value | Actionable plan.  ⟵ candidate
- art_short_text | value | artifact-value | Short free text.  ⟵ candidate
- art_social_post | value | artifact-value | A short social media post or microblogging message. | not: art_short_text (general unstructured short prose) or art_story (narrative fiction) | aliases: tweet, tweets, social_media_post, microblog_post  ⟵ candidate
- art_story | value | artifact-value | Narrative story.  ⟵ candidate
- art_technical_explanation | value | artifact-value | Technical explanation of a concept.  ⟵ candidate
- path_pandas_src_testing_pyx | value | code-value | Source code file path or exported symbol in scientific Python: path_pandas_src_testing_pyx. | aliases: path_pandas_src_testing_pyx  ⟵ candidate
- sym_pandas_testing_assert_almost_equal | value | code-value | Source code file path or exported symbol in scientific Python: sym_pandas_testing_assert_almost_equal. | aliases: sym_pandas_testing_assert_almost_equal  ⟵ candidate
- constitutional_ai | value | descriptive-value | Concept of rule-based constitutional training and self-critique principles in AI alignment. | aliases: constitutional_ai  ⟵ candidate
- yakuza | value | descriptive-value | Descriptive concept of yakuza in cultural and social contexts. | aliases: yakuza  ⟵ candidate
- unit_character | value | duration-unit-value | One Unicode scalar value in the final rendered artifact; line endings are normalized to LF before counting. | aliases: characters, chars  ⟵ candidate
- unit_day | value | duration-unit-value | Day. | aliases: days  ⟵ candidate
- unit_hour | value | duration-unit-value | Hour. | aliases: hours  ⟵ candidate
- unit_sentence | value | duration-unit-value | One grammatical sentence in text generation or constraint counting. | not: unit_paragraph (paragraph block) or unit_word (individual word) | aliases: sentence, sentences  ⟵ candidate
- unit_word | value | duration-unit-value | Rendered whitespace-delimited word. | aliases: words  ⟵ candidate
- bed | value | entity-name | A bed furniture surface or sleeping area. | aliases: bed  ⟵ candidate
- bowl | value | entity-name | A container/dish used for holding food or small items. | aliases: bowl  ⟵ candidate
- bowtie | value | entity-name | Item or prop in joke/creative context: bowtie. | aliases: bowtie  ⟵ candidate
- bread | value | entity-name | A bread loaf or slice food object. | aliases: bread  ⟵ candidate
- candle | value | entity-name | A candle light source made of wax with a wick. | not: lamp (an electric light appliance or fixture) | aliases: candle, wax candle  ⟵ candidate
- cd | value | entity-name | A compact disc physical object. | not: a digital media file or streaming track | aliases: CD, compact_disc  ⟵ candidate
- coffee_maker | value | entity-name | A coffee-making appliance; not automatically a heating resource  ⟵ candidate
- dried_fruit | value | entity-name | Generic dried fruit food item. | not: fresh fruit or specific dried varieties like raisin or sultana | aliases: dried fruit, dried fruits  ⟵ candidate
- dulce_de_leche | value | entity-name | Sweet caramelized milk confection or dessert spread: dulce de leche. | not: cheese or dulce_de_nata | aliases: dulce de leche, dulce_de_leche  ⟵ candidate
- dulce_de_nata | value | entity-name | Clotted cream milk confection or dessert item: dulce de nata. | not: dulce_de_leche or cheese | aliases: dulce de nata, dulce_de_nata  ⟵ candidate
- entity_appetizers | value | entity-name | Event planning item or menu category: entity_appetizers. | aliases: entity_appetizers  ⟵ candidate
- entity_checklist | value | entity-name | Event planning item or menu category: entity_checklist. | aliases: entity_checklist  ⟵ candidate
- entity_flowers | value | entity-name | Flowers, blossoms, or floral design elements. | not: constraint_exclude_flowery_language (a prose style constraint) or agricultural food items | aliases: flowers, floral, flower, floral decorations  ⟵ candidate
- entity_order_vs_assemble_plan | value | entity-name | Event planning item or menu category: entity_order_vs_assemble_plan. | aliases: entity_order_vs_assemble_plan  ⟵ candidate
- entity_sides | value | entity-name | Event planning item or menu category: entity_sides. | aliases: entity_sides  ⟵ candidate
- fridge | value | entity-name | A refrigerator cooling appliance. | aliases: fridge  ⟵ candidate
- fruit_juice | value | entity-name | Liquid juice extracted from fruit. | not: fermented wine or freshly crushed grape_must | aliases: fruit juice, juice  ⟵ candidate
- ginger | value | entity-name | Pungent aromatic spice root from Zingiber officinale used in cooking and baking. | not: cinnamon, cardamom, or other distinct spice varieties | aliases: ginger, ground ginger, fresh ginger, ginger root  ⟵ candidate
- grape_merlot | value | entity-name | Merlot wine grape variety. | not: other red grape varieties such as grape_cabernet_sauvignon or grape_pinot_noir | aliases: Merlot, merlot grape  ⟵ candidate
- grape_pinot_noir | value | entity-name | Pinot Noir wine grape variety. | not: other red grape varieties such as grape_cabernet_sauvignon or grape_merlot | aliases: Pinot Noir, pinot noir grape  ⟵ candidate
- grape_sauvignon_blanc | value | entity-name | Sauvignon Blanc wine grape variety. | not: other white grape varieties such as grape_chardonnay | aliases: Sauvignon Blanc, sauvignon blanc grape  ⟵ candidate
- ice_cream | value | entity-name | Frozen dessert food item: ice cream. | not: entity_desserts or entity_sweet_food (generic menu categories) | aliases: ice cream, ice_cream  ⟵ candidate
- lamp | value | entity-name | A lamp light source appliance. | not: an abstract lighting concept or ambient color | aliases: light, desk_lamp  ⟵ candidate
- lettuce | value | entity-name | A head of lettuce or leafy green vegetable food item. | not: food_label::tomato or food_label::potato (other vegetable items) | aliases: lettuce, head of lettuce, salad greens  ⟵ candidate
- mattress | value | entity-name | A mattress cushion or sleeping surface object. | not: bed (a bed furniture surface or frame) or object_label::pillow | aliases: mattress, mattresses  ⟵ candidate
- mittens | value | entity-name | Item or prop in joke/creative context: mittens. | aliases: mittens  ⟵ candidate
- moon | value | entity-name | Earth's natural celestial satellite. | not: an artificial satellite or other planetary moon | aliases: moon, the moon, Luna  ⟵ candidate
- mug | value | entity-name | Drinking cup. | aliases: mug  ⟵ candidate
- pencil | value | entity-name | A pencil writing instrument. | aliases: pencil  ⟵ candidate
- resource_chiller | value | entity-name | Canonical abstract chilling resource when no particular appliance is named.  ⟵ candidate
- resource_heater | value | entity-name | Canonical abstract heating resource when no particular appliance is named.  ⟵ candidate
- resource_sink | value | entity-name | Canonical abstract washing resource when no particular sink is named.  ⟵ candidate
- sultana | value | entity-name | Dried white seedless grape food product. | not: raisin (dark dried grape) or wine_grape | aliases: sultana, sultanas, golden raisin  ⟵ candidate
- vase | value | entity-name | A decorative or functional open container typically used for holding cut flowers or liquids. | not: bottle (a liquid storage container with a narrow neck) or bowl (a shallow dish) | aliases: vase, flower vase, flower_vase  ⟵ candidate
- yarn | value | entity-name | Item or prop in joke/creative context: yarn. | aliases: yarn  ⟵ candidate
- format_bullet_list | value | format-value | Bulleted list. | aliases: bullet points  ⟵ candidate
- counter | value | location-name | A kitchen or room countertop surface. | aliases: counter  ⟵ candidate
- night_stand | value | location-name | A small bedside table or nightstand furniture surface. | not: a chest of drawers (use dresser) or a general table surface (use table) | aliases: nightstand, bedside table  ⟵ candidate
- table | value | location-name | A table surface.  ⟵ candidate
- wall | value | location-name | A room boundary wall surface. | aliases: wall  ⟵ candidate
- metric_order_late | value | metric-value | Whether an order is late. | aliases: order is late, delayed  ⟵ candidate
- metric_repeat_buyer | value | metric-value | Whether the customer is a repeat buyer. | aliases: repeat buyer, returning customer  ⟵ candidate
- color_pink | value | product-attribute-value | Pink visual color qualifier. | not: color_label::red, color_label::purple, or other distinct color shades | aliases: pink, color_pink, blush pink, rose pink, pastel pink  ⟵ candidate
- gender_unisex | value | product-attribute-value | Unisex. | aliases: unisex  ⟵ candidate
- size_queen | value | product-attribute-value | Queen-size dimension classification for beds, mattresses, and bedding. | not: size_large (generic large apparel/goods size) or size_king | aliases: queen, queen size, Queen  ⟵ candidate
- role_daughter | value | recipient-value | Daughter participant role in family or travel context. | not: role_sister, role_mother, or generic role_kids | aliases: daughter, my daughter  ⟵ candidate
- role_mother | value | recipient-value | The mother of the user. | not: role_sister or role_kids | aliases: my mom, mother, mom  ⟵ candidate
- role_professor | value | recipient-value | The user's professor/instructor. | aliases: my professor, teacher  ⟵ candidate
- role_sister | value | recipient-value | Sister participant role in family/event context. | aliases: sister  ⟵ candidate
- role_user | value | recipient-value | The requesting human. | aliases: me, I  ⟵ candidate
- cat_game | value | search-value | Category: video game.  ⟵ candidate
- class_temple | value | semantic-category-value | The abstract class of temples. | aliases: temple, temples  ⟵ candidate
- shape_oval | value | shape-value | Oval. | aliases: oval  ⟵ candidate
- shape_rectangular | value | shape-value | Rectangular. | aliases: rectangular, rectangle  ⟵ candidate
- shape_round | value | shape-value | Circular/round. | aliases: round, circular  ⟵ candidate
- shape_square | value | shape-value | Square. | aliases: square  ⟵ candidate
- shape_triangular | value | shape-value | Triangular. | aliases: triangular, triangle  ⟵ candidate
- between | value | spatial-relation | Positioned between or in the middle of reference entities. | not: next_to or in_front_of | aliases: between, in the middle of, middle of, center of  ⟵ candidate
- in_front_of | value | spatial-relation | Positioned in front of. | aliases: in front of  ⟵ candidate
- on | value | spatial-relation | Resting atop. | aliases: on top of  ⟵ candidate
- other_side_of | value | spatial-relation | Positioned on the opposite or other side of a reference object. | not: next_to (which indicates general adjacency) | aliases: other side, other side of, opposite side of, opposite side  ⟵ candidate
- state_empty | value | state-value | Contains no intended material or usable remaining amount. | aliases: empty, used up  ⟵ candidate
- style_catchy | value | style-value | Catchy, attention-grabbing style. | aliases: catchy  ⟵ candidate
- daytime | value | time-of-day-value | The period of natural daylight between sunrise and sunset in the diurnal cycle. | not: unit_day (a 24-hour elapsed duration unit) or clock time timestamps | aliases: daytime, day, day time, daylight hours  ⟵ candidate
- nighttime | value | time-of-day-value | The period of darkness between sunset and sunrise in the diurnal cycle. | not: night_stand (a piece of furniture) or clock time timestamps | aliases: nighttime, night, night time, darkness  ⟵ candidate
- topic_baldurs_gate_3 | value | topic-value | Baldur's Gate 3.  ⟵ candidate
- topic_jazz_piano | value | topic-value | Jazz piano.  ⟵ candidate
- topic_politics | value | topic-value | Politics.  ⟵ candidate
- topic_spider_man_2 | value | topic-value | Marvel's Spider-Man 2.  ⟵ candidate

### attributes

- target | attribute | attribute-name | The acted-on entity or generated artifact.  ⟵ candidate

### examples

- example_a_select_two_pillows_and_move_those_objects (candidate): Select two pillows and move those objects

```braincode
MODE REQUEST
ENTRYPOINT ObjectLabelPillow
TASK ObjectLabelPillow {
  ACTION pick_up(target=object_label::pillow, quantity=2, source=object_label::sofa) -> object_label_pillow_refs : LIST[REF[STRING]]
  FOR EACH item IN object_label_pillow_refs {
    ACTION place(target=item, destination=object_label::armchair, relation=on)
  }
}
```

