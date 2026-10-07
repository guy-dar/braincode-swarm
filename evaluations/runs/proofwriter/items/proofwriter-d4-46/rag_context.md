# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 34 needs (decomposition: llm), 126 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | speech_act | t1:s1 | introduce a theory or set of premises | `respond`, `propose`, `inform`, `subject`, `supports`, `ask`, `conjunction`, `example_of`, `in_front_of`, `rule_structural_constructs`, `correct`, `express_interest` |
| n2 | claim | t1:s2 | Bob is cold | `state_cold`*, `state_dirty`, `motivated_by`, `leads_to`, `enables`, `outcome`, `chill`, `statement`, `causes`, `state_warm`, `mittens`, `important` |
| n3 | claim | t1:s3 | Bob is green | `lettuce`, `color_label`, `leads_to`, `enables`, `motivated_by`, `right_of`, `outcome`, `in_front_of`, `important`, `topic_spider_man_2`, `statement`, `causes` |
| n4 | constraint | t1:s3 | green → `color_label::<key>` | `color_label`*, `lettuce`, `outshines`, `right_of`, `constraint_exclude_flowery_language`, `left_of`, `grape_thompson_seedless`, `constraint_respectful`, `apple`, `constraint_realistic`, `shape_square`, `constraint_exclude_liberation_theme` |
| n5 | claim | t1:s4 | Bob is red | `indicator`, `color_label`, `enables`, `leads_to`, `motivated_by`, `outcome`, `statement`, `important`, `topic_spider_man_2`, `causes`, `comfortable`, `mug` |
| n6 | constraint | t1:s4 | red → `color_label::<key>` | `color_label`*, `color_pink`, `cinnamon`, `constraint_exclude_flowery_language`, `right_of`, `ginger`, `constraint_respectful`, `constraint_realistic`, `constraint_exclude_liberation_theme`, `pear`, `topic_current_events`, `constraint_budget_limited` |
| n7 | claim | t1:s5 | Bob is round | `shape_round`*, `in_front_of`, `enables`, `topic_baldurs_gate_3`, `leads_to`, `motivated_by`, `topic_pickup_lines`, `shape_triangular`, `shape_oval`, `important`, `shape_square`, `behind` |
| n8 | claim | t1:s6 | Fiona is green | `lettuce`, `color_label`, `color_pink`, `leads_to`, `enables`, `motivated_by`, `outcome`, `important`, `statement`, `yarn`, `outshines`, `grape_thompson_seedless` |
| n9 | constraint | t1:s6 | green → `color_label::<key>` | `color_label`*, `lettuce`, `outshines`, `right_of`, `constraint_exclude_flowery_language`, `left_of`, `grape_thompson_seedless`, `constraint_respectful`, `apple`, `constraint_realistic`, `shape_square`, `constraint_exclude_liberation_theme` |
| n10 | claim | t1:s7 | Fiona is smart | `style_catchy`, `enables`, `style_persuasive`, `outcome`, `leads_to`, `test_condition`, `motivated_by`, `important`, `path_ipython_core_magics_basic_py`, `statement`, `recommended`, `role_mother` |
| n11 | claim | t1:s8 | Gary is green | `lettuce`, `enables`, `color_label`, `leads_to`, `right_of`, `outshines`, `motivated_by`, `color_pink`, `outcome`, `important`, `left_of`, `statement` |
| n12 | constraint | t1:s8 | green → `color_label::<key>` | `color_label`*, `lettuce`, `outshines`, `right_of`, `constraint_exclude_flowery_language`, `left_of`, `grape_thompson_seedless`, `constraint_respectful`, `apple`, `constraint_realistic`, `shape_square`, `constraint_exclude_liberation_theme` |
| n13 | claim | t1:s9 | Gary is red | `color_pink`, `enables`, `cinnamon`, `outcome`, `leads_to`, `right_of`, `statement`, `motivated_by`, `important`, `ginger`, `topic_current_new_york_housing_market`, `recommended` |
| n14 | constraint | t1:s9 | red → `color_label::<key>` | `color_label`*, `color_pink`, `cinnamon`, `constraint_exclude_flowery_language`, `right_of`, `ginger`, `constraint_respectful`, `constraint_realistic`, `constraint_exclude_liberation_theme`, `pear`, `topic_current_events`, `constraint_budget_limited` |
| n15 | claim | t1:s10 | Harry is green | `lettuce`, `leads_to`, `enables`, `ginger`, `motivated_by`, `important`, `topic_spider_man_2`, `color_label`, `statement`, `outcome`, `united_kingdom`, `comfortable` |
| n16 | constraint | t1:s10 | green → `color_label::<key>` | `color_label`*, `lettuce`, `outshines`, `right_of`, `constraint_exclude_flowery_language`, `left_of`, `grape_thompson_seedless`, `constraint_respectful`, `apple`, `constraint_realistic`, `shape_square`, `constraint_exclude_liberation_theme` |
| n17 | claim | t1:s11 | Harry is smart | `important`, `style_catchy`, `style_persuasive`, `enables`, `motivated_by`, `leads_to`, `path_ipython_core_magics_basic_py`, `test_condition`, `outcome`, `comfortable`, `statement`, `recommended` |
| n18 | reasoning | t1:s12 | all smart people are cold | `state_cold`*, `unit_fahrenheit`, `style_catchy`, `rejects`, `supports`, `cinnamon`, `chill`, `state_dirty`, `mittens`, `contrast`, `heat`, `state_warm` |
| n19 | reasoning | t1:s13 | if someone is red then they are rough | `color_label`, `indicator`, `then`*, `state_dirty`, `color_pink`, `cinnamon`, `rejects`, `supports`, `style_catchy`, `tone_empathetic`, `character_trait`, `topic_profanity` |
| n20 | constraint | t1:s13 | red → `color_label::<key>` | `color_label`*, `color_pink`, `cinnamon`, `constraint_exclude_flowery_language`, `right_of`, `ginger`, `constraint_respectful`, `constraint_realistic`, `constraint_exclude_liberation_theme`, `pear`, `topic_current_events`, `constraint_budget_limited` |
| n21 | reasoning | t1:s14 | all nice, red people are green | `color_label`, `lettuce`, `apple`, `color_pink`, `supports`, `rejects`, `foreigners`, `revises`, `contrast`, `tone_polite`, `liberal_onsen`, `united_kingdom` |
| n22 | constraint | t1:s14 | red → `color_label::<key>` | `color_label`*, `color_pink`, `cinnamon`, `constraint_exclude_flowery_language`, `right_of`, `ginger`, `constraint_respectful`, `constraint_realistic`, `constraint_exclude_liberation_theme`, `pear`, `topic_current_events`, `constraint_budget_limited` |
| n23 | constraint | t1:s14 | green → `color_label::<key>` | `color_label`*, `lettuce`, `outshines`, `right_of`, `constraint_exclude_flowery_language`, `left_of`, `grape_thompson_seedless`, `constraint_respectful`, `apple`, `constraint_realistic`, `shape_square`, `constraint_exclude_liberation_theme` |
| n24 | reasoning | t1:s15 | all red, rough people are round | `shape_round`*, `rule_category_shape_value`, `color_pink`, `rejects`, `color_label`, `supports`, `shape_oval`, `shape_square`, `cinnamon`, `corner`, `shape_triangular`, `shape_rectangular` |
| n25 | constraint | t1:s15 | red → `color_label::<key>` | `color_label`*, `color_pink`, `cinnamon`, `constraint_exclude_flowery_language`, `right_of`, `ginger`, `constraint_respectful`, `constraint_realistic`, `constraint_exclude_liberation_theme`, `pear`, `topic_current_events`, `constraint_budget_limited` |
| n26 | reasoning | t1:s16 | if someone is rough and round then they are smart | `shape_round`*, `rule_category_shape_value`, `then`*, `style_catchy`, `tone_silly`, `supports`, `tone_polite`, `style_persuasive`, `rejects`, `test_condition`, `shape_oval`, `associated_with` |
| n27 | reasoning | t1:s17 | if Gary is smart and Gary is cold then Gary is nice | `state_cold`*, `then`*, `supports`, `style_catchy`, `right_of`, `tone_silly`, `rejects`, `style_persuasive`, `topic_baldurs_gate_3`, `condition_perfect`, `contrast`, `tone_polite` |
| n28 | reasoning | t1:s18 | green, smart people are red | `color_label`, `lettuce`, `apple`, `color_pink`, `style_catchy`, `outshines`, `rejects`, `supports`, `foreigners`, `style_persuasive`, `revises`, `bionic_person` |
| n29 | constraint | t1:s18 | green → `color_label::<key>` | `color_label`*, `lettuce`, `outshines`, `right_of`, `constraint_exclude_flowery_language`, `left_of`, `grape_thompson_seedless`, `constraint_respectful`, `apple`, `constraint_realistic`, `shape_square`, `constraint_exclude_liberation_theme` |
| n30 | constraint | t1:s18 | red → `color_label::<key>` | `color_label`*, `color_pink`, `cinnamon`, `constraint_exclude_flowery_language`, `right_of`, `ginger`, `constraint_respectful`, `constraint_realistic`, `constraint_exclude_liberation_theme`, `pear`, `topic_current_events`, `constraint_budget_limited` |
| n31 | speech_act | t1:s19 | ask if a statement is True, False, or Unknown | `ask`*, `statement`*, `confirm`, `respond`, `failure`, `inform`, `controversial`, `correct`, `motivated_by`, `unaware`, `run_tests`, `propose` |
| n32 | constraint | t1:s19 | base the answer only on the provided theory | `respond`*, `extract`, `subject`, `topic_baldurs_gate_3`, `constraint_exclude_flowery_language`, `constraint_realistic`, `supports`, `constraint_budget_limited`, `constraint_respectful`, `conjunction`, `constraint_exclude_liberation_theme`, `regression_case` |
| n33 | constraint | t1:s19 | answer must be True, False, or Unknown | `constraint_realistic`, `right_of`, `in_front_of`, `constraint_respectful`, `constraint_exclude_flowery_language`, `failure`, `metric_order_late`, `constraint_budget_limited`, `rejects`, `respond`*, `constraint_comprehensive`, `constraint_exclude_liberation_theme` |
| n34 | object | t1:s20 | the statement 'Gary is cold' to evaluate | `state_cold`*, `statement`*, `chill`, `heat`, `state_dirty`, `topic_baldurs_gate_3`, `assert_multinomial_scorer`, `state_warm`, `supports`, `rule_category_state_value`, `test_condition`, `rejects` |

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
- chill.destination → object_label
- heat.destination → object_label
- failure.system → platform_label
- run_tests.target → platform_label
- regression_case.framework → platform_label
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

