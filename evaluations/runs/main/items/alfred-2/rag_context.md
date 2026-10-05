# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 20 needs (decomposition: llm), 101 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | action | t1:s1 | cool a lettuce slice | `lettuce`*, `state_sliced`*, `slice`*, `bread`, `raisin`, `spatula`, `fridge`, `knife`, `bowl`, `sultana`, `dried_fruit`, `grape_must` |
| n2 | object | t1:s1 | lettuce slice → `food_label::<key>` | `lettuce`*, `state_sliced`*, `bread`, `slice`*, `raisin`, `knife`, `spatula`, `grape_must`, `sultana`, `dried_fruit`, `nutmeg`, `cheese` |
| n3 | action | t1:s1 | place object on the counter | `counter`*, `place`*, `island`, `add_to_cart`, `dishwasher`, `presentation_slide`, `heat`, `rinse`, `drop`, `desk`, `remove`, `table` |
| n4 | object | t1:s1 | counter → `object_label::<key>` | `counter`*, `island`, `coffee_maker`, `dishwasher`, `sink`, `spatula`, `knife`, `plate`, `stove`, `bread`, `desk`, `resource_heater` |
| n5 | action | t2:s2 | turn left and walk across the room to face the sink | `sink`*, `counter`, `walk_backward`, `turn`*, `walk`*, `face`*, `wall`, `floor`, `left_of`, `door`, `resource_sink`, `turn_on` |
| n6 | object | t2:s2 | sink → `object_label::<key>` | `sink`*, `dishwasher`, `resource_sink`, `water`, `shower`, `counter`, `rinse`, `spatula`, `spoon`, `bowl`, `plate`, `toilet` |
| n7 | action | t2:s4 | pick up the knife from the sink | `sink`*, `knife`*, `resource_sink`, `pick_up`*, `counter`, `dishwasher`, `select_option`, `island`, `spatula`, `stand_up`, `rinse`, `look` |
| n8 | object | t2:s4 | knife → `object_label::<key>` | `knife`*, `spatula`, `scissors`, `counter`, `bread`, `sink`, `dresser`, `plate`, `spoon`, `state_sliced`, `resource_sink`, `example_a_select_two_pillows_and_move_those_objects` |
| n9 | action | t2:s6 | turn around and step forward to face the lettuce on the counter | `lettuce`*, `counter`*, `turn`*, `face`*, `island`, `walk_backward`, `turn_on`, `in_front_of`, `dishwasher`, `spatula`, `sink`, `calculation` |
| n10 | object | t2:s6 | lettuce → `food_label::<key>` | `lettuce`*, `spatula`, `raisin`, `nutmeg`, `bowl`, `sultana`, `grape_must`, `cheese`, `cuisine_indian`, `cloves`, `resource_sink`, `spoon` |
| n11 | action | t2:s8 | cut the lettuce on the counter into slices | `lettuce`*, `slice`*, `state_sliced`*, `counter`*, `knife`, `scissors`, `island`, `dishwasher`, `sink`, `spatula`, `grape_must`, `calculation` |
| n12 | action | t2:s10 | turn around and step forward to face the counter | `counter`*, `turn`*, `face`*, `walk_backward`, `island`, `turn_on`, `look`, `stand_up`, `desk`, `corner`, `table`, `wall` |
| n13 | action | t2:s12 | place the knife on the counter | `counter`*, `knife`*, `island`, `place`*, `spatula`, `cabinet`, `scissors`, `dishwasher`, `sink`, `drop`, `table`, `floor` |
| n14 | action | t2:s14 | turn around and step forward to face the lettuce on the counter | `lettuce`*, `counter`*, `turn`*, `face`*, `island`, `walk_backward`, `turn_on`, `in_front_of`, `dishwasher`, `spatula`, `sink`, `calculation` |
| n15 | action | t2:s16 | pick up a slice of lettuce from the counter | `lettuce`*, `counter`*, `slice`*, `state_sliced`*, `pick_up`*, `bread`, `select_option`, `knife`, `spatula`, `stand_up`, `look`, `sink` |
| n16 | action | t2:s18 | turn around and step forward to face the fridge | `fridge`*, `turn`*, `walk_backward`, `turn_on`, `face`*, `counter`, `island`, `in_front_of`, `dishwasher`, `floor`, `wall`, `stove` |
| n17 | object | t2:s18 | fridge → `object_label::<key>` | `fridge`*, `coffee_maker`, `resource_chiller`, `resource_heater`, `dishwasher`, `cabinet`, `shelf`, `example_a_select_two_pillows_and_move_those_objects`, `bowl`, `resource_sink`, `chair`, `trash_can` |
| n18 | action | t2:s20 | cool the lettuce slice in the fridge and remove it | `lettuce`*, `fridge`*, `remove`*, `slice`*, `state_sliced`*, `dishwasher`, `spatula`, `raisin`, `topic_food_safety`, `nutmeg`, `bowl`, `grape_must` |
| n19 | action | t2:s22 | take a step to the left to face the counter | `counter`*, `island`, `face`*, `left_of`, `pick_up`*, `walk_backward`, `turn`, `sink`, `desk`, `table`, `stand_up`, `look` |
| n20 | action | t2:s24 | place the lettuce slice on the counter to the right of the sink | `lettuce`*, `counter`*, `sink`*, `slice`*, `island`, `place`*, `right_of`*, `state_sliced`*, `resource_sink`, `dishwasher`, `turn`, `knife` |

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
- heat.destination → object_label
- rinse.destination → object_label
- pour.destination → object_label
- walk.destination → object_label
- face.target → object_label
- pick_up.target → object_label, food_label
- pick_up.source → object_label
- pick_up.color → color_label
- failure.system → platform_label

