# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 34 needs (decomposition: llm), 160 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | speech_act | t1:s1 | Introduce a set of theoretical rules and facts | `rule_speech_acts_general`, `subject`, `respond`, `rule_structural_constructs`, `constraint_realistic`, `propose`, `inform`, `topic_baldurs_gate_3`, `ask`, `rule_trace_relations_general`, `rule_category_constraint_value`, `express_interest` |
| n2 | object | t1:s2 | Anne | `right_of`, `on`, `role_mother`, `next_to`, `art_plan`, `art_story`, `in_front_of`, `left_of`, `resource_sink`, `resource_heater`, `role_daughter`, `resource_chiller` |
| n3 | object | t1:s2 | blue → `color_label::<key>` | `color_label`*, `chill`, `right_of`, `sultana`, `dried_fruit`, `grape_merlot`, `on`, `yakuza`, `lettuce`, `fridge`, `resource_sink`, `grape_sauvignon_blanc` |
| n4 | claim | t1:s2 | Anne is blue | `color_label`, `color_pink`, `enables`, `leads_to`, `occurred_recently`, `recommended`, `outcome`, `sun`, `moon`, `apple`, `sultana`, `role_sister` |
| n5 | object | t1:s3 | red → `color_label::<key>` | `color_label`*, `color_pink`, `apple`, `right_of`, `pear`, `grape_merlot`, `grape_pinot_noir`, `topic_current_events`, `ginger`, `locale_en_us`, `gift`, `resource_sink` |
| n6 | claim | t1:s3 | Anne is red | `color_pink`, `enables`, `event_sadie_adler_unmasking`, `gender_unisex`, `apple`, `leads_to`, `char_female`, `occurred_recently`, `outcome`, `color_label`, `art_story`, `recommended` |
| n7 | claim | t1:s4 | Anne is young | `topic_profanity`, `constraint_17_plus`, `enables`, `occurred_recently`, `leads_to`, `art_short_text`, `rule_support_primitives_general`, `recommended`, `outcome`, `role_daughter`, `role_sister`, `important` |
| n8 | object | t1:s5 | Bob | `resource_sink`, `bread`, `in_front_of`, `right_of`, `role_professor`, `behind`, `left_of`, `on`, `topic_spider_man_2`, `bowtie`, `between`, `resource_heater` |
| n9 | claim | t1:s5 | Bob is nice | `enables`, `style_catchy`, `condition_perfect`, `tone_silly`, `tone_polite`, `leads_to`, `occurred_recently`, `recommended`, `outcome`, `important`, `role_professor`, `in_front_of` |
| n10 | claim | t1:s6 | Bob is young | `topic_profanity`, `constraint_17_plus`, `leads_to`, `enables`, `occurred_recently`, `rule_support_primitives_general`, `outcome`, `role_kids`, `size_small`, `recommended`, `motivated_by`, `role_professor` |
| n11 | object | t1:s7 | Charlie | `art_character_profile`, `dog`, `art_story`, `on`, `art_plan`, `event_sadie_adler_unmasking`, `in_front_of`, `right_of`, `resource_heater`, `resource_chiller`, `resource_sink`, `art_itinerary` |
| n12 | claim | t1:s7 | Charlie is nice | `comfortable`, `condition_perfect`, `art_character_profile`, `enables`, `leads_to`, `important`, `recommended`, `occurred_recently`, `style_catchy`, `tone_polite`, `motivated_by`, `tone_silly` |
| n13 | claim | t1:s8 | Charlie is quiet | `comfortable`, `unaware`, `event_sadie_adler_unmasking`, `leads_to`, `occurred_recently`, `enables`, `outcome`, `recommended`, `motivated_by`, `important`, `grape_thompson_seedless`, `occurred` |
| n14 | claim | t1:s9 | Charlie is red | `enables`, `event_sadie_adler_unmasking`, `art_character_profile`, `leads_to`, `dog`, `occurred_recently`, `char_female`, `outcome`, `char_2000s_anime_style`, `art_story`, `important`, `recommended` |
| n15 | object | t1:s10 | white → `color_label::<key>` | `color_label`*, `sultana`, `unit_word`, `art_short_text`, `dulce_de_leche`, `dulce_de_nata`, `gender_unisex`, `on`, `raisin`, `resource_sink`, `state_clean`, `under` |
| n16 | claim | t1:s10 | Charlie is white | `char_female`, `art_character_profile`, `enables`, `leads_to`, `occurred_recently`, `outcome`, `dog`, `dulce_de_leche`, `recommended`, `motivated_by`, `important`, `dulce_de_nata` |
| n17 | claim | t1:s11 | Charlie is young | `constraint_17_plus`, `leads_to`, `enables`, `art_character_profile`, `occurred_recently`, `size_small`, `topic_profanity`, `outcome`, `recommended`, `rule_support_primitives_general`, `motivated_by`, `important` |
| n18 | object | t1:s12 | Gary | `chill`, `right_of`, `in_front_of`, `on`, `left_of`, `next_to`, `topic_baldurs_gate_3`, `topic_politics`, `resource_sink`, `state_dirty`, `resource_chiller`, `subject` |
| n19 | object | t1:s12 | green → `color_label::<key>` | `color_label`*, `apple`, `lettuce`, `right_of`, `left_of`, `grape_thompson_seedless`, `sultana`, `outshines`, `shape_square`, `resource_sink`, `unit_day`, `locale_en_gb` |
| n20 | claim | t1:s12 | Gary is green | `lettuce`, `enables`, `color_label`, `leads_to`, `color_pink`, `right_of`, `left_of`, `outshines`, `on`, `outcome`, `occurred_recently`, `important` |
| n21 | claim | t1:s13 | If something is red and blue then it is white | `color_label`, `color_pink`, `enables`, `in_front_of`, `leads_to`, `dried_fruit`, `outcome`, `occurred_recently`, `apple`, `outshines`, `motivated_by`, `left_of` |
| n22 | claim | t1:s14 | Green things are red | `apple`, `lettuce`, `color_label`, `color_pink`, `enables`, `grape_thompson_seedless`, `leads_to`, `dried_fruit`, `important`, `occurred_recently`, `outcome`, `recommended` |
| n23 | claim | t1:s15 | If something is white then it is quiet | `outshines`, `unaware`, `enables`, `occurred_recently`, `tone_neutral`, `leads_to`, `unit_word`, `reflects_light`, `outcome`, `in_front_of`, `color_label`, `state_clean` |
| n24 | claim | t1:s16 | If something is red then it is blue | `color_label`, `color_pink`, `enables`, `leads_to`, `dried_fruit`, `occurred_recently`, `apple`, `outcome`, `motivated_by`, `grape_thompson_seedless`, `recommended`, `right_of` |
| n25 | claim | t1:s17 | All blue, young things are white | `color_label`, `color_pink`, `enables`, `leads_to`, `sultana`, `occurred_recently`, `outcome`, `grape_thompson_seedless`, `dried_fruit`, `under`, `grape_merlot`, `recommended` |
| n26 | claim | t1:s18 | If Bob is quiet and Bob is green then Bob is young | `in_front_of`, `constraint_17_plus`, `tone_silly`, `enables`, `leads_to`, `occurred_recently`, `behind`, `rule_support_primitives_general`, `style_catchy`, `outcome`, `topic_profanity`, `then`* |
| n27 | claim | t1:s19 | Quiet, green things are young | `lettuce`, `grape_thompson_seedless`, `tone_silly`, `leads_to`, `occurred_recently`, `topic_profanity`, `size_small`, `enables`, `under`, `in_front_of`, `constraint_17_plus`, `important` |
| n28 | claim | t1:s20 | Red, nice things are white | `color_pink`, `enables`, `color_label`, `art_short_text`, `leads_to`, `dulce_de_nata`, `important`, `outcome`, `occurred_recently`, `dried_fruit`, `recommended`, `sultana` |
| n29 | claim | t1:s21 | All white, nice things are quiet | `enables`, `tone_polite`, `condition_perfect`, `occurred_recently`, `tone_neutral`, `leads_to`, `outcome`, `color_pink`, `unit_word`, `recommended`, `art_short_text`, `state_clean` |
| n30 | action | t1:s22 | Determine if a statement is True, False, or Unknown | `statement`*, `run_tests`, `assert_multinomial_scorer`, `motivated_by`, `occurred`, `test_condition`, `conditional`, `distinguish`, `failure`, `unaware`, `validates_parameter`, `check_reservation_availability` |
| n31 | constraint | t1:s22 | Base the evaluation only on the provided theory | `extract`, `subject`, `test_condition`, `decision`, `constraint_respectful`, `constraint_exclude_flowery_language`, `constraint_realistic`, `supports`, `constraint_budget_limited`, `regression_case`, `constraint_beginner`, `considered` |
| n32 | constraint | t1:s22 | Output must be True, False, or Unknown | `constraint_realistic`, `test_condition`, `assert_multinomial_scorer`, `constraint_exclude_flowery_language`, `constraint_respectful`, `failure`, `conditional`, `constraint_budget_limited`, `unaware`, `entity_flowers`, `constraint_comprehensive`, `decision` |
| n33 | claim | t1:s23 | Bob is not quiet | `comfortable`, `in_front_of`, `unaware`, `enables`, `behind`, `occurred_recently`, `leads_to`, `on`, `tone_silly`, `outcome`, `tone_empathetic`, `motivated_by` |
| n34 | negation | t1:s23 | Bob is not quiet | `negation`, `in_front_of`, `behind`, `on`, `tone_silly`, `unaware`, `constraint_exclude_flowery_language`, `correct`, `tone_empathetic`, `decline`, `ask`, `tone_polite` |

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
- run_tests.target → platform_label
- failure.system → platform_label
- check_reservation_availability.currency → currency
- check_reservation_availability.location → country
- regression_case.framework → platform_label
- requirement.value → platform_label
- activity.object → object_label, food_label, animal_label
- activity.location → country
- activity.instrument → object_label, platform_label
- walk.destination → object_label
- attribute_claim.subject → platform_label
- attribute_claim.value → platform_label

