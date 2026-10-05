# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 7 needs (decomposition: llm), 86 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | speech_act | t1:s1 | Introduce a list of Tundra Yukaghir words and their English translations. | `locale_en_us`*, `unit_word`*, `locale_hi_en`, `constraint_exclude_flowery_language`, `locale_en_gb`, `yakuza`, `maqluba`, `cuisine_arab`, `offer`, `greeting`, `apologize`, `inform` |
| n2 | constraint | t1:s1 | The Tundra Yukaghir words and English translations are in arbitrary order. | `constraint_exclude_flowery_language`, `locale_en_us`*, `unit_word`*, `extract`, `locale_hi_en`, `locale_en_gb`, `locale_de`, `maqluba`, `rule_category_locale_value`, `topic_derogatory_language`, `metric_order_late`, `constraint_exclude_liberation_theme` |
| n3 | object | t1:s2, t1:s3, t1:s4, t1:s5, t1:s6, t1:s7, t1:s8, t1:s9, t1:s10, t1:s11, t1:s12, t1:s13, t1:s14, t1:s15, t1:s16, t1:s17, t1:s18, t1:s19, t1:s20, t1:s21, t1:s22, t1:s23, t1:s24, t1:s25, t1:s26, t1:s27, t1:s28, t1:s29, t1:s30, t1:s31, t1:s32, t1:s33, t1:s34, t1:s35, t1:s36, t1:s37 | A list of eighteen Tundra Yukaghir words. | `unit_word`*, `unit_sentence`, `locale_hi_en`, `constraint_exclude_flowery_language`, `maqluba`, `yakuza`, `class_temple`, `topic_derogatory_language`, `spoon`, `yarn`, `mug`, `unit_paragraph` |
| n4 | object | t1:s38, t1:s39, t1:s40, t1:s41, t1:s42, t1:s43, t1:s44, t1:s45, t1:s46, t1:s47, t1:s48, t1:s49, t1:s50, t1:s51, t1:s52, t1:s53, t1:s54, t1:s55, t1:s56, t1:s57, t1:s58, t1:s59, t1:s60, t1:s61, t1:s62, t1:s63, t1:s64, t1:s65, t1:s66, t1:s67, t1:s68, t1:s69, t1:s70, t1:s71, t1:s72, t1:s73 | A list of eighteen English translations. | `locale_en_us`*, `locale_hi_en`, `locale_en_gb`, `constraint_exclude_flowery_language`, `locale_es`, `locale_de`, `locale_fr`, `transform_remove_br`, `class_temple`, `format_plain_text`, `topic_derogatory_language`, `rule_category_locale_value` |
| n5 | claim | t1:s74 | The Tundra Yukaghir word 'ewce' means 'tip, point'. | `unit_word`*, `locale_hi_en`, `yakuza`, `spoon`, `maqluba`, `greeting`, `enables`, `tone_empathetic`, `leads_to`, `occurred_recently`, `outcome`, `similarity` |
| n6 | action | t1:s75 | Translate a Tundra Yukaghir word into English. | `locale_en_us`*, `locale_hi_en`, `locale_en_gb`, `unit_word`*, `greeting`, `word_blend`, `constraint_exclude_flowery_language`, `yakuza`, `maqluba`, `calculation`, `locale_es`, `rule_category_locale_value` |
| n7 | object | t1:s76 | The Tundra Yukaghir word 'ile' to be translated. | `unit_word`*, `locale_hi_en`, `locale_en_gb`, `yakuza`, `locale_es`, `constraint_exclude_flowery_language`, `locale_en_us`, `maqluba`, `cuisine_arab`, `locale_de`, `spoon`, `topic_derogatory_language` |

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
- activity.object → object_label, food_label, animal_label
- activity.location → country
- activity.instrument → object_label, platform_label
- failure.system → platform_label

## Retrieved records

### Shared rules that govern the records below (full text)

**rule_lexical_groups** (v19/rule/lexical-groups; rule governing platform_label)

Section 3.1 defines value groups: `group::key` values of type ATOM[group]. Open groups admit any key of their form (examples are not whitelists); standard groups admit the codes of their bundled standard (ISO 3166-1 alpha-2 for country, ISO 4217 for currency). Leaf values are never glossary entries. Consumer signatures alone decide where a group may appear. Retired bare symbols are invalid.

**rule_reading_guide** (v19/rule/reading-guide; core)

