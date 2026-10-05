# Glossary retrieval for this item

Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6). 93 needs (decomposition: llm), 271 glossary records retrieved.

Every need below must end up expressed in the translation, or listed as unresolved in the coverage table *after* widening the search (`node /kit/rag.mjs widen "<need text>"`). Candidates are ranked best first; `exact` means a symbol or alias phrase literally occurs in the need.

## Needs and candidates

| need | kind | source | meaning | candidates |
|---|---|---|---|---|
| n1 | action | t1:s50 | Determine the truth value of a statement based on facts, rules, and preferences | `statement`*, `failure`, `motivated_by`, `decision`, `test_condition`, `run_tests`, `propose`, `assert_multinomial_scorer`, `constraint_realistic`, `calculation`, `rule_category_style_value`, `constraint_single_choice` |
| n2 | object | t1:s50 | The statement 'does the dinosaur enjoy the company of the husky?' | `statement`*, `topic_spider_man_2`, `style_catchy`, `dog`, `role_professor`, `resource_chiller`, `role_manager`, `resource_heater`, `chair`, `next_to`, `role_colleague`, `respond` |
| n3 | constraint | t1:s51 | Answer must be 'proved', 'disproved', or 'unknown' | `constraint_budget_limited`, `constraint_realistic`, `constraint_exclude_liberation_theme`, `constraint_include_character_attribute_list`, `test_condition`, `respond`*, `confirm`, `metric_order_late`, `assert_multinomial_scorer`, `constraint_beginner`, `constraint_exclude_flowery_language`, `unaware` |
| n4 | claim | t1:s3 | The akita wants to see the vampire | `art_plan`, `art_story`, `outcome`, `art_character_profile`, `cat_game`, `art_itinerary`, `enables`, `style_narrative`, `character`, `occurred_recently`, `aesthetic`, `char_2000s_anime_style` |
| n5 | object | t1:s3 | akita → `animal_label::<key>` | `art_plan`, `ryokan`, `art_story`, `resource_chiller`, `class_temple`, `sultana`, `resource_heater`, `art_structured_report`, `char_2000s_anime_style`, `coffee_maker`, `locale_hi_en`, `art_character_profile` |
| n6 | object | t1:s3 | vampire → `animal_label::<key>` | `art_story`, `art_plan`, `cat_game`, `art_character_profile`, `topic_spider_man_2`, `resource_chiller`, `character`, `bionic_person`, `art_short_text`, `style_narrative`, `resource_heater`, `coffee_maker` |
| n7 | claim | t1:s4 | The dalmatian has a 12 x 18 inches notebook | `laptop`*, `size_large`, `outcome`, `cap_gb`, `size_medium`, `unit_paragraph`, `pencil`, `pen`, `size_tall`, `unit_liter`, `size_queen`, `enables` |
| n8 | object | t1:s4 | dalmatian → `animal_label::<key>` | `chill`, `topic_baldurs_gate_3`, `mug`, `on`, `resource_chiller`, `next_to`, `right_of`, `left_of`, `in_front_of`, `resource_heater`, `sun`, `unit_day` |
| n9 | object | t1:s4 | notebook → `object_label::<key>` | `laptop`*, `mattress`, `textbook`, `pencil`, `pen`, `unit_paragraph`, `resource_chiller`, `cap_gb`, `resource_heater`, `clock`, `desk`, `material_memory_foam` |
| n10 | claim | t1:s5 | The dalmatian is a grain elevator operator | `path_sklearn_linear_model_logistic_py`, `outcome`, `unit_second`, `enables`, `cd`, `cardamom`, `occurred_recently`, `sequence`, `ongoing`, `leads_to`, `metric_order_late`, `important` |
| n11 | claim | t1:s6 | The duck brings an oil tank for the pelikan | `pour`, `outcome`, `enables`, `bowl`, `spatula`, `occurred_recently`, `leads_to`, `ongoing`, `meat`, `statement`, `pan`, `recommended` |
| n12 | object | t1:s6 | duck → `animal_label::<key>` | `animal_label`*, `topic_spider_man_2`, `dog`, `meat`, `spatula`, `mug`, `resource_chiller`, `sponge`, `style_catchy`, `resource_heater`, `coffee_maker`, `fridge` |
| n13 | object | t1:s6 | pelikan → `animal_label::<key>` | `chill`, `spatula`, `art_story`, `topic_baldurs_gate_3`, `dog`, `on`, `resource_chiller`, `in_front_of`, `pen`, `next_to`, `resource_heater`, `style_catchy` |
| n14 | object | t1:s6 | oil tank → `object_label::<key>` | `resource_heater`, `coffee_maker`, `heat`, `unit_liter`, `resource_chiller`, `pour`, `citric_acid`, `tartaric_acid`, `valet`, `state_full`, `cardamom`, `state_dirty` |
| n15 | claim | t1:s7 | The dugong has 71 dollars, a couch, a luxury aircraft, and is turning four | `turn`*, `art_itinerary`, `avail_out_of_stock`, `outcome`, `unit_year`, `topic_baldurs_gate_3`, `avail_in_stock`, `dom_safari`, `art_plan`, `enables`, `chair`, `occurred_recently` |
| n16 | object | t1:s7 | dugong → `animal_label::<key>` | `chill`, `topic_baldurs_gate_3`, `spatula`, `resource_chiller`, `mug`, `ryokan`, `state_dirty`, `resource_heater`, `yakuza`, `coffee_maker`, `nutmeg`, `chair` |
| n17 | object | t1:s7 | dollars → `currency::<key>` | `currency`*, `rank_price`, `avail_out_of_stock`, `resource_chiller`, `unit_year`, `unit_character`, `state_full`, `avail_in_stock`, `unit_liter`, `state_empty`, `resource_heater`, `credit_card` |
| n18 | object | t1:s7 | couch → `object_label::<key>` | `chair`, `mattress`, `example_a_select_two_pillows_and_move_those_objects`, `art_plan`, `resource_chiller`, `wall`, `living_room`, `on`, `resource_heater`, `bed`, `night_stand`, `coffee_maker` |
| n19 | object | t1:s7 | luxury aircraft → `object_label::<key>` | `laptop`, `chair`, `art_itinerary`, `size_large`, `design_parameters`, `resource_chiller`, `avail_in_stock`, `avail_out_of_stock`, `size_queen`, `size_medium`, `moon`, `entity_order_vs_assemble_plan` |
| n20 | claim | t1:s8 | The fangtooth invests in the company owned by the liger | `avail_in_stock`, `outcome`, `avail_out_of_stock`, `size_large`, `enables`, `ryokan`, `occurred_recently`, `ongoing`, `mug`, `leads_to`, `important`, `recommended` |
| n21 | object | t1:s8 | fangtooth → `animal_label::<key>` | `chill`, `topic_baldurs_gate_3`, `spatula`, `style_catchy`, `resource_chiller`, `mug`, `in_front_of`, `on`, `resource_heater`, `close`, `coffee_maker`, `target` |
| n22 | object | t1:s8 | liger → `animal_label::<key>` | `chill`, `topic_baldurs_gate_3`, `resource_chiller`, `spatula`, `on`, `mug`, `resource_heater`, `right_of`, `left_of`, `next_to`, `in_front_of`, `coffee_maker` |
| n23 | claim | t1:s9 | The flamingo surrenders to the butterfly | `topic_spider_man_2`, `outcome`, `enables`, `illuminates`, `hover`, `occurred_recently`, `constraint_exclude_flowery_language`, `candle`, `lamp`, `leads_to`, `ongoing`, `statement` |
| n24 | object | t1:s9 | flamingo → `animal_label::<key>` | `resource_chiller`, `resource_heater`, `coffee_maker`, `chill`, `heat`, `mug`, `candle`, `spatula`, `lamp`, `alcohol`, `cardamom`, `chair` |
| n25 | object | t1:s9 | butterfly → `animal_label::<key>` | `topic_spider_man_2`, `entity_flowers`, `resource_chiller`, `moon`, `watch`, `resource_heater`, `tattooed_guests`, `hover`, `coffee_maker`, `tattoos`, `earth`, `art_itinerary` |
| n26 | claim | t1:s10 | The mule has 95 dollars | `dog`, `outcome`, `caddy`, `art_itinerary`, `enables`, `add_to_cart`, `rank_price`, `path_pandas_src_testing_pyx`, `currency`, `occurred_recently`, `avail_out_of_stock`, `leads_to` |
| n27 | object | t1:s10 | mule → `animal_label::<key>` | `animal_label`*, `dog`, `caddy`, `art_itinerary`, `meat`, `resource_chiller`, `event_sadie_adler_unmasking`, `event_camper_in_sludge_pit`, `resource_heater`, `coffee_maker`, `dulce_de_nata`, `chair` |
| n28 | reasoning | t1:s12 | Rule 1: If an animal brings an oil tank for the bison, the mermaid dances with the poodle | `dog`, `animal_label`, `sym_pandas_testing_assert_almost_equal`, `art_technical_explanation`, `path_pandas_src_testing_pyx`, `event_sadie_adler_unmasking`, `event_camper_in_sludge_pit`, `rejects`, `style_catchy`, `meat`, `supports`, `prohibited` |
| n29 | reasoning | t1:s13 | Rule 2: If the dugong invests in the ant's company, the ant won't swear to the frog | `topic_spider_man_2`, `topic_baldurs_gate_3`, `inform`, `possesses`, `dog`, `revises`, `rejects`, `dom_ovr`, `supports`, `role_agent`, `drop`, `ask` |
| n30 | reasoning | t1:s14 | Rule 3: If an animal wants to see the duck, it shouts at the dalmatian | `topic_baldurs_gate_3`, `dog`, `animal_label`, `prohibited`, `possesses`, `unaware`, `rejects`, `metric_order_late`, `drop`, `meat`, `supports`, `constraint_single_choice` |
| n31 | reasoning | t1:s15 | Rule 4: If a creature builds a power plant near the mannikin, it won't borrow the mermaid's weapons | `topic_baldurs_gate_3`, `constraint_budget_limited`, `constraint_single_choice`, `rejects`, `constraint_realistic`, `art_technical_explanation`, `trash_can`, `supports`, `revises`, `possesses`, `island`, `potential_harms` |
| n32 | reasoning | t1:s16 | Rule 5: If an animal brings an oil tank for the dragon, the mermaid swears to the pigeon | `animal_label`, `pour`, `sym_pandas_testing_assert_almost_equal`, `path_pandas_src_testing_pyx`, `prohibited`, `mug`, `rejects`, `art_story`, `constraint_single_choice`, `inform`, `supports`, `dog` |
| n33 | reasoning | t1:s17 | Rule 6: The basenji suspects the dove if an animal swims in the pool near the liger's house | `rejects`, `dog`, `supports`, `topic_baldurs_gate_3`, `inform`, `subject`, `confirm`, `close`, `revises`, `allowed_to_enter`, `ask`, `meat` |
| n34 | reasoning | t1:s18 | Rule 7: If the basenji suspects the dove, the dove creates a castle for the dolphin | `topic_baldurs_gate_3`, `inform`, `rejects`, `rule_category_style_value`, `rule_category_shape_value`, `sun`, `topic_spider_man_2`, `supports`, `revises`, `face`, `place`, `subject` |
| n35 | reasoning | t1:s19 | Rule 8: The dalmatian borrows a weapon from the seal if its notebook fits in a 9.5x20.1 box | `cardboard_box`*, `laptop`*, `topic_baldurs_gate_3`, `pour`, `safe`, `path_sklearn_linear_model_logistic_py`, `pen`, `art_technical_explanation`, `rejects`, `at_least`, `close`, `rule_examples_general` |
| n36 | reasoning | t1:s20 | Rule 9: The butterfly invests in the bear's company if the flamingo surrenders to the butterfly | `topic_spider_man_2`, `topic_baldurs_gate_3`, `inform`, `rejects`, `event_sadie_adler_unmasking`, `possesses`, `supports`, `revises`, `drop`, `enables`, `decision`, `has_state` |
| n37 | reasoning | t1:s21 | Rule 10: If the dalmatian works in agriculture, it borrows a weapon from the seal | `topic_baldurs_gate_3`, `possesses`, `spatula`, `constrained_by`, `rejects`, `activity`, `state_dirty`, `works_best`, `revises`, `inform`, `supports`, `constraint_single_choice` |
| n38 | reasoning | t1:s22 | Rule 11: If an animal invests in the bear's company, it invests in the pigeon's company | `topic_baldurs_gate_3`, `dog`, `event_camper_in_sludge_pit`, `possesses`, `decision`, `inform`, `size_small`, `comfortable`, `topic_spider_man_2`, `subject`, `causes`, `place` |
| n39 | reasoning | t1:s23 | Rule 12: If the dolphin doesn't take over the rhino's emperor and the ant doesn't stop the rhino's victory, the rhino brings an oil tank for the dragon | `topic_spider_man_2`, `sym_pandas_testing_assert_almost_equal`, `add_to_cart`, `inform`, `path_pandas_src_testing_pyx`, `rejects`, `pick_up`*, `rule_category_state_value`, `prohibited`, `dom_safari`, `supports`, `dog` |
| n40 | reasoning | t1:s24 | Rule 13: If the woodpecker doesn't shout at the dalmatian, the dalmatian shouts at the cougar | `topic_baldurs_gate_3`, `dog`, `rejects`, `metric_order_late`, `revises`, `prohibited`, `unit_sentence`, `supports`, `tone_urgent`, `constraint_exclude_flowery_language`, `in_front_of`, `metric_response_time` |
| n41 | reasoning | t1:s25 | Rule 14: If a creature doesn't swear to the frog, it won't stop the rhino's victory | `rejects`, `rule_speech_acts_general`, `topic_spider_man_2`, `inform`, `prohibited`, `failure`, `confirm`, `chill`, `acknowledge`, `revises`, `topic_baldurs_gate_3`, `supports` |
| n42 | reasoning | t1:s26 | Rule 15: The dugong invests in the ant's company if it has more money than the mule | `at_least`, `avail_out_of_stock`, `topic_baldurs_gate_3`, `cat_limited_time_offers`, `dog`, `rank_price`, `event_camper_in_sludge_pit`, `avail_in_stock`, `dom_ovr`, `dom_safari`, `revises`, `role_agent` |
| n43 | reasoning | t1:s27 | Rule 16: The dinosaur enjoys the husky's companionship if an animal swears to the pigeon | `dog`, `topic_spider_man_2`, `comfortable`, `topic_baldurs_gate_3`, `possesses`, `role_professor`, `rejects`, `style_catchy`, `close`, `supports`, `event_camper_in_sludge_pit`, `next_to` |
| n44 | reasoning | t1:s28 | Rule 17: If an animal brings an oil tank for the pelikan, the woodpecker doesn't shout at the dalmatian | `dog`, `animal_label`, `meat`, `rejects`, `topic_baldurs_gate_3`, `constraint_17_plus`, `prohibited`, `pour`, `ask`, `supports`, `revises`, `spatula` |
| n45 | reasoning | t1:s29 | Rule 18: If an animal invests in the pigeon's company, it borrows a weapon from the mermaid | `dog`, `animal_label`, `meat`, `possesses`, `art_technical_explanation`, `drop`, `art_story`, `target`, `rejects`, `role_agent`, `entity_order_vs_assemble_plan`, `supports` |
| n46 | reasoning | t1:s30 | Rule 19: If an animal wants to see the vampire, the owl brings an oil tank for the dove | `cat_game`, `cat_limited_time_offers`, `art_story`, `art_technical_explanation`, `art_plan`, `topic_baldurs_gate_3`, `pour`, `art_itinerary`, `rejects`, `dog`, `revises`, `supports` |
| n47 | reasoning | t1:s31 | Rule 20: If the owl brings an oil tank for the dove, the dove won't create a castle for the dolphin | `inform`, `constraint_single_choice`, `rule_category_constraint_value`, `topic_baldurs_gate_3`, `constraint_budget_limited`, `rejects`, `pour`, `art_technical_explanation`, `supports`, `exempt_from`, `bowl`, `revises` |
| n48 | reasoning | t1:s32 | Rule 21: The gorilla calls the worm if an animal shouts at the cougar | `dog`, `animal_label`, `sym_pandas_testing_assert_almost_equal`, `path_pandas_src_testing_pyx`, `prohibited`, `cat_limited_time_offers`, `metric_order_late`, `unit_sentence`, `causes`, `rejects`, `topic_baldurs_gate_3`, `revises` |
| n49 | reasoning | t1:s33 | Rule 22: The owl won't bring an oil tank for the dove if its notebook fits in an 18.4x16.6 box | `cardboard_box`*, `laptop`*, `topic_baldurs_gate_3`, `pour`, `art_itinerary`, `bowl`, `mug`, `rejects`, `constraint_budget_limited`, `art_technical_explanation`, `supports`, `add_to_cart` |
| n50 | reasoning | t1:s34 | Rule 23: If an animal swears to the elk, it won't bring an oil tank for the dragon | `dog`, `animal_label`, `meat`, `supports`, `prohibited`, `inform`, `possesses`, `rejects`, `constraint_single_choice`, `constraint_respectful`, `add_to_cart`, `revises` |
| n51 | reasoning | t1:s35 | Rule 24: If the dugong owns a luxury aircraft, it invests in the ant's company | `avail_out_of_stock`, `dom_safari`, `topic_baldurs_gate_3`, `possesses`, `inform`, `art_itinerary`, `avail_in_stock`, `art_plan`, `rejects`, `revises`, `supports`, `dom_ovr` |
| n52 | reasoning | t1:s36, t1:s37 | Rule 25: If an animal calls the worm, the mermaid swims in the pool next to the badger's house | `dog`, `animal_label`, `next_to`*, `sym_pandas_testing_assert_almost_equal`, `cat_game`, `topic_spider_man_2`, `sponge`, `path_pandas_src_testing_pyx`, `then`, `topic_baldurs_gate_3`, `rejects`, `class_temple` |
| n53 | reasoning | t1:s38 | Rule 26: If an animal takes over the songbird's emperor, it stops the rhino's victory | `topic_baldurs_gate_3`, `role_manager`, `rule_speech_acts_general`, `role_professor`, `cat_game`, `inform`, `dog`, `drop`, `sym_pandas_testing_assert_almost_equal`, `topic_spider_man_2`, `prohibited`, `rejects` |
| n54 | reasoning | t1:s39 | Rule 27: The dolphin doesn't take over the rhino's emperor if the dove creates a castle for the dolphin | `inform`, `topic_spider_man_2`, `exempt_from`, `rejects`, `pick_up`*, `constraint_respectful`, `prohibited`, `supports`, `dom_safari`, `revises`, `constraint_single_choice`, `role_manager` |
| n55 | reasoning | t1:s40 | Rule 28: If the butterfly borrows a weapon from the mermaid, the mermaid won't dance with the poodle | `topic_spider_man_2`, `prohibited`, `art_technical_explanation`, `event_sadie_adler_unmasking`, `rejects`, `revises`, `constraint_exclude_flowery_language`, `obligation`, `entity_order_vs_assemble_plan`, `style_catchy`, `supports`, `path_pandas_src_testing_pyx` |
| n56 | reasoning | t1:s41 | Rule 1 is preferred over Rule 28 | `rule_examples_general`, `rule_category_transformation_value`, `constraint_single_choice`, `rule_category_constraint_value`, `at_least`, `rejects`, `prohibited`, `constrained_by`, `rule_support_primitives_general`, `supports`, `revises`, `constraint_respectful` |
| n57 | reasoning | t1:s42 | Rule 18 is preferred over Rule 4 | `rule_examples_general`, `rule_category_transformation_value`, `constraint_17_plus`, `constraint_single_choice`, `rule_category_constraint_value`, `at_least`, `rejects`, `supports`, `rule_category_style_value`, `exempt_from`, `revises`, `proposed_policy` |
| n58 | reasoning | t1:s43 | Rule 22 is preferred over Rule 19 | `rule_category_transformation_value`, `constraint_17_plus`, `at_least`, `constraint_budget_limited`, `rule_category_constraint_value`, `proposed_policy`, `rejects`, `supports`, `rule_category_style_value`, `constraint_single_choice`, `at_most`, `revises` |
| n59 | reasoning | t1:s44 | Rule 23 is preferred over Rule 12 | `rule_examples_general`, `rule_category_transformation_value`, `constraint_17_plus`, `rule_category_constraint_value`, `at_least`, `constraint_single_choice`, `constraint_budget_limited`, `prohibited`, `rejects`, `supports`, `constraint_respectful`, `rule_category_style_value` |
| n60 | reasoning | t1:s45 | Rule 26 is preferred over Rule 14 | `rule_structural_constructs`, `rule_category_transformation_value`, `rule_supplemental_general`, `constraint_17_plus`, `rule_category_constraint_value`, `constraint_budget_limited`, `at_least`, `constraint_single_choice`, `rejects`, `constraint_respectful`, `supports`, `rule_category_style_value` |
| n61 | reasoning | t1:s46 | Rule 3 is preferred over Rule 17 | `constraint_17_plus`, `rule_examples_general`, `topic_baldurs_gate_3`, `constraint_single_choice`, `rejects`, `rule_category_constraint_value`, `at_least`, `supports`, `at_most`, `revises`, `constraint_respectful`, `constraint_comprehensive` |
| n62 | reasoning | t1:s47 | Rule 7 is preferred over Rule 20 | `rule_supplemental_general`, `rule_category_transformation_value`, `constraint_17_plus`, `at_least`, `constraint_single_choice`, `rule_category_constraint_value`, `rejects`, `constraint_respectful`, `rule_category_style_value`, `supports`, `revises`, `constrained_by` |
| n63 | reasoning | t1:s48 | A rule is only applicable if all of its antecedents can be proved | `rule_support_primitives_general`, `constrained_by`, `prohibited`, `rejects`, `validates_parameter`, `exempt_from`, `supports`, `rule_category_constraint_value`, `revises`, `confirm`, `enables`, `rule_trace_relations_general` |
| n64 | reasoning | t1:s49 | Preferred rules resolve contradictions in derived conclusions | `supports`, `rejects`, `contrast`, `failure`, `varies_with`, `subject`, `rule_category_constraint_value`, `test_condition`, `revises`, `rule_structural_constructs`, `distracts_from`, `metric_response_time` |
| n65 | object | t1:s12 | bison → `animal_label::<key>` | `animal_label`*, `dog`, `sym_pandas_testing_assert_almost_equal`, `meat`, `topic_spider_man_2`, `resource_chiller`, `unit_year`, `caddy`, `path_pandas_src_testing_pyx`, `resource_heater`, `yakuza`, `coffee_maker` |
| n66 | object | t1:s12 | mermaid → `animal_label::<key>` | `art_story`, `sponge`, `figurine`, `art_short_text`, `art_plan`, `topic_spider_man_2`, `art_character_profile`, `resource_chiller`, `char_2000s_anime_style`, `resource_heater`, `bionic_person`, `animal_label`* |
| n67 | object | t1:s12 | poodle → `animal_label::<key>` | `chill`, `dog`, `spatula`, `topic_baldurs_gate_3`, `meat`, `mug`, `in_front_of`, `resource_chiller`, `style_catchy`, `ryokan`, `resource_heater`, `right_of` |
| n68 | object | t1:s13 | ant → `animal_label::<key>` | `topic_spider_man_2`, `art_plan`, `dog`, `resource_chiller`, `dom_ovr`, `target`, `moon`, `art_story`, `entity_cake`, `earth`, `resource_heater`, `art_technical_explanation` |
| n69 | object | t1:s13 | frog → `animal_label::<key>` | `art_plan`, `topic_spider_man_2`, `sponge`, `art_story`, `art_technical_explanation`, `dog`, `resource_chiller`, `pen`, `resource_heater`, `art_character_profile`, `art_short_text`, `coffee_maker` |
| n70 | object | t1:s15 | mannikin → `animal_label::<key>` | `chill`, `ryokan`, `topic_baldurs_gate_3`, `art_story`, `resource_chiller`, `sultana`, `resource_heater`, `on`, `maqluba`, `yakuza`, `right_of`, `coffee_maker` |
| n71 | object | t1:s15 | power plant → `object_label::<key>` | `resource_chiller`, `resource_heater`, `coffee_maker`, `lamp`, `unit_year`, `unit_hour`, `unit_day`, `unit_second`, `fridge`, `cd`, `unit_item`, `chair` |
| n72 | object | t1:s15 | weapon → `object_label::<key>` | `spatula`, `art_plan`, `resource_chiller`, `format_bullet_list`, `target`, `meat`, `resource_heater`, `drop`, `coffee_maker`, `face`, `resource_sink`, `knife` |
| n73 | object | t1:s16 | dragon → `animal_label::<key>` | `chill`, `topic_spider_man_2`, `sym_pandas_testing_assert_almost_equal`, `cat_game`, `art_story`, `path_pandas_src_testing_pyx`, `art_plan`, `ryokan`, `class_temple`, `resource_chiller`, `art_itinerary`, `dom_safari` |
| n74 | object | t1:s16 | pigeon → `animal_label::<key>` | `spatula`, `topic_baldurs_gate_3`, `pen`, `topic_spider_man_2`, `resource_chiller`, `resource_heater`, `pan`, `moon`, `coffee_maker`, `sun`, `animal_label`*, `resource_sink` |
| n75 | object | t1:s17 | basenji → `animal_label::<key>` | `resource_sink`, `chill`, `rinse`, `resource_chiller`, `sponge`, `resource_heater`, `bowl`, `coffee_maker`, `pour`, `chair`, `shower`, `mattress` |
| n76 | object | t1:s17 | dove → `animal_label::<key>` | `in_front_of`, `resource_chiller`, `resource_heater`, `behind`, `locale_en_us`, `animal_label`*, `resource_sink`, `coffee_maker`, `rank_distance`, `chair`, `example_a_select_two_pillows_and_move_those_objects`, `exists_in` |
| n77 | object | t1:s17 | pool → `object_label::<key>` | `resource_sink`, `resource_chiller`, `wall`, `shape_oval`, `bowl`, `sponge`, `resource_heater`, `shape_triangular`, `pour`, `material_memory_foam`, `coffee_maker`, `shower` |
| n78 | object | t1:s17 | house → `object_label::<key>` | `chair`, `art_plan`, `wall`, `resource_chiller`, `living_room`, `door`, `resource_heater`, `floor`, `fridge`, `coffee_maker`, `night_stand`, `lamp` |
| n79 | object | t1:s18 | castle → `object_label::<key>` | `art_story`, `ryokan`, `art_itinerary`, `class_temple`, `resource_chiller`, `art_plan`, `art_structured_report`, `resource_heater`, `wall`, `coffee_maker`, `new_york_university`, `resource_sink` |
| n80 | object | t1:s18 | dolphin → `animal_label::<key>` | `animal_label`*, `topic_spider_man_2`, `style_catchy`, `dog`, `resource_chiller`, `waterproof_stickers`, `resource_heater`, `tattooed_guests`, `chair`, `dom_ovr`, `class_beach`, `cheese` |
| n81 | object | t1:s19 | seal → `animal_label::<key>` | `chill`, `resource_chiller`, `in_front_of`, `on`, `behind`, `resource_heater`, `next_to`, `under`, `coffee_maker`, `tone_urgent`, `left_of`, `animal_label`* |
| n82 | object | t1:s20 | bear → `animal_label::<key>` | `animal_label`*, `bread`, `topic_spider_man_2`, `cat_game`, `sym_pandas_testing_assert_almost_equal`, `dog`, `path_pandas_src_testing_pyx`, `caddy`, `resource_chiller`, `art_character_profile`, `sponge`, `event_sadie_adler_unmasking` |
| n83 | object | t1:s23 | rhino → `animal_label::<key>` | `animal_label`*, `topic_spider_man_2`, `sym_pandas_testing_assert_almost_equal`, `dog`, `dom_safari`, `path_pandas_src_testing_pyx`, `yakuza`, `resource_chiller`, `spatula`, `resource_heater`, `tone_empathetic`, `chair` |
| n84 | object | t1:s24 | woodpecker → `animal_label::<key>` | `bread`, `topic_baldurs_gate_3`, `spatula`, `caddy`, `pen`, `pencil`, `resource_chiller`, `dog`, `oak_chips`, `meat`, `resource_heater`, `coffee_maker` |
| n85 | object | t1:s24 | cougar → `animal_label::<key>` | `dog`, `in_front_of`, `resource_chiller`, `next_to`, `right_of`, `resource_heater`, `left_of`, `animal_label`*, `on`, `locale_fr`, `coffee_maker`, `role_friend` |
| n86 | object | t1:s27 | dinosaur → `animal_label::<key>` | `topic_spider_man_2`, `figurine`, `resource_chiller`, `sponge`, `bionic_person`, `spatula`, `resource_heater`, `entity_desserts`, `dog`, `earth`, `watch`, `coffee_maker` |
| n87 | object | t1:s27 | husky → `animal_label::<key>` | `chill`, `topic_baldurs_gate_3`, `dog`, `meat`, `resource_chiller`, `spatula`, `in_front_of`, `on`, `resource_heater`, `style_catchy`, `right_of`, `coffee_maker` |
| n88 | object | t1:s30 | owl → `animal_label::<key>` | `art_plan`, `art_story`, `resource_chiller`, `class_temple`, `art_character_profile`, `resource_heater`, `style_catchy`, `art_technical_explanation`, `nighttime`, `topic_baldurs_gate_3`, `illuminates`, `coffee_maker` |
| n89 | object | t1:s34 | elk → `animal_label::<key>` | `chill`, `topic_baldurs_gate_3`, `resource_chiller`, `on`, `in_front_of`, `style_catchy`, `right_of`, `resource_heater`, `animal_label`*, `target`, `next_to`, `left_of` |
| n90 | object | t1:s32 | gorilla → `animal_label::<key>` | `chill`, `animal_label`*, `topic_spider_man_2`, `sponge`, `dog`, `art_story`, `resource_chiller`, `dom_safari`, `bionic_person`, `sym_pandas_testing_assert_almost_equal`, `path_pandas_src_testing_pyx`, `eastern_cape` |
| n91 | object | t1:s32 | worm → `animal_label::<key>` | `sym_pandas_testing_assert_almost_equal`, `resource_chiller`, `sponge`, `path_pandas_src_testing_pyx`, `topic_baldurs_gate_3`, `topic_spider_man_2`, `spatula`, `nutmeg`, `resource_heater`, `cloves`, `bionic_person`, `animal_label`* |
| n92 | object | t1:s37 | badger → `animal_label::<key>` | `animal_label`*, `cat_game`, `dog`, `sym_pandas_testing_assert_almost_equal`, `topic_spider_man_2`, `caddy`, `event_sadie_adler_unmasking`, `path_pandas_src_testing_pyx`, `resource_chiller`, `resource_heater`, `yakuza`, `coffee_maker` |
| n93 | object | t1:s38 | songbird → `animal_label::<key>` | `chill`, `cat_game`, `topic_baldurs_gate_3`, `resource_chiller`, `cardamom`, `topic_jazz_piano`, `topic_classical_piano`, `piano`, `alcohol`, `tone_urgent`, `coffee_maker`, `song` |

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

