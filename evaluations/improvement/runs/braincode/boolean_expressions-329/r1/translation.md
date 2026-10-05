```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM rule_condition(condition=condition, consequence=consequence) -> rule_condition_2 : TERM
    UTTER ask(target=rule_condition_2)
  }
  TURN t2 SPEAKER=USER {
    TERM condition(A="A", B="B", C="C", D="D", E="E") -> condition_2 : TERM
    UTTER ask(target=condition_2)
  }
  TURN t3 SPEAKER=USER {
    TERM choice(A="A", B="B", C="C", D="D", E="E") -> choice_2 : TERM
    UTTER ask(target=choice_2)
  }
}

TASK rule_condition {
  TERM condition(condition=choice_2, consequence=rule_condition_2) -> condition_3 : TERM
  ACTION test_condition(condition=condition_3, expected=TRUE) -> test_condition_2 : TERM
  ACTION check_result(result=test_condition_2) -> result_2 : TERM
  ACTION choice(result=result_2, A="A", B="B", C="C", D="D", E="E") -> choice_2 : TERM
  ACTION rule_condition(condition=choice_2, consequence=rule_condition_2) -> rule_condition_2 : TERM
}

TASK condition {
  TERM choice(A="A", B="B", C="C", D="D", E="E") -> choice_2 : TERM
  ACTION test_condition(condition=choice_2, expected=TRUE) -> test_condition_2 : TERM
  ACTION check_result(result=test_condition_2) -> result_2 : TERM
  ACTION choice(result=result_2, A="A", B="B", C="C", D="D", E="E") -> choice_2 : TERM
  ACTION condition(condition=choice_2) -> condition_2 : TERM
}

TASK choice {
  TERM rule_condition(condition=condition_2, consequence=consequence_2) -> rule_condition_2 : TERM
  ACTION test_condition(condition=rule_condition_2, expected=TRUE) -> test_condition_2 : TERM
  ACTION check_result(result=test_condition_2) -> result_2 : TERM
  ACTION rule_condition(condition=result_2, consequence=consequence_2) -> rule_condition_2 : TERM
  ACTION choice(result=result_2, A="A", B="B", C="C", D="D", E="E") -> choice_2 : TERM
}

TASK test_condition {
  TERM check_result(result=result_2) -> check_result_2 : TERM
  ACTION rule_condition(condition=check_result_2, consequence=consequence_2) -> rule_condition_2 : TERM
  ACTION test_condition(condition=rule_condition_2, expected=TRUE) -> test_condition_2 : TERM
  ACTION check_result(result=test_condition_2) -> result_2 : TERM
  ACTION rule_condition(condition=result_2, consequence=consequence_2) -> rule_condition_2 : TERM
}

TASK check_result {
  TERM rule_condition(condition=result_2, consequence=consequence_2) -> rule_condition_2 : TERM
  ACTION test_condition(condition=rule_condition_2, expected=TRUE) -> test_condition_2 : TERM
  ACTION check_result(result=test_condition_2) -> result_2 : TERM
  ACTION rule_condition(condition=result_2, consequence=consequence_2) -> rule_condition_2 : TERM
  ACTION check_result(result=result_2) -> result_2 : TERM
}

TASK rule_condition {
  TERM condition(condition=consequence_2, consequence=consequence_2) -> condition_2 : TERM
  ACTION test_condition(condition=condition_2, expected=TRUE) -> test_condition_2 : TERM
  ACTION check_result(result=test_condition_2) -> result_2 : TERM
  ACTION condition(condition=result_2, consequence=consequence_2) -> condition_2 : TERM
  ACTION rule_condition(condition=condition_2, consequence=consequence_2) -> rule_condition_2 : TERM
}

TASK consequence {
  TERM rule_condition(condition=result_2, consequence=consequence_2) -> rule_condition_2 : TERM
  ACTION test_condition(condition=rule_condition_2, expected=TRUE) -> test_condition_2 : TERM
  ACTION check_result(result=test_condition_2) -> result_2 : TERM
  ACTION rule_condition(condition=result_2, consequence=consequence_2) -> rule_condition_2 : TERM
  ACTION consequence(result=result_2) -> consequence_2 : TERM
}

TASK consequence_2 {
  TERM rule_condition(condition=result_2, consequence=result_2) -> rule_condition_2 : TERM
  ACTION test_condition(condition=rule_condition_2, expected=TRUE) -> test_condition_2 : TERM
  ACTION check_result(result=test_condition_2) -> result_2 : TERM
  ACTION rule_condition(condition=result_2, consequence=result_2) -> rule_condition_2 : TERM
  ACTION consequence(result=result_2) -> consequence_2 : TERM
}
```