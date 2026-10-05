# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 51 needs (decomposition: llm), 132 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | constraint | t1:s1 | Participants work from 9 to 5 local time on weekdays | `cat_limited_time_offers`, `unit_week`, `unit_day`, `unit_hour`, `unit_minute`, `time_point`, `daytime`, `topic_school_work_routine`, `clock`, `unit_month`, `metric_response_time`, `minimum_per_period` |
| n2 | action | t1:s2 | Schedule a meeting for Olivia, Amelia, Victoria, Karen, Rachel, and Charlotte | `minimum_per_period`, `group_size`, `obligation`, `format_numbered_list`, `role_sister`, `search_travel`, `sequence`, `entity_grocery_list`, `entity_recipes`, `calculation`, `propose`, `entity_appetizers` |
| n3 | temporal | t1:s2 | The meeting must take place some time this week | `unit_week`*, `cat_limited_time_offers`, `metric_response_time`, `prep_time`, `time_point`, `unit_day`, `unit_minute`, `daytime`, `nighttime`, `metric_order_late`, `topic_politics`, `group_size` |
| n4 | constraint | t1:s3 | Olivia's weekly schedule constraints | `constraint_budget_limited`, `requirement`*, `rule_category_constraint_value`, `unit_week`, `unit_hour`, `cat_limited_time_offers`, `unit_month`, `unit_day`, `topic_school_work_routine`, `sequence`, `rule_category_duration_unit_value`, `unit_sentence` |
| n5 | constraint | t1:s4 | Olivia's Monday schedule | `unit_week`, `topic_school_work_routine`, `unit_day`, `sequence`, `prep_time`, `unit_month`, `constraint_budget_limited`, `entity_recipes`, `constraint_exclude_flowery_language`, `entity_grocery_list`, `wait`, `entity_condensed_grocery_list` |
| n6 | constraint | t1:s5 | Olivia's Tuesday schedule | `unit_week`, `sequence`, `unit_month`, `prep_time`, `constraint_budget_limited`, `entity_order_vs_assemble_plan`, `topic_school_work_routine`, `art_plan`, `role_sister`, `constraint_exclude_flowery_language`, `entity_recipes`, `cat_limited_time_offers` |
| n7 | constraint | t1:s6 | Olivia's Wednesday schedule | `unit_week`, `sequence`, `prep_time`, `entity_recipes`, `entity_grocery_list`, `entity_order_vs_assemble_plan`, `time_point`, `constraint_budget_limited`, `entity_appetizers`, `constraint_exclude_flowery_language`, `cat_limited_time_offers`, `art_plan` |
| n8 | constraint | t1:s7 | Olivia's Thursday schedule | `unit_week`, `unit_month`, `entity_recipes`, `entity_grocery_list`, `prep_time`, `time_point`, `constraint_budget_limited`, `rule_category_duration_unit_value`, `entity_appetizers`, `unit_day`, `entity_condensed_grocery_list`, `constraint_exclude_flowery_language` |
| n9 | constraint | t1:s8 | Olivia's Friday schedule | `unit_week`, `unit_month`, `unit_day`, `time_point`, `entity_recipes`, `entity_grocery_list`, `prep_time`, `constraint_budget_limited`, `rule_category_duration_unit_value`, `constraint_exclude_flowery_language`, `entity_condensed_grocery_list`, `entity_appetizers` |
| n10 | constraint | t1:s9 | Amelia's weekly schedule constraints | `constraint_budget_limited`, `requirement`*, `rule_category_constraint_value`, `unit_week`, `unit_hour`, `unit_day`, `unit_month`, `cat_limited_time_offers`, `unit_minute`, `unit_sentence`, `topic_school_work_routine`, `sequence` |
| n11 | constraint | t1:s10 | Amelia's Monday schedule | `unit_week`, `unit_day`, `topic_school_work_routine`, `unit_month`, `entity_order_vs_assemble_plan`, `sequence`, `daytime`, `constraint_budget_limited`, `unit_hour`, `constraint_exclude_flowery_language`, `entity_recipes`, `prep_time` |
| n12 | constraint | t1:s11 | Amelia's Tuesday schedule | `unit_week`, `entity_order_vs_assemble_plan`, `unit_month`, `role_sister`, `sequence`, `constraint_budget_limited`, `constraint_exclude_flowery_language`, `prep_time`, `art_plan`, `entity_recipes`, `topic_school_work_routine`, `cat_limited_time_offers` |
| n13 | constraint | t1:s12 | Amelia's Wednesday schedule | `unit_week`, `entity_order_vs_assemble_plan`, `sequence`, `entity_recipes`, `entity_assembly_tips`, `constraint_budget_limited`, `role_sister`, `constraint_exclude_flowery_language`, `unit_month`, `prep_time`, `entity_appetizers`, `entity_grocery_list` |
| n14 | constraint | t1:s13 | Amelia's Thursday schedule | `unit_week`, `unit_month`, `entity_recipes`, `unit_day`, `entity_order_vs_assemble_plan`, `rule_category_duration_unit_value`, `constraint_budget_limited`, `entity_grocery_list`, `constraint_exclude_flowery_language`, `entity_assembly_tips`, `prep_time`, `role_sister` |
| n15 | constraint | t1:s14 | Amelia's Friday schedule | `unit_week`, `unit_day`, `unit_month`, `entity_recipes`, `constraint_budget_limited`, `entity_grocery_list`, `rule_category_duration_unit_value`, `constraint_exclude_flowery_language`, `role_daughter`, `art_itinerary`, `entity_order_vs_assemble_plan`, `entity_assembly_tips` |
| n16 | constraint | t1:s15 | Victoria's weekly schedule constraints | `constraint_budget_limited`, `requirement`*, `unit_week`, `unit_hour`, `unit_day`, `cat_limited_time_offers`, `unit_minute`, `unit_month`, `time_point`, `daytime`, `metric_uptime`, `rule_category_duration_unit_value` |
| n17 | constraint | t1:s16 | Victoria's Monday schedule | `unit_week`, `unit_day`, `daytime`, `time_point`, `unit_hour`, `constraint_budget_limited`, `prep_time`, `nighttime`, `rule_category_tone_value`, `wait`, `clock`, `unit_month` |
| n18 | constraint | t1:s17 | Victoria's Tuesday schedule | `cat_limited_time_offers`, `unit_week`, `time_point`, `unit_day`, `daytime`, `metric_response_time`, `unit_month`, `clock`, `prep_time`, `rule_category_tone_value`, `constraint_budget_limited`, `sequence` |
| n19 | constraint | t1:s18 | Victoria's Wednesday schedule | `cat_limited_time_offers`, `unit_week`, `time_point`, `unit_day`, `entity_grocery_list`, `metric_order_late`, `sequence`, `metric_response_time`, `prep_time`, `constraint_budget_limited`, `rule_category_tone_value`, `wait` |
| n20 | constraint | t1:s19 | Victoria's Thursday schedule | `unit_week`, `time_point`, `unit_day`, `rule_category_duration_unit_value`, `unit_hour`, `metric_response_time`, `constraint_budget_limited`, `unit_month`, `prep_time`, `entity_grocery_list`, `unit_minute`, `rule_category_tone_value` |
| n21 | constraint | t1:s20 | Victoria's Friday schedule | `cat_limited_time_offers`, `unit_week`, `unit_day`, `time_point`, `unit_minute`, `unit_hour`, `unit_month`, `rule_category_duration_unit_value`, `entity_grocery_list`, `daytime`, `metric_response_time`, `constraint_budget_limited` |
| n22 | constraint | t1:s21 | Karen's weekly schedule constraints | `constraint_budget_limited`, `requirement`*, `unit_week`, `unit_hour`, `cat_limited_time_offers`, `unit_day`, `unit_minute`, `unit_month`, `metric_uptime`, `format_newsletter`, `rule_category_tone_value`, `example_b_preserve_the_class_and_amount_of_an_itinerary_constraint` |
| n23 | constraint | t1:s22 | Karen's Monday schedule | `unit_week`, `unit_day`, `format_newsletter`, `daytime`, `topic_school_work_routine`, `rule_category_tone_value`, `clock`, `wait`, `constraint_budget_limited`, `metric_response_time`, `prep_time`, `constraint_exclude_flowery_language` |
| n24 | constraint | t1:s23 | Karen's Tuesday schedule | `unit_week`, `metric_response_time`, `rule_category_tone_value`, `format_newsletter`, `clock`, `sequence`, `constraint_budget_limited`, `wait`, `prep_time`, `constraint_exclude_flowery_language`, `cat_limited_time_offers`, `role_sister` |
| n25 | constraint | t1:s24 | Karen's Wednesday schedule | `unit_week`, `format_newsletter`, `sequence`, `rule_category_tone_value`, `metric_uptime`, `constraint_budget_limited`, `wait`, `time_point`, `metric_response_time`, `prep_time`, `clock`, `metric_order_late` |
| n26 | constraint | t1:s25 | Karen's Thursday schedule | `unit_week`, `format_newsletter`, `clock`, `metric_response_time`, `unit_day`, `rule_category_tone_value`, `constraint_budget_limited`, `time_point`, `metric_order_late`, `prep_time`, `rule_category_duration_unit_value`, `constraint_exclude_flowery_language` |
| n27 | constraint | t1:s26 | Karen's Friday schedule | `cat_limited_time_offers`, `unit_week`, `unit_day`, `clock`, `format_newsletter`, `time_point`, `metric_response_time`, `rule_category_tone_value`, `rule_category_duration_unit_value`, `constraint_budget_limited`, `metric_uptime`, `prep_time` |
| n28 | constraint | t1:s27 | Rachel's weekly schedule constraints | `requirement`*, `unit_week`, `unit_hour`, `unit_day`, `cat_limited_time_offers`, `sequence`, `unit_minute`, `topic_school_work_routine`, `unit_month`, `constraint_budget_limited`, `unit_sentence`, `metric_uptime` |
| n29 | constraint | t1:s28 | Rachel's Monday schedule | `cat_limited_time_offers`, `unit_week`, `unit_day`, `daytime`, `sequence`, `topic_school_work_routine`, `wait`, `format_newsletter`, `constraint_budget_limited`, `rule_category_tone_value`, `topic_politics`, `constraint_exclude_flowery_language` |
| n30 | constraint | t1:s29 | Rachel's Tuesday schedule | `cat_limited_time_offers`, `unit_week`, `sequence`, `unit_day`, `topic_school_work_routine`, `clock`, `wait`, `role_sister`, `rule_category_tone_value`, `constraint_budget_limited`, `constraint_exclude_flowery_language`, `art_plan` |
| n31 | constraint | t1:s30 | Rachel's Wednesday schedule | `cat_limited_time_offers`, `unit_week`, `sequence`, `time_point`, `topic_school_work_routine`, `unit_day`, `wait`, `rule_category_tone_value`, `topic_politics`, `constraint_budget_limited`, `entity_grocery_list`, `constraint_exclude_flowery_language` |
| n32 | constraint | t1:s31 | Rachel's Thursday schedule | `cat_limited_time_offers`, `unit_week`, `unit_day`, `sequence`, `clock`, `time_point`, `entity_grocery_list`, `rule_category_tone_value`, `wait`, `entity_recipes`, `constraint_budget_limited`, `rule_category_duration_unit_value` |
| n33 | constraint | t1:s32 | Rachel's Friday schedule | `cat_limited_time_offers`, `unit_week`, `unit_day`, `clock`, `time_point`, `entity_grocery_list`, `daytime`, `wait`, `constraint_budget_limited`, `rule_category_tone_value`, `rule_category_duration_unit_value`, `constraint_exclude_flowery_language` |
| n34 | constraint | t1:s33 | Charlotte's weekly schedule constraints | `requirement`*, `unit_week`, `unit_hour`, `cat_limited_time_offers`, `unit_day`, `clock`, `time_point`, `unit_month`, `unit_minute`, `daytime`, `sequence`, `constraint_budget_limited` |
| n35 | constraint | t1:s34 | Charlotte's Monday schedule | `cat_limited_time_offers`, `unit_week`, `daytime`, `sequence`, `time_point`, `unit_day`, `clock`, `topic_school_work_routine`, `wait`, `nighttime`, `constraint_budget_limited`, `prep_time` |
| n36 | constraint | t1:s35 | Charlotte's Tuesday schedule | `cat_limited_time_offers`, `unit_week`, `time_point`, `sequence`, `clock`, `daytime`, `unit_day`, `eastern_cape`, `wait`, `constraint_budget_limited`, `prep_time`, `rule_category_tone_value` |
| n37 | constraint | t1:s36 | Charlotte's Wednesday schedule | `cat_limited_time_offers`, `unit_week`, `time_point`, `sequence`, `clock`, `eastern_cape`, `nighttime`, `cuisine_pizza`, `wait`, `prep_time`, `constraint_budget_limited`, `rule_category_tone_value` |
| n38 | constraint | t1:s37 | Charlotte's Thursday schedule | `cat_limited_time_offers`, `unit_week`, `time_point`, `clock`, `unit_day`, `sequence`, `nighttime`, `daytime`, `unit_month`, `eastern_cape`, `constraint_budget_limited`, `rule_category_tone_value` |
| n39 | constraint | t1:s38 | Charlotte's Friday schedule | `cat_limited_time_offers`, `unit_week`, `time_point`, `unit_day`, `clock`, `daytime`, `nighttime`, `unit_month`, `eastern_cape`, `entity_grocery_list`, `constraint_budget_limited`, `prep_time` |
| n40 | constraint | t1:s39 | Olivia can miss at most the last 10 minutes of the meeting | `unit_minute`*, `at_most`*, `metric_order_late`, `wait`, `cat_limited_time_offers`, `metric_response_time`, `duration`, `rule_category_duration_unit_value`, `role_sister`, `constraint_exclude_flowery_language`, `example_b_preserve_the_class_and_amount_of_an_itinerary_constraint`, `constraint_budget_limited` |
| n41 | constraint | t1:s40 | Amelia is in a timezone one hour ahead of other participants | `unit_hour`*, `clock`, `unit_minute`, `time_point`, `unit_day`, `metric_response_time`, `daytime`, `role_sister`, `nighttime`, `time_horizon`, `role_daughter`, `rule_category_duration_unit_value` |
| n42 | constraint | t1:s41 | Victoria needs a lunch break on Wednesday from 12:30 to 13:00 | `night_stand`, `time_point`, `constraint_budget_limited`, `nighttime`, `cuisine_mediterranean`, `bread`, `temporal_context`, `daytime`, `plate`, `constraint_include_character_attribute_list`, `clock`, `constraint_respectful` |
| n43 | constraint | t1:s42 | Karen can miss at most 10 minutes of the meeting | `unit_minute`*, `at_most`*, `unit_week`, `metric_response_time`, `cat_limited_time_offers`, `wait`, `metric_order_late`, `format_newsletter`, `time_horizon`, `role_sister`, `rule_category_tone_value`, `constraint_exclude_flowery_language` |
| n44 | constraint | t1:s43 | Rachel needs at least 10 minutes of free time before the meeting within 9am-5pm | `unit_minute`*, `cat_limited_time_offers`, `prep_time`, `at_least`*, `unit_hour`, `unit_week`, `unit_day`, `clock`, `wait`, `time_point`, `unit_sentence`, `daytime` |
| n45 | constraint | t1:s44 | Charlotte can clear morning schedule from 9:00 to 9:45 daily if needed | `maximum_between_stops`, `daytime`, `unit_hour`, `clock`, `nighttime`, `unit_day`, `unit_week`, `time_point`, `unit_minute`, `wait`, `prep_time`, `constraint_budget_limited` |
| n46 | constraint | t1:s45 | Meeting must start on the hour or half hour | `unit_hour`*, `clock`, `unit_week`, `unit_minute`, `unit_day`, `minimum_per_period`, `time_point`, `daytime`, `unit_month`, `prep_time`, `wait`, `desk` |
| n47 | object | t1:s45 | X, the length of the longest meeting in minutes | `unit_minute`*, `unit_week`, `unit_hour`, `unit_day`, `rule_category_duration_unit_value`, `wait`, `unit_month`, `minimum_per_period`, `cat_limited_time_offers`, `metric_response_time`, `duration`, `unit_second` |
| n48 | object | t1:s46 | Y, the number of possible options for the longest meeting | `format_numbered_list`, `unit_week`, `unit_minute`, `minimum_per_period`, `unit_hour`, `cat_limited_time_offers`, `rule_category_duration_unit_value`, `rank_distance`, `correct`, `dir_asc`, `dir_desc`, `duration` |
| n49 | action | t1:s47 | Compute X and Y | `calculation`, `wait`, `sequence`, `maximum_between_stops`, `duration`, `unit_second`, `obligation`, `at_most`, `unit_year`, `extract`, `at_least`, `conjunction` |
| n50 | constraint | t1:s47 | Report X and Y separated by a comma | `format_structured_report`*, `format_numbered_list`, `unit_sentence`, `sequence`, `format_newsletter`, `constraint_budget_limited`, `constraint_exclude_flowery_language`, `document_section`, `in_front_of`, `left_of`, `respond`, `constraint_exclude_liberation_theme` |
| n51 | constraint | t1:s48 | If X is 0, report 0, 0 | `extract`, `maximum_between_stops`, `format_structured_report`*, `constraint_budget_limited`, `calculation`, `constraint_exclude_flowery_language`, `tone_neutral`, `measure`, `assert_multinomial_scorer`, `unit_item`, `constraint_exclude_liberation_theme`, `unit_gram` |

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

