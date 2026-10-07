# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 31 needs (decomposition: llm), 154 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | speech_act | t1:s1 | introduce a theory or set of premises | `respond`, `propose`, `inform`, `subject`, `ask`, `supports`, `confirm`, `rule_structural_constructs`, `example_of`, `conjunction`, `propose_menu`, `property_question` |
| n2 | object | t1:s2 | bald eagle → `animal_label::<key>` | `resource_chiller`, `topic_baldurs_gate_3`, `oak_chips`, `earth`, `meat`, `animal_label`*, `art_structured_report`, `moon`, `tattoos`, `shape_oval`, `resource_heater`, `chair` |
| n3 | object | t1:s2 | green → `color_label::<key>` | `apple`, `lettuce`, `color_label`*, `right_of`, `left_of`, `grape_thompson_seedless`, `sultana`, `unit_day`, `shape_square`, `outshines`, `resource_chiller`, `resource_heater` |
| n4 | claim | t1:s2 | the bald eagle is green | `lettuce`, `apple`, `recommended`, `enables`, `leads_to`, `important`, `earth`, `statement`, `oak_chips`, `motivated_by`, `hover`, `causes` |
| n5 | object | t1:s3 | red → `color_label::<key>` | `color_label`*, `apple`, `color_pink`, `topic_current_events`, `right_of`, `cinnamon`, `resource_heater`, `pear`, `chair`, `resource_chiller`, `coffee_maker`, `ginger` |
| n6 | claim | t1:s3 | the bald eagle is red | `indicator`, `enables`, `recommended`, `leads_to`, `important`, `oak_chips`, `earth`, `statement`, `meat`, `motivated_by`, `apple`, `comfortable` |
| n7 | object | t1:s4 | cow → `animal_label::<key>` | `animal_label`*, `meat`, `dog`, `in_front_of`, `yakuza`, `dulce_de_nata`, `dulce_de_leche`, `resource_heater`, `cheese`, `coffee_maker`, `laptop`, `chair` |
| n8 | claim | t1:s4 | the cow is nice | `comfortable`, `animal_label`, `meat`, `important`, `recommended`, `enables`, `leads_to`, `condition_perfect`, `outcome`, `motivated_by`, `statement`, `causes` |
| n9 | object | t1:s5 | tiger → `animal_label::<key>` | `animal_label`*, `meat`, `cat_game`, `yakuza`, `tattoos`, `dog`, `dom_safari`, `cat_limited_time_offers`, `class_temple`, `right_of`, `art_character_profile`, `resource_heater` |
| n10 | claim | t1:s5 | the cow likes the tiger | `comfortable`, `animal_label`, `enables`, `leads_to`, `meat`, `important`, `recommended`, `dog`, `cat_game`, `motivated_by`, `causes`, `statement` |
| n11 | claim | t1:s6 | the cow needs the tiger | `meets_needs`, `meat`, `animal_label`, `enables`, `constraint_single_choice`, `leads_to`, `recommended`, `important`, `dog`, `yakuza`, `constraint_respectful`, `requirement` |
| n12 | object | t1:s7 | mouse → `animal_label::<key>` | `hover`, `laptop`, `dom_safari`, `topic_spider_man_2`, `animal_label`*, `fridge`, `pencil`, `pen`, `coffee_maker`, `piano`, `chair`, `resource_heater` |
| n13 | claim | t1:s7 | the mouse is nice | `enables`, `leads_to`, `hover`, `important`, `recommended`, `laptop`, `fridge`, `dom_safari`, `outcome`, `topic_spider_man_2`, `occurred_recently`, `statement` |
| n14 | claim | t1:s8 | the mouse needs the bald eagle | `meets_needs`, `topic_baldurs_gate_3`, `oak_chips`, `enables`, `hover`, `leads_to`, `recommended`, `topic_spider_man_2`, `important`, `statement`, `outcome`, `dom_safari` |
| n15 | claim | t1:s9 | the mouse sees the bald eagle | `enables`, `leads_to`, `oak_chips`, `hover`, `recommended`, `dom_safari`, `outcome`, `important`, `topic_baldurs_gate_3`, `occurred_recently`, `statement`, `topic_spider_man_2` |
| n16 | claim | t1:s10 | the tiger likes the bald eagle | `animal_label`, `enables`, `recommended`, `tattoos`, `leads_to`, `style_catchy`, `important`, `oak_chips`, `meat`, `statement`, `dom_safari`, `outcome` |
| n17 | claim | t1:s11 | the tiger needs the cow | `meets_needs`, `meat`, `animal_label`, `enables`, `constraint_single_choice`, `leads_to`, `recommended`, `yakuza`, `important`, `requirement`, `dog`, `constraint_respectful` |
| n18 | claim | t1:s12 | the tiger needs the mouse | `meets_needs`, `cat_game`, `enables`, `leads_to`, `dom_safari`, `oak_chips`, `animal_label`, `important`, `recommended`, `cat_limited_time_offers`, `topic_spider_man_2`, `occurred_recently` |
| n19 | reasoning | t1:s13 | if someone is young, then they need the tiger | `then`*, `rejects`, `constraint_17_plus`, `supports`, `meets_needs`, `requirement`, `animal_label`, `cat_game`, `constraint_respectful`, `contrast`, `yakuza`, `cat_limited_time_offers` |
| n20 | reasoning | t1:s14 | if the tiger is young, then the tiger is green | `then`*, `apple`, `rejects`, `constraint_17_plus`, `supports`, `metric_order_late`, `cat_game`, `contrast`, `yakuza`, `grape_thompson_seedless`, `cat_limited_time_offers`, `revises` |
| n21 | reasoning | t1:s15 | if someone needs the tiger, then the tiger sees the bald eagle | `then`*, `topic_baldurs_gate_3`, `supports`, `rejects`, `possesses`, `meets_needs`, `style_catchy`, `event_sadie_adler_unmasking`, `tattoos`, `animal_label`, `contrast`, `apple` |
| n22 | reasoning | t1:s16 | if someone sees the tiger and the tiger likes the bald eagle, then the bald eagle sees the tiger | `then`*, `style_catchy`, `entity_order_vs_assemble_plan`, `rejects`, `supports`, `topic_baldurs_gate_3`, `event_sadie_adler_unmasking`, `contrast`, `in_front_of`, `apple`, `distinguish`, `revises` |
| n23 | reasoning | t1:s17 | if someone is green and they see the bald eagle, then they are cold | `state_cold`*, `apple`, `then`*, `lettuce`, `rejects`, `supports`, `topic_baldurs_gate_3`, `style_catchy`, `contrast`, `illuminates`, `event_sadie_adler_unmasking`, `earth` |
| n24 | reasoning | t1:s18 | if someone is green and they like the tiger, then they see the bald eagle | `apple`, `then`*, `rejects`, `style_catchy`, `supports`, `animal_label`, `tattoos`, `topic_baldurs_gate_3`, `art_technical_explanation`, `oak_chips`, `contrast`, `event_sadie_adler_unmasking` |
| n25 | reasoning | t1:s19 | if the tiger is cold, then the tiger is young | `state_cold`*, `then`*, `constraint_17_plus`, `rejects`, `supports`, `metric_order_late`, `contrast`, `cat_limited_time_offers`, `at_least`, `cat_game`, `heat`, `state_warm` |
| n26 | reasoning | t1:s20 | if someone needs the tiger, then they like the tiger | `then`*, `rejects`, `supports`, `animal_label`, `meets_needs`, `cat_game`, `constraint_single_choice`, `yakuza`, `stereotype`, `contrast`, `meat`, `constraint_respectful` |
| n27 | reasoning | t1:s21 | if someone needs the mouse, then they are green | `apple`, `then`*, `hover`, `lettuce`, `rejects`, `supports`, `meets_needs`, `laptop`, `oak_chips`, `color_pink`, `contrast`, `fridge` |
| n28 | speech_act | t1:s22 | ask whether a statement is True, False, or Unknown | `ask`*, `statement`*, `confirm`, `respond`, `failure`, `inform`, `unaware`, `propose`, `rejects`, `negation`, `controversial`, `acknowledge` |
| n29 | constraint | t1:s22 | base the answer only on the provided theory | `respond`*, `extract`, `topic_baldurs_gate_3`, `subject`, `constraint_realistic`, `constraint_budget_limited`, `constraint_respectful`, `constraint_comprehensive`, `requirement`, `constraint_single_choice`, `supports`, `conjunction` |
| n30 | constraint | t1:s22 | answer must be True, False, or Unknown | `constraint_realistic`, `constraint_respectful`, `constraint_comprehensive`, `constraint_budget_limited`, `requirement`, `metric_order_late`, `constraint_single_choice`, `right_of`, `in_front_of`, `rejects`, `constraint_exclude_flowery_language`, `constraint_beginner` |
| n31 | action | t1:s23 | evaluate the statement: the tiger is young | `statement`*, `constraint_17_plus`, `at_least`, `metric_order_late`, `character_trait`, `size_small`, `block_evaluation`, `failure`, `unit_sentence`, `cat_limited_time_offers`, `rule_support_primitives_general`, `constraint_budget_limited` |

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

