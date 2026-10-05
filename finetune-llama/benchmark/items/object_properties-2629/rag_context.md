# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 18 needs (decomposition: llm), 156 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | speech_act | t1:s1 | Informs about an initial collection of 37 items that undergo changes. | `unit_item`*, `respond`, `inform`*, `art_structured_report`, `sequence`, `propose`, `target`, `apologize`, `acknowledge`, `rule_review_points`, `offer`, `express_interest` |
| n2 | object | t1:s2, t1:s3, t1:s4, t1:s5, t1:s6, t1:s7, t1:s8 | Initial collection of 37 items with attributes like size, origin, material, and smell. | `size_small`, `unit_item`*, `dried_fruit`, `size_medium`, `art_structured_report`, `clothing`, `material_memory_foam`, `size_large`, `art_character_profile`, `sponge`, `object_label`, `rule_category_artifact_value` |
| n3 | object | t1:s9 | Colors of the initial 37 items in sequence. | `sequence`*, `color_pink`, `unit_item`*, `color_label`, `art_structured_report`, `art_short_text`, `char_2000s_anime_style`, `art_character_profile`, `unit_character`, `aesthetic`, `format_bullet_list`, `pear` |
| n4 | action | t1:s10 | Duplicate items smelling of citrus, rose, or lavender, changing smell to cousin's favorite. | `color_pink`, `unit_item`*, `dried_fruit`, `sultana`, `raisin`, `fruit_juice`, `cloves`, `mug`, `duplicate_definition`, `grape_pinot_noir`, `dulce_de_nata`, `style_catchy` |
| n5 | claim | t1:s11, t1:s12 | Intermediate counts of items by smell after the first change. | `unit_item`*, `outcome`, `metric_first_time_buyer`, `dried_fruit`, `pour`, `size_small`, `occurred_recently`, `rinse`, `quantity`, `style_catchy`, `state_dirty`, `duplicate_definition` |
| n6 | action | t1:s13 | Discard items smelling of coffee, leather, or lavender. | `coffee_maker`, `unit_item`*, `mug`, `clothing`, `dulce_de_nata`, `dried_fruit`, `cloves`, `vase`, `style_catchy`, `sultana`, `dresser`, `cinnamon` |
| n7 | action | t1:s14 | Replace extra-large items with aunt's favorite material and freshly cut grass smell. | `slice`*, `size_large`*, `state_sliced`*, `dried_fruit`, `raisin`, `sultana`, `clothing`, `pour`, `trash_can`, `cloves`, `dulce_de_nata`, `bowl` |
| n8 | claim | t1:s15 | Intermediate counts of items by material after the third change. | `unit_item`*, `outcome`, `art_structured_report`, `occurred_recently`, `sequence`, `size_small`, `quantity`, `duplicate_definition`, `meets_needs`, `pour`, `works_best`, `duration` |
| n9 | action | t1:s16 | Duplicate gold items with specific new attributes (maroon, Spanish, extra-small, pine needles, plastic). | `size_small`*, `locale_es`*, `topic_current_events`*, `dried_fruit`, `color_pink`, `clothing`, `grape_merlot`, `sultana`, `raisin`, `scissors`, `unit_item`*, `waterproof_bandages` |
| n10 | action | t1:s17 | Duplicate items with (smell, color) pairs not present in the initial collection. | `color_pink`, `duplicate_definition`, `gift`*, `color_label`, `exists_in`*, `dried_fruit`, `clothing`, `sultana`, `raisin`, `grape_thompson_seedless`, `unit_item`*, `entity_desserts` |
| n11 | action | t1:s18 | Remove one extra-small item from the collection. | `remove`*, `remove_literal`, `size_small`*, `event_sadie_adler_unmasking`, `transform_remove_br`, `dried_fruit`, `exclude`, `figurine`, `bowl`, `example_a_select_two_pillows_and_move_those_objects`, `pick_up`, `slice` |
| n12 | action | t1:s19 | Count items in the final collection matching specific criteria. | `unit_item`*, `quantity`, `minimum_per_period`, `search_web`, `dried_fruit`, `apply_filters`, `add_to_cart`, `slice`, `sort`, `duration`, `entity_checklist`, `unit_character` |
| n13 | negation | t1:s19 | Exclude items with color brown. → `color_label::<key>` | `color_label`*, `color_pink`, `exclude`*, `unit_item`*, `dried_fruit`, `clothing`, `sultana`, `art_short_text`, `style_catchy`, `entity_desserts`, `bowl`, `waterproof_bandages` |
| n14 | negation | t1:s19 | Exclude items with size extra-small. | `size_small`*, `exclude`*, `size_large`, `size_medium`, `unit_item`*, `bowl`, `size_tall`, `size_queen`, `art_short_text`, `clothing`, `example_a_select_two_pillows_and_move_those_objects`, `figurine` |
| n15 | negation | t1:s19 | Exclude items with material steel. | `exclude`*, `unit_item`*, `state_empty`, `clothing`, `waterproof_bandages`, `waterproof_stickers`, `material_memory_foam`, `art_short_text`, `size_small`, `tape`, `sponge`, `example_a_select_two_pillows_and_move_those_objects` |
| n16 | negation | t1:s19 | Exclude items with smell pine needles. | `exclude`*, `unit_item`*, `dried_fruit`, `raisin`, `clothing`, `waterproof_stickers`, `waterproof_bandages`, `sultana`, `tissue_box`, `spatula`, `entity_flowers`, `bottle` |
| n17 | negation | t1:s19 | Exclude items with Turkish origin. → `country::<key>` | `exclude`*, `constraint_exclude_flowery_language`, `unit_item`*, `sultana`, `maqluba`, `clothing`, `bowl`, `cheese`, `entity_flowers`, `cuisine_mediterranean`, `cuisine_arab`, `include` |
| n18 | constraint | t1:s20 | Output 'unknown' if the exact number cannot be computed. | `at_most`, `extract`, `outcome`, `rule_category_constraint_value`, `test_condition`, `entity_flowers`, `constraint_exclude_flowery_language`, `quantity`, `constraint_budget_limited`, `assert_multinomial_scorer`, `measure`, `calculation` |

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