- failure.system → platform_label
- run_tests.target → platform_label
- chill.destination → object_label
- pour.destination → object_label
- heat.destination → object_label
- measure.unit → currency
- subject.qualifier → platform_label
- subject.location → country
- face.target → object_label
- place.destination → object_label
- place.location → object_label
- activity.object → object_label, food_label, animal_label
- activity.location → country
- activity.instrument → object_label, platform_label
- pick_up.target → object_label, food_label
- pick_up.source → object_label
- pick_up.color → color_label
- rinse.destination → object_label
- requirement.value → platform_label
- attribute_claim.subject → platform_label
- attribute_claim.value → platform_label
- walk.destination → object_label

## Retrieved records

### Shared rules that govern the records below (full text)

**rule_lexical_groups** (v19/rule/lexical-groups; rule governing platform_label)

Section 3.1 defines value groups: `group::key` values of type ATOM[group]. Open groups admit any key of their form (examples are not whitelists); standard groups admit the codes of their bundled standard (ISO 3166-1 alpha-2 for country, ISO 4217 for currency). Leaf values are never glossary entries. Consumer signatures alone decide where a group may appear. Retired bare symbols are invalid.

**rule_reading_guide** (v19/rule/reading-guide; core)

The spec governs syntax/types; this glossary defines vocabulary. Signature notation: ? optional, A / B explicit alternatives, void no result. Omitted optional arguments are unspecified. Value entries are category-refined STRING primitives; complex meanings require composition. Aliases are contextual hints, not unconditional equivalences. Report ambiguity. IDs use v19/<category>/<symbol>, v19/support/<symbol> or v19/composite/<symbol>. Statuses apply to this candidate: Retained preserves meaning; Adapted uses the stated contract; Composite requires TERM (bare STRING deprecated); Structural is syntax/argument vocabulary; Needs clarification is unusable until resolved; Deprecated is historical; Accepted is usable within this candidate.

