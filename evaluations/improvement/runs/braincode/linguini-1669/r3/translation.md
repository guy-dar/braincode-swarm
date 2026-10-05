```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  TERM property_question(property=tip_point, subject=ewce) -> property_question_2 : TERM
  ACTION translate(target=property_question_2, source_language=ilennime, target_language=English) -> result : STRING
}
```