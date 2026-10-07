# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 72 needs (decomposition: llm), 162 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | speech_act | t1:s1 | Introduce a set of premises or a theory | `respond`, `propose`, `subject`, `in_front_of`, `ask`, `inform`, `supports`, `conjunction`, `example_of`, `express_interest`, `confirm`, `rule_structural_constructs` |
| n2 | claim | t1:s2 | Bob is green | `lettuce`, `color_label`, `leads_to`, `enables`, `outcome`, `right_of`, `causes`, `motivated_by`, `outshines`, `in_front_of`, `topic_spider_man_2`, `bionic_person` |
| n3 | object | t1:s2 | Bob → `object_label::<key>` | `resource_sink`, `bread`, `in_front_of`, `role_professor`, `right_of`, `left_of`, `behind`, `on`, `bowtie`, `object_label`*, `resource_chiller`, `topic_spider_man_2` |
| n4 | constraint | t1:s2 | green → `color_label::<key>` | `color_label`*, `lettuce`, `outshines`, `grape_thompson_seedless`, `right_of`, `apple`, `left_of`, `constraint_exclude_flowery_language`, `sultana`, `constraint_respectful`, `locale_en_gb`, `constraint_exclude_liberation_theme` |
| n5 | claim | t1:s3 | Bob is white | `outcome`, `unit_word`, `enables`, `leads_to`, `role_professor`, `in_front_of`, `bionic_person`, `occurred_recently`, `causes`, `state_dirty`, `motivated_by`, `resource_sink` |
| n6 | object | t1:s3 | Bob → `object_label::<key>` | `resource_sink`, `bread`, `in_front_of`, `role_professor`, `right_of`, `left_of`, `behind`, `on`, `bowtie`, `object_label`*, `resource_chiller`, `topic_spider_man_2` |
| n7 | constraint | t1:s3 | white → `color_label::<key>` | `color_label`*, `unit_word`, `sultana`, `gender_unisex`, `constraint_exclude_flowery_language`, `state_dirty`, `on`, `dulce_de_leche`, `constraint_respectful`, `dulce_de_nata`, `locale_en_gb`, `constraint_exclude_liberation_theme` |
| n8 | claim | t1:s4 | Dave is blue | `color_label`, `enables`, `outcome`, `yarn`, `leads_to`, `mod_mixed_case`, `grape_thompson_seedless`, `chill`, `bowtie`, `lettuce`, `occurred_recently`, `yakuza` |
| n9 | object | t1:s4 | Dave → `object_label::<key>` | `resource_chiller`, `chill`, `yarn`, `on`, `bowtie`, `object_label`*, `resource_sink`, `liberal_onsen`, `candle`, `coffee_maker`, `resource_heater`, `rule_category_entity_name` |
| n10 | constraint | t1:s4 | blue → `color_label::<key>` | `color_label`*, `yakuza`, `lettuce`, `sultana`, `grape_merlot`, `right_of`, `constraint_exclude_flowery_language`, `constraint_respectful`, `dried_fruit`, `on`, `constraint_exclude_liberation_theme`, `mug` |
| n11 | claim | t1:s5 | Dave is cold | `state_cold`*, `yarn`, `chill`, `outcome`, `leads_to`, `enables`, `event_sadie_adler_unmasking`, `state_dirty`, `causes`, `resource_chiller`, `mittens`, `motivated_by` |
| n12 | object | t1:s5 | Dave → `object_label::<key>` | `resource_chiller`, `chill`, `yarn`, `on`, `bowtie`, `object_label`*, `resource_sink`, `liberal_onsen`, `candle`, `coffee_maker`, `resource_heater`, `rule_category_entity_name` |
| n13 | constraint | t1:s5 | cold | `state_cold`*, `state_warm`, `weather_condition`, `mittens`, `state_dirty`, `cinnamon`, `constraint_exclude_flowery_language`, `resource_chiller`, `chill`, `ice_cream`, `constraint_exclude_liberation_theme`, `constraint_respectful` |
| n14 | claim | t1:s6 | Dave is green | `lettuce`, `color_label`, `outshines`, `grape_thompson_seedless`, `outcome`, `enables`, `leads_to`, `apple`, `yarn`, `causes`, `grape_tannin`, `motivated_by` |
| n15 | object | t1:s6 | Dave → `object_label::<key>` | `resource_chiller`, `chill`, `yarn`, `on`, `bowtie`, `object_label`*, `resource_sink`, `liberal_onsen`, `candle`, `coffee_maker`, `resource_heater`, `rule_category_entity_name` |
| n16 | constraint | t1:s6 | green → `color_label::<key>` | `color_label`*, `lettuce`, `outshines`, `grape_thompson_seedless`, `right_of`, `apple`, `left_of`, `constraint_exclude_flowery_language`, `sultana`, `constraint_respectful`, `locale_en_gb`, `constraint_exclude_liberation_theme` |
| n17 | claim | t1:s7 | Dave is white | `outcome`, `color_label`, `outshines`, `enables`, `leads_to`, `unit_word`, `yarn`, `gender_unisex`, `causes`, `on`, `motivated_by`, `bionic_person` |
| n18 | object | t1:s7 | Dave → `object_label::<key>` | `resource_chiller`, `chill`, `yarn`, `on`, `bowtie`, `object_label`*, `resource_sink`, `liberal_onsen`, `candle`, `coffee_maker`, `resource_heater`, `rule_category_entity_name` |
| n19 | constraint | t1:s7 | white → `color_label::<key>` | `color_label`*, `unit_word`, `sultana`, `gender_unisex`, `constraint_exclude_flowery_language`, `state_dirty`, `on`, `dulce_de_leche`, `constraint_respectful`, `dulce_de_nata`, `locale_en_gb`, `constraint_exclude_liberation_theme` |
| n20 | claim | t1:s8 | Fiona is cold | `state_cold`*, `yarn`, `event_sadie_adler_unmasking`, `outcome`, `chill`, `cinnamon`, `character_trait`, `state_dirty`, `enables`, `leads_to`, `gender_unisex`, `motivated_by` |
| n21 | object | t1:s8 | Fiona → `object_label::<key>` | `chill`, `yarn`, `event_sadie_adler_unmasking`, `role_sister`, `on`, `style_catchy`, `role_mother`, `bowtie`, `right_of`, `art_story`, `object_label`*, `resource_sink` |
| n22 | constraint | t1:s8 | cold | `state_cold`*, `state_warm`, `weather_condition`, `mittens`, `state_dirty`, `cinnamon`, `constraint_exclude_flowery_language`, `resource_chiller`, `chill`, `ice_cream`, `constraint_exclude_liberation_theme`, `constraint_respectful` |
| n23 | claim | t1:s9 | Fiona is green | `lettuce`, `color_label`, `color_pink`, `yarn`, `grape_thompson_seedless`, `outcome`, `enables`, `leads_to`, `apple`, `outshines`, `causes`, `motivated_by` |
| n24 | object | t1:s9 | Fiona → `object_label::<key>` | `chill`, `yarn`, `event_sadie_adler_unmasking`, `role_sister`, `on`, `style_catchy`, `role_mother`, `bowtie`, `right_of`, `art_story`, `object_label`*, `resource_sink` |
| n25 | constraint | t1:s9 | green → `color_label::<key>` | `color_label`*, `lettuce`, `outshines`, `grape_thompson_seedless`, `right_of`, `apple`, `left_of`, `constraint_exclude_flowery_language`, `sultana`, `constraint_respectful`, `locale_en_gb`, `constraint_exclude_liberation_theme` |
| n26 | claim | t1:s10 | Fiona is white | `color_label`, `char_female`, `gender_unisex`, `sym_pandas_testing_assert_almost_equal`, `outcome`, `enables`, `yarn`, `leads_to`, `color_pink`, `event_sadie_adler_unmasking`, `rule_category_product_attribute_value`, `occurred_recently` |
| n27 | object | t1:s10 | Fiona → `object_label::<key>` | `chill`, `yarn`, `event_sadie_adler_unmasking`, `role_sister`, `on`, `style_catchy`, `role_mother`, `bowtie`, `right_of`, `art_story`, `object_label`*, `resource_sink` |
| n28 | constraint | t1:s10 | white → `color_label::<key>` | `color_label`*, `unit_word`, `sultana`, `gender_unisex`, `constraint_exclude_flowery_language`, `state_dirty`, `on`, `dulce_de_leche`, `constraint_respectful`, `dulce_de_nata`, `locale_en_gb`, `constraint_exclude_liberation_theme` |
| n29 | claim | t1:s11 | Fiona is young | `yarn`, `enables`, `outcome`, `leads_to`, `character_trait`, `role_mother`, `constraint_17_plus`, `role_sister`, `topic_profanity`, `occurred_recently`, `motivated_by`, `size_small` |
| n30 | object | t1:s11 | Fiona → `object_label::<key>` | `chill`, `yarn`, `event_sadie_adler_unmasking`, `role_sister`, `on`, `style_catchy`, `role_mother`, `bowtie`, `right_of`, `art_story`, `object_label`*, `resource_sink` |
| n31 | constraint | t1:s11 | young | `constraint_budget_limited`, `topic_profanity`, `constraint_17_plus`, `size_small`, `role_kids`, `constraint_exclude_flowery_language`, `under`, `constraint_respectful`, `unit_sentence`, `constraint_include_character_attribute_list`, `constraint_exclude_liberation_theme`, `role_mother` |
| n32 | claim | t1:s12 | Gary is kind | `enables`, `comfortable`, `right_of`, `outcome`, `leads_to`, `lettuce`, `causes`, `motivated_by`, `recommended`, `tone_empathetic`, `well_wishes`, `important` |
| n33 | object | t1:s12 | Gary → `object_label::<key>` | `chill`, `right_of`, `on`, `in_front_of`, `left_of`, `topic_baldurs_gate_3`, `next_to`, `state_dirty`, `resource_sink`, `resource_chiller`, `object_label`*, `topic_greatest_cricketer_of_all_time` |
| n34 | constraint | t1:s12 | kind | `style_catchy`, `right_of`, `well_wishes`, `constraint_exclude_flowery_language`, `similarity`, `character_trait`, `tone_polite`, `constraint_respectful`, `style_persuasive`, `constraint_include_character_attribute_list`, `next_to`, `constraint_budget_limited` |
| n35 | claim | t1:s13 | Gary is white | `color_label`, `outcome`, `enables`, `color_pink`, `unit_word`, `gender_unisex`, `leads_to`, `on`, `occurred_recently`, `causes`, `motivated_by`, `statement` |
| n36 | object | t1:s13 | Gary → `object_label::<key>` | `chill`, `right_of`, `on`, `in_front_of`, `left_of`, `topic_baldurs_gate_3`, `next_to`, `state_dirty`, `resource_sink`, `resource_chiller`, `object_label`*, `topic_greatest_cricketer_of_all_time` |
| n37 | constraint | t1:s13 | white → `color_label::<key>` | `color_label`*, `unit_word`, `sultana`, `gender_unisex`, `constraint_exclude_flowery_language`, `state_dirty`, `on`, `dulce_de_leche`, `constraint_respectful`, `dulce_de_nata`, `locale_en_gb`, `constraint_exclude_liberation_theme` |
| n38 | reasoning | t1:s14 | If a person is cold and white, then they are furry | `state_cold`*, `comfortable`, `then`*, `stereotype`, `char_female`, `bionic_person`, `dog`, `gender_identity`, `rejects`, `event_sadie_adler_unmasking`, `gender_unisex`, `supports` |
| n39 | constraint | t1:s14 | cold | `state_cold`*, `state_warm`, `weather_condition`, `mittens`, `state_dirty`, `cinnamon`, `constraint_exclude_flowery_language`, `resource_chiller`, `chill`, `ice_cream`, `constraint_exclude_liberation_theme`, `constraint_respectful` |
| n40 | constraint | t1:s14 | white → `color_label::<key>` | `color_label`*, `unit_word`, `sultana`, `gender_unisex`, `constraint_exclude_flowery_language`, `state_dirty`, `on`, `dulce_de_leche`, `constraint_respectful`, `dulce_de_nata`, `locale_en_gb`, `constraint_exclude_liberation_theme` |
| n41 | constraint | t1:s14 | furry | `cat_limited_time_offers`, `dog`, `yarn`, `event_sadie_adler_unmasking`, `style_catchy`, `cat_game`, `caddy`, `animal_label`, `constraint_exclude_flowery_language`, `state_cold`, `constraint_include_character_attribute_list`, `constraint_respectful` |
| n42 | reasoning | t1:s15 | If a person is furry, then they are green | `lettuce`, `bionic_person`, `apple`, `then`*, `stereotype`, `color_label`, `rejects`, `dog`, `comfortable`, `supports`, `yarn`, `style_catchy` |
| n43 | constraint | t1:s15 | furry | `cat_limited_time_offers`, `dog`, `yarn`, `event_sadie_adler_unmasking`, `style_catchy`, `cat_game`, `caddy`, `animal_label`, `constraint_exclude_flowery_language`, `state_cold`, `constraint_include_character_attribute_list`, `constraint_respectful` |
| n44 | constraint | t1:s15 | green → `color_label::<key>` | `color_label`*, `lettuce`, `outshines`, `grape_thompson_seedless`, `right_of`, `apple`, `left_of`, `constraint_exclude_flowery_language`, `sultana`, `constraint_respectful`, `locale_en_gb`, `constraint_exclude_liberation_theme` |
| n45 | reasoning | t1:s16 | If a person is cold, then they are young | `state_cold`*, `then`*, `rejects`, `topic_profanity`, `character_trait`, `bionic_person`, `comfortable`, `supports`, `mittens`, `chill`, `constraint_17_plus`, `contrast` |
| n46 | constraint | t1:s16 | cold | `state_cold`*, `state_warm`, `weather_condition`, `mittens`, `state_dirty`, `cinnamon`, `constraint_exclude_flowery_language`, `resource_chiller`, `chill`, `ice_cream`, `constraint_exclude_liberation_theme`, `constraint_respectful` |
| n47 | constraint | t1:s16 | young | `constraint_budget_limited`, `topic_profanity`, `constraint_17_plus`, `size_small`, `role_kids`, `constraint_exclude_flowery_language`, `under`, `constraint_respectful`, `unit_sentence`, `constraint_include_character_attribute_list`, `constraint_exclude_liberation_theme`, `role_mother` |
| n48 | reasoning | t1:s17 | If a person is kind and young, then they are blue | `color_label`, `then`*, `stereotype`, `yakuza`, `topic_profanity`, `rejects`, `grape_merlot`, `comfortable`, `bionic_person`, `character_trait`, `supports`, `right_of` |
| n49 | constraint | t1:s17 | kind | `style_catchy`, `right_of`, `well_wishes`, `constraint_exclude_flowery_language`, `similarity`, `character_trait`, `tone_polite`, `constraint_respectful`, `style_persuasive`, `constraint_include_character_attribute_list`, `next_to`, `constraint_budget_limited` |
| n50 | constraint | t1:s17 | young | `constraint_budget_limited`, `topic_profanity`, `constraint_17_plus`, `size_small`, `role_kids`, `constraint_exclude_flowery_language`, `under`, `constraint_respectful`, `unit_sentence`, `constraint_include_character_attribute_list`, `constraint_exclude_liberation_theme`, `role_mother` |
| n51 | constraint | t1:s17 | blue → `color_label::<key>` | `color_label`*, `yakuza`, `lettuce`, `sultana`, `grape_merlot`, `right_of`, `constraint_exclude_flowery_language`, `constraint_respectful`, `dried_fruit`, `on`, `constraint_exclude_liberation_theme`, `mug` |
| n52 | reasoning | t1:s18 | If a person is furry, then they are blue | `color_label`, `then`*, `stereotype`, `yarn`, `dog`, `bionic_person`, `rejects`, `yakuza`, `comfortable`, `char_female`, `character_trait`, `supports` |
| n53 | constraint | t1:s18 | furry | `cat_limited_time_offers`, `dog`, `yarn`, `event_sadie_adler_unmasking`, `style_catchy`, `cat_game`, `caddy`, `animal_label`, `constraint_exclude_flowery_language`, `state_cold`, `constraint_include_character_attribute_list`, `constraint_respectful` |
| n54 | constraint | t1:s18 | blue → `color_label::<key>` | `color_label`*, `yakuza`, `lettuce`, `sultana`, `grape_merlot`, `right_of`, `constraint_exclude_flowery_language`, `constraint_respectful`, `dried_fruit`, `on`, `constraint_exclude_liberation_theme`, `mug` |
| n55 | reasoning | t1:s19 | If a person is white and kind, then they are young | `then`*, `stereotype`, `char_female`, `topic_profanity`, `rejects`, `character_trait`, `outshines`, `bionic_person`, `gender_men`, `comfortable`, `supports`, `tone_polite` |
| n56 | constraint | t1:s19 | white → `color_label::<key>` | `color_label`*, `unit_word`, `sultana`, `gender_unisex`, `constraint_exclude_flowery_language`, `state_dirty`, `on`, `dulce_de_leche`, `constraint_respectful`, `dulce_de_nata`, `locale_en_gb`, `constraint_exclude_liberation_theme` |
| n57 | constraint | t1:s19 | kind | `style_catchy`, `right_of`, `well_wishes`, `constraint_exclude_flowery_language`, `similarity`, `character_trait`, `tone_polite`, `constraint_respectful`, `style_persuasive`, `constraint_include_character_attribute_list`, `next_to`, `constraint_budget_limited` |
| n58 | constraint | t1:s19 | young | `constraint_budget_limited`, `topic_profanity`, `constraint_17_plus`, `size_small`, `role_kids`, `constraint_exclude_flowery_language`, `under`, `constraint_respectful`, `unit_sentence`, `constraint_include_character_attribute_list`, `constraint_exclude_liberation_theme`, `role_mother` |
| n59 | reasoning | t1:s20 | If a person is kind and blue, then they are cold | `state_cold`*, `comfortable`, `then`*, `color_label`, `character_trait`, `right_of`, `bionic_person`, `rejects`, `chill`, `supports`, `style_catchy`, `contrast` |
| n60 | constraint | t1:s20 | kind | `style_catchy`, `right_of`, `well_wishes`, `constraint_exclude_flowery_language`, `similarity`, `character_trait`, `tone_polite`, `constraint_respectful`, `style_persuasive`, `constraint_include_character_attribute_list`, `next_to`, `constraint_budget_limited` |
| n61 | constraint | t1:s20 | blue → `color_label::<key>` | `color_label`*, `yakuza`, `lettuce`, `sultana`, `grape_merlot`, `right_of`, `constraint_exclude_flowery_language`, `constraint_respectful`, `dried_fruit`, `on`, `constraint_exclude_liberation_theme`, `mug` |
| n62 | constraint | t1:s20 | cold | `state_cold`*, `state_warm`, `weather_condition`, `mittens`, `state_dirty`, `cinnamon`, `constraint_exclude_flowery_language`, `resource_chiller`, `chill`, `ice_cream`, `constraint_exclude_liberation_theme`, `constraint_respectful` |
| n63 | reasoning | t1:s21 | If Bob is blue, then Bob is kind | `color_label`, `then`*, `right_of`, `style_catchy`, `supports`, `rejects`, `grape_merlot`, `yakuza`, `constraint_respectful`, `in_front_of`, `contrast`, `revises` |
| n64 | object | t1:s21 | Bob → `object_label::<key>` | `resource_sink`, `bread`, `in_front_of`, `role_professor`, `right_of`, `left_of`, `behind`, `on`, `bowtie`, `object_label`*, `resource_chiller`, `topic_spider_man_2` |
| n65 | constraint | t1:s21 | blue → `color_label::<key>` | `color_label`*, `yakuza`, `lettuce`, `sultana`, `grape_merlot`, `right_of`, `constraint_exclude_flowery_language`, `constraint_respectful`, `dried_fruit`, `on`, `constraint_exclude_liberation_theme`, `mug` |
| n66 | constraint | t1:s21 | kind | `style_catchy`, `right_of`, `well_wishes`, `constraint_exclude_flowery_language`, `similarity`, `character_trait`, `tone_polite`, `constraint_respectful`, `style_persuasive`, `constraint_include_character_attribute_list`, `next_to`, `constraint_budget_limited` |
| n67 | speech_act | t1:s22 | Ask whether a statement is True, False, or Unknown | `ask`*, `statement`*, `confirm`, `respond`, `failure`, `unaware`, `negation`, `inform`, `propose`, `correct`, `motivated_by`, `rejects` |
| n68 | constraint | t1:s22 | Rely only on the provided theory | `constraint_realistic`, `subject`, `constraint_exclude_flowery_language`, `constraint_respectful`, `constraint_include_character_attribute_list`, `constraint_budget_limited`, `supports`, `failure`, `causes`, `constraint_exclude_liberation_theme`, `rejects`, `regression_case` |
| n69 | constraint | t1:s22 | Answer must be True, False, or Unknown | `constraint_realistic`, `right_of`, `constraint_exclude_flowery_language`, `constraint_respectful`, `metric_order_late`, `constraint_include_character_attribute_list`, `rejects`, `constraint_budget_limited`, `failure`, `respond`*, `constraint_exclude_liberation_theme`, `entity_flowers` |
| n70 | claim | t1:s23 | Bob is kind (statement to evaluate) | `comfortable`, `statement`*, `recommended`, `enables`, `important`, `outcome`, `considered`, `leads_to`, `right_of`, `motivated_by`, `causes`, `style_catchy` |
| n71 | object | t1:s23 | Bob → `object_label::<key>` | `resource_sink`, `bread`, `in_front_of`, `role_professor`, `right_of`, `left_of`, `behind`, `on`, `bowtie`, `object_label`*, `resource_chiller`, `topic_spider_man_2` |
| n72 | constraint | t1:s23 | kind | `style_catchy`, `right_of`, `well_wishes`, `constraint_exclude_flowery_language`, `similarity`, `character_trait`, `tone_polite`, `constraint_respectful`, `style_persuasive`, `constraint_include_character_attribute_list`, `next_to`, `constraint_budget_limited` |

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
- chill.destination → object_label
- weather_condition.location → country
- failure.system → platform_label
- regression_case.framework → platform_label
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