**rule_recording_signatures** (v19/rule/recording-signatures; rule governing run_tests)

RECORD ACTION uses the operation signature with REF[STRING] → TERM and LIST[REF[STRING]] → LIST[TERM]; other types/categories stay unchanged. Return EVENT, never the runtime result. Record actual outputs as attributed CLAIMs. Do not infer missing resources.

**rule_speech_acts_general** (v19/rule/speech-acts-general; candidate)

UTTER-only, void, with the spec's speech attributes and LIST[TERM] constraints. No result binding. Literal content cannot replace required semantic arguments for structured coverage.

**rule_structural_constructs** (v19/rule/structural-constructs; candidate)

Apply spec Sections 2–14 for modes, binding, control, calls, claims, records and canonical form. No extra syntax is introduced by documentation aliases types-lexicon/action/bind. Epistemic and recording statuses are reserved in their grammar positions. SOURCE and lower-case source are distinct; names are case-sensitive. Residual descriptive values cannot hide propositions.

**rule_trace_relations_general** (v19/rule/trace-relations-general; candidate)

Relations cover their published signatures only; recording a success differs from assuming it. No unlisted reasoning relation is implied.

**rule_attributes_and_generate** (v19/rule/attributes-and-generate; rule governing art_plan)

Attribute entries name arguments; legality/types come from each operation, not global membership. GENERATE uses the spec's core fields; retained artifact profiles return STRING. Numeric/list results need explicit profiles. Legacy itinerary fields expand to TERM constraints: duration/duration_unit → duration(amount,unit); stop_min_per_day/stop_requirement → minimum_per_period(class,count,period=unit_day), never an inferred temple class; max_walk_duration/unit → maximum_between_stops(activity="walk",amount,unit). No legacy shorthand is enabled. Old events/character_properties/transformations become explicitly scoped TERM constraints. Message purpose is TERM, not send_email.content: GENERATE exact STRING content, then send. Report opaque fallback separately.

