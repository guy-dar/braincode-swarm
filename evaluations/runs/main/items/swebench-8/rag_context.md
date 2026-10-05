# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 16 needs (decomposition: llm), 110 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | claim | t1:s1 | Cross-file binaries are not being used for ConfigTool dependencies like LLVM | `pull_request`, `chg_modify_code`, `software_version`, `path_numpy_core_fromnumeric_py`, `config_overlay`, `rule_category_code_value`, `rule_category_capacity_unit_value`, `enables`, `recycle_bin`, `rule_review_points`, `reconcile_code`, `rule_category_entity_name` |
| n2 | object | t1:s1 | ConfigTool dependency | `chill`, `config_setting`, `resource_chiller`, `constraint_comprehensive`, `pull_request`, `conjunction`, `include`, `resource_heater`, `config_overlay`, `resource_sink`, `metric_compatibility`, `coffee_maker` |
| n3 | object | t1:s1 | LLVM → `platform_label::<key>` | `chill`, `sym_log_reg_scoring_path`, `dom_ddp`, `path_sklearn_linear_model_logistic_py`, `size_medium`, `resource_chiller`, `resource_heater`, `resource_sink`, `cd`, `dom_sgi`, `platform_label`*, `ram_unit` |
| n4 | object | t1:s2 | Mesa build → `platform_label::<key>` | `resource_heater`, `resource_sink`, `resource_chiller`, `platform_label`*, `coffee_maker`, `shape_triangular`, `art_structured_report`, `rule_category_entity_name`, `constitutional_ai`, `cd`, `art_plan`, `code_entity` |
| n5 | claim | t1:s2 | The issue occurs during Mesa build | `issue`*, `ongoing`, `raises_exception`, `duration`, `run_tests`, `regression_case`, `topic_baldurs_gate_3`, `enables`, `outcome`, `leads_to`, `constraint_budget_limited`, `occurred_recently` |
| n6 | object | t1:s3 | Cross-compilation definition file | `duplicate_definition`, `cd`, `reconcile_code`, `format_structured_report`, `config_overlay`, `rule_composites_general`, `chg_modify_code`, `resource_chiller`, `compression`, `resource_sink`, `include`, `conjunction` |
| n7 | object | t1:s5, t1:s6 | llvm-config binary definition → `platform_label::<key>` | `config_setting`, `rule_category_capacity_unit_value`, `config_overlay`, `platform_label`*, `rule_category_entity_name`, `path_sklearn_linear_model_logistic_py`, `sym_log_reg_scoring_path`, `software_version`, `chg_modify_code`, `code_entity`, `resource_chiller`, `rule_category_code_value` |
| n8 | claim | t1:s8 | The build system incorrectly finds host machine llvm-config despite cross file configuration | `platform_label`, `config_overlay`, `config_setting`, `path_ipython_core_magics_basic_py`, `path_sklearn_linear_model_logistic_py`, `path_gcloud_pubsub_subscription_py`, `failure`, `rule_category_code_value`, `issue`, `path_pandas_src_testing_pyx`, `chg_modify_code`, `path_numpy_core_fromnumeric_py` |
| n9 | object | t1:s10 | Meson build system → `platform_label::<key>` | `resource_heater`, `design_parameters`, `platform_label`*, `path_sklearn_linear_model_logistic_py`, `code_entity`, `resource_chiller`, `clock`, `resource_sink`, `size_medium`, `coffee_maker`, `unit_item`, `config_setting` |
| n10 | claim | t1:s14, t1:s22, t1:s23 | Meson performs a cross build and still resolves host llvm-config | `config_overlay`, `config_setting`, `path_sklearn_linear_model_logistic_py`, `issue`, `rule_category_code_value`, `sym_log_reg_scoring_path`, `code_entity`, `enables`, `chg_modify_code`, `menu_works`, `dom_ddp`, `path_gcloud_pubsub_subscription_py` |
| n11 | action | t1:s25 | Propose a patch to fix ConfigToolDependency handling in cross builds | `modify_code`*, `chg_modify_code`, `software_version`, `config_overlay`, `propose`*, `pull_request`, `issue`, `config_setting`, `reconcile_code`, `conjunction`, `include`, `rule_review_points` |
| n12 | object | t1:s27 | mesonbuild/dependencies/base.py file → `platform_label::<key>` | `path_numpy_core_fromnumeric_py`, `path_ipython_core_magics_basic_py`, `path_sklearn_linear_model_logistic_py`, `code_entity`, `path_pandas_src_testing_pyx`, `cd`, `path_gcloud_pubsub_subscription_py`, `include`, `software_version`, `pull_request`, `resource_heater`, `resource_chiller` |
| n13 | reasoning | t1:s37, t1:s39, t1:s43, t1:s44 | Cross-tool lookup logic should check cross_info binaries when want_cross is true | `run_tests`, `validates_parameter`, `supports`, `content_mixed_case_foreign_key_regression`, `meets_needs`, `rule_category_capacity_unit_value`, `revises`, `similarity`, `rule_category_code_value`, `mod_mixed_case`, `sym_pandas_testing_assert_almost_equal`, `rejects` |
| n14 | claim | t1:s54 | ConfigTool cross binary lookup logic should be centralized | `rule_category_capacity_unit_value`, `config_setting`, `path_sklearn_linear_model_logistic_py`, `config_overlay`, `reconcile_code`, `rule_category_code_value`, `conjunction`, `include`, `validates_parameter`, `rule_reading_guide`, `format_structured_report`, `enables` |
| n15 | action | t2:s2 | Modify mesonbuild/dependencies/base.py | `chg_modify_code`, `modify_code`, `path_numpy_core_fromnumeric_py`, `change_property`, `config_setting`, `issue`, `software_version`, `pull_request`, `include`, `chg_inherit_multi_class`, `constraint_include_character_attribute_list`, `rule_category_transformation_value` |
| n16 | object | t2:s2 | mesonbuild/dependencies/base.py target file → `platform_label::<key>` | `path_numpy_core_fromnumeric_py`, `target`*, `change_property`, `path_ipython_core_magics_basic_py`, `constraint_include_character_attribute_list`, `issue`, `path_gcloud_pubsub_subscription_py`, `request`, `remove`, `unit_item`, `pull_request`, `rule_attributes_and_generate` |

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

