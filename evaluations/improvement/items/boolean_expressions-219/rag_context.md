# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 18 needs (decomposition: llm), 145 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | speech_act | t1:s2 | Ask which of the five given expressions evaluates to true. | `ask`*, `respond`, `inform`, `confirm`, `decline`, `assert_multinomial_scorer`, `acknowledge`, `extract`, `propose`, `apologize`, `test_condition`, `express_interest` |
| n2 | constraint | t1:s1 | Only one of the five expressions evaluates to true. | `extract`, `constraint_single_choice`, `assert_multinomial_scorer`, `test_condition`, `constraint_exclude_flowery_language`, `constraint_exclude_liberation_theme`, `constraint_budget_limited`, `constraint_respectful`, `failure`, `constraint_comprehensive`, `confirm`, `decline` |
| n3 | action | t1:s3, t1:s4, t1:s5, t1:s6, t1:s7, t1:s8, t1:s9, t1:s10, t1:s11, t1:s12 | Evaluate nested boolean logic expressions with NOT, AND, and OR operators. | `test_condition`, `negation`, `conditional`, `calculation`, `motivated_by`, `extract`, `subject`, `distinguish`, `run_tests`, `decision`, `rule_operations_general`, `validates_parameter` |
| n4 | action | t1:s3, t1:s4, t1:s5, t1:s6, t1:s7, t1:s8, t1:s9, t1:s10, t1:s11, t1:s12 | Evaluate arithmetic operations and comparisons. | `calculation`, `extract`, `measure`, `test_condition`, `decision`, `assert_multinomial_scorer`, `run_tests`, `quantity`, `chill`, `wait`, `sequence`, `rate` |
| n5 | action | t1:s3, t1:s5, t1:s6, t1:s8, t1:s9, t1:s11, t1:s12 | Evaluate min and max functions on lists of numbers. | `extract`, `calculation`, `unit_minute`*, `format_numbered_list`, `at_most`, `minimum_per_period`, `at_least`, `maximum_between_stops`, `check_reservation_availability`, `quantity`, `unit_week`, `block_evaluation` |
| n6 | object | t1:s3 | Verify the capital of Gambia (Libreville). → `country::<key>` | `country`*, `africa`, `afcfta`, `eastern_cape`, `currency`, `united_kingdom`, `locale_en_gb`, `locale_fr`, `ukraine`, `confirm`, `pencil`, `coffee_maker` |
| n7 | object | t1:s4, t1:s11 | Verify the capital of Afghanistan (Kandahar, Kabul). → `country::<key>` | `ukraine`, `locale_en_gb`, `country`*, `russia`, `content_kyoto_itinerary`, `class_town`, `united_kingdom`, `confirm`, `locale_en_us`, `resource_chiller`, `location_spec`, `unit_kilometer` |
| n8 | object | t1:s6 | Verify the capital of Cameroon (Douala). → `country::<key>` | `country`*, `africa`, `afcfta`, `eastern_cape`, `currency`, `locale_en_gb`, `united_kingdom`, `locale_fr`, `confirm`, `locale_zh`, `dom_safari`, `inform` |
| n9 | object | t1:s7 | Verify the capital of Germany (Berlin). → `country::<key>` | `ukraine`, `locale_de`, `locale_fr`, `country`*, `russia`, `tone_neutral`, `tone_formal`, `liberal_onsen`, `confirm`, `japanese_government`, `resource_chiller`, `locale_en_gb` |
| n10 | object | t1:s9 | Verify the capital of Belarus (Grodno). → `country::<key>` | `country`*, `ukraine`, `russia`, `currency`, `locale_fr`, `tone_neutral`, `unit_gram`, `yakuza`, `japanese_government`, `resource_chiller`, `confirm`, `locale_de` |
| n11 | object | t1:s11 | Verify the capital of Nepal (Kathmandu). → `country::<key>` | `country`*, `africa`, `united_kingdom`, `locale_zh`, `confirm`, `inform`, `locale_fr`, `class_temple`, `validates_parameter`, `constitutional_ai`, `resource_sink`, `location_spec` |
| n12 | object | t1:s12 | Verify the capital of UAE (Abu Dhabi). → `country::<key>` | `country`*, `united_kingdom`, `cuisine_arab`, `confirm`, `currency`, `eastern_cape`, `sultana`, `inform`, `acknowledge`, `validates_parameter`, `island`, `sun` |
| n13 | object | t1:s12 | Verify the capital of Norway (Bergen). → `country::<key>` | `ukraine`, `russia`, `country`*, `locale_fr`, `tone_formal`, `locale_de`, `tone_neutral`, `confirm`, `content_kyoto_itinerary`, `resource_chiller`, `onsen`, `japanese_government` |
| n14 | object | t1:s3, t1:s4 | Expression A | `extract`, `coffee_maker`, `express_interest`, `resource_sink`, `subject`, `resource_chiller`, `instantiates`, `address_form`, `right_of`, `code_entity`, `rule_support_primitives_general`, `chill` |
| n15 | object | t1:s5, t1:s6 | Expression B | `extract`, `subject`, `coffee_maker`, `resource_sink`, `express_interest`, `character_trait`, `resource_chiller`, `example_c_existing_constraint_symbol_becomes_a_typed_construction`, `code_entity`, `rule_support_primitives_general`, `transform_remove_br`, `chill` |
| n16 | object | t1:s7, t1:s8 | Expression C | `example_c_existing_constraint_symbol_becomes_a_typed_construction`, `coffee_maker`, `extract`, `calculation`, `code_entity`, `resource_sink`, `resource_chiller`, `rule_support_primitives_general`, `conjunction`, `character_trait`, `chair`, `chill` |
| n17 | object | t1:s9, t1:s10 | Expression D | `locale_fr`, `rule_support_primitives_general`, `tone_empathetic`, `unit_word`, `subject`, `locale_de`, `transform_remove_br`, `coffee_maker`, `resource_sink`, `resource_chiller`, `character`, `chill` |
| n18 | object | t1:s11, t1:s12 | Expression E | `tone_empathetic`, `extract`, `locale_es`, `locale_hi_en`, `example_e_preserve_exact_wording_through_generation_and_sending`, `calculation`, `coffee_maker`, `resource_chiller`, `egift_card`, `resource_sink`, `express_interest`, `rule_support_primitives_general` |

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

