# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 35 needs (decomposition: llm), 119 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | speech_act | t1:s1 | introduce a set of premises or theory | `respond`, `propose`, `ask`, `subject`, `inform`, `supports`, `example_of`, `topic_school_work_routine`, `in_front_of`, `conjunction`, `confirm`, `express_interest` |
| n2 | object | t1:s2 | bald eagle → `animal_label::<key>` | `resource_chiller`, `topic_baldurs_gate_3`, `earth`, `oak_chips`, `moon`, `shape_oval`, `art_structured_report`, `meat`, `hover`, `chair`, `resource_heater`, `animal_label`* |
| n3 | object | t1:s2 | lion → `animal_label::<key>` | `animal_label`*, `path_pandas_src_testing_pyx`, `piano`, `topic_classical_piano`, `sym_pandas_testing_assert_almost_equal`, `style_catchy`, `cat_game`, `cat_limited_time_offers`, `topic_spider_man_2`, `dog`, `laptop`, `chair` |
| n4 | claim | t1:s2 | the bald eagle chases the lion | `leads_to`, `enables`, `hover`, `piano`, `entity_order_vs_assemble_plan`, `statement`, `recommended`, `motivated_by`, `occurred_recently`, `oak_chips`, `ongoing`, `select_option` |
| n5 | object | t1:s3 | mouse → `animal_label::<key>` | `hover`, `laptop`, `dom_safari`, `fridge`, `topic_spider_man_2`, `pencil`, `piano`, `dom_ovr`, `animal_label`*, `desk`, `chair`, `pen` |
| n6 | claim | t1:s3 | the bald eagle chases the mouse | `hover`, `leads_to`, `entity_order_vs_assemble_plan`, `enables`, `oak_chips`, `recommended`, `statement`, `occurred_recently`, `ongoing`, `motivated_by`, `dom_safari`, `important` |
| n7 | claim | t1:s4 | the bald eagle visits the lion | `leads_to`, `enables`, `topic_baldurs_gate_3`, `topic_classical_piano`, `earth`, `recommended`, `hover`, `piano`, `statement`, `occurred_recently`, `outcome`, `ongoing` |
| n8 | claim | t1:s5 | the lion is rough | `path_pandas_src_testing_pyx`, `leads_to`, `enables`, `occurred_recently`, `outcome`, `topic_classical_piano`, `important`, `piano`, `africa`, `sym_pandas_testing_assert_almost_equal`, `statement`, `ongoing` |
| n9 | claim | t1:s6 | the lion likes the bald eagle | `style_catchy`, `enables`, `entity_order_vs_assemble_plan`, `leads_to`, `piano`, `recommended`, `topic_classical_piano`, `important`, `statement`, `hover`, `earth`, `occurred_recently` |
| n10 | object | t1:s7 | squirrel → `animal_label::<key>` | `animal_label`*, `topic_baldurs_gate_3`, `topic_pickup_lines`, `topic_spider_man_2`, `cat_game`, `cat_limited_time_offers`, `caddy`, `oak_chips`, `pen`, `mittens`, `laptop`, `chair` |
| n11 | claim | t1:s7 | the lion likes the squirrel | `causes`, `leads_to`, `cat_game`, `style_catchy`, `enables`, `important`, `path_pandas_src_testing_pyx`, `recommended`, `motivated_by`, `animal_label`, `sym_pandas_testing_assert_almost_equal`, `statement` |
| n12 | claim | t1:s8 | the lion visits the mouse | `leads_to`, `hover`, `enables`, `cat_game`, `piano`, `occurred_recently`, `topic_classical_piano`, `path_pandas_src_testing_pyx`, `ongoing`, `laptop`, `topic_spider_man_2`, `recommended` |
| n13 | claim | t1:s9 | the mouse chases the lion | `path_pandas_src_testing_pyx`, `leads_to`, `sym_pandas_testing_assert_almost_equal`, `enables`, `hover`, `cat_game`, `occurred_recently`, `ongoing`, `motivated_by`, `statement`, `piano`, `recommended` |
| n14 | claim | t1:s10 | the mouse chases the squirrel | `leads_to`, `hover`, `cat_game`, `enables`, `path_pandas_src_testing_pyx`, `occurred_recently`, `ongoing`, `motivated_by`, `statement`, `oak_chips`, `outcome`, `recommended` |
| n15 | claim | t1:s11 | the mouse is rough | `hover`, `leads_to`, `laptop`, `occurred_recently`, `pencil`, `enables`, `outcome`, `important`, `ongoing`, `statement`, `recommended`, `causes` |
| n16 | claim | t1:s12 | the mouse is round | `shape_round`*, `hover`, `leads_to`, `ongoing`, `laptop`, `occurred`, `important`, `causes`, `enables`, `occurred_recently`, `statement`, `sym_pandas_testing_assert_almost_equal` |
| n17 | claim | t1:s13 | the mouse likes the bald eagle | `hover`, `leads_to`, `enables`, `style_catchy`, `entity_order_vs_assemble_plan`, `oak_chips`, `recommended`, `topic_baldurs_gate_3`, `dom_safari`, `important`, `statement`, `topic_spider_man_2` |
| n18 | claim | t1:s14 | the mouse visits the bald eagle | `hover`, `leads_to`, `topic_baldurs_gate_3`, `enables`, `oak_chips`, `recommended`, `dom_safari`, `occurred_recently`, `topic_spider_man_2`, `ongoing`, `outcome`, `statement` |
| n19 | claim | t1:s15 | the squirrel chases the lion | `path_pandas_src_testing_pyx`, `leads_to`, `cat_game`, `enables`, `sym_pandas_testing_assert_almost_equal`, `motivated_by`, `occurred_recently`, `cat_limited_time_offers`, `ongoing`, `statement`, `recommended`, `outcome` |
| n20 | claim | t1:s16 | the squirrel is kind | `comfortable`, `style_catchy`, `leads_to`, `animal_label`, `cat_game`, `enables`, `motivated_by`, `important`, `topic_pickup_lines`, `topic_baldurs_gate_3`, `causes`, `topic_spider_man_2` |
| n21 | claim | t1:s17 | the squirrel likes the mouse | `hover`, `leads_to`, `enables`, `topic_spider_man_2`, `cat_game`, `occurred_recently`, `important`, `recommended`, `statement`, `causes`, `motivated_by`, `caddy` |
| n22 | reasoning | t1:s18 | if something visits the bald eagle, then the bald eagle visits the lion | `then`*, `topic_baldurs_gate_3`, `rejects`, `in_front_of`, `next_to`, `entity_order_vs_assemble_plan`, `style_catchy`, `possesses`, `supports`, `contrast`, `on`, `topic_pickup_lines` |
| n23 | reasoning | t1:s19 | if something is kind, then it visits the squirrel | `then`*, `animal_label`, `rejects`, `style_catchy`, `cat_game`, `topic_baldurs_gate_3`, `comfortable`, `possesses`, `supports`, `contrast`, `next_to`, `topic_pickup_lines` |
| n24 | reasoning | t1:s20 | if something likes the mouse, then it visits the lion | `then`*, `hover`, `rejects`, `style_catchy`, `cat_game`, `contrast`, `sym_pandas_testing_assert_almost_equal`, `supports`, `next_to`, `piano`, `revises`, `path_pandas_src_testing_pyx` |
| n25 | reasoning | t1:s21 | if the bald eagle visits the lion and the lion visits the squirrel, then the bald eagle likes the squirrel | `then`*, `rejects`, `style_catchy`, `topic_baldurs_gate_3`, `entity_order_vs_assemble_plan`, `topic_pickup_lines`, `in_front_of`, `possesses`, `contrast`, `next_to`, `supports`, `on` |
| n26 | reasoning | t1:s22 | if something likes the lion, then it visits the lion | `then`*, `rejects`, `style_catchy`, `next_to`, `cat_game`, `contrast`, `supports`, `in_front_of`, `causes`, `topic_classical_piano`, `comfortable`, `sym_pandas_testing_assert_almost_equal` |
| n27 | reasoning | t1:s23 | if something likes the mouse and visits the lion, then it is young | `then`*, `hover`, `rejects`, `style_catchy`, `contrast`, `cat_game`, `supports`, `next_to`, `cat_limited_time_offers`, `topic_profanity`, `sym_pandas_testing_assert_almost_equal`, `constraint_17_plus` |
| n28 | reasoning | t1:s24 | if something visits the squirrel, then it likes the mouse | `then`*, `hover`, `rejects`, `style_catchy`, `cat_game`, `contrast`, `topic_pickup_lines`, `supports`, `topic_baldurs_gate_3`, `topic_spider_man_2`, `next_to`, `causes` |
| n29 | reasoning | t1:s25 | if something visits the lion and the lion chases the mouse, then the mouse is young | `then`*, `hover`, `rejects`, `metric_order_late`, `in_front_of`, `contrast`, `leads_to`, `style_catchy`, `supports`, `sym_pandas_testing_assert_almost_equal`, `cat_game`, `causes` |
| n30 | reasoning | t1:s26 | if something visits the bald eagle and chases the lion, then the lion is kind | `then`*, `animal_label`, `rejects`, `style_catchy`, `topic_baldurs_gate_3`, `supports`, `possesses`, `contrast`, `piano`, `cat_game`, `topic_school_work_routine`, `next_to` |
| n31 | speech_act | t1:s27 | ask whether a statement is true, false, or unknown | `ask`*, `statement`*, `confirm`, `respond`, `rejects`, `propose`, `failure`, `inform`, `controversial`, `unaware`, `run_tests`, `decline` |
| n32 | constraint | t1:s27 | rely only on the provided theory | `constraint_realistic`, `rejects`, `constraint_budget_limited`, `constraint_respectful`, `constraint_exclude_flowery_language`, `constraint_beginner`, `constraint_single_choice`, `subject`, `requirement`, `constraint_comprehensive`, `failure`, `constraint_exclude_liberation_theme` |
| n33 | constraint | t1:s27 | answer must be True, False, or Unknown | `constraint_realistic`, `in_front_of`, `rejects`, `metric_order_late`, `constraint_respectful`, `constraint_budget_limited`, `constraint_comprehensive`, `right_of`, `constraint_exclude_flowery_language`, `failure`, `constraint_beginner`, `constraint_single_choice` |
| n34 | claim | t1:s28 | the mouse visits the lion | `leads_to`, `hover`, `enables`, `cat_game`, `occurred_recently`, `piano`, `path_pandas_src_testing_pyx`, `topic_spider_man_2`, `ongoing`, `recommended`, `topic_classical_piano`, `outcome` |
| n35 | negation | t1:s28 | the mouse does not visit the lion | `negation`*, `hover`, `rejects`, `constraint_exclude_flowery_language`, `failure`, `path_pandas_src_testing_pyx`, `topic_spider_man_2`, `sym_pandas_testing_assert_almost_equal`, `decline`, `exclude`, `laptop`, `piano` |

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

