# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 32 needs (decomposition: llm), 157 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | speech_act | t1:s1 | introduce a set of premises or theory | `respond`, `propose`, `subject`, `ask`, `inform`, `supports`, `conjunction`, `example_of`, `negation`, `express_interest`, `confirm`, `topic_school_work_routine` |
| n2 | object | t1:s2 | cat → `animal_label::<key>` | `cat_game`, `cat_limited_time_offers`, `animal_label`*, `dog`, `caddy`, `apple`, `path_pandas_src_testing_pyx`, `meat`, `event_sadie_adler_unmasking`, `style_catchy`, `tattooed_guests`, `martini_glass` |
| n3 | object | t1:s2 | red → `color_label::<key>` | `color_label`*, `apple`, `color_pink`, `topic_current_events`, `cinnamon`, `right_of`, `gift`, `pear`, `ginger`, `coffee_maker`, `mug`, `resource_heater` |
| n4 | negation | t1:s2 | the cat is not red | `cat_game`, `cat_limited_time_offers`, `animal_label`, `negation`, `path_pandas_src_testing_pyx`, `rejects`, `event_sadie_adler_unmasking`, `sym_pandas_testing_assert_almost_equal`, `exclude`, `apple`, `constraint_exclude_flowery_language`, `caddy` |
| n5 | claim | t1:s2 | the cat is not red | `cat_game`, `cat_limited_time_offers`, `leads_to`, `enables`, `animal_label`, `path_pandas_src_testing_pyx`, `occurred_recently`, `causes`, `outcome`, `event_sadie_adler_unmasking`, `motivated_by`, `caddy` |
| n6 | object | t1:s3 | mouse → `animal_label::<key>` | `hover`, `laptop`, `animal_label`*, `topic_spider_man_2`, `dom_safari`, `caddy`, `pencil`, `coffee_maker`, `fridge`, `mug`, `pen`, `chair` |
| n7 | claim | t1:s3 | the cat needs the mouse | `cat_game`, `cat_limited_time_offers`, `meets_needs`, `leads_to`, `enables`, `caddy`, `occurred_recently`, `causes`, `animal_label`, `important`, `motivated_by`, `path_pandas_src_testing_pyx` |
| n8 | object | t1:s4 | tiger → `animal_label::<key>` | `animal_label`*, `cat_game`, `cat_limited_time_offers`, `meat`, `dog`, `yakuza`, `class_temple`, `dom_safari`, `tattoos`, `right_of`, `art_story`, `resource_heater` |
| n9 | claim | t1:s4 | the cat needs the tiger | `cat_limited_time_offers`, `cat_game`, `meets_needs`, `animal_label`, `enables`, `leads_to`, `occurred_recently`, `causes`, `important`, `recommended`, `meat`, `motivated_by` |
| n10 | object | t1:s5 | cow → `animal_label::<key>` | `animal_label`*, `meat`, `dog`, `in_front_of`, `yakuza`, `grape_must`, `dulce_de_nata`, `cheese`, `dulce_de_leche`, `coffee_maker`, `laptop`, `comfortable` |
| n11 | claim | t1:s5 | the cow eats the cat | `cat_game`, `cat_limited_time_offers`, `animal_label`, `meat`, `leads_to`, `enables`, `dog`, `occurred_recently`, `outcome`, `causes`, `motivated_by`, `important` |
| n12 | claim | t1:s6 | the cow is young | `leads_to`, `meat`, `occurred_recently`, `constraint_17_plus`, `enables`, `animal_label`, `outcome`, `causes`, `motivated_by`, `ongoing`, `important`, `recommended` |
| n13 | claim | t1:s7 | the mouse visits the cat | `cat_game`, `cat_limited_time_offers`, `leads_to`, `enables`, `occurred_recently`, `animal_label`, `path_pandas_src_testing_pyx`, `outcome`, `causes`, `ongoing`, `caddy`, `hover` |
| n14 | claim | t1:s8 | the tiger eats the cat | `cat_game`, `cat_limited_time_offers`, `animal_label`, `enables`, `leads_to`, `meat`, `occurred_recently`, `apple`, `outcome`, `causes`, `motivated_by`, `statement` |
| n15 | negation | t1:s9 | the tiger does not eat the cow | `negation`*, `exclude`, `meat`, `animal_label`, `cat_game`, `rejects`, `grape_thompson_seedless`, `decline`, `dog`, `constraint_exclude_flowery_language`, `rule_category_topic_value`, `grape_must` |
| n16 | claim | t1:s9 | the tiger does not eat the cow | `negation`*, `meat`, `animal_label`, `cat_game`, `leads_to`, `causes`, `enables`, `grape_thompson_seedless`, `motivated_by`, `occurred_recently`, `comfortable`, `statement` |
| n17 | claim | t1:s10 | the tiger is red | `indicator`, `cat_game`, `leads_to`, `animal_label`, `causes`, `path_pandas_src_testing_pyx`, `enables`, `meat`, `dog`, `motivated_by`, `important`, `outcome` |
| n18 | negation | t1:s11 | the tiger does not visit the cat | `negation`*, `cat_limited_time_offers`, `cat_game`, `animal_label`, `exclude`, `constraint_exclude_liberation_theme`, `rejects`, `unaware`, `grape_thompson_seedless`, `ask`, `decline`, `dog` |
| n19 | claim | t1:s11 | the tiger does not visit the cat | `negation`*, `cat_limited_time_offers`, `cat_game`, `unaware`, `leads_to`, `animal_label`, `enables`, `causes`, `occurred_recently`, `grape_thompson_seedless`, `motivated_by`, `recommended` |
| n20 | claim | t1:s12 | the tiger visits the cow | `comfortable`, `leads_to`, `cat_game`, `animal_label`, `cat_limited_time_offers`, `meat`, `dog`, `enables`, `path_pandas_src_testing_pyx`, `causes`, `occurred_recently`, `motivated_by` |
| n21 | claim | t1:s13 | the tiger visits the mouse | `cat_game`, `cat_limited_time_offers`, `leads_to`, `enables`, `occurred_recently`, `animal_label`, `path_pandas_src_testing_pyx`, `outcome`, `dom_safari`, `ongoing`, `causes`, `sym_pandas_testing_assert_almost_equal` |
| n22 | reasoning | t1:s14 | if the tiger visits the mouse, then the mouse eats the tiger | `then`*, `hover`, `cat_game`, `cat_limited_time_offers`, `rejects`, `dog`, `sym_pandas_testing_assert_almost_equal`, `revises`, `supports`, `event_camper_in_sludge_pit`, `associated_with`, `animal_label` |
| n23 | reasoning | t1:s15 | if someone is young and needs the mouse, then they eat the mouse | `then`*, `hover`, `spoon`, `rejects`, `constraint_17_plus`, `role_mother`, `meets_needs`, `supports`, `contrast`, `revises`, `topic_profanity`, `role_professor` |
| n24 | object | t1:s16 | green → `color_label::<key>` | `apple`, `color_label`*, `lettuce`, `grape_thompson_seedless`, `right_of`, `left_of`, `unit_day`, `sultana`, `coffee_maker`, `outshines`, `resource_chiller`, `resource_heater` |
| n25 | reasoning | t1:s16 | if someone eats the tiger, then they are green | `apple`, `then`*, `rejects`, `cat_game`, `supports`, `meat`, `grape_thompson_seedless`, `contrast`, `revises`, `yakuza`, `sultana`, `cuisine_italian` |
| n26 | reasoning | t1:s17 | if someone is green, then they are young | `then`*, `apple`, `lettuce`, `rejects`, `supports`, `constraint_17_plus`, `associated_with`, `outshines`, `contrast`, `grape_thompson_seedless`, `color_label`, `topic_profanity` |
| n27 | reasoning | t1:s18 | if someone is young, then they need the mouse | `then`*, `hover`, `rejects`, `constraint_17_plus`, `supports`, `meets_needs`, `role_mother`, `contrast`, `laptop`, `revises`, `topic_profanity`, `oak_chips` |
| n28 | action | t1:s19 | determine the truth value of a statement | `statement`*, `failure`, `test_condition`, `run_tests`, `motivated_by`, `supports`, `decision`, `assert_multinomial_scorer`, `calculation`, `confirm`, `example_d_record_an_actual_test_outcome_without_asserting_overall_correctness`, `obligation` |
| n29 | constraint | t1:s19 | base the answer only on the provided theory | `respond`*, `extract`, `subject`, `topic_baldurs_gate_3`, `constraint_budget_limited`, `constraint_realistic`, `constraint_exclude_flowery_language`, `causes`, `conjunction`, `failure`, `rejects`, `constraint_respectful` |
| n30 | constraint | t1:s19 | answer must be True, False, or Unknown | `constraint_realistic`, `failure`, `constraint_budget_limited`, `right_of`, `constraint_respectful`, `in_front_of`, `metric_order_late`, `constraint_exclude_flowery_language`, `rejects`, `constraint_comprehensive`, `unaware`, `respond`* |
| n31 | negation | t1:s20 | the cat does not eat the mouse | `negation`*, `cat_game`, `cat_limited_time_offers`, `animal_label`, `exclude`, `hover`, `path_pandas_src_testing_pyx`, `unaware`, `rejects`, `sym_pandas_testing_assert_almost_equal`, `decline`, `caddy` |
| n32 | claim | t1:s20 | the cat does not eat the mouse | `negation`*, `cat_game`, `cat_limited_time_offers`, `unaware`, `leads_to`, `path_pandas_src_testing_pyx`, `enables`, `causes`, `animal_label`, `occurred_recently`, `sym_pandas_testing_assert_almost_equal`, `motivated_by` |

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
- failure.system → platform_label
- run_tests.target → platform_label
- activity.object → object_label, food_label, animal_label
- activity.location → country
- activity.instrument → object_label, platform_label
- requirement.value → platform_label
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

