# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 39 needs (decomposition: llm), 176 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | speech_act | t1:s1 | command to place a pan with a knife onto a table | `knife`*, `pan`*, `table`*, `plate`, `counter`, `spoon`, `dishwasher`, `island`, `spatula`, `propose`, `stove`, `respond` |
| n2 | action | t1:s1 | place object onto surface | `place`*, `drop`, `floor`, `example_a_select_two_pillows_and_move_those_objects`, `counter`, `table`, `island`, `desk`, `rinse`, `rule_category_location_name`, `remove`, `face` |
| n3 | object | t1:s1 | pan → `object_label::<key>` | `pan`*, `chill`, `bread`, `coffee_maker`, `in_front_of`, `on`, `resource_sink`, `mug`, `resource_heater`, `topic_baldurs_gate_3`, `right_of`, `tone_urgent` |
| n4 | object | t1:s1 | knife → `object_label::<key>` | `knife`*, `spatula`, `scissors`, `bread`, `plate`, `spoon`, `pencil`, `counter`, `state_sliced`, `pen`, `sink`, `coffee_maker` |
| n5 | object | t1:s1 | table → `object_label::<key>` | `table`*, `format_table`, `night_stand`, `plate`, `counter`, `shelf`, `object_label`*, `example_a_select_two_pillows_and_move_those_objects`, `desk`, `coffee_maker`, `art_structured_report`, `transform_preserve_first_column` |
| n6 | constraint | t1:s1 | pan containing the knife | `pan`*, `knife`*, `plate`, `spoon`, `counter`, `spatula`, `dishwasher`, `scissors`, `pencil`, `bowl`, `bread`, `stove` |
| n7 | action | t2:s2 | walk forward | `walk`*, `walk_backward`, `turn`, `stand_up`, `left_of`, `in_front_of`, `face`, `performance_tracking`, `behind`, `calculation`, `propose`, `example_b_preserve_the_class_and_amount_of_an_itinerary_constraint` |
| n8 | temporal | t2:s2 | then | `then`*, `in_front_of`, `right_of`, `next_to`, `on`, `behind`, `tone_urgent`, `time_point`, `prep_time`, `nighttime`, `daytime`, `unit_day` |
| n9 | action | t2:s2 | turn left towards the table | `table`*, `turn`*, `left_of`, `format_table`, `night_stand`, `rule_category_location_name`, `counter`, `turn_on`, `walk_backward`, `desk`, `walk`, `face` |
| n10 | object | t2:s2 | table → `object_label::<key>` | `table`*, `format_table`, `night_stand`, `example_a_select_two_pillows_and_move_those_objects`, `counter`, `shelf`, `desk`, `object_label`*, `transform_preserve_first_column`, `plate`, `in_front_of`, `menu_works` |
| n11 | constraint | t2:s2 | black color → `color_label::<key>` | `color_label`*, `wall`, `left_of`, `corner`, `illuminates`, `constraint_exclude_flowery_language`, `color_pink`, `constraint_budget_limited`, `right_of`, `state_dirty`, `constraint_exclude_liberation_theme`, `style_catchy` |
| n12 | action | t2:s4 | pick up object | `pick_up`*, `select_option`, `remove`, `pour`, `drop`, `example_a_select_two_pillows_and_move_those_objects`, `add_to_cart`, `stand_up`, `spatula`, `place`, `look`, `entity_assembly_tips` |
| n13 | object | t2:s4 | knife → `object_label::<key>` | `knife`*, `spatula`, `scissors`, `bread`, `counter`, `plate`, `spoon`, `sink`, `state_sliced`, `dresser`, `pencil`, `coffee_maker` |
| n14 | object | t2:s4 | lettuce → `food_label::<key>` | `lettuce`*, `spatula`, `raisin`, `bowl`, `cuisine_indian`, `sultana`, `nutmeg`, `grape_must`, `cheese`, `cuisine_italian`, `spoon`, `dried_fruit` |
| n15 | constraint | t2:s4 | next to the lettuce | `lettuce`*, `next_to`*, `spatula`, `in_front_of`, `bowl`, `raisin`, `sultana`, `cuisine_indian`, `constraint_exclude_flowery_language`, `grape_must`, `right_of`, `cheese` |
| n16 | constraint | t2:s4 | closest one | `rank_distance`*, `in_front_of`, `next_to`, `left_of`, `other_side_of`, `behind`, `corner`, `between`, `right_of`, `on`, `constraint_budget_limited`, `door` |
| n17 | action | t2:s6 | turn around | `turn`*, `turn_on`, `walk_backward`, `look`, `corner`, `left_of`, `stand_up`, `behind`, `shape_round`, `in_front_of`, `calculation`, `other_side_of` |
| n18 | action | t2:s6 | go to the stove top | `stove`*, `walk`*, `open_page`*, `on`, `counter`, `island`, `dishwasher`, `turn_on`, `drop`, `pan`, `spatula`, `sink` |
| n19 | object | t2:s6 | stove top → `object_label::<key>` | `stove`*, `coffee_maker`, `resource_heater`, `counter`, `island`, `dishwasher`, `pan`, `spatula`, `plate`, `sink`, `on`, `wall` |
| n20 | constraint | t2:s6 | located on the left | `left_of`, `corner`, `table`, `in_front_of`, `behind`, `other_side_of`, `wall`, `floor`, `on`, `chair`, `right_of`, `between` |
| n21 | action | t2:s8 | put object into container | `remove`, `place`*, `drop`, `pour`, `rinse`, `bottle`, `trash_can`, `bowl`, `open`, `example_a_select_two_pillows_and_move_those_objects`, `vase`, `calculation` |
| n22 | object | t2:s8 | knife → `object_label::<key>` | `knife`*, `spatula`, `scissors`, `bread`, `counter`, `plate`, `spoon`, `sink`, `state_sliced`, `dresser`, `pencil`, `coffee_maker` |
| n23 | object | t2:s8 | pan → `object_label::<key>` | `pan`*, `chill`, `in_front_of`, `left_of`, `coffee_maker`, `right_of`, `on`, `example_a_select_two_pillows_and_move_those_objects`, `behind`, `next_to`, `resource_heater`, `topic_baldurs_gate_3` |
| n24 | object | t2:s8 | burner → `object_label::<key>` | `resource_heater`, `coffee_maker`, `resource_chiller`, `heat`, `stove`, `spatula`, `candle`, `lamp`, `state_warm`, `example_a_select_two_pillows_and_move_those_objects`, `chair`, `state_cold` |
| n25 | constraint | t2:s8 | on the back left burner | `left_of`, `stove`, `spatula`, `resource_heater`, `fridge`, `coffee_maker`, `lamp`, `behind`, `on`, `constraint_budget_limited`, `state_warm`, `constraint_exclude_flowery_language` |
| n26 | action | t2:s10 | pick up pan from the stove top | `stove`*, `pan`*, `pick_up`*, `counter`, `select_option`, `dishwasher`, `island`, `spatula`, `stand_up`, `plate`, `spoon`, `sink` |
| n27 | object | t2:s10 | pan → `object_label::<key>` | `pan`*, `chill`, `in_front_of`, `left_of`, `coffee_maker`, `right_of`, `on`, `example_a_select_two_pillows_and_move_those_objects`, `behind`, `next_to`, `resource_heater`, `topic_baldurs_gate_3` |
| n28 | object | t2:s10 | stove top → `object_label::<key>` | `stove`*, `coffee_maker`, `resource_heater`, `counter`, `island`, `dishwasher`, `pan`, `spatula`, `plate`, `sink`, `on`, `wall` |
| n29 | action | t2:s12 | turn left | `turn`*, `left_of`, `walk_backward`, `rule_category_spatial_relation`, `turn_on`, `corner`, `look`, `walk`, `stand_up`, `in_front_of`, `calculation`, `other_side_of` |
| n30 | action | t2:s12 | walk towards the safe | `walk`*, `safe`*, `walk_backward`, `face`, `topic_food_safety`, `pour`, `door`, `corner`, `wall`, `calculation`, `block_evaluation`, `self_protection` |
| n31 | object | t2:s12 | safe → `object_label::<key>` | `safe`*, `resource_chiller`, `topic_food_safety`, `state_clean`, `coffee_maker`, `waterproof_stickers`, `example_a_select_two_pillows_and_move_those_objects`, `resource_heater`, `chair`, `waterproof_bandages`, `reservation_available`, `state_cold` |
| n32 | action | t2:s12 | turn left to face the table | `table`*, `turn`*, `format_table`, `left_of`, `face`*, `night_stand`, `counter`, `desk`, `turn_on`, `corner`, `stand_up`, `look` |
| n33 | object | t2:s12 | black table → `object_label::<key>` | `table`*, `format_table`, `night_stand`, `counter`, `island`, `desk`, `wall`, `plate`, `maqluba`, `bowl`, `dresser`, `coffee_maker` |
| n34 | action | t2:s14 | put pan on the table | `pan`*, `table`*, `format_table`, `place`*, `counter`, `island`, `stove`, `plate`, `drop`, `spatula`, `night_stand`, `spoon` |
| n35 | object | t2:s14 | pan → `object_label::<key>` | `pan`*, `chill`, `in_front_of`, `left_of`, `coffee_maker`, `right_of`, `on`, `example_a_select_two_pillows_and_move_those_objects`, `behind`, `next_to`, `resource_heater`, `topic_baldurs_gate_3` |
| n36 | object | t2:s14 | table → `object_label::<key>` | `table`*, `format_table`, `night_stand`, `example_a_select_two_pillows_and_move_those_objects`, `counter`, `shelf`, `desk`, `object_label`*, `transform_preserve_first_column`, `plate`, `in_front_of`, `menu_works` |
| n37 | object | t2:s14 | lettuce → `food_label::<key>` | `lettuce`*, `spatula`, `raisin`, `bowl`, `cuisine_indian`, `sultana`, `nutmeg`, `grape_must`, `cheese`, `cuisine_italian`, `spoon`, `dried_fruit` |
| n38 | constraint | t2:s14 | on the left side of the table | `table`*, `left_of`, `other_side_of`, `counter`, `format_table`, `desk`, `night_stand`, `in_front_of`, `corner`, `right_of`, `wall`, `entity_sides` |
| n39 | constraint | t2:s14 | above the lettuce | `lettuce`*, `spatula`, `under`, `left_of`, `in_front_of`, `behind`, `bowl`, `raisin`, `constraint_exclude_flowery_language`, `on`, `cuisine_indian`, `sultana` |

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

