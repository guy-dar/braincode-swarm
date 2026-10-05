# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 14 needs (decomposition: llm), 87 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | speech_act | t1:s1 | Introduce a set of custom mathematical operations. | `rule_operations_general`, `calculation`, `conditional`, `sequence`, `inform`, `design_parameters`, `format_numbered_list`, `respond`, `extract`, `example_of`, `propose`, `modify_code` |
| n2 | claim | t1:s2 | Define the custom operation '&' using conditional logic and absolute difference. | `conditional`*, `calculation`, `motivated_by`, `example_of`, `test_condition`, `rule_operations_general`, `extract`, `constrained_by`, `rule_support_primitives_general`, `enables`, `validates_parameter`, `distinguish` |
| n3 | claim | t1:s3 | Define the custom operation '<>' based on whether the product is positive. | `calculation`, `check_reservation_availability`, `test_condition`, `conditional`, `assert_multinomial_scorer`, `example_of`, `validates_parameter`, `outcome`, `constrained_by`, `enables`, `menu_works`, `decision` |
| n4 | claim | t1:s4 | Define the custom operation '#' using the greatest common divisor (gcd). | `calculation`, `example_of`, `rule_operations_general`, `outcome`, `constrained_by`, `enables`, `rule_category_entity_name`, `user_practice`, `mod_mixed_case`, `validates_parameter`, `conjunction`, `leads_to` |
| n5 | claim | t1:s5 | Define the custom operation '~' using conditional logic on the second operand. | `conditional`*, `calculation`, `constrained_by`, `enables`, `unit_second`*, `test_condition`, `extract`, `rule_operations_general`, `reason_for`, `example_c_existing_constraint_symbol_becomes_a_typed_construction`, `outcome`, `decision` |
| n6 | claim | t1:s6 | Define the custom operation ';' based on the result of the '&' operation. | `calculation`, `rule_operations_general`, `extract`, `constrained_by`, `example_of`, `sequence`, `conditional`, `test_condition`, `user_practice`, `instantiates`, `enables`, `outcome` |
| n7 | claim | t1:s7 | Define the custom operation ':' based on whether either operand is prime. | `calculation`, `constrained_by`, `extract`, `rule_operations_general`, `validates_parameter`, `test_condition`, `decision`, `enables`, `conditional`, `modify_code`, `outcome`, `rule_support_primitives_general` |
| n8 | claim | t1:s8 | Define the operator chaining notation 'a <op1><op2> b' as '(a op1 b) op2 b'. | `rule_reading_guide`, `motivated_by`, `calculation`, `example_of`, `extract`, `instantiates`, `rule_operations_general`, `duplicate_definition`, `sequence`, `conditional`, `enables`, `leads_to` |
| n9 | claim | t1:s9 | Provide examples of the operator chaining notation. | `example_of`*, `example_c_existing_constraint_symbol_becomes_a_typed_construction`, `provides`*, `calculation`, `extract`, `rule_operations_general`, `conditional`, `sequence`, `maximum_between_stops`, `at_least`, `rule_support_primitives_general`, `rule_reading_guide` |
| n10 | claim | t1:s10 | Define variable A using a complex expression with custom operations and word-numbers. | `unit_word`*, `calculation`, `example_of`, `code_entity`, `constrained_by`, `example_c_existing_constraint_symbol_becomes_a_typed_construction`, `rule_operations_general`, `measure`, `extract`, `enables`, `character`, `rule_support_primitives_general` |
| n11 | claim | t1:s11 | Define variable B using a complex expression with custom operations and word-numbers. | `calculation`, `unit_word`*, `duplicate_definition`, `code_entity`, `example_of`, `example_c_existing_constraint_symbol_becomes_a_typed_construction`, `rule_operations_general`, `constrained_by`, `test_condition`, `character`, `extract`, `enables` |
| n12 | claim | t1:s12 | Define variable C using a complex expression with custom operations and word-numbers. | `calculation`, `unit_word`*, `example_c_existing_constraint_symbol_becomes_a_typed_construction`, `example_of`, `code_entity`, `constrained_by`, `rule_operations_general`, `conditional`, `character`, `enables`, `measure`, `rule_support_primitives_general` |
| n13 | action | t1:s13 | Compute the final value of the expression A + B - C. | `calculation`, `unit_character`, `extract`, `maximum_between_stops`, `test_condition`, `conditional`, `at_least`, `assert_multinomial_scorer`, `decision`, `activity`, `duration`, `minimum_per_period` |
| n14 | constraint | t1:s14 | Format the final answer as a number. | `format_numbered_list`, `extract`, `respond`*, `unit_character`, `calculation`, `measure`, `metric_order_late`, `metric_response_time`, `quantity`, `duration`, `tone_concise`, `constraint_budget_limited` |

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
- check_reservation_availability.currency → currency
- check_reservation_availability.location → country
- provides.actor → platform_label
- provides.subject → platform_label
- code_entity.project → platform_label
- measure.unit → currency
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

