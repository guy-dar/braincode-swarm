# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 15 needs (decomposition: llm), 112 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | speech_act | t1:s1 | Introduce translation examples between Vai and English | `locale_en_us`*, `offer`, `locale_en_gb`, `locale_hi_en`, `locale_es`, `acknowledge`, `locale_de`, `apologize`, `inform`, `rule_category_locale_value`, `correct`, `tone_urgent` |
| n2 | object | t1:s1 | Vai language | `locale_de`, `topic_derogatory_language`, `locale_hi_en`, `locale_en_gb`, `locale_en_us`, `locale_es`, `constraint_exclude_flowery_language`, `tone_casual`, `locale_zh`, `locale_fr`, `tone_formal`, `tone_neutral` |
| n3 | object | t1:s1 | English language | `locale_en_us`*, `locale_en_gb`, `locale_hi_en`, `locale_de`, `constraint_exclude_flowery_language`, `topic_derogatory_language`, `locale_es`, `tone_polite`, `tone_urgent`, `tone_formal`, `tone_silly`, `rule_category_locale_value` |
| n4 | claim | t1:s2 | In Vai, 'kàíɛ̌ á lɛ̀ndɛ́ɛ̌' translates to 'the man’s vessel' | `locale_hi_en`, `pen`, `yakuza`, `enables`, `gender_men`, `mug`, `greeting`, `acknowledge`, `user_preference`, `locale_en_gb`, `plate`, `topic_spider_man_2` |
| n5 | claim | t1:s3 | In Vai, 'kɔ̀ánjà-lèŋɛ̌ fǎ' translates to 'the baby-eagle’s father' | `role_son`, `role_mother`, `pen`, `yakuza`, `enables`, `moon`, `greeting`, `locale_en_gb`, `locale_hi_en`, `earth`, `role_daughter`, `statement` |
| n6 | claim | t1:s4 | In Vai, 'gbòmùɛ̌ á nyìmììɛ̌' translates to 'the fish’s snake' | `pen`, `yakuza`, `spoon`, `locale_hi_en`, `locale_en_gb`, `mug`, `locale_zh`, `enables`, `tattoos`, `user_preference`, `statement`, `occurred_recently` |
| n7 | claim | t1:s5 | In Vai, 'kàñiɛ̌ kàfà' translates to 'the man’s shoulder' | `yakuza`, `char_female`, `gender_men`, `meat`, `locale_hi_en`, `greeting`, `enables`, `right_of`, `dresser`, `user_preference`, `topic_spider_man_2`, `statement` |
| n8 | claim | t1:s6 | In Vai, 'nyìmìì jǎŋɛ̌ á gbòmù-lɛ̀ndɛ̀ɛ̌' translates to 'the long snake’s boat' | `locale_hi_en`, `pen`, `ryokan`, `yakuza`, `locale_zh`, `song`, `enables`, `spoon`, `naming_pattern`, `occurred_recently`, `user_preference`, `statement` |
| n9 | claim | t1:s7 | In Vai, 'mùsú jǎŋɛ̌ lɔ̀ɔ̀-kàì' translates to 'the tall woman’s brother' | `size_tall`, `locale_hi_en`, `yakuza`, `locale_en_gb`, `role_mother`, `char_female`, `role_sister`, `role_son`, `character`, `locale_zh`, `character_trait`, `user_preference` |
| n10 | claim | t1:s8 | In Vai, 'nyìmìì kúndúɛ̌ já' translates to 'the short snake’s eye' | `art_short_text`, `spoon`, `yakuza`, `pen`, `locale_hi_en`, `look`, `tattoos`, `aesthetic`, `grape_tannin`, `enables`, `greeting`, `watch` |
| n11 | claim | t1:s9 | In Vai, 'kɔ̀ánjà lɔ̀ɔ̀ɛ̌ kɛ̀njì' translates to 'the small eagle’s claw' | `size_small`*, `pen`, `yakuza`, `locale_hi_en`, `spoon`, `spatula`, `greeting`, `locale_en_gb`, `tattoos`, `art_short_text`, `locale_es`, `mug` |
| n12 | claim | t1:s10 | In Vai, 'kándɔ̀ jǎŋɛ̌' translates to 'the high sky' | `locale_hi_en`, `yakuza`, `moon`, `greeting`, `sun`, `earth`, `enables`, `locale_en_gb`, `time_horizon`, `occurred_recently`, `leads_to`, `ryokan` |
| n13 | action | t1:s11 | Translate a phrase | `greeting`, `dialogue`, `locale_es`, `locale_hi_en`, `word_blend`, `topic_derogatory_language`, `calculation`, `well_wishes`, `offer_help`, `tone_polite`, `obligation`, `propose` |
| n14 | constraint | t1:s11 | Translate into the Vai language | `locale_hi_en`, `locale_en_gb`, `locale_es`, `locale_en_us`, `locale_de`, `yakuza`, `constraint_exclude_flowery_language`, `locale_fr`, `pen`, `tone_casual`, `tone_formal`, `tone_urgent` |
| n15 | object | t1:s12 | The English phrase 'the eagle’s snake' | `locale_en_us`*, `locale_en_gb`, `style_catchy`, `locale_hi_en`, `tattoos`, `spoon`, `mug`, `art_story`, `aesthetic`, `pen`, `door`, `africa` |

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
- attribute_claim.subject → platform_label
- attribute_claim.value → platform_label
- failure.system → platform_label