- place.destination → object_label
- place.location → object_label
- rinse.destination → object_label
- face.target → object_label
- chill.destination → object_label
- walk.destination → object_label
- pick_up.target → object_label, food_label
- pick_up.source → object_label
- pick_up.color → color_label
- pour.destination → object_label
- heat.destination → object_label
- requirement.value → platform_label
- subject.qualifier → platform_label
- subject.location → country
- activity.object → object_label, food_label, animal_label
- activity.location → country
- activity.instrument → object_label, platform_label
- failure.system → platform_label

## Retrieved records

### Shared rules that govern the records below (full text)

**rule_lexical_groups** (v19/rule/lexical-groups; rule governing platform_label)

Section 3.1 defines value groups: `group::key` values of type ATOM[group]. Open groups admit any key of their form (examples are not whitelists); standard groups admit the codes of their bundled standard (ISO 3166-1 alpha-2 for country, ISO 4217 for currency). Leaf values are never glossary entries. Consumer signatures alone decide where a group may appear. Retired bare symbols are invalid.

**rule_reading_guide** (v19/rule/reading-guide; core)

The spec governs syntax/types; this glossary defines vocabulary. Signature notation: ? optional, A / B explicit alternatives, void no result. Omitted optional arguments are unspecified. Value entries are category-refined STRING primitives; complex meanings require composition. Aliases are contextual hints, not unconditional equivalences. Report ambiguity. IDs use v19/<category>/<symbol>, v19/support/<symbol> or v19/composite/<symbol>. Statuses apply to this candidate: Retained preserves meaning; Adapted uses the stated contract; Composite requires TERM (bare STRING deprecated); Structural is syntax/argument vocabulary; Needs clarification is unusable until resolved; Deprecated is historical; Accepted is usable within this candidate.

