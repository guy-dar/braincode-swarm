```braincode
MODE REQUEST
ENTRYPOINT MachineShortCircuit
TASK MachineShortCircuit {
  ACTION short_circuit(wire1: color_label::black, wire2: color_label::red, battery: battery, time: unit_second) -> short_circuit_event : EVENT
  ACTION touch(wire: color_label::black, battery: battery) -> touch_event : EVENT
  ACTION touch(wire: color_label::red, battery: battery) -> touch_event : EVENT
  ACTION causes(target: short_circuit_event, cause: touch_event) -> causes_event : CLAIM
  ACTION enables(condition: touch_event, outcome: short_circuit_event) -> enables_event : CLAIM
  ACTION failure(system: machine) -> failure_event : EVENT
  ACTION occurred(activity: short_circuit_event) -> occurred_event : CLAIM
  ACTION occurred_recently(target: occurred_event) -> occurred_recently_event : CLAIM
  ACTION occurred_recently(target: short_circuit_event) -> occurred_recently_event : CLAIM
  ACTION ongoing(target: short_circuit_event) -> ongoing_event : CLAIM
  ACTION outcome(event: short_circuit_event, value: short_circuit_event) -> outcome_event : CLAIM
  ACTION prep_time(value: unit_second) -> prep_time_event : CLAIM
  ACTION rank_rating(target: short_circuit_event) -> rank_rating_event : CLAIM
  ACTION next_to(target: short_circuit_event) -> next_to_event : CLAIM
  ACTION other_side_of(target: short_circuit_event) -> other_side_of_event : CLAIM
  ACTION state_dirty(condition: short_circuit_event) -> state_dirty_event : CLAIM
  ACTION style_persuasive(target: short_circuit_event) -> style_persuasive_event : CLAIM
  ACTION tone_neutral(target: short_circuit_event) -> tone_neutral_event : CLAIM
  ACTION topic_baldurs_gate_3(target: short_circuit_event) -> topic_baldurs_gate_3_event : CLAIM
  ACTION topic_pickup_lines(target: short_circuit_event) -> topic_pickup_lines_event : CLAIM
  ACTION topic_politics(target: short_circuit_event) -> topic_politics_event : CLAIM
  ACTION unit_percent(target: short_circuit_event) -> unit_percent_event : CLAIM
  ACTION unit_sentence(target: short_circuit_event) -> unit_sentence_event : CLAIM
  ACTION unit_second(target: short_circuit_event) -> unit_second_event : CLAIM
  ACTION constraint_budget_limited() -> constraint_budget_limited_event : CLAIM
  ACTION constraint_comprehensive() -> constraint_comprehensive_event : CLAIM
  ACTION constraint_exclude_flowery_language() -> constraint_exclude_flowery_language_event : CLAIM
  ACTION constraint_exclude_liberation_theme() -> constraint_exclude_liberation_theme_event : CLAIM
  ACTION constraint_include_character_attribute_list() -> constraint_include_character_attribute_list_event : CLAIM
  ACTION constraint_realistic() -> constraint_realistic_event : CLAIM
  ACTION constraint_respectful() -> constraint_respectful_event : CLAIM
  ACTION constraint_single_choice() -> constraint_single_choice_event : CLAIM
  ACTION ask(target: short_circuit_event) -> ask_event : CLAIM
  ACTION confirm(target: short_circuit_event) -> confirm_event : CLAIM
  ACTION decline(target: short_circuit_event) -> decline_event : CLAIM
  ACTION inform(target: short_circuit_event) -> inform_event : CLAIM
  ACTION propose(target: short_circuit_event) -> propose_event : CLAIM
  ACTION respond(target: short_circuit_event) -> respond_event : CLAIM
  ACTION causes(target: short_circuit_event, cause: touch_event) -> causes_event : CLAIM
  ACTION enables(condition: touch_event, outcome: short_circuit_event) -> enables_event : CLAIM
  ACTION motivates_by(target: short_circuit_event, motive: touch_event) -> motivates_by_event : CLAIM
  ACTION occurred(target: short_circuit_event) -> occurred_event : CLAIM
  ACTION occurred_recently(target: short_circuit_event) -> occurred_recently_event : CLAIM
  ACTION ongoing(target: short_circuit_event) -> ongoing_event : CLAIM
  ACTION outcome(target: short_circuit_event, value: short_circuit_event) -> outcome_event : CLAIM
  ACTION prep_time(target: short_circuit_event) -> prep_time_event : CLAIM
  ACTION rank_rating(target: short_circuit_event) -> rank_rating_event : CLAIM
  ACTION next_to(target: short_circuit_event) -> next_to_event : CLAIM
  ACTION other_side_of(target: short_circuit_event) -> other_side_of_event : CLAIM
  ACTION state_dirty(condition: short_circuit_event) -> state_dirty_event : CLAIM
  ACTION style_persuasive(target: short_circuit_event) -> style_persuasive_event : CLAIM
  ACTION tone_neutral(target: short_circuit_event) -> tone_neutral_event : CLAIM
  ACTION topic_baldurs_gate_3(target: short_circuit_event) -> topic_baldurs_gate_3_event : CLAIM
  ACTION topic_pickup_lines(target: short_circuit_event) -> topic_pickup_lines_event : CLAIM
  ACTION topic_politics(target: short_circuit_event) -> topic_politics_event : CLAIM
  ACTION unit_percent(target: short_circuit_event) -> unit_percent_event : CLAIM
  ACTION unit_sentence(target: short_circuit_event) -> unit_sentence_event : CLAIM
  ACTION unit_second(target: short_circuit_event) -> unit_second_event : CLAIM
  ACTION constraint_budget_limited() -> constraint_budget_limited_event : CLAIM
  ACTION constraint_comprehensive() -> constraint_comprehensive_event : CLAIM
  ACTION constraint_exclude_flowery_language() -> constraint_exclude_flowery_language_event : CLAIM
  ACTION constraint_exclude_liberation_theme() -> constraint_exclude_liberation_theme_event : CLAIM
  ACTION constraint_include_character_attribute_list() -> constraint_include_character_attribute_list_event : CLAIM
  ACTION constraint_realistic() -> constraint_realistic_event : CLAIM
  ACTION constraint_respectful() -> constraint_respectful_event : CLAIM
  ACTION constraint_single_choice() -> constraint_single_choice_event : CLAIM
  ACTION ask(target: short_circuit_event) -> ask_event : CLAIM
  ACTION confirm(target: short_circuit_event) -> confirm_event : CLAIM
  ACTION decline(target: short_circuit_event) -> decline_event : CLAIM
  ACTION inform(target: short_circuit_event) -> inform_event : CLAIM
  ACTION propose(target: short_circuit_event) -> propose_event : CLAIM
  ACTION respond(target: short_circuit_event) -> respond_event : CLAIM
  ACTION causes(target: short_circuit_event, cause: touch_event) -> causes_event : CLAIM
  ACTION enables(condition: touch_event, outcome: short_circuit_event) -> enables_event : CLAIM
  ACTION motivates_by(target: short_circuit_event, motive: touch_event) -> motivates_by_event : CLAIM
  ACTION occurred(target: short_circuit_event) -> occurred_event : CLAIM
  ACTION occurred_recently(target: short_circuit_event) -> occurred_recently_event : CLAIM
  ACTION ongoing(target: short_circuit_event) -> ongoing_event : CLAIM
  ACTION outcome(target: short_circuit_event, value: short_circuit_event) -> outcome_event : CLAIM
  ACTION prep_time(target: short_circuit_event) -> prep_time_event : CLAIM
  ACTION rank_rating(target: short_circuit_event) -> rank_rating_event : CLAIM
  ACTION next_to(target: short_circuit_event) -> next_to_event : CLAIM
  ACTION other_side_of(target: short_circuit_event) -> other_side_of_event : CLAIM
  ACTION state_dirty(condition: short_circuit_event) -> state_dirty_event : CLAIM
  ACTION style_persuasive(target: short_circuit_event) -> style_persuasive_event : CLAIM
  ACTION tone_neutral(target: short_circuit_event) -> tone_neutral_event : CLAIM
  ACTION topic_baldurs_gate_3(target: short_circuit_event) -> topic_baldurs_gate_3_event : CLAIM
  ACTION topic_pickup_lines(target: short_circuit_event) -> topic_pickup_lines_event : CLAIM
  ACTION topic_politics(target: short_circuit_event) -> topic_politics_event : CLAIM
  ACTION unit_percent(target: short_circuit_event) -> unit_percent_event : CLAIM
  ACTION unit_sentence(target: short_circuit_event) -> unit_sentence_event : CLAIM
  ACTION unit_second(target: short_circuit_event) -> unit_second_event : CLAIM
  ACTION constraint_budget_limited() -> constraint_budget_limited_event : CLAIM
  ACTION constraint_comprehensive() -> constraint_comprehensive_event : CLAIM
  ACTION constraint_exclude_flowery_language() -> constraint_exclude_flowery_language_event : CLAIM
  ACTION constraint_exclude_liberation_theme() -> constraint_exclude_liberation_theme_event : CLAIM
  ACTION constraint_include_character_attribute_list() -> constraint_include_character_attribute_list_event : CLAIM
  ACTION constraint_realistic() -> constraint_realistic_event : CLAIM
  ACTION constraint_respectful() -> constraint_respectful_event : CLAIM
  ACTION constraint_single_choice() -> constraint_single_choice_event : CLAIM
  ACTION ask(target: short_circuit_event) -> ask_event : CLAIM
  ACTION confirm(target: short_circuit_event) -> confirm_event : CLAIM
  ACTION decline(target: short_circuit_event) -> decline_event : CLAIM
  ACTION inform(target: short_circuit_event) -> inform_event : CLAIM
  ACTION propose(target: short_circuit_event) -> propose_event : CLAIM
  ACTION respond(target: short_circuit_event) -> respond_event : CLAIM
  ACTION causes(target: short_circuit_event, cause: touch_event) -> causes_event : CLAIM
  ACTION enables(condition: touch_event, outcome: short_circuit_event) -> enables_event : CLAIM
  ACTION motivates_by(target: short_circuit_event, motive: touch_event) -> motivates_by_event : CLAIM
  ACTION occurred(target: short_circuit_event) -> occurred_event : CLAIM
  ACTION occurred_recently(target: short_circuit_event) -> occurred_recently_event : CLAIM
  ACTION ongoing(target: short_circuit_event) -> ongoing_event : CLAIM
  ACTION outcome(target: short_circuit_event, value: short_circuit_event) -> outcome_event : CLAIM
  ACTION prep_time(target: short_circuit_event) -> prep_time_event : CLAIM
  ACTION rank_rating(target: short_circuit_event) -> rank_rating_event : CLAIM
  ACTION next_to(target: short_circuit_event) -> next_to_event : CLAIM
  ACTION other_side_of(target: short_circuit_event) -> other_side_of_event : CLAIM
  ACTION state_dirty(condition: short_circuit_event) -> state_dirty_event : CLAIM
  ACTION style_persuasive(target: short_circuit_event) -> style_persuasive_event : CLAIM
  ACTION tone_neutral(target: short_circuit_event) -> tone_neutral_event : CLAIM
  ACTION topic_baldurs_gate_3(target: short_circuit_event) -> topic_baldurs_gate_3_event : CLAIM
  ACTION topic_pickup_lines(target: short_circuit_event) -> topic_pickup_lines_event : CLAIM
  ACTION topic_politics(target: short_circuit_event) -> topic_politics_event : CLAIM
  ACTION unit_percent(target: short_circuit_event) -> unit_percent_event : CLAIM
  ACTION unit_sentence(target: short_circuit_event) -> unit_sentence_event : CLAIM
  ACTION unit_second(target: short_circuit_event) -> unit_second_event : CLAIM
  ACTION constraint_budget_limited() -> constraint_budget_limited_event : CLAIM
  ACTION constraint_comprehensive() -> constraint_comprehensive_event : CLAIM
  ACTION constraint_exclude_flowery_language() -> constraint_exclude_flowery_language_event : CLAIM
  ACTION constraint_exclude_liberation_theme() -> constraint_exclude_liberation_theme_event : CLAIM
  ACTION constraint_include_character_attribute_list() -> constraint_include_character_attribute_list_event : CLAIM
  ACTION constraint_realistic() -> constraint_realistic_event : CLAIM
  ACTION constraint_respectful() -> constraint_respectful_event : CLAIM
  ACTION constraint_single_choice() -> constraint_single_choice_event : CLAIM
  ACTION ask(target: short_circuit_event) -> ask_event : CLAIM
  ACTION confirm(target: short_circuit_event) -> confirm_event : CLAIM
  ACTION decline(target: short_circuit_event) -> decline_event : CLAIM
  ACTION inform(target: short_circuit_event) -> inform_event : CLAIM
  ACTION propose(target: short_circuit_event) -> propose_event : CLAIM
  ACTION respond(target: short_circuit_event) -> respond_event : CLAIM
  ACTION causes(target: short_circuit_event, cause: touch_event) -> causes_event : CLAIM
  ACTION enables(condition: touch_event, outcome: short_circuit_event) -> enables_event : CLAIM
  ACTION motivates_by(target: short_circuit_event, motive: touch_event) -> motivates_by_event : CLAIM
  ACTION occurred(target: short_circuit_event) -> occurred_event : CLAIM
  ACTION occurred_recently(target: short_circuit_event) -> occurred_recently_event : CLAIM
  ACTION ongoing(target: short_circuit_event) -> ongoing_event : CLAIM
  ACTION outcome(target: short_circuit_event, value: short_circuit_event) -> outcome_event : CLAIM
  ACTION prep_time(target: short_circuit_event) -> prep_time_event : CLAIM
  ACTION rank_rating(target: short_circuit_event) -> rank_rating_event : CLAIM
  ACTION next_to(target: short_circuit_event) -> next_to_event : CLAIM
  ACTION other_side_of(target: short_circuit_event) -> other_side_of_event : CLAIM
  ACTION state_dirty(condition: short_circuit_event) -> state_dirty_event : CLAIM
  ACTION style_persuasive(target: short_circuit_event) -> style_persuasive_event : CLAIM
  ACTION tone_neutral(target: short_circuit_event) -> tone_neutral_event : CLAIM
  ACTION topic_baldurs_gate_3(target: short_circuit_event) -> topic_baldurs_gate_3_event : CLAIM
  ACTION topic_pickup_lines(target: short_circuit_event) -> topic_pickup_lines_event : CLAIM
  ACTION topic_politics(target: short_circuit_event) -> topic_politics_event : CLAIM
  ACTION unit_percent(target: short_circuit_event) -> unit_percent_event : CLAIM
  ACTION unit_sentence(target: short_circuit_event) -> unit_sentence_event : CLAIM
  ACTION unit_second(target: short_circuit_event) -> unit_second_event : CLAIM
  ACTION constraint_budget_limited() -> constraint_budget_limited_event : CLAIM
  ACTION constraint_comprehensive() -> constraint_comprehensive_event : CLAIM
  ACTION constraint_exclude_flowery_language() -> constraint_exclude_flowery_language_event : CLAIM
  ACTION constraint_exclude_liberation_theme() -> constraint_exclude_liberation_theme_event : CLAIM
  ACTION constraint_include_character_attribute_list() -> constraint_include_character_attribute_list_event : CLAIM
  ACTION constraint_realistic() -> constraint_realistic_event : CLAIM
  ACTION constraint_respectful() -> constraint_respectful_event : CLAIM
  ACTION constraint_single_choice() -> constraint_single_choice_event : CLAIM
  ACTION ask(target: short_circuit_event) -> ask_event : CLAIM
  ACTION confirm(target: short_circuit_event) -> confirm_event : CLAIM
  ACTION decline(target: short_circuit_event) -> decline_event : CLAIM
  ACTION inform(target: short_circuit_event) -> inform_event : CLAIM
  ACTION propose(target: short_circuit_event) -> propose_event : CLAIM
  ACTION respond(target: short_circuit_event) -> respond_event : CLAIM
  ACTION causes(target: short_circuit_event, cause: touch_event) -> causes_event : CLAIM
  ACTION enables(condition: touch_event, outcome: short_circuit_event) -> enables_event : CLAIM
  ACTION motivates_by(target: short_circuit_event, motive: touch_event) -> motivates_by_event : CLAIM
  ACTION occurred(target: short_circuit_event) -> occurred_event : CLAIM
  ACTION occurred_recently(target: short_circuit_event) -> occurred_recently_event : CLAIM
  ACTION ongoing(target: short_circuit_event) -> ongoing_event : CLAIM
  ACTION outcome(target: short_circuit_event, value: short_circuit_event) -> outcome_event : CLAIM
  ACTION prep_time(target: short_circuit_event) -> prep_time_event : CLAIM
  ACTION rank_rating(target: short_circuit_event) -> rank_rating_event : CLAIM
  ACTION next_to(target: short_circuit_event) -> next_to_event : CLAIM
  ACTION other_side_of(target: short_circuit_event) -> other_side_of_event : CLAIM
  ACTION state_dirty(condition: short_circuit_event) -> state_dirty_event : CLAIM
  ACTION style_persuasive(target: short_circuit_event) -> style_persuasive_event : CLAIM
  ACTION tone_neutral(target: short_circuit_event) -> tone_neutral_event : CLAIM
  ACTION topic_baldurs_gate_3(target: short_circuit_event) -> topic_baldurs_gate_3_event : CLAIM
  ACTION topic_pickup_lines(target: short_circuit_event) -> topic_pickup_lines_event : CLAIM
  ACTION topic_politics(target: short_circuit_event) -> topic_politics_event : CLAIM
  ACTION unit_percent(target: short_circuit_event) -> unit_percent_event : CLAIM
  ACTION unit_sentence(target: short_circuit_event) -> unit_sentence_event : CLAIM
  ACTION unit_second(target: short_circuit_event) -> unit_second_event : CLAIM
  ACTION constraint_budget_limited() -> constraint_budget_limited_event : CLAIM
  ACTION constraint_comprehensive() -> constraint_comprehensive_event : CLAIM
  ACTION constraint_exclude_flowery_language() -> constraint_exclude_flowery_language_event : CLAIM
  ACTION constraint_exclude_liberation_theme() -> constraint_exclude_liberation_theme_event : CLAIM
  ACTION constraint_include_character_attribute_list() -> constraint_include_character_attribute_list_event : CLAIM
  ACTION constraint_realistic() -> constraint_realistic_event : CLAIM
  ACTION constraint_respectful() -> constraint_respectful_event : CLAIM
  ACTION constraint_single_choice() -> constraint_single_choice_event : CLAIM
  ACTION ask(target: short_circuit_event) -> ask_event : CLAIM
  ACTION confirm(target: short_circuit_event) -> confirm_event : CLAIM
  ACTION decline(target: short_circuit_event) -> decline_event : CLAIM
  ACTION inform(target: short_circuit_event) -> inform_event : CLAIM
  ACTION propose(target: short_circuit_event) -> propose_event : CLAIM
  ACTION respond(target: short_circuit_event) -> respond_event : CLAIM
  ACTION causes(target: short_circuit_event, cause: touch_event) -> causes_event : CLAIM
  ACTION enables(condition: touch_event, outcome: short_circuit_event) -> enables_event : CLAIM
  ACTION motivates_by(target: short_circuit_event, motive: touch_event) -> motivates_by_event : CLAIM
  ACTION occurred(target: short_circuit_event) -> occurred_event : CLAIM
  ACTION occurred_recently(target: short_circuit_event) -> occurred_recently_event : CLAIM
  ACTION ongoing(target: short_circuit_event) -> ongoing_event : CLAIM
  ACTION outcome(target: short_circuit_event, value: short_circuit_event) -> outcome_event : CLAIM
  ACTION prep_time(target: short_circuit_event) -> prep_time_event : CLAIM
  ACTION rank_rating(target: short_circuit_event) -> rank_rating_event : CLAIM
  ACTION next_to(target: short_circuit_event) -> next_to_event : CLAIM
  ACTION other_side_of(target: short_circuit_event) -> other_side_of_event : CLAIM
  ACTION state_dirty(condition: short