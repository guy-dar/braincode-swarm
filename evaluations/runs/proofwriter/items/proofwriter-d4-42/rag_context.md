# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 61 needs (decomposition: llm), 182 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | speech_act | t1:s1 | introduce a set of premises or theory | `respond`, `propose`, `ask`, `subject`, `inform`, `supports`, `topic_school_work_routine`, `conjunction`, `in_front_of`, `confirm`, `example_of`, `regression_case` |
| n2 | claim | t1:s2 | the bald eagle is rough | `earth`, `shape_oval`, `hover`, `topic_baldurs_gate_3`, `leads_to`, `enables`, `recommended`, `moon`, `occurred_recently`, `outcome`, `statement`, `important` |
| n3 | object | t1:s2 | bald eagle → `animal_label::<key>` | `resource_chiller`, `topic_baldurs_gate_3`, `earth`, `moon`, `shape_oval`, `art_structured_report`, `oak_chips`, `meat`, `animal_label`*, `hover`, `chair`, `pan` |
| n4 | constraint | t1:s2 | rough | `state_dirty`, `shape_oval`, `constraint_budget_limited`, `spatula`, `constraint_respectful`, `tone_empathetic`, `shape_round`, `mattress`, `constraint_exclude_flowery_language`, `spoon`, `constraint_realistic`, `dom_pain` |
| n5 | claim | t1:s3 | the bald eagle likes the dog | `dog`*, `entity_order_vs_assemble_plan`, `recommended`, `leads_to`, `comfortable`, `style_catchy`, `animal_label`, `enables`, `important`, `hover`, `topic_classical_piano`, `earth` |
| n6 | object | t1:s3 | bald eagle → `animal_label::<key>` | `resource_chiller`, `topic_baldurs_gate_3`, `earth`, `moon`, `shape_oval`, `art_structured_report`, `oak_chips`, `meat`, `animal_label`*, `hover`, `chair`, `pan` |
| n7 | object | t1:s3 | dog → `animal_label::<key>` | `dog`*, `animal_label`*, `next_to`, `meat`, `right_of`, `cat_game`, `comfortable`, `tone_empathetic`, `locale_hi_en`, `caddy`, `locale_de`, `chair` |
| n8 | action | t1:s3 | likes | `style_narrative`, `similarity`, `style_catchy`, `on`, `well_wishes`, `next_to`, `character_trait`, `has_style`, `style_persuasive`, `comfortable`, `right_of`, `obligation` |
| n9 | claim | t1:s4 | the bald eagle visits the dog | `dog`*, `leads_to`, `recommended`, `entity_order_vs_assemble_plan`, `enables`, `animal_label`, `hover`, `topic_classical_piano`, `important`, `earth`, `occurred`, `causes` |
| n10 | object | t1:s4 | bald eagle → `animal_label::<key>` | `resource_chiller`, `topic_baldurs_gate_3`, `earth`, `moon`, `shape_oval`, `art_structured_report`, `oak_chips`, `meat`, `animal_label`*, `hover`, `chair`, `pan` |
| n11 | object | t1:s4 | dog → `animal_label::<key>` | `dog`*, `animal_label`*, `next_to`, `meat`, `right_of`, `cat_game`, `comfortable`, `tone_empathetic`, `locale_hi_en`, `caddy`, `locale_de`, `chair` |
| n12 | action | t1:s4 | visits | `look`, `block_evaluation`, `search_travel`, `propose`, `calculation`, `obligation`, `role_daughter`, `role_son`, `art_itinerary`, `occurred`, `role_colleague`, `wait` |
| n13 | claim | t1:s5 | the bald eagle visits the rabbit | `leads_to`, `topic_baldurs_gate_3`, `enables`, `hover`, `recommended`, `moon`, `dog`, `earth`, `entity_order_vs_assemble_plan`, `topic_spider_man_2`, `occurred_recently`, `statement` |
| n14 | object | t1:s5 | bald eagle → `animal_label::<key>` | `resource_chiller`, `topic_baldurs_gate_3`, `earth`, `moon`, `shape_oval`, `art_structured_report`, `oak_chips`, `meat`, `animal_label`*, `hover`, `chair`, `pan` |
| n15 | object | t1:s5 | rabbit → `animal_label::<key>` | `bread`, `dog`, `figurine`, `entity_cake`, `topic_spider_man_2`, `bowtie`, `animal_label`*, `resource_chiller`, `laptop`, `cat_game`, `mittens`, `caddy` |
| n16 | action | t1:s5 | visits | `look`, `block_evaluation`, `search_travel`, `propose`, `calculation`, `obligation`, `role_daughter`, `role_son`, `art_itinerary`, `occurred`, `role_colleague`, `wait` |
| n17 | claim | t1:s6 | the dog visits the bald eagle | `dog`*, `leads_to`, `recommended`, `entity_order_vs_assemble_plan`, `enables`, `animal_label`, `hover`, `important`, `earth`, `occurred`, `causes`, `ongoing` |
| n18 | object | t1:s6 | dog → `animal_label::<key>` | `dog`*, `animal_label`*, `next_to`, `meat`, `right_of`, `cat_game`, `comfortable`, `tone_empathetic`, `locale_hi_en`, `caddy`, `locale_de`, `chair` |
| n19 | object | t1:s6 | bald eagle → `animal_label::<key>` | `resource_chiller`, `topic_baldurs_gate_3`, `earth`, `moon`, `shape_oval`, `art_structured_report`, `oak_chips`, `meat`, `animal_label`*, `hover`, `chair`, `pan` |
| n20 | action | t1:s6 | visits | `look`, `block_evaluation`, `search_travel`, `propose`, `calculation`, `obligation`, `role_daughter`, `role_son`, `art_itinerary`, `occurred`, `role_colleague`, `wait` |
| n21 | claim | t1:s7 | the mouse is green | `lettuce`, `leads_to`, `hover`, `laptop`, `enables`, `topic_spider_man_2`, `topic_macbook_pro_2017`, `fridge`, `important`, `recommended`, `causes`, `occurred_recently` |
| n22 | object | t1:s7 | mouse → `animal_label::<key>` | `hover`, `laptop`, `dom_safari`, `topic_spider_man_2`, `fridge`, `pencil`, `dom_ovr`, `animal_label`*, `desk`, `piano`, `resource_chiller`, `pen` |
| n23 | constraint | t1:s7 | green → `color_label::<key>` | `color_label`*, `apple`, `lettuce`, `constraint_respectful`, `right_of`, `outshines`, `left_of`, `constraint_budget_limited`, `constraint_realistic`, `constraint_exclude_flowery_language`, `shape_square`, `constraint_beginner` |
| n24 | claim | t1:s8 | the mouse is round | `shape_round`*, `hover`, `leads_to`, `shape_oval`, `laptop`, `topic_spider_man_2`, `shape_triangular`, `important`, `causes`, `ongoing`, `recommended`, `occurred` |
| n25 | object | t1:s8 | mouse → `animal_label::<key>` | `hover`, `laptop`, `dom_safari`, `topic_spider_man_2`, `fridge`, `pencil`, `dom_ovr`, `animal_label`*, `desk`, `piano`, `resource_chiller`, `pen` |
| n26 | constraint | t1:s8 | round | `shape_round`*, `shape_oval`, `shape_triangular`, `shape_square`, `shape_rectangular`, `left_of`, `constraint_respectful`, `constraint_exclude_flowery_language`, `constraint_budget_limited`, `unit_day`, `between`, `rule_category_shape_value` |
| n27 | claim | t1:s9 | the mouse visits the rabbit | `leads_to`, `hover`, `topic_spider_man_2`, `enables`, `dog`, `cat_game`, `recommended`, `next_to`, `occurred_recently`, `laptop`, `outcome`, `ongoing` |
| n28 | object | t1:s9 | mouse → `animal_label::<key>` | `hover`, `laptop`, `dom_safari`, `topic_spider_man_2`, `fridge`, `pencil`, `dom_ovr`, `animal_label`*, `desk`, `piano`, `resource_chiller`, `pen` |
| n29 | object | t1:s9 | rabbit → `animal_label::<key>` | `bread`, `dog`, `figurine`, `entity_cake`, `topic_spider_man_2`, `bowtie`, `animal_label`*, `resource_chiller`, `laptop`, `cat_game`, `mittens`, `caddy` |
| n30 | action | t1:s9 | visits | `look`, `block_evaluation`, `search_travel`, `propose`, `calculation`, `obligation`, `role_daughter`, `role_son`, `art_itinerary`, `occurred`, `role_colleague`, `wait` |
| n31 | claim | t1:s10 | the rabbit eats the bald eagle | `hover`, `enables`, `leads_to`, `earth`, `moon`, `recommended`, `select_option`, `statement`, `occurred_recently`, `meat`, `outcome`, `dog` |
| n32 | object | t1:s10 | rabbit → `animal_label::<key>` | `bread`, `dog`, `figurine`, `entity_cake`, `topic_spider_man_2`, `bowtie`, `animal_label`*, `resource_chiller`, `laptop`, `cat_game`, `mittens`, `caddy` |
| n33 | object | t1:s10 | bald eagle → `animal_label::<key>` | `resource_chiller`, `topic_baldurs_gate_3`, `earth`, `moon`, `shape_oval`, `art_structured_report`, `oak_chips`, `meat`, `animal_label`*, `hover`, `chair`, `pan` |
| n34 | action | t1:s10 | eats | `spoon`, `menu_works`, `block_evaluation`, `meat`, `obligation`, `bread`, `calculation`, `entity_desserts`, `user_preference`, `state_sliced`, `propose`, `wait` |
| n35 | claim | t1:s11 | the rabbit is rough | `leads_to`, `dog`, `bread`, `enables`, `occurred_recently`, `recommended`, `outcome`, `caddy`, `important`, `statement`, `ongoing`, `tone_silly` |
| n36 | object | t1:s11 | rabbit → `animal_label::<key>` | `bread`, `dog`, `figurine`, `entity_cake`, `topic_spider_man_2`, `bowtie`, `animal_label`*, `resource_chiller`, `laptop`, `cat_game`, `mittens`, `caddy` |
| n37 | constraint | t1:s11 | rough | `state_dirty`, `shape_oval`, `constraint_budget_limited`, `spatula`, `constraint_respectful`, `tone_empathetic`, `shape_round`, `mattress`, `constraint_exclude_flowery_language`, `spoon`, `constraint_realistic`, `dom_pain` |
| n38 | claim | t1:s12 | the rabbit likes the bald eagle | `leads_to`, `enables`, `dog`, `hover`, `recommended`, `moon`, `entity_order_vs_assemble_plan`, `statement`, `earth`, `important`, `occurred_recently`, `entity_cake` |
| n39 | object | t1:s12 | rabbit → `animal_label::<key>` | `bread`, `dog`, `figurine`, `entity_cake`, `topic_spider_man_2`, `bowtie`, `animal_label`*, `resource_chiller`, `laptop`, `cat_game`, `mittens`, `caddy` |
| n40 | object | t1:s12 | bald eagle → `animal_label::<key>` | `resource_chiller`, `topic_baldurs_gate_3`, `earth`, `moon`, `shape_oval`, `art_structured_report`, `oak_chips`, `meat`, `animal_label`*, `hover`, `chair`, `pan` |
| n41 | action | t1:s12 | likes | `style_narrative`, `similarity`, `style_catchy`, `on`, `well_wishes`, `next_to`, `character_trait`, `has_style`, `style_persuasive`, `comfortable`, `right_of`, `obligation` |
| n42 | claim | t1:s13 | the rabbit likes the mouse | `hover`, `leads_to`, `dog`, `laptop`, `enables`, `cat_game`, `recommended`, `topic_spider_man_2`, `occurred_recently`, `important`, `statement`, `causes` |
| n43 | object | t1:s13 | rabbit → `animal_label::<key>` | `bread`, `dog`, `figurine`, `entity_cake`, `topic_spider_man_2`, `bowtie`, `animal_label`*, `resource_chiller`, `laptop`, `cat_game`, `mittens`, `caddy` |
| n44 | object | t1:s13 | mouse → `animal_label::<key>` | `hover`, `laptop`, `dom_safari`, `topic_spider_man_2`, `fridge`, `pencil`, `dom_ovr`, `animal_label`*, `desk`, `piano`, `resource_chiller`, `pen` |
| n45 | action | t1:s13 | likes | `style_narrative`, `similarity`, `style_catchy`, `on`, `well_wishes`, `next_to`, `character_trait`, `has_style`, `style_persuasive`, `comfortable`, `right_of`, `obligation` |
| n46 | reasoning | t1:s14 | if the mouse visits the rabbit and the mouse visits the dog, then the mouse eats the rabbit | `dog`*, `then`*, `hover`, `rejects`, `next_to`, `entity_order_vs_assemble_plan`, `in_front_of`, `laptop`, `associated_with`, `contrast`, `revises`, `supports` |
| n47 | reasoning | t1:s15 | if something is rough, then it is big | `then`*, `rejects`, `style_catchy`, `supports`, `contrast`, `important`, `associated_with`, `revises`, `shape_oval`, `state_dirty`, `size_small`, `size_large` |
| n48 | constraint | t1:s15 | big | `size_large`, `size_tall`, `size_medium`, `constraint_budget_limited`, `size_small`, `constraint_respectful`, `size_queen`, `constraint_realistic`, `constraint_exclude_flowery_language`, `constraint_include_character_attribute_list`, `entity_mains`, `constraint_exclude_liberation_theme` |
| n49 | reasoning | t1:s16 | if something likes the mouse and the mouse likes the rabbit, then it likes the rabbit | `entity_order_vs_assemble_plan`, `rejects`, `then`*, `style_catchy`, `next_to`, `dog`, `revises`, `varies_with`, `supports`, `in_front_of`, `topic_pickup_lines`, `similarity` |
| n50 | reasoning | t1:s17 | if something likes the dog, then it visits the dog | `dog`*, `then`*, `comfortable`, `varies_with`, `next_to`, `style_catchy`, `possesses`, `rejects`, `supports`, `animal_label`, `contrast`, `user_preference` |
| n51 | reasoning | t1:s18 | if something visits the mouse, then it is round | `shape_round`*, `then`*, `hover`, `rejects`, `topic_baldurs_gate_3`, `in_front_of`, `supports`, `associated_with`, `revises`, `shape_oval`, `on`, `look` |
| n52 | reasoning | t1:s19 | if something is green, then it is rough | `lettuce`, `then`*, `apple`, `rejects`, `supports`, `topic_pickup_lines`, `style_catchy`, `contrast`, `tone_silly`, `rule_category_shape_value`, `state_dirty`, `revises` |
| n53 | reasoning | t1:s20 | if something is rough, then it is green | `then`*, `lettuce`, `apple`, `rejects`, `supports`, `topic_pickup_lines`, `tone_silly`, `rule_category_shape_value`, `style_catchy`, `revises`, `associated_with`, `contrast` |
| n54 | reasoning | t1:s21 | if something is big and green, then it likes the dog | `dog`*, `then`*, `lettuce`, `apple`, `style_catchy`, `rejects`, `comfortable`, `supports`, `important`, `contrast`, `animal_label`, `similarity` |
| n55 | speech_act | t1:s22 | ask whether a statement is True, False, or Unknown | `ask`*, `statement`*, `confirm`, `respond`, `failure`, `unaware`, `propose`, `inform`, `acknowledge`, `controversial`, `rejects`, `negation` |
| n56 | constraint | t1:s22 | base the answer only on the provided theory | `respond`*, `extract`, `topic_baldurs_gate_3`, `subject`, `constraint_budget_limited`, `constraint_respectful`, `conjunction`, `constraint_realistic`, `regression_case`, `constraint_beginner`, `requirement`, `constraint_comprehensive` |
| n57 | constraint | t1:s22 | answer must be True, False, or Unknown | `constraint_realistic`, `constraint_respectful`, `in_front_of`, `right_of`, `constraint_budget_limited`, `metric_order_late`, `constraint_comprehensive`, `rejects`, `requirement`, `failure`, `constraint_single_choice`, `constraint_beginner` |
| n58 | claim | t1:s23 | the mouse visits the dog | `dog`*, `leads_to`, `hover`, `next_to`, `recommended`, `topic_spider_man_2`, `enables`, `laptop`, `topic_classical_piano`, `important`, `causes`, `occurred` |
| n59 | object | t1:s23 | mouse → `animal_label::<key>` | `hover`, `laptop`, `dom_safari`, `topic_spider_man_2`, `fridge`, `pencil`, `dom_ovr`, `animal_label`*, `desk`, `piano`, `resource_chiller`, `pen` |
| n60 | object | t1:s23 | dog → `animal_label::<key>` | `dog`*, `animal_label`*, `next_to`, `meat`, `right_of`, `cat_game`, `comfortable`, `tone_empathetic`, `locale_hi_en`, `caddy`, `locale_de`, `chair` |
| n61 | action | t1:s23 | visits | `look`, `block_evaluation`, `search_travel`, `propose`, `calculation`, `obligation`, `role_daughter`, `role_son`, `art_itinerary`, `occurred`, `role_colleague`, `wait` |

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
- regression_case.framework → platform_label
- search_travel.location → country
- failure.system → platform_label
- requirement.value → platform_label
- activity.object → object_label, food_label, animal_label
- activity.location → country
- activity.instrument → object_label, platform_label
- attribute_claim.subject → platform_label
- attribute_claim.value → platform_label
- walk.destination → object_label

