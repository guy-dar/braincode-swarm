# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 65 needs (decomposition: llm), 267 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | constraint | t1:s1 | There are 8 people in a row in positions 1 to 8. | `extract`, `group_size`, `sort`, `minimum_per_period`, `rank_distance`, `format_numbered_list`, `constraint_include_character_attribute_list`, `constraint_single_choice`, `unit_week`, `entity_sides`, `dir_asc`, `entity_mains` |
| n2 | constraint | t1:s2 | Each person supports a unique NFL team. | `role_support_team`*, `entity_flowers`, `dog`, `entity_sides`, `constraint_include_character_attribute_list`, `entity_mains`, `constraint_single_choice`, `entity_menu_items`, `gender_identity`, `constraint_beginner`, `new_york_university`, `bionic_person` |
| n3 | constraint | t1:s3 | Each person drives a unique motorbike. | `driver_license`, `vehicle_allowance`, `bionic_person`, `constraint_include_character_attribute_list`, `eastern_cape`, `remote_control`, `turn`, `laptop`, `shape_oval`, `constraint_exclude_flowery_language`, `constraint_budget_limited`, `dom_ddp` |
| n4 | constraint | t1:s4 | Each person likes a unique gemstone. | `entity_flowers`, `art_character_profile`, `constraint_include_character_attribute_list`, `entity_desserts`, `grape_merlot`, `constraint_single_choice`, `art_structured_report`, `art_plan`, `entity_cake`, `constraint_beginner`, `constraint_exclude_flowery_language`, `art_story` |
| n5 | constraint | t1:s5 | Each person likes a unique fruit. → `food_label::<key>` | `dried_fruit`, `apple`, `sultana`, `pear`, `fruit_juice`, `grape_thompson_seedless`, `grape_must`, `wine_grape`, `constraint_include_character_attribute_list`, `grape_merlot`, `grape_chardonnay`, `entity_sweet_food` |
| n6 | constraint | t1:s6 | Each person lives in a unique colored house. → `color_label::<key>` | `color_label`*, `entity_flowers`, `living_room`, `color_pink`, `wall`, `lamp`, `constraint_include_character_attribute_list`, `counter`, `constraint_single_choice`, `constraint_respectful`, `mirror`, `constraint_budget_limited` |
| n7 | constraint | t1:s7 | Each person likes a unique flower. | `entity_flowers`*, `constraint_exclude_flowery_language`, `vase`, `color_pink`, `grape_thompson_seedless`, `cloves`, `grape_merlot`, `grape_pinot_noir`, `constraint_include_character_attribute_list`, `constraint_single_choice`, `grape_sauvignon_blanc`, `grape_cabernet_sauvignon` |
| n8 | constraint | t1:s8 | Each person has a unique name. | `entity_flowers`, `char_female`, `character_trait`, `constraint_include_character_attribute_list`, `naming_pattern`, `gender_identity`, `character`, `bionic_person`, `dog`, `entity_mains`, `constraint_single_choice`, `art_character_profile` |
| n9 | constraint | t1:s9 | Each person reads a unique book genre. → `genre_label::<key>` | `textbook`*, `genre_label`*, `char_female`, `art_character_profile`, `cat_game`, `character_trait`, `character`, `constraint_include_character_attribute_list`, `style_narrative`, `topic_baldurs_gate_3`, `art_story`, `format_newsletter` |
| n10 | speech_act | t1:s10 | Instructs to solve the puzzle using the provided clues. | `respond`, `ask`, `inform`, `propose`, `conjunction`, `test_condition`, `conditional`, `enables`, `calculation`, `decline`, `topic_baldurs_gate_3`, `confirm` |
| n11 | constraint | t1:s11 | The mango eater is between the science fiction reader and the Harley-Davidson driver. | `color_pink`, `bionic_person`, `driver_license`, `apple`, `topic_spider_man_2`, `tattoos`, `between`*, `constraint_include_character_attribute_list`, `constraint_exclude_flowery_language`, `art_character_profile`, `cuisine_arab`, `cat_game` |
| n12 | constraint | t1:s12 | The Benelli driver likes Corals. | `driver_license`, `rental_vehicle`, `cheese`, `shape_triangular`, `character_trait`, `style_catchy`, `constraint_include_character_attribute_list`, `cuisine_pizza`, `color_pink`, `grape_pinot_noir`, `similarity`, `cuisine_italian` |
| n13 | constraint | t1:s13 | The Carolina Panthers supporter reads magical realism. | `beliefs`, `style_persuasive`, `character`, `personal_values`, `constraint_include_character_attribute_list`, `eastern_cape`, `art_story`, `path_ipython_core_magics_basic_py`, `bionic_person`, `constraint_realistic`, `self_protection`, `constraint_exclude_liberation_theme` |
| n14 | constraint | t1:s14 | The history reader is immediately left of the daisy liker. | `left_of`*, `constraint_exclude_flowery_language`, `constraint_include_character_attribute_list`, `path_numpy_core_fromnumeric_py`, `time_horizon`, `entity_flowers`, `topic_baldurs_gate_3`, `constraint_single_choice`, `constraint_beginner`, `remove_literal`, `event_sadie_adler_unmasking`, `mug` |
| n15 | constraint | t1:s15 | The pear eater is immediately left of the Denver Broncos supporter. | `left_of`*, `pear`*, `shape_oval`, `constraint_include_character_attribute_list`, `grape_tannin`, `sultana`, `apple`, `enzyme`, `grape_thompson_seedless`, `raisin`, `constraint_single_choice`, `indicator` |
| n16 | constraint | t1:s16 | The grape eater lives in the yellow house. | `wine_grape`*, `grape_chardonnay`, `grape_merlot`, `sultana`, `raisin`, `grape_must`, `grape_tannin`, `wine`, `grape_sauvignon_blanc`, `grape_thompson_seedless`, `enzyme`, `grape_pinot_noir` |
| n17 | constraint | t1:s17 | Rose is immediately left of the rose liker. | `left_of`*, `color_pink`, `entity_flowers`, `well_wishes`, `pear`, `wine_grape`, `constraint_include_character_attribute_list`, `constraint_exclude_flowery_language`, `ginger`, `constraint_single_choice`, `apple`, `constraint_exclude_liberation_theme` |
| n18 | constraint | t1:s18 | The Ducati driver is between the daffodil liker and the Ruby liker. | `driver_license`, `color_pink`, `russia`, `between`*, `fermentation_nutrient`, `turn`, `constraint_exclude_flowery_language`, `grape_tannin`, `maximum_between_stops`, `constraint_include_character_attribute_list`, `path_sklearn_linear_model_logistic_py`, `path_numpy_core_fromnumeric_py` |
| n19 | constraint | t1:s19 | The spiritual reader is left of the marigold liker. | `left_of`*, `constraint_exclude_liberation_theme`, `sun`, `right_of`, `grape_thompson_seedless`, `beliefs`, `sultana`, `constraint_include_character_attribute_list`, `entity_flowers`, `grape_pinot_noir`, `constraint_exclude_flowery_language`, `constraint_single_choice` |
| n20 | constraint | t1:s20 | The fantasy reader supports the Buffalo Bills. | `role_support_team`*, `constraint_include_character_attribute_list`, `grape_pinot_noir`, `role_professor`, `metric_repeat_buyer`, `egift_card`, `constraint_beginner`, `constraint_single_choice`, `role_sister`, `constraint_budget_limited`, `format_newsletter`, `constraint_realistic` |
| n21 | constraint | t1:s21 | The raspberry eater is next to the indigo house resident. | `sultana`, `grape_merlot`, `next_to`*, `ginger`, `raisin`, `constraint_include_character_attribute_list`, `wine`, `constraint_exclude_flowery_language`, `grape_thompson_seedless`, `fruit_juice`, `enzyme`, `constraint_budget_limited` |
| n22 | constraint | t1:s22 | The Benelli driver is next to the Carolina Panthers supporter. | `driver_license`, `vehicle_allowance`, `rental_vehicle`, `eastern_cape`, `character_trait`, `constraint_include_character_attribute_list`, `performance_tracking`, `behind`, `next_to`*, `valet`, `role_son`, `in_front_of` |
| n23 | constraint | t1:s23 | Yair is immediately left of Jackson. | `left_of`*, `yakuza`, `constraint_include_character_attribute_list`, `constitutional_ai`, `maqluba`, `constraint_single_choice`, `constraint_exclude_liberation_theme`, `constraint_respectful`, `constraint_budget_limited`, `transform_remove_br`, `constraint_beginner`, `constraint_comprehensive` |
| n24 | constraint | t1:s24 | The indigo house resident is Rajiv. | `grape_merlot`, `locale_hi_en`, `tattooed_guests`, `metric_socio_economic_status`, `cuisine_indian`, `constraint_include_character_attribute_list`, `sultana`, `constraint_budget_limited`, `class_temple`, `entity_flowers`, `raisin`, `liberal_onsen` |
| n25 | constraint | t1:s25 | The gold house resident is at one of the ends. | `door`, `wall`, `living_room`, `counter`, `new_york_university`, `sun`, `floor`, `constraint_include_character_attribute_list`, `constraint_budget_limited`, `desk`, `lamp`, `night_stand` |
| n26 | constraint | t1:s26 | The blueberry eater likes roses. | `entity_flowers`, `constraint_exclude_flowery_language`, `grape_merlot`, `color_pink`, `cloves`, `ginger`, `grape_pinot_noir`, `wine_grape`, `vase`, `grape_thompson_seedless`, `constraint_include_character_attribute_list`, `grape_sauvignon_blanc` |
| n27 | constraint | t1:s27 | The Coral liker supports the Miami Dolphins. | `role_support_team`*, `class_beach`, `cheese`, `island`, `tattooed_guests`, `constraint_include_character_attribute_list`, `state_microwaved`, `locale_es`, `waterproof_stickers`, `cuisine_mediterranean`, `animal_label`, `microwave` |
| n28 | constraint | t1:s28 | The blueberry eater is next to the violet house resident. | `next_to`*, `grape_merlot`, `sultana`, `color_pink`, `fridge`, `lettuce`, `living_room`, `ginger`, `color_label`, `constraint_include_character_attribute_list`, `entity_flowers`, `role_sister` |
| n29 | constraint | t1:s29 | The Ducati driver is immediately left of the Bajaj driver. | `left_of`*, `driver_license`, `remote_control`, `rental_vehicle`, `turn`, `shape_oval`, `cuisine_pizza`, `maximum_between_stops`, `grape_tannin`, `locale_fr`, `constraint_include_character_attribute_list`, `wine_yeast` |
| n30 | constraint | t1:s30 | Bob is immediately left of the Piaggio driver. | `left_of`*, `driver_license`, `behind`, `remote_control`, `constraint_include_character_attribute_list`, `turn`, `wine_yeast`, `maximum_between_stops`, `constraint_single_choice`, `remove_literal`, `constraint_budget_limited`, `path_numpy_core_fromnumeric_py` |
| n31 | constraint | t1:s31 | Bob is immediately left of the Los Angeles Rams supporter. | `left_of`*, `min_ram`, `ram_unit`, `grape_merlot`, `remote_control`, `behind`, `constraint_include_character_attribute_list`, `state_upright`, `waterproof_stickers`, `sultana`, `constraint_single_choice`, `constraint_beginner` |
| n32 | constraint | t1:s32 | The orange house resident eats raspberries. | `dried_fruit`, `raisin`, `fruit_juice`, `sultana`, `ice_cream`, `pear`, `constraint_include_character_attribute_list`, `color_pink`, `ginger`, `constraint_budget_limited`, `constraint_exclude_flowery_language`, `grape_must` |
| n33 | constraint | t1:s33 | The Pearl liker is Randy. | `grape_pinot_noir`, `bowtie`, `constraint_include_character_attribute_list`, `pear`, `grape_merlot`, `color_pink`, `yarn`, `mittens`, `bowl`, `constraint_exclude_liberation_theme`, `constraint_budget_limited`, `constraint_exclude_flowery_language` |
| n34 | constraint | t1:s34 | The violet house resident is between the history reader and the short story reader. | `art_story`, `art_short_text`, `role_sister`, `role_daughter`, `living_room`, `between`*, `role_colleague`, `role_mother`, `role_professor`, `role_son`, `format_newsletter`, `constraint_include_character_attribute_list` |
| n35 | constraint | t1:s35 | The yellow house resident supports the Seattle Seahawks. | `role_support_team`*, `valet`, `remote_control`, `sun`, `living_room`, `preserve`, `microwave_stand`, `sort`, `constraint_include_character_attribute_list`, `waterproof_stickers`, `path_gcloud_pubsub_subscription_py`, `interpersonal_stance` |
| n36 | constraint | t1:s36 | The spiritual reader is at one of the ends. | `on`, `beliefs`, `constraint_include_character_attribute_list`, `art_story`, `right_of`, `behind`, `constraint_exclude_liberation_theme`, `constraint_respectful`, `next_to`, `activity`, `topic_baldurs_gate_3`, `constraint_exclude_flowery_language` |
| n37 | constraint | t1:s37 | The science fiction reader is next to the mango eater. | `bionic_person`, `topic_spider_man_2`, `next_to`*, `role_professor`, `art_story`, `apple`, `color_pink`, `constraint_include_character_attribute_list`, `art_character_profile`, `topic_macbook_pro_2017`, `constraint_exclude_flowery_language`, `topic_baldurs_gate_3` |
| n38 | constraint | t1:s38 | The Yamaha driver likes dahlias. | `driver_license`, `vehicle_allowance`, `grape_sauvignon_blanc`, `remote_control`, `shape_oval`, `shape_round`, `turn`, `shape_triangular`, `constraint_include_character_attribute_list`, `rental_vehicle`, `grape_cabernet_sauvignon`, `grape_tannin` |
| n39 | constraint | t1:s39 | Yair reads spiritual books. | `textbook`*, `yakuza`, `beliefs`, `grape_merlot`, `personal_values`, `constraint_include_character_attribute_list`, `topic_baldurs_gate_3`, `art_story`, `constraint_exclude_liberation_theme`, `entity_flowers`, `constraint_respectful`, `topic_classical_piano` |
| n40 | constraint | t1:s40 | The spiritual reader drives the Benelli. | `beliefs`, `sun`, `constraint_include_character_attribute_list`, `personal_values`, `art_story`, `constraint_exclude_liberation_theme`, `tone_empathetic`, `grape_chardonnay`, `on`, `constraint_budget_limited`, `constraint_exclude_flowery_language`, `constraint_respectful` |
| n41 | constraint | t1:s41 | Michelle is between Mohsen and the mango eater. | `color_pink`, `role_mother`, `sultana`, `constraint_include_character_attribute_list`, `between`*, `fruit_juice`, `constraint_exclude_flowery_language`, `entity_sweet_food`, `constraint_budget_limited`, `role_sister`, `dried_fruit`, `apple` |
| n42 | constraint | t1:s42 | The Pearl liker lives in the pink house. | `color_pink`*, `grape_merlot`, `grape_pinot_noir`, `pear`, `sym_pandas_testing_assert_almost_equal`, `path_pandas_src_testing_pyx`, `constraint_include_character_attribute_list`, `entity_flowers`, `yarn`, `constraint_single_choice`, `bowtie`, `dulce_de_leche` |
| n43 | constraint | t1:s43 | The Ruby liker is left of the Pearl liker. | `left_of`*, `cinnamon`, `pear`, `color_pink`, `grape_pinot_noir`, `ginger`, `constraint_include_character_attribute_list`, `grape_thompson_seedless`, `grape_tannin`, `wine_grape`, `yarn`, `constraint_exclude_flowery_language` |
| n44 | constraint | t1:s44 | The Opal liker is next to the Dallas Cowboys supporter. | `next_to`*, `behind`, `locale_fr`, `locale_es`, `in_front_of`, `constraint_include_character_attribute_list`, `left_of`, `corner`, `indicator`, `topic_pickup_lines`, `style_persuasive`, `constraint_exclude_liberation_theme` |
| n45 | constraint | t1:s45 | The Dolomite liker lives in the orange house. | `island`, `earth`, `desk`, `floor`, `constraint_include_character_attribute_list`, `living_room`, `path_ipython_core_magics_basic_py`, `shape_oval`, `constraint_exclude_liberation_theme`, `constraint_budget_limited`, `moon`, `entity_flowers` |
| n46 | constraint | t1:s46 | The begonia liker is immediately left of the dahlia liker. | `left_of`*, `constraint_exclude_flowery_language`, `constraint_include_character_attribute_list`, `sultana`, `grape_thompson_seedless`, `path_numpy_core_fromnumeric_py`, `entity_flowers`, `cloves`, `constraint_single_choice`, `constraint_exclude_liberation_theme`, `maximum_between_stops`, `constraint_beginner` |
| n47 | constraint | t1:s47 | The Carolina Panthers supporter likes peonies. | `eastern_cape`, `character_trait`, `constraint_include_character_attribute_list`, `style_persuasive`, `similarity`, `argues_for`, `tattooed_guests`, `audience_targeting`, `pan`, `constraint_budget_limited`, `africa`, `has_attribute` |
| n48 | constraint | t1:s48 | The Harley-Davidson driver lives in the pink house. | `color_pink`*, `driver_license`, `dom_ddp`, `laptop`, `remote_control`, `path_ipython_core_magics_basic_py`, `fridge`, `locale_zh`, `bionic_person`, `entity_flowers`, `desk`, `topic_spider_man_2` |
| n49 | constraint | t1:s49 | The peony liker likes Sapphires. | `grape_pinot_noir`, `grape_merlot`, `constraint_include_character_attribute_list`, `color_pink`, `martini_glass`, `style_catchy`, `wine_grape`, `constraint_exclude_flowery_language`, `illuminates`, `constraint_budget_limited`, `wine`, `entity_flowers` |
| n50 | constraint | t1:s50 | Bob is left of the Topaz liker. | `left_of`*, `dir_desc`, `behind`, `on`, `rank_direction`, `between`, `eastern_cape`, `rank_price`, `constraint_include_character_attribute_list`, `grape_merlot`, `constraint_single_choice`, `sun` |
| n51 | constraint | t1:s51 | The red house resident likes daffodils. | `entity_flowers`, `color_pink`, `new_york_university`, `living_room`, `dog`, `chair`, `topic_current_new_york_housing_market`, `constraint_exclude_flowery_language`, `constraint_include_character_attribute_list`, `united_kingdom`, `constraint_single_choice`, `constraint_budget_limited` |
| n52 | constraint | t1:s52 | The Piaggio driver is between the humor reader and the Ruby liker. | `driver_license`, `cinnamon`, `between`*, `constraint_include_character_attribute_list`, `yarn`, `character_trait`, `mittens`, `constraint_exclude_flowery_language`, `ginger`, `constraint_budget_limited`, `maximum_between_stops`, `cat_game` |
| n53 | constraint | t1:s53 | The pink house resident is next to Rose. | `color_pink`*, `entity_flowers`, `topic_current_new_york_housing_market`, `living_room`, `grape_merlot`, `new_york_university`, `next_to`*, `ginger`, `constraint_single_choice`, `oak_chips`, `role_sister`, `counter` |
| n54 | constraint | t1:s54 | The Pearl liker is next to the Buffalo Bills supporter. | `grape_merlot`, `grape_pinot_noir`, `wine_grape`, `grape_chardonnay`, `constraint_include_character_attribute_list`, `next_to`*, `wine`, `grape_sauvignon_blanc`, `bowtie`, `grape_thompson_seedless`, `grape_cabernet_sauvignon`, `constraint_budget_limited` |
| n55 | constraint | t1:s55 | The Denver Broncos supporter is immediately left of the Dolomite liker. | `left_of`*, `transform_preserve_first_column`, `shape_oval`, `constraint_include_character_attribute_list`, `locale_fr`, `constraint_exclude_liberation_theme`, `constraint_single_choice`, `inform`, `constraint_beginner`, `turn`, `transform_remove_br`, `constraint_budget_limited` |
| n56 | constraint | t1:s56 | The apple eater is immediately left of the orange house resident. | `apple`*, `left_of`*, `dried_fruit`, `pear`, `event_sadie_adler_unmasking`, `fruit_juice`, `enzyme`, `constraint_include_character_attribute_list`, `oak_chips`, `grape_must`, `entity_flowers`, `constraint_exclude_flowery_language` |
| n57 | constraint | t1:s57 | The orchid liker is at one of the ends. | `entity_flowers`, `vase`, `grape_pinot_noir`, `cloves`, `constraint_exclude_flowery_language`, `other_side_of`, `enzyme`, `grape_thompson_seedless`, `constraint_exclude_liberation_theme`, `art_structured_report`, `constraint_include_character_attribute_list`, `ginger` |
| n58 | constraint | t1:s58 | The Benelli driver eats bananas. | `driver_license`, `vehicle_allowance`, `rental_vehicle`, `constraint_include_character_attribute_list`, `fermentation_nutrient`, `bread`, `unit_gram`, `dried_fruit`, `sultana`, `moon`, `constraint_single_choice`, `lettuce` |
| n59 | constraint | t1:s59 | The Coral liker is immediately left of the pear eater. | `pear`*, `left_of`*, `cheese`, `sultana`, `grape_must`, `fruit_juice`, `dried_fruit`, `grape_thompson_seedless`, `constraint_include_character_attribute_list`, `raisin`, `material_memory_foam`, `dulce_de_leche` |
| n60 | constraint | t1:s60 | The fantasy reader is next to the Opal liker. | `character`, `next_to`*, `constraint_include_character_attribute_list`, `sun`, `art_plan`, `art_story`, `mittens`, `constraint_exclude_flowery_language`, `format_newsletter`, `art_character_profile`, `topic_spider_man_2`, `constraint_budget_limited` |
| n61 | constraint | t1:s61 | The Sapphire liker is immediately left of the Kawasaki driver. | `left_of`*, `driver_license`, `cuisine_pizza`, `conjunction`, `grape_tannin`, `constraint_include_character_attribute_list`, `path_numpy_core_fromnumeric_py`, `constraint_exclude_flowery_language`, `martini_glass`, `sultana`, `raisin`, `constraint_single_choice` |
| n62 | constraint | t1:s62 | The person at the 4th position is next to the Ducati driver. | `driver_license`, `vehicle_allowance`, `dir_desc`, `dir_asc`, `behind`, `chair`, `valet`, `in_front_of`, `rental_vehicle`, `between`, `next_to`*, `turn` |
| n63 | constraint | t1:s63 | The dahlia liker is next to Randy. | `next_to`*, `in_front_of`, `behind`, `on`, `left_of`, `constraint_include_character_attribute_list`, `corner`, `constraint_single_choice`, `art_character_profile`, `entity_flowers`, `constraint_exclude_flowery_language`, `constraint_budget_limited` |
| n64 | action | t1:s64 | Determine the position of the person who lives in the orange house. | `stand_up`, `sort`, `decision`, `living_room`, `place`, `walk`, `bionic_person`, `role_manager`, `character_trait`, `in_front_of`, `role_agent`, `behind` |
| n65 | object | t1:s64 | The person who lives in the orange house. → `color_label::<key>` | `chair`, `living_room`, `island`, `role_agent`, `role_mother`, `role_manager`, `fridge`, `resource_heater`, `wall`, `coffee_maker`, `role_colleague`, `door` |

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