## Retrieved records

### Shared rules that govern the records below (full text)

**rule_lexical_groups** (v19/rule/lexical-groups; rule governing platform_label)

Section 3.1 defines value groups: `group::key` values of type ATOM[group]. Open groups admit any key of their form (examples are not whitelists); standard groups admit the codes of their bundled standard (ISO 3166-1 alpha-2 for country, ISO 4217 for currency). Leaf values are never glossary entries. Consumer signatures alone decide where a group may appear. Retired bare symbols are invalid.

**rule_reading_guide** (v19/rule/reading-guide; core)

The spec governs syntax/types; this glossary defines vocabulary. Signature notation: ? optional, A / B explicit alternatives, void no result. Omitted optional arguments are unspecified. Value entries are category-refined STRING primitives; complex meanings require composition. Aliases are contextual hints, not unconditional equivalences. Report ambiguity. IDs use v19/<category>/<symbol>, v19/support/<symbol> or v19/composite/<symbol>. Statuses apply to this candidate: Retained preserves meaning; Adapted uses the stated contract; Composite requires TERM (bare STRING deprecated); Structural is syntax/argument vocabulary; Needs clarification is unusable until resolved; Deprecated is historical; Accepted is usable within this candidate.

**rule_recording_signatures** (v19/rule/recording-signatures; rule governing look)

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

**rule_category_character_property_value** (v19/rule/category/character-property-value; rule governing char_female)

TERM-described trait/style. Use constraints and explicit inclusion/scope; do not use an ungoverned character_properties attribute.

**rule_category_constraint_value** (v19/rule/category/constraint-value; rule governing constraint_exclude_flowery_language)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_descriptive_value** (v19/rule/category/descriptive-value; rule governing yakuza)

STRING modifier/domain label; never a free-form proposition. dom_sgi needs its intended referent established before semantically dependent use.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing pen)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_locale_value** (v19/rule/category/locale-value; candidate)

STRING locale. “English” alone does not always mean locale_en_us; preserve ambiguity.

**rule_category_location_name** (v19/rule/category/location-name; rule governing ryokan)

STRING location descriptor. A `table` surface is not the generated artifact category art_table.

**rule_category_product_attribute_value** (v19/rule/category/product-attribute-value; rule governing gender_men)

STRING color/size/product-market facets. gender_women describes a product category, not an assertion about a person's gender.

**rule_category_recipient_value** (v19/rule/category/recipient-value; rule governing role_son)

STRING roles or explicit named recipients. A role is not an exact person's identity. Keep an explicit name where substituting a role loses information.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing between)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_style_value** (v19/rule/category/style-value; rule governing style_catchy)

STRING production style. style_narrative does not establish that described events occurred.

**rule_category_tone_value** (v19/rule/category/tone-value; rule governing tone_urgent)

STRING register. tone_urgent describes urgency, not a concrete deadline.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_spider_man_2)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_composites_general** (v19/rule/composites-general; rule governing topic_derogatory_language)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_operations_general** (v19/rule/operations-general; rule governing look)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_support_primitives_general** (v19/rule/support-primitives-general; rule governing greeting)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- look | operation | operation-vocabulary | (direction: STRING) -> void | Tilt or adjust agent visual camera gaze. direction is up, down, or straight. | aliases: tilt_camera  ⟵ candidate

### speech acts