**rule_recording_signatures** (v19/rule/recording-signatures; rule governing chill)

RECORD ACTION uses the operation signature with REF[STRING] → TERM and LIST[REF[STRING]] → LIST[TERM]; other types/categories stay unchanged. Return EVENT, never the runtime result. Record actual outputs as attributed CLAIMs. Do not infer missing resources.

**rule_speech_acts_general** (v19/rule/speech-acts-general; rule governing respond)

UTTER-only, void, with the spec's speech attributes and LIST[TERM] constraints. No result binding. Literal content cannot replace required semantic arguments for structured coverage.

**rule_structural_constructs** (v19/rule/structural-constructs; candidate)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; rule governing supports)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_attributes_and_generate** (v19/rule/attributes-and-generate; rule governing art_story)

Attribute entries name arguments; legality/types come from each operation, not global membership. GENERATE uses the spec's core fields; retained artifact profiles return STRING. Numeric/list results need explicit profiles. Legacy itinerary fields expand to TERM constraints: duration/duration_unit → duration(amount,unit); stop_min_per_day/stop_requirement → minimum_per_period(class,count,period=unit_day), never an inferred temple class; max_walk_duration/unit → maximum_between_stops(activity="walk",amount,unit). No legacy shorthand is enabled. Old events/character_properties/transformations become explicitly scoped TERM constraints. Message purpose is TERM, not send_email.content: GENERATE exact STRING content, then send. Report opaque fallback separately.