## Retrieved records

### Shared rules that govern the records below (full text)

**rule_lexical_groups** (v19/rule/lexical-groups; rule governing platform_label)

Section 3.1 defines value groups: `group::key` values of type ATOM[group]. Open groups admit any key of their form (examples are not whitelists); standard groups admit the codes of their bundled standard (ISO 3166-1 alpha-2 for country, ISO 4217 for currency). Leaf values are never glossary entries. Consumer signatures alone decide where a group may appear. Retired bare symbols are invalid.

**rule_reading_guide** (v19/rule/reading-guide; core)

The spec governs syntax/types; this glossary defines vocabulary. Signature notation: ? optional, A / B explicit alternatives, void no result. Omitted optional arguments are unspecified. Value entries are category-refined STRING primitives; complex meanings require composition. Aliases are contextual hints, not unconditional equivalences. Report ambiguity. IDs use v19/<category>/<symbol>, v19/support/<symbol> or v19/composite/<symbol>. Statuses apply to this candidate: Retained preserves meaning; Adapted uses the stated contract; Composite requires TERM (bare STRING deprecated); Structural is syntax/argument vocabulary; Needs clarification is unusable until resolved; Deprecated is historical; Accepted is usable within this candidate.

**rule_recording_signatures** (v19/rule/recording-signatures; rule governing chill)