- apologize | speech_act | UTTER apologize(target?: CLAIM / TERM) | Speech act expressing apology or regret for an outcome or target. | not: decline (which is refusing) | aliases: apologize, apology, sorry  ⟵ candidate
- acknowledge | speech_act | operation-vocabulary | UTTER acknowledge(target: CLAIM / TERM) | Acknowledge receipt/awareness; does not imply agreement.  ⟵ candidate
- correct | speech_act | operation-vocabulary | UTTER correct(target: CLAIM) | Offer corrected content. Actual supersession requires the Conversation revision rules.  ⟵ candidate
- inform | speech_act | operation-vocabulary | UTTER inform(target: CLAIM) | Present the proposition; preserve its holder/status.  ⟵ candidate
- offer | speech_act | operation-vocabulary | UTTER offer(target: STRING / TERM) | Speech act offering assistance, service, or items to a conversation partner. speech act in dialogic traces. | aliases: proffer  ⟵ candidate
- propose | speech_act | operation-vocabulary | UTTER propose(target: TERM) | Suggest an action/idea; does not record it as performed.  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ dependency of obligation
- aesthetic | constructor | TERM aesthetic(period: STRING, style: STRING) -> TERM | A stylistic description with an explicit period | not: Not a character's age or production date  ⟵ candidate
- calculation | constructor | TERM calculation(inputs: LIST[TERM], operation: STRING, result?: TERM) -> TERM | Constructs a descriptive representation of an arithmetic or algorithmic calculation step with inputs, operation identifier, and optional resulting value. | not: an executed runtime action or factual claim of outcome | aliases: math_operation, compute_step  ⟵ candidate
- character | constructor | TERM character(name: STRING, series?: STRING) -> TERM | Constructs a descriptive representation of a fictional or narrative character. name specifies the character identifier. | aliases: fictional_character  ⟵ candidate
- character_trait | constructor | TERM character_trait(property: STRING, value: STRING / NUMBER) -> TERM | A character attribute | not: Not a claim about a real person  ⟵ candidate
- dialogue | constructor | TERM dialogue(style: STRING) -> TERM | Constructs a description of conversational dialogue adhering to a style. descriptive conversational term. | aliases: conversation_style  ⟵ candidate
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ dependency of constraint_exclude_flowery_language
- greeting | constructor | TERM greeting(recipient: STRING) -> TERM | Constructs a conversational salutation greeting descriptor. conversational discourse term. | aliases: salutation  ⟵ candidate
- naming_pattern | constructor | TERM naming_pattern(description: STRING, context?: STRING) -> TERM | Constructs a descriptive naming or morphological pattern. used for rule-based or conventional naming schemes. | aliases: pattern_naming  ⟵ candidate
- obligation | constructor | TERM obligation(actor: STRING / TERM, activity: TERM) -> TERM | Constructs a deontic obligation description requiring an actor to perform an activity. actor and activity specified. | aliases: duty, mandatory_activity  ⟵ candidate
- offer_help | constructor | TERM offer_help() -> TERM | Constructs a conversational proffer of assistance or support. conversational discourse term. | aliases: help_offer  ⟵ candidate
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ dependency of topic_derogatory_language
- time_horizon | constructor | TERM time_horizon(horizon: STRING) -> TERM | Constructs a temporal horizon or prospective timeframe descriptor indicating relative temporal distance into the future. | not: a specific calendar timestamp (use time_point) or an elapsed numerical duration (use duration). | aliases: future, future timeframe, time horizon, far off in the future, far future  ⟵ candidate
- well_wishes | constructor | TERM well_wishes(recipient?: STRING / TERM, sentiment?: STRING) -> TERM | Constructs a conversational discourse term representing well-wishes, good luck expressions, or parting encouragement. | not: a salutation greeting (use greeting) or apology (use apologize) | aliases: good_luck, best_wishes, encouragement  ⟵ candidate
- word_blend | constructor | TERM word_blend(base: STRING / TERM, replacement: STRING / TERM, result_name?: STRING) -> TERM | Constructs a morphological blend or portmanteau from base and replacement terms. descriptive lexical structure. | aliases: portmanteau  ⟵ candidate

### composites

- topic_derogatory_language | composite | TERM topic_derogatory_language() -> TERM | A composite term representing the topic of derogatory language. | = subject(kind="derogatory_language") | not: potential_harms (which is generic) | aliases: derogatory language  ⟵ candidate
- char_female | composite | character-property-value | TERM char_female() -> TERM | Female gender. | = character_trait(property="gender", value="female") | aliases: female  ⟵ candidate
- constraint_exclude_flowery_language | composite | constraint-value | TERM constraint_exclude_flowery_language() -> TERM | Avoid flowery language. | = exclude(item="flowery_language")  ⟵ candidate

