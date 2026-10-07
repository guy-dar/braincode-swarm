# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 46 needs (decomposition: llm), 118 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | speech_act | t1:s1 | introduce a set of premises or theory | `respond`, `propose`, `ask`, `subject`, `inform`, `supports`, `example_of`, `confirm`, `topic_school_work_routine`, `express_interest`, `conjunction`, `property_question` |
| n2 | claim | t1:s2 | the bald eagle is kind | `enables`, `style_catchy`, `recommended`, `possesses`, `topic_baldurs_gate_3`, `earth`, `important`, `statement`, `leads_to`, `oak_chips`, `animal_label`, `moon` |
| n3 | object | t1:s2 | bald eagle → `animal_label::<key>` | `resource_chiller`, `topic_baldurs_gate_3`, `earth`, `oak_chips`, `animal_label`*, `moon`, `possesses`, `art_structured_report`, `meat`, `tattoos`, `coffee_maker`, `shape_oval` |
| n4 | claim | t1:s3 | the bald eagle needs the bear | `meets_needs`, `possesses`, `enables`, `topic_baldurs_gate_3`, `topic_spider_man_2`, `recommended`, `important`, `statement`, `leads_to`, `dog`, `hover`, `entity_order_vs_assemble_plan` |
| n5 | object | t1:s3 | bald eagle → `animal_label::<key>` | `resource_chiller`, `topic_baldurs_gate_3`, `earth`, `oak_chips`, `animal_label`*, `moon`, `possesses`, `art_structured_report`, `meat`, `tattoos`, `coffee_maker`, `shape_oval` |
| n6 | object | t1:s3 | bear → `animal_label::<key>` | `animal_label`*, `bread`, `topic_spider_man_2`, `sym_pandas_testing_assert_almost_equal`, `dog`, `event_sadie_adler_unmasking`, `path_pandas_src_testing_pyx`, `caddy`, `yakuza`, `tattoos`, `cat_game`, `coffee_maker` |
| n7 | claim | t1:s4 | the bear is kind | `comfortable`, `enables`, `recommended`, `important`, `sym_pandas_testing_assert_almost_equal`, `style_catchy`, `animal_label`, `topic_spider_man_2`, `causes`, `statement`, `leads_to`, `motivated_by` |
| n8 | object | t1:s4 | bear → `animal_label::<key>` | `animal_label`*, `bread`, `topic_spider_man_2`, `sym_pandas_testing_assert_almost_equal`, `dog`, `event_sadie_adler_unmasking`, `path_pandas_src_testing_pyx`, `caddy`, `yakuza`, `tattoos`, `cat_game`, `coffee_maker` |
| n9 | claim | t1:s5 | the lion needs the bear | `causes`, `meets_needs`, `enables`, `important`, `recommended`, `constraint_single_choice`, `topic_spider_man_2`, `sym_pandas_testing_assert_almost_equal`, `leads_to`, `requirement`, `statement`, `motivated_by` |
| n10 | object | t1:s5 | lion → `animal_label::<key>` | `animal_label`*, `sym_pandas_testing_assert_almost_equal`, `style_catchy`, `cat_game`, `piano`, `path_pandas_src_testing_pyx`, `topic_spider_man_2`, `topic_classical_piano`, `cat_limited_time_offers`, `dog`, `coffee_maker`, `resource_chiller` |
| n11 | object | t1:s5 | bear → `animal_label::<key>` | `animal_label`*, `bread`, `topic_spider_man_2`, `sym_pandas_testing_assert_almost_equal`, `dog`, `event_sadie_adler_unmasking`, `path_pandas_src_testing_pyx`, `caddy`, `yakuza`, `tattoos`, `cat_game`, `coffee_maker` |
| n12 | claim | t1:s6 | the squirrel is kind | `comfortable`, `enables`, `animal_label`, `recommended`, `important`, `style_catchy`, `topic_spider_man_2`, `causes`, `leads_to`, `motivated_by`, `statement`, `cat_game` |
| n13 | object | t1:s6 | squirrel → `animal_label::<key>` | `animal_label`*, `topic_spider_man_2`, `topic_baldurs_gate_3`, `topic_pickup_lines`, `caddy`, `cat_game`, `mittens`, `cat_limited_time_offers`, `tattoos`, `oak_chips`, `tattooed_guests`, `resource_chiller` |
| n14 | claim | t1:s7 | the squirrel needs the bald eagle | `meets_needs`, `enables`, `topic_baldurs_gate_3`, `topic_spider_man_2`, `recommended`, `oak_chips`, `possesses`, `leads_to`, `important`, `mittens`, `statement`, `animal_label` |
| n15 | object | t1:s7 | squirrel → `animal_label::<key>` | `animal_label`*, `topic_spider_man_2`, `topic_baldurs_gate_3`, `topic_pickup_lines`, `caddy`, `cat_game`, `mittens`, `cat_limited_time_offers`, `tattoos`, `oak_chips`, `tattooed_guests`, `resource_chiller` |
| n16 | object | t1:s7 | bald eagle → `animal_label::<key>` | `resource_chiller`, `topic_baldurs_gate_3`, `earth`, `oak_chips`, `animal_label`*, `moon`, `possesses`, `art_structured_report`, `meat`, `tattoos`, `coffee_maker`, `shape_oval` |
| n17 | claim | t1:s8 | the squirrel visits the lion | `enables`, `leads_to`, `topic_spider_man_2`, `recommended`, `cat_game`, `important`, `outcome`, `cat_limited_time_offers`, `statement`, `animal_label`, `path_pandas_src_testing_pyx`, `motivated_by` |
| n18 | object | t1:s8 | squirrel → `animal_label::<key>` | `animal_label`*, `topic_spider_man_2`, `topic_baldurs_gate_3`, `topic_pickup_lines`, `caddy`, `cat_game`, `mittens`, `cat_limited_time_offers`, `tattoos`, `oak_chips`, `tattooed_guests`, `resource_chiller` |
| n19 | object | t1:s8 | lion → `animal_label::<key>` | `animal_label`*, `sym_pandas_testing_assert_almost_equal`, `style_catchy`, `cat_game`, `piano`, `path_pandas_src_testing_pyx`, `topic_spider_man_2`, `topic_classical_piano`, `cat_limited_time_offers`, `dog`, `coffee_maker`, `resource_chiller` |
| n20 | claim | t1:s9 | if someone is blue and rough, they need the bear | `meets_needs`, `enables`, `possesses`, `yakuza`, `recommended`, `topic_spider_man_2`, `constraint_respectful`, `dog`, `important`, `leads_to`, `statement`, `causes` |
| n21 | object | t1:s9 | blue → `color_label::<key>` | `color_label`*, `chill`, `yakuza`, `right_of`, `fridge`, `dried_fruit`, `grape_merlot`, `sultana`, `lettuce`, `resource_chiller`, `on`, `coffee_maker` |
| n22 | object | t1:s9 | bear → `animal_label::<key>` | `animal_label`*, `bread`, `topic_spider_man_2`, `sym_pandas_testing_assert_almost_equal`, `dog`, `event_sadie_adler_unmasking`, `path_pandas_src_testing_pyx`, `caddy`, `yakuza`, `tattoos`, `cat_game`, `coffee_maker` |
| n23 | claim | t1:s10 | if someone needs the bald eagle, they are blue | `meets_needs`, `enables`, `recommended`, `earth`, `moon`, `fridge`, `important`, `leads_to`, `topic_baldurs_gate_3`, `color_label`, `statement`, `oak_chips` |
| n24 | object | t1:s10 | bald eagle → `animal_label::<key>` | `resource_chiller`, `topic_baldurs_gate_3`, `earth`, `oak_chips`, `animal_label`*, `moon`, `possesses`, `art_structured_report`, `meat`, `tattoos`, `coffee_maker`, `shape_oval` |
| n25 | object | t1:s10 | blue → `color_label::<key>` | `color_label`*, `chill`, `yakuza`, `right_of`, `fridge`, `dried_fruit`, `grape_merlot`, `sultana`, `lettuce`, `resource_chiller`, `on`, `coffee_maker` |
| n26 | claim | t1:s11 | if someone needs the lion, they eat the lion | `meets_needs`, `spoon`, `enables`, `constraint_single_choice`, `important`, `recommended`, `well_wishes`, `causes`, `requirement`, `motivated_by`, `piano`, `leads_to` |
| n27 | object | t1:s11 | lion → `animal_label::<key>` | `animal_label`*, `sym_pandas_testing_assert_almost_equal`, `style_catchy`, `cat_game`, `piano`, `path_pandas_src_testing_pyx`, `topic_spider_man_2`, `topic_classical_piano`, `cat_limited_time_offers`, `dog`, `coffee_maker`, `resource_chiller` |
| n28 | claim | t1:s12 | if someone eats the bear, the bear is kind | `comfortable`, `enables`, `style_catchy`, `pear`, `bread`, `possesses`, `recommended`, `important`, `statement`, `sym_pandas_testing_assert_almost_equal`, `well_wishes`, `leads_to` |
| n29 | object | t1:s12 | bear → `animal_label::<key>` | `animal_label`*, `bread`, `topic_spider_man_2`, `sym_pandas_testing_assert_almost_equal`, `dog`, `event_sadie_adler_unmasking`, `path_pandas_src_testing_pyx`, `caddy`, `yakuza`, `tattoos`, `cat_game`, `coffee_maker` |
| n30 | claim | t1:s13 | if someone is blue, they visit the bear | `enables`, `topic_spider_man_2`, `recommended`, `leads_to`, `important`, `yakuza`, `sym_pandas_testing_assert_almost_equal`, `dog`, `statement`, `outcome`, `causes`, `motivated_by` |
| n31 | object | t1:s13 | blue → `color_label::<key>` | `color_label`*, `chill`, `yakuza`, `right_of`, `fridge`, `dried_fruit`, `grape_merlot`, `sultana`, `lettuce`, `resource_chiller`, `on`, `coffee_maker` |
| n32 | object | t1:s13 | bear → `animal_label::<key>` | `animal_label`*, `bread`, `topic_spider_man_2`, `sym_pandas_testing_assert_almost_equal`, `dog`, `event_sadie_adler_unmasking`, `path_pandas_src_testing_pyx`, `caddy`, `yakuza`, `tattoos`, `cat_game`, `coffee_maker` |
| n33 | claim | t1:s14 | if the lion is rough and eats the squirrel, the lion is blue | `causes`, `enables`, `recommended`, `sym_pandas_testing_assert_almost_equal`, `important`, `style_catchy`, `leads_to`, `comfortable`, `path_pandas_src_testing_pyx`, `cat_game`, `motivated_by`, `statement` |
| n34 | object | t1:s14 | lion → `animal_label::<key>` | `animal_label`*, `sym_pandas_testing_assert_almost_equal`, `style_catchy`, `cat_game`, `piano`, `path_pandas_src_testing_pyx`, `topic_spider_man_2`, `topic_classical_piano`, `cat_limited_time_offers`, `dog`, `coffee_maker`, `resource_chiller` |
| n35 | object | t1:s14 | squirrel → `animal_label::<key>` | `animal_label`*, `topic_spider_man_2`, `topic_baldurs_gate_3`, `topic_pickup_lines`, `caddy`, `cat_game`, `mittens`, `cat_limited_time_offers`, `tattoos`, `oak_chips`, `tattooed_guests`, `resource_chiller` |
| n36 | object | t1:s14 | blue → `color_label::<key>` | `color_label`*, `chill`, `yakuza`, `right_of`, `fridge`, `dried_fruit`, `grape_merlot`, `sultana`, `lettuce`, `resource_chiller`, `on`, `coffee_maker` |
| n37 | claim | t1:s15 | if someone is blue and visits the bear, the bear needs the bald eagle | `possesses`, `meets_needs`, `enables`, `topic_spider_man_2`, `recommended`, `topic_baldurs_gate_3`, `dog`, `important`, `leads_to`, `statement`, `art_invitation`, `constraint_respectful` |
| n38 | object | t1:s15 | blue → `color_label::<key>` | `color_label`*, `chill`, `yakuza`, `right_of`, `fridge`, `dried_fruit`, `grape_merlot`, `sultana`, `lettuce`, `resource_chiller`, `on`, `coffee_maker` |
| n39 | object | t1:s15 | bear → `animal_label::<key>` | `animal_label`*, `bread`, `topic_spider_man_2`, `sym_pandas_testing_assert_almost_equal`, `dog`, `event_sadie_adler_unmasking`, `path_pandas_src_testing_pyx`, `caddy`, `yakuza`, `tattoos`, `cat_game`, `coffee_maker` |
| n40 | object | t1:s15 | bald eagle → `animal_label::<key>` | `resource_chiller`, `topic_baldurs_gate_3`, `earth`, `oak_chips`, `animal_label`*, `moon`, `possesses`, `art_structured_report`, `meat`, `tattoos`, `coffee_maker`, `shape_oval` |
| n41 | speech_act | t1:s16 | ask whether a statement is True, False, or Unknown | `ask`*, `statement`*, `confirm`, `respond`, `inform`, `propose`, `unaware`, `failure`, `conditional`, `controversial`, `negation`, `acknowledge` |
| n42 | constraint | t1:s16 | base the answer only on the provided theory | `respond`*, `extract`, `topic_baldurs_gate_3`, `subject`, `constraint_realistic`, `constraint_respectful`, `constraint_budget_limited`, `requirement`, `constraint_single_choice`, `constraint_comprehensive`, `supports`, `constraint_beginner` |
| n43 | constraint | t1:s16 | answer must be True, False, or Unknown | `constraint_realistic`, `constraint_respectful`, `constraint_budget_limited`, `constraint_comprehensive`, `requirement`, `constraint_single_choice`, `right_of`, `metric_order_late`, `constraint_beginner`, `rejects`, `constraint_include_character_attribute_list`, `failure` |
| n44 | claim | t1:s17 | the bear needs the bald eagle | `meets_needs`, `possesses`, `enables`, `topic_baldurs_gate_3`, `topic_spider_man_2`, `recommended`, `important`, `leads_to`, `statement`, `mittens`, `tattoos`, `causes` |
| n45 | object | t1:s17 | bear → `animal_label::<key>` | `animal_label`*, `bread`, `topic_spider_man_2`, `sym_pandas_testing_assert_almost_equal`, `dog`, `event_sadie_adler_unmasking`, `path_pandas_src_testing_pyx`, `caddy`, `yakuza`, `tattoos`, `cat_game`, `coffee_maker` |
| n46 | object | t1:s17 | bald eagle → `animal_label::<key>` | `resource_chiller`, `topic_baldurs_gate_3`, `earth`, `oak_chips`, `animal_label`*, `moon`, `possesses`, `art_structured_report`, `meat`, `tattoos`, `coffee_maker`, `shape_oval` |

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
- chill.destination → object_label
- failure.system → platform_label
- activity.object → object_label, food_label, animal_label
- activity.location → country
- activity.instrument → object_label, platform_label
- attribute_claim.subject → platform_label
- attribute_claim.value → platform_label

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

