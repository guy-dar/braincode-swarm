# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 36 needs (decomposition: llm), 154 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | speech_act | t1:s1 | introduce a set of premises or a theory | `respond`, `propose`, `inform`, `ask`, `subject`, `supports`, `negation`, `topic_school_work_routine`, `confirm`, `rule_structural_constructs`, `example_of`, `acknowledge` |
| n2 | object | t1:s2 | bald eagle → `animal_label::<key>` | `resource_chiller`, `topic_baldurs_gate_3`, `meat`, `earth`, `oak_chips`, `animal_label`*, `moon`, `shape_oval`, `resource_heater`, `tattoos`, `art_structured_report`, `possesses` |
| n3 | object | t1:s2 | tiger → `animal_label::<key>` | `animal_label`*, `meat`, `yakuza`, `cat_game`, `tattoos`, `dog`, `class_temple`, `dom_safari`, `cat_limited_time_offers`, `resource_heater`, `resource_chiller`, `art_character_profile` |
| n4 | claim | t1:s2 | the bald eagle eats the tiger | `meat`, `oak_chips`, `enables`, `animal_label`, `recommended`, `leads_to`, `apple`, `statement`, `event_sadie_adler_unmasking`, `outcome`, `hover`, `occurred_recently` |
| n5 | claim | t1:s3 | the bald eagle does not need the tiger | `negation`*, `meets_needs`, `topic_baldurs_gate_3`, `enables`, `meat`, `recommended`, `leads_to`, `oak_chips`, `constraint_single_choice`, `animal_label`, `statement`, `important` |
| n6 | negation | t1:s3 | the bald eagle does not need the tiger | `negation`*, `exclude`, `constraint_exclude_liberation_theme`, `topic_baldurs_gate_3`, `ask`, `meat`, `rejects`, `constraint_single_choice`, `animal_label`, `oak_chips`, `constraint_respectful`, `decline` |
| n7 | object | t1:s4 | cow → `animal_label::<key>` | `animal_label`*, `meat`, `dog`, `dulce_de_nata`, `yakuza`, `dulce_de_leche`, `in_front_of`, `cheese`, `resource_heater`, `state_dirty`, `bread`, `heat` |
| n8 | claim | t1:s4 | the bald eagle sees the cow | `meat`, `animal_label`, `enables`, `leads_to`, `recommended`, `dog`, `statement`, `earth`, `outcome`, `motivated_by`, `occurred_recently`, `important` |
| n9 | claim | t1:s5 | the cow eats the bald eagle | `spoon`, `meat`, `animal_label`, `enables`, `leads_to`, `recommended`, `statement`, `comfortable`, `oak_chips`, `important`, `motivated_by`, `causes` |
| n10 | claim | t1:s6 | the cow is not nice | `comfortable`, `meat`, `failure`, `animal_label`, `leads_to`, `recommended`, `state_dirty`, `important`, `statement`, `enables`, `outcome`, `causes` |
| n11 | negation | t1:s6 | the cow is not nice | `negation`, `meat`, `animal_label`, `rejects`, `exclude`, `state_dirty`, `decline`, `failure`, `comfortable`, `constraint_exclude_flowery_language`, `grape_must`, `cheese` |
| n12 | object | t1:s7 | mouse → `animal_label::<key>` | `hover`, `dom_safari`, `laptop`, `topic_spider_man_2`, `animal_label`*, `fridge`, `pencil`, `pen`, `dom_ovr`, `resource_heater`, `resource_chiller`, `piano` |
| n13 | claim | t1:s7 | the mouse needs the bald eagle | `meets_needs`, `topic_baldurs_gate_3`, `oak_chips`, `hover`, `enables`, `leads_to`, `recommended`, `topic_spider_man_2`, `important`, `statement`, `outcome`, `dom_safari` |
| n14 | claim | t1:s8 | the tiger eats the cow | `meat`, `animal_label`, `enables`, `cuisine_indian`, `leads_to`, `statement`, `dog`, `recommended`, `outcome`, `cat_game`, `yakuza`, `important` |
| n15 | claim | t1:s9 | the tiger is rough | `meat`, `animal_label`, `yakuza`, `outcome`, `enables`, `leads_to`, `recommended`, `topic_greatest_cricketer_of_all_time`, `important`, `statement`, `occurred_recently`, `cat_game` |
| n16 | claim | t1:s10 | the tiger is not young | `constraint_17_plus`, `animal_label`, `meat`, `leads_to`, `enables`, `occurred_recently`, `outcome`, `recommended`, `cat_limited_time_offers`, `statement`, `important`, `cat_game` |
| n17 | negation | t1:s10 | the tiger is not young | `negation`, `constraint_17_plus`, `animal_label`, `exclude`, `rejects`, `meat`, `character_trait`, `cat_limited_time_offers`, `decline`, `cat_game`, `tattoos`, `constraint_exclude_flowery_language` |
| n18 | claim | t1:s11 | the tiger sees the bald eagle | `animal_label`, `enables`, `leads_to`, `recommended`, `statement`, `outcome`, `dom_safari`, `earth`, `tattoos`, `meat`, `oak_chips`, `motivated_by` |
| n19 | reasoning | t1:s12 | if the tiger needs and eats the cow, then the cow does not eat the bald eagle | `negation`*, `then`*, `meat`, `rejects`, `possesses`, `animal_label`, `supports`, `constraint_single_choice`, `constraint_respectful`, `meets_needs`, `event_sadie_adler_unmasking`, `topic_baldurs_gate_3` |
| n20 | negation | t1:s12 | the cow does not eat the bald eagle | `negation`*, `exclude`, `meat`, `animal_label`, `rejects`, `topic_baldurs_gate_3`, `decline`, `food_label`, `cuisine`, `dulce_de_nata`, `dog`, `earth` |
| n21 | reasoning | t1:s13 | if something sees the tiger, then it eats the mouse | `then`*, `hover`, `rejects`, `supports`, `animal_label`, `cat_game`, `event_sadie_adler_unmasking`, `cat_limited_time_offers`, `contrast`, `apple`, `meat`, `oak_chips` |
| n22 | reasoning | t1:s14 | if something is nice, then it is rough | `then`*, `rejects`, `supports`, `comfortable`, `style_catchy`, `constraint_respectful`, `contrast`, `tone_silly`, `well_wishes`, `tone_polite`, `state_dirty`, `tone_empathetic` |
| n23 | constraint | t1:s15 | red → `color_label::<key>` | `color_label`*, `constraint_budget_limited`, `constraint_respectful`, `constraint_realistic`, `constraint_exclude_flowery_language`, `constraint_single_choice`, `color_pink`, `requirement`, `constraint_comprehensive`, `constraint_exclude_liberation_theme`, `constraint_include_character_attribute_list`, `cinnamon` |
| n24 | reasoning | t1:s15 | if something is red, then it is not young | `then`*, `color_label`, `rejects`, `supports`, `constraint_17_plus`, `contrast`, `negation`, `rule_support_primitives_general`, `color_pink`, `topic_profanity`, `revises`, `outshines` |
| n25 | negation | t1:s15 | not young | `negation`, `constraint_17_plus`, `rejects`, `exclude`, `rule_support_primitives_general`, `decline`, `constraint_budget_limited`, `topic_profanity`, `size_small`, `constraint_exclude_flowery_language`, `role_son`, `role_mother` |
| n26 | reasoning | t1:s16 | if something needs the mouse, then the mouse does not need the bald eagle | `negation`*, `hover`, `then`*, `rejects`, `possesses`, `meets_needs`, `supports`, `entity_order_vs_assemble_plan`, `topic_pickup_lines`, `topic_baldurs_gate_3`, `oak_chips`, `contrast` |
| n27 | negation | t1:s16 | the mouse does not need the bald eagle | `negation`*, `hover`, `exclude`, `oak_chips`, `rejects`, `topic_baldurs_gate_3`, `entity_order_vs_assemble_plan`, `decline`, `constraint_17_plus`, `constraint_exclude_flowery_language`, `topic_spider_man_2`, `laptop` |
| n28 | reasoning | t1:s17 | if the mouse needs the cow and the cow needs the tiger, then the cow sees the mouse | `then`*, `rejects`, `meets_needs`, `dog`, `supports`, `topic_pickup_lines`, `in_front_of`, `meat`, `causes`, `cat_game`, `unit_sentence`, `cat_limited_time_offers` |
| n29 | reasoning | t1:s18 | if something eats the mouse, then the mouse sees the cow | `then`*, `hover`, `distinguish`, `rejects`, `meat`, `supports`, `dog`, `in_front_of`, `style_catchy`, `topic_baldurs_gate_3`, `event_camper_in_sludge_pit`, `cat_game` |
| n30 | reasoning | t1:s19 | if something eats the bald eagle, then the bald eagle is nice | `then`*, `food_label`, `spoon`, `possesses`, `rejects`, `meat`, `supports`, `apple`, `topic_baldurs_gate_3`, `style_catchy`, `oak_chips`, `contrast` |
| n31 | reasoning | t1:s20 | if something sees the cow, then it sees the tiger | `then`*, `distinguish`, `visual_contrast`, `rejects`, `meat`, `supports`, `animal_label`, `dog`, `comfortable`, `in_front_of`, `contrast`, `style_catchy` |
| n32 | speech_act | t1:s21 | ask whether a statement is True, False, or Unknown | `ask`*, `statement`*, `confirm`, `respond`, `unaware`, `inform`, `failure`, `negation`, `rejects`, `propose`, `acknowledge`, `controversial` |
| n33 | constraint | t1:s21 | rely only on the provided theory | `constraint_realistic`, `constraint_budget_limited`, `constraint_respectful`, `constraint_single_choice`, `requirement`, `constraint_comprehensive`, `rejects`, `constraint_include_character_attribute_list`, `constraint_beginner`, `subject`, `constraint_exclude_flowery_language`, `failure` |
| n34 | constraint | t1:s21 | answer must be True, False, or Unknown | `constraint_realistic`, `constraint_respectful`, `constraint_budget_limited`, `constraint_comprehensive`, `requirement`, `constraint_single_choice`, `metric_order_late`, `rejects`, `failure`, `constraint_include_character_attribute_list`, `unaware`, `right_of` |
| n35 | claim | t1:s22 | the mouse does not see the tiger | `negation`*, `unaware`, `failure`, `leads_to`, `sym_pandas_testing_assert_almost_equal`, `hover`, `animal_label`, `enables`, `causes`, `recommended`, `path_pandas_src_testing_pyx`, `cat_game` |
| n36 | negation | t1:s22 | the mouse does not see the tiger | `negation`*, `hover`, `rejects`, `failure`, `exclude`, `unaware`, `sym_pandas_testing_assert_almost_equal`, `animal_label`, `path_pandas_src_testing_pyx`, `cat_game`, `topic_spider_man_2`, `oak_chips` |

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
- heat.destination → object_label
- failure.system → platform_label
- requirement.value → platform_label
- activity.object → object_label, food_label, animal_label
- activity.location → country
- activity.instrument → object_label, platform_label
- attribute_claim.subject → platform_label
- attribute_claim.value → platform_label
- walk.destination → object_label

