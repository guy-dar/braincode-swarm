# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 25 needs (decomposition: llm), 172 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | action | t1:s1 | reconcile accounts receivable balance sheet accounts | `reconcile_code`, `rule_category_capacity_unit_value`, `format_structured_report`, `pick_up`, `rule_category_reservation_status_value`, `recycle_bin`, `metric_repeat_buyer`, `transform_preserve_first_column`, `rule_recording_signatures`, `calculation`, `meets_needs`, `duplicate_definition` |
| n2 | action | t1:s1 | reconcile deferred revenue balance sheet accounts | `reconcile_code`, `rule_category_capacity_unit_value`, `pick_up`, `rule_category_reservation_status_value`, `transform_preserve_first_column`, `recycle_bin`, `rule_recording_signatures`, `calculation`, `metric_repeat_buyer`, `credit_card`, `rule_category_transformation_value`, `reservation_availability` |
| n3 | temporal | t1:s1 | maintain ongoing reconciliation over time | `ongoing`*, `reconcile_code`, `reservation_available`, `role_support_team`, `occurred_recently`, `rule_trace_relations_general`, `temporal_context`, `substitute`, `time_horizon`, `metric_response_time`, `time_point`, `duration` |
| n4 | speech_act | t1:s2 | ask what balance sheet reconciliation means in Zuora reporting | `format_structured_report`*, `respond`, `acknowledge`, `ask`*, `confirm`, `reconcile_code`, `rule_trace_relations_general`, `rule_category_capacity_unit_value`, `inform`, `apologize`, `decline`, `role_respondent` |
| n5 | object | t1:s2 | Zuora subscription management platform → `platform_label::<key>` | `path_gcloud_pubsub_subscription_py`, `role_manager`, `dom_sgi`, `role_customer`, `resource_sink`, `dom_safari`, `onsen`, `role_support_team`, `reservation_availability`, `role_friend`, `role_colleague`, `avail_out_of_stock` |
| n6 | object | t1:s2 | Zuora reporting module | `format_structured_report`*, `unit_item`, `resource_chiller`, `chill`, `art_structured_report`, `resource_sink`, `issue`, `send_message`, `rate`, `dom_sgi`, `provides`, `path_sklearn_linear_model_logistic_py` |
| n7 | claim | t2:s1, t2:s2 | Zuora reconciliation involves syncing Zuora AR and deferred revenue with financial statements | `occurred_recently`, `statement`*, `outcome`, `involves`*, `reconcile_code`, `rule_trace_relations_general`, `substitute`, `reservation_availability`, `leads_to`, `enables`, `occurred`, `ongoing` |
| n8 | object | t2:s5 | Zuora Accounts Receivable Aging Report | `format_structured_report`*, `art_structured_report`, `constraint_17_plus`, `topic_macbook_pro_2017`, `unit_year`, `unit_item`, `reservation_availability`, `dom_sgi`, `rule_category_capacity_unit_value`, `resource_sink`, `rule_category_duration_unit_value`, `resource_heater` |
| n9 | claim | t2:s5, t2:s6 | AR Aging report categorizes unpaid invoices by age to spot discrepancies | `occurred_recently`, `format_structured_report`*, `outcome`, `rule_category_duration_unit_value`, `rule_category_capacity_unit_value`, `unit_year`, `leads_to`, `constraint_17_plus`, `ongoing`, `rule_attributes_and_generate`, `recommended`, `enables` |
| n10 | object | t2:s8 | Zuora Deferred Revenue Schedule report | `format_structured_report`*, `clock`, `occurred_recently`, `reservation_unavailable`, `constraint_budget_limited`, `unit_item`, `reservation_availability`, `art_structured_report`, `rule_category_duration_unit_value`, `prep_time`, `time_point`, `unit_month` |
| n11 | claim | t2:s9, t2:s10 | Deferred Revenue Schedule shows deferred balances and recognition entries for reconciliation | `occurred_recently`, `outcome`, `rule_category_reservation_status_value`, `rule_category_capacity_unit_value`, `duration`, `ongoing`, `rule_recording_signatures`, `rule_category_duration_unit_value`, `occurred`, `leads_to`, `check_reservation_availability`, `unit_item`* |
| n12 | object | t2:s12 | Zuora Revenue Reports | `format_structured_report`*, `unit_item`, `resource_sink`, `art_structured_report`, `rule_category_capacity_unit_value`, `avail_out_of_stock`, `outcome`, `avail_in_stock`, `japanese_government`, `reservation_availability`, `dom_sgi`, `dir_desc` |
| n13 | claim | t2:s14, t2:s15 | regular review and prompt investigation of report discrepancies keeps accounts reconciled | `format_structured_report`*, `occurred_recently`, `example_d_record_an_actual_test_outcome_without_asserting_overall_correctness`, `outcome`, `rule_category_capacity_unit_value`, `rule_trace_relations_general`, `ongoing`, `metric_repeat_buyer`, `rule_category_reservation_status_value`, `rule_recording_signatures`, `leads_to`, `failure` |
| n14 | speech_act | t3:s1 | ask whether a custom report with specified columns can be created in Zuora | `format_structured_report`*, `ask`*, `transform_preserve_first_column`, `propose_menu`, `document_section`, `unit_item`, `inform`, `propose`, `respond`, `include`, `policy_document`, `art_structured_report` |
| n15 | object | t3:s1 | usage data and adjustment records | `metric_response_time`, `rule_category_duration_unit_value`, `unit_item`, `metric_uptime`, `unit_month`, `rule_recording_signatures`, `unit_year`, `rule_category_capacity_unit_value`, `user_practice`, `resource_heater`, `resource_chiller`, `resource_sink` |
| n16 | object | t3:s1 | school entity with parent hierarchy | `topic_school_work_routine`, `role_kids`, `minimum_per_period`, `role_mother`, `entity_condensed_grocery_list`, `entity_mains`, `chg_inherit_multi_class`, `role_professor`, `japanese_government`, `class_temple`, `resource_sink`, `class_town` |
| n17 | object | t3:s1 | date of usage and date billed | `time_point`, `unit_month`, `unit_year`, `rule_category_duration_unit_value`, `unit_day`, `clock`, `daytime`, `rank_price`, `cat_limited_time_offers`, `metric_response_time`, `unit_week`, `metric_uptime` |
| n18 | object | t3:s1 | invoice number and amount columns | `transform_preserve_first_column`, `format_numbered_list`, `unit_item`, `format_table`, `quantity`, `sort`, `pick_up`, `avail_in_stock`, `metric_uptime`, `add_to_cart`, `minimum_per_period`, `unit_percent` |
| n19 | claim | t4:s1 | custom report fetching requested usage, school, invoice, and amount fields can be created | `format_structured_report`*, `request`*, `unit_item`, `provides`, `send_email`, `user_practice`, `outcome`, `created_by`, `send_message`, `policy_document`, `include`, `sort` |
| n20 | action | t4:s4, t4:s6, t4:s8 | navigate to Zuora reporting section and create new custom report | `document_section`*, `format_structured_report`*, `issue`, `send_message`, `walk`*, `art_structured_report`, `presentation_slide`, `unit_item`, `topic_current_events`*, `medical_condition`, `include`, `format_newsletter` |
| n21 | object | t4:s10 | Invoice and Payment data source in Zuora | `dom_sgi`, `avail_out_of_stock`, `avail_in_stock`, `dom_safari`, `resource_sink`, `currency`, `afcfta`, `reservation_availability`, `resource_heater`, `credit_card`, `rank_price`, `onsen` |
| n22 | action | t4:s12, t4:s14, t4:s15 | select reporting date range and add specified data columns | `format_structured_report`*, `stove`*, `add_to_cart`, `search_web`, `time_point`, `format_numbered_list`, `unit_item`, `send_message`, `sort`, `select_option`, `select_filter`, `unit_month` |
| n23 | action | t4:s17 | include Account data source to retrieve parent hierarchy fields | `pick_up`*, `include`*, `rank_field`, `change_property`, `preserve`, `sort`, `transform_preserve_first_column`, `rule_attributes_and_generate`, `select_filter`, `entity_mains`, `type_text`, `rule_category_recipient_value` |
| n24 | action | t4:s19, t4:s21 | apply filters, configure groupings, and execute report | `format_structured_report`*, `apply_filters`*, `select_filter`, `issue`, `search_web`, `include`, `policy_document`, `send_message`, `config_setting`, `sequence`, `check_reservation_availability`, `performance_tracking` |
| n25 | temporal | t4:s23 | schedule report to run at recurring intervals | `time_point`, `unit_week`, `unit_day`, `prep_time`, `daytime`, `rule_category_duration_unit_value`, `unit_hour`, `duration`, `format_structured_report`*, `clock`, `unit_item`, `performance_tracking` |

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