**rule_category_code_value** (v19/rule/category/code-value; rule governing sym_pandas_testing_assert_almost_equal)

path_/sym_ remain STRING identities; migrated chg_/assert_ are TERM constructors. Do not recover an exact file path by guessing from underscores.

**rule_category_constraint_value** (v19/rule/category/constraint-value; rule governing constraint_single_choice)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_descriptive_value** (v19/rule/category/descriptive-value; rule governing tattoos)

STRING modifier/domain label; never a free-form proposition. dom_sgi needs its intended referent established before semantically dependent use.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing earth)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_event_value** (v19/rule/category/event-value; rule governing event_sadie_adler_unmasking)

TERM-described narrative event, not a recorded EVENT. Require inclusion explicitly when generating a story.

**rule_category_metric_value** (v19/rule/category/metric-value; rule governing metric_order_late)

STRING metric identity, not a Boolean value. Uptime and response time need numeric observations with units; order-late is Boolean-valued. Do not type every metric as BOOL.

**rule_category_recipient_value** (v19/rule/category/recipient-value; rule governing tattooed_guests)

STRING roles or explicit named recipients. A role is not an exact person's identity. Keep an explicit name where substituting a role loses information.

**rule_category_search_value** (v19/rule/category/search-value; rule governing cat_game)

