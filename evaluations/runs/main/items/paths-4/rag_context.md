# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 22 needs (decomposition: llm), 135 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | action | t1:s1 | edit the provided text | `send_message`*, `type_text`, `transform_remove_br`, `format_plain_text`, `rule_category_format_value`, `policy_revision_request`, `modify_code`, `send_email`, `calculation`, `document_section`, `press_key`, `obligation` |
| n2 | claim | t1:s1 | speaker is a visiting researcher at Hagen University in Germany | `considered`, `locale_de`, `enables`, `role_professor`, `topic_classical_piano`, `topic_jazz_piano`, `recommended`, `ongoing`, `role_colleague`, `new_york_university`, `outcome`, `occurred_recently` |
| n3 | object | t1:s1 | Germany → `country::<key>` | `bread`, `ukraine`, `locale_de`, `liberal_onsen`, `locale_fr`, `russia`, `onsen`, `topic_jazz_piano`, `locale_hi_en`, `grape_sauvignon_blanc`, `foreigners`, `topic_classical_piano` |
| n4 | claim | t1:s1 | speaker's visa is valid until the end of August of this year | `unit_year`*, `considered`, `unit_month`, `allowed_to_enter`, `enables`, `recommended`, `occurred_recently`, `confirm`, `ongoing`, `user_preference`, `inform`, `has_state` |
| n5 | temporal | t1:s1 | end of August of this year | `unit_year`*, `unit_month`, `daytime`, `unit_day`, `nighttime`, `unit_week`, `unit_hour`, `rule_category_duration_unit_value`, `topic_current_events`, `locale_en_us`, `duration`, `time_point` |
| n6 | claim | t1:s2 | the university is extending the speaker's stay | `new_york_university`, `correct`, `considered`, `ongoing`, `revises`, `enables`, `offer`, `recommended`, `user_preference`, `role_professor`, `outcome`, `express_interest` |
| n7 | action | t1:s2 | apply for a visa extension | `search_travel`, `modify_code`, `vehicle_allowance`, `apply_filters`, `allowed_to_enter`, `role_daughter`, `select_filter`, `role_adults`, `calculation`, `conjunction`, `obligation`, `constraint_comprehensive` |
| n8 | claim | t1:s3 | speaker is currently in Iran and will likely stay there until end of August | `ukraine`, `russia`, `considered`, `topic_current_events`, `enables`, `correct`, `has_state`, `inform`, `ongoing`, `outcome`, `locale_en_us`, `occurred_recently` |
| n9 | object | t1:s3 | Iran → `country::<key>` | `country`*, `ukraine`, `russia`, `topic_current_events`, `foreigners`, `grape_tannin`, `cuisine_arab`, `locale_zh`, `resource_chiller`, `sultana`, `eastern_cape`, `resource_heater` |
| n10 | speech_act | t1:s3 | inquire whether visa extension can be obtained from the German embassy in Tehran | `locale_de`*, `ukraine`, `liberal_onsen`, `express_interest`, `offer`, `onsen`, `foreigners`, `correct`, `inform`, `search_travel`, `confirm`, `ask` |
| n11 | object | t1:s3 | German embassy in Tehran | `locale_de`*, `ukraine`, `liberal_onsen`, `onsen`, `russia`, `foreigners`, `locale_fr`, `locale_zh`, `new_york_university`, `topic_jazz_piano`, `locale_en_us`, `resource_heater` |
| n12 | negation | t2:s1 | AI model does not possess latest immigration policy updates | `policy_revision_request`, `constitutional_ai`, `topic_ai_earning_methods`, `content_status_update`, `policy_document`, `proposed_policy`, `negation`*, `decline`, `design_parameters`, `software_version`, `country`, `art_itinerary` |
| n13 | speech_act | t2:s2 | advise contacting the German Embassy in Tehran for visa extension details | `locale_de`*, `offer`, `express_interest`, `ukraine`, `liberal_onsen`, `ask`, `correct`, `search_travel`, `propose`, `locale_fr`, `inform`, `respond` |
| n14 | speech_act | t2:s3 | advise applying well before visa expiration date | `ask`, `decline`, `inform`, `propose`, `confirm`, `wait`, `express_interest`, `offer`, `respond`, `apologize`, `search_travel`, `correct` |
| n15 | reasoning | t2:s3 | applying early avoids legal implications and ensures smooth transition | `supports`, `revises`, `contrast`, `ongoing`, `rule_category_tone_value`, `wait`, `constraint_exclude_flowery_language`, `confirm`, `exempt_from`, `rejects`, `decline`, `rule_support_primitives_general` |
| n16 | speech_act | t2:s4 | wish good luck with the extension request | `well_wishes`*, `offer`, `search_travel`, `express_interest`, `ask`, `policy_revision_request`, `confirm`, `inform`, `content_status_update`, `decline`, `correct`, `propose` |
| n17 | action | t3:s1 | edit the provided text passage | `send_message`*, `type_text`, `transform_remove_br`, `format_plain_text`, `unit_paragraph`, `policy_revision_request`, `modify_code`, `dialogue`, `document_section`, `calculation`, `press_key`, `revises` |
| n18 | speech_act | t4:s1, t4:s2, t4:s3, t4:s4 | provide an edited version of the visa extension inquiry email | `send_email`*, `express_interest`, `offer`, `format_email`, `inform`, `ask`, `correct`, `policy_revision_request`, `respond`, `apologize`, `confirm`, `propose` |
| n19 | action | t5:s1 | rewrite the provided text passage | `send_message`*, `type_text`, `transform_remove_br`, `format_plain_text`, `policy_revision_request`, `modify_code`, `footnote`, `substitute`, `dialogue`, `revises`, `calculation`, `press_key` |
| n20 | speech_act | t6:s1, t6:s2, t6:s3 | provide an alternative rewritten draft of the visa extension inquiry | `inform`, `confirm`, `offer`, `provides`*, `policy_revision_request`, `search_travel`, `express_interest`, `respond`, `correct`, `ask`, `propose`, `decline` |
| n21 | action | t7:s1 | rewrite the provided text passage | `send_message`*, `type_text`, `format_plain_text`, `transform_remove_br`, `policy_revision_request`, `modify_code`, `footnote`, `dialogue`, `substitute`, `revises`, `calculation`, `press_key` |
| n22 | speech_act | t8:s1, t8:s2, t8:s3, t8:s4 | provide a third rewritten draft of the inquiry to the German Embassy | `locale_de`*, `correct`, `respond`, `decline`, `propose`, `provides`*, `ukraine`, `inform`, `policy_revision_request`, `ask`, `express_interest`, `liberal_onsen` |

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

