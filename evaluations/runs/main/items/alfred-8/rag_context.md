# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 42 needs (decomposition: llm), 181 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | speech_act | t1:s1 | user requests moving objects between locations | `request`*, `example_a_select_two_pillows_and_move_those_objects`, `offer`, `walk`, `search_travel`, `propose`, `hover`, `ask`, `correct`, `express_interest`, `decline`, `between`* |
| n2 | action | t1:s1 | move items | `example_a_select_two_pillows_and_move_those_objects`, `add_to_cart`, `walk_backward`, `walk`, `unit_item`*, `pour`, `drop`, `art_itinerary`, `hover`, `art_plan`, `pick_up`, `calculation` |
| n3 | object | t1:s1 | book → `object_label::<key>` | `textbook`*, `mattress`, `example_a_select_two_pillows_and_move_those_objects`, `topic_baldurs_gate_3`, `pen`, `pencil`, `chair`, `role_professor`, `art_short_text`, `topic_classical_piano`, `art_itinerary`, `art_story` |
| n4 | constraint | t1:s1 | quantity of two books | `textbook`*, `quantity`*, `unit_percent`, `unit_paragraph`, `unit_second`, `cap_gb`, `unit_liter`, `cap_tb`, `format_plain_text`, `topic_baldurs_gate_3`, `unit_sentence`, `size_large` |
| n5 | object | t1:s1 | desk → `object_label::<key>` | `desk`*, `lamp`, `night_stand`, `format_table`, `table`, `laptop`, `textbook`, `example_a_select_two_pillows_and_move_those_objects`, `shelf`, `mattress`, `counter`, `chair` |
| n6 | object | t1:s1 | bed → `object_label::<key>` | `bed`*, `mattress`, `size_queen`, `example_a_select_two_pillows_and_move_those_objects`, `night_stand`, `desk`, `object_label`*, `textbook`, `dresser`, `wall`, `chair`, `nighttime` |
| n7 | action | t2:s2 | turn around | `turn`*, `turn_on`, `walk_backward`, `look`, `corner`, `stand_up`, `shape_round`, `left_of`, `calculation`, `wait`, `propose`, `on` |
| n8 | action | t2:s2 | walk across the room | `walk`*, `walk_backward`, `wall`, `counter`, `floor`, `living_room`, `door`, `desk`, `example_a_select_two_pillows_and_move_those_objects`, `dresser`, `chair`, `propose` |
| n9 | object | t2:s2 | room → `object_label::<key>` | `wall`, `floor`, `living_room`, `counter`, `door`, `chair`, `desk`, `bed`, `night_stand`, `dresser`, `example_a_select_two_pillows_and_move_those_objects`, `unit_paragraph` |
| n10 | action | t2:s2 | turn right | `turn`*, `turn_on`, `right_of`, `walk_backward`, `stand_up`, `look`, `left_of`, `corner`, `calculation`, `propose`, `in_front_of`, `on` |
| n11 | constraint | t2:s2 | just before the green garbage can | `trash_can`, `state_clean`, `topic_pickup_lines`, `lettuce`, `topic_baldurs_gate_3`, `state_dirty`, `constraint_budget_limited`, `constraint_exclude_liberation_theme`, `resource_chiller`, `constraint_exclude_flowery_language`, `topic_food_safety`, `tone_urgent` |
| n12 | constraint | t2:s2 | green → `color_label::<key>` | `color_label`*, `constraint_exclude_liberation_theme`, `lettuce`, `left_of`, `right_of`, `locale_en_gb`, `constraint_exclude_flowery_language`, `unit_day`, `constraint_budget_limited`, `shape_square`, `apple`, `locale_fr` |
| n13 | object | t2:s2 | garbage can → `object_label::<key>` | `resource_chiller`, `rinse`, `resource_sink`, `trash_can`, `recycle_bin`, `sponge`, `cardboard_box`, `mattress`, `safe`, `state_dirty`, `laptop`, `bottle` |
| n14 | action | t2:s2 | walk straight until reaching the desk | `desk`*, `walk`*, `walk_backward`, `lamp`, `counter`, `laptop`, `wall`, `table`, `stand_up`, `floor`, `island`, `look` |
| n15 | object | t2:s2 | desk → `object_label::<key>` | `desk`*, `lamp`, `counter`, `laptop`, `night_stand`, `table`, `example_a_select_two_pillows_and_move_those_objects`, `format_table`, `chair`, `piano`, `shelf`, `coffee_maker` |
| n16 | action | t2:s4 | pick up the book | `textbook`*, `pick_up`*, `art_itinerary`, `drop`, `topic_pickup_lines`, `select_option`, `stand_up`, `role_professor`, `topic_baldurs_gate_3`, `search_travel`, `look`, `propose` |
| n17 | object | t2:s4 | book → `object_label::<key>` | `textbook`*, `role_professor`, `topic_baldurs_gate_3`, `example_a_select_two_pillows_and_move_those_objects`, `right_of`, `art_short_text`, `topic_classical_piano`, `art_itinerary`, `next_to`, `chair`, `coffee_maker`, `left_of` |
| n18 | constraint | t2:s4 | located to the right of the coffee mug | `mug`*, `coffee_maker`, `right_of`*, `counter`, `dresser`, `fridge`, `chair`, `corner`, `constraint_exclude_liberation_theme`, `spoon`, `bottle`, `left_of` |
| n19 | object | t2:s4 | coffee mug → `object_label::<key>` | `mug`*, `coffee_maker`, `bottle`, `martini_glass`, `chill`, `spoon`, `chair`, `pen`, `example_a_select_two_pillows_and_move_those_objects`, `vase`, `bowl`, `entity_drinks` |
| n20 | action | t2:s6 | turn right | `turn`*, `turn_on`, `right_of`, `walk_backward`, `stand_up`, `look`, `left_of`, `corner`, `calculation`, `propose`, `in_front_of`, `on` |
| n21 | action | t2:s6 | walk to the bed | `bed`*, `walk`*, `walk_backward`, `mattress`, `size_queen`, `night_stand`, `example_a_select_two_pillows_and_move_those_objects`, `desk`, `wall`, `dresser`, `door`, `calculation` |
| n22 | object | t2:s6 | bed → `object_label::<key>` | `bed`*, `mattress`, `size_queen`, `example_a_select_two_pillows_and_move_those_objects`, `night_stand`, `desk`, `wall`, `object_label`*, `dresser`, `coffee_maker`, `chair`, `nighttime` |
| n23 | action | t2:s8 | place the book on the bed | `bed`*, `textbook`*, `mattress`, `place`*, `size_queen`, `night_stand`, `footnote`, `add_to_cart`, `example_a_select_two_pillows_and_move_those_objects`, `drop`, `dresser`, `wall` |
| n24 | object | t2:s8 | book → `object_label::<key>` | `textbook`*, `role_professor`, `topic_baldurs_gate_3`, `example_a_select_two_pillows_and_move_those_objects`, `right_of`, `art_short_text`, `topic_classical_piano`, `art_itinerary`, `next_to`, `chair`, `coffee_maker`, `left_of` |
| n25 | object | t2:s8 | bed → `object_label::<key>` | `bed`*, `mattress`, `size_queen`, `example_a_select_two_pillows_and_move_those_objects`, `night_stand`, `desk`, `wall`, `object_label`*, `dresser`, `coffee_maker`, `chair`, `nighttime` |
| n26 | constraint | t2:s8 | in front of the computer | `in_front_of`*, `desk`, `laptop`, `counter`, `lamp`, `floor`, `piano`, `role_professor`, `fridge`, `constraint_exclude_liberation_theme`, `role_mother`, `topic_macbook_pro_2017` |
| n27 | object | t2:s8 | computer → `object_label::<key>` | `laptop`, `resource_chiller`, `desk`, `lamp`, `piano`, `cd`, `coffee_maker`, `example_a_select_two_pillows_and_move_those_objects`, `cap_gb`, `fridge`, `shelf`, `chair` |
| n28 | action | t2:s10 | turn around | `turn`*, `turn_on`, `walk_backward`, `look`, `corner`, `stand_up`, `shape_round`, `left_of`, `calculation`, `wait`, `propose`, `on` |
| n29 | action | t2:s10 | walk back to the desk | `desk`*, `walk`*, `walk_backward`, `lamp`, `counter`, `laptop`, `table`, `wall`, `chair`, `island`, `floor`, `calculation` |
| n30 | object | t2:s10 | desk → `object_label::<key>` | `desk`*, `lamp`, `counter`, `laptop`, `night_stand`, `table`, `example_a_select_two_pillows_and_move_those_objects`, `format_table`, `chair`, `piano`, `shelf`, `coffee_maker` |
| n31 | action | t2:s12 | pick up the book | `textbook`*, `pick_up`*, `art_itinerary`, `drop`, `topic_pickup_lines`, `select_option`, `stand_up`, `role_professor`, `topic_baldurs_gate_3`, `search_travel`, `look`, `propose` |
| n32 | object | t2:s12 | book → `object_label::<key>` | `textbook`*, `role_professor`, `topic_baldurs_gate_3`, `example_a_select_two_pillows_and_move_those_objects`, `right_of`, `art_short_text`, `topic_classical_piano`, `art_itinerary`, `next_to`, `chair`, `coffee_maker`, `left_of` |
| n33 | constraint | t2:s12 | located to the right of the lamp | `lamp`*, `right_of`*, `desk`, `night_stand`, `wall`, `counter`, `corner`, `illuminates`, `left_of`, `other_side_of`, `door`, `constraint_exclude_liberation_theme` |
| n34 | object | t2:s12 | lamp → `object_label::<key>` | `lamp`*, `coffee_maker`, `candle`, `resource_heater`, `night_stand`, `example_a_select_two_pillows_and_move_those_objects`, `mug`, `mattress`, `nighttime`, `textbook`, `chair`, `illuminates` |
| n35 | action | t2:s14 | turn right | `turn`*, `turn_on`, `right_of`, `walk_backward`, `stand_up`, `look`, `left_of`, `corner`, `calculation`, `propose`, `in_front_of`, `on` |
| n36 | action | t2:s14 | walk to the bed | `bed`*, `walk`*, `walk_backward`, `mattress`, `size_queen`, `night_stand`, `example_a_select_two_pillows_and_move_those_objects`, `desk`, `wall`, `dresser`, `door`, `calculation` |
| n37 | object | t2:s14 | bed → `object_label::<key>` | `bed`*, `mattress`, `size_queen`, `example_a_select_two_pillows_and_move_those_objects`, `night_stand`, `desk`, `wall`, `object_label`*, `dresser`, `coffee_maker`, `chair`, `nighttime` |
| n38 | action | t2:s16 | place the book at the end of the bed | `bed`*, `textbook`*, `mattress`, `place`*, `size_queen`, `night_stand`, `footnote`, `add_to_cart`, `wall`, `dresser`, `drop`, `activity` |
| n39 | object | t2:s16 | book → `object_label::<key>` | `textbook`*, `role_professor`, `topic_baldurs_gate_3`, `example_a_select_two_pillows_and_move_those_objects`, `right_of`, `art_short_text`, `topic_classical_piano`, `art_itinerary`, `next_to`, `chair`, `coffee_maker`, `left_of` |
| n40 | object | t2:s16 | bed → `object_label::<key>` | `bed`*, `mattress`, `size_queen`, `example_a_select_two_pillows_and_move_those_objects`, `night_stand`, `desk`, `wall`, `object_label`*, `dresser`, `coffee_maker`, `chair`, `nighttime` |
| n41 | constraint | t2:s16 | across from the stuffed bear | `caddy`, `dresser`, `other_side_of`, `mattress`, `figurine`, `constraint_exclude_liberation_theme`, `gift`, `topic_spider_man_2`, `constraint_exclude_flowery_language`, `art_itinerary`, `constraint_budget_limited`, `under` |
| n42 | object | t2:s16 | stuffed bear → `object_label::<key>` | `mattress`, `bread`, `caddy`, `figurine`, `example_a_select_two_pillows_and_move_those_objects`, `sponge`, `topic_spider_man_2`, `gift`, `coffee_maker`, `laptop`, `mittens`, `chair` |

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