## Retrieved records

### Shared rules that govern the records below (full text)

**rule_lexical_groups** (v19/rule/lexical-groups; rule governing platform_label)

Section 3.1 defines value groups: `group::key` values of type ATOM[group]. Open groups admit any key of their form (examples are not whitelists); standard groups admit the codes of their bundled standard (ISO 3166-1 alpha-2 for country, ISO 4217 for currency). Leaf values are never glossary entries. Consumer signatures alone decide where a group may appear. Retired bare symbols are invalid.

**rule_reading_guide** (v19/rule/reading-guide; core)

The spec governs syntax/types; this glossary defines vocabulary. Signature notation: ? optional, A / B explicit alternatives, void no result. Omitted optional arguments are unspecified. Value entries are category-refined STRING primitives; complex meanings require composition. Aliases are contextual hints, not unconditional equivalences. Report ambiguity. IDs use v19/<category>/<symbol>, v19/support/<symbol> or v19/composite/<symbol>. Statuses apply to this candidate: Retained preserves meaning; Adapted uses the stated contract; Composite requires TERM (bare STRING deprecated); Structural is syntax/argument vocabulary; Needs clarification is unusable until resolved; Deprecated is historical; Accepted is usable within this candidate.

**rule_recording_signatures** (v19/rule/recording-signatures; rule governing hover)