- modify_code.target → platform_label
- search_travel.location → country
- software_version.project → platform_label
- provides.actor → platform_label
- provides.subject → platform_label
- activity.object → object_label, food_label, animal_label
- activity.location → country
- activity.instrument → object_label, platform_label
- subject.qualifier → platform_label
- subject.location → country
- requirement.value → platform_label
- failure.system → platform_label

## Retrieved records

### Shared rules that govern the records below (full text)

**rule_lexical_groups** (v19/rule/lexical-groups; rule governing platform_label)

Section 3.1 defines value groups: `group::key` values of type ATOM[group]. Open groups admit any key of their form (examples are not whitelists); standard groups admit the codes of their bundled standard (ISO 3166-1 alpha-2 for country, ISO 4217 for currency). Leaf values are never glossary entries. Consumer signatures alone decide where a group may appear. Retired bare symbols are invalid.

**rule_reading_guide** (v19/rule/reading-guide; core)

The spec governs syntax/types; this glossary defines vocabulary. Signature notation: ? optional, A / B explicit alternatives, void no result. Omitted optional arguments are unspecified. Value entries are category-refined STRING primitives; complex meanings require composition. Aliases are contextual hints, not unconditional equivalences. Report ambiguity. IDs use v19/<category>/<symbol>, v19/support/<symbol> or v19/composite/<symbol>. Statuses apply to this candidate: Retained preserves meaning; Adapted uses the stated contract; Composite requires TERM (bare STRING deprecated); Structural is syntax/argument vocabulary; Needs clarification is unusable until resolved; Deprecated is historical; Accepted is usable within this candidate.

**rule_recording_signatures** (v19/rule/recording-signatures; rule governing send_message)

RECORD ACTION uses the operation signature with REF[STRING] → TERM and LIST[REF[STRING]] → LIST[TERM]; other types/categories stay unchanged. Return EVENT, never the runtime result. Record actual outputs as attributed CLAIMs. Do not infer missing resources.

**rule_speech_acts_general** (v19/rule/speech-acts-general; rule governing confirm)