**rule_structural_constructs** (v19/rule/structural-constructs; core)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; rule governing supports)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_attributes_and_generate** (v19/rule/attributes-and-generate; rule governing art_story)

Attribute entries name arguments; legality/types come from each operation, not global membership. GENERATE uses the spec's core fields; retained artifact profiles return STRING. Numeric/list results need explicit profiles. Legacy itinerary fields expand to TERM constraints: duration/duration_unit → duration(amount,unit); stop_min_per_day/stop_requirement → minimum_per_period(class,count,period=unit_day), never an inferred temple class; max_walk_duration/unit → maximum_between_stops(activity="walk",amount,unit). No legacy shorthand is enabled. Old events/character_properties/transformations become explicitly scoped TERM constraints. Message purpose is TERM, not send_email.content: GENERATE exact STRING content, then send. Report opaque fallback separately.

**rule_category_artifact_value** (v19/rule/category/artifact-value; rule governing art_story)

STRING artifact class for GENERATE.target. art_story says what kind of artifact to produce, not what occurs in its plot.

**rule_category_code_value** (v19/rule/category/code-value; rule governing path_pandas_src_testing_pyx)

path_/sym_ remain STRING identities; migrated chg_/assert_ are TERM constructors. Do not recover an exact file path by guessing from underscores.

