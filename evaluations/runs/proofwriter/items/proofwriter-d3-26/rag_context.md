# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 30 needs (decomposition: llm), 125 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | speech_act | t1:s1 | Introduce a set of facts and rules as a theory | `respond`, `propose`, `statement`, `subject`, `ask`, `failure`, `inform`, `supports`, `example_of`, `topic_politics`, `rule_trace_relations_general`, `reason_for` |
| n2 | claim | t1:s2 | Bob is kind | `comfortable`, `style_catchy`, `enables`, `well_wishes`, `right_of`, `important`, `recommended`, `leads_to`, `motivated_by`, `tone_polite`, `statement`, `role_professor` |
| n3 | claim | t1:s3 | Bob is young | `topic_profanity`, `constraint_17_plus`, `enables`, `leads_to`, `important`, `size_small`, `outcome`, `rule_support_primitives_general`, `recommended`, `motivated_by`, `statement`, `role_kids` |
| n4 | claim | t1:s4 | Dave is kind | `comfortable`, `enables`, `style_catchy`, `important`, `well_wishes`, `recommended`, `leads_to`, `tone_polite`, `similarity`, `bowtie`, `motivated_by`, `statement` |
| n5 | claim | t1:s5 | Dave is red | `enables`, `yarn`, `cinnamon`, `leads_to`, `outcome`, `important`, `grape_tannin`, `pear`, `statement`, `recommended`, `motivated_by`, `color_pink` |
| n6 | constraint | t1:s5 | red → `color_label::<key>` | `color_label`*, `color_pink`, `cinnamon`, `constraint_exclude_flowery_language`, `constraint_respectful`, `pear`, `right_of`, `constraint_realistic`, `constraint_include_character_attribute_list`, `constraint_budget_limited`, `ginger`, `constraint_exclude_liberation_theme` |
| n7 | claim | t1:s6 | Fiona is big | `enables`, `size_large`, `important`, `style_catchy`, `leads_to`, `yarn`, `size_tall`, `character_trait`, `statement`, `recommended`, `outcome`, `size_small` |
| n8 | claim | t1:s7 | Fiona is cold | `state_cold`*, `event_sadie_adler_unmasking`, `cinnamon`, `character_trait`, `enables`, `yarn`, `chill`, `important`, `leads_to`, `motivated_by`, `state_dirty`, `statement` |
| n9 | claim | t1:s8 | Fiona is kind | `comfortable`, `style_catchy`, `style_persuasive`, `enables`, `has_attribute`, `well_wishes`, `important`, `character_trait`, `recommended`, `yarn`, `leads_to`, `motivated_by` |
| n10 | claim | t1:s9 | Fiona is smart | `style_catchy`, `enables`, `style_persuasive`, `important`, `role_mother`, `recommended`, `leads_to`, `test_condition`, `outcome`, `statement`, `motivated_by`, `path_ipython_core_magics_basic_py` |
| n11 | claim | t1:s10 | Fiona is young | `enables`, `constraint_17_plus`, `role_mother`, `yarn`, `leads_to`, `character_trait`, `topic_profanity`, `important`, `recommended`, `outcome`, `size_small`, `role_sister` |
| n12 | claim | t1:s11 | Harry is big | `important`, `enables`, `size_large`, `leads_to`, `united_kingdom`, `statement`, `comfortable`, `recommended`, `size_tall`, `motivated_by`, `correct`, `outcome` |
| n13 | claim | t1:s12 | Big and smart people are red | `style_catchy`, `outshines`, `enables`, `foreigners`, `important`, `color_pink`, `outcome`, `size_large`, `leads_to`, `style_persuasive`, `recommended`, `statement` |
| n14 | constraint | t1:s12 | red → `color_label::<key>` | `color_label`*, `color_pink`, `cinnamon`, `constraint_exclude_flowery_language`, `constraint_respectful`, `pear`, `right_of`, `constraint_realistic`, `constraint_include_character_attribute_list`, `constraint_budget_limited`, `ginger`, `constraint_exclude_liberation_theme` |
| n15 | claim | t1:s13 | Young and red people are big | `enables`, `important`, `group_size`, `role_kids`, `leads_to`, `character_trait`, `foreigners`, `size_large`, `outcome`, `constraint_17_plus`, `statement`, `recommended` |
| n16 | constraint | t1:s13 | red → `color_label::<key>` | `color_label`*, `color_pink`, `cinnamon`, `constraint_exclude_flowery_language`, `constraint_respectful`, `pear`, `right_of`, `constraint_realistic`, `constraint_include_character_attribute_list`, `constraint_budget_limited`, `ginger`, `constraint_exclude_liberation_theme` |
| n17 | claim | t1:s14 | If someone is smart then they are red | `style_catchy`, `outshines`, `enables`, `color_pink`, `important`, `tone_polite`, `tone_silly`, `outcome`, `leads_to`, `recommended`, `motivated_by`, `style_persuasive` |
| n18 | constraint | t1:s14 | red → `color_label::<key>` | `color_label`*, `color_pink`, `cinnamon`, `constraint_exclude_flowery_language`, `constraint_respectful`, `pear`, `right_of`, `constraint_realistic`, `constraint_include_character_attribute_list`, `constraint_budget_limited`, `ginger`, `constraint_exclude_liberation_theme` |
| n19 | claim | t1:s15 | All big and kind people are rough | `stereotype`, `character_trait`, `enables`, `style_catchy`, `topic_greatest_cricketer_of_all_time`, `important`, `leads_to`, `outcome`, `well_wishes`, `recommended`, `foreigners`, `group_size` |
| n20 | claim | t1:s16 | Red and big people are kind | `style_catchy`, `enables`, `well_wishes`, `foreigners`, `style_persuasive`, `important`, `group_size`, `leads_to`, `recommended`, `outcome`, `statement`, `comfortable` |
| n21 | constraint | t1:s16 | red → `color_label::<key>` | `color_label`*, `color_pink`, `cinnamon`, `constraint_exclude_flowery_language`, `constraint_respectful`, `pear`, `right_of`, `constraint_realistic`, `constraint_include_character_attribute_list`, `constraint_budget_limited`, `ginger`, `constraint_exclude_liberation_theme` |
| n22 | claim | t1:s17 | If someone is young then they are cold | `state_cold`*, `topic_profanity`, `constraint_17_plus`, `enables`, `leads_to`, `motivated_by`, `mittens`, `important`, `recommended`, `statement`, `chill`, `state_dirty` |
| n23 | claim | t1:s18 | All kind people are smart | `style_catchy`, `tone_polite`, `well_wishes`, `enables`, `style_persuasive`, `important`, `recommended`, `tone_silly`, `leads_to`, `outcome`, `motivated_by`, `foreigners` |
| n24 | claim | t1:s19 | All rough and smart people are young | `style_catchy`, `tone_silly`, `topic_profanity`, `constraint_17_plus`, `character_trait`, `enables`, `leads_to`, `state_dirty`, `important`, `outcome`, `recommended`, `tone_polite` |
| n25 | claim | t1:s20 | All big people are smart | `style_catchy`, `size_large`, `enables`, `important`, `group_size`, `outshines`, `outcome`, `size_queen`, `recommended`, `leads_to`, `statement`, `foreigners` |
| n26 | speech_act | t1:s21 | Ask whether a statement is True, False, or Unknown | `ask`*, `statement`*, `confirm`, `respond`, `failure`, `correct`, `inform`, `unaware`, `express_interest`, `motivated_by`, `propose`, `controversial` |
| n27 | constraint | t1:s21 | Base the answer only on the provided theory | `respond`*, `extract`, `subject`, `topic_baldurs_gate_3`, `constraint_realistic`, `constraint_respectful`, `constraint_exclude_flowery_language`, `supports`, `constraint_budget_limited`, `constraint_include_character_attribute_list`, `conjunction`, `constraint_beginner` |
| n28 | constraint | t1:s21 | Answer must be True, False, or Unknown | `constraint_realistic`, `right_of`, `constraint_respectful`, `constraint_exclude_flowery_language`, `metric_order_late`, `failure`, `constraint_include_character_attribute_list`, `constraint_budget_limited`, `constraint_comprehensive`, `constraint_beginner`, `respond`*, `entity_flowers` |
| n29 | claim | t1:s22 | Dave is not rough | `comfortable`, `character_trait`, `enables`, `rule_support_primitives_general`, `style_catchy`, `leads_to`, `important`, `tone_silly`, `recommended`, `rule_category_character_property_value`, `negation`, `grape_thompson_seedless` |
| n30 | negation | t1:s22 | not rough | `style_catchy`, `negation`, `state_dirty`, `constraint_exclude_flowery_language`, `exclude`, `rejects`, `weather_condition`, `comfortable`, `decline`, `tone_polite`, `spatula`, `tone_empathetic` |

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
- chill.destination → object_label
- weather_condition.location → country
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