**rule_recording_signatures** (v19/rule/recording-signatures; rule governing chill)

RECORD ACTION uses the operation signature with REF[STRING] → TERM and LIST[REF[STRING]] → LIST[TERM]; other types/categories stay unchanged. Return EVENT, never the runtime result. Record actual outputs as attributed CLAIMs. Do not infer missing resources.

**rule_speech_acts_general** (v19/rule/speech-acts-general; rule governing respond)

UTTER-only, void, with the spec's speech attributes and LIST[TERM] constraints. No result binding. Literal content cannot replace required semantic arguments for structured coverage.

**rule_structural_constructs** (v19/rule/structural-constructs; candidate)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; rule governing supports)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_category_code_value** (v19/rule/category/code-value; rule governing path_ipython_core_magics_basic_py)

path_/sym_ remain STRING identities; migrated chg_/assert_ are TERM constructors. Do not recover an exact file path by guessing from underscores.

**rule_category_constraint_value** (v19/rule/category/constraint-value; rule governing constraint_exclude_flowery_language)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing mittens)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_location_name** (v19/rule/category/location-name; rule governing united_kingdom)

STRING location descriptor. A `table` surface is not the generated artifact category art_table.

**rule_category_metric_value** (v19/rule/category/metric-value; rule governing metric_order_late)