- search_travel.location → country
- pick_up.target → object_label, food_label
- pick_up.source → object_label
- pick_up.color → color_label
- place.destination → object_label
- place.location → object_label
- requirement.value → platform_label
- measure.unit → currency
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

**rule_recording_signatures** (v19/rule/recording-signatures; rule governing search_travel)

RECORD ACTION uses the operation signature with REF[STRING] → TERM and LIST[REF[STRING]] → LIST[TERM]; other types/categories stay unchanged. Return EVENT, never the runtime result. Record actual outputs as attributed CLAIMs. Do not infer missing resources.

**rule_speech_acts_general** (v19/rule/speech-acts-general; rule governing propose)

UTTER-only, void, with the spec's speech attributes and LIST[TERM] constraints. No result binding. Literal content cannot replace required semantic arguments for structured coverage.

**rule_structural_constructs** (v19/rule/structural-constructs; core)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; rule governing prep_time)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_attributes_and_generate** (v19/rule/attributes-and-generate; rule governing art_plan)

Attribute entries name arguments; legality/types come from each operation, not global membership. GENERATE uses the spec's core fields; retained artifact profiles return STRING. Numeric/list results need explicit profiles. Legacy itinerary fields expand to TERM constraints: duration/duration_unit → duration(amount,unit); stop_min_per_day/stop_requirement → minimum_per_period(class,count,period=unit_day), never an inferred temple class; max_walk_duration/unit → maximum_between_stops(activity="walk",amount,unit). No legacy shorthand is enabled. Old events/character_properties/transformations become explicitly scoped TERM constraints. Message purpose is TERM, not send_email.content: GENERATE exact STRING content, then send. Report opaque fallback separately.

