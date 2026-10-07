# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 45 needs (decomposition: llm), 127 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | speech_act | t1:s1 | introduce a set of premises or theory | `respond`, `propose`, `subject`, `ask`, `inform`, `supports`, `example_of`, `conjunction`, `express_interest`, `activity`, `topic_school_work_routine`, `confirm` |
| n2 | claim | t1:s2 | the bald eagle sees the cat | `cat_game`, `enables`, `cat_limited_time_offers`, `leads_to`, `recommended`, `animal_label`, `earth`, `important`, `statement`, `outcome`, `motivated_by`, `occurred_recently` |
| n3 | object | t1:s2 | bald eagle → `animal_label::<key>` | `resource_chiller`, `topic_baldurs_gate_3`, `earth`, `moon`, `animal_label`*, `art_structured_report`, `shape_oval`, `meat`, `oak_chips`, `resource_heater`, `possesses`, `coffee_maker` |
| n4 | object | t1:s2 | cat → `animal_label::<key>` | `cat_game`, `cat_limited_time_offers`, `animal_label`*, `dog`, `style_catchy`, `caddy`, `apple`, `event_sadie_adler_unmasking`, `meat`, `path_pandas_src_testing_pyx`, `tattooed_guests`, `comfortable` |
| n5 | claim | t1:s3 | the cat is round | `shape_round`*, `cat_game`, `cat_limited_time_offers`, `leads_to`, `enables`, `important`, `recommended`, `causes`, `motivated_by`, `topic_pickup_lines`, `shape_triangular`, `occurred_recently` |
| n6 | object | t1:s3 | cat → `animal_label::<key>` | `cat_game`, `cat_limited_time_offers`, `animal_label`*, `dog`, `style_catchy`, `caddy`, `apple`, `event_sadie_adler_unmasking`, `meat`, `path_pandas_src_testing_pyx`, `tattooed_guests`, `comfortable` |
| n7 | claim | t1:s4 | the cat needs the rabbit | `cat_game`, `meets_needs`, `cat_limited_time_offers`, `enables`, `leads_to`, `recommended`, `important`, `caddy`, `animal_label`, `dog`, `causes`, `motivated_by` |
| n8 | object | t1:s4 | cat → `animal_label::<key>` | `cat_game`, `cat_limited_time_offers`, `animal_label`*, `dog`, `style_catchy`, `caddy`, `apple`, `event_sadie_adler_unmasking`, `meat`, `path_pandas_src_testing_pyx`, `tattooed_guests`, `comfortable` |
| n9 | object | t1:s4 | rabbit → `animal_label::<key>` | `bread`, `dog`, `cat_game`, `figurine`, `bowtie`, `caddy`, `animal_label`*, `topic_spider_man_2`, `mittens`, `entity_cake`, `resource_chiller`, `coffee_maker` |
| n10 | claim | t1:s5 | the cat sees the lion | `cat_game`, `cat_limited_time_offers`, `enables`, `leads_to`, `animal_label`, `recommended`, `important`, `occurred_recently`, `outcome`, `motivated_by`, `path_pandas_src_testing_pyx`, `causes` |
| n11 | object | t1:s5 | cat → `animal_label::<key>` | `cat_game`, `cat_limited_time_offers`, `animal_label`*, `dog`, `style_catchy`, `caddy`, `apple`, `event_sadie_adler_unmasking`, `meat`, `path_pandas_src_testing_pyx`, `tattooed_guests`, `comfortable` |
| n12 | object | t1:s5 | lion → `animal_label::<key>` | `animal_label`*, `cat_game`, `cat_limited_time_offers`, `style_catchy`, `sym_pandas_testing_assert_almost_equal`, `piano`, `path_pandas_src_testing_pyx`, `topic_classical_piano`, `dog`, `topic_spider_man_2`, `coffee_maker`, `resource_chiller` |
| n13 | claim | t1:s6 | the cat visits the lion | `cat_game`, `cat_limited_time_offers`, `enables`, `leads_to`, `animal_label`, `recommended`, `important`, `path_pandas_src_testing_pyx`, `outcome`, `occurred_recently`, `motivated_by`, `statement` |
| n14 | object | t1:s6 | cat → `animal_label::<key>` | `cat_game`, `cat_limited_time_offers`, `animal_label`*, `dog`, `style_catchy`, `caddy`, `apple`, `event_sadie_adler_unmasking`, `meat`, `path_pandas_src_testing_pyx`, `tattooed_guests`, `comfortable` |
| n15 | object | t1:s6 | lion → `animal_label::<key>` | `animal_label`*, `cat_game`, `cat_limited_time_offers`, `style_catchy`, `sym_pandas_testing_assert_almost_equal`, `piano`, `path_pandas_src_testing_pyx`, `topic_classical_piano`, `dog`, `topic_spider_man_2`, `coffee_maker`, `resource_chiller` |
| n16 | claim | t1:s7 | the lion is big | `enables`, `leads_to`, `important`, `piano`, `statement`, `size_large`, `recommended`, `outcome`, `causes`, `occurred_recently`, `motivated_by`, `ongoing` |
| n17 | object | t1:s7 | lion → `animal_label::<key>` | `animal_label`*, `cat_game`, `cat_limited_time_offers`, `style_catchy`, `sym_pandas_testing_assert_almost_equal`, `piano`, `path_pandas_src_testing_pyx`, `topic_classical_piano`, `dog`, `topic_spider_man_2`, `coffee_maker`, `resource_chiller` |
| n18 | claim | t1:s8 | the lion is cold | `state_cold`*, `leads_to`, `enables`, `causes`, `motivated_by`, `heat`, `important`, `weather_condition`, `statement`, `outcome`, `recommended`, `state_warm` |
| n19 | object | t1:s8 | lion → `animal_label::<key>` | `animal_label`*, `cat_game`, `cat_limited_time_offers`, `style_catchy`, `sym_pandas_testing_assert_almost_equal`, `piano`, `path_pandas_src_testing_pyx`, `topic_classical_piano`, `dog`, `topic_spider_man_2`, `coffee_maker`, `resource_chiller` |
| n20 | claim | t1:s9 | the lion is nice | `enables`, `style_catchy`, `leads_to`, `cat_game`, `important`, `topic_classical_piano`, `recommended`, `piano`, `outcome`, `statement`, `occurred_recently`, `comfortable` |
| n21 | object | t1:s9 | lion → `animal_label::<key>` | `animal_label`*, `cat_game`, `cat_limited_time_offers`, `style_catchy`, `sym_pandas_testing_assert_almost_equal`, `piano`, `path_pandas_src_testing_pyx`, `topic_classical_piano`, `dog`, `topic_spider_man_2`, `coffee_maker`, `resource_chiller` |
| n22 | claim | t1:s10 | the lion visits the rabbit | `enables`, `cat_game`, `leads_to`, `cat_limited_time_offers`, `dog`, `recommended`, `important`, `outcome`, `occurred_recently`, `statement`, `causes`, `ongoing` |
| n23 | object | t1:s10 | lion → `animal_label::<key>` | `animal_label`*, `cat_game`, `cat_limited_time_offers`, `style_catchy`, `sym_pandas_testing_assert_almost_equal`, `piano`, `path_pandas_src_testing_pyx`, `topic_classical_piano`, `dog`, `topic_spider_man_2`, `coffee_maker`, `resource_chiller` |
| n24 | object | t1:s10 | rabbit → `animal_label::<key>` | `bread`, `dog`, `cat_game`, `figurine`, `bowtie`, `caddy`, `animal_label`*, `topic_spider_man_2`, `mittens`, `entity_cake`, `resource_chiller`, `coffee_maker` |
| n25 | claim | t1:s11 | the rabbit is nice | `enables`, `dog`, `leads_to`, `recommended`, `cat_game`, `important`, `outcome`, `occurred_recently`, `statement`, `comfortable`, `causes`, `bowtie` |
| n26 | object | t1:s11 | rabbit → `animal_label::<key>` | `bread`, `dog`, `cat_game`, `figurine`, `bowtie`, `caddy`, `animal_label`*, `topic_spider_man_2`, `mittens`, `entity_cake`, `resource_chiller`, `coffee_maker` |
| n27 | claim | t1:s12 | the rabbit is round | `shape_round`*, `leads_to`, `enables`, `important`, `causes`, `dog`, `recommended`, `shape_square`, `ongoing`, `shape_triangular`, `occurred_recently`, `motivated_by` |
| n28 | object | t1:s12 | rabbit → `animal_label::<key>` | `bread`, `dog`, `cat_game`, `figurine`, `bowtie`, `caddy`, `animal_label`*, `topic_spider_man_2`, `mittens`, `entity_cake`, `resource_chiller`, `coffee_maker` |
| n29 | claim | t1:s13 | the rabbit sees the cat | `cat_game`, `cat_limited_time_offers`, `enables`, `leads_to`, `dog`, `recommended`, `important`, `caddy`, `animal_label`, `occurred_recently`, `outcome`, `statement` |
| n30 | object | t1:s13 | rabbit → `animal_label::<key>` | `bread`, `dog`, `cat_game`, `figurine`, `bowtie`, `caddy`, `animal_label`*, `topic_spider_man_2`, `mittens`, `entity_cake`, `resource_chiller`, `coffee_maker` |
| n31 | object | t1:s13 | cat → `animal_label::<key>` | `cat_game`, `cat_limited_time_offers`, `animal_label`*, `dog`, `style_catchy`, `caddy`, `apple`, `event_sadie_adler_unmasking`, `meat`, `path_pandas_src_testing_pyx`, `tattooed_guests`, `comfortable` |
| n32 | claim | t1:s14 | if something is nice then it is big | `important`, `comfortable`, `enables`, `style_catchy`, `leads_to`, `well_wishes`, `recommended`, `motivated_by`, `causes`, `statement`, `art_technical_explanation`, `outcome` |
| n33 | claim | t1:s15 | if something is kind and sees the rabbit then it needs the lion | `meets_needs`, `enables`, `comfortable`, `causes`, `leads_to`, `important`, `cat_game`, `recommended`, `cat_limited_time_offers`, `well_wishes`, `motivated_by`, `constraint_respectful` |
| n34 | claim | t1:s16 | if something needs the rabbit then it is nice | `meets_needs`, `enables`, `cat_game`, `leads_to`, `important`, `cat_limited_time_offers`, `recommended`, `causes`, `motivated_by`, `well_wishes`, `art_technical_explanation`, `statement` |
| n35 | claim | t1:s17 | all cold, big things are kind | `state_cold`*, `important`, `style_catchy`, `enables`, `leads_to`, `causes`, `well_wishes`, `recommended`, `statement`, `motivated_by`, `weather_condition`, `right_of` |
| n36 | claim | t1:s18 | if something sees the bald eagle and the bald eagle is nice then it needs the rabbit | `meets_needs`, `style_catchy`, `enables`, `art_technical_explanation`, `entity_order_vs_assemble_plan`, `topic_baldurs_gate_3`, `leads_to`, `recommended`, `important`, `statement`, `topic_pickup_lines`, `then`* |
| n37 | claim | t1:s19 | if something sees the lion then it visits the rabbit | `then`*, `leads_to`, `cat_game`, `enables`, `cat_limited_time_offers`, `recommended`, `comfortable`, `important`, `in_front_of`, `causes`, `dog`, `next_to` |
| n38 | claim | t1:s20 | if the bald eagle sees the cat then the bald eagle visits the rabbit | `topic_baldurs_gate_3`, `cat_game`, `enables`, `leads_to`, `cat_limited_time_offers`, `recommended`, `then`*, `outcome`, `in_front_of`, `style_catchy`, `occurred_recently`, `important` |
| n39 | claim | t1:s21 | if something visits the rabbit then it needs the rabbit | `meets_needs`, `failure`, `enables`, `leads_to`, `varies_with`, `important`, `recommended`, `dog`, `causes`, `event_camper_in_sludge_pit`, `cat_limited_time_offers`, `statement` |
| n40 | claim | t1:s22 | if something is big then it is cold | `state_cold`*, `leads_to`, `enables`, `important`, `causes`, `motivated_by`, `statement`, `weather_condition`, `recommended`, `outcome`, `heat`, `state_warm` |
| n41 | speech_act | t1:s23 | ask whether a statement is True, False, or Unknown | `ask`*, `statement`*, `confirm`, `failure`, `respond`, `inform`, `unaware`, `propose`, `acknowledge`, `conditional`, `negation`, `express_interest` |
| n42 | constraint | t1:s23 | base the answer only on the provided theory | `respond`*, `extract`, `topic_baldurs_gate_3`, `subject`, `constraint_realistic`, `conjunction`, `constraint_budget_limited`, `constraint_respectful`, `constraint_comprehensive`, `supports`, `constraint_single_choice`, `requirement` |
| n43 | constraint | t1:s23 | answer must be True, False, or Unknown | `constraint_realistic`, `constraint_respectful`, `in_front_of`, `right_of`, `metric_order_late`, `failure`, `constraint_budget_limited`, `constraint_comprehensive`, `rejects`, `constraint_single_choice`, `constraint_exclude_flowery_language`, `unaware` |
| n44 | claim | t1:s24 | the bald eagle is big | `enables`, `leads_to`, `earth`, `important`, `recommended`, `statement`, `size_large`, `outcome`, `moon`, `occurred_recently`, `motivated_by`, `ongoing` |
| n45 | object | t1:s24 | bald eagle → `animal_label::<key>` | `resource_chiller`, `topic_baldurs_gate_3`, `earth`, `moon`, `animal_label`*, `art_structured_report`, `shape_oval`, `meat`, `oak_chips`, `resource_heater`, `possesses`, `coffee_maker` |

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
- activity.object → object_label, food_label, animal_label
- activity.location → country
- activity.instrument → object_label, platform_label
- heat.destination → object_label
- weather_condition.location → country
- failure.system → platform_label
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

