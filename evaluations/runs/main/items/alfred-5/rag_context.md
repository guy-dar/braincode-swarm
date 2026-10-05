# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 32 needs (decomposition: llm), 138 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | speech_act | t1:s1 | User requests instructions or actions to place eggs in the microwave | `microwave`*, `state_microwaved`, `microwave_stand`, `request`*, `propose`, `turn_on`, `ask`, `island`, `clock`, `respond`, `coffee_maker`, `dishwasher` |
| n2 | action | t1:s1 | Put or place items inside an appliance | `microwave`, `place`*, `turn_on`, `dishwasher`, `fridge`, `close`, `add_to_cart`, `in`*, `coffee_maker`, `stove`, `pan`, `open` |
| n3 | object | t1:s1 | Egg → `food_label::<key>` | `food_label`*, `mattress`, `bread`, `island`, `pan`, `cardamom`, `coffee_maker`, `spoon`, `apple`, `bowl`, `resource_heater`, `resource_chiller` |
| n4 | constraint | t1:s1 | Quantity of two | `rate`, `quantity`*, `unit_percent`, `unit_second`, `unit_liter`, `size_large`, `cap_tb`, `size_small`, `size_medium`, `unit_sentence`, `unit_hour`, `unit_gram` |
| n5 | object | t1:s1 | Microwave → `object_label::<key>` | `microwave`*, `microwave_stand`, `state_microwaved`, `coffee_maker`, `stove`, `resource_heater`, `resource_chiller`, `dishwasher`, `clock`, `fridge`, `tone_neutral`, `spatula` |
| n6 | action | t2:s2 | Go right | `turn`, `drop`, `walk`, `right_of`, `look`, `walk_backward`, `stand_up`, `left_of`, `calculation`, `in_front_of`, `propose`, `ask` |
| n7 | temporal | t2:s2 | Then / sequential step | `prep_time`, `format_numbered_list`, `sequence`, `maximum_between_stops`, `wait`, `in_front_of`, `calculation`, `unit_second`, `duration`, `then`, `unit_day`, `daytime` |
| n8 | action | t2:s2 | Turn left to face the sink | `turn`*, `sink`*, `dishwasher`, `face`*, `left_of`, `resource_sink`, `counter`, `water`, `turn_on`, `island`, `shower`, `desk` |
| n9 | object | t2:s2 | Sink → `object_label::<key>` | `sink`*, `dishwasher`, `resource_sink`, `water`, `rinse`, `counter`, `shower`, `island`, `spoon`, `coffee_maker`, `spatula`, `bowl` |
| n10 | action | t2:s4 | Pick up the egg from the sink | `sink`*, `pick_up`*, `resource_sink`, `food_label`, `counter`, `island`, `rinse`, `dishwasher`, `select_option`, `look`, `stand_up`, `spoon` |
| n11 | object | t2:s4 | Egg → `food_label::<key>` | `food_label`*, `mattress`, `island`, `bread`, `pan`, `coffee_maker`, `spoon`, `apple`, `bowl`, `cardamom`, `resource_heater`, `ice_cream` |
| n12 | object | t2:s4 | Sink → `object_label::<key>` | `sink`*, `dishwasher`, `resource_sink`, `water`, `rinse`, `counter`, `shower`, `island`, `spoon`, `coffee_maker`, `spatula`, `bowl` |
| n13 | action | t2:s6 | Go to the right and face the microwave | `microwave`*, `microwave_stand`, `stove`, `face`*, `walk`*, `state_microwaved`, `open_page`*, `counter`, `turn_on`, `dishwasher`, `turn`, `fridge` |
| n14 | object | t2:s6 | Microwave → `object_label::<key>` | `microwave`*, `microwave_stand`, `stove`, `coffee_maker`, `resource_heater`, `state_microwaved`, `resource_chiller`, `dishwasher`, `fridge`, `clock`, `lamp`, `tone_neutral` |
| n15 | action | t2:s8 | Put the egg in the microwave | `microwave`*, `microwave_stand`, `stove`, `place`*, `state_microwaved`, `turn_on`, `dishwasher`, `counter`, `island`, `drop`, `clock`, `coffee_maker` |
| n16 | object | t2:s8 | Egg → `food_label::<key>` | `food_label`*, `mattress`, `island`, `bread`, `pan`, `coffee_maker`, `spoon`, `apple`, `bowl`, `cardamom`, `resource_heater`, `ice_cream` |
| n17 | object | t2:s8 | Microwave → `object_label::<key>` | `microwave`*, `microwave_stand`, `stove`, `coffee_maker`, `resource_heater`, `state_microwaved`, `resource_chiller`, `dishwasher`, `fridge`, `clock`, `lamp`, `tone_neutral` |
| n18 | action | t2:s8 | Shut the microwave door | `microwave`*, `door`*, `microwave_stand`, `close`, `stove`, `cabinet`, `state_microwaved`, `turn_on`, `dishwasher`, `counter`, `open`, `wait` |
| n19 | object | t2:s8 | Door → `object_label::<key>` | `door`*, `close`, `cabinet`, `open`, `floor`, `coffee_maker`, `wall`, `dresser`, `resource_heater`, `left_of`, `resource_chiller`, `in_front_of` |
| n20 | action | t2:s10 | Go right, go right again, and turn to face the salt shaker on the table | `turn`*, `table`*, `face`*, `rinse`, `counter`, `turn_on`, `drop`, `sink`, `tartaric_acid`, `bowl`, `spoon`, `on` |
| n21 | object | t2:s10 | Salt shaker → `object_label::<key>` | `rinse`, `dishwasher`, `sink`, `spatula`, `tartaric_acid`, `water`, `raisin`, `bowl`, `resource_chiller`, `coffee_maker`, `resource_heater`, `waterproof_stickers` |
| n22 | object | t2:s10 | Table → `object_label::<key>` | `table`*, `format_table`, `night_stand`, `counter`, `example_a_select_two_pillows_and_move_those_objects`, `shelf`, `desk`, `object_label`*, `coffee_maker`, `transform_preserve_first_column`, `format_numbered_list`, `resource_heater` |
| n23 | action | t2:s12 | Pick the egg up from the table | `table`*, `select_option`, `food_label`, `pick_up`, `counter`, `island`, `drop`, `look`, `stand_up`, `entity_assembly_tips`, `example_a_select_two_pillows_and_move_those_objects`, `calculation` |
| n24 | object | t2:s12 | Egg → `food_label::<key>` | `food_label`*, `mattress`, `island`, `bread`, `pan`, `coffee_maker`, `spoon`, `apple`, `bowl`, `cardamom`, `resource_heater`, `ice_cream` |
| n25 | object | t2:s12 | Table → `object_label::<key>` | `table`*, `format_table`, `night_stand`, `counter`, `example_a_select_two_pillows_and_move_those_objects`, `shelf`, `desk`, `object_label`*, `coffee_maker`, `transform_preserve_first_column`, `format_numbered_list`, `resource_heater` |
| n26 | action | t2:s14 | Go right, then left, and turn right to face the microwave | `microwave`*, `turn`*, `microwave_stand`, `turn_on`, `stove`, `face`*, `left_of`, `state_microwaved`, `counter`, `dishwasher`, `drop`, `clock` |
| n27 | object | t2:s14 | Microwave → `object_label::<key>` | `microwave`*, `microwave_stand`, `stove`, `coffee_maker`, `resource_heater`, `state_microwaved`, `resource_chiller`, `dishwasher`, `fridge`, `clock`, `lamp`, `tone_neutral` |
| n28 | action | t2:s16 | Put the egg in the microwave | `microwave`*, `microwave_stand`, `stove`, `place`*, `state_microwaved`, `turn_on`, `dishwasher`, `counter`, `island`, `drop`, `clock`, `coffee_maker` |
| n29 | object | t2:s16 | Egg → `food_label::<key>` | `food_label`*, `mattress`, `island`, `bread`, `pan`, `coffee_maker`, `spoon`, `apple`, `bowl`, `cardamom`, `resource_heater`, `ice_cream` |
| n30 | object | t2:s16 | Microwave → `object_label::<key>` | `microwave`*, `microwave_stand`, `stove`, `coffee_maker`, `resource_heater`, `state_microwaved`, `resource_chiller`, `dishwasher`, `fridge`, `clock`, `lamp`, `tone_neutral` |
| n31 | action | t2:s16 | Shut the door | `door`*, `close`, `open`, `cabinet`, `wait`, `drop`, `maximum_between_stops`, `floor`, `greeting`, `dresser`, `calculation`, `tone_polite` |
| n32 | object | t2:s16 | Door → `object_label::<key>` | `door`*, `close`, `cabinet`, `open`, `floor`, `coffee_maker`, `wall`, `dresser`, `resource_heater`, `left_of`, `resource_chiller`, `in_front_of` |

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
- walk.destination → object_label
- face.target → object_label
- rinse.destination → object_label
- pick_up.target → object_label, food_label
- pick_up.source → object_label
- pick_up.color → color_label
- pour.destination → object_label
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

