# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 20 needs (decomposition: llm), 187 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | action | t1:s1 | solve a grid-based logic puzzle with 6 positions | `calculation`, `conditional`, `sequence`, `sort`, `extract`, `format_numbered_list`, `preserve`, `rank_distance`, `slice`, `conjunction`, `stand_up`, `respond` |
| n2 | object | t1:s2 | house colors (gold, pink, purple, white, yellow, turquoise) → `color_label::<key>` | `color_pink`*, `color_label`*, `lamp`, `sultana`, `entity_flowers`, `living_room`, `wall`, `grape_merlot`, `coffee_maker`, `grape_chardonnay`, `resource_heater`, `fruit_juice` |
| n3 | object | t1:s3 | NFL teams (Baltimore Ravens, New England Patriots, San Francisco 49ers, Philadelphia Eagles, Seattle Seahawks, Carolina Panthers) | `new_york_university`, `topic_current_events`*, `dog`, `cuisine_pizza`, `cat_game`, `role_support_team`, `format_numbered_list`, `animal_label`, `sort`, `rank_distance`, `unit_item`, `stove` |
| n4 | object | t1:s4 | professions (actor, dancer, writer, athlete, singer, doctor) | `tone_professional`, `role_agent`, `style_academic`, `foreigners`, `gender_women`, `role_colleague`, `topic_greatest_cricketer_of_all_time`, `role_adults`, `role_respondent`, `gender_men`, `role_user`, `art_character_profile` |
| n5 | object | t1:s5 | book genres (science fiction, magical realism, mystery, humor, spiritual, romance) → `genre_label::<key>` | `genre_label`*, `textbook`*, `genre_electronic`, `cat_game`, `art_story`, `style_narrative`, `beliefs`, `rule_category_search_value`, `topic_baldurs_gate_3`, `genre_pop_rock`, `mittens`, `art_short_text` |
| n6 | object | t1:s6 | gemstones (Ambers, Pearls, Gypsum, Dolomites, Topaz, Jade) | `grape_merlot`, `wine_grape`, `grape_pinot_noir`, `grape_chardonnay`, `resource_chiller`, `ginger`, `pear`, `resource_heater`, `sultana`, `genre_pop_rock`, `cloves`, `sun` |
| n7 | object | t1:s7 | sports (soccer, ice hockey, volleyball, cricket, squash, table tennis) | `table`*, `format_table`, `cat_game`, `topic_greatest_cricketer_of_all_time`, `rank_distance`, `ukraine`, `russia`, `meat`, `rank_field`, `africa`, `apple`, `coffee_maker` |
| n8 | object | t1:s8 | NBA teams (Bulls, Lakers, Hawks, Bucks, Knicks, Mavericks) | `rank_distance`, `role_support_team`, `format_bullet_list`, `rank_field`, `meat`, `rank_direction`, `entity_mains`, `coffee_maker`, `cuisine`, `resource_heater`, `entity_menu_items`, `restaurant` |
| n9 | object | t1:s9 | hobbies (beekeeping, wood carving, biking, origami, video games, canoeing) | `cat_game`, `example_a_select_two_pillows_and_move_those_objects`, `topic_greatest_cricketer_of_all_time`, `coffee_maker`, `art_story`, `style_catchy`, `art_plan`, `resource_heater`, `tattoos`, `chair`, `resource_chiller`, `oak_chips` |
| n10 | object | t1:s10 | animals (crabs, elk, dugongs, blobfish, cats, finches) → `animal_label::<key>` | `animal_label`*, `dog`, `cat_game`, `meat`, `cat_limited_time_offers`, `char_female`, `rank_distance`, `style_catchy`, `rank_field`, `sort`, `caddy`, `earth` |
| n11 | object | t1:s11 | nationalities (Japanese, Serbian, Swede, Russian, Pakistani, Italian) → `country::<key>` | `cuisine_italian`*, `japanese_government`, `country`*, `locale_zh`, `foreigners`, `ukraine`, `russia`, `tattooed_guests`, `united_kingdom`, `africa`, `locale_en_gb`, `locale_en_us` |
| n12 | object | t1:s12 | fruits (mangoes, oranges, raspberries, grapes, pears, bananas) → `food_label::<key>` | `pear`*, `wine_grape`*, `fruit_juice`, `dried_fruit`, `apple`, `grape_must`, `grape_thompson_seedless`, `grape_chardonnay`, `grape_merlot`, `wine`, `grape_pinot_noir`, `color_pink` |
| n13 | object | t1:s13 | motorbikes (Bajaj, Buell, Kawasaki, Piaggio, Benelli, Yamaha) | `driver_license`, `vehicle_allowance`, `grape_sauvignon_blanc`, `cuisine_pizza`, `shape_triangular`, `shape_round`, `coffee_maker`, `grape_merlot`, `resource_chiller`, `grape_cabernet_sauvignon`, `resource_heater`, `chair` |
| n14 | object | t1:s14 | cigarettes (Blends, Marlboro, Blue Master, Salem, Newport, Davidoff) | `coffee_maker`, `rank_distance`, `grape_merlot`, `rank_price`, `grape_thompson_seedless`, `resource_heater`, `resource_chiller`, `format_numbered_list`, `dir_desc`, `color_label`, `grape_pinot_noir`, `wine_grape` |
| n15 | object | t1:s15 | physical activities (base jumping, scuba diving, weight lifting, biking, hiking, bungee jumping) | `activity`*, `rank_distance`, `unit_item`, `on`, `event_camper_in_sludge_pit`, `resource_chiller`, `resource_heater`, `laptop`, `class_beach`, `cd`, `walk_backward`, `resource_sink` |
| n16 | object | t1:s16 | handbag brands (Polo Ralph Lauren, Gucci, Coach, Versace, Tory Burch, Tumi) | `style_catchy`, `gender_women`, `clothing`, `dresser`, `valet`, `mittens`, `tattooed_guests`, `coffee_maker`, `resource_chiller`, `resource_heater`, `tattoos`, `resource_sink` |
| n17 | object | t1:s17 | soft drinks (Powerade, Canada Dry, 7up, Mountain Dew, Pepsi, Coke) | `mug`, `entity_drinks`, `martini_glass`, `bottle`, `fruit_juice`, `wine`, `coffee_maker`, `grape_pinot_noir`, `dried_fruit`, `resource_heater`, `grape_thompson_seedless`, `resource_sink` |
| n18 | object | t1:s18 | names (Jones, Nour, Charlie, Margaret, Rafael, Drew) | `format_numbered_list`, `rank_direction`, `grape_thompson_seedless`, `char_female`, `rank_field`, `coffee_maker`, `resource_heater`, `resource_sink`, `resource_chiller`, `dog`, `sort`, `chair` |
| n19 | constraint | t1:s19 | use the provided clues to solve the puzzle, ignoring irrelevant ones | `extract`, `rule_category_constraint_value`, `constraint_include_character_attribute_list`, `in_front_of`, `topic_baldurs_gate_3`, `constraint_beginner`, `constraint_exclude_flowery_language`, `entity_flowers`, `constraint_budget_limited`, `constraint_single_choice`, `constraint_respectful`, `subject` |
| n20 | action | t1:s151 | determine the position of the person who likes biking | `stand_up`, `behind`, `rank_direction`, `rank_distance`, `bionic_person`, `decision`, `walk_backward`, `walk`, `character_trait`, `rank_rating`, `dir_desc`, `turn` |

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
- subject.qualifier → platform_label
- subject.location → country
- walk.destination → object_label
- requirement.value → platform_label
- pick_up.target → object_label, food_label
- pick_up.source → object_label
- pick_up.color → color_label
- place.destination → object_label
- place.location → object_label
- failure.system → platform_label

