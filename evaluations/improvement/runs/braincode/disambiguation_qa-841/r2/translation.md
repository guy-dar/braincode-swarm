```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  ACTION ask(target=explain_ambiguity) -> explanation : TERM
  CLAIM explain_ambiguity BY task STATUS hypothesized SOURCE "task description" -> explain_ambiguity_2 : CLAIM
  ACTION generate_explanation(options=[A, B, C, D, E]) -> explanation : TERM
  CLAIM A BY task STATUS hypothesized SOURCE "option A" -> option_A : CLAIM
  CLAIM B BY task STATUS hypothesized SOURCE "option B" -> option_B : CLAIM
  CLAIM C BY task STATUS hypothesized SOURCE "option C" -> option_C : CLAIM
  CLAIM D BY task STATUS hypothesized SOURCE "option D" -> option_D : CLAIM
  CLAIM E BY task STATUS hypothesized SOURCE "option E" -> option_E : CLAIM
  CLAIM none BY task STATUS hypothesized SOURCE "option F" -> option_F : CLAIM
}
```