**rule_category_artifact_value** (v19/rule/category/artifact-value; rule governing art_plan)

STRING artifact class for GENERATE.target. art_story says what kind of artifact to produce, not what occurs in its plot.

**rule_category_code_value** (v19/rule/category/code-value; rule governing assert_multinomial_scorer)

path_/sym_ remain STRING identities; migrated chg_/assert_ are TERM constructors. Do not recover an exact file path by guessing from underscores.

**rule_category_constraint_value** (v19/rule/category/constraint-value; candidate)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_content_value** (v19/rule/category/content-value; rule governing content_kyoto_itinerary)

Existing compounds become the constructors in Section 5. Their outputs go in topic/target/constraints as appropriate, not content, whose spec type remains STRING.

**rule_category_cuisine_value** (v19/rule/category/cuisine-value; rule governing cuisine_pizza)

STRING cuisine class; cuisine_indian is a cuisine filter, not the location India.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; candidate)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing clock)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_event_value** (v19/rule/category/event-value; rule governing event_camper_in_sludge_pit)

TERM-described narrative event, not a recorded EVENT. Require inclusion explicitly when generating a story.

**rule_category_format_value** (v19/rule/category/format-value; rule governing format_numbered_list)

STRING format. format_email is layout, not the action send_email.

**rule_category_location_name** (v19/rule/category/location-name; rule governing eastern_cape)