- subject.qualifier → platform_label
- subject.location → country
- requirement.value → platform_label
- heat.destination → object_label
- failure.system → platform_label
- activity.object → object_label, food_label, animal_label
- activity.location → country
- activity.instrument → object_label, platform_label
- measure.unit → currency
- attribute_claim.subject → platform_label
- attribute_claim.value → platform_label
- walk.destination → object_label

## Retrieved records

### Shared rules that govern the records below (full text)

**rule_lexical_groups** (v19/rule/lexical-groups; rule governing platform_label)

Section 3.1 defines value groups: `group::key` values of type ATOM[group]. Open groups admit any key of their form (examples are not whitelists); standard groups admit the codes of their bundled standard (ISO 3166-1 alpha-2 for country, ISO 4217 for currency). Leaf values are never glossary entries. Consumer signatures alone decide where a group may appear. Retired bare symbols are invalid.

**rule_reading_guide** (v19/rule/reading-guide; core)

The spec governs syntax/types; this glossary defines vocabulary. Signature notation: ? optional, A / B explicit alternatives, void no result. Omitted optional arguments are unspecified. Value entries are category-refined STRING primitives; complex meanings require composition. Aliases are contextual hints, not unconditional equivalences. Report ambiguity. IDs use v19/<category>/<symbol>, v19/support/<symbol> or v19/composite/<symbol>. Statuses apply to this candidate: Retained preserves meaning; Adapted uses the stated contract; Composite requires TERM (bare STRING deprecated); Structural is syntax/argument vocabulary; Needs clarification is unusable until resolved; Deprecated is historical; Accepted is usable within this candidate.

