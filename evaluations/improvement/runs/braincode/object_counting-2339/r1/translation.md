```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM property_question(property=total_number, subject=total_musical_instruments_and_mobiles) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
}
```