- pour.destination → object_label
- rinse.destination → object_label
- pick_up.target → object_label, food_label
- pick_up.source → object_label
- pick_up.color → color_label
- search_web.target → object_label, food_label, animal_label
- search_web.color → color_label
- search_web.currency → currency
- search_web.genre → genre_label
- search_web.location → country
- measure.unit → currency
- activity.object → object_label, food_label, animal_label
- activity.location → country
- activity.instrument → object_label, platform_label
- place.destination → object_label
- place.location → object_label
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

**rule_recording_signatures** (v19/rule/recording-signatures; rule governing pour)

RECORD ACTION uses the operation signature with REF[STRING] → TERM and LIST[REF[STRING]] → LIST[TERM]; other types/categories stay unchanged. Return EVENT, never the runtime result. Record actual outputs as attributed CLAIMs. Do not infer missing resources.

**rule_speech_acts_general** (v19/rule/speech-acts-general; rule governing respond)

UTTER-only, void, with the spec's speech attributes and LIST[TERM] constraints. No result binding. Literal content cannot replace required semantic arguments for structured coverage.

**rule_structural_constructs** (v19/rule/structural-constructs; core)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; rule governing duplicate_definition)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_attributes_and_generate** (v19/rule/attributes-and-generate; rule governing art_structured_report)

Attribute entries name arguments; legality/types come from each operation, not global membership. GENERATE uses the spec's core fields; retained artifact profiles return STRING. Numeric/list results need explicit profiles. Legacy itinerary fields expand to TERM constraints: duration/duration_unit → duration(amount,unit); stop_min_per_day/stop_requirement → minimum_per_period(class,count,period=unit_day), never an inferred temple class; max_walk_duration/unit → maximum_between_stops(activity="walk",amount,unit). No legacy shorthand is enabled. Old events/character_properties/transformations become explicitly scoped TERM constraints. Message purpose is TERM, not send_email.content: GENERATE exact STRING content, then send. Report opaque fallback separately.

**rule_category_artifact_value** (v19/rule/category/artifact-value; candidate)