**rule_category_artifact_value** (v19/rule/category/artifact-value; rule governing art_plan)

STRING artifact class for GENERATE.target. art_story says what kind of artifact to produce, not what occurs in its plot.

**rule_category_capacity_unit_value** (v19/rule/category/capacity-unit-value; rule governing cap_gb)

Preserve original binary-unit definitions for audit, but mark Needs clarification: GB/TB aliases conflate decimal and binary units. No silent change to scale.

**rule_category_character_property_value** (v19/rule/category/character-property-value; rule governing char_2000s_anime_style)

TERM-described trait/style. Use constraints and explicit inclusion/scope; do not use an ungoverned character_properties attribute.

**rule_category_code_value** (v19/rule/category/code-value; rule governing assert_multinomial_scorer)

path_/sym_ remain STRING identities; migrated chg_/assert_ are TERM constructors. Do not recover an exact file path by guessing from underscores.

**rule_category_constraint_value** (v19/rule/category/constraint-value; candidate)

Existing requirements are TERM constructors, except unresolved entries explicitly marked. `constraints=[constraint_realistic]` is invalid; construct the TERM first.

**rule_category_descriptive_value** (v19/rule/category/descriptive-value; rule governing dom_safari)

STRING modifier/domain label; never a free-form proposition. dom_sgi needs its intended referent established before semantically dependent use.

**rule_category_duration_unit_value** (v19/rule/category/duration-unit-value; rule governing unit_paragraph)

STRING units partitioned into temporal (second through year) and output counts (word/item/paragraph/character). Do not use unit_word as elapsed time. Months/years are calendar units, not fixed seconds.

**rule_category_entity_name** (v19/rule/category/entity-name; rule governing dog)

STRING descriptors select kinds/resources. `mug` is a descriptor, not REF. Resource symbols may be used only when the source explicitly requests such a resource; missing equipment is not automatically inserted.

**rule_category_event_value** (v19/rule/category/event-value; rule governing event_sadie_adler_unmasking)

TERM-described narrative event, not a recorded EVENT. Require inclusion explicitly when generating a story.

**rule_category_format_value** (v19/rule/category/format-value; rule governing format_bullet_list)

STRING format. format_email is layout, not the action send_email.

**rule_category_locale_value** (v19/rule/category/locale-value; rule governing locale_hi_en)

STRING locale. “English” alone does not always mean locale_en_us; preserve ambiguity.

**rule_category_location_name** (v19/rule/category/location-name; rule governing ryokan)

STRING location descriptor. A `table` surface is not the generated artifact category art_table.

**rule_category_metric_value** (v19/rule/category/metric-value; rule governing metric_order_late)

STRING metric identity, not a Boolean value. Uptime and response time need numeric observations with units; order-late is Boolean-valued. Do not type every metric as BOOL.

**rule_category_product_attribute_value** (v19/rule/category/product-attribute-value; rule governing size_large)

STRING color/size/product-market facets. gender_women describes a product category, not an assertion about a person's gender.

**rule_category_recipient_value** (v19/rule/category/recipient-value; rule governing role_professor)

STRING roles or explicit named recipients. A role is not an exact person's identity. Keep an explicit name where substituting a role loses information.

**rule_category_search_value** (v19/rule/category/search-value; rule governing cat_game)

STRING refinements rank_ / dir_ / cat_ / avail_ / genre_ are separate. rank_rating may fill rank_field; genre_label::comedy may not. “Cheapest” usually requires both rank_price and dir_asc, not rank_price alone.

**rule_category_semantic_category_value** (v19/rule/category/semantic-category-value; rule governing class_temple)

STRING class label used by typed constraints. class_temple describes a class, not an acquired physical temple reference.

**rule_category_shape_value** (v19/rule/category/shape-value; candidate)

STRING geometry. shape_round may select a circular object; it does not imply color or dimensions.

**rule_category_spatial_relation** (v19/rule/category/spatial-relation; rule governing next_to)

STRING relation used by place. `in` and `on` have different spatial meaning and are not aliases. Orientation requires context when left/right/front are ambiguous.

**rule_category_state_value** (v19/rule/category/state-value; candidate)

STRING condition used in selection. state_warm does not command heat; “hot” is not automatically synonymous with “warm.”

**rule_category_style_value** (v19/rule/category/style-value; candidate)

STRING production style. style_narrative does not establish that described events occurred.

**rule_category_tone_value** (v19/rule/category/tone-value; rule governing tone_urgent)

STRING register. tone_urgent describes urgency, not a concrete deadline.

**rule_category_topic_value** (v19/rule/category/topic-value; rule governing topic_spider_man_2)

Named subjects remain STRING; complex compositional topics use the listed TERM constructors. A subject label does not encode the question or claim about it.

**rule_category_transformation_value** (v19/rule/category/transformation-value; candidate)