## Retrieved records

### Shared rules that govern the records below (full text)

**rule_lexical_groups** (v19/rule/lexical-groups; rule governing platform_label)

Section 3.1 defines value groups: `group::key` values of type ATOM[group]. Open groups admit any key of their form (examples are not whitelists); standard groups admit the codes of their bundled standard (ISO 3166-1 alpha-2 for country, ISO 4217 for currency). Leaf values are never glossary entries. Consumer signatures alone decide where a group may appear. Retired bare symbols are invalid.

**rule_reading_guide** (v19/rule/reading-guide; core)

The spec governs syntax/types; this glossary defines vocabulary. Signature notation: ? optional, A / B explicit alternatives, void no result. Omitted optional arguments are unspecified. Value entries are category-refined STRING primitives; complex meanings require composition. Aliases are contextual hints, not unconditional equivalences. Report ambiguity. IDs use v19/<category>/<symbol>, v19/support/<symbol> or v19/composite/<symbol>. Statuses apply to this candidate: Retained preserves meaning; Adapted uses the stated contract; Composite requires TERM (bare STRING deprecated); Structural is syntax/argument vocabulary; Needs clarification is unusable until resolved; Deprecated is historical; Accepted is usable within this candidate.

**rule_recording_signatures** (v19/rule/recording-signatures; rule governing sort)

RECORD ACTION uses the operation signature with REF[STRING] → TERM and LIST[REF[STRING]] → LIST[TERM]; other types/categories stay unchanged. Return EVENT, never the runtime result. Record actual outputs as attributed CLAIMs. Do not infer missing resources.

