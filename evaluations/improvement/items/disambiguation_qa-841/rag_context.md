# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 17 needs (decomposition: llm), 129 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | claim | t1:s1 | A sentence contains pronouns with antecedents that are either context-derivable or ambiguous | `unit_sentence`*, `enables`, `comfortable`, `unaware`, `style_persuasive`, `varies_with`, `reason_for`, `naming_convention`, `subject`, `failure`, `motivated_by`, `temporal_context` |
| n2 | object | t1:s2 | chef → `object_label::<key>` | `chill`, `role_manager`, `role_colleague`, `role_professor`, `role_agent`, `in_front_of`, `coffee_maker`, `role_user`, `chair`, `tone_polite`, `resource_heater`, `resource_chiller` |
| n3 | object | t1:s2 | waiter → `object_label::<key>` | `restaurant`, `cuisine_mediterranean`, `cuisine`, `cuisine_italian`, `ryokan`, `coffee_maker`, `menu_works`, `plate`, `spoon`, `cuisine_pizza`, `tone_polite`, `chair` |
| n4 | object | t1:s2 | customers → `object_label::<key>` | `role_customer`, `role_support_team`, `metric_repeat_buyer`, `role_manager`, `role_colleague`, `restaurant`, `role_user`, `valet`, `coffee_maker`, `role_friend`, `menu_works`, `user_preference` |
| n5 | object | t1:s2 | staff members → `object_label::<key>` | `role_manager`, `role_colleague`, `role_agent`, `role_support_team`, `role_professor`, `role_customer`, `role_user`, `tone_professional`, `coffee_maker`, `role_respondent`, `role_friend`, `resource_chiller` |
| n6 | object | t1:s3 | order → `object_label::<key>` | `entity_order_vs_assemble_plan`, `metric_order_late`, `in_front_of`, `sort`, `right_of`, `ask`, `coffee_maker`, `chair`, `add_to_cart`, `style_catchy`, `decision`, `sequence` |
| n7 | object | t1:s4 | job → `object_label::<key>` | `role_colleague`, `role_manager`, `role_agent`, `tone_professional`, `role_user`, `role_customer`, `coffee_maker`, `desk`, `role_professor`, `topic_school_work_routine`, `resource_chiller`, `chair` |
| n8 | object | t1:s4 | manager → `object_label::<key>` | `role_manager`, `coffee_maker`, `role_colleague`, `role_professor`, `restaurant`, `role_agent`, `role_customer`, `counter`, `tone_professional`, `chair`, `island`, `desk` |
| n9 | object | t1:s2, t1:s3, t1:s4, t1:s5, t1:s6 | The narrative text containing pronouns and ambiguous antecedents | `style_narrative`*, `art_story`, `style_persuasive`, `beliefs`, `rule_category_style_value`, `character`, `rule_category_event_value`, `in`, `respond`, `subject`, `topic_pickup_lines`, `coffee_maker` |
| n10 | speech_act | t1:s7 | Asks to identify the correct explanation of pronoun antecedents | `ask`*, `correct`*, `respond`, `inform`, `propose`, `distinguish`, `reason_for`, `acknowledge`, `gender_men`, `subject`, `created_by`, `style_persuasive` |
| n11 | action | t1:s7 | Identify the correct option explaining the pronoun antecedents | `correct`*, `distinguish`, `subject`, `activity`, `style_persuasive`, `propose`, `in_front_of`, `obligation`, `select_option`, `role_agent`, `enables`, `right_of` |
| n12 | constraint | t1:s8, t1:s9, t1:s10, t1:s11 | Option A: Waiter forgot order, waiter angry, waiter spoke to manager, final sentence speaker is ambiguous | `unit_sentence`*, `metric_order_late`, `role_manager`, `ask`, `greeting`, `correct`, `tone_polite`, `constraint_exclude_flowery_language`, `propose`, `constraint_budget_limited`, `respond`, `constraint_respectful` |
| n13 | constraint | t1:s12, t1:s13, t1:s14, t1:s15 | Option B: Chef forgot order, chef angry, waiter spoke to manager, final sentence speaker is ambiguous | `unit_sentence`*, `role_manager`, `ask`, `greeting`, `metric_order_late`, `constraint_exclude_flowery_language`, `correct`, `tone_urgent`, `propose`, `constraint_budget_limited`, `tone_polite`, `menu_works` |
| n14 | constraint | t1:s16, t1:s17, t1:s18, t1:s19 | Option C: Chef forgot order, chef angry, chef and waiter spoke to manager, chef said final sentence | `unit_sentence`*, `role_manager`, `metric_order_late`, `constraint_exclude_flowery_language`, `menu_works`, `constraint_budget_limited`, `restaurant`, `greeting`, `correct`, `ask`, `role_professor`, `propose` |
| n15 | constraint | t1:s20, t1:s21, t1:s22, t1:s23 | Option D: Waiter forgot order, chef angry, chef and waiter spoke to manager, final sentence speaker is ambiguous | `unit_sentence`*, `role_manager`, `greeting`, `metric_order_late`, `ask`, `correct`, `tone_polite`, `offer_help`, `constraint_exclude_flowery_language`, `propose`, `constraint_budget_limited`, `restaurant` |
| n16 | constraint | t1:s24, t1:s25, t1:s26, t1:s27 | Option E: Chef forgot order, chef angry, chef and waiter spoke to manager, manager said final sentence | `role_manager`, `unit_sentence`*, `metric_order_late`, `constraint_exclude_flowery_language`, `restaurant`, `menu_works`, `ask`, `greeting`, `constraint_budget_limited`, `propose`, `acknowledge`, `role_professor` |
| n17 | constraint | t1:s28 | Option F: None of the above options are correct | `correct`*, `select_option`, `constraint_respectful`, `constraint_exclude_flowery_language`, `constraint_budget_limited`, `in_front_of`, `constraint_single_choice`, `constraint_realistic`, `menu_works`, `propose_menu`, `constraint_comprehensive`, `constraint_beginner` |

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
- activity.object → object_label, food_label, animal_label
- activity.location → country
- activity.instrument → object_label, platform_label
- requirement.value → platform_label