- run_tests.target → platform_label
- failure.system → platform_label
- subject.qualifier → platform_label
- subject.location → country
- measure.unit → currency
- chill.destination → object_label
- check_reservation_availability.currency → currency
- check_reservation_availability.location → country
- code_entity.project → platform_label
- requirement.value → platform_label
- activity.object → object_label, food_label, animal_label
- activity.location → country
- activity.instrument → object_label, platform_label

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

**rule_trace_relations_general** (v19/rule/trace-relations-general; rule governing failure)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_attributes_and_generate** (v19/rule/attributes-and-generate; rule governing quantity)

Attribute entries name arguments; legality/types come from each operation, not global membership. GENERATE uses the spec's core fields; retained artifact profiles return STRING. Numeric/list results need explicit profiles. Legacy itinerary fields expand to TERM constraints: duration/duration_unit → duration(amount,unit); stop_min_per_day/stop_requirement → minimum_per_period(class,count,period=unit_day), never an inferred temple class; max_walk_duration/unit → maximum_between_stops(activity="walk",amount,unit). No legacy shorthand is enabled. Old events/character_properties/transformations become explicitly scoped TERM constraints. Message purpose is TERM, not send_email.content: GENERATE exact STRING content, then send. Report opaque fallback separately.

**rule_category_artifact_value** (v19/rule/category/artifact-value; rule governing art_short_text)

STRING artifact class for GENERATE.target. art_story says what kind of artifact to produce, not what occurs in its plot.

**rule_category_code_value** (v19/rule/category/code-value; rule governing assert_multinomial_scorer)

path_/sym_ remain STRING identities; migrated chg_/assert_ are TERM constructors. Do not recover an exact file path by guessing from underscores.

**rule_category_constraint_value** (v19/rule/category/constraint-value; rule governing constraint_single_choice)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_content_value** (v19/rule/category/content-value; rule governing content_kyoto_itinerary)

