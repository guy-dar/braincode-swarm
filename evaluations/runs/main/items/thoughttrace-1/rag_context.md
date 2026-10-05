# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 30 needs (decomposition: llm), 169 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | speech_act | t1:s1 | greet the assistant | `role_agent`*, `greeting`*, `offer`, `acknowledge`, `apologize`, `propose`, `respond`, `inform`, `express_interest`, `ask`, `correct`, `propose_menu` |
| n2 | action | t1:s2 | request assistance with planning and organization | `propose`, `offer_help`, `request`*, `offer`, `decline`, `ask`, `provides`, `propose_menu`, `entity_assembly_tips`, `calculation`, `policy_document`, `works_best` |
| n3 | action | t1:s3 | categorize best methods for staying organized while writing a story | `style_narrative`, `rule_category_event_value`, `sequence`, `format_structured_report`, `temporal_context`*, `decision`, `rule_category_style_value`, `propose`, `modify_code`, `respond`, `art_story`, `slice` |
| n4 | object | t1:s3 | story planning and organization framework | `style_narrative`, `art_story`, `entity_recipes`, `entity_grocery_list`, `entity_assembly_tips`, `art_plan`, `format_structured_report`, `rule_category_event_value`, `entity_order_vs_assemble_plan`, `art_structured_report`, `rule_category_style_value`, `entity_appetizers` |
| n5 | object | t1:s4 | fanfiction → `genre_label::<key>` | `art_story`, `style_narrative`, `art_plan`, `character`, `art_short_text`, `art_character_profile`, `resource_chiller`, `art_structured_report`, `aesthetic`, `resource_heater`, `art_technical_explanation`, `topic_baldurs_gate_3` |
| n6 | claim | t1:s5 | organization will help realize the author's vision | `created_by`, `art_plan`, `art_story`, `designed_to_be`, `art_structured_report`, `style_narrative`, `propose`, `target`, `enables`, `ongoing`, `decision`, `involves` |
| n7 | speech_act | t2:s2, t2:s3 | greet the user and accept the request | `greeting`*, `request`*, `acknowledge`, `offer`, `role_user`, `inform`, `respond`, `propose`, `decline`, `express_interest`, `correct`, `confirm` |
| n8 | action | t2:s1, t2:s3, t2:s4 | present a comprehensive organization guide for fanfiction writing | `pen`, `gift`*, `aesthetic`, `art_structured_report`, `style_narrative`, `art_story`, `character`, `genre_label`, `include`, `art_character_profile`, `art_plan`, `inform` |
| n9 | action | t2:s7, t2:s8, t2:s9, t2:s10, t2:s11, t2:s12, t2:s13 | create a story bible covering summary, themes, tone, audience, and length | `style_narrative`, `art_story`, `document_section`, `format_plain_text`, `footnote`, `format_structured_report`, `rule_category_style_value`, `art_structured_report`, `constraint_exclude_liberation_theme`, `character`, `audience_targeting`, `format_newsletter` |
| n10 | action | t2:s16, t2:s17, t2:s18, t2:s19, t2:s20, t2:s21, t2:s22, t2:s23, t2:s24 | create character profiles detailing roles, canon reinterpretations, traits, motivations, and arcs | `character`*, `character_trait`, `art_character_profile`, `rule_category_character_property_value`, `char_female`, `constraint_include_character_attribute_list`, `role`*, `interpersonal_stance`, `style_narrative`, `rule_category_style_value`, `char_2000s_anime_style`, `art_story` |
| n11 | action | t2:s27, t2:s28, t2:s30, t2:s31, t2:s32, t2:s33 | structure worldbuilding, setting, timeline, and canon divergences | `aesthetic`, `class_temple`, `art_structured_report`, `config_setting`, `spatial_constraint`, `time_horizon`, `location_spec`, `rule_structural_constructs`, `word_blend`, `obligation`, `duration`, `rule_attributes_and_generate` |
| n12 | action | t2:s36, t2:s37, t2:s40, t2:s41, t2:s42, t2:s43, t2:s44, t2:s45, t2:s46, t2:s47, t2:s48 | build a three-level narrative structure for acts, character arcs, and chapters | `style_narrative`*, `character`*, `art_story`, `interpersonal_stance`, `document_section`, `art_structured_report`, `sequence`, `rule_category_style_value`, `format_structured_report`, `art_plan`, `art_short_text`, `art_character_profile` |
| n13 | action | t2:s51, t2:s52, t2:s53, t2:s54, t2:s55 | track main plots, subplots, and unresolved story threads across chapters | `performance_tracking`, `style_narrative`, `slice`, `song`*, `sequence`, `document_section`, `format_structured_report`, `art_structured_report`, `rule_category_style_value`, `unit_paragraph`, `art_story`, `send_message` |
| n14 | object | t2:s61, t2:s63 | Notion → `platform_label::<key>` | `beliefs`, `activity`, `resource_chiller`, `subject`, `resource_sink`, `inform`, `art_technical_explanation`, `resource_heater`, `reason_for`, `textbook`, `chill`, `chair` |
| n15 | object | t2:s61 | Obsidian → `platform_label::<key>` | `art_structured_report`, `art_story`, `class_temple`, `aesthetic`, `art_plan`, `resource_chiller`, `topic_jazz_piano`, `art_itinerary`, `resource_sink`, `candle`, `art_short_text`, `constraint_exclude_liberation_theme` |
| n16 | object | t2:s62 | Google Docs → `platform_label::<key>` | `textbook`, `path_gcloud_pubsub_subscription_py`, `format_newsletter`, `art_structured_report`, `resource_chiller`, `resource_sink`, `format_pdf`, `role_professor`, `chill`, `locale_en_gb`, `chair`, `policy_document` |
| n17 | object | t2:s63 | Trello → `platform_label::<key>` | `chill`, `topic_baldurs_gate_3`, `locale_fr`, `tone_urgent`, `resource_chiller`, `on`, `style_catchy`, `resource_sink`, `right_of`, `in_front_of`, `textbook`, `pen` |
| n18 | object | t2:s64 | Scrivener → `platform_label::<key>` | `chill`, `resource_chiller`, `resource_sink`, `textbook`, `pencil`, `conjunction`, `role_professor`, `sequence`, `pen`, `locale_fr`, `decision`, `chair` |
| n19 | action | t2:s68, t2:s69, t2:s70, t2:s71 | establish a pre-writing, writing, and post-writing routine | `propose`, `pen`, `pencil`, `sequence`, `format_structured_report`, `decision`, `style_narrative`, `tone_casual`, `format_newsletter`, `topic_school_work_routine`, `rule_category_style_value`, `obligation` |
| n20 | speech_act | t2:s74 | ask user to specify the fandom and initial ideas for customized templates | `propose_menu`, `ask`*, `has_style`, `art_structured_report`, `propose`, `art_character_profile`, `include`, `inform`, `respond`, `rule_category_descriptive_value`, `art_plan`, `style_technical` |
| n21 | speech_act | t3:s1, t3:s2, t3:s3 | thank the assistant and express appreciation for the guide | `role_agent`*, `acknowledge`, `offer`, `propose`, `role_professor`, `role_colleague`, `inform`, `recommended`, `respond`, `express_interest`, `role_manager`, `ask` |
| n22 | action | t4:s4, t4:s5, t4:s6, t4:s7, t4:s8, t4:s9 | give advice on balancing planning with actual writing, flexibility, and pacing | `propose`, `decision`, `performance_tracking`, `art_plan`, `propose_menu`, `works_best`, `calculation`, `walk_backward`, `art_structured_report`, `ongoing`, `format_structured_report`, `prep_time` |
| n23 | speech_act | t4:s12, t4:s13, t4:s14, t4:s15, t4:s16, t4:s17 | offer ongoing support for character sheets, chapter outlines, scene unblocking, and proofreading | `offer`*, `character`*, `ongoing`*, `propose`, `art_short_text`, `respond`, `correct`, `art_structured_report`, `document_section`, `include`, `inform`, `exclude` |
| n24 | speech_act | t5:s1 | ask if the assistant can help overcome writer's block during writing | `role_agent`*, `propose`, `respond`, `ask`*, `offer_help`, `pen`, `pencil`, `exclude`, `offer`, `role_colleague`, `example_e_preserve_exact_wording_through_generation_and_sending`, `art_short_text` |
| n25 | action | t5:s2 | generate ideas to bridge planned story points when stuck | `propose`, `art_story`, `rule_category_event_value`, `style_narrative`, `sequence`, `art_plan`, `propose_menu`, `entity_assembly_tips`, `time_point`, `calculation`, `art_structured_report`, `obligation` |
| n26 | speech_act | t6:s1, t6:s2 | confirm ability to help with writer's block | `confirm`*, `block_evaluation`, `respond`, `propose`, `exclude`, `pen`, `topic_baldurs_gate_3`, `ask`, `inform`, `correct`, `include`, `type_text` |
| n27 | action | t6:s7, t6:s8, t6:s9, t6:s11, t6:s12, t6:s13, t6:s15, t6:s16, t6:s17 | propose narrative pathways, transitional scenes, and character psychology analysis to unblock writing | `character`*, `style_narrative`*, `propose`*, `art_story`, `art_character_profile`, `character_trait`, `unit_character`*, `aesthetic`, `dialogue`, `art_short_text`, `constraint_exclude_liberation_theme`, `obligation` |
| n28 | action | t6:s19, t6:s20, t6:s21, t6:s22, t6:s24 | instruct user to provide current story status, intended progression, and specific obstacle | `propose`, `style_narrative`, `art_story`, `provides`*, `designed_to_be`, `medical_condition`, `propose_menu`, `include`, `decision`, `rule_category_event_value`, `rule_category_style_value`, `regression_case` |
| n29 | speech_act | t7:s1, t7:s2 | thank the assistant and state intention to return when help is needed | `role_agent`*, `offer`, `acknowledge`, `apologize`, `decline`, `ask`, `offer_help`, `inform`, `propose`, `role_support_team`, `confirm`, `express_interest` |
| n30 | speech_act | t8:s1, t8:s2, t8:s9, t8:s11 | welcome future return and wish good luck with the fanfiction | `well_wishes`*, `time_horizon`*, `art_story`, `art_itinerary`, `inform`, `style_narrative`, `apologize`, `propose`, `acknowledge`, `art_character_profile`, `ryokan`, `aesthetic` |

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

