# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 18 needs (decomposition: llm), 125 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | speech_act | t1:s2 | asks which of the five boolean expressions evaluates to true | `ask`*, `test_condition`, `inform`, `assert_multinomial_scorer`, `confirm`, `decline`, `respond`, `propose`, `extract`, `subject`, `apologize`, `express_interest` |
| n2 | action | t1:s2 | evaluate five complex boolean expressions | `test_condition`, `calculation`, `block_evaluation`, `rule_category_metric_value`, `subject`, `extract`, `assert_multinomial_scorer`, `decision`, `conjunction`, `conditional`, `negation`, `distinguish` |
| n3 | constraint | t1:s1 | exactly one of the five expressions evaluates to true | `extract`, `assert_multinomial_scorer`, `conjunction`, `test_condition`, `constraint_exclude_flowery_language`, `decision`, `confirm`, `right_of`, `left_of`, `calculation`, `conditional`, `constraint_budget_limited` |
| n4 | object | t1:s3 | boolean expression A | `rule_category_metric_value`, `test_condition`, `constraint_exclude_flowery_language`, `right_of`, `subject`, `extract`, `motivated_by`, `conditional`, `character_trait`, `example_c_existing_constraint_symbol_becomes_a_typed_construction`, `pear`, `instantiates` |
| n5 | object | t1:s3 | the country India → `country::<key>` | `country`*, `rule_category_cuisine_value`, `cuisine_indian`, `africa`, `locale_hi_en`, `united_kingdom`, `locale_en_us`, `topic_greatest_cricketer_of_all_time`, `locale_en_gb`, `japanese_government`, `class_temple`, `foreigners` |
| n6 | object | t1:s4 | boolean expression B | `rule_category_metric_value`, `test_condition`, `constraint_exclude_flowery_language`, `subject`, `motivated_by`, `conditional`, `character_trait`, `extract`, `event_sadie_adler_unmasking`, `example_c_existing_constraint_symbol_becomes_a_typed_construction`, `sym_log_reg_scoring_path`, `code_entity` |
| n7 | object | t1:s4 | the country Germany → `country::<key>` | `country`*, `locale_de`, `ukraine`, `russia`, `japanese_government`, `locale_fr`, `locale_hi_en`, `foreigners`, `locale_en_us`, `locale_en_gb`, `liberal_onsen`, `bread` |
| n8 | object | t1:s5 | the country India → `country::<key>` | `country`*, `rule_category_cuisine_value`, `cuisine_indian`, `africa`, `locale_hi_en`, `united_kingdom`, `locale_en_us`, `topic_greatest_cricketer_of_all_time`, `locale_en_gb`, `japanese_government`, `class_temple`, `foreigners` |
| n9 | object | t1:s6 | boolean expression C | `rule_category_metric_value`, `test_condition`, `example_c_existing_constraint_symbol_becomes_a_typed_construction`, `conditional`, `grape_chardonnay`, `path_numpy_core_fromnumeric_py`, `subject`, `character_trait`, `sym_log_reg_scoring_path`, `motivated_by`, `decision`, `pear` |
| n10 | object | t1:s6 | the country Nepal → `country::<key>` | `country`*, `africa`, `cuisine_indian`, `united_kingdom`, `class_temple`, `locale_hi_en`, `locale_en_us`, `afcfta`, `foreigners`, `locale_zh`, `state_dirty`, `locale_de` |
| n11 | object | t1:s8 | boolean expression D | `rule_category_metric_value`, `test_condition`, `assert_multinomial_scorer`, `constraint_exclude_flowery_language`, `locale_de`, `subject`, `left_of`, `conditional`, `char_female`, `tone_empathetic`, `locale_fr`, `rule_support_primitives_general` |
| n12 | object | t1:s8 | the country Turkey → `country::<key>` | `country`*, `ukraine`, `russia`, `africa`, `cuisine_mediterranean`, `cuisine_arab`, `maqluba`, `currency`, `locale_en_us`, `meat`, `right_of`, `topic_current_events` |
| n13 | object | t1:s9 | the country Iran → `country::<key>` | `country`*, `russia`, `ukraine`, `africa`, `united_kingdom`, `topic_current_events`, `foreigners`, `cuisine_arab`, `reason_for`, `locale_en_us`, `topic_politics`, `locale_de` |
| n14 | object | t1:s9 | the country Malaysia → `country::<key>` | `country`*, `africa`, `united_kingdom`, `locale_zh`, `locale_en_gb`, `japanese_government`, `locale_hi_en`, `foreigners`, `locale_de`, `currency`, `locale_en_us`, `afcfta` |
| n15 | object | t1:s9 | the country Nigeria → `country::<key>` | `country`*, `africa`, `united_kingdom`, `afcfta`, `locale_en_gb`, `currency`, `ukraine`, `state_full`, `confirm`, `locale_en_us`, `topic_current_events`, `eastern_cape` |
| n16 | object | t1:s10 | boolean expression E | `rule_category_metric_value`, `test_condition`, `constraint_exclude_flowery_language`, `tone_empathetic`, `extract`, `locale_fr`, `event_sadie_adler_unmasking`, `calculation`, `example_e_preserve_exact_wording_through_generation_and_sending`, `character_trait`, `egift_card`, `subject` |
| n17 | object | t1:s11 | the country Gambia → `country::<key>` | `country`*, `africa`, `united_kingdom`, `afcfta`, `locale_en_gb`, `ukraine`, `currency`, `eastern_cape`, `locale_en_us`, `topic_current_events`, `foreigners`, `confirm` |
| n18 | object | t1:s11 | the country Azerbaijan → `country::<key>` | `country`*, `russia`, `ukraine`, `chill`, `africa`, `foreigners`, `topic_current_events`, `locale_fr`, `locale_en_us`, `locale_de`, `right_of`, `topic_politics` |

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
- code_entity.project → platform_label
- chill.destination → object_label
- activity.object → object_label, food_label, animal_label
- activity.location → country
- activity.instrument → object_label, platform_label
- requirement.value → platform_label
- failure.system → platform_label