**rule_recording_signatures** (v19/rule/recording-signatures; rule governing hover)

RECORD ACTION uses the operation signature with REF[STRING] → TERM and LIST[REF[STRING]] → LIST[TERM]; other types/categories stay unchanged. Return EVENT, never the runtime result. Record actual outputs as attributed CLAIMs. Do not infer missing resources.

**rule_speech_acts_general** (v19/rule/speech-acts-general; rule governing respond)

UTTER-only, void, with the spec's speech attributes and LIST[TERM] constraints. No result binding. Literal content cannot replace required semantic arguments for structured coverage.

**rule_structural_constructs** (v19/rule/structural-constructs; candidate)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; rule governing supports)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_attributes_and_generate** (v19/rule/attributes-and-generate; rule governing art_structured_report)

Attribute entries name arguments; legality/types come from each operation, not global membership. GENERATE uses the spec's core fields; retained artifact profiles return STRING. Numeric/list results need explicit profiles. Legacy itinerary fields expand to TERM constraints: duration/duration_unit → duration(amount,unit); stop_min_per_day/stop_requirement → minimum_per_period(class,count,period=unit_day), never an inferred temple class; max_walk_duration/unit → maximum_between_stops(activity="walk",amount,unit). No legacy shorthand is enabled. Old events/character_properties/transformations become explicitly scoped TERM constraints. Message purpose is TERM, not send_email.content: GENERATE exact STRING content, then send. Report opaque fallback separately.

**rule_category_artifact_value** (v19/rule/category/artifact-value; rule governing art_structured_report)

STRING artifact class for GENERATE.target. art_story says what kind of artifact to produce, not what occurs in its plot.

**rule_category_constraint_value** (v19/rule/category/constraint-value; rule governing constraint_single_choice)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_descriptive_value** (v19/rule/category/descriptive-value; rule governing tattoos)

STRING modifier/domain label; never a free-form proposition. dom_sgi needs its intended referent established before semantically dependent use.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; rule governing unit_day)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing resource_chiller)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_event_value** (v19/rule/category/event-value; rule governing event_sadie_adler_unmasking)

TERM-described narrative event, not a recorded EVENT. Require inclusion explicitly when generating a story.

**rule_category_metric_value** (v19/rule/category/metric-value; rule governing metric_order_late)

STRING metric identity, not a Boolean value. Uptime and response time need numeric observations with units; order-late is Boolean-valued. Do not type every metric as BOOL.

**rule_category_product_attribute_value** (v19/rule/category/product-attribute-value; rule governing color_pink)

STRING color/size/product-market facets. gender_women describes a product category, not an assertion about a person's gender.

