# BrainCode migrated glossary

**Version:** 19.0.0-draft.1  
**Date:** 2026-10-03  
**Target specification:** [language-spec-revised.md](language-spec-revised.md)  
**Source:** `C:/projects/BrainCode/syntax-loop-favourite-products/v2/glossary.md`  
**Status:** migrated draft; not an adopted language release or a claim of vocabulary sufficiency.

This file preserves the source glossary's explicitly listed vocabulary and records how its existing content changes under the revised specification. Original examples and membership rules are replaced, not silently carried forward. Both source documents remain unchanged.

The final inventory accounts for every explicitly listed source member, including structural tokens and attributes. Names that appeared only inside source examples were not thereby fully defined; Section 8 explicitly supplies the few needed by this file. Other example-only names are not implicitly accepted. An open category permits reviewed additions, not unlimited runtime invention.

## 1. How to read this glossary

The specification governs grammar, scope, mode, types and canonical form. This glossary governs the vocabulary meanings and signatures below. Signatures are documentation notation: `?` means optional; `A / B` means explicitly allowed alternative types; `void` means no result. These are not new BrainCode type tokens. An omitted optional value is unspecified, not a fabricated default.

Stable IDs use `v19/<category>/<symbol>`. Supplementary entries use `v19/support/<symbol>` and composite constructors use `v19/composite/<symbol>`. Their source is this migration unless the inventory identifies the original category. Each family table supplies shared typing, restrictions, and example conventions for its member rows.

Migration statuses:

| Status | Meaning |
|---|---|
| Retained | The source meaning remains usable under the category contract |
| Adapted | The symbol remains, with the revised contract stated here |
| Composite | The name is retained as a TERM constructor with an explicit expansion; bare STRING use is deprecated |
| Needs clarification | Preserved for review, but cannot be used as an accepted entry in a frozen evaluation release until the ambiguity is resolved |
| Structural | Syntax or an argument name, not a STRING-valued concept |

All statuses describe this proposed migration, not prior human approval. No symbol is silently deleted. Natural-language aliases are contextual recognition hints, not assertions that every occurrence of the phrase has the same meaning. When a context suggests different meanings, report the ambiguity rather than selecting by alphabetical order.

For retained value entries, kind is `primitive value`, signature is `STRING` refined by its category, and the member's gloss is its definition. This uses the revised spec's explicit primitive option; it does not claim every English expression is semantically atomic. Complex propositions and requirements instead receive expansions below.

## 2. Structural constructs: replacement documentation

| Source entry | Migrated meaning and example reference |
|---|---|
| Types & Lexicon | Accepted value symbols remain STRING; TERM, CLAIM and EVENT are distinct semantic types. Example A shows typed references. |
| Task | A REQUEST plan, not evidence that its work occurred. Exactly one entrypoint. Examples A and B. |
| Action | Requested external work with an exact signature. TRACE uses RECORD and produces EVENT. Examples A and D. |
| Utterance | A speech act inside TURN; never binds a STRING result. Targets and constraints carry meaning. Example C. |
| Check | Pure comparisons of supported types; CLAIM is not BOOL. A Check belongs inside IF or a quantified Check, never alone as a step. |
| Flow-If | REQUEST-only branching in a Task or Turn; branch-local bindings do not escape. No TRACE execution. |
| Iterate | Finite sequential LIST iteration; ANY/ALL use pure predicates. A list of one REF is still a list. Example A. |
| Bind | Immutable LET and typed producer results; no UTTER result. Earlier top-level semantic objects may be read across turns using qualified names. |
| Conversation | One turn per supplied message. Whole replacement uses REVISES; targeted claim replacement uses AMENDS and revises links. |
| Generate | Requested artifact production. Typed glossary extensions replace hard-coded domain exceptions; artifact constraints are LIST[TERM]. Example B. |
| descriptive-value | Residual modifiers and domains; no permission to hide arbitrary propositions in names. |
| canonical-form | Target first, then alphabetical attributes; canonical handles; semantic aliases only; no automatic custom operations. |
| types-lexicon, action, bind | Retained documentation aliases of their capitalized entries, not separate syntax. Empty TASK examples are removed. |

Additions required to express the migrated contracts: MODE REQUEST/TRACE, TERM, CLAIM, EVENT, LINK, RECORD, CALL, BY, STATUS, SOURCE, and AMENDS. The specification defines their syntax. These additions do not expand the subject-domain inventory.

Structural tokens inherited from the source remain listed in the inventory. Add `.` for qualified references. `asserted`, `observed`, `inferred`, `assumed`, `hypothesized`, `reported`, `attempted`, `succeeded`, `failed`, and `unknown` are reserved in their grammar positions. SOURCE is a keyword; lower-case `source` can be an operation argument. Exact names are case-sensitive.

## 3. Operation contracts

All listed source operations are retained. Operation symbols are callable vocabulary, not arbitrary argument values. Their natural-language aliases appear in the inventory. Parameter types include category checks; a name accepted by one category is not automatically accepted by another.

Every result-producing operation binds its result in REQUEST mode. All external operations may fail; failure does not create the declared successful result. Runtime failure handling is outside this glossary. TRACE represents attempts/failures without manufacturing successful runtime values.

### External operations