- issue.project → platform_label
- activity.object → object_label, food_label, animal_label
- activity.location → country
- activity.instrument → object_label, platform_label
- place.destination → object_label
- place.location → object_label
- walk.destination → object_label
- requirement.value → platform_label
- subject.qualifier → platform_label
- subject.location → country
- failure.system → platform_label

## Retrieved records

### Shared rules that govern the records below (full text)

**rule_lexical_groups** (v19/rule/lexical-groups; rule governing platform_label)

Section 3.1 defines value groups: `group::key` values of type ATOM[group]. Open groups admit any key of their form (examples are not whitelists); standard groups admit the codes of their bundled standard (ISO 3166-1 alpha-2 for country, ISO 4217 for currency). Leaf values are never glossary entries. Consumer signatures alone decide where a group may appear. Retired bare symbols are invalid.

**rule_reading_guide** (v19/rule/reading-guide; core)

The spec governs syntax/types; this glossary defines vocabulary. Signature notation: ? optional, A / B explicit alternatives, void no result. Omitted optional arguments are unspecified. Value entries are category-refined STRING primitives; complex meanings require composition. Aliases are contextual hints, not unconditional equivalences. Report ambiguity. IDs use v19/<category>/<symbol>, v19/support/<symbol> or v19/composite/<symbol>. Statuses apply to this candidate: Retained preserves meaning; Adapted uses the stated contract; Composite requires TERM (bare STRING deprecated); Structural is syntax/argument vocabulary; Needs clarification is unusable until resolved; Deprecated is historical; Accepted is usable within this candidate.