**rule_recording_signatures** (v19/rule/recording-signatures; rule governing place)

RECORD ACTION uses the operation signature with REF[STRING] → TERM and LIST[REF[STRING]] → LIST[TERM]; other types/categories stay unchanged. Return EVENT, never the runtime result. Record actual outputs as attributed CLAIMs. Do not infer missing resources.

**rule_speech_acts_general** (v19/rule/speech-acts-general; rule governing propose)

UTTER-only, void, with the spec's speech attributes and LIST[TERM] constraints. No result binding. Literal content cannot replace required semantic arguments for structured coverage.

**rule_structural_constructs** (v19/rule/structural-constructs; core)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; rule governing then)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_attributes_and_generate** (v19/rule/attributes-and-generate; rule governing art_structured_report)

Attribute entries name arguments; legality/types come from each operation, not global membership. GENERATE uses the spec's core fields; retained artifact profiles return STRING. Numeric/list results need explicit profiles. Legacy itinerary fields expand to TERM constraints: duration/duration_unit → duration(amount,unit); stop_min_per_day/stop_requirement → minimum_per_period(class,count,period=unit_day), never an inferred temple class; max_walk_duration/unit → maximum_between_stops(activity="walk",amount,unit). No legacy shorthand is enabled. Old events/character_properties/transformations become explicitly scoped TERM constraints. Message purpose is TERM, not send_email.content: GENERATE exact STRING content, then send. Report opaque fallback separately.

**rule_category_artifact_value** (v19/rule/category/artifact-value; rule governing art_structured_report)

STRING artifact class for GENERATE.target. art_story says what kind of artifact to produce, not what occurs in its plot.

**rule_category_constraint_value** (v19/rule/category/constraint-value; rule governing constraint_exclude_flowery_language)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_content_value** (v19/rule/category/content-value; rule governing content_kyoto_itinerary)

Existing compounds become the constructors in Section 5. Their outputs go in topic/target/constraints as appropriate, not content, whose spec type remains STRING.

**rule_category_cuisine_value** (v19/rule/category/cuisine-value; rule governing cuisine_indian)

