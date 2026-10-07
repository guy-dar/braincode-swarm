# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 118 needs (decomposition: llm), 155 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | speech_act | t1:s1 | introduce a set of logical premises | `respond`, `propose`, `supports`, `inform`, `ask`, `subject`, `conditional`, `constraint_realistic`, `topic_school_work_routine`, `confirm`, `motivated_by`, `conjunction` |
| n2 | claim | t1:s2 | the bear needs the tiger | `meets_needs`, `cat_limited_time_offers`, `cat_game`, `enables`, `animal_label`, `leads_to`, `causes`, `dog`, `important`, `recommended`, `topic_spider_man_2`, `sym_pandas_testing_assert_almost_equal` |
| n3 | object | t1:s2 | bear → `animal_label::<key>` | `animal_label`*, `bread`, `sym_pandas_testing_assert_almost_equal`, `topic_spider_man_2`, `caddy`, `dog`, `path_pandas_src_testing_pyx`, `cat_game`, `event_sadie_adler_unmasking`, `yakuza`, `tattoos`, `sponge` |
| n4 | object | t1:s2 | tiger → `animal_label::<key>` | `animal_label`*, `cat_game`, `cat_limited_time_offers`, `dog`, `yakuza`, `meat`, `tattoos`, `right_of`, `class_temple`, `dom_safari`, `resource_chiller`, `resource_heater` |
| n5 | action | t1:s2 | needs | `meets_needs`, `requirement`, `constraint_realistic`, `constraint_budget_limited`, `constraint_single_choice`, `obligation`, `constraint_comprehensive`, `proposed_policy`, `important`, `constraint_respectful`, `block_evaluation`, `motivated_by` |
| n6 | claim | t1:s3 | the cat eats the squirrel | `cat_game`, `cat_limited_time_offers`, `enables`, `animal_label`, `caddy`, `leads_to`, `occurred_recently`, `causes`, `motivated_by`, `important`, `outcome`, `recommended` |
| n7 | object | t1:s3 | cat → `animal_label::<key>` | `cat_game`, `cat_limited_time_offers`, `animal_label`*, `dog`, `caddy`, `apple`, `path_pandas_src_testing_pyx`, `style_catchy`, `meat`, `event_sadie_adler_unmasking`, `tattooed_guests`, `coffee_maker` |
| n8 | object | t1:s3 | squirrel → `animal_label::<key>` | `animal_label`*, `caddy`, `cat_limited_time_offers`, `cat_game`, `topic_spider_man_2`, `topic_pickup_lines`, `topic_baldurs_gate_3`, `mittens`, `tattoos`, `coffee_maker`, `tattooed_guests`, `resource_chiller` |
| n9 | action | t1:s3 | eats | `spoon`, `obligation`, `block_evaluation`, `state_sliced`, `motivated_by`, `menu_works`, `meat`, `calculation`, `bread`, `occurred`, `user_preference`, `propose` |
| n10 | claim | t1:s4 | the cat is not green | `cat_game`, `cat_limited_time_offers`, `leads_to`, `enables`, `animal_label`, `path_pandas_src_testing_pyx`, `occurred_recently`, `apple`, `causes`, `important`, `outcome`, `grape_thompson_seedless` |
| n11 | object | t1:s4 | cat → `animal_label::<key>` | `cat_game`, `cat_limited_time_offers`, `animal_label`*, `dog`, `caddy`, `apple`, `path_pandas_src_testing_pyx`, `style_catchy`, `meat`, `event_sadie_adler_unmasking`, `tattooed_guests`, `coffee_maker` |
| n12 | constraint | t1:s4 | green → `color_label::<key>` | `color_label`*, `apple`, `constraint_budget_limited`, `cat_limited_time_offers`, `constraint_realistic`, `constraint_exclude_flowery_language`, `right_of`, `constraint_respectful`, `constraint_single_choice`, `grape_thompson_seedless`, `constraint_exclude_liberation_theme`, `requirement` |
| n13 | negation | t1:s4 | not green | `negation`, `constraint_exclude_flowery_language`, `constraint_exclude_liberation_theme`, `apple`, `lettuce`, `grape_thompson_seedless`, `rejects`, `exclude`, `weather_condition`, `decline`, `color_label`, `dried_fruit` |
| n14 | claim | t1:s5 | the cat is not round | `shape_round`*, `cat_game`, `cat_limited_time_offers`, `causes`, `leads_to`, `enables`, `important`, `occurred_recently`, `motivated_by`, `caddy`, `animal_label`, `path_pandas_src_testing_pyx` |
| n15 | object | t1:s5 | cat → `animal_label::<key>` | `cat_game`, `cat_limited_time_offers`, `animal_label`*, `dog`, `caddy`, `apple`, `path_pandas_src_testing_pyx`, `style_catchy`, `meat`, `event_sadie_adler_unmasking`, `tattooed_guests`, `coffee_maker` |
| n16 | constraint | t1:s5 | round | `shape_round`*, `constraint_budget_limited`, `constraint_exclude_flowery_language`, `constraint_single_choice`, `constraint_realistic`, `shape_triangular`, `constraint_respectful`, `left_of`, `constraint_exclude_liberation_theme`, `shape_rectangular`, `shape_square`, `constraint_comprehensive` |
| n17 | negation | t1:s5 | not round | `shape_round`*, `negation`, `rule_category_shape_value`, `rejects`, `topic_baldurs_gate_3`, `constraint_exclude_flowery_language`, `decline`, `exclude`, `shape_triangular`, `constraint_exclude_liberation_theme`, `left_of`, `measure` |
| n18 | claim | t1:s6 | the cat likes the squirrel | `cat_game`, `cat_limited_time_offers`, `enables`, `leads_to`, `animal_label`, `caddy`, `path_pandas_src_testing_pyx`, `causes`, `occurred_recently`, `topic_pickup_lines`, `style_catchy`, `important` |
| n19 | object | t1:s6 | cat → `animal_label::<key>` | `cat_game`, `cat_limited_time_offers`, `animal_label`*, `dog`, `caddy`, `apple`, `path_pandas_src_testing_pyx`, `style_catchy`, `meat`, `event_sadie_adler_unmasking`, `tattooed_guests`, `coffee_maker` |
| n20 | object | t1:s6 | squirrel → `animal_label::<key>` | `animal_label`*, `caddy`, `cat_limited_time_offers`, `cat_game`, `topic_spider_man_2`, `topic_pickup_lines`, `topic_baldurs_gate_3`, `mittens`, `tattoos`, `coffee_maker`, `tattooed_guests`, `resource_chiller` |
| n21 | action | t1:s6 | likes | `style_narrative`, `similarity`, `style_catchy`, `character_trait`, `comfortable`, `well_wishes`, `obligation`, `has_style`, `next_to`, `on`, `right_of`, `calculation` |
| n22 | claim | t1:s7 | the cat needs the bear | `cat_limited_time_offers`, `cat_game`, `meets_needs`, `enables`, `animal_label`, `caddy`, `leads_to`, `comfortable`, `path_pandas_src_testing_pyx`, `causes`, `sym_pandas_testing_assert_almost_equal`, `important` |
| n23 | object | t1:s7 | cat → `animal_label::<key>` | `cat_game`, `cat_limited_time_offers`, `animal_label`*, `dog`, `caddy`, `apple`, `path_pandas_src_testing_pyx`, `style_catchy`, `meat`, `event_sadie_adler_unmasking`, `tattooed_guests`, `coffee_maker` |
| n24 | object | t1:s7 | bear → `animal_label::<key>` | `animal_label`*, `bread`, `sym_pandas_testing_assert_almost_equal`, `topic_spider_man_2`, `caddy`, `dog`, `path_pandas_src_testing_pyx`, `cat_game`, `event_sadie_adler_unmasking`, `yakuza`, `tattoos`, `sponge` |
| n25 | action | t1:s7 | needs | `meets_needs`, `requirement`, `constraint_realistic`, `constraint_budget_limited`, `constraint_single_choice`, `obligation`, `constraint_comprehensive`, `proposed_policy`, `important`, `constraint_respectful`, `block_evaluation`, `motivated_by` |
| n26 | claim | t1:s8 | the squirrel eats the bear | `enables`, `caddy`, `cat_game`, `leads_to`, `topic_spider_man_2`, `cat_limited_time_offers`, `causes`, `occurred_recently`, `sym_pandas_testing_assert_almost_equal`, `statement`, `outcome`, `important` |
| n27 | object | t1:s8 | squirrel → `animal_label::<key>` | `animal_label`*, `caddy`, `cat_limited_time_offers`, `cat_game`, `topic_spider_man_2`, `topic_pickup_lines`, `topic_baldurs_gate_3`, `mittens`, `tattoos`, `coffee_maker`, `tattooed_guests`, `resource_chiller` |
| n28 | object | t1:s8 | bear → `animal_label::<key>` | `animal_label`*, `bread`, `sym_pandas_testing_assert_almost_equal`, `topic_spider_man_2`, `caddy`, `dog`, `path_pandas_src_testing_pyx`, `cat_game`, `event_sadie_adler_unmasking`, `yakuza`, `tattoos`, `sponge` |
| n29 | action | t1:s8 | eats | `spoon`, `obligation`, `block_evaluation`, `state_sliced`, `motivated_by`, `menu_works`, `meat`, `calculation`, `bread`, `occurred`, `user_preference`, `propose` |
| n30 | claim | t1:s9 | the squirrel does not eat the cat | `negation`*, `cat_limited_time_offers`, `cat_game`, `animal_label`, `leads_to`, `enables`, `causes`, `caddy`, `motivated_by`, `occurred_recently`, `important`, `path_pandas_src_testing_pyx` |
| n31 | object | t1:s9 | squirrel → `animal_label::<key>` | `animal_label`*, `caddy`, `cat_limited_time_offers`, `cat_game`, `topic_spider_man_2`, `topic_pickup_lines`, `topic_baldurs_gate_3`, `mittens`, `tattoos`, `coffee_maker`, `tattooed_guests`, `resource_chiller` |
| n32 | object | t1:s9 | cat → `animal_label::<key>` | `cat_game`, `cat_limited_time_offers`, `animal_label`*, `dog`, `caddy`, `apple`, `path_pandas_src_testing_pyx`, `style_catchy`, `meat`, `event_sadie_adler_unmasking`, `tattooed_guests`, `coffee_maker` |
| n33 | action | t1:s9 | eats | `spoon`, `obligation`, `block_evaluation`, `state_sliced`, `motivated_by`, `menu_works`, `meat`, `calculation`, `bread`, `occurred`, `user_preference`, `propose` |
| n34 | negation | t1:s9 | does not eat | `negation`*, `exclude`, `decline`, `spoon`, `rejects`, `unaware`, `topic_food_safety`, `constraint_exclude_flowery_language`, `menu_works`, `prohibited`, `constraint_exclude_liberation_theme`, `user_preference` |
| n35 | claim | t1:s10 | the squirrel does not eat the tiger | `negation`*, `cat_game`, `animal_label`, `cat_limited_time_offers`, `enables`, `causes`, `leads_to`, `topic_spider_man_2`, `motivated_by`, `occurred_recently`, `sym_pandas_testing_assert_almost_equal`, `important` |
| n36 | object | t1:s10 | squirrel → `animal_label::<key>` | `animal_label`*, `caddy`, `cat_limited_time_offers`, `cat_game`, `topic_spider_man_2`, `topic_pickup_lines`, `topic_baldurs_gate_3`, `mittens`, `tattoos`, `coffee_maker`, `tattooed_guests`, `resource_chiller` |
| n37 | object | t1:s10 | tiger → `animal_label::<key>` | `animal_label`*, `cat_game`, `cat_limited_time_offers`, `dog`, `yakuza`, `meat`, `tattoos`, `right_of`, `class_temple`, `dom_safari`, `resource_chiller`, `resource_heater` |
| n38 | action | t1:s10 | eats | `spoon`, `obligation`, `block_evaluation`, `state_sliced`, `motivated_by`, `menu_works`, `meat`, `calculation`, `bread`, `occurred`, `user_preference`, `propose` |
| n39 | negation | t1:s10 | does not eat | `negation`*, `exclude`, `decline`, `spoon`, `rejects`, `unaware`, `topic_food_safety`, `constraint_exclude_flowery_language`, `menu_works`, `prohibited`, `constraint_exclude_liberation_theme`, `user_preference` |
| n40 | claim | t1:s11 | the squirrel is cold | `state_cold`*, `causes`, `leads_to`, `motivated_by`, `enables`, `topic_baldurs_gate_3`, `topic_spider_man_2`, `cat_game`, `important`, `animal_label`, `caddy`, `statement` |
| n41 | object | t1:s11 | squirrel → `animal_label::<key>` | `animal_label`*, `caddy`, `cat_limited_time_offers`, `cat_game`, `topic_spider_man_2`, `topic_pickup_lines`, `topic_baldurs_gate_3`, `mittens`, `tattoos`, `coffee_maker`, `tattooed_guests`, `resource_chiller` |
| n42 | constraint | t1:s11 | cold | `state_cold`*, `weather_condition`, `constraint_budget_limited`, `mittens`, `state_warm`, `constraint_exclude_flowery_language`, `constraint_exclude_liberation_theme`, `constraint_realistic`, `constraint_single_choice`, `ice_cream`, `constraint_respectful`, `requirement` |
| n43 | claim | t1:s12 | the squirrel likes the bear | `enables`, `cat_game`, `leads_to`, `caddy`, `topic_spider_man_2`, `animal_label`, `cat_limited_time_offers`, `causes`, `path_pandas_src_testing_pyx`, `important`, `occurred_recently`, `sym_pandas_testing_assert_almost_equal` |
| n44 | object | t1:s12 | squirrel → `animal_label::<key>` | `animal_label`*, `caddy`, `cat_limited_time_offers`, `cat_game`, `topic_spider_man_2`, `topic_pickup_lines`, `topic_baldurs_gate_3`, `mittens`, `tattoos`, `coffee_maker`, `tattooed_guests`, `resource_chiller` |
| n45 | object | t1:s12 | bear → `animal_label::<key>` | `animal_label`*, `bread`, `sym_pandas_testing_assert_almost_equal`, `topic_spider_man_2`, `caddy`, `dog`, `path_pandas_src_testing_pyx`, `cat_game`, `event_sadie_adler_unmasking`, `yakuza`, `tattoos`, `sponge` |
| n46 | action | t1:s12 | likes | `style_narrative`, `similarity`, `style_catchy`, `character_trait`, `comfortable`, `well_wishes`, `obligation`, `has_style`, `next_to`, `on`, `right_of`, `calculation` |
| n47 | claim | t1:s13 | the squirrel likes the cat | `causes`, `cat_game`, `cat_limited_time_offers`, `leads_to`, `animal_label`, `enables`, `caddy`, `topic_pickup_lines`, `motivated_by`, `important`, `comfortable`, `occurred_recently` |
| n48 | object | t1:s13 | squirrel → `animal_label::<key>` | `animal_label`*, `caddy`, `cat_limited_time_offers`, `cat_game`, `topic_spider_man_2`, `topic_pickup_lines`, `topic_baldurs_gate_3`, `mittens`, `tattoos`, `coffee_maker`, `tattooed_guests`, `resource_chiller` |
| n49 | object | t1:s13 | cat → `animal_label::<key>` | `cat_game`, `cat_limited_time_offers`, `animal_label`*, `dog`, `caddy`, `apple`, `path_pandas_src_testing_pyx`, `style_catchy`, `meat`, `event_sadie_adler_unmasking`, `tattooed_guests`, `coffee_maker` |
| n50 | action | t1:s13 | likes | `style_narrative`, `similarity`, `style_catchy`, `character_trait`, `comfortable`, `well_wishes`, `obligation`, `has_style`, `next_to`, `on`, `right_of`, `calculation` |
| n51 | claim | t1:s14 | the squirrel needs the cat | `causes`, `cat_limited_time_offers`, `meets_needs`, `cat_game`, `topic_pickup_lines`, `leads_to`, `enables`, `caddy`, `animal_label`, `motivated_by`, `important`, `recommended` |
| n52 | object | t1:s14 | squirrel → `animal_label::<key>` | `animal_label`*, `caddy`, `cat_limited_time_offers`, `cat_game`, `topic_spider_man_2`, `topic_pickup_lines`, `topic_baldurs_gate_3`, `mittens`, `tattoos`, `coffee_maker`, `tattooed_guests`, `resource_chiller` |
| n53 | object | t1:s14 | cat → `animal_label::<key>` | `cat_game`, `cat_limited_time_offers`, `animal_label`*, `dog`, `caddy`, `apple`, `path_pandas_src_testing_pyx`, `style_catchy`, `meat`, `event_sadie_adler_unmasking`, `tattooed_guests`, `coffee_maker` |
| n54 | action | t1:s14 | needs | `meets_needs`, `requirement`, `constraint_realistic`, `constraint_budget_limited`, `constraint_single_choice`, `obligation`, `constraint_comprehensive`, `proposed_policy`, `important`, `constraint_respectful`, `block_evaluation`, `motivated_by` |
| n55 | claim | t1:s15 | the tiger is not green | `grape_thompson_seedless`, `enables`, `leads_to`, `animal_label`, `path_pandas_src_testing_pyx`, `sym_pandas_testing_assert_almost_equal`, `cat_game`, `causes`, `occurred_recently`, `important`, `outcome`, `motivated_by` |
| n56 | object | t1:s15 | tiger → `animal_label::<key>` | `animal_label`*, `cat_game`, `cat_limited_time_offers`, `dog`, `yakuza`, `meat`, `tattoos`, `right_of`, `class_temple`, `dom_safari`, `resource_chiller`, `resource_heater` |
| n57 | constraint | t1:s15 | green → `color_label::<key>` | `color_label`*, `apple`, `constraint_budget_limited`, `cat_limited_time_offers`, `constraint_realistic`, `constraint_exclude_flowery_language`, `right_of`, `constraint_respectful`, `constraint_single_choice`, `grape_thompson_seedless`, `constraint_exclude_liberation_theme`, `requirement` |
| n58 | negation | t1:s15 | not green | `negation`, `constraint_exclude_flowery_language`, `constraint_exclude_liberation_theme`, `apple`, `lettuce`, `grape_thompson_seedless`, `rejects`, `exclude`, `weather_condition`, `decline`, `color_label`, `dried_fruit` |
| n59 | claim | t1:s16 | the tiger does not like the cat | `cat_game`, `cat_limited_time_offers`, `animal_label`, `negation`*, `leads_to`, `enables`, `path_pandas_src_testing_pyx`, `causes`, `occurred_recently`, `sym_pandas_testing_assert_almost_equal`, `important`, `recommended` |
| n60 | object | t1:s16 | tiger → `animal_label::<key>` | `animal_label`*, `cat_game`, `cat_limited_time_offers`, `dog`, `yakuza`, `meat`, `tattoos`, `right_of`, `class_temple`, `dom_safari`, `resource_chiller`, `resource_heater` |
| n61 | object | t1:s16 | cat → `animal_label::<key>` | `cat_game`, `cat_limited_time_offers`, `animal_label`*, `dog`, `caddy`, `apple`, `path_pandas_src_testing_pyx`, `style_catchy`, `meat`, `event_sadie_adler_unmasking`, `tattooed_guests`, `coffee_maker` |
| n62 | action | t1:s16 | likes | `style_narrative`, `similarity`, `style_catchy`, `character_trait`, `comfortable`, `well_wishes`, `obligation`, `has_style`, `next_to`, `on`, `right_of`, `calculation` |
| n63 | negation | t1:s16 | does not like | `negation`*, `decline`, `exclude`, `constraint_exclude_flowery_language`, `constraint_exclude_liberation_theme`, `style_narrative`, `rejects`, `comfortable`, `style_catchy`, `topic_profanity`, `opposes`, `grape_thompson_seedless` |
| n64 | claim | t1:s17 | the tiger needs the cat | `cat_limited_time_offers`, `cat_game`, `meets_needs`, `animal_label`, `enables`, `leads_to`, `causes`, `important`, `caddy`, `motivated_by`, `recommended`, `occurred_recently` |
| n65 | object | t1:s17 | tiger → `animal_label::<key>` | `animal_label`*, `cat_game`, `cat_limited_time_offers`, `dog`, `yakuza`, `meat`, `tattoos`, `right_of`, `class_temple`, `dom_safari`, `resource_chiller`, `resource_heater` |
| n66 | object | t1:s17 | cat → `animal_label::<key>` | `cat_game`, `cat_limited_time_offers`, `animal_label`*, `dog`, `caddy`, `apple`, `path_pandas_src_testing_pyx`, `style_catchy`, `meat`, `event_sadie_adler_unmasking`, `tattooed_guests`, `coffee_maker` |
| n67 | action | t1:s17 | needs | `meets_needs`, `requirement`, `constraint_realistic`, `constraint_budget_limited`, `constraint_single_choice`, `obligation`, `constraint_comprehensive`, `proposed_policy`, `important`, `constraint_respectful`, `block_evaluation`, `motivated_by` |
| n68 | reasoning | t1:s18 | if something is round, it likes the tiger | `shape_round`*, `cat_game`, `rejects`, `cat_limited_time_offers`, `style_catchy`, `topic_pickup_lines`, `topic_baldurs_gate_3`, `supports`, `animal_label`, `sym_pandas_testing_assert_almost_equal`, `dog`, `apple` |
| n69 | constraint | t1:s18 | round | `shape_round`*, `constraint_budget_limited`, `constraint_exclude_flowery_language`, `constraint_single_choice`, `constraint_realistic`, `shape_triangular`, `constraint_respectful`, `left_of`, `constraint_exclude_liberation_theme`, `shape_rectangular`, `shape_square`, `constraint_comprehensive` |
| n70 | action | t1:s18 | likes | `style_narrative`, `similarity`, `style_catchy`, `character_trait`, `comfortable`, `well_wishes`, `obligation`, `has_style`, `next_to`, `on`, `right_of`, `calculation` |
| n71 | object | t1:s18 | tiger → `animal_label::<key>` | `animal_label`*, `cat_game`, `cat_limited_time_offers`, `dog`, `yakuza`, `meat`, `tattoos`, `right_of`, `class_temple`, `dom_safari`, `resource_chiller`, `resource_heater` |
| n72 | reasoning | t1:s19 | if something needs the squirrel, it does not like the cat | `cat_limited_time_offers`, `cat_game`, `negation`*, `meets_needs`, `rejects`, `caddy`, `animal_label`, `causes`, `topic_pickup_lines`, `possesses`, `supports`, `comfortable` |
| n73 | action | t1:s19 | needs | `meets_needs`, `requirement`, `constraint_realistic`, `constraint_budget_limited`, `constraint_single_choice`, `obligation`, `constraint_comprehensive`, `proposed_policy`, `important`, `constraint_respectful`, `block_evaluation`, `motivated_by` |
| n74 | object | t1:s19 | squirrel → `animal_label::<key>` | `animal_label`*, `caddy`, `cat_limited_time_offers`, `cat_game`, `topic_spider_man_2`, `topic_pickup_lines`, `topic_baldurs_gate_3`, `mittens`, `tattoos`, `coffee_maker`, `tattooed_guests`, `resource_chiller` |
| n75 | action | t1:s19 | likes | `style_narrative`, `similarity`, `style_catchy`, `character_trait`, `comfortable`, `well_wishes`, `obligation`, `has_style`, `next_to`, `on`, `right_of`, `calculation` |
| n76 | object | t1:s19 | cat → `animal_label::<key>` | `cat_game`, `cat_limited_time_offers`, `animal_label`*, `dog`, `caddy`, `apple`, `path_pandas_src_testing_pyx`, `style_catchy`, `meat`, `event_sadie_adler_unmasking`, `tattooed_guests`, `coffee_maker` |
| n77 | negation | t1:s19 | does not like | `negation`*, `decline`, `exclude`, `constraint_exclude_flowery_language`, `constraint_exclude_liberation_theme`, `style_narrative`, `rejects`, `comfortable`, `style_catchy`, `topic_profanity`, `opposes`, `grape_thompson_seedless` |
| n78 | reasoning | t1:s20 | if something is cold and likes the tiger, the tiger is round | `state_cold`*, `shape_round`*, `cat_game`, `rejects`, `style_catchy`, `cat_limited_time_offers`, `topic_baldurs_gate_3`, `supports`, `event_camper_in_sludge_pit`, `topic_pickup_lines`, `contrast`, `dog` |
| n79 | constraint | t1:s20 | cold | `state_cold`*, `weather_condition`, `constraint_budget_limited`, `mittens`, `state_warm`, `constraint_exclude_flowery_language`, `constraint_exclude_liberation_theme`, `constraint_realistic`, `constraint_single_choice`, `ice_cream`, `constraint_respectful`, `requirement` |
| n80 | action | t1:s20 | likes | `style_narrative`, `similarity`, `style_catchy`, `character_trait`, `comfortable`, `well_wishes`, `obligation`, `has_style`, `next_to`, `on`, `right_of`, `calculation` |
| n81 | object | t1:s20 | tiger → `animal_label::<key>` | `animal_label`*, `cat_game`, `cat_limited_time_offers`, `dog`, `yakuza`, `meat`, `tattoos`, `right_of`, `class_temple`, `dom_safari`, `resource_chiller`, `resource_heater` |
| n82 | constraint | t1:s20 | round | `shape_round`*, `constraint_budget_limited`, `constraint_exclude_flowery_language`, `constraint_single_choice`, `constraint_realistic`, `shape_triangular`, `constraint_respectful`, `left_of`, `constraint_exclude_liberation_theme`, `shape_rectangular`, `shape_square`, `constraint_comprehensive` |
| n83 | reasoning | t1:s21 | if something eats the bear, the bear likes the tiger | `rejects`, `sym_pandas_testing_assert_almost_equal`, `cat_game`, `animal_label`, `supports`, `dog`, `style_catchy`, `possesses`, `contrast`, `bread`, `cat_limited_time_offers`, `then` |
| n84 | action | t1:s21 | eats | `spoon`, `obligation`, `block_evaluation`, `state_sliced`, `motivated_by`, `menu_works`, `meat`, `calculation`, `bread`, `occurred`, `user_preference`, `propose` |
| n85 | object | t1:s21 | bear → `animal_label::<key>` | `animal_label`*, `bread`, `sym_pandas_testing_assert_almost_equal`, `topic_spider_man_2`, `caddy`, `dog`, `path_pandas_src_testing_pyx`, `cat_game`, `event_sadie_adler_unmasking`, `yakuza`, `tattoos`, `sponge` |
| n86 | action | t1:s21 | likes | `style_narrative`, `similarity`, `style_catchy`, `character_trait`, `comfortable`, `well_wishes`, `obligation`, `has_style`, `next_to`, `on`, `right_of`, `calculation` |
| n87 | object | t1:s21 | tiger → `animal_label::<key>` | `animal_label`*, `cat_game`, `cat_limited_time_offers`, `dog`, `yakuza`, `meat`, `tattoos`, `right_of`, `class_temple`, `dom_safari`, `resource_chiller`, `resource_heater` |
| n88 | reasoning | t1:s22 | if something eats the cat, the cat does not like the tiger | `cat_game`, `cat_limited_time_offers`, `animal_label`, `negation`*, `dog`, `rejects`, `unaware`, `caddy`, `apple`, `supports`, `meat`, `style_catchy` |
| n89 | action | t1:s22 | eats | `spoon`, `obligation`, `block_evaluation`, `state_sliced`, `motivated_by`, `menu_works`, `meat`, `calculation`, `bread`, `occurred`, `user_preference`, `propose` |
| n90 | object | t1:s22 | cat → `animal_label::<key>` | `cat_game`, `cat_limited_time_offers`, `animal_label`*, `dog`, `caddy`, `apple`, `path_pandas_src_testing_pyx`, `style_catchy`, `meat`, `event_sadie_adler_unmasking`, `tattooed_guests`, `coffee_maker` |
| n91 | action | t1:s22 | likes | `style_narrative`, `similarity`, `style_catchy`, `character_trait`, `comfortable`, `well_wishes`, `obligation`, `has_style`, `next_to`, `on`, `right_of`, `calculation` |
| n92 | object | t1:s22 | tiger → `animal_label::<key>` | `animal_label`*, `cat_game`, `cat_limited_time_offers`, `dog`, `yakuza`, `meat`, `tattoos`, `right_of`, `class_temple`, `dom_safari`, `resource_chiller`, `resource_heater` |
| n93 | negation | t1:s22 | does not like | `negation`*, `decline`, `exclude`, `constraint_exclude_flowery_language`, `constraint_exclude_liberation_theme`, `style_narrative`, `rejects`, `comfortable`, `style_catchy`, `topic_profanity`, `opposes`, `grape_thompson_seedless` |
| n94 | reasoning | t1:s23 | if the squirrel likes the cat, the cat eats the squirrel | `cat_game`, `cat_limited_time_offers`, `animal_label`, `rejects`, `topic_pickup_lines`, `caddy`, `style_catchy`, `supports`, `contrast`, `apple`, `dog`, `sym_pandas_testing_assert_almost_equal` |
| n95 | object | t1:s23 | squirrel → `animal_label::<key>` | `animal_label`*, `caddy`, `cat_limited_time_offers`, `cat_game`, `topic_spider_man_2`, `topic_pickup_lines`, `topic_baldurs_gate_3`, `mittens`, `tattoos`, `coffee_maker`, `tattooed_guests`, `resource_chiller` |
| n96 | action | t1:s23 | likes | `style_narrative`, `similarity`, `style_catchy`, `character_trait`, `comfortable`, `well_wishes`, `obligation`, `has_style`, `next_to`, `on`, `right_of`, `calculation` |
| n97 | object | t1:s23 | cat → `animal_label::<key>` | `cat_game`, `cat_limited_time_offers`, `animal_label`*, `dog`, `caddy`, `apple`, `path_pandas_src_testing_pyx`, `style_catchy`, `meat`, `event_sadie_adler_unmasking`, `tattooed_guests`, `coffee_maker` |
| n98 | action | t1:s23 | eats | `spoon`, `obligation`, `block_evaluation`, `state_sliced`, `motivated_by`, `menu_works`, `meat`, `calculation`, `bread`, `occurred`, `user_preference`, `propose` |
| n99 | reasoning | t1:s24 | if something needs the squirrel, the squirrel likes the cat | `cat_game`, `cat_limited_time_offers`, `rejects`, `meets_needs`, `topic_pickup_lines`, `causes`, `caddy`, `animal_label`, `possesses`, `comfortable`, `supports`, `style_catchy` |
| n100 | action | t1:s24 | needs | `meets_needs`, `requirement`, `constraint_realistic`, `constraint_budget_limited`, `constraint_single_choice`, `obligation`, `constraint_comprehensive`, `proposed_policy`, `important`, `constraint_respectful`, `block_evaluation`, `motivated_by` |
| n101 | object | t1:s24 | squirrel → `animal_label::<key>` | `animal_label`*, `caddy`, `cat_limited_time_offers`, `cat_game`, `topic_spider_man_2`, `topic_pickup_lines`, `topic_baldurs_gate_3`, `mittens`, `tattoos`, `coffee_maker`, `tattooed_guests`, `resource_chiller` |
| n102 | action | t1:s24 | likes | `style_narrative`, `similarity`, `style_catchy`, `character_trait`, `comfortable`, `well_wishes`, `obligation`, `has_style`, `next_to`, `on`, `right_of`, `calculation` |
| n103 | object | t1:s24 | cat → `animal_label::<key>` | `cat_game`, `cat_limited_time_offers`, `animal_label`*, `dog`, `caddy`, `apple`, `path_pandas_src_testing_pyx`, `style_catchy`, `meat`, `event_sadie_adler_unmasking`, `tattooed_guests`, `coffee_maker` |
| n104 | reasoning | t1:s25 | if something likes the tiger, it is cold | `state_cold`*, `cat_game`, `rejects`, `animal_label`, `supports`, `style_catchy`, `contrast`, `cat_limited_time_offers`, `topic_baldurs_gate_3`, `event_sadie_adler_unmasking`, `heat`, `weather_condition` |
| n105 | action | t1:s25 | likes | `style_narrative`, `similarity`, `style_catchy`, `character_trait`, `comfortable`, `well_wishes`, `obligation`, `has_style`, `next_to`, `on`, `right_of`, `calculation` |
| n106 | object | t1:s25 | tiger → `animal_label::<key>` | `animal_label`*, `cat_game`, `cat_limited_time_offers`, `dog`, `yakuza`, `meat`, `tattoos`, `right_of`, `class_temple`, `dom_safari`, `resource_chiller`, `resource_heater` |
| n107 | constraint | t1:s25 | cold | `state_cold`*, `weather_condition`, `constraint_budget_limited`, `mittens`, `state_warm`, `constraint_exclude_flowery_language`, `constraint_exclude_liberation_theme`, `constraint_realistic`, `constraint_single_choice`, `ice_cream`, `constraint_respectful`, `requirement` |
| n108 | reasoning | t1:s26 | if something eats the cat, the cat eats the bear | `cat_game`, `cat_limited_time_offers`, `animal_label`, `dog`, `rejects`, `caddy`, `apple`, `supports`, `event_sadie_adler_unmasking`, `then`, `contrast`, `style_catchy` |
| n109 | action | t1:s26 | eats | `spoon`, `obligation`, `block_evaluation`, `state_sliced`, `motivated_by`, `menu_works`, `meat`, `calculation`, `bread`, `occurred`, `user_preference`, `propose` |
| n110 | object | t1:s26 | cat → `animal_label::<key>` | `cat_game`, `cat_limited_time_offers`, `animal_label`*, `dog`, `caddy`, `apple`, `path_pandas_src_testing_pyx`, `style_catchy`, `meat`, `event_sadie_adler_unmasking`, `tattooed_guests`, `coffee_maker` |
| n111 | object | t1:s26 | bear → `animal_label::<key>` | `animal_label`*, `bread`, `sym_pandas_testing_assert_almost_equal`, `topic_spider_man_2`, `caddy`, `dog`, `path_pandas_src_testing_pyx`, `cat_game`, `event_sadie_adler_unmasking`, `yakuza`, `tattoos`, `sponge` |
| n112 | speech_act | t1:s27 | ask whether a statement is True, False, or Unknown | `ask`*, `statement`*, `confirm`, `respond`, `failure`, `controversial`, `negation`, `propose`, `unaware`, `inform`, `rejects`, `motivated_by` |
| n113 | constraint | t1:s27 | base the answer only on the provided theory | `respond`*, `extract`, `subject`, `constraint_budget_limited`, `topic_baldurs_gate_3`, `constraint_realistic`, `causes`, `constraint_exclude_flowery_language`, `constraint_single_choice`, `requirement`, `conjunction`, `rejects` |
| n114 | constraint | t1:s27 | answer format must be True, False, or Unknown | `constraint_realistic`, `respond`*, `metric_order_late`, `constraint_budget_limited`, `subject`, `constraint_respectful`, `failure`, `constraint_exclude_flowery_language`, `requirement`, `constraint_single_choice`, `constraint_comprehensive`, `constraint_include_character_attribute_list` |
| n115 | claim | t1:s28 | the tiger does not like the tiger | `negation`*, `animal_label`, `cat_game`, `leads_to`, `causes`, `enables`, `stereotype`, `important`, `motivated_by`, `comfortable`, `recommended`, `occurred_recently` |
| n116 | object | t1:s28 | tiger → `animal_label::<key>` | `animal_label`*, `cat_game`, `cat_limited_time_offers`, `dog`, `yakuza`, `meat`, `tattoos`, `right_of`, `class_temple`, `dom_safari`, `resource_chiller`, `resource_heater` |
| n117 | action | t1:s28 | likes | `style_narrative`, `similarity`, `style_catchy`, `character_trait`, `comfortable`, `well_wishes`, `obligation`, `has_style`, `next_to`, `on`, `right_of`, `calculation` |
| n118 | negation | t1:s28 | does not like | `negation`*, `decline`, `exclude`, `constraint_exclude_flowery_language`, `constraint_exclude_liberation_theme`, `style_narrative`, `rejects`, `comfortable`, `style_catchy`, `topic_profanity`, `opposes`, `grape_thompson_seedless` |

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
- requirement.value → platform_label
- weather_condition.location → country
- measure.unit → currency
- heat.destination → object_label
- failure.system → platform_label
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

