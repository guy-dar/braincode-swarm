```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  ACTION select_option(target=question_1, value=answer_1) -> answer_1_result : TERM
  ACTION select_option(target=question_2, value=answer_2) -> answer_2_result : TERM
  ACTION select_option(target=question_3, value=answer_3) -> answer_3_result : TERM
  ACTION combine_answers(answer_1_result, answer_2_result, answer_3_result) -> final_answer : TERM
  CLAIM outcome(event=combine_answers, value=final_answer) BY solver STATUS hypothesized SOURCE "task description" -> outcome : CLAIM
}
```