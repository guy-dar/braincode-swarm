```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    UTTER ask(target=property_question(property=procedures_immediately_after_goal, subject=football_match))
  }
  TURN t2 SPEAKER=USER REPLY_TO t1 {
    UTTER ask(target=property_question(property=referee_action_immediately_after_goal, subject=football_match))
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    UTTER ask(target=property_question(property=conceded_team_next_action, subject=football_match))
  }
  TURN t4 SPEAKER=USER REPLY_TO t3 {
    TERM property_question(property=procedures_immediately_after_goal, subject=football_match) -> procedures_immediately_after_goal : TERM
    TERM property_question(property=referee_action_immediately_after_goal, subject=football_match) -> referee_action_immediately_after_goal : TERM
    TERM property_question(property=conceded_team_next_action, subject=football_match) -> conceded_team_next_action : TERM
    UTTER ask(target=respond(procedures_immediately_after_goal, referee_action_immediately_after_goal, conceded_team_next_action))
  }
  TURN t5 SPEAKER=USER REPLY_TO t4 {
    TERM respond(procedures_immediately_after_goal, referee_action_immediately_after_goal, conceded_team_next_action) -> answer : TERM
    RECORD ACTION select_option(target=answer, value="AC, D, BD") STATUS succeeded SOURCE "t5:answer"
    TERM extract(target=answer, limit=1) -> answer : TERM
    UTTER provides(target=answer)
  }
}
```