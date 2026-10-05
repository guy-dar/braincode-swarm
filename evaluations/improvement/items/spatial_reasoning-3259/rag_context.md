# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 22 needs (decomposition: llm), 168 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | object | t1:s1 | circular path of 9 connected dots | `shape_round`*, `path_sklearn_linear_model_logistic_py`, `path_numpy_core_fromnumeric_py`, `rule_category_shape_value`, `corner`, `shape_triangular`, `path_pandas_src_testing_pyx`, `shape_rectangular`, `shape_oval`, `behind`, `wall`, `shape_square` |
| n2 | claim | t1:s2 | the starting position is the top dot of the path | `behind`, `in_front_of`, `on`, `path_numpy_core_fromnumeric_py`, `corner`, `rank_distance`, `walk`, `dir_desc`, `rank_direction`, `dir_asc`, `path_pandas_src_testing_pyx`, `location_spec` |
| n3 | object | t1:s2 | great white shark → `animal_label::<key>` | `sultana`, `resource_sink`, `topic_spider_man_2`, `topic_greatest_cricketer_of_all_time`, `sponge`, `material_memory_foam`, `unit_word`, `bionic_person`, `meat`, `animal_label`*, `sun`, `resource_heater` |
| n4 | claim | t1:s2 | the great white shark is located at the top dot | `spatial_state`*, `on`, `corner`, `other_side_of`, `outcome`, `face`, `sun`, `in_front_of`, `wall`, `rank_distance`, `look`, `rank_direction` |
| n5 | claim | t1:s3 | the elements are arranged in a clockwise direction from the great white shark | `other_side_of`, `shape_oval`, `on`, `in_front_of`, `outcome`, `wall`, `left_of`, `earth`, `shape_round`, `behind`, `corner`, `rank_direction` |
| n6 | object | t1:s3 | umbrella → `object_label::<key>` | `resource_chiller`, `chill`, `heat`, `art_plan`, `constraint_exclude_liberation_theme`, `fridge`, `table`, `resource_sink`, `chair`, `example_a_select_two_pillows_and_move_those_objects`, `laptop`, `state_cold` |
| n7 | object | t1:s3 | garter snake → `animal_label::<key>` | `figurine`, `spatula`, `caddy`, `tattoos`, `watch`, `yarn`, `entity_flowers`, `animal_label`*, `topic_spider_man_2`, `resource_chiller`, `art_story`, `style_catchy` |
| n8 | object | t1:s3 | Christmas stocking → `object_label::<key>` | `avail_in_stock`, `avail_out_of_stock`, `gift`, `egift_card`, `entity_grocery_list`, `cat_limited_time_offers`, `entity_desserts`, `entity_cake`, `entity_condensed_grocery_list`, `cardboard_box`, `entity_sweet_food`, `meat` |
| n9 | object | t1:s3 | jigsaw puzzle → `object_label::<key>` | `scissors`, `yarn`, `spatula`, `topic_baldurs_gate_3`, `path_sklearn_linear_model_logistic_py`, `event_camper_in_sludge_pit`, `spoon`, `pan`, `resource_sink`, `bowl`, `resource_chiller`, `object_label`* |
| n10 | object | t1:s3 | Gila monster → `animal_label::<key>` | `figurine`, `art_story`, `spatula`, `bionic_person`, `topic_spider_man_2`, `resource_chiller`, `animal_label`*, `resource_sink`, `sun`, `target`, `resource_heater`, `example_a_select_two_pillows_and_move_those_objects` |
| n11 | object | t1:s3 | Tibetan Terrier → `animal_label::<key>` | `animal_label`*, `chill`, `dog`, `path_pandas_src_testing_pyx`, `locale_zh`, `sym_pandas_testing_assert_almost_equal`, `locale_hi_en`, `caddy`, `ryokan`, `chair`, `tone_empathetic`, `resource_chiller` |
| n12 | object | t1:s3 | moped → `object_label::<key>` | `chair`, `laptop`, `turn`, `remote_control`, `spatula`, `driver_license`, `phone`, `dishwasher`, `resource_sink`, `example_a_select_two_pillows_and_move_those_objects`, `toilet`, `walk_backward` |
| n13 | object | t1:s3 | horse-drawn vehicle → `object_label::<key>` | `rental_vehicle`, `valet`, `driver_license`, `chair`, `example_a_select_two_pillows_and_move_those_objects`, `vehicle_allowance`, `art_itinerary`, `art_structured_report`, `art_plan`, `art_technical_explanation`, `shape_round`, `walk` |
| n14 | action | t1:s4 | move around the circular path | `shape_round`*, `turn`, `walk`, `walk_backward`, `path_sklearn_linear_model_logistic_py`, `rule_category_shape_value`, `corner`, `hover`, `shape_triangular`, `shape_oval`, `path_pandas_src_testing_pyx`, `shape_rectangular` |
| n15 | constraint | t1:s4 | start moving from the jigsaw puzzle | `path_sklearn_linear_model_logistic_py`, `topic_baldurs_gate_3`, `door`, `event_camper_in_sludge_pit`, `yarn`, `behind`, `entity_assembly_tips`, `on`, `constraint_exclude_flowery_language`, `constraint_budget_limited`, `walk`, `constraint_exclude_liberation_theme` |
| n16 | temporal | t1:s4 | first move 8 steps in a clockwise direction | `walk_backward`, `dir_desc`, `shape_oval`, `shape_triangular`, `corner`, `turn`, `left_of`, `shape_round`, `in_front_of`, `behind`, `walk`, `look` |
| n17 | temporal | t1:s4 | then move 2 steps in a clockwise direction | `walk_backward`, `other_side_of`, `corner`, `behind`, `turn`, `in_front_of`, `shape_round`, `shape_triangular`, `left_of`, `look`, `shape_oval`, `walk` |
| n18 | temporal | t1:s4 | then move 2 steps in a clockwise direction | `walk_backward`, `other_side_of`, `corner`, `behind`, `turn`, `in_front_of`, `shape_round`, `shape_triangular`, `left_of`, `look`, `shape_oval`, `walk` |
| n19 | temporal | t1:s4 | then move 3 steps in a counter-clockwise direction | `walk_backward`, `corner`, `shape_triangular`, `in_front_of`, `shape_round`, `other_side_of`, `turn`, `behind`, `look`, `shape_oval`, `on`, `wall` |
| n20 | speech_act | t1:s5 | ask what object is found at the final position | `ask`*, `place`, `close`, `respond`, `other_side_of`, `rank_direction`, `propose`, `rank_distance`, `then`, `inform`, `rule_category_artifact_value`, `drop` |
| n21 | constraint | t1:s6 | final answer must be only the object name | `activity`, `entity_mains`, `close`, `object_label`, `dog`, `entity_flowers`, `target`, `constraint_include_character_attribute_list`, `respond`*, `decision`, `keys`, `constraint_budget_limited` |
| n22 | constraint | t1:s7 | final answer must be 'unknown' if the object was not previously seen | `metric_order_late`, `place`, `remove_literal`, `test_condition`, `close`, `constraint_exclude_flowery_language`, `respond`*, `constraint_budget_limited`, `constraint_include_character_attribute_list`, `state_empty`, `constraint_exclude_liberation_theme`, `entity_flowers` |

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
- face.target → object_label
- chill.destination → object_label
- heat.destination → object_label
- place.destination → object_label
- place.location → object_label
- activity.object → object_label, food_label, animal_label
- activity.location → country
- activity.instrument → object_label, platform_label
- subject.qualifier → platform_label
- subject.location → country
- requirement.value → platform_label
- pick_up.target → object_label, food_label
- pick_up.source → object_label
- pick_up.color → color_label
- failure.system → platform_label

