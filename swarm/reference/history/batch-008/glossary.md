# BrainCode glossary

Language 19.0.0-draft.1 · glossary 19.0.0-draft.1+g11 · 632 live records (2 deprecated, listed last)

Rendered from glossary.jsonl (the source of truth); see swarm/README.md for how to edit it. In cells, `<br>` is a line break and `\|` a literal pipe. To deprecate, set status to `Deprecated` and give a reason in `not`; never delete a row. Signatures: `?` optional, `A / B` alternatives, `void` no result. `not` is the nearest wrong reading of the symbol.

## Shared rules

| symbol | kind | definition |
|---|---|---|
| rule_reading_guide | rule | The specification governs grammar, scope, mode, types and canonical form. This glossary governs the vocabulary meanings and signatures below. Signatures are documentation notation: `?` means optional; `A / B` means explicitly allowed alternative types; `void` means no result. These are not new BrainCode type tokens. An omitted optional value is unspecified, not a fabricated default.<br><br>Stable IDs use `v19/<category>/<symbol>`. Supplementary entries use `v19/support/<symbol>` and composite constructors use `v19/composite/<symbol>`. Their source is this migration unless the inventory identifies the original category. Each family table supplies shared typing, restrictions, and example conventions for its member rows.<br><br>Migration statuses:<br><br>All statuses describe this proposed migration, not prior human approval. No symbol is silently deleted. Natural-language aliases are contextual recognition hints, not assertions that every occurrence of the phrase has the same meaning. When a context suggests different meanings, report the ambiguity rather than selecting by alphabetical order.<br><br>For retained value entries, kind is `primitive value`, signature is `STRING` refined by its category, and the member's gloss is its definition. This uses the revised spec's explicit primitive option; it does not claim every English expression is semantically atomic. Complex propositions and requirements instead receive expansions below.<br><br>\| Status \| Meaning \|<br>\|---\|---\|<br>\| Retained \| The source meaning remains usable under the category contract \|<br>\| Adapted \| The symbol remains, with the revised contract stated here \|<br>\| Composite \| The name is retained as a TERM constructor with an explicit expansion; bare STRING use is deprecated \|<br>\| Needs clarification \| Preserved for review, but cannot be used as an accepted entry in a frozen evaluation release until the ambiguity is resolved \|<br>\| Structural \| Syntax or an argument name, not a STRING-valued concept \| |
| rule_recording_signatures | rule | For RECORD ACTION, use the same operation attributes with every REF[STRING] replaced by TERM describing the identified object, and every LIST[REF[STRING]] by LIST[TERM]. Other parameter types and categories remain. RECORD returns EVENT regardless of the REQUEST result. A recording of run_tests may therefore fail or return an incorrect result without creating a valid runtime BOOL. Record actual outputs with attributed CLAIMs. No physical resources are inferred merely because an operation normally needs them. |
| rule_speech_acts_general | rule | All are UTTER-only, return void, and may use the specification's audience, recipient, tone, topic, content and LIST[TERM] constraints attributes. Required semantic arguments cannot be replaced by content="..." to claim fully structured coverage. There are no UTTER result bindings. |
| rule_structural_constructs | rule | \| Source entry \| Migrated meaning and example reference \|<br>\|---\|---\|<br>\| Types & Lexicon \| Accepted value symbols remain STRING; TERM, CLAIM and EVENT are distinct semantic types. Example A shows typed references. \|<br>\| Task \| A REQUEST plan, not evidence that its work occurred. Exactly one entrypoint. Examples A and B. \|<br>\| Action \| Requested external work with an exact signature. TRACE uses RECORD and produces EVENT. Examples A and D. \|<br>\| Utterance \| A speech act inside TURN; never binds a STRING result. Targets and constraints carry meaning. Example C. \|<br>\| Check \| Pure comparisons of supported types; CLAIM is not BOOL. A Check belongs inside IF or a quantified Check, never alone as a step. \|<br>\| Flow-If \| REQUEST-only branching in a Task or Turn; branch-local bindings do not escape. No TRACE execution. \|<br>\| Iterate \| Finite sequential LIST iteration; ANY/ALL use pure predicates. A list of one REF is still a list. Example A. \|<br>\| Bind \| Immutable LET and typed producer results; no UTTER result. Earlier top-level semantic objects may be read across turns using qualified names. \|<br>\| Conversation \| One turn per supplied message. Whole replacement uses REVISES; targeted claim replacement uses AMENDS and revises links. \|<br>\| Generate \| Requested artifact production. Typed glossary extensions replace hard-coded domain exceptions; artifact constraints are LIST[TERM]. Example B. \|<br>\| descriptive-value \| Residual modifiers and domains; no permission to hide arbitrary propositions in names. \|<br>\| canonical-form \| Target first, then alphabetical attributes; canonical handles; semantic aliases only; no automatic custom operations. \|<br>\| types-lexicon, action, bind \| Retained documentation aliases of their capitalized entries, not separate syntax. Empty TASK examples are removed. \|<br><br>Additions required to express the migrated contracts: MODE REQUEST/TRACE, TERM, CLAIM, EVENT, LINK, RECORD, CALL, BY, STATUS, SOURCE, and AMENDS. The specification defines their syntax. These additions do not expand the subject-domain inventory.<br><br>Structural tokens inherited from the source remain listed in the inventory. Add `.` for qualified references. `asserted`, `observed`, `inferred`, `assumed`, `hypothesized`, `reported`, `attempted`, `succeeded`, `failed`, and `unknown` are reserved in their grammar positions. SOURCE is a keyword; lower-case `source` can be an operation argument. Exact names are case-sensitive. |
| rule_trace_relations_general | rule | These primitive relations support recording existing operations and corrections; they are not a comprehensive reasoning vocabulary. Example D demonstrates use and the distinction between success and an assumption. |
| rule_attributes_and_generate | rule | `target`, `cuisine`, `min_ram`, `ram_unit`, `reservation_availability`, `rank_field`, `rank_direction`, and `quantity` from the source inventory are argument names, not values. Their types are supplied by the operation tables. Attribute legality is per operation, never granted globally by an attribute-name entry.<br><br>GENERATE supports exactly the revised spec's core fields. All retained artifact symbols return STRING in this profile. Numeric/list generation requires another explicit artifact profile, not a guessed result type.<br><br>Migrate old itinerary fields to TERM constraints:<br><br>- duration + duration_unit -> `duration(amount=..., unit=...)`.<br><br>- stop_min_per_day + stop_requirement -> `minimum_per_period(class=..., count=..., period=unit_day)`; do not assume temple if the class is absent.<br><br>- max_walk_duration + max_walk_duration_unit -> `maximum_between_stops(activity="walk", amount=..., unit=...)`.<br><br>No compatibility shorthand for these attributes is enabled by this file; use the expanded forms. Domain fields `events`, `character_properties`, and `transformations` in old examples likewise migrate into explicitly scoped TERMS supplied through constraints. This preserves meaning without changing the spec's core attribute types.<br><br>Exact message content remains STRING. A message-purpose composite cannot be passed directly to send_email.content; first request generation of the message from its structured topic, then send the resulting STRING. Opaque free-text fallback must be recorded as such and does not count as structured coverage. |
| rule_composites_general | rule | The following are acyclic expansion templates, not inline BrainCode syntax. Each left-hand name is a TERM constructor; translate an application with `TERM <name>(...) -> <handle> : TERM`. Its output may fill a TERM-valued field. A bare occurrence of the old symbol in a STRING content/constraint field is deprecated. Nested applications on the right must be emitted as separate TERM bindings when expanded into BrainCode.<br><br>Parameters denoted `$name` on the right are copied from the corresponding typed argument on the left. Fixed strings are explicit semantic atoms. There is no silent default parameter value.<br><br>The family names are retained for continuity, not treated as independent primitives. Fixed composite constructors can have zero arguments because their full decomposition is published here. This is different from an unexplained empty call.<br><br>`topic_jazz_piano` and `topic_classical_piano` remain established genre/instrument subject labels; when the source reasons separately about instrument and genre, use a decomposed TERM rather than pretending the label expresses that relationship. Named works/products remain exact referents. `topic_greatest_cricketer_of_all_time` leaves the criterion of greatness unresolved; it does not identify a winner or select an unstated metric.<br><br>`constraint_budget_limited` preserves a qualitative restriction without inventing a monetary ceiling. `constraint_17_plus` remains Needs clarification: the source conflates numeric age threshold and unspecified mature-rating systems. Use a numeric age requirement only if the source actually specifies it; do not convert every mature rating to age 17.<br><br>`event_*` constructors describe narrative content. Their result is TERM, never EVENT. `char_*` constructors describe a character, not an asserted real-world person. `chg_*` describes an intended change; `assert_*` describes an expected test condition, not test success. |
| rule_examples_general | rule | These are complete documents, not incomplete fragments. They use the supplemental entries in Section 8. The examples have been reviewed for the documented contracts; no implemented BrainCode parser has verified them. |
| rule_operations_general | rule | All listed source operations are retained. Operation symbols are callable vocabulary, not arbitrary argument values. Their natural-language aliases appear in the inventory. Parameter types include category checks; a name accepted by one category is not automatically accepted by another.<br><br>Every result-producing operation binds its result in REQUEST mode. All external operations may fail; failure does not create the declared successful result. Runtime failure handling is outside this glossary. TRACE represents attempts/failures without manufacturing successful runtime values.<br><br><br><br>These explicit signatures are proposed migration decisions where the source had only a gloss; they are not claims that an existing runtime adapter supports them. Additional attributes require a reviewed operation profile. No `custom_general_<predicate>` operation is automatically legal. |
| rule_review_points | rule | - `cap_gb` and `cap_tb`: retain source wording for audit; resolve decimal versus binary scale before acceptance.<br><br>- `constraint_17_plus`: resolve exact age threshold versus rating system before acceptance.<br><br>- `dom_sgi`: the source names an acronym without resolving its referent. Preserve it, but flag semantically dependent translations until context/review resolves it. No expansion of the acronym is invented here.<br><br>- Bare money symbols, locale aliases, warm/hot, and ranking phrases are contextual aliases. Matching a token alone is not enough to normalize meaning.<br><br>- The source's “all previously listed members remain valid” wording is replaced by the explicit inventory here. Unavailable historical entries are not guessed.<br><br>- Source examples using missing symbols or silently losing constraints are replaced by the complete examples above. This file does not preserve those defects as normative demonstrations.<br><br>- The revised specification's own illustrative trace/claim profiles remain examples, not a claim that this migration covers every possible reasoning construct.<br><br>This is a migrated seed, not a production-certified release. Structural and inventory checks do not replace a parser or semantic evaluation. Publishing requires resolution of entries marked Needs clarification and review of the proposed signatures/composite expansions.<br><br>- Resolved 2026-10-04 (human decision): `cap_gb`, `cap_tb`, `constraint_17_plus` and `dom_sgi` keep their current definitions and are no longer marked Needs clarification. |
| rule_search_web_attributes | rule | `search_web` optional attributes: `availability`, `category`, `color`, `cuisine`, `currency`, `gender`, `genre`, `location`, `platform`, `ram_unit`, `reservation_availability`, `shape`, `size`, `rank` is **not** accepted; ranking belongs to sort. Numeric filters: `max_price`, `min_ram`, `min_rating`; `trending` is BOOL. All other listed filters are STRING with matching categories. Price requires currency and RAM requires a capacity unit. No unstated default scale or source is inferred.<br><br>Search ranking uses only rank_* for rank_field and dir_* for rank_direction, not any arbitrary search-value member. Product category/genre/availability similarly accept only their own subfamilies. |
| rule_supplemental_general | rule | These entries were used in old examples or are needed by the migrated examples; they are explicitly declared here rather than assumed to exist.<br><br>Supplementary aliases are empty unless explicitly stated. The same static restrictions and RECORD signature conversion as Section 3 apply. No broader domain expansion is intended. |
| rule_support_primitives_general | rule | Each entry below is a proposed primitive constructor returning TERM, with stable ID `v19/support/<name>`. Literals in expansions are exact identifiers or atomic values, not hidden sentences. Optional arguments are absent unless supported. All constructors are pure descriptions and assert no occurrence or truth. The positive application is the expansion table in Section 5; the contrast column identifies an excluded interpretation.<br><br>Counts and indices are nonnegative integers, with preserve index at least 1. Amounts are nonnegative. `minimum_per_period.class` uses semantic-category-value; period and temporal duration units use the temporal subset of duration-unit-value. `activity` verbs are atomic identifiers with their ordinary role-specific meaning as specified in each composite expansion; this primitive is for described content, not a route to automatic executable custom operations. A new ambiguous verb requires its own reviewed definition. |

## Operations

