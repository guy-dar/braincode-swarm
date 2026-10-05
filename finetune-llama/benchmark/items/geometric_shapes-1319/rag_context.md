# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 16 needs (decomposition: llm), 107 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | action | t1:s1 | visualize the SVG path | `path_sklearn_linear_model_logistic_py`, `path_pandas_src_testing_pyx`, `sym_log_reg_scoring_path`, `path_gcloud_pubsub_subscription_py`, `performance_tracking`, `look`, `walk`, `dom_sgi`, `walk_backward`, `hover`, `path_numpy_core_fromnumeric_py`, `calculation` |
| n2 | object | t1:s1 | SVG path data | `path_sklearn_linear_model_logistic_py`, `path_pandas_src_testing_pyx`, `sym_log_reg_scoring_path`, `path_numpy_core_fromnumeric_py`, `path_gcloud_pubsub_subscription_py`, `rule_category_code_value`, `dom_sgi`, `content_decision_study_sgi_japan`, `dom_safari`, `performance_tracking`, `dom_ovr`, `path_ipython_core_magics_basic_py` |
| n3 | speech_act | t1:s28 | ask which shapes are present in the SVG visualization | `shape_oval`, `shape_square`, `ask`*, `look`, `rule_category_shape_value`, `size_tall`, `shape_rectangular`, `shape_triangular`, `content_decision_study_sgi_japan`, `art_character_profile`, `turn`, `art_structured_report` |
| n4 | constraint | t1:s9 | candidate shape 1: rectangle that is not a square with no diagonals | `shape_rectangular`*, `shape_square`*, `shape_oval`, `shape_triangular`, `shape_round`, `corner`, `rule_category_shape_value`, `wall`, `recycle_bin`, `other_side_of`, `chair`, `table` |
| n5 | constraint | t1:s11 | candidate shape 2: square with no diagonals | `shape_square`*, `shape_oval`, `shape_rectangular`, `shape_triangular`, `shape_round`, `size_tall`, `corner`, `unit_second`, `wall`, `rule_category_shape_value`, `other_side_of`, `turn` |
| n6 | constraint | t1:s13 | candidate shape 3: triangle that is not a right triangle | `shape_triangular`*, `shape_oval`, `shape_rectangular`, `shape_square`, `shape_round`, `rule_category_shape_value`, `size_tall`, `corner`, `behind`, `topic_baldurs_gate_3`, `turn`, `other_side_of` |
| n7 | constraint | t1:s15 | candidate shape 4: right triangle | `shape_triangular`*, `shape_oval`, `shape_square`, `shape_rectangular`, `shape_round`, `size_tall`, `corner`, `rule_category_shape_value`, `behind`, `left_of`, `turn`, `in_front_of` |
| n8 | constraint | t1:s17 | candidate shape 5: parallelogram that is not a rectangle with no diagonals | `shape_rectangular`*, `shape_oval`, `shape_triangular`, `shape_square`, `shape_round`, `size_tall`, `corner`, `similarity`, `wall`, `rule_category_shape_value`, `other_side_of`, `format_markdown` |
| n9 | constraint | t1:s19 | candidate shape 6: trapezoid with exactly one pair of parallel sides and no diagonals | `other_side_of`, `shape_oval`, `shape_triangular`, `shape_rectangular`, `shape_square`, `shape_round`, `corner`, `wall`, `turn`, `left_of`, `dom_ddp`, `entity_sides` |
| n10 | constraint | t1:s21 | candidate shape 7: irregular convex pentagon with no diagonals | `shape_oval`, `shape_rectangular`, `shape_square`, `shape_round`, `shape_triangular`, `corner`, `rule_category_shape_value`, `wall`, `size_tall`, `dir_desc`, `turn`, `constraint_exclude_liberation_theme` |
| n11 | constraint | t1:s23 | candidate shape 8: irregular concave pentagon with no diagonals | `shape_oval`, `shape_rectangular`, `shape_triangular`, `shape_square`, `shape_round`, `corner`, `wall`, `size_tall`, `rule_category_shape_value`, `constraint_exclude_liberation_theme`, `dir_desc`, `turn` |
| n12 | constraint | t1:s25 | candidate shape 9: regular pentagon with no diagonals | `shape_oval`, `shape_square`, `shape_rectangular`, `shape_round`, `corner`, `shape_triangular`, `wall`, `rule_category_shape_value`, `dir_desc`, `unit_word`, `constraint_exclude_liberation_theme`, `size_tall` |
| n13 | constraint | t1:s27 | candidate shape 10: regular hexagon with no diagonals | `shape_oval`, `shape_rectangular`, `shape_square`, `shape_triangular`, `shape_round`, `corner`, `rule_category_shape_value`, `wall`, `unit_word`, `tone_neutral`, `constraint_budget_limited`, `constraint_include_character_attribute_list` |
| n14 | constraint | t1:s29 | allow shapes to be drawn by collinear lines | `shape_oval`, `shape_square`, `shape_rectangular`, `shape_round`, `shape_triangular`, `rule_category_shape_value`, `corner`, `wall`, `aesthetic`, `pencil`, `constraint_include_character_attribute_list`, `constraint_exclude_liberation_theme` |
| n15 | constraint | t1:s30 | select from multiple-choice options A through P | `constraint_single_choice`, `select_option`, `search_travel`, `constraint_include_character_attribute_list`, `format_numbered_list`, `constraint_exclude_liberation_theme`, `constraint_budget_limited`, `constraint_comprehensive`, `rank_direction`, `pick_up`, `constraint_exclude_flowery_language`, `constraint_beginner` |
| n16 | constraint | t1:s47 | ignore slight coordinate differences due to rounding | `shape_round`*, `shape_oval`, `shape_square`, `shape_rectangular`, `rank_distance`, `shape_triangular`, `corner`, `behind`, `rule_category_shape_value`, `maximum_between_stops`, `tone_neutral`, `rank_direction` |

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