STRING location descriptor. A `table` surface is not the generated artifact category art_table.

**rule_category_metric_value** (v19/rule/category/metric-value; rule governing metric_response_time)

STRING metric identity, not a Boolean value. Uptime and response time need numeric observations with units; order-late is Boolean-valued. Do not type every metric as BOOL.

**rule_category_recipient_value** (v19/rule/category/recipient-value; rule governing role_sister)

STRING roles or explicit named recipients. A role is not an exact person's identity. Keep an explicit name where substituting a role loses information.

**rule_category_search_value** (v19/rule/category/search-value; rule governing cat_limited_time_offers)

STRING refinements rank_ / dir_ / cat_ / avail_ / genre_ are separate. rank_rating may fill rank_field; genre_label::comedy may not. “Cheapest” usually requires both rank_price and dir_asc, not rank_price alone.

**rule_category_semantic_category_value** (v19/rule/category/semantic-category-value; rule governing class_temple)

STRING class label used by typed constraints. class_temple describes a class, not an acquired physical temple reference.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing on)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_tone_value** (v19/rule/category/tone-value; candidate)

STRING register. tone_urgent describes urgency, not a concrete deadline.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_school_work_routine)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_composites_general** (v19/rule/composites-general; rule governing topic_school_work_routine)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_examples_general** (v19/rule/examples-general; rule governing example_b_preserve_the_class_and_amount_of_an_itinerary_constraint)