## Retrieved records

### Shared rules that govern the records below (full text)

**rule_lexical_groups** (v19/rule/lexical-groups; core)

Section 3.1 defines value groups: `group::key` values of type ATOM[group]. Open groups admit any key of their form (examples are not whitelists); standard groups admit the codes of their bundled standard (ISO 3166-1 alpha-2 for country, ISO 4217 for currency). Leaf values are never glossary entries. Consumer signatures alone decide where a group may appear. Retired bare symbols are invalid.

**rule_reading_guide** (v19/rule/reading-guide; core)

The spec governs syntax/types; this glossary defines vocabulary. Signature notation: ? optional, A / B explicit alternatives, void no result. Omitted optional arguments are unspecified. Value entries are category-refined STRING primitives; complex meanings require composition. Aliases are contextual hints, not unconditional equivalences. Report ambiguity. IDs use v19/<category>/<symbol>, v19/support/<symbol> or v19/composite/<symbol>. Statuses apply to this candidate: Retained preserves meaning; Adapted uses the stated contract; Composite requires TERM (bare STRING deprecated); Structural is syntax/argument vocabulary; Needs clarification is unusable until resolved; Deprecated is historical; Accepted is usable within this candidate.

**rule_recording_signatures** (v19/rule/recording-signatures; rule governing slice)

RECORD ACTION uses the operation signature with REF[STRING] → TERM and LIST[REF[STRING]] → LIST[TERM]; other types/categories stay unchanged. Return EVENT, never the runtime result. Record actual outputs as attributed CLAIMs. Do not infer missing resources.

**rule_speech_acts_general** (v19/rule/speech-acts-general; core)

UTTER-only, void, with the spec's speech attributes and LIST[TERM] constraints. No result binding. Literal content cannot replace required semantic arguments for structured coverage.

**rule_structural_constructs** (v19/rule/structural-constructs; core)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; rule governing menu_works)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_category_cuisine_value** (v19/rule/category/cuisine-value; rule governing cuisine_indian)

STRING cuisine class; cuisine_indian is a cuisine filter, not the location India.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing lettuce)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_location_name** (v19/rule/category/location-name; rule governing counter)

STRING location descriptor. A `table` surface is not the generated artifact category art_table.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing left_of)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_state_value** (v19/rule/category/state-value; rule governing state_sliced)

STRING condition used in selection. state_warm does not command heat; “hot” is not automatically synonymous with “warm.”

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_food_safety)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_category_transformation_value** (v19/rule/category/transformation-value; rule governing transform_remove_br)

TERM-described transformation. Pass it through constraints; no ungoverned transformations attribute.

**rule_composites_general** (v19/rule/composites-general; rule governing transform_remove_br)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_examples_general** (v19/rule/examples-general; rule governing example_a_select_two_pillows_and_move_those_objects)