**rule_recording_signatures** (v19/rule/recording-signatures; rule governing hover)

RECORD ACTION uses the operation signature with REF[STRING] → TERM and LIST[REF[STRING]] → LIST[TERM]; other types/categories stay unchanged. Return EVENT, never the runtime result. Record actual outputs as attributed CLAIMs. Do not infer missing resources.

**rule_speech_acts_general** (v19/rule/speech-acts-general; rule governing respond)

UTTER-only, void, with the spec's speech attributes and LIST[TERM] constraints. No result binding. Literal content cannot replace required semantic arguments for structured coverage.

**rule_structural_constructs** (v19/rule/structural-constructs; core)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; rule governing supports)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_attributes_and_generate** (v19/rule/attributes-and-generate; rule governing art_structured_report)

Attribute entries name arguments; legality/types come from each operation, not global membership. GENERATE uses the spec's core fields; retained artifact profiles return STRING. Numeric/list results need explicit profiles. Legacy itinerary fields expand to TERM constraints: duration/duration_unit → duration(amount,unit); stop_min_per_day/stop_requirement → minimum_per_period(class,count,period=unit_day), never an inferred temple class; max_walk_duration/unit → maximum_between_stops(activity="walk",amount,unit). No legacy shorthand is enabled. Old events/character_properties/transformations become explicitly scoped TERM constraints. Message purpose is TERM, not send_email.content: GENERATE exact STRING content, then send. Report opaque fallback separately.