Examples use this glossary's contracts. They have not been verified by an implemented BrainCode parser.

**rule_operations_general** (v19/rule/operations-general; rule governing search_travel)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_supplemental_general** (v19/rule/supplemental-general; rule governing art_itinerary)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; rule governing time_point)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- extract | operation | operation-vocabulary | (target: LIST[REF[STRING]], limit: NUMBER) -> LIST[REF[STRING]] | First limit results, preserving order and identity; limit is a nonnegative integer; limit=1 is still a list  ⟵ candidate
- pick_up | operation | operation-vocabulary | (target: STRING / ATOM[object_label] / ATOM[food_label], quantity?: NUMBER, source?: STRING / ATOM[object_label], color?: STRING / ATOM[color_label], shape?: STRING, state?: STRING) -> REF[STRING] or LIST[REF[STRING]] | Select/acquire objects. Missing quantity or literal 1 returns REF; integer literal greater than 1 returns LIST[REF]. Other values are invalid for this profile. | aliases: grab, take, retrieve  ⟵ candidate
- place | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label], location?: STRING / ATOM[object_label], relation?: STRING) -> void | Place an already acquired object. Spatial relation must be explicit if the source distinguishes it. | aliases: put, insert  ⟵ candidate
- search_travel | operation | operation-vocabulary | (target: STRING, constraints?: LIST[TERM], location?: STRING / ATOM[country]) -> LIST[REF[STRING]] | Query travel options meeting supplied constraints. Does not book them.  ⟵ candidate
- send_message | operation | operation-vocabulary | (recipient: STRING, content: STRING, tone?: STRING) -> void | Send supplied exact content through the specified message context. If the channel is unresolved, report it. | aliases: text  ⟵ candidate
- wait | operation | operation-vocabulary | (duration?: NUMBER) -> void | Pause execution for a duration or cycle. duration in seconds or ticks. | aliases: idle, pause  ⟵ candidate

### speech acts