- provides.actor → platform_label
- provides.subject → platform_label
- modify_code.target → platform_label
- config_setting.value → platform_label
- activity.object → object_label, food_label, animal_label
- activity.location → country
- activity.instrument → object_label, platform_label
- subject.qualifier → platform_label
- subject.location → country
- chill.destination → object_label
- regression_case.framework → platform_label
- failure.system → platform_label

## Retrieved records

### Shared rules that govern the records below (full text)

**rule_lexical_groups** (v19/rule/lexical-groups; rule governing platform_label)

Section 3.1 defines value groups: `group::key` values of type ATOM[group]. Open groups admit any key of their form (examples are not whitelists); standard groups admit the codes of their bundled standard (ISO 3166-1 alpha-2 for country, ISO 4217 for currency). Leaf values are never glossary entries. Consumer signatures alone decide where a group may appear. Retired bare symbols are invalid.

**rule_reading_guide** (v19/rule/reading-guide; core)

The spec governs syntax/types; this glossary defines vocabulary. Signature notation: ? optional, A / B explicit alternatives, void no result. Omitted optional arguments are unspecified. Value entries are category-refined STRING primitives; complex meanings require composition. Aliases are contextual hints, not unconditional equivalences. Report ambiguity. IDs use v19/<category>/<symbol>, v19/support/<symbol> or v19/composite/<symbol>. Statuses apply to this candidate: Retained preserves meaning; Adapted uses the stated contract; Composite requires TERM (bare STRING deprecated); Structural is syntax/argument vocabulary; Needs clarification is unusable until resolved; Deprecated is historical; Accepted is usable within this candidate.

