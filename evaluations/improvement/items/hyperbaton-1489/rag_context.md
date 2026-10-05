# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 19 needs (decomposition: llm), 171 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | claim | t1:s1 | A variant of English has a specific correct adjective order. | `locale_en_us`*, `locale_en_gb`, `metric_order_late`, `sort`, `correct`*, `style_catchy`, `rule_category_locale_value`, `has_style`, `right_of`, `considered`, `enables`, `tone_polite` |
| n2 | object | t1:s2, t1:s3, t1:s4, t1:s5, t1:s6, t1:s7, t1:s8, t1:s9 | A list of 137 example sentences demonstrating correct adjective order. | `unit_sentence`*, `entity_order_vs_assemble_plan`, `sort`, `correct`*, `topic_pickup_lines`, `style_catchy`, `format_numbered_list`, `sequence`, `metric_order_late`, `unit_paragraph`, `in_front_of`, `entity_condensed_grocery_list` |
| n3 | action | t1:s10 | Determine which of the given options use the correct adjective order. | `sort`, `select_option`, `add_to_cart`, `entity_order_vs_assemble_plan`, `correct`*, `metric_order_late`, `decision`, `style_catchy`, `ask`, `constraint_single_choice`, `search_travel`, `search_web` |
| n4 | negation | t1:s11 | None of the sentences (Options A-J) use the correct adjective order. | `unit_sentence`*, `correct`*, `constraint_exclude_flowery_language`, `entity_order_vs_assemble_plan`, `sort`, `ask`, `respond`, `style_catchy`, `topic_pickup_lines`, `in_front_of`, `rule_category_topic_value`, `metric_order_late` |
| n5 | action | t1:s11 | Select option K. | `select_option`*, `add_to_cart`, `sort`, `search_travel`, `search_transit`, `click`, `select_filter`, `slice`, `pour`, `constraint_single_choice`, `search_web`, `extract` |
| n6 | constraint | t1:s12 | Select all options that apply. | `constraint_single_choice`, `select_option`, `constraint_comprehensive`, `search_travel`, `constraint_exclude_flowery_language`, `constraint_budget_limited`, `constraint_respectful`, `entity_flowers`, `propose_menu`, `add_to_cart`, `constraint_realistic`, `constraint_beginner` |
| n7 | object | t1:s13 | Option A: filipino drinking glass indigo enormous rectangular old-fashioned flower pot | `martini_glass`*, `mug`, `vase`, `entity_flowers`*, `bottle`, `shape_rectangular`*, `pan`*, `wine`, `grape_pinot_noir`, `entity_drinks`, `sultana`, `bowl` |
| n8 | object | t1:s14 | Option B: german driving cardboard yellow normal-size prismlike brand-new lovely shoe | `locale_de`*, `cardboard_box`, `size_medium`, `size_small`, `topic_current_events`*, `mittens`, `dresser`, `piano`, `topic_classical_piano`, `clothing`, `size_large`, `size_queen` |
| n9 | object | t1:s15 | Option C: old wood aqua massive rectangular snorkeling pakistani sofa | `shape_rectangular`*, `chair`, `example_a_select_two_pillows_and_move_those_objects`, `mattress`, `piano`, `material_memory_foam`, `night_stand`, `bed`, `waterproof_bandages`, `desk`, `scissors`, `tissue_box` |
| n10 | object | t1:s16 | Option D: repulsive new wool maroon large rectangular shirt | `size_large`*, `shape_rectangular`*, `topic_current_events`*, `yarn`, `clothing`, `dresser`, `size_medium`, `color_pink`, `size_small`, `mittens`, `bowtie`, `cheese` |
| n11 | object | t1:s17 | Option E: indian exercise iron yellow massive square hammer | `cuisine_indian`*, `shape_square`*, `resource_heater`, `art_plan`, `unit_item`, `art_structured_report`, `size_large`, `spatula`, `art_technical_explanation`, `shape_oval`, `size_medium`, `shape_round` |
| n12 | object | t1:s18 | Option F: old-fashioned awful cloth cyan small circular drinking iranian screwdriver | `clothing`*, `mug`, `martini_glass`, `bottle`, `size_small`*, `shape_round`*, `scissors`, `dresser`, `entity_drinks`, `spatula`, `vase`, `spoon` |
| n13 | object | t1:s19 | Option G: cloth teal little prismlike wonderful ancient scissors | `scissors`*, `clothing`*, `yarn`, `vase`, `dresser`, `martini_glass`, `art_short_text`, `grape_pinot_noir`, `tape`, `knife`, `chair`, `aesthetic` |
| n14 | object | t1:s20 | Option H: american snorkeling glass cyan massive spherical mysterious shoe | `martini_glass`*, `chair`, `mittens`, `cardboard_box`, `grape_pinot_noir`, `dresser`, `mug`, `scissors`, `bottle`, `tissue_box`, `waterproof_bandages`, `figurine` |
| n15 | object | t1:s21 | Option I: exercise iron aqua enormous spherical ridiculous old-fashioned flower pot | `entity_flowers`*, `vase`, `pan`*, `cloves`, `art_plan`, `bowl`, `shape_triangular`, `shape_oval`, `spatula`, `shape_round`, `shape_square`, `cardamom` |
| n16 | object | t1:s22 | Option J: hiking fiberglass yellow tiny pyramidal old-fashioned repulsive bag | `dresser`, `clothing`, `bottle`, `art_itinerary`, `cardboard_box`, `art_short_text`, `art_plan`, `example_a_select_two_pillows_and_move_those_objects`, `bowl`, `chair`, `waterproof_bandages`, `trash_can` |
| n17 | object | t1:s23 | Option K: None of the above | `select_option`, `constraint_exclude_flowery_language`, `format_numbered_list`, `next_to`, `chair`, `add_to_cart`, `grape_thompson_seedless`, `example_a_select_two_pillows_and_move_those_objects`, `coffee_maker`, `constraint_single_choice`, `resource_sink`, `constraint_exclude_liberation_theme` |
| n18 | constraint | t1:s24 | Provide the final answer as a concatenation of all correct choices. | `constraint_single_choice`, `respond`*, `correct`*, `right_of`, `constraint_exclude_flowery_language`, `decision`, `metric_order_late`, `left_of`, `constraint_budget_limited`, `entity_flowers`, `constraint_comprehensive`, `constraint_respectful` |
| n19 | constraint | t1:s25 | Format example: if B and C are correct, the answer must be BC. | `example_c_existing_constraint_symbol_becomes_a_typed_construction`, `respond`*, `correct`*, `sequence`, `constraint_exclude_flowery_language`, `metric_order_late`, `unit_character`, `constraint_budget_limited`, `entity_flowers`, `state_sliced`, `constraint_respectful`, `constraint_comprehensive` |

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
- search_web.target → object_label, food_label, animal_label
- search_web.color → color_label
- search_web.currency → currency
- search_web.genre → genre_label
- search_web.location → country
- search_transit.location → country
- pour.destination → object_label
- provides.actor → platform_label
- provides.subject → platform_label
- subject.qualifier → platform_label
- subject.location → country
- activity.object → object_label, food_label, animal_label
- activity.location → country
- activity.instrument → object_label, platform_label
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