## Retrieved records

### Shared rules that govern the records below (full text)

**rule_lexical_groups** (v19/rule/lexical-groups; rule governing platform_label)

Section 3.1 defines value groups: `group::key` values of type ATOM[group]. Open groups admit any key of their form (examples are not whitelists); standard groups admit the codes of their bundled standard (ISO 3166-1 alpha-2 for country, ISO 4217 for currency). Leaf values are never glossary entries. Consumer signatures alone decide where a group may appear. Retired bare symbols are invalid.

**rule_reading_guide** (v19/rule/reading-guide; core)

The spec governs syntax/types; this glossary defines vocabulary. Signature notation: ? optional, A / B explicit alternatives, void no result. Omitted optional arguments are unspecified. Value entries are category-refined STRING primitives; complex meanings require composition. Aliases are contextual hints, not unconditional equivalences. Report ambiguity. IDs use v19/<category>/<symbol>, v19/support/<symbol> or v19/composite/<symbol>. Statuses apply to this candidate: Retained preserves meaning; Adapted uses the stated contract; Composite requires TERM (bare STRING deprecated); Structural is syntax/argument vocabulary; Needs clarification is unusable until resolved; Deprecated is historical; Accepted is usable within this candidate.

**rule_recording_signatures** (v19/rule/recording-signatures; rule governing extract)

RECORD ACTION uses the operation signature with REF[STRING] → TERM and LIST[REF[STRING]] → LIST[TERM]; other types/categories stay unchanged. Return EVENT, never the runtime result. Record actual outputs as attributed CLAIMs. Do not infer missing resources.

**rule_speech_acts_general** (v19/rule/speech-acts-general; rule governing ask)