**rule_reading_guide** (v19/rule/reading-guide; candidate)

The spec governs syntax/types; this glossary defines vocabulary. Signature notation: ? optional, A / B explicit alternatives, void no result. Omitted optional arguments are unspecified. Value entries are category-refined STRING primitives; complex meanings require composition. Aliases are contextual hints, not unconditional equivalences. Report ambiguity. IDs use v19/<category>/<symbol>, v19/support/<symbol> or v19/composite/<symbol>. Statuses apply to this candidate: Retained preserves meaning; Adapted uses the stated contract; Composite requires TERM (bare STRING deprecated); Structural is syntax/argument vocabulary; Needs clarification is unusable until resolved; Deprecated is historical; Accepted is usable within this candidate.

**rule_recording_signatures** (v19/rule/recording-signatures; rule governing extract)

RECORD ACTION uses the operation signature with REF[STRING] → TERM and LIST[REF[STRING]] → LIST[TERM]; other types/categories stay unchanged. Return EVENT, never the runtime result. Record actual outputs as attributed CLAIMs. Do not infer missing resources.

**rule_speech_acts_general** (v19/rule/speech-acts-general; rule governing inform)

UTTER-only, void, with the spec's speech attributes and LIST[TERM] constraints. No result binding. Literal content cannot replace required semantic arguments for structured coverage.

**rule_structural_constructs** (v19/rule/structural-constructs; core)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; rule governing example_of)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_attributes_and_generate** (v19/rule/attributes-and-generate; rule governing quantity)

Attribute entries name arguments; legality/types come from each operation, not global membership. GENERATE uses the spec's core fields; retained artifact profiles return STRING. Numeric/list results need explicit profiles. Legacy itinerary fields expand to TERM constraints: duration/duration_unit → duration(amount,unit); stop_min_per_day/stop_requirement → minimum_per_period(class,count,period=unit_day), never an inferred temple class; max_walk_duration/unit → maximum_between_stops(activity="walk",amount,unit). No legacy shorthand is enabled. Old events/character_properties/transformations become explicitly scoped TERM constraints. Message purpose is TERM, not send_email.content: GENERATE exact STRING content, then send. Report opaque fallback separately.

**rule_category_code_value** (v19/rule/category/code-value; rule governing assert_multinomial_scorer)

path_/sym_ remain STRING identities; migrated chg_/assert_ are TERM constructors. Do not recover an exact file path by guessing from underscores.

**rule_category_constraint_value** (v19/rule/category/constraint-value; rule governing constraint_exclude_flowery_language)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_descriptive_value** (v19/rule/category/descriptive-value; rule governing design_parameters)

STRING modifier/domain label; never a free-form proposition. dom_sgi needs its intended referent established before semantically dependent use.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; rule governing unit_second)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; candidate)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_format_value** (v19/rule/category/format-value; rule governing format_numbered_list)

STRING format. format_email is layout, not the action send_email.