| Symbol | REQUEST signature | Meaning, effects and boundaries |
|---|---|---|
| open_page | `(target: STRING) -> REF[STRING]` | Navigate to the specified URL/page identity and return its page reference. Not a search for an unspecified page. |
| click | `(target: REF[STRING]) -> void` | Activate the selected UI element. Requires its identity, not an invented selector. |
| select_filter | `(target: REF[STRING], criterion: TERM) -> void` | Apply one specified filter in an existing UI. Do not add this operation when the source only requests filtered search. |
| apply_filters | `(target: REF[STRING], criteria: LIST[TERM]) -> void` | Apply the listed filters to an existing UI. Not repeated evidence of a search already represented. |
| search_travel | `(target: STRING, constraints?: LIST[TERM], location?: STRING) -> LIST[REF[STRING]]` | Query travel options meeting supplied constraints. Does not book them. |
| search_transit | `(target: STRING, constraints?: LIST[TERM], location?: STRING) -> LIST[REF[STRING]]` | Query transit options. Does not buy tickets. |
| search_web | `(target: STRING, ...search attributes below) -> LIST[REF[STRING]]` | Query a catalog/web source. Criteria filter the result; rank separately when requested. |
| sort | `(target: LIST[REF[STRING]], rank_direction: STRING, rank_field: STRING) -> LIST[REF[STRING]]` | Request ordering of selected results. Preserve member identity; this is not a claim that order was observed. |
| pick_up | `(target: STRING, quantity?: NUMBER, source?: STRING, color?: STRING, shape?: STRING, state?: STRING) -> REF[STRING] or LIST[REF[STRING]]` | Select/acquire objects. Missing quantity or literal 1 returns REF; integer literal greater than 1 returns LIST[REF]. Other values are invalid for this profile. |
| place | `(target: REF[STRING], destination: STRING, location?: STRING, relation?: STRING) -> void` | Place an already acquired object. Spatial relation must be explicit if the source distinguishes it. |
| rinse | `(target: REF[STRING], destination: STRING) -> REF[STRING]` | Rinse using the stated resource; return the same identity. It is not enough that the object is already clean. |
| heat | `(target: REF[STRING], destination: STRING) -> REF[STRING]` | Heat using the stated resource; same identity. Selecting a warm object does not imply heating it. |
| chill | `(target: REF[STRING], destination: STRING) -> REF[STRING]` | Chill using the stated resource; same identity. |
| slice | `(target: REF[STRING]) -> REF[STRING]` | Slice the selected material, preserving its tracked aggregate identity. Individually addressed pieces need another accepted profile. |
| pour | `(target: REF[STRING], destination: STRING) -> REF[STRING]` | Transfer selected liquid to the destination, preserving tracked material identity. |
| modify_code | `(target: STRING, file: STRING, revision: TERM, method?: STRING) -> void` | Apply the structured change to the indicated code. A method name alone does not specify the change. |
| run_tests | `(target: STRING, assertion?: TERM) -> BOOL` | Run the selected project's tests, optionally checking the specified assertion. TRUE means the declared test condition passed, not overall software correctness. |
| add_to_cart | `(target: LIST[REF[STRING]]) -> void` | Add the explicitly selected items. Does not pay or place an order. |
| check_reservation_availability | `(target: STRING, cuisine?: STRING, currency?: STRING, location?: STRING, max_price?: NUMBER) -> BOOL` | Check current availability under supplied filters. A positive result does not make a reservation. |
| send_email | `(recipient: STRING, content: STRING, tone?: STRING) -> void` | Send supplied exact message content to the identified recipient. A requested message purpose is not already a composed message. |
| send_message | `(recipient: STRING, content: STRING, tone?: STRING) -> void` | Send supplied exact content through the specified message context. If the channel is unresolved, report it. |

`search_web` optional attributes: `availability`, `category`, `color`, `cuisine`, `currency`, `gender`, `genre`, `location`, `platform`, `ram_unit`, `reservation_availability`, `shape`, `size`, `rank` is **not** accepted; ranking belongs to sort. Numeric filters: `max_price`, `min_ram`, `min_rating`; `trending` is BOOL. All other listed filters are STRING with matching categories. Price requires currency and RAM requires a capacity unit. No unstated default scale or source is inferred.

Search ranking uses only rank_* for rank_field and dir_* for rank_direction, not any arbitrary search-value member. Product category/genre/availability similarly accept only their own subfamilies.

These explicit signatures are proposed migration decisions where the source had only a gloss; they are not claims that an existing runtime adapter supports them. Additional attributes require a reviewed operation profile. No `custom_general_<predicate>` operation is automatically legal.

### Speech acts

| Symbol | Required semantic argument | Meaning and contrast |
|---|---|---|
| ask | `target: TERM`, or a sufficiently precise `topic: STRING / TERM` | Request information/advice; not an assertion of an answer. |
| inform | `target: CLAIM` | Present the proposition; preserve its holder/status. |
| respond | `target: CLAIM / TERM` | Answer with structured content; not merely label the question's topic. |
| propose | `target: TERM` | Suggest an action/idea; does not record it as performed. |
| correct | `target: CLAIM` | Offer corrected content. Actual supersession requires the Conversation revision rules. |
| acknowledge | `target: CLAIM / TERM` | Acknowledge receipt/awareness; does not imply agreement. |
| confirm | `target: CLAIM` | Confirm the proposition; its evidence/status remains explicit. |
| decline | `target: TERM` | Decline the represented request/proposal; not negate every proposition within it. |

All are UTTER-only, return void, and may use the specification's audience, recipient, tone, topic, content and LIST[TERM] constraints attributes. Required semantic arguments cannot be replaced by content="..." to claim fully structured coverage. There are no UTTER result bindings.

### Recording signatures

For RECORD ACTION, use the same operation attributes with every REF[STRING] replaced by TERM describing the identified object, and every LIST[REF[STRING]] by LIST[TERM]. Other parameter types and categories remain. RECORD returns EVENT regardless of the REQUEST result. A recording of run_tests may therefore fail or return an incorrect result without creating a valid runtime BOOL. Record actual outputs with attributed CLAIMs. No physical resources are inferred merely because an operation normally needs them.

## 4. Semantic primitives supporting existing composite content

Each entry below is a proposed primitive constructor returning TERM, with stable ID `v19/support/<name>`. Literals in expansions are exact identifiers or atomic values, not hidden sentences. Optional arguments are absent unless supported. All constructors are pure descriptions and assert no occurrence or truth. The positive application is the expansion table in Section 5; the contrast column identifies an excluded interpretation.

| Constructor and signature | Definition | Distinguishing boundary |
|---|---|---|
| requirement(property: STRING, value: STRING / NUMBER / BOOL) | Require the named property to have the given value in the enclosing request/artifact | Does not assert an existing artifact already satisfies it |
| include(item: STRING / TERM) | Require the identified content/item | Not permission to invent an instance in a recorded trace |
| exclude(item: STRING / TERM) | Require absence of that content/item | Not a claim of observed absence |
| activity(verb: STRING, actor?: STRING, object?: STRING / TERM, location?: STRING, instrument?: STRING, purpose?: TERM) | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | Does not execute or assert it |
| sequence(items: LIST[TERM]) | Ordered described activities/content | Not unordered conjunction |
| conjunction(items: LIST[TERM]) | All described components apply | Does not imply temporal order |
| subject(kind: STRING, qualifier?: STRING / TERM, location?: STRING, time?: STRING) | Subject matter with explicit qualifiers | Does not make a factual claim about it |
| decision(activity: TERM) | A decision whose content is the described activity | Not proof it was carried out |
| regression_case(framework: STRING, modifier: STRING, relation: STRING) | A regression scenario specifying affected framework, condition and relation | Does not invent a passing test or exact implementation |
| change_property(property: STRING, source: STRING, target: STRING) | Require target to inherit the property value from source | Not an arbitrary code patch |
| test_condition(condition: STRING, expected: BOOL) | A testable condition with the expected Boolean outcome | Expected outcome is not an observed result |
| preserve(component: STRING, index: NUMBER) | Keep the indexed component unchanged, using one-based indexing | Not preserve all components |
| remove_literal(text: STRING) | Remove occurrences of that exact literal in the stated artifact | Not remove similar markup unless specified |
| character_trait(property: STRING, value: STRING / NUMBER) | A character attribute | Not a claim about a real person |
| aesthetic(period: STRING, style: STRING) | A stylistic description with an explicit period | Not a character's age or production date |
| minimum_per_period(class: STRING, count: NUMBER, period: STRING) | At least count members of class in each period | Not a minimum total over the whole artifact |
| maximum_between_stops(activity: STRING, amount: NUMBER, unit: STRING) | Upper bound on the stated activity between successive stops | Not a limit on total daily duration |
| duration(amount: NUMBER, unit: STRING) | Requested elapsed/calendar extent | Word/item counts are not time |
| property_question(property: STRING, subject: STRING / TERM) | An open request for a property of a subject | Does not supply the property's value |