Examples use this glossary's contracts. They have not been verified by an implemented BrainCode parser.

**rule_operations_general** (v19/rule/operations-general; rule governing slice)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_supplemental_general** (v19/rule/supplemental-general; rule governing coffee_maker)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; rule governing presentation_slide)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- add_to_cart | operation | operation-vocabulary | (target: LIST[REF[STRING]]) -> void | Add the explicitly selected items. Does not pay or place an order.  ⟵ candidate
- drop | operation | operation-vocabulary | (target: REF[STRING] / TERM) -> void | Drop or release the held target object from the agent's hand. | not: place (which requires a destination receptacle) | aliases: drop, let go, put down  ⟵ candidate
- face | operation | operation-vocabulary | (target: STRING / TERM / ATOM[object_label]) -> void | Orient agent body/camera directly toward a target entity. target must be a perceptible entity. | aliases: orient_towards  ⟵ candidate
- heat | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Heat using the stated resource; same identity. Selecting a warm object does not imply heating it.  ⟵ candidate
- look | operation | operation-vocabulary | (direction: STRING) -> void | Tilt or adjust agent visual camera gaze. direction is up, down, or straight. | aliases: tilt_camera  ⟵ candidate
- pick_up | operation | operation-vocabulary | (target: STRING / ATOM[object_label] / ATOM[food_label], quantity?: NUMBER, source?: STRING / ATOM[object_label], color?: STRING / ATOM[color_label], shape?: STRING, state?: STRING) -> REF[STRING] or LIST[REF[STRING]] | Select/acquire objects. Missing quantity or literal 1 returns REF; integer literal greater than 1 returns LIST[REF]. Other values are invalid for this profile. | aliases: grab, take, retrieve  ⟵ candidate
- place | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label], location?: STRING / ATOM[object_label], relation?: STRING) -> void | Place an already acquired object. Spatial relation must be explicit if the source distinguishes it. | aliases: put, insert  ⟵ candidate
- pour | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Transfer selected liquid to the destination, preserving tracked material identity.  ⟵ candidate
- remove | operation | operation-vocabulary | (target: REF[STRING] / TERM, source?: STRING / TERM) -> void | Remove an object from an enclosure or container. target must be an object inside source. | aliases: take_out  ⟵ candidate
- rinse | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Rinse using the stated resource; return the same identity. It is not enough that the object is already clean. | aliases: wash  ⟵ candidate
- select_option | operation | operation-vocabulary | (target: REF[STRING], value: STRING) -> void | Select an option from a dropdown or select menu element. target must be a select element. | aliases: choose_option, choose_dropdown, pick_option  ⟵ candidate
- slice | operation | operation-vocabulary | (target: REF[STRING] / TERM) -> REF[STRING] | Slice the selected material or described term, preserving its tracked aggregate identity. | aliases: chop, cut  ⟵ candidate
- stand_up | operation | operation-vocabulary | () -> void | Return agent posture to standard upright standing position. agent must be in a non-standing posture. | aliases: stand  ⟵ candidate
- turn | operation | operation-vocabulary | (direction: STRING) -> void | Rotate agent body/view orientation. direction is typically left, right, or angle. | aliases: rotate, turn_around  ⟵ candidate
- turn_on | operation | operation-vocabulary | (target: REF[STRING] / TERM) -> void | Activate or start an appliance or device. target must be an activatable device. | aliases: activate, activate_appliance, switch_on  ⟵ candidate
- walk | operation | operation-vocabulary | (destination: STRING / TERM / ATOM[object_label], relation?: STRING) -> void | Locomote towards a target destination or landmark. destination must identify a valid entity or location. | aliases: move_to, go_to, navigate_to  ⟵ candidate
- walk_backward | operation | operation-vocabulary | (modifier?: STRING) -> void | Walk backward. Optional modifier can specify the degree or minor distance of movement. | not: walk (which moves forward toward a destination) | aliases: move backward, step back  ⟵ candidate

### constructors