## Retrieved records

### Shared rules that govern the records below (full text)

**rule_lexical_groups** (v19/rule/lexical-groups; rule governing platform_label)

Section 3.1 defines value groups: `group::key` values of type ATOM[group]. Open groups admit any key of their form (examples are not whitelists); standard groups admit the codes of their bundled standard (ISO 3166-1 alpha-2 for country, ISO 4217 for currency). Leaf values are never glossary entries. Consumer signatures alone decide where a group may appear. Retired bare symbols are invalid.

**rule_reading_guide** (v19/rule/reading-guide; core)

The spec governs syntax/types; this glossary defines vocabulary. Signature notation: ? optional, A / B explicit alternatives, void no result. Omitted optional arguments are unspecified. Value entries are category-refined STRING primitives; complex meanings require composition. Aliases are contextual hints, not unconditional equivalences. Report ambiguity. IDs use v19/<category>/<symbol>, v19/support/<symbol> or v19/composite/<symbol>. Statuses apply to this candidate: Retained preserves meaning; Adapted uses the stated contract; Composite requires TERM (bare STRING deprecated); Structural is syntax/argument vocabulary; Needs clarification is unusable until resolved; Deprecated is historical; Accepted is usable within this candidate.

**rule_recording_signatures** (v19/rule/recording-signatures; rule governing chill)

RECORD ACTION uses the operation signature with REF[STRING] → TERM and LIST[REF[STRING]] → LIST[TERM]; other types/categories stay unchanged. Return EVENT, never the runtime result. Record actual outputs as attributed CLAIMs. Do not infer missing resources.

**rule_speech_acts_general** (v19/rule/speech-acts-general; rule governing ask)

UTTER-only, void, with the spec's speech attributes and LIST[TERM] constraints. No result binding. Literal content cannot replace required semantic arguments for structured coverage.

**rule_structural_constructs** (v19/rule/structural-constructs; core)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; rule governing enables)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_attributes_and_generate** (v19/rule/attributes-and-generate; rule governing cuisine)

Attribute entries name arguments; legality/types come from each operation, not global membership. GENERATE uses the spec's core fields; retained artifact profiles return STRING. Numeric/list results need explicit profiles. Legacy itinerary fields expand to TERM constraints: duration/duration_unit → duration(amount,unit); stop_min_per_day/stop_requirement → minimum_per_period(class,count,period=unit_day), never an inferred temple class; max_walk_duration/unit → maximum_between_stops(activity="walk",amount,unit). No legacy shorthand is enabled. Old events/character_properties/transformations become explicitly scoped TERM constraints. Message purpose is TERM, not send_email.content: GENERATE exact STRING content, then send. Report opaque fallback separately.

**rule_category_artifact_value** (v19/rule/category/artifact-value; rule governing art_story)