**rule_category_search_value** (v19/rule/category/search-value; rule governing cat_game)

STRING refinements rank_ / dir_ / cat_ / avail_ / genre_ are separate. rank_rating may fill rank_field; genre_label::comedy may not. “Cheapest” usually requires both rank_price and dir_asc, not rank_price alone.

**rule_category_semantic_category_value** (v19/rule/category/semantic-category-value; rule governing class_temple)

STRING class label used by typed constraints. class_temple describes a class, not an acquired physical temple reference.

**rule_category_shape_value** (v19/rule/category/shape-value; rule governing shape_oval)

STRING geometry. shape_round may select a circular object; it does not imply color or dimensions.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing right_of)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_state_value** (v19/rule/category/state-value; rule governing state_dirty)

STRING condition used in selection. state_warm does not command heat; “hot” is not automatically synonymous with “warm.”

**rule_category_style_value** (v19/rule/category/style-value; rule governing style_catchy)

STRING production style. style_narrative does not establish that described events occurred.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_baldurs_gate_3)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_composites_general** (v19/rule/composites-general; rule governing constraint_single_choice)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_operations_general** (v19/rule/operations-general; rule governing hover)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_supplemental_general** (v19/rule/supplemental-general; rule governing coffee_maker)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; candidate)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- extract | operation | operation-vocabulary | (target: LIST[REF[STRING]], limit: NUMBER) -> LIST[REF[STRING]] | First limit results, preserving order and identity; limit is a nonnegative integer; limit=1 is still a list  ⟵ candidate
- heat | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Heat using the stated resource; same identity. Selecting a warm object does not imply heating it.  ⟵ candidate
- hover | operation | operation-vocabulary | (target: REF[STRING]) -> void | Move pointer cursor over an interactive web element without clicking. target must resolve to a valid element reference. | aliases: mouse_over  ⟵ candidate
- turn | operation | operation-vocabulary | (direction: STRING) -> void | Rotate agent body/view orientation. direction is typically left, right, or angle. | aliases: rotate, turn_around  ⟵ related to then
- walk | operation | operation-vocabulary | (destination: STRING / TERM / ATOM[object_label], relation?: STRING) -> void | Locomote towards a target destination or landmark. destination must identify a valid entity or location. | aliases: move_to, go_to, navigate_to  ⟵ related to then

### speech acts