**rule_recording_signatures** (v19/rule/recording-signatures; rule governing chill)

RECORD ACTION uses the operation signature with REF[STRING] → TERM and LIST[REF[STRING]] → LIST[TERM]; other types/categories stay unchanged. Return EVENT, never the runtime result. Record actual outputs as attributed CLAIMs. Do not infer missing resources.

**rule_speech_acts_general** (v19/rule/speech-acts-general; rule governing respond)

UTTER-only, void, with the spec's speech attributes and LIST[TERM] constraints. No result binding. Literal content cannot replace required semantic arguments for structured coverage.

**rule_structural_constructs** (v19/rule/structural-constructs; core)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; candidate)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_category_character_property_value** (v19/rule/category/character-property-value; candidate)

TERM-described trait/style. Use constraints and explicit inclusion/scope; do not use an ungoverned character_properties attribute.

**rule_category_code_value** (v19/rule/category/code-value; rule governing path_ipython_core_magics_basic_py)

path_/sym_ remain STRING identities; migrated chg_/assert_ are TERM constructors. Do not recover an exact file path by guessing from underscores.

**rule_category_constraint_value** (v19/rule/category/constraint-value; rule governing constraint_17_plus)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing bowtie)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_event_value** (v19/rule/category/event-value; rule governing event_sadie_adler_unmasking)