Existing compounds become the constructors in Section 5. Their outputs go in topic/target/constraints as appropriate, not content, whose spec type remains STRING.

**rule_category_cuisine_value** (v19/rule/category/cuisine-value; rule governing cuisine_arab)

STRING cuisine class; cuisine_indian is a cuisine filter, not the location India.

**rule_category_descriptive_value** (v19/rule/category/descriptive-value; rule governing dom_safari)

STRING modifier/domain label; never a free-form proposition. dom_sgi needs its intended referent established before semantically dependent use.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; rule governing unit_minute)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing afcfta)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_format_value** (v19/rule/category/format-value; rule governing format_numbered_list)

STRING format. format_email is layout, not the action send_email.

**rule_category_locale_value** (v19/rule/category/locale-value; rule governing locale_en_gb)

STRING locale. “English” alone does not always mean locale_en_us; preserve ambiguity.

**rule_category_location_name** (v19/rule/category/location-name; rule governing africa)

STRING location descriptor. A `table` surface is not the generated artifact category art_table.

**rule_category_recipient_value** (v19/rule/category/recipient-value; rule governing japanese_government)

STRING roles or explicit named recipients. A role is not an exact person's identity. Keep an explicit name where substituting a role loses information.

**rule_category_semantic_category_value** (v19/rule/category/semantic-category-value; rule governing class_town)

STRING class label used by typed constraints. class_temple describes a class, not an acquired physical temple reference.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing right_of)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_tone_value** (v19/rule/category/tone-value; rule governing tone_neutral)

STRING register. tone_urgent describes urgency, not a concrete deadline.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_pickup_lines)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_category_transformation_value** (v19/rule/category/transformation-value; rule governing transform_remove_br)

TERM-described transformation. Pass it through constraints; no ungoverned transformations attribute.

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
- chill | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Chill using the stated resource; same identity.  ⟵ candidate
- extract | operation | operation-vocabulary | (target: LIST[REF[STRING]], limit: NUMBER) -> LIST[REF[STRING]] | First limit results, preserving order and identity; limit is a nonnegative integer; limit=1 is still a list  ⟵ candidate
- run_tests | operation | operation-vocabulary | (target: STRING / ATOM[platform_label], assertion?: TERM) -> BOOL | Run the selected project's tests, optionally checking the specified assertion. TRUE means the declared test condition passed, not overall software correctness.  ⟵ candidate
- send_email | operation | operation-vocabulary | (recipient: STRING, content: STRING, tone?: STRING) -> void | Send supplied exact message content to the identified recipient. A requested message purpose is not already a composed message. | aliases: email  ⟵ dependency of example_e_preserve_exact_wording_through_generation_and_sending
- wait | operation | operation-vocabulary | (duration?: NUMBER) -> void | Pause execution for a duration or cycle. duration in seconds or ticks. | aliases: idle, pause  ⟵ candidate

### speech acts