RECORD ACTION uses the operation signature with REF[STRING] → TERM and LIST[REF[STRING]] → LIST[TERM]; other types/categories stay unchanged. Return EVENT, never the runtime result. Record actual outputs as attributed CLAIMs. Do not infer missing resources.

**rule_speech_acts_general** (v19/rule/speech-acts-general; rule governing respond)

UTTER-only, void, with the spec's speech attributes and LIST[TERM] constraints. No result binding. Literal content cannot replace required semantic arguments for structured coverage.

**rule_structural_constructs** (v19/rule/structural-constructs; core)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; rule governing supports)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_attributes_and_generate** (v19/rule/attributes-and-generate; rule governing art_structured_report)

Attribute entries name arguments; legality/types come from each operation, not global membership. GENERATE uses the spec's core fields; retained artifact profiles return STRING. Numeric/list results need explicit profiles. Legacy itinerary fields expand to TERM constraints: duration/duration_unit → duration(amount,unit); stop_min_per_day/stop_requirement → minimum_per_period(class,count,period=unit_day), never an inferred temple class; max_walk_duration/unit → maximum_between_stops(activity="walk",amount,unit). No legacy shorthand is enabled. Old events/character_properties/transformations become explicitly scoped TERM constraints. Message purpose is TERM, not send_email.content: GENERATE exact STRING content, then send. Report opaque fallback separately.

