# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 17 needs (decomposition: llm), 142 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | claim | t1:s1 | encountering UnboundLocalError: local variable 'seq_length' referenced before assignment | `rule_category_code_value`, `rule_category_locale_value`, `spatial_constraint`, `spatial_state`, `rule_category_semantic_category_value`, `location_spec`, `raises_exception`, `constraint_include_character_attribute_list`, `rule_attributes_and_generate`, `rule_operations_general`, `occurred_recently`, `outcome` |
| n2 | speech_act | t1:s3 | greet and report an issue with ConvBertForTokenClassification | `issue`*, `greeting`*, `format_structured_report`*, `respond`, `correct`, `acknowledge`, `send_message`, `raises_exception`, `warning`, `example_e_preserve_exact_wording_through_generation_and_sending`, `send_email`, `rule_category_format_value` |
| n3 | object | t1:s3 | ConvBertForTokenClassification model in transformers convbert module → `platform_label::<key>` | `path_sklearn_linear_model_logistic_py`, `rule_category_transformation_value`, `config_setting`, `chg_inherit_multi_class`, `duration`, `reconcile_code`, `conjunction`, `mod_mixed_case`, `resource_chiller`, `duplicate_definition`, `resource_heater`, `config_overlay` |
| n4 | action | t1:s3 | call forward method passing only input_embeds argument | `modify_code`, `example_e_preserve_exact_wording_through_generation_and_sending`, `raises_exception`, `send_email`, `hover`, `type_text`, `calculation`, `pick_up`, `request`, `code_entity`, `remove`, `cli_command` |
| n5 | object | t1:s4 | source file modeling_convbert.py line 833 | `path_numpy_core_fromnumeric_py`, `path_sklearn_linear_model_logistic_py`, `path_ipython_core_magics_basic_py`, `code_entity`*, `path_pandas_src_testing_pyx`, `rule_category_code_value`, `software_version`, `path_gcloud_pubsub_subscription_py`, `rule_category_entity_name`, `chg_modify_code`, `pull_request`, `config_overlay` |
| n6 | claim | t1:s6, t1:s7, t1:s8 | token_type_ids slicing uses seq_length variable when token_type_ids is None | `state_sliced`*, `rule_category_code_value`, `rule_category_capacity_unit_value`, `raises_exception`, `rule_category_semantic_category_value`, `rule_category_reservation_status_value`, `slice`, `validates_parameter`, `rule_category_character_property_value`, `rule_reading_guide`, `unit_character`, `sym_log_reg_scoring_path` |
| n7 | claim | t1:s10 | seq_length variable remains unassigned in execution path | `rule_category_code_value`, `path_numpy_core_fromnumeric_py`, `duration`, `path_sklearn_linear_model_logistic_py`, `rule_operations_general`, `sym_log_reg_scoring_path`, `rule_attributes_and_generate`, `constraint_include_character_attribute_list`, `rule_category_reservation_status_value`, `path_ipython_core_magics_basic_py`, `leads_to`, `path_pandas_src_testing_pyx` |
| n8 | claim | t1:s13, t1:s14, t1:s15, t1:s16, t1:s17, t1:s19 | inputs_embeds branch extracts input_shape but omits unpacking seq_length | `type_text`, `software_version`, `rule_category_code_value`, `rule_category_semantic_category_value`, `config_overlay`, `path_numpy_core_fromnumeric_py`, `rule_category_entity_name`, `sym_log_reg_scoring_path`, `constraint_include_character_attribute_list`, `rule_category_capacity_unit_value`, `code_entity`, `duration` |
| n9 | speech_act | t1:s20 | ask whether missing batch_size and seq_length unpacking is a bug or misuse | `ask`*, `rule_category_code_value`, `rule_category_capacity_unit_value`, `duration`, `rule_reading_guide`, `config_overlay`, `rule_review_points`, `rule_attributes_and_generate`, `rule_support_primitives_general`, `size_tall`, `raises_exception`, `size_medium` |
| n10 | object | t1:s22 | requested maintainers ArthurZucker and younesbelkada | `request`*, `role_user`, `rule_category_entity_name`, `duration`, `constraint_comprehensive`, `resource_heater`, `resource_chiller`, `constraint_beginner`, `requirement`, `rule_category_constraint_value`, `resource_sink`, `constraint_budget_limited` |
| n11 | claim | t1:s24, t1:s25 | running custom modified script rather than official example | `modify_code`, `example_of`, `chg_modify_code`, `cli_command`, `rule_composites_general`, `mod_mixed_case`, `example_d_record_an_actual_test_outcome_without_asserting_overall_correctness`, `enables`, `substitute`, `rule_category_descriptive_value`, `leads_to`, `sequence` |
| n12 | claim | t1:s27, t1:s28 | running custom task or dataset rather than standard benchmark | `rule_operations_general`, `menu_works`, `performance_tracking`, `trained_for`, `run_tests`, `outcome`, `enables`, `example_d_record_an_actual_test_outcome_without_asserting_overall_correctness`, `occurred_recently`, `entity_checklist`, `leads_to`, `user_practice` |
| n13 | action | t1:s30 | reproduce bug by passing inputs_embeds and attention_mask to ConvBertForTokenClassification | `issue`, `example_e_preserve_exact_wording_through_generation_and_sending`, `type_text`, `rule_recording_signatures`, `rule_category_code_value`, `reconcile_code`, `rule_attributes_and_generate`, `calculation`, `constraint_include_character_attribute_list`, `duplicate_definition`, `sym_log_reg_scoring_path`, `apply_filters` |
| n14 | constraint | t1:s32 | expected execution without raising UnboundLocalError | `raises_exception`*, `test_condition`, `constraint_include_character_attribute_list`, `rule_operations_general`, `conditional`, `maximum_between_stops`, `constraint_budget_limited`, `sequence`, `requirement`, `assert_multinomial_scorer`, `constraint_exclude_flowery_language`, `calculation` |
| n15 | negation | t1:s32 | no error should occur during model execution | `raises_exception`, `temporal_context`*, `wait`, `rule_operations_general`, `exclude`, `rule_recording_signatures`, `test_condition`, `run_tests`, `path_sklearn_linear_model_logistic_py`, `failure`, `calculation`, `example_d_record_an_actual_test_outcome_without_asserting_overall_correctness` |
| n16 | action | t2:s2 | modify file src/transformers/models/convbert/modeling_convbert.py | `chg_modify_code`, `modify_code`, `config_overlay`, `path_sklearn_linear_model_logistic_py`, `policy_revision_request`, `software_version`, `reconcile_code`, `config_setting`, `rule_category_transformation_value`, `pull_request`, `substitute`, `transform_remove_br` |
| n17 | object | t2:s2 | transformers library codebase → `platform_label::<key>` | `duplicate_definition`, `chg_modify_code`, `software_version`, `transform_remove_br`, `rule_category_transformation_value`, `reconcile_code`, `lamp`, `modify_code`, `code_entity`, `resource_chiller`, `sym_log_reg_scoring_path`, `wine_yeast` |

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