STRING cuisine class; cuisine_indian is a cuisine filter, not the location India.

**rule_category_descriptive_value** (v19/rule/category/descriptive-value; rule governing potential_harms)

STRING modifier/domain label; never a free-form proposition. dom_sgi needs its intended referent established before semantically dependent use.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; rule governing unit_day)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing knife)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_format_value** (v19/rule/category/format-value; rule governing format_table)

STRING format. format_email is layout, not the action send_email.

**rule_category_location_name** (v19/rule/category/location-name; candidate)

STRING location descriptor. A `table` surface is not the generated artifact category art_table.

**rule_category_product_attribute_value** (v19/rule/category/product-attribute-value; rule governing color_pink)

STRING color/size/product-market facets. gender_women describes a product category, not an assertion about a person's gender.

**rule_category_reservation_status_value** (v19/rule/category/reservation-status-value; rule governing reservation_available)

STRING filter states; neither is a BOOL result binding. check_reservation_availability returns a BOOL with a distinct handle.

**rule_category_search_value** (v19/rule/category/search-value; rule governing rank_distance)

STRING refinements rank_ / dir_ / cat_ / avail_ / genre_ are separate. rank_rating may fill rank_field; genre_label::comedy may not. “Cheapest” usually requires both rank_price and dir_asc, not rank_price alone.

**rule_category_semantic_category_value** (v19/rule/category/semantic-category-value; rule governing class_temple)

STRING class label used by typed constraints. class_temple describes a class, not an acquired physical temple reference.

**rule_category_shape_value** (v19/rule/category/shape-value; rule governing shape_round)

STRING geometry. shape_round may select a circular object; it does not imply color or dimensions.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; candidate)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_state_value** (v19/rule/category/state-value; rule governing state_sliced)

STRING condition used in selection. state_warm does not command heat; “hot” is not automatically synonymous with “warm.”

**rule_category_style_value** (v19/rule/category/style-value; rule governing style_catchy)

STRING production style. style_narrative does not establish that described events occurred.

**rule_category_tone_value** (v19/rule/category/tone-value; rule governing tone_urgent)

STRING register. tone_urgent describes urgency, not a concrete deadline.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_baldurs_gate_3)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_category_transformation_value** (v19/rule/category/transformation-value; rule governing transform_preserve_first_column)

TERM-described transformation. Pass it through constraints; no ungoverned transformations attribute.

**rule_composites_general** (v19/rule/composites-general; rule governing transform_preserve_first_column)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_examples_general** (v19/rule/examples-general; rule governing example_a_select_two_pillows_and_move_those_objects)

Examples use this glossary's contracts. They have not been verified by an implemented BrainCode parser.

**rule_operations_general** (v19/rule/operations-general; rule governing place)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_supplemental_general** (v19/rule/supplemental-general; rule governing coffee_maker)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; rule governing calculation)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- add_to_cart | operation | operation-vocabulary | (target: LIST[REF[STRING]]) -> void | Add the explicitly selected items. Does not pay or place an order.  ⟵ candidate
- chill | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Chill using the stated resource; same identity.  ⟵ candidate
- drop | operation | operation-vocabulary | (target: REF[STRING] / TERM) -> void | Drop or release the held target object from the agent's hand. | not: place (which requires a destination receptacle) | aliases: drop, let go, put down  ⟵ candidate
- face | operation | operation-vocabulary | (target: STRING / TERM / ATOM[object_label]) -> void | Orient agent body/camera directly toward a target entity. target must be a perceptible entity. | aliases: orient_towards  ⟵ candidate
- heat | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Heat using the stated resource; same identity. Selecting a warm object does not imply heating it.  ⟵ candidate
- look | operation | operation-vocabulary | (direction: STRING) -> void | Tilt or adjust agent visual camera gaze. direction is up, down, or straight. | aliases: tilt_camera  ⟵ candidate
- open | operation | operation-vocabulary | (target: REF[STRING] / TERM) -> void | Open an articulated receptacle or appliance door. target must be an openable entity. | aliases: open_receptacle, open_door  ⟵ candidate
- open_page | operation | operation-vocabulary | (target: STRING) -> REF[STRING] | Navigate to the specified URL/page identity and return its page reference. Not a search for an unspecified page. | aliases: go to  ⟵ candidate
- pick_up | operation | operation-vocabulary | (target: STRING / ATOM[object_label] / ATOM[food_label], quantity?: NUMBER, source?: STRING / ATOM[object_label], color?: STRING / ATOM[color_label], shape?: STRING, state?: STRING) -> REF[STRING] or LIST[REF[STRING]] | Select/acquire objects. Missing quantity or literal 1 returns REF; integer literal greater than 1 returns LIST[REF]. Other values are invalid for this profile. | aliases: grab, take, retrieve  ⟵ candidate
- place | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label], location?: STRING / ATOM[object_label], relation?: STRING) -> void | Place an already acquired object. Spatial relation must be explicit if the source distinguishes it. | aliases: put, insert  ⟵ candidate
- pour | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Transfer selected liquid to the destination, preserving tracked material identity.  ⟵ candidate
- remove | operation | operation-vocabulary | (target: REF[STRING] / TERM, source?: STRING / TERM) -> void | Remove an object from an enclosure or container. target must be an object inside source. | aliases: take_out  ⟵ candidate
- rinse | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Rinse using the stated resource; return the same identity. It is not enough that the object is already clean. | aliases: wash  ⟵ candidate
- select_option | operation | operation-vocabulary | (target: REF[STRING], value: STRING) -> void | Select an option from a dropdown or select menu element. target must be a select element. | aliases: choose_option, choose_dropdown, pick_option  ⟵ candidate
- stand_up | operation | operation-vocabulary | () -> void | Return agent posture to standard upright standing position. agent must be in a non-standing posture. | aliases: stand  ⟵ candidate
- turn | operation | operation-vocabulary | (direction: STRING) -> void | Rotate agent body/view orientation. direction is typically left, right, or angle. | aliases: rotate, turn_around  ⟵ candidate
- turn_on | operation | operation-vocabulary | (target: REF[STRING] / TERM) -> void | Activate or start an appliance or device. target must be an activatable device. | aliases: activate, activate_appliance, switch_on  ⟵ candidate
- walk | operation | operation-vocabulary | (destination: STRING / TERM / ATOM[object_label], relation?: STRING) -> void | Locomote towards a target destination or landmark. destination must identify a valid entity or location. | aliases: move_to, go_to, navigate_to  ⟵ candidate
- walk_backward | operation | operation-vocabulary | (modifier?: STRING) -> void | Walk backward. Optional modifier can specify the degree or minor distance of movement. | not: walk (which moves forward toward a destination) | aliases: move backward, step back  ⟵ candidate