**rule_category_constraint_value** (v19/rule/category/constraint-value; rule governing constraint_exclude_flowery_language)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_cuisine_value** (v19/rule/category/cuisine-value; rule governing cuisine_indian)

STRING cuisine class; cuisine_indian is a cuisine filter, not the location India.

**rule_category_descriptive_value** (v19/rule/category/descriptive-value; rule governing dom_safari)

STRING modifier/domain label; never a free-form proposition. dom_sgi needs its intended referent established before semantically dependent use.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; rule governing unit_day)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing dog)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_event_value** (v19/rule/category/event-value; rule governing event_sadie_adler_unmasking)

TERM-described narrative event, not a recorded EVENT. Require inclusion explicitly when generating a story.

**rule_category_locale_value** (v19/rule/category/locale-value; rule governing locale_en_gb)

STRING locale. “English” alone does not always mean locale_en_us; preserve ambiguity.

**rule_category_metric_value** (v19/rule/category/metric-value; rule governing metric_order_late)

STRING metric identity, not a Boolean value. Uptime and response time need numeric observations with units; order-late is Boolean-valued. Do not type every metric as BOOL.

**rule_category_product_attribute_value** (v19/rule/category/product-attribute-value; rule governing color_pink)

STRING color/size/product-market facets. gender_women describes a product category, not an assertion about a person's gender.

**rule_category_recipient_value** (v19/rule/category/recipient-value; rule governing tattooed_guests)

STRING roles or explicit named recipients. A role is not an exact person's identity. Keep an explicit name where substituting a role loses information.

**rule_category_search_value** (v19/rule/category/search-value; rule governing cat_game)

STRING refinements rank_ / dir_ / cat_ / avail_ / genre_ are separate. rank_rating may fill rank_field; genre_label::comedy may not. “Cheapest” usually requires both rank_price and dir_asc, not rank_price alone.

**rule_category_semantic_category_value** (v19/rule/category/semantic-category-value; rule governing class_temple)

STRING class label used by typed constraints. class_temple describes a class, not an acquired physical temple reference.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing right_of)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_style_value** (v19/rule/category/style-value; rule governing style_catchy)

STRING production style. style_narrative does not establish that described events occurred.