STRING artifact class for GENERATE.target. art_story says what kind of artifact to produce, not what occurs in its plot.

**rule_category_constraint_value** (v19/rule/category/constraint-value; rule governing constraint_exclude_flowery_language)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_cuisine_value** (v19/rule/category/cuisine-value; rule governing cuisine_mediterranean)

STRING cuisine class; cuisine_indian is a cuisine filter, not the location India.

**rule_category_descriptive_value** (v19/rule/category/descriptive-value; rule governing beliefs)

STRING modifier/domain label; never a free-form proposition. dom_sgi needs its intended referent established before semantically dependent use.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; rule governing unit_sentence)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing coffee_maker)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_event_value** (v19/rule/category/event-value; candidate)

TERM-described narrative event, not a recorded EVENT. Require inclusion explicitly when generating a story.

**rule_category_format_value** (v19/rule/category/format-value; rule governing format_numbered_list)

STRING format. format_email is layout, not the action send_email.

**rule_category_location_name** (v19/rule/category/location-name; rule governing ryokan)

STRING location descriptor. A `table` surface is not the generated artifact category art_table.

**rule_category_metric_value** (v19/rule/category/metric-value; rule governing metric_repeat_buyer)

STRING metric identity, not a Boolean value. Uptime and response time need numeric observations with units; order-late is Boolean-valued. Do not type every metric as BOOL.

**rule_category_product_attribute_value** (v19/rule/category/product-attribute-value; rule governing valet)

STRING color/size/product-market facets. gender_women describes a product category, not an assertion about a person's gender.

**rule_category_recipient_value** (v19/rule/category/recipient-value; rule governing role_manager)

STRING roles or explicit named recipients. A role is not an exact person's identity. Keep an explicit name where substituting a role loses information.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing in_front_of)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_style_value** (v19/rule/category/style-value; candidate)

STRING production style. style_narrative does not establish that described events occurred.

**rule_category_tone_value** (v19/rule/category/tone-value; rule governing tone_polite)

STRING register. tone_urgent describes urgency, not a concrete deadline.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_school_work_routine)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_composites_general** (v19/rule/composites-general; rule governing topic_school_work_routine)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_operations_general** (v19/rule/operations-general; rule governing chill)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_search_web_attributes** (v19/rule/search-web-attributes; rule governing sort)

Optional filters: availability, category, color, cuisine, currency, gender, genre, location, platform, ram_unit, reservation_availability, shape, size (category-refined STRING); max_price, min_ram, min_rating (NUMBER); trending (BOOL). Explicit signature alternatives additionally admit atoms. Price requires currency; RAM requires a capacity unit; no default scale/source. rank is invalid: use sort, whose rank_field accepts rank_* and rank_direction accepts dir_*. Category/genre/availability accept only their own subfamilies.

**rule_supplemental_general** (v19/rule/supplemental-general; rule governing coffee_maker)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; rule governing subject)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- add_to_cart | operation | operation-vocabulary | (target: LIST[REF[STRING]]) -> void | Add the explicitly selected items. Does not pay or place an order.  ⟵ candidate
- chill | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Chill using the stated resource; same identity.  ⟵ candidate
- select_option | operation | operation-vocabulary | (target: REF[STRING], value: STRING) -> void | Select an option from a dropdown or select menu element. target must be a select element. | aliases: choose_option, choose_dropdown, pick_option  ⟵ candidate
- send_message | operation | operation-vocabulary | (recipient: STRING, content: STRING, tone?: STRING) -> void | Send supplied exact content through the specified message context. If the channel is unresolved, report it. | aliases: text  ⟵ candidate
- sort | operation | operation-vocabulary | (target: LIST[REF[STRING]], rank_direction: STRING, rank_field: STRING) -> LIST[REF[STRING]] | Request ordering of selected results. Preserve member identity; this is not a claim that order was observed. | aliases: rank, order by  ⟵ candidate

### speech acts