### claim relations

- attribute_claim | claim_relation | CLAIM attribute_claim(subject: STRING / TERM / ATOM[platform_label], property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) | Asserts that a subject possesses a named property evaluated to a specific primitive or structured value. general property attribution claim. | aliases: property_value, word_property, has_property, property attribution  ⟵ related to statement
- enables | claim_relation | CLAIM enables(condition: TERM / CLAIM, outcome: TERM / CLAIM) | Asserts that an enabling condition or capability facilitates an outcome. enabling condition. | aliases: facilitates, allows  ⟵ candidate
- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ core
- has_state | claim_relation | CLAIM has_state(subject: TERM, state: STRING) | Asserts that an entity is currently in a physical, thermal, or operational state. state must be a valid state descriptor string. | aliases: in_state, state_is  ⟵ related to statement
- leads_to | claim_relation | CLAIM leads_to(cause: TERM, effect: TERM) | Asserts a conceptual consequence or progression from cause to effect. progression relation. | aliases: results_in  ⟵ candidate
- occurred_recently | claim_relation | CLAIM occurred_recently(target: CLAIM) | Asserts temporal recency of an asserted occurrence or claim. temporal recency qualifier. | aliases: recently_happened  ⟵ candidate
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ dependency of enables
- prohibited | claim_relation | CLAIM prohibited(subject: STRING / TERM, location: STRING / TERM, condition?: STRING / TERM) | Asserts that a subject is prohibited from a location or activity under specified conditions. deontic prohibition claim. | aliases: forbidden, banned_from  ⟵ related to obligation
- proposed_policy | claim_relation | CLAIM proposed_policy(policy: TERM, requirements: LIST[TERM]) | Asserts that a proposed policy framework comprises the specified requirement terms. policy must be a policy term. | aliases: policy_proposal  ⟵ related to obligation
- spatial_state | claim_relation | CLAIM spatial_state(relation: STRING, object: TERM, reference: TERM) | Asserts an observed spatial configuration between an object and a reference landmark. relation must specify spatial configuration. | aliases: placed_at, located_at  ⟵ related to statement
- statement | claim_relation | CLAIM statement(fact: TERM) | Foundational claim relation converting any descriptive TERM into an attributed, truth-evaluated assertion. universal fact assertion. | aliases: assert_fact, fact_claim, claim_statement  ⟵ candidate
- user_preference | claim_relation | CLAIM user_preference(constraints: TERM) | Asserts a user's stated preference constraints or dietary requirements. user constraint assertion. | aliases: stated_preference  ⟵ candidate

### links

- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ core
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ core
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ core

### values