STRING artifact class for GENERATE.target. art_story says what kind of artifact to produce, not what occurs in its plot.

**rule_category_character_property_value** (v19/rule/category/character-property-value; rule governing char_2000s_anime_style)

TERM-described trait/style. Use constraints and explicit inclusion/scope; do not use an ungoverned character_properties attribute.

**rule_category_code_value** (v19/rule/category/code-value; rule governing assert_multinomial_scorer)

path_/sym_ remain STRING identities; migrated chg_/assert_ are TERM constructors. Do not recover an exact file path by guessing from underscores.

**rule_category_constraint_value** (v19/rule/category/constraint-value; candidate)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_cuisine_value** (v19/rule/category/cuisine-value; rule governing cuisine_mediterranean)

STRING cuisine class; cuisine_indian is a cuisine filter, not the location India.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; rule governing unit_item)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing dried_fruit)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_event_value** (v19/rule/category/event-value; rule governing event_sadie_adler_unmasking)

TERM-described narrative event, not a recorded EVENT. Require inclusion explicitly when generating a story.

**rule_category_format_value** (v19/rule/category/format-value; rule governing format_structured_report)

STRING format. format_email is layout, not the action send_email.

**rule_category_locale_value** (v19/rule/category/locale-value; rule governing locale_es)

STRING locale. “English” alone does not always mean locale_en_us; preserve ambiguity.

**rule_category_metric_value** (v19/rule/category/metric-value; rule governing metric_first_time_buyer)

STRING metric identity, not a Boolean value. Uptime and response time need numeric observations with units; order-late is Boolean-valued. Do not type every metric as BOOL.

**rule_category_product_attribute_value** (v19/rule/category/product-attribute-value; rule governing size_small)

STRING color/size/product-market facets. gender_women describes a product category, not an assertion about a person's gender.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing on)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_state_value** (v19/rule/category/state-value; rule governing state_dirty)

STRING condition used in selection. state_warm does not command heat; “hot” is not automatically synonymous with “warm.”

**rule_category_style_value** (v19/rule/category/style-value; rule governing style_catchy)

STRING production style. style_narrative does not establish that described events occurred.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_pickup_lines)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_category_transformation_value** (v19/rule/category/transformation-value; rule governing transform_remove_br)

TERM-described transformation. Pass it through constraints; no ungoverned transformations attribute.

**rule_composites_general** (v19/rule/composites-general; rule governing char_2000s_anime_style)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_examples_general** (v19/rule/examples-general; rule governing example_a_select_two_pillows_and_move_those_objects)

Examples use this glossary's contracts. They have not been verified by an implemented BrainCode parser.

**rule_operations_general** (v19/rule/operations-general; rule governing pour)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_review_points** (v19/rule/review-points; candidate)

The 2026-10-04 review retained the current definitions of cap_gb, cap_tb, constraint_17_plus and dom_sgi. Do not invent scale choices, rating thresholds or acronym expansions beyond those definitions. Money signs, locale aliases, warm/hot and ranking phrases require context. Only this explicit inventory is usable; do not guess historical entries. Before adoption, resolve any remaining Needs clarification entries and review signatures/expansions. Artifact checks do not establish parser correctness or semantic fidelity.

**rule_search_web_attributes** (v19/rule/search-web-attributes; rule governing search_web)

Optional filters: availability, category, color, cuisine, currency, gender, genre, location, platform, ram_unit, reservation_availability, shape, size (category-refined STRING); max_price, min_ram, min_rating (NUMBER); trending (BOOL). Explicit signature alternatives additionally admit atoms. Price requires currency; RAM requires a capacity unit; no default scale/source. rank is invalid: use sort, whose rank_field accepts rank_* and rank_direction accepts dir_*. Category/genre/availability accept only their own subfamilies.

