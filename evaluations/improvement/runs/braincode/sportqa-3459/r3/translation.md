```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM property_question(property="select_all_correct_choices", subject="multiple_choice_question") -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
  TURN t1 SPEAKER=USER {
    TERM requirement(property="multiple_choice_question", value=property_question_2) -> requirement_2 : TERM
    UTTER ask(target=requirement_2)
  }
  TURN t1 SPEAKER=USER {
    TERM property_question(property="main_question", subject="why_might_a_football_player_be_allowed_to_retake_a_penalty") -> property_question_3 : TERM
    UTTER ask(target=property_question_3)
  }
  TURN t1 SPEAKER=USER {
    TERM property_question(property="sub_question_1", subject="why_might_the_goalkeeper_moving_off_the_goal_line_result_in_a_retake") -> property_question_4 : TERM
    UTTER ask(target=property_question_4)
  }
  TURN t1 SPEAKER=USER {
    TERM property_question(property="sub_question_2", subject="why_might_the_referee_blowing_the_whistle_before_the_player_kicked_the_ball_result_in_a_retake") -> property_question_5 : TERM
    UTTER ask(target=property_question_5)
  }
  TURN t1 SPEAKER=USER {
    TERM property_question(property="answer_format", subject="concatenate_correct_choices") -> property_question_6 : TERM
    UTTER ask(target=property_question_6)
  }
  TURN t1 SPEAKER=USER {
    TERM property_question(property="answer_separation", subject="separate_answers_with_comma") -> property_question_7 : TERM
    UTTER ask(target=property_question_7)
  }
  TURN t1 SPEAKER=USER {
    TERM property_question(property="example", subject="AC,BD") -> property_question_8 : TERM
    UTTER ask(target=property_question_8)
  }
}
```