- pick_up.target → object_label, food_label
- pick_up.source → object_label
- pick_up.color → color_label
- chill.destination → object_label
- issue.project → platform_label
- provides.actor → platform_label
- provides.subject → platform_label
- check_reservation_availability.currency → currency
- check_reservation_availability.location → country
- failure.system → platform_label
- walk.destination → object_label
- config_setting.value → platform_label
- search_web.target → object_label, food_label, animal_label
- search_web.color → color_label
- search_web.currency → currency
- search_web.genre → genre_label
- search_web.location → country
- subject.qualifier → platform_label
- subject.location → country
- activity.object → object_label, food_label, animal_label
- activity.location → country
- activity.instrument → object_label, platform_label
- requirement.value → platform_label
- run_tests.target → platform_label
- attribute_claim.subject → platform_label
- attribute_claim.value → platform_label

## Retrieved records

### Shared rules that govern the records below (full text)

**rule_lexical_groups** (v19/rule/lexical-groups; rule governing platform_label)

Section 3.1 defines value groups: `group::key` values of type ATOM[group]. Open groups admit any key of their form (examples are not whitelists); standard groups admit the codes of their bundled standard (ISO 3166-1 alpha-2 for country, ISO 4217 for currency). Leaf values are never glossary entries. Consumer signatures alone decide where a group may appear. Retired bare symbols are invalid.

