```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM property_question(property=adjective_order, subject=correct_adjective_order) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
  TURN t2 SPEAKER=USER {
    TERM correct_adjective_order() BY user STATUS asserted SOURCE "t2:duration" -> correct_adjective_order_2 : TERM
    RECORD ACTION search_web(target=correct_adjective_order_2, constraints=[]) STATUS succeeded SOURCE "t2:s2" -> search_web_event : EVENT
    CLAIM connectivity_works(event=search_web_event) BY user STATUS observed SOURCE "t2:s2" -> connectivity_works_2 : CLAIM
    LINK rejects(evidence=connectivity_works_2, hypothesis=incorrect_adjective_order) SOURCE "t2:s3"
    CLAIM incorrect_adjective_order() BY user STATUS hypothesized SOURCE "t2:s3" -> incorrect_adjective_order_3 : CLAIM
    LINK supports(conclusion=incorrect_adjective_order_3, premise=connectivity_works_2) SOURCE "t2:s3"
  }
}
```