**rule_category_artifact_value** (v19/rule/category/artifact-value; rule governing art_story)

STRING artifact class for GENERATE.target. art_story says what kind of artifact to produce, not what occurs in its plot.

**rule_category_character_property_value** (v19/rule/category/character-property-value; rule governing char_female)

TERM-described trait/style. Use constraints and explicit inclusion/scope; do not use an ungoverned character_properties attribute.

**rule_category_code_value** (v19/rule/category/code-value; rule governing sym_pandas_testing_assert_almost_equal)

path_/sym_ remain STRING identities; migrated chg_/assert_ are TERM constructors. Do not recover an exact file path by guessing from underscores.

**rule_category_constraint_value** (v19/rule/category/constraint-value; rule governing constraint_exclude_flowery_language)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_descriptive_value** (v19/rule/category/descriptive-value; rule governing mod_mixed_case)

STRING modifier/domain label; never a free-form proposition. dom_sgi needs its intended referent established before semantically dependent use.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; rule governing unit_word)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; candidate)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_event_value** (v19/rule/category/event-value; rule governing event_sadie_adler_unmasking)

TERM-described narrative event, not a recorded EVENT. Require inclusion explicitly when generating a story.

**rule_category_locale_value** (v19/rule/category/locale-value; rule governing locale_en_gb)