- acknowledge | speech_act | operation-vocabulary | UTTER acknowledge(target: CLAIM / TERM) | Acknowledge receipt/awareness; does not imply agreement.  ⟵ candidate
- ask | speech_act | operation-vocabulary | UTTER ask(target: TERM, or a sufficiently precise topic: STRING / TERM) | Request information/advice; not an assertion of an answer. | aliases: ask, how should  ⟵ candidate
- confirm | speech_act | operation-vocabulary | UTTER confirm(target: CLAIM) | Confirm the proposition; its evidence/status remains explicit.  ⟵ candidate
- inform | speech_act | operation-vocabulary | UTTER inform(target: CLAIM) | Present the proposition; preserve its holder/status.  ⟵ candidate
- propose | speech_act | operation-vocabulary | UTTER propose(target: TERM) | Suggest an action/idea; does not record it as performed.  ⟵ candidate
- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ dependency of event_sadie_adler_unmasking
- at_least | constructor | TERM at_least(measure: TERM) -> TERM | A lower bound: the constrained value is greater than or equal to the given measure (or number term). Use inside requirement(value=...). | not: an exact value; a strict 'more than' only when the source says so explicitly | aliases: at least, minimum, or more, no less than, plus  ⟵ candidate
- block_evaluation | constructor | TERM block_evaluation(block: STRING / TERM, maturity?: STRING, potential?: STRING, quality?: STRING, rank?: NUMBER, traps?: STRING) -> TERM | Constructs a structured evaluation, categorization, or ranking descriptor for a geological exploration block. | not: an external execution action or generic list sorting operation (use sort) | aliases: block assessment, block ranking, block rating, block categorization  ⟵ candidate
- character_trait | constructor | TERM character_trait(property: STRING, value: STRING / NUMBER) -> TERM | A character attribute | not: Not a claim about a real person  ⟵ candidate
- conditional | constructor | TERM conditional(condition: TERM, consequence: TERM) -> TERM | Constructs a structured conditional proposition term connecting a condition and consequence. descriptive logic structure. | aliases: if_then  ⟵ candidate
- conjunction | constructor | TERM conjunction(items: LIST[TERM]) -> TERM | All described components apply | not: Does not imply temporal order  ⟵ candidate
- distinguish | constructor | TERM distinguish(first: TERM, second: TERM, criterion?: STRING / TERM) -> TERM | Constructs a descriptive representation of discerning or differentiating between two entities, conditions, or behaviors along an optional criterion. | not: visual_contrast (optical contrast) or LINK contrast (rhetorical opposition between claims) | aliases: tell the difference, differentiate, distinguish between  ⟵ candidate
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ dependency of constraint_exclude_flowery_language
- illuminates | constructor | TERM illuminates(target: STRING / TERM, source: STRING / TERM) -> TERM | Constructs a description of directional illumination where a light source casts light onto a target body. | not: an ambient color state or reflection (use reflects_light) | aliases: illuminates, shines on, shining towards  ⟵ candidate
- indicator | constructor | TERM indicator(condition: STRING / TERM, indicator_type?: STRING) -> TERM | Constructs a descriptive term representing a warning sign, behavioral marker, or red flag indicating an underlying condition or risk. | not: warning (a system alert claim relation) or color_label::red (a product color) | aliases: red flag, warning sign, behavioral marker, signal  ⟵ candidate
- measure | constructor | TERM measure(amount: NUMBER, unit: STRING / ATOM[currency]) -> TERM | A measured amount: a number with its unit symbol (a unit-category value such as unit_minute, cap_gb or currency::USD). Describes the amount only; asserts nothing. ATOM[currency] is also accepted and supplies the pinned currency identity; no exchange rate or conversion is implicit. | not: a symbol with the number baked in (char_age_18, size_16gb); a unitless count (use the quantity argument) | aliases: amount of, size of, measured in  ⟵ dependency of at_least
- negation | constructor | TERM negation(target: TERM) -> TERM | Constructs a descriptive semantic negation of a target descriptive proposition or condition term. | not: Check's runtime Boolean operator NOT or a speech-act decline | aliases: not, does not, negation, absence of  ⟵ candidate
- outshines | constructor | TERM outshines(brighter: STRING / TERM, dimmer: STRING / TERM) -> TERM | Constructs a description of relative visual brightness where a brighter light source overpowers the perceived brightness of a dimmer object. | not: an absolute numeric brightness measurement | aliases: outshines, overpowers brightness, drowns out light  ⟵ candidate
- property_question | constructor | TERM property_question(property: STRING, subject: STRING / TERM) -> TERM | An open request for a property of a subject | not: Does not supply the property's value  ⟵ candidate
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ candidate
- sequence | constructor | TERM sequence(items: LIST[TERM]) -> TERM | Ordered described activities/content | not: Not unordered conjunction  ⟵ dependency of event_sadie_adler_unmasking
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ candidate

### composites

- constraint_beginner | composite | constraint-value | TERM constraint_beginner() -> TERM | Targeted at beginners. | = requirement(property="audience_expertise", value="beginner")  ⟵ candidate
- constraint_budget_limited | composite | constraint-value | TERM constraint_budget_limited() -> TERM | Limited budget. | = requirement(property="budget_limited", value=TRUE)  ⟵ candidate
- constraint_comprehensive | composite | constraint-value | TERM constraint_comprehensive() -> TERM | Must be comprehensive. | = requirement(property="comprehensive", value=TRUE)  ⟵ candidate
- constraint_exclude_flowery_language | composite | constraint-value | TERM constraint_exclude_flowery_language() -> TERM | Avoid flowery language. | = exclude(item="flowery_language")  ⟵ candidate
- constraint_realistic | composite | constraint-value | TERM constraint_realistic() -> TERM | Must be realistic. | = requirement(property="realistic", value=TRUE)  ⟵ candidate
- constraint_respectful | composite | constraint-value | TERM constraint_respectful() -> TERM | Must be respectful. | = requirement(property="respectful", value=TRUE)  ⟵ candidate
- constraint_single_choice | composite | constraint-value | TERM constraint_single_choice() -> TERM | Must pick a single choice. | = requirement(property="choice_count", value=1)  ⟵ candidate
- event_sadie_adler_unmasking | composite | event-value | TERM event_sadie_adler_unmasking() -> TERM | Sadie Adler taking off her hat and peeling skin. | = sequence(items=[activity(verb="remove", actor="Sadie Adler", object="hat"), activity(verb="peel", actor="Sadie Adler", object="skin")])  ⟵ candidate

### claim relations