STRING metric identity, not a Boolean value. Uptime and response time need numeric observations with units; order-late is Boolean-valued. Do not type every metric as BOOL.

**rule_category_product_attribute_value** (v19/rule/category/product-attribute-value; rule governing color_pink)

STRING color/size/product-market facets. gender_women describes a product category, not an assertion about a person's gender.

**rule_category_recipient_value** (v19/rule/category/recipient-value; rule governing role_mother)

STRING roles or explicit named recipients. A role is not an exact person's identity. Keep an explicit name where substituting a role loses information.

**rule_category_shape_value** (v19/rule/category/shape-value; candidate)

STRING geometry. shape_round may select a circular object; it does not imply color or dimensions.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing in_front_of)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_state_value** (v19/rule/category/state-value; candidate)

STRING condition used in selection. state_warm does not command heat; “hot” is not automatically synonymous with “warm.”

**rule_category_style_value** (v19/rule/category/style-value; rule governing style_catchy)

STRING production style. style_narrative does not establish that described events occurred.

**rule_category_tone_value** (v19/rule/category/tone-value; rule governing tone_empathetic)

STRING register. tone_urgent describes urgency, not a concrete deadline.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_spider_man_2)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_composites_general** (v19/rule/composites-general; rule governing constraint_exclude_flowery_language)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_operations_general** (v19/rule/operations-general; rule governing chill)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_supplemental_general** (v19/rule/supplemental-general; rule governing extract)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; rule governing subject)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- chill | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Chill using the stated resource; same identity.  ⟵ candidate
- extract | operation | operation-vocabulary | (target: LIST[REF[STRING]], limit: NUMBER) -> LIST[REF[STRING]] | First limit results, preserving order and identity; limit is a nonnegative integer; limit=1 is still a list  ⟵ candidate
- heat | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Heat using the stated resource; same identity. Selecting a warm object does not imply heating it.  ⟵ candidate
- run_tests | operation | operation-vocabulary | (target: STRING / ATOM[platform_label], assertion?: TERM) -> BOOL | Run the selected project's tests, optionally checking the specified assertion. TRUE means the declared test condition passed, not overall software correctness.  ⟵ candidate
- turn | operation | operation-vocabulary | (direction: STRING) -> void | Rotate agent body/view orientation. direction is typically left, right, or angle. | aliases: rotate, turn_around  ⟵ related to then
- walk | operation | operation-vocabulary | (destination: STRING / TERM / ATOM[object_label], relation?: STRING) -> void | Locomote towards a target destination or landmark. destination must identify a valid entity or location. | aliases: move_to, go_to, navigate_to  ⟵ related to then