| symbol | kind | signature | definition | not | aliases | expansion | status |
|---|---|---|---|---|---|---|---|
| press_key | operation | (target: REF[STRING], key: STRING) -> void | Press a specific keyboard key on the designated UI element. target must identify an interactive web element. | type_text (which enters text character strings into an input field) | press_enter, send_keys, key_press, hit_key |  | Accepted |
| add_to_cart | operation | (target: LIST[REF[STRING]]) -> void | Add the explicitly selected items. Does not pay or place an order. |  |  |  | Adapted |
| apply_filters | operation | (target: REF[STRING], criteria: LIST[TERM]) -> void | Apply the listed filters to an existing UI. Not repeated evidence of a search already represented. |  |  |  | Adapted |
| check_reservation_availability | operation | (target: STRING, cuisine?: STRING, currency?: STRING, location?: STRING, max_price?: NUMBER) -> BOOL | Check current availability under supplied filters. A positive result does not make a reservation. |  | check reservation availability |  | Adapted |
| chill | operation | (target: REF[STRING], destination: STRING) -> REF[STRING] | Chill using the stated resource; same identity. |  |  |  | Adapted |
| click | operation | (target: REF[STRING]) -> void | Activate the selected UI element. Requires its identity, not an invented selector. |  |  |  | Adapted |
| close | operation | (target: REF[STRING] / TERM) -> void | Close an articulated receptacle or appliance door. target must be a closable entity. |  | close_receptacle, close_door |  | Accepted |
| drop | operation | (target: REF[STRING] / TERM) -> void | Drop or release the held target object from the agent's hand. | place (which requires a destination receptacle) | drop, let go, put down |  | Accepted |
| extract | operation | (target: LIST[REF[STRING]], limit: NUMBER) -> LIST[REF[STRING]] | First limit results, preserving order and identity; limit is a nonnegative integer; limit=1 is still a list |  |  |  | Retained |
| face | operation | (target: STRING / TERM) -> void | Orient agent body/camera directly toward a target entity. target must be a perceptible entity. |  | orient_towards |  | Accepted |
| heat | operation | (target: REF[STRING], destination: STRING) -> REF[STRING] | Heat using the stated resource; same identity. Selecting a warm object does not imply heating it. |  |  |  | Adapted |
| hover | operation | (target: REF[STRING]) -> void | Move pointer cursor over an interactive web element without clicking. target must resolve to a valid element reference. |  | mouse_over |  | Accepted |
| look | operation | (direction: STRING) -> void | Tilt or adjust agent visual camera gaze. direction is up, down, or straight. |  | tilt_camera |  | Accepted |
| modify_code | operation | (target: STRING, file: STRING, revision: TERM, method?: STRING) -> void | Apply the structured change to the indicated code. A method name alone does not specify the change. |  | fix, reduce, optimize |  | Adapted |
| open | operation | (target: REF[STRING] / TERM) -> void | Open an articulated receptacle or appliance door. target must be an openable entity. |  | open_receptacle, open_door |  | Accepted |
| open_page | operation | (target: STRING) -> REF[STRING] | Navigate to the specified URL/page identity and return its page reference. Not a search for an unspecified page. |  | go to |  | Adapted |
| pick_up | operation | (target: STRING, quantity?: NUMBER, source?: STRING, color?: STRING, shape?: STRING, state?: STRING) -> REF[STRING] or LIST[REF[STRING]] | Select/acquire objects. Missing quantity or literal 1 returns REF; integer literal greater than 1 returns LIST[REF]. Other values are invalid for this profile. |  | grab, take, retrieve |  | Adapted |
| place | operation | (target: REF[STRING], destination: STRING, location?: STRING, relation?: STRING) -> void | Place an already acquired object. Spatial relation must be explicit if the source distinguishes it. |  | put, insert |  | Adapted |
| pour | operation | (target: REF[STRING], destination: STRING) -> REF[STRING] | Transfer selected liquid to the destination, preserving tracked material identity. |  |  |  | Adapted |
| remove | operation | (target: REF[STRING] / TERM, source?: STRING / TERM) -> void | Remove an object from an enclosure or container. target must be an object inside source. |  | take_out |  | Accepted |
| rinse | operation | (target: REF[STRING], destination: STRING) -> REF[STRING] | Rinse using the stated resource; return the same identity. It is not enough that the object is already clean. |  | wash |  | Adapted |
| run_tests | operation | (target: STRING, assertion?: TERM) -> BOOL | Run the selected project's tests, optionally checking the specified assertion. TRUE means the declared test condition passed, not overall software correctness. |  |  |  | Adapted |
| search_transit | operation | (target: STRING, constraints?: LIST[TERM], location?: STRING) -> LIST[REF[STRING]] | Query transit options. Does not buy tickets. |  |  |  | Adapted |
| search_travel | operation | (target: STRING, constraints?: LIST[TERM], location?: STRING) -> LIST[REF[STRING]] | Query travel options meeting supplied constraints. Does not book them. |  |  |  | Adapted |
| search_web | operation | (target: STRING, ...search attributes below) -> LIST[REF[STRING]] | Query a catalog/web source. Criteria filter the result; rank separately when requested. |  | find, look for |  | Adapted |
| select_filter | operation | (target: REF[STRING], criterion: TERM) -> void | Apply one specified filter in an existing UI. Do not add this operation when the source only requests filtered search. |  |  |  | Adapted |
| select_option | operation | (target: REF[STRING], value: STRING) -> void | Select an option from a dropdown or select menu element. target must be a select element. |  | choose_option, choose_dropdown, pick_option |  | Accepted |
| send_email | operation | (recipient: STRING, content: STRING, tone?: STRING) -> void | Send supplied exact message content to the identified recipient. A requested message purpose is not already a composed message. |  | email |  | Adapted |
| send_message | operation | (recipient: STRING, content: STRING, tone?: STRING) -> void | Send supplied exact content through the specified message context. If the channel is unresolved, report it. |  | text |  | Adapted |
| slice | operation | (target: REF[STRING] / TERM) -> REF[STRING] | Slice the selected material or described term, preserving its tracked aggregate identity. |  | chop, cut |  | Adapted |
| sort | operation | (target: LIST[REF[STRING]], rank_direction: STRING, rank_field: STRING) -> LIST[REF[STRING]] | Request ordering of selected results. Preserve member identity; this is not a claim that order was observed. |  | rank, order by |  | Adapted |
| stand_up | operation | () -> void | Return agent posture to standard upright standing position. agent must be in a non-standing posture. |  | stand |  | Accepted |
| turn | operation | (direction: STRING) -> void | Rotate agent body/view orientation. direction is typically left, right, or angle. |  | rotate, turn_around |  | Accepted |
| turn_on | operation | (target: REF[STRING] / TERM) -> void | Activate or start an appliance or device. target must be an activatable device. |  | activate, activate_appliance, switch_on |  | Accepted |
| type_text | operation | (target: REF[STRING], text: STRING) -> void | Type text into a designated input field, text box, or editable area. target must identify an editable element. |  | enter_text, input_text, input_string |  | Accepted |
| wait | operation | (duration?: NUMBER) -> void | Pause execution for a duration or cycle. duration in seconds or ticks. |  | idle, pause |  | Accepted |
| walk | operation | (destination: STRING / TERM, relation?: STRING) -> void | Locomote towards a target destination or landmark. destination must identify a valid entity or location. |  | move_to, go_to, navigate_to |  | Accepted |
| walk_backward | operation | (modifier?: STRING) -> void | Walk backward. Optional modifier can specify the degree or minor distance of movement. | walk (which moves forward toward a destination) | move backward, step back |  | Accepted |

## Speech acts

| symbol | kind | signature | definition | not | aliases | expansion | status |
|---|---|---|---|---|---|---|---|
| apologize | speech_act | UTTER apologize(target?: CLAIM / TERM) | Speech act expressing apology or regret for an outcome or target. | decline (which is refusing) | apologize, apology, sorry |  | Accepted |
| acknowledge | speech_act | UTTER acknowledge(target: CLAIM / TERM) | Acknowledge receipt/awareness; does not imply agreement. |  |  |  | Adapted |
| ask | speech_act | UTTER ask(target: TERM, or a sufficiently precise topic: STRING / TERM) | Request information/advice; not an assertion of an answer. |  | ask, how should |  | Adapted |
| confirm | speech_act | UTTER confirm(target: CLAIM) | Confirm the proposition; its evidence/status remains explicit. |  |  |  | Adapted |
| correct | speech_act | UTTER correct(target: CLAIM) | Offer corrected content. Actual supersession requires the Conversation revision rules. |  |  |  | Adapted |
| decline | speech_act | UTTER decline(target: TERM) | Decline the represented request/proposal; not negate every proposition within it. |  |  |  | Adapted |
| express_interest | speech_act | UTTER express_interest(target: STRING / TERM) | Speech act expressing conversational interest or engagement in a topic. speech act in dialogic traces. |  | show_interest |  | Accepted |
| inform | speech_act | UTTER inform(target: CLAIM) | Present the proposition; preserve its holder/status. |  |  |  | Adapted |
| offer | speech_act | UTTER offer(target: STRING / TERM) | Speech act offering assistance, service, or items to a conversation partner. speech act in dialogic traces. |  | proffer |  | Accepted |
| propose | speech_act | UTTER propose(target: TERM) | Suggest an action/idea; does not record it as performed. |  |  |  | Adapted |
| respond | speech_act | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. |  | answer |  | Adapted |

## Constructors