## Retrieved records

### Shared rules that govern the records below (full text)

**rule_lexical_groups** (v19/rule/lexical-groups; rule governing platform_label)

Section 3.1 defines value groups: `group::key` values of type ATOM[group]. Open groups admit any key of their form (examples are not whitelists); standard groups admit the codes of their bundled standard (ISO 3166-1 alpha-2 for country, ISO 4217 for currency). Leaf values are never glossary entries. Consumer signatures alone decide where a group may appear. Retired bare symbols are invalid.

**rule_reading_guide** (v19/rule/reading-guide; core)

The spec governs syntax/types; this glossary defines vocabulary. Signature notation: ? optional, A / B explicit alternatives, void no result. Omitted optional arguments are unspecified. Value entries are category-refined STRING primitives; complex meanings require composition. Aliases are contextual hints, not unconditional equivalences. Report ambiguity. IDs use v19/<category>/<symbol>, v19/support/<symbol> or v19/composite/<symbol>. Statuses apply to this candidate: Retained preserves meaning; Adapted uses the stated contract; Composite requires TERM (bare STRING deprecated); Structural is syntax/argument vocabulary; Needs clarification is unusable until resolved; Deprecated is historical; Accepted is usable within this candidate.

**rule_recording_signatures** (v19/rule/recording-signatures; rule governing heat)

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