- correct | speech_act | operation-vocabulary | UTTER correct(target: CLAIM) | Offer corrected content. Actual supersession requires the Conversation revision rules.  ⟵ candidate
- propose | speech_act | operation-vocabulary | UTTER propose(target: TERM) | Suggest an action/idea; does not record it as performed.  ⟵ candidate
- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ dependency of obligation
- at_least | constructor | TERM at_least(measure: TERM) -> TERM | A lower bound: the constrained value is greater than or equal to the given measure (or number term). Use inside requirement(value=...). | not: an exact value; a strict 'more than' only when the source says so explicitly | aliases: at least, minimum, or more, no less than, plus  ⟵ candidate
- at_most | constructor | TERM at_most(measure: TERM) -> TERM | An upper bound: the constrained value is less than or equal to the given measure (or number term). Use inside requirement(value=...). | not: an exact value or a target to aim for | aliases: at most, maximum, up to, no more than, under  ⟵ candidate
- calculation | constructor | TERM calculation(inputs: LIST[TERM], operation: STRING, result?: TERM) -> TERM | Constructs a descriptive representation of an arithmetic or algorithmic calculation step with inputs, operation identifier, and optional resulting value. | not: an executed runtime action or factual claim of outcome | aliases: math_operation, compute_step  ⟵ candidate
- conjunction | constructor | TERM conjunction(items: LIST[TERM]) -> TERM | All described components apply | not: Does not imply temporal order  ⟵ candidate
- document_section | constructor | TERM document_section(title: STRING, items?: LIST[TERM]) -> TERM | Constructs a structural document section descriptor with a section title and optional content items. | not: a complete document artifact class (use art_structured_report) | aliases: section, report_section, article_section  ⟵ candidate
- duration | constructor | TERM duration(amount: NUMBER, unit: STRING) -> TERM | Requested elapsed/calendar extent | not: Word/item counts are not time  ⟵ candidate
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ dependency of constraint_exclude_flowery_language
- group_size | constructor | TERM group_size(count: NUMBER, group?: STRING / TERM) -> TERM | The headcount or number of members in a specified group or party; count is a nonnegative integer. | not: minimum_per_period (a per-period minimum bound) or measure (measured quantities with units) | aliases: party_size, party of, number of guests, guest_count  ⟵ candidate
- include | constructor | TERM include(item: STRING / TERM) -> TERM | Require the identified content/item | not: Not permission to invent an instance in a recorded trace  ⟵ dependency of constraint_include_character_attribute_list
- maximum_between_stops | constructor | TERM maximum_between_stops(activity: STRING, amount: NUMBER, unit: STRING) -> TERM | Upper bound on the stated activity between successive stops | not: Not a limit on total daily duration  ⟵ candidate
- measure | constructor | TERM measure(amount: NUMBER, unit: STRING / ATOM[currency]) -> TERM | A measured amount: a number with its unit symbol (a unit-category value such as unit_minute, cap_gb or currency::USD). Describes the amount only; asserts nothing. ATOM[currency] is also accepted and supplies the pinned currency identity; no exchange rate or conversion is implicit. | not: a symbol with the number baked in (char_age_18, size_16gb); a unitless count (use the quantity argument) | aliases: amount of, size of, measured in  ⟵ candidate
- minimum_per_period | constructor | TERM minimum_per_period(class: STRING, count: NUMBER, period: STRING) -> TERM | At least count members of class in each period | not: Not a minimum total over the whole artifact  ⟵ candidate
- obligation | constructor | TERM obligation(actor: STRING / TERM, activity: TERM) -> TERM | Constructs a deontic obligation description requiring an actor to perform an activity. actor and activity specified. | aliases: duty, mandatory_activity  ⟵ candidate
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ candidate
- sequence | constructor | TERM sequence(items: LIST[TERM]) -> TERM | Ordered described activities/content | not: Not unordered conjunction  ⟵ candidate
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ dependency of topic_school_work_routine
- temporal_context | constructor | TERM temporal_context(activity: STRING / TERM, period?: STRING) -> TERM | Constructs a temporal or situational context descriptor specifying an ongoing process, evaluation phase, or historical timeframe. | not: time_point (a specific timestamp/date) or duration (an elapsed numerical duration) | aliases: while, during, in past relationships, timeframe  ⟵ candidate
- test_condition | constructor | TERM test_condition(condition: STRING, expected: BOOL) -> TERM | A testable condition with the expected Boolean outcome | not: Expected outcome is not an observed result  ⟵ dependency of assert_multinomial_scorer
- time_horizon | constructor | TERM time_horizon(horizon: STRING) -> TERM | Constructs a temporal horizon or prospective timeframe descriptor indicating relative temporal distance into the future. | not: a specific calendar timestamp (use time_point) or an elapsed numerical duration (use duration). | aliases: future, future timeframe, time horizon, far off in the future, far future  ⟵ candidate
- time_point | constructor | TERM time_point(date?: STRING, time?: STRING, timezone?: STRING) -> TERM | Constructs a structured representation of a specific calendar date, time of day, or scheduled timestamp. | not: an elapsed time duration (use duration) | aliases: timestamp, datetime, scheduled_time  ⟵ candidate