## Retrieved records

### Shared rules that govern the records below (full text)

**rule_lexical_groups** (v19/rule/lexical-groups; rule governing platform_label)

Section 3.1 defines value groups: `group::key` values of type ATOM[group]. Open groups admit any key of their form (examples are not whitelists); standard groups admit the codes of their bundled standard (ISO 3166-1 alpha-2 for country, ISO 4217 for currency). Leaf values are never glossary entries. Consumer signatures alone decide where a group may appear. Retired bare symbols are invalid.

**rule_reading_guide** (v19/rule/reading-guide; core)

The spec governs syntax/types; this glossary defines vocabulary. Signature notation: ? optional, A / B explicit alternatives, void no result. Omitted optional arguments are unspecified. Value entries are category-refined STRING primitives; complex meanings require composition. Aliases are contextual hints, not unconditional equivalences. Report ambiguity. IDs use v19/<category>/<symbol>, v19/support/<symbol> or v19/composite/<symbol>. Statuses apply to this candidate: Retained preserves meaning; Adapted uses the stated contract; Composite requires TERM (bare STRING deprecated); Structural is syntax/argument vocabulary; Needs clarification is unusable until resolved; Deprecated is historical; Accepted is usable within this candidate.

**rule_recording_signatures** (v19/rule/recording-signatures; rule governing walk)