| symbol | kind | signature | definition | not | aliases | expansion | status |
|---|---|---|---|---|---|---|---|
| activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM, location?: STRING, instrument?: STRING, purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | Does not execute or assert it |  |  | Retained |
| aesthetic | constructor | TERM aesthetic(period: STRING, style: STRING) -> TERM | A stylistic description with an explicit period | Not a character's age or production date |  |  | Retained |
| at_least | constructor | TERM at_least(measure: TERM) -> TERM | A lower bound: the constrained value is greater than or equal to the given measure (or number term). Use inside requirement(value=...). | an exact value; a strict 'more than' only when the source says so explicitly | at least, minimum, or more, no less than, plus |  | Accepted |
| at_most | constructor | TERM at_most(measure: TERM) -> TERM | An upper bound: the constrained value is less than or equal to the given measure (or number term). Use inside requirement(value=...). | an exact value or a target to aim for | at most, maximum, up to, no more than, under |  | Accepted |
| calculation | constructor | TERM calculation(inputs: LIST[TERM], operation: STRING, result?: TERM) -> TERM | Constructs a descriptive representation of an arithmetic or algorithmic calculation step with inputs, operation identifier, and optional resulting value. | an executed runtime action or factual claim of outcome | math_operation, compute_step |  | Accepted |
| captioned_figure | constructor | TERM captioned_figure(caption: STRING, label: STRING, content?: TERM) -> TERM | Constructs a descriptor for a captioned figure, photo, or visual diagram within a structured document. | an executed visual observation or UI image asset | figure, image_caption, photograph, captioned_image |  | Accepted |
| change_property | constructor | TERM change_property(property: STRING, source: STRING, target: STRING) -> TERM | Require target to inherit the property value from source | Not an arbitrary code patch |  |  | Retained |
| character | constructor | TERM character(name: STRING, series?: STRING) -> TERM | Constructs a descriptive representation of a fictional or narrative character. name specifies the character identifier. |  | fictional_character |  | Accepted |
| character_trait | constructor | TERM character_trait(property: STRING, value: STRING / NUMBER) -> TERM | A character attribute | Not a claim about a real person |  |  | Retained |
| chg_modify_code | constructor | TERM chg_modify_code(target: STRING, file: STRING / TERM, revision: TERM) -> TERM | Constructs a structured change specification describing code file modifications. software engineering revision term. |  | modify_source_code |  | Accepted |
| cli_command | constructor | TERM cli_command(executable: STRING, args?: LIST[STRING] / LIST[TERM]) -> TERM | Constructs a structured representation of a command-line invocation with executable and optional arguments or flags. | an executed external action or process run (pure description) | command_line, shell_command, cli_invocation |  | Accepted |
| code_entity | constructor | TERM code_entity(file?: STRING / TERM, kind: STRING, name: STRING, project?: STRING) -> TERM | Constructs a structured descriptor for a source code entity such as a function, method, class, module, or source file within a project. | an executed runtime call or file system operation | code_function, source_file, code_symbol |  | Accepted |
| compression | constructor | TERM compression(target?: STRING / TERM, algorithm: STRING, format?: STRING) -> TERM | Constructs a descriptive representation of a data or package compression configuration specifying optional target platform or file, compression algorithm, and optional format. | an executed archive extraction/compression action or document layout format | compression_algorithm, compress_with, compression_format |  | Accepted |
| conditional | constructor | TERM conditional(condition: TERM, consequence: TERM) -> TERM | Constructs a structured conditional proposition term connecting a condition and consequence. descriptive logic structure. |  | if_then |  | Accepted |
| config_overlay | constructor | TERM config_overlay(files: LIST[STRING] / LIST[TERM], reverse_order?: BOOL) -> TERM | Constructs a specification of configuration file overlay precedence and ordering across multiple configuration files. | a general list sorting operation or spatial layering | overlay_config, config_precedence, overlay_order |  | Accepted |
| config_setting | constructor | TERM config_setting(option: STRING, section: STRING, value: STRING / NUMBER / BOOL / TERM) -> TERM | Constructs a structured representation of a configuration key-value setting within an identified section. | an active runtime configuration state or environment setting | ini_setting, config_option, configuration_setting |  | Accepted |
| conjunction | constructor | TERM conjunction(items: LIST[TERM]) -> TERM | All described components apply | Does not imply temporal order |  |  | Retained |
| decision | constructor | TERM decision(activity: TERM) -> TERM | A decision whose content is the described activity | Not proof it was carried out |  |  | Retained |
| dialogue | constructor | TERM dialogue(style: STRING) -> TERM | Constructs a description of conversational dialogue adhering to a style. descriptive conversational term. |  | conversation_style |  | Accepted |
| document_section | constructor | TERM document_section(title: STRING, items?: LIST[TERM]) -> TERM | Constructs a structural document section descriptor with a section title and optional content items. | a complete document artifact class (use art_structured_report) | section, report_section, article_section |  | Accepted |
| duration | constructor | TERM duration(amount: NUMBER, unit: STRING) -> TERM | Requested elapsed/calendar extent | Word/item counts are not time |  |  | Retained |
| emits_light | constructor | TERM emits_light(source: STRING / TERM) -> TERM | Constructs a description of intrinsic light emission generated by an entity or light source. | reflected light (use reflects_light) or an electric appliance (use lamp) | emits light, generates light, gives off light |  | Accepted |
| exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | Not a claim of observed absence |  |  | Retained |
| footnote | constructor | TERM footnote(function: STRING, number: NUMBER) -> TERM | Constructs a footnote reference or citation marker descriptor. document formatting descriptor. |  | citation_note |  | Accepted |
| greeting | constructor | TERM greeting(recipient: STRING) -> TERM | Constructs a conversational salutation greeting descriptor. conversational discourse term. |  | salutation |  | Accepted |
| group_size | constructor | TERM group_size(count: NUMBER, group?: STRING / TERM) -> TERM | The headcount or number of members in a specified group or party; count is a nonnegative integer. | minimum_per_period (a per-period minimum bound) or measure (measured quantities with units) | party_size, party of, number of guests, guest_count |  | Accepted |
| historical_event | constructor | TERM historical_event(name: STRING, location?: STRING / TERM, period?: STRING / NUMBER) -> TERM | Constructs a descriptive representation of a historical event, conflict, or epoch. | an executed runtime event (EVENT) or past occurrence claim (use occurred) | historic_event, historical_conflict, war_event |  | Accepted |
| illuminates | constructor | TERM illuminates(target: STRING / TERM, source: STRING / TERM) -> TERM | Constructs a description of directional illumination where a light source casts light onto a target body. | an ambient color state or reflection (use reflects_light) | illuminates, shines on, shining towards |  | Accepted |
| include | constructor | TERM include(item: STRING / TERM) -> TERM | Require the identified content/item | Not permission to invent an instance in a recorded trace |  |  | Retained |
| issue | constructor | TERM issue(project: STRING, number: NUMBER) -> TERM | Constructs an issue tracker ticket reference. issue tracker descriptor. |  | issue_ticket, bug_report |  | Accepted |
| location_spec | constructor | TERM location_spec(address?: STRING, area?: STRING, city?: STRING, state?: STRING) -> TERM | Constructs a structured geographical location specification with regional and administrative qualifiers. | a fixed atomic location descriptor in location-name or a spatial relation | location_details, geographic_location |  | Accepted |
| maximum_between_stops | constructor | TERM maximum_between_stops(activity: STRING, amount: NUMBER, unit: STRING) -> TERM | Upper bound on the stated activity between successive stops | Not a limit on total daily duration |  |  | Retained |
| measure | constructor | TERM measure(amount: NUMBER, unit: STRING) -> TERM | A measured amount: a number with its unit symbol (a unit-category value such as unit_minute, cap_gb or curr_usd). Describes the amount only; asserts nothing. | a symbol with the number baked in (char_age_18, size_16gb); a unitless count (use the quantity argument) | amount of, size of, measured in |  | Accepted |
| medical_condition | constructor | TERM medical_condition(condition: STRING, patient: STRING / TERM, severity?: STRING) -> TERM | Constructs a descriptive representation of a medical condition, pathology, or symptom profile. | an asserted factual attribution (use attribute_claim) or executed treatment | condition, symptom, pathology, diagnosis |  | Accepted |
| minimum_per_period | constructor | TERM minimum_per_period(class: STRING, count: NUMBER, period: STRING) -> TERM | At least count members of class in each period | Not a minimum total over the whole artifact |  |  | Retained |
| naming_pattern | constructor | TERM naming_pattern(description: STRING, context?: STRING) -> TERM | Constructs a descriptive naming or morphological pattern. used for rule-based or conventional naming schemes. |  | pattern_naming |  | Accepted |
| negation | constructor | TERM negation(target: TERM) -> TERM | Constructs a descriptive semantic negation of a target descriptive proposition or condition term. | Check's runtime Boolean operator NOT or a speech-act decline | not, does not, negation, absence of |  | Accepted |
| obligation | constructor | TERM obligation(actor: STRING / TERM, activity: TERM) -> TERM | Constructs a deontic obligation description requiring an actor to perform an activity. actor and activity specified. |  | duty, mandatory_activity |  | Accepted |
| offer_help | constructor | TERM offer_help() -> TERM | Constructs a conversational proffer of assistance or support. conversational discourse term. |  | help_offer |  | Accepted |
| outshines | constructor | TERM outshines(brighter: STRING / TERM, dimmer: STRING / TERM) -> TERM | Constructs a description of relative visual brightness where a brighter light source overpowers the perceived brightness of a dimmer object. | an absolute numeric brightness measurement | outshines, overpowers brightness, drowns out light |  | Accepted |
| policy_document | constructor | TERM policy_document(title: STRING, audience?: STRING, constraints?: LIST[TERM]) -> TERM | Constructs a structured policy document representation. used for formal organizational guidelines. |  | policy_spec |  | Accepted |
| policy_revision_request | constructor | TERM policy_revision_request(original_policy: CLAIM / TERM, inclusions: LIST[TERM]) -> TERM | Constructs a request to revise an existing policy with additional clauses. descriptive revision term. |  | policy_amendment |  | Accepted |
| preserve | constructor | TERM preserve(component: STRING, index: NUMBER) -> TERM | Keep the indexed component unchanged, using one-based indexing | Not preserve all components |  |  | Retained |
| property_question | constructor | TERM property_question(property: STRING, subject: STRING / TERM) -> TERM | An open request for a property of a subject | Does not supply the property's value |  |  | Retained |
| pull_request | constructor | TERM pull_request(project: STRING, number: NUMBER) -> TERM | Constructs a repository pull request reference. software repository reference. |  | pr |  | Accepted |
| rate | constructor | TERM rate(denominator: TERM, numerator: TERM) -> TERM | Constructs a structured proportional rate or frequency relating a numerator measured quantity to a denominator reference quantity. | an asserted factual attribution (use attribute_claim) or bound constraint (use requirement) | per_unit, ratio |  | Accepted |
| reconcile_code | constructor | TERM reconcile_code(entities: LIST[TERM], objective: STRING / TERM) -> TERM | Constructs a specification to reconcile multiple code entities or implementations to standardize their behavior. | a general file merge operation | reconcile_functions, standardize_behavior, reconcile_implementations |  | Accepted |
| reflects_light | constructor | TERM reflects_light(target: STRING / TERM, source: STRING / TERM) -> TERM | Constructs a description of an optical reflection where a target surface or body reflects light emanating from a light source. | intrinsic light emission (use emits_light) | reflects, reflection of light, reflects sunlight |  | Accepted |
| regression_case | constructor | TERM regression_case(framework: STRING, modifier: STRING, relation: STRING) -> TERM | A regression scenario specifying affected framework, condition and relation | Does not invent a passing test or exact implementation |  |  | Retained |
| remove_literal | constructor | TERM remove_literal(text: STRING) -> TERM | Remove occurrences of that exact literal in the stated artifact | Not remove similar markup unless specified |  |  | Retained |
| rental_vehicle | constructor | TERM rental_vehicle(category: STRING, model?: STRING) -> TERM | Constructs a descriptive representation of a rental vehicle or vehicle category. | an acquired physical vehicle reference or employee vehicle policy (use vehicle_allowance) | rental_car, hire_car, mystery_car |  | Accepted |
| requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | Does not assert an existing artifact already satisfies it | constraint, property_requirement, structured_requirement |  | Retained |
| sequence | constructor | TERM sequence(items: LIST[TERM]) -> TERM | Ordered described activities/content | Not unordered conjunction |  |  | Retained |
| similarity | constructor | TERM similarity(target: STRING / TERM, dimension?: STRING / TERM) -> TERM | Constructs a descriptor representing comparative closeness or similarity to a target along a given dimension. | spatial proximity (use rank_distance or next_to) or an assertion of exact identity (use identity) | closest_to, similar_to, resembles |  | Accepted |
| software_version | constructor | TERM software_version(branch?: STRING, project: STRING, version?: STRING) -> TERM | Constructs a descriptor for a software project version, release tag, or branch identifier. | an installed runtime package environment | repo_branch, git_branch, project_version |  | Accepted |
| spatial_constraint | constructor | TERM spatial_constraint(relation: STRING, object: TERM, reference: TERM) -> TERM | Constructs a descriptive spatial constraint between an object and a reference landmark. relation must specify a spatial configuration. |  | spatial_relation |  | Accepted |
| subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM, location?: STRING, time?: STRING) -> TERM | Subject matter with explicit qualifiers | Does not make a factual claim about it |  |  | Retained |
| test_condition | constructor | TERM test_condition(condition: STRING, expected: BOOL) -> TERM | A testable condition with the expected Boolean outcome | Expected outcome is not an observed result |  |  | Retained |
| time_point | constructor | TERM time_point(date?: STRING, time?: STRING, timezone?: STRING) -> TERM | Constructs a structured representation of a specific calendar date, time of day, or scheduled timestamp. | an elapsed time duration (use duration) | timestamp, datetime, scheduled_time |  | Accepted |
| training_program | constructor | TERM training_program(topic: STRING / TERM, audience: STRING / TERM) -> TERM | Constructs a description of an educational or compliance training program. used for instructional policy requirements. |  | training_course |  | Accepted |
| vehicle_allowance | constructor | TERM vehicle_allowance(roles: STRING, types: LIST[STRING]) -> TERM | Constructs a specification of permitted vehicle types for defined employee roles. specifies vehicle permissions. |  | vehicle_permission |  | Accepted |
| visual_contrast | constructor | TERM visual_contrast(background: STRING / TERM, foreground: STRING / TERM) -> TERM | Constructs a descriptive term representing the optical contrast between a foreground object and its surrounding background environment. | a rhetorical claim link (use LINK contrast) | visual contrast, contrast against, contrast with background |  | Accepted |
| web_element | constructor | TERM web_element(label: STRING, tag?: STRING) -> TERM | Constructs a descriptive representation of a web UI element by visible text label and optional tag. used to identify interactive DOM nodes. |  | ui_element, dom_element |  | Accepted |
| word_blend | constructor | TERM word_blend(base: STRING / TERM, replacement: STRING / TERM, result_name?: STRING) -> TERM | Constructs a morphological blend or portmanteau from base and replacement terms. descriptive lexical structure. |  | portmanteau |  | Accepted |

## Claim relations and links