- walk.destination → object_label
- search_travel.location → country
- place.destination → object_label
- place.location → object_label
- pour.destination → object_label
- pick_up.target → object_label, food_label
- pick_up.source → object_label
- pick_up.color → color_label
- rinse.destination → object_label
- chill.destination → object_label
- activity.object → object_label, food_label, animal_label
- activity.location → country
- activity.instrument → object_label, platform_label
- requirement.value → platform_label
- subject.qualifier → platform_label
- subject.location → country
- failure.system → platform_label

## Retrieved records

### Shared rules that govern the records below (full text)

**rule_lexical_groups** (v19/rule/lexical-groups; rule governing platform_label)

Section 3.1 defines value groups: `group::key` values of type ATOM[group]. Open groups admit any key of their form (examples are not whitelists); standard groups admit the codes of their bundled standard (ISO 3166-1 alpha-2 for country, ISO 4217 for currency). Leaf values are never glossary entries. Consumer signatures alone decide where a group may appear. Retired bare symbols are invalid.

**rule_reading_guide** (v19/rule/reading-guide; core)

The spec governs syntax/types; this glossary defines vocabulary. Signature notation: ? optional, A / B explicit alternatives, void no result. Omitted optional arguments are unspecified. Value entries are category-refined STRING primitives; complex meanings require composition. Aliases are contextual hints, not unconditional equivalences. Report ambiguity. IDs use v19/<category>/<symbol>, v19/support/<symbol> or v19/composite/<symbol>. Statuses apply to this candidate: Retained preserves meaning; Adapted uses the stated contract; Composite requires TERM (bare STRING deprecated); Structural is syntax/argument vocabulary; Needs clarification is unusable until resolved; Deprecated is historical; Accepted is usable within this candidate.