**rule_reading_guide** (v19/rule/reading-guide; core)

The spec governs syntax/types; this glossary defines vocabulary. Signature notation: ? optional, A / B explicit alternatives, void no result. Omitted optional arguments are unspecified. Value entries are category-refined STRING primitives; complex meanings require composition. Aliases are contextual hints, not unconditional equivalences. Report ambiguity. IDs use v19/<category>/<symbol>, v19/support/<symbol> or v19/composite/<symbol>. Statuses apply to this candidate: Retained preserves meaning; Adapted uses the stated contract; Composite requires TERM (bare STRING deprecated); Structural is syntax/argument vocabulary; Needs clarification is unusable until resolved; Deprecated is historical; Accepted is usable within this candidate.

**rule_recording_signatures** (v19/rule/recording-signatures; candidate)

RECORD ACTION uses the operation signature with REF[STRING] → TERM and LIST[REF[STRING]] → LIST[TERM]; other types/categories stay unchanged. Return EVENT, never the runtime result. Record actual outputs as attributed CLAIMs. Do not infer missing resources.

**rule_speech_acts_general** (v19/rule/speech-acts-general; rule governing acknowledge)

UTTER-only, void, with the spec's speech attributes and LIST[TERM] constraints. No result binding. Literal content cannot replace required semantic arguments for structured coverage.

**rule_structural_constructs** (v19/rule/structural-constructs; core)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; candidate)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_attributes_and_generate** (v19/rule/attributes-and-generate; candidate)

Attribute entries name arguments; legality/types come from each operation, not global membership. GENERATE uses the spec's core fields; retained artifact profiles return STRING. Numeric/list results need explicit profiles. Legacy itinerary fields expand to TERM constraints: duration/duration_unit → duration(amount,unit); stop_min_per_day/stop_requirement → minimum_per_period(class,count,period=unit_day), never an inferred temple class; max_walk_duration/unit → maximum_between_stops(activity="walk",amount,unit). No legacy shorthand is enabled. Old events/character_properties/transformations become explicitly scoped TERM constraints. Message purpose is TERM, not send_email.content: GENERATE exact STRING content, then send. Report opaque fallback separately.

**rule_category_artifact_value** (v19/rule/category/artifact-value; rule governing art_structured_report)

STRING artifact class for GENERATE.target. art_story says what kind of artifact to produce, not what occurs in its plot.

**rule_category_capacity_unit_value** (v19/rule/category/capacity-unit-value; candidate)

Preserve original binary-unit definitions for audit, but mark Needs clarification: GB/TB aliases conflate decimal and binary units. No silent change to scale.

**rule_category_code_value** (v19/rule/category/code-value; rule governing path_gcloud_pubsub_subscription_py)

path_/sym_ remain STRING identities; migrated chg_/assert_ are TERM constructors. Do not recover an exact file path by guessing from underscores.

**rule_category_constraint_value** (v19/rule/category/constraint-value; rule governing constraint_17_plus)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_descriptive_value** (v19/rule/category/descriptive-value; rule governing dom_sgi)

STRING modifier/domain label; never a free-form proposition. dom_sgi needs its intended referent established before semantically dependent use.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; candidate)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing recycle_bin)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_format_value** (v19/rule/category/format-value; rule governing format_structured_report)

STRING format. format_email is layout, not the action send_email.

**rule_category_location_name** (v19/rule/category/location-name; rule governing onsen)

STRING location descriptor. A `table` surface is not the generated artifact category art_table.

**rule_category_metric_value** (v19/rule/category/metric-value; rule governing metric_repeat_buyer)

STRING metric identity, not a Boolean value. Uptime and response time need numeric observations with units; order-late is Boolean-valued. Do not type every metric as BOOL.

**rule_category_recipient_value** (v19/rule/category/recipient-value; candidate)

STRING roles or explicit named recipients. A role is not an exact person's identity. Keep an explicit name where substituting a role loses information.

**rule_category_reservation_status_value** (v19/rule/category/reservation-status-value; candidate)

STRING filter states; neither is a BOOL result binding. check_reservation_availability returns a BOOL with a distinct handle.

**rule_category_search_value** (v19/rule/category/search-value; rule governing avail_out_of_stock)

STRING refinements rank_ / dir_ / cat_ / avail_ / genre_ are separate. rank_rating may fill rank_field; genre_label::comedy may not. “Cheapest” usually requires both rank_price and dir_asc, not rank_price alone.

**rule_category_semantic_category_value** (v19/rule/category/semantic-category-value; rule governing class_temple)

STRING class label used by typed constraints. class_temple describes a class, not an acquired physical temple reference.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_macbook_pro_2017)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_category_transformation_value** (v19/rule/category/transformation-value; candidate)

TERM-described transformation. Pass it through constraints; no ungoverned transformations attribute.