- art_short_text | value | artifact-value | Short free text.  ⟵ candidate
- art_story | value | artifact-value | Narrative story.  ⟵ candidate
- tattoos | value | descriptive-value | Descriptive concept of tattoos in cultural and social contexts. | aliases: tattoos  ⟵ candidate
- yakuza | value | descriptive-value | Descriptive concept of yakuza in cultural and social contexts. | aliases: yakuza  ⟵ candidate
- door | value | entity-name | A door architectural barrier or entryway. | not: wall or close/open operations | aliases: door, doorway, room door  ⟵ candidate
- dresser | value | entity-name | A chest of drawers / dresser furniture. | aliases: dresser  ⟵ candidate
- earth | value | entity-name | The planet Earth as an astronomical celestial body. | not: soil, ground surface, or electrical grounding | aliases: earth, the earth, planet earth, Earth  ⟵ candidate
- grape_tannin | value | entity-name | Tannin powder derived from grapes for wine structure. | not: oak_chips or wood aging additives | aliases: grape tannin, tannin, wine tannin  ⟵ candidate
- meat | value | entity-name | Food item: meat or beef. | not: animal_label::tuna or animal_label::fish (specific aquatic foods) | aliases: meat, beef  ⟵ candidate
- moon | value | entity-name | Earth's natural celestial satellite. | not: an artificial satellite or other planetary moon | aliases: moon, the moon, Luna  ⟵ candidate
- mug | value | entity-name | Drinking cup. | aliases: mug  ⟵ candidate
- pen | value | entity-name | A writing instrument. | aliases: pen  ⟵ candidate
- plate | value | entity-name | A shallow, flat dish or vessel used for holding, preparing, or serving food. | not: bowl (deep concave vessel) or table (furniture surface) | aliases: dish, plate  ⟵ candidate
- song | value | entity-name | A musical piece, audio track, or song entity. | not: piano (a musical instrument) or cd (a physical compact disc storage medium) | aliases: song, music track, audio track, track  ⟵ candidate
- spatula | value | entity-name | A kitchen utensil with a broad, flat, and flexible blade used for lifting, flipping, or spreading food. | not: knife (cutting utensil) or spoon (scooping utensil) | aliases: spatula, turner, flipper  ⟵ candidate
- spoon | value | entity-name | An eating or cooking utensil. | aliases: spoon  ⟵ candidate
- sun | value | entity-name | The central star of the Solar System. | not: an artificial lighting appliance or sunlight | aliases: sun, the sun, Sol  ⟵ candidate
- watch | value | entity-name | A watch or wristwatch timepiece object. | not: clock (a stationary timepiece appliance) or duration units like unit_hour | aliases: watch, wristwatch, wrist watch  ⟵ candidate
- locale_de | value | locale-value | German language or locale descriptor. | not: other language locales (such as locale_en_us or locale_fr) or country entity (country::DE) | aliases: German, german, Deutsch, de, de-DE  ⟵ candidate
- locale_en_gb | value | locale-value | UK English. | aliases: british english  ⟵ candidate
- locale_en_us | value | locale-value | US English. | aliases: english, en-us  ⟵ candidate
- locale_es | value | locale-value | Spanish. | aliases: spanish  ⟵ candidate
- locale_fr | value | locale-value | French. | aliases: french  ⟵ candidate
- locale_hi_en | value | locale-value | Hinglish (Hindi-English mix). | aliases: hinglish  ⟵ candidate
- locale_zh | value | locale-value | Chinese language locale (Simplified and Traditional Chinese). | not: a specific geographical region or nationality (use location-name) | aliases: chinese, zh, zh-cn, zh-tw, mandarin  ⟵ candidate
- africa | value | location-name | Geopolitical nation or continental region: africa. | aliases: africa  ⟵ candidate
- ryokan | value | location-name | Traditional Japanese establishment or hospitality venue: ryokan. | aliases: ryokan  ⟵ candidate
- gender_men | value | product-attribute-value | Men's/male-targeted. | aliases: men, male  ⟵ candidate
- size_small | value | product-attribute-value | Small size. | aliases: small, S  ⟵ candidate
- size_tall | value | product-attribute-value | Tall relative vertical dimension qualifier. | aliases: size_tall  ⟵ candidate
- role_daughter | value | recipient-value | Daughter participant role in family or travel context. | not: role_sister, role_mother, or generic role_kids | aliases: daughter, my daughter  ⟵ candidate
- role_mother | value | recipient-value | The mother of the user. | not: role_sister or role_kids | aliases: my mom, mother, mom  ⟵ candidate
- role_sister | value | recipient-value | Sister participant role in family/event context. | aliases: sister  ⟵ candidate
- role_son | value | recipient-value | Son participant role in family or travel context. | not: role_daughter, role_sister, role_mother, or generic role_kids | aliases: son, my son  ⟵ candidate
- between | value | spatial-relation | Positioned between or in the middle of reference entities. | not: next_to or in_front_of | aliases: between, in the middle of, middle of, center of  ⟵ candidate
- right_of | value | spatial-relation | To the right of. | aliases: right of  ⟵ candidate
- style_catchy | value | style-value | Catchy, attention-grabbing style. | aliases: catchy  ⟵ candidate
- tone_casual | value | tone-value | Informal register. | aliases: casually  ⟵ candidate
- tone_formal | value | tone-value | Formal register. | aliases: formally  ⟵ candidate
- tone_neutral | value | tone-value | Plain, unmarked register.  ⟵ candidate
- tone_polite | value | tone-value | Courteous, respectful register. | aliases: politely, kindly  ⟵ candidate
- tone_silly | value | tone-value | Playful, lighthearted, or silly conversational tone. | aliases: silly  ⟵ candidate
- tone_urgent | value | tone-value | Conveys urgency. | aliases: urgently, ASAP  ⟵ candidate
- topic_spider_man_2 | value | topic-value | Marvel's Spider-Man 2.  ⟵ candidate