**rule_speech_acts_general** (v19/rule/speech-acts-general; rule governing respond)

UTTER-only, void, with the spec's speech attributes and LIST[TERM] constraints. No result binding. Literal content cannot replace required semantic arguments for structured coverage.

**rule_structural_constructs** (v19/rule/structural-constructs; core)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; core)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_attributes_and_generate** (v19/rule/attributes-and-generate; rule governing art_character_profile)

Attribute entries name arguments; legality/types come from each operation, not global membership. GENERATE uses the spec's core fields; retained artifact profiles return STRING. Numeric/list results need explicit profiles. Legacy itinerary fields expand to TERM constraints: duration/duration_unit → duration(amount,unit); stop_min_per_day/stop_requirement → minimum_per_period(class,count,period=unit_day), never an inferred temple class; max_walk_duration/unit → maximum_between_stops(activity="walk",amount,unit). No legacy shorthand is enabled. Old events/character_properties/transformations become explicitly scoped TERM constraints. Message purpose is TERM, not send_email.content: GENERATE exact STRING content, then send. Report opaque fallback separately.

**rule_category_artifact_value** (v19/rule/category/artifact-value; rule governing art_character_profile)

STRING artifact class for GENERATE.target. art_story says what kind of artifact to produce, not what occurs in its plot.

**rule_category_character_property_value** (v19/rule/category/character-property-value; rule governing char_female)

TERM-described trait/style. Use constraints and explicit inclusion/scope; do not use an ungoverned character_properties attribute.

**rule_category_constraint_value** (v19/rule/category/constraint-value; candidate)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_cuisine_value** (v19/rule/category/cuisine-value; rule governing cuisine_pizza)

STRING cuisine class; cuisine_indian is a cuisine filter, not the location India.

**rule_category_descriptive_value** (v19/rule/category/descriptive-value; rule governing beliefs)

STRING modifier/domain label; never a free-form proposition. dom_sgi needs its intended referent established before semantically dependent use.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; rule governing unit_item)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing lamp)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_event_value** (v19/rule/category/event-value; rule governing event_camper_in_sludge_pit)

TERM-described narrative event, not a recorded EVENT. Require inclusion explicitly when generating a story.

**rule_category_format_value** (v19/rule/category/format-value; rule governing format_numbered_list)

STRING format. format_email is layout, not the action send_email.

**rule_category_locale_value** (v19/rule/category/locale-value; rule governing locale_zh)

STRING locale. “English” alone does not always mean locale_en_us; preserve ambiguity.

**rule_category_location_name** (v19/rule/category/location-name; rule governing living_room)

STRING location descriptor. A `table` surface is not the generated artifact category art_table.

**rule_category_product_attribute_value** (v19/rule/category/product-attribute-value; rule governing color_pink)

STRING color/size/product-market facets. gender_women describes a product category, not an assertion about a person's gender.

**rule_category_recipient_value** (v19/rule/category/recipient-value; rule governing role_support_team)

STRING roles or explicit named recipients. A role is not an exact person's identity. Keep an explicit name where substituting a role loses information.

**rule_category_search_value** (v19/rule/category/search-value; candidate)

STRING refinements rank_ / dir_ / cat_ / avail_ / genre_ are separate. rank_rating may fill rank_field; genre_label::comedy may not. “Cheapest” usually requires both rank_price and dir_asc, not rank_price alone.

**rule_category_semantic_category_value** (v19/rule/category/semantic-category-value; rule governing class_beach)

STRING class label used by typed constraints. class_temple describes a class, not an acquired physical temple reference.

**rule_category_shape_value** (v19/rule/category/shape-value; rule governing shape_triangular)

STRING geometry. shape_round may select a circular object; it does not imply color or dimensions.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing on)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_style_value** (v19/rule/category/style-value; rule governing style_academic)

STRING production style. style_narrative does not establish that described events occurred.

**rule_category_tone_value** (v19/rule/category/tone-value; rule governing tone_professional)

STRING register. tone_urgent describes urgency, not a concrete deadline.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_current_events)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_composites_general** (v19/rule/composites-general; rule governing topic_greatest_cricketer_of_all_time)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_examples_general** (v19/rule/examples-general; rule governing example_a_select_two_pillows_and_move_those_objects)

Examples use this glossary's contracts. They have not been verified by an implemented BrainCode parser.

**rule_operations_general** (v19/rule/operations-general; rule governing sort)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_search_web_attributes** (v19/rule/search-web-attributes; rule governing sort)