RECORD ACTION uses the operation signature with REF[STRING] → TERM and LIST[REF[STRING]] → LIST[TERM]; other types/categories stay unchanged. Return EVENT, never the runtime result. Record actual outputs as attributed CLAIMs. Do not infer missing resources.

**rule_speech_acts_general** (v19/rule/speech-acts-general; rule governing ask)

UTTER-only, void, with the spec's speech attributes and LIST[TERM] constraints. No result binding. Literal content cannot replace required semantic arguments for structured coverage.

**rule_structural_constructs** (v19/rule/structural-constructs; core)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; rule governing spatial_state)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_attributes_and_generate** (v19/rule/attributes-and-generate; rule governing rank_direction)

Attribute entries name arguments; legality/types come from each operation, not global membership. GENERATE uses the spec's core fields; retained artifact profiles return STRING. Numeric/list results need explicit profiles. Legacy itinerary fields expand to TERM constraints: duration/duration_unit → duration(amount,unit); stop_min_per_day/stop_requirement → minimum_per_period(class,count,period=unit_day), never an inferred temple class; max_walk_duration/unit → maximum_between_stops(activity="walk",amount,unit). No legacy shorthand is enabled. Old events/character_properties/transformations become explicitly scoped TERM constraints. Message purpose is TERM, not send_email.content: GENERATE exact STRING content, then send. Report opaque fallback separately.

**rule_category_artifact_value** (v19/rule/category/artifact-value; candidate)

STRING artifact class for GENERATE.target. art_story says what kind of artifact to produce, not what occurs in its plot.

**rule_category_code_value** (v19/rule/category/code-value; rule governing path_sklearn_linear_model_logistic_py)

path_/sym_ remain STRING identities; migrated chg_/assert_ are TERM constructors. Do not recover an exact file path by guessing from underscores.

**rule_category_constraint_value** (v19/rule/category/constraint-value; rule governing constraint_exclude_liberation_theme)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_descriptive_value** (v19/rule/category/descriptive-value; rule governing tattoos)

STRING modifier/domain label; never a free-form proposition. dom_sgi needs its intended referent established before semantically dependent use.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; rule governing unit_word)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing sultana)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_event_value** (v19/rule/category/event-value; rule governing event_camper_in_sludge_pit)

TERM-described narrative event, not a recorded EVENT. Require inclusion explicitly when generating a story.

**rule_category_locale_value** (v19/rule/category/locale-value; rule governing locale_zh)

STRING locale. “English” alone does not always mean locale_en_us; preserve ambiguity.

**rule_category_location_name** (v19/rule/category/location-name; rule governing corner)

STRING location descriptor. A `table` surface is not the generated artifact category art_table.

**rule_category_metric_value** (v19/rule/category/metric-value; rule governing metric_order_late)

STRING metric identity, not a Boolean value. Uptime and response time need numeric observations with units; order-late is Boolean-valued. Do not type every metric as BOOL.

**rule_category_product_attribute_value** (v19/rule/category/product-attribute-value; rule governing material_memory_foam)

STRING color/size/product-market facets. gender_women describes a product category, not an assertion about a person's gender.

**rule_category_search_value** (v19/rule/category/search-value; rule governing rank_distance)

STRING refinements rank_ / dir_ / cat_ / avail_ / genre_ are separate. rank_rating may fill rank_field; genre_label::comedy may not. “Cheapest” usually requires both rank_price and dir_asc, not rank_price alone.

**rule_category_shape_value** (v19/rule/category/shape-value; candidate)

STRING geometry. shape_round may select a circular object; it does not imply color or dimensions.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing behind)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_state_value** (v19/rule/category/state-value; rule governing state_cold)

STRING condition used in selection. state_warm does not command heat; “hot” is not automatically synonymous with “warm.”

**rule_category_style_value** (v19/rule/category/style-value; rule governing style_catchy)