**rule_recording_signatures** (v19/rule/recording-signatures; rule governing turn_on)

RECORD ACTION uses the operation signature with REF[STRING] → TERM and LIST[REF[STRING]] → LIST[TERM]; other types/categories stay unchanged. Return EVENT, never the runtime result. Record actual outputs as attributed CLAIMs. Do not infer missing resources.

**rule_speech_acts_general** (v19/rule/speech-acts-general; rule governing propose)

UTTER-only, void, with the spec's speech attributes and LIST[TERM] constraints. No result binding. Literal content cannot replace required semantic arguments for structured coverage.

**rule_structural_constructs** (v19/rule/structural-constructs; core)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; rule governing request)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_attributes_and_generate** (v19/rule/attributes-and-generate; rule governing quantity)

Attribute entries name arguments; legality/types come from each operation, not global membership. GENERATE uses the spec's core fields; retained artifact profiles return STRING. Numeric/list results need explicit profiles. Legacy itinerary fields expand to TERM constraints: duration/duration_unit → duration(amount,unit); stop_min_per_day/stop_requirement → minimum_per_period(class,count,period=unit_day), never an inferred temple class; max_walk_duration/unit → maximum_between_stops(activity="walk",amount,unit). No legacy shorthand is enabled. Old events/character_properties/transformations become explicitly scoped TERM constraints. Message purpose is TERM, not send_email.content: GENERATE exact STRING content, then send. Report opaque fallback separately.