**rule_category_metric_value** (v19/rule/category/metric-value; rule governing metric_order_late)

STRING metric identity, not a Boolean value. Uptime and response time need numeric observations with units; order-late is Boolean-valued. Do not type every metric as BOOL.

**rule_category_tone_value** (v19/rule/category/tone-value; rule governing tone_concise)

STRING register. tone_urgent describes urgency, not a concrete deadline.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_pickup_lines)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_composites_general** (v19/rule/composites-general; rule governing assert_multinomial_scorer)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_examples_general** (v19/rule/examples-general; rule governing example_c_existing_constraint_symbol_becomes_a_typed_construction)

Examples use this glossary's contracts. They have not been verified by an implemented BrainCode parser.

**rule_operations_general** (v19/rule/operations-general; candidate)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_supplemental_general** (v19/rule/supplemental-general; rule governing extract)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; candidate)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- check_reservation_availability | operation | operation-vocabulary | (target: STRING, cuisine?: STRING, currency?: STRING / ATOM[currency], location?: STRING / ATOM[country], max_price?: NUMBER) -> BOOL | Check current availability under supplied filters. A positive result does not make a reservation. | aliases: check reservation availability  ⟵ candidate
- extract | operation | operation-vocabulary | (target: LIST[REF[STRING]], limit: NUMBER) -> LIST[REF[STRING]] | First limit results, preserving order and identity; limit is a nonnegative integer; limit=1 is still a list  ⟵ candidate
- modify_code | operation | operation-vocabulary | (target: STRING / ATOM[platform_label], file: STRING, revision: TERM, method?: STRING) -> void | Apply the structured change to the indicated code. A method name alone does not specify the change. | aliases: fix, reduce, optimize  ⟵ candidate

### speech acts