### speech acts

- propose | speech_act | operation-vocabulary | UTTER propose(target: TERM) | Suggest an action/idea; does not record it as performed.  ⟵ candidate
- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ dependency of maximum_between_stops
- block_evaluation | constructor | TERM block_evaluation(block: STRING / TERM, maturity?: STRING, potential?: STRING, quality?: STRING, rank?: NUMBER, traps?: STRING) -> TERM | Constructs a structured evaluation, categorization, or ranking descriptor for a geological exploration block. | not: an external execution action or generic list sorting operation (use sort) | aliases: block assessment, block ranking, block rating, block categorization  ⟵ candidate
- calculation | constructor | TERM calculation(inputs: LIST[TERM], operation: STRING, result?: TERM) -> TERM | Constructs a descriptive representation of an arithmetic or algorithmic calculation step with inputs, operation identifier, and optional resulting value. | not: an executed runtime action or factual claim of outcome | aliases: math_operation, compute_step  ⟵ candidate
- duration | constructor | TERM duration(amount: NUMBER, unit: STRING) -> TERM | Requested elapsed/calendar extent | not: Word/item counts are not time  ⟵ dependency of example_b_preserve_the_class_and_amount_of_an_itinerary_constraint
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ dependency of constraint_exclude_flowery_language
- illuminates | constructor | TERM illuminates(target: STRING / TERM, source: STRING / TERM) -> TERM | Constructs a description of directional illumination where a light source casts light onto a target body. | not: an ambient color state or reflection (use reflects_light) | aliases: illuminates, shines on, shining towards  ⟵ candidate
- maximum_between_stops | constructor | TERM maximum_between_stops(activity: STRING, amount: NUMBER, unit: STRING) -> TERM | Upper bound on the stated activity between successive stops | not: Not a limit on total daily duration  ⟵ dependency of example_b_preserve_the_class_and_amount_of_an_itinerary_constraint
- minimum_per_period | constructor | TERM minimum_per_period(class: STRING, count: NUMBER, period: STRING) -> TERM | At least count members of class in each period | not: Not a minimum total over the whole artifact  ⟵ dependency of example_b_preserve_the_class_and_amount_of_an_itinerary_constraint
- performance_tracking | constructor | TERM performance_tracking(adjustment?: STRING / TERM, target: STRING / TERM) -> TERM | Constructs a descriptive representation of monitoring performance metrics or campaign results with an optional strategy adjustment. | not: a runtime metric observation or software test run | aliases: track_results, monitor_performance, campaign_tracking  ⟵ candidate
- preserve | constructor | TERM preserve(component: STRING, index: NUMBER) -> TERM | Keep the indexed component unchanged, using one-based indexing | not: Not preserve all components  ⟵ dependency of transform_preserve_first_column
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ dependency of constraint_budget_limited
- self_protection | constructor | TERM self_protection(actor: STRING / TERM, domain: STRING, strategy?: STRING / TERM) -> TERM | Constructs a descriptive term representing an actor's self-protection practice, emotional boundary guarding, or coping strategy within a domain. | not: safe (a physical security container) or prohibited (a deontic rule) | aliases: guarding heart, emotional boundaries, protect oneself, coping strategy  ⟵ candidate
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ dependency of content_kyoto_itinerary
- time_point | constructor | TERM time_point(date?: STRING, time?: STRING, timezone?: STRING) -> TERM | Constructs a structured representation of a specific calendar date, time of day, or scheduled timestamp. | not: an elapsed time duration (use duration) | aliases: timestamp, datetime, scheduled_time  ⟵ candidate