- pull_request.project → platform_label
- chg_modify_code.target → platform_label
- software_version.project → platform_label
- chill.destination → object_label
- config_setting.value → platform_label
- code_entity.project → platform_label
- issue.project → platform_label
- run_tests.target → platform_label
- regression_case.framework → platform_label
- failure.system → platform_label
- search_web.target → object_label, food_label, animal_label
- search_web.color → color_label
- search_web.currency → currency
- search_web.genre → genre_label
- search_web.location → country
- modify_code.target → platform_label
- requirement.value → platform_label
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

**rule_recording_signatures** (v19/rule/recording-signatures; rule governing chill)

RECORD ACTION uses the operation signature with REF[STRING] → TERM and LIST[REF[STRING]] → LIST[TERM]; other types/categories stay unchanged. Return EVENT, never the runtime result. Record actual outputs as attributed CLAIMs. Do not infer missing resources.

**rule_speech_acts_general** (v19/rule/speech-acts-general; rule governing propose)

UTTER-only, void, with the spec's speech attributes and LIST[TERM] constraints. No result binding. Literal content cannot replace required semantic arguments for structured coverage.

**rule_structural_constructs** (v19/rule/structural-constructs; core)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; rule governing enables)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_attributes_and_generate** (v19/rule/attributes-and-generate; candidate)

Attribute entries name arguments; legality/types come from each operation, not global membership. GENERATE uses the spec's core fields; retained artifact profiles return STRING. Numeric/list results need explicit profiles. Legacy itinerary fields expand to TERM constraints: duration/duration_unit → duration(amount,unit); stop_min_per_day/stop_requirement → minimum_per_period(class,count,period=unit_day), never an inferred temple class; max_walk_duration/unit → maximum_between_stops(activity="walk",amount,unit). No legacy shorthand is enabled. Old events/character_properties/transformations become explicitly scoped TERM constraints. Message purpose is TERM, not send_email.content: GENERATE exact STRING content, then send. Report opaque fallback separately.

**rule_category_artifact_value** (v19/rule/category/artifact-value; rule governing art_structured_report)

STRING artifact class for GENERATE.target. art_story says what kind of artifact to produce, not what occurs in its plot.

**rule_category_capacity_unit_value** (v19/rule/category/capacity-unit-value; candidate)