UTTER-only, void, with the spec's speech attributes and LIST[TERM] constraints. No result binding. Literal content cannot replace required semantic arguments for structured coverage.

**rule_structural_constructs** (v19/rule/structural-constructs; core)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; rule governing motivated_by)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_attributes_and_generate** (v19/rule/attributes-and-generate; rule governing art_short_text)

Attribute entries name arguments; legality/types come from each operation, not global membership. GENERATE uses the spec's core fields; retained artifact profiles return STRING. Numeric/list results need explicit profiles. Legacy itinerary fields expand to TERM constraints: duration/duration_unit → duration(amount,unit); stop_min_per_day/stop_requirement → minimum_per_period(class,count,period=unit_day), never an inferred temple class; max_walk_duration/unit → maximum_between_stops(activity="walk",amount,unit). No legacy shorthand is enabled. Old events/character_properties/transformations become explicitly scoped TERM constraints. Message purpose is TERM, not send_email.content: GENERATE exact STRING content, then send. Report opaque fallback separately.

**rule_category_artifact_value** (v19/rule/category/artifact-value; rule governing art_short_text)

STRING artifact class for GENERATE.target. art_story says what kind of artifact to produce, not what occurs in its plot.

**rule_category_character_property_value** (v19/rule/category/character-property-value; rule governing char_female)

TERM-described trait/style. Use constraints and explicit inclusion/scope; do not use an ungoverned character_properties attribute.

**rule_category_code_value** (v19/rule/category/code-value; rule governing assert_multinomial_scorer)

path_/sym_ remain STRING identities; migrated chg_/assert_ are TERM constructors. Do not recover an exact file path by guessing from underscores.

**rule_category_constraint_value** (v19/rule/category/constraint-value; rule governing constraint_exclude_flowery_language)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_content_value** (v19/rule/category/content-value; rule governing content_status_update)

Existing compounds become the constructors in Section 5. Their outputs go in topic/target/constraints as appropriate, not content, whose spec type remains STRING.

**rule_category_cuisine_value** (v19/rule/category/cuisine-value; candidate)

STRING cuisine class; cuisine_indian is a cuisine filter, not the location India.

**rule_category_descriptive_value** (v19/rule/category/descriptive-value; rule governing yakuza)

STRING modifier/domain label; never a free-form proposition. dom_sgi needs its intended referent established before semantically dependent use.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; rule governing unit_year)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing pear)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_event_value** (v19/rule/category/event-value; rule governing event_sadie_adler_unmasking)

TERM-described narrative event, not a recorded EVENT. Require inclusion explicitly when generating a story.

**rule_category_format_value** (v19/rule/category/format-value; rule governing format_email)

STRING format. format_email is layout, not the action send_email.

**rule_category_locale_value** (v19/rule/category/locale-value; rule governing locale_hi_en)

STRING locale. “English” alone does not always mean locale_en_us; preserve ambiguity.

**rule_category_location_name** (v19/rule/category/location-name; rule governing africa)

STRING location descriptor. A `table` surface is not the generated artifact category art_table.

**rule_category_metric_value** (v19/rule/category/metric-value; candidate)

STRING metric identity, not a Boolean value. Uptime and response time need numeric observations with units; order-late is Boolean-valued. Do not type every metric as BOOL.

**rule_category_recipient_value** (v19/rule/category/recipient-value; rule governing japanese_government)

STRING roles or explicit named recipients. A role is not an exact person's identity. Keep an explicit name where substituting a role loses information.

**rule_category_semantic_category_value** (v19/rule/category/semantic-category-value; rule governing class_temple)

STRING class label used by typed constraints. class_temple describes a class, not an acquired physical temple reference.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing right_of)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_state_value** (v19/rule/category/state-value; rule governing state_dirty)

STRING condition used in selection. state_warm does not command heat; “hot” is not automatically synonymous with “warm.”