- acknowledge | speech_act | operation-vocabulary | UTTER acknowledge(target: CLAIM / TERM) | Acknowledge receipt/awareness; does not imply agreement.  ⟵ candidate
- ask | speech_act | operation-vocabulary | UTTER ask(target: TERM, or a sufficiently precise topic: STRING / TERM) | Request information/advice; not an assertion of an answer. | aliases: ask, how should  ⟵ candidate
- correct | speech_act | operation-vocabulary | UTTER correct(target: CLAIM) | Offer corrected content. Actual supersession requires the Conversation revision rules.  ⟵ candidate
- inform | speech_act | operation-vocabulary | UTTER inform(target: CLAIM) | Present the proposition; preserve its holder/status.  ⟵ candidate
- offer | speech_act | operation-vocabulary | UTTER offer(target: STRING / TERM) | Speech act offering assistance, service, or items to a conversation partner. speech act in dialogic traces. | aliases: proffer  ⟵ candidate
- propose | speech_act | operation-vocabulary | UTTER propose(target: TERM) | Suggest an action/idea; does not record it as performed.  ⟵ candidate
- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ candidate
- character | constructor | TERM character(name: STRING, series?: STRING) -> TERM | Constructs a descriptive representation of a fictional or narrative character. name specifies the character identifier. | aliases: fictional_character  ⟵ candidate
- conjunction | constructor | TERM conjunction(items: LIST[TERM]) -> TERM | All described components apply | not: Does not imply temporal order  ⟵ dependency of topic_school_work_routine
- decision | constructor | TERM decision(activity: TERM) -> TERM | A decision whose content is the described activity | not: Not proof it was carried out  ⟵ candidate
- distinguish | constructor | TERM distinguish(first: TERM, second: TERM, criterion?: STRING / TERM) -> TERM | Constructs a descriptive representation of discerning or differentiating between two entities, conditions, or behaviors along an optional criterion. | not: visual_contrast (optical contrast) or LINK contrast (rhetorical opposition between claims) | aliases: tell the difference, differentiate, distinguish between  ⟵ candidate
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ dependency of constraint_exclude_flowery_language
- greeting | constructor | TERM greeting(recipient: STRING) -> TERM | Constructs a conversational salutation greeting descriptor. conversational discourse term. | aliases: salutation  ⟵ candidate
- obligation | constructor | TERM obligation(actor: STRING / TERM, activity: TERM) -> TERM | Constructs a deontic obligation description requiring an actor to perform an activity. actor and activity specified. | aliases: duty, mandatory_activity  ⟵ candidate
- offer_help | constructor | TERM offer_help() -> TERM | Constructs a conversational proffer of assistance or support. conversational discourse term. | aliases: help_offer  ⟵ candidate
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ dependency of constraint_budget_limited
- sequence | constructor | TERM sequence(items: LIST[TERM]) -> TERM | Ordered described activities/content | not: Not unordered conjunction  ⟵ candidate
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ candidate
- temporal_context | constructor | TERM temporal_context(activity: STRING / TERM, period?: STRING) -> TERM | Constructs a temporal or situational context descriptor specifying an ongoing process, evaluation phase, or historical timeframe. | not: time_point (a specific timestamp/date) or duration (an elapsed numerical duration) | aliases: while, during, in past relationships, timeframe  ⟵ candidate

### composites

- constraint_beginner | composite | constraint-value | TERM constraint_beginner() -> TERM | Targeted at beginners. | = requirement(property="audience_expertise", value="beginner")  ⟵ candidate
- constraint_budget_limited | composite | constraint-value | TERM constraint_budget_limited() -> TERM | Limited budget. | = requirement(property="budget_limited", value=TRUE)  ⟵ candidate
- constraint_comprehensive | composite | constraint-value | TERM constraint_comprehensive() -> TERM | Must be comprehensive. | = requirement(property="comprehensive", value=TRUE)  ⟵ candidate
- constraint_exclude_flowery_language | composite | constraint-value | TERM constraint_exclude_flowery_language() -> TERM | Avoid flowery language. | = exclude(item="flowery_language")  ⟵ candidate
- constraint_realistic | composite | constraint-value | TERM constraint_realistic() -> TERM | Must be realistic. | = requirement(property="realistic", value=TRUE)  ⟵ candidate
- constraint_respectful | composite | constraint-value | TERM constraint_respectful() -> TERM | Must be respectful. | = requirement(property="respectful", value=TRUE)  ⟵ candidate
- constraint_single_choice | composite | constraint-value | TERM constraint_single_choice() -> TERM | Must pick a single choice. | = requirement(property="choice_count", value=1)  ⟵ candidate
- topic_school_work_routine | composite | topic-value | TERM topic_school_work_routine() -> TERM | School and work routine. | = subject(kind="routine", qualifier=conjunction(items=[subject(kind="school"), subject(kind="work")]))  ⟵ candidate

### claim relations