**rule_category_code_value** (v19/rule/category/code-value; rule governing sym_pandas_testing_assert_almost_equal)

path_/sym_ remain STRING identities; migrated chg_/assert_ are TERM constructors. Do not recover an exact file path by guessing from underscores.

**rule_category_constraint_value** (v19/rule/category/constraint-value; rule governing constraint_single_choice)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_cuisine_value** (v19/rule/category/cuisine-value; rule governing cuisine_indian)

STRING cuisine class; cuisine_indian is a cuisine filter, not the location India.

**rule_category_descriptive_value** (v19/rule/category/descriptive-value; rule governing tattoos)

STRING modifier/domain label; never a free-form proposition. dom_sgi needs its intended referent established before semantically dependent use.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; rule governing unit_sentence)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing resource_chiller)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_event_value** (v19/rule/category/event-value; rule governing event_sadie_adler_unmasking)

TERM-described narrative event, not a recorded EVENT. Require inclusion explicitly when generating a story.

**rule_category_metric_value** (v19/rule/category/metric-value; rule governing metric_order_late)

STRING metric identity, not a Boolean value. Uptime and response time need numeric observations with units; order-late is Boolean-valued. Do not type every metric as BOOL.

**rule_category_product_attribute_value** (v19/rule/category/product-attribute-value; rule governing color_pink)