**rule_recording_signatures** (v19/rule/recording-signatures; rule governing walk)

RECORD ACTION uses the operation signature with REF[STRING] → TERM and LIST[REF[STRING]] → LIST[TERM]; other types/categories stay unchanged. Return EVENT, never the runtime result. Record actual outputs as attributed CLAIMs. Do not infer missing resources.

**rule_speech_acts_general** (v19/rule/speech-acts-general; rule governing offer)

UTTER-only, void, with the spec's speech attributes and LIST[TERM] constraints. No result binding. Literal content cannot replace required semantic arguments for structured coverage.

**rule_structural_constructs** (v19/rule/structural-constructs; core)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; rule governing request)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_attributes_and_generate** (v19/rule/attributes-and-generate; rule governing art_itinerary)

Attribute entries name arguments; legality/types come from each operation, not global membership. GENERATE uses the spec's core fields; retained artifact profiles return STRING. Numeric/list results need explicit profiles. Legacy itinerary fields expand to TERM constraints: duration/duration_unit → duration(amount,unit); stop_min_per_day/stop_requirement → minimum_per_period(class,count,period=unit_day), never an inferred temple class; max_walk_duration/unit → maximum_between_stops(activity="walk",amount,unit). No legacy shorthand is enabled. Old events/character_properties/transformations become explicitly scoped TERM constraints. Message purpose is TERM, not send_email.content: GENERATE exact STRING content, then send. Report opaque fallback separately.