UTTER-only, void, with the spec's speech attributes and LIST[TERM] constraints. No result binding. Literal content cannot replace required semantic arguments for structured coverage.

**rule_structural_constructs** (v19/rule/structural-constructs; core)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; rule governing considered)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_attributes_and_generate** (v19/rule/attributes-and-generate; rule governing art_itinerary)

Attribute entries name arguments; legality/types come from each operation, not global membership. GENERATE uses the spec's core fields; retained artifact profiles return STRING. Numeric/list results need explicit profiles. Legacy itinerary fields expand to TERM constraints: duration/duration_unit → duration(amount,unit); stop_min_per_day/stop_requirement → minimum_per_period(class,count,period=unit_day), never an inferred temple class; max_walk_duration/unit → maximum_between_stops(activity="walk",amount,unit). No legacy shorthand is enabled. Old events/character_properties/transformations become explicitly scoped TERM constraints. Message purpose is TERM, not send_email.content: GENERATE exact STRING content, then send. Report opaque fallback separately.

**rule_category_artifact_value** (v19/rule/category/artifact-value; rule governing art_itinerary)

STRING artifact class for GENERATE.target. art_story says what kind of artifact to produce, not what occurs in its plot.

**rule_category_constraint_value** (v19/rule/category/constraint-value; rule governing constraint_comprehensive)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_content_value** (v19/rule/category/content-value; rule governing content_status_update)

Existing compounds become the constructors in Section 5. Their outputs go in topic/target/constraints as appropriate, not content, whose spec type remains STRING.

**rule_category_cuisine_value** (v19/rule/category/cuisine-value; rule governing cuisine_arab)

STRING cuisine class; cuisine_indian is a cuisine filter, not the location India.

**rule_category_descriptive_value** (v19/rule/category/descriptive-value; rule governing constitutional_ai)

STRING modifier/domain label; never a free-form proposition. dom_sgi needs its intended referent established before semantically dependent use.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; candidate)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing bread)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_format_value** (v19/rule/category/format-value; candidate)

STRING format. format_email is layout, not the action send_email.

**rule_category_locale_value** (v19/rule/category/locale-value; rule governing locale_de)

STRING locale. “English” alone does not always mean locale_en_us; preserve ambiguity.

**rule_category_location_name** (v19/rule/category/location-name; rule governing new_york_university)

STRING location descriptor. A `table` surface is not the generated artifact category art_table.

**rule_category_recipient_value** (v19/rule/category/recipient-value; rule governing role_professor)

STRING roles or explicit named recipients. A role is not an exact person's identity. Keep an explicit name where substituting a role loses information.

**rule_category_tone_value** (v19/rule/category/tone-value; candidate)

STRING register. tone_urgent describes urgency, not a concrete deadline.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_classical_piano)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_category_transformation_value** (v19/rule/category/transformation-value; rule governing transform_remove_br)

TERM-described transformation. Pass it through constraints; no ungoverned transformations attribute.

**rule_composites_general** (v19/rule/composites-general; rule governing transform_remove_br)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_operations_general** (v19/rule/operations-general; rule governing send_message)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_supplemental_general** (v19/rule/supplemental-general; rule governing art_itinerary)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; candidate)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- press_key | operation | (target: REF[STRING], key: STRING) -> void | Press a specific keyboard key on the designated UI element. target must identify an interactive web element. | not: type_text (which enters text character strings into an input field) | aliases: press_enter, send_keys, key_press, hit_key  ⟵ candidate
- apply_filters | operation | operation-vocabulary | (target: REF[STRING], criteria: LIST[TERM]) -> void | Apply the listed filters to an existing UI. Not repeated evidence of a search already represented.  ⟵ candidate
- modify_code | operation | operation-vocabulary | (target: STRING / ATOM[platform_label], file: STRING, revision: TERM, method?: STRING) -> void | Apply the structured change to the indicated code. A method name alone does not specify the change. | aliases: fix, reduce, optimize  ⟵ candidate
- search_travel | operation | operation-vocabulary | (target: STRING, constraints?: LIST[TERM], location?: STRING / ATOM[country]) -> LIST[REF[STRING]] | Query travel options meeting supplied constraints. Does not book them.  ⟵ candidate
- select_filter | operation | operation-vocabulary | (target: REF[STRING], criterion: TERM) -> void | Apply one specified filter in an existing UI. Do not add this operation when the source only requests filtered search.  ⟵ candidate
- send_email | operation | operation-vocabulary | (recipient: STRING, content: STRING, tone?: STRING) -> void | Send supplied exact message content to the identified recipient. A requested message purpose is not already a composed message. | aliases: email  ⟵ candidate
- send_message | operation | operation-vocabulary | (recipient: STRING, content: STRING, tone?: STRING) -> void | Send supplied exact content through the specified message context. If the channel is unresolved, report it. | aliases: text  ⟵ candidate
- type_text | operation | operation-vocabulary | (target: REF[STRING], text: STRING) -> void | Type text into a designated input field, text box, or editable area. target must identify an editable element. | aliases: enter_text, input_text, input_string  ⟵ candidate
- wait | operation | operation-vocabulary | (duration?: NUMBER) -> void | Pause execution for a duration or cycle. duration in seconds or ticks. | aliases: idle, pause  ⟵ candidate