**rule_category_artifact_value** (v19/rule/category/artifact-value; rule governing art_structured_report)

STRING artifact class for GENERATE.target. art_story says what kind of artifact to produce, not what occurs in its plot.

**rule_category_code_value** (v19/rule/category/code-value; rule governing path_pandas_src_testing_pyx)

path_/sym_ remain STRING identities; migrated chg_/assert_ are TERM constructors. Do not recover an exact file path by guessing from underscores.

**rule_category_constraint_value** (v19/rule/category/constraint-value; rule governing constraint_17_plus)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_descriptive_value** (v19/rule/category/descriptive-value; rule governing dom_safari)

STRING modifier/domain label; never a free-form proposition. dom_sgi needs its intended referent established before semantically dependent use.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing resource_chiller)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_location_name** (v19/rule/category/location-name; rule governing africa)

STRING location descriptor. A `table` surface is not the generated artifact category art_table.

**rule_category_metric_value** (v19/rule/category/metric-value; rule governing metric_order_late)

STRING metric identity, not a Boolean value. Uptime and response time need numeric observations with units; order-late is Boolean-valued. Do not type every metric as BOOL.

**rule_category_search_value** (v19/rule/category/search-value; rule governing cat_game)

STRING refinements rank_ / dir_ / cat_ / avail_ / genre_ are separate. rank_rating may fill rank_field; genre_label::comedy may not. “Cheapest” usually requires both rank_price and dir_asc, not rank_price alone.