**rule_category_tone_value** (v19/rule/category/tone-value; rule governing tone_empathetic)

STRING register. tone_urgent describes urgency, not a concrete deadline.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_greatest_cricketer_of_all_time)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_composites_general** (v19/rule/composites-general; rule governing assert_multinomial_scorer)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_examples_general** (v19/rule/examples-general; rule governing example_c_existing_constraint_symbol_becomes_a_typed_construction)

Examples use this glossary's contracts. They have not been verified by an implemented BrainCode parser.

**rule_operations_general** (v19/rule/operations-general; rule governing extract)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_supplemental_general** (v19/rule/supplemental-general; rule governing extract)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; candidate)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- chill | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Chill using the stated resource; same identity.  ⟵ candidate
- extract | operation | operation-vocabulary | (target: LIST[REF[STRING]], limit: NUMBER) -> LIST[REF[STRING]] | First limit results, preserving order and identity; limit is a nonnegative integer; limit=1 is still a list  ⟵ candidate
- send_email | operation | operation-vocabulary | (recipient: STRING, content: STRING, tone?: STRING) -> void | Send supplied exact message content to the identified recipient. A requested message purpose is not already a composed message. | aliases: email  ⟵ dependency of example_e_preserve_exact_wording_through_generation_and_sending

### speech acts

- apologize | speech_act | UTTER apologize(target?: CLAIM / TERM) | Speech act expressing apology or regret for an outcome or target. | not: decline (which is refusing) | aliases: apologize, apology, sorry  ⟵ candidate
- ask | speech_act | operation-vocabulary | UTTER ask(target: TERM, or a sufficiently precise topic: STRING / TERM) | Request information/advice; not an assertion of an answer. | aliases: ask, how should  ⟵ candidate
- confirm | speech_act | operation-vocabulary | UTTER confirm(target: CLAIM) | Confirm the proposition; its evidence/status remains explicit.  ⟵ candidate
- decline | speech_act | operation-vocabulary | UTTER decline(target: TERM) | Decline the represented request/proposal; not negate every proposition within it.  ⟵ candidate
- express_interest | speech_act | operation-vocabulary | UTTER express_interest(target: STRING / TERM) | Speech act expressing conversational interest or engagement in a topic. speech act in dialogic traces. | aliases: show_interest  ⟵ candidate
- inform | speech_act | operation-vocabulary | UTTER inform(target: CLAIM) | Present the proposition; preserve its holder/status.  ⟵ candidate
- propose | speech_act | operation-vocabulary | UTTER propose(target: TERM) | Suggest an action/idea; does not record it as performed.  ⟵ candidate
- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ dependency of decision
- block_evaluation | constructor | TERM block_evaluation(block: STRING / TERM, maturity?: STRING, potential?: STRING, quality?: STRING, rank?: NUMBER, traps?: STRING) -> TERM | Constructs a structured evaluation, categorization, or ranking descriptor for a geological exploration block. | not: an external execution action or generic list sorting operation (use sort) | aliases: block assessment, block ranking, block rating, block categorization  ⟵ candidate
- calculation | constructor | TERM calculation(inputs: LIST[TERM], operation: STRING, result?: TERM) -> TERM | Constructs a descriptive representation of an arithmetic or algorithmic calculation step with inputs, operation identifier, and optional resulting value. | not: an executed runtime action or factual claim of outcome | aliases: math_operation, compute_step  ⟵ candidate
- character_trait | constructor | TERM character_trait(property: STRING, value: STRING / NUMBER) -> TERM | A character attribute | not: Not a claim about a real person  ⟵ candidate
- code_entity | constructor | TERM code_entity(file?: STRING / TERM, kind: STRING, name: STRING, project?: STRING / ATOM[platform_label]) -> TERM | Constructs a structured descriptor for a source code entity such as a function, method, class, module, or source file within a project. | not: an executed runtime call or file system operation | aliases: code_function, source_file, code_symbol  ⟵ candidate
- conditional | constructor | TERM conditional(condition: TERM, consequence: TERM) -> TERM | Constructs a structured conditional proposition term connecting a condition and consequence. descriptive logic structure. | aliases: if_then  ⟵ candidate
- conjunction | constructor | TERM conjunction(items: LIST[TERM]) -> TERM | All described components apply | not: Does not imply temporal order  ⟵ candidate
- decision | constructor | TERM decision(activity: TERM) -> TERM | A decision whose content is the described activity | not: Not proof it was carried out  ⟵ candidate
- distinguish | constructor | TERM distinguish(first: TERM, second: TERM, criterion?: STRING / TERM) -> TERM | Constructs a descriptive representation of discerning or differentiating between two entities, conditions, or behaviors along an optional criterion. | not: visual_contrast (optical contrast) or LINK contrast (rhetorical opposition between claims) | aliases: tell the difference, differentiate, distinguish between  ⟵ candidate
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ dependency of constraint_exclude_flowery_language
- negation | constructor | TERM negation(target: TERM) -> TERM | Constructs a descriptive semantic negation of a target descriptive proposition or condition term. | not: Check's runtime Boolean operator NOT or a speech-act decline | aliases: not, does not, negation, absence of  ⟵ candidate
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ dependency of constraint_budget_limited
- sequence | constructor | TERM sequence(items: LIST[TERM]) -> TERM | Ordered described activities/content | not: Not unordered conjunction  ⟵ dependency of event_sadie_adler_unmasking
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ candidate
- test_condition | constructor | TERM test_condition(condition: STRING, expected: BOOL) -> TERM | A testable condition with the expected Boolean outcome | not: Expected outcome is not an observed result  ⟵ candidate