- walk.destination → object_label
- face.target → object_label
- search_travel.location → country
- pick_up.target → object_label, food_label
- pick_up.source → object_label
- pick_up.color → color_label
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

**rule_reading_guide** (v19/rule/reading-guide; core)

The spec governs syntax/types; this glossary defines vocabulary. Signature notation: ? optional, A / B explicit alternatives, void no result. Omitted optional arguments are unspecified. Value entries are category-refined STRING primitives; complex meanings require composition. Aliases are contextual hints, not unconditional equivalences. Report ambiguity. IDs use v19/<category>/<symbol>, v19/support/<symbol> or v19/composite/<symbol>. Statuses apply to this candidate: Retained preserves meaning; Adapted uses the stated contract; Composite requires TERM (bare STRING deprecated); Structural is syntax/argument vocabulary; Needs clarification is unusable until resolved; Deprecated is historical; Accepted is usable within this candidate.

**rule_recording_signatures** (v19/rule/recording-signatures; rule governing look)

RECORD ACTION uses the operation signature with REF[STRING] → TERM and LIST[REF[STRING]] → LIST[TERM]; other types/categories stay unchanged. Return EVENT, never the runtime result. Record actual outputs as attributed CLAIMs. Do not infer missing resources.

**rule_speech_acts_general** (v19/rule/speech-acts-general; rule governing ask)

UTTER-only, void, with the spec's speech attributes and LIST[TERM] constraints. No result binding. Literal content cannot replace required semantic arguments for structured coverage.

**rule_structural_constructs** (v19/rule/structural-constructs; core)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; rule governing exists_in)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_attributes_and_generate** (v19/rule/attributes-and-generate; rule governing art_character_profile)

Attribute entries name arguments; legality/types come from each operation, not global membership. GENERATE uses the spec's core fields; retained artifact profiles return STRING. Numeric/list results need explicit profiles. Legacy itinerary fields expand to TERM constraints: duration/duration_unit → duration(amount,unit); stop_min_per_day/stop_requirement → minimum_per_period(class,count,period=unit_day), never an inferred temple class; max_walk_duration/unit → maximum_between_stops(activity="walk",amount,unit). No legacy shorthand is enabled. Old events/character_properties/transformations become explicitly scoped TERM constraints. Message purpose is TERM, not send_email.content: GENERATE exact STRING content, then send. Report opaque fallback separately.

**rule_category_artifact_value** (v19/rule/category/artifact-value; rule governing art_character_profile)

STRING artifact class for GENERATE.target. art_story says what kind of artifact to produce, not what occurs in its plot.

**rule_category_code_value** (v19/rule/category/code-value; candidate)

path_/sym_ remain STRING identities; migrated chg_/assert_ are TERM constructors. Do not recover an exact file path by guessing from underscores.

**rule_category_constraint_value** (v19/rule/category/constraint-value; rule governing constraint_exclude_liberation_theme)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_content_value** (v19/rule/category/content-value; rule governing content_decision_study_sgi_japan)

Existing compounds become the constructors in Section 5. Their outputs go in topic/target/constraints as appropriate, not content, whose spec type remains STRING.

**rule_category_descriptive_value** (v19/rule/category/descriptive-value; rule governing dom_sgi)