**rule_category_artifact_value** (v19/rule/category/artifact-value; rule governing art_itinerary)

STRING artifact class for GENERATE.target. art_story says what kind of artifact to produce, not what occurs in its plot.

**rule_category_capacity_unit_value** (v19/rule/category/capacity-unit-value; rule governing cap_gb)

Preserve original binary-unit definitions for audit, but mark Needs clarification: GB/TB aliases conflate decimal and binary units. No silent change to scale.

**rule_category_constraint_value** (v19/rule/category/constraint-value; rule governing constraint_budget_limited)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_content_value** (v19/rule/category/content-value; rule governing content_kyoto_itinerary)

Existing compounds become the constructors in Section 5. Their outputs go in topic/target/constraints as appropriate, not content, whose spec type remains STRING.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; rule governing unit_item)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing textbook)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_format_value** (v19/rule/category/format-value; rule governing format_plain_text)

STRING format. format_email is layout, not the action send_email.

**rule_category_locale_value** (v19/rule/category/locale-value; rule governing locale_en_gb)

STRING locale. “English” alone does not always mean locale_en_us; preserve ambiguity.

**rule_category_location_name** (v19/rule/category/location-name; rule governing night_stand)

STRING location descriptor. A `table` surface is not the generated artifact category art_table.

**rule_category_product_attribute_value** (v19/rule/category/product-attribute-value; rule governing size_large)

STRING color/size/product-market facets. gender_women describes a product category, not an assertion about a person's gender.

**rule_category_recipient_value** (v19/rule/category/recipient-value; rule governing role_professor)

STRING roles or explicit named recipients. A role is not an exact person's identity. Keep an explicit name where substituting a role loses information.

**rule_category_search_value** (v19/rule/category/search-value; rule governing cat_limited_time_offers)

STRING refinements rank_ / dir_ / cat_ / avail_ / genre_ are separate. rank_rating may fill rank_field; genre_label::comedy may not. “Cheapest” usually requires both rank_price and dir_asc, not rank_price alone.

**rule_category_semantic_category_value** (v19/rule/category/semantic-category-value; rule governing class_temple)

STRING class label used by typed constraints. class_temple describes a class, not an acquired physical temple reference.

**rule_category_shape_value** (v19/rule/category/shape-value; rule governing shape_round)

STRING geometry. shape_round may select a circular object; it does not imply color or dimensions.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing between)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_state_value** (v19/rule/category/state-value; rule governing state_clean)

STRING condition used in selection. state_warm does not command heat; “hot” is not automatically synonymous with “warm.”

**rule_category_tone_value** (v19/rule/category/tone-value; rule governing tone_urgent)

STRING register. tone_urgent describes urgency, not a concrete deadline.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_baldurs_gate_3)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_composites_general** (v19/rule/composites-general; rule governing constraint_budget_limited)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_examples_general** (v19/rule/examples-general; rule governing example_a_select_two_pillows_and_move_those_objects)

Examples use this glossary's contracts. They have not been verified by an implemented BrainCode parser.

**rule_operations_general** (v19/rule/operations-general; rule governing walk)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_supplemental_general** (v19/rule/supplemental-general; rule governing art_itinerary)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; rule governing calculation)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- add_to_cart | operation | operation-vocabulary | (target: LIST[REF[STRING]]) -> void | Add the explicitly selected items. Does not pay or place an order.  ⟵ candidate
- chill | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Chill using the stated resource; same identity.  ⟵ candidate
- drop | operation | operation-vocabulary | (target: REF[STRING] / TERM) -> void | Drop or release the held target object from the agent's hand. | not: place (which requires a destination receptacle) | aliases: drop, let go, put down  ⟵ candidate
- hover | operation | operation-vocabulary | (target: REF[STRING]) -> void | Move pointer cursor over an interactive web element without clicking. target must resolve to a valid element reference. | aliases: mouse_over  ⟵ candidate
- look | operation | operation-vocabulary | (direction: STRING) -> void | Tilt or adjust agent visual camera gaze. direction is up, down, or straight. | aliases: tilt_camera  ⟵ candidate
- pick_up | operation | operation-vocabulary | (target: STRING / ATOM[object_label] / ATOM[food_label], quantity?: NUMBER, source?: STRING / ATOM[object_label], color?: STRING / ATOM[color_label], shape?: STRING, state?: STRING) -> REF[STRING] or LIST[REF[STRING]] | Select/acquire objects. Missing quantity or literal 1 returns REF; integer literal greater than 1 returns LIST[REF]. Other values are invalid for this profile. | aliases: grab, take, retrieve  ⟵ candidate
- place | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label], location?: STRING / ATOM[object_label], relation?: STRING) -> void | Place an already acquired object. Spatial relation must be explicit if the source distinguishes it. | aliases: put, insert  ⟵ candidate
- pour | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Transfer selected liquid to the destination, preserving tracked material identity.  ⟵ candidate
- rinse | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Rinse using the stated resource; return the same identity. It is not enough that the object is already clean. | aliases: wash  ⟵ candidate
- search_travel | operation | operation-vocabulary | (target: STRING, constraints?: LIST[TERM], location?: STRING / ATOM[country]) -> LIST[REF[STRING]] | Query travel options meeting supplied constraints. Does not book them.  ⟵ candidate
- select_option | operation | operation-vocabulary | (target: REF[STRING], value: STRING) -> void | Select an option from a dropdown or select menu element. target must be a select element. | aliases: choose_option, choose_dropdown, pick_option  ⟵ candidate
- stand_up | operation | operation-vocabulary | () -> void | Return agent posture to standard upright standing position. agent must be in a non-standing posture. | aliases: stand  ⟵ candidate
- turn | operation | operation-vocabulary | (direction: STRING) -> void | Rotate agent body/view orientation. direction is typically left, right, or angle. | aliases: rotate, turn_around  ⟵ candidate
- turn_on | operation | operation-vocabulary | (target: REF[STRING] / TERM) -> void | Activate or start an appliance or device. target must be an activatable device. | aliases: activate, activate_appliance, switch_on  ⟵ candidate
- wait | operation | operation-vocabulary | (duration?: NUMBER) -> void | Pause execution for a duration or cycle. duration in seconds or ticks. | aliases: idle, pause  ⟵ candidate
- walk | operation | operation-vocabulary | (destination: STRING / TERM / ATOM[object_label], relation?: STRING) -> void | Locomote towards a target destination or landmark. destination must identify a valid entity or location. | aliases: move_to, go_to, navigate_to  ⟵ candidate
- walk_backward | operation | operation-vocabulary | (modifier?: STRING) -> void | Walk backward. Optional modifier can specify the degree or minor distance of movement. | not: walk (which moves forward toward a destination) | aliases: move backward, step back  ⟵ candidate