| symbol | kind | signature | definition | not | aliases | expansion | status |
|---|---|---|---|---|---|---|---|
| failure | claim_relation | CLAIM failure(system: STRING) | The indicated system is failing in context; hypothesis status does not establish truth |  |  |  | Retained |
| outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec |  |  |  | Retained |
| rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis |  |  |  | Retained |
| revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content |  |  |  | Retained |
| supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment |  |  |  | Retained |
| allowed_to_enter | claim_relation | CLAIM allowed_to_enter(subject: STRING / TERM, location: STRING / TERM, condition?: STRING / TERM) | Asserts that a subject is permitted access to a location or facility. permission claim. |  | permitted_in |  | Accepted |
| argues_for | claim_relation | CLAIM argues_for(subject: STRING / TERM, value: STRING / TERM) | Asserts that an actor advocates for or defends a stance, value, or principle. advocacy claim. |  | advocates_for |  | Accepted |
| associated_with | claim_relation | CLAIM associated_with(subject: STRING / TERM, concept: STRING / TERM) | Asserts a cultural, semantic, or historical association between a subject and concept. association claim. |  | linked_to, correlated_with |  | Accepted |
| attitude | claim_relation | CLAIM attitude(holder: STRING / TERM, type: STRING, target: CLAIM / TERM) | Asserts an affective or cognitive attitude held by a party toward a target. attitudinal stance. |  | sentiment |  | Accepted |
| attribute_claim | claim_relation | CLAIM attribute_claim(subject: STRING / TERM, property: STRING, value: STRING / NUMBER / BOOL / TERM) | Asserts that a subject possesses a named property evaluated to a specific primitive or structured value. general property attribution claim. |  | property_value, word_property, has_property, property attribution |  | Accepted |
| causes | claim_relation | CLAIM causes(cause: CLAIM / TERM, effect: CLAIM) | Asserts a direct causal relationship producing an effect proposition. causal assertion. |  | produces |  | Accepted |
| comfortable | claim_relation | CLAIM comfortable(person: TERM, value: BOOL) | Asserts whether a person or animal is comfortable in a situation. affective/state claim. |  | is_comfortable |  | Accepted |
| considered | claim_relation | CLAIM considered(subject: TERM) | Asserts that an agent or speaker evaluated or entertained a specific candidate term or concept. subject is the evaluated term. |  | evaluated, weighed |  | Accepted |
| constrained_by | claim_relation | CLAIM constrained_by(activity: TERM, constraint: TERM) | Asserts that an activity or operation is governed or restricted by a constraint. governance/constraint claim. |  | restricted_by |  | Accepted |
| contrast | link | LINK contrast(first: CLAIM, second: CLAIM) | Expresses rhetorical qualification, opposition, or contrast between two claims. link between claims. |  | qualification, however |  | Accepted |
| controversial | claim_relation | CLAIM controversial(subject: STRING / TERM) | Asserts that a topic, policy, or practice is the subject of public debate or controversy. evaluative debate claim. |  | debated, disputed |  | Accepted |
| created_by | claim_relation | CLAIM created_by(subject: STRING / TERM, creator: STRING) | Asserts the developer, author, or creator of an entity or system. provenance/creator assertion. |  | authored_by |  | Accepted |
| designed_to_be | claim_relation | CLAIM designed_to_be(subject: STRING / TERM, quality: STRING) | Asserts the intended design goal, alignment quality, or persona attribute of a system. design objective. |  | intended_to_be |  | Accepted |
| duplicate_definition | claim_relation | CLAIM duplicate_definition(count: NUMBER, entity: TERM, location?: STRING / TERM) | Asserts that multiple duplicate copies or definitions of a code entity exist within a codebase or location. | an exact string equality check | duplicate_code, two_copies, duplicate_function |  | Accepted |
| enables | claim_relation | CLAIM enables(condition: TERM / CLAIM, outcome: TERM / CLAIM) | Asserts that an enabling condition or capability facilitates an outcome. enabling condition. |  | facilitates, allows |  | Accepted |
| escalation | claim_relation | CLAIM escalation(cause: CLAIM, conflict: TERM) | Asserts an escalation in intensity or scale of a conflict triggered by an event. conflict dynamics. |  | conflict_escalation |  | Accepted |
| example_of | claim_relation | CLAIM example_of(example: TERM, concept: TERM) | Asserts that an instance or term exemplifies a general concept, pattern, or category. example and concept are descriptive terms. |  | exemplifies, instance_of |  | Accepted |
| exempt_from | claim_relation | CLAIM exempt_from(subject: STRING / TERM, rule: CLAIM / TERM) | Asserts that a subject is granted exemption from a designated rule or prohibition. exemption claim. |  | excepted_from |  | Accepted |
| exists_in | claim_relation | CLAIM exists_in(subject: STRING / TERM, location: STRING / TERM) | Asserts that an entity, policy, or phenomenon exists within a geographical or conceptual location. spatial/locational existence. |  | present_in |  | Accepted |
| focus_of | claim_relation | CLAIM focus_of(subject: TERM, concept: STRING) | Asserts that a subject term emphasizes or focuses on a given thematic concept. subject is a descriptive term. |  | centered_on |  | Accepted |
| has_attribute | claim_relation | CLAIM has_attribute(subject: STRING / TERM, attribute: STRING / TERM) | Asserts that an entity, group, or person possesses a stated characteristic or attribute. general characteristic attribution. |  | possesses_attribute |  | Accepted |
| has_goal | claim_relation | CLAIM has_goal(subject: STRING / TERM, goal: TERM) | Asserts that an entity or agent pursues a stated goal or objective. teleological claim. |  | pursues_goal |  | Accepted |
| has_state | claim_relation | CLAIM has_state(subject: TERM, state: STRING) | Asserts that an entity is currently in a physical, thermal, or operational state. state must be a valid state descriptor string. |  | in_state, state_is |  | Accepted |
| has_style | claim_relation | CLAIM has_style(target: CLAIM / EVENT / TERM, value: TERM / STRING) | Asserts that an artifact, utterance, or action possesses a designated style. style qualifier. |  | style_is |  | Accepted |
| identity | claim_relation | CLAIM identity(subject: STRING / TERM, name: STRING) | Asserts the identified name or persona of an agent or entity. identity assertion. |  | agent_name |  | Accepted |
| important | claim_relation | CLAIM important(target: TERM) | Asserts that a concept, activity, or condition is important or significant. evaluative importance claim. |  | significant |  | Accepted |
| involves | claim_relation | CLAIM involves(subject: CLAIM, target: TERM) | Asserts participant involvement or inclusion of an entity in an initiative or event. involvement claim. |  | includes_participant |  | Accepted |
| leads_to | claim_relation | CLAIM leads_to(cause: TERM, effect: TERM) | Asserts a conceptual consequence or progression from cause to effect. progression relation. |  | results_in |  | Accepted |
| meets_needs | claim_relation | CLAIM meets_needs(subject: TERM, beneficiary: STRING / TERM) | Asserts that an item, activity, or plan satisfies the needs of a beneficiary. utility/satisfaction claim. |  | satisfies_needs |  | Accepted |
| menu_works | claim_relation | CLAIM menu_works(property: STRING) | Asserts that a menu or recipe plan satisfies an operational criterion. menu evaluation. |  | menu_satisfies |  | Accepted |
| motivated_by | claim_relation | CLAIM motivated_by(claim: CLAIM, motive: STRING / TERM) | Asserts that an action, rule, or claim is motivated by an underlying motive or goal. motive explanation. |  | rationale_is |  | Accepted |
| naming_convention | claim_relation | CLAIM naming_convention(pattern: TERM, context?: STRING) | Asserts that a naming pattern is a recognized convention within a given domain. pattern must be a naming_pattern or term. |  | is_naming_convention |  | Accepted |
| occurred | claim_relation | CLAIM occurred(activity: TERM) | Asserts that an event, action, or activity took place in the past. past occurrence claim. |  | happened |  | Accepted |
| occurred_recently | claim_relation | CLAIM occurred_recently(target: CLAIM) | Asserts temporal recency of an asserted occurrence or claim. temporal recency qualifier. |  | recently_happened |  | Accepted |
| ongoing | claim_relation | CLAIM ongoing(target: TERM) | Asserts that a conflict, process, or initiative is actively ongoing. temporal aspect claim. |  | in_progress |  | Accepted |
| opposes | claim_relation | CLAIM opposes(actor: STRING / TERM, subject: STRING / TERM) | Asserts that an actor opposes or objects to a practice, entity, or policy. opposition stance. |  | objects_to, against |  | Accepted |
| perceived_as | claim_relation | CLAIM perceived_as(subject: STRING / TERM, concept: STRING / TERM) | Asserts public perception attributing a quality, reputation, or image to a subject. perception attribution. |  | regarded_as |  | Accepted |
| possesses | claim_relation | CLAIM possesses(subject: STRING / TERM, item: TERM, value: BOOL) | Asserts whether a subject possesses or lacks a stated property, capability, or entity. possession assertion with boolean polarity. |  | holds_property |  | Accepted |
| prep_time | claim_relation | CLAIM prep_time(value: TERM) | Asserts an estimated preparation or assembly time duration. time requirement assertion. |  | preparation_duration |  | Accepted |
| prohibited | claim_relation | CLAIM prohibited(subject: STRING / TERM, location: STRING / TERM, condition?: STRING / TERM) | Asserts that a subject is prohibited from a location or activity under specified conditions. deontic prohibition claim. |  | forbidden, banned_from |  | Accepted |
| propose_menu | claim_relation | CLAIM propose_menu(menu: TERM) | Asserts the proposal of a comprehensive menu plan. planning proposal. |  | suggest_menu |  | Accepted |
| proposed_policy | claim_relation | CLAIM proposed_policy(policy: TERM, requirements: LIST[TERM]) | Asserts that a proposed policy framework comprises the specified requirement terms. policy must be a policy term. |  | policy_proposal |  | Accepted |
| provides | claim_relation | CLAIM provides(actor: STRING / TERM, subject: STRING / TERM) | Asserts that an establishment, organization, or provider supplies a specified item or service. provision claim. |  | supplies |  | Accepted |
| reason_for | claim_relation | CLAIM reason_for(subject: CLAIM / TERM, reason: STRING / TERM) | Asserts an explanatory reason for a policy, belief, or state of affairs. explanatory reason. |  | basis_for |  | Accepted |
| recommended | claim_relation | CLAIM recommended(target: TERM / CLAIM) | Asserts an advisory recommendation that an activity or measure is advisable. advisory normative claim. |  | advisable |  | Accepted |
| request | claim_relation | CLAIM request(target: TERM / STRING) | Represents an active communicative request or constraint state in conversation tracking. target is the requested action or topic. |  | user_request |  | Accepted |
| role | claim_relation | CLAIM role(subject: STRING / TERM, role_type: STRING) | Asserts the functional role or capacity of an agent or entity. role assertion. |  | agent_role |  | Accepted |
| spatial_state | claim_relation | CLAIM spatial_state(relation: STRING, object: TERM, reference: TERM) | Asserts an observed spatial configuration between an object and a reference landmark. relation must specify spatial configuration. |  | placed_at, located_at |  | Accepted |
| statement | claim_relation | CLAIM statement(fact: TERM) | Foundational claim relation converting any descriptive TERM into an attributed, truth-evaluated assertion. universal fact assertion. |  | assert_fact, fact_claim, claim_statement |  | Accepted |
| then | link | LINK then(previous: EVENT, next: EVENT) | Represents temporal sequence and succession between two events where next follows previous. previous and next must be event terms. |  | followed_by, after_which |  | Accepted |
| trained_for | claim_relation | CLAIM trained_for(subject: STRING / TERM, activity: TERM) | Asserts that an agent or model underwent training for a designated activity. training objective. |  | fine_tuned_for |  | Accepted |
| unaware | claim_relation | CLAIM unaware(person: STRING / TERM, topic: STRING / TERM) | Asserts epistemic lack of awareness regarding a topic, fact, or event. epistemic state. |  | ignorant_of |  | Accepted |
| user_practice | claim_relation | CLAIM user_practice(activity: TERM) | Asserts a habitual, workflow, or recurring practice of a user. workflow practice. |  | habitual_activity |  | Accepted |
| user_preference | claim_relation | CLAIM user_preference(constraints: TERM) | Asserts a user's stated preference constraints or dietary requirements. user constraint assertion. |  | stated_preference |  | Accepted |
| validates_parameter | claim_relation | CLAIM validates_parameter(condition: STRING, entity: TERM, parameter: STRING) | Asserts that a code entity inspects or validates parameter names or types for a specified condition. | a runtime assertion test | inspects_parameter, checks_parameter, validates_parameter_names |  | Accepted |
| varies_by_location | claim_relation | CLAIM varies_by_location(target: CLAIM / TERM) | Asserts that a policy, rule, or phenomenon differs across regional or geographic locations. regional variation claim. |  | varies_by_region, regional_variance, location_dependent |  | Accepted |
| varies_with | claim_relation | CLAIM varies_with(target: CLAIM / TERM, condition: STRING / TERM) | Asserts that a target claim or term varies contingently depending on specified conditions, external factors, or behavioral habits. | geographic variation only (use varies_by_location) | depends_on, contingent_on |  | Accepted |
| warning | claim_relation | CLAIM warning(message: STRING, target?: TERM) | Asserts a recorded library warning, deprecation notice, or advisory alert. system alert claim. |  | alert, deprecation_warning |  | Accepted |
| works_best | claim_relation | CLAIM works_best(style: STRING, count: NUMBER, purpose: STRING) | Asserts an advisory evaluation of optimal event style and participant capacity. planning evaluation. |  | optimal_format |  | Accepted |

## Composite definitions

| symbol | kind | signature | definition | not | aliases | expansion | status |
|---|---|---|---|---|---|---|---|
| topic_derogatory_language | composite | TERM topic_derogatory_language() -> TERM | A composite term representing the topic of derogatory language. | potential_harms (which is generic) | derogatory language | subject(kind="derogatory_language") | Accepted |
| char_2000s_anime_style | composite | TERM char_2000s_anime_style() -> TERM | 2000s anime style. |  |  | aesthetic(period="2000s", style="anime") | Composite |
| char_female | composite | TERM char_female() -> TERM | Female gender. |  | female | character_trait(property="gender", value="female") | Composite |
| assert_multinomial_scorer | composite | TERM assert_multinomial_scorer() -> TERM | Assertion that multinomial probabilistic scoring succeeds. |  |  | test_condition(condition="multinomial_probabilistic_scoring", expected=TRUE) | Composite |
| chg_inherit_multi_class | composite | TERM chg_inherit_multi_class(source: STRING, target: STRING) -> TERM | Change requiring a constructed estimator to inherit multi_class. |  |  | change_property(property="multi_class", source=$source, target=$target) | Composite |
| constraint_beginner | composite | TERM constraint_beginner() -> TERM | Targeted at beginners. |  |  | requirement(property="audience_expertise", value="beginner") | Composite |
| constraint_budget_limited | composite | TERM constraint_budget_limited() -> TERM | Limited budget. |  |  | requirement(property="budget_limited", value=TRUE) | Composite |
| constraint_comprehensive | composite | TERM constraint_comprehensive() -> TERM | Must be comprehensive. |  |  | requirement(property="comprehensive", value=TRUE) | Composite |
| constraint_exclude_flowery_language | composite | TERM constraint_exclude_flowery_language() -> TERM | Avoid flowery language. |  |  | exclude(item="flowery_language") | Composite |
| constraint_exclude_liberation_theme | composite | TERM constraint_exclude_liberation_theme() -> TERM | Avoid liberation theme. |  |  | exclude(item="liberation_theme") | Composite |
| constraint_include_character_attribute_list | composite | TERM constraint_include_character_attribute_list() -> TERM | Include character attributes. |  |  | include(item="character_attribute_list") | Composite |
| constraint_realistic | composite | TERM constraint_realistic() -> TERM | Must be realistic. |  |  | requirement(property="realistic", value=TRUE) | Composite |
| constraint_respectful | composite | TERM constraint_respectful() -> TERM | Must be respectful. |  |  | requirement(property="respectful", value=TRUE) | Composite |
| constraint_single_choice | composite | TERM constraint_single_choice() -> TERM | Must pick a single choice. |  |  | requirement(property="choice_count", value=1) | Composite |
| content_decision_study_sgi_japan | composite | TERM content_decision_study_sgi_japan(actor: STRING) -> TERM | A personal decision to travel to Japan to study SGI. |  |  | decision(activity=activity(verb="travel", actor=$actor, location=japan, purpose=activity(verb="study", actor=$actor, object=dom_sgi))) | Composite |
| content_kyoto_itinerary | composite | TERM content_kyoto_itinerary() -> TERM | A Kyoto itinerary subject. |  |  | subject(kind="itinerary", location="Kyoto") | Composite |
| content_mixed_case_foreign_key_regression | composite | TERM content_mixed_case_foreign_key_regression() -> TERM | A mixed-case Django app-name ForeignKey regression test purpose. |  |  | regression_case(framework=django, modifier=mod_mixed_case, relation="ForeignKey") | Composite |
| content_status_update | composite | TERM content_status_update(subject: STRING) -> TERM | A request for a status update. |  | status update | activity(verb="request_update", object=$subject) | Composite |
| event_camper_in_sludge_pit | composite | TERM event_camper_in_sludge_pit() -> TERM | Campers interacting in a sludge pit. |  |  | activity(verb="interact", actor="campers", location="sludge_pit") | Composite |
| event_sadie_adler_unmasking | composite | TERM event_sadie_adler_unmasking() -> TERM | Sadie Adler taking off her hat and peeling skin. |  |  | sequence(items=[activity(verb="remove", actor="Sadie Adler", object="hat"), activity(verb="peel", actor="Sadie Adler", object="skin")]) | Composite |
| topic_ai_earning_methods | composite | TERM topic_ai_earning_methods() -> TERM | AI earning methods. |  |  | subject(kind="methods", qualifier=activity(verb="earn", instrument="AI", object="income")) | Composite |
| topic_current_new_york_housing_market | composite | TERM topic_current_new_york_housing_market(as_of: STRING) -> TERM | Current New York housing market. |  |  | subject(kind="housing_market", location="New York", time=$as_of) | Composite |
| topic_greatest_cricketer_of_all_time | composite | TERM topic_greatest_cricketer_of_all_time() -> TERM | Greatest cricketer of all time. |  |  | subject(kind="cricketer", qualifier=requirement(property="rank_by_greatness", value=1), time="all_time") | Composite |
| topic_profanity | composite | TERM topic_profanity() -> TERM | A composite term representing the topic of profanity. | potential_harms (which is generic) | profanity | subject(kind="profanity") | Accepted |
| topic_school_work_routine | composite | TERM topic_school_work_routine() -> TERM | School and work routine. |  |  | subject(kind="routine", qualifier=conjunction(items=[subject(kind="school"), subject(kind="work")])) | Composite |
| transform_preserve_first_column | composite | TERM transform_preserve_first_column() -> TERM | Preserve the first column of a table. |  |  | preserve(component="column", index=1) | Composite |
| transform_remove_br | composite | TERM transform_remove_br() -> TERM | Remove <br /> tags. |  |  | remove_literal(text="<br />") | Composite |

