```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM constraint_17_plus() -> constraint_17_plus_2 : TERM
    TERM property_question(property=evaluates_to_true, subject=one_of_five_expressions) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
}
```