**rule_recording_signatures** (v19/rule/recording-signatures; rule governing heat)

RECORD ACTION uses the operation signature with REF[STRING] → TERM and LIST[REF[STRING]] → LIST[TERM]; other types/categories stay unchanged. Return EVENT, never the runtime result. Record actual outputs as attributed CLAIMs. Do not infer missing resources.

**rule_speech_acts_general** (v19/rule/speech-acts-general; rule governing respond)

UTTER-only, void, with the spec's speech attributes and LIST[TERM] constraints. No result binding. Literal content cannot replace required semantic arguments for structured coverage.

**rule_structural_constructs** (v19/rule/structural-constructs; core)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; rule governing supports)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_attributes_and_generate** (v19/rule/attributes-and-generate; rule governing art_story)

Attribute entries name arguments; legality/types come from each operation, not global membership. GENERATE uses the spec's core fields; retained artifact profiles return STRING. Numeric/list results need explicit profiles. Legacy itinerary fields expand to TERM constraints: duration/duration_unit → duration(amount,unit); stop_min_per_day/stop_requirement → minimum_per_period(class,count,period=unit_day), never an inferred temple class; max_walk_duration/unit → maximum_between_stops(activity="walk",amount,unit). No legacy shorthand is enabled. Old events/character_properties/transformations become explicitly scoped TERM constraints. Message purpose is TERM, not send_email.content: GENERATE exact STRING content, then send. Report opaque fallback separately.