RECORD ACTION uses the operation signature with REF[STRING] → TERM and LIST[REF[STRING]] → LIST[TERM]; other types/categories stay unchanged. Return EVENT, never the runtime result. Record actual outputs as attributed CLAIMs. Do not infer missing resources.

**rule_speech_acts_general** (v19/rule/speech-acts-general; candidate)

UTTER-only, void, with the spec's speech attributes and LIST[TERM] constraints. No result binding. Literal content cannot replace required semantic arguments for structured coverage.

**rule_structural_constructs** (v19/rule/structural-constructs; candidate)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; candidate)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_attributes_and_generate** (v19/rule/attributes-and-generate; rule governing art_plan)

Attribute entries name arguments; legality/types come from each operation, not global membership. GENERATE uses the spec's core fields; retained artifact profiles return STRING. Numeric/list results need explicit profiles. Legacy itinerary fields expand to TERM constraints: duration/duration_unit → duration(amount,unit); stop_min_per_day/stop_requirement → minimum_per_period(class,count,period=unit_day), never an inferred temple class; max_walk_duration/unit → maximum_between_stops(activity="walk",amount,unit). No legacy shorthand is enabled. Old events/character_properties/transformations become explicitly scoped TERM constraints. Message purpose is TERM, not send_email.content: GENERATE exact STRING content, then send. Report opaque fallback separately.

**rule_category_artifact_value** (v19/rule/category/artifact-value; rule governing art_plan)

STRING artifact class for GENERATE.target. art_story says what kind of artifact to produce, not what occurs in its plot.

**rule_category_character_property_value** (v19/rule/category/character-property-value; rule governing char_female)

TERM-described trait/style. Use constraints and explicit inclusion/scope; do not use an ungoverned character_properties attribute.

**rule_category_code_value** (v19/rule/category/code-value; rule governing assert_multinomial_scorer)

path_/sym_ remain STRING identities; migrated chg_/assert_ are TERM constructors. Do not recover an exact file path by guessing from underscores.