**rule_category_topic_value** (v19/rule/category/topic-value; candidate)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_composites_general** (v19/rule/composites-general; rule governing topic_school_work_routine)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_examples_general** (v19/rule/examples-general; rule governing example_d_record_an_actual_test_outcome_without_asserting_overall_correctness)

Examples use this glossary's contracts. They have not been verified by an implemented BrainCode parser.

**rule_operations_general** (v19/rule/operations-general; rule governing hover)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_supplemental_general** (v19/rule/supplemental-general; rule governing coffee_maker)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; rule governing subject)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- extract | operation | operation-vocabulary | (target: LIST[REF[STRING]], limit: NUMBER) -> LIST[REF[STRING]] | First limit results, preserving order and identity; limit is a nonnegative integer; limit=1 is still a list  ⟵ candidate
- hover | operation | operation-vocabulary | (target: REF[STRING]) -> void | Move pointer cursor over an interactive web element without clicking. target must resolve to a valid element reference. | aliases: mouse_over  ⟵ candidate
- run_tests | operation | operation-vocabulary | (target: STRING / ATOM[platform_label], assertion?: TERM) -> BOOL | Run the selected project's tests, optionally checking the specified assertion. TRUE means the declared test condition passed, not overall software correctness.  ⟵ candidate
- turn | operation | operation-vocabulary | (direction: STRING) -> void | Rotate agent body/view orientation. direction is typically left, right, or angle. | aliases: rotate, turn_around  ⟵ related to then
- walk | operation | operation-vocabulary | (destination: STRING / TERM / ATOM[object_label], relation?: STRING) -> void | Locomote towards a target destination or landmark. destination must identify a valid entity or location. | aliases: move_to, go_to, navigate_to  ⟵ related to then

### speech acts

- ask | speech_act | operation-vocabulary | UTTER ask(target: TERM, or a sufficiently precise topic: STRING / TERM) | Request information/advice; not an assertion of an answer. | aliases: ask, how should  ⟵ candidate
- confirm | speech_act | operation-vocabulary | UTTER confirm(target: CLAIM) | Confirm the proposition; its evidence/status remains explicit.  ⟵ candidate
- decline | speech_act | operation-vocabulary | UTTER decline(target: TERM) | Decline the represented request/proposal; not negate every proposition within it.  ⟵ candidate
- express_interest | speech_act | operation-vocabulary | UTTER express_interest(target: STRING / TERM) | Speech act expressing conversational interest or engagement in a topic. speech act in dialogic traces. | aliases: show_interest  ⟵ candidate
- inform | speech_act | operation-vocabulary | UTTER inform(target: CLAIM) | Present the proposition; preserve its holder/status.  ⟵ candidate
- propose | speech_act | operation-vocabulary | UTTER propose(target: TERM) | Suggest an action/idea; does not record it as performed.  ⟵ candidate
- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ dependency of event_sadie_adler_unmasking
- calculation | constructor | TERM calculation(inputs: LIST[TERM], operation: STRING, result?: TERM) -> TERM | Constructs a descriptive representation of an arithmetic or algorithmic calculation step with inputs, operation identifier, and optional resulting value. | not: an executed runtime action or factual claim of outcome | aliases: math_operation, compute_step  ⟵ candidate
- conjunction | constructor | TERM conjunction(items: LIST[TERM]) -> TERM | All described components apply | not: Does not imply temporal order  ⟵ candidate
- decision | constructor | TERM decision(activity: TERM) -> TERM | A decision whose content is the described activity | not: Not proof it was carried out  ⟵ candidate
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ candidate
- indicator | constructor | TERM indicator(condition: STRING / TERM, indicator_type?: STRING) -> TERM | Constructs a descriptive term representing a warning sign, behavioral marker, or red flag indicating an underlying condition or risk. | not: warning (a system alert claim relation) or color_label::red (a product color) | aliases: red flag, warning sign, behavioral marker, signal  ⟵ candidate
- negation | constructor | TERM negation(target: TERM) -> TERM | Constructs a descriptive semantic negation of a target descriptive proposition or condition term. | not: Check's runtime Boolean operator NOT or a speech-act decline | aliases: not, does not, negation, absence of  ⟵ candidate
- obligation | constructor | TERM obligation(actor: STRING / TERM, activity: TERM) -> TERM | Constructs a deontic obligation description requiring an actor to perform an activity. actor and activity specified. | aliases: duty, mandatory_activity  ⟵ candidate
- outshines | constructor | TERM outshines(brighter: STRING / TERM, dimmer: STRING / TERM) -> TERM | Constructs a description of relative visual brightness where a brighter light source overpowers the perceived brightness of a dimmer object. | not: an absolute numeric brightness measurement | aliases: outshines, overpowers brightness, drowns out light  ⟵ candidate
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ dependency of constraint_budget_limited
- sequence | constructor | TERM sequence(items: LIST[TERM]) -> TERM | Ordered described activities/content | not: Not unordered conjunction  ⟵ dependency of event_sadie_adler_unmasking
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ candidate
- test_condition | constructor | TERM test_condition(condition: STRING, expected: BOOL) -> TERM | A testable condition with the expected Boolean outcome | not: Expected outcome is not an observed result  ⟵ candidate