Optional filters: availability, category, color, cuisine, currency, gender, genre, location, platform, ram_unit, reservation_availability, shape, size (category-refined STRING); max_price, min_ram, min_rating (NUMBER); trending (BOOL). Explicit signature alternatives additionally admit atoms. Price requires currency; RAM requires a capacity unit; no default scale/source. rank is invalid: use sort, whose rank_field accepts rank_* and rank_direction accepts dir_*. Category/genre/availability accept only their own subfamilies.

**rule_supplemental_general** (v19/rule/supplemental-general; rule governing extract)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; rule governing calculation)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- extract | operation | operation-vocabulary | (target: LIST[REF[STRING]], limit: NUMBER) -> LIST[REF[STRING]] | First limit results, preserving order and identity; limit is a nonnegative integer; limit=1 is still a list  ⟵ candidate
- pick_up | operation | operation-vocabulary | (target: STRING / ATOM[object_label] / ATOM[food_label], quantity?: NUMBER, source?: STRING / ATOM[object_label], color?: STRING / ATOM[color_label], shape?: STRING, state?: STRING) -> REF[STRING] or LIST[REF[STRING]] | Select/acquire objects. Missing quantity or literal 1 returns REF; integer literal greater than 1 returns LIST[REF]. Other values are invalid for this profile. | aliases: grab, take, retrieve  ⟵ dependency of example_a_select_two_pillows_and_move_those_objects
- place | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label], location?: STRING / ATOM[object_label], relation?: STRING) -> void | Place an already acquired object. Spatial relation must be explicit if the source distinguishes it. | aliases: put, insert  ⟵ dependency of example_a_select_two_pillows_and_move_those_objects
- slice | operation | operation-vocabulary | (target: REF[STRING] / TERM) -> REF[STRING] | Slice the selected material or described term, preserving its tracked aggregate identity. | aliases: chop, cut  ⟵ candidate
- sort | operation | operation-vocabulary | (target: LIST[REF[STRING]], rank_direction: STRING, rank_field: STRING) -> LIST[REF[STRING]] | Request ordering of selected results. Preserve member identity; this is not a claim that order was observed. | aliases: rank, order by  ⟵ candidate
- stand_up | operation | operation-vocabulary | () -> void | Return agent posture to standard upright standing position. agent must be in a non-standing posture. | aliases: stand  ⟵ candidate
- turn | operation | operation-vocabulary | (direction: STRING) -> void | Rotate agent body/view orientation. direction is typically left, right, or angle. | aliases: rotate, turn_around  ⟵ candidate
- walk | operation | operation-vocabulary | (destination: STRING / TERM / ATOM[object_label], relation?: STRING) -> void | Locomote towards a target destination or landmark. destination must identify a valid entity or location. | aliases: move_to, go_to, navigate_to  ⟵ candidate
- walk_backward | operation | operation-vocabulary | (modifier?: STRING) -> void | Walk backward. Optional modifier can specify the degree or minor distance of movement. | not: walk (which moves forward toward a destination) | aliases: move backward, step back  ⟵ candidate

### speech acts

- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ candidate
- bionic_person | constructor | TERM bionic_person(composition?: STRING / TERM) -> TERM | Constructs a descriptive representation of a bionic person or cyborg entity with biological and mechanical components. | not: a standard human role (use role_user or role_adults) or a purely artificial device. | aliases: bionic person, bionic people, cyborg, half human half robot  ⟵ candidate
- calculation | constructor | TERM calculation(inputs: LIST[TERM], operation: STRING, result?: TERM) -> TERM | Constructs a descriptive representation of an arithmetic or algorithmic calculation step with inputs, operation identifier, and optional resulting value. | not: an executed runtime action or factual claim of outcome | aliases: math_operation, compute_step  ⟵ candidate
- character_trait | constructor | TERM character_trait(property: STRING, value: STRING / NUMBER) -> TERM | A character attribute | not: Not a claim about a real person  ⟵ candidate
- conditional | constructor | TERM conditional(condition: TERM, consequence: TERM) -> TERM | Constructs a structured conditional proposition term connecting a condition and consequence. descriptive logic structure. | aliases: if_then  ⟵ candidate
- conjunction | constructor | TERM conjunction(items: LIST[TERM]) -> TERM | All described components apply | not: Does not imply temporal order  ⟵ candidate
- decision | constructor | TERM decision(activity: TERM) -> TERM | A decision whose content is the described activity | not: Not proof it was carried out  ⟵ candidate
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ dependency of constraint_exclude_flowery_language
- include | constructor | TERM include(item: STRING / TERM) -> TERM | Require the identified content/item | not: Not permission to invent an instance in a recorded trace  ⟵ dependency of constraint_include_character_attribute_list
- preserve | constructor | TERM preserve(component: STRING, index: NUMBER) -> TERM | Keep the indexed component unchanged, using one-based indexing | not: Not preserve all components  ⟵ candidate
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ dependency of topic_greatest_cricketer_of_all_time
- sequence | constructor | TERM sequence(items: LIST[TERM]) -> TERM | Ordered described activities/content | not: Not unordered conjunction  ⟵ candidate
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ candidate
- vehicle_allowance | constructor | TERM vehicle_allowance(roles: STRING, types: LIST[STRING]) -> TERM | Constructs a specification of permitted vehicle types for defined employee roles. specifies vehicle permissions. | aliases: vehicle_permission  ⟵ candidate