**rule_category_constraint_value** (v19/rule/category/constraint-value; candidate)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_descriptive_value** (v19/rule/category/descriptive-value; rule governing yakuza)

STRING modifier/domain label; never a free-form proposition. dom_sgi needs its intended referent established before semantically dependent use.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; rule governing unit_word)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing resource_sink)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_event_value** (v19/rule/category/event-value; rule governing event_sadie_adler_unmasking)

TERM-described narrative event, not a recorded EVENT. Require inclusion explicitly when generating a story.

**rule_category_locale_value** (v19/rule/category/locale-value; rule governing locale_en_us)

STRING locale. “English” alone does not always mean locale_en_us; preserve ambiguity.

**rule_category_product_attribute_value** (v19/rule/category/product-attribute-value; rule governing color_pink)

STRING color/size/product-market facets. gender_women describes a product category, not an assertion about a person's gender.

**rule_category_recipient_value** (v19/rule/category/recipient-value; rule governing role_mother)

STRING roles or explicit named recipients. A role is not an exact person's identity. Keep an explicit name where substituting a role loses information.

**rule_category_shape_value** (v19/rule/category/shape-value; rule governing shape_square)

STRING geometry. shape_round may select a circular object; it does not imply color or dimensions.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing right_of)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_state_value** (v19/rule/category/state-value; rule governing state_clean)

STRING condition used in selection. state_warm does not command heat; “hot” is not automatically synonymous with “warm.”

**rule_category_style_value** (v19/rule/category/style-value; rule governing style_catchy)

STRING production style. style_narrative does not establish that described events occurred.

**rule_category_tone_value** (v19/rule/category/tone-value; rule governing tone_silly)

STRING register. tone_urgent describes urgency, not a concrete deadline.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_baldurs_gate_3)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_composites_general** (v19/rule/composites-general; rule governing constraint_realistic)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_operations_general** (v19/rule/operations-general; rule governing chill)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_supplemental_general** (v19/rule/supplemental-general; rule governing art_itinerary)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; candidate)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- check_reservation_availability | operation | operation-vocabulary | (target: STRING, cuisine?: STRING, currency?: STRING / ATOM[currency], location?: STRING / ATOM[country], max_price?: NUMBER) -> BOOL | Check current availability under supplied filters. A positive result does not make a reservation. | aliases: check reservation availability  ⟵ candidate
- chill | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Chill using the stated resource; same identity.  ⟵ candidate
- extract | operation | operation-vocabulary | (target: LIST[REF[STRING]], limit: NUMBER) -> LIST[REF[STRING]] | First limit results, preserving order and identity; limit is a nonnegative integer; limit=1 is still a list  ⟵ candidate
- run_tests | operation | operation-vocabulary | (target: STRING / ATOM[platform_label], assertion?: TERM) -> BOOL | Run the selected project's tests, optionally checking the specified assertion. TRUE means the declared test condition passed, not overall software correctness.  ⟵ candidate
- turn | operation | operation-vocabulary | (direction: STRING) -> void | Rotate agent body/view orientation. direction is typically left, right, or angle. | aliases: rotate, turn_around  ⟵ related to then
- walk | operation | operation-vocabulary | (destination: STRING / TERM / ATOM[object_label], relation?: STRING) -> void | Locomote towards a target destination or landmark. destination must identify a valid entity or location. | aliases: move_to, go_to, navigate_to  ⟵ related to then

### speech acts