- calculation | constructor | TERM calculation(inputs: LIST[TERM], operation: STRING, result?: TERM) -> TERM | Constructs a descriptive representation of an arithmetic or algorithmic calculation step with inputs, operation identifier, and optional resulting value. | not: an executed runtime action or factual claim of outcome | aliases: math_operation, compute_step  ⟵ candidate
- presentation_slide | constructor | TERM presentation_slide(number: NUMBER, title: STRING, content?: LIST[TERM]) -> TERM | Constructs a descriptor for a presentation slide with slide number, title, and optional content items. | not: a complete document artifact (use art_structured_report or art_plan) | aliases: slide, presentation slide, slide outline  ⟵ candidate
- remove_literal | constructor | TERM remove_literal(text: STRING) -> TERM | Remove occurrences of that exact literal in the stated artifact | not: Not remove similar markup unless specified  ⟵ candidate

### composites

- transform_remove_br | composite | transformation-value | TERM transform_remove_br() -> TERM | Remove <br /> tags. | = remove_literal(text="<br />")  ⟵ candidate

### claim relations

- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ core
- menu_works | claim_relation | CLAIM menu_works(property: STRING) | Asserts that a menu or recipe plan satisfies an operational criterion. menu evaluation. | aliases: menu_satisfies  ⟵ candidate
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ core

### links

- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ core
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ core
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ core

### values