- associated_with | claim_relation | CLAIM associated_with(subject: STRING / TERM, concept: STRING / TERM) | Asserts a cultural, semantic, or historical association between a subject and concept. association claim. | aliases: linked_to, correlated_with  ⟵ candidate
- attribute_claim | claim_relation | CLAIM attribute_claim(subject: STRING / TERM / ATOM[platform_label], property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) | Asserts that a subject possesses a named property evaluated to a specific primitive or structured value. general property attribution claim. | aliases: property_value, word_property, has_property, property attribution  ⟵ related to statement
- causes | claim_relation | CLAIM causes(cause: CLAIM / TERM, effect: CLAIM) | Asserts a direct causal relationship producing an effect proposition. causal assertion. | aliases: produces  ⟵ candidate
- comfortable | claim_relation | CLAIM comfortable(person: TERM, value: BOOL) | Asserts whether a person or animal is comfortable in a situation. affective/state claim. | aliases: is_comfortable  ⟵ candidate
- controversial | claim_relation | CLAIM controversial(subject: STRING / TERM) | Asserts that a topic, policy, or practice is the subject of public debate or controversy. evaluative debate claim. | aliases: debated, disputed  ⟵ candidate
- enables | claim_relation | CLAIM enables(condition: TERM / CLAIM, outcome: TERM / CLAIM) | Asserts that an enabling condition or capability facilitates an outcome. enabling condition. | aliases: facilitates, allows  ⟵ candidate
- example_of | claim_relation | CLAIM example_of(example: TERM, concept: TERM) | Asserts that an instance or term exemplifies a general concept, pattern, or category. example and concept are descriptive terms. | aliases: exemplifies, instance_of  ⟵ candidate
- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ candidate
- has_state | claim_relation | CLAIM has_state(subject: TERM, state: STRING) | Asserts that an entity is currently in a physical, thermal, or operational state. state must be a valid state descriptor string. | aliases: in_state, state_is  ⟵ related to statement
- important | claim_relation | CLAIM important(target: TERM) | Asserts that a concept, activity, or condition is important or significant. evaluative importance claim. | aliases: significant  ⟵ candidate
- leads_to | claim_relation | CLAIM leads_to(cause: TERM, effect: TERM) | Asserts a conceptual consequence or progression from cause to effect. progression relation. | aliases: results_in  ⟵ candidate
- meets_needs | claim_relation | CLAIM meets_needs(subject: TERM, beneficiary: STRING / TERM) | Asserts that an item, activity, or plan satisfies the needs of a beneficiary. utility/satisfaction claim. | aliases: satisfies_needs  ⟵ candidate
- motivated_by | claim_relation | CLAIM motivated_by(claim: CLAIM, motive: STRING / TERM) | Asserts that an action, rule, or claim is motivated by an underlying motive or goal. motive explanation. | aliases: rationale_is  ⟵ candidate
- occurred_recently | claim_relation | CLAIM occurred_recently(target: CLAIM) | Asserts temporal recency of an asserted occurrence or claim. temporal recency qualifier. | aliases: recently_happened  ⟵ candidate
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ candidate
- possesses | claim_relation | CLAIM possesses(subject: STRING / TERM, item: TERM, value: BOOL) | Asserts whether a subject possesses or lacks a stated property, capability, or entity. possession assertion with boolean polarity. | aliases: holds_property  ⟵ candidate
- propose_menu | claim_relation | CLAIM propose_menu(menu: TERM) | Asserts the proposal of a comprehensive menu plan. planning proposal. | aliases: suggest_menu  ⟵ candidate
- recommended | claim_relation | CLAIM recommended(target: TERM / CLAIM) | Asserts an advisory recommendation that an activity or measure is advisable. advisory normative claim. | aliases: advisable  ⟵ candidate
- spatial_state | claim_relation | CLAIM spatial_state(relation: STRING, object: TERM, reference: TERM) | Asserts an observed spatial configuration between an object and a reference landmark. relation must specify spatial configuration. | aliases: placed_at, located_at  ⟵ related to statement
- statement | claim_relation | CLAIM statement(fact: TERM) | Foundational claim relation converting any descriptive TERM into an attributed, truth-evaluated assertion. universal fact assertion. | aliases: assert_fact, fact_claim, claim_statement  ⟵ candidate
- stereotype | claim_relation | CLAIM stereotype(target: STRING / TERM, trait: STRING / TERM) | Asserts that an attributed trait, generalization, or assumption about a demographic group or social category is a stereotype. | not: an individual character trait or verified fact | aliases: social_stereotype, generalization, bias  ⟵ candidate
- unaware | claim_relation | CLAIM unaware(person: STRING / TERM, topic: STRING / TERM) | Asserts epistemic lack of awareness regarding a topic, fact, or event. epistemic state. | aliases: ignorant_of  ⟵ candidate