**rule_category_artifact_value** (v19/rule/category/artifact-value; rule governing art_structured_report)

STRING artifact class for GENERATE.target. art_story says what kind of artifact to produce, not what occurs in its plot.

**rule_category_constraint_value** (v19/rule/category/constraint-value; rule governing constraint_budget_limited)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_descriptive_value** (v19/rule/category/descriptive-value; rule governing tattoos)

STRING modifier/domain label; never a free-form proposition. dom_sgi needs its intended referent established before semantically dependent use.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; rule governing unit_day)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing earth)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_event_value** (v19/rule/category/event-value; rule governing event_camper_in_sludge_pit)

TERM-described narrative event, not a recorded EVENT. Require inclusion explicitly when generating a story.

**rule_category_locale_value** (v19/rule/category/locale-value; rule governing locale_hi_en)

STRING locale. “English” alone does not always mean locale_en_us; preserve ambiguity.

**rule_category_location_name** (v19/rule/category/location-name; rule governing wall)

STRING location descriptor. A `table` surface is not the generated artifact category art_table.

**rule_category_metric_value** (v19/rule/category/metric-value; rule governing metric_order_late)

STRING metric identity, not a Boolean value. Uptime and response time need numeric observations with units; order-late is Boolean-valued. Do not type every metric as BOOL.

**rule_category_product_attribute_value** (v19/rule/category/product-attribute-value; rule governing size_small)

STRING color/size/product-market facets. gender_women describes a product category, not an assertion about a person's gender.

**rule_category_recipient_value** (v19/rule/category/recipient-value; rule governing role_friend)

STRING roles or explicit named recipients. A role is not an exact person's identity. Keep an explicit name where substituting a role loses information.

**rule_category_search_value** (v19/rule/category/search-value; rule governing cat_game)

STRING refinements rank_ / dir_ / cat_ / avail_ / genre_ are separate. rank_rating may fill rank_field; genre_label::comedy may not. “Cheapest” usually requires both rank_price and dir_asc, not rank_price alone.

**rule_category_shape_value** (v19/rule/category/shape-value; candidate)

STRING geometry. shape_round may select a circular object; it does not imply color or dimensions.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing in_front_of)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_state_value** (v19/rule/category/state-value; rule governing state_dirty)

STRING condition used in selection. state_warm does not command heat; “hot” is not automatically synonymous with “warm.”

**rule_category_style_value** (v19/rule/category/style-value; rule governing style_catchy)

STRING production style. style_narrative does not establish that described events occurred.

**rule_category_tone_value** (v19/rule/category/tone-value; rule governing tone_empathetic)

STRING register. tone_urgent describes urgency, not a concrete deadline.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_school_work_routine)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_composites_general** (v19/rule/composites-general; rule governing topic_school_work_routine)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_operations_general** (v19/rule/operations-general; rule governing hover)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_supplemental_general** (v19/rule/supplemental-general; rule governing art_itinerary)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; rule governing subject)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- extract | operation | operation-vocabulary | (target: LIST[REF[STRING]], limit: NUMBER) -> LIST[REF[STRING]] | First limit results, preserving order and identity; limit is a nonnegative integer; limit=1 is still a list  ⟵ candidate
- hover | operation | operation-vocabulary | (target: REF[STRING]) -> void | Move pointer cursor over an interactive web element without clicking. target must resolve to a valid element reference. | aliases: mouse_over  ⟵ candidate
- look | operation | operation-vocabulary | (direction: STRING) -> void | Tilt or adjust agent visual camera gaze. direction is up, down, or straight. | aliases: tilt_camera  ⟵ candidate
- search_travel | operation | operation-vocabulary | (target: STRING, constraints?: LIST[TERM], location?: STRING / ATOM[country]) -> LIST[REF[STRING]] | Query travel options meeting supplied constraints. Does not book them.  ⟵ candidate
- select_option | operation | operation-vocabulary | (target: REF[STRING], value: STRING) -> void | Select an option from a dropdown or select menu element. target must be a select element. | aliases: choose_option, choose_dropdown, pick_option  ⟵ candidate
- turn | operation | operation-vocabulary | (direction: STRING) -> void | Rotate agent body/view orientation. direction is typically left, right, or angle. | aliases: rotate, turn_around  ⟵ related to then
- wait | operation | operation-vocabulary | (duration?: NUMBER) -> void | Pause execution for a duration or cycle. duration in seconds or ticks. | aliases: idle, pause  ⟵ candidate
- walk | operation | operation-vocabulary | (destination: STRING / TERM / ATOM[object_label], relation?: STRING) -> void | Locomote towards a target destination or landmark. destination must identify a valid entity or location. | aliases: move_to, go_to, navigate_to  ⟵ related to then