**rule_category_artifact_value** (v19/rule/category/artifact-value; rule governing art_story)

STRING artifact class for GENERATE.target. art_story says what kind of artifact to produce, not what occurs in its plot.

**rule_category_code_value** (v19/rule/category/code-value; rule governing sym_pandas_testing_assert_almost_equal)

path_/sym_ remain STRING identities; migrated chg_/assert_ are TERM constructors. Do not recover an exact file path by guessing from underscores.

**rule_category_constraint_value** (v19/rule/category/constraint-value; rule governing constraint_realistic)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_descriptive_value** (v19/rule/category/descriptive-value; rule governing yakuza)

STRING modifier/domain label; never a free-form proposition. dom_sgi needs its intended referent established before semantically dependent use.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; rule governing unit_day)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing dog)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_event_value** (v19/rule/category/event-value; rule governing event_sadie_adler_unmasking)

TERM-described narrative event, not a recorded EVENT. Require inclusion explicitly when generating a story.

**rule_category_metric_value** (v19/rule/category/metric-value; rule governing metric_order_late)

STRING metric identity, not a Boolean value. Uptime and response time need numeric observations with units; order-late is Boolean-valued. Do not type every metric as BOOL.

**rule_category_recipient_value** (v19/rule/category/recipient-value; rule governing tattooed_guests)