**rule_category_shape_value** (v19/rule/category/shape-value; rule governing shape_oval)

STRING geometry. shape_round may select a circular object; it does not imply color or dimensions.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing in_front_of)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_style_value** (v19/rule/category/style-value; rule governing style_catchy)

STRING production style. style_narrative does not establish that described events occurred.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_school_work_routine)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_composites_general** (v19/rule/composites-general; rule governing topic_school_work_routine)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_operations_general** (v19/rule/operations-general; rule governing hover)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_support_primitives_general** (v19/rule/support-primitives-general; rule governing subject)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- hover | operation | operation-vocabulary | (target: REF[STRING]) -> void | Move pointer cursor over an interactive web element without clicking. target must resolve to a valid element reference. | aliases: mouse_over  ⟵ candidate
- run_tests | operation | operation-vocabulary | (target: STRING / ATOM[platform_label], assertion?: TERM) -> BOOL | Run the selected project's tests, optionally checking the specified assertion. TRUE means the declared test condition passed, not overall software correctness.  ⟵ candidate
- select_option | operation | operation-vocabulary | (target: REF[STRING], value: STRING) -> void | Select an option from a dropdown or select menu element. target must be a select element. | aliases: choose_option, choose_dropdown, pick_option  ⟵ candidate
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

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ dependency of occurred
- conjunction | constructor | TERM conjunction(items: LIST[TERM]) -> TERM | All described components apply | not: Does not imply temporal order  ⟵ candidate
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ candidate
- negation | constructor | TERM negation(target: TERM) -> TERM | Constructs a descriptive semantic negation of a target descriptive proposition or condition term. | not: Check's runtime Boolean operator NOT or a speech-act decline | aliases: not, does not, negation, absence of  ⟵ candidate
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ candidate
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ candidate