STRING color/size/product-market facets. gender_women describes a product category, not an assertion about a person's gender.

**rule_category_recipient_value** (v19/rule/category/recipient-value; rule governing role_son)

STRING roles or explicit named recipients. A role is not an exact person's identity. Keep an explicit name where substituting a role loses information.

**rule_category_search_value** (v19/rule/category/search-value; rule governing cat_game)

STRING refinements rank_ / dir_ / cat_ / avail_ / genre_ are separate. rank_rating may fill rank_field; genre_label::comedy may not. “Cheapest” usually requires both rank_price and dir_asc, not rank_price alone.

**rule_category_semantic_category_value** (v19/rule/category/semantic-category-value; rule governing class_temple)

STRING class label used by typed constraints. class_temple describes a class, not an acquired physical temple reference.

**rule_category_shape_value** (v19/rule/category/shape-value; rule governing shape_oval)

STRING geometry. shape_round may select a circular object; it does not imply color or dimensions.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing in_front_of)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_state_value** (v19/rule/category/state-value; rule governing state_dirty)

STRING condition used in selection. state_warm does not command heat; “hot” is not automatically synonymous with “warm.”

**rule_category_style_value** (v19/rule/category/style-value; rule governing style_catchy)

STRING production style. style_narrative does not establish that described events occurred.

**rule_category_tone_value** (v19/rule/category/tone-value; rule governing tone_silly)

STRING register. tone_urgent describes urgency, not a concrete deadline.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_school_work_routine)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_composites_general** (v19/rule/composites-general; rule governing topic_school_work_routine)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_operations_general** (v19/rule/operations-general; rule governing heat)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_support_primitives_general** (v19/rule/support-primitives-general; candidate)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- heat | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Heat using the stated resource; same identity. Selecting a warm object does not imply heating it.  ⟵ candidate
- hover | operation | operation-vocabulary | (target: REF[STRING]) -> void | Move pointer cursor over an interactive web element without clicking. target must resolve to a valid element reference. | aliases: mouse_over  ⟵ candidate
- turn | operation | operation-vocabulary | (direction: STRING) -> void | Rotate agent body/view orientation. direction is typically left, right, or angle. | aliases: rotate, turn_around  ⟵ related to then
- walk | operation | operation-vocabulary | (destination: STRING / TERM / ATOM[object_label], relation?: STRING) -> void | Locomote towards a target destination or landmark. destination must identify a valid entity or location. | aliases: move_to, go_to, navigate_to  ⟵ related to then

### speech acts