### speech acts

- acknowledge | speech_act | operation-vocabulary | UTTER acknowledge(target: CLAIM / TERM) | Acknowledge receipt/awareness; does not imply agreement.  ⟵ candidate
- ask | speech_act | operation-vocabulary | UTTER ask(target: TERM, or a sufficiently precise topic: STRING / TERM) | Request information/advice; not an assertion of an answer. | aliases: ask, how should  ⟵ candidate
- confirm | speech_act | operation-vocabulary | UTTER confirm(target: CLAIM) | Confirm the proposition; its evidence/status remains explicit.  ⟵ candidate
- correct | speech_act | operation-vocabulary | UTTER correct(target: CLAIM) | Offer corrected content. Actual supersession requires the Conversation revision rules.  ⟵ candidate
- decline | speech_act | operation-vocabulary | UTTER decline(target: TERM) | Decline the represented request/proposal; not negate every proposition within it.  ⟵ candidate
- inform | speech_act | operation-vocabulary | UTTER inform(target: CLAIM) | Present the proposition; preserve its holder/status.  ⟵ candidate
- propose | speech_act | operation-vocabulary | UTTER propose(target: TERM) | Suggest an action/idea; does not record it as performed.  ⟵ candidate
- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ dependency of obligation
- block_evaluation | constructor | TERM block_evaluation(block: STRING / TERM, maturity?: STRING, potential?: STRING, quality?: STRING, rank?: NUMBER, traps?: STRING) -> TERM | Constructs a structured evaluation, categorization, or ranking descriptor for a geological exploration block. | not: an external execution action or generic list sorting operation (use sort) | aliases: block assessment, block ranking, block rating, block categorization  ⟵ candidate
- calculation | constructor | TERM calculation(inputs: LIST[TERM], operation: STRING, result?: TERM) -> TERM | Constructs a descriptive representation of an arithmetic or algorithmic calculation step with inputs, operation identifier, and optional resulting value. | not: an executed runtime action or factual claim of outcome | aliases: math_operation, compute_step  ⟵ candidate
- character_trait | constructor | TERM character_trait(property: STRING, value: STRING / NUMBER) -> TERM | A character attribute | not: Not a claim about a real person  ⟵ candidate
- conjunction | constructor | TERM conjunction(items: LIST[TERM]) -> TERM | All described components apply | not: Does not imply temporal order  ⟵ candidate
- duration | constructor | TERM duration(amount: NUMBER, unit: STRING) -> TERM | Requested elapsed/calendar extent | not: Word/item counts are not time  ⟵ dependency of wait
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ dependency of constraint_exclude_flowery_language
- include | constructor | TERM include(item: STRING / TERM) -> TERM | Require the identified content/item | not: Not permission to invent an instance in a recorded trace  ⟵ dependency of constraint_include_character_attribute_list
- negation | constructor | TERM negation(target: TERM) -> TERM | Constructs a descriptive semantic negation of a target descriptive proposition or condition term. | not: Check's runtime Boolean operator NOT or a speech-act decline | aliases: not, does not, negation, absence of  ⟵ candidate
- obligation | constructor | TERM obligation(actor: STRING / TERM, activity: TERM) -> TERM | Constructs a deontic obligation description requiring an actor to perform an activity. actor and activity specified. | aliases: duty, mandatory_activity  ⟵ candidate
- outshines | constructor | TERM outshines(brighter: STRING / TERM, dimmer: STRING / TERM) -> TERM | Constructs a description of relative visual brightness where a brighter light source overpowers the perceived brightness of a dimmer object. | not: an absolute numeric brightness measurement | aliases: outshines, overpowers brightness, drowns out light  ⟵ candidate
- regression_case | constructor | TERM regression_case(framework: STRING / ATOM[platform_label], modifier: STRING, relation: STRING) -> TERM | A regression scenario specifying affected framework, condition and relation | not: Does not invent a passing test or exact implementation  ⟵ candidate
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ candidate
- similarity | constructor | TERM similarity(target: STRING / TERM, dimension?: STRING / TERM) -> TERM | Constructs a descriptor representing comparative closeness or similarity to a target along a given dimension. | not: spatial proximity (use rank_distance or next_to) or an assertion of exact identity (use identity) | aliases: closest_to, similar_to, resembles  ⟵ candidate
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ candidate
- well_wishes | constructor | TERM well_wishes(recipient?: STRING / TERM, sentiment?: STRING) -> TERM | Constructs a conversational discourse term representing well-wishes, good luck expressions, or parting encouragement. | not: a salutation greeting (use greeting) or apology (use apologize) | aliases: good_luck, best_wishes, encouragement  ⟵ candidate

### composites