STRING refinements rank_ / dir_ / cat_ / avail_ / genre_ are separate. rank_rating may fill rank_field; genre_label::comedy may not. “Cheapest” usually requires both rank_price and dir_asc, not rank_price alone.

**rule_category_shape_value** (v19/rule/category/shape-value; rule governing shape_oval)

STRING geometry. shape_round may select a circular object; it does not imply color or dimensions.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing right_of)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_style_value** (v19/rule/category/style-value; rule governing style_catchy)

STRING production style. style_narrative does not establish that described events occurred.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_school_work_routine)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_composites_general** (v19/rule/composites-general; rule governing topic_school_work_routine)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_operations_general** (v19/rule/operations-general; rule governing hover)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_supplemental_general** (v19/rule/supplemental-general; rule governing coffee_maker)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; rule governing subject)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- chill | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Chill using the stated resource; same identity.  ⟵ candidate
- extract | operation | operation-vocabulary | (target: LIST[REF[STRING]], limit: NUMBER) -> LIST[REF[STRING]] | First limit results, preserving order and identity; limit is a nonnegative integer; limit=1 is still a list  ⟵ candidate
- hover | operation | operation-vocabulary | (target: REF[STRING]) -> void | Move pointer cursor over an interactive web element without clicking. target must resolve to a valid element reference. | aliases: mouse_over  ⟵ candidate