### composites

- constraint_budget_limited | composite | constraint-value | TERM constraint_budget_limited() -> TERM | Limited budget. | = requirement(property="budget_limited", value=TRUE)  ⟵ candidate
- constraint_exclude_flowery_language | composite | constraint-value | TERM constraint_exclude_flowery_language() -> TERM | Avoid flowery language. | = exclude(item="flowery_language")  ⟵ candidate
- constraint_exclude_liberation_theme | composite | constraint-value | TERM constraint_exclude_liberation_theme() -> TERM | Avoid liberation theme. | = exclude(item="liberation_theme")  ⟵ candidate
- content_kyoto_itinerary | composite | content-value | TERM content_kyoto_itinerary() -> TERM | A Kyoto itinerary subject. | = subject(kind="itinerary", location="Kyoto")  ⟵ dependency of example_b_preserve_the_class_and_amount_of_an_itinerary_constraint
- transform_preserve_first_column | composite | transformation-value | TERM transform_preserve_first_column() -> TERM | Preserve the first column of a table. | = preserve(component="column", index=1)  ⟵ candidate

### claim relations

- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ core
- menu_works | claim_relation | CLAIM menu_works(property: STRING) | Asserts that a menu or recipe plan satisfies an operational criterion. menu evaluation. | aliases: menu_satisfies  ⟵ candidate
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ core
- prep_time | claim_relation | CLAIM prep_time(value: TERM) | Asserts an estimated preparation or assembly time duration. time requirement assertion. | aliases: preparation_duration  ⟵ candidate

### links

- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ core
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ core
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ core
- then | link | LINK then(previous: EVENT, next: EVENT) | Represents temporal sequence and succession between two events where next follows previous. previous and next must be event terms. | aliases: followed_by, after_which  ⟵ candidate

### values