Counts and indices are nonnegative integers, with preserve index at least 1. Amounts are nonnegative. `minimum_per_period.class` uses semantic-category-value; period and temporal duration units use the temporal subset of duration-unit-value. `activity` verbs are atomic identifiers with their ordinary role-specific meaning as specified in each composite expansion; this primitive is for described content, not a route to automatic executable custom operations. A new ambiguous verb requires its own reviewed definition.

### Minimal trace relations and links

| Symbol | Kind/signature | Meaning and restriction |
|---|---|---|
| outcome | CLAIM `(event: EVENT, value: STRING / NUMBER / BOOL)` | Recorded output of that event; BY, STATUS and SOURCE required by spec |
| failure | CLAIM `(system: STRING)` | The indicated system is failing in context; hypothesis status does not establish truth |
| supports | LINK `(conclusion: CLAIM, premise: CLAIM)` | Source presents premise as a reason for conclusion; not necessarily logical entailment |
| rejects | LINK `(evidence: CLAIM, hypothesis: CLAIM)` | Source uses the evidence to reject that hypothesis |
| revises | LINK `(previous: CLAIM, replacement: CLAIM)` | Explicit replacement; use with AMENDS when changing active conversation content |

These primitive relations support recording existing operations and corrections; they are not a comprehensive reasoning vocabulary. Example D demonstrates use and the distinction between success and an assumption.

## 5. Composite migration definitions

The following are acyclic expansion templates, not inline BrainCode syntax. Each left-hand name is a TERM constructor; translate an application with `TERM <name>(...) -> <handle> : TERM`. Its output may fill a TERM-valued field. A bare occurrence of the old symbol in a STRING content/constraint field is deprecated. Nested applications on the right must be emitted as separate TERM bindings when expanded into BrainCode.

Parameters denoted `$name` on the right are copied from the corresponding typed argument on the left. Fixed strings are explicit semantic atoms. There is no silent default parameter value.

| Preserved name and signature | Structured expansion |
|---|---|
| content_status_update(subject: STRING) | `activity(verb="request_update", object=$subject)` |
| content_kyoto_itinerary() | `subject(kind="itinerary", location="Kyoto")` |
| content_decision_study_sgi_japan(actor: STRING) | `decision(activity=activity(verb="travel", actor=$actor, location=japan, purpose=activity(verb="study", actor=$actor, object=dom_sgi)))` |
| content_mixed_case_foreign_key_regression() | `regression_case(framework=django, modifier=mod_mixed_case, relation="ForeignKey")` |
| chg_inherit_multi_class(source: STRING, target: STRING) | `change_property(property="multi_class", source=$source, target=$target)` |
| assert_multinomial_scorer() | `test_condition(condition="multinomial_probabilistic_scoring", expected=TRUE)` |
| topic_school_work_routine() | `subject(kind="routine", qualifier=conjunction(items=[subject(kind="school"), subject(kind="work")]))` |
| topic_ai_earning_methods() | `subject(kind="methods", qualifier=activity(verb="earn", instrument="AI", object="income"))` |
| topic_greatest_cricketer_of_all_time() | `subject(kind="cricketer", qualifier=requirement(property="rank_by_greatness", value=1), time="all_time")` |
| topic_current_new_york_housing_market(as_of: STRING) | `subject(kind="housing_market", location="New York", time=$as_of)` |
| constraint_single_choice() | `requirement(property="choice_count", value=1)` |
| constraint_realistic() | `requirement(property="realistic", value=TRUE)` |
| constraint_respectful() | `requirement(property="respectful", value=TRUE)` |
| constraint_beginner() | `requirement(property="audience_expertise", value="beginner")` |
| constraint_budget_limited() | `requirement(property="budget_limited", value=TRUE)` |
| constraint_comprehensive() | `requirement(property="comprehensive", value=TRUE)` |
| constraint_exclude_flowery_language() | `exclude(item="flowery_language")` |
| constraint_exclude_liberation_theme() | `exclude(item="liberation_theme")` |
| constraint_include_character_attribute_list() | `include(item="character_attribute_list")` |
| transform_preserve_first_column() | `preserve(component="column", index=1)` |
| transform_remove_br() | `remove_literal(text="<br />")` |
| event_camper_in_sludge_pit() | `activity(verb="interact", actor="campers", location="sludge_pit")` |
| event_sadie_adler_unmasking() | `sequence(items=[activity(verb="remove", actor="Sadie Adler", object="hat"), activity(verb="peel", actor="Sadie Adler", object="skin")])` |
| char_female() | `character_trait(property="gender", value="female")` |
| char_age_14() | `character_trait(property="age_years", value=14)` |
| char_2000s_anime_style() | `aesthetic(period="2000s", style="anime")` |

The family names are retained for continuity, not treated as independent primitives. Fixed composite constructors can have zero arguments because their full decomposition is published here. This is different from an unexplained empty call.

`topic_jazz_piano` and `topic_classical_piano` remain established genre/instrument subject labels; when the source reasons separately about instrument and genre, use a decomposed TERM rather than pretending the label expresses that relationship. Named works/products remain exact referents. `topic_greatest_cricketer_of_all_time` leaves the criterion of greatness unresolved; it does not identify a winner or select an unstated metric.

`constraint_budget_limited` preserves a qualitative restriction without inventing a monetary ceiling. `constraint_17_plus` remains Needs clarification: the source conflates numeric age threshold and unspecified mature-rating systems. Use a numeric age requirement only if the source actually specifies it; do not convert every mature rating to age 17.

`event_*` constructors describe narrative content. Their result is TERM, never EVENT. `char_*` constructors describe a character, not an asserted real-world person. `chg_*` describes an intended change; `assert_*` describes an expected test condition, not test success.