STRING modifier/domain label; never a free-form proposition. dom_sgi needs its intended referent established before semantically dependent use.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; rule governing unit_second)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing gift)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_format_value** (v19/rule/category/format-value; rule governing format_markdown)

STRING format. format_email is layout, not the action send_email.

**rule_category_location_name** (v19/rule/category/location-name; rule governing corner)

STRING location descriptor. A `table` surface is not the generated artifact category art_table.

**rule_category_product_attribute_value** (v19/rule/category/product-attribute-value; rule governing size_tall)

STRING color/size/product-market facets. gender_women describes a product category, not an assertion about a person's gender.

**rule_category_search_value** (v19/rule/category/search-value; rule governing dir_desc)

STRING refinements rank_ / dir_ / cat_ / avail_ / genre_ are separate. rank_rating may fill rank_field; genre_label::comedy may not. “Cheapest” usually requires both rank_price and dir_asc, not rank_price alone.

**rule_category_shape_value** (v19/rule/category/shape-value; candidate)

STRING geometry. shape_round may select a circular object; it does not imply color or dimensions.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing other_side_of)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_tone_value** (v19/rule/category/tone-value; rule governing tone_neutral)

STRING register. tone_urgent describes urgency, not a concrete deadline.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_baldurs_gate_3)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_composites_general** (v19/rule/composites-general; rule governing content_decision_study_sgi_japan)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_operations_general** (v19/rule/operations-general; rule governing look)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_support_primitives_general** (v19/rule/support-primitives-general; rule governing performance_tracking)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- face | operation | operation-vocabulary | (target: STRING / TERM / ATOM[object_label]) -> void | Orient agent body/camera directly toward a target entity. target must be a perceptible entity. | aliases: orient_towards  ⟵ candidate
- hover | operation | operation-vocabulary | (target: REF[STRING]) -> void | Move pointer cursor over an interactive web element without clicking. target must resolve to a valid element reference. | aliases: mouse_over  ⟵ candidate
- look | operation | operation-vocabulary | (direction: STRING) -> void | Tilt or adjust agent visual camera gaze. direction is up, down, or straight. | aliases: tilt_camera  ⟵ candidate
- pick_up | operation | operation-vocabulary | (target: STRING / ATOM[object_label] / ATOM[food_label], quantity?: NUMBER, source?: STRING / ATOM[object_label], color?: STRING / ATOM[color_label], shape?: STRING, state?: STRING) -> REF[STRING] or LIST[REF[STRING]] | Select/acquire objects. Missing quantity or literal 1 returns REF; integer literal greater than 1 returns LIST[REF]. Other values are invalid for this profile. | aliases: grab, take, retrieve  ⟵ candidate
- search_travel | operation | operation-vocabulary | (target: STRING, constraints?: LIST[TERM], location?: STRING / ATOM[country]) -> LIST[REF[STRING]] | Query travel options meeting supplied constraints. Does not book them.  ⟵ candidate
- select_option | operation | operation-vocabulary | (target: REF[STRING], value: STRING) -> void | Select an option from a dropdown or select menu element. target must be a select element. | aliases: choose_option, choose_dropdown, pick_option  ⟵ candidate
- turn | operation | operation-vocabulary | (direction: STRING) -> void | Rotate agent body/view orientation. direction is typically left, right, or angle. | aliases: rotate, turn_around  ⟵ candidate
- walk | operation | operation-vocabulary | (destination: STRING / TERM / ATOM[object_label], relation?: STRING) -> void | Locomote towards a target destination or landmark. destination must identify a valid entity or location. | aliases: move_to, go_to, navigate_to  ⟵ candidate
- walk_backward | operation | operation-vocabulary | (modifier?: STRING) -> void | Walk backward. Optional modifier can specify the degree or minor distance of movement. | not: walk (which moves forward toward a destination) | aliases: move backward, step back  ⟵ candidate

### speech acts