**rule_recording_signatures** (v19/rule/recording-signatures; rule governing send_email)

RECORD ACTION uses the operation signature with REF[STRING] → TERM and LIST[REF[STRING]] → LIST[TERM]; other types/categories stay unchanged. Return EVENT, never the runtime result. Record actual outputs as attributed CLAIMs. Do not infer missing resources.

**rule_speech_acts_general** (v19/rule/speech-acts-general; rule governing offer)

UTTER-only, void, with the spec's speech attributes and LIST[TERM] constraints. No result binding. Literal content cannot replace required semantic arguments for structured coverage.

**rule_structural_constructs** (v19/rule/structural-constructs; candidate)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; rule governing propose_menu)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_attributes_and_generate** (v19/rule/attributes-and-generate; candidate)

Attribute entries name arguments; legality/types come from each operation, not global membership. GENERATE uses the spec's core fields; retained artifact profiles return STRING. Numeric/list results need explicit profiles. Legacy itinerary fields expand to TERM constraints: duration/duration_unit → duration(amount,unit); stop_min_per_day/stop_requirement → minimum_per_period(class,count,period=unit_day), never an inferred temple class; max_walk_duration/unit → maximum_between_stops(activity="walk",amount,unit). No legacy shorthand is enabled. Old events/character_properties/transformations become explicitly scoped TERM constraints. Message purpose is TERM, not send_email.content: GENERATE exact STRING content, then send. Report opaque fallback separately.

**rule_category_artifact_value** (v19/rule/category/artifact-value; rule governing art_story)

STRING artifact class for GENERATE.target. art_story says what kind of artifact to produce, not what occurs in its plot.

**rule_category_character_property_value** (v19/rule/category/character-property-value; candidate)

TERM-described trait/style. Use constraints and explicit inclusion/scope; do not use an ungoverned character_properties attribute.

**rule_category_code_value** (v19/rule/category/code-value; rule governing path_gcloud_pubsub_subscription_py)

path_/sym_ remain STRING identities; migrated chg_/assert_ are TERM constructors. Do not recover an exact file path by guessing from underscores.

**rule_category_constraint_value** (v19/rule/category/constraint-value; rule governing constraint_exclude_liberation_theme)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_content_value** (v19/rule/category/content-value; rule governing content_status_update)