STRING roles or explicit named recipients. A role is not an exact person's identity. Keep an explicit name where substituting a role loses information.

**rule_category_reservation_status_value** (v19/rule/category/reservation-status-value; rule governing reservation_unavailable)

STRING filter states; neither is a BOOL result binding. check_reservation_availability returns a BOOL with a distinct handle.

**rule_category_search_value** (v19/rule/category/search-value; rule governing cat_limited_time_offers)

STRING refinements rank_ / dir_ / cat_ / avail_ / genre_ are separate. rank_rating may fill rank_field; genre_label::comedy may not. “Cheapest” usually requires both rank_price and dir_asc, not rank_price alone.

**rule_category_semantic_category_value** (v19/rule/category/semantic-category-value; rule governing class_temple)

STRING class label used by typed constraints. class_temple describes a class, not an acquired physical temple reference.

**rule_category_shape_value** (v19/rule/category/shape-value; candidate)

STRING geometry. shape_round may select a circular object; it does not imply color or dimensions.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing right_of)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_state_value** (v19/rule/category/state-value; rule governing state_sliced)

STRING condition used in selection. state_warm does not command heat; “hot” is not automatically synonymous with “warm.”

**rule_category_style_value** (v19/rule/category/style-value; rule governing style_catchy)

STRING production style. style_narrative does not establish that described events occurred.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_school_work_routine)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_composites_general** (v19/rule/composites-general; rule governing constraint_realistic)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_operations_general** (v19/rule/operations-general; rule governing heat)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_supplemental_general** (v19/rule/supplemental-general; rule governing coffee_maker)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; rule governing subject)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- extract | operation | operation-vocabulary | (target: LIST[REF[STRING]], limit: NUMBER) -> LIST[REF[STRING]] | First limit results, preserving order and identity; limit is a nonnegative integer; limit=1 is still a list  ⟵ candidate
- heat | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Heat using the stated resource; same identity. Selecting a warm object does not imply heating it.  ⟵ candidate
- turn | operation | operation-vocabulary | (direction: STRING) -> void | Rotate agent body/view orientation. direction is typically left, right, or angle. | aliases: rotate, turn_around  ⟵ related to then
- walk | operation | operation-vocabulary | (destination: STRING / TERM / ATOM[object_label], relation?: STRING) -> void | Locomote towards a target destination or landmark. destination must identify a valid entity or location. | aliases: move_to, go_to, navigate_to  ⟵ related to then