### composites

- assert_multinomial_scorer | composite | code-value | TERM assert_multinomial_scorer() -> TERM | Assertion that multinomial probabilistic scoring succeeds. | = test_condition(condition="multinomial_probabilistic_scoring", expected=TRUE)  ⟵ candidate
- constraint_budget_limited | composite | constraint-value | TERM constraint_budget_limited() -> TERM | Limited budget. | = requirement(property="budget_limited", value=TRUE)  ⟵ candidate
- constraint_exclude_flowery_language | composite | constraint-value | TERM constraint_exclude_flowery_language() -> TERM | Avoid flowery language. | = exclude(item="flowery_language")  ⟵ candidate
- constraint_exclude_liberation_theme | composite | constraint-value | TERM constraint_exclude_liberation_theme() -> TERM | Avoid liberation theme. | = exclude(item="liberation_theme")  ⟵ candidate
- constraint_include_character_attribute_list | composite | constraint-value | TERM constraint_include_character_attribute_list() -> TERM | Include character attributes. | = include(item="character_attribute_list")  ⟵ candidate
- constraint_realistic | composite | constraint-value | TERM constraint_realistic() -> TERM | Must be realistic. | = requirement(property="realistic", value=TRUE)  ⟵ candidate
- constraint_respectful | composite | constraint-value | TERM constraint_respectful() -> TERM | Must be respectful. | = requirement(property="respectful", value=TRUE)  ⟵ candidate
- content_kyoto_itinerary | composite | content-value | TERM content_kyoto_itinerary() -> TERM | A Kyoto itinerary subject. | = subject(kind="itinerary", location="Kyoto")  ⟵ dependency of example_b_preserve_the_class_and_amount_of_an_itinerary_constraint
- event_camper_in_sludge_pit | composite | event-value | TERM event_camper_in_sludge_pit() -> TERM | Campers interacting in a sludge pit. | = activity(verb="interact", actor="campers", location="sludge_pit")  ⟵ candidate
- topic_school_work_routine | composite | topic-value | TERM topic_school_work_routine() -> TERM | School and work routine. | = subject(kind="routine", qualifier=conjunction(items=[subject(kind="school"), subject(kind="work")]))  ⟵ candidate

### claim relations

- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ core
- occurred_recently | claim_relation | CLAIM occurred_recently(target: CLAIM) | Asserts temporal recency of an asserted occurrence or claim. temporal recency qualifier. | aliases: recently_happened  ⟵ candidate
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ core
- prep_time | claim_relation | CLAIM prep_time(value: TERM) | Asserts an estimated preparation or assembly time duration. time requirement assertion. | aliases: preparation_duration  ⟵ candidate
- prohibited | claim_relation | CLAIM prohibited(subject: STRING / TERM, location: STRING / TERM, condition?: STRING / TERM) | Asserts that a subject is prohibited from a location or activity under specified conditions. deontic prohibition claim. | aliases: forbidden, banned_from  ⟵ related to obligation
- proposed_policy | claim_relation | CLAIM proposed_policy(policy: TERM, requirements: LIST[TERM]) | Asserts that a proposed policy framework comprises the specified requirement terms. policy must be a policy term. | aliases: policy_proposal  ⟵ related to obligation

### links

- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ core
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ core
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ core

### values