TERM-described transformation. Pass it through constraints; no ungoverned transformations attribute.

**rule_composites_general** (v19/rule/composites-general; rule governing assert_multinomial_scorer)

Composites are acyclic TERM expansion templates. $name substitutes the typed argument; fixed strings are semantic atoms. No silent defaults. Emit nested applications as separate TERM bindings; zero-argument calls are allowed only with a published decomposition. Bare legacy STRING use is deprecated. Jazz/classical piano topic labels do not express a separate genre/instrument relationship; decompose when needed. Named works/products are exact referents. Greatest-cricketer topic specifies neither a winner nor a greatness metric. Budget-limited supplies no monetary ceiling. constraint_17_plus retains its reviewed definition; use a numeric age requirement only when the source specifies age, not for an unspecified mature rating. event_* returns narrative TERM, not EVENT; char_* describes a character, not an asserted real person; chg_* describes intent; assert_* describes a test expectation, not success.

**rule_examples_general** (v19/rule/examples-general; candidate)

Examples use this glossary's contracts. They have not been verified by an implemented BrainCode parser.

**rule_operations_general** (v19/rule/operations-general; rule governing run_tests)

Operations are callable vocabulary, not arbitrary values. Signatures and categories constrain each parameter; extra attributes need a reviewed profile. Bind REQUEST results. Failure creates no successful result; TRACE records failures without fabricated runtime values. Runtime failure handling is outside this profile. No automatic custom_general_<predicate> operation exists.

**rule_supplemental_general** (v19/rule/supplemental-general; candidate)

Supplementary entries obey the same static and RECORD rules. Aliases are empty unless explicitly stated; no undeclared domain vocabulary is implied.

**rule_support_primitives_general** (v19/rule/support-primitives-general; candidate)

Pure TERM constructors assert nothing. Expansion literals are exact identifiers/atomic values, never hidden sentences. Omit unsupported optional arguments. Counts/indices are nonnegative integers; preserve.index ≥ 1; amounts are nonnegative. minimum_per_period.class uses semantic-category-value; period and temporal duration use the temporal duration-unit-value subset. activity verbs have the role-specific meanings defined in their composites; ambiguous new verbs need review and do not create executable operations.

### operations

- add_to_cart | operation | operation-vocabulary | (target: LIST[REF[STRING]]) -> void | Add the explicitly selected items. Does not pay or place an order.  ⟵ candidate
- chill | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Chill using the stated resource; same identity.  ⟵ candidate
- close | operation | operation-vocabulary | (target: REF[STRING] / TERM) -> void | Close an articulated receptacle or appliance door. target must be a closable entity. | aliases: close_receptacle, close_door  ⟵ candidate
- drop | operation | operation-vocabulary | (target: REF[STRING] / TERM) -> void | Drop or release the held target object from the agent's hand. | not: place (which requires a destination receptacle) | aliases: drop, let go, put down  ⟵ candidate
- face | operation | operation-vocabulary | (target: STRING / TERM / ATOM[object_label]) -> void | Orient agent body/camera directly toward a target entity. target must be a perceptible entity. | aliases: orient_towards  ⟵ candidate
- heat | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Heat using the stated resource; same identity. Selecting a warm object does not imply heating it.  ⟵ candidate
- hover | operation | operation-vocabulary | (target: REF[STRING]) -> void | Move pointer cursor over an interactive web element without clicking. target must resolve to a valid element reference. | aliases: mouse_over  ⟵ candidate
- pick_up | operation | operation-vocabulary | (target: STRING / ATOM[object_label] / ATOM[food_label], quantity?: NUMBER, source?: STRING / ATOM[object_label], color?: STRING / ATOM[color_label], shape?: STRING, state?: STRING) -> REF[STRING] or LIST[REF[STRING]] | Select/acquire objects. Missing quantity or literal 1 returns REF; integer literal greater than 1 returns LIST[REF]. Other values are invalid for this profile. | aliases: grab, take, retrieve  ⟵ candidate
- place | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label], location?: STRING / ATOM[object_label], relation?: STRING) -> void | Place an already acquired object. Spatial relation must be explicit if the source distinguishes it. | aliases: put, insert  ⟵ candidate
- pour | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Transfer selected liquid to the destination, preserving tracked material identity.  ⟵ candidate
- rinse | operation | operation-vocabulary | (target: REF[STRING], destination: STRING / ATOM[object_label]) -> REF[STRING] | Rinse using the stated resource; return the same identity. It is not enough that the object is already clean. | aliases: wash  ⟵ candidate
- run_tests | operation | operation-vocabulary | (target: STRING / ATOM[platform_label], assertion?: TERM) -> BOOL | Run the selected project's tests, optionally checking the specified assertion. TRUE means the declared test condition passed, not overall software correctness.  ⟵ candidate
- turn | operation | operation-vocabulary | (direction: STRING) -> void | Rotate agent body/view orientation. direction is typically left, right, or angle. | aliases: rotate, turn_around  ⟵ candidate
- walk | operation | operation-vocabulary | (destination: STRING / TERM / ATOM[object_label], relation?: STRING) -> void | Locomote towards a target destination or landmark. destination must identify a valid entity or location. | aliases: move_to, go_to, navigate_to  ⟵ related to then

### speech acts

- acknowledge | speech_act | operation-vocabulary | UTTER acknowledge(target: CLAIM / TERM) | Acknowledge receipt/awareness; does not imply agreement.  ⟵ candidate
- ask | speech_act | operation-vocabulary | UTTER ask(target: TERM, or a sufficiently precise topic: STRING / TERM) | Request information/advice; not an assertion of an answer. | aliases: ask, how should  ⟵ candidate
- confirm | speech_act | operation-vocabulary | UTTER confirm(target: CLAIM) | Confirm the proposition; its evidence/status remains explicit.  ⟵ candidate
- inform | speech_act | operation-vocabulary | UTTER inform(target: CLAIM) | Present the proposition; preserve its holder/status.  ⟵ candidate
- propose | speech_act | operation-vocabulary | UTTER propose(target: TERM) | Suggest an action/idea; does not record it as performed.  ⟵ candidate
- respond | speech_act | operation-vocabulary | UTTER respond(target: CLAIM / TERM) | Answer with structured content; not merely label the question's topic. | aliases: answer  ⟵ candidate

### constructors

- activity | constructor | TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM) -> TERM | Description of the action and its roles; instrument identifies means, purpose identifies an intended end | not: Does not execute or assert it  ⟵ candidate
- aesthetic | constructor | TERM aesthetic(period: STRING, style: STRING) -> TERM | A stylistic description with an explicit period | not: Not a character's age or production date  ⟵ candidate
- at_least | constructor | TERM at_least(measure: TERM) -> TERM | A lower bound: the constrained value is greater than or equal to the given measure (or number term). Use inside requirement(value=...). | not: an exact value; a strict 'more than' only when the source says so explicitly | aliases: at least, minimum, or more, no less than, plus  ⟵ candidate
- at_most | constructor | TERM at_most(measure: TERM) -> TERM | An upper bound: the constrained value is less than or equal to the given measure (or number term). Use inside requirement(value=...). | not: an exact value or a target to aim for | aliases: at most, maximum, up to, no more than, under  ⟵ candidate
- bionic_person | constructor | TERM bionic_person(composition?: STRING / TERM) -> TERM | Constructs a descriptive representation of a bionic person or cyborg entity with biological and mechanical components. | not: a standard human role (use role_user or role_adults) or a purely artificial device. | aliases: bionic person, bionic people, cyborg, half human half robot  ⟵ candidate
- calculation | constructor | TERM calculation(inputs: LIST[TERM], operation: STRING, result?: TERM) -> TERM | Constructs a descriptive representation of an arithmetic or algorithmic calculation step with inputs, operation identifier, and optional resulting value. | not: an executed runtime action or factual claim of outcome | aliases: math_operation, compute_step  ⟵ candidate
- character | constructor | TERM character(name: STRING, series?: STRING) -> TERM | Constructs a descriptive representation of a fictional or narrative character. name specifies the character identifier. | aliases: fictional_character  ⟵ candidate
- character_trait | constructor | TERM character_trait(property: STRING, value: STRING / NUMBER) -> TERM | A character attribute | not: Not a claim about a real person  ⟵ dependency of char_female
- decision | constructor | TERM decision(activity: TERM) -> TERM | A decision whose content is the described activity | not: Not proof it was carried out  ⟵ candidate
- exclude | constructor | TERM exclude(item: STRING / TERM) -> TERM | Require absence of that content/item | not: Not a claim of observed absence  ⟵ dependency of constraint_exclude_liberation_theme
- illuminates | constructor | TERM illuminates(target: STRING / TERM, source: STRING / TERM) -> TERM | Constructs a description of directional illumination where a light source casts light onto a target body. | not: an ambient color state or reflection (use reflects_light) | aliases: illuminates, shines on, shining towards  ⟵ candidate
- include | constructor | TERM include(item: STRING / TERM) -> TERM | Require the identified content/item | not: Not permission to invent an instance in a recorded trace  ⟵ dependency of constraint_include_character_attribute_list
- measure | constructor | TERM measure(amount: NUMBER, unit: STRING / ATOM[currency]) -> TERM | A measured amount: a number with its unit symbol (a unit-category value such as unit_minute, cap_gb or currency::USD). Describes the amount only; asserts nothing. ATOM[currency] is also accepted and supplies the pinned currency identity; no exchange rate or conversion is implicit. | not: a symbol with the number baked in (char_age_18, size_16gb); a unitless count (use the quantity argument) | aliases: amount of, size of, measured in  ⟵ candidate
- obligation | constructor | TERM obligation(actor: STRING / TERM, activity: TERM) -> TERM | Constructs a deontic obligation description requiring an actor to perform an activity. actor and activity specified. | aliases: duty, mandatory_activity  ⟵ candidate
- requirement | constructor | TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM | Specifies a required property constraint with an expected primitive or structured value. | not: Does not assert an existing artifact already satisfies it | aliases: constraint, property_requirement, structured_requirement  ⟵ dependency of constraint_realistic
- sequence | constructor | TERM sequence(items: LIST[TERM]) -> TERM | Ordered described activities/content | not: Not unordered conjunction  ⟵ candidate
- subject | constructor | TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM | Subject matter with explicit qualifiers | not: Does not make a factual claim about it  ⟵ candidate
- test_condition | constructor | TERM test_condition(condition: STRING, expected: BOOL) -> TERM | A testable condition with the expected Boolean outcome | not: Expected outcome is not an observed result  ⟵ candidate