### speech acts

- ask | speech_act | operation-vocabulary | UTTER ask(target: TERM, or a sufficiently precise topic: STRING / TERM) | Request information/advice; not an assertion of an answer. | aliases: ask, how should  ⟵ candidate
- correct | speech_act | operation-vocabulary | UTTER correct(target: CLAIM) | Offer corrected content. Actual supersession requires the Conversation revision rules.  ⟵ candidate
- decline | speech_act | operation-vocabulary | UTTER decline(target: TERM) | Decline the represented request/proposal; not negate every proposition within it.  ⟵ candidate
- express_interest | speech_act | operation-vocabulary | UTTER express_interest(target: STRING / TERM) | Speech act expressing conversational interest or engagement in a topic. speech act in dialogic traces. | aliases: show_interest  ⟵ candidate
- offer | speech_act | operation-vocabulary | UTTER offer(target: STRING / TERM) | Speech act offering assistance, service, or items to a conversation partner. speech act in dialogic traces. | aliases: proffer  ⟵ candidate
- propose | speech_act | operation-vocabulary | UTTER propose(target: TERM) | Suggest an action/idea; does not record it as performed.  ⟵ candidate
- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ candidate
- aesthetic | constructor | TERM aesthetic(period: STRING, style: STRING) -> TERM | A stylistic description with an explicit period | not: Not a character's age or production date  ⟵ candidate
- calculation | constructor | TERM calculation(inputs: LIST[TERM], operation: STRING, result?: TERM) -> TERM | Constructs a descriptive representation of an arithmetic or algorithmic calculation step with inputs, operation identifier, and optional resulting value. | not: an executed runtime action or factual claim of outcome | aliases: math_operation, compute_step  ⟵ candidate
- duration | constructor | TERM duration(amount: NUMBER, unit: STRING) -> TERM | Requested elapsed/calendar extent | not: Word/item counts are not time  ⟵ dependency of wait
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ dependency of constraint_exclude_liberation_theme
- footnote | constructor | TERM footnote(function: STRING, number: NUMBER) -> TERM | Constructs a footnote reference or citation marker descriptor. document formatting descriptor. | aliases: citation_note  ⟵ candidate
- illuminates | constructor | TERM illuminates(target: STRING / TERM, source: STRING / TERM) -> TERM | Constructs a description of directional illumination where a light source casts light onto a target body. | not: an ambient color state or reflection (use reflects_light) | aliases: illuminates, shines on, shining towards  ⟵ candidate
- maximum_between_stops | constructor | TERM maximum_between_stops(activity: STRING, amount: NUMBER, unit: STRING) -> TERM | Upper bound on the stated activity between successive stops | not: Not a limit on total daily duration  ⟵ dependency of example_b_preserve_the_class_and_amount_of_an_itinerary_constraint
- minimum_per_period | constructor | TERM minimum_per_period(class: STRING, count: NUMBER, period: STRING) -> TERM | At least count members of class in each period | not: Not a minimum total over the whole artifact  ⟵ dependency of example_b_preserve_the_class_and_amount_of_an_itinerary_constraint
- rate | constructor | TERM rate(denominator: TERM, numerator: TERM) -> TERM | Constructs a structured proportional rate or frequency relating a numerator measured quantity to a denominator reference quantity. | not: an asserted factual attribution (use attribute_claim) or bound constraint (use requirement) | aliases: per_unit, ratio  ⟵ candidate
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ dependency of constraint_budget_limited
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ dependency of content_kyoto_itinerary