- apologize | speech_act | UTTER apologize(target?: CLAIM / TERM) | Speech act expressing apology or regret for an outcome or target. | not: decline (which is refusing) | aliases: apologize, apology, sorry  ⟵ candidate
- acknowledge | speech_act | operation-vocabulary | UTTER acknowledge(target: CLAIM / TERM) | Acknowledge receipt/awareness; does not imply agreement.  ⟵ candidate
- ask | speech_act | operation-vocabulary | UTTER ask(target: TERM, or a sufficiently precise topic: STRING / TERM) | Request information/advice; not an assertion of an answer. | aliases: ask, how should  ⟵ candidate
- confirm | speech_act | operation-vocabulary | UTTER confirm(target: CLAIM) | Confirm the proposition; its evidence/status remains explicit.  ⟵ candidate
- decline | speech_act | operation-vocabulary | UTTER decline(target: TERM) | Decline the represented request/proposal; not negate every proposition within it.  ⟵ candidate
- express_interest | speech_act | operation-vocabulary | UTTER express_interest(target: STRING / TERM) | Speech act expressing conversational interest or engagement in a topic. speech act in dialogic traces. | aliases: show_interest  ⟵ candidate
- inform | speech_act | operation-vocabulary | UTTER inform(target: CLAIM) | Present the proposition; preserve its holder/status.  ⟵ candidate
- propose | speech_act | operation-vocabulary | UTTER propose(target: TERM) | Suggest an action/idea; does not record it as performed.  ⟵ candidate
- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ dependency of decision
- address_form | constructor | TERM address_form(form: STRING / TERM, subject: STRING / TERM) -> TERM | Constructs a descriptive term representing a convention, title, or manner of addressing a person or group. | not: a postal address or email destination | aliases: address_as, manner_of_address, form_of_address  ⟵ candidate
- at_least | constructor | TERM at_least(measure: TERM) -> TERM | A lower bound: the constrained value is greater than or equal to the given measure (or number term). Use inside requirement(value=...). | not: an exact value; a strict 'more than' only when the source says so explicitly | aliases: at least, minimum, or more, no less than, plus  ⟵ candidate
- at_most | constructor | TERM at_most(measure: TERM) -> TERM | An upper bound: the constrained value is less than or equal to the given measure (or number term). Use inside requirement(value=...). | not: an exact value or a target to aim for | aliases: at most, maximum, up to, no more than, under  ⟵ candidate
- block_evaluation | constructor | TERM block_evaluation(block: STRING / TERM, maturity?: STRING, potential?: STRING, quality?: STRING, rank?: NUMBER, traps?: STRING) -> TERM | Constructs a structured evaluation, categorization, or ranking descriptor for a geological exploration block. | not: an external execution action or generic list sorting operation (use sort) | aliases: block assessment, block ranking, block rating, block categorization  ⟵ candidate
- calculation | constructor | TERM calculation(inputs: LIST[TERM], operation: STRING, result?: TERM) -> TERM | Constructs a descriptive representation of an arithmetic or algorithmic calculation step with inputs, operation identifier, and optional resulting value. | not: an executed runtime action or factual claim of outcome | aliases: math_operation, compute_step  ⟵ candidate
- character | constructor | TERM character(name: STRING, series?: STRING) -> TERM | Constructs a descriptive representation of a fictional or narrative character. name specifies the character identifier. | aliases: fictional_character  ⟵ candidate
- character_trait | constructor | TERM character_trait(property: STRING, value: STRING / NUMBER) -> TERM | A character attribute | not: Not a claim about a real person  ⟵ candidate
- code_entity | constructor | TERM code_entity(file?: STRING / TERM, kind: STRING, name: STRING, project?: STRING / ATOM[platform_label]) -> TERM | Constructs a structured descriptor for a source code entity such as a function, method, class, module, or source file within a project. | not: an executed runtime call or file system operation | aliases: code_function, source_file, code_symbol  ⟵ candidate
- conditional | constructor | TERM conditional(condition: TERM, consequence: TERM) -> TERM | Constructs a structured conditional proposition term connecting a condition and consequence. descriptive logic structure. | aliases: if_then  ⟵ candidate
- conjunction | constructor | TERM conjunction(items: LIST[TERM]) -> TERM | All described components apply | not: Does not imply temporal order  ⟵ candidate
- decision | constructor | TERM decision(activity: TERM) -> TERM | A decision whose content is the described activity | not: Not proof it was carried out  ⟵ candidate
- distinguish | constructor | TERM distinguish(first: TERM, second: TERM, criterion?: STRING / TERM) -> TERM | Constructs a descriptive representation of discerning or differentiating between two entities, conditions, or behaviors along an optional criterion. | not: visual_contrast (optical contrast) or LINK contrast (rhetorical opposition between claims) | aliases: tell the difference, differentiate, distinguish between  ⟵ candidate
- duration | constructor | TERM duration(amount: NUMBER, unit: STRING) -> TERM | Requested elapsed/calendar extent | not: Word/item counts are not time  ⟵ dependency of wait
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ dependency of constraint_exclude_flowery_language
- footnote | constructor | TERM footnote(function: STRING, number: NUMBER) -> TERM | Constructs a footnote reference or citation marker descriptor. document formatting descriptor. | aliases: citation_note  ⟵ candidate
- location_spec | constructor | TERM location_spec(address?: STRING, area?: STRING, city?: STRING, state?: STRING) -> TERM | Constructs a structured geographical location specification with regional and administrative qualifiers. | not: a fixed atomic location descriptor in location-name or a spatial relation | aliases: location_details, geographic_location  ⟵ candidate
- maximum_between_stops | constructor | TERM maximum_between_stops(activity: STRING, amount: NUMBER, unit: STRING) -> TERM | Upper bound on the stated activity between successive stops | not: Not a limit on total daily duration  ⟵ candidate
- measure | constructor | TERM measure(amount: NUMBER, unit: STRING / ATOM[currency]) -> TERM | A measured amount: a number with its unit symbol (a unit-category value such as unit_minute, cap_gb or currency::USD). Describes the amount only; asserts nothing. ATOM[currency] is also accepted and supplies the pinned currency identity; no exchange rate or conversion is implicit. | not: a symbol with the number baked in (char_age_18, size_16gb); a unitless count (use the quantity argument) | aliases: amount of, size of, measured in  ⟵ candidate
- minimum_per_period | constructor | TERM minimum_per_period(class: STRING, count: NUMBER, period: STRING) -> TERM | At least count members of class in each period | not: Not a minimum total over the whole artifact  ⟵ candidate
- negation | constructor | TERM negation(target: TERM) -> TERM | Constructs a descriptive semantic negation of a target descriptive proposition or condition term. | not: Check's runtime Boolean operator NOT or a speech-act decline | aliases: not, does not, negation, absence of  ⟵ candidate
- rate | constructor | TERM rate(denominator: TERM, numerator: TERM) -> TERM | Constructs a structured proportional rate or frequency relating a numerator measured quantity to a denominator reference quantity. | not: an asserted factual attribution (use attribute_claim) or bound constraint (use requirement) | aliases: per_unit, ratio  ⟵ candidate
- remove_literal | constructor | TERM remove_literal(text: STRING) -> TERM | Remove occurrences of that exact literal in the stated artifact | not: Not remove similar markup unless specified  ⟵ dependency of transform_remove_br
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ dependency of constraint_single_choice
- sequence | constructor | TERM sequence(items: LIST[TERM]) -> TERM | Ordered described activities/content | not: Not unordered conjunction  ⟵ candidate
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ candidate
- test_condition | constructor | TERM test_condition(condition: STRING, expected: BOOL) -> TERM | A testable condition with the expected Boolean outcome | not: Expected outcome is not an observed result  ⟵ candidate