- ask | speech_act | operation-vocabulary | UTTER ask(target: TERM, or a sufficiently precise topic: STRING / TERM) | Request information/advice; not an assertion of an answer. | aliases: ask, how should  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ dependency of content_decision_study_sgi_japan
- aesthetic | constructor | TERM aesthetic(period: STRING, style: STRING) -> TERM | A stylistic description with an explicit period | not: Not a character's age or production date  ⟵ candidate
- calculation | constructor | TERM calculation(inputs: LIST[TERM], operation: STRING, result?: TERM) -> TERM | Constructs a descriptive representation of an arithmetic or algorithmic calculation step with inputs, operation identifier, and optional resulting value. | not: an executed runtime action or factual claim of outcome | aliases: math_operation, compute_step  ⟵ candidate
- decision | constructor | TERM decision(activity: TERM) -> TERM | A decision whose content is the described activity | not: Not proof it was carried out  ⟵ dependency of content_decision_study_sgi_japan
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ dependency of constraint_exclude_liberation_theme
- include | constructor | TERM include(item: STRING / TERM) -> TERM | Require the identified content/item | not: Not permission to invent an instance in a recorded trace  ⟵ dependency of constraint_include_character_attribute_list
- maximum_between_stops | constructor | TERM maximum_between_stops(activity: STRING, amount: NUMBER, unit: STRING) -> TERM | Upper bound on the stated activity between successive stops | not: Not a limit on total daily duration  ⟵ candidate
- performance_tracking | constructor | TERM performance_tracking(adjustment?: STRING / TERM, target: STRING / TERM) -> TERM | Constructs a descriptive representation of monitoring performance metrics or campaign results with an optional strategy adjustment. | not: a runtime metric observation or software test run | aliases: track_results, monitor_performance, campaign_tracking  ⟵ candidate
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ dependency of constraint_budget_limited
- similarity | constructor | TERM similarity(target: STRING / TERM, dimension?: STRING / TERM) -> TERM | Constructs a descriptor representing comparative closeness or similarity to a target along a given dimension. | not: spatial proximity (use rank_distance or next_to) or an assertion of exact identity (use identity) | aliases: closest_to, similar_to, resembles  ⟵ candidate
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ dependency of exists_in

### composites

- constraint_beginner | composite | constraint-value | TERM constraint_beginner() -> TERM | Targeted at beginners. | = requirement(property="audience_expertise", value="beginner")  ⟵ candidate
- constraint_budget_limited | composite | constraint-value | TERM constraint_budget_limited() -> TERM | Limited budget. | = requirement(property="budget_limited", value=TRUE)  ⟵ candidate
- constraint_comprehensive | composite | constraint-value | TERM constraint_comprehensive() -> TERM | Must be comprehensive. | = requirement(property="comprehensive", value=TRUE)  ⟵ candidate
- constraint_exclude_flowery_language | composite | constraint-value | TERM constraint_exclude_flowery_language() -> TERM | Avoid flowery language. | = exclude(item="flowery_language")  ⟵ candidate
- constraint_exclude_liberation_theme | composite | constraint-value | TERM constraint_exclude_liberation_theme() -> TERM | Avoid liberation theme. | = exclude(item="liberation_theme")  ⟵ candidate
- constraint_include_character_attribute_list | composite | constraint-value | TERM constraint_include_character_attribute_list() -> TERM | Include character attributes. | = include(item="character_attribute_list")  ⟵ candidate
- constraint_single_choice | composite | constraint-value | TERM constraint_single_choice() -> TERM | Must pick a single choice. | = requirement(property="choice_count", value=1)  ⟵ candidate
- content_decision_study_sgi_japan | composite | content-value | TERM content_decision_study_sgi_japan(actor: STRING) -> TERM | A personal decision to travel to Japan to study SGI. | = decision(activity=activity(verb="travel", actor=$actor, location=country::JP, purpose=activity(verb="study", actor=$actor, object=dom_sgi)))  ⟵ candidate

### claim relations

- enables | claim_relation | CLAIM enables(condition: TERM / CLAIM, outcome: TERM / CLAIM) | Asserts that an enabling condition or capability facilitates an outcome. enabling condition. | aliases: facilitates, allows  ⟵ candidate
- exists_in | claim_relation | CLAIM exists_in(subject: STRING / TERM, location: STRING / TERM) | Asserts that an entity, policy, or phenomenon exists within a geographical or conceptual location. spatial/locational existence. | aliases: present_in  ⟵ candidate
- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ core
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ dependency of enables

### links

- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ core
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ core
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ core

### values

