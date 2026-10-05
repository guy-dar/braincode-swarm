Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="national_independence", location=united_kingdom) -> subject_2 : TERM
    TERM property_question(property="national_independence", subject=subject_2) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM subject(kind="national_independence", location=united_kingdom) -> subject_2 : TERM
    CLAIM controversial(subject=subject_2) BY role_agent STATUS asserted SOURCE "t2:s1" -> controversial_2 : CLAIM
    CLAIM ongoing(target=subject_2) BY role_agent STATUS asserted SOURCE "t2:s1" -> ongoing_2 : CLAIM
    TERM measure(amount=2014, unit=unit_year) -> measure_2 : TERM
    TERM historical_event(location=united_kingdom, name="referendum", period=2014) -> historical_event_2 : TERM
    CLAIM statement(fact=historical_event_2) BY role_agent STATUS asserted SOURCE "t2:s2" -> statement_2 : CLAIM
    CLAIM has_goal(goal=subject_2, subject="political_parties") BY role_agent STATUS asserted SOURCE "t2:s3" -> has_goal_2 : CLAIM
    CLAIM ongoing(target=subject_2) BY role_agent STATUS asserted SOURCE "t2:s3" -> ongoing_3 : CLAIM
    LINK contrast(first=statement_2, second=has_goal_2) SOURCE "t2:s3"
    TERM time_horizon(horizon="future") -> time_horizon_2 : TERM
    CLAIM varies_with(target=subject_2, condition="will_of_people_and_government") BY role_agent STATUS asserted SOURCE "t2:s4" -> varies_with_2 : CLAIM
  }
  TURN t3 SPEAKER=USER {
    TERM historical_event(location=united_kingdom, name="referendum", period=2014) -> historical_event_2 : TERM
    TERM property_question(property="closeness", subject=historical_event_2) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
  TURN t4 SPEAKER=AGENT {
    TERM subject(kind="national_independence", location=united_kingdom) -> subject_2 : TERM
    TERM measure(amount=55.3, unit=unit_percent) -> measure_2 : TERM
    TERM measure(amount=44.7, unit=unit_percent) -> measure_3 : TERM
    CLAIM opposes(actor="majority_voters", subject=subject_2) BY role_agent STATUS asserted SOURCE "t4:s1" -> opposes_2 : CLAIM
    TERM measure(amount=84.6, unit=unit_percent) -> measure_4 : TERM
    TERM group_size(count=3623344, group="valid_votes") -> group_size_2 : TERM
    CLAIM statement(fact=group_size_2) BY role_agent STATUS asserted SOURCE "t4:s2" -> statement_2 : CLAIM
    TERM measure(amount=10.6, unit=unit_percent) -> measure_5 : TERM
    CLAIM statement(fact=measure_5) BY role_agent STATUS asserted SOURCE "t4:s3" -> statement_3 : CLAIM
    TERM historical_event(location=united_kingdom, name="referendum", period=2014) -> historical_event_2 : TERM
    CLAIM statement(fact=historical_event_2) BY role_agent STATUS asserted SOURCE "t4:s4" -> statement_4 : CLAIM
    LINK contrast(first=statement_3, second=statement_4) SOURCE "t4:s4"
  }
  TURN t5 SPEAKER=USER {
    TERM subject(kind="referendum", location=united_kingdom) -> subject_2 : TERM
    TERM property_question(property="timing", subject=subject_2) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
  TURN t6 SPEAKER=AGENT {
    TERM subject(kind="referendum", location=united_kingdom) -> subject_2 : TERM
    CLAIM statement(fact=subject_2) BY role_agent STATUS asserted SOURCE "t6:s1" -> statement_2 : CLAIM
    TERM time_point(date="2017") -> time_point_2 : TERM
    TERM historical_event(location=united_kingdom, name="proposal_referendum", period=2017) -> historical_event_2 : TERM
    CLAIM has_goal(goal=historical_event_2, subject="snp") BY role_agent STATUS asserted SOURCE "t6:s2" -> has_goal_2 : CLAIM
    CLAIM opposes(actor="uk_government", subject=historical_event_2) BY role_agent STATUS asserted SOURCE "t6:s2" -> opposes_2 : CLAIM
    LINK contrast(first=has_goal_2, second=opposes_2) SOURCE "t6:s2"
    CLAIM has_goal(goal=subject_2, subject="snp") BY role_agent STATUS asserted SOURCE "t6:s3" -> has_goal_3 : CLAIM
    CLAIM ongoing(target=subject_2) BY role_agent STATUS asserted SOURCE "t6:s3" -> ongoing_2 : CLAIM
    TERM subject(kind="autonomy", location=united_kingdom, qualifier="greater_autonomy") -> subject_3 : TERM
    CLAIM enables(condition=subject_2, outcome=subject_3) BY role_agent STATUS asserted SOURCE "t6:s4" -> enables_2 : CLAIM
    CLAIM opposes(actor="uk_government", subject=subject_2) BY role_agent STATUS asserted SOURCE "t6:s5" -> opposes_3 : CLAIM
    LINK contrast(first=has_goal_3, second=opposes_3) SOURCE "t6:s5"
    CLAIM enables(condition=subject_2, outcome=subject_2) BY role_agent STATUS asserted SOURCE "t6:s6" -> enables_3 : CLAIM
  }
  TURN t7 SPEAKER=USER {
    TERM property_question(property="vote_choice", subject=role_agent) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
  TURN t8 SPEAKER=AGENT {
    TERM property_question(property="vote_choice", subject=role_agent) -> property_question_2 : TERM
    UTTER apologize(target=property_question_2)
    TERM subject(kind="beliefs", qualifier=beliefs) -> subject_2 : TERM
    CLAIM possesses(item=subject_2, subject=role_agent, value=FALSE) BY role_agent STATUS asserted SOURCE "t8:s1" -> possesses_2 : CLAIM
    CLAIM has_goal(goal=subject_2, subject=role_agent) BY role_agent STATUS asserted SOURCE "t8:s2" -> has_goal_2 : CLAIM
    TERM subject(kind="personal_values", qualifier=personal_values) -> subject_3 : TERM
    CLAIM possesses(item=subject_3, subject=role_agent, value=FALSE) BY role_agent STATUS asserted SOURCE "t8:s3" -> possesses_3 : CLAIM
    CLAIM designed_to_be(quality="factual_neutral", subject=role_agent) BY role_agent STATUS asserted SOURCE "t8:s4" -> designed_to_be_2 : CLAIM
    CLAIM provides(actor=role_agent, subject="factual_information") BY role_agent STATUS asserted SOURCE "t8:s4" -> provides_2 : CLAIM
    UTTER decline(target=property_question_2)
    CLAIM statement(fact=property_question_2) BY role_agent STATUS asserted SOURCE "t8:s5" -> statement_2 : CLAIM
    LINK supports(conclusion=statement_2, premise=possesses_2) SOURCE "t8:s5"
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask | covered |
| n2 | object | united_kingdom | covered |
| n3 | object | subject | covered |
| n4 | claim | controversial, ongoing | covered |
| n5 | claim | statement, historical_event | covered |
| n6 | object | united_kingdom | covered |
| n7 | temporal | unit_year | covered |
| n8 | claim | has_goal, ongoing, contrast | covered |
| n9 | claim | varies_with, time_horizon | covered |
| n10 | speech_act | ask | covered |
| n11 | object | historical_event | covered |
| n12 | claim | opposes, measure, unit_percent | covered |
| n13 | claim | measure, unit_percent, group_size, statement | covered |
| n14 | claim | measure, unit_percent, statement | covered |
| n15 | claim | statement, historical_event, contrast | covered |
| n16 | speech_act | ask | covered |
| n17 | claim | statement | covered |
| n18 | claim | opposes, contrast | covered |
| n19 | temporal | time_point | covered |
| n20 | claim | has_goal, ongoing | covered |
| n21 | claim | enables | covered |
| n22 | claim | opposes, contrast | covered |
| n23 | claim | enables | covered |
| n24 | speech_act | ask, role_agent | covered |
| n25 | negation | beliefs, possesses | covered |
| n26 | claim | has_goal, provides, designed_to_be | covered |
| n27 | negation | personal_values, possesses | covered |
| n28 | speech_act | decline, apologize | covered |
| n29 | reasoning | supports | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t8:s5 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