### composites

- constraint_beginner | composite | constraint-value | TERM constraint_beginner() -> TERM | Targeted at beginners. | = requirement(property="audience_expertise", value="beginner")  ⟵ candidate
- constraint_budget_limited | composite | constraint-value | TERM constraint_budget_limited() -> TERM | Limited budget. | = requirement(property="budget_limited", value=TRUE)  ⟵ candidate
- constraint_comprehensive | composite | constraint-value | TERM constraint_comprehensive() -> TERM | Must be comprehensive. | = requirement(property="comprehensive", value=TRUE)  ⟵ candidate
- constraint_exclude_flowery_language | composite | constraint-value | TERM constraint_exclude_flowery_language() -> TERM | Avoid flowery language. | = exclude(item="flowery_language")  ⟵ candidate
- constraint_exclude_liberation_theme | composite | constraint-value | TERM constraint_exclude_liberation_theme() -> TERM | Avoid liberation theme. | = exclude(item="liberation_theme")  ⟵ candidate
- constraint_realistic | composite | constraint-value | TERM constraint_realistic() -> TERM | Must be realistic. | = requirement(property="realistic", value=TRUE)  ⟵ candidate
- constraint_respectful | composite | constraint-value | TERM constraint_respectful() -> TERM | Must be respectful. | = requirement(property="respectful", value=TRUE)  ⟵ candidate
- constraint_single_choice | composite | constraint-value | TERM constraint_single_choice() -> TERM | Must pick a single choice. | = requirement(property="choice_count", value=1)  ⟵ candidate
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
- motivated_by | claim_relation | CLAIM motivated_by(claim: CLAIM, motive: STRING / TERM) | Asserts that an action, rule, or claim is motivated by an underlying motive or goal. motive explanation. | aliases: rationale_is  ⟵ candidate
- occurred | claim_relation | CLAIM occurred(activity: TERM) | Asserts that an event, action, or activity took place in the past. past occurrence claim. | aliases: happened  ⟵ candidate
- occurred_recently | claim_relation | CLAIM occurred_recently(target: CLAIM) | Asserts temporal recency of an asserted occurrence or claim. temporal recency qualifier. | aliases: recently_happened  ⟵ candidate
- ongoing | claim_relation | CLAIM ongoing(target: TERM) | Asserts that a conflict, process, or initiative is actively ongoing. temporal aspect claim. | aliases: in_progress  ⟵ candidate
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ candidate
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