**rule_composites_general** (v19/rule/composites-general; rule governing transform_preserve_first_column)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_examples_general** (v19/rule/examples-general; rule governing example_d_record_an_actual_test_outcome_without_asserting_overall_correctness)

Examples use this glossary's contracts. They have not been verified by an implemented BrainCode parser.

**rule_operations_general** (v19/rule/operations-general; rule governing pick_up)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_search_web_attributes** (v19/rule/search-web-attributes; rule governing sort)

Optional filters: availability, category, color, cuisine, currency, gender, genre, location, platform, ram_unit, reservation_availability, shape, size (category-refined STRING); max_price, min_ram, min_rating (NUMBER); trending (BOOL). Explicit signature alternatives additionally admit atoms. Price requires currency; RAM requires a capacity unit; no default scale/source. rank is invalid: use sort, whose rank_field accepts rank_* and rank_direction accepts dir_*. Category/genre/availability accept only their own subfamilies.

**rule_support_primitives_general** (v19/rule/support-primitives-general; rule governing reconcile_code)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- add_to_cart | operation | operation-vocabulary | (target: LIST[REF[STRING]]) -> void | Add the explicitly selected items. Does not pay or place an order.  ⟵ candidate
- apply_filters | operation | operation-vocabulary | (target: REF[STRING], criteria: LIST[TERM]) -> void | Apply the listed filters to an existing UI. Not repeated evidence of a search already represented.  ⟵ candidate
- check_reservation_availability | operation | operation-vocabulary | (target: STRING, cuisine?: STRING, currency?: STRING / ATOM[currency], location?: STRING / ATOM[country], max_price?: NUMBER) -> BOOL | Check current availability under supplied filters. A positive result does not make a reservation. | aliases: check reservation availability  ⟵ candidate
- chill | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Chill using the stated resource; same identity.  ⟵ candidate
- open_page | operation | operation-vocabulary | (target: STRING) -> REF[STRING] | Navigate to the specified URL/page identity and return its page reference. Not a search for an unspecified page. | aliases: go to  ⟵ candidate
- pick_up | operation | operation-vocabulary | (target: STRING / ATOM[object_label] / ATOM[food_label], quantity?: NUMBER, source?: STRING / ATOM[object_label], color?: STRING / ATOM[color_label], shape?: STRING, state?: STRING) -> REF[STRING] or LIST[REF[STRING]] | Select/acquire objects. Missing quantity or literal 1 returns REF; integer literal greater than 1 returns LIST[REF]. Other values are invalid for this profile. | aliases: grab, take, retrieve  ⟵ candidate
- run_tests | operation | operation-vocabulary | (target: STRING / ATOM[platform_label], assertion?: TERM) -> BOOL | Run the selected project's tests, optionally checking the specified assertion. TRUE means the declared test condition passed, not overall software correctness.  ⟵ dependency of example_d_record_an_actual_test_outcome_without_asserting_overall_correctness
- search_web | operation | operation-vocabulary | (target: STRING / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], color?: STRING / ATOM[color_label], currency?: STRING / ATOM[currency], genre?: STRING / ATOM[genre_label], location?: STRING / ATOM[country], ...other search attributes below) -> LIST[REF[STRING]] | Query a catalog/web source. Criteria filter the result; rank separately when requested. | aliases: find, look for  ⟵ candidate
- select_filter | operation | operation-vocabulary | (target: REF[STRING], criterion: TERM) -> void | Apply one specified filter in an existing UI. Do not add this operation when the source only requests filtered search.  ⟵ candidate
- select_option | operation | operation-vocabulary | (target: REF[STRING], value: STRING) -> void | Select an option from a dropdown or select menu element. target must be a select element. | aliases: choose_option, choose_dropdown, pick_option  ⟵ candidate
- send_email | operation | operation-vocabulary | (recipient: STRING, content: STRING, tone?: STRING) -> void | Send supplied exact message content to the identified recipient. A requested message purpose is not already a composed message. | aliases: email  ⟵ candidate
- send_message | operation | operation-vocabulary | (recipient: STRING, content: STRING, tone?: STRING) -> void | Send supplied exact content through the specified message context. If the channel is unresolved, report it. | aliases: text  ⟵ candidate
- sort | operation | operation-vocabulary | (target: LIST[REF[STRING]], rank_direction: STRING, rank_field: STRING) -> LIST[REF[STRING]] | Request ordering of selected results. Preserve member identity; this is not a claim that order was observed. | aliases: rank, order by  ⟵ candidate
- type_text | operation | operation-vocabulary | (target: REF[STRING], text: STRING) -> void | Type text into a designated input field, text box, or editable area. target must identify an editable element. | aliases: enter_text, input_text, input_string  ⟵ candidate
- walk | operation | operation-vocabulary | (destination: STRING / TERM / ATOM[object_label], relation?: STRING) -> void | Locomote towards a target destination or landmark. destination must identify a valid entity or location. | aliases: move_to, go_to, navigate_to  ⟵ candidate

### speech acts