### speech acts

- acknowledge | speech_act | operation-vocabulary | UTTER acknowledge(target: CLAIM / TERM) | Acknowledge receipt/awareness; does not imply agreement.  ⟵ candidate
- ask | speech_act | operation-vocabulary | UTTER ask(target: TERM, or a sufficiently precise topic: STRING / TERM) | Request information/advice; not an assertion of an answer. | aliases: ask, how should  ⟵ candidate
- confirm | speech_act | operation-vocabulary | UTTER confirm(target: CLAIM) | Confirm the proposition; its evidence/status remains explicit.  ⟵ candidate
- express_interest | speech_act | operation-vocabulary | UTTER express_interest(target: STRING / TERM) | Speech act expressing conversational interest or engagement in a topic. speech act in dialogic traces. | aliases: show_interest  ⟵ candidate
- inform | speech_act | operation-vocabulary | UTTER inform(target: CLAIM) | Present the proposition; preserve its holder/status.  ⟵ candidate
- propose | speech_act | operation-vocabulary | UTTER propose(target: TERM) | Suggest an action/idea; does not record it as performed.  ⟵ candidate
- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ dependency of event_sadie_adler_unmasking
- conditional | constructor | TERM conditional(condition: TERM, consequence: TERM) -> TERM | Constructs a structured conditional proposition term connecting a condition and consequence. descriptive logic structure. | aliases: if_then  ⟵ candidate
- conjunction | constructor | TERM conjunction(items: LIST[TERM]) -> TERM | All described components apply | not: Does not imply temporal order  ⟵ candidate
- include | constructor | TERM include(item: STRING / TERM) -> TERM | Require the identified content/item | not: Not permission to invent an instance in a recorded trace  ⟵ dependency of constraint_include_character_attribute_list
- negation | constructor | TERM negation(target: TERM) -> TERM | Constructs a descriptive semantic negation of a target descriptive proposition or condition term. | not: Check's runtime Boolean operator NOT or a speech-act decline | aliases: not, does not, negation, absence of  ⟵ candidate
- property_question | constructor | TERM property_question(property: STRING, subject: STRING / TERM) -> TERM | An open request for a property of a subject | not: Does not supply the property's value  ⟵ candidate
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ candidate
- sequence | constructor | TERM sequence(items: LIST[TERM]) -> TERM | Ordered described activities/content | not: Not unordered conjunction  ⟵ dependency of event_sadie_adler_unmasking
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ candidate
- well_wishes | constructor | TERM well_wishes(recipient?: STRING / TERM, sentiment?: STRING) -> TERM | Constructs a conversational discourse term representing well-wishes, good luck expressions, or parting encouragement. | not: a salutation greeting (use greeting) or apology (use apologize) | aliases: good_luck, best_wishes, encouragement  ⟵ candidate