**rule_supplemental_general** (v19/rule/supplemental-general; rule governing coffee_maker)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; rule governing sequence)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- add_to_cart | operation | operation-vocabulary | (target: LIST[REF[STRING]]) -> void | Add the explicitly selected items. Does not pay or place an order.  ⟵ candidate
- apply_filters | operation | operation-vocabulary | (target: REF[STRING], criteria: LIST[TERM]) -> void | Apply the listed filters to an existing UI. Not repeated evidence of a search already represented.  ⟵ candidate
- extract | operation | operation-vocabulary | (target: LIST[REF[STRING]], limit: NUMBER) -> LIST[REF[STRING]] | First limit results, preserving order and identity; limit is a nonnegative integer; limit=1 is still a list  ⟵ candidate
- pick_up | operation | operation-vocabulary | (target: STRING / ATOM[object_label] / ATOM[food_label], quantity?: NUMBER, source?: STRING / ATOM[object_label], color?: STRING / ATOM[color_label], shape?: STRING, state?: STRING) -> REF[STRING] or LIST[REF[STRING]] | Select/acquire objects. Missing quantity or literal 1 returns REF; integer literal greater than 1 returns LIST[REF]. Other values are invalid for this profile. | aliases: grab, take, retrieve  ⟵ candidate
- place | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label], location?: STRING / ATOM[object_label], relation?: STRING) -> void | Place an already acquired object. Spatial relation must be explicit if the source distinguishes it. | aliases: put, insert  ⟵ dependency of example_a_select_two_pillows_and_move_those_objects
- pour | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Transfer selected liquid to the destination, preserving tracked material identity.  ⟵ candidate
- remove | operation | operation-vocabulary | (target: REF[STRING] / TERM, source?: STRING / TERM) -> void | Remove an object from an enclosure or container. target must be an object inside source. | aliases: take_out  ⟵ candidate
- rinse | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Rinse using the stated resource; return the same identity. It is not enough that the object is already clean. | aliases: wash  ⟵ candidate
- search_web | operation | operation-vocabulary | (target: STRING / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], color?: STRING / ATOM[color_label], currency?: STRING / ATOM[currency], genre?: STRING / ATOM[genre_label], location?: STRING / ATOM[country], ...other search attributes below) -> LIST[REF[STRING]] | Query a catalog/web source. Criteria filter the result; rank separately when requested. | aliases: find, look for  ⟵ candidate
- slice | operation | operation-vocabulary | (target: REF[STRING] / TERM) -> REF[STRING] | Slice the selected material or described term, preserving its tracked aggregate identity. | aliases: chop, cut  ⟵ candidate
- sort | operation | operation-vocabulary | (target: LIST[REF[STRING]], rank_direction: STRING, rank_field: STRING) -> LIST[REF[STRING]] | Request ordering of selected results. Preserve member identity; this is not a claim that order was observed. | aliases: rank, order by  ⟵ candidate

### speech acts