- constraint_beginner | composite | constraint-value | TERM constraint_beginner() -> TERM | Targeted at beginners. | = requirement(property="audience_expertise", value="beginner")  ⟵ candidate
- constraint_budget_limited | composite | constraint-value | TERM constraint_budget_limited() -> TERM | Limited budget. | = requirement(property="budget_limited", value=TRUE)  ⟵ candidate
- constraint_comprehensive | composite | constraint-value | TERM constraint_comprehensive() -> TERM | Must be comprehensive. | = requirement(property="comprehensive", value=TRUE)  ⟵ candidate
- constraint_exclude_flowery_language | composite | constraint-value | TERM constraint_exclude_flowery_language() -> TERM | Avoid flowery language. | = exclude(item="flowery_language")  ⟵ candidate
- constraint_exclude_liberation_theme | composite | constraint-value | TERM constraint_exclude_liberation_theme() -> TERM | Avoid liberation theme. | = exclude(item="liberation_theme")  ⟵ candidate
- constraint_include_character_attribute_list | composite | constraint-value | TERM constraint_include_character_attribute_list() -> TERM | Include character attributes. | = include(item="character_attribute_list")  ⟵ candidate
- constraint_realistic | composite | constraint-value | TERM constraint_realistic() -> TERM | Must be realistic. | = requirement(property="realistic", value=TRUE)  ⟵ candidate
- constraint_respectful | composite | constraint-value | TERM constraint_respectful() -> TERM | Must be respectful. | = requirement(property="respectful", value=TRUE)  ⟵ candidate
- constraint_single_choice | composite | constraint-value | TERM constraint_single_choice() -> TERM | Must pick a single choice. | = requirement(property="choice_count", value=1)  ⟵ candidate
- event_camper_in_sludge_pit | composite | event-value | TERM event_camper_in_sludge_pit() -> TERM | Campers interacting in a sludge pit. | = activity(verb="interact", actor="campers", location="sludge_pit")  ⟵ candidate
- topic_school_work_routine | composite | topic-value | TERM topic_school_work_routine() -> TERM | School and work routine. | = subject(kind="routine", qualifier=conjunction(items=[subject(kind="school"), subject(kind="work")]))  ⟵ candidate

### claim relations

- associated_with | claim_relation | CLAIM associated_with(subject: STRING / TERM, concept: STRING / TERM) | Asserts a cultural, semantic, or historical association between a subject and concept. association claim. | aliases: linked_to, correlated_with  ⟵ candidate
- attribute_claim | claim_relation | CLAIM attribute_claim(subject: STRING / TERM / ATOM[platform_label], property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) | Asserts that a subject possesses a named property evaluated to a specific primitive or structured value. general property attribution claim. | aliases: property_value, word_property, has_property, property attribution  ⟵ related to statement
- causes | claim_relation | CLAIM causes(cause: CLAIM / TERM, effect: CLAIM) | Asserts a direct causal relationship producing an effect proposition. causal assertion. | aliases: produces  ⟵ candidate
- comfortable | claim_relation | CLAIM comfortable(person: TERM, value: BOOL) | Asserts whether a person or animal is comfortable in a situation. affective/state claim. | aliases: is_comfortable  ⟵ candidate
- considered | claim_relation | CLAIM considered(subject: TERM) | Asserts that an agent or speaker evaluated or entertained a specific candidate term or concept. subject is the evaluated term. | aliases: evaluated, weighed  ⟵ candidate
- controversial | claim_relation | CLAIM controversial(subject: STRING / TERM) | Asserts that a topic, policy, or practice is the subject of public debate or controversy. evaluative debate claim. | aliases: debated, disputed  ⟵ candidate
- enables | claim_relation | CLAIM enables(condition: TERM / CLAIM, outcome: TERM / CLAIM) | Asserts that an enabling condition or capability facilitates an outcome. enabling condition. | aliases: facilitates, allows  ⟵ candidate
- example_of | claim_relation | CLAIM example_of(example: TERM, concept: TERM) | Asserts that an instance or term exemplifies a general concept, pattern, or category. example and concept are descriptive terms. | aliases: exemplifies, instance_of  ⟵ candidate
- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ candidate
- has_state | claim_relation | CLAIM has_state(subject: TERM, state: STRING) | Asserts that an entity is currently in a physical, thermal, or operational state. state must be a valid state descriptor string. | aliases: in_state, state_is  ⟵ related to statement
- has_style | claim_relation | CLAIM has_style(target: CLAIM / EVENT / TERM, value: TERM / STRING) | Asserts that an artifact, utterance, or action possesses a designated style. style qualifier. | aliases: style_is  ⟵ candidate
- important | claim_relation | CLAIM important(target: TERM) | Asserts that a concept, activity, or condition is important or significant. evaluative importance claim. | aliases: significant  ⟵ candidate
- leads_to | claim_relation | CLAIM leads_to(cause: TERM, effect: TERM) | Asserts a conceptual consequence or progression from cause to effect. progression relation. | aliases: results_in  ⟵ candidate
- menu_works | claim_relation | CLAIM menu_works(property: STRING) | Asserts that a menu or recipe plan satisfies an operational criterion. menu evaluation. | aliases: menu_satisfies  ⟵ candidate
- occurred | claim_relation | CLAIM occurred(activity: TERM) | Asserts that an event, action, or activity took place in the past. past occurrence claim. | aliases: happened  ⟵ candidate
- occurred_recently | claim_relation | CLAIM occurred_recently(target: CLAIM) | Asserts temporal recency of an asserted occurrence or claim. temporal recency qualifier. | aliases: recently_happened  ⟵ candidate
- ongoing | claim_relation | CLAIM ongoing(target: TERM) | Asserts that a conflict, process, or initiative is actively ongoing. temporal aspect claim. | aliases: in_progress  ⟵ candidate
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ candidate
- possesses | claim_relation | CLAIM possesses(subject: STRING / TERM, item: TERM, value: BOOL) | Asserts whether a subject possesses or lacks a stated property, capability, or entity. possession assertion with boolean polarity. | aliases: holds_property  ⟵ candidate
- prohibited | claim_relation | CLAIM prohibited(subject: STRING / TERM, location: STRING / TERM, condition?: STRING / TERM) | Asserts that a subject is prohibited from a location or activity under specified conditions. deontic prohibition claim. | aliases: forbidden, banned_from  ⟵ related to obligation
- proposed_policy | claim_relation | CLAIM proposed_policy(policy: TERM, requirements: LIST[TERM]) | Asserts that a proposed policy framework comprises the specified requirement terms. policy must be a policy term. | aliases: policy_proposal  ⟵ related to obligation
- recommended | claim_relation | CLAIM recommended(target: TERM / CLAIM) | Asserts an advisory recommendation that an activity or measure is advisable. advisory normative claim. | aliases: advisable  ⟵ candidate
- spatial_state | claim_relation | CLAIM spatial_state(relation: STRING, object: TERM, reference: TERM) | Asserts an observed spatial configuration between an object and a reference landmark. relation must specify spatial configuration. | aliases: placed_at, located_at  ⟵ related to statement
- statement | claim_relation | CLAIM statement(fact: TERM) | Foundational claim relation converting any descriptive TERM into an attributed, truth-evaluated assertion. universal fact assertion. | aliases: assert_fact, fact_claim, claim_statement  ⟵ candidate
- unaware | claim_relation | CLAIM unaware(person: STRING / TERM, topic: STRING / TERM) | Asserts epistemic lack of awareness regarding a topic, fact, or event. epistemic state. | aliases: ignorant_of  ⟵ candidate
- user_preference | claim_relation | CLAIM user_preference(constraints: TERM) | Asserts a user's stated preference constraints or dietary requirements. user constraint assertion. | aliases: stated_preference  ⟵ candidate
- varies_with | claim_relation | CLAIM varies_with(target: CLAIM / TERM, condition: STRING / TERM) | Asserts that a target claim or term varies contingently depending on specified conditions, external factors, or behavioral habits. | not: geographic variation only (use varies_by_location) | aliases: depends_on, contingent_on  ⟵ candidate