### speech acts

- ask | speech_act | operation-vocabulary | UTTER ask(target: TERM, or a sufficiently precise topic: STRING / TERM) | Request information/advice; not an assertion of an answer. | aliases: ask, how should  ⟵ candidate
- confirm | speech_act | operation-vocabulary | UTTER confirm(target: CLAIM) | Confirm the proposition; its evidence/status remains explicit.  ⟵ candidate
- decline | speech_act | operation-vocabulary | UTTER decline(target: TERM) | Decline the represented request/proposal; not negate every proposition within it.  ⟵ candidate
- inform | speech_act | operation-vocabulary | UTTER inform(target: CLAIM) | Present the proposition; preserve its holder/status.  ⟵ candidate
- propose | speech_act | operation-vocabulary | UTTER propose(target: TERM) | Suggest an action/idea; does not record it as performed.  ⟵ candidate
- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ dependency of event_sadie_adler_unmasking
- block_evaluation | constructor | TERM block_evaluation(block: STRING / TERM, maturity?: STRING, potential?: STRING, quality?: STRING, rank?: NUMBER, traps?: STRING) -> TERM | Constructs a structured evaluation, categorization, or ranking descriptor for a geological exploration block. | not: an external execution action or generic list sorting operation (use sort) | aliases: block assessment, block ranking, block rating, block categorization  ⟵ candidate
- calculation | constructor | TERM calculation(inputs: LIST[TERM], operation: STRING, result?: TERM) -> TERM | Constructs a descriptive representation of an arithmetic or algorithmic calculation step with inputs, operation identifier, and optional resulting value. | not: an executed runtime action or factual claim of outcome | aliases: math_operation, compute_step  ⟵ candidate
- character_trait | constructor | TERM character_trait(property: STRING, value: STRING / NUMBER) -> TERM | A character attribute | not: Not a claim about a real person  ⟵ candidate
- conditional | constructor | TERM conditional(condition: TERM, consequence: TERM) -> TERM | Constructs a structured conditional proposition term connecting a condition and consequence. descriptive logic structure. | aliases: if_then  ⟵ candidate
- conjunction | constructor | TERM conjunction(items: LIST[TERM]) -> TERM | All described components apply | not: Does not imply temporal order  ⟵ candidate
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ candidate
- include | constructor | TERM include(item: STRING / TERM) -> TERM | Require the identified content/item | not: Not permission to invent an instance in a recorded trace  ⟵ dependency of constraint_include_character_attribute_list
- measure | constructor | TERM measure(amount: NUMBER, unit: STRING / ATOM[currency]) -> TERM | A measured amount: a number with its unit symbol (a unit-category value such as unit_minute, cap_gb or currency::USD). Describes the amount only; asserts nothing. ATOM[currency] is also accepted and supplies the pinned currency identity; no exchange rate or conversion is implicit. | not: a symbol with the number baked in (char_age_18, size_16gb); a unitless count (use the quantity argument) | aliases: amount of, size of, measured in  ⟵ candidate
- negation | constructor | TERM negation(target: TERM) -> TERM | Constructs a descriptive semantic negation of a target descriptive proposition or condition term. | not: Check's runtime Boolean operator NOT or a speech-act decline | aliases: not, does not, negation, absence of  ⟵ candidate
- obligation | constructor | TERM obligation(actor: STRING / TERM, activity: TERM) -> TERM | Constructs a deontic obligation description requiring an actor to perform an activity. actor and activity specified. | aliases: duty, mandatory_activity  ⟵ candidate
- outshines | constructor | TERM outshines(brighter: STRING / TERM, dimmer: STRING / TERM) -> TERM | Constructs a description of relative visual brightness where a brighter light source overpowers the perceived brightness of a dimmer object. | not: an absolute numeric brightness measurement | aliases: outshines, overpowers brightness, drowns out light  ⟵ candidate
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ candidate
- sequence | constructor | TERM sequence(items: LIST[TERM]) -> TERM | Ordered described activities/content | not: Not unordered conjunction  ⟵ dependency of event_sadie_adler_unmasking
- similarity | constructor | TERM similarity(target: STRING / TERM, dimension?: STRING / TERM) -> TERM | Constructs a descriptor representing comparative closeness or similarity to a target along a given dimension. | not: spatial proximity (use rank_distance or next_to) or an assertion of exact identity (use identity) | aliases: closest_to, similar_to, resembles  ⟵ candidate
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ candidate
- test_condition | constructor | TERM test_condition(condition: STRING, expected: BOOL) -> TERM | A testable condition with the expected Boolean outcome | not: Expected outcome is not an observed result  ⟵ candidate
- weather_condition | constructor | TERM weather_condition(condition: STRING, location?: STRING / TERM / ATOM[country], severity?: STRING) -> TERM | A structured descriptor of atmospheric or weather phenomena such as wind, rain, or storm at an optional location; asserts nothing. | not: state_cold or state_warm (thermal states of physical objects) or occurred (past factual occurrence assertion) | aliases: weather, storm_condition, atmospheric_condition  ⟵ candidate
- well_wishes | constructor | TERM well_wishes(recipient?: STRING / TERM, sentiment?: STRING) -> TERM | Constructs a conversational discourse term representing well-wishes, good luck expressions, or parting encouragement. | not: a salutation greeting (use greeting) or apology (use apologize) | aliases: good_luck, best_wishes, encouragement  ⟵ candidate