- ask | speech_act | operation-vocabulary | UTTER ask(target: TERM, or a sufficiently precise topic: STRING / TERM) | Request information/advice; not an assertion of an answer. | aliases: ask, how should  ⟵ candidate
- correct | speech_act | operation-vocabulary | UTTER correct(target: CLAIM) | Offer corrected content. Actual supersession requires the Conversation revision rules.  ⟵ candidate
- decline | speech_act | operation-vocabulary | UTTER decline(target: TERM) | Decline the represented request/proposal; not negate every proposition within it.  ⟵ candidate
- express_interest | speech_act | operation-vocabulary | UTTER express_interest(target: STRING / TERM) | Speech act expressing conversational interest or engagement in a topic. speech act in dialogic traces. | aliases: show_interest  ⟵ candidate
- inform | speech_act | operation-vocabulary | UTTER inform(target: CLAIM) | Present the proposition; preserve its holder/status.  ⟵ candidate
- propose | speech_act | operation-vocabulary | UTTER propose(target: TERM) | Suggest an action/idea; does not record it as performed.  ⟵ candidate
- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ dependency of event_sadie_adler_unmasking
- aesthetic | constructor | TERM aesthetic(period: STRING, style: STRING) -> TERM | A stylistic description with an explicit period | not: Not a character's age or production date  ⟵ dependency of char_2000s_anime_style
- character_trait | constructor | TERM character_trait(property: STRING, value: STRING / NUMBER) -> TERM | A character attribute | not: Not a claim about a real person  ⟵ dependency of char_female
- conditional | constructor | TERM conditional(condition: TERM, consequence: TERM) -> TERM | Constructs a structured conditional proposition term connecting a condition and consequence. descriptive logic structure. | aliases: if_then  ⟵ candidate
- decision | constructor | TERM decision(activity: TERM) -> TERM | A decision whose content is the described activity | not: Not proof it was carried out  ⟵ candidate
- distinguish | constructor | TERM distinguish(first: TERM, second: TERM, criterion?: STRING / TERM) -> TERM | Constructs a descriptive representation of discerning or differentiating between two entities, conditions, or behaviors along an optional criterion. | not: visual_contrast (optical contrast) or LINK contrast (rhetorical opposition between claims) | aliases: tell the difference, differentiate, distinguish between  ⟵ candidate
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ dependency of constraint_exclude_flowery_language
- negation | constructor | TERM negation(target: TERM) -> TERM | Constructs a descriptive semantic negation of a target descriptive proposition or condition term. | not: Check's runtime Boolean operator NOT or a speech-act decline | aliases: not, does not, negation, absence of  ⟵ candidate
- outshines | constructor | TERM outshines(brighter: STRING / TERM, dimmer: STRING / TERM) -> TERM | Constructs a description of relative visual brightness where a brighter light source overpowers the perceived brightness of a dimmer object. | not: an absolute numeric brightness measurement | aliases: outshines, overpowers brightness, drowns out light  ⟵ candidate
- reflects_light | constructor | TERM reflects_light(target: STRING / TERM, source: STRING / TERM) -> TERM | Constructs a description of an optical reflection where a target surface or body reflects light emanating from a light source. | not: intrinsic light emission (use emits_light) | aliases: reflects, reflection of light, reflects sunlight  ⟵ candidate
- regression_case | constructor | TERM regression_case(framework: STRING / ATOM[platform_label], modifier: STRING, relation: STRING) -> TERM | A regression scenario specifying affected framework, condition and relation | not: Does not invent a passing test or exact implementation  ⟵ candidate
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ dependency of constraint_realistic
- sequence | constructor | TERM sequence(items: LIST[TERM]) -> TERM | Ordered described activities/content | not: Not unordered conjunction  ⟵ dependency of event_sadie_adler_unmasking
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ candidate
- test_condition | constructor | TERM test_condition(condition: STRING, expected: BOOL) -> TERM | A testable condition with the expected Boolean outcome | not: Expected outcome is not an observed result  ⟵ candidate

### composites

- char_2000s_anime_style | composite | character-property-value | TERM char_2000s_anime_style() -> TERM | 2000s anime style. | = aesthetic(period="2000s", style="anime")  ⟵ candidate
- char_female | composite | character-property-value | TERM char_female() -> TERM | Female gender. | = character_trait(property="gender", value="female") | aliases: female  ⟵ candidate
- assert_multinomial_scorer | composite | code-value | TERM assert_multinomial_scorer() -> TERM | Assertion that multinomial probabilistic scoring succeeds. | = test_condition(condition="multinomial_probabilistic_scoring", expected=TRUE)  ⟵ candidate
- constraint_beginner | composite | constraint-value | TERM constraint_beginner() -> TERM | Targeted at beginners. | = requirement(property="audience_expertise", value="beginner")  ⟵ candidate
- constraint_budget_limited | composite | constraint-value | TERM constraint_budget_limited() -> TERM | Limited budget. | = requirement(property="budget_limited", value=TRUE)  ⟵ candidate
- constraint_comprehensive | composite | constraint-value | TERM constraint_comprehensive() -> TERM | Must be comprehensive. | = requirement(property="comprehensive", value=TRUE)  ⟵ candidate
- constraint_exclude_flowery_language | composite | constraint-value | TERM constraint_exclude_flowery_language() -> TERM | Avoid flowery language. | = exclude(item="flowery_language")  ⟵ candidate
- constraint_realistic | composite | constraint-value | TERM constraint_realistic() -> TERM | Must be realistic. | = requirement(property="realistic", value=TRUE)  ⟵ candidate
- constraint_respectful | composite | constraint-value | TERM constraint_respectful() -> TERM | Must be respectful. | = requirement(property="respectful", value=TRUE)  ⟵ candidate
- event_sadie_adler_unmasking | composite | event-value | TERM event_sadie_adler_unmasking() -> TERM | Sadie Adler taking off her hat and peeling skin. | = sequence(items=[activity(verb="remove", actor="Sadie Adler", object="hat"), activity(verb="peel", actor="Sadie Adler", object="skin")])  ⟵ candidate
- topic_profanity | composite | topic-value | TERM topic_profanity() -> TERM | A composite term representing the topic of profanity. | = subject(kind="profanity") | not: potential_harms (which is generic) | aliases: profanity  ⟵ candidate