### composites

- assert_multinomial_scorer | composite | code-value | TERM assert_multinomial_scorer() -> TERM | Assertion that multinomial probabilistic scoring succeeds. | = test_condition(condition="multinomial_probabilistic_scoring", expected=TRUE)  ⟵ candidate
- constraint_budget_limited | composite | constraint-value | TERM constraint_budget_limited() -> TERM | Limited budget. | = requirement(property="budget_limited", value=TRUE)  ⟵ candidate
- constraint_comprehensive | composite | constraint-value | TERM constraint_comprehensive() -> TERM | Must be comprehensive. | = requirement(property="comprehensive", value=TRUE)  ⟵ candidate
- constraint_exclude_flowery_language | composite | constraint-value | TERM constraint_exclude_flowery_language() -> TERM | Avoid flowery language. | = exclude(item="flowery_language")  ⟵ candidate
- constraint_exclude_liberation_theme | composite | constraint-value | TERM constraint_exclude_liberation_theme() -> TERM | Avoid liberation theme. | = exclude(item="liberation_theme")  ⟵ candidate
- constraint_realistic | composite | constraint-value | TERM constraint_realistic() -> TERM | Must be realistic. | = requirement(property="realistic", value=TRUE)  ⟵ dependency of example_c_existing_constraint_symbol_becomes_a_typed_construction
- constraint_respectful | composite | constraint-value | TERM constraint_respectful() -> TERM | Must be respectful. | = requirement(property="respectful", value=TRUE)  ⟵ candidate
- constraint_single_choice | composite | constraint-value | TERM constraint_single_choice() -> TERM | Must pick a single choice. | = requirement(property="choice_count", value=1)  ⟵ candidate
- content_kyoto_itinerary | composite | content-value | TERM content_kyoto_itinerary() -> TERM | A Kyoto itinerary subject. | = subject(kind="itinerary", location="Kyoto")  ⟵ candidate
- content_status_update | composite | content-value | TERM content_status_update(subject: STRING) -> TERM | A request for a status update. | = activity(verb="request_update", object=$subject) | aliases: status update  ⟵ dependency of example_e_preserve_exact_wording_through_generation_and_sending
- transform_remove_br | composite | transformation-value | TERM transform_remove_br() -> TERM | Remove <br /> tags. | = remove_literal(text="<br />")  ⟵ candidate