- issue.project → platform_label
- config_setting.value → platform_label
- modify_code.target → platform_label
- pick_up.target → object_label, food_label
- pick_up.source → object_label
- pick_up.color → color_label
- code_entity.project → platform_label
- software_version.project → platform_label
- chg_modify_code.target → platform_label
- pull_request.project → platform_label
- requirement.value → platform_label
- run_tests.target → platform_label
- failure.system → platform_label
- activity.object → object_label, food_label, animal_label
- activity.location → country
- activity.instrument → object_label, platform_label
- subject.qualifier → platform_label
- subject.location → country

## Retrieved records

### Shared rules that govern the records below (full text)

**rule_lexical_groups** (v19/rule/lexical-groups; rule governing platform_label)

Section 3.1 defines value groups: `group::key` values of type ATOM[group]. Open groups admit any key of their form (examples are not whitelists); standard groups admit the codes of their bundled standard (ISO 3166-1 alpha-2 for country, ISO 4217 for currency). Leaf values are never glossary entries. Consumer signatures alone decide where a group may appear. Retired bare symbols are invalid.

**rule_reading_guide** (v19/rule/reading-guide; candidate)

The spec governs syntax/types; this glossary defines vocabulary. Signature notation: ? optional, A / B explicit alternatives, void no result. Omitted optional arguments are unspecified. Value entries are category-refined STRING primitives; complex meanings require composition. Aliases are contextual hints, not unconditional equivalences. Report ambiguity. IDs use v19/<category>/<symbol>, v19/support/<symbol> or v19/composite/<symbol>. Statuses apply to this candidate: Retained preserves meaning; Adapted uses the stated contract; Composite requires TERM (bare STRING deprecated); Structural is syntax/argument vocabulary; Needs clarification is unusable until resolved; Deprecated is historical; Accepted is usable within this candidate.