**rule_recording_signatures** (v19/rule/recording-signatures; rule governing extract)

RECORD ACTION uses the operation signature with REF[STRING] → TERM and LIST[REF[STRING]] → LIST[TERM]; other types/categories stay unchanged. Return EVENT, never the runtime result. Record actual outputs as attributed CLAIMs. Do not infer missing resources.

**rule_speech_acts_general** (v19/rule/speech-acts-general; rule governing respond)

UTTER-only, void, with the spec's speech attributes and LIST[TERM] constraints. No result binding. Literal content cannot replace required semantic arguments for structured coverage.

**rule_structural_constructs** (v19/rule/structural-constructs; core)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; rule governing supports)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_attributes_and_generate** (v19/rule/attributes-and-generate; rule governing art_character_profile)

Attribute entries name arguments; legality/types come from each operation, not global membership. GENERATE uses the spec's core fields; retained artifact profiles return STRING. Numeric/list results need explicit profiles. Legacy itinerary fields expand to TERM constraints: duration/duration_unit → duration(amount,unit); stop_min_per_day/stop_requirement → minimum_per_period(class,count,period=unit_day), never an inferred temple class; max_walk_duration/unit → maximum_between_stops(activity="walk",amount,unit). No legacy shorthand is enabled. Old events/character_properties/transformations become explicitly scoped TERM constraints. Message purpose is TERM, not send_email.content: GENERATE exact STRING content, then send. Report opaque fallback separately.