**rule_recording_signatures** (v19/rule/recording-signatures; rule governing heat)

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

**rule_category_constraint_value** (v19/rule/category/constraint-value; rule governing constraint_respectful)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing earth)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_event_value** (v19/rule/category/event-value; rule governing event_sadie_adler_unmasking)

TERM-described narrative event, not a recorded EVENT. Require inclusion explicitly when generating a story.

**rule_category_metric_value** (v19/rule/category/metric-value; rule governing metric_order_late)

STRING metric identity, not a Boolean value. Uptime and response time need numeric observations with units; order-late is Boolean-valued. Do not type every metric as BOOL.

**rule_category_product_attribute_value** (v19/rule/category/product-attribute-value; rule governing size_large)

STRING color/size/product-market facets. gender_women describes a product category, not an assertion about a person's gender.

**rule_category_recipient_value** (v19/rule/category/recipient-value; rule governing tattooed_guests)

STRING roles or explicit named recipients. A role is not an exact person's identity. Keep an explicit name where substituting a role loses information.

**rule_category_search_value** (v19/rule/category/search-value; rule governing cat_game)

STRING refinements rank_ / dir_ / cat_ / avail_ / genre_ are separate. rank_rating may fill rank_field; genre_label::comedy may not. “Cheapest” usually requires both rank_price and dir_asc, not rank_price alone.