### links

- contrast | link | LINK contrast(first: CLAIM, second: CLAIM) | Expresses rhetorical qualification, opposition, or contrast between two claims. link between claims. | aliases: qualification, however  ⟵ candidate
- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ candidate
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ candidate
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ candidate
- then | link | LINK then(previous: EVENT, next: EVENT) | Represents temporal sequence and succession between two events where next follows previous. previous and next must be event terms. | aliases: followed_by, after_which  ⟵ candidate

### values

- art_itinerary | value | artifact-value | An ordered travel plan; GENERATE returns STRING, not booked travel  ⟵ candidate
- art_structured_report | value | artifact-value | Headed/structured report.  ⟵ candidate
- dom_ovr | value | descriptive-value | One-versus-rest domain concept.  ⟵ candidate
- dom_pain | value | descriptive-value | Pain domain concept. | aliases: pain  ⟵ candidate
- dom_safari | value | descriptive-value | Safari domain concept. | aliases: safari  ⟵ candidate
- tattoos | value | descriptive-value | Descriptive concept of tattoos in cultural and social contexts. | aliases: tattoos  ⟵ candidate
- unit_day | value | duration-unit-value | Day. | aliases: days  ⟵ candidate
- apple | value | entity-name | An apple fruit item, typically an ingredient or interactive food object. | not: food_label::tomato or other fruits/vegetables | aliases: apple, apples, red apple, green apple, apple slice  ⟵ candidate
- bowtie | value | entity-name | Item or prop in joke/creative context: bowtie. | aliases: bowtie  ⟵ candidate
- bread | value | entity-name | A bread loaf or slice food object. | aliases: bread  ⟵ candidate
- caddy | value | entity-name | A portable storage caddy, organizer box, or supply tote for carrying and organizing handheld tools and supplies. | not: cabinet (a stationary furniture cupboard) or safe (a secure metal lockbox) | aliases: caddy, supply caddy, wrapping caddy, tool caddy, organizer caddy, supply tote  ⟵ candidate
- chair | value | entity-name | A chair furniture seat with a backrest. | not: object_label::armchair (specifically an object_label::armchair with side armrests) or object_label::sofa | aliases: chair, seat  ⟵ candidate
- desk | value | entity-name | A work desk furniture surface. | aliases: desk  ⟵ candidate
- dog | value | entity-name | Animal entity: dog. | not: animal_label::cat or animal_label::donkey | aliases: dog, dogs, canine, pup, puppy  ⟵ candidate
- earth | value | entity-name | The planet Earth as an astronomical celestial body. | not: soil, ground surface, or electrical grounding | aliases: earth, the earth, planet earth, Earth  ⟵ candidate
- entity_cake | value | entity-name | Event planning item or menu category: entity_cake. | aliases: entity_cake  ⟵ candidate
- entity_desserts | value | entity-name | Event planning item or menu category: entity_desserts. | aliases: entity_desserts  ⟵ candidate
- entity_mains | value | entity-name | Event planning item or menu category: entity_mains. | aliases: entity_mains  ⟵ candidate
- entity_order_vs_assemble_plan | value | entity-name | Event planning item or menu category: entity_order_vs_assemble_plan. | aliases: entity_order_vs_assemble_plan  ⟵ candidate
- figurine | value | entity-name | A small carved, molded, or sculpted decorative statuette object. | not: character (a fictional persona) or captioned_figure (a document figure/photo) | aliases: figurine, statuette, statue, small statue, sculptural figure, miniature figure  ⟵ candidate
- fridge | value | entity-name | A refrigerator cooling appliance. | aliases: fridge  ⟵ candidate
- laptop | value | entity-name | A portable laptop computer physical object. | not: topic_macbook_pro_2017 (a generation topic label) | aliases: laptop, laptop computer, notebook  ⟵ candidate
- lettuce | value | entity-name | A head of lettuce or leafy green vegetable food item. | not: food_label::tomato or food_label::potato (other vegetable items) | aliases: lettuce, head of lettuce, salad greens  ⟵ candidate
- mattress | value | entity-name | A mattress cushion or sleeping surface object. | not: bed (a bed furniture surface or frame) or object_label::pillow | aliases: mattress, mattresses  ⟵ candidate
- meat | value | entity-name | Food item: meat or beef. | not: animal_label::tuna or animal_label::fish (specific aquatic foods) | aliases: meat, beef  ⟵ candidate
- mittens | value | entity-name | Item or prop in joke/creative context: mittens. | aliases: mittens  ⟵ candidate
- moon | value | entity-name | Earth's natural celestial satellite. | not: an artificial satellite or other planetary moon | aliases: moon, the moon, Luna  ⟵ candidate
- oak_chips | value | entity-name | Oak wood pieces or barrels used for wine aging and flavor extraction. | not: grape_tannin or structural chemical additives | aliases: oak chips, oak pieces, oak barrels  ⟵ candidate
- pan | value | entity-name | A metal cooking vessel, frying pan, skillet, saucepan, or pot cookware item used for preparing, heating, or holding food. | not: bowl (deep concave vessel) or plate (shallow flat dining dish) | aliases: pan, frying pan, skillet, saucepan, pot  ⟵ candidate
- pen | value | entity-name | A writing instrument. | aliases: pen  ⟵ candidate
- pencil | value | entity-name | A pencil writing instrument. | aliases: pencil  ⟵ candidate
- piano | value | entity-name | A piano musical instrument or large furniture object. | not: topic_classical_piano or topic_jazz_piano (music genre topics) | aliases: piano, grand piano, upright piano, keyboard  ⟵ candidate
- resource_chiller | value | entity-name | Canonical abstract chilling resource when no particular appliance is named.  ⟵ candidate
- spatula | value | entity-name | A kitchen utensil with a broad, flat, and flexible blade used for lifting, flipping, or spreading food. | not: knife (cutting utensil) or spoon (scooping utensil) | aliases: spatula, turner, flipper  ⟵ candidate
- spoon | value | entity-name | An eating or cooking utensil. | aliases: spoon  ⟵ candidate
- locale_de | value | locale-value | German language or locale descriptor. | not: other language locales (such as locale_en_us or locale_fr) or country entity (country::DE) | aliases: German, german, Deutsch, de, de-DE  ⟵ candidate
- locale_hi_en | value | locale-value | Hinglish (Hindi-English mix). | aliases: hinglish  ⟵ candidate
- wall | value | location-name | A room boundary wall surface. | aliases: wall  ⟵ candidate
- metric_order_late | value | metric-value | Whether an order is late. | aliases: order is late, delayed  ⟵ candidate
- size_large | value | product-attribute-value | Large size. | aliases: large, L  ⟵ candidate
- size_medium | value | product-attribute-value | Medium size. | aliases: medium, M  ⟵ candidate
- size_queen | value | product-attribute-value | Queen-size dimension classification for beds, mattresses, and bedding. | not: size_large (generic large apparel/goods size) or size_king | aliases: queen, queen size, Queen  ⟵ candidate
- size_small | value | product-attribute-value | Small size. | aliases: small, S  ⟵ candidate
- size_tall | value | product-attribute-value | Tall relative vertical dimension qualifier. | aliases: size_tall  ⟵ candidate
- role_colleague | value | recipient-value | A coworker of the user. | aliases: my colleague, coworker  ⟵ candidate
- role_daughter | value | recipient-value | Daughter participant role in family or travel context. | not: role_sister, role_mother, or generic role_kids | aliases: daughter, my daughter  ⟵ candidate
- role_friend | value | recipient-value | A friend of the user. | aliases: my friend  ⟵ candidate
- role_son | value | recipient-value | Son participant role in family or travel context. | not: role_daughter, role_sister, role_mother, or generic role_kids | aliases: son, my son  ⟵ candidate
- cat_game | value | search-value | Category: video game.  ⟵ candidate
- shape_oval | value | shape-value | Oval. | aliases: oval  ⟵ candidate
- shape_rectangular | value | shape-value | Rectangular. | aliases: rectangular, rectangle  ⟵ candidate
- shape_round | value | shape-value | Circular/round. | aliases: round, circular  ⟵ candidate
- shape_square | value | shape-value | Square. | aliases: square  ⟵ candidate
- shape_triangular | value | shape-value | Triangular. | aliases: triangular, triangle  ⟵ candidate
- between | value | spatial-relation | Positioned between or in the middle of reference entities. | not: next_to or in_front_of | aliases: between, in the middle of, middle of, center of  ⟵ candidate
- in_front_of | value | spatial-relation | Positioned in front of. | aliases: in front of  ⟵ candidate
- left_of | value | spatial-relation | To the left of. | aliases: left of  ⟵ candidate
- next_to | value | spatial-relation | Adjacent to. | aliases: beside  ⟵ candidate
- on | value | spatial-relation | Resting atop. | aliases: on top of  ⟵ candidate
- right_of | value | spatial-relation | To the right of. | aliases: right of  ⟵ candidate
- state_dirty | value | state-value | Dirty condition. | aliases: dirty  ⟵ candidate
- state_sliced | value | state-value | The condition of being sliced or cut into thin pieces. | not: the operation slice itself | aliases: sliced, slice, chopped, cut  ⟵ candidate
- style_catchy | value | style-value | Catchy, attention-grabbing style. | aliases: catchy  ⟵ candidate
- style_narrative | value | style-value | Story-like narrative style. | aliases: narrative, story-style  ⟵ candidate
- style_persuasive | value | style-value | Persuasive/argumentative style. | aliases: persuasive  ⟵ candidate
- tone_empathetic | value | tone-value | Conveys empathy/understanding. | aliases: sympathetically  ⟵ candidate
- tone_silly | value | tone-value | Playful, lighthearted, or silly conversational tone. | aliases: silly  ⟵ candidate
- topic_baldurs_gate_3 | value | topic-value | Baldur's Gate 3.  ⟵ candidate
- topic_classical_piano | value | topic-value | Classical piano.  ⟵ candidate
- topic_macbook_pro_2017 | value | topic-value | MacBook Pro 2017.  ⟵ candidate
- topic_pickup_lines | value | topic-value | Pickup lines.  ⟵ candidate
- topic_spider_man_2 | value | topic-value | Marvel's Spider-Man 2.  ⟵ candidate