**rule_category_artifact_value** (v19/rule/category/artifact-value; rule governing art_character_profile)

STRING artifact class for GENERATE.target. art_story says what kind of artifact to produce, not what occurs in its plot.

**rule_category_character_property_value** (v19/rule/category/character-property-value; rule governing char_female)

TERM-described trait/style. Use constraints and explicit inclusion/scope; do not use an ungoverned character_properties attribute.

**rule_category_code_value** (v19/rule/category/code-value; rule governing path_ipython_core_magics_basic_py)

path_/sym_ remain STRING identities; migrated chg_/assert_ are TERM constructors. Do not recover an exact file path by guessing from underscores.

**rule_category_constraint_value** (v19/rule/category/constraint-value; rule governing constraint_include_character_attribute_list)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_cuisine_value** (v19/rule/category/cuisine-value; rule governing cuisine_arab)

STRING cuisine class; cuisine_indian is a cuisine filter, not the location India.

**rule_category_descriptive_value** (v19/rule/category/descriptive-value; rule governing dom_ddp)

STRING modifier/domain label; never a free-form proposition. dom_sgi needs its intended referent established before semantically dependent use.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; rule governing unit_week)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing entity_sides)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_event_value** (v19/rule/category/event-value; rule governing event_sadie_adler_unmasking)

TERM-described narrative event, not a recorded EVENT. Require inclusion explicitly when generating a story.

**rule_category_format_value** (v19/rule/category/format-value; rule governing format_numbered_list)

STRING format. format_email is layout, not the action send_email.

**rule_category_locale_value** (v19/rule/category/locale-value; rule governing locale_hi_en)

STRING locale. “English” alone does not always mean locale_en_us; preserve ambiguity.

**rule_category_location_name** (v19/rule/category/location-name; rule governing new_york_university)

STRING location descriptor. A `table` surface is not the generated artifact category art_table.

**rule_category_metric_value** (v19/rule/category/metric-value; rule governing metric_repeat_buyer)

STRING metric identity, not a Boolean value. Uptime and response time need numeric observations with units; order-late is Boolean-valued. Do not type every metric as BOOL.

**rule_category_product_attribute_value** (v19/rule/category/product-attribute-value; rule governing color_pink)

STRING color/size/product-market facets. gender_women describes a product category, not an assertion about a person's gender.

**rule_category_recipient_value** (v19/rule/category/recipient-value; rule governing role_support_team)

STRING roles or explicit named recipients. A role is not an exact person's identity. Keep an explicit name where substituting a role loses information.

**rule_category_search_value** (v19/rule/category/search-value; rule governing rank_distance)

STRING refinements rank_ / dir_ / cat_ / avail_ / genre_ are separate. rank_rating may fill rank_field; genre_label::comedy may not. “Cheapest” usually requires both rank_price and dir_asc, not rank_price alone.

**rule_category_semantic_category_value** (v19/rule/category/semantic-category-value; rule governing class_temple)

STRING class label used by typed constraints. class_temple describes a class, not an acquired physical temple reference.

**rule_category_shape_value** (v19/rule/category/shape-value; rule governing shape_oval)

STRING geometry. shape_round may select a circular object; it does not imply color or dimensions.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing between)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_state_value** (v19/rule/category/state-value; rule governing state_microwaved)

STRING condition used in selection. state_warm does not command heat; “hot” is not automatically synonymous with “warm.”

**rule_category_style_value** (v19/rule/category/style-value; rule governing style_narrative)

STRING production style. style_narrative does not establish that described events occurred.

**rule_category_tone_value** (v19/rule/category/tone-value; rule governing tone_empathetic)

STRING register. tone_urgent describes urgency, not a concrete deadline.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_baldurs_gate_3)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_category_transformation_value** (v19/rule/category/transformation-value; rule governing transform_remove_br)

TERM-described transformation. Pass it through constraints; no ungoverned transformations attribute.

**rule_composites_general** (v19/rule/composites-general; rule governing constraint_include_character_attribute_list)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_operations_general** (v19/rule/operations-general; rule governing extract)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_search_web_attributes** (v19/rule/search-web-attributes; rule governing sort)

Optional filters: availability, category, color, cuisine, currency, gender, genre, location, platform, ram_unit, reservation_availability, shape, size (category-refined STRING); max_price, min_ram, min_rating (NUMBER); trending (BOOL). Explicit signature alternatives additionally admit atoms. Price requires currency; RAM requires a capacity unit; no default scale/source. rank is invalid: use sort, whose rank_field accepts rank_* and rank_direction accepts dir_*. Category/genre/availability accept only their own subfamilies.

**rule_supplemental_general** (v19/rule/supplemental-general; rule governing extract)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; rule governing group_size)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- extract | operation | operation-vocabulary | (target: LIST[REF[STRING]], limit: NUMBER) -> LIST[REF[STRING]] | First limit results, preserving order and identity; limit is a nonnegative integer; limit=1 is still a list  ⟵ candidate
- place | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label], location?: STRING / ATOM[object_label], relation?: STRING) -> void | Place an already acquired object. Spatial relation must be explicit if the source distinguishes it. | aliases: put, insert  ⟵ candidate
- sort | operation | operation-vocabulary | (target: LIST[REF[STRING]], rank_direction: STRING, rank_field: STRING) -> LIST[REF[STRING]] | Request ordering of selected results. Preserve member identity; this is not a claim that order was observed. | aliases: rank, order by  ⟵ candidate
- stand_up | operation | operation-vocabulary | () -> void | Return agent posture to standard upright standing position. agent must be in a non-standing posture. | aliases: stand  ⟵ candidate
- turn | operation | operation-vocabulary | (direction: STRING) -> void | Rotate agent body/view orientation. direction is typically left, right, or angle. | aliases: rotate, turn_around  ⟵ candidate
- walk | operation | operation-vocabulary | (destination: STRING / TERM / ATOM[object_label], relation?: STRING) -> void | Locomote towards a target destination or landmark. destination must identify a valid entity or location. | aliases: move_to, go_to, navigate_to  ⟵ candidate

### speech acts