### composites

- constraint_beginner | composite | constraint-value | TERM constraint_beginner() -> TERM | Targeted at beginners. | = requirement(property="audience_expertise", value="beginner")  ⟵ candidate
- constraint_budget_limited | composite | constraint-value | TERM constraint_budget_limited() -> TERM | Limited budget. | = requirement(property="budget_limited", value=TRUE)  ⟵ candidate
- constraint_comprehensive | composite | constraint-value | TERM constraint_comprehensive() -> TERM | Must be comprehensive. | = requirement(property="comprehensive", value=TRUE)  ⟵ candidate
- constraint_include_character_attribute_list | composite | constraint-value | TERM constraint_include_character_attribute_list() -> TERM | Include character attributes. | = include(item="character_attribute_list")  ⟵ candidate
- constraint_realistic | composite | constraint-value | TERM constraint_realistic() -> TERM | Must be realistic. | = requirement(property="realistic", value=TRUE)  ⟵ candidate
- constraint_respectful | composite | constraint-value | TERM constraint_respectful() -> TERM | Must be respectful. | = requirement(property="respectful", value=TRUE)  ⟵ candidate
- constraint_single_choice | composite | constraint-value | TERM constraint_single_choice() -> TERM | Must pick a single choice. | = requirement(property="choice_count", value=1)  ⟵ candidate
- event_sadie_adler_unmasking | composite | event-value | TERM event_sadie_adler_unmasking() -> TERM | Sadie Adler taking off her hat and peeling skin. | = sequence(items=[activity(verb="remove", actor="Sadie Adler", object="hat"), activity(verb="peel", actor="Sadie Adler", object="skin")])  ⟵ candidate
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
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ candidate
- possesses | claim_relation | CLAIM possesses(subject: STRING / TERM, item: TERM, value: BOOL) | Asserts whether a subject possesses or lacks a stated property, capability, or entity. possession assertion with boolean polarity. | aliases: holds_property  ⟵ candidate
- recommended | claim_relation | CLAIM recommended(target: TERM / CLAIM) | Asserts an advisory recommendation that an activity or measure is advisable. advisory normative claim. | aliases: advisable  ⟵ candidate
- spatial_state | claim_relation | CLAIM spatial_state(relation: STRING, object: TERM, reference: TERM) | Asserts an observed spatial configuration between an object and a reference landmark. relation must specify spatial configuration. | aliases: placed_at, located_at  ⟵ related to statement
- statement | claim_relation | CLAIM statement(fact: TERM) | Foundational claim relation converting any descriptive TERM into an attributed, truth-evaluated assertion. universal fact assertion. | aliases: assert_fact, fact_claim, claim_statement  ⟵ candidate
- unaware | claim_relation | CLAIM unaware(person: STRING / TERM, topic: STRING / TERM) | Asserts epistemic lack of awareness regarding a topic, fact, or event. epistemic state. | aliases: ignorant_of  ⟵ candidate