### speech acts

- apologize | speech_act | UTTER apologize(target?: CLAIM / TERM) | Speech act expressing apology or regret for an outcome or target. | not: decline (which is refusing) | aliases: apologize, apology, sorry  ⟵ candidate
- ask | speech_act | operation-vocabulary | UTTER ask(target: TERM, or a sufficiently precise topic: STRING / TERM) | Request information/advice; not an assertion of an answer. | aliases: ask, how should  ⟵ candidate
- confirm | speech_act | operation-vocabulary | UTTER confirm(target: CLAIM) | Confirm the proposition; its evidence/status remains explicit.  ⟵ candidate
- correct | speech_act | operation-vocabulary | UTTER correct(target: CLAIM) | Offer corrected content. Actual supersession requires the Conversation revision rules.  ⟵ candidate
- decline | speech_act | operation-vocabulary | UTTER decline(target: TERM) | Decline the represented request/proposal; not negate every proposition within it.  ⟵ candidate
- express_interest | speech_act | operation-vocabulary | UTTER express_interest(target: STRING / TERM) | Speech act expressing conversational interest or engagement in a topic. speech act in dialogic traces. | aliases: show_interest  ⟵ candidate
- inform | speech_act | operation-vocabulary | UTTER inform(target: CLAIM) | Present the proposition; preserve its holder/status.  ⟵ candidate
- offer | speech_act | operation-vocabulary | UTTER offer(target: STRING / TERM) | Speech act offering assistance, service, or items to a conversation partner. speech act in dialogic traces. | aliases: proffer  ⟵ candidate
- propose | speech_act | operation-vocabulary | UTTER propose(target: TERM) | Suggest an action/idea; does not record it as performed.  ⟵ candidate
- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ dependency of obligation
- calculation | constructor | TERM calculation(inputs: LIST[TERM], operation: STRING, result?: TERM) -> TERM | Constructs a descriptive representation of an arithmetic or algorithmic calculation step with inputs, operation identifier, and optional resulting value. | not: an executed runtime action or factual claim of outcome | aliases: math_operation, compute_step  ⟵ candidate
- conjunction | constructor | TERM conjunction(items: LIST[TERM]) -> TERM | All described components apply | not: Does not imply temporal order  ⟵ candidate
- dialogue | constructor | TERM dialogue(style: STRING) -> TERM | Constructs a description of conversational dialogue adhering to a style. descriptive conversational term. | aliases: conversation_style  ⟵ candidate
- document_section | constructor | TERM document_section(title: STRING, items?: LIST[TERM]) -> TERM | Constructs a structural document section descriptor with a section title and optional content items. | not: a complete document artifact class (use art_structured_report) | aliases: section, report_section, article_section  ⟵ candidate
- duration | constructor | TERM duration(amount: NUMBER, unit: STRING) -> TERM | Requested elapsed/calendar extent | not: Word/item counts are not time  ⟵ candidate
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ candidate
- footnote | constructor | TERM footnote(function: STRING, number: NUMBER) -> TERM | Constructs a footnote reference or citation marker descriptor. document formatting descriptor. | aliases: citation_note  ⟵ candidate
- include | constructor | TERM include(item: STRING / TERM) -> TERM | Require the identified content/item | not: Not permission to invent an instance in a recorded trace  ⟵ candidate
- negation | constructor | TERM negation(target: TERM) -> TERM | Constructs a descriptive semantic negation of a target descriptive proposition or condition term. | not: Check's runtime Boolean operator NOT or a speech-act decline | aliases: not, does not, negation, absence of  ⟵ candidate
- obligation | constructor | TERM obligation(actor: STRING / TERM, activity: TERM) -> TERM | Constructs a deontic obligation description requiring an actor to perform an activity. actor and activity specified. | aliases: duty, mandatory_activity  ⟵ candidate
- policy_document | constructor | TERM policy_document(title: STRING, audience?: STRING, constraints?: LIST[TERM]) -> TERM | Constructs a structured policy document representation. used for formal organizational guidelines. | aliases: policy_spec  ⟵ candidate
- policy_revision_request | constructor | TERM policy_revision_request(original_policy: CLAIM / TERM, inclusions: LIST[TERM]) -> TERM | Constructs a request to revise an existing policy with additional clauses. descriptive revision term. | aliases: policy_amendment  ⟵ candidate
- remove_literal | constructor | TERM remove_literal(text: STRING) -> TERM | Remove occurrences of that exact literal in the stated artifact | not: Not remove similar markup unless specified  ⟵ dependency of transform_remove_br
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ dependency of constraint_comprehensive
- software_version | constructor | TERM software_version(branch?: STRING, project: STRING / ATOM[platform_label], version?: STRING) -> TERM | Constructs a descriptor for a software project version, release tag, or branch identifier. | not: an installed runtime package environment | aliases: repo_branch, git_branch, project_version  ⟵ candidate
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ dependency of considered
- substitute | constructor | TERM substitute(original: STRING / TERM, replacement: STRING / TERM, purpose?: STRING / TERM) -> TERM | Constructs a descriptive representation of substituting an original entity or ingredient with a replacement alternative. | not: an executed change or runtime revision (use LINK revises) | aliases: substitute, substitution, alternative for, replace with  ⟵ candidate
- temporal_context | constructor | TERM temporal_context(activity: STRING / TERM, period?: STRING) -> TERM | Constructs a temporal or situational context descriptor specifying an ongoing process, evaluation phase, or historical timeframe. | not: time_point (a specific timestamp/date) or duration (an elapsed numerical duration) | aliases: while, during, in past relationships, timeframe  ⟵ candidate
- time_point | constructor | TERM time_point(date?: STRING, time?: STRING, timezone?: STRING) -> TERM | Constructs a structured representation of a specific calendar date, time of day, or scheduled timestamp. | not: an elapsed time duration (use duration) | aliases: timestamp, datetime, scheduled_time  ⟵ candidate
- vehicle_allowance | constructor | TERM vehicle_allowance(roles: STRING, types: LIST[STRING]) -> TERM | Constructs a specification of permitted vehicle types for defined employee roles. specifies vehicle permissions. | aliases: vehicle_permission  ⟵ candidate
- well_wishes | constructor | TERM well_wishes(recipient?: STRING / TERM, sentiment?: STRING) -> TERM | Constructs a conversational discourse term representing well-wishes, good luck expressions, or parting encouragement. | not: a salutation greeting (use greeting) or apology (use apologize) | aliases: good_luck, best_wishes, encouragement  ⟵ candidate