**rule_category_shape_value** (v19/rule/category/shape-value; rule governing shape_oval)

STRING geometry. shape_round may select a circular object; it does not imply color or dimensions.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing right_of)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_state_value** (v19/rule/category/state-value; rule governing state_cold)

STRING condition used in selection. state_warm does not command heat; “hot” is not automatically synonymous with “warm.”

**rule_category_style_value** (v19/rule/category/style-value; rule governing style_catchy)

STRING production style. style_narrative does not establish that described events occurred.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_school_work_routine)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_composites_general** (v19/rule/composites-general; rule governing topic_school_work_routine)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_operations_general** (v19/rule/operations-general; rule governing heat)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_supplemental_general** (v19/rule/supplemental-general; rule governing coffee_maker)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; rule governing subject)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- extract | operation | operation-vocabulary | (target: LIST[REF[STRING]], limit: NUMBER) -> LIST[REF[STRING]] | First limit results, preserving order and identity; limit is a nonnegative integer; limit=1 is still a list  ⟵ candidate
- heat | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Heat using the stated resource; same identity. Selecting a warm object does not imply heating it.  ⟵ candidate
- turn | operation | operation-vocabulary | (direction: STRING) -> void | Rotate agent body/view orientation. direction is typically left, right, or angle. | aliases: rotate, turn_around  ⟵ related to then
- walk | operation | operation-vocabulary | (destination: STRING / TERM / ATOM[object_label], relation?: STRING) -> void | Locomote towards a target destination or landmark. destination must identify a valid entity or location. | aliases: move_to, go_to, navigate_to  ⟵ related to then