**rule_speech_acts_general** (v19/rule/speech-acts-general; rule governing correct)

UTTER-only, void, with the spec's speech attributes and LIST[TERM] constraints. No result binding. Literal content cannot replace required semantic arguments for structured coverage.

**rule_structural_constructs** (v19/rule/structural-constructs; core)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; rule governing has_style)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_attributes_and_generate** (v19/rule/attributes-and-generate; rule governing rank_direction)

Attribute entries name arguments; legality/types come from each operation, not global membership. GENERATE uses the spec's core fields; retained artifact profiles return STRING. Numeric/list results need explicit profiles. Legacy itinerary fields expand to TERM constraints: duration/duration_unit → duration(amount,unit); stop_min_per_day/stop_requirement → minimum_per_period(class,count,period=unit_day), never an inferred temple class; max_walk_duration/unit → maximum_between_stops(activity="walk",amount,unit). No legacy shorthand is enabled. Old events/character_properties/transformations become explicitly scoped TERM constraints. Message purpose is TERM, not send_email.content: GENERATE exact STRING content, then send. Report opaque fallback separately.

**rule_category_artifact_value** (v19/rule/category/artifact-value; rule governing art_plan)

STRING artifact class for GENERATE.target. art_story says what kind of artifact to produce, not what occurs in its plot.