### composites

- char_2000s_anime_style | composite | character-property-value | TERM char_2000s_anime_style() -> TERM | 2000s anime style. | = aesthetic(period="2000s", style="anime")  ⟵ candidate
- char_female | composite | character-property-value | TERM char_female() -> TERM | Female gender. | = character_trait(property="gender", value="female") | aliases: female  ⟵ candidate
- assert_multinomial_scorer | composite | code-value | TERM assert_multinomial_scorer() -> TERM | Assertion that multinomial probabilistic scoring succeeds. | = test_condition(condition="multinomial_probabilistic_scoring", expected=TRUE)  ⟵ candidate
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
- event_sadie_adler_unmasking | composite | event-value | TERM event_sadie_adler_unmasking() -> TERM | Sadie Adler taking off her hat and peeling skin. | = sequence(items=[activity(verb="remove", actor="Sadie Adler", object="hat"), activity(verb="peel", actor="Sadie Adler", object="skin")])  ⟵ candidate

### claim relations

- allowed_to_enter | claim_relation | CLAIM allowed_to_enter(subject: STRING / TERM, location: STRING / TERM, condition?: STRING / TERM) | Asserts that a subject is permitted access to a location or facility. permission claim. | aliases: permitted_in  ⟵ candidate
- attribute_claim | claim_relation | CLAIM attribute_claim(subject: STRING / TERM / ATOM[platform_label], property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) | Asserts that a subject possesses a named property evaluated to a specific primitive or structured value. general property attribution claim. | aliases: property_value, word_property, has_property, property attribution  ⟵ related to statement
- causes | claim_relation | CLAIM causes(cause: CLAIM / TERM, effect: CLAIM) | Asserts a direct causal relationship producing an effect proposition. causal assertion. | aliases: produces  ⟵ candidate
- comfortable | claim_relation | CLAIM comfortable(person: TERM, value: BOOL) | Asserts whether a person or animal is comfortable in a situation. affective/state claim. | aliases: is_comfortable  ⟵ candidate
- constrained_by | claim_relation | CLAIM constrained_by(activity: TERM, constraint: TERM) | Asserts that an activity or operation is governed or restricted by a constraint. governance/constraint claim. | aliases: restricted_by  ⟵ candidate
- distracts_from | claim_relation | CLAIM distracts_from(distraction: STRING / TERM, focus: STRING / TERM) | Asserts that focusing on a specific factor or distraction interferes with or detracts from considering or evaluating a target focus. | not: a logical contradiction or temporal pause | aliases: detracts_from, interferes_with, diverts_from  ⟵ candidate
- enables | claim_relation | CLAIM enables(condition: TERM / CLAIM, outcome: TERM / CLAIM) | Asserts that an enabling condition or capability facilitates an outcome. enabling condition. | aliases: facilitates, allows  ⟵ candidate
- exempt_from | claim_relation | CLAIM exempt_from(subject: STRING / TERM, rule: CLAIM / TERM) | Asserts that a subject is granted exemption from a designated rule or prohibition. exemption claim. | aliases: excepted_from  ⟵ candidate
- exists_in | claim_relation | CLAIM exists_in(subject: STRING / TERM, location: STRING / TERM) | Asserts that an entity, policy, or phenomenon exists within a geographical or conceptual location. spatial/locational existence. | aliases: present_in  ⟵ candidate
- failure | claim_relation | CLAIM failure(system: STRING / ATOM[platform_label]) | The indicated system is failing in context; hypothesis status does not establish truth  ⟵ candidate
- has_state | claim_relation | CLAIM has_state(subject: TERM, state: STRING) | Asserts that an entity is currently in a physical, thermal, or operational state. state must be a valid state descriptor string. | aliases: in_state, state_is  ⟵ candidate
- important | claim_relation | CLAIM important(target: TERM) | Asserts that a concept, activity, or condition is important or significant. evaluative importance claim. | aliases: significant  ⟵ candidate
- leads_to | claim_relation | CLAIM leads_to(cause: TERM, effect: TERM) | Asserts a conceptual consequence or progression from cause to effect. progression relation. | aliases: results_in  ⟵ candidate
- motivated_by | claim_relation | CLAIM motivated_by(claim: CLAIM, motive: STRING / TERM) | Asserts that an action, rule, or claim is motivated by an underlying motive or goal. motive explanation. | aliases: rationale_is  ⟵ candidate
- occurred_recently | claim_relation | CLAIM occurred_recently(target: CLAIM) | Asserts temporal recency of an asserted occurrence or claim. temporal recency qualifier. | aliases: recently_happened  ⟵ candidate
- ongoing | claim_relation | CLAIM ongoing(target: TERM) | Asserts that a conflict, process, or initiative is actively ongoing. temporal aspect claim. | aliases: in_progress  ⟵ candidate
- outcome | claim_relation | CLAIM outcome(event: EVENT, value: STRING / NUMBER / BOOL) | Recorded output of that event; BY, STATUS and SOURCE required by spec  ⟵ candidate
- possesses | claim_relation | CLAIM possesses(subject: STRING / TERM, item: TERM, value: BOOL) | Asserts whether a subject possesses or lacks a stated property, capability, or entity. possession assertion with boolean polarity. | aliases: holds_property  ⟵ candidate
- prohibited | claim_relation | CLAIM prohibited(subject: STRING / TERM, location: STRING / TERM, condition?: STRING / TERM) | Asserts that a subject is prohibited from a location or activity under specified conditions. deontic prohibition claim. | aliases: forbidden, banned_from  ⟵ candidate
- proposed_policy | claim_relation | CLAIM proposed_policy(policy: TERM, requirements: LIST[TERM]) | Asserts that a proposed policy framework comprises the specified requirement terms. policy must be a policy term. | aliases: policy_proposal  ⟵ candidate
- recommended | claim_relation | CLAIM recommended(target: TERM / CLAIM) | Asserts an advisory recommendation that an activity or measure is advisable. advisory normative claim. | aliases: advisable  ⟵ candidate
- spatial_state | claim_relation | CLAIM spatial_state(relation: STRING, object: TERM, reference: TERM) | Asserts an observed spatial configuration between an object and a reference landmark. relation must specify spatial configuration. | aliases: placed_at, located_at  ⟵ related to statement
- statement | claim_relation | CLAIM statement(fact: TERM) | Foundational claim relation converting any descriptive TERM into an attributed, truth-evaluated assertion. universal fact assertion. | aliases: assert_fact, fact_claim, claim_statement  ⟵ candidate
- unaware | claim_relation | CLAIM unaware(person: STRING / TERM, topic: STRING / TERM) | Asserts epistemic lack of awareness regarding a topic, fact, or event. epistemic state. | aliases: ignorant_of  ⟵ candidate
- validates_parameter | claim_relation | CLAIM validates_parameter(condition: STRING, entity: TERM, parameter: STRING) | Asserts that a code entity inspects or validates parameter names or types for a specified condition. | not: a runtime assertion test | aliases: inspects_parameter, checks_parameter, validates_parameter_names  ⟵ candidate
- varies_with | claim_relation | CLAIM varies_with(target: CLAIM / TERM, condition: STRING / TERM) | Asserts that a target claim or term varies contingently depending on specified conditions, external factors, or behavioral habits. | not: geographic variation only (use varies_by_location) | aliases: depends_on, contingent_on  ⟵ candidate
- works_best | claim_relation | CLAIM works_best(style: STRING, count: NUMBER, purpose: STRING) | Asserts an advisory evaluation of optimal event style and participant capacity. planning evaluation. | aliases: optimal_format  ⟵ candidate

### links

- contrast | link | LINK contrast(first: CLAIM, second: CLAIM) | Expresses rhetorical qualification, opposition, or contrast between two claims. link between claims. | aliases: qualification, however  ⟵ candidate
- rejects | link | LINK rejects(evidence: CLAIM, hypothesis: CLAIM) | Source uses the evidence to reject that hypothesis  ⟵ candidate
- revises | link | LINK revises(previous: CLAIM, replacement: CLAIM) | Explicit replacement; use with AMENDS when changing active conversation content  ⟵ candidate
- supports | link | LINK supports(conclusion: CLAIM, premise: CLAIM) | Source presents premise as a reason for conclusion; not necessarily logical entailment  ⟵ candidate
- then | link | LINK then(previous: EVENT, next: EVENT) | Represents temporal sequence and succession between two events where next follows previous. previous and next must be event terms. | aliases: followed_by, after_which  ⟵ candidate

### values