**rule_category_capacity_unit_value** (v19/rule/category/capacity-unit-value; rule governing cap_tb)

Preserve original binary-unit definitions for audit, but mark Needs clarification: GB/TB aliases conflate decimal and binary units. No silent change to scale.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; rule governing unit_item)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing microwave)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_format_value** (v19/rule/category/format-value; rule governing format_numbered_list)

STRING format. format_email is layout, not the action send_email.

**rule_category_location_name** (v19/rule/category/location-name; rule governing microwave_stand)

STRING location descriptor. A `table` surface is not the generated artifact category art_table.

**rule_category_product_attribute_value** (v19/rule/category/product-attribute-value; rule governing size_large)

STRING color/size/product-market facets. gender_women describes a product category, not an assertion about a person's gender.

**rule_category_shape_value** (v19/rule/category/shape-value; rule governing shape_round)

STRING geometry. shape_round may select a circular object; it does not imply color or dimensions.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing in)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_state_value** (v19/rule/category/state-value; rule governing state_microwaved)

STRING condition used in selection. state_warm does not command heat; “hot” is not automatically synonymous with “warm.”

**rule_category_tone_value** (v19/rule/category/tone-value; rule governing tone_neutral)

STRING register. tone_urgent describes urgency, not a concrete deadline.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_baldurs_gate_3)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_category_transformation_value** (v19/rule/category/transformation-value; rule governing transform_preserve_first_column)

TERM-described transformation. Pass it through constraints; no ungoverned transformations attribute.

**rule_composites_general** (v19/rule/composites-general; rule governing transform_preserve_first_column)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_examples_general** (v19/rule/examples-general; rule governing example_a_select_two_pillows_and_move_those_objects)

Examples use this glossary's contracts. They have not been verified by an implemented BrainCode parser.