**rule_category_constraint_value** (v19/rule/category/constraint-value; rule governing constraint_single_choice)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_cuisine_value** (v19/rule/category/cuisine-value; rule governing cuisine_indian)

STRING cuisine class; cuisine_indian is a cuisine filter, not the location India.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; rule governing unit_sentence)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing entity_order_vs_assemble_plan)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_format_value** (v19/rule/category/format-value; rule governing format_numbered_list)

STRING format. format_email is layout, not the action send_email.

**rule_category_locale_value** (v19/rule/category/locale-value; candidate)

STRING locale. “English” alone does not always mean locale_en_us; preserve ambiguity.

**rule_category_location_name** (v19/rule/category/location-name; rule governing night_stand)

STRING location descriptor. A `table` surface is not the generated artifact category art_table.

**rule_category_metric_value** (v19/rule/category/metric-value; rule governing metric_order_late)

STRING metric identity, not a Boolean value. Uptime and response time need numeric observations with units; order-late is Boolean-valued. Do not type every metric as BOOL.

**rule_category_product_attribute_value** (v19/rule/category/product-attribute-value; rule governing size_medium)

STRING color/size/product-market facets. gender_women describes a product category, not an assertion about a person's gender.

**rule_category_shape_value** (v19/rule/category/shape-value; rule governing shape_rectangular)

STRING geometry. shape_round may select a circular object; it does not imply color or dimensions.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing right_of)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_state_value** (v19/rule/category/state-value; rule governing state_sliced)

STRING condition used in selection. state_warm does not command heat; “hot” is not automatically synonymous with “warm.”

**rule_category_style_value** (v19/rule/category/style-value; rule governing style_catchy)

STRING production style. style_narrative does not establish that described events occurred.

**rule_category_tone_value** (v19/rule/category/tone-value; rule governing tone_polite)

STRING register. tone_urgent describes urgency, not a concrete deadline.

**rule_category_topic_value** (v19/rule/category/topic-value; candidate)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_composites_general** (v19/rule/composites-general; rule governing topic_school_work_routine)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_examples_general** (v19/rule/examples-general; rule governing example_a_select_two_pillows_and_move_those_objects)

Examples use this glossary's contracts. They have not been verified by an implemented BrainCode parser.

**rule_operations_general** (v19/rule/operations-general; rule governing sort)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_search_web_attributes** (v19/rule/search-web-attributes; rule governing sort)

Optional filters: availability, category, color, cuisine, currency, gender, genre, location, platform, ram_unit, reservation_availability, shape, size (category-refined STRING); max_price, min_ram, min_rating (NUMBER); trending (BOOL). Explicit signature alternatives additionally admit atoms. Price requires currency; RAM requires a capacity unit; no default scale/source. rank is invalid: use sort, whose rank_field accepts rank_* and rank_direction accepts dir_*. Category/genre/availability accept only their own subfamilies.