Existing compounds become the constructors in Section 5. Their outputs go in topic/target/constraints as appropriate, not content, whose spec type remains STRING.

**rule_category_descriptive_value** (v19/rule/category/descriptive-value; candidate)

STRING modifier/domain label; never a free-form proposition. dom_sgi needs its intended referent established before semantically dependent use.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; rule governing unit_character)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing entity_assembly_tips)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_event_value** (v19/rule/category/event-value; candidate)

TERM-described narrative event, not a recorded EVENT. Require inclusion explicitly when generating a story.

**rule_category_format_value** (v19/rule/category/format-value; rule governing format_structured_report)

STRING format. format_email is layout, not the action send_email.

**rule_category_locale_value** (v19/rule/category/locale-value; rule governing locale_en_gb)

STRING locale. “English” alone does not always mean locale_en_us; preserve ambiguity.

**rule_category_location_name** (v19/rule/category/location-name; rule governing ryokan)

STRING location descriptor. A `table` surface is not the generated artifact category art_table.

**rule_category_recipient_value** (v19/rule/category/recipient-value; rule governing role_agent)

STRING roles or explicit named recipients. A role is not an exact person's identity. Keep an explicit name where substituting a role loses information.

**rule_category_semantic_category_value** (v19/rule/category/semantic-category-value; rule governing class_temple)

STRING class label used by typed constraints. class_temple describes a class, not an acquired physical temple reference.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing on)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_style_value** (v19/rule/category/style-value; candidate)

STRING production style. style_narrative does not establish that described events occurred.

**rule_category_tone_value** (v19/rule/category/tone-value; rule governing tone_urgent)

STRING register. tone_urgent describes urgency, not a concrete deadline.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_baldurs_gate_3)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_composites_general** (v19/rule/composites-general; rule governing constraint_exclude_liberation_theme)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_examples_general** (v19/rule/examples-general; rule governing example_e_preserve_exact_wording_through_generation_and_sending)

Examples use this glossary's contracts. They have not been verified by an implemented BrainCode parser.

**rule_operations_general** (v19/rule/operations-general; rule governing send_email)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_supplemental_general** (v19/rule/supplemental-general; rule governing art_itinerary)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; rule governing greeting)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- chill | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Chill using the stated resource; same identity.  ⟵ candidate
- modify_code | operation | operation-vocabulary | (target: STRING / ATOM[platform_label], file: STRING, revision: TERM, method?: STRING) -> void | Apply the structured change to the indicated code. A method name alone does not specify the change. | aliases: fix, reduce, optimize  ⟵ candidate
- send_email | operation | operation-vocabulary | (recipient: STRING, content: STRING, tone?: STRING) -> void | Send supplied exact message content to the identified recipient. A requested message purpose is not already a composed message. | aliases: email  ⟵ candidate
- send_message | operation | operation-vocabulary | (recipient: STRING, content: STRING, tone?: STRING) -> void | Send supplied exact content through the specified message context. If the channel is unresolved, report it. | aliases: text  ⟵ candidate
- slice | operation | operation-vocabulary | (target: REF[STRING] / TERM) -> REF[STRING] | Slice the selected material or described term, preserving its tracked aggregate identity. | aliases: chop, cut  ⟵ candidate
- type_text | operation | operation-vocabulary | (target: REF[STRING], text: STRING) -> void | Type text into a designated input field, text box, or editable area. target must identify an editable element. | aliases: enter_text, input_text, input_string  ⟵ candidate
- walk_backward | operation | operation-vocabulary | (modifier?: STRING) -> void | Walk backward. Optional modifier can specify the degree or minor distance of movement. | not: walk (which moves forward toward a destination) | aliases: move backward, step back  ⟵ candidate

### speech acts