- cuisine_indian | value | cuisine-value | Indian cuisine. | aliases: Indian food, Indian  ⟵ candidate
- bowl | value | entity-name | A container/dish used for holding food or small items. | aliases: bowl  ⟵ candidate
- bread | value | entity-name | A bread loaf or slice food object. | aliases: bread  ⟵ candidate
- cabinet | value | entity-name | An enclosed cupboard or cabinet storage furniture unit with doors or shelves. | not: counter (a countertop surface) or dresser (a chest of drawers) | aliases: cabinet, cupboard, storage cabinet, kitchen cupboard  ⟵ candidate
- chair | value | entity-name | A chair furniture seat with a backrest. | not: object_label::armchair (specifically an object_label::armchair with side armrests) or object_label::sofa | aliases: chair, seat  ⟵ candidate
- cheese | value | entity-name | Dairy food item: cheese. | not: meat or non-dairy food items | aliases: cheese  ⟵ candidate
- cloves | value | entity-name | Aromatic dried flower buds of Syzygium aromaticum used as a culinary spice. | not: cinnamon, nutmeg, or other distinct spice varieties | aliases: cloves, clove, ground cloves, whole cloves  ⟵ candidate
- coffee_maker | value | entity-name | A coffee-making appliance; not automatically a heating resource  ⟵ candidate
- desk | value | entity-name | A work desk furniture surface. | aliases: desk  ⟵ candidate
- dishwasher | value | entity-name | A dishwasher kitchen appliance. | not: sink (a washing basin) or washing_machine (a laundry appliance) | aliases: dishwasher, dish washer, dishwashing machine  ⟵ candidate
- door | value | entity-name | A door architectural barrier or entryway. | not: wall or close/open operations | aliases: door, doorway, room door  ⟵ candidate
- dresser | value | entity-name | A chest of drawers / dresser furniture. | aliases: dresser  ⟵ candidate
- dried_fruit | value | entity-name | Generic dried fruit food item. | not: fresh fruit or specific dried varieties like raisin or sultana | aliases: dried fruit, dried fruits  ⟵ candidate
- fridge | value | entity-name | A refrigerator cooling appliance. | aliases: fridge  ⟵ candidate
- grape_must | value | entity-name | Freshly crushed fruit juice mixture before fermentation. | not: clarified fruit_juice or finished wine | aliases: grape must, must  ⟵ candidate
- knife | value | entity-name | A cutting utensil used for slicing or food preparation. | aliases: knife  ⟵ candidate
- lettuce | value | entity-name | A head of lettuce or leafy green vegetable food item. | not: food_label::tomato or food_label::potato (other vegetable items) | aliases: lettuce, head of lettuce, salad greens  ⟵ candidate
- microwave | value | entity-name | A microwave oven appliance. | aliases: microwave  ⟵ candidate
- nutmeg | value | entity-name | Ground or whole nutmeg culinary spice from Myristica fragrans seed. | not: cinnamon, cloves, or other distinct spice varieties | aliases: nutmeg, ground nutmeg  ⟵ candidate
- pan | value | entity-name | A metal cooking vessel, frying pan, skillet, saucepan, or pot cookware item used for preparing, heating, or holding food. | not: bowl (deep concave vessel) or plate (shallow flat dining dish) | aliases: pan, frying pan, skillet, saucepan, pot  ⟵ candidate
- pencil | value | entity-name | A pencil writing instrument. | aliases: pencil  ⟵ candidate
- plate | value | entity-name | A shallow, flat dish or vessel used for holding, preparing, or serving food. | not: bowl (deep concave vessel) or table (furniture surface) | aliases: dish, plate  ⟵ candidate
- raisin | value | entity-name | Dried grape food item. | not: sultana (specifically dried white grape) or fresh wine_grape | aliases: raisin, raisins, dried grape  ⟵ candidate
- resource_chiller | value | entity-name | Canonical abstract chilling resource when no particular appliance is named.  ⟵ candidate
- resource_heater | value | entity-name | Canonical abstract heating resource when no particular appliance is named.  ⟵ candidate
- resource_sink | value | entity-name | Canonical abstract washing resource when no particular sink is named.  ⟵ candidate
- scissors | value | entity-name | A handheld shearing cutting tool with two pivoted blades used for cutting paper, ribbon, and crafting materials. | not: knife (a kitchen or food preparation cutting utensil) | aliases: scissors, shears, pair of scissors  ⟵ candidate
- shelf | value | entity-name | A flat horizontal shelving structure or shelving furniture unit used for storage and holding objects. | not: cabinet (an enclosed cupboard with doors) or table (a freestanding table surface) | aliases: shelf, shelves, bookshelf, wall shelf, shelving  ⟵ candidate
- shower | value | entity-name | A bathroom shower fixture or stall used for bathing. | not: sink (a washing basin) or toilet (a toilet fixture) | aliases: shower, shower stall  ⟵ candidate
- sink | value | entity-name | Washing basin. | aliases: sink  ⟵ candidate
- spatula | value | entity-name | A kitchen utensil with a broad, flat, and flexible blade used for lifting, flipping, or spreading food. | not: knife (cutting utensil) or spoon (scooping utensil) | aliases: spatula, turner, flipper  ⟵ candidate
- spoon | value | entity-name | An eating or cooking utensil. | aliases: spoon  ⟵ candidate
- stove | value | entity-name | A kitchen stove / range appliance for cooking or heating. | not: microwave | aliases: stove, range, cooktop  ⟵ candidate
- sultana | value | entity-name | Dried white seedless grape food product. | not: raisin (dark dried grape) or wine_grape | aliases: sultana, sultanas, golden raisin  ⟵ candidate
- toilet | value | entity-name | A toilet bathroom fixture or receptacle. | not: sink or trash_can | aliases: toilet, commode, restroom toilet  ⟵ candidate
- trash_can | value | entity-name | A waste receptacle container. | aliases: trash_can  ⟵ candidate
- water | value | entity-name | Water from a tap or faucet used for washing or rinsing. | not: sink or other liquids | aliases: water, tap water  ⟵ candidate
- corner | value | location-name | A corner area.  ⟵ candidate
- counter | value | location-name | A kitchen or room countertop surface. | aliases: counter  ⟵ candidate
- floor | value | location-name | The floor surface of an indoor room or architectural space. | not: wall (a vertical room boundary surface) or counter (a countertop surface) | aliases: floor, ground  ⟵ candidate
- island | value | location-name | A freestanding kitchen island counter or food preparation work surface. | not: counter (a perimeter countertop surface) or table (a dining or general furniture surface) | aliases: island, kitchen island, kitchen_island  ⟵ candidate
- table | value | location-name | A table surface.  ⟵ candidate
- wall | value | location-name | A room boundary wall surface. | aliases: wall  ⟵ candidate
- behind | value | spatial-relation | Positioned behind.  ⟵ candidate
- in_front_of | value | spatial-relation | Positioned in front of. | aliases: in front of  ⟵ candidate
- left_of | value | spatial-relation | To the left of. | aliases: left of  ⟵ candidate
- on | value | spatial-relation | Resting atop. | aliases: on top of  ⟵ dependency of example_a_select_two_pillows_and_move_those_objects
- right_of | value | spatial-relation | To the right of. | aliases: right of  ⟵ candidate
- state_clean | value | state-value | Clean condition. | aliases: clean  ⟵ candidate
- state_sliced | value | state-value | The condition of being sliced or cut into thin pieces. | not: the operation slice itself | aliases: sliced, slice, chopped, cut  ⟵ candidate
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