STRING locale. “English” alone does not always mean locale_en_us; preserve ambiguity.

**rule_category_location_name** (v19/rule/category/location-name; rule governing liberal_onsen)

STRING location descriptor. A `table` surface is not the generated artifact category art_table.

**rule_category_metric_value** (v19/rule/category/metric-value; rule governing metric_order_late)

STRING metric identity, not a Boolean value. Uptime and response time need numeric observations with units; order-late is Boolean-valued. Do not type every metric as BOOL.

**rule_category_product_attribute_value** (v19/rule/category/product-attribute-value; candidate)

STRING color/size/product-market facets. gender_women describes a product category, not an assertion about a person's gender.

**rule_category_recipient_value** (v19/rule/category/recipient-value; rule governing role_professor)

STRING roles or explicit named recipients. A role is not an exact person's identity. Keep an explicit name where substituting a role loses information.

**rule_category_search_value** (v19/rule/category/search-value; rule governing cat_limited_time_offers)

STRING refinements rank_ / dir_ / cat_ / avail_ / genre_ are separate. rank_rating may fill rank_field; genre_label::comedy may not. “Cheapest” usually requires both rank_price and dir_asc, not rank_price alone.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing in_front_of)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_state_value** (v19/rule/category/state-value; rule governing state_dirty)