### composites

- constraint_comprehensive | composite | constraint-value | TERM constraint_comprehensive() -> TERM | Must be comprehensive. | = requirement(property="comprehensive", value=TRUE)  ⟵ candidate
- constraint_exclude_flowery_language | composite | constraint-value | TERM constraint_exclude_flowery_language() -> TERM | Avoid flowery language. | = exclude(item="flowery_language")  ⟵ candidate
- content_status_update | composite | content-value | TERM content_status_update(subject: STRING) -> TERM | A request for a status update. | = activity(verb="request_update", object=$subject) | aliases: status update  ⟵ candidate
- topic_ai_earning_methods | composite | topic-value | TERM topic_ai_earning_methods() -> TERM | AI earning methods. | = subject(kind="methods", qualifier=activity(verb="earn", instrument="AI", object="income"))  ⟵ candidate
- transform_remove_br | composite | transformation-value | TERM transform_remove_br() -> TERM | Remove <br /> tags. | = remove_literal(text="<br />")  ⟵ candidate

### claim relations

- allowed_to_enter | claim_relation | CLAIM allowed_to_enter(subject: STRING / TERM, location: STRING / TERM, condition?: STRING / TERM) | Asserts that a subject is permitted access to a location or facility. permission claim. | aliases: permitted_in  ⟵ candidate
- considered | claim_relation | CLAIM considered(subject: TERM) | Asserts that an agent or speaker evaluated or entertained a specific candidate term or concept. subject is the evaluated term. | aliases: evaluated, weighed  ⟵ candidate
- enables | claim_relation | CLAIM enables(condition: TERM / CLAIM, outcome: TERM / CLAIM) | Asserts that an enabling condition or capability facilitates an outcome. enabling condition. | aliases: facilitates, allows  ⟵ candidate
- exempt_from | claim_relation | CLAIM exempt_from(subject: STRING / TERM, rule: CLAIM / TERM) | Asserts that a subject is granted exemption from a designated rule or prohibition. exemption claim. | aliases: excepted_from  ⟵ candidate
- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ core
- has_state | claim_relation | CLAIM has_state(subject: TERM, state: STRING) | Asserts that an entity is currently in a physical, thermal, or operational state. state must be a valid state descriptor string. | aliases: in_state, state_is  ⟵ candidate
- occurred_recently | claim_relation | CLAIM occurred_recently(target: CLAIM) | Asserts temporal recency of an asserted occurrence or claim. temporal recency qualifier. | aliases: recently_happened  ⟵ candidate
- ongoing | claim_relation | CLAIM ongoing(target: TERM) | Asserts that a conflict, process, or initiative is actively ongoing. temporal aspect claim. | aliases: in_progress  ⟵ candidate
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ candidate
- prohibited | claim_relation | CLAIM prohibited(subject: STRING / TERM, location: STRING / TERM, condition?: STRING / TERM) | Asserts that a subject is prohibited from a location or activity under specified conditions. deontic prohibition claim. | aliases: forbidden, banned_from  ⟵ related to obligation
- proposed_policy | claim_relation | CLAIM proposed_policy(policy: TERM, requirements: LIST[TERM]) | Asserts that a proposed policy framework comprises the specified requirement terms. policy must be a policy term. | aliases: policy_proposal  ⟵ candidate
- provides | claim_relation | CLAIM provides(actor: STRING / TERM / ATOM[platform_label], subject: STRING / TERM / ATOM[platform_label]) | Asserts that an establishment, organization, or provider supplies a specified item or service. provision claim. | aliases: supplies  ⟵ candidate
- recommended | claim_relation | CLAIM recommended(target: TERM / CLAIM) | Asserts an advisory recommendation that an activity or measure is advisable. advisory normative claim. | aliases: advisable  ⟵ candidate
- request | claim_relation | CLAIM request(target: TERM / STRING) | Represents an active communicative request or constraint state in conversation tracking. target is the requested action or topic. | aliases: user_request  ⟵ candidate
- user_preference | claim_relation | CLAIM user_preference(constraints: TERM) | Asserts a user's stated preference constraints or dietary requirements. user constraint assertion. | aliases: stated_preference  ⟵ candidate