STRING production style. style_narrative does not establish that described events occurred.

**rule_category_tone_value** (v19/rule/category/tone-value; rule governing tone_empathetic)

STRING register. tone_urgent describes urgency, not a concrete deadline.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_spider_man_2)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_composites_general** (v19/rule/composites-general; rule governing topic_greatest_cricketer_of_all_time)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_examples_general** (v19/rule/examples-general; rule governing example_a_select_two_pillows_and_move_those_objects)

Examples use this glossary's contracts. They have not been verified by an implemented BrainCode parser.

**rule_operations_general** (v19/rule/operations-general; rule governing walk)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_supplemental_general** (v19/rule/supplemental-general; rule governing art_itinerary)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; rule governing location_spec)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- chill | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Chill using the stated resource; same identity.  ⟵ candidate
- close | operation | operation-vocabulary | (target: REF[STRING] / TERM) -> void | Close an articulated receptacle or appliance door. target must be a closable entity. | aliases: close_receptacle, close_door  ⟵ candidate
- drop | operation | operation-vocabulary | (target: REF[STRING] / TERM) -> void | Drop or release the held target object from the agent's hand. | not: place (which requires a destination receptacle) | aliases: drop, let go, put down  ⟵ candidate
- face | operation | operation-vocabulary | (target: STRING / TERM / ATOM[object_label]) -> void | Orient agent body/camera directly toward a target entity. target must be a perceptible entity. | aliases: orient_towards  ⟵ candidate
- heat | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Heat using the stated resource; same identity. Selecting a warm object does not imply heating it.  ⟵ candidate
- hover | operation | operation-vocabulary | (target: REF[STRING]) -> void | Move pointer cursor over an interactive web element without clicking. target must resolve to a valid element reference. | aliases: mouse_over  ⟵ candidate
- look | operation | operation-vocabulary | (direction: STRING) -> void | Tilt or adjust agent visual camera gaze. direction is up, down, or straight. | aliases: tilt_camera  ⟵ candidate
- pick_up | operation | operation-vocabulary | (target: STRING / ATOM[object_label] / ATOM[food_label], quantity?: NUMBER, source?: STRING / ATOM[object_label], color?: STRING / ATOM[color_label], shape?: STRING, state?: STRING) -> REF[STRING] or LIST[REF[STRING]] | Select/acquire objects. Missing quantity or literal 1 returns REF; integer literal greater than 1 returns LIST[REF]. Other values are invalid for this profile. | aliases: grab, take, retrieve  ⟵ dependency of example_a_select_two_pillows_and_move_those_objects
- place | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label], location?: STRING / ATOM[object_label], relation?: STRING) -> void | Place an already acquired object. Spatial relation must be explicit if the source distinguishes it. | aliases: put, insert  ⟵ candidate
- stand_up | operation | operation-vocabulary | () -> void | Return agent posture to standard upright standing position. agent must be in a non-standing posture. | aliases: stand  ⟵ candidate
- turn | operation | operation-vocabulary | (direction: STRING) -> void | Rotate agent body/view orientation. direction is typically left, right, or angle. | aliases: rotate, turn_around  ⟵ candidate
- walk | operation | operation-vocabulary | (destination: STRING / TERM / ATOM[object_label], relation?: STRING) -> void | Locomote towards a target destination or landmark. destination must identify a valid entity or location. | aliases: move_to, go_to, navigate_to  ⟵ candidate
- walk_backward | operation | operation-vocabulary | (modifier?: STRING) -> void | Walk backward. Optional modifier can specify the degree or minor distance of movement. | not: walk (which moves forward toward a destination) | aliases: move backward, step back  ⟵ candidate

### speech acts