STRING condition used in selection. state_warm does not command heat; “hot” is not automatically synonymous with “warm.”

**rule_category_style_value** (v19/rule/category/style-value; rule governing style_catchy)

STRING production style. style_narrative does not establish that described events occurred.

**rule_category_tone_value** (v19/rule/category/tone-value; rule governing tone_empathetic)

STRING register. tone_urgent describes urgency, not a concrete deadline.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_spider_man_2)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_composites_general** (v19/rule/composites-general; rule governing constraint_exclude_flowery_language)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_operations_general** (v19/rule/operations-general; rule governing chill)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_supplemental_general** (v19/rule/supplemental-general; rule governing coffee_maker)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; rule governing subject)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- chill | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Chill using the stated resource; same identity.  ⟵ candidate
- turn | operation | operation-vocabulary | (direction: STRING) -> void | Rotate agent body/view orientation. direction is typically left, right, or angle. | aliases: rotate, turn_around  ⟵ related to then
- walk | operation | operation-vocabulary | (destination: STRING / TERM / ATOM[object_label], relation?: STRING) -> void | Locomote towards a target destination or landmark. destination must identify a valid entity or location. | aliases: move_to, go_to, navigate_to  ⟵ related to then

### speech acts

- ask | speech_act | operation-vocabulary | UTTER ask(target: TERM, or a sufficiently precise topic: STRING / TERM) | Request information/advice; not an assertion of an answer. | aliases: ask, how should  ⟵ candidate
- confirm | speech_act | operation-vocabulary | UTTER confirm(target: CLAIM) | Confirm the proposition; its evidence/status remains explicit.  ⟵ candidate
- correct | speech_act | operation-vocabulary | UTTER correct(target: CLAIM) | Offer corrected content. Actual supersession requires the Conversation revision rules.  ⟵ candidate
- express_interest | speech_act | operation-vocabulary | UTTER express_interest(target: STRING / TERM) | Speech act expressing conversational interest or engagement in a topic. speech act in dialogic traces. | aliases: show_interest  ⟵ candidate
- inform | speech_act | operation-vocabulary | UTTER inform(target: CLAIM) | Present the proposition; preserve its holder/status.  ⟵ candidate
- propose | speech_act | operation-vocabulary | UTTER propose(target: TERM) | Suggest an action/idea; does not record it as performed.  ⟵ candidate
- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ dependency of event_sadie_adler_unmasking
- bionic_person | constructor | TERM bionic_person(composition?: STRING / TERM) -> TERM | Constructs a descriptive representation of a bionic person or cyborg entity with biological and mechanical components. | not: a standard human role (use role_user or role_adults) or a purely artificial device. | aliases: bionic person, bionic people, cyborg, half human half robot  ⟵ candidate
- character_trait | constructor | TERM character_trait(property: STRING, value: STRING / NUMBER) -> TERM | A character attribute | not: Not a claim about a real person  ⟵ candidate
- conditional | constructor | TERM conditional(condition: TERM, consequence: TERM) -> TERM | Constructs a structured conditional proposition term connecting a condition and consequence. descriptive logic structure. | aliases: if_then  ⟵ candidate
- conjunction | constructor | TERM conjunction(items: LIST[TERM]) -> TERM | All described components apply | not: Does not imply temporal order  ⟵ candidate
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ dependency of constraint_exclude_flowery_language
- gender_identity | constructor | TERM gender_identity(identity: STRING) -> TERM | Constructs a descriptive term representing an individual's or demographic group's gender identity. | not: gender_women (product attribute) or char_female (fictional character trait) or identity (name/persona claim) | aliases: gender, gender_expression  ⟵ candidate
- include | constructor | TERM include(item: STRING / TERM) -> TERM | Require the identified content/item | not: Not permission to invent an instance in a recorded trace  ⟵ dependency of constraint_include_character_attribute_list
- negation | constructor | TERM negation(target: TERM) -> TERM | Constructs a descriptive semantic negation of a target descriptive proposition or condition term. | not: Check's runtime Boolean operator NOT or a speech-act decline | aliases: not, does not, negation, absence of  ⟵ candidate
- outshines | constructor | TERM outshines(brighter: STRING / TERM, dimmer: STRING / TERM) -> TERM | Constructs a description of relative visual brightness where a brighter light source overpowers the perceived brightness of a dimmer object. | not: an absolute numeric brightness measurement | aliases: outshines, overpowers brightness, drowns out light  ⟵ candidate
- regression_case | constructor | TERM regression_case(framework: STRING / ATOM[platform_label], modifier: STRING, relation: STRING) -> TERM | A regression scenario specifying affected framework, condition and relation | not: Does not invent a passing test or exact implementation  ⟵ candidate
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ dependency of constraint_respectful
- sequence | constructor | TERM sequence(items: LIST[TERM]) -> TERM | Ordered described activities/content | not: Not unordered conjunction  ⟵ dependency of event_sadie_adler_unmasking
- similarity | constructor | TERM similarity(target: STRING / TERM, dimension?: STRING / TERM) -> TERM | Constructs a descriptor representing comparative closeness or similarity to a target along a given dimension. | not: spatial proximity (use rank_distance or next_to) or an assertion of exact identity (use identity) | aliases: closest_to, similar_to, resembles  ⟵ candidate
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ candidate
- weather_condition | constructor | TERM weather_condition(condition: STRING, location?: STRING / TERM / ATOM[country], severity?: STRING) -> TERM | A structured descriptor of atmospheric or weather phenomena such as wind, rain, or storm at an optional location; asserts nothing. | not: state_cold or state_warm (thermal states of physical objects) or occurred (past factual occurrence assertion) | aliases: weather, storm_condition, atmospheric_condition  ⟵ candidate
- well_wishes | constructor | TERM well_wishes(recipient?: STRING / TERM, sentiment?: STRING) -> TERM | Constructs a conversational discourse term representing well-wishes, good luck expressions, or parting encouragement. | not: a salutation greeting (use greeting) or apology (use apologize) | aliases: good_luck, best_wishes, encouragement  ⟵ candidate