- art_itinerary | value | artifact-value | An ordered travel plan; GENERATE returns STRING, not booked travel  ⟵ candidate
- art_plan | value | artifact-value | Actionable plan.  ⟵ candidate
- cuisine_mediterranean | value | cuisine-value | Mediterranean culinary cuisine style. | aliases: mediterranean  ⟵ candidate
- cuisine_pizza | value | cuisine-value | Pizza culinary cuisine style and food category. | not: cuisine_italian (broader regional/national cuisine) | aliases: pizza, pizzeria, pizza cuisine  ⟵ candidate
- unit_day | value | duration-unit-value | Day. | aliases: days  ⟵ candidate
- unit_hour | value | duration-unit-value | Hour. | aliases: hours  ⟵ candidate
- unit_item | value | duration-unit-value | Top-level generated list or report item. | aliases: items, entries  ⟵ candidate
- unit_minute | value | duration-unit-value | Minute. | aliases: minutes, min  ⟵ candidate
- unit_month | value | duration-unit-value | Month. | aliases: months  ⟵ candidate
- unit_second | value | duration-unit-value | Second. | aliases: seconds, sec  ⟵ candidate
- unit_sentence | value | duration-unit-value | One grammatical sentence in text generation or constraint counting. | not: unit_paragraph (paragraph block) or unit_word (individual word) | aliases: sentence, sentences  ⟵ candidate
- unit_week | value | duration-unit-value | Week. | aliases: weeks  ⟵ candidate
- unit_year | value | duration-unit-value | Year. | aliases: years  ⟵ candidate
- bread | value | entity-name | A bread loaf or slice food object. | aliases: bread  ⟵ candidate
- clock | value | entity-name | A clock timepiece appliance. | not: duration units like unit_hour | aliases: clock, timer  ⟵ candidate
- desk | value | entity-name | A work desk furniture surface. | aliases: desk  ⟵ candidate
- entity_appetizers | value | entity-name | Event planning item or menu category: entity_appetizers. | aliases: entity_appetizers  ⟵ candidate
- entity_assembly_tips | value | entity-name | Event planning item or menu category: entity_assembly_tips. | aliases: entity_assembly_tips  ⟵ candidate
- entity_condensed_grocery_list | value | entity-name | Event planning item or menu category: entity_condensed_grocery_list. | aliases: entity_condensed_grocery_list  ⟵ candidate
- entity_grocery_list | value | entity-name | Event planning item or menu category: entity_grocery_list. | aliases: entity_grocery_list  ⟵ candidate
- entity_order_vs_assemble_plan | value | entity-name | Event planning item or menu category: entity_order_vs_assemble_plan. | aliases: entity_order_vs_assemble_plan  ⟵ candidate
- entity_recipes | value | entity-name | Event planning item or menu category: entity_recipes. | aliases: entity_recipes  ⟵ candidate
- plate | value | entity-name | A shallow, flat dish or vessel used for holding, preparing, or serving food. | not: bowl (deep concave vessel) or table (furniture surface) | aliases: dish, plate  ⟵ candidate
- format_newsletter | value | format-value | Newsletter layout. | aliases: newsletter  ⟵ candidate
- format_numbered_list | value | format-value | Numbered list. | aliases: numbered steps  ⟵ candidate
- format_structured_report | value | format-value | Headed structured report layout. | aliases: structured report, report  ⟵ candidate
- eastern_cape | value | location-name | Eastern Cape region.  ⟵ candidate
- night_stand | value | location-name | A small bedside table or nightstand furniture surface. | not: a chest of drawers (use dresser) or a general table surface (use table) | aliases: nightstand, bedside table  ⟵ candidate
- metric_order_late | value | metric-value | Whether an order is late. | aliases: order is late, delayed  ⟵ candidate
- metric_response_time | value | metric-value | Support response time. | aliases: response time  ⟵ candidate
- metric_uptime | value | metric-value | Service uptime status. | aliases: uptime, is up  ⟵ candidate
- role_daughter | value | recipient-value | Daughter participant role in family or travel context. | not: role_sister, role_mother, or generic role_kids | aliases: daughter, my daughter  ⟵ candidate
- role_sister | value | recipient-value | Sister participant role in family/event context. | aliases: sister  ⟵ candidate
- cat_limited_time_offers | value | search-value | Category: time-limited deals.  ⟵ candidate
- dir_asc | value | search-value | Ascending rank direction. | aliases: lowest first  ⟵ candidate
- dir_desc | value | search-value | Descending rank direction. | aliases: highest first  ⟵ candidate
- rank_distance | value | search-value | Rank field: proximity. | aliases: nearest, closest  ⟵ candidate
- class_temple | value | semantic-category-value | The abstract class of temples. | aliases: temple, temples  ⟵ dependency of example_b_preserve_the_class_and_amount_of_an_itinerary_constraint
- in_front_of | value | spatial-relation | Positioned in front of. | aliases: in front of  ⟵ candidate
- left_of | value | spatial-relation | To the left of. | aliases: left of  ⟵ candidate
- on | value | spatial-relation | Resting atop. | aliases: on top of  ⟵ candidate
- daytime | value | time-of-day-value | The period of natural daylight between sunrise and sunset in the diurnal cycle. | not: unit_day (a 24-hour elapsed duration unit) or clock time timestamps | aliases: daytime, day, day time, daylight hours  ⟵ candidate
- nighttime | value | time-of-day-value | The period of darkness between sunset and sunrise in the diurnal cycle. | not: night_stand (a piece of furniture) or clock time timestamps | aliases: nighttime, night, night time, darkness  ⟵ candidate
- tone_neutral | value | tone-value | Plain, unmarked register.  ⟵ candidate
- topic_politics | value | topic-value | Politics.  ⟵ candidate
- unit_gram | value | unit-value | Standard metric measurement unit of mass equal to 1/1,000 of a kilogram (0.001 kg). | not: digital capacity units (like cap_gb) or temporal duration units | aliases: g, gram, grams  ⟵ candidate

### examples

- example_b_preserve_the_class_and_amount_of_an_itinerary_constraint (candidate): Preserve the class and amount of an itinerary constraint

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