## Values by category

### artifact-value

| symbol | kind | category | definition | not | aliases | status |
|---|---|---|---|---|---|---|
| rule_category_artifact_value | category_rule | artifact-value | STRING artifact class for GENERATE.target. art_story says what kind of artifact to produce, not what occurs in its plot. |  |  | Retained |
| art_character_profile | value | artifact-value | Descriptive character profile. |  |  | Retained |
| art_invitation | value | artifact-value | An invitation card, announcement, or digital invite artifact for an event. | art_plan (an actionable procedure or schedule) or art_short_text (unstructured short text) | invitation, invitation card, invite, digital invitation, printable invitation | Accepted |
| art_itinerary | value | artifact-value | An ordered travel plan; GENERATE returns STRING, not booked travel |  |  | Retained |
| art_plan | value | artifact-value | Actionable plan. |  |  | Retained |
| art_short_text | value | artifact-value | Short free text. |  |  | Retained |
| art_story | value | artifact-value | Narrative story. |  |  | Retained |
| art_structured_report | value | artifact-value | Headed/structured report. |  |  | Retained |
| art_technical_explanation | value | artifact-value | Technical explanation of a concept. |  |  | Retained |

### capacity-unit-value

| symbol | kind | category | definition | not | aliases | status |
|---|---|---|---|---|---|---|
| rule_category_capacity_unit_value | category_rule | capacity-unit-value | Preserve original binary-unit definitions for audit, but mark Needs clarification: GB/TB aliases conflate decimal and binary units. No silent change to scale. |  |  | Retained |
| cap_gb | value | capacity-unit-value | One gibibyte-equivalent RAM capacity unit. |  | GB, gigabytes | Retained |
| cap_tb | value | capacity-unit-value | One tebibyte-equivalent capacity unit. |  | TB, terabytes | Retained |

### character-property-value

| symbol | kind | category | definition | not | aliases | status |
|---|---|---|---|---|---|---|
| rule_category_character_property_value | category_rule | character-property-value | TERM-described trait/style. Use constraints and explicit inclusion/scope; do not use an ungoverned character_properties attribute. |  |  | Retained |

### code-value

| symbol | kind | category | definition | not | aliases | status |
|---|---|---|---|---|---|---|
| rule_category_code_value | category_rule | code-value | path_/sym_ remain STRING identities; migrated chg_/assert_ are TERM constructors. Do not recover an exact file path by guessing from underscores. |  |  | Retained |
| path_gcloud_pubsub_subscription_py | value | code-value | File path to the Google Cloud Pub/Sub subscription module. |  | gcloud_pubsub_subscription_path | Accepted |
| path_numpy_core_fromnumeric_py | value | code-value | Source code file path or exported symbol in scientific Python: path_numpy_core_fromnumeric_py. |  | path_numpy_core_fromnumeric_py | Accepted |
| path_pandas_src_testing_pyx | value | code-value | Source code file path or exported symbol in scientific Python: path_pandas_src_testing_pyx. |  | path_pandas_src_testing_pyx | Accepted |
| path_sklearn_linear_model_logistic_py | value | code-value | The scikit-learn logistic module path. |  |  | Retained |
| sym_log_reg_scoring_path | value | code-value | The _log_reg_scoring_path program symbol. |  |  | Retained |
| sym_pandas_testing_assert_almost_equal | value | code-value | Source code file path or exported symbol in scientific Python: sym_pandas_testing_assert_almost_equal. |  | sym_pandas_testing_assert_almost_equal | Accepted |

### constraint-value

| symbol | kind | category | definition | not | aliases | status |
|---|---|---|---|---|---|---|
| rule_category_constraint_value | category_rule | constraint-value | Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first. |  |  | Retained |
| constraint_17_plus | value | constraint-value | Rated 17+ or mature. |  |  | Retained |

### content-value

| symbol | kind | category | definition | not | aliases | status |
|---|---|---|---|---|---|---|
| rule_category_content_value | category_rule | content-value | Existing compounds become the constructors in Section 5. Their outputs go in topic/target/constraints as appropriate, not content, whose spec type remains STRING. |  |  | Retained |

### cuisine-value

| symbol | kind | category | definition | not | aliases | status |
|---|---|---|---|---|---|---|
| rule_category_cuisine_value | category_rule | cuisine-value | STRING cuisine class; cuisine_indian is a cuisine filter, not the location India. |  |  | Retained |
| cuisine_arab | value | cuisine-value | Arab culinary cuisine style. | cuisine_mediterranean (broader regional category) | Arab food, Arabic food, Arab cuisine | Accepted |
| cuisine_indian | value | cuisine-value | Indian cuisine. |  | Indian food, Indian | Retained |
| cuisine_italian | value | cuisine-value | Italian cuisine. |  | Italian food, Italian | Retained |
| cuisine_mediterranean | value | cuisine-value | Mediterranean culinary cuisine style. |  | mediterranean | Accepted |
| cuisine_pizza | value | cuisine-value | Pizza culinary cuisine style and food category. | cuisine_italian (broader regional/national cuisine) | pizza, pizzeria, pizza cuisine | Accepted |

### currency-value

| symbol | kind | category | definition | not | aliases | status |
|---|---|---|---|---|---|---|
| rule_category_currency_value | category_rule | currency-value | STRING currency identity. A bare dollar sign is not always curr_usd; require contextual resolution. |  |  | Retained |
| curr_clp | value | currency-value | Chilean peso. |  | clp, Chilean pesos, Chilean peso | Retained |
| curr_eur | value | currency-value | Euro. |  | eur, euros | Retained |
| curr_usd | value | currency-value | United States dollar. |  | $, usd, dollars | Retained |

### descriptive-value

| symbol | kind | category | definition | not | aliases | status |
|---|---|---|---|---|---|---|
| rule_category_descriptive_value | category_rule | descriptive-value | STRING modifier/domain label; never a free-form proposition. dom_sgi needs its intended referent established before semantically dependent use. |  |  | Retained |
| beliefs | value | descriptive-value | Concept of cognitive beliefs, convictions, or worldviews. |  | beliefs | Accepted |
| constitutional_ai | value | descriptive-value | Concept of rule-based constitutional training and self-critique principles in AI alignment. |  | constitutional_ai | Accepted |
| criminality | value | descriptive-value | Descriptive concept of criminality in cultural and social contexts. |  | criminality | Accepted |
| design_parameters | value | descriptive-value | Concept of operational and behavioral design specifications for AI systems. |  | design_parameters | Accepted |
| dom_ovr | value | descriptive-value | One-versus-rest domain concept. |  |  | Retained |
| dom_pain | value | descriptive-value | Pain domain concept. |  | pain | Retained |
| dom_safari | value | descriptive-value | Safari domain concept. |  | safari | Retained |
| dom_sgi | value | descriptive-value | SGI domain concept. |  |  | Retained |
| mod_mixed_case | value | descriptive-value | Mixed-case modifier. |  | mixed case | Retained |
| personal_values | value | descriptive-value | Concept of personal moral beliefs and subjective ethical commitments. |  | personal_values | Accepted |
| potential_harms | value | descriptive-value | Concept of potential safety hazards, adverse outcomes, or risks in AI interaction. |  | potential_harms | Accepted |
| tattoos | value | descriptive-value | Descriptive concept of tattoos in cultural and social contexts. |  | tattoos | Accepted |
| yakuza | value | descriptive-value | Descriptive concept of yakuza in cultural and social contexts. |  | yakuza | Accepted |

### duration-unit-value

| symbol | kind | category | definition | not | aliases | status |
|---|---|---|---|---|---|---|
| rule_category_duration_unit_value | category_rule | duration-unit-value | STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds. |  |  | Retained |
| unit_character | value | duration-unit-value | One Unicode scalar value in the final rendered artifact; line endings are normalized to LF before counting. |  | characters, chars | Adapted |
| unit_day | value | duration-unit-value | Day. |  | days | Adapted |
| unit_hour | value | duration-unit-value | Hour. |  | hours | Adapted |
| unit_item | value | duration-unit-value | Top-level generated list or report item. |  | items, entries | Adapted |
| unit_minute | value | duration-unit-value | Minute. |  | minutes, min | Adapted |
| unit_month | value | duration-unit-value | Month. |  | months | Adapted |
| unit_paragraph | value | duration-unit-value | Paragraph of text. |  | paragraphs, paragraph | Adapted |
| unit_second | value | duration-unit-value | Second. |  | seconds, sec | Adapted |
| unit_week | value | duration-unit-value | Week. |  | weeks | Adapted |
| unit_word | value | duration-unit-value | Rendered whitespace-delimited word. |  | words | Adapted |
| unit_year | value | duration-unit-value | Year. |  | years | Adapted |

### entity-name