### speech acts

- acknowledge | speech_act | operation-vocabulary | UTTER acknowledge(target: CLAIM / TERM) | Acknowledge receipt/awareness; does not imply agreement.  ⟵ candidate
- ask | speech_act | operation-vocabulary | UTTER ask(target: TERM, or a sufficiently precise topic: STRING / TERM) | Request information/advice; not an assertion of an answer. | aliases: ask, how should  ⟵ candidate
- confirm | speech_act | operation-vocabulary | UTTER confirm(target: CLAIM) | Confirm the proposition; its evidence/status remains explicit.  ⟵ candidate
- express_interest | speech_act | operation-vocabulary | UTTER express_interest(target: STRING / TERM) | Speech act expressing conversational interest or engagement in a topic. speech act in dialogic traces. | aliases: show_interest  ⟵ candidate
- inform | speech_act | operation-vocabulary | UTTER inform(target: CLAIM) | Present the proposition; preserve its holder/status.  ⟵ candidate
- propose | speech_act | operation-vocabulary | UTTER propose(target: TERM) | Suggest an action/idea; does not record it as performed.  ⟵ candidate
- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ candidate
- conditional | constructor | TERM conditional(condition: TERM, consequence: TERM) -> TERM | Constructs a structured conditional proposition term connecting a condition and consequence. descriptive logic structure. | aliases: if_then  ⟵ candidate
- conjunction | constructor | TERM conjunction(items: LIST[TERM]) -> TERM | All described components apply | not: Does not imply temporal order  ⟵ candidate
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ dependency of constraint_exclude_flowery_language
- negation | constructor | TERM negation(target: TERM) -> TERM | Constructs a descriptive semantic negation of a target descriptive proposition or condition term. | not: Check's runtime Boolean operator NOT or a speech-act decline | aliases: not, does not, negation, absence of  ⟵ candidate
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ candidate
- sequence | constructor | TERM sequence(items: LIST[TERM]) -> TERM | Ordered described activities/content | not: Not unordered conjunction  ⟵ dependency of event_sadie_adler_unmasking
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ candidate
- weather_condition | constructor | TERM weather_condition(condition: STRING, location?: STRING / TERM / ATOM[country], severity?: STRING) -> TERM | A structured descriptor of atmospheric or weather phenomena such as wind, rain, or storm at an optional location; asserts nothing. | not: state_cold or state_warm (thermal states of physical objects) or occurred (past factual occurrence assertion) | aliases: weather, storm_condition, atmospheric_condition  ⟵ candidate
- well_wishes | constructor | TERM well_wishes(recipient?: STRING / TERM, sentiment?: STRING) -> TERM | Constructs a conversational discourse term representing well-wishes, good luck expressions, or parting encouragement. | not: a salutation greeting (use greeting) or apology (use apologize) | aliases: good_luck, best_wishes, encouragement  ⟵ candidate