- ask | speech_act | operation-vocabulary | UTTER ask(target: TERM, or a sufficiently precise topic: STRING / TERM) | Request information/advice; not an assertion of an answer. | aliases: ask, how should  ⟵ candidate
- inform | speech_act | operation-vocabulary | UTTER inform(target: CLAIM) | Present the proposition; preserve its holder/status.  ⟵ candidate
- propose | speech_act | operation-vocabulary | UTTER propose(target: TERM) | Suggest an action/idea; does not record it as performed.  ⟵ candidate
- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ candidate
- bionic_person | constructor | TERM bionic_person(composition?: STRING / TERM) -> TERM | Constructs a descriptive representation of a bionic person or cyborg entity with biological and mechanical components. | not: a standard human role (use role_user or role_adults) or a purely artificial device. | aliases: bionic person, bionic people, cyborg, half human half robot  ⟵ candidate
- decision | constructor | TERM decision(activity: TERM) -> TERM | A decision whose content is the described activity | not: Not proof it was carried out  ⟵ candidate
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ dependency of constraint_exclude_liberation_theme
- include | constructor | TERM include(item: STRING / TERM) -> TERM | Require the identified content/item | not: Not permission to invent an instance in a recorded trace  ⟵ dependency of constraint_include_character_attribute_list
- location_spec | constructor | TERM location_spec(address?: STRING, area?: STRING, city?: STRING, state?: STRING) -> TERM | Constructs a structured geographical location specification with regional and administrative qualifiers. | not: a fixed atomic location descriptor in location-name or a spatial relation | aliases: location_details, geographic_location  ⟵ candidate
- remove_literal | constructor | TERM remove_literal(text: STRING) -> TERM | Remove occurrences of that exact literal in the stated artifact | not: Not remove similar markup unless specified  ⟵ candidate
- rental_vehicle | constructor | TERM rental_vehicle(category: STRING, model?: STRING) -> TERM | Constructs a descriptive representation of a rental vehicle or vehicle category. | not: an acquired physical vehicle reference or employee vehicle policy (use vehicle_allowance) | aliases: rental_car, hire_car, mystery_car  ⟵ candidate
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ dependency of topic_greatest_cricketer_of_all_time
- spatial_constraint | constructor | TERM spatial_constraint(relation: STRING, object: TERM, reference: TERM) -> TERM | Constructs a descriptive spatial constraint between an object and a reference landmark. relation must specify a spatial configuration. | aliases: spatial_relation  ⟵ related to spatial_state
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ dependency of topic_greatest_cricketer_of_all_time
- test_condition | constructor | TERM test_condition(condition: STRING, expected: BOOL) -> TERM | A testable condition with the expected Boolean outcome | not: Expected outcome is not an observed result  ⟵ candidate
- vehicle_allowance | constructor | TERM vehicle_allowance(roles: STRING, types: LIST[STRING]) -> TERM | Constructs a specification of permitted vehicle types for defined employee roles. specifies vehicle permissions. | aliases: vehicle_permission  ⟵ candidate

### composites

- constraint_budget_limited | composite | constraint-value | TERM constraint_budget_limited() -> TERM | Limited budget. | = requirement(property="budget_limited", value=TRUE)  ⟵ candidate
- constraint_exclude_flowery_language | composite | constraint-value | TERM constraint_exclude_flowery_language() -> TERM | Avoid flowery language. | = exclude(item="flowery_language")  ⟵ candidate
- constraint_exclude_liberation_theme | composite | constraint-value | TERM constraint_exclude_liberation_theme() -> TERM | Avoid liberation theme. | = exclude(item="liberation_theme")  ⟵ candidate
- constraint_include_character_attribute_list | composite | constraint-value | TERM constraint_include_character_attribute_list() -> TERM | Include character attributes. | = include(item="character_attribute_list")  ⟵ candidate
- event_camper_in_sludge_pit | composite | event-value | TERM event_camper_in_sludge_pit() -> TERM | Campers interacting in a sludge pit. | = activity(verb="interact", actor="campers", location="sludge_pit")  ⟵ candidate
- topic_greatest_cricketer_of_all_time | composite | topic-value | TERM topic_greatest_cricketer_of_all_time() -> TERM | Greatest cricketer of all time. | = subject(kind="cricketer", qualifier=requirement(property="rank_by_greatness", value=1), time="all_time")  ⟵ candidate

### claim relations

- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ core
- has_state | claim_relation | CLAIM has_state(subject: TERM, state: STRING) | Asserts that an entity is currently in a physical, thermal, or operational state. state must be a valid state descriptor string. | aliases: in_state, state_is  ⟵ related to spatial_state
- occurred | claim_relation | CLAIM occurred(activity: TERM) | Asserts that an event, action, or activity took place in the past. past occurrence claim. | aliases: happened  ⟵ candidate
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ candidate
- spatial_state | claim_relation | CLAIM spatial_state(relation: STRING, object: TERM, reference: TERM) | Asserts an observed spatial configuration between an object and a reference landmark. relation must specify spatial configuration. | aliases: placed_at, located_at  ⟵ candidate