**rule_recording_signatures** (v19/rule/recording-signatures; candidate)

RECORD ACTION uses the operation signature with REF[STRING] → TERM and LIST[REF[STRING]] → LIST[TERM]; other types/categories stay unchanged. Return EVENT, never the runtime result. Record actual outputs as attributed CLAIMs. Do not infer missing resources.

**rule_speech_acts_general** (v19/rule/speech-acts-general; rule governing respond)

UTTER-only, void, with the spec's speech attributes and LIST[TERM] constraints. No result binding. Literal content cannot replace required semantic arguments for structured coverage.

**rule_structural_constructs** (v19/rule/structural-constructs; core)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; rule governing spatial_state)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_attributes_and_generate** (v19/rule/attributes-and-generate; candidate)

Attribute entries name arguments; legality/types come from each operation, not global membership. GENERATE uses the spec's core fields; retained artifact profiles return STRING. Numeric/list results need explicit profiles. Legacy itinerary fields expand to TERM constraints: duration/duration_unit → duration(amount,unit); stop_min_per_day/stop_requirement → minimum_per_period(class,count,period=unit_day), never an inferred temple class; max_walk_duration/unit → maximum_between_stops(activity="walk",amount,unit). No legacy shorthand is enabled. Old events/character_properties/transformations become explicitly scoped TERM constraints. Message purpose is TERM, not send_email.content: GENERATE exact STRING content, then send. Report opaque fallback separately.

**rule_category_artifact_value** (v19/rule/category/artifact-value; rule governing art_short_text)

STRING artifact class for GENERATE.target. art_story says what kind of artifact to produce, not what occurs in its plot.

**rule_category_capacity_unit_value** (v19/rule/category/capacity-unit-value; candidate)

Preserve original binary-unit definitions for audit, but mark Needs clarification: GB/TB aliases conflate decimal and binary units. No silent change to scale.

**rule_category_character_property_value** (v19/rule/category/character-property-value; candidate)

TERM-described trait/style. Use constraints and explicit inclusion/scope; do not use an ungoverned character_properties attribute.

**rule_category_code_value** (v19/rule/category/code-value; candidate)

path_/sym_ remain STRING identities; migrated chg_/assert_ are TERM constructors. Do not recover an exact file path by guessing from underscores.

**rule_category_constraint_value** (v19/rule/category/constraint-value; candidate)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_content_value** (v19/rule/category/content-value; rule governing content_status_update)

Existing compounds become the constructors in Section 5. Their outputs go in topic/target/constraints as appropriate, not content, whose spec type remains STRING.

**rule_category_descriptive_value** (v19/rule/category/descriptive-value; candidate)

STRING modifier/domain label; never a free-form proposition. dom_sgi needs its intended referent established before semantically dependent use.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; rule governing unit_character)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; candidate)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_format_value** (v19/rule/category/format-value; candidate)

STRING format. format_email is layout, not the action send_email.

**rule_category_locale_value** (v19/rule/category/locale-value; candidate)

STRING locale. “English” alone does not always mean locale_en_us; preserve ambiguity.

**rule_category_product_attribute_value** (v19/rule/category/product-attribute-value; rule governing size_tall)

STRING color/size/product-market facets. gender_women describes a product category, not an assertion about a person's gender.

**rule_category_recipient_value** (v19/rule/category/recipient-value; rule governing role_user)

STRING roles or explicit named recipients. A role is not an exact person's identity. Keep an explicit name where substituting a role loses information.

**rule_category_reservation_status_value** (v19/rule/category/reservation-status-value; candidate)

STRING filter states; neither is a BOOL result binding. check_reservation_availability returns a BOOL with a distinct handle.

**rule_category_semantic_category_value** (v19/rule/category/semantic-category-value; candidate)

STRING class label used by typed constraints. class_temple describes a class, not an acquired physical temple reference.

**rule_category_state_value** (v19/rule/category/state-value; rule governing state_sliced)

STRING condition used in selection. state_warm does not command heat; “hot” is not automatically synonymous with “warm.”

**rule_category_tone_value** (v19/rule/category/tone-value; rule governing tone_polite)

STRING register. tone_urgent describes urgency, not a concrete deadline.

**rule_category_transformation_value** (v19/rule/category/transformation-value; candidate)

TERM-described transformation. Pass it through constraints; no ungoverned transformations attribute.