### composites

- constraint_budget_limited | composite | constraint-value | TERM constraint_budget_limited() -> TERM | Limited budget. | = requirement(property="budget_limited", value=TRUE)  ⟵ candidate
- constraint_comprehensive | composite | constraint-value | TERM constraint_comprehensive() -> TERM | Must be comprehensive. | = requirement(property="comprehensive", value=TRUE)  ⟵ candidate
- constraint_exclude_flowery_language | composite | constraint-value | TERM constraint_exclude_flowery_language() -> TERM | Avoid flowery language. | = exclude(item="flowery_language")  ⟵ candidate
- constraint_realistic | composite | constraint-value | TERM constraint_realistic() -> TERM | Must be realistic. | = requirement(property="realistic", value=TRUE)  ⟵ candidate
- constraint_respectful | composite | constraint-value | TERM constraint_respectful() -> TERM | Must be respectful. | = requirement(property="respectful", value=TRUE)  ⟵ candidate
- constraint_single_choice | composite | constraint-value | TERM constraint_single_choice() -> TERM | Must pick a single choice. | = requirement(property="choice_count", value=1)  ⟵ candidate
- event_camper_in_sludge_pit | composite | event-value | TERM event_camper_in_sludge_pit() -> TERM | Campers interacting in a sludge pit. | = activity(verb="interact", actor="campers", location="sludge_pit")  ⟵ candidate
- event_sadie_adler_unmasking | composite | event-value | TERM event_sadie_adler_unmasking() -> TERM | Sadie Adler taking off her hat and peeling skin. | = sequence(items=[activity(verb="remove", actor="Sadie Adler", object="hat"), activity(verb="peel", actor="Sadie Adler", object="skin")])  ⟵ candidate
- topic_school_work_routine | composite | topic-value | TERM topic_school_work_routine() -> TERM | School and work routine. | = subject(kind="routine", qualifier=conjunction(items=[subject(kind="school"), subject(kind="work")]))  ⟵ candidate