Preserve original binary-unit definitions for audit, but mark Needs clarification: GB/TB aliases conflate decimal and binary units. No silent change to scale.

**rule_category_code_value** (v19/rule/category/code-value; candidate)

path_/sym_ remain STRING identities; migrated chg_/assert_ are TERM constructors. Do not recover an exact file path by guessing from underscores.

**rule_category_constraint_value** (v19/rule/category/constraint-value; candidate)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_content_value** (v19/rule/category/content-value; rule governing content_mixed_case_foreign_key_regression)

Existing compounds become the constructors in Section 5. Their outputs go in topic/target/constraints as appropriate, not content, whose spec type remains STRING.

**rule_category_descriptive_value** (v19/rule/category/descriptive-value; rule governing dom_ddp)

STRING modifier/domain label; never a free-form proposition. dom_sgi needs its intended referent established before semantically dependent use.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; rule governing unit_item)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; candidate)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_format_value** (v19/rule/category/format-value; rule governing format_structured_report)

STRING format. format_email is layout, not the action send_email.

**rule_category_metric_value** (v19/rule/category/metric-value; rule governing metric_compatibility)

STRING metric identity, not a Boolean value. Uptime and response time need numeric observations with units; order-late is Boolean-valued. Do not type every metric as BOOL.

**rule_category_product_attribute_value** (v19/rule/category/product-attribute-value; rule governing size_medium)

STRING color/size/product-market facets. gender_women describes a product category, not an assertion about a person's gender.

**rule_category_shape_value** (v19/rule/category/shape-value; rule governing shape_triangular)

STRING geometry. shape_round may select a circular object; it does not imply color or dimensions.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_baldurs_gate_3)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_category_transformation_value** (v19/rule/category/transformation-value; candidate)

TERM-described transformation. Pass it through constraints; no ungoverned transformations attribute.

**rule_composites_general** (v19/rule/composites-general; candidate)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_operations_general** (v19/rule/operations-general; rule governing chill)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_review_points** (v19/rule/review-points; candidate)

The 2026-10-04 review retained the current definitions of cap_gb, cap_tb, constraint_17_plus and dom_sgi. Do not invent scale choices, rating thresholds or acronym expansions beyond those definitions. Money signs, locale aliases, warm/hot and ranking phrases require context. Only this explicit inventory is usable; do not guess historical entries. Before adoption, resolve any remaining Needs clarification entries and review signatures/expansions. Artifact checks do not establish parser correctness or semantic fidelity.

**rule_search_web_attributes** (v19/rule/search-web-attributes; rule governing search_web)

Optional filters: availability, category, color, cuisine, currency, gender, genre, location, platform, ram_unit, reservation_availability, shape, size (category-refined STRING); max_price, min_ram, min_rating (NUMBER); trending (BOOL). Explicit signature alternatives additionally admit atoms. Price requires currency; RAM requires a capacity unit; no default scale/source. rank is invalid: use sort, whose rank_field accepts rank_* and rank_direction accepts dir_*. Category/genre/availability accept only their own subfamilies.

**rule_supplemental_general** (v19/rule/supplemental-general; rule governing coffee_maker)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; rule governing pull_request)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- chill | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Chill using the stated resource; same identity.  ⟵ candidate
- modify_code | operation | operation-vocabulary | (target: STRING / ATOM[platform_label], file: STRING, revision: TERM, method?: STRING) -> void | Apply the structured change to the indicated code. A method name alone does not specify the change. | aliases: fix, reduce, optimize  ⟵ candidate
- remove | operation | operation-vocabulary | (target: REF[STRING] / TERM, source?: STRING / TERM) -> void | Remove an object from an enclosure or container. target must be an object inside source. | aliases: take_out  ⟵ candidate
- run_tests | operation | operation-vocabulary | (target: STRING / ATOM[platform_label], assertion?: TERM) -> BOOL | Run the selected project's tests, optionally checking the specified assertion. TRUE means the declared test condition passed, not overall software correctness.  ⟵ candidate
- search_web | operation | operation-vocabulary | (target: STRING / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], color?: STRING / ATOM[color_label], currency?: STRING / ATOM[currency], genre?: STRING / ATOM[genre_label], location?: STRING / ATOM[country], ...other search attributes below) -> LIST[REF[STRING]] | Query a catalog/web source. Criteria filter the result; rank separately when requested. | aliases: find, look for  ⟵ candidate