- comfortable | claim_relation | CLAIM comfortable(person: TERM, value: BOOL) | Asserts whether a person or animal is comfortable in a situation. affective/state claim. | aliases: is_comfortable  ⟵ candidate
- created_by | claim_relation | CLAIM created_by(subject: STRING / TERM, creator: STRING) | Asserts the developer, author, or creator of an entity or system. provenance/creator assertion. | aliases: authored_by  ⟵ candidate
- enables | claim_relation | CLAIM enables(condition: TERM / CLAIM, outcome: TERM / CLAIM) | Asserts that an enabling condition or capability facilitates an outcome. enabling condition. | aliases: facilitates, allows  ⟵ candidate
- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ candidate
- menu_works | claim_relation | CLAIM menu_works(property: STRING) | Asserts that a menu or recipe plan satisfies an operational criterion. menu evaluation. | aliases: menu_satisfies  ⟵ candidate
- motivated_by | claim_relation | CLAIM motivated_by(claim: CLAIM, motive: STRING / TERM) | Asserts that an action, rule, or claim is motivated by an underlying motive or goal. motive explanation. | aliases: rationale_is  ⟵ candidate
- naming_convention | claim_relation | CLAIM naming_convention(pattern: TERM, context?: STRING) | Asserts that a naming pattern is a recognized convention within a given domain. pattern must be a naming_pattern or term. | aliases: is_naming_convention  ⟵ candidate
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ dependency of enables
- prohibited | claim_relation | CLAIM prohibited(subject: STRING / TERM, location: STRING / TERM, condition?: STRING / TERM) | Asserts that a subject is prohibited from a location or activity under specified conditions. deontic prohibition claim. | aliases: forbidden, banned_from  ⟵ related to obligation
- propose_menu | claim_relation | CLAIM propose_menu(menu: TERM) | Asserts the proposal of a comprehensive menu plan. planning proposal. | aliases: suggest_menu  ⟵ candidate
- proposed_policy | claim_relation | CLAIM proposed_policy(policy: TERM, requirements: LIST[TERM]) | Asserts that a proposed policy framework comprises the specified requirement terms. policy must be a policy term. | aliases: policy_proposal  ⟵ related to obligation
- reason_for | claim_relation | CLAIM reason_for(subject: CLAIM / TERM, reason: STRING / TERM) | Asserts an explanatory reason for a policy, belief, or state of affairs. explanatory reason. | aliases: basis_for  ⟵ candidate
- recommended | claim_relation | CLAIM recommended(target: TERM / CLAIM) | Asserts an advisory recommendation that an activity or measure is advisable. advisory normative claim. | aliases: advisable  ⟵ candidate
- unaware | claim_relation | CLAIM unaware(person: STRING / TERM, topic: STRING / TERM) | Asserts epistemic lack of awareness regarding a topic, fact, or event. epistemic state. | aliases: ignorant_of  ⟵ candidate
- user_preference | claim_relation | CLAIM user_preference(constraints: TERM) | Asserts a user's stated preference constraints or dietary requirements. user constraint assertion. | aliases: stated_preference  ⟵ candidate
- varies_with | claim_relation | CLAIM varies_with(target: CLAIM / TERM, condition: STRING / TERM) | Asserts that a target claim or term varies contingently depending on specified conditions, external factors, or behavioral habits. | not: geographic variation only (use varies_by_location) | aliases: depends_on, contingent_on  ⟵ candidate

### links

- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ core
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ core
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ core

### values