**rule_operations_general** (v19/rule/operations-general; rule governing turn_on)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_supplemental_general** (v19/rule/supplemental-general; rule governing coffee_maker)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; rule governing rate)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- add_to_cart | operation | operation-vocabulary | (target: LIST[REF[STRING]]) -> void | Add the explicitly selected items. Does not pay or place an order.  ⟵ candidate
- close | operation | operation-vocabulary | (target: REF[STRING] / TERM) -> void | Close an articulated receptacle or appliance door. target must be a closable entity. | aliases: close_receptacle, close_door  ⟵ candidate
- drop | operation | operation-vocabulary | (target: REF[STRING] / TERM) -> void | Drop or release the held target object from the agent's hand. | not: place (which requires a destination receptacle) | aliases: drop, let go, put down  ⟵ candidate
- face | operation | operation-vocabulary | (target: STRING / TERM / ATOM[object_label]) -> void | Orient agent body/camera directly toward a target entity. target must be a perceptible entity. | aliases: orient_towards  ⟵ candidate
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
- wait | operation | operation-vocabulary | (duration?: NUMBER) -> void | Pause execution for a duration or cycle. duration in seconds or ticks. | aliases: idle, pause  ⟵ candidate
- walk | operation | operation-vocabulary | (destination: STRING / TERM / ATOM[object_label], relation?: STRING) -> void | Locomote towards a target destination or landmark. destination must identify a valid entity or location. | aliases: move_to, go_to, navigate_to  ⟵ candidate
- walk_backward | operation | operation-vocabulary | (modifier?: STRING) -> void | Walk backward. Optional modifier can specify the degree or minor distance of movement. | not: walk (which moves forward toward a destination) | aliases: move backward, step back  ⟵ candidate

### speech acts

- ask | speech_act | operation-vocabulary | UTTER ask(target: TERM, or a sufficiently precise topic: STRING / TERM) | Request information/advice; not an assertion of an answer. | aliases: ask, how should  ⟵ candidate
- offer | speech_act | operation-vocabulary | UTTER offer(target: STRING / TERM) | Speech act offering assistance, service, or items to a conversation partner. speech act in dialogic traces. | aliases: proffer  ⟵ candidate
- propose | speech_act | operation-vocabulary | UTTER propose(target: TERM) | Suggest an action/idea; does not record it as performed.  ⟵ candidate
- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ dependency of maximum_between_stops
- calculation | constructor | TERM calculation(inputs: LIST[TERM], operation: STRING, result?: TERM) -> TERM | Constructs a descriptive representation of an arithmetic or algorithmic calculation step with inputs, operation identifier, and optional resulting value. | not: an executed runtime action or factual claim of outcome | aliases: math_operation, compute_step  ⟵ candidate
- duration | constructor | TERM duration(amount: NUMBER, unit: STRING) -> TERM | Requested elapsed/calendar extent | not: Word/item counts are not time  ⟵ candidate
- greeting | constructor | TERM greeting(recipient: STRING) -> TERM | Constructs a conversational salutation greeting descriptor. conversational discourse term. | aliases: salutation  ⟵ candidate
- maximum_between_stops | constructor | TERM maximum_between_stops(activity: STRING, amount: NUMBER, unit: STRING) -> TERM | Upper bound on the stated activity between successive stops | not: Not a limit on total daily duration  ⟵ candidate
- preserve | constructor | TERM preserve(component: STRING, index: NUMBER) -> TERM | Keep the indexed component unchanged, using one-based indexing | not: Not preserve all components  ⟵ dependency of transform_preserve_first_column
- rate | constructor | TERM rate(denominator: TERM, numerator: TERM) -> TERM | Constructs a structured proportional rate or frequency relating a numerator measured quantity to a denominator reference quantity. | not: an asserted factual attribution (use attribute_claim) or bound constraint (use requirement) | aliases: per_unit, ratio  ⟵ candidate
- sequence | constructor | TERM sequence(items: LIST[TERM]) -> TERM | Ordered described activities/content | not: Not unordered conjunction  ⟵ candidate

### composites

- transform_preserve_first_column | composite | transformation-value | TERM transform_preserve_first_column() -> TERM | Preserve the first column of a table. | = preserve(component="column", index=1)  ⟵ candidate

### claim relations

- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ core
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ core
- prep_time | claim_relation | CLAIM prep_time(value: TERM) | Asserts an estimated preparation or assembly time duration. time requirement assertion. | aliases: preparation_duration  ⟵ candidate
- request | claim_relation | CLAIM request(target: TERM / STRING) | Represents an active communicative request or constraint state in conversation tracking. target is the requested action or topic. | aliases: user_request  ⟵ candidate

### links

- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ core
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ core
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ core
- then | link | LINK then(previous: EVENT, next: EVENT) | Represents temporal sequence and succession between two events where next follows previous. previous and next must be event terms. | aliases: followed_by, after_which  ⟵ candidate

### values