### speech acts

- propose | speech_act | operation-vocabulary | UTTER propose(target: TERM) | Suggest an action/idea; does not record it as performed.  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ dependency of temporal_context
- change_property | constructor | TERM change_property(property: STRING, source: STRING, target: STRING) -> TERM | Require target to inherit the property value from source | not: Not an arbitrary code patch  ⟵ candidate
- chg_modify_code | constructor | TERM chg_modify_code(target: STRING / ATOM[platform_label], file: STRING / TERM, revision: TERM) -> TERM | Constructs a structured change specification describing code file modifications. software engineering revision term. | aliases: modify_source_code  ⟵ candidate
- code_entity | constructor | TERM code_entity(file?: STRING / TERM, kind: STRING, name: STRING, project?: STRING / ATOM[platform_label]) -> TERM | Constructs a structured descriptor for a source code entity such as a function, method, class, module, or source file within a project. | not: an executed runtime call or file system operation | aliases: code_function, source_file, code_symbol  ⟵ candidate
- compression | constructor | TERM compression(target?: STRING / TERM, algorithm: STRING, format?: STRING) -> TERM | Constructs a descriptive representation of a data or package compression configuration specifying optional target platform or file, compression algorithm, and optional format. | not: an executed archive extraction/compression action or document layout format | aliases: compression_algorithm, compress_with, compression_format  ⟵ candidate
- config_overlay | constructor | TERM config_overlay(files: LIST[STRING] / LIST[TERM], reverse_order?: BOOL) -> TERM | Constructs a specification of configuration file overlay precedence and ordering across multiple configuration files. | not: a general list sorting operation or spatial layering | aliases: overlay_config, config_precedence, overlay_order  ⟵ candidate
- config_setting | constructor | TERM config_setting(option: STRING, section: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Constructs a structured representation of a configuration key-value setting within an identified section. | not: an active runtime configuration state or environment setting | aliases: ini_setting, config_option, configuration_setting  ⟵ candidate
- conjunction | constructor | TERM conjunction(items: LIST[TERM]) -> TERM | All described components apply | not: Does not imply temporal order  ⟵ candidate
- duration | constructor | TERM duration(amount: NUMBER, unit: STRING) -> TERM | Requested elapsed/calendar extent | not: Word/item counts are not time  ⟵ candidate
- include | constructor | TERM include(item: STRING / TERM) -> TERM | Require the identified content/item | not: Not permission to invent an instance in a recorded trace  ⟵ candidate
- issue | constructor | TERM issue(project: STRING / ATOM[platform_label], number: NUMBER) -> TERM | Constructs an issue tracker ticket reference. issue tracker descriptor. | aliases: issue_ticket, bug_report  ⟵ candidate
- pull_request | constructor | TERM pull_request(project: STRING / ATOM[platform_label], number: NUMBER) -> TERM | Constructs a repository pull request reference. software repository reference. | aliases: pr  ⟵ candidate
- reconcile_code | constructor | TERM reconcile_code(entities: LIST[TERM], objective: STRING / TERM) -> TERM | Constructs a specification to reconcile multiple code entities or implementations to standardize their behavior. | not: a general file merge operation | aliases: reconcile_functions, standardize_behavior, reconcile_implementations  ⟵ candidate
- regression_case | constructor | TERM regression_case(framework: STRING / ATOM[platform_label], modifier: STRING, relation: STRING) -> TERM | A regression scenario specifying affected framework, condition and relation | not: Does not invent a passing test or exact implementation  ⟵ candidate
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ dependency of constraint_comprehensive
- similarity | constructor | TERM similarity(target: STRING / TERM, dimension?: STRING / TERM) -> TERM | Constructs a descriptor representing comparative closeness or similarity to a target along a given dimension. | not: spatial proximity (use rank_distance or next_to) or an assertion of exact identity (use identity) | aliases: closest_to, similar_to, resembles  ⟵ candidate
- software_version | constructor | TERM software_version(branch?: STRING, project: STRING / ATOM[platform_label], version?: STRING) -> TERM | Constructs a descriptor for a software project version, release tag, or branch identifier. | not: an installed runtime package environment | aliases: repo_branch, git_branch, project_version  ⟵ candidate
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ dependency of meets_needs
- temporal_context | constructor | TERM temporal_context(activity: STRING / TERM, period?: STRING) -> TERM | Constructs a temporal or situational context descriptor specifying an ongoing process, evaluation phase, or historical timeframe. | not: time_point (a specific timestamp/date) or duration (an elapsed numerical duration) | aliases: while, during, in past relationships, timeframe  ⟵ candidate

### composites

- chg_inherit_multi_class | composite | code-value | TERM chg_inherit_multi_class(source: STRING, target: STRING) -> TERM | Change requiring a constructed estimator to inherit multi_class. | = change_property(property="multi_class", source=$source, target=$target)  ⟵ candidate
- constraint_budget_limited | composite | constraint-value | TERM constraint_budget_limited() -> TERM | Limited budget. | = requirement(property="budget_limited", value=TRUE)  ⟵ candidate
- constraint_comprehensive | composite | constraint-value | TERM constraint_comprehensive() -> TERM | Must be comprehensive. | = requirement(property="comprehensive", value=TRUE)  ⟵ candidate
- constraint_include_character_attribute_list | composite | constraint-value | TERM constraint_include_character_attribute_list() -> TERM | Include character attributes. | = include(item="character_attribute_list")  ⟵ candidate
- content_mixed_case_foreign_key_regression | composite | content-value | TERM content_mixed_case_foreign_key_regression() -> TERM | A mixed-case Django app-name ForeignKey regression test purpose. | = regression_case(framework=platform_label::django, modifier=mod_mixed_case, relation="ForeignKey")  ⟵ candidate

### claim relations

- duplicate_definition | claim_relation | CLAIM duplicate_definition(count: NUMBER, entity: TERM, location?: STRING / TERM) | Asserts that multiple duplicate copies or definitions of a code entity exist within a codebase or location. | not: an exact string equality check | aliases: duplicate_code, two_copies, duplicate_function  ⟵ candidate
- enables | claim_relation | CLAIM enables(condition: TERM / CLAIM, outcome: TERM / CLAIM) | Asserts that an enabling condition or capability facilitates an outcome. enabling condition. | aliases: facilitates, allows  ⟵ candidate
- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ candidate
- leads_to | claim_relation | CLAIM leads_to(cause: TERM, effect: TERM) | Asserts a conceptual consequence or progression from cause to effect. progression relation. | aliases: results_in  ⟵ candidate
- meets_needs | claim_relation | CLAIM meets_needs(subject: TERM, beneficiary: STRING / TERM) | Asserts that an item, activity, or plan satisfies the needs of a beneficiary. utility/satisfaction claim. | aliases: satisfies_needs  ⟵ candidate
- menu_works | claim_relation | CLAIM menu_works(property: STRING) | Asserts that a menu or recipe plan satisfies an operational criterion. menu evaluation. | aliases: menu_satisfies  ⟵ candidate
- occurred_recently | claim_relation | CLAIM occurred_recently(target: CLAIM) | Asserts temporal recency of an asserted occurrence or claim. temporal recency qualifier. | aliases: recently_happened  ⟵ candidate
- ongoing | claim_relation | CLAIM ongoing(target: TERM) | Asserts that a conflict, process, or initiative is actively ongoing. temporal aspect claim. | aliases: in_progress  ⟵ candidate
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ candidate
- raises_exception | claim_relation | CLAIM raises_exception(target?: TERM, exception_type: STRING, message?: STRING) | Asserts that an unhandled runtime error or exception was raised with the specified exception type, message, and target entity. | not: warning (a non-fatal library warning or deprecation notice) or failure (a general system failure hypothesis) | aliases: raises, exception, throws_error, type_error  ⟵ candidate
- request | claim_relation | CLAIM request(target: TERM / STRING) | Represents an active communicative request or constraint state in conversation tracking. target is the requested action or topic. | aliases: user_request  ⟵ candidate
- validates_parameter | claim_relation | CLAIM validates_parameter(condition: STRING, entity: TERM, parameter: STRING) | Asserts that a code entity inspects or validates parameter names or types for a specified condition. | not: a runtime assertion test | aliases: inspects_parameter, checks_parameter, validates_parameter_names  ⟵ candidate

### links

- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ candidate
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ candidate
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ candidate

### values

- art_plan | value | artifact-value | Actionable plan.  ⟵ candidate
- art_structured_report | value | artifact-value | Headed/structured report.  ⟵ candidate
- path_gcloud_pubsub_subscription_py | value | code-value | File path to the Google Cloud Pub/Sub subscription module. | aliases: gcloud_pubsub_subscription_path  ⟵ candidate
- path_ipython_core_magics_basic_py | value | code-value | File path to the IPython basic magics module. | not: an individual command line script or general config file | aliases: IPython/core/magics/basic.py, ipython_core_magics_basic_py  ⟵ candidate
- path_numpy_core_fromnumeric_py | value | code-value | Source code file path or exported symbol in scientific Python: path_numpy_core_fromnumeric_py. | aliases: path_numpy_core_fromnumeric_py  ⟵ candidate
- path_pandas_src_testing_pyx | value | code-value | Source code file path or exported symbol in scientific Python: path_pandas_src_testing_pyx. | aliases: path_pandas_src_testing_pyx  ⟵ candidate
- path_sklearn_linear_model_logistic_py | value | code-value | The scikit-learn logistic module path.  ⟵ candidate
- sym_log_reg_scoring_path | value | code-value | The _log_reg_scoring_path program symbol.  ⟵ candidate
- sym_pandas_testing_assert_almost_equal | value | code-value | Source code file path or exported symbol in scientific Python: sym_pandas_testing_assert_almost_equal. | aliases: sym_pandas_testing_assert_almost_equal  ⟵ candidate
- constitutional_ai | value | descriptive-value | Concept of rule-based constitutional training and self-critique principles in AI alignment. | aliases: constitutional_ai  ⟵ candidate
- design_parameters | value | descriptive-value | Concept of operational and behavioral design specifications for AI systems. | aliases: design_parameters  ⟵ candidate
- dom_ddp | value | descriptive-value | DistributedDataParallel (DDP) multi-GPU distributed training configuration and execution paradigm. | not: dom_ovr (one-versus-rest classification) or platform_label::python (general Python runtime) | aliases: DDP, DistributedDataParallel, distributed data parallel  ⟵ candidate
- dom_sgi | value | descriptive-value | SGI domain concept.  ⟵ candidate
- mod_mixed_case | value | descriptive-value | Mixed-case modifier. | aliases: mixed case  ⟵ candidate
- unit_item | value | duration-unit-value | Top-level generated list or report item. | aliases: items, entries  ⟵ candidate
- cd | value | entity-name | A compact disc physical object. | not: a digital media file or streaming track | aliases: CD, compact_disc  ⟵ candidate
- clock | value | entity-name | A clock timepiece appliance. | not: duration units like unit_hour | aliases: clock, timer  ⟵ candidate
- coffee_maker | value | entity-name | A coffee-making appliance; not automatically a heating resource  ⟵ candidate
- recycle_bin | value | entity-name | A dedicated receptacle container for recyclable waste materials. | not: trash_can (a general waste receptacle container) | aliases: recycle bin, recycling bin, recycle_bin  ⟵ candidate
- resource_chiller | value | entity-name | Canonical abstract chilling resource when no particular appliance is named.  ⟵ candidate
- resource_heater | value | entity-name | Canonical abstract heating resource when no particular appliance is named.  ⟵ candidate
- resource_sink | value | entity-name | Canonical abstract washing resource when no particular sink is named.  ⟵ candidate
- format_structured_report | value | format-value | Headed structured report layout. | aliases: structured report, report  ⟵ candidate
- metric_compatibility | value | metric-value | Compatibility status. | aliases: compatible  ⟵ candidate
- size_medium | value | product-attribute-value | Medium size. | aliases: medium, M  ⟵ candidate
- shape_oval | value | shape-value | Oval. | aliases: oval  ⟵ candidate
- shape_triangular | value | shape-value | Triangular. | aliases: triangular, triangle  ⟵ candidate
- topic_baldurs_gate_3 | value | topic-value | Baldur's Gate 3.  ⟵ candidate

### attributes

- ram_unit | attribute | attribute-name | Unit for min_ram from capacity-unit-value.  ⟵ candidate
- target | attribute | attribute-name | The acted-on entity or generated artifact.  ⟵ candidate