### composites

- char_female | composite | character-property-value | TERM char_female() -> TERM | Female gender. | = character_trait(property="gender", value="female") | aliases: female  ⟵ candidate
- assert_multinomial_scorer | composite | code-value | TERM assert_multinomial_scorer() -> TERM | Assertion that multinomial probabilistic scoring succeeds. | = test_condition(condition="multinomial_probabilistic_scoring", expected=TRUE)  ⟵ candidate
- constraint_budget_limited | composite | constraint-value | TERM constraint_budget_limited() -> TERM | Limited budget. | = requirement(property="budget_limited", value=TRUE)  ⟵ candidate
- constraint_exclude_flowery_language | composite | constraint-value | TERM constraint_exclude_flowery_language() -> TERM | Avoid flowery language. | = exclude(item="flowery_language")  ⟵ candidate
- constraint_realistic | composite | constraint-value | TERM constraint_realistic() -> TERM | Must be realistic. | = requirement(property="realistic", value=TRUE)  ⟵ dependency of example_c_existing_constraint_symbol_becomes_a_typed_construction
- content_status_update | composite | content-value | TERM content_status_update(subject: STRING) -> TERM | A request for a status update. | = activity(verb="request_update", object=$subject) | aliases: status update  ⟵ dependency of example_e_preserve_exact_wording_through_generation_and_sending
- event_sadie_adler_unmasking | composite | event-value | TERM event_sadie_adler_unmasking() -> TERM | Sadie Adler taking off her hat and peeling skin. | = sequence(items=[activity(verb="remove", actor="Sadie Adler", object="hat"), activity(verb="peel", actor="Sadie Adler", object="skin")])  ⟵ candidate
- topic_greatest_cricketer_of_all_time | composite | topic-value | TERM topic_greatest_cricketer_of_all_time() -> TERM | Greatest cricketer of all time. | = subject(kind="cricketer", qualifier=requirement(property="rank_by_greatness", value=1), time="all_time")  ⟵ candidate

### claim relations

- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ core
- instantiates | claim_relation | CLAIM instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) | Asserts that a code entity or constructor instantiates a target class or object under an optional condition. | not: an executed runtime object creation (pure factual assertion about code structure) | aliases: creates_instance, constructs_instance  ⟵ candidate
- motivated_by | claim_relation | CLAIM motivated_by(claim: CLAIM, motive: STRING / TERM) | Asserts that an action, rule, or claim is motivated by an underlying motive or goal. motive explanation. | aliases: rationale_is  ⟵ candidate
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ core
- reason_for | claim_relation | CLAIM reason_for(subject: CLAIM / TERM, reason: STRING / TERM) | Asserts an explanatory reason for a policy, belief, or state of affairs. explanatory reason. | aliases: basis_for  ⟵ candidate

### links

- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ core
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ core
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ core

### values

- art_short_text | value | artifact-value | Short free text.  ⟵ dependency of example_e_preserve_exact_wording_through_generation_and_sending
- path_numpy_core_fromnumeric_py | value | code-value | Source code file path or exported symbol in scientific Python: path_numpy_core_fromnumeric_py. | aliases: path_numpy_core_fromnumeric_py  ⟵ candidate
- sym_log_reg_scoring_path | value | code-value | The _log_reg_scoring_path program symbol.  ⟵ candidate
- cuisine_arab | value | cuisine-value | Arab culinary cuisine style. | not: cuisine_mediterranean (broader regional category) | aliases: Arab food, Arabic food, Arab cuisine  ⟵ candidate
- cuisine_indian | value | cuisine-value | Indian cuisine. | aliases: Indian food, Indian  ⟵ candidate
- cuisine_mediterranean | value | cuisine-value | Mediterranean culinary cuisine style. | aliases: mediterranean  ⟵ candidate
- yakuza | value | descriptive-value | Descriptive concept of yakuza in cultural and social contexts. | aliases: yakuza  ⟵ candidate
- unit_year | value | duration-unit-value | Year. | aliases: years  ⟵ candidate
- afcfta | value | entity-name | African Continental Free Trade Area international agreement. | aliases: african_continental_free_trade_area  ⟵ candidate
- bread | value | entity-name | A bread loaf or slice food object. | aliases: bread  ⟵ candidate
- chair | value | entity-name | A chair furniture seat with a backrest. | not: object_label::armchair (specifically an object_label::armchair with side armrests) or object_label::sofa | aliases: chair, seat  ⟵ candidate
- egift_card | value | entity-name | Electronic gift card or digital voucher product. | aliases: digital_gift_card, e_gift_card  ⟵ candidate
- grape_chardonnay | value | entity-name | Chardonnay wine grape variety. | not: other white grape varieties such as grape_sauvignon_blanc | aliases: Chardonnay, chardonnay grape  ⟵ candidate
- maqluba | value | entity-name | Traditional Arab layered rice dish: maqluba. | not: cuisine_mediterranean (cuisine style rather than specific dish) | aliases: maqluba, makloubeh  ⟵ candidate
- meat | value | entity-name | Food item: meat or beef. | not: animal_label::tuna or animal_label::fish (specific aquatic foods) | aliases: meat, beef  ⟵ candidate
- pear | value | entity-name | A pear fruit item, typically an ingredient or fresh fruit object. | not: apple, food_label::tomato, or other distinct fruit items | aliases: pear, pears, fresh pear, sliced pear  ⟵ candidate
- sultana | value | entity-name | Dried white seedless grape food product. | not: raisin (dark dried grape) or wine_grape | aliases: sultana, sultanas, golden raisin  ⟵ candidate
- format_email | value | format-value | Email layout. | aliases: as an email  ⟵ dependency of example_e_preserve_exact_wording_through_generation_and_sending
- locale_de | value | locale-value | German language or locale descriptor. | not: other language locales (such as locale_en_us or locale_fr) or country entity (country::DE) | aliases: German, german, Deutsch, de, de-DE  ⟵ candidate
- locale_en_gb | value | locale-value | UK English. | aliases: british english  ⟵ candidate
- locale_en_us | value | locale-value | US English. | aliases: english, en-us  ⟵ candidate
- locale_fr | value | locale-value | French. | aliases: french  ⟵ candidate
- locale_hi_en | value | locale-value | Hinglish (Hindi-English mix). | aliases: hinglish  ⟵ candidate
- locale_zh | value | locale-value | Chinese language locale (Simplified and Traditional Chinese). | not: a specific geographical region or nationality (use location-name) | aliases: chinese, zh, zh-cn, zh-tw, mandarin  ⟵ candidate
- africa | value | location-name | Geopolitical nation or continental region: africa. | aliases: africa  ⟵ candidate
- eastern_cape | value | location-name | Eastern Cape region.  ⟵ candidate
- liberal_onsen | value | location-name | Traditional Japanese establishment or hospitality venue: liberal_onsen. | aliases: liberal_onsen  ⟵ candidate
- russia | value | location-name | Geopolitical nation or continental region: russia. | aliases: russia  ⟵ candidate
- ukraine | value | location-name | Geopolitical nation or continental region: ukraine. | aliases: ukraine  ⟵ candidate
- united_kingdom | value | location-name | Geopolitical nation or sovereign state: United Kingdom (Great Britain). | not: locale_en_gb (a language/locale code, not a location) | aliases: United Kingdom, UK, Great Britain, Britain  ⟵ candidate
- foreigners | value | recipient-value | Social, demographic, or institutional group: foreigners. | aliases: foreigners  ⟵ candidate
- japanese_government | value | recipient-value | Social, demographic, or institutional group: japanese_government. | aliases: japanese_government  ⟵ candidate
- role_manager | value | recipient-value | The user's manager. | aliases: my manager, boss  ⟵ dependency of example_e_preserve_exact_wording_through_generation_and_sending
- class_temple | value | semantic-category-value | The abstract class of temples. | aliases: temple, temples  ⟵ candidate
- left_of | value | spatial-relation | To the left of. | aliases: left of  ⟵ candidate
- right_of | value | spatial-relation | To the right of. | aliases: right of  ⟵ candidate
- state_dirty | value | state-value | Dirty condition. | aliases: dirty  ⟵ candidate
- state_full | value | state-value | Contains its intended material or remaining usable amount. | aliases: full, filled  ⟵ candidate
- tone_empathetic | value | tone-value | Conveys empathy/understanding. | aliases: sympathetically  ⟵ candidate
- tone_polite | value | tone-value | Courteous, respectful register. | aliases: politely, kindly  ⟵ dependency of example_e_preserve_exact_wording_through_generation_and_sending
- topic_current_events | value | topic-value | Current news, geopolitical events, and ongoing international developments. | aliases: current_events, news  ⟵ candidate
- topic_pickup_lines | value | topic-value | Pickup lines.  ⟵ dependency of example_c_existing_constraint_symbol_becomes_a_typed_construction
- topic_politics | value | topic-value | Politics.  ⟵ candidate

### examples

- example_c_existing_constraint_symbol_becomes_a_typed_construction (candidate): Existing constraint symbol becomes a typed construction

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM constraint_realistic() -> constraint_realistic_2 : TERM
    UTTER ask(constraints=[constraint_realistic_2], topic=topic_pickup_lines)
  }
}
```

- example_e_preserve_exact_wording_through_generation_and_sending (candidate): Preserve exact wording through generation and sending

```braincode
MODE REQUEST
ENTRYPOINT ShortText
TASK ShortText {
  TERM content_status_update(subject="Project Atlas") -> content_status_update_2 : TERM
  GENERATE(target=art_short_text, format=format_email, tone=tone_polite, topic=content_status_update_2) -> short_text : STRING
  ACTION send_email(content=short_text, recipient=role_manager, tone=tone_polite)
}
```