### composites

- assert_multinomial_scorer | composite | code-value | TERM assert_multinomial_scorer() -> TERM | Assertion that multinomial probabilistic scoring succeeds. | = test_condition(condition="multinomial_probabilistic_scoring", expected=TRUE)  ⟵ candidate
- constraint_budget_limited | composite | constraint-value | TERM constraint_budget_limited() -> TERM | Limited budget. | = requirement(property="budget_limited", value=TRUE)  ⟵ candidate
- constraint_comprehensive | composite | constraint-value | TERM constraint_comprehensive() -> TERM | Must be comprehensive. | = requirement(property="comprehensive", value=TRUE)  ⟵ candidate
- constraint_exclude_flowery_language | composite | constraint-value | TERM constraint_exclude_flowery_language() -> TERM | Avoid flowery language. | = exclude(item="flowery_language")  ⟵ candidate
- constraint_exclude_liberation_theme | composite | constraint-value | TERM constraint_exclude_liberation_theme() -> TERM | Avoid liberation theme. | = exclude(item="liberation_theme")  ⟵ candidate
- constraint_realistic | composite | constraint-value | TERM constraint_realistic() -> TERM | Must be realistic. | = requirement(property="realistic", value=TRUE)  ⟵ candidate
- constraint_respectful | composite | constraint-value | TERM constraint_respectful() -> TERM | Must be respectful. | = requirement(property="respectful", value=TRUE)  ⟵ candidate
- constraint_single_choice | composite | constraint-value | TERM constraint_single_choice() -> TERM | Must pick a single choice. | = requirement(property="choice_count", value=1)  ⟵ candidate
- event_camper_in_sludge_pit | composite | event-value | TERM event_camper_in_sludge_pit() -> TERM | Campers interacting in a sludge pit. | = activity(verb="interact", actor="campers", location="sludge_pit")  ⟵ candidate
- event_sadie_adler_unmasking | composite | event-value | TERM event_sadie_adler_unmasking() -> TERM | Sadie Adler taking off her hat and peeling skin. | = sequence(items=[activity(verb="remove", actor="Sadie Adler", object="hat"), activity(verb="peel", actor="Sadie Adler", object="skin")])  ⟵ candidate
- topic_profanity | composite | topic-value | TERM topic_profanity() -> TERM | A composite term representing the topic of profanity. | = subject(kind="profanity") | not: potential_harms (which is generic) | aliases: profanity  ⟵ candidate
- topic_school_work_routine | composite | topic-value | TERM topic_school_work_routine() -> TERM | School and work routine. | = subject(kind="routine", qualifier=conjunction(items=[subject(kind="school"), subject(kind="work")]))  ⟵ candidate

### claim relations