TERM-described narrative event, not a recorded EVENT. Require inclusion explicitly when generating a story.

**rule_category_location_name** (v19/rule/category/location-name; rule governing united_kingdom)

STRING location descriptor. A `table` surface is not the generated artifact category art_table.

**rule_category_metric_value** (v19/rule/category/metric-value; rule governing metric_order_late)

STRING metric identity, not a Boolean value. Uptime and response time need numeric observations with units; order-late is Boolean-valued. Do not type every metric as BOOL.

**rule_category_product_attribute_value** (v19/rule/category/product-attribute-value; rule governing size_small)

STRING color/size/product-market facets. gender_women describes a product category, not an assertion about a person's gender.

**rule_category_recipient_value** (v19/rule/category/recipient-value; rule governing role_professor)

STRING roles or explicit named recipients. A role is not an exact person's identity. Keep an explicit name where substituting a role loses information.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing right_of)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_state_value** (v19/rule/category/state-value; rule governing state_cold)

STRING condition used in selection. state_warm does not command heat; “hot” is not automatically synonymous with “warm.”

**rule_category_style_value** (v19/rule/category/style-value; rule governing style_catchy)

STRING production style. style_narrative does not establish that described events occurred.

**rule_category_tone_value** (v19/rule/category/tone-value; rule governing tone_polite)