### speech acts

- ask | speech_act | operation-vocabulary | UTTER ask(target: TERM, or a sufficiently precise topic: STRING / TERM) | Request information/advice; not an assertion of an answer. | aliases: ask, how should  ⟵ candidate
- confirm | speech_act | operation-vocabulary | UTTER confirm(target: CLAIM) | Confirm the proposition; its evidence/status remains explicit.  ⟵ candidate
- correct | speech_act | operation-vocabulary | UTTER correct(target: CLAIM) | Offer corrected content. Actual supersession requires the Conversation revision rules.  ⟵ candidate
- express_interest | speech_act | operation-vocabulary | UTTER express_interest(target: STRING / TERM) | Speech act expressing conversational interest or engagement in a topic. speech act in dialogic traces. | aliases: show_interest  ⟵ candidate
- inform | speech_act | operation-vocabulary | UTTER inform(target: CLAIM) | Present the proposition; preserve its holder/status.  ⟵ candidate
- propose | speech_act | operation-vocabulary | UTTER propose(target: TERM) | Suggest an action/idea; does not record it as performed.  ⟵ candidate
- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- bionic_person | constructor | TERM bionic_person(composition?: STRING / TERM) -> TERM | Constructs a descriptive representation of a bionic person or cyborg entity with biological and mechanical components. | not: a standard human role (use role_user or role_adults) or a purely artificial device. | aliases: bionic person, bionic people, cyborg, half human half robot  ⟵ candidate
- character_trait | constructor | TERM character_trait(property: STRING, value: STRING / NUMBER) -> TERM | A character attribute | not: Not a claim about a real person  ⟵ candidate
- conditional | constructor | TERM conditional(condition: TERM, consequence: TERM) -> TERM | Constructs a structured conditional proposition term connecting a condition and consequence. descriptive logic structure. | aliases: if_then  ⟵ candidate
- conjunction | constructor | TERM conjunction(items: LIST[TERM]) -> TERM | All described components apply | not: Does not imply temporal order  ⟵ candidate
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ dependency of constraint_exclude_flowery_language
- indicator | constructor | TERM indicator(condition: STRING / TERM, indicator_type?: STRING) -> TERM | Constructs a descriptive term representing a warning sign, behavioral marker, or red flag indicating an underlying condition or risk. | not: warning (a system alert claim relation) or color_label::red (a product color) | aliases: red flag, warning sign, behavioral marker, signal  ⟵ candidate
- negation | constructor | TERM negation(target: TERM) -> TERM | Constructs a descriptive semantic negation of a target descriptive proposition or condition term. | not: Check's runtime Boolean operator NOT or a speech-act decline | aliases: not, does not, negation, absence of  ⟵ candidate
- outshines | constructor | TERM outshines(brighter: STRING / TERM, dimmer: STRING / TERM) -> TERM | Constructs a description of relative visual brightness where a brighter light source overpowers the perceived brightness of a dimmer object. | not: an absolute numeric brightness measurement | aliases: outshines, overpowers brightness, drowns out light  ⟵ candidate
- regression_case | constructor | TERM regression_case(framework: STRING / ATOM[platform_label], modifier: STRING, relation: STRING) -> TERM | A regression scenario specifying affected framework, condition and relation | not: Does not invent a passing test or exact implementation  ⟵ candidate
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ dependency of constraint_respectful
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ candidate
- test_condition | constructor | TERM test_condition(condition: STRING, expected: BOOL) -> TERM | A testable condition with the expected Boolean outcome | not: Expected outcome is not an observed result  ⟵ candidate
- well_wishes | constructor | TERM well_wishes(recipient?: STRING / TERM, sentiment?: STRING) -> TERM | Constructs a conversational discourse term representing well-wishes, good luck expressions, or parting encouragement. | not: a salutation greeting (use greeting) or apology (use apologize) | aliases: good_luck, best_wishes, encouragement  ⟵ candidate