- associated_with | claim_relation | CLAIM associated_with(subject: STRING / TERM, concept: STRING / TERM) | Asserts a cultural, semantic, or historical association between a subject and concept. association claim. | aliases: linked_to, correlated_with  ⟵ candidate
- attribute_claim | claim_relation | CLAIM attribute_claim(subject: STRING / TERM / ATOM[platform_label], property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) | Asserts that a subject possesses a named property evaluated to a specific primitive or structured value. general property attribution claim. | aliases: property_value, word_property, has_property, property attribution  ⟵ related to statement
- causes | claim_relation | CLAIM causes(cause: CLAIM / TERM, effect: CLAIM) | Asserts a direct causal relationship producing an effect proposition. causal assertion. | aliases: produces  ⟵ candidate
- comfortable | claim_relation | CLAIM comfortable(person: TERM, value: BOOL) | Asserts whether a person or animal is comfortable in a situation. affective/state claim. | aliases: is_comfortable  ⟵ candidate
- enables | claim_relation | CLAIM enables(condition: TERM / CLAIM, outcome: TERM / CLAIM) | Asserts that an enabling condition or capability facilitates an outcome. enabling condition. | aliases: facilitates, allows  ⟵ candidate
- example_of | claim_relation | CLAIM example_of(example: TERM, concept: TERM) | Asserts that an instance or term exemplifies a general concept, pattern, or category. example and concept are descriptive terms. | aliases: exemplifies, instance_of  ⟵ candidate
- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ candidate
- has_state | claim_relation | CLAIM has_state(subject: TERM, state: STRING) | Asserts that an entity is currently in a physical, thermal, or operational state. state must be a valid state descriptor string. | aliases: in_state, state_is  ⟵ related to statement
- important | claim_relation | CLAIM important(target: TERM) | Asserts that a concept, activity, or condition is important or significant. evaluative importance claim. | aliases: significant  ⟵ candidate
- leads_to | claim_relation | CLAIM leads_to(cause: TERM, effect: TERM) | Asserts a conceptual consequence or progression from cause to effect. progression relation. | aliases: results_in  ⟵ candidate
- meets_needs | claim_relation | CLAIM meets_needs(subject: TERM, beneficiary: STRING / TERM) | Asserts that an item, activity, or plan satisfies the needs of a beneficiary. utility/satisfaction claim. | aliases: satisfies_needs  ⟵ candidate
- motivated_by | claim_relation | CLAIM motivated_by(claim: CLAIM, motive: STRING / TERM) | Asserts that an action, rule, or claim is motivated by an underlying motive or goal. motive explanation. | aliases: rationale_is  ⟵ candidate
- occurred_recently | claim_relation | CLAIM occurred_recently(target: CLAIM) | Asserts temporal recency of an asserted occurrence or claim. temporal recency qualifier. | aliases: recently_happened  ⟵ candidate
- ongoing | claim_relation | CLAIM ongoing(target: TERM) | Asserts that a conflict, process, or initiative is actively ongoing. temporal aspect claim. | aliases: in_progress  ⟵ candidate
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ candidate
- prohibited | claim_relation | CLAIM prohibited(subject: STRING / TERM, location: STRING / TERM, condition?: STRING / TERM) | Asserts that a subject is prohibited from a location or activity under specified conditions. deontic prohibition claim. | aliases: forbidden, banned_from  ⟵ related to obligation
- proposed_policy | claim_relation | CLAIM proposed_policy(policy: TERM, requirements: LIST[TERM]) | Asserts that a proposed policy framework comprises the specified requirement terms. policy must be a policy term. | aliases: policy_proposal  ⟵ related to obligation
- recommended | claim_relation | CLAIM recommended(target: TERM / CLAIM) | Asserts an advisory recommendation that an activity or measure is advisable. advisory normative claim. | aliases: advisable  ⟵ candidate
- spatial_state | claim_relation | CLAIM spatial_state(relation: STRING, object: TERM, reference: TERM) | Asserts an observed spatial configuration between an object and a reference landmark. relation must specify spatial configuration. | aliases: placed_at, located_at  ⟵ related to statement
- statement | claim_relation | CLAIM statement(fact: TERM) | Foundational claim relation converting any descriptive TERM into an attributed, truth-evaluated assertion. universal fact assertion. | aliases: assert_fact, fact_claim, claim_statement  ⟵ candidate
- unaware | claim_relation | CLAIM unaware(person: STRING / TERM, topic: STRING / TERM) | Asserts epistemic lack of awareness regarding a topic, fact, or event. epistemic state. | aliases: ignorant_of  ⟵ candidate
- validates_parameter | claim_relation | CLAIM validates_parameter(condition: STRING, entity: TERM, parameter: STRING) | Asserts that a code entity inspects or validates parameter names or types for a specified condition. | not: a runtime assertion test | aliases: inspects_parameter, checks_parameter, validates_parameter_names  ⟵ candidate

### links

- contrast | link | LINK contrast(first: CLAIM, second: CLAIM) | Expresses rhetorical qualification, opposition, or contrast between two claims. link between claims. | aliases: qualification, however  ⟵ candidate
- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ candidate
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ candidate
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ candidate
- then | link | LINK then(previous: EVENT, next: EVENT) | Represents temporal sequence and succession between two events where next follows previous. previous and next must be event terms. | aliases: followed_by, after_which  ⟵ candidate

### values