STRING register. tone_urgent describes urgency, not a concrete deadline.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_politics)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_composites_general** (v19/rule/composites-general; rule governing topic_profanity)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_operations_general** (v19/rule/operations-general; rule governing chill)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_supplemental_general** (v19/rule/supplemental-general; rule governing extract)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; candidate)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- chill | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Chill using the stated resource; same identity.  ⟵ candidate
- extract | operation | operation-vocabulary | (target: LIST[REF[STRING]], limit: NUMBER) -> LIST[REF[STRING]] | First limit results, preserving order and identity; limit is a nonnegative integer; limit=1 is still a list  ⟵ candidate
- turn | operation | operation-vocabulary | (direction: STRING) -> void | Rotate agent body/view orientation. direction is typically left, right, or angle. | aliases: rotate, turn_around  ⟵ related to then
- walk | operation | operation-vocabulary | (destination: STRING / TERM / ATOM[object_label], relation?: STRING) -> void | Locomote towards a target destination or landmark. destination must identify a valid entity or location. | aliases: move_to, go_to, navigate_to  ⟵ related to then

### speech acts

- acknowledge | speech_act | operation-vocabulary | UTTER acknowledge(target: CLAIM / TERM) | Acknowledge receipt/awareness; does not imply agreement.  ⟵ candidate
- ask | speech_act | operation-vocabulary | UTTER ask(target: TERM, or a sufficiently precise topic: STRING / TERM) | Request information/advice; not an assertion of an answer. | aliases: ask, how should  ⟵ candidate
- confirm | speech_act | operation-vocabulary | UTTER confirm(target: CLAIM) | Confirm the proposition; its evidence/status remains explicit.  ⟵ candidate
- correct | speech_act | operation-vocabulary | UTTER correct(target: CLAIM) | Offer corrected content. Actual supersession requires the Conversation revision rules.  ⟵ candidate
- decline | speech_act | operation-vocabulary | UTTER decline(target: TERM) | Decline the represented request/proposal; not negate every proposition within it.  ⟵ candidate
- express_interest | speech_act | operation-vocabulary | UTTER express_interest(target: STRING / TERM) | Speech act expressing conversational interest or engagement in a topic. speech act in dialogic traces. | aliases: show_interest  ⟵ candidate
- inform | speech_act | operation-vocabulary | UTTER inform(target: CLAIM) | Present the proposition; preserve its holder/status.  ⟵ candidate
- propose | speech_act | operation-vocabulary | UTTER propose(target: TERM) | Suggest an action/idea; does not record it as performed.  ⟵ candidate
- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ dependency of event_sadie_adler_unmasking
- character_trait | constructor | TERM character_trait(property: STRING, value: STRING / NUMBER) -> TERM | A character attribute | not: Not a claim about a real person  ⟵ candidate
- conjunction | constructor | TERM conjunction(items: LIST[TERM]) -> TERM | All described components apply | not: Does not imply temporal order  ⟵ candidate
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ candidate
- group_size | constructor | TERM group_size(count: NUMBER, group?: STRING / TERM) -> TERM | The headcount or number of members in a specified group or party; count is a nonnegative integer. | not: minimum_per_period (a per-period minimum bound) or measure (measured quantities with units) | aliases: party_size, party of, number of guests, guest_count  ⟵ candidate
- include | constructor | TERM include(item: STRING / TERM) -> TERM | Require the identified content/item | not: Not permission to invent an instance in a recorded trace  ⟵ dependency of constraint_include_character_attribute_list
- negation | constructor | TERM negation(target: TERM) -> TERM | Constructs a descriptive semantic negation of a target descriptive proposition or condition term. | not: Check's runtime Boolean operator NOT or a speech-act decline | aliases: not, does not, negation, absence of  ⟵ candidate
- outshines | constructor | TERM outshines(brighter: STRING / TERM, dimmer: STRING / TERM) -> TERM | Constructs a description of relative visual brightness where a brighter light source overpowers the perceived brightness of a dimmer object. | not: an absolute numeric brightness measurement | aliases: outshines, overpowers brightness, drowns out light  ⟵ candidate
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ dependency of constraint_respectful
- sequence | constructor | TERM sequence(items: LIST[TERM]) -> TERM | Ordered described activities/content | not: Not unordered conjunction  ⟵ dependency of event_sadie_adler_unmasking
- similarity | constructor | TERM similarity(target: STRING / TERM, dimension?: STRING / TERM) -> TERM | Constructs a descriptor representing comparative closeness or similarity to a target along a given dimension. | not: spatial proximity (use rank_distance or next_to) or an assertion of exact identity (use identity) | aliases: closest_to, similar_to, resembles  ⟵ candidate
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ candidate
- test_condition | constructor | TERM test_condition(condition: STRING, expected: BOOL) -> TERM | A testable condition with the expected Boolean outcome | not: Expected outcome is not an observed result  ⟵ candidate
- weather_condition | constructor | TERM weather_condition(condition: STRING, location?: STRING / TERM / ATOM[country], severity?: STRING) -> TERM | A structured descriptor of atmospheric or weather phenomena such as wind, rain, or storm at an optional location; asserts nothing. | not: state_cold or state_warm (thermal states of physical objects) or occurred (past factual occurrence assertion) | aliases: weather, storm_condition, atmospheric_condition  ⟵ candidate
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
- event_sadie_adler_unmasking | composite | event-value | TERM event_sadie_adler_unmasking() -> TERM | Sadie Adler taking off her hat and peeling skin. | = sequence(items=[activity(verb="remove", actor="Sadie Adler", object="hat"), activity(verb="peel", actor="Sadie Adler", object="skin")])  ⟵ candidate
- topic_greatest_cricketer_of_all_time | composite | topic-value | TERM topic_greatest_cricketer_of_all_time() -> TERM | Greatest cricketer of all time. | = subject(kind="cricketer", qualifier=requirement(property="rank_by_greatness", value=1), time="all_time")  ⟵ candidate
- topic_profanity | composite | topic-value | TERM topic_profanity() -> TERM | A composite term representing the topic of profanity. | = subject(kind="profanity") | not: potential_harms (which is generic) | aliases: profanity  ⟵ candidate