### composites

- char_female | composite | character-property-value | TERM char_female() -> TERM | Female gender. | = character_trait(property="gender", value="female") | aliases: female  ⟵ candidate
- constraint_beginner | composite | constraint-value | TERM constraint_beginner() -> TERM | Targeted at beginners. | = requirement(property="audience_expertise", value="beginner")  ⟵ candidate
- constraint_budget_limited | composite | constraint-value | TERM constraint_budget_limited() -> TERM | Limited budget. | = requirement(property="budget_limited", value=TRUE)  ⟵ candidate
- constraint_exclude_flowery_language | composite | constraint-value | TERM constraint_exclude_flowery_language() -> TERM | Avoid flowery language. | = exclude(item="flowery_language")  ⟵ candidate
- constraint_exclude_liberation_theme | composite | constraint-value | TERM constraint_exclude_liberation_theme() -> TERM | Avoid liberation theme. | = exclude(item="liberation_theme")  ⟵ candidate
- constraint_include_character_attribute_list | composite | constraint-value | TERM constraint_include_character_attribute_list() -> TERM | Include character attributes. | = include(item="character_attribute_list")  ⟵ candidate
- constraint_realistic | composite | constraint-value | TERM constraint_realistic() -> TERM | Must be realistic. | = requirement(property="realistic", value=TRUE)  ⟵ candidate
- constraint_respectful | composite | constraint-value | TERM constraint_respectful() -> TERM | Must be respectful. | = requirement(property="respectful", value=TRUE)  ⟵ candidate
- event_sadie_adler_unmasking | composite | event-value | TERM event_sadie_adler_unmasking() -> TERM | Sadie Adler taking off her hat and peeling skin. | = sequence(items=[activity(verb="remove", actor="Sadie Adler", object="hat"), activity(verb="peel", actor="Sadie Adler", object="skin")])  ⟵ candidate
- topic_greatest_cricketer_of_all_time | composite | topic-value | TERM topic_greatest_cricketer_of_all_time() -> TERM | Greatest cricketer of all time. | = subject(kind="cricketer", qualifier=requirement(property="rank_by_greatness", value=1), time="all_time")  ⟵ candidate
- topic_profanity | composite | topic-value | TERM topic_profanity() -> TERM | A composite term representing the topic of profanity. | = subject(kind="profanity") | not: potential_harms (which is generic) | aliases: profanity  ⟵ candidate

### claim relations