- art_itinerary | value | artifact-value | An ordered travel plan; GENERATE returns STRING, not booked travel  ⟵ dependency of example_b_preserve_the_class_and_amount_of_an_itinerary_constraint
- art_plan | value | artifact-value | Actionable plan.  ⟵ candidate
- art_structured_report | value | artifact-value | Headed/structured report.  ⟵ candidate
- cuisine_indian | value | cuisine-value | Indian cuisine. | aliases: Indian food, Indian  ⟵ candidate
- cuisine_italian | value | cuisine-value | Italian cuisine. | aliases: Italian food, Italian  ⟵ candidate
- cuisine_mediterranean | value | cuisine-value | Mediterranean culinary cuisine style. | aliases: mediterranean  ⟵ candidate
- potential_harms | value | descriptive-value | Concept of potential safety hazards, adverse outcomes, or risks in AI interaction. | aliases: potential_harms  ⟵ candidate
- unit_day | value | duration-unit-value | Day. | aliases: days  ⟵ candidate
- unit_minute | value | duration-unit-value | Minute. | aliases: minutes, min  ⟵ dependency of example_b_preserve_the_class_and_amount_of_an_itinerary_constraint
- bottle | value | entity-name | A bottle container object, typically used for holding liquids. | not: mug (a drinking cup with a handle) or water (the liquid itself) | aliases: bottle, water bottle, plastic bottle  ⟵ candidate
- bowl | value | entity-name | A container/dish used for holding food or small items. | aliases: bowl  ⟵ candidate
- bread | value | entity-name | A bread loaf or slice food object. | aliases: bread  ⟵ candidate
- candle | value | entity-name | A candle light source made of wax with a wick. | not: lamp (an electric light appliance or fixture) | aliases: candle, wax candle  ⟵ candidate
- chair | value | entity-name | A chair furniture seat with a backrest. | not: object_label::armchair (specifically an object_label::armchair with side armrests) or object_label::sofa | aliases: chair, seat  ⟵ candidate
- cheese | value | entity-name | Dairy food item: cheese. | not: meat or non-dairy food items | aliases: cheese  ⟵ candidate
- clock | value | entity-name | A clock timepiece appliance. | not: duration units like unit_hour | aliases: clock, timer  ⟵ candidate
- coffee_maker | value | entity-name | A coffee-making appliance; not automatically a heating resource  ⟵ candidate
- desk | value | entity-name | A work desk furniture surface. | aliases: desk  ⟵ candidate
- dishwasher | value | entity-name | A dishwasher kitchen appliance. | not: sink (a washing basin) or washing_machine (a laundry appliance) | aliases: dishwasher, dish washer, dishwashing machine  ⟵ candidate
- door | value | entity-name | A door architectural barrier or entryway. | not: wall or close/open operations | aliases: door, doorway, room door  ⟵ candidate
- dresser | value | entity-name | A chest of drawers / dresser furniture. | aliases: dresser  ⟵ candidate
- dried_fruit | value | entity-name | Generic dried fruit food item. | not: fresh fruit or specific dried varieties like raisin or sultana | aliases: dried fruit, dried fruits  ⟵ candidate
- entity_assembly_tips | value | entity-name | Event planning item or menu category: entity_assembly_tips. | aliases: entity_assembly_tips  ⟵ candidate
- entity_sides | value | entity-name | Event planning item or menu category: entity_sides. | aliases: entity_sides  ⟵ candidate
- fridge | value | entity-name | A refrigerator cooling appliance. | aliases: fridge  ⟵ candidate
- grape_must | value | entity-name | Freshly crushed fruit juice mixture before fermentation. | not: clarified fruit_juice or finished wine | aliases: grape must, must  ⟵ candidate
- knife | value | entity-name | A cutting utensil used for slicing or food preparation. | aliases: knife  ⟵ candidate
- lamp | value | entity-name | A lamp light source appliance. | not: an abstract lighting concept or ambient color | aliases: light, desk_lamp  ⟵ candidate
- lettuce | value | entity-name | A head of lettuce or leafy green vegetable food item. | not: food_label::tomato or food_label::potato (other vegetable items) | aliases: lettuce, head of lettuce, salad greens  ⟵ candidate
- maqluba | value | entity-name | Traditional Arab layered rice dish: maqluba. | not: cuisine_mediterranean (cuisine style rather than specific dish) | aliases: maqluba, makloubeh  ⟵ candidate
- mug | value | entity-name | Drinking cup. | aliases: mug  ⟵ candidate
- nutmeg | value | entity-name | Ground or whole nutmeg culinary spice from Myristica fragrans seed. | not: cinnamon, cloves, or other distinct spice varieties | aliases: nutmeg, ground nutmeg  ⟵ candidate
- pan | value | entity-name | A metal cooking vessel, frying pan, skillet, saucepan, or pot cookware item used for preparing, heating, or holding food. | not: bowl (deep concave vessel) or plate (shallow flat dining dish) | aliases: pan, frying pan, skillet, saucepan, pot  ⟵ candidate
- pen | value | entity-name | A writing instrument. | aliases: pen  ⟵ candidate
- pencil | value | entity-name | A pencil writing instrument. | aliases: pencil  ⟵ candidate
- plate | value | entity-name | A shallow, flat dish or vessel used for holding, preparing, or serving food. | not: bowl (deep concave vessel) or table (furniture surface) | aliases: dish, plate  ⟵ candidate
- raisin | value | entity-name | Dried grape food item. | not: sultana (specifically dried white grape) or fresh wine_grape | aliases: raisin, raisins, dried grape  ⟵ candidate
- resource_chiller | value | entity-name | Canonical abstract chilling resource when no particular appliance is named.  ⟵ candidate
- resource_heater | value | entity-name | Canonical abstract heating resource when no particular appliance is named.  ⟵ candidate
- resource_sink | value | entity-name | Canonical abstract washing resource when no particular sink is named.  ⟵ candidate
- safe | value | entity-name | A secure, lockable metal storage container or receptacle for holding valuables. | not: cabinet (a general storage cupboard) or dresser (a chest of drawers) | aliases: safe, strongbox, lockbox, deposit box  ⟵ candidate
- scissors | value | entity-name | A handheld shearing cutting tool with two pivoted blades used for cutting paper, ribbon, and crafting materials. | not: knife (a kitchen or food preparation cutting utensil) | aliases: scissors, shears, pair of scissors  ⟵ candidate
- shelf | value | entity-name | A flat horizontal shelving structure or shelving furniture unit used for storage and holding objects. | not: cabinet (an enclosed cupboard with doors) or table (a freestanding table surface) | aliases: shelf, shelves, bookshelf, wall shelf, shelving  ⟵ candidate
- sink | value | entity-name | Washing basin. | aliases: sink  ⟵ candidate
- spatula | value | entity-name | A kitchen utensil with a broad, flat, and flexible blade used for lifting, flipping, or spreading food. | not: knife (cutting utensil) or spoon (scooping utensil) | aliases: spatula, turner, flipper  ⟵ candidate
- spoon | value | entity-name | An eating or cooking utensil. | aliases: spoon  ⟵ candidate
- stove | value | entity-name | A kitchen stove / range appliance for cooking or heating. | not: microwave | aliases: stove, range, cooktop  ⟵ candidate
- sultana | value | entity-name | Dried white seedless grape food product. | not: raisin (dark dried grape) or wine_grape | aliases: sultana, sultanas, golden raisin  ⟵ candidate
- tape | value | entity-name | Adhesive tape used for fastening and securing wrapping paper, boxes, or packaging materials. | not: waterproof_bandages (medical wound dressing) or waterproof_stickers (decorative stickers) | aliases: tape, adhesive tape, sticky tape, scotch tape  ⟵ candidate
- trash_can | value | entity-name | A waste receptacle container. | aliases: trash_can  ⟵ candidate
- vase | value | entity-name | A decorative or functional open container typically used for holding cut flowers or liquids. | not: bottle (a liquid storage container with a narrow neck) or bowl (a shallow dish) | aliases: vase, flower vase, flower_vase  ⟵ candidate
- waterproof_bandages | value | entity-name | Physical item used for concealment or covering: waterproof_bandages. | aliases: waterproof_bandages  ⟵ candidate
- waterproof_stickers | value | entity-name | Physical item used for concealment or covering: waterproof_stickers. | aliases: waterproof_stickers  ⟵ candidate
- format_table | value | format-value | Tabular layout. | aliases: as a table  ⟵ candidate
- corner | value | location-name | A corner area.  ⟵ candidate
- counter | value | location-name | A kitchen or room countertop surface. | aliases: counter  ⟵ candidate
- floor | value | location-name | The floor surface of an indoor room or architectural space. | not: wall (a vertical room boundary surface) or counter (a countertop surface) | aliases: floor, ground  ⟵ candidate
- island | value | location-name | A freestanding kitchen island counter or food preparation work surface. | not: counter (a perimeter countertop surface) or table (a dining or general furniture surface) | aliases: island, kitchen island, kitchen_island  ⟵ candidate
- night_stand | value | location-name | A small bedside table or nightstand furniture surface. | not: a chest of drawers (use dresser) or a general table surface (use table) | aliases: nightstand, bedside table  ⟵ candidate
- table | value | location-name | A table surface.  ⟵ candidate
- wall | value | location-name | A room boundary wall surface. | aliases: wall  ⟵ candidate
- color_pink | value | product-attribute-value | Pink visual color qualifier. | not: color_label::red, color_label::purple, or other distinct color shades | aliases: pink, color_pink, blush pink, rose pink, pastel pink  ⟵ candidate
- gender_unisex | value | product-attribute-value | Unisex. | aliases: unisex  ⟵ candidate
- reservation_available | value | reservation-status-value | A reservation can be made. | aliases: reservation availability, available reservations  ⟵ candidate
- rank_distance | value | search-value | Rank field: proximity. | aliases: nearest, closest  ⟵ candidate
- class_temple | value | semantic-category-value | The abstract class of temples. | aliases: temple, temples  ⟵ dependency of example_b_preserve_the_class_and_amount_of_an_itinerary_constraint
- shape_round | value | shape-value | Circular/round. | aliases: round, circular  ⟵ candidate
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
- state_cold | value | state-value | Cold or chilled condition. | aliases: cold, chilled  ⟵ candidate
- state_dirty | value | state-value | Dirty condition. | aliases: dirty  ⟵ candidate
- state_sliced | value | state-value | The condition of being sliced or cut into thin pieces. | not: the operation slice itself | aliases: sliced, slice, chopped, cut  ⟵ candidate
- state_upright | value | state-value | An upright or vertically standing physical state of an object. | not: stand_up (which is an agent posture operation) | aliases: standing up, upright, vertical  ⟵ candidate
- state_warm | value | state-value | Warm or heated condition. | aliases: warm, hot  ⟵ candidate
- style_catchy | value | style-value | Catchy, attention-grabbing style. | aliases: catchy  ⟵ candidate
- daytime | value | time-of-day-value | The period of natural daylight between sunrise and sunset in the diurnal cycle. | not: unit_day (a 24-hour elapsed duration unit) or clock time timestamps | aliases: daytime, day, day time, daylight hours  ⟵ candidate
- nighttime | value | time-of-day-value | The period of darkness between sunset and sunrise in the diurnal cycle. | not: night_stand (a piece of furniture) or clock time timestamps | aliases: nighttime, night, night time, darkness  ⟵ candidate
- tone_urgent | value | tone-value | Conveys urgency. | aliases: urgently, ASAP  ⟵ candidate
- topic_baldurs_gate_3 | value | topic-value | Baldur's Gate 3.  ⟵ candidate
- topic_food_safety | value | topic-value | Food safety guidelines, sanitary regulations, or handling practices. | aliases: food_safety  ⟵ candidate

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