- acknowledge | speech_act | operation-vocabulary | UTTER acknowledge(target: CLAIM / TERM) | Acknowledge receipt/awareness; does not imply agreement.  ⟵ candidate
- ask | speech_act | operation-vocabulary | UTTER ask(target: TERM, or a sufficiently precise topic: STRING / TERM) | Request information/advice; not an assertion of an answer. | aliases: ask, how should  ⟵ candidate
- confirm | speech_act | operation-vocabulary | UTTER confirm(target: CLAIM) | Confirm the proposition; its evidence/status remains explicit.  ⟵ candidate
- correct | speech_act | operation-vocabulary | UTTER correct(target: CLAIM) | Offer corrected content. Actual supersession requires the Conversation revision rules.  ⟵ candidate
- decline | speech_act | operation-vocabulary | UTTER decline(target: TERM) | Decline the represented request/proposal; not negate every proposition within it.  ⟵ candidate
- inform | speech_act | operation-vocabulary | UTTER inform(target: CLAIM) | Present the proposition; preserve its holder/status.  ⟵ candidate
- propose | speech_act | operation-vocabulary | UTTER propose(target: TERM) | Suggest an action/idea; does not record it as performed.  ⟵ candidate
- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ dependency of event_sadie_adler_unmasking
- character_trait | constructor | TERM character_trait(property: STRING, value: STRING / NUMBER) -> TERM | A character attribute | not: Not a claim about a real person  ⟵ candidate
- conjunction | constructor | TERM conjunction(items: LIST[TERM]) -> TERM | All described components apply | not: Does not imply temporal order  ⟵ dependency of topic_school_work_routine
- distinguish | constructor | TERM distinguish(first: TERM, second: TERM, criterion?: STRING / TERM) -> TERM | Constructs a descriptive representation of discerning or differentiating between two entities, conditions, or behaviors along an optional criterion. | not: visual_contrast (optical contrast) or LINK contrast (rhetorical opposition between claims) | aliases: tell the difference, differentiate, distinguish between  ⟵ candidate
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ candidate
- include | constructor | TERM include(item: STRING / TERM) -> TERM | Require the identified content/item | not: Not permission to invent an instance in a recorded trace  ⟵ dependency of constraint_include_character_attribute_list
- negation | constructor | TERM negation(target: TERM) -> TERM | Constructs a descriptive semantic negation of a target descriptive proposition or condition term. | not: Check's runtime Boolean operator NOT or a speech-act decline | aliases: not, does not, negation, absence of  ⟵ candidate
- outshines | constructor | TERM outshines(brighter: STRING / TERM, dimmer: STRING / TERM) -> TERM | Constructs a description of relative visual brightness where a brighter light source overpowers the perceived brightness of a dimmer object. | not: an absolute numeric brightness measurement | aliases: outshines, overpowers brightness, drowns out light  ⟵ candidate
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ candidate
- sequence | constructor | TERM sequence(items: LIST[TERM]) -> TERM | Ordered described activities/content | not: Not unordered conjunction  ⟵ dependency of event_sadie_adler_unmasking
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ candidate
- visual_contrast | constructor | TERM visual_contrast(background: STRING / TERM, foreground: STRING / TERM) -> TERM | Constructs a descriptive term representing the optical contrast between a foreground object and its surrounding background environment. | not: a rhetorical claim link (use LINK contrast) | aliases: visual contrast, contrast against, contrast with background  ⟵ candidate
- well_wishes | constructor | TERM well_wishes(recipient?: STRING / TERM, sentiment?: STRING) -> TERM | Constructs a conversational discourse term representing well-wishes, good luck expressions, or parting encouragement. | not: a salutation greeting (use greeting) or apology (use apologize) | aliases: good_luck, best_wishes, encouragement  ⟵ candidate

### composites