- attribute_claim | claim_relation | CLAIM attribute_claim(subject: STRING / TERM / ATOM[platform_label], property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) | Asserts that a subject possesses a named property evaluated to a specific primitive or structured value. general property attribution claim. | aliases: property_value, word_property, has_property, property attribution  ⟵ related to statement
- causes | claim_relation | CLAIM causes(cause: CLAIM / TERM, effect: CLAIM) | Asserts a direct causal relationship producing an effect proposition. causal assertion. | aliases: produces  ⟵ candidate
- comfortable | claim_relation | CLAIM comfortable(person: TERM, value: BOOL) | Asserts whether a person or animal is comfortable in a situation. affective/state claim. | aliases: is_comfortable  ⟵ candidate
- considered | claim_relation | CLAIM considered(subject: TERM) | Asserts that an agent or speaker evaluated or entertained a specific candidate term or concept. subject is the evaluated term. | aliases: evaluated, weighed  ⟵ candidate
- controversial | claim_relation | CLAIM controversial(subject: STRING / TERM) | Asserts that a topic, policy, or practice is the subject of public debate or controversy. evaluative debate claim. | aliases: debated, disputed  ⟵ candidate
- enables | claim_relation | CLAIM enables(condition: TERM / CLAIM, outcome: TERM / CLAIM) | Asserts that an enabling condition or capability facilitates an outcome. enabling condition. | aliases: facilitates, allows  ⟵ candidate
- example_of | claim_relation | CLAIM example_of(example: TERM, concept: TERM) | Asserts that an instance or term exemplifies a general concept, pattern, or category. example and concept are descriptive terms. | aliases: exemplifies, instance_of  ⟵ candidate
- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ candidate
- has_state | claim_relation | CLAIM has_state(subject: TERM, state: STRING) | Asserts that an entity is currently in a physical, thermal, or operational state. state must be a valid state descriptor string. | aliases: in_state, state_is  ⟵ related to statement
- identity | claim_relation | CLAIM identity(subject: STRING / TERM, name: STRING) | Asserts the identified name or persona of an agent or entity. identity assertion. | aliases: agent_name  ⟵ dependency of gender_identity
- important | claim_relation | CLAIM important(target: TERM) | Asserts that a concept, activity, or condition is important or significant. evaluative importance claim. | aliases: significant  ⟵ candidate
- leads_to | claim_relation | CLAIM leads_to(cause: TERM, effect: TERM) | Asserts a conceptual consequence or progression from cause to effect. progression relation. | aliases: results_in  ⟵ candidate
- motivated_by | claim_relation | CLAIM motivated_by(claim: CLAIM, motive: STRING / TERM) | Asserts that an action, rule, or claim is motivated by an underlying motive or goal. motive explanation. | aliases: rationale_is  ⟵ candidate
- occurred_recently | claim_relation | CLAIM occurred_recently(target: CLAIM) | Asserts temporal recency of an asserted occurrence or claim. temporal recency qualifier. | aliases: recently_happened  ⟵ candidate
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ candidate
- recommended | claim_relation | CLAIM recommended(target: TERM / CLAIM) | Asserts an advisory recommendation that an activity or measure is advisable. advisory normative claim. | aliases: advisable  ⟵ candidate
- spatial_state | claim_relation | CLAIM spatial_state(relation: STRING, object: TERM, reference: TERM) | Asserts an observed spatial configuration between an object and a reference landmark. relation must specify spatial configuration. | aliases: placed_at, located_at  ⟵ related to statement
- statement | claim_relation | CLAIM statement(fact: TERM) | Foundational claim relation converting any descriptive TERM into an attributed, truth-evaluated assertion. universal fact assertion. | aliases: assert_fact, fact_claim, claim_statement  ⟵ candidate
- stereotype | claim_relation | CLAIM stereotype(target: STRING / TERM, trait: STRING / TERM) | Asserts that an attributed trait, generalization, or assumption about a demographic group or social category is a stereotype. | not: an individual character trait or verified fact | aliases: social_stereotype, generalization, bias  ⟵ candidate
- unaware | claim_relation | CLAIM unaware(person: STRING / TERM, topic: STRING / TERM) | Asserts epistemic lack of awareness regarding a topic, fact, or event. epistemic state. | aliases: ignorant_of  ⟵ candidate

### links

- contrast | link | LINK contrast(first: CLAIM, second: CLAIM) | Expresses rhetorical qualification, opposition, or contrast between two claims. link between claims. | aliases: qualification, however  ⟵ candidate
- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ candidate
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ candidate
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ candidate
- then | link | LINK then(previous: EVENT, next: EVENT) | Represents temporal sequence and succession between two events where next follows previous. previous and next must be event terms. | aliases: followed_by, after_which  ⟵ candidate

### values

