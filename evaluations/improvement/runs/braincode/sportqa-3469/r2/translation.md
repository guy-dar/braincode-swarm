```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  ACTION select_option(target=main_question) -> selected_choice_1 : TERM
  ACTION select_option(target=sub_question_1) -> selected_choice_2 : TERM
  ACTION select_option(target=sub_question_2) -> selected_choice_3 : TERM
  ACTION concatenate_choices(choice_1: selected_choice_1, choice_2: selected_choice_2, choice_3: selected_choice_3) -> final_answer : TERM
  ACTION format_answer(answer: final_answer) -> formatted_answer : TERM
  ACTION record_answer(answer: formatted_answer) -> recorded_answer : EVENT
}
```