- ask | speech_act | operation-vocabulary | UTTER ask(target: TERM, or a sufficiently precise topic: STRING / TERM) | Request information/advice; not an assertion of an answer. | aliases: ask, how should  ⟵ dependency of example_c_existing_constraint_symbol_becomes_a_typed_construction
- inform | speech_act | operation-vocabulary | UTTER inform(target: CLAIM) | Present the proposition; preserve its holder/status.  ⟵ candidate
- propose | speech_act | operation-vocabulary | UTTER propose(target: TERM) | Suggest an action/idea; does not record it as performed.  ⟵ candidate
- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ candidate
- at_least | constructor | TERM at_least(measure: TERM) -> TERM | A lower bound: the constrained value is greater than or equal to the given measure (or number term). Use inside requirement(value=...). | not: an exact value; a strict 'more than' only when the source says so explicitly | aliases: at least, minimum, or more, no less than, plus  ⟵ candidate
- calculation | constructor | TERM calculation(inputs: LIST[TERM], operation: STRING, result?: TERM) -> TERM | Constructs a descriptive representation of an arithmetic or algorithmic calculation step with inputs, operation identifier, and optional resulting value. | not: an executed runtime action or factual claim of outcome | aliases: math_operation, compute_step  ⟵ candidate
- character | constructor | TERM character(name: STRING, series?: STRING) -> TERM | Constructs a descriptive representation of a fictional or narrative character. name specifies the character identifier. | aliases: fictional_character  ⟵ candidate
- code_entity | constructor | TERM code_entity(file?: STRING / TERM, kind: STRING, name: STRING, project?: STRING / ATOM[platform_label]) -> TERM | Constructs a structured descriptor for a source code entity such as a function, method, class, module, or source file within a project. | not: an executed runtime call or file system operation | aliases: code_function, source_file, code_symbol  ⟵ candidate
- conditional | constructor | TERM conditional(condition: TERM, consequence: TERM) -> TERM | Constructs a structured conditional proposition term connecting a condition and consequence. descriptive logic structure. | aliases: if_then  ⟵ candidate
- conjunction | constructor | TERM conjunction(items: LIST[TERM]) -> TERM | All described components apply | not: Does not imply temporal order  ⟵ candidate
- decision | constructor | TERM decision(activity: TERM) -> TERM | A decision whose content is the described activity | not: Not proof it was carried out  ⟵ candidate
- distinguish | constructor | TERM distinguish(first: TERM, second: TERM, criterion?: STRING / TERM) -> TERM | Constructs a descriptive representation of discerning or differentiating between two entities, conditions, or behaviors along an optional criterion. | not: visual_contrast (optical contrast) or LINK contrast (rhetorical opposition between claims) | aliases: tell the difference, differentiate, distinguish between  ⟵ candidate
- duration | constructor | TERM duration(amount: NUMBER, unit: STRING) -> TERM | Requested elapsed/calendar extent | not: Word/item counts are not time  ⟵ candidate
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ dependency of constraint_exclude_flowery_language
- maximum_between_stops | constructor | TERM maximum_between_stops(activity: STRING, amount: NUMBER, unit: STRING) -> TERM | Upper bound on the stated activity between successive stops | not: Not a limit on total daily duration  ⟵ candidate
- measure | constructor | TERM measure(amount: NUMBER, unit: STRING / ATOM[currency]) -> TERM | A measured amount: a number with its unit symbol (a unit-category value such as unit_minute, cap_gb or currency::USD). Describes the amount only; asserts nothing. ATOM[currency] is also accepted and supplies the pinned currency identity; no exchange rate or conversion is implicit. | not: a symbol with the number baked in (char_age_18, size_16gb); a unitless count (use the quantity argument) | aliases: amount of, size of, measured in  ⟵ candidate
- minimum_per_period | constructor | TERM minimum_per_period(class: STRING, count: NUMBER, period: STRING) -> TERM | At least count members of class in each period | not: Not a minimum total over the whole artifact  ⟵ candidate
- naming_pattern | constructor | TERM naming_pattern(description: STRING, context?: STRING) -> TERM | Constructs a descriptive naming or morphological pattern. used for rule-based or conventional naming schemes. | aliases: pattern_naming  ⟵ candidate
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ dependency of constraint_budget_limited
- sequence | constructor | TERM sequence(items: LIST[TERM]) -> TERM | Ordered described activities/content | not: Not unordered conjunction  ⟵ candidate
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ dependency of reason_for
- test_condition | constructor | TERM test_condition(condition: STRING, expected: BOOL) -> TERM | A testable condition with the expected Boolean outcome | not: Expected outcome is not an observed result  ⟵ candidate

### composites

- assert_multinomial_scorer | composite | code-value | TERM assert_multinomial_scorer() -> TERM | Assertion that multinomial probabilistic scoring succeeds. | = test_condition(condition="multinomial_probabilistic_scoring", expected=TRUE)  ⟵ candidate
- constraint_budget_limited | composite | constraint-value | TERM constraint_budget_limited() -> TERM | Limited budget. | = requirement(property="budget_limited", value=TRUE)  ⟵ candidate
- constraint_exclude_flowery_language | composite | constraint-value | TERM constraint_exclude_flowery_language() -> TERM | Avoid flowery language. | = exclude(item="flowery_language")  ⟵ candidate
- constraint_realistic | composite | constraint-value | TERM constraint_realistic() -> TERM | Must be realistic. | = requirement(property="realistic", value=TRUE)  ⟵ dependency of example_c_existing_constraint_symbol_becomes_a_typed_construction

### claim relations