- apologize | speech_act | UTTER apologize(target?: CLAIM / TERM) | Speech act expressing apology or regret for an outcome or target. | not: decline (which is refusing) | aliases: apologize, apology, sorry  ⟵ candidate
- acknowledge | speech_act | operation-vocabulary | UTTER acknowledge(target: CLAIM / TERM) | Acknowledge receipt/awareness; does not imply agreement.  ⟵ candidate
- express_interest | speech_act | operation-vocabulary | UTTER express_interest(target: STRING / TERM) | Speech act expressing conversational interest or engagement in a topic. speech act in dialogic traces. | aliases: show_interest  ⟵ candidate
- inform | speech_act | operation-vocabulary | UTTER inform(target: CLAIM) | Present the proposition; preserve its holder/status.  ⟵ candidate
- offer | speech_act | operation-vocabulary | UTTER offer(target: STRING / TERM) | Speech act offering assistance, service, or items to a conversation partner. speech act in dialogic traces. | aliases: proffer  ⟵ candidate
- propose | speech_act | operation-vocabulary | UTTER propose(target: TERM) | Suggest an action/idea; does not record it as performed.  ⟵ candidate
- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ dependency of event_sadie_adler_unmasking
- aesthetic | constructor | TERM aesthetic(period: STRING, style: STRING) -> TERM | A stylistic description with an explicit period | not: Not a character's age or production date  ⟵ candidate
- at_most | constructor | TERM at_most(measure: TERM) -> TERM | An upper bound: the constrained value is less than or equal to the given measure (or number term). Use inside requirement(value=...). | not: an exact value or a target to aim for | aliases: at most, maximum, up to, no more than, under  ⟵ candidate
- calculation | constructor | TERM calculation(inputs: LIST[TERM], operation: STRING, result?: TERM) -> TERM | Constructs a descriptive representation of an arithmetic or algorithmic calculation step with inputs, operation identifier, and optional resulting value. | not: an executed runtime action or factual claim of outcome | aliases: math_operation, compute_step  ⟵ candidate
- duration | constructor | TERM duration(amount: NUMBER, unit: STRING) -> TERM | Requested elapsed/calendar extent | not: Word/item counts are not time  ⟵ candidate
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ candidate
- include | constructor | TERM include(item: STRING / TERM) -> TERM | Require the identified content/item | not: Not permission to invent an instance in a recorded trace  ⟵ candidate
- indicator | constructor | TERM indicator(condition: STRING / TERM, indicator_type?: STRING) -> TERM | Constructs a descriptive term representing a warning sign, behavioral marker, or red flag indicating an underlying condition or risk. | not: warning (a system alert claim relation) or color_label::red (a product color) | aliases: red flag, warning sign, behavioral marker, signal  ⟵ candidate
- measure | constructor | TERM measure(amount: NUMBER, unit: STRING / ATOM[currency]) -> TERM | A measured amount: a number with its unit symbol (a unit-category value such as unit_minute, cap_gb or currency::USD). Describes the amount only; asserts nothing. ATOM[currency] is also accepted and supplies the pinned currency identity; no exchange rate or conversion is implicit. | not: a symbol with the number baked in (char_age_18, size_16gb); a unitless count (use the quantity argument) | aliases: amount of, size of, measured in  ⟵ candidate
- minimum_per_period | constructor | TERM minimum_per_period(class: STRING, count: NUMBER, period: STRING) -> TERM | At least count members of class in each period | not: Not a minimum total over the whole artifact  ⟵ candidate
- remove_literal | constructor | TERM remove_literal(text: STRING) -> TERM | Remove occurrences of that exact literal in the stated artifact | not: Not remove similar markup unless specified  ⟵ candidate
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ dependency of constraint_budget_limited
- sequence | constructor | TERM sequence(items: LIST[TERM]) -> TERM | Ordered described activities/content | not: Not unordered conjunction  ⟵ candidate
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ dependency of meets_needs
- test_condition | constructor | TERM test_condition(condition: STRING, expected: BOOL) -> TERM | A testable condition with the expected Boolean outcome | not: Expected outcome is not an observed result  ⟵ candidate

### composites

- char_2000s_anime_style | composite | character-property-value | TERM char_2000s_anime_style() -> TERM | 2000s anime style. | = aesthetic(period="2000s", style="anime")  ⟵ candidate
- assert_multinomial_scorer | composite | code-value | TERM assert_multinomial_scorer() -> TERM | Assertion that multinomial probabilistic scoring succeeds. | = test_condition(condition="multinomial_probabilistic_scoring", expected=TRUE)  ⟵ candidate
- constraint_budget_limited | composite | constraint-value | TERM constraint_budget_limited() -> TERM | Limited budget. | = requirement(property="budget_limited", value=TRUE)  ⟵ candidate
- constraint_exclude_flowery_language | composite | constraint-value | TERM constraint_exclude_flowery_language() -> TERM | Avoid flowery language. | = exclude(item="flowery_language")  ⟵ candidate
- event_sadie_adler_unmasking | composite | event-value | TERM event_sadie_adler_unmasking() -> TERM | Sadie Adler taking off her hat and peeling skin. | = sequence(items=[activity(verb="remove", actor="Sadie Adler", object="hat"), activity(verb="peel", actor="Sadie Adler", object="skin")])  ⟵ candidate
- transform_remove_br | composite | transformation-value | TERM transform_remove_br() -> TERM | Remove <br /> tags. | = remove_literal(text="<br />")  ⟵ candidate

### claim relations