The spec governs syntax/types; this glossary defines vocabulary. Signature notation: ? optional, A / B explicit alternatives, void no result. Omitted optional arguments are unspecified. Value entries are category-refined STRING primitives; complex meanings require composition. Aliases are contextual hints, not unconditional equivalences. Report ambiguity. IDs use v19/<category>/<symbol>, v19/support/<symbol> or v19/composite/<symbol>. Statuses apply to this candidate: Retained preserves meaning; Adapted uses the stated contract; Composite requires TERM (bare STRING deprecated); Structural is syntax/argument vocabulary; Needs clarification is unusable until resolved; Deprecated is historical; Accepted is usable within this candidate.

**rule_recording_signatures** (v19/rule/recording-signatures; rule governing extract)

RECORD ACTION uses the operation signature with REF[STRING] → TERM and LIST[REF[STRING]] → LIST[TERM]; other types/categories stay unchanged. Return EVENT, never the runtime result. Record actual outputs as attributed CLAIMs. Do not infer missing resources.

**rule_speech_acts_general** (v19/rule/speech-acts-general; rule governing offer)

UTTER-only, void, with the spec's speech attributes and LIST[TERM] constraints. No result binding. Literal content cannot replace required semantic arguments for structured coverage.

**rule_structural_constructs** (v19/rule/structural-constructs; core)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; rule governing enables)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_attributes_and_generate** (v19/rule/attributes-and-generate; rule governing art_short_text)

Attribute entries name arguments; legality/types come from each operation, not global membership. GENERATE uses the spec's core fields; retained artifact profiles return STRING. Numeric/list results need explicit profiles. Legacy itinerary fields expand to TERM constraints: duration/duration_unit → duration(amount,unit); stop_min_per_day/stop_requirement → minimum_per_period(class,count,period=unit_day), never an inferred temple class; max_walk_duration/unit → maximum_between_stops(activity="walk",amount,unit). No legacy shorthand is enabled. Old events/character_properties/transformations become explicitly scoped TERM constraints. Message purpose is TERM, not send_email.content: GENERATE exact STRING content, then send. Report opaque fallback separately.

**rule_category_artifact_value** (v19/rule/category/artifact-value; rule governing art_short_text)

STRING artifact class for GENERATE.target. art_story says what kind of artifact to produce, not what occurs in its plot.

**rule_category_constraint_value** (v19/rule/category/constraint-value; rule governing constraint_exclude_flowery_language)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_content_value** (v19/rule/category/content-value; rule governing content_status_update)

Existing compounds become the constructors in Section 5. Their outputs go in topic/target/constraints as appropriate, not content, whose spec type remains STRING.

**rule_category_cuisine_value** (v19/rule/category/cuisine-value; rule governing cuisine_arab)

STRING cuisine class; cuisine_indian is a cuisine filter, not the location India.

**rule_category_descriptive_value** (v19/rule/category/descriptive-value; rule governing yakuza)

STRING modifier/domain label; never a free-form proposition. dom_sgi needs its intended referent established before semantically dependent use.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; rule governing unit_word)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing maqluba)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_format_value** (v19/rule/category/format-value; rule governing format_numbered_list)

STRING format. format_email is layout, not the action send_email.

**rule_category_locale_value** (v19/rule/category/locale-value; candidate)

STRING locale. “English” alone does not always mean locale_en_us; preserve ambiguity.

**rule_category_metric_value** (v19/rule/category/metric-value; rule governing metric_order_late)

STRING metric identity, not a Boolean value. Uptime and response time need numeric observations with units; order-late is Boolean-valued. Do not type every metric as BOOL.

**rule_category_recipient_value** (v19/rule/category/recipient-value; rule governing role_manager)

STRING roles or explicit named recipients. A role is not an exact person's identity. Keep an explicit name where substituting a role loses information.

**rule_category_semantic_category_value** (v19/rule/category/semantic-category-value; rule governing class_temple)

STRING class label used by typed constraints. class_temple describes a class, not an acquired physical temple reference.

**rule_category_tone_value** (v19/rule/category/tone-value; rule governing tone_empathetic)

STRING register. tone_urgent describes urgency, not a concrete deadline.

**rule_category_transformation_value** (v19/rule/category/transformation-value; rule governing transform_remove_br)

TERM-described transformation. Pass it through constraints; no ungoverned transformations attribute.