- ask | speech_act | operation-vocabulary | UTTER ask(target: TERM, or a sufficiently precise topic: STRING / TERM) | Request information/advice; not an assertion of an answer. | aliases: ask, how should  ⟵ candidate
- confirm | speech_act | operation-vocabulary | UTTER confirm(target: CLAIM) | Confirm the proposition; its evidence/status remains explicit.  ⟵ candidate
- decline | speech_act | operation-vocabulary | UTTER decline(target: TERM) | Decline the represented request/proposal; not negate every proposition within it.  ⟵ candidate
- inform | speech_act | operation-vocabulary | UTTER inform(target: CLAIM) | Present the proposition; preserve its holder/status.  ⟵ candidate
- propose | speech_act | operation-vocabulary | UTTER propose(target: TERM) | Suggest an action/idea; does not record it as performed.  ⟵ candidate
- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ candidate
- audience_targeting | constructor | TERM audience_targeting(criteria: LIST[STRING] / LIST[TERM], audience?: STRING / TERM) -> TERM | Constructs a descriptive representation of audience targeting criteria such as demographics, geography, or interests. | not: an individual user constraint or character trait | aliases: target_audience, audience_criteria, ad_targeting  ⟵ candidate
- bionic_person | constructor | TERM bionic_person(composition?: STRING / TERM) -> TERM | Constructs a descriptive representation of a bionic person or cyborg entity with biological and mechanical components. | not: a standard human role (use role_user or role_adults) or a purely artificial device. | aliases: bionic person, bionic people, cyborg, half human half robot  ⟵ candidate
- calculation | constructor | TERM calculation(inputs: LIST[TERM], operation: STRING, result?: TERM) -> TERM | Constructs a descriptive representation of an arithmetic or algorithmic calculation step with inputs, operation identifier, and optional resulting value. | not: an executed runtime action or factual claim of outcome | aliases: math_operation, compute_step  ⟵ candidate
- character | constructor | TERM character(name: STRING, series?: STRING) -> TERM | Constructs a descriptive representation of a fictional or narrative character. name specifies the character identifier. | aliases: fictional_character  ⟵ candidate
- character_trait | constructor | TERM character_trait(property: STRING, value: STRING / NUMBER) -> TERM | A character attribute | not: Not a claim about a real person  ⟵ candidate
- conditional | constructor | TERM conditional(condition: TERM, consequence: TERM) -> TERM | Constructs a structured conditional proposition term connecting a condition and consequence. descriptive logic structure. | aliases: if_then  ⟵ candidate
- conjunction | constructor | TERM conjunction(items: LIST[TERM]) -> TERM | All described components apply | not: Does not imply temporal order  ⟵ candidate
- decision | constructor | TERM decision(activity: TERM) -> TERM | A decision whose content is the described activity | not: Not proof it was carried out  ⟵ candidate
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ dependency of constraint_exclude_flowery_language
- gender_identity | constructor | TERM gender_identity(identity: STRING) -> TERM | Constructs a descriptive term representing an individual's or demographic group's gender identity. | not: gender_women (product attribute) or char_female (fictional character trait) or identity (name/persona claim) | aliases: gender, gender_expression  ⟵ candidate
- group_size | constructor | TERM group_size(count: NUMBER, group?: STRING / TERM) -> TERM | The headcount or number of members in a specified group or party; count is a nonnegative integer. | not: minimum_per_period (a per-period minimum bound) or measure (measured quantities with units) | aliases: party_size, party of, number of guests, guest_count  ⟵ candidate
- illuminates | constructor | TERM illuminates(target: STRING / TERM, source: STRING / TERM) -> TERM | Constructs a description of directional illumination where a light source casts light onto a target body. | not: an ambient color state or reflection (use reflects_light) | aliases: illuminates, shines on, shining towards  ⟵ candidate
- include | constructor | TERM include(item: STRING / TERM) -> TERM | Require the identified content/item | not: Not permission to invent an instance in a recorded trace  ⟵ dependency of constraint_include_character_attribute_list
- indicator | constructor | TERM indicator(condition: STRING / TERM, indicator_type?: STRING) -> TERM | Constructs a descriptive term representing a warning sign, behavioral marker, or red flag indicating an underlying condition or risk. | not: warning (a system alert claim relation) or color_label::red (a product color) | aliases: red flag, warning sign, behavioral marker, signal  ⟵ candidate
- interpersonal_stance | constructor | TERM interpersonal_stance(actor: STRING / TERM, stance: STRING, target?: STRING / TERM) -> TERM | Constructs a descriptive representation of an actor's interpersonal stance, level of commitment, or relational engagement toward a partner. | not: character_trait (fictional characters) or attitude (an asserted claim relation) | aliases: relational_commitment, interpersonal_behavior, relationship_stance  ⟵ candidate
- issue | constructor | TERM issue(project: STRING / ATOM[platform_label], number: NUMBER) -> TERM | Constructs an issue tracker ticket reference. issue tracker descriptor. | aliases: issue_ticket, bug_report  ⟵ candidate
- maximum_between_stops | constructor | TERM maximum_between_stops(activity: STRING, amount: NUMBER, unit: STRING) -> TERM | Upper bound on the stated activity between successive stops | not: Not a limit on total daily duration  ⟵ candidate
- minimum_per_period | constructor | TERM minimum_per_period(class: STRING, count: NUMBER, period: STRING) -> TERM | At least count members of class in each period | not: Not a minimum total over the whole artifact  ⟵ candidate
- naming_pattern | constructor | TERM naming_pattern(description: STRING, context?: STRING) -> TERM | Constructs a descriptive naming or morphological pattern. used for rule-based or conventional naming schemes. | aliases: pattern_naming  ⟵ candidate
- performance_tracking | constructor | TERM performance_tracking(adjustment?: STRING / TERM, target: STRING / TERM) -> TERM | Constructs a descriptive representation of monitoring performance metrics or campaign results with an optional strategy adjustment. | not: a runtime metric observation or software test run | aliases: track_results, monitor_performance, campaign_tracking  ⟵ candidate
- preserve | constructor | TERM preserve(component: STRING, index: NUMBER) -> TERM | Keep the indexed component unchanged, using one-based indexing | not: Not preserve all components  ⟵ candidate
- remove_literal | constructor | TERM remove_literal(text: STRING) -> TERM | Remove occurrences of that exact literal in the stated artifact | not: Not remove similar markup unless specified  ⟵ candidate
- rental_vehicle | constructor | TERM rental_vehicle(category: STRING, model?: STRING) -> TERM | Constructs a descriptive representation of a rental vehicle or vehicle category. | not: an acquired physical vehicle reference or employee vehicle policy (use vehicle_allowance) | aliases: rental_car, hire_car, mystery_car  ⟵ candidate
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ dependency of constraint_single_choice
- self_protection | constructor | TERM self_protection(actor: STRING / TERM, domain: STRING, strategy?: STRING / TERM) -> TERM | Constructs a descriptive term representing an actor's self-protection practice, emotional boundary guarding, or coping strategy within a domain. | not: safe (a physical security container) or prohibited (a deontic rule) | aliases: guarding heart, emotional boundaries, protect oneself, coping strategy  ⟵ candidate
- sequence | constructor | TERM sequence(items: LIST[TERM]) -> TERM | Ordered described activities/content | not: Not unordered conjunction  ⟵ dependency of event_sadie_adler_unmasking
- similarity | constructor | TERM similarity(target: STRING / TERM, dimension?: STRING / TERM) -> TERM | Constructs a descriptor representing comparative closeness or similarity to a target along a given dimension. | not: spatial proximity (use rank_distance or next_to) or an assertion of exact identity (use identity) | aliases: closest_to, similar_to, resembles  ⟵ candidate
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ dependency of argues_for
- test_condition | constructor | TERM test_condition(condition: STRING, expected: BOOL) -> TERM | A testable condition with the expected Boolean outcome | not: Expected outcome is not an observed result  ⟵ candidate
- time_horizon | constructor | TERM time_horizon(horizon: STRING) -> TERM | Constructs a temporal horizon or prospective timeframe descriptor indicating relative temporal distance into the future. | not: a specific calendar timestamp (use time_point) or an elapsed numerical duration (use duration). | aliases: future, future timeframe, time horizon, far off in the future, far future  ⟵ candidate
- vehicle_allowance | constructor | TERM vehicle_allowance(roles: STRING, types: LIST[STRING]) -> TERM | Constructs a specification of permitted vehicle types for defined employee roles. specifies vehicle permissions. | aliases: vehicle_permission  ⟵ candidate
- well_wishes | constructor | TERM well_wishes(recipient?: STRING / TERM, sentiment?: STRING) -> TERM | Constructs a conversational discourse term representing well-wishes, good luck expressions, or parting encouragement. | not: a salutation greeting (use greeting) or apology (use apologize) | aliases: good_luck, best_wishes, encouragement  ⟵ candidate

### composites

- char_female | composite | character-property-value | TERM char_female() -> TERM | Female gender. | = character_trait(property="gender", value="female") | aliases: female  ⟵ candidate
- constraint_beginner | composite | constraint-value | TERM constraint_beginner() -> TERM | Targeted at beginners. | = requirement(property="audience_expertise", value="beginner")  ⟵ candidate
- constraint_budget_limited | composite | constraint-value | TERM constraint_budget_limited() -> TERM | Limited budget. | = requirement(property="budget_limited", value=TRUE)  ⟵ candidate
- constraint_comprehensive | composite | constraint-value | TERM constraint_comprehensive() -> TERM | Must be comprehensive. | = requirement(property="comprehensive", value=TRUE)  ⟵ candidate
- constraint_exclude_flowery_language | composite | constraint-value | TERM constraint_exclude_flowery_language() -> TERM | Avoid flowery language. | = exclude(item="flowery_language")  ⟵ candidate
- constraint_exclude_liberation_theme | composite | constraint-value | TERM constraint_exclude_liberation_theme() -> TERM | Avoid liberation theme. | = exclude(item="liberation_theme")  ⟵ candidate
- constraint_include_character_attribute_list | composite | constraint-value | TERM constraint_include_character_attribute_list() -> TERM | Include character attributes. | = include(item="character_attribute_list")  ⟵ candidate
- constraint_realistic | composite | constraint-value | TERM constraint_realistic() -> TERM | Must be realistic. | = requirement(property="realistic", value=TRUE)  ⟵ candidate
- constraint_respectful | composite | constraint-value | TERM constraint_respectful() -> TERM | Must be respectful. | = requirement(property="respectful", value=TRUE)  ⟵ candidate
- constraint_single_choice | composite | constraint-value | TERM constraint_single_choice() -> TERM | Must pick a single choice. | = requirement(property="choice_count", value=1)  ⟵ candidate
- event_sadie_adler_unmasking | composite | event-value | TERM event_sadie_adler_unmasking() -> TERM | Sadie Adler taking off her hat and peeling skin. | = sequence(items=[activity(verb="remove", actor="Sadie Adler", object="hat"), activity(verb="peel", actor="Sadie Adler", object="skin")])  ⟵ candidate
- topic_current_new_york_housing_market | composite | topic-value | TERM topic_current_new_york_housing_market(as_of: STRING) -> TERM | Current New York housing market. | = subject(kind="housing_market", location="New York", time=$as_of)  ⟵ candidate
- transform_preserve_first_column | composite | transformation-value | TERM transform_preserve_first_column() -> TERM | Preserve the first column of a table. | = preserve(component="column", index=1)  ⟵ candidate
- transform_remove_br | composite | transformation-value | TERM transform_remove_br() -> TERM | Remove <br /> tags. | = remove_literal(text="<br />")  ⟵ candidate