- art_story | value | artifact-value | Narrative story.  ⟵ candidate
- sym_pandas_testing_assert_almost_equal | value | code-value | Source code file path or exported symbol in scientific Python: sym_pandas_testing_assert_almost_equal. | aliases: sym_pandas_testing_assert_almost_equal  ⟵ candidate
- constraint_17_plus | value | constraint-value | Rated 17+ or mature.  ⟵ candidate
- mod_mixed_case | value | descriptive-value | Mixed-case modifier. | aliases: mixed case  ⟵ candidate
- yakuza | value | descriptive-value | Descriptive concept of yakuza in cultural and social contexts. | aliases: yakuza  ⟵ candidate
- unit_sentence | value | duration-unit-value | One grammatical sentence in text generation or constraint counting. | not: unit_paragraph (paragraph block) or unit_word (individual word) | aliases: sentence, sentences  ⟵ candidate
- unit_word | value | duration-unit-value | Rendered whitespace-delimited word. | aliases: words  ⟵ candidate
- apple | value | entity-name | An apple fruit item, typically an ingredient or interactive food object. | not: food_label::tomato or other fruits/vegetables | aliases: apple, apples, red apple, green apple, apple slice  ⟵ candidate
- bowtie | value | entity-name | Item or prop in joke/creative context: bowtie. | aliases: bowtie  ⟵ candidate
- bread | value | entity-name | A bread loaf or slice food object. | aliases: bread  ⟵ candidate
- caddy | value | entity-name | A portable storage caddy, organizer box, or supply tote for carrying and organizing handheld tools and supplies. | not: cabinet (a stationary furniture cupboard) or safe (a secure metal lockbox) | aliases: caddy, supply caddy, wrapping caddy, tool caddy, organizer caddy, supply tote  ⟵ candidate
- candle | value | entity-name | A candle light source made of wax with a wick. | not: lamp (an electric light appliance or fixture) | aliases: candle, wax candle  ⟵ candidate
- cinnamon | value | entity-name | Ground or whole cinnamon culinary spice from Cinnamomum tree bark. | not: nutmeg, cloves, or other distinct spice varieties | aliases: cinnamon, ground cinnamon, cinnamon spice, cinnamon stick  ⟵ candidate
- coffee_maker | value | entity-name | A coffee-making appliance; not automatically a heating resource  ⟵ candidate
- dog | value | entity-name | Animal entity: dog. | not: animal_label::cat or animal_label::donkey | aliases: dog, dogs, canine, pup, puppy  ⟵ candidate
- dried_fruit | value | entity-name | Generic dried fruit food item. | not: fresh fruit or specific dried varieties like raisin or sultana | aliases: dried fruit, dried fruits  ⟵ candidate
- dulce_de_leche | value | entity-name | Sweet caramelized milk confection or dessert spread: dulce de leche. | not: cheese or dulce_de_nata | aliases: dulce de leche, dulce_de_leche  ⟵ candidate
- dulce_de_nata | value | entity-name | Clotted cream milk confection or dessert item: dulce de nata. | not: dulce_de_leche or cheese | aliases: dulce de nata, dulce_de_nata  ⟵ candidate
- entity_flowers | value | entity-name | Flowers, blossoms, or floral design elements. | not: constraint_exclude_flowery_language (a prose style constraint) or agricultural food items | aliases: flowers, floral, flower, floral decorations  ⟵ candidate
- grape_merlot | value | entity-name | Merlot wine grape variety. | not: other red grape varieties such as grape_cabernet_sauvignon or grape_pinot_noir | aliases: Merlot, merlot grape  ⟵ candidate
- grape_tannin | value | entity-name | Tannin powder derived from grapes for wine structure. | not: oak_chips or wood aging additives | aliases: grape tannin, tannin, wine tannin  ⟵ candidate
- grape_thompson_seedless | value | entity-name | Thompson Seedless grape variety. | not: wine grape cultivars like grape_merlot or grape_chardonnay | aliases: Thompson Seedless, thompson seedless grape, sultana grape  ⟵ candidate
- ice_cream | value | entity-name | Frozen dessert food item: ice cream. | not: entity_desserts or entity_sweet_food (generic menu categories) | aliases: ice cream, ice_cream  ⟵ candidate
- lettuce | value | entity-name | A head of lettuce or leafy green vegetable food item. | not: food_label::tomato or food_label::potato (other vegetable items) | aliases: lettuce, head of lettuce, salad greens  ⟵ candidate
- mittens | value | entity-name | Item or prop in joke/creative context: mittens. | aliases: mittens  ⟵ candidate
- mug | value | entity-name | Drinking cup. | aliases: mug  ⟵ candidate
- pencil | value | entity-name | A pencil writing instrument. | aliases: pencil  ⟵ candidate
- resource_chiller | value | entity-name | Canonical abstract chilling resource when no particular appliance is named.  ⟵ candidate
- resource_heater | value | entity-name | Canonical abstract heating resource when no particular appliance is named.  ⟵ candidate
- resource_sink | value | entity-name | Canonical abstract washing resource when no particular sink is named.  ⟵ candidate
- sultana | value | entity-name | Dried white seedless grape food product. | not: raisin (dark dried grape) or wine_grape | aliases: sultana, sultanas, golden raisin  ⟵ candidate
- yarn | value | entity-name | Item or prop in joke/creative context: yarn. | aliases: yarn  ⟵ candidate
- locale_de | value | locale-value | German language or locale descriptor. | not: other language locales (such as locale_en_us or locale_fr) or country entity (country::DE) | aliases: German, german, Deutsch, de, de-DE  ⟵ candidate
- locale_en_gb | value | locale-value | UK English. | aliases: british english  ⟵ candidate
- liberal_onsen | value | location-name | Traditional Japanese establishment or hospitality venue: liberal_onsen. | aliases: liberal_onsen  ⟵ candidate
- metric_order_late | value | metric-value | Whether an order is late. | aliases: order is late, delayed  ⟵ candidate
- color_pink | value | product-attribute-value | Pink visual color qualifier. | not: color_label::red, color_label::purple, or other distinct color shades | aliases: pink, color_pink, blush pink, rose pink, pastel pink  ⟵ candidate
- gender_men | value | product-attribute-value | Men's/male-targeted. | aliases: men, male  ⟵ candidate
- gender_unisex | value | product-attribute-value | Unisex. | aliases: unisex  ⟵ candidate
- size_small | value | product-attribute-value | Small size. | aliases: small, S  ⟵ candidate
- role_kids | value | recipient-value | Children/kids participant group in event context. | aliases: kids, children  ⟵ candidate
- role_mother | value | recipient-value | The mother of the user. | not: role_sister or role_kids | aliases: my mom, mother, mom  ⟵ candidate
- role_professor | value | recipient-value | The user's professor/instructor. | aliases: my professor, teacher  ⟵ candidate
- role_sister | value | recipient-value | Sister participant role in family/event context. | aliases: sister  ⟵ candidate
- cat_game | value | search-value | Category: video game.  ⟵ candidate
- cat_limited_time_offers | value | search-value | Category: time-limited deals.  ⟵ candidate
- behind | value | spatial-relation | Positioned behind.  ⟵ candidate
- in_front_of | value | spatial-relation | Positioned in front of. | aliases: in front of  ⟵ candidate
- left_of | value | spatial-relation | To the left of. | aliases: left of  ⟵ candidate
- next_to | value | spatial-relation | Adjacent to. | aliases: beside  ⟵ candidate
- on | value | spatial-relation | Resting atop. | aliases: on top of  ⟵ candidate
- right_of | value | spatial-relation | To the right of. | aliases: right of  ⟵ candidate
- under | value | spatial-relation | Beneath. | aliases: below  ⟵ candidate
- state_cold | value | state-value | Cold or chilled condition. | aliases: cold, chilled  ⟵ candidate
- state_dirty | value | state-value | Dirty condition. | aliases: dirty  ⟵ candidate
- state_warm | value | state-value | Warm or heated condition. | aliases: warm, hot  ⟵ candidate
- style_catchy | value | style-value | Catchy, attention-grabbing style. | aliases: catchy  ⟵ candidate
- style_persuasive | value | style-value | Persuasive/argumentative style. | aliases: persuasive  ⟵ candidate
- tone_empathetic | value | tone-value | Conveys empathy/understanding. | aliases: sympathetically  ⟵ candidate
- tone_polite | value | tone-value | Courteous, respectful register. | aliases: politely, kindly  ⟵ candidate
- topic_baldurs_gate_3 | value | topic-value | Baldur's Gate 3.  ⟵ candidate
- topic_politics | value | topic-value | Politics.  ⟵ candidate
- topic_spider_man_2 | value | topic-value | Marvel's Spider-Man 2.  ⟵ candidate