- art_character_profile | value | artifact-value | Descriptive character profile.  ⟵ candidate
- art_structured_report | value | artifact-value | Headed/structured report.  ⟵ candidate
- path_gcloud_pubsub_subscription_py | value | code-value | File path to the Google Cloud Pub/Sub subscription module. | aliases: gcloud_pubsub_subscription_path  ⟵ candidate
- path_ipython_core_magics_basic_py | value | code-value | File path to the IPython basic magics module. | not: an individual command line script or general config file | aliases: IPython/core/magics/basic.py, ipython_core_magics_basic_py  ⟵ candidate
- path_numpy_core_fromnumeric_py | value | code-value | Source code file path or exported symbol in scientific Python: path_numpy_core_fromnumeric_py. | aliases: path_numpy_core_fromnumeric_py  ⟵ candidate
- path_pandas_src_testing_pyx | value | code-value | Source code file path or exported symbol in scientific Python: path_pandas_src_testing_pyx. | aliases: path_pandas_src_testing_pyx  ⟵ candidate
- path_sklearn_linear_model_logistic_py | value | code-value | The scikit-learn logistic module path.  ⟵ candidate
- sym_log_reg_scoring_path | value | code-value | The _log_reg_scoring_path program symbol.  ⟵ candidate
- dom_ddp | value | descriptive-value | DistributedDataParallel (DDP) multi-GPU distributed training configuration and execution paradigm. | not: dom_ovr (one-versus-rest classification) or platform_label::python (general Python runtime) | aliases: DDP, DistributedDataParallel, distributed data parallel  ⟵ candidate
- dom_ovr | value | descriptive-value | One-versus-rest domain concept.  ⟵ candidate
- dom_safari | value | descriptive-value | Safari domain concept. | aliases: safari  ⟵ candidate
- dom_sgi | value | descriptive-value | SGI domain concept.  ⟵ candidate
- unit_second | value | duration-unit-value | Second. | aliases: seconds, sec  ⟵ candidate
- unit_word | value | duration-unit-value | Rendered whitespace-delimited word. | aliases: words  ⟵ candidate
- chair | value | entity-name | A chair furniture seat with a backrest. | not: object_label::armchair (specifically an object_label::armchair with side armrests) or object_label::sofa | aliases: chair, seat  ⟵ candidate
- entity_sides | value | entity-name | Event planning item or menu category: entity_sides. | aliases: entity_sides  ⟵ candidate
- figurine | value | entity-name | A small carved, molded, or sculpted decorative statuette object. | not: character (a fictional persona) or captioned_figure (a document figure/photo) | aliases: figurine, statuette, statue, small statue, sculptural figure, miniature figure  ⟵ candidate
- gift | value | entity-name | A physical gift or present item to be wrapped, given, or received. | not: egift_card (an electronic gift card or digital voucher product) | aliases: gift, present, wrapped gift, package  ⟵ candidate
- pencil | value | entity-name | A pencil writing instrument. | aliases: pencil  ⟵ candidate
- recycle_bin | value | entity-name | A dedicated receptacle container for recyclable waste materials. | not: trash_can (a general waste receptacle container) | aliases: recycle bin, recycling bin, recycle_bin  ⟵ candidate
- format_markdown | value | format-value | Markdown layout. | aliases: in markdown  ⟵ candidate
- format_numbered_list | value | format-value | Numbered list. | aliases: numbered steps  ⟵ candidate
- corner | value | location-name | A corner area.  ⟵ candidate
- table | value | location-name | A table surface.  ⟵ candidate
- wall | value | location-name | A room boundary wall surface. | aliases: wall  ⟵ candidate
- size_tall | value | product-attribute-value | Tall relative vertical dimension qualifier. | aliases: size_tall  ⟵ candidate
- dir_desc | value | search-value | Descending rank direction. | aliases: highest first  ⟵ candidate
- rank_distance | value | search-value | Rank field: proximity. | aliases: nearest, closest  ⟵ candidate
- shape_oval | value | shape-value | Oval. | aliases: oval  ⟵ candidate
- shape_rectangular | value | shape-value | Rectangular. | aliases: rectangular, rectangle  ⟵ candidate
- shape_round | value | shape-value | Circular/round. | aliases: round, circular  ⟵ candidate
- shape_square | value | shape-value | Square. | aliases: square  ⟵ candidate
- shape_triangular | value | shape-value | Triangular. | aliases: triangular, triangle  ⟵ candidate
- behind | value | spatial-relation | Positioned behind.  ⟵ candidate
- in_front_of | value | spatial-relation | Positioned in front of. | aliases: in front of  ⟵ candidate
- left_of | value | spatial-relation | To the left of. | aliases: left of  ⟵ candidate
- other_side_of | value | spatial-relation | Positioned on the opposite or other side of a reference object. | not: next_to (which indicates general adjacency) | aliases: other side, other side of, opposite side of, opposite side  ⟵ candidate
- tone_neutral | value | tone-value | Plain, unmarked register.  ⟵ candidate
- topic_baldurs_gate_3 | value | topic-value | Baldur's Gate 3.  ⟵ candidate

### attributes

- rank_direction | attribute | attribute-name | Sort direction from search-value.  ⟵ candidate