## 6. Category rules that replace old membership rules

| Category | Migrated contract, positive use, and contrast |
|---|---|
| entity-name | STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted. |
| search-value | STRING refinements rank_ / dir_ / cat_ / avail_ / genre_ are separate. rank_rating may fill rank_field; genre_comedy may not. “Cheapest” usually requires both rank_price and dir_asc, not rank_price alone. |
| spatial-relation | STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous. |
| platform-name | STRING service/framework identity. `django` does not also mean the project being edited unless context establishes that identity. |
| location-name | STRING location descriptor. A `table` surface is not the generated artifact category art_table. |
| descriptive-value | STRING modifier/domain label; never a free-form proposition. dom_sgi needs its intended referent established before semantically dependent use. |
| format-value | STRING format. format_email is layout, not the action send_email. |
| tone-value | STRING register. tone_urgent describes urgency, not a concrete deadline. |
| duration-unit-value | STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds. |
| currency-value | STRING currency identity. A bare dollar sign is not always curr_usd; require contextual resolution. |
| recipient-value | STRING roles or explicit named recipients. A role is not an exact person's identity. Keep an explicit name where substituting a role loses information. |
| artifact-value | STRING artifact class for GENERATE.target. art_story says what kind of artifact to produce, not what occurs in its plot. |
| product-attribute-value | STRING color/size/product-market facets. gender_women describes a product category, not an assertion about a person's gender. |
| shape-value | STRING geometry. shape_round may select a circular object; it does not imply color or dimensions. |
| state-value | STRING condition used in selection. state_warm does not command heat; “hot” is not automatically synonymous with “warm.” |
| style-value | STRING production style. style_narrative does not establish that described events occurred. |
| locale-value | STRING locale. “English” alone does not always mean locale_en_us; preserve ambiguity. |
| metric-value | STRING metric identity, not a Boolean value. Uptime and response time need numeric observations with units; order-late is Boolean-valued. Do not type every metric as BOOL. |
| semantic-category-value | STRING class label used by typed constraints. class_temple describes a class, not an acquired physical temple reference. |
| code-value | path_/sym_ remain STRING identities; migrated chg_/assert_ are TERM constructors. Do not recover an exact file path by guessing from underscores. |
| content-value | Existing compounds become the constructors in Section 5. Their outputs go in topic/target/constraints as appropriate, not content, whose spec type remains STRING. |
| topic-value | Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it. |
| constraint-value | Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first. |
| transformation-value | TERM-described transformation. Pass it through constraints; no ungoverned transformations attribute. |
| event-value | TERM-described narrative event, not a recorded EVENT. Require inclusion explicitly when generating a story. |
| character-property-value | TERM-described trait/style. Use constraints and explicit inclusion/scope; do not use an ungoverned character_properties attribute. |
| capacity-unit-value | Preserve original binary-unit definitions for audit, but mark Needs clarification: GB/TB aliases conflate decimal and binary units. No silent change to scale. |
| cuisine-value | STRING cuisine class; cuisine_indian is a cuisine filter, not the location India. |
| reservation-status-value | STRING filter states; neither is a BOOL result binding. check_reservation_availability returns a BOOL with a distinct handle. |

### Attributes and Generate extensions

`target`, `cuisine`, `min_ram`, `ram_unit`, `reservation_availability`, `rank_field`, `rank_direction`, and `quantity` from the source inventory are argument names, not values. Their types are supplied by the operation tables. Attribute legality is per operation, never granted globally by an attribute-name entry.

GENERATE supports exactly the revised spec's core fields. All retained artifact symbols return STRING in this profile. Numeric/list generation requires another explicit artifact profile, not a guessed result type.

Migrate old itinerary fields to TERM constraints:

- duration + duration_unit -> `duration(amount=..., unit=...)`.
- stop_min_per_day + stop_requirement -> `minimum_per_period(class=..., count=..., period=unit_day)`; do not assume temple if the class is absent.
- max_walk_duration + max_walk_duration_unit -> `maximum_between_stops(activity="walk", amount=..., unit=...)`.

No compatibility shorthand for these attributes is enabled by this file; use the expanded forms. Domain fields `events`, `character_properties`, and `transformations` in old examples likewise migrate into explicitly scoped TERMS supplied through constraints. This preserves meaning without changing the spec's core attribute types.

Exact message content remains STRING. A message-purpose composite cannot be passed directly to send_email.content; first request generation of the message from its structured topic, then send the resulting STRING. Opaque free-text fallback must be recorded as such and does not count as structured coverage.

## 7. Corrected examples

These are complete documents, not incomplete fragments. They use the supplemental entries in Section 8. The examples have been reviewed for the documented contracts; no implemented BrainCode parser has verified them.

### A. Select two pillows and move those objects

NL: “Move two pillows from the sofa onto the armchair.” No implied heating, cleaning, or extra resources.

```braincode
MODE REQUEST
ENTRYPOINT Pillow
TASK Pillow {
  ACTION pick_up(target=pillow, quantity=2, source=sofa) -> pillow_refs : LIST[REF[STRING]]
  FOR EACH item IN pillow_refs {
    ACTION place(target=item, destination=armchair, relation=on)
  }
}
```

### B. Preserve the class and amount of an itinerary constraint

NL: “Make a three-day Kyoto itinerary, including at least one temple each day, with at most twenty minutes of walking between stops.”

```braincode
MODE REQUEST
ENTRYPOINT Itinerary
TASK Itinerary : STRING {
  TERM content_kyoto_itinerary() -> content_kyoto_itinerary_2 : TERM
  TERM duration(amount=3, unit=unit_day) -> duration_2 : TERM
  TERM minimum_per_period(class=class_temple, count=1, period=unit_day) -> minimum_per_period_2 : TERM
  TERM maximum_between_stops(activity="walk", amount=20, unit=unit_minute) -> maximum_between_stops_2 : TERM
  GENERATE(target=art_itinerary, constraints=[duration_2, minimum_per_period_2, maximum_between_stops_2], topic=content_kyoto_itinerary_2) -> itinerary : STRING
  RETURN itinerary
}
```

### C. Existing constraint symbol becomes a typed construction

NL: “Suggest realistic pickup lines.” This example treats the message as a conversational request for suggestions.

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

The TERM is a requirement; it does not assert that an existing answer is realistic. Unlike the old STRING list, constraints has LIST[TERM].

### D. Record an actual test outcome without asserting overall correctness