**rule_supplemental_general** (v19/rule/supplemental-general; rule governing extract)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; rule governing sequence)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- add_to_cart | operation | operation-vocabulary | (target: LIST[REF[STRING]]) -> void | Add the explicitly selected items. Does not pay or place an order.  ⟵ candidate
- click | operation | operation-vocabulary | (target: REF[STRING]) -> void | Activate the selected UI element. Requires its identity, not an invented selector.  ⟵ candidate
- extract | operation | operation-vocabulary | (target: LIST[REF[STRING]], limit: NUMBER) -> LIST[REF[STRING]] | First limit results, preserving order and identity; limit is a nonnegative integer; limit=1 is still a list  ⟵ candidate
- pick_up | operation | operation-vocabulary | (target: STRING / ATOM[object_label] / ATOM[food_label], quantity?: NUMBER, source?: STRING / ATOM[object_label], color?: STRING / ATOM[color_label], shape?: STRING, state?: STRING) -> REF[STRING] or LIST[REF[STRING]] | Select/acquire objects. Missing quantity or literal 1 returns REF; integer literal greater than 1 returns LIST[REF]. Other values are invalid for this profile. | aliases: grab, take, retrieve  ⟵ dependency of example_a_select_two_pillows_and_move_those_objects
- place | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label], location?: STRING / ATOM[object_label], relation?: STRING) -> void | Place an already acquired object. Spatial relation must be explicit if the source distinguishes it. | aliases: put, insert  ⟵ dependency of example_a_select_two_pillows_and_move_those_objects
- pour | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Transfer selected liquid to the destination, preserving tracked material identity.  ⟵ candidate
- search_transit | operation | operation-vocabulary | (target: STRING, constraints?: LIST[TERM], location?: STRING / ATOM[country]) -> LIST[REF[STRING]] | Query transit options. Does not buy tickets.  ⟵ candidate
- search_travel | operation | operation-vocabulary | (target: STRING, constraints?: LIST[TERM], location?: STRING / ATOM[country]) -> LIST[REF[STRING]] | Query travel options meeting supplied constraints. Does not book them.  ⟵ candidate
- search_web | operation | operation-vocabulary | (target: STRING / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], color?: STRING / ATOM[color_label], currency?: STRING / ATOM[currency], genre?: STRING / ATOM[genre_label], location?: STRING / ATOM[country], ...other search attributes below) -> LIST[REF[STRING]] | Query a catalog/web source. Criteria filter the result; rank separately when requested. | aliases: find, look for  ⟵ candidate
- select_filter | operation | operation-vocabulary | (target: REF[STRING], criterion: TERM) -> void | Apply one specified filter in an existing UI. Do not add this operation when the source only requests filtered search.  ⟵ candidate
- select_option | operation | operation-vocabulary | (target: REF[STRING], value: STRING) -> void | Select an option from a dropdown or select menu element. target must be a select element. | aliases: choose_option, choose_dropdown, pick_option  ⟵ candidate
- slice | operation | operation-vocabulary | (target: REF[STRING] / TERM) -> REF[STRING] | Slice the selected material or described term, preserving its tracked aggregate identity. | aliases: chop, cut  ⟵ candidate
- sort | operation | operation-vocabulary | (target: LIST[REF[STRING]], rank_direction: STRING, rank_field: STRING) -> LIST[REF[STRING]] | Request ordering of selected results. Preserve member identity; this is not a claim that order was observed. | aliases: rank, order by  ⟵ candidate

### speech acts

- ask | speech_act | operation-vocabulary | UTTER ask(target: TERM, or a sufficiently precise topic: STRING / TERM) | Request information/advice; not an assertion of an answer. | aliases: ask, how should  ⟵ candidate
- correct | speech_act | operation-vocabulary | UTTER correct(target: CLAIM) | Offer corrected content. Actual supersession requires the Conversation revision rules.  ⟵ candidate
- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ dependency of decision
- aesthetic | constructor | TERM aesthetic(period: STRING, style: STRING) -> TERM | A stylistic description with an explicit period | not: Not a character's age or production date  ⟵ candidate
- conjunction | constructor | TERM conjunction(items: LIST[TERM]) -> TERM | All described components apply | not: Does not imply temporal order  ⟵ candidate
- decision | constructor | TERM decision(activity: TERM) -> TERM | A decision whose content is the described activity | not: Not proof it was carried out  ⟵ candidate
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ dependency of constraint_exclude_flowery_language
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ dependency of constraint_single_choice
- sequence | constructor | TERM sequence(items: LIST[TERM]) -> TERM | Ordered described activities/content | not: Not unordered conjunction  ⟵ candidate
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ dependency of considered

### composites