- duplicate_definition | claim_relation | CLAIM duplicate_definition(count: NUMBER, entity: TERM, location?: STRING / TERM) | Asserts that multiple duplicate copies or definitions of a code entity exist within a codebase or location. | not: an exact string equality check | aliases: duplicate_code, two_copies, duplicate_function  ⟵ candidate
- exists_in | claim_relation | CLAIM exists_in(subject: STRING / TERM, location: STRING / TERM) | Asserts that an entity, policy, or phenomenon exists within a geographical or conceptual location. spatial/locational existence. | aliases: present_in  ⟵ candidate
- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ core
- leads_to | claim_relation | CLAIM leads_to(cause: TERM, effect: TERM) | Asserts a conceptual consequence or progression from cause to effect. progression relation. | aliases: results_in  ⟵ candidate
- meets_needs | claim_relation | CLAIM meets_needs(subject: TERM, beneficiary: STRING / TERM) | Asserts that an item, activity, or plan satisfies the needs of a beneficiary. utility/satisfaction claim. | aliases: satisfies_needs  ⟵ candidate
- occurred_recently | claim_relation | CLAIM occurred_recently(target: CLAIM) | Asserts temporal recency of an asserted occurrence or claim. temporal recency qualifier. | aliases: recently_happened  ⟵ candidate
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ candidate
- works_best | claim_relation | CLAIM works_best(style: STRING, count: NUMBER, purpose: STRING) | Asserts an advisory evaluation of optimal event style and participant capacity. planning evaluation. | aliases: optimal_format  ⟵ candidate

### links

- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ core
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ core
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ core

### values