**rule_composites_general** (v19/rule/composites-general; candidate)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_examples_general** (v19/rule/examples-general; rule governing example_e_preserve_exact_wording_through_generation_and_sending)

Examples use this glossary's contracts. They have not been verified by an implemented BrainCode parser.

**rule_operations_general** (v19/rule/operations-general; candidate)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_review_points** (v19/rule/review-points; candidate)

The 2026-10-04 review retained the current definitions of cap_gb, cap_tb, constraint_17_plus and dom_sgi. Do not invent scale choices, rating thresholds or acronym expansions beyond those definitions. Money signs, locale aliases, warm/hot and ranking phrases require context. Only this explicit inventory is usable; do not guess historical entries. Before adoption, resolve any remaining Needs clarification entries and review signatures/expansions. Artifact checks do not establish parser correctness or semantic fidelity.

**rule_supplemental_general** (v19/rule/supplemental-general; rule governing extract)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; candidate)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- apply_filters | operation | operation-vocabulary | (target: REF[STRING], criteria: LIST[TERM]) -> void | Apply the listed filters to an existing UI. Not repeated evidence of a search already represented.  ⟵ candidate
- extract | operation | operation-vocabulary | (target: LIST[REF[STRING]], limit: NUMBER) -> LIST[REF[STRING]] | First limit results, preserving order and identity; limit is a nonnegative integer; limit=1 is still a list  ⟵ candidate
- hover | operation | operation-vocabulary | (target: REF[STRING]) -> void | Move pointer cursor over an interactive web element without clicking. target must resolve to a valid element reference. | aliases: mouse_over  ⟵ candidate
- modify_code | operation | operation-vocabulary | (target: STRING / ATOM[platform_label], file: STRING, revision: TERM, method?: STRING) -> void | Apply the structured change to the indicated code. A method name alone does not specify the change. | aliases: fix, reduce, optimize  ⟵ candidate
- pick_up | operation | operation-vocabulary | (target: STRING / ATOM[object_label] / ATOM[food_label], quantity?: NUMBER, source?: STRING / ATOM[object_label], color?: STRING / ATOM[color_label], shape?: STRING, state?: STRING) -> REF[STRING] or LIST[REF[STRING]] | Select/acquire objects. Missing quantity or literal 1 returns REF; integer literal greater than 1 returns LIST[REF]. Other values are invalid for this profile. | aliases: grab, take, retrieve  ⟵ candidate
- remove | operation | operation-vocabulary | (target: REF[STRING] / TERM, source?: STRING / TERM) -> void | Remove an object from an enclosure or container. target must be an object inside source. | aliases: take_out  ⟵ candidate
- run_tests | operation | operation-vocabulary | (target: STRING / ATOM[platform_label], assertion?: TERM) -> BOOL | Run the selected project's tests, optionally checking the specified assertion. TRUE means the declared test condition passed, not overall software correctness.  ⟵ candidate
- send_email | operation | operation-vocabulary | (recipient: STRING, content: STRING, tone?: STRING) -> void | Send supplied exact message content to the identified recipient. A requested message purpose is not already a composed message. | aliases: email  ⟵ candidate
- send_message | operation | operation-vocabulary | (recipient: STRING, content: STRING, tone?: STRING) -> void | Send supplied exact content through the specified message context. If the channel is unresolved, report it. | aliases: text  ⟵ candidate
- slice | operation | operation-vocabulary | (target: REF[STRING] / TERM) -> REF[STRING] | Slice the selected material or described term, preserving its tracked aggregate identity. | aliases: chop, cut  ⟵ candidate
- type_text | operation | operation-vocabulary | (target: REF[STRING], text: STRING) -> void | Type text into a designated input field, text box, or editable area. target must identify an editable element. | aliases: enter_text, input_text, input_string  ⟵ candidate
- wait | operation | operation-vocabulary | (duration?: NUMBER) -> void | Pause execution for a duration or cycle. duration in seconds or ticks. | aliases: idle, pause  ⟵ candidate

### speech acts