- art_story | value | artifact-value | Narrative story.  ⟵ candidate
- cuisine_italian | value | cuisine-value | Italian cuisine. | aliases: Italian food, Italian  ⟵ candidate
- cuisine_mediterranean | value | cuisine-value | Mediterranean culinary cuisine style. | aliases: mediterranean  ⟵ candidate
- cuisine_pizza | value | cuisine-value | Pizza culinary cuisine style and food category. | not: cuisine_italian (broader regional/national cuisine) | aliases: pizza, pizzeria, pizza cuisine  ⟵ candidate
- beliefs | value | descriptive-value | Concept of cognitive beliefs, convictions, or worldviews. | aliases: beliefs  ⟵ candidate
- criminality | value | descriptive-value | Descriptive concept of criminality in cultural and social contexts. | aliases: criminality  ⟵ candidate
- unit_sentence | value | duration-unit-value | One grammatical sentence in text generation or constraint counting. | not: unit_paragraph (paragraph block) or unit_word (individual word) | aliases: sentence, sentences  ⟵ candidate
- chair | value | entity-name | A chair furniture seat with a backrest. | not: object_label::armchair (specifically an object_label::armchair with side armrests) or object_label::sofa | aliases: chair, seat  ⟵ candidate
- coffee_maker | value | entity-name | A coffee-making appliance; not automatically a heating resource  ⟵ candidate
- desk | value | entity-name | A work desk furniture surface. | aliases: desk  ⟵ candidate
- entity_order_vs_assemble_plan | value | entity-name | Event planning item or menu category: entity_order_vs_assemble_plan. | aliases: entity_order_vs_assemble_plan  ⟵ candidate
- plate | value | entity-name | A shallow, flat dish or vessel used for holding, preparing, or serving food. | not: bowl (deep concave vessel) or table (furniture surface) | aliases: dish, plate  ⟵ candidate
- resource_chiller | value | entity-name | Canonical abstract chilling resource when no particular appliance is named.  ⟵ candidate
- resource_heater | value | entity-name | Canonical abstract heating resource when no particular appliance is named.  ⟵ candidate
- restaurant | value | entity-name | A commercial restaurant, eatery, or dining establishment where meals are prepared and served. | not: ryokan or onsen (specific traditional hospitality establishments) | aliases: restaurant, eatery, dining establishment, restaurants  ⟵ candidate
- spoon | value | entity-name | An eating or cooking utensil. | aliases: spoon  ⟵ candidate
- format_numbered_list | value | format-value | Numbered list. | aliases: numbered steps  ⟵ candidate
- counter | value | location-name | A kitchen or room countertop surface. | aliases: counter  ⟵ candidate
- island | value | location-name | A freestanding kitchen island counter or food preparation work surface. | not: counter (a perimeter countertop surface) or table (a dining or general furniture surface) | aliases: island, kitchen island, kitchen_island  ⟵ candidate
- ryokan | value | location-name | Traditional Japanese establishment or hospitality venue: ryokan. | aliases: ryokan  ⟵ candidate
- metric_order_late | value | metric-value | Whether an order is late. | aliases: order is late, delayed  ⟵ candidate
- metric_repeat_buyer | value | metric-value | Whether the customer is a repeat buyer. | aliases: repeat buyer, returning customer  ⟵ candidate
- gender_men | value | product-attribute-value | Men's/male-targeted. | aliases: men, male  ⟵ candidate
- valet | value | product-attribute-value | Valet parking or dedicated vehicle attendant service. | aliases: valet_parking  ⟵ candidate
- role_agent | value | recipient-value | The assistant. | aliases: you, the assistant  ⟵ candidate
- role_colleague | value | recipient-value | A coworker of the user. | aliases: my colleague, coworker  ⟵ candidate
- role_customer | value | recipient-value | A customer/client of the user. | aliases: the customer, client  ⟵ candidate
- role_friend | value | recipient-value | A friend of the user. | aliases: my friend  ⟵ candidate
- role_manager | value | recipient-value | The user's manager. | aliases: my manager, boss  ⟵ candidate
- role_professor | value | recipient-value | The user's professor/instructor. | aliases: my professor, teacher  ⟵ candidate
- role_respondent | value | recipient-value | A respondent, survey participant, or interviewee providing primary research data. | not: role_customer (the user's client) or role_user (the conversational user) | aliases: respondent, respondents, survey respondent, study participant  ⟵ candidate
- role_support_team | value | recipient-value | A customer-support team. | aliases: support, customer service  ⟵ candidate
- role_user | value | recipient-value | The requesting human. | aliases: me, I  ⟵ candidate
- in | value | spatial-relation | Contained within. | aliases: inside  ⟵ candidate
- in_front_of | value | spatial-relation | Positioned in front of. | aliases: in front of  ⟵ candidate
- right_of | value | spatial-relation | To the right of. | aliases: right of  ⟵ candidate
- style_catchy | value | style-value | Catchy, attention-grabbing style. | aliases: catchy  ⟵ candidate
- style_narrative | value | style-value | Story-like narrative style. | aliases: narrative, story-style  ⟵ candidate
- style_persuasive | value | style-value | Persuasive/argumentative style. | aliases: persuasive  ⟵ candidate
- tone_polite | value | tone-value | Courteous, respectful register. | aliases: politely, kindly  ⟵ candidate
- tone_professional | value | tone-value | Workplace-appropriate register. | aliases: professionally  ⟵ candidate
- tone_urgent | value | tone-value | Conveys urgency. | aliases: urgently, ASAP  ⟵ candidate
- topic_pickup_lines | value | topic-value | Pickup lines.  ⟵ candidate

### attributes

- cuisine | attribute | attribute-name | Restaurant or food cuisine from cuisine-value.  ⟵ candidate