- art_character_profile | value | artifact-value | Descriptive character profile.  ⟵ candidate
- art_itinerary | value | artifact-value | An ordered travel plan; GENERATE returns STRING, not booked travel  ⟵ candidate
- art_plan | value | artifact-value | Actionable plan.  ⟵ candidate
- art_short_text | value | artifact-value | Short free text.  ⟵ candidate
- art_story | value | artifact-value | Narrative story.  ⟵ candidate
- art_structured_report | value | artifact-value | Headed/structured report.  ⟵ candidate
- art_technical_explanation | value | artifact-value | Technical explanation of a concept.  ⟵ candidate
- cap_gb | value | capacity-unit-value | One gibibyte-equivalent RAM capacity unit. | aliases: GB, gigabytes  ⟵ candidate
- path_pandas_src_testing_pyx | value | code-value | Source code file path or exported symbol in scientific Python: path_pandas_src_testing_pyx. | aliases: path_pandas_src_testing_pyx  ⟵ candidate
- path_sklearn_linear_model_logistic_py | value | code-value | The scikit-learn logistic module path.  ⟵ candidate
- sym_pandas_testing_assert_almost_equal | value | code-value | Source code file path or exported symbol in scientific Python: sym_pandas_testing_assert_almost_equal. | aliases: sym_pandas_testing_assert_almost_equal  ⟵ candidate
- constraint_17_plus | value | constraint-value | Rated 17+ or mature.  ⟵ candidate
- design_parameters | value | descriptive-value | Concept of operational and behavioral design specifications for AI systems. | aliases: design_parameters  ⟵ candidate
- dom_ovr | value | descriptive-value | One-versus-rest domain concept.  ⟵ candidate
- dom_safari | value | descriptive-value | Safari domain concept. | aliases: safari  ⟵ candidate
- potential_harms | value | descriptive-value | Concept of potential safety hazards, adverse outcomes, or risks in AI interaction. | aliases: potential_harms  ⟵ candidate
- tattoos | value | descriptive-value | Descriptive concept of tattoos in cultural and social contexts. | aliases: tattoos  ⟵ candidate
- yakuza | value | descriptive-value | Descriptive concept of yakuza in cultural and social contexts. | aliases: yakuza  ⟵ candidate
- unit_character | value | duration-unit-value | One Unicode scalar value in the final rendered artifact; line endings are normalized to LF before counting. | aliases: characters, chars  ⟵ candidate
- unit_day | value | duration-unit-value | Day. | aliases: days  ⟵ candidate
- unit_hour | value | duration-unit-value | Hour. | aliases: hours  ⟵ candidate
- unit_item | value | duration-unit-value | Top-level generated list or report item. | aliases: items, entries  ⟵ candidate
- unit_paragraph | value | duration-unit-value | Paragraph of text. | aliases: paragraphs, paragraph  ⟵ candidate
- unit_second | value | duration-unit-value | Second. | aliases: seconds, sec  ⟵ candidate
- unit_sentence | value | duration-unit-value | One grammatical sentence in text generation or constraint counting. | not: unit_paragraph (paragraph block) or unit_word (individual word) | aliases: sentence, sentences  ⟵ candidate
- unit_year | value | duration-unit-value | Year. | aliases: years  ⟵ candidate
- alcohol | value | entity-name | Alcoholic spirit or liquid such as brandy, rum, or whisky. | not: fermented non-distilled wine or pure chemical formula notation | aliases: alcohol, spirits, liquor  ⟵ candidate
- bed | value | entity-name | A bed furniture surface or sleeping area. | aliases: bed  ⟵ candidate
- bowl | value | entity-name | A container/dish used for holding food or small items. | aliases: bowl  ⟵ candidate
- bowtie | value | entity-name | Item or prop in joke/creative context: bowtie. | aliases: bowtie  ⟵ candidate
- bread | value | entity-name | A bread loaf or slice food object. | aliases: bread  ⟵ candidate
- caddy | value | entity-name | A portable storage caddy, organizer box, or supply tote for carrying and organizing handheld tools and supplies. | not: cabinet (a stationary furniture cupboard) or safe (a secure metal lockbox) | aliases: caddy, supply caddy, wrapping caddy, tool caddy, organizer caddy, supply tote  ⟵ candidate
- candle | value | entity-name | A candle light source made of wax with a wick. | not: lamp (an electric light appliance or fixture) | aliases: candle, wax candle  ⟵ candidate
- cardamom | value | entity-name | Aromatic spice seeds or pods from Elettaria or Amomum used in cooking and baking. | not: cinnamon, ginger, or other distinct spice varieties | aliases: cardamom, ground cardamom, cardamom pods  ⟵ candidate
- cardboard_box | value | entity-name | A cardboard box, carton, or general storage box container. | not: tissue_box (specifically a box of paper tissues) or safe (a lockable metal container) | aliases: cardboard box, box, carton, storage box  ⟵ candidate
- cd | value | entity-name | A compact disc physical object. | not: a digital media file or streaming track | aliases: CD, compact_disc  ⟵ candidate
- chair | value | entity-name | A chair furniture seat with a backrest. | not: object_label::armchair (specifically an object_label::armchair with side armrests) or object_label::sofa | aliases: chair, seat  ⟵ candidate
- cheese | value | entity-name | Dairy food item: cheese. | not: meat or non-dairy food items | aliases: cheese  ⟵ candidate
- citric_acid | value | entity-name | Food and beverage acid additive. | not: tartaric_acid or pure chemical formula notation | aliases: citric acid  ⟵ candidate
- clock | value | entity-name | A clock timepiece appliance. | not: duration units like unit_hour | aliases: clock, timer  ⟵ candidate
- cloves | value | entity-name | Aromatic dried flower buds of Syzygium aromaticum used as a culinary spice. | not: cinnamon, nutmeg, or other distinct spice varieties | aliases: cloves, clove, ground cloves, whole cloves  ⟵ candidate
- coffee_maker | value | entity-name | A coffee-making appliance; not automatically a heating resource  ⟵ candidate
- credit_card | value | entity-name | A physical plastic credit, debit, or payment card object. | not: egift_card (an electronic gift card or digital voucher) | aliases: credit card, card, payment card  ⟵ candidate
- desk | value | entity-name | A work desk furniture surface. | aliases: desk  ⟵ candidate
- dog | value | entity-name | Animal entity: dog. | not: animal_label::cat or animal_label::donkey | aliases: dog, dogs, canine, pup, puppy  ⟵ candidate
- door | value | entity-name | A door architectural barrier or entryway. | not: wall or close/open operations | aliases: door, doorway, room door  ⟵ candidate
- dulce_de_nata | value | entity-name | Clotted cream milk confection or dessert item: dulce de nata. | not: dulce_de_leche or cheese | aliases: dulce de nata, dulce_de_nata  ⟵ candidate
- earth | value | entity-name | The planet Earth as an astronomical celestial body. | not: soil, ground surface, or electrical grounding | aliases: earth, the earth, planet earth, Earth  ⟵ candidate
- entity_cake | value | entity-name | Event planning item or menu category: entity_cake. | aliases: entity_cake  ⟵ candidate
- entity_desserts | value | entity-name | Event planning item or menu category: entity_desserts. | aliases: entity_desserts  ⟵ candidate
- entity_flowers | value | entity-name | Flowers, blossoms, or floral design elements. | not: constraint_exclude_flowery_language (a prose style constraint) or agricultural food items | aliases: flowers, floral, flower, floral decorations  ⟵ candidate
- entity_order_vs_assemble_plan | value | entity-name | Event planning item or menu category: entity_order_vs_assemble_plan. | aliases: entity_order_vs_assemble_plan  ⟵ candidate
- figurine | value | entity-name | A small carved, molded, or sculpted decorative statuette object. | not: character (a fictional persona) or captioned_figure (a document figure/photo) | aliases: figurine, statuette, statue, small statue, sculptural figure, miniature figure  ⟵ candidate
- fridge | value | entity-name | A refrigerator cooling appliance. | aliases: fridge  ⟵ candidate
- knife | value | entity-name | A cutting utensil used for slicing or food preparation. | aliases: knife  ⟵ candidate
- lamp | value | entity-name | A lamp light source appliance. | not: an abstract lighting concept or ambient color | aliases: light, desk_lamp  ⟵ candidate
- laptop | value | entity-name | A portable laptop computer physical object. | not: topic_macbook_pro_2017 (a generation topic label) | aliases: laptop, laptop computer, notebook  ⟵ candidate
- maqluba | value | entity-name | Traditional Arab layered rice dish: maqluba. | not: cuisine_mediterranean (cuisine style rather than specific dish) | aliases: maqluba, makloubeh  ⟵ candidate
- mattress | value | entity-name | A mattress cushion or sleeping surface object. | not: bed (a bed furniture surface or frame) or object_label::pillow | aliases: mattress, mattresses  ⟵ candidate
- meat | value | entity-name | Food item: meat or beef. | not: animal_label::tuna or animal_label::fish (specific aquatic foods) | aliases: meat, beef  ⟵ candidate
- moon | value | entity-name | Earth's natural celestial satellite. | not: an artificial satellite or other planetary moon | aliases: moon, the moon, Luna  ⟵ candidate
- mug | value | entity-name | Drinking cup. | aliases: mug  ⟵ candidate
- nutmeg | value | entity-name | Ground or whole nutmeg culinary spice from Myristica fragrans seed. | not: cinnamon, cloves, or other distinct spice varieties | aliases: nutmeg, ground nutmeg  ⟵ candidate
- oak_chips | value | entity-name | Oak wood pieces or barrels used for wine aging and flavor extraction. | not: grape_tannin or structural chemical additives | aliases: oak chips, oak pieces, oak barrels  ⟵ candidate
- pan | value | entity-name | A metal cooking vessel, frying pan, skillet, saucepan, or pot cookware item used for preparing, heating, or holding food. | not: bowl (deep concave vessel) or plate (shallow flat dining dish) | aliases: pan, frying pan, skillet, saucepan, pot  ⟵ candidate
- pen | value | entity-name | A writing instrument. | aliases: pen  ⟵ candidate
- pencil | value | entity-name | A pencil writing instrument. | aliases: pencil  ⟵ candidate
- piano | value | entity-name | A piano musical instrument or large furniture object. | not: topic_classical_piano or topic_jazz_piano (music genre topics) | aliases: piano, grand piano, upright piano, keyboard  ⟵ candidate
- resource_chiller | value | entity-name | Canonical abstract chilling resource when no particular appliance is named.  ⟵ candidate
- resource_heater | value | entity-name | Canonical abstract heating resource when no particular appliance is named.  ⟵ candidate
- resource_sink | value | entity-name | Canonical abstract washing resource when no particular sink is named.  ⟵ candidate
- safe | value | entity-name | A secure, lockable metal storage container or receptacle for holding valuables. | not: cabinet (a general storage cupboard) or dresser (a chest of drawers) | aliases: safe, strongbox, lockbox, deposit box  ⟵ candidate
- shower | value | entity-name | A bathroom shower fixture or stall used for bathing. | not: sink (a washing basin) or toilet (a toilet fixture) | aliases: shower, shower stall  ⟵ candidate
- song | value | entity-name | A musical piece, audio track, or song entity. | not: piano (a musical instrument) or cd (a physical compact disc storage medium) | aliases: song, music track, audio track, track  ⟵ candidate
- spatula | value | entity-name | A kitchen utensil with a broad, flat, and flexible blade used for lifting, flipping, or spreading food. | not: knife (cutting utensil) or spoon (scooping utensil) | aliases: spatula, turner, flipper  ⟵ candidate
- sponge | value | entity-name | A porous, absorbent sponge cleaning tool or object. | not: tissue_box (a paper tissue box) or other wiping materials | aliases: sponge, cleaning sponge  ⟵ candidate
- sultana | value | entity-name | Dried white seedless grape food product. | not: raisin (dark dried grape) or wine_grape | aliases: sultana, sultanas, golden raisin  ⟵ candidate
- sun | value | entity-name | The central star of the Solar System. | not: an artificial lighting appliance or sunlight | aliases: sun, the sun, Sol  ⟵ candidate
- tartaric_acid | value | entity-name | Winemaking acid additive used for acidity adjustment. | not: citric_acid or general organic chemicals | aliases: tartaric acid  ⟵ candidate
- textbook | value | entity-name | A textbook or instructional book used as an educational resource. | not: style_academic (which is a stylistic mode) or art_short_text (which is a brief generated text artifact) | aliases: textbook, book, coursebook, textbooks  ⟵ candidate
- trash_can | value | entity-name | A waste receptacle container. | aliases: trash_can  ⟵ candidate
- watch | value | entity-name | A watch or wristwatch timepiece object. | not: clock (a stationary timepiece appliance) or duration units like unit_hour | aliases: watch, wristwatch, wrist watch  ⟵ candidate
- waterproof_stickers | value | entity-name | Physical item used for concealment or covering: waterproof_stickers. | aliases: waterproof_stickers  ⟵ candidate
- format_bullet_list | value | format-value | Bulleted list. | aliases: bullet points  ⟵ candidate
- locale_en_us | value | locale-value | US English. | aliases: english, en-us  ⟵ candidate
- locale_fr | value | locale-value | French. | aliases: french  ⟵ candidate
- locale_hi_en | value | locale-value | Hinglish (Hindi-English mix). | aliases: hinglish  ⟵ candidate
- africa | value | location-name | Geopolitical nation or continental region: africa. | aliases: africa  ⟵ candidate
- eastern_cape | value | location-name | Eastern Cape region.  ⟵ candidate
- floor | value | location-name | The floor surface of an indoor room or architectural space. | not: wall (a vertical room boundary surface) or counter (a countertop surface) | aliases: floor, ground  ⟵ candidate
- island | value | location-name | A freestanding kitchen island counter or food preparation work surface. | not: counter (a perimeter countertop surface) or table (a dining or general furniture surface) | aliases: island, kitchen island, kitchen_island  ⟵ candidate
- living_room | value | location-name | A residential room or general indoor living area. | not: floor (a floor surface) or wall (a vertical boundary surface) | aliases: living room, living_room, sitting room, lounge  ⟵ candidate
- new_york_university | value | location-name | New York University institution or campus grounds. | aliases: nyu  ⟵ candidate
- night_stand | value | location-name | A small bedside table or nightstand furniture surface. | not: a chest of drawers (use dresser) or a general table surface (use table) | aliases: nightstand, bedside table  ⟵ candidate
- ryokan | value | location-name | Traditional Japanese establishment or hospitality venue: ryokan. | aliases: ryokan  ⟵ candidate
- wall | value | location-name | A room boundary wall surface. | aliases: wall  ⟵ candidate
- metric_order_late | value | metric-value | Whether an order is late. | aliases: order is late, delayed  ⟵ candidate
- metric_response_time | value | metric-value | Support response time. | aliases: response time  ⟵ candidate
- material_memory_foam | value | product-attribute-value | Memory foam viscoelastic polyurethane material qualifier. | not: sponge (a porous cleaning tool) or generic bedding | aliases: memory foam, memory_foam, viscoelastic foam  ⟵ candidate
- size_large | value | product-attribute-value | Large size. | aliases: large, L  ⟵ candidate
- size_medium | value | product-attribute-value | Medium size. | aliases: medium, M  ⟵ candidate
- size_queen | value | product-attribute-value | Queen-size dimension classification for beds, mattresses, and bedding. | not: size_large (generic large apparel/goods size) or size_king | aliases: queen, queen size, Queen  ⟵ candidate
- size_small | value | product-attribute-value | Small size. | aliases: small, S  ⟵ candidate
- size_tall | value | product-attribute-value | Tall relative vertical dimension qualifier. | aliases: size_tall  ⟵ candidate
- valet | value | product-attribute-value | Valet parking or dedicated vehicle attendant service. | aliases: valet_parking  ⟵ candidate
- role_agent | value | recipient-value | The assistant. | aliases: you, the assistant  ⟵ candidate
- role_colleague | value | recipient-value | A coworker of the user. | aliases: my colleague, coworker  ⟵ candidate
- role_friend | value | recipient-value | A friend of the user. | aliases: my friend  ⟵ candidate
- role_manager | value | recipient-value | The user's manager. | aliases: my manager, boss  ⟵ candidate
- role_professor | value | recipient-value | The user's professor/instructor. | aliases: my professor, teacher  ⟵ candidate
- tattooed_guests | value | recipient-value | Social, demographic, or institutional group: tattooed_guests. | aliases: tattooed_guests  ⟵ candidate
- avail_in_stock | value | search-value | Available for purchase now. | aliases: available  ⟵ candidate
- avail_out_of_stock | value | search-value | Unavailable for purchase now. | aliases: sold out  ⟵ candidate
- cat_game | value | search-value | Category: video game.  ⟵ candidate
- cat_limited_time_offers | value | search-value | Category: time-limited deals.  ⟵ candidate
- rank_distance | value | search-value | Rank field: proximity. | aliases: nearest, closest  ⟵ candidate
- rank_price | value | search-value | Rank or filter field: monetary cost. | aliases: cheapest, lowest price  ⟵ candidate
- class_beach | value | semantic-category-value | The abstract class or category of beach destinations and coastal environments. | not: island (kitchen island work surface) or a specific named beach location | aliases: beach, beaches, beach destination, seaside  ⟵ candidate
- class_temple | value | semantic-category-value | The abstract class of temples. | aliases: temple, temples  ⟵ candidate
- shape_oval | value | shape-value | Oval. | aliases: oval  ⟵ candidate
- shape_triangular | value | shape-value | Triangular. | aliases: triangular, triangle  ⟵ candidate
- behind | value | spatial-relation | Positioned behind.  ⟵ candidate
- in_front_of | value | spatial-relation | Positioned in front of. | aliases: in front of  ⟵ candidate
- left_of | value | spatial-relation | To the left of. | aliases: left of  ⟵ candidate
- next_to | value | spatial-relation | Adjacent to. | aliases: beside  ⟵ candidate
- on | value | spatial-relation | Resting atop. | aliases: on top of  ⟵ candidate
- right_of | value | spatial-relation | To the right of. | aliases: right of  ⟵ candidate
- under | value | spatial-relation | Beneath. | aliases: below  ⟵ candidate
- state_dirty | value | state-value | Dirty condition. | aliases: dirty  ⟵ candidate
- state_empty | value | state-value | Contains no intended material or usable remaining amount. | aliases: empty, used up  ⟵ candidate
- state_full | value | state-value | Contains its intended material or remaining usable amount. | aliases: full, filled  ⟵ candidate
- style_catchy | value | style-value | Catchy, attention-grabbing style. | aliases: catchy  ⟵ candidate
- style_narrative | value | style-value | Story-like narrative style. | aliases: narrative, story-style  ⟵ candidate
- nighttime | value | time-of-day-value | The period of darkness between sunset and sunrise in the diurnal cycle. | not: night_stand (a piece of furniture) or clock time timestamps | aliases: nighttime, night, night time, darkness  ⟵ candidate
- tone_empathetic | value | tone-value | Conveys empathy/understanding. | aliases: sympathetically  ⟵ candidate
- tone_urgent | value | tone-value | Conveys urgency. | aliases: urgently, ASAP  ⟵ candidate
- topic_baldurs_gate_3 | value | topic-value | Baldur's Gate 3.  ⟵ candidate
- topic_classical_piano | value | topic-value | Classical piano.  ⟵ candidate
- topic_jazz_piano | value | topic-value | Jazz piano.  ⟵ candidate
- topic_spider_man_2 | value | topic-value | Marvel's Spider-Man 2.  ⟵ candidate
- unit_liter | value | unit-value | Standard metric measurement unit of liquid volume equal to 1 cubic decimeter (1,000 milliliters). | not: digital capacity units (like cap_gb) or temporal duration units | aliases: l, liter, liters, litres  ⟵ candidate

### attributes

- target | attribute | attribute-name | The acted-on entity or generated artifact.  ⟵ candidate

### examples

- example_a_select_two_pillows_and_move_those_objects (candidate): Select two pillows and move those objects

```braincode
MODE REQUEST
ENTRYPOINT ObjectLabelPillow
TASK ObjectLabelPillow {
  ACTION pick_up(target=object_label::pillow, quantity=2, source=object_label::sofa) -> object_label_pillow_refs : LIST[REF[STRING]]
  FOR EACH item IN object_label_pillow_refs {
    ACTION place(target=item, destination=object_label::armchair, relation=on)
  }
}
```

- example_d_record_an_actual_test_outcome_without_asserting_overall_correctness (candidate): Record an actual test outcome without asserting overall correctness

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=AGENT {
    RECORD ACTION run_tests(target=platform_label::scikit_learn) STATUS succeeded SOURCE "t1:tests" -> run_tests_event : EVENT
    CLAIM outcome(event=run_tests_event, value=TRUE) BY role_agent STATUS observed SOURCE "t1:tests" -> outcome_2 : CLAIM
  }
}
```