- constrained_by | claim_relation | CLAIM constrained_by(activity: TERM, constraint: TERM) | Asserts that an activity or operation is governed or restricted by a constraint. governance/constraint claim. | aliases: restricted_by  ⟵ candidate
- duplicate_definition | claim_relation | CLAIM duplicate_definition(count: NUMBER, entity: TERM, location?: STRING / TERM) | Asserts that multiple duplicate copies or definitions of a code entity exist within a codebase or location. | not: an exact string equality check | aliases: duplicate_code, two_copies, duplicate_function  ⟵ candidate
- enables | claim_relation | CLAIM enables(condition: TERM / CLAIM, outcome: TERM / CLAIM) | Asserts that an enabling condition or capability facilitates an outcome. enabling condition. | aliases: facilitates, allows  ⟵ candidate
- example_of | claim_relation | CLAIM example_of(example: TERM, concept: TERM) | Asserts that an instance or term exemplifies a general concept, pattern, or category. example and concept are descriptive terms. | aliases: exemplifies, instance_of  ⟵ candidate
- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ core
- instantiates | claim_relation | CLAIM instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) | Asserts that a code entity or constructor instantiates a target class or object under an optional condition. | not: an executed runtime object creation (pure factual assertion about code structure) | aliases: creates_instance, constructs_instance  ⟵ candidate
- leads_to | claim_relation | CLAIM leads_to(cause: TERM, effect: TERM) | Asserts a conceptual consequence or progression from cause to effect. progression relation. | aliases: results_in  ⟵ candidate
- menu_works | claim_relation | CLAIM menu_works(property: STRING) | Asserts that a menu or recipe plan satisfies an operational criterion. menu evaluation. | aliases: menu_satisfies  ⟵ candidate
- motivated_by | claim_relation | CLAIM motivated_by(claim: CLAIM, motive: STRING / TERM) | Asserts that an action, rule, or claim is motivated by an underlying motive or goal. motive explanation. | aliases: rationale_is  ⟵ candidate
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ candidate
- provides | claim_relation | CLAIM provides(actor: STRING / TERM / ATOM[platform_label], subject: STRING / TERM / ATOM[platform_label]) | Asserts that an establishment, organization, or provider supplies a specified item or service. provision claim. | aliases: supplies  ⟵ candidate
- reason_for | claim_relation | CLAIM reason_for(subject: CLAIM / TERM, reason: STRING / TERM) | Asserts an explanatory reason for a policy, belief, or state of affairs. explanatory reason. | aliases: basis_for  ⟵ candidate
- user_practice | claim_relation | CLAIM user_practice(activity: TERM) | Asserts a habitual, workflow, or recurring practice of a user. workflow practice. | aliases: habitual_activity  ⟵ candidate
- validates_parameter | claim_relation | CLAIM validates_parameter(condition: STRING, entity: TERM, parameter: STRING) | Asserts that a code entity inspects or validates parameter names or types for a specified condition. | not: a runtime assertion test | aliases: inspects_parameter, checks_parameter, validates_parameter_names  ⟵ candidate

### links

- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ core
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ core
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ core

### values

- design_parameters | value | descriptive-value | Concept of operational and behavioral design specifications for AI systems. | aliases: design_parameters  ⟵ candidate
- mod_mixed_case | value | descriptive-value | Mixed-case modifier. | aliases: mixed case  ⟵ candidate
- unit_character | value | duration-unit-value | One Unicode scalar value in the final rendered artifact; line endings are normalized to LF before counting. | aliases: characters, chars  ⟵ candidate
- unit_minute | value | duration-unit-value | Minute. | aliases: minutes, min  ⟵ candidate
- unit_second | value | duration-unit-value | Second. | aliases: seconds, sec  ⟵ candidate
- unit_word | value | duration-unit-value | Rendered whitespace-delimited word. | aliases: words  ⟵ candidate
- format_numbered_list | value | format-value | Numbered list. | aliases: numbered steps  ⟵ candidate
- metric_order_late | value | metric-value | Whether an order is late. | aliases: order is late, delayed  ⟵ candidate
- metric_response_time | value | metric-value | Support response time. | aliases: response time  ⟵ candidate
- tone_concise | value | tone-value | Brief, to-the-point register. | aliases: briefly, concisely  ⟵ candidate
- topic_pickup_lines | value | topic-value | Pickup lines.  ⟵ dependency of example_c_existing_constraint_symbol_becomes_a_typed_construction

### attributes

- quantity | attribute | attribute-name | Explicit count as NUMBER.  ⟵ candidate

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