### composites

- constraint_budget_limited | composite | constraint-value | TERM constraint_budget_limited() -> TERM | Limited budget. | = requirement(property="budget_limited", value=TRUE)  ⟵ candidate
- constraint_comprehensive | composite | constraint-value | TERM constraint_comprehensive() -> TERM | Must be comprehensive. | = requirement(property="comprehensive", value=TRUE)  ⟵ candidate
- constraint_exclude_flowery_language | composite | constraint-value | TERM constraint_exclude_flowery_language() -> TERM | Avoid flowery language. | = exclude(item="flowery_language")  ⟵ candidate
- constraint_exclude_liberation_theme | composite | constraint-value | TERM constraint_exclude_liberation_theme() -> TERM | Avoid liberation theme. | = exclude(item="liberation_theme")  ⟵ candidate
- constraint_include_character_attribute_list | composite | constraint-value | TERM constraint_include_character_attribute_list() -> TERM | Include character attributes. | = include(item="character_attribute_list")  ⟵ candidate
- constraint_realistic | composite | constraint-value | TERM constraint_realistic() -> TERM | Must be realistic. | = requirement(property="realistic", value=TRUE)  ⟵ candidate
- constraint_respectful | composite | constraint-value | TERM constraint_respectful() -> TERM | Must be respectful. | = requirement(property="respectful", value=TRUE)  ⟵ candidate
- constraint_single_choice | composite | constraint-value | TERM constraint_single_choice() -> TERM | Must pick a single choice. | = requirement(property="choice_count", value=1)  ⟵ candidate
- event_camper_in_sludge_pit | composite | event-value | TERM event_camper_in_sludge_pit() -> TERM | Campers interacting in a sludge pit. | = activity(verb="interact", actor="campers", location="sludge_pit")  ⟵ candidate
- event_sadie_adler_unmasking | composite | event-value | TERM event_sadie_adler_unmasking() -> TERM | Sadie Adler taking off her hat and peeling skin. | = sequence(items=[activity(verb="remove", actor="Sadie Adler", object="hat"), activity(verb="peel", actor="Sadie Adler", object="skin")])  ⟵ candidate
- topic_profanity | composite | topic-value | TERM topic_profanity() -> TERM | A composite term representing the topic of profanity. | = subject(kind="profanity") | not: potential_harms (which is generic) | aliases: profanity  ⟵ candidate
- topic_school_work_routine | composite | topic-value | TERM topic_school_work_routine() -> TERM | School and work routine. | = subject(kind="routine", qualifier=conjunction(items=[subject(kind="school"), subject(kind="work")]))  ⟵ candidate