### links

- contrast | link | LINK contrast(first: CLAIM, second: CLAIM) | Expresses rhetorical qualification, opposition, or contrast between two claims. link between claims. | aliases: qualification, however  ⟵ candidate
- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ candidate
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ candidate
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ candidate

### values

- art_itinerary | value | artifact-value | An ordered travel plan; GENERATE returns STRING, not booked travel  ⟵ candidate
- cuisine_arab | value | cuisine-value | Arab culinary cuisine style. | not: cuisine_mediterranean (broader regional category) | aliases: Arab food, Arabic food, Arab cuisine  ⟵ candidate
- constitutional_ai | value | descriptive-value | Concept of rule-based constitutional training and self-critique principles in AI alignment. | aliases: constitutional_ai  ⟵ candidate
- design_parameters | value | descriptive-value | Concept of operational and behavioral design specifications for AI systems. | aliases: design_parameters  ⟵ candidate
- unit_day | value | duration-unit-value | Day. | aliases: days  ⟵ candidate
- unit_hour | value | duration-unit-value | Hour. | aliases: hours  ⟵ candidate
- unit_month | value | duration-unit-value | Month. | aliases: months  ⟵ candidate
- unit_paragraph | value | duration-unit-value | Paragraph of text. | aliases: paragraphs, paragraph  ⟵ candidate
- unit_week | value | duration-unit-value | Week. | aliases: weeks  ⟵ candidate
- unit_year | value | duration-unit-value | Year. | aliases: years  ⟵ candidate
- bread | value | entity-name | A bread loaf or slice food object. | aliases: bread  ⟵ candidate
- grape_sauvignon_blanc | value | entity-name | Sauvignon Blanc wine grape variety. | not: other white grape varieties such as grape_chardonnay | aliases: Sauvignon Blanc, sauvignon blanc grape  ⟵ candidate
- grape_tannin | value | entity-name | Tannin powder derived from grapes for wine structure. | not: oak_chips or wood aging additives | aliases: grape tannin, tannin, wine tannin  ⟵ candidate
- resource_chiller | value | entity-name | Canonical abstract chilling resource when no particular appliance is named.  ⟵ candidate
- resource_heater | value | entity-name | Canonical abstract heating resource when no particular appliance is named.  ⟵ candidate
- resource_sink | value | entity-name | Canonical abstract washing resource when no particular sink is named.  ⟵ candidate
- sultana | value | entity-name | Dried white seedless grape food product. | not: raisin (dark dried grape) or wine_grape | aliases: sultana, sultanas, golden raisin  ⟵ candidate
- format_email | value | format-value | Email layout. | aliases: as an email  ⟵ candidate
- format_plain_text | value | format-value | Unstructured prose text. | aliases: plain text  ⟵ candidate
- locale_de | value | locale-value | German language or locale descriptor. | not: other language locales (such as locale_en_us or locale_fr) or country entity (country::DE) | aliases: German, german, Deutsch, de, de-DE  ⟵ candidate
- locale_en_us | value | locale-value | US English. | aliases: english, en-us  ⟵ candidate
- locale_fr | value | locale-value | French. | aliases: french  ⟵ candidate
- locale_hi_en | value | locale-value | Hinglish (Hindi-English mix). | aliases: hinglish  ⟵ candidate
- locale_zh | value | locale-value | Chinese language locale (Simplified and Traditional Chinese). | not: a specific geographical region or nationality (use location-name) | aliases: chinese, zh, zh-cn, zh-tw, mandarin  ⟵ candidate
- eastern_cape | value | location-name | Eastern Cape region.  ⟵ candidate
- liberal_onsen | value | location-name | Traditional Japanese establishment or hospitality venue: liberal_onsen. | aliases: liberal_onsen  ⟵ candidate
- new_york_university | value | location-name | New York University institution or campus grounds. | aliases: nyu  ⟵ candidate
- onsen | value | location-name | Traditional Japanese establishment or hospitality venue: onsen. | aliases: onsen  ⟵ candidate
- russia | value | location-name | Geopolitical nation or continental region: russia. | aliases: russia  ⟵ candidate
- ukraine | value | location-name | Geopolitical nation or continental region: ukraine. | aliases: ukraine  ⟵ candidate
- foreigners | value | recipient-value | Social, demographic, or institutional group: foreigners. | aliases: foreigners  ⟵ candidate
- role_adults | value | recipient-value | Adult participant group in family, event, or travel context. | not: role_kids (children participant group) or role_user (the specific conversational user) | aliases: adults, adult, grown-ups  ⟵ candidate
- role_colleague | value | recipient-value | A coworker of the user. | aliases: my colleague, coworker  ⟵ candidate
- role_daughter | value | recipient-value | Daughter participant role in family or travel context. | not: role_sister, role_mother, or generic role_kids | aliases: daughter, my daughter  ⟵ candidate
- role_professor | value | recipient-value | The user's professor/instructor. | aliases: my professor, teacher  ⟵ candidate
- daytime | value | time-of-day-value | The period of natural daylight between sunrise and sunset in the diurnal cycle. | not: unit_day (a 24-hour elapsed duration unit) or clock time timestamps | aliases: daytime, day, day time, daylight hours  ⟵ candidate
- nighttime | value | time-of-day-value | The period of darkness between sunset and sunrise in the diurnal cycle. | not: night_stand (a piece of furniture) or clock time timestamps | aliases: nighttime, night, night time, darkness  ⟵ candidate
- topic_classical_piano | value | topic-value | Classical piano.  ⟵ candidate
- topic_current_events | value | topic-value | Current news, geopolitical events, and ongoing international developments. | aliases: current_events, news  ⟵ candidate
- topic_jazz_piano | value | topic-value | Jazz piano.  ⟵ candidate