### links

- contrast | link | LINK contrast(first: CLAIM, second: CLAIM) | Expresses rhetorical qualification, opposition, or contrast between two claims. link between claims. | aliases: qualification, however  ⟵ candidate
- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ candidate
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ candidate
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ candidate
- then | link | LINK then(previous: EVENT, next: EVENT) | Represents temporal sequence and succession between two events where next follows previous. previous and next must be event terms. | aliases: followed_by, after_which  ⟵ candidate

### values

- art_character_profile | value | artifact-value | Descriptive character profile.  ⟵ candidate
- art_story | value | artifact-value | Narrative story.  ⟵ candidate
- art_structured_report | value | artifact-value | Headed/structured report.  ⟵ candidate
- art_technical_explanation | value | artifact-value | Technical explanation of a concept.  ⟵ candidate
- constraint_17_plus | value | constraint-value | Rated 17+ or mature.  ⟵ candidate
- dom_ovr | value | descriptive-value | One-versus-rest domain concept.  ⟵ candidate
- dom_safari | value | descriptive-value | Safari domain concept. | aliases: safari  ⟵ candidate
- tattoos | value | descriptive-value | Descriptive concept of tattoos in cultural and social contexts. | aliases: tattoos  ⟵ candidate
- yakuza | value | descriptive-value | Descriptive concept of yakuza in cultural and social contexts. | aliases: yakuza  ⟵ candidate
- unit_day | value | duration-unit-value | Day. | aliases: days  ⟵ candidate
- unit_sentence | value | duration-unit-value | One grammatical sentence in text generation or constraint counting. | not: unit_paragraph (paragraph block) or unit_word (individual word) | aliases: sentence, sentences  ⟵ candidate
- unit_year | value | duration-unit-value | Year. | aliases: years  ⟵ candidate
- apple | value | entity-name | An apple fruit item, typically an ingredient or interactive food object. | not: food_label::tomato or other fruits/vegetables | aliases: apple, apples, red apple, green apple, apple slice  ⟵ candidate
- chair | value | entity-name | A chair furniture seat with a backrest. | not: object_label::armchair (specifically an object_label::armchair with side armrests) or object_label::sofa | aliases: chair, seat  ⟵ candidate
- cheese | value | entity-name | Dairy food item: cheese. | not: meat or non-dairy food items | aliases: cheese  ⟵ candidate
- cinnamon | value | entity-name | Ground or whole cinnamon culinary spice from Cinnamomum tree bark. | not: nutmeg, cloves, or other distinct spice varieties | aliases: cinnamon, ground cinnamon, cinnamon spice, cinnamon stick  ⟵ candidate
- coffee_maker | value | entity-name | A coffee-making appliance; not automatically a heating resource  ⟵ candidate
- dog | value | entity-name | Animal entity: dog. | not: animal_label::cat or animal_label::donkey | aliases: dog, dogs, canine, pup, puppy  ⟵ candidate
- dulce_de_leche | value | entity-name | Sweet caramelized milk confection or dessert spread: dulce de leche. | not: cheese or dulce_de_nata | aliases: dulce de leche, dulce_de_leche  ⟵ candidate
- dulce_de_nata | value | entity-name | Clotted cream milk confection or dessert item: dulce de nata. | not: dulce_de_leche or cheese | aliases: dulce de nata, dulce_de_nata  ⟵ candidate
- earth | value | entity-name | The planet Earth as an astronomical celestial body. | not: soil, ground surface, or electrical grounding | aliases: earth, the earth, planet earth, Earth  ⟵ candidate
- entity_order_vs_assemble_plan | value | entity-name | Event planning item or menu category: entity_order_vs_assemble_plan. | aliases: entity_order_vs_assemble_plan  ⟵ candidate
- fridge | value | entity-name | A refrigerator cooling appliance. | aliases: fridge  ⟵ candidate
- gift | value | entity-name | A physical gift or present item to be wrapped, given, or received. | not: egift_card (an electronic gift card or digital voucher product) | aliases: gift, present, wrapped gift, package  ⟵ candidate
- ginger | value | entity-name | Pungent aromatic spice root from Zingiber officinale used in cooking and baking. | not: cinnamon, cardamom, or other distinct spice varieties | aliases: ginger, ground ginger, fresh ginger, ginger root  ⟵ candidate
- grape_thompson_seedless | value | entity-name | Thompson Seedless grape variety. | not: wine grape cultivars like grape_merlot or grape_chardonnay | aliases: Thompson Seedless, thompson seedless grape, sultana grape  ⟵ candidate
- laptop | value | entity-name | A portable laptop computer physical object. | not: topic_macbook_pro_2017 (a generation topic label) | aliases: laptop, laptop computer, notebook  ⟵ candidate
- lettuce | value | entity-name | A head of lettuce or leafy green vegetable food item. | not: food_label::tomato or food_label::potato (other vegetable items) | aliases: lettuce, head of lettuce, salad greens  ⟵ candidate
- meat | value | entity-name | Food item: meat or beef. | not: animal_label::tuna or animal_label::fish (specific aquatic foods) | aliases: meat, beef  ⟵ candidate
- moon | value | entity-name | Earth's natural celestial satellite. | not: an artificial satellite or other planetary moon | aliases: moon, the moon, Luna  ⟵ candidate
- oak_chips | value | entity-name | Oak wood pieces or barrels used for wine aging and flavor extraction. | not: grape_tannin or structural chemical additives | aliases: oak chips, oak pieces, oak barrels  ⟵ candidate
- pear | value | entity-name | A pear fruit item, typically an ingredient or fresh fruit object. | not: apple, food_label::tomato, or other distinct fruit items | aliases: pear, pears, fresh pear, sliced pear  ⟵ candidate
- pen | value | entity-name | A writing instrument. | aliases: pen  ⟵ candidate
- pencil | value | entity-name | A pencil writing instrument. | aliases: pencil  ⟵ candidate
- piano | value | entity-name | A piano musical instrument or large furniture object. | not: topic_classical_piano or topic_jazz_piano (music genre topics) | aliases: piano, grand piano, upright piano, keyboard  ⟵ candidate
- resource_chiller | value | entity-name | Canonical abstract chilling resource when no particular appliance is named.  ⟵ candidate
- resource_heater | value | entity-name | Canonical abstract heating resource when no particular appliance is named.  ⟵ candidate
- sultana | value | entity-name | Dried white seedless grape food product. | not: raisin (dark dried grape) or wine_grape | aliases: sultana, sultanas, golden raisin  ⟵ candidate
- metric_order_late | value | metric-value | Whether an order is late. | aliases: order is late, delayed  ⟵ candidate
- color_pink | value | product-attribute-value | Pink visual color qualifier. | not: color_label::red, color_label::purple, or other distinct color shades | aliases: pink, color_pink, blush pink, rose pink, pastel pink  ⟵ candidate
- condition_perfect | value | product-attribute-value | Product condition rating: perfect or mint physical and operational condition. | not: test_condition (software testing) or state_dirty (physical environmental state) | aliases: perfect, mint, pristine, flawless, like new  ⟵ candidate
- size_small | value | product-attribute-value | Small size. | aliases: small, S  ⟵ candidate
- cat_game | value | search-value | Category: video game.  ⟵ candidate
- cat_limited_time_offers | value | search-value | Category: time-limited deals.  ⟵ candidate
- class_temple | value | semantic-category-value | The abstract class of temples. | aliases: temple, temples  ⟵ candidate
- shape_oval | value | shape-value | Oval. | aliases: oval  ⟵ candidate
- shape_square | value | shape-value | Square. | aliases: square  ⟵ candidate
- in_front_of | value | spatial-relation | Positioned in front of. | aliases: in front of  ⟵ candidate
- left_of | value | spatial-relation | To the left of. | aliases: left of  ⟵ candidate
- right_of | value | spatial-relation | To the right of. | aliases: right of  ⟵ candidate
- state_cold | value | state-value | Cold or chilled condition. | aliases: cold, chilled  ⟵ candidate
- state_dirty | value | state-value | Dirty condition. | aliases: dirty  ⟵ candidate
- state_warm | value | state-value | Warm or heated condition. | aliases: warm, hot  ⟵ candidate
- style_catchy | value | style-value | Catchy, attention-grabbing style. | aliases: catchy  ⟵ candidate
- topic_baldurs_gate_3 | value | topic-value | Baldur's Gate 3.  ⟵ candidate
- topic_current_events | value | topic-value | Current news, geopolitical events, and ongoing international developments. | aliases: current_events, news  ⟵ candidate
- topic_macbook_pro_2017 | value | topic-value | MacBook Pro 2017.  ⟵ candidate
- topic_spider_man_2 | value | topic-value | Marvel's Spider-Man 2.  ⟵ candidate