### composites

- char_female | composite | character-property-value | TERM char_female() -> TERM | Female gender. | = character_trait(property="gender", value="female") | aliases: female  ⟵ candidate
- constraint_beginner | composite | constraint-value | TERM constraint_beginner() -> TERM | Targeted at beginners. | = requirement(property="audience_expertise", value="beginner")  ⟵ candidate
- constraint_budget_limited | composite | constraint-value | TERM constraint_budget_limited() -> TERM | Limited budget. | = requirement(property="budget_limited", value=TRUE)  ⟵ candidate
- constraint_exclude_flowery_language | composite | constraint-value | TERM constraint_exclude_flowery_language() -> TERM | Avoid flowery language. | = exclude(item="flowery_language")  ⟵ candidate
- constraint_include_character_attribute_list | composite | constraint-value | TERM constraint_include_character_attribute_list() -> TERM | Include character attributes. | = include(item="character_attribute_list")  ⟵ candidate
- constraint_respectful | composite | constraint-value | TERM constraint_respectful() -> TERM | Must be respectful. | = requirement(property="respectful", value=TRUE)  ⟵ candidate
- constraint_single_choice | composite | constraint-value | TERM constraint_single_choice() -> TERM | Must pick a single choice. | = requirement(property="choice_count", value=1)  ⟵ candidate
- event_camper_in_sludge_pit | composite | event-value | TERM event_camper_in_sludge_pit() -> TERM | Campers interacting in a sludge pit. | = activity(verb="interact", actor="campers", location="sludge_pit")  ⟵ candidate
- topic_greatest_cricketer_of_all_time | composite | topic-value | TERM topic_greatest_cricketer_of_all_time() -> TERM | Greatest cricketer of all time. | = subject(kind="cricketer", qualifier=requirement(property="rank_by_greatness", value=1), time="all_time")  ⟵ candidate

### claim relations

- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ core
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ core

### links

- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ core
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ core
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ core

### values