- apologize | speech_act | UTTER apologize(target?: CLAIM / TERM) | Speech act expressing apology or regret for an outcome or target. | not: decline (which is refusing) | aliases: apologize, apology, sorry  ⟵ candidate
- acknowledge | speech_act | operation-vocabulary | UTTER acknowledge(target: CLAIM / TERM) | Acknowledge receipt/awareness; does not imply agreement.  ⟵ candidate
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

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ candidate
- aesthetic | constructor | TERM aesthetic(period: STRING, style: STRING) -> TERM | A stylistic description with an explicit period | not: Not a character's age or production date  ⟵ candidate
- audience_targeting | constructor | TERM audience_targeting(criteria: LIST[STRING] / LIST[TERM], audience?: STRING / TERM) -> TERM | Constructs a descriptive representation of audience targeting criteria such as demographics, geography, or interests. | not: an individual user constraint or character trait | aliases: target_audience, audience_criteria, ad_targeting  ⟵ candidate
- block_evaluation | constructor | TERM block_evaluation(block: STRING / TERM, maturity?: STRING, potential?: STRING, quality?: STRING, rank?: NUMBER, traps?: STRING) -> TERM | Constructs a structured evaluation, categorization, or ranking descriptor for a geological exploration block. | not: an external execution action or generic list sorting operation (use sort) | aliases: block assessment, block ranking, block rating, block categorization  ⟵ candidate
- calculation | constructor | TERM calculation(inputs: LIST[TERM], operation: STRING, result?: TERM) -> TERM | Constructs a descriptive representation of an arithmetic or algorithmic calculation step with inputs, operation identifier, and optional resulting value. | not: an executed runtime action or factual claim of outcome | aliases: math_operation, compute_step  ⟵ candidate
- character | constructor | TERM character(name: STRING, series?: STRING) -> TERM | Constructs a descriptive representation of a fictional or narrative character. name specifies the character identifier. | aliases: fictional_character  ⟵ candidate
- character_trait | constructor | TERM character_trait(property: STRING, value: STRING / NUMBER) -> TERM | A character attribute | not: Not a claim about a real person  ⟵ candidate
- config_setting | constructor | TERM config_setting(option: STRING, section: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Constructs a structured representation of a configuration key-value setting within an identified section. | not: an active runtime configuration state or environment setting | aliases: ini_setting, config_option, configuration_setting  ⟵ candidate
- conjunction | constructor | TERM conjunction(items: LIST[TERM]) -> TERM | All described components apply | not: Does not imply temporal order  ⟵ candidate
- decision | constructor | TERM decision(activity: TERM) -> TERM | A decision whose content is the described activity | not: Not proof it was carried out  ⟵ candidate
- dialogue | constructor | TERM dialogue(style: STRING) -> TERM | Constructs a description of conversational dialogue adhering to a style. descriptive conversational term. | aliases: conversation_style  ⟵ candidate
- document_section | constructor | TERM document_section(title: STRING, items?: LIST[TERM]) -> TERM | Constructs a structural document section descriptor with a section title and optional content items. | not: a complete document artifact class (use art_structured_report) | aliases: section, report_section, article_section  ⟵ candidate
- duration | constructor | TERM duration(amount: NUMBER, unit: STRING) -> TERM | Requested elapsed/calendar extent | not: Word/item counts are not time  ⟵ candidate
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ candidate
- footnote | constructor | TERM footnote(function: STRING, number: NUMBER) -> TERM | Constructs a footnote reference or citation marker descriptor. document formatting descriptor. | aliases: citation_note  ⟵ candidate
- greeting | constructor | TERM greeting(recipient: STRING) -> TERM | Constructs a conversational salutation greeting descriptor. conversational discourse term. | aliases: salutation  ⟵ candidate
- include | constructor | TERM include(item: STRING / TERM) -> TERM | Require the identified content/item | not: Not permission to invent an instance in a recorded trace  ⟵ candidate
- interpersonal_stance | constructor | TERM interpersonal_stance(actor: STRING / TERM, stance: STRING, target?: STRING / TERM) -> TERM | Constructs a descriptive representation of an actor's interpersonal stance, level of commitment, or relational engagement toward a partner. | not: character_trait (fictional characters) or attitude (an asserted claim relation) | aliases: relational_commitment, interpersonal_behavior, relationship_stance  ⟵ candidate
- location_spec | constructor | TERM location_spec(address?: STRING, area?: STRING, city?: STRING, state?: STRING) -> TERM | Constructs a structured geographical location specification with regional and administrative qualifiers. | not: a fixed atomic location descriptor in location-name or a spatial relation | aliases: location_details, geographic_location  ⟵ candidate
- medical_condition | constructor | TERM medical_condition(condition: STRING, patient: STRING / TERM, severity?: STRING) -> TERM | Constructs a descriptive representation of a medical condition, pathology, or symptom profile. | not: an asserted factual attribution (use attribute_claim) or executed treatment | aliases: condition, symptom, pathology, diagnosis  ⟵ candidate
- obligation | constructor | TERM obligation(actor: STRING / TERM, activity: TERM) -> TERM | Constructs a deontic obligation description requiring an actor to perform an activity. actor and activity specified. | aliases: duty, mandatory_activity  ⟵ candidate
- offer_help | constructor | TERM offer_help() -> TERM | Constructs a conversational proffer of assistance or support. conversational discourse term. | aliases: help_offer  ⟵ candidate
- performance_tracking | constructor | TERM performance_tracking(adjustment?: STRING / TERM, target: STRING / TERM) -> TERM | Constructs a descriptive representation of monitoring performance metrics or campaign results with an optional strategy adjustment. | not: a runtime metric observation or software test run | aliases: track_results, monitor_performance, campaign_tracking  ⟵ candidate
- policy_document | constructor | TERM policy_document(title: STRING, audience?: STRING, constraints?: LIST[TERM]) -> TERM | Constructs a structured policy document representation. used for formal organizational guidelines. | aliases: policy_spec  ⟵ candidate
- regression_case | constructor | TERM regression_case(framework: STRING / ATOM[platform_label], modifier: STRING, relation: STRING) -> TERM | A regression scenario specifying affected framework, condition and relation | not: Does not invent a passing test or exact implementation  ⟵ candidate
- sequence | constructor | TERM sequence(items: LIST[TERM]) -> TERM | Ordered described activities/content | not: Not unordered conjunction  ⟵ candidate
- spatial_constraint | constructor | TERM spatial_constraint(relation: STRING, object: TERM, reference: TERM) -> TERM | Constructs a descriptive spatial constraint between an object and a reference landmark. relation must specify a spatial configuration. | aliases: spatial_relation  ⟵ candidate
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ candidate
- temporal_context | constructor | TERM temporal_context(activity: STRING / TERM, period?: STRING) -> TERM | Constructs a temporal or situational context descriptor specifying an ongoing process, evaluation phase, or historical timeframe. | not: time_point (a specific timestamp/date) or duration (an elapsed numerical duration) | aliases: while, during, in past relationships, timeframe  ⟵ candidate
- time_horizon | constructor | TERM time_horizon(horizon: STRING) -> TERM | Constructs a temporal horizon or prospective timeframe descriptor indicating relative temporal distance into the future. | not: a specific calendar timestamp (use time_point) or an elapsed numerical duration (use duration). | aliases: future, future timeframe, time horizon, far off in the future, far future  ⟵ candidate
- time_point | constructor | TERM time_point(date?: STRING, time?: STRING, timezone?: STRING) -> TERM | Constructs a structured representation of a specific calendar date, time of day, or scheduled timestamp. | not: an elapsed time duration (use duration) | aliases: timestamp, datetime, scheduled_time  ⟵ candidate
- well_wishes | constructor | TERM well_wishes(recipient?: STRING / TERM, sentiment?: STRING) -> TERM | Constructs a conversational discourse term representing well-wishes, good luck expressions, or parting encouragement. | not: a salutation greeting (use greeting) or apology (use apologize) | aliases: good_luck, best_wishes, encouragement  ⟵ candidate
- word_blend | constructor | TERM word_blend(base: STRING / TERM, replacement: STRING / TERM, result_name?: STRING) -> TERM | Constructs a morphological blend or portmanteau from base and replacement terms. descriptive lexical structure. | aliases: portmanteau  ⟵ candidate

### composites

- char_2000s_anime_style | composite | character-property-value | TERM char_2000s_anime_style() -> TERM | 2000s anime style. | = aesthetic(period="2000s", style="anime")  ⟵ candidate
- char_female | composite | character-property-value | TERM char_female() -> TERM | Female gender. | = character_trait(property="gender", value="female") | aliases: female  ⟵ candidate
- constraint_exclude_liberation_theme | composite | constraint-value | TERM constraint_exclude_liberation_theme() -> TERM | Avoid liberation theme. | = exclude(item="liberation_theme")  ⟵ candidate
- constraint_include_character_attribute_list | composite | constraint-value | TERM constraint_include_character_attribute_list() -> TERM | Include character attributes. | = include(item="character_attribute_list")  ⟵ candidate
- content_status_update | composite | content-value | TERM content_status_update(subject: STRING) -> TERM | A request for a status update. | = activity(verb="request_update", object=$subject) | aliases: status update  ⟵ dependency of example_e_preserve_exact_wording_through_generation_and_sending
- topic_school_work_routine | composite | topic-value | TERM topic_school_work_routine() -> TERM | School and work routine. | = subject(kind="routine", qualifier=conjunction(items=[subject(kind="school"), subject(kind="work")]))  ⟵ candidate

### claim relations

- created_by | claim_relation | CLAIM created_by(subject: STRING / TERM, creator: STRING) | Asserts the developer, author, or creator of an entity or system. provenance/creator assertion. | aliases: authored_by  ⟵ candidate
- designed_to_be | claim_relation | CLAIM designed_to_be(subject: STRING / TERM, quality: STRING) | Asserts the intended design goal, alignment quality, or persona attribute of a system. design objective. | aliases: intended_to_be  ⟵ candidate
- enables | claim_relation | CLAIM enables(condition: TERM / CLAIM, outcome: TERM / CLAIM) | Asserts that an enabling condition or capability facilitates an outcome. enabling condition. | aliases: facilitates, allows  ⟵ candidate
- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ core
- has_style | claim_relation | CLAIM has_style(target: CLAIM / EVENT / TERM, value: TERM / STRING) | Asserts that an artifact, utterance, or action possesses a designated style. style qualifier. | aliases: style_is  ⟵ candidate
- involves | claim_relation | CLAIM involves(subject: CLAIM, target: TERM) | Asserts participant involvement or inclusion of an entity in an initiative or event. involvement claim. | aliases: includes_participant  ⟵ candidate
- ongoing | claim_relation | CLAIM ongoing(target: TERM) | Asserts that a conflict, process, or initiative is actively ongoing. temporal aspect claim. | aliases: in_progress  ⟵ candidate
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ dependency of enables
- prep_time | claim_relation | CLAIM prep_time(value: TERM) | Asserts an estimated preparation or assembly time duration. time requirement assertion. | aliases: preparation_duration  ⟵ candidate
- prohibited | claim_relation | CLAIM prohibited(subject: STRING / TERM, location: STRING / TERM, condition?: STRING / TERM) | Asserts that a subject is prohibited from a location or activity under specified conditions. deontic prohibition claim. | aliases: forbidden, banned_from  ⟵ related to obligation
- propose_menu | claim_relation | CLAIM propose_menu(menu: TERM) | Asserts the proposal of a comprehensive menu plan. planning proposal. | aliases: suggest_menu  ⟵ candidate
- proposed_policy | claim_relation | CLAIM proposed_policy(policy: TERM, requirements: LIST[TERM]) | Asserts that a proposed policy framework comprises the specified requirement terms. policy must be a policy term. | aliases: policy_proposal  ⟵ related to obligation
- provides | claim_relation | CLAIM provides(actor: STRING / TERM / ATOM[platform_label], subject: STRING / TERM / ATOM[platform_label]) | Asserts that an establishment, organization, or provider supplies a specified item or service. provision claim. | aliases: supplies  ⟵ candidate
- reason_for | claim_relation | CLAIM reason_for(subject: CLAIM / TERM, reason: STRING / TERM) | Asserts an explanatory reason for a policy, belief, or state of affairs. explanatory reason. | aliases: basis_for  ⟵ candidate
- recommended | claim_relation | CLAIM recommended(target: TERM / CLAIM) | Asserts an advisory recommendation that an activity or measure is advisable. advisory normative claim. | aliases: advisable  ⟵ candidate
- request | claim_relation | CLAIM request(target: TERM / STRING) | Represents an active communicative request or constraint state in conversation tracking. target is the requested action or topic. | aliases: user_request  ⟵ candidate
- role | claim_relation | CLAIM role(subject: STRING / TERM, role_type: STRING) | Asserts the functional role or capacity of an agent or entity. role assertion. | aliases: agent_role  ⟵ candidate
- works_best | claim_relation | CLAIM works_best(style: STRING, count: NUMBER, purpose: STRING) | Asserts an advisory evaluation of optimal event style and participant capacity. planning evaluation. | aliases: optimal_format  ⟵ candidate

### links

- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ core
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ core
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ candidate

### values

- art_character_profile | value | artifact-value | Descriptive character profile.  ⟵ candidate
- art_itinerary | value | artifact-value | An ordered travel plan; GENERATE returns STRING, not booked travel  ⟵ candidate
- art_plan | value | artifact-value | Actionable plan.  ⟵ candidate
- art_short_text | value | artifact-value | Short free text.  ⟵ candidate
- art_story | value | artifact-value | Narrative story.  ⟵ candidate
- art_structured_report | value | artifact-value | Headed/structured report.  ⟵ candidate
- art_technical_explanation | value | artifact-value | Technical explanation of a concept.  ⟵ candidate
- path_gcloud_pubsub_subscription_py | value | code-value | File path to the Google Cloud Pub/Sub subscription module. | aliases: gcloud_pubsub_subscription_path  ⟵ candidate
- beliefs | value | descriptive-value | Concept of cognitive beliefs, convictions, or worldviews. | aliases: beliefs  ⟵ candidate
- unit_character | value | duration-unit-value | One Unicode scalar value in the final rendered artifact; line endings are normalized to LF before counting. | aliases: characters, chars  ⟵ candidate
- unit_paragraph | value | duration-unit-value | Paragraph of text. | aliases: paragraphs, paragraph  ⟵ candidate
- candle | value | entity-name | A candle light source made of wax with a wick. | not: lamp (an electric light appliance or fixture) | aliases: candle, wax candle  ⟵ candidate
- chair | value | entity-name | A chair furniture seat with a backrest. | not: object_label::armchair (specifically an object_label::armchair with side armrests) or object_label::sofa | aliases: chair, seat  ⟵ candidate
- entity_appetizers | value | entity-name | Event planning item or menu category: entity_appetizers. | aliases: entity_appetizers  ⟵ candidate
- entity_assembly_tips | value | entity-name | Event planning item or menu category: entity_assembly_tips. | aliases: entity_assembly_tips  ⟵ candidate
- entity_grocery_list | value | entity-name | Event planning item or menu category: entity_grocery_list. | aliases: entity_grocery_list  ⟵ candidate
- entity_order_vs_assemble_plan | value | entity-name | Event planning item or menu category: entity_order_vs_assemble_plan. | aliases: entity_order_vs_assemble_plan  ⟵ candidate
- entity_recipes | value | entity-name | Event planning item or menu category: entity_recipes. | aliases: entity_recipes  ⟵ candidate
- gift | value | entity-name | A physical gift or present item to be wrapped, given, or received. | not: egift_card (an electronic gift card or digital voucher product) | aliases: gift, present, wrapped gift, package  ⟵ candidate
- pen | value | entity-name | A writing instrument. | aliases: pen  ⟵ candidate
- pencil | value | entity-name | A pencil writing instrument. | aliases: pencil  ⟵ candidate
- resource_chiller | value | entity-name | Canonical abstract chilling resource when no particular appliance is named.  ⟵ candidate
- resource_heater | value | entity-name | Canonical abstract heating resource when no particular appliance is named.  ⟵ candidate
- resource_sink | value | entity-name | Canonical abstract washing resource when no particular sink is named.  ⟵ candidate
- song | value | entity-name | A musical piece, audio track, or song entity. | not: piano (a musical instrument) or cd (a physical compact disc storage medium) | aliases: song, music track, audio track, track  ⟵ candidate
- textbook | value | entity-name | A textbook or instructional book used as an educational resource. | not: style_academic (which is a stylistic mode) or art_short_text (which is a brief generated text artifact) | aliases: textbook, book, coursebook, textbooks  ⟵ candidate
- format_email | value | format-value | Email layout. | aliases: as an email  ⟵ dependency of example_e_preserve_exact_wording_through_generation_and_sending
- format_newsletter | value | format-value | Newsletter layout. | aliases: newsletter  ⟵ candidate
- format_pdf | value | format-value | PDF document. | aliases: as a pdf  ⟵ candidate
- format_plain_text | value | format-value | Unstructured prose text. | aliases: plain text  ⟵ candidate
- format_structured_report | value | format-value | Headed structured report layout. | aliases: structured report, report  ⟵ candidate
- locale_en_gb | value | locale-value | UK English. | aliases: british english  ⟵ candidate
- locale_fr | value | locale-value | French. | aliases: french  ⟵ candidate
- ryokan | value | location-name | Traditional Japanese establishment or hospitality venue: ryokan. | aliases: ryokan  ⟵ candidate
- role_agent | value | recipient-value | The assistant. | aliases: you, the assistant  ⟵ candidate
- role_colleague | value | recipient-value | A coworker of the user. | aliases: my colleague, coworker  ⟵ candidate
- role_manager | value | recipient-value | The user's manager. | aliases: my manager, boss  ⟵ candidate
- role_professor | value | recipient-value | The user's professor/instructor. | aliases: my professor, teacher  ⟵ candidate
- role_support_team | value | recipient-value | A customer-support team. | aliases: support, customer service  ⟵ candidate
- role_user | value | recipient-value | The requesting human. | aliases: me, I  ⟵ candidate
- class_temple | value | semantic-category-value | The abstract class of temples. | aliases: temple, temples  ⟵ candidate
- in_front_of | value | spatial-relation | Positioned in front of. | aliases: in front of  ⟵ candidate
- on | value | spatial-relation | Resting atop. | aliases: on top of  ⟵ candidate
- right_of | value | spatial-relation | To the right of. | aliases: right of  ⟵ candidate
- style_catchy | value | style-value | Catchy, attention-grabbing style. | aliases: catchy  ⟵ candidate
- style_narrative | value | style-value | Story-like narrative style. | aliases: narrative, story-style  ⟵ candidate
- style_technical | value | style-value | Technical/expository style. | aliases: technical  ⟵ candidate
- tone_casual | value | tone-value | Informal register. | aliases: casually  ⟵ candidate
- tone_polite | value | tone-value | Courteous, respectful register. | aliases: politely, kindly  ⟵ dependency of example_e_preserve_exact_wording_through_generation_and_sending
- tone_urgent | value | tone-value | Conveys urgency. | aliases: urgently, ASAP  ⟵ candidate
- topic_baldurs_gate_3 | value | topic-value | Baldur's Gate 3.  ⟵ candidate
- topic_current_events | value | topic-value | Current news, geopolitical events, and ongoing international developments. | aliases: current_events, news  ⟵ candidate
- topic_jazz_piano | value | topic-value | Jazz piano.  ⟵ candidate

### attributes

- target | attribute | attribute-name | The acted-on entity or generated artifact.  ⟵ candidate

### examples

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