### links

- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ core
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ core
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ core
- then | link | LINK then(previous: EVENT, next: EVENT) | Represents temporal sequence and succession between two events where next follows previous. previous and next must be event terms. | aliases: followed_by, after_which  ⟵ candidate

### values

- art_character_profile | value | artifact-value | Descriptive character profile.  ⟵ candidate
- art_itinerary | value | artifact-value | An ordered travel plan; GENERATE returns STRING, not booked travel  ⟵ candidate
- art_plan | value | artifact-value | Actionable plan.  ⟵ candidate
- art_story | value | artifact-value | Narrative story.  ⟵ candidate
- art_structured_report | value | artifact-value | Headed/structured report.  ⟵ candidate
- art_technical_explanation | value | artifact-value | Technical explanation of a concept.  ⟵ candidate
- path_numpy_core_fromnumeric_py | value | code-value | Source code file path or exported symbol in scientific Python: path_numpy_core_fromnumeric_py. | aliases: path_numpy_core_fromnumeric_py  ⟵ candidate
- path_pandas_src_testing_pyx | value | code-value | Source code file path or exported symbol in scientific Python: path_pandas_src_testing_pyx. | aliases: path_pandas_src_testing_pyx  ⟵ candidate
- path_sklearn_linear_model_logistic_py | value | code-value | The scikit-learn logistic module path.  ⟵ candidate
- sym_pandas_testing_assert_almost_equal | value | code-value | Source code file path or exported symbol in scientific Python: sym_pandas_testing_assert_almost_equal. | aliases: sym_pandas_testing_assert_almost_equal  ⟵ candidate
- tattoos | value | descriptive-value | Descriptive concept of tattoos in cultural and social contexts. | aliases: tattoos  ⟵ candidate
- unit_word | value | duration-unit-value | Rendered whitespace-delimited word. | aliases: words  ⟵ candidate
- bowl | value | entity-name | A container/dish used for holding food or small items. | aliases: bowl  ⟵ candidate
- caddy | value | entity-name | A portable storage caddy, organizer box, or supply tote for carrying and organizing handheld tools and supplies. | not: cabinet (a stationary furniture cupboard) or safe (a secure metal lockbox) | aliases: caddy, supply caddy, wrapping caddy, tool caddy, organizer caddy, supply tote  ⟵ candidate
- cardboard_box | value | entity-name | A cardboard box, carton, or general storage box container. | not: tissue_box (specifically a box of paper tissues) or safe (a lockable metal container) | aliases: cardboard box, box, carton, storage box  ⟵ candidate
- chair | value | entity-name | A chair furniture seat with a backrest. | not: object_label::armchair (specifically an object_label::armchair with side armrests) or object_label::sofa | aliases: chair, seat  ⟵ candidate
- dishwasher | value | entity-name | A dishwasher kitchen appliance. | not: sink (a washing basin) or washing_machine (a laundry appliance) | aliases: dishwasher, dish washer, dishwashing machine  ⟵ candidate
- dog | value | entity-name | Animal entity: dog. | not: animal_label::cat or animal_label::donkey | aliases: dog, dogs, canine, pup, puppy  ⟵ candidate
- door | value | entity-name | A door architectural barrier or entryway. | not: wall or close/open operations | aliases: door, doorway, room door  ⟵ candidate
- driver_license | value | entity-name | An official government credential or authorization permitting an individual to operate motor vehicles. | not: vehicle_allowance (an employee vehicle policy) or rental_vehicle (a rental vehicle) | aliases: driver license, driver's license, driving license, driver licence, driver ID  ⟵ candidate
- earth | value | entity-name | The planet Earth as an astronomical celestial body. | not: soil, ground surface, or electrical grounding | aliases: earth, the earth, planet earth, Earth  ⟵ candidate
- egift_card | value | entity-name | Electronic gift card or digital voucher product. | aliases: digital_gift_card, e_gift_card  ⟵ candidate
- entity_assembly_tips | value | entity-name | Event planning item or menu category: entity_assembly_tips. | aliases: entity_assembly_tips  ⟵ candidate
- entity_cake | value | entity-name | Event planning item or menu category: entity_cake. | aliases: entity_cake  ⟵ candidate
- entity_condensed_grocery_list | value | entity-name | Event planning item or menu category: entity_condensed_grocery_list. | aliases: entity_condensed_grocery_list  ⟵ candidate
- entity_desserts | value | entity-name | Event planning item or menu category: entity_desserts. | aliases: entity_desserts  ⟵ candidate
- entity_flowers | value | entity-name | Flowers, blossoms, or floral design elements. | not: constraint_exclude_flowery_language (a prose style constraint) or agricultural food items | aliases: flowers, floral, flower, floral decorations  ⟵ candidate
- entity_grocery_list | value | entity-name | Event planning item or menu category: entity_grocery_list. | aliases: entity_grocery_list  ⟵ candidate
- entity_mains | value | entity-name | Event planning item or menu category: entity_mains. | aliases: entity_mains  ⟵ candidate
- entity_sweet_food | value | entity-name | Event planning item or menu category: entity_sweet_food. | aliases: entity_sweet_food  ⟵ candidate
- figurine | value | entity-name | A small carved, molded, or sculpted decorative statuette object. | not: character (a fictional persona) or captioned_figure (a document figure/photo) | aliases: figurine, statuette, statue, small statue, sculptural figure, miniature figure  ⟵ candidate
- fridge | value | entity-name | A refrigerator cooling appliance. | aliases: fridge  ⟵ candidate
- gift | value | entity-name | A physical gift or present item to be wrapped, given, or received. | not: egift_card (an electronic gift card or digital voucher product) | aliases: gift, present, wrapped gift, package  ⟵ candidate
- keys | value | entity-name | A physical key or set of keys / keychain object. | not: press_key (a UI keyboard key press operation) | aliases: keys, key, key chain, keychain  ⟵ candidate
- laptop | value | entity-name | A portable laptop computer physical object. | not: topic_macbook_pro_2017 (a generation topic label) | aliases: laptop, laptop computer, notebook  ⟵ candidate
- meat | value | entity-name | Food item: meat or beef. | not: animal_label::tuna or animal_label::fish (specific aquatic foods) | aliases: meat, beef  ⟵ candidate
- mittens | value | entity-name | Item or prop in joke/creative context: mittens. | aliases: mittens  ⟵ candidate
- pan | value | entity-name | A metal cooking vessel, frying pan, skillet, saucepan, or pot cookware item used for preparing, heating, or holding food. | not: bowl (deep concave vessel) or plate (shallow flat dining dish) | aliases: pan, frying pan, skillet, saucepan, pot  ⟵ candidate
- phone | value | entity-name | A telephone, mobile phone, smartphone, or cellular handset device. | not: remote_control (a handheld TV remote) or laptop (a portable computer) | aliases: phone, cell phone, cellphone, mobile phone, smartphone, telephone  ⟵ candidate
- remote_control | value | entity-name | A handheld electronic remote control device. | not: an individual button or interactive UI element | aliases: remote, remote control, TV remote, controller  ⟵ candidate
- resource_chiller | value | entity-name | Canonical abstract chilling resource when no particular appliance is named.  ⟵ candidate
- resource_heater | value | entity-name | Canonical abstract heating resource when no particular appliance is named.  ⟵ candidate
- resource_sink | value | entity-name | Canonical abstract washing resource when no particular sink is named.  ⟵ candidate
- scissors | value | entity-name | A handheld shearing cutting tool with two pivoted blades used for cutting paper, ribbon, and crafting materials. | not: knife (a kitchen or food preparation cutting utensil) | aliases: scissors, shears, pair of scissors  ⟵ candidate
- spatula | value | entity-name | A kitchen utensil with a broad, flat, and flexible blade used for lifting, flipping, or spreading food. | not: knife (cutting utensil) or spoon (scooping utensil) | aliases: spatula, turner, flipper  ⟵ candidate
- sponge | value | entity-name | A porous, absorbent sponge cleaning tool or object. | not: tissue_box (a paper tissue box) or other wiping materials | aliases: sponge, cleaning sponge  ⟵ candidate
- spoon | value | entity-name | An eating or cooking utensil. | aliases: spoon  ⟵ candidate
- sultana | value | entity-name | Dried white seedless grape food product. | not: raisin (dark dried grape) or wine_grape | aliases: sultana, sultanas, golden raisin  ⟵ candidate
- sun | value | entity-name | The central star of the Solar System. | not: an artificial lighting appliance or sunlight | aliases: sun, the sun, Sol  ⟵ candidate
- toilet | value | entity-name | A toilet bathroom fixture or receptacle. | not: sink or trash_can | aliases: toilet, commode, restroom toilet  ⟵ candidate
- watch | value | entity-name | A watch or wristwatch timepiece object. | not: clock (a stationary timepiece appliance) or duration units like unit_hour | aliases: watch, wristwatch, wrist watch  ⟵ candidate
- yarn | value | entity-name | Item or prop in joke/creative context: yarn. | aliases: yarn  ⟵ candidate
- locale_hi_en | value | locale-value | Hinglish (Hindi-English mix). | aliases: hinglish  ⟵ candidate
- locale_zh | value | locale-value | Chinese language locale (Simplified and Traditional Chinese). | not: a specific geographical region or nationality (use location-name) | aliases: chinese, zh, zh-cn, zh-tw, mandarin  ⟵ candidate
- corner | value | location-name | A corner area.  ⟵ candidate
- counter | value | location-name | A kitchen or room countertop surface. | aliases: counter  ⟵ candidate
- ryokan | value | location-name | Traditional Japanese establishment or hospitality venue: ryokan. | aliases: ryokan  ⟵ candidate
- table | value | location-name | A table surface.  ⟵ candidate
- wall | value | location-name | A room boundary wall surface. | aliases: wall  ⟵ candidate
- metric_order_late | value | metric-value | Whether an order is late. | aliases: order is late, delayed  ⟵ candidate
- material_memory_foam | value | product-attribute-value | Memory foam viscoelastic polyurethane material qualifier. | not: sponge (a porous cleaning tool) or generic bedding | aliases: memory foam, memory_foam, viscoelastic foam  ⟵ candidate
- valet | value | product-attribute-value | Valet parking or dedicated vehicle attendant service. | aliases: valet_parking  ⟵ candidate
- avail_in_stock | value | search-value | Available for purchase now. | aliases: available  ⟵ candidate
- avail_out_of_stock | value | search-value | Unavailable for purchase now. | aliases: sold out  ⟵ candidate
- cat_limited_time_offers | value | search-value | Category: time-limited deals.  ⟵ candidate
- dir_asc | value | search-value | Ascending rank direction. | aliases: lowest first  ⟵ candidate
- dir_desc | value | search-value | Descending rank direction. | aliases: highest first  ⟵ candidate
- rank_distance | value | search-value | Rank field: proximity. | aliases: nearest, closest  ⟵ candidate
- shape_oval | value | shape-value | Oval. | aliases: oval  ⟵ candidate
- shape_rectangular | value | shape-value | Rectangular. | aliases: rectangular, rectangle  ⟵ candidate
- shape_round | value | shape-value | Circular/round. | aliases: round, circular  ⟵ candidate
- shape_square | value | shape-value | Square. | aliases: square  ⟵ candidate
- shape_triangular | value | shape-value | Triangular. | aliases: triangular, triangle  ⟵ candidate
- behind | value | spatial-relation | Positioned behind.  ⟵ candidate
- in_front_of | value | spatial-relation | Positioned in front of. | aliases: in front of  ⟵ candidate
- left_of | value | spatial-relation | To the left of. | aliases: left of  ⟵ candidate
- on | value | spatial-relation | Resting atop. | aliases: on top of  ⟵ candidate
- other_side_of | value | spatial-relation | Positioned on the opposite or other side of a reference object. | not: next_to (which indicates general adjacency) | aliases: other side, other side of, opposite side of, opposite side  ⟵ candidate
- state_cold | value | state-value | Cold or chilled condition. | aliases: cold, chilled  ⟵ candidate
- state_empty | value | state-value | Contains no intended material or usable remaining amount. | aliases: empty, used up  ⟵ candidate
- style_catchy | value | style-value | Catchy, attention-grabbing style. | aliases: catchy  ⟵ candidate
- tone_empathetic | value | tone-value | Conveys empathy/understanding. | aliases: sympathetically  ⟵ candidate
- topic_baldurs_gate_3 | value | topic-value | Baldur's Gate 3.  ⟵ candidate
- topic_spider_man_2 | value | topic-value | Marvel's Spider-Man 2.  ⟵ candidate

### attributes

- rank_direction | attribute | attribute-name | Sort direction from search-value.  ⟵ candidate
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