### composites

- constraint_budget_limited | composite | constraint-value | TERM constraint_budget_limited() -> TERM | Limited budget. | = requirement(property="budget_limited", value=TRUE)  ⟵ candidate
- constraint_exclude_flowery_language | composite | constraint-value | TERM constraint_exclude_flowery_language() -> TERM | Avoid flowery language. | = exclude(item="flowery_language")  ⟵ candidate
- constraint_exclude_liberation_theme | composite | constraint-value | TERM constraint_exclude_liberation_theme() -> TERM | Avoid liberation theme. | = exclude(item="liberation_theme")  ⟵ candidate
- content_kyoto_itinerary | composite | content-value | TERM content_kyoto_itinerary() -> TERM | A Kyoto itinerary subject. | = subject(kind="itinerary", location="Kyoto")  ⟵ dependency of example_b_preserve_the_class_and_amount_of_an_itinerary_constraint

### claim relations

- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ core
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ core
- request | claim_relation | CLAIM request(target: TERM / STRING) | Represents an active communicative request or constraint state in conversation tracking. target is the requested action or topic. | aliases: user_request  ⟵ candidate

### links

- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ core
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ core
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ core

### values

- art_itinerary | value | artifact-value | An ordered travel plan; GENERATE returns STRING, not booked travel  ⟵ candidate
- art_plan | value | artifact-value | Actionable plan.  ⟵ candidate
- art_short_text | value | artifact-value | Short free text.  ⟵ candidate
- art_story | value | artifact-value | Narrative story.  ⟵ candidate
- cap_gb | value | capacity-unit-value | One gibibyte-equivalent RAM capacity unit. | aliases: GB, gigabytes  ⟵ candidate
- cap_tb | value | capacity-unit-value | One tebibyte-equivalent capacity unit. | aliases: TB, terabytes  ⟵ candidate
- unit_day | value | duration-unit-value | Day. | aliases: days  ⟵ candidate
- unit_hour | value | duration-unit-value | Hour. | aliases: hours  ⟵ candidate
- unit_item | value | duration-unit-value | Top-level generated list or report item. | aliases: items, entries  ⟵ candidate
- unit_minute | value | duration-unit-value | Minute. | aliases: minutes, min  ⟵ dependency of example_b_preserve_the_class_and_amount_of_an_itinerary_constraint
- unit_paragraph | value | duration-unit-value | Paragraph of text. | aliases: paragraphs, paragraph  ⟵ candidate
- unit_second | value | duration-unit-value | Second. | aliases: seconds, sec  ⟵ candidate
- unit_sentence | value | duration-unit-value | One grammatical sentence in text generation or constraint counting. | not: unit_paragraph (paragraph block) or unit_word (individual word) | aliases: sentence, sentences  ⟵ candidate
- alcohol | value | entity-name | Alcoholic spirit or liquid such as brandy, rum, or whisky. | not: fermented non-distilled wine or pure chemical formula notation | aliases: alcohol, spirits, liquor  ⟵ candidate
- apple | value | entity-name | An apple fruit item, typically an ingredient or interactive food object. | not: food_label::tomato or other fruits/vegetables | aliases: apple, apples, red apple, green apple, apple slice  ⟵ candidate
- bed | value | entity-name | A bed furniture surface or sleeping area. | aliases: bed  ⟵ candidate
- bottle | value | entity-name | A bottle container object, typically used for holding liquids. | not: mug (a drinking cup with a handle) or water (the liquid itself) | aliases: bottle, water bottle, plastic bottle  ⟵ candidate
- bowl | value | entity-name | A container/dish used for holding food or small items. | aliases: bowl  ⟵ candidate
- bread | value | entity-name | A bread loaf or slice food object. | aliases: bread  ⟵ candidate
- caddy | value | entity-name | A portable storage caddy, organizer box, or supply tote for carrying and organizing handheld tools and supplies. | not: cabinet (a stationary furniture cupboard) or safe (a secure metal lockbox) | aliases: caddy, supply caddy, wrapping caddy, tool caddy, organizer caddy, supply tote  ⟵ candidate
- candle | value | entity-name | A candle light source made of wax with a wick. | not: lamp (an electric light appliance or fixture) | aliases: candle, wax candle  ⟵ candidate
- cardboard_box | value | entity-name | A cardboard box, carton, or general storage box container. | not: tissue_box (specifically a box of paper tissues) or safe (a lockable metal container) | aliases: cardboard box, box, carton, storage box  ⟵ candidate
- cd | value | entity-name | A compact disc physical object. | not: a digital media file or streaming track | aliases: CD, compact_disc  ⟵ candidate
- chair | value | entity-name | A chair furniture seat with a backrest. | not: object_label::armchair (specifically an object_label::armchair with side armrests) or object_label::sofa | aliases: chair, seat  ⟵ candidate
- coffee_maker | value | entity-name | A coffee-making appliance; not automatically a heating resource  ⟵ candidate
- desk | value | entity-name | A work desk furniture surface. | aliases: desk  ⟵ candidate
- door | value | entity-name | A door architectural barrier or entryway. | not: wall or close/open operations | aliases: door, doorway, room door  ⟵ candidate
- dresser | value | entity-name | A chest of drawers / dresser furniture. | aliases: dresser  ⟵ candidate
- entity_drinks | value | entity-name | Event planning item or menu category: entity_drinks. | aliases: entity_drinks  ⟵ candidate
- figurine | value | entity-name | A small carved, molded, or sculpted decorative statuette object. | not: character (a fictional persona) or captioned_figure (a document figure/photo) | aliases: figurine, statuette, statue, small statue, sculptural figure, miniature figure  ⟵ candidate
- fridge | value | entity-name | A refrigerator cooling appliance. | aliases: fridge  ⟵ candidate
- gift | value | entity-name | A physical gift or present item to be wrapped, given, or received. | not: egift_card (an electronic gift card or digital voucher product) | aliases: gift, present, wrapped gift, package  ⟵ candidate
- lamp | value | entity-name | A lamp light source appliance. | not: an abstract lighting concept or ambient color | aliases: light, desk_lamp  ⟵ candidate
- laptop | value | entity-name | A portable laptop computer physical object. | not: topic_macbook_pro_2017 (a generation topic label) | aliases: laptop, laptop computer, notebook  ⟵ candidate
- lettuce | value | entity-name | A head of lettuce or leafy green vegetable food item. | not: food_label::tomato or food_label::potato (other vegetable items) | aliases: lettuce, head of lettuce, salad greens  ⟵ candidate
- martini_glass | value | entity-name | A cocktail or Martini drinking glass object. | not: mug (a drinking cup with a handle) or bottle (liquid storage container) | aliases: martini glass, cocktail glass, glass  ⟵ candidate
- mattress | value | entity-name | A mattress cushion or sleeping surface object. | not: bed (a bed furniture surface or frame) or object_label::pillow | aliases: mattress, mattresses  ⟵ candidate
- mittens | value | entity-name | Item or prop in joke/creative context: mittens. | aliases: mittens  ⟵ candidate
- mug | value | entity-name | Drinking cup. | aliases: mug  ⟵ candidate
- pen | value | entity-name | A writing instrument. | aliases: pen  ⟵ candidate
- pencil | value | entity-name | A pencil writing instrument. | aliases: pencil  ⟵ candidate
- piano | value | entity-name | A piano musical instrument or large furniture object. | not: topic_classical_piano or topic_jazz_piano (music genre topics) | aliases: piano, grand piano, upright piano, keyboard  ⟵ candidate
- recycle_bin | value | entity-name | A dedicated receptacle container for recyclable waste materials. | not: trash_can (a general waste receptacle container) | aliases: recycle bin, recycling bin, recycle_bin  ⟵ candidate
- resource_chiller | value | entity-name | Canonical abstract chilling resource when no particular appliance is named.  ⟵ candidate
- resource_heater | value | entity-name | Canonical abstract heating resource when no particular appliance is named.  ⟵ candidate
- resource_sink | value | entity-name | Canonical abstract washing resource when no particular sink is named.  ⟵ candidate
- safe | value | entity-name | A secure, lockable metal storage container or receptacle for holding valuables. | not: cabinet (a general storage cupboard) or dresser (a chest of drawers) | aliases: safe, strongbox, lockbox, deposit box  ⟵ candidate
- shelf | value | entity-name | A flat horizontal shelving structure or shelving furniture unit used for storage and holding objects. | not: cabinet (an enclosed cupboard with doors) or table (a freestanding table surface) | aliases: shelf, shelves, bookshelf, wall shelf, shelving  ⟵ candidate
- sponge | value | entity-name | A porous, absorbent sponge cleaning tool or object. | not: tissue_box (a paper tissue box) or other wiping materials | aliases: sponge, cleaning sponge  ⟵ candidate
- spoon | value | entity-name | An eating or cooking utensil. | aliases: spoon  ⟵ candidate
- textbook | value | entity-name | A textbook or instructional book used as an educational resource. | not: style_academic (which is a stylistic mode) or art_short_text (which is a brief generated text artifact) | aliases: textbook, book, coursebook, textbooks  ⟵ candidate
- trash_can | value | entity-name | A waste receptacle container. | aliases: trash_can  ⟵ candidate
- vase | value | entity-name | A decorative or functional open container typically used for holding cut flowers or liquids. | not: bottle (a liquid storage container with a narrow neck) or bowl (a shallow dish) | aliases: vase, flower vase, flower_vase  ⟵ candidate
- format_plain_text | value | format-value | Unstructured prose text. | aliases: plain text  ⟵ candidate
- format_table | value | format-value | Tabular layout. | aliases: as a table  ⟵ candidate
- locale_en_gb | value | locale-value | UK English. | aliases: british english  ⟵ candidate
- locale_fr | value | locale-value | French. | aliases: french  ⟵ candidate
- corner | value | location-name | A corner area.  ⟵ candidate
- counter | value | location-name | A kitchen or room countertop surface. | aliases: counter  ⟵ candidate
- floor | value | location-name | The floor surface of an indoor room or architectural space. | not: wall (a vertical room boundary surface) or counter (a countertop surface) | aliases: floor, ground  ⟵ candidate
- island | value | location-name | A freestanding kitchen island counter or food preparation work surface. | not: counter (a perimeter countertop surface) or table (a dining or general furniture surface) | aliases: island, kitchen island, kitchen_island  ⟵ candidate
- living_room | value | location-name | A residential room or general indoor living area. | not: floor (a floor surface) or wall (a vertical boundary surface) | aliases: living room, living_room, sitting room, lounge  ⟵ candidate
- night_stand | value | location-name | A small bedside table or nightstand furniture surface. | not: a chest of drawers (use dresser) or a general table surface (use table) | aliases: nightstand, bedside table  ⟵ candidate
- table | value | location-name | A table surface.  ⟵ candidate
- wall | value | location-name | A room boundary wall surface. | aliases: wall  ⟵ candidate
- size_large | value | product-attribute-value | Large size. | aliases: large, L  ⟵ candidate
- size_queen | value | product-attribute-value | Queen-size dimension classification for beds, mattresses, and bedding. | not: size_large (generic large apparel/goods size) or size_king | aliases: queen, queen size, Queen  ⟵ candidate
- role_mother | value | recipient-value | The mother of the user. | not: role_sister or role_kids | aliases: my mom, mother, mom  ⟵ candidate
- role_professor | value | recipient-value | The user's professor/instructor. | aliases: my professor, teacher  ⟵ candidate
- cat_limited_time_offers | value | search-value | Category: time-limited deals.  ⟵ candidate
- class_temple | value | semantic-category-value | The abstract class of temples. | aliases: temple, temples  ⟵ dependency of example_b_preserve_the_class_and_amount_of_an_itinerary_constraint
- shape_round | value | shape-value | Circular/round. | aliases: round, circular  ⟵ candidate
- shape_square | value | shape-value | Square. | aliases: square  ⟵ candidate
- behind | value | spatial-relation | Positioned behind.  ⟵ candidate
- between | value | spatial-relation | Positioned between or in the middle of reference entities. | not: next_to or in_front_of | aliases: between, in the middle of, middle of, center of  ⟵ candidate
- in_front_of | value | spatial-relation | Positioned in front of. | aliases: in front of  ⟵ candidate
- left_of | value | spatial-relation | To the left of. | aliases: left of  ⟵ candidate
- next_to | value | spatial-relation | Adjacent to. | aliases: beside  ⟵ candidate
- on | value | spatial-relation | Resting atop. | aliases: on top of  ⟵ candidate
- other_side_of | value | spatial-relation | Positioned on the opposite or other side of a reference object. | not: next_to (which indicates general adjacency) | aliases: other side, other side of, opposite side of, opposite side  ⟵ candidate
- right_of | value | spatial-relation | To the right of. | aliases: right of  ⟵ candidate
- under | value | spatial-relation | Beneath. | aliases: below  ⟵ candidate
- state_clean | value | state-value | Clean condition. | aliases: clean  ⟵ candidate
- state_dirty | value | state-value | Dirty condition. | aliases: dirty  ⟵ candidate
- daytime | value | time-of-day-value | The period of natural daylight between sunrise and sunset in the diurnal cycle. | not: unit_day (a 24-hour elapsed duration unit) or clock time timestamps | aliases: daytime, day, day time, daylight hours  ⟵ candidate
- nighttime | value | time-of-day-value | The period of darkness between sunset and sunrise in the diurnal cycle. | not: night_stand (a piece of furniture) or clock time timestamps | aliases: nighttime, night, night time, darkness  ⟵ candidate
- tone_urgent | value | tone-value | Conveys urgency. | aliases: urgently, ASAP  ⟵ candidate
- topic_baldurs_gate_3 | value | topic-value | Baldur's Gate 3.  ⟵ candidate
- topic_classical_piano | value | topic-value | Classical piano.  ⟵ candidate
- topic_food_safety | value | topic-value | Food safety guidelines, sanitary regulations, or handling practices. | aliases: food_safety  ⟵ candidate
- topic_jazz_piano | value | topic-value | Jazz piano.  ⟵ candidate
- topic_macbook_pro_2017 | value | topic-value | MacBook Pro 2017.  ⟵ candidate
- topic_pickup_lines | value | topic-value | Pickup lines.  ⟵ candidate
- topic_spider_man_2 | value | topic-value | Marvel's Spider-Man 2.  ⟵ candidate
- unit_liter | value | unit-value | Standard metric measurement unit of liquid volume equal to 1 cubic decimeter (1,000 milliliters). | not: digital capacity units (like cap_gb) or temporal duration units | aliases: l, liter, liters, litres  ⟵ candidate
- unit_percent | value | unit-value | Standard unit of proportion or ratio representing parts per hundred (%). | not: rate (a constructor relating two quantities) or unitless counts | aliases: percent, percentage, %, pct  ⟵ candidate

### attributes

- quantity | attribute | attribute-name | Explicit count as NUMBER.  ⟵ candidate

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