- cap_tb | value | capacity-unit-value | One tebibyte-equivalent capacity unit. | aliases: TB, terabytes  ⟵ candidate
- unit_day | value | duration-unit-value | Day. | aliases: days  ⟵ candidate
- unit_hour | value | duration-unit-value | Hour. | aliases: hours  ⟵ candidate
- unit_item | value | duration-unit-value | Top-level generated list or report item. | aliases: items, entries  ⟵ candidate
- unit_minute | value | duration-unit-value | Minute. | aliases: minutes, min  ⟵ candidate
- unit_second | value | duration-unit-value | Second. | aliases: seconds, sec  ⟵ candidate
- unit_sentence | value | duration-unit-value | One grammatical sentence in text generation or constraint counting. | not: unit_paragraph (paragraph block) or unit_word (individual word) | aliases: sentence, sentences  ⟵ candidate
- apple | value | entity-name | An apple fruit item, typically an ingredient or interactive food object. | not: food_label::tomato or other fruits/vegetables | aliases: apple, apples, red apple, green apple, apple slice  ⟵ candidate
- bowl | value | entity-name | A container/dish used for holding food or small items. | aliases: bowl  ⟵ candidate
- bread | value | entity-name | A bread loaf or slice food object. | aliases: bread  ⟵ candidate
- cabinet | value | entity-name | An enclosed cupboard or cabinet storage furniture unit with doors or shelves. | not: counter (a countertop surface) or dresser (a chest of drawers) | aliases: cabinet, cupboard, storage cabinet, kitchen cupboard  ⟵ candidate
- cardamom | value | entity-name | Aromatic spice seeds or pods from Elettaria or Amomum used in cooking and baking. | not: cinnamon, ginger, or other distinct spice varieties | aliases: cardamom, ground cardamom, cardamom pods  ⟵ candidate
- clock | value | entity-name | A clock timepiece appliance. | not: duration units like unit_hour | aliases: clock, timer  ⟵ candidate
- coffee_maker | value | entity-name | A coffee-making appliance; not automatically a heating resource  ⟵ candidate
- desk | value | entity-name | A work desk furniture surface. | aliases: desk  ⟵ candidate
- dishwasher | value | entity-name | A dishwasher kitchen appliance. | not: sink (a washing basin) or washing_machine (a laundry appliance) | aliases: dishwasher, dish washer, dishwashing machine  ⟵ candidate
- door | value | entity-name | A door architectural barrier or entryway. | not: wall or close/open operations | aliases: door, doorway, room door  ⟵ candidate
- dresser | value | entity-name | A chest of drawers / dresser furniture. | aliases: dresser  ⟵ candidate
- entity_assembly_tips | value | entity-name | Event planning item or menu category: entity_assembly_tips. | aliases: entity_assembly_tips  ⟵ candidate
- fridge | value | entity-name | A refrigerator cooling appliance. | aliases: fridge  ⟵ candidate
- ice_cream | value | entity-name | Frozen dessert food item: ice cream. | not: entity_desserts or entity_sweet_food (generic menu categories) | aliases: ice cream, ice_cream  ⟵ candidate
- lamp | value | entity-name | A lamp light source appliance. | not: an abstract lighting concept or ambient color | aliases: light, desk_lamp  ⟵ candidate
- mattress | value | entity-name | A mattress cushion or sleeping surface object. | not: bed (a bed furniture surface or frame) or object_label::pillow | aliases: mattress, mattresses  ⟵ candidate
- microwave | value | entity-name | A microwave oven appliance. | aliases: microwave  ⟵ candidate
- pan | value | entity-name | A metal cooking vessel, frying pan, skillet, saucepan, or pot cookware item used for preparing, heating, or holding food. | not: bowl (deep concave vessel) or plate (shallow flat dining dish) | aliases: pan, frying pan, skillet, saucepan, pot  ⟵ candidate
- plate | value | entity-name | A shallow, flat dish or vessel used for holding, preparing, or serving food. | not: bowl (deep concave vessel) or table (furniture surface) | aliases: dish, plate  ⟵ candidate
- raisin | value | entity-name | Dried grape food item. | not: sultana (specifically dried white grape) or fresh wine_grape | aliases: raisin, raisins, dried grape  ⟵ candidate
- resource_chiller | value | entity-name | Canonical abstract chilling resource when no particular appliance is named.  ⟵ candidate
- resource_heater | value | entity-name | Canonical abstract heating resource when no particular appliance is named.  ⟵ candidate
- resource_sink | value | entity-name | Canonical abstract washing resource when no particular sink is named.  ⟵ candidate
- shelf | value | entity-name | A flat horizontal shelving structure or shelving furniture unit used for storage and holding objects. | not: cabinet (an enclosed cupboard with doors) or table (a freestanding table surface) | aliases: shelf, shelves, bookshelf, wall shelf, shelving  ⟵ candidate
- shower | value | entity-name | A bathroom shower fixture or stall used for bathing. | not: sink (a washing basin) or toilet (a toilet fixture) | aliases: shower, shower stall  ⟵ candidate
- sink | value | entity-name | Washing basin. | aliases: sink  ⟵ candidate
- spatula | value | entity-name | A kitchen utensil with a broad, flat, and flexible blade used for lifting, flipping, or spreading food. | not: knife (cutting utensil) or spoon (scooping utensil) | aliases: spatula, turner, flipper  ⟵ candidate
- spoon | value | entity-name | An eating or cooking utensil. | aliases: spoon  ⟵ candidate
- stove | value | entity-name | A kitchen stove / range appliance for cooking or heating. | not: microwave | aliases: stove, range, cooktop  ⟵ candidate
- tartaric_acid | value | entity-name | Winemaking acid additive used for acidity adjustment. | not: citric_acid or general organic chemicals | aliases: tartaric acid  ⟵ candidate
- water | value | entity-name | Water from a tap or faucet used for washing or rinsing. | not: sink or other liquids | aliases: water, tap water  ⟵ candidate
- waterproof_stickers | value | entity-name | Physical item used for concealment or covering: waterproof_stickers. | aliases: waterproof_stickers  ⟵ candidate
- format_numbered_list | value | format-value | Numbered list. | aliases: numbered steps  ⟵ candidate
- format_table | value | format-value | Tabular layout. | aliases: as a table  ⟵ candidate
- counter | value | location-name | A kitchen or room countertop surface. | aliases: counter  ⟵ candidate
- floor | value | location-name | The floor surface of an indoor room or architectural space. | not: wall (a vertical room boundary surface) or counter (a countertop surface) | aliases: floor, ground  ⟵ candidate
- island | value | location-name | A freestanding kitchen island counter or food preparation work surface. | not: counter (a perimeter countertop surface) or table (a dining or general furniture surface) | aliases: island, kitchen island, kitchen_island  ⟵ candidate
- microwave_stand | value | location-name | A dedicated stand or cart supporting a microwave. | aliases: microwave_stand  ⟵ candidate
- night_stand | value | location-name | A small bedside table or nightstand furniture surface. | not: a chest of drawers (use dresser) or a general table surface (use table) | aliases: nightstand, bedside table  ⟵ candidate
- table | value | location-name | A table surface.  ⟵ candidate
- wall | value | location-name | A room boundary wall surface. | aliases: wall  ⟵ candidate
- size_large | value | product-attribute-value | Large size. | aliases: large, L  ⟵ candidate
- size_medium | value | product-attribute-value | Medium size. | aliases: medium, M  ⟵ candidate
- size_small | value | product-attribute-value | Small size. | aliases: small, S  ⟵ candidate
- shape_round | value | shape-value | Circular/round. | aliases: round, circular  ⟵ candidate
- in | value | spatial-relation | Contained within. | aliases: inside  ⟵ candidate
- in_front_of | value | spatial-relation | Positioned in front of. | aliases: in front of  ⟵ candidate
- left_of | value | spatial-relation | To the left of. | aliases: left of  ⟵ candidate
- on | value | spatial-relation | Resting atop. | aliases: on top of  ⟵ candidate
- right_of | value | spatial-relation | To the right of. | aliases: right of  ⟵ candidate
- state_clean | value | state-value | Clean condition. | aliases: clean  ⟵ candidate
- state_microwaved | value | state-value | Has been microwaved. | aliases: microwaved  ⟵ candidate
- daytime | value | time-of-day-value | The period of natural daylight between sunrise and sunset in the diurnal cycle. | not: unit_day (a 24-hour elapsed duration unit) or clock time timestamps | aliases: daytime, day, day time, daylight hours  ⟵ candidate
- tone_neutral | value | tone-value | Plain, unmarked register.  ⟵ candidate
- tone_polite | value | tone-value | Courteous, respectful register. | aliases: politely, kindly  ⟵ candidate
- topic_baldurs_gate_3 | value | topic-value | Baldur's Gate 3.  ⟵ candidate
- unit_gram | value | unit-value | Standard metric measurement unit of mass equal to 1/1,000 of a kilogram (0.001 kg). | not: digital capacity units (like cap_gb) or temporal duration units | aliases: g, gram, grams  ⟵ candidate
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