### links

- contrast | link | LINK contrast(first: CLAIM, second: CLAIM) | Expresses rhetorical qualification, opposition, or contrast between two claims. link between claims. | aliases: qualification, however  ⟵ candidate
- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ candidate
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ core
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ candidate

### values

- art_invitation | value | artifact-value | An invitation card, announcement, or digital invite artifact for an event. | not: art_plan (an actionable procedure or schedule) or art_short_text (unstructured short text) | aliases: invitation, invitation card, invite, digital invitation, printable invitation  ⟵ candidate
- art_structured_report | value | artifact-value | Headed/structured report.  ⟵ candidate
- path_pandas_src_testing_pyx | value | code-value | Source code file path or exported symbol in scientific Python: path_pandas_src_testing_pyx. | aliases: path_pandas_src_testing_pyx  ⟵ candidate
- sym_pandas_testing_assert_almost_equal | value | code-value | Source code file path or exported symbol in scientific Python: sym_pandas_testing_assert_almost_equal. | aliases: sym_pandas_testing_assert_almost_equal  ⟵ candidate
- tattoos | value | descriptive-value | Descriptive concept of tattoos in cultural and social contexts. | aliases: tattoos  ⟵ candidate
- yakuza | value | descriptive-value | Descriptive concept of yakuza in cultural and social contexts. | aliases: yakuza  ⟵ candidate
- bread | value | entity-name | A bread loaf or slice food object. | aliases: bread  ⟵ candidate
- caddy | value | entity-name | A portable storage caddy, organizer box, or supply tote for carrying and organizing handheld tools and supplies. | not: cabinet (a stationary furniture cupboard) or safe (a secure metal lockbox) | aliases: caddy, supply caddy, wrapping caddy, tool caddy, organizer caddy, supply tote  ⟵ candidate
- coffee_maker | value | entity-name | A coffee-making appliance; not automatically a heating resource  ⟵ candidate
- dog | value | entity-name | Animal entity: dog. | not: animal_label::cat or animal_label::donkey | aliases: dog, dogs, canine, pup, puppy  ⟵ candidate
- dried_fruit | value | entity-name | Generic dried fruit food item. | not: fresh fruit or specific dried varieties like raisin or sultana | aliases: dried fruit, dried fruits  ⟵ candidate
- earth | value | entity-name | The planet Earth as an astronomical celestial body. | not: soil, ground surface, or electrical grounding | aliases: earth, the earth, planet earth, Earth  ⟵ candidate
- entity_order_vs_assemble_plan | value | entity-name | Event planning item or menu category: entity_order_vs_assemble_plan. | aliases: entity_order_vs_assemble_plan  ⟵ candidate
- fridge | value | entity-name | A refrigerator cooling appliance. | aliases: fridge  ⟵ candidate
- grape_merlot | value | entity-name | Merlot wine grape variety. | not: other red grape varieties such as grape_cabernet_sauvignon or grape_pinot_noir | aliases: Merlot, merlot grape  ⟵ candidate
- lettuce | value | entity-name | A head of lettuce or leafy green vegetable food item. | not: food_label::tomato or food_label::potato (other vegetable items) | aliases: lettuce, head of lettuce, salad greens  ⟵ candidate
- meat | value | entity-name | Food item: meat or beef. | not: animal_label::tuna or animal_label::fish (specific aquatic foods) | aliases: meat, beef  ⟵ candidate
- mittens | value | entity-name | Item or prop in joke/creative context: mittens. | aliases: mittens  ⟵ candidate
- moon | value | entity-name | Earth's natural celestial satellite. | not: an artificial satellite or other planetary moon | aliases: moon, the moon, Luna  ⟵ candidate
- oak_chips | value | entity-name | Oak wood pieces or barrels used for wine aging and flavor extraction. | not: grape_tannin or structural chemical additives | aliases: oak chips, oak pieces, oak barrels  ⟵ candidate
- pear | value | entity-name | A pear fruit item, typically an ingredient or fresh fruit object. | not: apple, food_label::tomato, or other distinct fruit items | aliases: pear, pears, fresh pear, sliced pear  ⟵ candidate
- piano | value | entity-name | A piano musical instrument or large furniture object. | not: topic_classical_piano or topic_jazz_piano (music genre topics) | aliases: piano, grand piano, upright piano, keyboard  ⟵ candidate
- resource_chiller | value | entity-name | Canonical abstract chilling resource when no particular appliance is named.  ⟵ candidate
- spoon | value | entity-name | An eating or cooking utensil. | aliases: spoon  ⟵ candidate
- sultana | value | entity-name | Dried white seedless grape food product. | not: raisin (dark dried grape) or wine_grape | aliases: sultana, sultanas, golden raisin  ⟵ candidate
- metric_order_late | value | metric-value | Whether an order is late. | aliases: order is late, delayed  ⟵ candidate
- tattooed_guests | value | recipient-value | Social, demographic, or institutional group: tattooed_guests. | aliases: tattooed_guests  ⟵ candidate
- cat_game | value | search-value | Category: video game.  ⟵ candidate
- cat_limited_time_offers | value | search-value | Category: time-limited deals.  ⟵ candidate
- shape_oval | value | shape-value | Oval. | aliases: oval  ⟵ candidate
- on | value | spatial-relation | Resting atop. | aliases: on top of  ⟵ candidate
- right_of | value | spatial-relation | To the right of. | aliases: right of  ⟵ candidate
- style_catchy | value | style-value | Catchy, attention-grabbing style. | aliases: catchy  ⟵ candidate
- topic_baldurs_gate_3 | value | topic-value | Baldur's Gate 3.  ⟵ candidate
- topic_classical_piano | value | topic-value | Classical piano.  ⟵ candidate
- topic_pickup_lines | value | topic-value | Pickup lines.  ⟵ candidate
- topic_spider_man_2 | value | topic-value | Marvel's Spider-Man 2.  ⟵ candidate