### claim relations

- argues_for | claim_relation | CLAIM argues_for(subject: STRING / TERM, value: STRING / TERM) | Asserts that an actor advocates for or defends a stance, value, or principle. advocacy claim. | aliases: advocates_for  ⟵ candidate
- enables | claim_relation | CLAIM enables(condition: TERM / CLAIM, outcome: TERM / CLAIM) | Asserts that an enabling condition or capability facilitates an outcome. enabling condition. | aliases: facilitates, allows  ⟵ candidate
- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ core
- has_attribute | claim_relation | CLAIM has_attribute(subject: STRING / TERM, attribute: STRING / TERM) | Asserts that an entity, group, or person possesses a stated characteristic or attribute. general characteristic attribution. | aliases: possesses_attribute  ⟵ candidate
- identity | claim_relation | CLAIM identity(subject: STRING / TERM, name: STRING) | Asserts the identified name or persona of an agent or entity. identity assertion. | aliases: agent_name  ⟵ dependency of gender_identity
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ dependency of enables

### links

- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ core
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ core
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ candidate

### values

- art_character_profile | value | artifact-value | Descriptive character profile.  ⟵ candidate
- art_plan | value | artifact-value | Actionable plan.  ⟵ candidate
- art_short_text | value | artifact-value | Short free text.  ⟵ candidate
- art_story | value | artifact-value | Narrative story.  ⟵ candidate
- art_structured_report | value | artifact-value | Headed/structured report.  ⟵ candidate
- path_gcloud_pubsub_subscription_py | value | code-value | File path to the Google Cloud Pub/Sub subscription module. | aliases: gcloud_pubsub_subscription_path  ⟵ candidate
- path_ipython_core_magics_basic_py | value | code-value | File path to the IPython basic magics module. | not: an individual command line script or general config file | aliases: IPython/core/magics/basic.py, ipython_core_magics_basic_py  ⟵ candidate
- path_numpy_core_fromnumeric_py | value | code-value | Source code file path or exported symbol in scientific Python: path_numpy_core_fromnumeric_py. | aliases: path_numpy_core_fromnumeric_py  ⟵ candidate
- path_pandas_src_testing_pyx | value | code-value | Source code file path or exported symbol in scientific Python: path_pandas_src_testing_pyx. | aliases: path_pandas_src_testing_pyx  ⟵ candidate
- path_sklearn_linear_model_logistic_py | value | code-value | The scikit-learn logistic module path.  ⟵ candidate
- sym_pandas_testing_assert_almost_equal | value | code-value | Source code file path or exported symbol in scientific Python: sym_pandas_testing_assert_almost_equal. | aliases: sym_pandas_testing_assert_almost_equal  ⟵ candidate
- cuisine_arab | value | cuisine-value | Arab culinary cuisine style. | not: cuisine_mediterranean (broader regional category) | aliases: Arab food, Arabic food, Arab cuisine  ⟵ candidate
- cuisine_indian | value | cuisine-value | Indian cuisine. | aliases: Indian food, Indian  ⟵ candidate
- cuisine_italian | value | cuisine-value | Italian cuisine. | aliases: Italian food, Italian  ⟵ candidate
- cuisine_mediterranean | value | cuisine-value | Mediterranean culinary cuisine style. | aliases: mediterranean  ⟵ candidate
- cuisine_pizza | value | cuisine-value | Pizza culinary cuisine style and food category. | not: cuisine_italian (broader regional/national cuisine) | aliases: pizza, pizzeria, pizza cuisine  ⟵ candidate
- beliefs | value | descriptive-value | Concept of cognitive beliefs, convictions, or worldviews. | aliases: beliefs  ⟵ candidate
- constitutional_ai | value | descriptive-value | Concept of rule-based constitutional training and self-critique principles in AI alignment. | aliases: constitutional_ai  ⟵ candidate
- dom_ddp | value | descriptive-value | DistributedDataParallel (DDP) multi-GPU distributed training configuration and execution paradigm. | not: dom_ovr (one-versus-rest classification) or platform_label::python (general Python runtime) | aliases: DDP, DistributedDataParallel, distributed data parallel  ⟵ candidate
- personal_values | value | descriptive-value | Concept of personal moral beliefs and subjective ethical commitments. | aliases: personal_values  ⟵ candidate
- tattoos | value | descriptive-value | Descriptive concept of tattoos in cultural and social contexts. | aliases: tattoos  ⟵ candidate
- yakuza | value | descriptive-value | Descriptive concept of yakuza in cultural and social contexts. | aliases: yakuza  ⟵ candidate
- unit_week | value | duration-unit-value | Week. | aliases: weeks  ⟵ candidate
- apple | value | entity-name | An apple fruit item, typically an ingredient or interactive food object. | not: food_label::tomato or other fruits/vegetables | aliases: apple, apples, red apple, green apple, apple slice  ⟵ candidate
- bowl | value | entity-name | A container/dish used for holding food or small items. | aliases: bowl  ⟵ candidate
- bowtie | value | entity-name | Item or prop in joke/creative context: bowtie. | aliases: bowtie  ⟵ candidate
- bread | value | entity-name | A bread loaf or slice food object. | aliases: bread  ⟵ candidate
- chair | value | entity-name | A chair furniture seat with a backrest. | not: object_label::armchair (specifically an object_label::armchair with side armrests) or object_label::sofa | aliases: chair, seat  ⟵ candidate
- cheese | value | entity-name | Dairy food item: cheese. | not: meat or non-dairy food items | aliases: cheese  ⟵ candidate
- cinnamon | value | entity-name | Ground or whole cinnamon culinary spice from Cinnamomum tree bark. | not: nutmeg, cloves, or other distinct spice varieties | aliases: cinnamon, ground cinnamon, cinnamon spice, cinnamon stick  ⟵ candidate
- cloves | value | entity-name | Aromatic dried flower buds of Syzygium aromaticum used as a culinary spice. | not: cinnamon, nutmeg, or other distinct spice varieties | aliases: cloves, clove, ground cloves, whole cloves  ⟵ candidate
- coffee_maker | value | entity-name | A coffee-making appliance; not automatically a heating resource  ⟵ candidate
- desk | value | entity-name | A work desk furniture surface. | aliases: desk  ⟵ candidate
- dog | value | entity-name | Animal entity: dog. | not: animal_label::cat or animal_label::donkey | aliases: dog, dogs, canine, pup, puppy  ⟵ candidate
- door | value | entity-name | A door architectural barrier or entryway. | not: wall or close/open operations | aliases: door, doorway, room door  ⟵ candidate
- dried_fruit | value | entity-name | Generic dried fruit food item. | not: fresh fruit or specific dried varieties like raisin or sultana | aliases: dried fruit, dried fruits  ⟵ candidate
- driver_license | value | entity-name | An official government credential or authorization permitting an individual to operate motor vehicles. | not: vehicle_allowance (an employee vehicle policy) or rental_vehicle (a rental vehicle) | aliases: driver license, driver's license, driving license, driver licence, driver ID  ⟵ candidate
- dulce_de_leche | value | entity-name | Sweet caramelized milk confection or dessert spread: dulce de leche. | not: cheese or dulce_de_nata | aliases: dulce de leche, dulce_de_leche  ⟵ candidate
- earth | value | entity-name | The planet Earth as an astronomical celestial body. | not: soil, ground surface, or electrical grounding | aliases: earth, the earth, planet earth, Earth  ⟵ candidate
- egift_card | value | entity-name | Electronic gift card or digital voucher product. | aliases: digital_gift_card, e_gift_card  ⟵ candidate
- entity_cake | value | entity-name | Event planning item or menu category: entity_cake. | aliases: entity_cake  ⟵ candidate
- entity_checklist | value | entity-name | Event planning item or menu category: entity_checklist. | aliases: entity_checklist  ⟵ candidate
- entity_desserts | value | entity-name | Event planning item or menu category: entity_desserts. | aliases: entity_desserts  ⟵ candidate
- entity_flowers | value | entity-name | Flowers, blossoms, or floral design elements. | not: constraint_exclude_flowery_language (a prose style constraint) or agricultural food items | aliases: flowers, floral, flower, floral decorations  ⟵ candidate
- entity_mains | value | entity-name | Event planning item or menu category: entity_mains. | aliases: entity_mains  ⟵ candidate
- entity_menu_items | value | entity-name | Event planning item or menu category: entity_menu_items. | aliases: entity_menu_items  ⟵ candidate
- entity_sides | value | entity-name | Event planning item or menu category: entity_sides. | aliases: entity_sides  ⟵ candidate
- entity_sweet_food | value | entity-name | Event planning item or menu category: entity_sweet_food. | aliases: entity_sweet_food  ⟵ candidate
- enzyme | value | entity-name | Winemaking enzyme for breaking down fruit cellular structure. | not: living yeast strains or non-enzymatic chemical additives | aliases: enzyme, pectic enzyme, pectinase  ⟵ candidate
- fermentation_nutrient | value | entity-name | Yeast nutrient supplement such as diammonium phosphate (DAP). | not: wine_yeast (the living organism itself) or acid additives | aliases: fermentation nutrient, yeast nutrient, DAP  ⟵ candidate
- fridge | value | entity-name | A refrigerator cooling appliance. | aliases: fridge  ⟵ candidate
- fruit_juice | value | entity-name | Liquid juice extracted from fruit. | not: fermented wine or freshly crushed grape_must | aliases: fruit juice, juice  ⟵ candidate
- ginger | value | entity-name | Pungent aromatic spice root from Zingiber officinale used in cooking and baking. | not: cinnamon, cardamom, or other distinct spice varieties | aliases: ginger, ground ginger, fresh ginger, ginger root  ⟵ candidate
- grape_cabernet_sauvignon | value | entity-name | Cabernet Sauvignon wine grape variety. | not: other red grape varieties such as grape_merlot or grape_pinot_noir | aliases: Cabernet Sauvignon, cabernet, cabernet sauvignon grape  ⟵ candidate
- grape_chardonnay | value | entity-name | Chardonnay wine grape variety. | not: other white grape varieties such as grape_sauvignon_blanc | aliases: Chardonnay, chardonnay grape  ⟵ candidate
- grape_merlot | value | entity-name | Merlot wine grape variety. | not: other red grape varieties such as grape_cabernet_sauvignon or grape_pinot_noir | aliases: Merlot, merlot grape  ⟵ candidate
- grape_must | value | entity-name | Freshly crushed fruit juice mixture before fermentation. | not: clarified fruit_juice or finished wine | aliases: grape must, must  ⟵ candidate
- grape_pinot_noir | value | entity-name | Pinot Noir wine grape variety. | not: other red grape varieties such as grape_cabernet_sauvignon or grape_merlot | aliases: Pinot Noir, pinot noir grape  ⟵ candidate
- grape_sauvignon_blanc | value | entity-name | Sauvignon Blanc wine grape variety. | not: other white grape varieties such as grape_chardonnay | aliases: Sauvignon Blanc, sauvignon blanc grape  ⟵ candidate
- grape_tannin | value | entity-name | Tannin powder derived from grapes for wine structure. | not: oak_chips or wood aging additives | aliases: grape tannin, tannin, wine tannin  ⟵ candidate
- grape_thompson_seedless | value | entity-name | Thompson Seedless grape variety. | not: wine grape cultivars like grape_merlot or grape_chardonnay | aliases: Thompson Seedless, thompson seedless grape, sultana grape  ⟵ candidate
- ice_cream | value | entity-name | Frozen dessert food item: ice cream. | not: entity_desserts or entity_sweet_food (generic menu categories) | aliases: ice cream, ice_cream  ⟵ candidate
- lamp | value | entity-name | A lamp light source appliance. | not: an abstract lighting concept or ambient color | aliases: light, desk_lamp  ⟵ candidate
- laptop | value | entity-name | A portable laptop computer physical object. | not: topic_macbook_pro_2017 (a generation topic label) | aliases: laptop, laptop computer, notebook  ⟵ candidate
- lettuce | value | entity-name | A head of lettuce or leafy green vegetable food item. | not: food_label::tomato or food_label::potato (other vegetable items) | aliases: lettuce, head of lettuce, salad greens  ⟵ candidate
- maqluba | value | entity-name | Traditional Arab layered rice dish: maqluba. | not: cuisine_mediterranean (cuisine style rather than specific dish) | aliases: maqluba, makloubeh  ⟵ candidate
- martini_glass | value | entity-name | A cocktail or Martini drinking glass object. | not: mug (a drinking cup with a handle) or bottle (liquid storage container) | aliases: martini glass, cocktail glass, glass  ⟵ candidate
- microwave | value | entity-name | A microwave oven appliance. | aliases: microwave  ⟵ candidate
- mirror | value | entity-name | A reflective mirror physical object or wall fixture. | not: reflects_light (a constructor describing optical reflection) | aliases: mirror, wall mirror, looking glass  ⟵ candidate
- mittens | value | entity-name | Item or prop in joke/creative context: mittens. | aliases: mittens  ⟵ candidate
- moon | value | entity-name | Earth's natural celestial satellite. | not: an artificial satellite or other planetary moon | aliases: moon, the moon, Luna  ⟵ candidate
- mug | value | entity-name | Drinking cup. | aliases: mug  ⟵ candidate
- oak_chips | value | entity-name | Oak wood pieces or barrels used for wine aging and flavor extraction. | not: grape_tannin or structural chemical additives | aliases: oak chips, oak pieces, oak barrels  ⟵ candidate
- pan | value | entity-name | A metal cooking vessel, frying pan, skillet, saucepan, or pot cookware item used for preparing, heating, or holding food. | not: bowl (deep concave vessel) or plate (shallow flat dining dish) | aliases: pan, frying pan, skillet, saucepan, pot  ⟵ candidate
- pear | value | entity-name | A pear fruit item, typically an ingredient or fresh fruit object. | not: apple, food_label::tomato, or other distinct fruit items | aliases: pear, pears, fresh pear, sliced pear  ⟵ candidate
- raisin | value | entity-name | Dried grape food item. | not: sultana (specifically dried white grape) or fresh wine_grape | aliases: raisin, raisins, dried grape  ⟵ candidate
- remote_control | value | entity-name | A handheld electronic remote control device. | not: an individual button or interactive UI element | aliases: remote, remote control, TV remote, controller  ⟵ candidate
- resource_heater | value | entity-name | Canonical abstract heating resource when no particular appliance is named.  ⟵ candidate
- sultana | value | entity-name | Dried white seedless grape food product. | not: raisin (dark dried grape) or wine_grape | aliases: sultana, sultanas, golden raisin  ⟵ candidate
- sun | value | entity-name | The central star of the Solar System. | not: an artificial lighting appliance or sunlight | aliases: sun, the sun, Sol  ⟵ candidate
- textbook | value | entity-name | A textbook or instructional book used as an educational resource. | not: style_academic (which is a stylistic mode) or art_short_text (which is a brief generated text artifact) | aliases: textbook, book, coursebook, textbooks  ⟵ candidate
- vase | value | entity-name | A decorative or functional open container typically used for holding cut flowers or liquids. | not: bottle (a liquid storage container with a narrow neck) or bowl (a shallow dish) | aliases: vase, flower vase, flower_vase  ⟵ candidate
- waterproof_stickers | value | entity-name | Physical item used for concealment or covering: waterproof_stickers. | aliases: waterproof_stickers  ⟵ candidate
- wine | value | entity-name | Fermented fruit or grape beverage. | not: unfermented fruit juice or distilled alcohol/spirits | aliases: wine, wines  ⟵ candidate
- wine_grape | value | entity-name | Grape variety cultivated specifically for winemaking. | not: table grapes or processed wine product | aliases: wine grape, wine grapes, grape  ⟵ candidate
- wine_yeast | value | entity-name | Yeast strain selected for alcoholic fermentation. | not: baking yeast or fermentation_nutrient | aliases: wine yeast, yeast, fermentation yeast  ⟵ candidate
- yarn | value | entity-name | Item or prop in joke/creative context: yarn. | aliases: yarn  ⟵ candidate
- format_newsletter | value | format-value | Newsletter layout. | aliases: newsletter  ⟵ candidate
- format_numbered_list | value | format-value | Numbered list. | aliases: numbered steps  ⟵ candidate
- locale_es | value | locale-value | Spanish. | aliases: spanish  ⟵ candidate
- locale_fr | value | locale-value | French. | aliases: french  ⟵ candidate
- locale_hi_en | value | locale-value | Hinglish (Hindi-English mix). | aliases: hinglish  ⟵ candidate
- locale_zh | value | locale-value | Chinese language locale (Simplified and Traditional Chinese). | not: a specific geographical region or nationality (use location-name) | aliases: chinese, zh, zh-cn, zh-tw, mandarin  ⟵ candidate
- africa | value | location-name | Geopolitical nation or continental region: africa. | aliases: africa  ⟵ candidate
- corner | value | location-name | A corner area.  ⟵ candidate
- counter | value | location-name | A kitchen or room countertop surface. | aliases: counter  ⟵ candidate
- eastern_cape | value | location-name | Eastern Cape region.  ⟵ candidate
- floor | value | location-name | The floor surface of an indoor room or architectural space. | not: wall (a vertical room boundary surface) or counter (a countertop surface) | aliases: floor, ground  ⟵ candidate
- island | value | location-name | A freestanding kitchen island counter or food preparation work surface. | not: counter (a perimeter countertop surface) or table (a dining or general furniture surface) | aliases: island, kitchen island, kitchen_island  ⟵ candidate
- liberal_onsen | value | location-name | Traditional Japanese establishment or hospitality venue: liberal_onsen. | aliases: liberal_onsen  ⟵ candidate
- living_room | value | location-name | A residential room or general indoor living area. | not: floor (a floor surface) or wall (a vertical boundary surface) | aliases: living room, living_room, sitting room, lounge  ⟵ candidate
- microwave_stand | value | location-name | A dedicated stand or cart supporting a microwave. | aliases: microwave_stand  ⟵ candidate
- new_york_university | value | location-name | New York University institution or campus grounds. | aliases: nyu  ⟵ candidate
- night_stand | value | location-name | A small bedside table or nightstand furniture surface. | not: a chest of drawers (use dresser) or a general table surface (use table) | aliases: nightstand, bedside table  ⟵ candidate
- russia | value | location-name | Geopolitical nation or continental region: russia. | aliases: russia  ⟵ candidate
- united_kingdom | value | location-name | Geopolitical nation or sovereign state: United Kingdom (Great Britain). | not: locale_en_gb (a language/locale code, not a location) | aliases: United Kingdom, UK, Great Britain, Britain  ⟵ candidate
- wall | value | location-name | A room boundary wall surface. | aliases: wall  ⟵ candidate
- metric_repeat_buyer | value | metric-value | Whether the customer is a repeat buyer. | aliases: repeat buyer, returning customer  ⟵ candidate
- metric_socio_economic_status | value | metric-value | Socio-economic status (SES) composite metric, index, or classification tier. | not: a specific income currency amount (use measure) or customer purchase metric (use metric_first_time_buyer) | aliases: SES, socio-economic status, socioeconomic status, wealth index  ⟵ candidate
- metric_uptime | value | metric-value | Service uptime status. | aliases: uptime, is up  ⟵ candidate
- color_pink | value | product-attribute-value | Pink visual color qualifier. | not: color_label::red, color_label::purple, or other distinct color shades | aliases: pink, color_pink, blush pink, rose pink, pastel pink  ⟵ candidate
- material_memory_foam | value | product-attribute-value | Memory foam viscoelastic polyurethane material qualifier. | not: sponge (a porous cleaning tool) or generic bedding | aliases: memory foam, memory_foam, viscoelastic foam  ⟵ candidate
- valet | value | product-attribute-value | Valet parking or dedicated vehicle attendant service. | aliases: valet_parking  ⟵ candidate
- role_agent | value | recipient-value | The assistant. | aliases: you, the assistant  ⟵ candidate
- role_colleague | value | recipient-value | A coworker of the user. | aliases: my colleague, coworker  ⟵ candidate
- role_daughter | value | recipient-value | Daughter participant role in family or travel context. | not: role_sister, role_mother, or generic role_kids | aliases: daughter, my daughter  ⟵ candidate
- role_manager | value | recipient-value | The user's manager. | aliases: my manager, boss  ⟵ candidate
- role_mother | value | recipient-value | The mother of the user. | not: role_sister or role_kids | aliases: my mom, mother, mom  ⟵ candidate
- role_professor | value | recipient-value | The user's professor/instructor. | aliases: my professor, teacher  ⟵ candidate
- role_sister | value | recipient-value | Sister participant role in family/event context. | aliases: sister  ⟵ candidate
- role_son | value | recipient-value | Son participant role in family or travel context. | not: role_daughter, role_sister, role_mother, or generic role_kids | aliases: son, my son  ⟵ candidate
- role_support_team | value | recipient-value | A customer-support team. | aliases: support, customer service  ⟵ candidate
- tattooed_guests | value | recipient-value | Social, demographic, or institutional group: tattooed_guests. | aliases: tattooed_guests  ⟵ candidate
- cat_game | value | search-value | Category: video game.  ⟵ candidate
- dir_asc | value | search-value | Ascending rank direction. | aliases: lowest first  ⟵ candidate
- dir_desc | value | search-value | Descending rank direction. | aliases: highest first  ⟵ candidate
- rank_distance | value | search-value | Rank field: proximity. | aliases: nearest, closest  ⟵ candidate
- rank_price | value | search-value | Rank or filter field: monetary cost. | aliases: cheapest, lowest price  ⟵ candidate
- class_beach | value | semantic-category-value | The abstract class or category of beach destinations and coastal environments. | not: island (kitchen island work surface) or a specific named beach location | aliases: beach, beaches, beach destination, seaside  ⟵ candidate
- class_temple | value | semantic-category-value | The abstract class of temples. | aliases: temple, temples  ⟵ candidate
- shape_oval | value | shape-value | Oval. | aliases: oval  ⟵ candidate
- shape_round | value | shape-value | Circular/round. | aliases: round, circular  ⟵ candidate
- shape_triangular | value | shape-value | Triangular. | aliases: triangular, triangle  ⟵ candidate
- behind | value | spatial-relation | Positioned behind.  ⟵ candidate
- between | value | spatial-relation | Positioned between or in the middle of reference entities. | not: next_to or in_front_of | aliases: between, in the middle of, middle of, center of  ⟵ candidate
- in_front_of | value | spatial-relation | Positioned in front of. | aliases: in front of  ⟵ candidate
- left_of | value | spatial-relation | To the left of. | aliases: left of  ⟵ candidate
- next_to | value | spatial-relation | Adjacent to. | aliases: beside  ⟵ candidate
- on | value | spatial-relation | Resting atop. | aliases: on top of  ⟵ candidate
- other_side_of | value | spatial-relation | Positioned on the opposite or other side of a reference object. | not: next_to (which indicates general adjacency) | aliases: other side, other side of, opposite side of, opposite side  ⟵ candidate
- right_of | value | spatial-relation | To the right of. | aliases: right of  ⟵ candidate
- state_microwaved | value | state-value | Has been microwaved. | aliases: microwaved  ⟵ candidate
- state_upright | value | state-value | An upright or vertically standing physical state of an object. | not: stand_up (which is an agent posture operation) | aliases: standing up, upright, vertical  ⟵ candidate
- style_catchy | value | style-value | Catchy, attention-grabbing style. | aliases: catchy  ⟵ candidate
- style_narrative | value | style-value | Story-like narrative style. | aliases: narrative, story-style  ⟵ candidate
- style_persuasive | value | style-value | Persuasive/argumentative style. | aliases: persuasive  ⟵ candidate
- tone_empathetic | value | tone-value | Conveys empathy/understanding. | aliases: sympathetically  ⟵ candidate
- topic_baldurs_gate_3 | value | topic-value | Baldur's Gate 3.  ⟵ candidate
- topic_classical_piano | value | topic-value | Classical piano.  ⟵ candidate
- topic_macbook_pro_2017 | value | topic-value | MacBook Pro 2017.  ⟵ candidate
- topic_pickup_lines | value | topic-value | Pickup lines.  ⟵ candidate
- topic_spider_man_2 | value | topic-value | Marvel's Spider-Man 2.  ⟵ candidate
- unit_gram | value | unit-value | Standard metric measurement unit of mass equal to 1/1,000 of a kilogram (0.001 kg). | not: digital capacity units (like cap_gb) or temporal duration units | aliases: g, gram, grams  ⟵ candidate

### attributes

- min_ram | attribute | attribute-name | Minimum RAM capacity as NUMBER. | aliases: RAM or more, at least RAM  ⟵ candidate
- ram_unit | attribute | attribute-name | Unit for min_ram from capacity-unit-value.  ⟵ candidate
- rank_direction | attribute | attribute-name | Sort direction from search-value.  ⟵ candidate