- art_character_profile | value | artifact-value | Descriptive character profile.  ⟵ candidate
- art_story | value | artifact-value | Narrative story.  ⟵ candidate
- path_pandas_src_testing_pyx | value | code-value | Source code file path or exported symbol in scientific Python: path_pandas_src_testing_pyx. | aliases: path_pandas_src_testing_pyx  ⟵ candidate
- sym_pandas_testing_assert_almost_equal | value | code-value | Source code file path or exported symbol in scientific Python: sym_pandas_testing_assert_almost_equal. | aliases: sym_pandas_testing_assert_almost_equal  ⟵ candidate
- constraint_17_plus | value | constraint-value | Rated 17+ or mature.  ⟵ candidate
- cuisine_indian | value | cuisine-value | Indian cuisine. | aliases: Indian food, Indian  ⟵ candidate
- cuisine_italian | value | cuisine-value | Italian cuisine. | aliases: Italian food, Italian  ⟵ candidate
- dom_safari | value | descriptive-value | Safari domain concept. | aliases: safari  ⟵ candidate
- tattoos | value | descriptive-value | Descriptive concept of tattoos in cultural and social contexts. | aliases: tattoos  ⟵ candidate
- yakuza | value | descriptive-value | Descriptive concept of yakuza in cultural and social contexts. | aliases: yakuza  ⟵ candidate
- unit_day | value | duration-unit-value | Day. | aliases: days  ⟵ candidate
- apple | value | entity-name | An apple fruit item, typically an ingredient or interactive food object. | not: food_label::tomato or other fruits/vegetables | aliases: apple, apples, red apple, green apple, apple slice  ⟵ candidate
- caddy | value | entity-name | A portable storage caddy, organizer box, or supply tote for carrying and organizing handheld tools and supplies. | not: cabinet (a stationary furniture cupboard) or safe (a secure metal lockbox) | aliases: caddy, supply caddy, wrapping caddy, tool caddy, organizer caddy, supply tote  ⟵ candidate
- chair | value | entity-name | A chair furniture seat with a backrest. | not: object_label::armchair (specifically an object_label::armchair with side armrests) or object_label::sofa | aliases: chair, seat  ⟵ candidate
- cheese | value | entity-name | Dairy food item: cheese. | not: meat or non-dairy food items | aliases: cheese  ⟵ candidate
- cinnamon | value | entity-name | Ground or whole cinnamon culinary spice from Cinnamomum tree bark. | not: nutmeg, cloves, or other distinct spice varieties | aliases: cinnamon, ground cinnamon, cinnamon spice, cinnamon stick  ⟵ candidate
- coffee_maker | value | entity-name | A coffee-making appliance; not automatically a heating resource  ⟵ candidate
- dog | value | entity-name | Animal entity: dog. | not: animal_label::cat or animal_label::donkey | aliases: dog, dogs, canine, pup, puppy  ⟵ candidate
- dulce_de_leche | value | entity-name | Sweet caramelized milk confection or dessert spread: dulce de leche. | not: cheese or dulce_de_nata | aliases: dulce de leche, dulce_de_leche  ⟵ candidate
- dulce_de_nata | value | entity-name | Clotted cream milk confection or dessert item: dulce de nata. | not: dulce_de_leche or cheese | aliases: dulce de nata, dulce_de_nata  ⟵ candidate
- enzyme | value | entity-name | Winemaking enzyme for breaking down fruit cellular structure. | not: living yeast strains or non-enzymatic chemical additives | aliases: enzyme, pectic enzyme, pectinase  ⟵ candidate
- fridge | value | entity-name | A refrigerator cooling appliance. | aliases: fridge  ⟵ candidate
- gift | value | entity-name | A physical gift or present item to be wrapped, given, or received. | not: egift_card (an electronic gift card or digital voucher product) | aliases: gift, present, wrapped gift, package  ⟵ candidate
- ginger | value | entity-name | Pungent aromatic spice root from Zingiber officinale used in cooking and baking. | not: cinnamon, cardamom, or other distinct spice varieties | aliases: ginger, ground ginger, fresh ginger, ginger root  ⟵ candidate
- grape_must | value | entity-name | Freshly crushed fruit juice mixture before fermentation. | not: clarified fruit_juice or finished wine | aliases: grape must, must  ⟵ candidate
- grape_thompson_seedless | value | entity-name | Thompson Seedless grape variety. | not: wine grape cultivars like grape_merlot or grape_chardonnay | aliases: Thompson Seedless, thompson seedless grape, sultana grape  ⟵ candidate
- laptop | value | entity-name | A portable laptop computer physical object. | not: topic_macbook_pro_2017 (a generation topic label) | aliases: laptop, laptop computer, notebook  ⟵ candidate
- lettuce | value | entity-name | A head of lettuce or leafy green vegetable food item. | not: food_label::tomato or food_label::potato (other vegetable items) | aliases: lettuce, head of lettuce, salad greens  ⟵ candidate
- martini_glass | value | entity-name | A cocktail or Martini drinking glass object. | not: mug (a drinking cup with a handle) or bottle (liquid storage container) | aliases: martini glass, cocktail glass, glass  ⟵ candidate
- meat | value | entity-name | Food item: meat or beef. | not: animal_label::tuna or animal_label::fish (specific aquatic foods) | aliases: meat, beef  ⟵ candidate
- mug | value | entity-name | Drinking cup. | aliases: mug  ⟵ candidate
- oak_chips | value | entity-name | Oak wood pieces or barrels used for wine aging and flavor extraction. | not: grape_tannin or structural chemical additives | aliases: oak chips, oak pieces, oak barrels  ⟵ candidate
- pear | value | entity-name | A pear fruit item, typically an ingredient or fresh fruit object. | not: apple, food_label::tomato, or other distinct fruit items | aliases: pear, pears, fresh pear, sliced pear  ⟵ candidate
- pen | value | entity-name | A writing instrument. | aliases: pen  ⟵ candidate
- pencil | value | entity-name | A pencil writing instrument. | aliases: pencil  ⟵ candidate
- resource_chiller | value | entity-name | Canonical abstract chilling resource when no particular appliance is named.  ⟵ candidate
- resource_heater | value | entity-name | Canonical abstract heating resource when no particular appliance is named.  ⟵ candidate
- spoon | value | entity-name | An eating or cooking utensil. | aliases: spoon  ⟵ candidate
- sultana | value | entity-name | Dried white seedless grape food product. | not: raisin (dark dried grape) or wine_grape | aliases: sultana, sultanas, golden raisin  ⟵ candidate
- locale_en_gb | value | locale-value | UK English. | aliases: british english  ⟵ candidate
- metric_order_late | value | metric-value | Whether an order is late. | aliases: order is late, delayed  ⟵ candidate
- color_pink | value | product-attribute-value | Pink visual color qualifier. | not: color_label::red, color_label::purple, or other distinct color shades | aliases: pink, color_pink, blush pink, rose pink, pastel pink  ⟵ candidate
- role_agent | value | recipient-value | The assistant. | aliases: you, the assistant  ⟵ dependency of example_d_record_an_actual_test_outcome_without_asserting_overall_correctness
- role_kids | value | recipient-value | Children/kids participant group in event context. | aliases: kids, children  ⟵ candidate
- role_mother | value | recipient-value | The mother of the user. | not: role_sister or role_kids | aliases: my mom, mother, mom  ⟵ candidate
- role_professor | value | recipient-value | The user's professor/instructor. | aliases: my professor, teacher  ⟵ candidate
- tattooed_guests | value | recipient-value | Social, demographic, or institutional group: tattooed_guests. | aliases: tattooed_guests  ⟵ candidate
- cat_game | value | search-value | Category: video game.  ⟵ candidate
- cat_limited_time_offers | value | search-value | Category: time-limited deals.  ⟵ candidate
- class_temple | value | semantic-category-value | The abstract class of temples. | aliases: temple, temples  ⟵ candidate
- in_front_of | value | spatial-relation | Positioned in front of. | aliases: in front of  ⟵ candidate
- left_of | value | spatial-relation | To the left of. | aliases: left of  ⟵ candidate
- right_of | value | spatial-relation | To the right of. | aliases: right of  ⟵ candidate
- style_catchy | value | style-value | Catchy, attention-grabbing style. | aliases: catchy  ⟵ candidate
- topic_baldurs_gate_3 | value | topic-value | Baldur's Gate 3.  ⟵ candidate
- topic_current_events | value | topic-value | Current news, geopolitical events, and ongoing international developments. | aliases: current_events, news  ⟵ candidate
- topic_spider_man_2 | value | topic-value | Marvel's Spider-Man 2.  ⟵ candidate

### examples

- example_d_record_an_actual_test_outcome_without_asserting_overall_correctness (candidate): Record an actual test outcome without asserting overall correctness

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=AGENT {
    RECORD ACTION run_tests(target=platform_label::scikit_learn) STATUS succeeded SOURCE "t1:tests" -> run_tests_event : EVENT
    CLAIM outcome(event=run_tests_event, value=TRUE) BY role_agent STATUS observed SOURCE "t1:tests" -> outcome_2 : CLAIM
  }
}
```