| symbol | kind | category | definition | not | aliases | status |
|---|---|---|---|---|---|---|
| rule_category_entity_name | category_rule | entity-name | STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted. |  |  | Retained |
| afcfta | value | entity-name | African Continental Free Trade Area international agreement. |  | african_continental_free_trade_area | Accepted |
| alcohol | value | entity-name | Alcoholic spirit or liquid such as brandy, rum, or whisky. | fermented non-distilled wine or pure chemical formula notation | alcohol, spirits, liquor | Accepted |
| apple | value | entity-name | An apple fruit item, typically an ingredient or interactive food object. | tomato or other fruits/vegetables | apple, apples, red apple, green apple, apple slice | Accepted |
| armchair | value | entity-name | An armchair; distinct from a sofa |  |  | Retained |
| bed | value | entity-name | A bed furniture surface or sleeping area. |  | bed | Accepted |
| bottle | value | entity-name | A bottle container object, typically used for holding liquids. | mug (a drinking cup with a handle) or water (the liquid itself) | bottle, water bottle, plastic bottle | Accepted |
| bowl | value | entity-name | A container/dish used for holding food or small items. |  | bowl | Accepted |
| bowtie | value | entity-name | Item or prop in joke/creative context: bowtie. |  | bowtie | Accepted |
| bread | value | entity-name | A bread loaf or slice food object. |  | bread | Accepted |
| cabinet | value | entity-name | An enclosed cupboard or cabinet storage furniture unit with doors or shelves. | counter (a countertop surface) or dresser (a chest of drawers) | cabinet, cupboard, storage cabinet, kitchen cupboard | Accepted |
| candle | value | entity-name | A candle light source made of wax with a wick. | lamp (an electric light appliance or fixture) | candle, wax candle | Accepted |
| cat | value | entity-name | Animal entity: cat. |  | cat | Accepted |
| cd | value | entity-name | A compact disc physical object. | a digital media file or streaming track | CD, compact_disc | Accepted |
| chair | value | entity-name | A chair furniture seat with a backrest. | armchair (specifically an armchair with side armrests) or sofa | chair, seat | Accepted |
| cheese | value | entity-name | Dairy food item: cheese. | meat or non-dairy food items | cheese | Accepted |
| citric_acid | value | entity-name | Food and beverage acid additive. | tartaric_acid or pure chemical formula notation | citric acid | Accepted |
| clock | value | entity-name | A clock timepiece appliance. | duration units like unit_hour | clock, timer | Accepted |
| clothing | value | entity-name | Physical item used for concealment or covering: clothing. |  | clothing | Accepted |
| coffee_maker | value | entity-name | A coffee-making appliance; not automatically a heating resource |  |  | Retained |
| credit_card | value | entity-name | A physical plastic credit, debit, or payment card object. | egift_card (an electronic gift card or digital voucher) | credit card, card, payment card | Accepted |
| desk | value | entity-name | A work desk furniture surface. |  | desk | Accepted |
| dishwasher | value | entity-name | A dishwasher kitchen appliance. | sink (a washing basin) or washing_machine (a laundry appliance) | dishwasher, dish washer, dishwashing machine | Accepted |
| donkey | value | entity-name | Animal entity: donkey. |  | donkey | Accepted |
| door | value | entity-name | A door architectural barrier or entryway. | wall or close/open operations | door, doorway, room door | Accepted |
| dresser | value | entity-name | A chest of drawers / dresser furniture. |  | dresser | Accepted |
| dried_fruit | value | entity-name | Generic dried fruit food item. | fresh fruit or specific dried varieties like raisin or sultana | dried fruit, dried fruits | Accepted |
| dulce_de_leche | value | entity-name | Sweet caramelized milk confection or dessert spread: dulce de leche. | cheese or dulce_de_nata | dulce de leche, dulce_de_leche | Accepted |
| dulce_de_nata | value | entity-name | Clotted cream milk confection or dessert item: dulce de nata. | dulce_de_leche or cheese | dulce de nata, dulce_de_nata | Accepted |
| earth | value | entity-name | The planet Earth as an astronomical celestial body. | soil, ground surface, or electrical grounding | earth, the earth, planet earth, Earth | Accepted |
| egg | value | entity-name | An egg food item, typically an ingredient or interactive food object. | apple, tomato, or other food items | egg, eggs, boiled egg, cooked egg | Accepted |
| egift_card | value | entity-name | Electronic gift card or digital voucher product. |  | digital_gift_card, e_gift_card | Accepted |
| entity_appetizers | value | entity-name | Event planning item or menu category: entity_appetizers. |  | entity_appetizers | Accepted |
| entity_assembly_tips | value | entity-name | Event planning item or menu category: entity_assembly_tips. |  | entity_assembly_tips | Accepted |
| entity_cake | value | entity-name | Event planning item or menu category: entity_cake. |  | entity_cake | Accepted |
| entity_checklist | value | entity-name | Event planning item or menu category: entity_checklist. |  | entity_checklist | Accepted |
| entity_condensed_grocery_list | value | entity-name | Event planning item or menu category: entity_condensed_grocery_list. |  | entity_condensed_grocery_list | Accepted |
| entity_desserts | value | entity-name | Event planning item or menu category: entity_desserts. |  | entity_desserts | Accepted |
| entity_drinks | value | entity-name | Event planning item or menu category: entity_drinks. |  | entity_drinks | Accepted |
| entity_flowers | value | entity-name | Flowers, blossoms, or floral design elements. | constraint_exclude_flowery_language (a prose style constraint) or agricultural food items | flowers, floral, flower, floral decorations | Accepted |
| entity_grocery_list | value | entity-name | Event planning item or menu category: entity_grocery_list. |  | entity_grocery_list | Accepted |
| entity_mains | value | entity-name | Event planning item or menu category: entity_mains. |  | entity_mains | Accepted |
| entity_menu_items | value | entity-name | Event planning item or menu category: entity_menu_items. |  | entity_menu_items | Accepted |
| entity_order_vs_assemble_plan | value | entity-name | Event planning item or menu category: entity_order_vs_assemble_plan. |  | entity_order_vs_assemble_plan | Accepted |
| entity_recipes | value | entity-name | Event planning item or menu category: entity_recipes. |  | entity_recipes | Accepted |
| entity_sides | value | entity-name | Event planning item or menu category: entity_sides. |  | entity_sides | Accepted |
| entity_sweet_food | value | entity-name | Event planning item or menu category: entity_sweet_food. |  | entity_sweet_food | Accepted |
| enzyme | value | entity-name | Winemaking enzyme for breaking down fruit cellular structure. | living yeast strains or non-enzymatic chemical additives | enzyme, pectic enzyme, pectinase | Accepted |
| fermentation_nutrient | value | entity-name | Yeast nutrient supplement such as diammonium phosphate (DAP). | wine_yeast (the living organism itself) or acid additives | fermentation nutrient, yeast nutrient, DAP | Accepted |
| figurine | value | entity-name | A small carved, molded, or sculpted decorative statuette object. | character (a fictional persona) or captioned_figure (a document figure/photo) | figurine, statuette, statue, small statue, sculptural figure, miniature figure | Accepted |
| fish | value | entity-name | Animal entity: fish. |  | fish | Accepted |
| fridge | value | entity-name | A refrigerator cooling appliance. |  | fridge | Accepted |
| fruit_juice | value | entity-name | Liquid juice extracted from fruit. | fermented wine or freshly crushed grape_must | fruit juice, juice | Accepted |
| grape_cabernet_sauvignon | value | entity-name | Cabernet Sauvignon wine grape variety. | other red grape varieties such as grape_merlot or grape_pinot_noir | Cabernet Sauvignon, cabernet, cabernet sauvignon grape | Accepted |
| grape_chardonnay | value | entity-name | Chardonnay wine grape variety. | other white grape varieties such as grape_sauvignon_blanc | Chardonnay, chardonnay grape | Accepted |
| grape_merlot | value | entity-name | Merlot wine grape variety. | other red grape varieties such as grape_cabernet_sauvignon or grape_pinot_noir | Merlot, merlot grape | Accepted |
| grape_must | value | entity-name | Freshly crushed fruit juice mixture before fermentation. | clarified fruit_juice or finished wine | grape must, must | Accepted |
| grape_pinot_noir | value | entity-name | Pinot Noir wine grape variety. | other red grape varieties such as grape_cabernet_sauvignon or grape_merlot | Pinot Noir, pinot noir grape | Accepted |
| grape_sauvignon_blanc | value | entity-name | Sauvignon Blanc wine grape variety. | other white grape varieties such as grape_chardonnay | Sauvignon Blanc, sauvignon blanc grape | Accepted |
| grape_tannin | value | entity-name | Tannin powder derived from grapes for wine structure. | oak_chips or wood aging additives | grape tannin, tannin, wine tannin | Accepted |
| grape_thompson_seedless | value | entity-name | Thompson Seedless grape variety. | wine grape cultivars like grape_merlot or grape_chardonnay | Thompson Seedless, thompson seedless grape, sultana grape | Accepted |
| ice_cream | value | entity-name | Frozen dessert food item: ice cream. | entity_desserts or entity_sweet_food (generic menu categories) | ice cream, ice_cream | Accepted |
| keys | value | entity-name | A physical key or set of keys / keychain object. | press_key (a UI keyboard key press operation) | keys, key, key chain, keychain | Accepted |
| knife | value | entity-name | A cutting utensil used for slicing or food preparation. |  | knife | Accepted |
| lamp | value | entity-name | A lamp light source appliance. | an abstract lighting concept or ambient color | light, desk_lamp | Accepted |
| laptop | value | entity-name | A portable laptop computer physical object. | topic_macbook_pro_2017 (a generation topic label) | laptop, laptop computer, notebook | Accepted |
| lettuce | value | entity-name | A head of lettuce or leafy green vegetable food item. | tomato or potato (other vegetable items) | lettuce, head of lettuce, salad greens | Accepted |
| maqluba | value | entity-name | Traditional Arab layered rice dish: maqluba. | cuisine_mediterranean (cuisine style rather than specific dish) | maqluba, makloubeh | Accepted |
| martini_glass | value | entity-name | A cocktail or Martini drinking glass object. | mug (a drinking cup with a handle) or bottle (liquid storage container) | martini glass, cocktail glass, glass | Accepted |
| meat | value | entity-name | Food item: meat or beef. | tuna or fish (specific aquatic foods) | meat, beef | Accepted |
| microwave | value | entity-name | A microwave oven appliance. |  | microwave | Accepted |
| mittens | value | entity-name | Item or prop in joke/creative context: mittens. |  | mittens | Accepted |
| moon | value | entity-name | Earth's natural celestial satellite. | an artificial satellite or other planetary moon | moon, the moon, Luna | Accepted |
| mug | value | entity-name | Drinking cup. |  | mug | Adapted |
| oak_chips | value | entity-name | Oak wood pieces or barrels used for wine aging and flavor extraction. | grape_tannin or structural chemical additives | oak chips, oak pieces, oak barrels | Accepted |
| pan | value | entity-name | A metal cooking vessel, frying pan, skillet, saucepan, or pot cookware item used for preparing, heating, or holding food. | bowl (deep concave vessel) or plate (shallow flat dining dish) | pan, frying pan, skillet, saucepan, pot | Accepted |
| pen | value | entity-name | A writing instrument. |  | pen | Accepted |
| pencil | value | entity-name | A pencil writing instrument. |  | pencil | Accepted |
| piano | value | entity-name | A piano musical instrument or large furniture object. | topic_classical_piano or topic_jazz_piano (music genre topics) | piano, grand piano, upright piano, keyboard | Accepted |
| pillow | value | entity-name | A pillow; not a specific selected pillow until pick_up returns REF |  |  | Retained |
| plate | value | entity-name | A shallow, flat dish or vessel used for holding, preparing, or serving food. | bowl (deep concave vessel) or table (furniture surface) | dish, plate | Accepted |
| popcorn | value | entity-name | Popcorn food item or snack. |  | popped_corn | Accepted |
| potato | value | entity-name | A potato food item, typically an ingredient or object in interactive environments. | tomato or other vegetables | potato, potatoes, spud | Accepted |
| raisin | value | entity-name | Dried grape food item. | sultana (specifically dried white grape) or fresh wine_grape | raisin, raisins, dried grape | Accepted |
| recycle_bin | value | entity-name | A dedicated receptacle container for recyclable waste materials. | trash_can (a general waste receptacle container) | recycle bin, recycling bin, recycle_bin | Accepted |
| remote_control | value | entity-name | A handheld electronic remote control device. | an individual button or interactive UI element | remote, remote control, TV remote, controller | Accepted |
| resource_chiller | value | entity-name | Canonical abstract chilling resource when no particular appliance is named. |  |  | Adapted |
| resource_heater | value | entity-name | Canonical abstract heating resource when no particular appliance is named. |  |  | Adapted |
| resource_sink | value | entity-name | Canonical abstract washing resource when no particular sink is named. |  |  | Adapted |
| restaurant | value | entity-name | A commercial restaurant, eatery, or dining establishment where meals are prepared and served. | ryokan or onsen (specific traditional hospitality establishments) | restaurant, eatery, dining establishment, restaurants | Accepted |
| safe | value | entity-name | A secure, lockable metal storage container or receptacle for holding valuables. | cabinet (a general storage cupboard) or dresser (a chest of drawers) | safe, strongbox, lockbox, deposit box | Accepted |
| shower | value | entity-name | A bathroom shower fixture or stall used for bathing. | sink (a washing basin) or toilet (a toilet fixture) | shower, shower stall | Accepted |
| sink | value | entity-name | Washing basin. |  | sink | Adapted |
| sofa | value | entity-name | A sofa used as source/destination; not the pillow on it |  |  | Retained |
| spatula | value | entity-name | A kitchen utensil with a broad, flat, and flexible blade used for lifting, flipping, or spreading food. | knife (cutting utensil) or spoon (scooping utensil) | spatula, turner, flipper | Accepted |
| sponge | value | entity-name | A porous, absorbent sponge cleaning tool or object. | tissue_box (a paper tissue box) or other wiping materials | sponge, cleaning sponge | Accepted |
| spoon | value | entity-name | An eating or cooking utensil. |  | spoon | Accepted |
| stove | value | entity-name | A kitchen stove / range appliance for cooking or heating. | microwave | stove, range, cooktop | Accepted |
| sultana | value | entity-name | Dried white seedless grape food product. | raisin (dark dried grape) or wine_grape | sultana, sultanas, golden raisin | Accepted |
| sun | value | entity-name | The central star of the Solar System. | an artificial lighting appliance or sunlight | sun, the sun, Sol | Accepted |
| tartaric_acid | value | entity-name | Winemaking acid additive used for acidity adjustment. | citric_acid or general organic chemicals | tartaric acid | Accepted |
| textbook | value | entity-name | A textbook or instructional book used as an educational resource. | style_academic (which is a stylistic mode) or art_short_text (which is a brief generated text artifact) | textbook, book, coursebook, textbooks | Accepted |
| tissue_box | value | entity-name | A cardboard or plastic box containing paper tissues used for wiping or cleaning. | waterproof bandages or other medical coverings | tissue box, tissues, tissue | Accepted |
| toilet | value | entity-name | A toilet bathroom fixture or receptacle. | sink or trash_can | toilet, commode, restroom toilet | Accepted |
| tomato | value | entity-name | A tomato item, typically a food object in interactive environments. |  | tomato | Accepted |
| trash_can | value | entity-name | A waste receptacle container. |  | trash_can | Accepted |
| tuna | value | entity-name | Animal entity: tuna. |  | tuna | Accepted |
| vase | value | entity-name | A decorative or functional open container typically used for holding cut flowers or liquids. | bottle (a liquid storage container with a narrow neck) or bowl (a shallow dish) | vase, flower vase, flower_vase | Accepted |
| water | value | entity-name | Water from a tap or faucet used for washing or rinsing. | sink or other liquids | water, tap water | Accepted |
| waterproof_bandages | value | entity-name | Physical item used for concealment or covering: waterproof_bandages. |  | waterproof_bandages | Accepted |
| waterproof_stickers | value | entity-name | Physical item used for concealment or covering: waterproof_stickers. |  | waterproof_stickers | Accepted |
| wine | value | entity-name | Fermented fruit or grape beverage. | unfermented fruit juice or distilled alcohol/spirits | wine, wines | Accepted |
| wine_grape | value | entity-name | Grape variety cultivated specifically for winemaking. | table grapes or processed wine product | wine grape, wine grapes, grape | Accepted |
| wine_yeast | value | entity-name | Yeast strain selected for alcoholic fermentation. | baking yeast or fermentation_nutrient | wine yeast, yeast, fermentation yeast | Accepted |
| yarn | value | entity-name | Item or prop in joke/creative context: yarn. |  | yarn | Accepted |

### event-value

| symbol | kind | category | definition | not | aliases | status |
|---|---|---|---|---|---|---|
| rule_category_event_value | category_rule | event-value | TERM-described narrative event, not a recorded EVENT. Require inclusion explicitly when generating a story. |  |  | Retained |

### format-value

| symbol | kind | category | definition | not | aliases | status |
|---|---|---|---|---|---|---|
| rule_category_format_value | category_rule | format-value | STRING format. format_email is layout, not the action send_email. |  |  | Retained |
| format_bullet_list | value | format-value | Bulleted list. |  | bullet points | Retained |
| format_email | value | format-value | Email layout. |  | as an email | Retained |
| format_markdown | value | format-value | Markdown layout. |  | in markdown | Retained |
| format_newsletter | value | format-value | Newsletter layout. |  | newsletter | Retained |
| format_numbered_list | value | format-value | Numbered list. |  | numbered steps | Retained |
| format_pdf | value | format-value | PDF document. |  | as a pdf | Retained |
| format_plain_text | value | format-value | Unstructured prose text. |  | plain text | Retained |
| format_structured_report | value | format-value | Headed structured report layout. |  | structured report, report | Retained |
| format_table | value | format-value | Tabular layout. |  | as a table | Retained |

### locale-value

| symbol | kind | category | definition | not | aliases | status |
|---|---|---|---|---|---|---|
| rule_category_locale_value | category_rule | locale-value | STRING locale. “English” alone does not always mean locale_en_us; preserve ambiguity. |  |  | Retained |
| locale_de | value | locale-value | German language or locale descriptor. | other language locales (such as locale_en_us or locale_fr) or country entity (germany) | German, german, Deutsch, de, de-DE | Accepted |
| locale_en_gb | value | locale-value | UK English. |  | british english | Adapted |
| locale_en_us | value | locale-value | US English. |  | english, en-us | Adapted |
| locale_es | value | locale-value | Spanish. |  | spanish | Adapted |
| locale_fr | value | locale-value | French. |  | french | Adapted |
| locale_hi_en | value | locale-value | Hinglish (Hindi-English mix). |  | hinglish | Adapted |
| locale_zh | value | locale-value | Chinese language locale (Simplified and Traditional Chinese). | a specific geographical region or nationality (use location-name) | chinese, zh, zh-cn, zh-tw, mandarin | Accepted |

### location-name