- art_structured_report | value | artifact-value | Headed/structured report.  ⟵ candidate
- path_pandas_src_testing_pyx | value | code-value | Source code file path or exported symbol in scientific Python: path_pandas_src_testing_pyx. | aliases: path_pandas_src_testing_pyx  ⟵ candidate
- sym_pandas_testing_assert_almost_equal | value | code-value | Source code file path or exported symbol in scientific Python: sym_pandas_testing_assert_almost_equal. | aliases: sym_pandas_testing_assert_almost_equal  ⟵ candidate
- constraint_17_plus | value | constraint-value | Rated 17+ or mature.  ⟵ candidate
- dom_ovr | value | descriptive-value | One-versus-rest domain concept.  ⟵ candidate
- dom_safari | value | descriptive-value | Safari domain concept. | aliases: safari  ⟵ candidate
- caddy | value | entity-name | A portable storage caddy, organizer box, or supply tote for carrying and organizing handheld tools and supplies. | not: cabinet (a stationary furniture cupboard) or safe (a secure metal lockbox) | aliases: caddy, supply caddy, wrapping caddy, tool caddy, organizer caddy, supply tote  ⟵ candidate
- chair | value | entity-name | A chair furniture seat with a backrest. | not: object_label::armchair (specifically an object_label::armchair with side armrests) or object_label::sofa | aliases: chair, seat  ⟵ candidate
- desk | value | entity-name | A work desk furniture surface. | aliases: desk  ⟵ candidate
- dog | value | entity-name | Animal entity: dog. | not: animal_label::cat or animal_label::donkey | aliases: dog, dogs, canine, pup, puppy  ⟵ candidate
- earth | value | entity-name | The planet Earth as an astronomical celestial body. | not: soil, ground surface, or electrical grounding | aliases: earth, the earth, planet earth, Earth  ⟵ candidate
- entity_order_vs_assemble_plan | value | entity-name | Event planning item or menu category: entity_order_vs_assemble_plan. | aliases: entity_order_vs_assemble_plan  ⟵ candidate
- fridge | value | entity-name | A refrigerator cooling appliance. | aliases: fridge  ⟵ candidate
- laptop | value | entity-name | A portable laptop computer physical object. | not: topic_macbook_pro_2017 (a generation topic label) | aliases: laptop, laptop computer, notebook  ⟵ candidate
- meat | value | entity-name | Food item: meat or beef. | not: animal_label::tuna or animal_label::fish (specific aquatic foods) | aliases: meat, beef  ⟵ candidate
- mittens | value | entity-name | Item or prop in joke/creative context: mittens. | aliases: mittens  ⟵ candidate
- moon | value | entity-name | Earth's natural celestial satellite. | not: an artificial satellite or other planetary moon | aliases: moon, the moon, Luna  ⟵ candidate
- oak_chips | value | entity-name | Oak wood pieces or barrels used for wine aging and flavor extraction. | not: grape_tannin or structural chemical additives | aliases: oak chips, oak pieces, oak barrels  ⟵ candidate
- pan | value | entity-name | A metal cooking vessel, frying pan, skillet, saucepan, or pot cookware item used for preparing, heating, or holding food. | not: bowl (deep concave vessel) or plate (shallow flat dining dish) | aliases: pan, frying pan, skillet, saucepan, pot  ⟵ candidate
- pen | value | entity-name | A writing instrument. | aliases: pen  ⟵ candidate
- pencil | value | entity-name | A pencil writing instrument. | aliases: pencil  ⟵ candidate
- piano | value | entity-name | A piano musical instrument or large furniture object. | not: topic_classical_piano or topic_jazz_piano (music genre topics) | aliases: piano, grand piano, upright piano, keyboard  ⟵ candidate
- resource_chiller | value | entity-name | Canonical abstract chilling resource when no particular appliance is named.  ⟵ candidate
- resource_heater | value | entity-name | Canonical abstract heating resource when no particular appliance is named.  ⟵ candidate
- africa | value | location-name | Geopolitical nation or continental region: africa. | aliases: africa  ⟵ candidate
- metric_order_late | value | metric-value | Whether an order is late. | aliases: order is late, delayed  ⟵ candidate
- cat_game | value | search-value | Category: video game.  ⟵ candidate
- cat_limited_time_offers | value | search-value | Category: time-limited deals.  ⟵ candidate
- shape_oval | value | shape-value | Oval. | aliases: oval  ⟵ candidate
- shape_round | value | shape-value | Circular/round. | aliases: round, circular  ⟵ candidate
- in_front_of | value | spatial-relation | Positioned in front of. | aliases: in front of  ⟵ candidate
- next_to | value | spatial-relation | Adjacent to. | aliases: beside  ⟵ candidate
- on | value | spatial-relation | Resting atop. | aliases: on top of  ⟵ candidate
- right_of | value | spatial-relation | To the right of. | aliases: right of  ⟵ candidate
- style_catchy | value | style-value | Catchy, attention-grabbing style. | aliases: catchy  ⟵ candidate
- topic_baldurs_gate_3 | value | topic-value | Baldur's Gate 3.  ⟵ candidate
- topic_classical_piano | value | topic-value | Classical piano.  ⟵ candidate
- topic_pickup_lines | value | topic-value | Pickup lines.  ⟵ candidate
- topic_spider_man_2 | value | topic-value | Marvel's Spider-Man 2.  ⟵ candidate