Source manifest: `t1:tests` identifies a supplied agent/tool trace in which the scikit-learn test run exits successfully. The source explicitly reports the selected tests passed; it does not establish that every bug is fixed.

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=AGENT {
    RECORD ACTION run_tests(target=sklearn) STATUS succeeded SOURCE "t1:tests" -> run_tests_event : EVENT
    CLAIM outcome(event=run_tests_event, value=TRUE) BY role_agent STATUS observed SOURCE "t1:tests" -> outcome_2 : CLAIM
  }
}
```

### E. Preserve exact wording through generation and sending

NL: “Write a polite email asking my manager for an update on Project Atlas, and send it.”

```braincode
MODE REQUEST
ENTRYPOINT ShortText
TASK ShortText {
  TERM content_status_update(subject="Project Atlas") -> content_status_update_2 : TERM
  GENERATE(target=art_short_text, format=format_email, tone=tone_polite, topic=content_status_update_2) -> short_text : STRING
  ACTION send_email(content=short_text, recipient=role_manager, tone=tone_polite)
}
```

The input authorizes sending in this represented request. Reading this encoding does not itself authorize a tool action. Generating a purpose label and sending that label verbatim would not preserve the request.

## 8. Minimal supplemental entries

These entries were used in old examples or are needed by the migrated examples; they are explicitly declared here rather than assumed to exist.

| Symbol | Kind/signature | Definition and contrast |
|---|---|---|
| pillow | entity-name STRING | A pillow; not a specific selected pillow until pick_up returns REF |
| sofa | entity-name STRING | A sofa used as source/destination; not the pillow on it |
| armchair | entity-name STRING | An armchair; distinct from a sofa |
| coffee_maker | entity-name STRING | A coffee-making appliance; not automatically a heating resource |
| art_itinerary | artifact-value STRING | An ordered travel plan; GENERATE returns STRING, not booked travel |
| extract | Action `(target: LIST[REF[STRING]], limit: NUMBER) -> LIST[REF[STRING]]` | First limit results, preserving order and identity; limit is a nonnegative integer; limit=1 is still a list |

Supplementary aliases are empty unless explicitly stated. The same static restrictions and RECORD signature conversion as Section 3 apply. No broader domain expansion is intended.

## 9. Review points and migration boundaries

- `cap_gb` and `cap_tb`: retain source wording for audit; resolve decimal versus binary scale before acceptance.
- `constraint_17_plus`: resolve exact age threshold versus rating system before acceptance.
- `dom_sgi`: the source names an acronym without resolving its referent. Preserve it, but flag semantically dependent translations until context/review resolves it. No expansion of the acronym is invented here.
- Bare money symbols, locale aliases, warm/hot, and ranking phrases are contextual aliases. Matching a token alone is not enough to normalize meaning.
- The source's “all previously listed members remain valid” wording is replaced by the explicit inventory here. Unavailable historical entries are not guessed.
- Source examples using missing symbols or silently losing constraints are replaced by the complete examples above. This file does not preserve those defects as normative demonstrations.
- The revised specification's own illustrative trace/claim profiles remain examples, not a claim that this migration covers every possible reasoning construct.

This is a migrated seed, not a production-certified release. Structural and inventory checks do not replace a parser or semantic evaluation. Publishing requires resolution of entries marked Needs clarification and review of the proposed signatures/composite expansions.

## 10. Source-member inventory

Every explicitly listed source member appears below. Stable ID is `v19/<category>/<symbol>`. For simple values, the retained definition and aliases below combine with the category-level type, example and contrast contract in Section 6. Operation signatures and contrasts are in Section 3; composite definitions are in Section 5. Original synonym hints are retained as source evidence and are subordinate to the contextual restrictions above.


### Inventory: structural-word

| Symbol | Retained source definition / alias hints | Migration status |
|---|---|---|
| `TASK` | Declares a task. | Structural |
| `ACTION` | Executes an external operation. | Structural |
| `GENERATE` | Generates a non-effectful artifact. | Structural |
| `UTTER` | Records a speech act. | Structural |
| `CONVO` | Declares a conversation. | Structural |
| `TURN` | Declares a conversation turn. | Structural |
| `ENTRYPOINT` | Names the single execution root. | Structural |
| `IF` | Starts a conditional branch. | Structural |
| `THEN` | Starts the true branch. | Structural |
| `ELSE` | Starts the false branch. | Structural |
| `FOR` | Starts iteration. | Structural |
| `EACH` | Marks per-member iteration. | Structural |
| `IN` | Introduces an iterable or relation. | Structural |
| `ANY` | Existential quantifier. | Structural |
| `ALL` | Universal quantifier. | Structural |
| `SATISFIES` | Introduces a quantifier condition. | Structural |
| `LET` | Binds a value. | Structural |
| `RETURN` | Returns a task value. | Structural |
| `NUMBER` | Numeric type. | Structural |
| `STRING` | Text type. | Structural |
| `BOOL` | Boolean type. | Structural |
| `LIST` | List type. | Structural |
| `REF` | Runtime entity-reference type. | Structural |
| `TRUE` | Boolean true literal. | Structural |
| `FALSE` | Boolean false literal. | Structural |
| `SPEAKER` | Speaker label. | Structural |
| `USER` | User speaker. | Structural |
| `AGENT` | Agent speaker. | Structural |
| `REPLY_TO` | Turn adjacency. | Structural |
| `REVISES` | Turn correction. | Structural |
| `DECREASES` | Recursion guard. | Structural |
| `CONTEXT` | Task context. | Structural |
| `AND` | Logical AND. | Structural |
| `OR` | Logical OR. | Structural |
| `NOT` | Logical NOT. | Structural |
| `{` | Block start. | Structural |
| `}` | Block end. | Structural |
| `(` | Paren start. | Structural |
| `)` | Paren end. | Structural |
| `[` | Bracket start. | Structural |
| `]` | Bracket end. | Structural |
| `,` | Separator. | Structural |
| `:` | Type annotator. | Structural |
| `=` | Assignment. | Structural |
| `->` | Result bind. | Structural |
| `==` | Equality. | Structural |
| `!=` | Inequality. | Structural |
| `<` | Less-than. | Structural |
| `<=` | Less-or-equal. | Structural |
| `>` | Greater-than. | Structural |
| `>=` | Greater-or-equal. | Structural |
| `-` | Arithmetic difference. | Structural |

### Inventory: operation-vocabulary

| Symbol | Retained source definition / alias hints | Migration status |
|---|---|---|
| `open_page` | Navigate to a page. (natural-language synonyms: go to) | Adapted |
| `click` | Click an element. | Adapted |
| `select_filter` | Apply one filter. | Adapted |
| `apply_filters` | Apply multiple filters. | Adapted |
| `sort` | Rank a list. (natural-language synonyms: rank, order by) | Adapted |
| `search_travel` | Search travel. | Adapted |
| `search_transit` | Search transit. | Adapted |
| `search_web` | Search a catalog or web source. (natural-language synonyms: find, look for) | Adapted |
| `pick_up` | Acquire an entity. (natural-language synonyms: grab, take, retrieve) | Adapted |
| `place` | Place an acquired entity. (natural-language synonyms: put, insert) | Adapted |
| `rinse` | Rinse an entity. (natural-language synonyms: wash) | Adapted |
| `heat` | Heat an entity. | Adapted |
| `chill` | Chill an entity. | Adapted |
| `slice` | Cut an entity into pieces. (natural-language synonyms: chop, cut) | Adapted |
| `pour` | Pour a liquid. | Adapted |
| `modify_code` | Change source code. (natural-language synonyms: fix, reduce, optimize) | Adapted |
| `run_tests` | Run tests. | Adapted |
| `add_to_cart` | Add a selected item to a cart. | Adapted |
| `check_reservation_availability` | Check whether reservations are available. (natural-language synonyms: check reservation availability) | Adapted |
| `send_email` | Send email. (natural-language synonyms: email) | Adapted |
| `send_message` | Send a message. (natural-language synonyms: text) | Adapted |
| `ask` | Ask for information or advice. (natural-language synonyms: ask, how should) | Adapted |
| `inform` | State information. | Adapted |
| `respond` | Answer a request. (natural-language synonyms: answer) | Adapted |
| `propose` | Propose an idea. | Adapted |
| `correct` | Correct a statement. | Adapted |
| `acknowledge` | Acknowledge a statement. | Adapted |
| `confirm` | Confirm a statement. | Adapted |
| `decline` | Decline a request. | Adapted |

### Inventory: attribute-name

| Symbol | Retained source definition / alias hints | Migration status |
|---|---|---|
| `target` | The acted-on entity or generated artifact. | Structural |
| `cuisine` | Restaurant or food cuisine from cuisine-value. | Structural |
| `min_ram` | Minimum RAM capacity as NUMBER. (natural-language synonyms: RAM or more, at least RAM) | Structural |
| `ram_unit` | Unit for min_ram from capacity-unit-value. | Structural |
| `reservation_availability` | Required reservation state from reservation-status-value. | Structural |
| `rank_field` | Field used by sort from search-value. | Structural |
| `rank_direction` | Sort direction from search-value. | Structural |
| `quantity` | Explicit count as NUMBER. | Structural |

### Inventory: entity-name

| Symbol | Retained source definition / alias hints | Migration status |
|---|---|---|
| `mug` | Drinking cup. (natural-language synonyms: mug) | Adapted |
| `sink` | Washing basin. (natural-language synonyms: sink) | Adapted |
| `resource_sink` | Canonical abstract washing resource when no particular sink is named. | Adapted |
| `resource_heater` | Canonical abstract heating resource when no particular appliance is named. | Adapted |
| `resource_chiller` | Canonical abstract chilling resource when no particular appliance is named. | Adapted |

### Inventory: search-value

| Symbol | Retained source definition / alias hints | Migration status |
|---|---|---|
| `rank_price` | Rank or filter field: monetary cost. (natural-language synonyms: cheapest, lowest price) | Adapted |
| `rank_rating` | Rank or filter field: user or critic score. | Adapted |
| `rank_distance` | Rank field: proximity. (natural-language synonyms: nearest, closest) | Adapted |
| `dir_asc` | Ascending rank direction. (natural-language synonyms: lowest first) | Adapted |
| `dir_desc` | Descending rank direction. (natural-language synonyms: highest first) | Adapted |
| `cat_game` | Category: video game. | Adapted |
| `cat_limited_time_offers` | Category: time-limited deals. | Adapted |
| `avail_in_stock` | Available for purchase now. (natural-language synonyms: available) | Adapted |
| `avail_out_of_stock` | Unavailable for purchase now. (natural-language synonyms: sold out) | Adapted |
| `genre_comedy` | Genre: comedy. | Adapted |

### Inventory: spatial-relation

| Symbol | Retained source definition / alias hints | Migration status |
|---|---|---|
| `in` | Contained within. (natural-language synonyms: inside) | Retained |
| `on` | Resting atop. (natural-language synonyms: on top of) | Retained |
| `under` | Beneath. (natural-language synonyms: below) | Retained |
| `next_to` | Adjacent to. (natural-language synonyms: beside) | Retained |
| `left_of` | To the left of. (natural-language synonyms: left of) | Retained |
| `right_of` | To the right of. (natural-language synonyms: right of) | Retained |
| `in_front_of` | Positioned in front of. (natural-language synonyms: in front of) | Retained |
| `behind` | Positioned behind. | Retained |

### Inventory: platform-name

| Symbol | Retained source definition / alias hints | Migration status |
|---|---|---|
| `netflix` | Streaming platform. | Retained |
| `django` | Web framework. | Retained |
| `sklearn` | Machine learning library. | Retained |
| `youtube` | Video platform. | Retained |

### Inventory: location-name

| Symbol | Retained source definition / alias hints | Migration status |
|---|---|---|
| `corner` | A corner area. | Retained |
| `table` | A table surface. | Retained |
| `eastern_cape` | Eastern Cape region. | Retained |
| `japan` | Country of Japan. | Retained |

### Inventory: descriptive-value

| Symbol | Retained source definition / alias hints | Migration status |
|---|---|---|
| `mod_mixed_case` | Mixed-case modifier. (natural-language synonyms: mixed case) | Retained |
| `dom_safari` | Safari domain concept. (natural-language synonyms: safari) | Retained |
| `dom_pain` | Pain domain concept. (natural-language synonyms: pain) | Retained |
| `dom_ovr` | One-versus-rest domain concept. | Retained |
| `dom_sgi` | SGI domain concept. | Needs clarification |

### Inventory: format-value

| Symbol | Retained source definition / alias hints | Migration status |
|---|---|---|
| `format_plain_text` | Unstructured prose text. (natural-language synonyms: plain text) | Retained |
| `format_bullet_list` | Bulleted list. (natural-language synonyms: bullet points) | Retained |
| `format_numbered_list` | Numbered list. (natural-language synonyms: numbered steps) | Retained |
| `format_email` | Email layout. (natural-language synonyms: as an email) | Retained |
| `format_markdown` | Markdown layout. (natural-language synonyms: in markdown) | Retained |
| `format_table` | Tabular layout. (natural-language synonyms: as a table) | Retained |
| `format_pdf` | PDF document. (natural-language synonyms: as a pdf) | Retained |
| `format_newsletter` | Newsletter layout. (natural-language synonyms: newsletter) | Retained |
| `format_structured_report` | Headed structured report layout. (natural-language synonyms: structured report, report) | Retained |

### Inventory: tone-value

| Symbol | Retained source definition / alias hints | Migration status |
|---|---|---|
| `tone_polite` | Courteous, respectful register. (natural-language synonyms: politely, kindly) | Retained |
| `tone_formal` | Formal register. (natural-language synonyms: formally) | Retained |
| `tone_casual` | Informal register. (natural-language synonyms: casually) | Retained |
| `tone_concise` | Brief, to-the-point register. (natural-language synonyms: briefly, concisely) | Retained |
| `tone_neutral` | Plain, unmarked register. | Retained |
| `tone_urgent` | Conveys urgency. (natural-language synonyms: urgently, ASAP) | Retained |
| `tone_empathetic` | Conveys empathy/understanding. (natural-language synonyms: sympathetically) | Retained |
| `tone_professional` | Workplace-appropriate register. (natural-language synonyms: professionally) | Retained |

### Inventory: duration-unit-value

| Symbol | Retained source definition / alias hints | Migration status |
|---|---|---|
| `unit_second` | Second. (natural-language synonyms: seconds, sec) | Adapted |
| `unit_minute` | Minute. (natural-language synonyms: minutes, min) | Adapted |
| `unit_hour` | Hour. (natural-language synonyms: hours) | Adapted |
| `unit_day` | Day. (natural-language synonyms: days) | Adapted |
| `unit_week` | Week. (natural-language synonyms: weeks) | Adapted |
| `unit_month` | Month. (natural-language synonyms: months) | Adapted |
| `unit_year` | Year. (natural-language synonyms: years) | Adapted |
| `unit_word` | Rendered whitespace-delimited word. (natural-language synonyms: words) | Adapted |
| `unit_item` | Top-level generated list or report item. (natural-language synonyms: items, entries) | Adapted |
| `unit_paragraph` | Paragraph of text. (natural-language synonyms: paragraphs, paragraph) | Adapted |
| `unit_character` | One Unicode scalar value in the final rendered artifact; line endings are normalized to LF before counting. (natural-language synonyms: characters, chars) | Adapted |

### Inventory: currency-value

| Symbol | Retained source definition / alias hints | Migration status |
|---|---|---|
| `curr_usd` | United States dollar. (natural-language synonyms: $, usd, dollars) | Retained |
| `curr_eur` | Euro. (natural-language synonyms: eur, euros) | Retained |
| `curr_clp` | Chilean peso. (natural-language synonyms: clp, Chilean pesos, Chilean peso) | Retained |

### Inventory: recipient-value

| Symbol | Retained source definition / alias hints | Migration status |
|---|---|---|
| `role_user` | The requesting human. (natural-language synonyms: me, I) | Adapted |
| `role_agent` | The assistant. (natural-language synonyms: you, the assistant) | Adapted |
| `role_manager` | The user's manager. (natural-language synonyms: my manager, boss) | Adapted |
| `role_professor` | The user's professor/instructor. (natural-language synonyms: my professor, teacher) | Adapted |
| `role_friend` | A friend of the user. (natural-language synonyms: my friend) | Adapted |
| `role_colleague` | A coworker of the user. (natural-language synonyms: my colleague, coworker) | Adapted |
| `role_support_team` | A customer-support team. (natural-language synonyms: support, customer service) | Adapted |
| `role_customer` | A customer/client of the user. (natural-language synonyms: the customer, client) | Adapted |

### Inventory: artifact-value

| Symbol | Retained source definition / alias hints | Migration status |
|---|---|---|
| `art_story` | Narrative story. | Retained |
| `art_short_text` | Short free text. | Retained |
| `art_plan` | Actionable plan. | Retained |
| `art_structured_report` | Headed/structured report. | Retained |
| `art_technical_explanation` | Technical explanation of a concept. | Retained |
| `art_character_profile` | Descriptive character profile. | Retained |

### Inventory: product-attribute-value

| Symbol | Retained source definition / alias hints | Migration status |
|---|---|---|
| `color_yellow` | Yellow. | Retained |
| `color_red` | Red. | Retained |
| `color_black` | Black. | Retained |
| `color_white` | White. | Retained |
| `size_small` | Small size. (natural-language synonyms: small, S) | Retained |
| `size_medium` | Medium size. (natural-language synonyms: medium, M) | Retained |
| `size_large` | Large size. (natural-language synonyms: large, L) | Retained |
| `gender_women` | Women's/female-targeted. (natural-language synonyms: women, female) | Retained |
| `gender_men` | Men's/male-targeted. (natural-language synonyms: men, male) | Retained |
| `gender_unisex` | Unisex. (natural-language synonyms: unisex) | Retained |

### Inventory: shape-value

| Symbol | Retained source definition / alias hints | Migration status |
|---|---|---|
| `shape_round` | Circular/round. (natural-language synonyms: round, circular) | Retained |
| `shape_square` | Square. (natural-language synonyms: square) | Retained |
| `shape_rectangular` | Rectangular. (natural-language synonyms: rectangular, rectangle) | Retained |
| `shape_oval` | Oval. (natural-language synonyms: oval) | Retained |
| `shape_triangular` | Triangular. (natural-language synonyms: triangular, triangle) | Retained |

### Inventory: state-value

| Symbol | Retained source definition / alias hints | Migration status |
|---|---|---|
| `state_warm` | Warm or heated condition. (natural-language synonyms: warm, hot) | Adapted |
| `state_cold` | Cold or chilled condition. (natural-language synonyms: cold, chilled) | Adapted |
| `state_microwaved` | Has been microwaved. (natural-language synonyms: microwaved) | Adapted |
| `state_clean` | Clean condition. (natural-language synonyms: clean) | Adapted |
| `state_dirty` | Dirty condition. (natural-language synonyms: dirty) | Adapted |
| `state_full` | Contains its intended material or remaining usable amount. (natural-language synonyms: full, filled) | Adapted |
| `state_empty` | Contains no intended material or usable remaining amount. (natural-language synonyms: empty, used up) | Adapted |

### Inventory: style-value

| Symbol | Retained source definition / alias hints | Migration status |
|---|---|---|
| `style_narrative` | Story-like narrative style. (natural-language synonyms: narrative, story-style) | Retained |
| `style_technical` | Technical/expository style. (natural-language synonyms: technical) | Retained |
| `style_academic` | Academic style. (natural-language synonyms: academic) | Retained |
| `style_persuasive` | Persuasive/argumentative style. (natural-language synonyms: persuasive) | Retained |
| `style_catchy` | Catchy, attention-grabbing style. (natural-language synonyms: catchy) | Retained |

### Inventory: locale-value

| Symbol | Retained source definition / alias hints | Migration status |
|---|---|---|
| `locale_en_us` | US English. (natural-language synonyms: english, en-us) | Adapted |
| `locale_en_gb` | UK English. (natural-language synonyms: british english) | Adapted |
| `locale_hi_en` | Hinglish (Hindi-English mix). (natural-language synonyms: hinglish) | Adapted |
| `locale_es` | Spanish. (natural-language synonyms: spanish) | Adapted |
| `locale_fr` | French. (natural-language synonyms: french) | Adapted |

### Inventory: metric-value

| Symbol | Retained source definition / alias hints | Migration status |
|---|---|---|
| `metric_uptime` | Service uptime status. (natural-language synonyms: uptime, is up) | Adapted |
| `metric_response_time` | Support response time. (natural-language synonyms: response time) | Adapted |
| `metric_compatibility` | Compatibility status. (natural-language synonyms: compatible) | Adapted |
| `metric_order_late` | Whether an order is late. (natural-language synonyms: order is late, delayed) | Adapted |
| `metric_first_time_buyer` | Whether the customer is a first-time buyer. (natural-language synonyms: first-time buyer, new customer) | Adapted |
| `metric_repeat_buyer` | Whether the customer is a repeat buyer. (natural-language synonyms: repeat buyer, returning customer) | Adapted |

### Inventory: semantic-category-value

| Symbol | Retained source definition / alias hints | Migration status |
|---|---|---|
| `class_temple` | The abstract class of temples. (natural-language synonyms: temple, temples) | Retained |
| `class_town` | The abstract class of towns. (natural-language synonyms: town, towns) | Retained |

### Inventory: code-value

| Symbol | Retained source definition / alias hints | Migration status |
|---|---|---|
| `path_sklearn_linear_model_logistic_py` | The scikit-learn logistic module path. | Retained |
| `sym_log_reg_scoring_path` | The _log_reg_scoring_path program symbol. | Retained |
| `chg_inherit_multi_class` | Change requiring a constructed estimator to inherit multi_class. | Composite |
| `assert_multinomial_scorer` | Assertion that multinomial probabilistic scoring succeeds. | Composite |

### Inventory: content-value

| Symbol | Retained source definition / alias hints | Migration status |
|---|---|---|
| `content_status_update` | A request for a status update. (natural-language synonyms: status update) | Composite |
| `content_kyoto_itinerary` | A Kyoto itinerary subject. | Composite |
| `content_decision_study_sgi_japan` | A personal decision to travel to Japan to study SGI. | Composite |
| `content_mixed_case_foreign_key_regression` | A mixed-case Django app-name ForeignKey regression test purpose. | Composite |

### Inventory: topic-value

| Symbol | Retained source definition / alias hints | Migration status |
|---|---|---|
| `topic_politics` | Politics. | Retained |
| `topic_jazz_piano` | Jazz piano. | Retained |
| `topic_classical_piano` | Classical piano. | Retained |
| `topic_spider_man_2` | Marvel's Spider-Man 2. | Retained |
| `topic_baldurs_gate_3` | Baldur's Gate 3. | Retained |
| `topic_macbook_pro_2017` | MacBook Pro 2017. | Retained |
| `topic_school_work_routine` | School and work routine. | Composite |
| `topic_ai_earning_methods` | AI earning methods. | Composite |
| `topic_pickup_lines` | Pickup lines. | Retained |
| `topic_greatest_cricketer_of_all_time` | Greatest cricketer of all time. | Composite |
| `topic_current_new_york_housing_market` | Current New York housing market. | Composite |

### Inventory: constraint-value

| Symbol | Retained source definition / alias hints | Migration status |
|---|---|---|
| `constraint_17_plus` | Rated 17+ or mature. | Needs clarification |
| `constraint_single_choice` | Must pick a single choice. | Composite |
| `constraint_realistic` | Must be realistic. | Composite |
| `constraint_respectful` | Must be respectful. | Composite |
| `constraint_beginner` | Targeted at beginners. | Composite |
| `constraint_budget_limited` | Limited budget. | Composite |
| `constraint_comprehensive` | Must be comprehensive. | Composite |
| `constraint_exclude_flowery_language` | Avoid flowery language. | Composite |
| `constraint_exclude_liberation_theme` | Avoid liberation theme. | Composite |
| `constraint_include_character_attribute_list` | Include character attributes. | Composite |

### Inventory: transformation-value

| Symbol | Retained source definition / alias hints | Migration status |
|---|---|---|
| `transform_preserve_first_column` | Preserve the first column of a table. | Composite |
| `transform_remove_br` | Remove <br /> tags. | Composite |

### Inventory: event-value

| Symbol | Retained source definition / alias hints | Migration status |
|---|---|---|
| `event_camper_in_sludge_pit` | Campers interacting in a sludge pit. | Composite |
| `event_sadie_adler_unmasking` | Sadie Adler taking off her hat and peeling skin. | Composite |

### Inventory: character-property-value

| Symbol | Retained source definition / alias hints | Migration status |
|---|---|---|
| `char_female` | Female gender. (natural-language synonyms: female) | Composite |
| `char_age_14` | Age 14. (natural-language synonyms: 14) | Composite |
| `char_2000s_anime_style` | 2000s anime style. | Composite |

### Inventory: capacity-unit-value

| Symbol | Retained source definition / alias hints | Migration status |
|---|---|---|
| `cap_gb` | One gibibyte-equivalent RAM capacity unit. (natural-language synonyms: GB, gigabytes) | Needs clarification |
| `cap_tb` | One tebibyte-equivalent capacity unit. (natural-language synonyms: TB, terabytes) | Needs clarification |

### Inventory: cuisine-value

| Symbol | Retained source definition / alias hints | Migration status |
|---|---|---|
| `cuisine_indian` | Indian cuisine. (natural-language synonyms: Indian food, Indian) | Retained |
| `cuisine_italian` | Italian cuisine. (natural-language synonyms: Italian food, Italian) | Retained |

### Inventory: reservation-status-value

| Symbol | Retained source definition / alias hints | Migration status |
|---|---|---|
| `reservation_available` | A reservation can be made. (natural-language synonyms: reservation availability, available reservations) | Retained |
| `reservation_unavailable` | A reservation cannot be made. (natural-language synonyms: no reservations) | Retained |

Inventory audit: 252 explicitly listed source members across 32 categories. Source SHA-256: `3ea402869380ef1e12584b6ebddee355f1de0a8e5a554fc1a1b1dc0510ffcceb`.