- constraint_beginner | composite | constraint-value | TERM constraint_beginner() -> TERM | Targeted at beginners. | = requirement(property="audience_expertise", value="beginner")  ⟵ candidate
- constraint_budget_limited | composite | constraint-value | TERM constraint_budget_limited() -> TERM | Limited budget. | = requirement(property="budget_limited", value=TRUE)  ⟵ candidate
- constraint_comprehensive | composite | constraint-value | TERM constraint_comprehensive() -> TERM | Must be comprehensive. | = requirement(property="comprehensive", value=TRUE)  ⟵ candidate
- constraint_exclude_flowery_language | composite | constraint-value | TERM constraint_exclude_flowery_language() -> TERM | Avoid flowery language. | = exclude(item="flowery_language")  ⟵ candidate
- constraint_exclude_liberation_theme | composite | constraint-value | TERM constraint_exclude_liberation_theme() -> TERM | Avoid liberation theme. | = exclude(item="liberation_theme")  ⟵ candidate
- constraint_include_character_attribute_list | composite | constraint-value | TERM constraint_include_character_attribute_list() -> TERM | Include character attributes. | = include(item="character_attribute_list")  ⟵ candidate
- constraint_realistic | composite | constraint-value | TERM constraint_realistic() -> TERM | Must be realistic. | = requirement(property="realistic", value=TRUE)  ⟵ candidate
- constraint_respectful | composite | constraint-value | TERM constraint_respectful() -> TERM | Must be respectful. | = requirement(property="respectful", value=TRUE)  ⟵ candidate
- constraint_single_choice | composite | constraint-value | TERM constraint_single_choice() -> TERM | Must pick a single choice. | = requirement(property="choice_count", value=1)  ⟵ candidate
- event_camper_in_sludge_pit | composite | event-value | TERM event_camper_in_sludge_pit() -> TERM | Campers interacting in a sludge pit. | = activity(verb="interact", actor="campers", location="sludge_pit")  ⟵ candidate
- event_sadie_adler_unmasking | composite | event-value | TERM event_sadie_adler_unmasking() -> TERM | Sadie Adler taking off her hat and peeling skin. | = sequence(items=[activity(verb="remove", actor="Sadie Adler", object="hat"), activity(verb="peel", actor="Sadie Adler", object="skin")])  ⟵ candidate
- topic_greatest_cricketer_of_all_time | composite | topic-value | TERM topic_greatest_cricketer_of_all_time() -> TERM | Greatest cricketer of all time. | = subject(kind="cricketer", qualifier=requirement(property="rank_by_greatness", value=1), time="all_time")  ⟵ candidate
- topic_profanity | composite | topic-value | TERM topic_profanity() -> TERM | A composite term representing the topic of profanity. | = subject(kind="profanity") | not: potential_harms (which is generic) | aliases: profanity  ⟵ candidate
- topic_school_work_routine | composite | topic-value | TERM topic_school_work_routine() -> TERM | School and work routine. | = subject(kind="routine", qualifier=conjunction(items=[subject(kind="school"), subject(kind="work")]))  ⟵ candidate

### claim relations

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
- perceived_as | claim_relation | CLAIM perceived_as(subject: STRING / TERM, concept: STRING / TERM) | Asserts public perception attributing a quality, reputation, or image to a subject. perception attribution. | aliases: regarded_as  ⟵ candidate
- possesses | claim_relation | CLAIM possesses(subject: STRING / TERM, item: TERM, value: BOOL) | Asserts whether a subject possesses or lacks a stated property, capability, or entity. possession assertion with boolean polarity. | aliases: holds_property  ⟵ candidate
- recommended | claim_relation | CLAIM recommended(target: TERM / CLAIM) | Asserts an advisory recommendation that an activity or measure is advisable. advisory normative claim. | aliases: advisable  ⟵ candidate
- spatial_state | claim_relation | CLAIM spatial_state(relation: STRING, object: TERM, reference: TERM) | Asserts an observed spatial configuration between an object and a reference landmark. relation must specify spatial configuration. | aliases: placed_at, located_at  ⟵ related to statement
- statement | claim_relation | CLAIM statement(fact: TERM) | Foundational claim relation converting any descriptive TERM into an attributed, truth-evaluated assertion. universal fact assertion. | aliases: assert_fact, fact_claim, claim_statement  ⟵ candidate
- unaware | claim_relation | CLAIM unaware(person: STRING / TERM, topic: STRING / TERM) | Asserts epistemic lack of awareness regarding a topic, fact, or event. epistemic state. | aliases: ignorant_of  ⟵ candidate

### links