- art_character_profile | value | artifact-value | Descriptive character profile.  ⟵ candidate
- art_plan | value | artifact-value | Actionable plan.  ⟵ candidate
- art_short_text | value | artifact-value | Short free text.  ⟵ candidate
- art_story | value | artifact-value | Narrative story.  ⟵ candidate
- cuisine_italian | value | cuisine-value | Italian cuisine. | aliases: Italian food, Italian  ⟵ candidate
- cuisine_pizza | value | cuisine-value | Pizza culinary cuisine style and food category. | not: cuisine_italian (broader regional/national cuisine) | aliases: pizza, pizzeria, pizza cuisine  ⟵ candidate
- beliefs | value | descriptive-value | Concept of cognitive beliefs, convictions, or worldviews. | aliases: beliefs  ⟵ candidate
- tattoos | value | descriptive-value | Descriptive concept of tattoos in cultural and social contexts. | aliases: tattoos  ⟵ candidate
- unit_item | value | duration-unit-value | Top-level generated list or report item. | aliases: items, entries  ⟵ candidate
- apple | value | entity-name | An apple fruit item, typically an ingredient or interactive food object. | not: food_label::tomato or other fruits/vegetables | aliases: apple, apples, red apple, green apple, apple slice  ⟵ candidate
- bottle | value | entity-name | A bottle container object, typically used for holding liquids. | not: mug (a drinking cup with a handle) or water (the liquid itself) | aliases: bottle, water bottle, plastic bottle  ⟵ candidate
- caddy | value | entity-name | A portable storage caddy, organizer box, or supply tote for carrying and organizing handheld tools and supplies. | not: cabinet (a stationary furniture cupboard) or safe (a secure metal lockbox) | aliases: caddy, supply caddy, wrapping caddy, tool caddy, organizer caddy, supply tote  ⟵ candidate
- cd | value | entity-name | A compact disc physical object. | not: a digital media file or streaming track | aliases: CD, compact_disc  ⟵ candidate
- chair | value | entity-name | A chair furniture seat with a backrest. | not: object_label::armchair (specifically an object_label::armchair with side armrests) or object_label::sofa | aliases: chair, seat  ⟵ candidate
- clothing | value | entity-name | Physical item used for concealment or covering: clothing. | aliases: clothing  ⟵ candidate
- cloves | value | entity-name | Aromatic dried flower buds of Syzygium aromaticum used as a culinary spice. | not: cinnamon, nutmeg, or other distinct spice varieties | aliases: cloves, clove, ground cloves, whole cloves  ⟵ candidate
- coffee_maker | value | entity-name | A coffee-making appliance; not automatically a heating resource  ⟵ candidate
- dog | value | entity-name | Animal entity: dog. | not: animal_label::cat or animal_label::donkey | aliases: dog, dogs, canine, pup, puppy  ⟵ candidate
- dresser | value | entity-name | A chest of drawers / dresser furniture. | aliases: dresser  ⟵ candidate
- dried_fruit | value | entity-name | Generic dried fruit food item. | not: fresh fruit or specific dried varieties like raisin or sultana | aliases: dried fruit, dried fruits  ⟵ candidate
- driver_license | value | entity-name | An official government credential or authorization permitting an individual to operate motor vehicles. | not: vehicle_allowance (an employee vehicle policy) or rental_vehicle (a rental vehicle) | aliases: driver license, driver's license, driving license, driver licence, driver ID  ⟵ candidate
- earth | value | entity-name | The planet Earth as an astronomical celestial body. | not: soil, ground surface, or electrical grounding | aliases: earth, the earth, planet earth, Earth  ⟵ candidate
- entity_drinks | value | entity-name | Event planning item or menu category: entity_drinks. | aliases: entity_drinks  ⟵ candidate
- entity_flowers | value | entity-name | Flowers, blossoms, or floral design elements. | not: constraint_exclude_flowery_language (a prose style constraint) or agricultural food items | aliases: flowers, floral, flower, floral decorations  ⟵ candidate
- entity_mains | value | entity-name | Event planning item or menu category: entity_mains. | aliases: entity_mains  ⟵ candidate
- entity_menu_items | value | entity-name | Event planning item or menu category: entity_menu_items. | aliases: entity_menu_items  ⟵ candidate
- fruit_juice | value | entity-name | Liquid juice extracted from fruit. | not: fermented wine or freshly crushed grape_must | aliases: fruit juice, juice  ⟵ candidate
- ginger | value | entity-name | Pungent aromatic spice root from Zingiber officinale used in cooking and baking. | not: cinnamon, cardamom, or other distinct spice varieties | aliases: ginger, ground ginger, fresh ginger, ginger root  ⟵ candidate
- grape_cabernet_sauvignon | value | entity-name | Cabernet Sauvignon wine grape variety. | not: other red grape varieties such as grape_merlot or grape_pinot_noir | aliases: Cabernet Sauvignon, cabernet, cabernet sauvignon grape  ⟵ candidate
- grape_chardonnay | value | entity-name | Chardonnay wine grape variety. | not: other white grape varieties such as grape_sauvignon_blanc | aliases: Chardonnay, chardonnay grape  ⟵ candidate
- grape_merlot | value | entity-name | Merlot wine grape variety. | not: other red grape varieties such as grape_cabernet_sauvignon or grape_pinot_noir | aliases: Merlot, merlot grape  ⟵ candidate
- grape_must | value | entity-name | Freshly crushed fruit juice mixture before fermentation. | not: clarified fruit_juice or finished wine | aliases: grape must, must  ⟵ candidate
- grape_pinot_noir | value | entity-name | Pinot Noir wine grape variety. | not: other red grape varieties such as grape_cabernet_sauvignon or grape_merlot | aliases: Pinot Noir, pinot noir grape  ⟵ candidate
- grape_sauvignon_blanc | value | entity-name | Sauvignon Blanc wine grape variety. | not: other white grape varieties such as grape_chardonnay | aliases: Sauvignon Blanc, sauvignon blanc grape  ⟵ candidate
- grape_thompson_seedless | value | entity-name | Thompson Seedless grape variety. | not: wine grape cultivars like grape_merlot or grape_chardonnay | aliases: Thompson Seedless, thompson seedless grape, sultana grape  ⟵ candidate
- keys | value | entity-name | A physical key or set of keys / keychain object. | not: press_key (a UI keyboard key press operation) | aliases: keys, key, key chain, keychain  ⟵ candidate
- lamp | value | entity-name | A lamp light source appliance. | not: an abstract lighting concept or ambient color | aliases: light, desk_lamp  ⟵ candidate
- laptop | value | entity-name | A portable laptop computer physical object. | not: topic_macbook_pro_2017 (a generation topic label) | aliases: laptop, laptop computer, notebook  ⟵ candidate
- martini_glass | value | entity-name | A cocktail or Martini drinking glass object. | not: mug (a drinking cup with a handle) or bottle (liquid storage container) | aliases: martini glass, cocktail glass, glass  ⟵ candidate
- meat | value | entity-name | Food item: meat or beef. | not: animal_label::tuna or animal_label::fish (specific aquatic foods) | aliases: meat, beef  ⟵ candidate
- mittens | value | entity-name | Item or prop in joke/creative context: mittens. | aliases: mittens  ⟵ candidate
- mug | value | entity-name | Drinking cup. | aliases: mug  ⟵ candidate
- oak_chips | value | entity-name | Oak wood pieces or barrels used for wine aging and flavor extraction. | not: grape_tannin or structural chemical additives | aliases: oak chips, oak pieces, oak barrels  ⟵ candidate
- pear | value | entity-name | A pear fruit item, typically an ingredient or fresh fruit object. | not: apple, food_label::tomato, or other distinct fruit items | aliases: pear, pears, fresh pear, sliced pear  ⟵ candidate
- raisin | value | entity-name | Dried grape food item. | not: sultana (specifically dried white grape) or fresh wine_grape | aliases: raisin, raisins, dried grape  ⟵ candidate
- resource_chiller | value | entity-name | Canonical abstract chilling resource when no particular appliance is named.  ⟵ candidate
- resource_heater | value | entity-name | Canonical abstract heating resource when no particular appliance is named.  ⟵ candidate
- resource_sink | value | entity-name | Canonical abstract washing resource when no particular sink is named.  ⟵ candidate
- restaurant | value | entity-name | A commercial restaurant, eatery, or dining establishment where meals are prepared and served. | not: ryokan or onsen (specific traditional hospitality establishments) | aliases: restaurant, eatery, dining establishment, restaurants  ⟵ candidate
- stove | value | entity-name | A kitchen stove / range appliance for cooking or heating. | not: microwave | aliases: stove, range, cooktop  ⟵ candidate
- sultana | value | entity-name | Dried white seedless grape food product. | not: raisin (dark dried grape) or wine_grape | aliases: sultana, sultanas, golden raisin  ⟵ candidate
- sun | value | entity-name | The central star of the Solar System. | not: an artificial lighting appliance or sunlight | aliases: sun, the sun, Sol  ⟵ candidate
- textbook | value | entity-name | A textbook or instructional book used as an educational resource. | not: style_academic (which is a stylistic mode) or art_short_text (which is a brief generated text artifact) | aliases: textbook, book, coursebook, textbooks  ⟵ candidate
- wine | value | entity-name | Fermented fruit or grape beverage. | not: unfermented fruit juice or distilled alcohol/spirits | aliases: wine, wines  ⟵ candidate
- wine_grape | value | entity-name | Grape variety cultivated specifically for winemaking. | not: table grapes or processed wine product | aliases: wine grape, wine grapes, grape  ⟵ candidate
- format_bullet_list | value | format-value | Bulleted list. | aliases: bullet points  ⟵ candidate
- format_numbered_list | value | format-value | Numbered list. | aliases: numbered steps  ⟵ candidate
- format_table | value | format-value | Tabular layout. | aliases: as a table  ⟵ candidate
- locale_en_gb | value | locale-value | UK English. | aliases: british english  ⟵ candidate
- locale_en_us | value | locale-value | US English. | aliases: english, en-us  ⟵ candidate
- locale_hi_en | value | locale-value | Hinglish (Hindi-English mix). | aliases: hinglish  ⟵ candidate
- locale_zh | value | locale-value | Chinese language locale (Simplified and Traditional Chinese). | not: a specific geographical region or nationality (use location-name) | aliases: chinese, zh, zh-cn, zh-tw, mandarin  ⟵ candidate
- africa | value | location-name | Geopolitical nation or continental region: africa. | aliases: africa  ⟵ candidate
- living_room | value | location-name | A residential room or general indoor living area. | not: floor (a floor surface) or wall (a vertical boundary surface) | aliases: living room, living_room, sitting room, lounge  ⟵ candidate
- new_york_university | value | location-name | New York University institution or campus grounds. | aliases: nyu  ⟵ candidate
- russia | value | location-name | Geopolitical nation or continental region: russia. | aliases: russia  ⟵ candidate
- table | value | location-name | A table surface.  ⟵ candidate
- ukraine | value | location-name | Geopolitical nation or continental region: ukraine. | aliases: ukraine  ⟵ candidate
- united_kingdom | value | location-name | Geopolitical nation or sovereign state: United Kingdom (Great Britain). | not: locale_en_gb (a language/locale code, not a location) | aliases: United Kingdom, UK, Great Britain, Britain  ⟵ candidate
- wall | value | location-name | A room boundary wall surface. | aliases: wall  ⟵ candidate
- color_pink | value | product-attribute-value | Pink visual color qualifier. | not: color_label::red, color_label::purple, or other distinct color shades | aliases: pink, color_pink, blush pink, rose pink, pastel pink  ⟵ candidate
- gender_men | value | product-attribute-value | Men's/male-targeted. | aliases: men, male  ⟵ candidate
- gender_women | value | product-attribute-value | Women's/female-targeted. | aliases: women, female  ⟵ candidate
- valet | value | product-attribute-value | Valet parking or dedicated vehicle attendant service. | aliases: valet_parking  ⟵ candidate
- foreigners | value | recipient-value | Social, demographic, or institutional group: foreigners. | aliases: foreigners  ⟵ candidate
- japanese_government | value | recipient-value | Social, demographic, or institutional group: japanese_government. | aliases: japanese_government  ⟵ candidate
- role_adults | value | recipient-value | Adult participant group in family, event, or travel context. | not: role_kids (children participant group) or role_user (the specific conversational user) | aliases: adults, adult, grown-ups  ⟵ candidate
- role_agent | value | recipient-value | The assistant. | aliases: you, the assistant  ⟵ candidate
- role_colleague | value | recipient-value | A coworker of the user. | aliases: my colleague, coworker  ⟵ candidate
- role_respondent | value | recipient-value | A respondent, survey participant, or interviewee providing primary research data. | not: role_customer (the user's client) or role_user (the conversational user) | aliases: respondent, respondents, survey respondent, study participant  ⟵ candidate
- role_support_team | value | recipient-value | A customer-support team. | aliases: support, customer service  ⟵ candidate
- role_user | value | recipient-value | The requesting human. | aliases: me, I  ⟵ candidate
- tattooed_guests | value | recipient-value | Social, demographic, or institutional group: tattooed_guests. | aliases: tattooed_guests  ⟵ candidate
- cat_game | value | search-value | Category: video game.  ⟵ candidate
- cat_limited_time_offers | value | search-value | Category: time-limited deals.  ⟵ candidate
- dir_desc | value | search-value | Descending rank direction. | aliases: highest first  ⟵ candidate
- genre_electronic | value | search-value | Music genre refinement: electronic music. | not: genre_pop_rock or general style descriptors | aliases: electronic, electronic music, EDM  ⟵ candidate
- genre_pop_rock | value | search-value | Music genre: pop rock. | not: genre_label::comedy or general tone descriptors | aliases: pop rock, pop-rock, pop/rock  ⟵ candidate
- rank_distance | value | search-value | Rank field: proximity. | aliases: nearest, closest  ⟵ candidate
- rank_price | value | search-value | Rank or filter field: monetary cost. | aliases: cheapest, lowest price  ⟵ candidate
- rank_rating | value | search-value | Rank or filter field: user or critic score.  ⟵ candidate
- class_beach | value | semantic-category-value | The abstract class or category of beach destinations and coastal environments. | not: island (kitchen island work surface) or a specific named beach location | aliases: beach, beaches, beach destination, seaside  ⟵ candidate
- shape_round | value | shape-value | Circular/round. | aliases: round, circular  ⟵ candidate
- shape_triangular | value | shape-value | Triangular. | aliases: triangular, triangle  ⟵ candidate
- behind | value | spatial-relation | Positioned behind.  ⟵ candidate
- in_front_of | value | spatial-relation | Positioned in front of. | aliases: in front of  ⟵ candidate
- on | value | spatial-relation | Resting atop. | aliases: on top of  ⟵ candidate
- style_academic | value | style-value | Academic style. | aliases: academic  ⟵ candidate
- style_catchy | value | style-value | Catchy, attention-grabbing style. | aliases: catchy  ⟵ candidate
- style_narrative | value | style-value | Story-like narrative style. | aliases: narrative, story-style  ⟵ candidate
- tone_professional | value | tone-value | Workplace-appropriate register. | aliases: professionally  ⟵ candidate
- topic_baldurs_gate_3 | value | topic-value | Baldur's Gate 3.  ⟵ candidate
- topic_current_events | value | topic-value | Current news, geopolitical events, and ongoing international developments. | aliases: current_events, news  ⟵ candidate
- topic_jazz_piano | value | topic-value | Jazz piano.  ⟵ candidate
- topic_politics | value | topic-value | Politics.  ⟵ candidate

### attributes

- cuisine | attribute | attribute-name | Restaurant or food cuisine from cuisine-value.  ⟵ candidate
- rank_direction | attribute | attribute-name | Sort direction from search-value.  ⟵ candidate
- rank_field | attribute | attribute-name | Field used by sort from search-value.  ⟵ candidate

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