### claim relations

- attribute_claim | claim_relation | CLAIM attribute_claim(subject: STRING / TERM / ATOM[platform_label], property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) | Asserts that a subject possesses a named property evaluated to a specific primitive or structured value. general property attribution claim. | aliases: property_value, word_property, has_property, property attribution  ⟵ related to statement
- causes | claim_relation | CLAIM causes(cause: CLAIM / TERM, effect: CLAIM) | Asserts a direct causal relationship producing an effect proposition. causal assertion. | aliases: produces  ⟵ candidate
- comfortable | claim_relation | CLAIM comfortable(person: TERM, value: BOOL) | Asserts whether a person or animal is comfortable in a situation. affective/state claim. | aliases: is_comfortable  ⟵ candidate
- controversial | claim_relation | CLAIM controversial(subject: STRING / TERM) | Asserts that a topic, policy, or practice is the subject of public debate or controversy. evaluative debate claim. | aliases: debated, disputed  ⟵ candidate
- enables | claim_relation | CLAIM enables(condition: TERM / CLAIM, outcome: TERM / CLAIM) | Asserts that an enabling condition or capability facilitates an outcome. enabling condition. | aliases: facilitates, allows  ⟵ candidate
- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ candidate
- has_state | claim_relation | CLAIM has_state(subject: TERM, state: STRING) | Asserts that an entity is currently in a physical, thermal, or operational state. state must be a valid state descriptor string. | aliases: in_state, state_is  ⟵ related to statement
- has_style | claim_relation | CLAIM has_style(target: CLAIM / EVENT / TERM, value: TERM / STRING) | Asserts that an artifact, utterance, or action possesses a designated style. style qualifier. | aliases: style_is  ⟵ candidate
- important | claim_relation | CLAIM important(target: TERM) | Asserts that a concept, activity, or condition is important or significant. evaluative importance claim. | aliases: significant  ⟵ candidate
- leads_to | claim_relation | CLAIM leads_to(cause: TERM, effect: TERM) | Asserts a conceptual consequence or progression from cause to effect. progression relation. | aliases: results_in  ⟵ candidate
- meets_needs | claim_relation | CLAIM meets_needs(subject: TERM, beneficiary: STRING / TERM) | Asserts that an item, activity, or plan satisfies the needs of a beneficiary. utility/satisfaction claim. | aliases: satisfies_needs  ⟵ candidate
- menu_works | claim_relation | CLAIM menu_works(property: STRING) | Asserts that a menu or recipe plan satisfies an operational criterion. menu evaluation. | aliases: menu_satisfies  ⟵ candidate
- motivated_by | claim_relation | CLAIM motivated_by(claim: CLAIM, motive: STRING / TERM) | Asserts that an action, rule, or claim is motivated by an underlying motive or goal. motive explanation. | aliases: rationale_is  ⟵ candidate
- occurred | claim_relation | CLAIM occurred(activity: TERM) | Asserts that an event, action, or activity took place in the past. past occurrence claim. | aliases: happened  ⟵ candidate
- occurred_recently | claim_relation | CLAIM occurred_recently(target: CLAIM) | Asserts temporal recency of an asserted occurrence or claim. temporal recency qualifier. | aliases: recently_happened  ⟵ candidate
- opposes | claim_relation | CLAIM opposes(actor: STRING / TERM, subject: STRING / TERM) | Asserts that an actor opposes or objects to a practice, entity, or policy. opposition stance. | aliases: objects_to, against  ⟵ candidate
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ candidate
- possesses | claim_relation | CLAIM possesses(subject: STRING / TERM, item: TERM, value: BOOL) | Asserts whether a subject possesses or lacks a stated property, capability, or entity. possession assertion with boolean polarity. | aliases: holds_property  ⟵ candidate
- prohibited | claim_relation | CLAIM prohibited(subject: STRING / TERM, location: STRING / TERM, condition?: STRING / TERM) | Asserts that a subject is prohibited from a location or activity under specified conditions. deontic prohibition claim. | aliases: forbidden, banned_from  ⟵ candidate
- proposed_policy | claim_relation | CLAIM proposed_policy(policy: TERM, requirements: LIST[TERM]) | Asserts that a proposed policy framework comprises the specified requirement terms. policy must be a policy term. | aliases: policy_proposal  ⟵ candidate
- recommended | claim_relation | CLAIM recommended(target: TERM / CLAIM) | Asserts an advisory recommendation that an activity or measure is advisable. advisory normative claim. | aliases: advisable  ⟵ candidate
- spatial_state | claim_relation | CLAIM spatial_state(relation: STRING, object: TERM, reference: TERM) | Asserts an observed spatial configuration between an object and a reference landmark. relation must specify spatial configuration. | aliases: placed_at, located_at  ⟵ related to statement
- statement | claim_relation | CLAIM statement(fact: TERM) | Foundational claim relation converting any descriptive TERM into an attributed, truth-evaluated assertion. universal fact assertion. | aliases: assert_fact, fact_claim, claim_statement  ⟵ candidate
- stereotype | claim_relation | CLAIM stereotype(target: STRING / TERM, trait: STRING / TERM) | Asserts that an attributed trait, generalization, or assumption about a demographic group or social category is a stereotype. | not: an individual character trait or verified fact | aliases: social_stereotype, generalization, bias  ⟵ candidate
- unaware | claim_relation | CLAIM unaware(person: STRING / TERM, topic: STRING / TERM) | Asserts epistemic lack of awareness regarding a topic, fact, or event. epistemic state. | aliases: ignorant_of  ⟵ candidate
- user_preference | claim_relation | CLAIM user_preference(constraints: TERM) | Asserts a user's stated preference constraints or dietary requirements. user constraint assertion. | aliases: stated_preference  ⟵ candidate