- contrast | link | LINK contrast(first: CLAIM, second: CLAIM) | Expresses rhetorical qualification, opposition, or contrast between two claims. link between claims. | aliases: qualification, however  ⟵ candidate
- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ candidate
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ candidate
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ candidate
- then | link | LINK then(previous: EVENT, next: EVENT) | Represents temporal sequence and succession between two events where next follows previous. previous and next must be event terms. | aliases: followed_by, after_which  ⟵ candidate

### values

- art_character_profile | value | artifact-value | Descriptive character profile.  ⟵ candidate
- art_structured_report | value | artifact-value | Headed/structured report.  ⟵ candidate
- path_pandas_src_testing_pyx | value | code-value | Source code file path or exported symbol in scientific Python: path_pandas_src_testing_pyx. | aliases: path_pandas_src_testing_pyx  ⟵ candidate
- sym_pandas_testing_assert_almost_equal | value | code-value | Source code file path or exported symbol in scientific Python: sym_pandas_testing_assert_almost_equal. | aliases: sym_pandas_testing_assert_almost_equal  ⟵ candidate
- constraint_17_plus | value | constraint-value | Rated 17+ or mature.  ⟵ candidate
- cuisine_indian | value | cuisine-value | Indian cuisine. | aliases: Indian food, Indian  ⟵ candidate
- dom_ovr | value | descriptive-value | One-versus-rest domain concept.  ⟵ candidate
- dom_safari | value | descriptive-value | Safari domain concept. | aliases: safari  ⟵ candidate
- tattoos | value | descriptive-value | Descriptive concept of tattoos in cultural and social contexts. | aliases: tattoos  ⟵ candidate
- yakuza | value | descriptive-value | Descriptive concept of yakuza in cultural and social contexts. | aliases: yakuza  ⟵ candidate
- unit_sentence | value | duration-unit-value | One grammatical sentence in text generation or constraint counting. | not: unit_paragraph (paragraph block) or unit_word (individual word) | aliases: sentence, sentences  ⟵ candidate
- apple | value | entity-name | An apple fruit item, typically an ingredient or interactive food object. | not: food_label::tomato or other fruits/vegetables | aliases: apple, apples, red apple, green apple, apple slice  ⟵ candidate
- bread | value | entity-name | A bread loaf or slice food object. | aliases: bread  ⟵ candidate
- caddy | value | entity-name | A portable storage caddy, organizer box, or supply tote for carrying and organizing handheld tools and supplies. | not: cabinet (a stationary furniture cupboard) or safe (a secure metal lockbox) | aliases: caddy, supply caddy, wrapping caddy, tool caddy, organizer caddy, supply tote  ⟵ candidate
- cheese | value | entity-name | Dairy food item: cheese. | not: meat or non-dairy food items | aliases: cheese  ⟵ candidate
- cinnamon | value | entity-name | Ground or whole cinnamon culinary spice from Cinnamomum tree bark. | not: nutmeg, cloves, or other distinct spice varieties | aliases: cinnamon, ground cinnamon, cinnamon spice, cinnamon stick  ⟵ candidate
- dog | value | entity-name | Animal entity: dog. | not: animal_label::cat or animal_label::donkey | aliases: dog, dogs, canine, pup, puppy  ⟵ candidate
- dulce_de_leche | value | entity-name | Sweet caramelized milk confection or dessert spread: dulce de leche. | not: cheese or dulce_de_nata | aliases: dulce de leche, dulce_de_leche  ⟵ candidate
- dulce_de_nata | value | entity-name | Clotted cream milk confection or dessert item: dulce de nata. | not: dulce_de_leche or cheese | aliases: dulce de nata, dulce_de_nata  ⟵ candidate
- earth | value | entity-name | The planet Earth as an astronomical celestial body. | not: soil, ground surface, or electrical grounding | aliases: earth, the earth, planet earth, Earth  ⟵ candidate
- entity_order_vs_assemble_plan | value | entity-name | Event planning item or menu category: entity_order_vs_assemble_plan. | aliases: entity_order_vs_assemble_plan  ⟵ candidate
- fridge | value | entity-name | A refrigerator cooling appliance. | aliases: fridge  ⟵ candidate
- grape_must | value | entity-name | Freshly crushed fruit juice mixture before fermentation. | not: clarified fruit_juice or finished wine | aliases: grape must, must  ⟵ candidate
- laptop | value | entity-name | A portable laptop computer physical object. | not: topic_macbook_pro_2017 (a generation topic label) | aliases: laptop, laptop computer, notebook  ⟵ candidate
- meat | value | entity-name | Food item: meat or beef. | not: animal_label::tuna or animal_label::fish (specific aquatic foods) | aliases: meat, beef  ⟵ candidate
- moon | value | entity-name | Earth's natural celestial satellite. | not: an artificial satellite or other planetary moon | aliases: moon, the moon, Luna  ⟵ candidate
- oak_chips | value | entity-name | Oak wood pieces or barrels used for wine aging and flavor extraction. | not: grape_tannin or structural chemical additives | aliases: oak chips, oak pieces, oak barrels  ⟵ candidate
- pen | value | entity-name | A writing instrument. | aliases: pen  ⟵ candidate
- pencil | value | entity-name | A pencil writing instrument. | aliases: pencil  ⟵ candidate
- piano | value | entity-name | A piano musical instrument or large furniture object. | not: topic_classical_piano or topic_jazz_piano (music genre topics) | aliases: piano, grand piano, upright piano, keyboard  ⟵ candidate
- resource_chiller | value | entity-name | Canonical abstract chilling resource when no particular appliance is named.  ⟵ candidate
- resource_heater | value | entity-name | Canonical abstract heating resource when no particular appliance is named.  ⟵ candidate
- resource_sink | value | entity-name | Canonical abstract washing resource when no particular sink is named.  ⟵ candidate
- spoon | value | entity-name | An eating or cooking utensil. | aliases: spoon  ⟵ candidate
- metric_order_late | value | metric-value | Whether an order is late. | aliases: order is late, delayed  ⟵ candidate
- color_pink | value | product-attribute-value | Pink visual color qualifier. | not: color_label::red, color_label::purple, or other distinct color shades | aliases: pink, color_pink, blush pink, rose pink, pastel pink  ⟵ candidate
- size_small | value | product-attribute-value | Small size. | aliases: small, S  ⟵ candidate
- role_mother | value | recipient-value | The mother of the user. | not: role_sister or role_kids | aliases: my mom, mother, mom  ⟵ candidate
- role_son | value | recipient-value | Son participant role in family or travel context. | not: role_daughter, role_sister, role_mother, or generic role_kids | aliases: son, my son  ⟵ candidate
- cat_game | value | search-value | Category: video game.  ⟵ candidate
- cat_limited_time_offers | value | search-value | Category: time-limited deals.  ⟵ candidate
- class_temple | value | semantic-category-value | The abstract class of temples. | aliases: temple, temples  ⟵ candidate
- shape_oval | value | shape-value | Oval. | aliases: oval  ⟵ candidate
- in_front_of | value | spatial-relation | Positioned in front of. | aliases: in front of  ⟵ candidate
- right_of | value | spatial-relation | To the right of. | aliases: right of  ⟵ candidate
- state_dirty | value | state-value | Dirty condition. | aliases: dirty  ⟵ candidate
- style_catchy | value | style-value | Catchy, attention-grabbing style. | aliases: catchy  ⟵ candidate
- tone_empathetic | value | tone-value | Conveys empathy/understanding. | aliases: sympathetically  ⟵ candidate
- tone_polite | value | tone-value | Courteous, respectful register. | aliases: politely, kindly  ⟵ candidate
- tone_silly | value | tone-value | Playful, lighthearted, or silly conversational tone. | aliases: silly  ⟵ candidate
- topic_baldurs_gate_3 | value | topic-value | Baldur's Gate 3.  ⟵ candidate
- topic_current_events | value | topic-value | Current news, geopolitical events, and ongoing international developments. | aliases: current_events, news  ⟵ candidate
- topic_pickup_lines | value | topic-value | Pickup lines.  ⟵ candidate
- topic_spider_man_2 | value | topic-value | Marvel's Spider-Man 2.  ⟵ candidate

### attributes

- cuisine | attribute | attribute-name | Restaurant or food cuisine from cuisine-value.  ⟵ candidate
