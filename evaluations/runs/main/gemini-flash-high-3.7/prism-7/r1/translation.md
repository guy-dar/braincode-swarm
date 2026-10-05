Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="independence", location=united_kingdom) -> subject_2 : TERM
    TERM property_question(property="future_status", subject=subject_2) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
  TURN t2 SPEAKER=AGENT {
    CLAIM controversial(subject=t1.subject_2) BY role_agent STATUS asserted SOURCE "t2:s1" -> controversial_2 : CLAIM
    CLAIM ongoing(target=t1.subject_2) BY role_agent STATUS asserted SOURCE "t2:s1" -> ongoing_2 : CLAIM
    TERM time_point(date="2014") -> time_point_2 : TERM
    TERM historical_event(location=united_kingdom, name="independence_referendum", period=2014) -> historical_event_2 : TERM
    CLAIM statement(fact=historical_event_2) BY role_agent STATUS reported SOURCE "t2:s2" -> statement_2 : CLAIM
    CLAIM opposes(actor="majority", subject=t1.subject_2) BY role_agent STATUS reported SOURCE "t2:s2" -> opposes_2 : CLAIM
    TERM activity(actor="political_parties", purpose=t1.subject_2, verb="campaign") -> activity_2 : TERM
    CLAIM ongoing(target=activity_2) BY role_agent STATUS asserted SOURCE "t2:s3" -> ongoing_3 : CLAIM
    CLAIM has_goal(goal=t1.subject_2, subject="political_parties") BY role_agent STATUS asserted SOURCE "t2:s3" -> has_goal_2 : CLAIM
    LINK contrast(first=opposes_2, second=ongoing_3) SOURCE "t2:s3"
    TERM time_horizon(horizon="future") -> time_horizon_2 : TERM
    CLAIM varies_with(target=t1.subject_2, condition="will_of_people_and_government") BY role_agent STATUS asserted SOURCE "t2:s4" -> varies_with_2 : CLAIM
  }
  TURN t3 SPEAKER=USER {
    TERM property_question(property="closeness", subject=t2.historical_event_2) -> property_question_3 : TERM
    UTTER ask(target=property_question_3)
  }
  TURN t4 SPEAKER=AGENT {
    TERM measure(amount=55.3, unit=unit_percent) -> measure_2 : TERM
    TERM measure(amount=44.7, unit=unit_percent) -> measure_3 : TERM
    CLAIM statement(fact=measure_2) BY role_agent STATUS reported SOURCE "t4:s1" -> statement_3 : CLAIM
    CLAIM statement(fact=measure_3) BY role_agent STATUS reported SOURCE "t4:s1" -> statement_4 : CLAIM
    CLAIM opposes(actor="majority", subject=t1.subject_2) BY role_agent STATUS reported SOURCE "t4:s1" -> opposes_3 : CLAIM
    TERM measure(amount=84.6, unit=unit_percent) -> measure_4 : TERM
    TERM group_size(count=3623344, group="valid_votes") -> group_size_2 : TERM
    CLAIM statement(fact=measure_4) BY role_agent STATUS reported SOURCE "t4:s2" -> statement_5 : CLAIM
    CLAIM statement(fact=group_size_2) BY role_agent STATUS reported SOURCE "t4:s2" -> statement_6 : CLAIM
    TERM measure(amount=10.6, unit=unit_percent) -> measure_5 : TERM
    CLAIM statement(fact=measure_5) BY role_agent STATUS asserted SOURCE "t4:s3" -> statement_7 : CLAIM
    CLAIM statement(fact=t1.subject_2) BY role_agent STATUS asserted SOURCE "t4:s4" -> statement_8 : CLAIM
    LINK contrast(first=statement_7, second=statement_8) SOURCE "t4:s4"
  }
  TURN t5 SPEAKER=USER {
    TERM property_question(property="next_timing", subject=t1.subject_2) -> property_question_4 : TERM
    UTTER ask(target=property_question_4)
  }
  TURN t6 SPEAKER=AGENT {
    TERM time_horizon(horizon="uncertain_timing") -> time_horizon_3 : TERM
    CLAIM statement(fact=time_horizon_3) BY role_agent STATUS asserted SOURCE "t6:s1" -> statement_9 : CLAIM
    TERM time_point(date="2017") -> time_point_3 : TERM
    TERM subject(kind="referendum_proposal", location=united_kingdom, time="2017") -> subject_3 : TERM
    CLAIM opposes(actor=united_kingdom, subject=subject_3) BY role_agent STATUS reported SOURCE "t6:s2" -> opposes_4 : CLAIM
    CLAIM ongoing(target=subject_3) BY role_agent STATUS asserted SOURCE "t6:s3" -> ongoing_4 : CLAIM
    TERM subject(kind="devolution_bill", location=united_kingdom) -> subject_4 : TERM
    CLAIM enables(condition=subject_4, outcome=t1.subject_2) BY role_agent STATUS inferred SOURCE "t6:s4" -> enables_2 : CLAIM
    CLAIM statement(fact=t1.subject_2) BY role_agent STATUS reported SOURCE "t6:s5" -> statement_10 : CLAIM
    CLAIM varies_with(target=t1.subject_2, condition="government_agreement") BY role_agent STATUS asserted SOURCE "t6:s6" -> varies_with_3 : CLAIM
  }
  TURN t7 SPEAKER=USER {
    TERM property_question(property="personal_vote", subject=role_agent) -> property_question_5 : TERM
    UTTER ask(target=property_question_5)
  }
  TURN t8 SPEAKER=AGENT {
    TERM subject(kind=beliefs) -> subject_5 : TERM
    TERM negation(target=subject_5) -> negation_2 : TERM
    CLAIM statement(fact=negation_2) BY role_agent STATUS asserted SOURCE "t8:s1" -> statement_11 : CLAIM
    CLAIM possesses(item=subject_5, subject=role_agent, value=FALSE) BY role_agent STATUS asserted SOURCE "t8:s1" -> possesses_2 : CLAIM
    CLAIM provides(actor=role_agent, subject="factual_information") BY role_agent STATUS asserted SOURCE "t8:s2" -> provides_2 : CLAIM
    TERM subject(kind=personal_values) -> subject_6 : TERM
    TERM negation(target=subject_6) -> negation_3 : TERM
    CLAIM statement(fact=negation_3) BY role_agent STATUS asserted SOURCE "t8:s3" -> statement_12 : CLAIM
    CLAIM possesses(item=subject_6, subject=role_agent, value=FALSE) BY role_agent STATUS asserted SOURCE "t8:s3" -> possesses_3 : CLAIM
    CLAIM designed_to_be(quality="neutral", subject=role_agent) BY role_agent STATUS asserted SOURCE "t8:s4" -> designed_to_be_2 : CLAIM
    UTTER decline(target=t7.property_question_5)
    LINK supports(conclusion=statement_11, premise=statement_12) SOURCE "t8:s5"
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
| n5 | claim | statement, opposes, united_kingdom | covered |
| n6 | object | united_kingdom | covered |
| n7 | temporal | time_point | covered |
| n8 | claim | ongoing, has_goal | covered |
| n9 | claim | varies_with, time_horizon | covered |
| n10 | speech_act | ask | covered |
| n11 | object | historical_event, united_kingdom | covered |
| n12 | claim | unit_percent, statement, opposes | covered |
| n13 | claim | unit_percent, group_size, statement | covered |
| n14 | claim | unit_percent, statement | covered |
| n15 | claim | statement, contrast | covered |
| n16 | speech_act | ask | covered |
| n17 | claim | time_horizon, statement | covered |
| n18 | claim | opposes, united_kingdom | covered |
| n19 | temporal | time_point | covered |
| n20 | claim | ongoing | covered |
| n21 | claim | enables | covered |
| n22 | claim | statement | covered |
| n23 | claim | varies_with | covered |
| n24 | speech_act | ask, role_agent | covered |
| n25 | negation | negation, possesses, beliefs, statement | covered |
| n26 | claim | provides, designed_to_be | covered |
| n27 | negation | negation, possesses, personal_values, statement | covered |
| n28 | speech_act | decline | covered |
| n29 | reasoning | supports, statement | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t8:s5 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