### claim relations

- attribute_claim | claim_relation | CLAIM attribute_claim(subject: STRING / TERM / ATOM[platform_label], property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) | Asserts that a subject possesses a named property evaluated to a specific primitive or structured value. general property attribution claim. | aliases: property_value, word_property, has_property, property attribution  ⟵ related to statement
- comfortable | claim_relation | CLAIM comfortable(person: TERM, value: BOOL) | Asserts whether a person or animal is comfortable in a situation. affective/state claim. | aliases: is_comfortable  ⟵ candidate
- considered | claim_relation | CLAIM considered(subject: TERM) | Asserts that an agent or speaker evaluated or entertained a specific candidate term or concept. subject is the evaluated term. | aliases: evaluated, weighed  ⟵ candidate
- enables | claim_relation | CLAIM enables(condition: TERM / CLAIM, outcome: TERM / CLAIM) | Asserts that an enabling condition or capability facilitates an outcome. enabling condition. | aliases: facilitates, allows  ⟵ candidate
- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ candidate
- has_state | claim_relation | CLAIM has_state(subject: TERM, state: STRING) | Asserts that an entity is currently in a physical, thermal, or operational state. state must be a valid state descriptor string. | aliases: in_state, state_is  ⟵ related to statement
- important | claim_relation | CLAIM important(target: TERM) | Asserts that a concept, activity, or condition is important or significant. evaluative importance claim. | aliases: significant  ⟵ candidate
- leads_to | claim_relation | CLAIM leads_to(cause: TERM, effect: TERM) | Asserts a conceptual consequence or progression from cause to effect. progression relation. | aliases: results_in  ⟵ candidate
- motivated_by | claim_relation | CLAIM motivated_by(claim: CLAIM, motive: STRING / TERM) | Asserts that an action, rule, or claim is motivated by an underlying motive or goal. motive explanation. | aliases: rationale_is  ⟵ candidate
- occurred | claim_relation | CLAIM occurred(activity: TERM) | Asserts that an event, action, or activity took place in the past. past occurrence claim. | aliases: happened  ⟵ candidate
- occurred_recently | claim_relation | CLAIM occurred_recently(target: CLAIM) | Asserts temporal recency of an asserted occurrence or claim. temporal recency qualifier. | aliases: recently_happened  ⟵ candidate
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ candidate
- recommended | claim_relation | CLAIM recommended(target: TERM / CLAIM) | Asserts an advisory recommendation that an activity or measure is advisable. advisory normative claim. | aliases: advisable  ⟵ candidate
- spatial_state | claim_relation | CLAIM spatial_state(relation: STRING, object: TERM, reference: TERM) | Asserts an observed spatial configuration between an object and a reference landmark. relation must specify spatial configuration. | aliases: placed_at, located_at  ⟵ related to statement
- statement | claim_relation | CLAIM statement(fact: TERM) | Foundational claim relation converting any descriptive TERM into an attributed, truth-evaluated assertion. universal fact assertion. | aliases: assert_fact, fact_claim, claim_statement  ⟵ candidate
- unaware | claim_relation | CLAIM unaware(person: STRING / TERM, topic: STRING / TERM) | Asserts epistemic lack of awareness regarding a topic, fact, or event. epistemic state. | aliases: ignorant_of  ⟵ candidate
- validates_parameter | claim_relation | CLAIM validates_parameter(condition: STRING, entity: TERM, parameter: STRING) | Asserts that a code entity inspects or validates parameter names or types for a specified condition. | not: a runtime assertion test | aliases: inspects_parameter, checks_parameter, validates_parameter_names  ⟵ candidate

### links

- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ core
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ core
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ candidate
- then | link | LINK then(previous: EVENT, next: EVENT) | Represents temporal sequence and succession between two events where next follows previous. previous and next must be event terms. | aliases: followed_by, after_which  ⟵ candidate

### values