- constraint_beginner | composite | constraint-value | TERM constraint_beginner() -> TERM | Targeted at beginners. | = requirement(property="audience_expertise", value="beginner")  ⟵ candidate
- constraint_budget_limited | composite | constraint-value | TERM constraint_budget_limited() -> TERM | Limited budget. | = requirement(property="budget_limited", value=TRUE)  ⟵ candidate
- constraint_comprehensive | composite | constraint-value | TERM constraint_comprehensive() -> TERM | Must be comprehensive. | = requirement(property="comprehensive", value=TRUE)  ⟵ candidate
- constraint_exclude_flowery_language | composite | constraint-value | TERM constraint_exclude_flowery_language() -> TERM | Avoid flowery language. | = exclude(item="flowery_language")  ⟵ candidate
- constraint_exclude_liberation_theme | composite | constraint-value | TERM constraint_exclude_liberation_theme() -> TERM | Avoid liberation theme. | = exclude(item="liberation_theme")  ⟵ candidate
- constraint_realistic | composite | constraint-value | TERM constraint_realistic() -> TERM | Must be realistic. | = requirement(property="realistic", value=TRUE)  ⟵ candidate
- constraint_respectful | composite | constraint-value | TERM constraint_respectful() -> TERM | Must be respectful. | = requirement(property="respectful", value=TRUE)  ⟵ candidate
- constraint_single_choice | composite | constraint-value | TERM constraint_single_choice() -> TERM | Must pick a single choice. | = requirement(property="choice_count", value=1)  ⟵ candidate
- topic_school_work_routine | composite | topic-value | TERM topic_school_work_routine() -> TERM | School and work routine. | = subject(kind="routine", qualifier=conjunction(items=[subject(kind="school"), subject(kind="work")]))  ⟵ candidate

### claim relations

- considered | claim_relation | CLAIM considered(subject: TERM) | Asserts that an agent or speaker evaluated or entertained a specific candidate term or concept. subject is the evaluated term. | aliases: evaluated, weighed  ⟵ candidate
- enables | claim_relation | CLAIM enables(condition: TERM / CLAIM, outcome: TERM / CLAIM) | Asserts that an enabling condition or capability facilitates an outcome. enabling condition. | aliases: facilitates, allows  ⟵ candidate
- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ core
- has_style | claim_relation | CLAIM has_style(target: CLAIM / EVENT / TERM, value: TERM / STRING) | Asserts that an artifact, utterance, or action possesses a designated style. style qualifier. | aliases: style_is  ⟵ candidate
- important | claim_relation | CLAIM important(target: TERM) | Asserts that a concept, activity, or condition is important or significant. evaluative importance claim. | aliases: significant  ⟵ candidate
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ dependency of enables
- propose_menu | claim_relation | CLAIM propose_menu(menu: TERM) | Asserts the proposal of a comprehensive menu plan. planning proposal. | aliases: suggest_menu  ⟵ candidate
- provides | claim_relation | CLAIM provides(actor: STRING / TERM / ATOM[platform_label], subject: STRING / TERM / ATOM[platform_label]) | Asserts that an establishment, organization, or provider supplies a specified item or service. provision claim. | aliases: supplies  ⟵ candidate

### links

- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ core
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ core
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ core

### values