- acknowledge | speech_act | operation-vocabulary | UTTER acknowledge(target: CLAIM / TERM) | Acknowledge receipt/awareness; does not imply agreement.  ⟵ candidate
- ask | speech_act | operation-vocabulary | UTTER ask(target: TERM, or a sufficiently precise topic: STRING / TERM) | Request information/advice; not an assertion of an answer. | aliases: ask, how should  ⟵ candidate
- correct | speech_act | operation-vocabulary | UTTER correct(target: CLAIM) | Offer corrected content. Actual supersession requires the Conversation revision rules.  ⟵ candidate
- inform | speech_act | operation-vocabulary | UTTER inform(target: CLAIM) | Present the proposition; preserve its holder/status.  ⟵ candidate
- offer | speech_act | operation-vocabulary | UTTER offer(target: STRING / TERM) | Speech act offering assistance, service, or items to a conversation partner. speech act in dialogic traces. | aliases: proffer  ⟵ candidate
- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ dependency of content_status_update
- calculation | constructor | TERM calculation(inputs: LIST[TERM], operation: STRING, result?: TERM) -> TERM | Constructs a descriptive representation of an arithmetic or algorithmic calculation step with inputs, operation identifier, and optional resulting value. | not: an executed runtime action or factual claim of outcome | aliases: math_operation, compute_step  ⟵ candidate
- change_property | constructor | TERM change_property(property: STRING, source: STRING, target: STRING) -> TERM | Require target to inherit the property value from source | not: Not an arbitrary code patch  ⟵ dependency of chg_inherit_multi_class
- chg_modify_code | constructor | TERM chg_modify_code(target: STRING / ATOM[platform_label], file: STRING / TERM, revision: TERM) -> TERM | Constructs a structured change specification describing code file modifications. software engineering revision term. | aliases: modify_source_code  ⟵ candidate
- cli_command | constructor | TERM cli_command(executable: STRING, args?: LIST[STRING] / LIST[TERM]) -> TERM | Constructs a structured representation of a command-line invocation with executable and optional arguments or flags. | not: an executed external action or process run (pure description) | aliases: command_line, shell_command, cli_invocation  ⟵ candidate
- code_entity | constructor | TERM code_entity(file?: STRING / TERM, kind: STRING, name: STRING, project?: STRING / ATOM[platform_label]) -> TERM | Constructs a structured descriptor for a source code entity such as a function, method, class, module, or source file within a project. | not: an executed runtime call or file system operation | aliases: code_function, source_file, code_symbol  ⟵ candidate
- conditional | constructor | TERM conditional(condition: TERM, consequence: TERM) -> TERM | Constructs a structured conditional proposition term connecting a condition and consequence. descriptive logic structure. | aliases: if_then  ⟵ candidate
- config_overlay | constructor | TERM config_overlay(files: LIST[STRING] / LIST[TERM], reverse_order?: BOOL) -> TERM | Constructs a specification of configuration file overlay precedence and ordering across multiple configuration files. | not: a general list sorting operation or spatial layering | aliases: overlay_config, config_precedence, overlay_order  ⟵ candidate
- config_setting | constructor | TERM config_setting(option: STRING, section: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Constructs a structured representation of a configuration key-value setting within an identified section. | not: an active runtime configuration state or environment setting | aliases: ini_setting, config_option, configuration_setting  ⟵ candidate
- conjunction | constructor | TERM conjunction(items: LIST[TERM]) -> TERM | All described components apply | not: Does not imply temporal order  ⟵ candidate
- duration | constructor | TERM duration(amount: NUMBER, unit: STRING) -> TERM | Requested elapsed/calendar extent | not: Word/item counts are not time  ⟵ candidate
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ candidate
- greeting | constructor | TERM greeting(recipient: STRING) -> TERM | Constructs a conversational salutation greeting descriptor. conversational discourse term. | aliases: salutation  ⟵ candidate
- include | constructor | TERM include(item: STRING / TERM) -> TERM | Require the identified content/item | not: Not permission to invent an instance in a recorded trace  ⟵ dependency of constraint_include_character_attribute_list
- issue | constructor | TERM issue(project: STRING / ATOM[platform_label], number: NUMBER) -> TERM | Constructs an issue tracker ticket reference. issue tracker descriptor. | aliases: issue_ticket, bug_report  ⟵ candidate
- location_spec | constructor | TERM location_spec(address?: STRING, area?: STRING, city?: STRING, state?: STRING) -> TERM | Constructs a structured geographical location specification with regional and administrative qualifiers. | not: a fixed atomic location descriptor in location-name or a spatial relation | aliases: location_details, geographic_location  ⟵ candidate
- maximum_between_stops | constructor | TERM maximum_between_stops(activity: STRING, amount: NUMBER, unit: STRING) -> TERM | Upper bound on the stated activity between successive stops | not: Not a limit on total daily duration  ⟵ candidate
- negation | constructor | TERM negation(target: TERM) -> TERM | Constructs a descriptive semantic negation of a target descriptive proposition or condition term. | not: Check's runtime Boolean operator NOT or a speech-act decline | aliases: not, does not, negation, absence of  ⟵ candidate
- performance_tracking | constructor | TERM performance_tracking(adjustment?: STRING / TERM, target: STRING / TERM) -> TERM | Constructs a descriptive representation of monitoring performance metrics or campaign results with an optional strategy adjustment. | not: a runtime metric observation or software test run | aliases: track_results, monitor_performance, campaign_tracking  ⟵ candidate
- policy_revision_request | constructor | TERM policy_revision_request(original_policy: CLAIM / TERM, inclusions: LIST[TERM]) -> TERM | Constructs a request to revise an existing policy with additional clauses. descriptive revision term. | aliases: policy_amendment  ⟵ candidate
- pull_request | constructor | TERM pull_request(project: STRING / ATOM[platform_label], number: NUMBER) -> TERM | Constructs a repository pull request reference. software repository reference. | aliases: pr  ⟵ candidate
- reconcile_code | constructor | TERM reconcile_code(entities: LIST[TERM], objective: STRING / TERM) -> TERM | Constructs a specification to reconcile multiple code entities or implementations to standardize their behavior. | not: a general file merge operation | aliases: reconcile_functions, standardize_behavior, reconcile_implementations  ⟵ candidate
- remove_literal | constructor | TERM remove_literal(text: STRING) -> TERM | Remove occurrences of that exact literal in the stated artifact | not: Not remove similar markup unless specified  ⟵ dependency of transform_remove_br
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ candidate
- sequence | constructor | TERM sequence(items: LIST[TERM]) -> TERM | Ordered described activities/content | not: Not unordered conjunction  ⟵ candidate
- software_version | constructor | TERM software_version(branch?: STRING, project: STRING / ATOM[platform_label], version?: STRING) -> TERM | Constructs a descriptor for a software project version, release tag, or branch identifier. | not: an installed runtime package environment | aliases: repo_branch, git_branch, project_version  ⟵ candidate
- spatial_constraint | constructor | TERM spatial_constraint(relation: STRING, object: TERM, reference: TERM) -> TERM | Constructs a descriptive spatial constraint between an object and a reference landmark. relation must specify a spatial configuration. | aliases: spatial_relation  ⟵ candidate
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ dependency of content_status_update
- substitute | constructor | TERM substitute(original: STRING / TERM, replacement: STRING / TERM, purpose?: STRING / TERM) -> TERM | Constructs a descriptive representation of substituting an original entity or ingredient with a replacement alternative. | not: an executed change or runtime revision (use LINK revises) | aliases: substitute, substitution, alternative for, replace with  ⟵ candidate
- temporal_context | constructor | TERM temporal_context(activity: STRING / TERM, period?: STRING) -> TERM | Constructs a temporal or situational context descriptor specifying an ongoing process, evaluation phase, or historical timeframe. | not: time_point (a specific timestamp/date) or duration (an elapsed numerical duration) | aliases: while, during, in past relationships, timeframe  ⟵ candidate
- test_condition | constructor | TERM test_condition(condition: STRING, expected: BOOL) -> TERM | A testable condition with the expected Boolean outcome | not: Expected outcome is not an observed result  ⟵ candidate
- training_program | constructor | TERM training_program(topic: STRING / TERM, audience: STRING / TERM) -> TERM | Constructs a description of an educational or compliance training program. used for instructional policy requirements. | aliases: training_course  ⟵ candidate

### composites

- assert_multinomial_scorer | composite | code-value | TERM assert_multinomial_scorer() -> TERM | Assertion that multinomial probabilistic scoring succeeds. | = test_condition(condition="multinomial_probabilistic_scoring", expected=TRUE)  ⟵ candidate
- chg_inherit_multi_class | composite | code-value | TERM chg_inherit_multi_class(source: STRING, target: STRING) -> TERM | Change requiring a constructed estimator to inherit multi_class. | = change_property(property="multi_class", source=$source, target=$target)  ⟵ candidate
- constraint_beginner | composite | constraint-value | TERM constraint_beginner() -> TERM | Targeted at beginners. | = requirement(property="audience_expertise", value="beginner")  ⟵ candidate
- constraint_budget_limited | composite | constraint-value | TERM constraint_budget_limited() -> TERM | Limited budget. | = requirement(property="budget_limited", value=TRUE)  ⟵ candidate
- constraint_comprehensive | composite | constraint-value | TERM constraint_comprehensive() -> TERM | Must be comprehensive. | = requirement(property="comprehensive", value=TRUE)  ⟵ candidate
- constraint_exclude_flowery_language | composite | constraint-value | TERM constraint_exclude_flowery_language() -> TERM | Avoid flowery language. | = exclude(item="flowery_language")  ⟵ candidate
- constraint_include_character_attribute_list | composite | constraint-value | TERM constraint_include_character_attribute_list() -> TERM | Include character attributes. | = include(item="character_attribute_list")  ⟵ candidate
- content_status_update | composite | content-value | TERM content_status_update(subject: STRING) -> TERM | A request for a status update. | = activity(verb="request_update", object=$subject) | aliases: status update  ⟵ candidate
- transform_remove_br | composite | transformation-value | TERM transform_remove_br() -> TERM | Remove <br /> tags. | = remove_literal(text="<br />")  ⟵ candidate

### claim relations

- duplicate_definition | claim_relation | CLAIM duplicate_definition(count: NUMBER, entity: TERM, location?: STRING / TERM) | Asserts that multiple duplicate copies or definitions of a code entity exist within a codebase or location. | not: an exact string equality check | aliases: duplicate_code, two_copies, duplicate_function  ⟵ candidate
- enables | claim_relation | CLAIM enables(condition: TERM / CLAIM, outcome: TERM / CLAIM) | Asserts that an enabling condition or capability facilitates an outcome. enabling condition. | aliases: facilitates, allows  ⟵ candidate
- example_of | claim_relation | CLAIM example_of(example: TERM, concept: TERM) | Asserts that an instance or term exemplifies a general concept, pattern, or category. example and concept are descriptive terms. | aliases: exemplifies, instance_of  ⟵ candidate
- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ candidate
- has_state | claim_relation | CLAIM has_state(subject: TERM, state: STRING) | Asserts that an entity is currently in a physical, thermal, or operational state. state must be a valid state descriptor string. | aliases: in_state, state_is  ⟵ related to spatial_state
- leads_to | claim_relation | CLAIM leads_to(cause: TERM, effect: TERM) | Asserts a conceptual consequence or progression from cause to effect. progression relation. | aliases: results_in  ⟵ candidate
- menu_works | claim_relation | CLAIM menu_works(property: STRING) | Asserts that a menu or recipe plan satisfies an operational criterion. menu evaluation. | aliases: menu_satisfies  ⟵ candidate
- occurred_recently | claim_relation | CLAIM occurred_recently(target: CLAIM) | Asserts temporal recency of an asserted occurrence or claim. temporal recency qualifier. | aliases: recently_happened  ⟵ candidate
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ candidate
- raises_exception | claim_relation | CLAIM raises_exception(target?: TERM, exception_type: STRING, message?: STRING) | Asserts that an unhandled runtime error or exception was raised with the specified exception type, message, and target entity. | not: warning (a non-fatal library warning or deprecation notice) or failure (a general system failure hypothesis) | aliases: raises, exception, throws_error, type_error  ⟵ candidate
- request | claim_relation | CLAIM request(target: TERM / STRING) | Represents an active communicative request or constraint state in conversation tracking. target is the requested action or topic. | aliases: user_request  ⟵ candidate
- spatial_state | claim_relation | CLAIM spatial_state(relation: STRING, object: TERM, reference: TERM) | Asserts an observed spatial configuration between an object and a reference landmark. relation must specify spatial configuration. | aliases: placed_at, located_at  ⟵ candidate
- trained_for | claim_relation | CLAIM trained_for(subject: STRING / TERM, activity: TERM) | Asserts that an agent or model underwent training for a designated activity. training objective. | aliases: fine_tuned_for  ⟵ candidate
- user_practice | claim_relation | CLAIM user_practice(activity: TERM) | Asserts a habitual, workflow, or recurring practice of a user. workflow practice. | aliases: habitual_activity  ⟵ candidate
- validates_parameter | claim_relation | CLAIM validates_parameter(condition: STRING, entity: TERM, parameter: STRING) | Asserts that a code entity inspects or validates parameter names or types for a specified condition. | not: a runtime assertion test | aliases: inspects_parameter, checks_parameter, validates_parameter_names  ⟵ candidate
- warning | claim_relation | CLAIM warning(message: STRING, target?: TERM) | Asserts a recorded library warning, deprecation notice, or advisory alert. system alert claim. | aliases: alert, deprecation_warning  ⟵ candidate

### links

- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ core
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ core
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ core

### values

- art_short_text | value | artifact-value | Short free text.  ⟵ dependency of example_e_preserve_exact_wording_through_generation_and_sending
- path_gcloud_pubsub_subscription_py | value | code-value | File path to the Google Cloud Pub/Sub subscription module. | aliases: gcloud_pubsub_subscription_path  ⟵ candidate
- path_ipython_core_magics_basic_py | value | code-value | File path to the IPython basic magics module. | not: an individual command line script or general config file | aliases: IPython/core/magics/basic.py, ipython_core_magics_basic_py  ⟵ candidate
- path_numpy_core_fromnumeric_py | value | code-value | Source code file path or exported symbol in scientific Python: path_numpy_core_fromnumeric_py. | aliases: path_numpy_core_fromnumeric_py  ⟵ candidate
- path_pandas_src_testing_pyx | value | code-value | Source code file path or exported symbol in scientific Python: path_pandas_src_testing_pyx. | aliases: path_pandas_src_testing_pyx  ⟵ candidate
- path_sklearn_linear_model_logistic_py | value | code-value | The scikit-learn logistic module path.  ⟵ candidate
- sym_log_reg_scoring_path | value | code-value | The _log_reg_scoring_path program symbol.  ⟵ candidate
- mod_mixed_case | value | descriptive-value | Mixed-case modifier. | aliases: mixed case  ⟵ candidate
- unit_character | value | duration-unit-value | One Unicode scalar value in the final rendered artifact; line endings are normalized to LF before counting. | aliases: characters, chars  ⟵ candidate
- entity_checklist | value | entity-name | Event planning item or menu category: entity_checklist. | aliases: entity_checklist  ⟵ candidate
- lamp | value | entity-name | A lamp light source appliance. | not: an abstract lighting concept or ambient color | aliases: light, desk_lamp  ⟵ candidate
- resource_chiller | value | entity-name | Canonical abstract chilling resource when no particular appliance is named.  ⟵ candidate
- resource_heater | value | entity-name | Canonical abstract heating resource when no particular appliance is named.  ⟵ candidate
- resource_sink | value | entity-name | Canonical abstract washing resource when no particular sink is named.  ⟵ candidate
- wine_yeast | value | entity-name | Yeast strain selected for alcoholic fermentation. | not: baking yeast or fermentation_nutrient | aliases: wine yeast, yeast, fermentation yeast  ⟵ candidate
- format_email | value | format-value | Email layout. | aliases: as an email  ⟵ dependency of example_e_preserve_exact_wording_through_generation_and_sending
- format_structured_report | value | format-value | Headed structured report layout. | aliases: structured report, report  ⟵ candidate
- size_medium | value | product-attribute-value | Medium size. | aliases: medium, M  ⟵ candidate
- size_small | value | product-attribute-value | Small size. | aliases: small, S  ⟵ candidate
- size_tall | value | product-attribute-value | Tall relative vertical dimension qualifier. | aliases: size_tall  ⟵ candidate
- role_agent | value | recipient-value | The assistant. | aliases: you, the assistant  ⟵ dependency of example_d_record_an_actual_test_outcome_without_asserting_overall_correctness
- role_manager | value | recipient-value | The user's manager. | aliases: my manager, boss  ⟵ dependency of example_e_preserve_exact_wording_through_generation_and_sending
- role_user | value | recipient-value | The requesting human. | aliases: me, I  ⟵ candidate
- state_sliced | value | state-value | The condition of being sliced or cut into thin pieces. | not: the operation slice itself | aliases: sliced, slice, chopped, cut  ⟵ candidate
- tone_polite | value | tone-value | Courteous, respectful register. | aliases: politely, kindly  ⟵ dependency of example_e_preserve_exact_wording_through_generation_and_sending

### examples

- example_d_record_an_actual_test_outcome_without_asserting_overall_correctness (candidate): Record an actual test outcome without asserting overall correctness

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=AGENT {
    RECORD ACTION run_tests(target=platform_label::scikit_learn) STATUS succeeded SOURCE "t1:tests" -> run_tests_event : EVENT
    CLAIM outcome(event=run_tests_event, value=TRUE) BY role_agent STATUS observed SOURCE "t1:tests" -> outcome_2 : CLAIM
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