### composites

- assert_multinomial_scorer | composite | code-value | TERM assert_multinomial_scorer() -> TERM | Assertion that multinomial probabilistic scoring succeeds. | = test_condition(condition="multinomial_probabilistic_scoring", expected=TRUE)  ⟵ candidate
- constraint_budget_limited | composite | constraint-value | TERM constraint_budget_limited() -> TERM | Limited budget. | = requirement(property="budget_limited", value=TRUE)  ⟵ candidate
- constraint_comprehensive | composite | constraint-value | TERM constraint_comprehensive() -> TERM | Must be comprehensive. | = requirement(property="comprehensive", value=TRUE)  ⟵ candidate
- constraint_exclude_flowery_language | composite | constraint-value | TERM constraint_exclude_flowery_language() -> TERM | Avoid flowery language. | = exclude(item="flowery_language")  ⟵ candidate
- constraint_exclude_liberation_theme | composite | constraint-value | TERM constraint_exclude_liberation_theme() -> TERM | Avoid liberation theme. | = exclude(item="liberation_theme")  ⟵ candidate
- constraint_realistic | composite | constraint-value | TERM constraint_realistic() -> TERM | Must be realistic. | = requirement(property="realistic", value=TRUE)  ⟵ candidate
- constraint_respectful | composite | constraint-value | TERM constraint_respectful() -> TERM | Must be respectful. | = requirement(property="respectful", value=TRUE)  ⟵ candidate
- topic_current_new_york_housing_market | composite | topic-value | TERM topic_current_new_york_housing_market(as_of: STRING) -> TERM | Current New York housing market. | = subject(kind="housing_market", location="New York", time=$as_of)  ⟵ candidate
- topic_profanity | composite | topic-value | TERM topic_profanity() -> TERM | A composite term representing the topic of profanity. | = subject(kind="profanity") | not: potential_harms (which is generic) | aliases: profanity  ⟵ candidate

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
- motivated_by | claim_relation | CLAIM motivated_by(claim: CLAIM, motive: STRING / TERM) | Asserts that an action, rule, or claim is motivated by an underlying motive or goal. motive explanation. | aliases: rationale_is  ⟵ candidate
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ candidate
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