### claim relations

- attribute_claim | claim_relation | CLAIM attribute_claim(subject: STRING / TERM / ATOM[platform_label], property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) | Asserts that a subject possesses a named property evaluated to a specific primitive or structured value. general property attribution claim. | aliases: property_value, word_property, has_property, property attribution  ⟵ related to statement
- comfortable | claim_relation | CLAIM comfortable(person: TERM, value: BOOL) | Asserts whether a person or animal is comfortable in a situation. affective/state claim. | aliases: is_comfortable  ⟵ candidate
- controversial | claim_relation | CLAIM controversial(subject: STRING / TERM) | Asserts that a topic, policy, or practice is the subject of public debate or controversy. evaluative debate claim. | aliases: debated, disputed  ⟵ candidate
- enables | claim_relation | CLAIM enables(condition: TERM / CLAIM, outcome: TERM / CLAIM) | Asserts that an enabling condition or capability facilitates an outcome. enabling condition. | aliases: facilitates, allows  ⟵ candidate
- example_of | claim_relation | CLAIM example_of(example: TERM, concept: TERM) | Asserts that an instance or term exemplifies a general concept, pattern, or category. example and concept are descriptive terms. | aliases: exemplifies, instance_of  ⟵ candidate
- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ candidate
- has_attribute | claim_relation | CLAIM has_attribute(subject: STRING / TERM, attribute: STRING / TERM) | Asserts that an entity, group, or person possesses a stated characteristic or attribute. general characteristic attribution. | aliases: possesses_attribute  ⟵ candidate
- has_state | claim_relation | CLAIM has_state(subject: TERM, state: STRING) | Asserts that an entity is currently in a physical, thermal, or operational state. state must be a valid state descriptor string. | aliases: in_state, state_is  ⟵ related to statement
- important | claim_relation | CLAIM important(target: TERM) | Asserts that a concept, activity, or condition is important or significant. evaluative importance claim. | aliases: significant  ⟵ candidate
- leads_to | claim_relation | CLAIM leads_to(cause: TERM, effect: TERM) | Asserts a conceptual consequence or progression from cause to effect. progression relation. | aliases: results_in  ⟵ candidate
- motivated_by | claim_relation | CLAIM motivated_by(claim: CLAIM, motive: STRING / TERM) | Asserts that an action, rule, or claim is motivated by an underlying motive or goal. motive explanation. | aliases: rationale_is  ⟵ candidate
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ candidate
- reason_for | claim_relation | CLAIM reason_for(subject: CLAIM / TERM, reason: STRING / TERM) | Asserts an explanatory reason for a policy, belief, or state of affairs. explanatory reason. | aliases: basis_for  ⟵ candidate
- recommended | claim_relation | CLAIM recommended(target: TERM / CLAIM) | Asserts an advisory recommendation that an activity or measure is advisable. advisory normative claim. | aliases: advisable  ⟵ candidate
- spatial_state | claim_relation | CLAIM spatial_state(relation: STRING, object: TERM, reference: TERM) | Asserts an observed spatial configuration between an object and a reference landmark. relation must specify spatial configuration. | aliases: placed_at, located_at  ⟵ related to statement
- statement | claim_relation | CLAIM statement(fact: TERM) | Foundational claim relation converting any descriptive TERM into an attributed, truth-evaluated assertion. universal fact assertion. | aliases: assert_fact, fact_claim, claim_statement  ⟵ candidate
- stereotype | claim_relation | CLAIM stereotype(target: STRING / TERM, trait: STRING / TERM) | Asserts that an attributed trait, generalization, or assumption about a demographic group or social category is a stereotype. | not: an individual character trait or verified fact | aliases: social_stereotype, generalization, bias  ⟵ candidate
- unaware | claim_relation | CLAIM unaware(person: STRING / TERM, topic: STRING / TERM) | Asserts epistemic lack of awareness regarding a topic, fact, or event. epistemic state. | aliases: ignorant_of  ⟵ candidate