### claim relations

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
- occurred | claim_relation | CLAIM occurred(activity: TERM) | Asserts that an event, action, or activity took place in the past. past occurrence claim. | aliases: happened  ⟵ candidate
- occurred_recently | claim_relation | CLAIM occurred_recently(target: CLAIM) | Asserts temporal recency of an asserted occurrence or claim. temporal recency qualifier. | aliases: recently_happened  ⟵ candidate
- ongoing | claim_relation | CLAIM ongoing(target: TERM) | Asserts that a conflict, process, or initiative is actively ongoing. temporal aspect claim. | aliases: in_progress  ⟵ candidate
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ candidate
- possesses | claim_relation | CLAIM possesses(subject: STRING / TERM, item: TERM, value: BOOL) | Asserts whether a subject possesses or lacks a stated property, capability, or entity. possession assertion with boolean polarity. | aliases: holds_property  ⟵ candidate
- recommended | claim_relation | CLAIM recommended(target: TERM / CLAIM) | Asserts an advisory recommendation that an activity or measure is advisable. advisory normative claim. | aliases: advisable  ⟵ candidate
- spatial_state | claim_relation | CLAIM spatial_state(relation: STRING, object: TERM, reference: TERM) | Asserts an observed spatial configuration between an object and a reference landmark. relation must specify spatial configuration. | aliases: placed_at, located_at  ⟵ related to statement
- statement | claim_relation | CLAIM statement(fact: TERM) | Foundational claim relation converting any descriptive TERM into an attributed, truth-evaluated assertion. universal fact assertion. | aliases: assert_fact, fact_claim, claim_statement  ⟵ candidate
- unaware | claim_relation | CLAIM unaware(person: STRING / TERM, topic: STRING / TERM) | Asserts epistemic lack of awareness regarding a topic, fact, or event. epistemic state. | aliases: ignorant_of  ⟵ candidate
- varies_with | claim_relation | CLAIM varies_with(target: CLAIM / TERM, condition: STRING / TERM) | Asserts that a target claim or term varies contingently depending on specified conditions, external factors, or behavioral habits. | not: geographic variation only (use varies_by_location) | aliases: depends_on, contingent_on  ⟵ candidate

### links

- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ candidate
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ core
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ candidate
- then | link | LINK then(previous: EVENT, next: EVENT) | Represents temporal sequence and succession between two events where next follows previous. previous and next must be event terms. | aliases: followed_by, after_which  ⟵ candidate

### values