- path_ipython_core_magics_basic_py | value | code-value | File path to the IPython basic magics module. | not: an individual command line script or general config file | aliases: IPython/core/magics/basic.py, ipython_core_magics_basic_py  ⟵ candidate
- apple | value | entity-name | An apple fruit item, typically an ingredient or interactive food object. | not: food_label::tomato or other fruits/vegetables | aliases: apple, apples, red apple, green apple, apple slice  ⟵ candidate
- cinnamon | value | entity-name | Ground or whole cinnamon culinary spice from Cinnamomum tree bark. | not: nutmeg, cloves, or other distinct spice varieties | aliases: cinnamon, ground cinnamon, cinnamon spice, cinnamon stick  ⟵ candidate
- ginger | value | entity-name | Pungent aromatic spice root from Zingiber officinale used in cooking and baking. | not: cinnamon, cardamom, or other distinct spice varieties | aliases: ginger, ground ginger, fresh ginger, ginger root  ⟵ candidate
- grape_thompson_seedless | value | entity-name | Thompson Seedless grape variety. | not: wine grape cultivars like grape_merlot or grape_chardonnay | aliases: Thompson Seedless, thompson seedless grape, sultana grape  ⟵ candidate
- lettuce | value | entity-name | A head of lettuce or leafy green vegetable food item. | not: food_label::tomato or food_label::potato (other vegetable items) | aliases: lettuce, head of lettuce, salad greens  ⟵ candidate
- mittens | value | entity-name | Item or prop in joke/creative context: mittens. | aliases: mittens  ⟵ candidate
- mug | value | entity-name | Drinking cup. | aliases: mug  ⟵ candidate
- pear | value | entity-name | A pear fruit item, typically an ingredient or fresh fruit object. | not: apple, food_label::tomato, or other distinct fruit items | aliases: pear, pears, fresh pear, sliced pear  ⟵ candidate
- resource_chiller | value | entity-name | Canonical abstract chilling resource when no particular appliance is named.  ⟵ candidate
- yarn | value | entity-name | Item or prop in joke/creative context: yarn. | aliases: yarn  ⟵ candidate
- corner | value | location-name | A corner area.  ⟵ candidate
- liberal_onsen | value | location-name | Traditional Japanese establishment or hospitality venue: liberal_onsen. | aliases: liberal_onsen  ⟵ candidate
- united_kingdom | value | location-name | Geopolitical nation or sovereign state: United Kingdom (Great Britain). | not: locale_en_gb (a language/locale code, not a location) | aliases: United Kingdom, UK, Great Britain, Britain  ⟵ candidate
- metric_order_late | value | metric-value | Whether an order is late. | aliases: order is late, delayed  ⟵ candidate
- color_pink | value | product-attribute-value | Pink visual color qualifier. | not: color_label::red, color_label::purple, or other distinct color shades | aliases: pink, color_pink, blush pink, rose pink, pastel pink  ⟵ candidate
- condition_perfect | value | product-attribute-value | Product condition rating: perfect or mint physical and operational condition. | not: test_condition (software testing) or state_dirty (physical environmental state) | aliases: perfect, mint, pristine, flawless, like new  ⟵ candidate
- foreigners | value | recipient-value | Social, demographic, or institutional group: foreigners. | aliases: foreigners  ⟵ candidate
- role_mother | value | recipient-value | The mother of the user. | not: role_sister or role_kids | aliases: my mom, mother, mom  ⟵ candidate
- shape_oval | value | shape-value | Oval. | aliases: oval  ⟵ candidate
- shape_rectangular | value | shape-value | Rectangular. | aliases: rectangular, rectangle  ⟵ candidate
- shape_round | value | shape-value | Circular/round. | aliases: round, circular  ⟵ candidate
- shape_square | value | shape-value | Square. | aliases: square  ⟵ candidate
- shape_triangular | value | shape-value | Triangular. | aliases: triangular, triangle  ⟵ candidate
- behind | value | spatial-relation | Positioned behind.  ⟵ candidate
- in_front_of | value | spatial-relation | Positioned in front of. | aliases: in front of  ⟵ candidate
- left_of | value | spatial-relation | To the left of. | aliases: left of  ⟵ candidate
- on | value | spatial-relation | Resting atop. | aliases: on top of  ⟵ candidate
- right_of | value | spatial-relation | To the right of. | aliases: right of  ⟵ candidate
- state_cold | value | state-value | Cold or chilled condition. | aliases: cold, chilled  ⟵ candidate
- state_dirty | value | state-value | Dirty condition. | aliases: dirty  ⟵ candidate
- state_warm | value | state-value | Warm or heated condition. | aliases: warm, hot  ⟵ candidate
- style_catchy | value | style-value | Catchy, attention-grabbing style. | aliases: catchy  ⟵ candidate
- style_persuasive | value | style-value | Persuasive/argumentative style. | aliases: persuasive  ⟵ candidate
- tone_empathetic | value | tone-value | Conveys empathy/understanding. | aliases: sympathetically  ⟵ candidate
- tone_polite | value | tone-value | Courteous, respectful register. | aliases: politely, kindly  ⟵ candidate
- tone_silly | value | tone-value | Playful, lighthearted, or silly conversational tone. | aliases: silly  ⟵ candidate
- topic_baldurs_gate_3 | value | topic-value | Baldur's Gate 3.  ⟵ candidate
- topic_current_events | value | topic-value | Current news, geopolitical events, and ongoing international developments. | aliases: current_events, news  ⟵ candidate
- topic_pickup_lines | value | topic-value | Pickup lines.  ⟵ candidate
- topic_spider_man_2 | value | topic-value | Marvel's Spider-Man 2.  ⟵ candidate
- unit_fahrenheit | value | unit-value | Standard unit of temperature measurement on the Fahrenheit scale. | not: qualitative thermal states (use state_warm or state_cold) or duration units (use unit_minute, etc.) | aliases: Fahrenheit, deg F, degrees Fahrenheit, degrees F, F  ⟵ candidate