### links

- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ candidate
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ core
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ candidate
- then | link | LINK then(previous: EVENT, next: EVENT) | Represents temporal sequence and succession between two events where next follows previous. previous and next must be event terms. | aliases: followed_by, after_which  ⟵ candidate

### values

- path_ipython_core_magics_basic_py | value | code-value | File path to the IPython basic magics module. | not: an individual command line script or general config file | aliases: IPython/core/magics/basic.py, ipython_core_magics_basic_py  ⟵ candidate
- constraint_17_plus | value | constraint-value | Rated 17+ or mature.  ⟵ candidate
- bowtie | value | entity-name | Item or prop in joke/creative context: bowtie. | aliases: bowtie  ⟵ candidate
- cinnamon | value | entity-name | Ground or whole cinnamon culinary spice from Cinnamomum tree bark. | not: nutmeg, cloves, or other distinct spice varieties | aliases: cinnamon, ground cinnamon, cinnamon spice, cinnamon stick  ⟵ candidate
- entity_flowers | value | entity-name | Flowers, blossoms, or floral design elements. | not: constraint_exclude_flowery_language (a prose style constraint) or agricultural food items | aliases: flowers, floral, flower, floral decorations  ⟵ candidate
- ginger | value | entity-name | Pungent aromatic spice root from Zingiber officinale used in cooking and baking. | not: cinnamon, cardamom, or other distinct spice varieties | aliases: ginger, ground ginger, fresh ginger, ginger root  ⟵ candidate
- grape_tannin | value | entity-name | Tannin powder derived from grapes for wine structure. | not: oak_chips or wood aging additives | aliases: grape tannin, tannin, wine tannin  ⟵ candidate
- grape_thompson_seedless | value | entity-name | Thompson Seedless grape variety. | not: wine grape cultivars like grape_merlot or grape_chardonnay | aliases: Thompson Seedless, thompson seedless grape, sultana grape  ⟵ candidate
- mittens | value | entity-name | Item or prop in joke/creative context: mittens. | aliases: mittens  ⟵ candidate
- pear | value | entity-name | A pear fruit item, typically an ingredient or fresh fruit object. | not: apple, food_label::tomato, or other distinct fruit items | aliases: pear, pears, fresh pear, sliced pear  ⟵ candidate
- spatula | value | entity-name | A kitchen utensil with a broad, flat, and flexible blade used for lifting, flipping, or spreading food. | not: knife (cutting utensil) or spoon (scooping utensil) | aliases: spatula, turner, flipper  ⟵ candidate
- yarn | value | entity-name | Item or prop in joke/creative context: yarn. | aliases: yarn  ⟵ candidate
- united_kingdom | value | location-name | Geopolitical nation or sovereign state: United Kingdom (Great Britain). | not: locale_en_gb (a language/locale code, not a location) | aliases: United Kingdom, UK, Great Britain, Britain  ⟵ candidate
- metric_order_late | value | metric-value | Whether an order is late. | aliases: order is late, delayed  ⟵ candidate
- color_pink | value | product-attribute-value | Pink visual color qualifier. | not: color_label::red, color_label::purple, or other distinct color shades | aliases: pink, color_pink, blush pink, rose pink, pastel pink  ⟵ candidate
- size_large | value | product-attribute-value | Large size. | aliases: large, L  ⟵ candidate
- size_queen | value | product-attribute-value | Queen-size dimension classification for beds, mattresses, and bedding. | not: size_large (generic large apparel/goods size) or size_king | aliases: queen, queen size, Queen  ⟵ candidate
- size_small | value | product-attribute-value | Small size. | aliases: small, S  ⟵ candidate
- size_tall | value | product-attribute-value | Tall relative vertical dimension qualifier. | aliases: size_tall  ⟵ candidate
- foreigners | value | recipient-value | Social, demographic, or institutional group: foreigners. | aliases: foreigners  ⟵ candidate
- role_kids | value | recipient-value | Children/kids participant group in event context. | aliases: kids, children  ⟵ candidate
- role_mother | value | recipient-value | The mother of the user. | not: role_sister or role_kids | aliases: my mom, mother, mom  ⟵ candidate
- role_professor | value | recipient-value | The user's professor/instructor. | aliases: my professor, teacher  ⟵ candidate
- role_sister | value | recipient-value | Sister participant role in family/event context. | aliases: sister  ⟵ candidate
- right_of | value | spatial-relation | To the right of. | aliases: right of  ⟵ candidate
- state_cold | value | state-value | Cold or chilled condition. | aliases: cold, chilled  ⟵ candidate
- state_dirty | value | state-value | Dirty condition. | aliases: dirty  ⟵ candidate
- style_catchy | value | style-value | Catchy, attention-grabbing style. | aliases: catchy  ⟵ candidate
- style_persuasive | value | style-value | Persuasive/argumentative style. | aliases: persuasive  ⟵ candidate
- tone_empathetic | value | tone-value | Conveys empathy/understanding. | aliases: sympathetically  ⟵ candidate
- tone_polite | value | tone-value | Courteous, respectful register. | aliases: politely, kindly  ⟵ candidate
- tone_silly | value | tone-value | Playful, lighthearted, or silly conversational tone. | aliases: silly  ⟵ candidate
- topic_baldurs_gate_3 | value | topic-value | Baldur's Gate 3.  ⟵ candidate
- topic_politics | value | topic-value | Politics.  ⟵ candidate