| symbol | kind | category | definition | not | aliases | status |
|---|---|---|---|---|---|---|
| rule_category_location_name | category_rule | location-name | STRING location descriptor. A `table` surface is not the generated artifact category art_table. |  |  | Retained |
| africa | value | location-name | Geopolitical nation or continental region: africa. |  | africa | Accepted |
| argentina | value | location-name | Geopolitical nation or location: Argentina. | locale_es (language) or curr_clp (currency) | Argentina, argentine | Accepted |
| corner | value | location-name | A corner area. |  |  | Retained |
| counter | value | location-name | A kitchen or room countertop surface. |  | counter | Accepted |
| eastern_cape | value | location-name | Eastern Cape region. |  |  | Retained |
| floor | value | location-name | The floor surface of an indoor room or architectural space. | wall (a vertical room boundary surface) or counter (a countertop surface) | floor, ground | Accepted |
| germany | value | location-name | Geopolitical nation or location: Germany. | locale_de (language) or curr_eur (currency) | Germany, German, Deutschland, Federal Republic of Germany | Accepted |
| island | value | location-name | A freestanding kitchen island counter or food preparation work surface. | counter (a perimeter countertop surface) or table (a dining or general furniture surface) | island, kitchen island, kitchen_island | Accepted |
| japan | value | location-name | Country of Japan. |  |  | Retained |
| liberal_onsen | value | location-name | Traditional Japanese establishment or hospitality venue: liberal_onsen. |  | liberal_onsen | Accepted |
| living_room | value | location-name | A residential room or general indoor living area. | floor (a floor surface) or wall (a vertical boundary surface) | living room, living_room, sitting room, lounge | Accepted |
| mexico | value | location-name | Geopolitical nation or location: Mexico. | locale_es (language) or other nations (use argentina, etc.) | Mexico, Mexican, Estados Unidos Mexicanos | Accepted |
| microwave_stand | value | location-name | A dedicated stand or cart supporting a microwave. |  | microwave_stand | Accepted |
| new_york_university | value | location-name | New York University institution or campus grounds. |  | nyu | Accepted |
| night_stand | value | location-name | A small bedside table or nightstand furniture surface. | a chest of drawers (use dresser) or a general table surface (use table) | nightstand, bedside table | Accepted |
| onsen | value | location-name | Traditional Japanese establishment or hospitality venue: onsen. |  | onsen | Accepted |
| russia | value | location-name | Geopolitical nation or continental region: russia. |  | russia | Accepted |
| ryokan | value | location-name | Traditional Japanese establishment or hospitality venue: ryokan. |  | ryokan | Accepted |
| table | value | location-name | A table surface. |  |  | Retained |
| ukraine | value | location-name | Geopolitical nation or continental region: ukraine. |  | ukraine | Accepted |
| wall | value | location-name | A room boundary wall surface. |  | wall | Accepted |

### metric-value

| symbol | kind | category | definition | not | aliases | status |
|---|---|---|---|---|---|---|
| rule_category_metric_value | category_rule | metric-value | STRING metric identity, not a Boolean value. Uptime and response time need numeric observations with units; order-late is Boolean-valued. Do not type every metric as BOOL. |  |  | Retained |
| metric_compatibility | value | metric-value | Compatibility status. |  | compatible | Adapted |
| metric_first_time_buyer | value | metric-value | Whether the customer is a first-time buyer. |  | first-time buyer, new customer | Adapted |
| metric_order_late | value | metric-value | Whether an order is late. |  | order is late, delayed | Adapted |
| metric_repeat_buyer | value | metric-value | Whether the customer is a repeat buyer. |  | repeat buyer, returning customer | Adapted |
| metric_response_time | value | metric-value | Support response time. |  | response time | Adapted |
| metric_uptime | value | metric-value | Service uptime status. |  | uptime, is up | Adapted |

### platform-name

| symbol | kind | category | definition | not | aliases | status |
|---|---|---|---|---|---|---|
| rule_category_platform_name | category_rule | platform-name | STRING service/framework identity. `django` does not also mean the project being edited unless context establishes that identity. |  |  | Retained |
| conda | value | platform-name | Conda package and environment management platform and software ecosystem. | an individual python script or general environment path | conda, anaconda, miniconda | Accepted |
| django | value | platform-name | Web framework. |  |  | Retained |
| gcloud | value | platform-name | Google Cloud Platform CLI and cloud software ecosystem. |  | google_cloud | Accepted |
| meson | value | platform-name | Meson build system software project. | an individual file path (use a string literal) | meson | Accepted |
| netflix | value | platform-name | Streaming platform. |  |  | Retained |
| numpy | value | platform-name | Python scientific package and computing platform: numpy. |  | numpy | Accepted |
| os_macos | value | platform-name | Apple macOS / OSX operating system platform. | Apple hardware or machine architecture | OSX, macOS, darwin, OS X | Accepted |
| pandas | value | platform-name | Python scientific package and computing platform: pandas. |  | pandas | Accepted |
| pants | value | platform-name | Pants build system and software execution platform. | clothing item (which is clothing in entity-name) | pants, pantsbuild, pants_build | Accepted |
| python_platform | value | platform-name | Python programming language execution environment and runtime platform. | an individual Python source file or package | python, python3, cpython | Accepted |
| qiskit | value | platform-name | Quantum computing SDK and open-source software development framework: qiskit / qiskit-terra. | an individual source file path or script | qiskit, qiskit_terra, qiskit-terra | Accepted |
| sklearn | value | platform-name | Machine learning library. |  |  | Retained |
| xarray | value | platform-name | Python scientific package and computing platform: xarray. |  | xarray | Accepted |
| youtube | value | platform-name | Video platform. |  |  | Retained |

### product-attribute-value

| symbol | kind | category | definition | not | aliases | status |
|---|---|---|---|---|---|---|
| rule_category_product_attribute_value | category_rule | product-attribute-value | STRING color/size/product-market facets. gender_women describes a product category, not an assertion about a person's gender. |  |  | Retained |
| color_black | value | product-attribute-value | Black. |  |  | Retained |
| color_blue | value | product-attribute-value | Blue visual color qualifier. |  | color_blue | Accepted |
| color_brown | value | product-attribute-value | Brown visual color qualifier. | color_black, color_grey, or other distinct color shades | brown | Accepted |
| color_green | value | product-attribute-value | Green visual color qualifier. | color_yellow or other distinct color shades | green, color_green | Accepted |
| color_grey | value | product-attribute-value | Grey visual color qualifier. |  | color_grey | Accepted |
| color_pink | value | product-attribute-value | Pink visual color qualifier. | color_red, color_purple, or other distinct color shades | pink, color_pink, blush pink, rose pink, pastel pink | Accepted |
| color_purple | value | product-attribute-value | Purple visual color qualifier. |  | color_purple | Accepted |
| color_red | value | product-attribute-value | Red. |  |  | Retained |
| color_white | value | product-attribute-value | White. |  |  | Retained |
| color_yellow | value | product-attribute-value | Yellow. |  |  | Retained |
| gender_men | value | product-attribute-value | Men's/male-targeted. |  | men, male | Retained |
| gender_unisex | value | product-attribute-value | Unisex. |  | unisex | Retained |
| gender_women | value | product-attribute-value | Women's/female-targeted. |  | women, female | Retained |
| size_large | value | product-attribute-value | Large size. |  | large, L | Retained |
| size_medium | value | product-attribute-value | Medium size. |  | medium, M | Retained |
| size_small | value | product-attribute-value | Small size. |  | small, S | Retained |
| size_tall | value | product-attribute-value | Tall relative vertical dimension qualifier. |  | size_tall | Accepted |
| valet | value | product-attribute-value | Valet parking or dedicated vehicle attendant service. |  | valet_parking | Accepted |

### recipient-value

| symbol | kind | category | definition | not | aliases | status |
|---|---|---|---|---|---|---|
| rule_category_recipient_value | category_rule | recipient-value | STRING roles or explicit named recipients. A role is not an exact person's identity. Keep an explicit name where substituting a role loses information. |  |  | Retained |
| foreigners | value | recipient-value | Social, demographic, or institutional group: foreigners. |  | foreigners | Accepted |
| japanese_government | value | recipient-value | Social, demographic, or institutional group: japanese_government. |  | japanese_government | Accepted |
| role_agent | value | recipient-value | The assistant. |  | you, the assistant | Adapted |
| role_colleague | value | recipient-value | A coworker of the user. |  | my colleague, coworker | Adapted |
| role_customer | value | recipient-value | A customer/client of the user. |  | the customer, client | Adapted |
| role_daughter | value | recipient-value | Daughter participant role in family or travel context. | role_sister, role_mother, or generic role_kids | daughter, my daughter | Accepted |
| role_friend | value | recipient-value | A friend of the user. |  | my friend | Adapted |
| role_kids | value | recipient-value | Children/kids participant group in event context. |  | kids, children | Accepted |
| role_manager | value | recipient-value | The user's manager. |  | my manager, boss | Adapted |
| role_mother | value | recipient-value | The mother of the user. | role_sister or role_kids | my mom, mother, mom | Accepted |
| role_professor | value | recipient-value | The user's professor/instructor. |  | my professor, teacher | Adapted |
| role_sister | value | recipient-value | Sister participant role in family/event context. |  | sister | Accepted |
| role_support_team | value | recipient-value | A customer-support team. |  | support, customer service | Adapted |
| role_user | value | recipient-value | The requesting human. |  | me, I | Adapted |
| tattooed_guests | value | recipient-value | Social, demographic, or institutional group: tattooed_guests. |  | tattooed_guests | Accepted |

### reservation-status-value

| symbol | kind | category | definition | not | aliases | status |
|---|---|---|---|---|---|---|
| rule_category_reservation_status_value | category_rule | reservation-status-value | STRING filter states; neither is a BOOL result binding. check_reservation_availability returns a BOOL with a distinct handle. |  |  | Retained |
| reservation_available | value | reservation-status-value | A reservation can be made. |  | reservation availability, available reservations | Retained |
| reservation_unavailable | value | reservation-status-value | A reservation cannot be made. |  | no reservations | Retained |

### search-value

| symbol | kind | category | definition | not | aliases | status |
|---|---|---|---|---|---|---|
| rule_category_search_value | category_rule | search-value | STRING refinements rank_ / dir_ / cat_ / avail_ / genre_ are separate. rank_rating may fill rank_field; genre_comedy may not. “Cheapest” usually requires both rank_price and dir_asc, not rank_price alone. |  |  | Retained |
| avail_in_stock | value | search-value | Available for purchase now. |  | available | Adapted |
| avail_out_of_stock | value | search-value | Unavailable for purchase now. |  | sold out | Adapted |
| cat_game | value | search-value | Category: video game. |  |  | Adapted |
| cat_limited_time_offers | value | search-value | Category: time-limited deals. |  |  | Adapted |
| dir_asc | value | search-value | Ascending rank direction. |  | lowest first | Adapted |
| dir_desc | value | search-value | Descending rank direction. |  | highest first | Adapted |
| genre_comedy | value | search-value | Genre: comedy. |  |  | Adapted |
| rank_distance | value | search-value | Rank field: proximity. |  | nearest, closest | Adapted |
| rank_price | value | search-value | Rank or filter field: monetary cost. |  | cheapest, lowest price | Adapted |
| rank_rating | value | search-value | Rank or filter field: user or critic score. |  |  | Adapted |

### semantic-category-value

| symbol | kind | category | definition | not | aliases | status |
|---|---|---|---|---|---|---|
| rule_category_semantic_category_value | category_rule | semantic-category-value | STRING class label used by typed constraints. class_temple describes a class, not an acquired physical temple reference. |  |  | Retained |
| class_beach | value | semantic-category-value | The abstract class or category of beach destinations and coastal environments. | island (kitchen island work surface) or a specific named beach location | beach, beaches, beach destination, seaside | Accepted |
| class_temple | value | semantic-category-value | The abstract class of temples. |  | temple, temples | Retained |
| class_town | value | semantic-category-value | The abstract class of towns. |  | town, towns | Retained |

### shape-value

| symbol | kind | category | definition | not | aliases | status |
|---|---|---|---|---|---|---|
| rule_category_shape_value | category_rule | shape-value | STRING geometry. shape_round may select a circular object; it does not imply color or dimensions. |  |  | Retained |
| shape_oval | value | shape-value | Oval. |  | oval | Retained |
| shape_rectangular | value | shape-value | Rectangular. |  | rectangular, rectangle | Retained |
| shape_round | value | shape-value | Circular/round. |  | round, circular | Retained |
| shape_square | value | shape-value | Square. |  | square | Retained |
| shape_triangular | value | shape-value | Triangular. |  | triangular, triangle | Retained |

### spatial-relation

| symbol | kind | category | definition | not | aliases | status |
|---|---|---|---|---|---|---|
| rule_category_spatial_relation | category_rule | spatial-relation | STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous. |  |  | Retained |
| behind | value | spatial-relation | Positioned behind. |  |  | Retained |
| between | value | spatial-relation | Positioned between or in the middle of reference entities. | next_to or in_front_of | between, in the middle of, middle of, center of | Accepted |
| in | value | spatial-relation | Contained within. |  | inside | Retained |
| in_front_of | value | spatial-relation | Positioned in front of. |  | in front of | Retained |
| left_of | value | spatial-relation | To the left of. |  | left of | Retained |
| next_to | value | spatial-relation | Adjacent to. |  | beside | Retained |
| on | value | spatial-relation | Resting atop. |  | on top of | Retained |
| other_side_of | value | spatial-relation | Positioned on the opposite or other side of a reference object. | next_to (which indicates general adjacency) | other side, other side of, opposite side of, opposite side | Accepted |
| right_of | value | spatial-relation | To the right of. |  | right of | Retained |
| under | value | spatial-relation | Beneath. |  | below | Retained |

### state-value