### links

- contrast | link | LINK contrast(first: CLAIM, second: CLAIM) | Expresses rhetorical qualification, opposition, or contrast between two claims. link between claims. | aliases: qualification, however  ⟵ candidate
- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ candidate
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ core
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ candidate
- then | link | LINK then(previous: EVENT, next: EVENT) | Represents temporal sequence and succession between two events where next follows previous. previous and next must be event terms. | aliases: followed_by, after_which  ⟵ candidate

### values

- art_story | value | artifact-value | Narrative story.  ⟵ candidate
- path_pandas_src_testing_pyx | value | code-value | Source code file path or exported symbol in scientific Python: path_pandas_src_testing_pyx. | aliases: path_pandas_src_testing_pyx  ⟵ candidate
- sym_pandas_testing_assert_almost_equal | value | code-value | Source code file path or exported symbol in scientific Python: sym_pandas_testing_assert_almost_equal. | aliases: sym_pandas_testing_assert_almost_equal  ⟵ candidate
- dom_safari | value | descriptive-value | Safari domain concept. | aliases: safari  ⟵ candidate
- tattoos | value | descriptive-value | Descriptive concept of tattoos in cultural and social contexts. | aliases: tattoos  ⟵ candidate
- yakuza | value | descriptive-value | Descriptive concept of yakuza in cultural and social contexts. | aliases: yakuza  ⟵ candidate
- unit_day | value | duration-unit-value | Day. | aliases: days  ⟵ candidate
- apple | value | entity-name | An apple fruit item, typically an ingredient or interactive food object. | not: food_label::tomato or other fruits/vegetables | aliases: apple, apples, red apple, green apple, apple slice  ⟵ candidate
- bread | value | entity-name | A bread loaf or slice food object. | aliases: bread  ⟵ candidate
- caddy | value | entity-name | A portable storage caddy, organizer box, or supply tote for carrying and organizing handheld tools and supplies. | not: cabinet (a stationary furniture cupboard) or safe (a secure metal lockbox) | aliases: caddy, supply caddy, wrapping caddy, tool caddy, organizer caddy, supply tote  ⟵ candidate
- coffee_maker | value | entity-name | A coffee-making appliance; not automatically a heating resource  ⟵ candidate
- dog | value | entity-name | Animal entity: dog. | not: animal_label::cat or animal_label::donkey | aliases: dog, dogs, canine, pup, puppy  ⟵ candidate
- dried_fruit | value | entity-name | Generic dried fruit food item. | not: fresh fruit or specific dried varieties like raisin or sultana | aliases: dried fruit, dried fruits  ⟵ candidate
- fridge | value | entity-name | A refrigerator cooling appliance. | aliases: fridge  ⟵ candidate
- grape_thompson_seedless | value | entity-name | Thompson Seedless grape variety. | not: wine grape cultivars like grape_merlot or grape_chardonnay | aliases: Thompson Seedless, thompson seedless grape, sultana grape  ⟵ candidate
- ice_cream | value | entity-name | Frozen dessert food item: ice cream. | not: entity_desserts or entity_sweet_food (generic menu categories) | aliases: ice cream, ice_cream  ⟵ candidate
- lettuce | value | entity-name | A head of lettuce or leafy green vegetable food item. | not: food_label::tomato or food_label::potato (other vegetable items) | aliases: lettuce, head of lettuce, salad greens  ⟵ candidate
- meat | value | entity-name | Food item: meat or beef. | not: animal_label::tuna or animal_label::fish (specific aquatic foods) | aliases: meat, beef  ⟵ candidate
- mittens | value | entity-name | Item or prop in joke/creative context: mittens. | aliases: mittens  ⟵ candidate
- oak_chips | value | entity-name | Oak wood pieces or barrels used for wine aging and flavor extraction. | not: grape_tannin or structural chemical additives | aliases: oak chips, oak pieces, oak barrels  ⟵ candidate
- resource_chiller | value | entity-name | Canonical abstract chilling resource when no particular appliance is named.  ⟵ candidate
- resource_heater | value | entity-name | Canonical abstract heating resource when no particular appliance is named.  ⟵ candidate
- sponge | value | entity-name | A porous, absorbent sponge cleaning tool or object. | not: tissue_box (a paper tissue box) or other wiping materials | aliases: sponge, cleaning sponge  ⟵ candidate
- spoon | value | entity-name | An eating or cooking utensil. | aliases: spoon  ⟵ candidate
- metric_order_late | value | metric-value | Whether an order is late. | aliases: order is late, delayed  ⟵ candidate
- tattooed_guests | value | recipient-value | Social, demographic, or institutional group: tattooed_guests. | aliases: tattooed_guests  ⟵ candidate
- reservation_unavailable | value | reservation-status-value | A reservation cannot be made. | aliases: no reservations  ⟵ candidate
- cat_game | value | search-value | Category: video game.  ⟵ candidate
- cat_limited_time_offers | value | search-value | Category: time-limited deals.  ⟵ candidate
- class_temple | value | semantic-category-value | The abstract class of temples. | aliases: temple, temples  ⟵ candidate
- shape_rectangular | value | shape-value | Rectangular. | aliases: rectangular, rectangle  ⟵ candidate
- shape_round | value | shape-value | Circular/round. | aliases: round, circular  ⟵ candidate
- shape_square | value | shape-value | Square. | aliases: square  ⟵ candidate
- shape_triangular | value | shape-value | Triangular. | aliases: triangular, triangle  ⟵ candidate
- in_front_of | value | spatial-relation | Positioned in front of. | aliases: in front of  ⟵ candidate
- left_of | value | spatial-relation | To the left of. | aliases: left of  ⟵ candidate
- next_to | value | spatial-relation | Adjacent to. | aliases: beside  ⟵ candidate
- on | value | spatial-relation | Resting atop. | aliases: on top of  ⟵ candidate
- right_of | value | spatial-relation | To the right of. | aliases: right of  ⟵ candidate
- state_cold | value | state-value | Cold or chilled condition. | aliases: cold, chilled  ⟵ candidate
- state_sliced | value | state-value | The condition of being sliced or cut into thin pieces. | not: the operation slice itself | aliases: sliced, slice, chopped, cut  ⟵ candidate
- state_warm | value | state-value | Warm or heated condition. | aliases: warm, hot  ⟵ candidate
- style_catchy | value | style-value | Catchy, attention-grabbing style. | aliases: catchy  ⟵ candidate
- style_narrative | value | style-value | Story-like narrative style. | aliases: narrative, story-style  ⟵ candidate
- topic_baldurs_gate_3 | value | topic-value | Baldur's Gate 3.  ⟵ candidate
- topic_food_safety | value | topic-value | Food safety guidelines, sanitary regulations, or handling practices. | aliases: food_safety  ⟵ candidate
- topic_pickup_lines | value | topic-value | Pickup lines.  ⟵ candidate
- topic_spider_man_2 | value | topic-value | Marvel's Spider-Man 2.  ⟵ candidate