- art_story | value | artifact-value | Narrative story.  ⟵ candidate
- art_structured_report | value | artifact-value | Headed/structured report.  ⟵ candidate
- art_technical_explanation | value | artifact-value | Technical explanation of a concept.  ⟵ candidate
- path_pandas_src_testing_pyx | value | code-value | Source code file path or exported symbol in scientific Python: path_pandas_src_testing_pyx. | aliases: path_pandas_src_testing_pyx  ⟵ candidate
- sym_pandas_testing_assert_almost_equal | value | code-value | Source code file path or exported symbol in scientific Python: sym_pandas_testing_assert_almost_equal. | aliases: sym_pandas_testing_assert_almost_equal  ⟵ candidate
- apple | value | entity-name | An apple fruit item, typically an ingredient or interactive food object. | not: food_label::tomato or other fruits/vegetables | aliases: apple, apples, red apple, green apple, apple slice  ⟵ candidate
- bowtie | value | entity-name | Item or prop in joke/creative context: bowtie. | aliases: bowtie  ⟵ candidate
- bread | value | entity-name | A bread loaf or slice food object. | aliases: bread  ⟵ candidate
- caddy | value | entity-name | A portable storage caddy, organizer box, or supply tote for carrying and organizing handheld tools and supplies. | not: cabinet (a stationary furniture cupboard) or safe (a secure metal lockbox) | aliases: caddy, supply caddy, wrapping caddy, tool caddy, organizer caddy, supply tote  ⟵ candidate
- chair | value | entity-name | A chair furniture seat with a backrest. | not: object_label::armchair (specifically an object_label::armchair with side armrests) or object_label::sofa | aliases: chair, seat  ⟵ candidate
- coffee_maker | value | entity-name | A coffee-making appliance; not automatically a heating resource  ⟵ candidate
- dog | value | entity-name | Animal entity: dog. | not: animal_label::cat or animal_label::donkey | aliases: dog, dogs, canine, pup, puppy  ⟵ candidate
- earth | value | entity-name | The planet Earth as an astronomical celestial body. | not: soil, ground surface, or electrical grounding | aliases: earth, the earth, planet earth, Earth  ⟵ candidate
- entity_cake | value | entity-name | Event planning item or menu category: entity_cake. | aliases: entity_cake  ⟵ candidate
- entity_order_vs_assemble_plan | value | entity-name | Event planning item or menu category: entity_order_vs_assemble_plan. | aliases: entity_order_vs_assemble_plan  ⟵ candidate
- figurine | value | entity-name | A small carved, molded, or sculpted decorative statuette object. | not: character (a fictional persona) or captioned_figure (a document figure/photo) | aliases: figurine, statuette, statue, small statue, sculptural figure, miniature figure  ⟵ candidate
- meat | value | entity-name | Food item: meat or beef. | not: animal_label::tuna or animal_label::fish (specific aquatic foods) | aliases: meat, beef  ⟵ candidate
- mittens | value | entity-name | Item or prop in joke/creative context: mittens. | aliases: mittens  ⟵ candidate
- moon | value | entity-name | Earth's natural celestial satellite. | not: an artificial satellite or other planetary moon | aliases: moon, the moon, Luna  ⟵ candidate
- oak_chips | value | entity-name | Oak wood pieces or barrels used for wine aging and flavor extraction. | not: grape_tannin or structural chemical additives | aliases: oak chips, oak pieces, oak barrels  ⟵ candidate
- piano | value | entity-name | A piano musical instrument or large furniture object. | not: topic_classical_piano or topic_jazz_piano (music genre topics) | aliases: piano, grand piano, upright piano, keyboard  ⟵ candidate
- resource_chiller | value | entity-name | Canonical abstract chilling resource when no particular appliance is named.  ⟵ candidate
- resource_heater | value | entity-name | Canonical abstract heating resource when no particular appliance is named.  ⟵ candidate
- metric_order_late | value | metric-value | Whether an order is late. | aliases: order is late, delayed  ⟵ candidate
- size_large | value | product-attribute-value | Large size. | aliases: large, L  ⟵ candidate
- tattooed_guests | value | recipient-value | Social, demographic, or institutional group: tattooed_guests. | aliases: tattooed_guests  ⟵ candidate
- cat_game | value | search-value | Category: video game.  ⟵ candidate
- cat_limited_time_offers | value | search-value | Category: time-limited deals.  ⟵ candidate
- shape_oval | value | shape-value | Oval. | aliases: oval  ⟵ candidate
- shape_round | value | shape-value | Circular/round. | aliases: round, circular  ⟵ candidate
- shape_square | value | shape-value | Square. | aliases: square  ⟵ candidate
- shape_triangular | value | shape-value | Triangular. | aliases: triangular, triangle  ⟵ candidate
- in_front_of | value | spatial-relation | Positioned in front of. | aliases: in front of  ⟵ candidate
- next_to | value | spatial-relation | Adjacent to. | aliases: beside  ⟵ candidate
- right_of | value | spatial-relation | To the right of. | aliases: right of  ⟵ candidate
- state_cold | value | state-value | Cold or chilled condition. | aliases: cold, chilled  ⟵ candidate
- state_warm | value | state-value | Warm or heated condition. | aliases: warm, hot  ⟵ candidate
- style_catchy | value | style-value | Catchy, attention-grabbing style. | aliases: catchy  ⟵ candidate
- topic_baldurs_gate_3 | value | topic-value | Baldur's Gate 3.  ⟵ candidate
- topic_classical_piano | value | topic-value | Classical piano.  ⟵ candidate
- topic_pickup_lines | value | topic-value | Pickup lines.  ⟵ candidate
- topic_spider_man_2 | value | topic-value | Marvel's Spider-Man 2.  ⟵ candidate