### claim relations

- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ candidate
- instantiates | claim_relation | CLAIM instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) | Asserts that a code entity or constructor instantiates a target class or object under an optional condition. | not: an executed runtime object creation (pure factual assertion about code structure) | aliases: creates_instance, constructs_instance  ⟵ candidate
- motivated_by | claim_relation | CLAIM motivated_by(claim: CLAIM, motive: STRING / TERM) | Asserts that an action, rule, or claim is motivated by an underlying motive or goal. motive explanation. | aliases: rationale_is  ⟵ candidate
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ core
- validates_parameter | claim_relation | CLAIM validates_parameter(condition: STRING, entity: TERM, parameter: STRING) | Asserts that a code entity inspects or validates parameter names or types for a specified condition. | not: a runtime assertion test | aliases: inspects_parameter, checks_parameter, validates_parameter_names  ⟵ candidate

### links

- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ core
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ core
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ core

### values

- art_short_text | value | artifact-value | Short free text.  ⟵ dependency of example_e_preserve_exact_wording_through_generation_and_sending
- cuisine_arab | value | cuisine-value | Arab culinary cuisine style. | not: cuisine_mediterranean (broader regional category) | aliases: Arab food, Arabic food, Arab cuisine  ⟵ candidate
- constitutional_ai | value | descriptive-value | Concept of rule-based constitutional training and self-critique principles in AI alignment. | aliases: constitutional_ai  ⟵ candidate
- dom_safari | value | descriptive-value | Safari domain concept. | aliases: safari  ⟵ candidate
- yakuza | value | descriptive-value | Descriptive concept of yakuza in cultural and social contexts. | aliases: yakuza  ⟵ candidate
- unit_minute | value | duration-unit-value | Minute. | aliases: minutes, min  ⟵ candidate
- unit_week | value | duration-unit-value | Week. | aliases: weeks  ⟵ candidate
- unit_word | value | duration-unit-value | Rendered whitespace-delimited word. | aliases: words  ⟵ candidate
- afcfta | value | entity-name | African Continental Free Trade Area international agreement. | aliases: african_continental_free_trade_area  ⟵ candidate
- chair | value | entity-name | A chair furniture seat with a backrest. | not: object_label::armchair (specifically an object_label::armchair with side armrests) or object_label::sofa | aliases: chair, seat  ⟵ candidate
- coffee_maker | value | entity-name | A coffee-making appliance; not automatically a heating resource  ⟵ candidate
- egift_card | value | entity-name | Electronic gift card or digital voucher product. | aliases: digital_gift_card, e_gift_card  ⟵ candidate
- pencil | value | entity-name | A pencil writing instrument. | aliases: pencil  ⟵ candidate
- resource_chiller | value | entity-name | Canonical abstract chilling resource when no particular appliance is named.  ⟵ candidate
- resource_sink | value | entity-name | Canonical abstract washing resource when no particular sink is named.  ⟵ candidate
- sultana | value | entity-name | Dried white seedless grape food product. | not: raisin (dark dried grape) or wine_grape | aliases: sultana, sultanas, golden raisin  ⟵ candidate
- sun | value | entity-name | The central star of the Solar System. | not: an artificial lighting appliance or sunlight | aliases: sun, the sun, Sol  ⟵ candidate
- format_email | value | format-value | Email layout. | aliases: as an email  ⟵ dependency of example_e_preserve_exact_wording_through_generation_and_sending
- format_numbered_list | value | format-value | Numbered list. | aliases: numbered steps  ⟵ candidate
- locale_de | value | locale-value | German language or locale descriptor. | not: other language locales (such as locale_en_us or locale_fr) or country entity (country::DE) | aliases: German, german, Deutsch, de, de-DE  ⟵ candidate
- locale_en_gb | value | locale-value | UK English. | aliases: british english  ⟵ candidate
- locale_en_us | value | locale-value | US English. | aliases: english, en-us  ⟵ candidate
- locale_es | value | locale-value | Spanish. | aliases: spanish  ⟵ candidate
- locale_fr | value | locale-value | French. | aliases: french  ⟵ candidate
- locale_hi_en | value | locale-value | Hinglish (Hindi-English mix). | aliases: hinglish  ⟵ candidate
- locale_zh | value | locale-value | Chinese language locale (Simplified and Traditional Chinese). | not: a specific geographical region or nationality (use location-name) | aliases: chinese, zh, zh-cn, zh-tw, mandarin  ⟵ candidate
- africa | value | location-name | Geopolitical nation or continental region: africa. | aliases: africa  ⟵ candidate
- eastern_cape | value | location-name | Eastern Cape region.  ⟵ candidate
- island | value | location-name | A freestanding kitchen island counter or food preparation work surface. | not: counter (a perimeter countertop surface) or table (a dining or general furniture surface) | aliases: island, kitchen island, kitchen_island  ⟵ candidate
- liberal_onsen | value | location-name | Traditional Japanese establishment or hospitality venue: liberal_onsen. | aliases: liberal_onsen  ⟵ candidate
- onsen | value | location-name | Traditional Japanese establishment or hospitality venue: onsen. | aliases: onsen  ⟵ candidate
- russia | value | location-name | Geopolitical nation or continental region: russia. | aliases: russia  ⟵ candidate
- ukraine | value | location-name | Geopolitical nation or continental region: ukraine. | aliases: ukraine  ⟵ candidate
- united_kingdom | value | location-name | Geopolitical nation or sovereign state: United Kingdom (Great Britain). | not: locale_en_gb (a language/locale code, not a location) | aliases: United Kingdom, UK, Great Britain, Britain  ⟵ candidate
- japanese_government | value | recipient-value | Social, demographic, or institutional group: japanese_government. | aliases: japanese_government  ⟵ candidate
- role_manager | value | recipient-value | The user's manager. | aliases: my manager, boss  ⟵ dependency of example_e_preserve_exact_wording_through_generation_and_sending
- class_temple | value | semantic-category-value | The abstract class of temples. | aliases: temple, temples  ⟵ candidate
- class_town | value | semantic-category-value | The abstract class of towns. | aliases: town, towns  ⟵ candidate
- right_of | value | spatial-relation | To the right of. | aliases: right of  ⟵ candidate
- tone_empathetic | value | tone-value | Conveys empathy/understanding. | aliases: sympathetically  ⟵ candidate
- tone_formal | value | tone-value | Formal register. | aliases: formally  ⟵ candidate
- tone_neutral | value | tone-value | Plain, unmarked register.  ⟵ candidate
- tone_polite | value | tone-value | Courteous, respectful register. | aliases: politely, kindly  ⟵ dependency of example_e_preserve_exact_wording_through_generation_and_sending
- topic_pickup_lines | value | topic-value | Pickup lines.  ⟵ dependency of example_c_existing_constraint_symbol_becomes_a_typed_construction
- unit_gram | value | unit-value | Standard metric measurement unit of mass equal to 1/1,000 of a kilogram (0.001 kg). | not: digital capacity units (like cap_gb) or temporal duration units | aliases: g, gram, grams  ⟵ candidate
- unit_kilometer | value | unit-value | Standard metric measurement unit of distance equal to 1,000 meters. | not: temporal duration units (like unit_minute) or non-metric distance units | aliases: km, kilometer, kilometres, kilometers  ⟵ candidate

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

