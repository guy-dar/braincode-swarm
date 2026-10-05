```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM property_question(property=answer_format, subject=main_question) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
  TURN t2 SPEAKER=USER REPLY_TO t1 AMENDS [t1.property_question_2] {
    TERM property_question(property=answer_format, subject=sub_question_1) -> property_question_3 : TERM
    UTTER ask(target=property_question_3)
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 AMENDS [t2.property_question_3] {
    TERM property_question(property=answer_format, subject=sub_question_2) -> property_question_4 : TERM
    UTTER ask(target=property_question_4)
  }
  TURN t4 SPEAKER=USER REPLY_TO t3 {
    TERM property_question(property=answer_format, subject=main_question) -> property_question_5 : TERM
    UTTER ask(target=property_question_5)
  }
}
```