- art_itinerary | value | artifact-value | An ordered travel plan; GENERATE returns STRING, not booked travel  ⟵ candidate
- art_plan | value | artifact-value | Actionable plan.  ⟵ candidate
- art_short_text | value | artifact-value | Short free text.  ⟵ candidate
- art_structured_report | value | artifact-value | Headed/structured report.  ⟵ candidate
- art_technical_explanation | value | artifact-value | Technical explanation of a concept.  ⟵ candidate
- cuisine_indian | value | cuisine-value | Indian cuisine. | aliases: Indian food, Indian  ⟵ candidate
- unit_character | value | duration-unit-value | One Unicode scalar value in the final rendered artifact; line endings are normalized to LF before counting. | aliases: characters, chars  ⟵ candidate
- unit_item | value | duration-unit-value | Top-level generated list or report item. | aliases: items, entries  ⟵ candidate
- unit_paragraph | value | duration-unit-value | Paragraph of text. | aliases: paragraphs, paragraph  ⟵ candidate
- unit_sentence | value | duration-unit-value | One grammatical sentence in text generation or constraint counting. | not: unit_paragraph (paragraph block) or unit_word (individual word) | aliases: sentence, sentences  ⟵ candidate
- bed | value | entity-name | A bed furniture surface or sleeping area. | aliases: bed  ⟵ candidate
- bottle | value | entity-name | A bottle container object, typically used for holding liquids. | not: mug (a drinking cup with a handle) or water (the liquid itself) | aliases: bottle, water bottle, plastic bottle  ⟵ candidate
- bowl | value | entity-name | A container/dish used for holding food or small items. | aliases: bowl  ⟵ candidate
- bowtie | value | entity-name | Item or prop in joke/creative context: bowtie. | aliases: bowtie  ⟵ candidate
- cardamom | value | entity-name | Aromatic spice seeds or pods from Elettaria or Amomum used in cooking and baking. | not: cinnamon, ginger, or other distinct spice varieties | aliases: cardamom, ground cardamom, cardamom pods  ⟵ candidate
- cardboard_box | value | entity-name | A cardboard box, carton, or general storage box container. | not: tissue_box (specifically a box of paper tissues) or safe (a lockable metal container) | aliases: cardboard box, box, carton, storage box  ⟵ candidate
- chair | value | entity-name | A chair furniture seat with a backrest. | not: object_label::armchair (specifically an object_label::armchair with side armrests) or object_label::sofa | aliases: chair, seat  ⟵ candidate
- cheese | value | entity-name | Dairy food item: cheese. | not: meat or non-dairy food items | aliases: cheese  ⟵ candidate
- clothing | value | entity-name | Physical item used for concealment or covering: clothing. | aliases: clothing  ⟵ candidate
- cloves | value | entity-name | Aromatic dried flower buds of Syzygium aromaticum used as a culinary spice. | not: cinnamon, nutmeg, or other distinct spice varieties | aliases: cloves, clove, ground cloves, whole cloves  ⟵ candidate
- coffee_maker | value | entity-name | A coffee-making appliance; not automatically a heating resource  ⟵ candidate
- desk | value | entity-name | A work desk furniture surface. | aliases: desk  ⟵ candidate
- dresser | value | entity-name | A chest of drawers / dresser furniture. | aliases: dresser  ⟵ candidate
- egift_card | value | entity-name | Electronic gift card or digital voucher product. | aliases: digital_gift_card, e_gift_card  ⟵ candidate
- entity_condensed_grocery_list | value | entity-name | Event planning item or menu category: entity_condensed_grocery_list. | aliases: entity_condensed_grocery_list  ⟵ candidate
- entity_drinks | value | entity-name | Event planning item or menu category: entity_drinks. | aliases: entity_drinks  ⟵ candidate
- entity_flowers | value | entity-name | Flowers, blossoms, or floral design elements. | not: constraint_exclude_flowery_language (a prose style constraint) or agricultural food items | aliases: flowers, floral, flower, floral decorations  ⟵ candidate
- entity_grocery_list | value | entity-name | Event planning item or menu category: entity_grocery_list. | aliases: entity_grocery_list  ⟵ candidate
- entity_order_vs_assemble_plan | value | entity-name | Event planning item or menu category: entity_order_vs_assemble_plan. | aliases: entity_order_vs_assemble_plan  ⟵ candidate
- figurine | value | entity-name | A small carved, molded, or sculpted decorative statuette object. | not: character (a fictional persona) or captioned_figure (a document figure/photo) | aliases: figurine, statuette, statue, small statue, sculptural figure, miniature figure  ⟵ candidate
- grape_merlot | value | entity-name | Merlot wine grape variety. | not: other red grape varieties such as grape_cabernet_sauvignon or grape_pinot_noir | aliases: Merlot, merlot grape  ⟵ candidate
- grape_pinot_noir | value | entity-name | Pinot Noir wine grape variety. | not: other red grape varieties such as grape_cabernet_sauvignon or grape_merlot | aliases: Pinot Noir, pinot noir grape  ⟵ candidate
- grape_thompson_seedless | value | entity-name | Thompson Seedless grape variety. | not: wine grape cultivars like grape_merlot or grape_chardonnay | aliases: Thompson Seedless, thompson seedless grape, sultana grape  ⟵ candidate
- knife | value | entity-name | A cutting utensil used for slicing or food preparation. | aliases: knife  ⟵ candidate
- martini_glass | value | entity-name | A cocktail or Martini drinking glass object. | not: mug (a drinking cup with a handle) or bottle (liquid storage container) | aliases: martini glass, cocktail glass, glass  ⟵ candidate
- mattress | value | entity-name | A mattress cushion or sleeping surface object. | not: bed (a bed furniture surface or frame) or object_label::pillow | aliases: mattress, mattresses  ⟵ candidate
- meat | value | entity-name | Food item: meat or beef. | not: animal_label::tuna or animal_label::fish (specific aquatic foods) | aliases: meat, beef  ⟵ candidate
- mittens | value | entity-name | Item or prop in joke/creative context: mittens. | aliases: mittens  ⟵ candidate
- mug | value | entity-name | Drinking cup. | aliases: mug  ⟵ candidate
- pan | value | entity-name | A metal cooking vessel, frying pan, skillet, saucepan, or pot cookware item used for preparing, heating, or holding food. | not: bowl (deep concave vessel) or plate (shallow flat dining dish) | aliases: pan, frying pan, skillet, saucepan, pot  ⟵ candidate
- piano | value | entity-name | A piano musical instrument or large furniture object. | not: topic_classical_piano or topic_jazz_piano (music genre topics) | aliases: piano, grand piano, upright piano, keyboard  ⟵ candidate
- resource_heater | value | entity-name | Canonical abstract heating resource when no particular appliance is named.  ⟵ candidate
- resource_sink | value | entity-name | Canonical abstract washing resource when no particular sink is named.  ⟵ candidate
- scissors | value | entity-name | A handheld shearing cutting tool with two pivoted blades used for cutting paper, ribbon, and crafting materials. | not: knife (a kitchen or food preparation cutting utensil) | aliases: scissors, shears, pair of scissors  ⟵ candidate
- spatula | value | entity-name | A kitchen utensil with a broad, flat, and flexible blade used for lifting, flipping, or spreading food. | not: knife (cutting utensil) or spoon (scooping utensil) | aliases: spatula, turner, flipper  ⟵ candidate
- spoon | value | entity-name | An eating or cooking utensil. | aliases: spoon  ⟵ candidate
- sultana | value | entity-name | Dried white seedless grape food product. | not: raisin (dark dried grape) or wine_grape | aliases: sultana, sultanas, golden raisin  ⟵ candidate
- tape | value | entity-name | Adhesive tape used for fastening and securing wrapping paper, boxes, or packaging materials. | not: waterproof_bandages (medical wound dressing) or waterproof_stickers (decorative stickers) | aliases: tape, adhesive tape, sticky tape, scotch tape  ⟵ candidate
- tissue_box | value | entity-name | A cardboard or plastic box containing paper tissues used for wiping or cleaning. | not: waterproof bandages or other medical coverings | aliases: tissue box, tissues, tissue  ⟵ candidate
- trash_can | value | entity-name | A waste receptacle container. | aliases: trash_can  ⟵ candidate
- vase | value | entity-name | A decorative or functional open container typically used for holding cut flowers or liquids. | not: bottle (a liquid storage container with a narrow neck) or bowl (a shallow dish) | aliases: vase, flower vase, flower_vase  ⟵ candidate
- watch | value | entity-name | A watch or wristwatch timepiece object. | not: clock (a stationary timepiece appliance) or duration units like unit_hour | aliases: watch, wristwatch, wrist watch  ⟵ candidate
- waterproof_bandages | value | entity-name | Physical item used for concealment or covering: waterproof_bandages. | aliases: waterproof_bandages  ⟵ candidate
- waterproof_stickers | value | entity-name | Physical item used for concealment or covering: waterproof_stickers. | aliases: waterproof_stickers  ⟵ candidate
- wine | value | entity-name | Fermented fruit or grape beverage. | not: unfermented fruit juice or distilled alcohol/spirits | aliases: wine, wines  ⟵ candidate
- wine_grape | value | entity-name | Grape variety cultivated specifically for winemaking. | not: table grapes or processed wine product | aliases: wine grape, wine grapes, grape  ⟵ candidate
- yarn | value | entity-name | Item or prop in joke/creative context: yarn. | aliases: yarn  ⟵ candidate
- format_numbered_list | value | format-value | Numbered list. | aliases: numbered steps  ⟵ candidate
- locale_de | value | locale-value | German language or locale descriptor. | not: other language locales (such as locale_en_us or locale_fr) or country entity (country::DE) | aliases: German, german, Deutsch, de, de-DE  ⟵ candidate
- locale_en_gb | value | locale-value | UK English. | aliases: british english  ⟵ candidate
- locale_en_us | value | locale-value | US English. | aliases: english, en-us  ⟵ candidate
- night_stand | value | location-name | A small bedside table or nightstand furniture surface. | not: a chest of drawers (use dresser) or a general table surface (use table) | aliases: nightstand, bedside table  ⟵ candidate
- metric_order_late | value | metric-value | Whether an order is late. | aliases: order is late, delayed  ⟵ candidate
- color_pink | value | product-attribute-value | Pink visual color qualifier. | not: color_label::red, color_label::purple, or other distinct color shades | aliases: pink, color_pink, blush pink, rose pink, pastel pink  ⟵ candidate
- material_memory_foam | value | product-attribute-value | Memory foam viscoelastic polyurethane material qualifier. | not: sponge (a porous cleaning tool) or generic bedding | aliases: memory foam, memory_foam, viscoelastic foam  ⟵ candidate
- size_large | value | product-attribute-value | Large size. | aliases: large, L  ⟵ candidate
- size_medium | value | product-attribute-value | Medium size. | aliases: medium, M  ⟵ candidate
- size_queen | value | product-attribute-value | Queen-size dimension classification for beds, mattresses, and bedding. | not: size_large (generic large apparel/goods size) or size_king | aliases: queen, queen size, Queen  ⟵ candidate
- size_small | value | product-attribute-value | Small size. | aliases: small, S  ⟵ candidate
- size_tall | value | product-attribute-value | Tall relative vertical dimension qualifier. | aliases: size_tall  ⟵ candidate
- shape_oval | value | shape-value | Oval. | aliases: oval  ⟵ candidate
- shape_rectangular | value | shape-value | Rectangular. | aliases: rectangular, rectangle  ⟵ candidate
- shape_round | value | shape-value | Circular/round. | aliases: round, circular  ⟵ candidate
- shape_square | value | shape-value | Square. | aliases: square  ⟵ candidate
- shape_triangular | value | shape-value | Triangular. | aliases: triangular, triangle  ⟵ candidate
- in_front_of | value | spatial-relation | Positioned in front of. | aliases: in front of  ⟵ candidate
- left_of | value | spatial-relation | To the left of. | aliases: left of  ⟵ candidate
- next_to | value | spatial-relation | Adjacent to. | aliases: beside  ⟵ candidate
- on | value | spatial-relation | Resting atop. | aliases: on top of  ⟵ dependency of example_a_select_two_pillows_and_move_those_objects
- right_of | value | spatial-relation | To the right of. | aliases: right of  ⟵ candidate
- state_sliced | value | state-value | The condition of being sliced or cut into thin pieces. | not: the operation slice itself | aliases: sliced, slice, chopped, cut  ⟵ candidate
- style_catchy | value | style-value | Catchy, attention-grabbing style. | aliases: catchy  ⟵ candidate
- tone_concise | value | tone-value | Brief, to-the-point register. | aliases: briefly, concisely  ⟵ candidate
- tone_polite | value | tone-value | Courteous, respectful register. | aliases: politely, kindly  ⟵ candidate
- topic_classical_piano | value | topic-value | Classical piano.  ⟵ candidate
- topic_current_events | value | topic-value | Current news, geopolitical events, and ongoing international developments. | aliases: current_events, news  ⟵ candidate
- topic_pickup_lines | value | topic-value | Pickup lines.  ⟵ candidate

### attributes

- rank_direction | attribute | attribute-name | Sort direction from search-value.  ⟵ candidate

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