**rule_composites_general** (v19/rule/composites-general; rule governing constraint_exclude_flowery_language)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_examples_general** (v19/rule/examples-general; rule governing example_e_preserve_exact_wording_through_generation_and_sending)

Examples use this glossary's contracts. They have not been verified by an implemented BrainCode parser.

**rule_operations_general** (v19/rule/operations-general; rule governing extract)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_supplemental_general** (v19/rule/supplemental-general; rule governing extract)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; rule governing greeting)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- extract | operation | operation-vocabulary | (target: LIST[REF[STRING]], limit: NUMBER) -> LIST[REF[STRING]] | First limit results, preserving order and identity; limit is a nonnegative integer; limit=1 is still a list  ⟵ candidate
- send_email | operation | operation-vocabulary | (recipient: STRING, content: STRING, tone?: STRING) -> void | Send supplied exact message content to the identified recipient. A requested message purpose is not already a composed message. | aliases: email  ⟵ dependency of example_e_preserve_exact_wording_through_generation_and_sending

### speech acts

- apologize | speech_act | UTTER apologize(target?: CLAIM / TERM) | Speech act expressing apology or regret for an outcome or target. | not: decline (which is refusing) | aliases: apologize, apology, sorry  ⟵ candidate
- inform | speech_act | operation-vocabulary | UTTER inform(target: CLAIM) | Present the proposition; preserve its holder/status.  ⟵ candidate
- offer | speech_act | operation-vocabulary | UTTER offer(target: STRING / TERM) | Speech act offering assistance, service, or items to a conversation partner. speech act in dialogic traces. | aliases: proffer  ⟵ candidate
- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ dependency of content_status_update
- calculation | constructor | TERM calculation(inputs: LIST[TERM], operation: STRING, result?: TERM) -> TERM | Constructs a descriptive representation of an arithmetic or algorithmic calculation step with inputs, operation identifier, and optional resulting value. | not: an executed runtime action or factual claim of outcome | aliases: math_operation, compute_step  ⟵ candidate
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ dependency of constraint_exclude_flowery_language
- greeting | constructor | TERM greeting(recipient: STRING) -> TERM | Constructs a conversational salutation greeting descriptor. conversational discourse term. | aliases: salutation  ⟵ candidate
- include | constructor | TERM include(item: STRING / TERM) -> TERM | Require the identified content/item | not: Not permission to invent an instance in a recorded trace  ⟵ dependency of constraint_include_character_attribute_list
- remove_literal | constructor | TERM remove_literal(text: STRING) -> TERM | Remove occurrences of that exact literal in the stated artifact | not: Not remove similar markup unless specified  ⟵ dependency of transform_remove_br
- similarity | constructor | TERM similarity(target: STRING / TERM, dimension?: STRING / TERM) -> TERM | Constructs a descriptor representing comparative closeness or similarity to a target along a given dimension. | not: spatial proximity (use rank_distance or next_to) or an assertion of exact identity (use identity) | aliases: closest_to, similar_to, resembles  ⟵ candidate
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ dependency of topic_derogatory_language
- word_blend | constructor | TERM word_blend(base: STRING / TERM, replacement: STRING / TERM, result_name?: STRING) -> TERM | Constructs a morphological blend or portmanteau from base and replacement terms. descriptive lexical structure. | aliases: portmanteau  ⟵ candidate

### composites

- topic_derogatory_language | composite | TERM topic_derogatory_language() -> TERM | A composite term representing the topic of derogatory language. | = subject(kind="derogatory_language") | not: potential_harms (which is generic) | aliases: derogatory language  ⟵ candidate
- constraint_exclude_flowery_language | composite | constraint-value | TERM constraint_exclude_flowery_language() -> TERM | Avoid flowery language. | = exclude(item="flowery_language")  ⟵ candidate
- constraint_exclude_liberation_theme | composite | constraint-value | TERM constraint_exclude_liberation_theme() -> TERM | Avoid liberation theme. | = exclude(item="liberation_theme")  ⟵ candidate
- constraint_include_character_attribute_list | composite | constraint-value | TERM constraint_include_character_attribute_list() -> TERM | Include character attributes. | = include(item="character_attribute_list")  ⟵ candidate
- content_status_update | composite | content-value | TERM content_status_update(subject: STRING) -> TERM | A request for a status update. | = activity(verb="request_update", object=$subject) | aliases: status update  ⟵ dependency of example_e_preserve_exact_wording_through_generation_and_sending
- transform_remove_br | composite | transformation-value | TERM transform_remove_br() -> TERM | Remove <br /> tags. | = remove_literal(text="<br />")  ⟵ candidate