- art_character_profile | value | artifact-value | Descriptive character profile.  ⟵ candidate
- art_itinerary | value | artifact-value | An ordered travel plan; GENERATE returns STRING, not booked travel  ⟵ candidate
- art_plan | value | artifact-value | Actionable plan.  ⟵ candidate
- art_short_text | value | artifact-value | Short free text.  ⟵ candidate
- art_story | value | artifact-value | Narrative story.  ⟵ candidate
- constraint_17_plus | value | constraint-value | Rated 17+ or mature.  ⟵ candidate
- yakuza | value | descriptive-value | Descriptive concept of yakuza in cultural and social contexts. | aliases: yakuza  ⟵ candidate
- unit_day | value | duration-unit-value | Day. | aliases: days  ⟵ candidate
- unit_word | value | duration-unit-value | Rendered whitespace-delimited word. | aliases: words  ⟵ candidate
- apple | value | entity-name | An apple fruit item, typically an ingredient or interactive food object. | not: food_label::tomato or other fruits/vegetables | aliases: apple, apples, red apple, green apple, apple slice  ⟵ candidate
- bowtie | value | entity-name | Item or prop in joke/creative context: bowtie. | aliases: bowtie  ⟵ candidate
- bread | value | entity-name | A bread loaf or slice food object. | aliases: bread  ⟵ candidate
- candle | value | entity-name | A candle light source made of wax with a wick. | not: lamp (an electric light appliance or fixture) | aliases: candle, wax candle  ⟵ candidate
- dog | value | entity-name | Animal entity: dog. | not: animal_label::cat or animal_label::donkey | aliases: dog, dogs, canine, pup, puppy  ⟵ candidate
- dried_fruit | value | entity-name | Generic dried fruit food item. | not: fresh fruit or specific dried varieties like raisin or sultana | aliases: dried fruit, dried fruits  ⟵ candidate
- dulce_de_leche | value | entity-name | Sweet caramelized milk confection or dessert spread: dulce de leche. | not: cheese or dulce_de_nata | aliases: dulce de leche, dulce_de_leche  ⟵ candidate
- dulce_de_nata | value | entity-name | Clotted cream milk confection or dessert item: dulce de nata. | not: dulce_de_leche or cheese | aliases: dulce de nata, dulce_de_nata  ⟵ candidate
- entity_flowers | value | entity-name | Flowers, blossoms, or floral design elements. | not: constraint_exclude_flowery_language (a prose style constraint) or agricultural food items | aliases: flowers, floral, flower, floral decorations  ⟵ candidate
- fridge | value | entity-name | A refrigerator cooling appliance. | aliases: fridge  ⟵ candidate
- gift | value | entity-name | A physical gift or present item to be wrapped, given, or received. | not: egift_card (an electronic gift card or digital voucher product) | aliases: gift, present, wrapped gift, package  ⟵ candidate
- ginger | value | entity-name | Pungent aromatic spice root from Zingiber officinale used in cooking and baking. | not: cinnamon, cardamom, or other distinct spice varieties | aliases: ginger, ground ginger, fresh ginger, ginger root  ⟵ candidate
- grape_merlot | value | entity-name | Merlot wine grape variety. | not: other red grape varieties such as grape_cabernet_sauvignon or grape_pinot_noir | aliases: Merlot, merlot grape  ⟵ candidate
- grape_pinot_noir | value | entity-name | Pinot Noir wine grape variety. | not: other red grape varieties such as grape_cabernet_sauvignon or grape_merlot | aliases: Pinot Noir, pinot noir grape  ⟵ candidate
- grape_sauvignon_blanc | value | entity-name | Sauvignon Blanc wine grape variety. | not: other white grape varieties such as grape_chardonnay | aliases: Sauvignon Blanc, sauvignon blanc grape  ⟵ candidate
- grape_thompson_seedless | value | entity-name | Thompson Seedless grape variety. | not: wine grape cultivars like grape_merlot or grape_chardonnay | aliases: Thompson Seedless, thompson seedless grape, sultana grape  ⟵ candidate
- lettuce | value | entity-name | A head of lettuce or leafy green vegetable food item. | not: food_label::tomato or food_label::potato (other vegetable items) | aliases: lettuce, head of lettuce, salad greens  ⟵ candidate
- moon | value | entity-name | Earth's natural celestial satellite. | not: an artificial satellite or other planetary moon | aliases: moon, the moon, Luna  ⟵ candidate
- pear | value | entity-name | A pear fruit item, typically an ingredient or fresh fruit object. | not: apple, food_label::tomato, or other distinct fruit items | aliases: pear, pears, fresh pear, sliced pear  ⟵ candidate
- raisin | value | entity-name | Dried grape food item. | not: sultana (specifically dried white grape) or fresh wine_grape | aliases: raisin, raisins, dried grape  ⟵ candidate
- resource_chiller | value | entity-name | Canonical abstract chilling resource when no particular appliance is named.  ⟵ candidate
- resource_heater | value | entity-name | Canonical abstract heating resource when no particular appliance is named.  ⟵ candidate
- resource_sink | value | entity-name | Canonical abstract washing resource when no particular sink is named.  ⟵ candidate
- sultana | value | entity-name | Dried white seedless grape food product. | not: raisin (dark dried grape) or wine_grape | aliases: sultana, sultanas, golden raisin  ⟵ candidate
- sun | value | entity-name | The central star of the Solar System. | not: an artificial lighting appliance or sunlight | aliases: sun, the sun, Sol  ⟵ candidate
- locale_en_gb | value | locale-value | UK English. | aliases: british english  ⟵ candidate
- locale_en_us | value | locale-value | US English. | aliases: english, en-us  ⟵ candidate
- color_pink | value | product-attribute-value | Pink visual color qualifier. | not: color_label::red, color_label::purple, or other distinct color shades | aliases: pink, color_pink, blush pink, rose pink, pastel pink  ⟵ candidate
- condition_perfect | value | product-attribute-value | Product condition rating: perfect or mint physical and operational condition. | not: test_condition (software testing) or state_dirty (physical environmental state) | aliases: perfect, mint, pristine, flawless, like new  ⟵ candidate
- gender_unisex | value | product-attribute-value | Unisex. | aliases: unisex  ⟵ candidate
- size_small | value | product-attribute-value | Small size. | aliases: small, S  ⟵ candidate
- role_daughter | value | recipient-value | Daughter participant role in family or travel context. | not: role_sister, role_mother, or generic role_kids | aliases: daughter, my daughter  ⟵ candidate
- role_kids | value | recipient-value | Children/kids participant group in event context. | aliases: kids, children  ⟵ candidate
- role_mother | value | recipient-value | The mother of the user. | not: role_sister or role_kids | aliases: my mom, mother, mom  ⟵ candidate
- role_professor | value | recipient-value | The user's professor/instructor. | aliases: my professor, teacher  ⟵ candidate
- role_sister | value | recipient-value | Sister participant role in family/event context. | aliases: sister  ⟵ candidate
- shape_square | value | shape-value | Square. | aliases: square  ⟵ candidate
- behind | value | spatial-relation | Positioned behind.  ⟵ candidate
- between | value | spatial-relation | Positioned between or in the middle of reference entities. | not: next_to or in_front_of | aliases: between, in the middle of, middle of, center of  ⟵ candidate
- in_front_of | value | spatial-relation | Positioned in front of. | aliases: in front of  ⟵ candidate
- left_of | value | spatial-relation | To the left of. | aliases: left of  ⟵ candidate
- next_to | value | spatial-relation | Adjacent to. | aliases: beside  ⟵ candidate
- on | value | spatial-relation | Resting atop. | aliases: on top of  ⟵ candidate
- right_of | value | spatial-relation | To the right of. | aliases: right of  ⟵ candidate
- under | value | spatial-relation | Beneath. | aliases: below  ⟵ candidate
- state_clean | value | state-value | Clean condition. | aliases: clean  ⟵ candidate
- state_dirty | value | state-value | Dirty condition. | aliases: dirty  ⟵ candidate
- style_catchy | value | style-value | Catchy, attention-grabbing style. | aliases: catchy  ⟵ candidate
- tone_empathetic | value | tone-value | Conveys empathy/understanding. | aliases: sympathetically  ⟵ candidate
- tone_neutral | value | tone-value | Plain, unmarked register.  ⟵ candidate
- tone_polite | value | tone-value | Courteous, respectful register. | aliases: politely, kindly  ⟵ candidate
- tone_silly | value | tone-value | Playful, lighthearted, or silly conversational tone. | aliases: silly  ⟵ candidate
- topic_baldurs_gate_3 | value | topic-value | Baldur's Gate 3.  ⟵ candidate
- topic_current_events | value | topic-value | Current news, geopolitical events, and ongoing international developments. | aliases: current_events, news  ⟵ candidate
- topic_politics | value | topic-value | Politics.  ⟵ candidate
- topic_spider_man_2 | value | topic-value | Marvel's Spider-Man 2.  ⟵ candidate