- art_character_profile | value | artifact-value | Descriptive character profile.  ⟵ candidate
- art_short_text | value | artifact-value | Short free text.  ⟵ candidate
- art_structured_report | value | artifact-value | Headed/structured report.  ⟵ candidate
- cuisine_arab | value | cuisine-value | Arab culinary cuisine style. | not: cuisine_mediterranean (broader regional category) | aliases: Arab food, Arabic food, Arab cuisine  ⟵ candidate
- cuisine_mediterranean | value | cuisine-value | Mediterranean culinary cuisine style. | aliases: mediterranean  ⟵ candidate
- unit_character | value | duration-unit-value | One Unicode scalar value in the final rendered artifact; line endings are normalized to LF before counting. | aliases: characters, chars  ⟵ candidate
- unit_item | value | duration-unit-value | Top-level generated list or report item. | aliases: items, entries  ⟵ candidate
- bottle | value | entity-name | A bottle container object, typically used for holding liquids. | not: mug (a drinking cup with a handle) or water (the liquid itself) | aliases: bottle, water bottle, plastic bottle  ⟵ candidate
- bowl | value | entity-name | A container/dish used for holding food or small items. | aliases: bowl  ⟵ candidate
- cheese | value | entity-name | Dairy food item: cheese. | not: meat or non-dairy food items | aliases: cheese  ⟵ candidate
- cinnamon | value | entity-name | Ground or whole cinnamon culinary spice from Cinnamomum tree bark. | not: nutmeg, cloves, or other distinct spice varieties | aliases: cinnamon, ground cinnamon, cinnamon spice, cinnamon stick  ⟵ candidate
- clothing | value | entity-name | Physical item used for concealment or covering: clothing. | aliases: clothing  ⟵ candidate
- cloves | value | entity-name | Aromatic dried flower buds of Syzygium aromaticum used as a culinary spice. | not: cinnamon, nutmeg, or other distinct spice varieties | aliases: cloves, clove, ground cloves, whole cloves  ⟵ candidate
- coffee_maker | value | entity-name | A coffee-making appliance; not automatically a heating resource  ⟵ candidate
- dresser | value | entity-name | A chest of drawers / dresser furniture. | aliases: dresser  ⟵ candidate
- dried_fruit | value | entity-name | Generic dried fruit food item. | not: fresh fruit or specific dried varieties like raisin or sultana | aliases: dried fruit, dried fruits  ⟵ candidate
- dulce_de_leche | value | entity-name | Sweet caramelized milk confection or dessert spread: dulce de leche. | not: cheese or dulce_de_nata | aliases: dulce de leche, dulce_de_leche  ⟵ candidate
- dulce_de_nata | value | entity-name | Clotted cream milk confection or dessert item: dulce de nata. | not: dulce_de_leche or cheese | aliases: dulce de nata, dulce_de_nata  ⟵ candidate
- entity_checklist | value | entity-name | Event planning item or menu category: entity_checklist. | aliases: entity_checklist  ⟵ candidate
- entity_condensed_grocery_list | value | entity-name | Event planning item or menu category: entity_condensed_grocery_list. | aliases: entity_condensed_grocery_list  ⟵ candidate
- entity_desserts | value | entity-name | Event planning item or menu category: entity_desserts. | aliases: entity_desserts  ⟵ candidate
- entity_flowers | value | entity-name | Flowers, blossoms, or floral design elements. | not: constraint_exclude_flowery_language (a prose style constraint) or agricultural food items | aliases: flowers, floral, flower, floral decorations  ⟵ candidate
- entity_grocery_list | value | entity-name | Event planning item or menu category: entity_grocery_list. | aliases: entity_grocery_list  ⟵ candidate
- figurine | value | entity-name | A small carved, molded, or sculpted decorative statuette object. | not: character (a fictional persona) or captioned_figure (a document figure/photo) | aliases: figurine, statuette, statue, small statue, sculptural figure, miniature figure  ⟵ candidate
- fruit_juice | value | entity-name | Liquid juice extracted from fruit. | not: fermented wine or freshly crushed grape_must | aliases: fruit juice, juice  ⟵ candidate
- gift | value | entity-name | A physical gift or present item to be wrapped, given, or received. | not: egift_card (an electronic gift card or digital voucher product) | aliases: gift, present, wrapped gift, package  ⟵ candidate
- grape_merlot | value | entity-name | Merlot wine grape variety. | not: other red grape varieties such as grape_cabernet_sauvignon or grape_pinot_noir | aliases: Merlot, merlot grape  ⟵ candidate
- grape_pinot_noir | value | entity-name | Pinot Noir wine grape variety. | not: other red grape varieties such as grape_cabernet_sauvignon or grape_merlot | aliases: Pinot Noir, pinot noir grape  ⟵ candidate
- grape_thompson_seedless | value | entity-name | Thompson Seedless grape variety. | not: wine grape cultivars like grape_merlot or grape_chardonnay | aliases: Thompson Seedless, thompson seedless grape, sultana grape  ⟵ candidate
- maqluba | value | entity-name | Traditional Arab layered rice dish: maqluba. | not: cuisine_mediterranean (cuisine style rather than specific dish) | aliases: maqluba, makloubeh  ⟵ candidate
- mug | value | entity-name | Drinking cup. | aliases: mug  ⟵ candidate
- pear | value | entity-name | A pear fruit item, typically an ingredient or fresh fruit object. | not: apple, food_label::tomato, or other distinct fruit items | aliases: pear, pears, fresh pear, sliced pear  ⟵ candidate
- raisin | value | entity-name | Dried grape food item. | not: sultana (specifically dried white grape) or fresh wine_grape | aliases: raisin, raisins, dried grape  ⟵ candidate
- safe | value | entity-name | A secure, lockable metal storage container or receptacle for holding valuables. | not: cabinet (a general storage cupboard) or dresser (a chest of drawers) | aliases: safe, strongbox, lockbox, deposit box  ⟵ candidate
- scissors | value | entity-name | A handheld shearing cutting tool with two pivoted blades used for cutting paper, ribbon, and crafting materials. | not: knife (a kitchen or food preparation cutting utensil) | aliases: scissors, shears, pair of scissors  ⟵ candidate
- spatula | value | entity-name | A kitchen utensil with a broad, flat, and flexible blade used for lifting, flipping, or spreading food. | not: knife (cutting utensil) or spoon (scooping utensil) | aliases: spatula, turner, flipper  ⟵ candidate
- sponge | value | entity-name | A porous, absorbent sponge cleaning tool or object. | not: tissue_box (a paper tissue box) or other wiping materials | aliases: sponge, cleaning sponge  ⟵ candidate
- sultana | value | entity-name | Dried white seedless grape food product. | not: raisin (dark dried grape) or wine_grape | aliases: sultana, sultanas, golden raisin  ⟵ candidate
- tape | value | entity-name | Adhesive tape used for fastening and securing wrapping paper, boxes, or packaging materials. | not: waterproof_bandages (medical wound dressing) or waterproof_stickers (decorative stickers) | aliases: tape, adhesive tape, sticky tape, scotch tape  ⟵ candidate
- tissue_box | value | entity-name | A cardboard or plastic box containing paper tissues used for wiping or cleaning. | not: waterproof bandages or other medical coverings | aliases: tissue box, tissues, tissue  ⟵ candidate
- trash_can | value | entity-name | A waste receptacle container. | aliases: trash_can  ⟵ candidate
- vase | value | entity-name | A decorative or functional open container typically used for holding cut flowers or liquids. | not: bottle (a liquid storage container with a narrow neck) or bowl (a shallow dish) | aliases: vase, flower vase, flower_vase  ⟵ candidate
- waterproof_bandages | value | entity-name | Physical item used for concealment or covering: waterproof_bandages. | aliases: waterproof_bandages  ⟵ candidate
- waterproof_stickers | value | entity-name | Physical item used for concealment or covering: waterproof_stickers. | aliases: waterproof_stickers  ⟵ candidate
- wine_grape | value | entity-name | Grape variety cultivated specifically for winemaking. | not: table grapes or processed wine product | aliases: wine grape, wine grapes, grape  ⟵ candidate
- yarn | value | entity-name | Item or prop in joke/creative context: yarn. | aliases: yarn  ⟵ candidate
- format_bullet_list | value | format-value | Bulleted list. | aliases: bullet points  ⟵ candidate
- format_structured_report | value | format-value | Headed structured report layout. | aliases: structured report, report  ⟵ candidate
- locale_es | value | locale-value | Spanish. | aliases: spanish  ⟵ candidate
- metric_first_time_buyer | value | metric-value | Whether the customer is a first-time buyer. | aliases: first-time buyer, new customer  ⟵ candidate
- color_pink | value | product-attribute-value | Pink visual color qualifier. | not: color_label::red, color_label::purple, or other distinct color shades | aliases: pink, color_pink, blush pink, rose pink, pastel pink  ⟵ candidate
- material_memory_foam | value | product-attribute-value | Memory foam viscoelastic polyurethane material qualifier. | not: sponge (a porous cleaning tool) or generic bedding | aliases: memory foam, memory_foam, viscoelastic foam  ⟵ candidate
- size_large | value | product-attribute-value | Large size. | aliases: large, L  ⟵ candidate
- size_medium | value | product-attribute-value | Medium size. | aliases: medium, M  ⟵ candidate
- size_queen | value | product-attribute-value | Queen-size dimension classification for beds, mattresses, and bedding. | not: size_large (generic large apparel/goods size) or size_king | aliases: queen, queen size, Queen  ⟵ candidate
- size_small | value | product-attribute-value | Small size. | aliases: small, S  ⟵ candidate
- size_tall | value | product-attribute-value | Tall relative vertical dimension qualifier. | aliases: size_tall  ⟵ candidate
- on | value | spatial-relation | Resting atop. | aliases: on top of  ⟵ dependency of example_a_select_two_pillows_and_move_those_objects
- state_dirty | value | state-value | Dirty condition. | aliases: dirty  ⟵ candidate
- state_empty | value | state-value | Contains no intended material or usable remaining amount. | aliases: empty, used up  ⟵ candidate
- state_sliced | value | state-value | The condition of being sliced or cut into thin pieces. | not: the operation slice itself | aliases: sliced, slice, chopped, cut  ⟵ candidate
- style_catchy | value | style-value | Catchy, attention-grabbing style. | aliases: catchy  ⟵ candidate
- topic_current_events | value | topic-value | Current news, geopolitical events, and ongoing international developments. | aliases: current_events, news  ⟵ candidate
- topic_pickup_lines | value | topic-value | Pickup lines.  ⟵ candidate

### attributes

- quantity | attribute | attribute-name | Explicit count as NUMBER.  ⟵ candidate
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