### claim relations

- enables | claim_relation | CLAIM enables(condition: TERM / CLAIM, outcome: TERM / CLAIM) | Asserts that an enabling condition or capability facilitates an outcome. enabling condition. | aliases: facilitates, allows  ⟵ candidate
- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ core
- leads_to | claim_relation | CLAIM leads_to(cause: TERM, effect: TERM) | Asserts a conceptual consequence or progression from cause to effect. progression relation. | aliases: results_in  ⟵ candidate
- occurred_recently | claim_relation | CLAIM occurred_recently(target: CLAIM) | Asserts temporal recency of an asserted occurrence or claim. temporal recency qualifier. | aliases: recently_happened  ⟵ candidate
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ candidate

### links

- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ core
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ core
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ core

### values

- art_short_text | value | artifact-value | Short free text.  ⟵ dependency of example_e_preserve_exact_wording_through_generation_and_sending
- cuisine_arab | value | cuisine-value | Arab culinary cuisine style. | not: cuisine_mediterranean (broader regional category) | aliases: Arab food, Arabic food, Arab cuisine  ⟵ candidate
- yakuza | value | descriptive-value | Descriptive concept of yakuza in cultural and social contexts. | aliases: yakuza  ⟵ candidate
- unit_paragraph | value | duration-unit-value | Paragraph of text. | aliases: paragraphs, paragraph  ⟵ candidate
- unit_sentence | value | duration-unit-value | One grammatical sentence in text generation or constraint counting. | not: unit_paragraph (paragraph block) or unit_word (individual word) | aliases: sentence, sentences  ⟵ candidate
- unit_word | value | duration-unit-value | Rendered whitespace-delimited word. | aliases: words  ⟵ candidate
- maqluba | value | entity-name | Traditional Arab layered rice dish: maqluba. | not: cuisine_mediterranean (cuisine style rather than specific dish) | aliases: maqluba, makloubeh  ⟵ candidate
- mug | value | entity-name | Drinking cup. | aliases: mug  ⟵ candidate
- spoon | value | entity-name | An eating or cooking utensil. | aliases: spoon  ⟵ candidate
- yarn | value | entity-name | Item or prop in joke/creative context: yarn. | aliases: yarn  ⟵ candidate
- format_email | value | format-value | Email layout. | aliases: as an email  ⟵ dependency of example_e_preserve_exact_wording_through_generation_and_sending
- format_numbered_list | value | format-value | Numbered list. | aliases: numbered steps  ⟵ candidate
- format_plain_text | value | format-value | Unstructured prose text. | aliases: plain text  ⟵ candidate
- locale_de | value | locale-value | German language or locale descriptor. | not: other language locales (such as locale_en_us or locale_fr) or country entity (country::DE) | aliases: German, german, Deutsch, de, de-DE  ⟵ candidate
- locale_en_gb | value | locale-value | UK English. | aliases: british english  ⟵ candidate
- locale_en_us | value | locale-value | US English. | aliases: english, en-us  ⟵ candidate
- locale_es | value | locale-value | Spanish. | aliases: spanish  ⟵ candidate
- locale_fr | value | locale-value | French. | aliases: french  ⟵ candidate
- locale_hi_en | value | locale-value | Hinglish (Hindi-English mix). | aliases: hinglish  ⟵ candidate
- metric_order_late | value | metric-value | Whether an order is late. | aliases: order is late, delayed  ⟵ candidate
- role_manager | value | recipient-value | The user's manager. | aliases: my manager, boss  ⟵ dependency of example_e_preserve_exact_wording_through_generation_and_sending
- class_temple | value | semantic-category-value | The abstract class of temples. | aliases: temple, temples  ⟵ candidate
- tone_empathetic | value | tone-value | Conveys empathy/understanding. | aliases: sympathetically  ⟵ candidate
- tone_polite | value | tone-value | Courteous, respectful register. | aliases: politely, kindly  ⟵ dependency of example_e_preserve_exact_wording_through_generation_and_sending
- tone_silly | value | tone-value | Playful, lighthearted, or silly conversational tone. | aliases: silly  ⟵ candidate

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