| symbol | kind | category | definition | not | aliases | status |
|---|---|---|---|---|---|---|
| rule_category_state_value | category_rule | state-value | STRING condition used in selection. state_warm does not command heat; “hot” is not automatically synonymous with “warm.” |  |  | Retained |
| state_clean | value | state-value | Clean condition. |  | clean | Adapted |
| state_cold | value | state-value | Cold or chilled condition. |  | cold, chilled | Adapted |
| state_dirty | value | state-value | Dirty condition. |  | dirty | Adapted |
| state_empty | value | state-value | Contains no intended material or usable remaining amount. |  | empty, used up | Adapted |
| state_full | value | state-value | Contains its intended material or remaining usable amount. |  | full, filled | Adapted |
| state_microwaved | value | state-value | Has been microwaved. |  | microwaved | Adapted |
| state_sliced | value | state-value | The condition of being sliced or cut into thin pieces. | the operation slice itself | sliced, slice, chopped, cut | Accepted |
| state_upright | value | state-value | An upright or vertically standing physical state of an object. | stand_up (which is an agent posture operation) | standing up, upright, vertical | Accepted |
| state_warm | value | state-value | Warm or heated condition. |  | warm, hot | Adapted |

### style-value

| symbol | kind | category | definition | not | aliases | status |
|---|---|---|---|---|---|---|
| rule_category_style_value | category_rule | style-value | STRING production style. style_narrative does not establish that described events occurred. |  |  | Retained |
| style_academic | value | style-value | Academic style. |  | academic | Retained |
| style_catchy | value | style-value | Catchy, attention-grabbing style. |  | catchy | Retained |
| style_narrative | value | style-value | Story-like narrative style. |  | narrative, story-style | Retained |
| style_persuasive | value | style-value | Persuasive/argumentative style. |  | persuasive | Retained |
| style_technical | value | style-value | Technical/expository style. |  | technical | Retained |

### time-of-day-value

| symbol | kind | category | definition | not | aliases | status |
|---|---|---|---|---|---|---|
| daytime | value | time-of-day-value | The period of natural daylight between sunrise and sunset in the diurnal cycle. | unit_day (a 24-hour elapsed duration unit) or clock time timestamps | daytime, day, day time, daylight hours | Accepted |
| nighttime | value | time-of-day-value | The period of darkness between sunset and sunrise in the diurnal cycle. | night_stand (a piece of furniture) or clock time timestamps | nighttime, night, night time, darkness | Accepted |

### tone-value

| symbol | kind | category | definition | not | aliases | status |
|---|---|---|---|---|---|---|
| rule_category_tone_value | category_rule | tone-value | STRING register. tone_urgent describes urgency, not a concrete deadline. |  |  | Retained |
| tone_casual | value | tone-value | Informal register. |  | casually | Retained |
| tone_concise | value | tone-value | Brief, to-the-point register. |  | briefly, concisely | Retained |
| tone_empathetic | value | tone-value | Conveys empathy/understanding. |  | sympathetically | Retained |
| tone_formal | value | tone-value | Formal register. |  | formally | Retained |
| tone_neutral | value | tone-value | Plain, unmarked register. |  |  | Retained |
| tone_polite | value | tone-value | Courteous, respectful register. |  | politely, kindly | Retained |
| tone_professional | value | tone-value | Workplace-appropriate register. |  | professionally | Retained |
| tone_silly | value | tone-value | Playful, lighthearted, or silly conversational tone. |  | silly | Accepted |
| tone_urgent | value | tone-value | Conveys urgency. |  | urgently, ASAP | Retained |

### topic-value

| symbol | kind | category | definition | not | aliases | status |
|---|---|---|---|---|---|---|
| rule_category_topic_value | category_rule | topic-value | Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it. |  |  | Retained |
| topic_abortion | value | topic-value | The subject matter, ethical debate, healthcare procedure, or legal question of abortion and reproductive choice. | general politics (use topic_politics) or cognitive belief concepts (use beliefs) | abortion, reproductive rights, abortion rights | Accepted |
| topic_baldurs_gate_3 | value | topic-value | Baldur's Gate 3. |  |  | Retained |
| topic_classical_piano | value | topic-value | Classical piano. |  |  | Retained |
| topic_current_events | value | topic-value | Current news, geopolitical events, and ongoing international developments. |  | current_events, news | Accepted |
| topic_food_safety | value | topic-value | Food safety guidelines, sanitary regulations, or handling practices. |  | food_safety | Accepted |
| topic_jazz_piano | value | topic-value | Jazz piano. |  |  | Retained |
| topic_macbook_pro_2017 | value | topic-value | MacBook Pro 2017. |  |  | Retained |
| topic_pickup_lines | value | topic-value | Pickup lines. |  |  | Retained |
| topic_politics | value | topic-value | Politics. |  |  | Retained |
| topic_spider_man_2 | value | topic-value | Marvel's Spider-Man 2. |  |  | Retained |

### transformation-value

| symbol | kind | category | definition | not | aliases | status |
|---|---|---|---|---|---|---|
| rule_category_transformation_value | category_rule | transformation-value | TERM-described transformation. Pass it through constraints; no ungoverned transformations attribute. |  |  | Retained |

### unit-value

| symbol | kind | category | definition | not | aliases | status |
|---|---|---|---|---|---|---|
| unit_fahrenheit | value | unit-value | Standard unit of temperature measurement on the Fahrenheit scale. | qualitative thermal states (use state_warm or state_cold) or duration units (use unit_minute, etc.) | Fahrenheit, deg F, degrees Fahrenheit, degrees F, F | Accepted |
| unit_kilometer | value | unit-value | Standard metric measurement unit of distance equal to 1,000 meters. | temporal duration units (like unit_minute) or non-metric distance units | km, kilometer, kilometres, kilometers | Accepted |
| unit_liter | value | unit-value | Standard metric measurement unit of liquid volume equal to 1 cubic decimeter (1,000 milliliters). | digital capacity units (like cap_gb) or temporal duration units | l, liter, liters, litres | Accepted |

## Attributes

| symbol | kind | category | definition | aliases | status |
|---|---|---|---|---|---|
| cuisine | attribute | attribute-name | Restaurant or food cuisine from cuisine-value. |  | Structural |
| min_ram | attribute | attribute-name | Minimum RAM capacity as NUMBER. | RAM or more, at least RAM | Structural |
| quantity | attribute | attribute-name | Explicit count as NUMBER. |  | Structural |
| ram_unit | attribute | attribute-name | Unit for min_ram from capacity-unit-value. |  | Structural |
| rank_direction | attribute | attribute-name | Sort direction from search-value. |  | Structural |
| rank_field | attribute | attribute-name | Field used by sort from search-value. |  | Structural |
| reservation_availability | attribute | attribute-name | Required reservation state from reservation-status-value. |  | Structural |
| target | attribute | attribute-name | The acted-on entity or generated artifact. |  | Structural |

## Structural tokens

| symbol | kind | category | definition | status |
|---|---|---|---|---|
| != | structural | structural-word | Inequality. | Structural |
| ( | structural | structural-word | Paren start. | Structural |
| ) | structural | structural-word | Paren end. | Structural |
| , | structural | structural-word | Separator. | Structural |
| - | structural | structural-word | Arithmetic difference. | Structural |
| -> | structural | structural-word | Result bind. | Structural |
| : | structural | structural-word | Type annotator. | Structural |
| < | structural | structural-word | Less-than. | Structural |
| <= | structural | structural-word | Less-or-equal. | Structural |
| = | structural | structural-word | Assignment. | Structural |
| == | structural | structural-word | Equality. | Structural |
| > | structural | structural-word | Greater-than. | Structural |
| >= | structural | structural-word | Greater-or-equal. | Structural |
| ACTION | structural | structural-word | Executes an external operation. | Structural |
| AGENT | structural | structural-word | Agent speaker. | Structural |
| ALL | structural | structural-word | Universal quantifier. | Structural |
| AND | structural | structural-word | Logical AND. | Structural |
| ANY | structural | structural-word | Existential quantifier. | Structural |
| BOOL | structural | structural-word | Boolean type. | Structural |
| CONTEXT | structural | structural-word | Task context. | Structural |
| CONVO | structural | structural-word | Declares a conversation. | Structural |
| DECREASES | structural | structural-word | Recursion guard. | Structural |
| EACH | structural | structural-word | Marks per-member iteration. | Structural |
| ELSE | structural | structural-word | Starts the false branch. | Structural |
| ENTRYPOINT | structural | structural-word | Names the single execution root. | Structural |
| FALSE | structural | structural-word | Boolean false literal. | Structural |
| FOR | structural | structural-word | Starts iteration. | Structural |
| GENERATE | structural | structural-word | Generates a non-effectful artifact. | Structural |
| IF | structural | structural-word | Starts a conditional branch. | Structural |
| IN | structural | structural-word | Introduces an iterable or relation. | Structural |
| LET | structural | structural-word | Binds a value. | Structural |
| LIST | structural | structural-word | List type. | Structural |
| NOT | structural | structural-word | Logical NOT. | Structural |
| NUMBER | structural | structural-word | Numeric type. | Structural |
| OR | structural | structural-word | Logical OR. | Structural |
| REF | structural | structural-word | Runtime entity-reference type. | Structural |
| REPLY_TO | structural | structural-word | Turn adjacency. | Structural |
| RETURN | structural | structural-word | Returns a task value. | Structural |
| REVISES | structural | structural-word | Turn correction. | Structural |
| SATISFIES | structural | structural-word | Introduces a quantifier condition. | Structural |
| SPEAKER | structural | structural-word | Speaker label. | Structural |
| STRING | structural | structural-word | Text type. | Structural |
| TASK | structural | structural-word | Declares a task. | Structural |
| THEN | structural | structural-word | Starts the true branch. | Structural |
| TRUE | structural | structural-word | Boolean true literal. | Structural |
| TURN | structural | structural-word | Declares a conversation turn. | Structural |
| USER | structural | structural-word | User speaker. | Structural |
| UTTER | structural | structural-word | Records a speech act. | Structural |
| [ | structural | structural-word | Bracket start. | Structural |
| ] | structural | structural-word | Bracket end. | Structural |
| { | structural | structural-word | Block start. | Structural |
| } | structural | structural-word | Block end. | Structural |

## Worked examples

| symbol | kind | definition | code |
|---|---|---|---|
| example_a_select_two_pillows_and_move_those_objects | example | Select two pillows and move those objects<br><br>NL: “Move two pillows from the sofa onto the armchair.” No implied heating, cleaning, or extra resources. | MODE REQUEST<br>ENTRYPOINT Pillow<br>TASK Pillow {<br>  ACTION pick_up(target=pillow, quantity=2, source=sofa) -> pillow_refs : LIST[REF[STRING]]<br>  FOR EACH item IN pillow_refs {<br>    ACTION place(target=item, destination=armchair, relation=on)<br>  }<br>} |
| example_b_preserve_the_class_and_amount_of_an_itinerary_constraint | example | Preserve the class and amount of an itinerary constraint<br><br>NL: “Make a three-day Kyoto itinerary, including at least one temple each day, with at most twenty minutes of walking between stops.” | MODE REQUEST<br>ENTRYPOINT Itinerary<br>TASK Itinerary : STRING {<br>  TERM content_kyoto_itinerary() -> content_kyoto_itinerary_2 : TERM<br>  TERM duration(amount=3, unit=unit_day) -> duration_2 : TERM<br>  TERM minimum_per_period(class=class_temple, count=1, period=unit_day) -> minimum_per_period_2 : TERM<br>  TERM maximum_between_stops(activity="walk", amount=20, unit=unit_minute) -> maximum_between_stops_2 : TERM<br>  GENERATE(target=art_itinerary, constraints=[duration_2, minimum_per_period_2, maximum_between_stops_2], topic=content_kyoto_itinerary_2) -> itinerary : STRING<br>  RETURN itinerary<br>} |
| example_c_existing_constraint_symbol_becomes_a_typed_construction | example | Existing constraint symbol becomes a typed construction<br><br>NL: “Suggest realistic pickup lines.” This example treats the message as a conversational request for suggestions.<br><br>The TERM is a requirement; it does not assert that an existing answer is realistic. Unlike the old STRING list, constraints has LIST[TERM]. | MODE REQUEST<br>ENTRYPOINT Conversation<br>CONVO Conversation {<br>  TURN t1 SPEAKER=USER {<br>    TERM constraint_realistic() -> constraint_realistic_2 : TERM<br>    UTTER ask(constraints=[constraint_realistic_2], topic=topic_pickup_lines)<br>  }<br>} |
| example_d_record_an_actual_test_outcome_without_asserting_overall_correctness | example | Record an actual test outcome without asserting overall correctness<br><br>Source manifest: `t1:tests` identifies a supplied agent/tool trace in which the scikit-learn test run exits successfully. The source explicitly reports the selected tests passed; it does not establish that every bug is fixed. | MODE TRACE<br>ENTRYPOINT Conversation<br>CONVO Conversation {<br>  TURN t1 SPEAKER=AGENT {<br>    RECORD ACTION run_tests(target=sklearn) STATUS succeeded SOURCE "t1:tests" -> run_tests_event : EVENT<br>    CLAIM outcome(event=run_tests_event, value=TRUE) BY role_agent STATUS observed SOURCE "t1:tests" -> outcome_2 : CLAIM<br>  }<br>} |
| example_e_preserve_exact_wording_through_generation_and_sending | example | Preserve exact wording through generation and sending<br><br>NL: “Write a polite email asking my manager for an update on Project Atlas, and send it.”<br><br>The input authorizes sending in this represented request. Reading this encoding does not itself authorize a tool action. Generating a purpose label and sending that label verbatim would not preserve the request. | MODE REQUEST<br>ENTRYPOINT ShortText<br>TASK ShortText {<br>  TERM content_status_update(subject="Project Atlas") -> content_status_update_2 : TERM<br>  GENERATE(target=art_short_text, format=format_email, tone=tone_polite, topic=content_status_update_2) -> short_text : STRING<br>  ACTION send_email(content=short_text, recipient=role_manager, tone=tone_polite)<br>} |

## Deprecated

| symbol | kind | category | definition | deprecated | superseded_by | status |
|---|---|---|---|---|---|---|
| char_age_14 | composite | character-property-value | Age 14. | use character_trait(property="age_years", value=14); human decision 2026-10-04: sizes and amounts are a number plus a unit, built with a constructor; no symbol per value | v19/support/character_trait | Deprecated |
| char_age_18 | composite |  | Age 18 character trait. | use character_trait(property="age_years", value=18); human decision 2026-10-04: sizes and amounts are a number plus a unit, built with a constructor; no symbol per value | v19/support/character_trait | Deprecated |