- apologize | speech_act | UTTER apologize(target?: CLAIM / TERM) | Speech act expressing apology or regret for an outcome or target. | not: decline (which is refusing) | aliases: apologize, apology, sorry  ⟵ candidate
- acknowledge | speech_act | operation-vocabulary | UTTER acknowledge(target: CLAIM / TERM) | Acknowledge receipt/awareness; does not imply agreement.  ⟵ candidate
- ask | speech_act | operation-vocabulary | UTTER ask(target: TERM, or a sufficiently precise topic: STRING / TERM) | Request information/advice; not an assertion of an answer. | aliases: ask, how should  ⟵ candidate
- confirm | speech_act | operation-vocabulary | UTTER confirm(target: CLAIM) | Confirm the proposition; its evidence/status remains explicit.  ⟵ candidate
- decline | speech_act | operation-vocabulary | UTTER decline(target: TERM) | Decline the represented request/proposal; not negate every proposition within it.  ⟵ candidate
- inform | speech_act | operation-vocabulary | UTTER inform(target: CLAIM) | Present the proposition; preserve its holder/status.  ⟵ candidate
- offer | speech_act | operation-vocabulary | UTTER offer(target: STRING / TERM) | Speech act offering assistance, service, or items to a conversation partner. speech act in dialogic traces. | aliases: proffer  ⟵ candidate
- propose | speech_act | operation-vocabulary | UTTER propose(target: TERM) | Suggest an action/idea; does not record it as performed.  ⟵ candidate
- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ dependency of temporal_context
- calculation | constructor | TERM calculation(inputs: LIST[TERM], operation: STRING, result?: TERM) -> TERM | Constructs a descriptive representation of an arithmetic or algorithmic calculation step with inputs, operation identifier, and optional resulting value. | not: an executed runtime action or factual claim of outcome | aliases: math_operation, compute_step  ⟵ candidate
- change_property | constructor | TERM change_property(property: STRING, source: STRING, target: STRING) -> TERM | Require target to inherit the property value from source | not: Not an arbitrary code patch  ⟵ candidate
- config_setting | constructor | TERM config_setting(option: STRING, section: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Constructs a structured representation of a configuration key-value setting within an identified section. | not: an active runtime configuration state or environment setting | aliases: ini_setting, config_option, configuration_setting  ⟵ candidate
- conjunction | constructor | TERM conjunction(items: LIST[TERM]) -> TERM | All described components apply | not: Does not imply temporal order  ⟵ dependency of topic_school_work_routine
- document_section | constructor | TERM document_section(title: STRING, items?: LIST[TERM]) -> TERM | Constructs a structural document section descriptor with a section title and optional content items. | not: a complete document artifact class (use art_structured_report) | aliases: section, report_section, article_section  ⟵ candidate
- duration | constructor | TERM duration(amount: NUMBER, unit: STRING) -> TERM | Requested elapsed/calendar extent | not: Word/item counts are not time  ⟵ candidate
- include | constructor | TERM include(item: STRING / TERM) -> TERM | Require the identified content/item | not: Not permission to invent an instance in a recorded trace  ⟵ candidate
- issue | constructor | TERM issue(project: STRING / ATOM[platform_label], number: NUMBER) -> TERM | Constructs an issue tracker ticket reference. issue tracker descriptor. | aliases: issue_ticket, bug_report  ⟵ candidate
- medical_condition | constructor | TERM medical_condition(condition: STRING, patient: STRING / TERM, severity?: STRING) -> TERM | Constructs a descriptive representation of a medical condition, pathology, or symptom profile. | not: an asserted factual attribution (use attribute_claim) or executed treatment | aliases: condition, symptom, pathology, diagnosis  ⟵ candidate
- minimum_per_period | constructor | TERM minimum_per_period(class: STRING, count: NUMBER, period: STRING) -> TERM | At least count members of class in each period | not: Not a minimum total over the whole artifact  ⟵ candidate
- performance_tracking | constructor | TERM performance_tracking(adjustment?: STRING / TERM, target: STRING / TERM) -> TERM | Constructs a descriptive representation of monitoring performance metrics or campaign results with an optional strategy adjustment. | not: a runtime metric observation or software test run | aliases: track_results, monitor_performance, campaign_tracking  ⟵ candidate
- policy_document | constructor | TERM policy_document(title: STRING, audience?: STRING, constraints?: LIST[TERM]) -> TERM | Constructs a structured policy document representation. used for formal organizational guidelines. | aliases: policy_spec  ⟵ candidate
- presentation_slide | constructor | TERM presentation_slide(number: NUMBER, title: STRING, content?: LIST[TERM]) -> TERM | Constructs a descriptor for a presentation slide with slide number, title, and optional content items. | not: a complete document artifact (use art_structured_report or art_plan) | aliases: slide, presentation slide, slide outline  ⟵ candidate
- preserve | constructor | TERM preserve(component: STRING, index: NUMBER) -> TERM | Keep the indexed component unchanged, using one-based indexing | not: Not preserve all components  ⟵ candidate
- rate | constructor | TERM rate(denominator: TERM, numerator: TERM) -> TERM | Constructs a structured proportional rate or frequency relating a numerator measured quantity to a denominator reference quantity. | not: an asserted factual attribution (use attribute_claim) or bound constraint (use requirement) | aliases: per_unit, ratio  ⟵ candidate
- reconcile_code | constructor | TERM reconcile_code(entities: LIST[TERM], objective: STRING / TERM) -> TERM | Constructs a specification to reconcile multiple code entities or implementations to standardize their behavior. | not: a general file merge operation | aliases: reconcile_functions, standardize_behavior, reconcile_implementations  ⟵ candidate
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ dependency of constraint_budget_limited
- sequence | constructor | TERM sequence(items: LIST[TERM]) -> TERM | Ordered described activities/content | not: Not unordered conjunction  ⟵ candidate
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ dependency of meets_needs
- substitute | constructor | TERM substitute(original: STRING / TERM, replacement: STRING / TERM, purpose?: STRING / TERM) -> TERM | Constructs a descriptive representation of substituting an original entity or ingredient with a replacement alternative. | not: an executed change or runtime revision (use LINK revises) | aliases: substitute, substitution, alternative for, replace with  ⟵ candidate
- temporal_context | constructor | TERM temporal_context(activity: STRING / TERM, period?: STRING) -> TERM | Constructs a temporal or situational context descriptor specifying an ongoing process, evaluation phase, or historical timeframe. | not: time_point (a specific timestamp/date) or duration (an elapsed numerical duration) | aliases: while, during, in past relationships, timeframe  ⟵ candidate
- time_horizon | constructor | TERM time_horizon(horizon: STRING) -> TERM | Constructs a temporal horizon or prospective timeframe descriptor indicating relative temporal distance into the future. | not: a specific calendar timestamp (use time_point) or an elapsed numerical duration (use duration). | aliases: future, future timeframe, time horizon, far off in the future, far future  ⟵ candidate
- time_point | constructor | TERM time_point(date?: STRING, time?: STRING, timezone?: STRING) -> TERM | Constructs a structured representation of a specific calendar date, time of day, or scheduled timestamp. | not: an elapsed time duration (use duration) | aliases: timestamp, datetime, scheduled_time  ⟵ candidate

### composites

- chg_inherit_multi_class | composite | code-value | TERM chg_inherit_multi_class(source: STRING, target: STRING) -> TERM | Change requiring a constructed estimator to inherit multi_class. | = change_property(property="multi_class", source=$source, target=$target)  ⟵ candidate
- constraint_budget_limited | composite | constraint-value | TERM constraint_budget_limited() -> TERM | Limited budget. | = requirement(property="budget_limited", value=TRUE)  ⟵ candidate
- topic_school_work_routine | composite | topic-value | TERM topic_school_work_routine() -> TERM | School and work routine. | = subject(kind="routine", qualifier=conjunction(items=[subject(kind="school"), subject(kind="work")]))  ⟵ candidate
- transform_preserve_first_column | composite | transformation-value | TERM transform_preserve_first_column() -> TERM | Preserve the first column of a table. | = preserve(component="column", index=1)  ⟵ candidate

### claim relations

- attribute_claim | claim_relation | CLAIM attribute_claim(subject: STRING / TERM / ATOM[platform_label], property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) | Asserts that a subject possesses a named property evaluated to a specific primitive or structured value. general property attribution claim. | aliases: property_value, word_property, has_property, property attribution  ⟵ related to statement
- created_by | claim_relation | CLAIM created_by(subject: STRING / TERM, creator: STRING) | Asserts the developer, author, or creator of an entity or system. provenance/creator assertion. | aliases: authored_by  ⟵ candidate
- duplicate_definition | claim_relation | CLAIM duplicate_definition(count: NUMBER, entity: TERM, location?: STRING / TERM) | Asserts that multiple duplicate copies or definitions of a code entity exist within a codebase or location. | not: an exact string equality check | aliases: duplicate_code, two_copies, duplicate_function  ⟵ candidate
- enables | claim_relation | CLAIM enables(condition: TERM / CLAIM, outcome: TERM / CLAIM) | Asserts that an enabling condition or capability facilitates an outcome. enabling condition. | aliases: facilitates, allows  ⟵ candidate
- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ candidate
- has_state | claim_relation | CLAIM has_state(subject: TERM, state: STRING) | Asserts that an entity is currently in a physical, thermal, or operational state. state must be a valid state descriptor string. | aliases: in_state, state_is  ⟵ related to statement
- involves | claim_relation | CLAIM involves(subject: CLAIM, target: TERM) | Asserts participant involvement or inclusion of an entity in an initiative or event. involvement claim. | aliases: includes_participant  ⟵ candidate
- leads_to | claim_relation | CLAIM leads_to(cause: TERM, effect: TERM) | Asserts a conceptual consequence or progression from cause to effect. progression relation. | aliases: results_in  ⟵ candidate
- meets_needs | claim_relation | CLAIM meets_needs(subject: TERM, beneficiary: STRING / TERM) | Asserts that an item, activity, or plan satisfies the needs of a beneficiary. utility/satisfaction claim. | aliases: satisfies_needs  ⟵ candidate
- occurred | claim_relation | CLAIM occurred(activity: TERM) | Asserts that an event, action, or activity took place in the past. past occurrence claim. | aliases: happened  ⟵ candidate
- occurred_recently | claim_relation | CLAIM occurred_recently(target: CLAIM) | Asserts temporal recency of an asserted occurrence or claim. temporal recency qualifier. | aliases: recently_happened  ⟵ candidate
- ongoing | claim_relation | CLAIM ongoing(target: TERM) | Asserts that a conflict, process, or initiative is actively ongoing. temporal aspect claim. | aliases: in_progress  ⟵ candidate
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ candidate
- prep_time | claim_relation | CLAIM prep_time(value: TERM) | Asserts an estimated preparation or assembly time duration. time requirement assertion. | aliases: preparation_duration  ⟵ candidate
- propose_menu | claim_relation | CLAIM propose_menu(menu: TERM) | Asserts the proposal of a comprehensive menu plan. planning proposal. | aliases: suggest_menu  ⟵ candidate
- provides | claim_relation | CLAIM provides(actor: STRING / TERM / ATOM[platform_label], subject: STRING / TERM / ATOM[platform_label]) | Asserts that an establishment, organization, or provider supplies a specified item or service. provision claim. | aliases: supplies  ⟵ candidate
- recommended | claim_relation | CLAIM recommended(target: TERM / CLAIM) | Asserts an advisory recommendation that an activity or measure is advisable. advisory normative claim. | aliases: advisable  ⟵ candidate
- request | claim_relation | CLAIM request(target: TERM / STRING) | Represents an active communicative request or constraint state in conversation tracking. target is the requested action or topic. | aliases: user_request  ⟵ candidate
- spatial_state | claim_relation | CLAIM spatial_state(relation: STRING, object: TERM, reference: TERM) | Asserts an observed spatial configuration between an object and a reference landmark. relation must specify spatial configuration. | aliases: placed_at, located_at  ⟵ related to statement
- statement | claim_relation | CLAIM statement(fact: TERM) | Foundational claim relation converting any descriptive TERM into an attributed, truth-evaluated assertion. universal fact assertion. | aliases: assert_fact, fact_claim, claim_statement  ⟵ candidate
- user_practice | claim_relation | CLAIM user_practice(activity: TERM) | Asserts a habitual, workflow, or recurring practice of a user. workflow practice. | aliases: habitual_activity  ⟵ candidate

### links

- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ core
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ core
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ core

### values

- art_structured_report | value | artifact-value | Headed/structured report.  ⟵ candidate
- path_gcloud_pubsub_subscription_py | value | code-value | File path to the Google Cloud Pub/Sub subscription module. | aliases: gcloud_pubsub_subscription_path  ⟵ candidate
- path_sklearn_linear_model_logistic_py | value | code-value | The scikit-learn logistic module path.  ⟵ candidate
- constraint_17_plus | value | constraint-value | Rated 17+ or mature.  ⟵ candidate
- dom_safari | value | descriptive-value | Safari domain concept. | aliases: safari  ⟵ candidate
- dom_sgi | value | descriptive-value | SGI domain concept.  ⟵ candidate
- unit_day | value | duration-unit-value | Day. | aliases: days  ⟵ candidate
- unit_hour | value | duration-unit-value | Hour. | aliases: hours  ⟵ candidate
- unit_item | value | duration-unit-value | Top-level generated list or report item. | aliases: items, entries  ⟵ candidate
- unit_month | value | duration-unit-value | Month. | aliases: months  ⟵ candidate
- unit_week | value | duration-unit-value | Week. | aliases: weeks  ⟵ candidate
- unit_year | value | duration-unit-value | Year. | aliases: years  ⟵ candidate
- afcfta | value | entity-name | African Continental Free Trade Area international agreement. | aliases: african_continental_free_trade_area  ⟵ candidate
- clock | value | entity-name | A clock timepiece appliance. | not: duration units like unit_hour | aliases: clock, timer  ⟵ candidate
- credit_card | value | entity-name | A physical plastic credit, debit, or payment card object. | not: egift_card (an electronic gift card or digital voucher) | aliases: credit card, card, payment card  ⟵ candidate
- entity_checklist | value | entity-name | Event planning item or menu category: entity_checklist. | aliases: entity_checklist  ⟵ candidate
- entity_condensed_grocery_list | value | entity-name | Event planning item or menu category: entity_condensed_grocery_list. | aliases: entity_condensed_grocery_list  ⟵ candidate
- entity_mains | value | entity-name | Event planning item or menu category: entity_mains. | aliases: entity_mains  ⟵ candidate
- recycle_bin | value | entity-name | A dedicated receptacle container for recyclable waste materials. | not: trash_can (a general waste receptacle container) | aliases: recycle bin, recycling bin, recycle_bin  ⟵ candidate
- resource_chiller | value | entity-name | Canonical abstract chilling resource when no particular appliance is named.  ⟵ candidate
- resource_heater | value | entity-name | Canonical abstract heating resource when no particular appliance is named.  ⟵ candidate
- resource_sink | value | entity-name | Canonical abstract washing resource when no particular sink is named.  ⟵ candidate
- stove | value | entity-name | A kitchen stove / range appliance for cooking or heating. | not: microwave | aliases: stove, range, cooktop  ⟵ candidate
- format_newsletter | value | format-value | Newsletter layout. | aliases: newsletter  ⟵ candidate
- format_numbered_list | value | format-value | Numbered list. | aliases: numbered steps  ⟵ candidate
- format_structured_report | value | format-value | Headed structured report layout. | aliases: structured report, report  ⟵ candidate
- format_table | value | format-value | Tabular layout. | aliases: as a table  ⟵ candidate
- onsen | value | location-name | Traditional Japanese establishment or hospitality venue: onsen. | aliases: onsen  ⟵ candidate
- metric_repeat_buyer | value | metric-value | Whether the customer is a repeat buyer. | aliases: repeat buyer, returning customer  ⟵ candidate
- metric_response_time | value | metric-value | Support response time. | aliases: response time  ⟵ candidate
- metric_uptime | value | metric-value | Service uptime status. | aliases: uptime, is up  ⟵ candidate
- japanese_government | value | recipient-value | Social, demographic, or institutional group: japanese_government. | aliases: japanese_government  ⟵ candidate
- role_adults | value | recipient-value | Adult participant group in family, event, or travel context. | not: role_kids (children participant group) or role_user (the specific conversational user) | aliases: adults, adult, grown-ups  ⟵ candidate
- role_agent | value | recipient-value | The assistant. | aliases: you, the assistant  ⟵ dependency of example_d_record_an_actual_test_outcome_without_asserting_overall_correctness
- role_colleague | value | recipient-value | A coworker of the user. | aliases: my colleague, coworker  ⟵ candidate
- role_customer | value | recipient-value | A customer/client of the user. | aliases: the customer, client  ⟵ candidate
- role_friend | value | recipient-value | A friend of the user. | aliases: my friend  ⟵ candidate
- role_kids | value | recipient-value | Children/kids participant group in event context. | aliases: kids, children  ⟵ candidate
- role_manager | value | recipient-value | The user's manager. | aliases: my manager, boss  ⟵ candidate
- role_mother | value | recipient-value | The mother of the user. | not: role_sister or role_kids | aliases: my mom, mother, mom  ⟵ candidate
- role_professor | value | recipient-value | The user's professor/instructor. | aliases: my professor, teacher  ⟵ candidate
- role_respondent | value | recipient-value | A respondent, survey participant, or interviewee providing primary research data. | not: role_customer (the user's client) or role_user (the conversational user) | aliases: respondent, respondents, survey respondent, study participant  ⟵ candidate
- role_support_team | value | recipient-value | A customer-support team. | aliases: support, customer service  ⟵ candidate
- reservation_available | value | reservation-status-value | A reservation can be made. | aliases: reservation availability, available reservations  ⟵ candidate
- reservation_unavailable | value | reservation-status-value | A reservation cannot be made. | aliases: no reservations  ⟵ candidate
- avail_in_stock | value | search-value | Available for purchase now. | aliases: available  ⟵ candidate
- avail_out_of_stock | value | search-value | Unavailable for purchase now. | aliases: sold out  ⟵ candidate
- cat_limited_time_offers | value | search-value | Category: time-limited deals.  ⟵ candidate
- dir_desc | value | search-value | Descending rank direction. | aliases: highest first  ⟵ candidate
- rank_price | value | search-value | Rank or filter field: monetary cost. | aliases: cheapest, lowest price  ⟵ candidate
- class_temple | value | semantic-category-value | The abstract class of temples. | aliases: temple, temples  ⟵ candidate
- class_town | value | semantic-category-value | The abstract class of towns. | aliases: town, towns  ⟵ candidate
- daytime | value | time-of-day-value | The period of natural daylight between sunrise and sunset in the diurnal cycle. | not: unit_day (a 24-hour elapsed duration unit) or clock time timestamps | aliases: daytime, day, day time, daylight hours  ⟵ candidate
- topic_current_events | value | topic-value | Current news, geopolitical events, and ongoing international developments. | aliases: current_events, news  ⟵ candidate
- topic_macbook_pro_2017 | value | topic-value | MacBook Pro 2017.  ⟵ candidate
- unit_percent | value | unit-value | Standard unit of proportion or ratio representing parts per hundred (%). | not: rate (a constructor relating two quantities) or unitless counts | aliases: percent, percentage, %, pct  ⟵ candidate

### attributes

- quantity | attribute | attribute-name | Explicit count as NUMBER.  ⟵ candidate
- rank_field | attribute | attribute-name | Field used by sort from search-value.  ⟵ candidate
- reservation_availability | attribute | attribute-name | Required reservation state from reservation-status-value.  ⟵ candidate

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

