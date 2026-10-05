Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="independence", location=united_kingdom, qualifier="scotland") -> subject_2 : TERM
    TERM property_question(property="independence", subject=subject_2) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
  TURN t2 SPEAKER=AGENT {
    CLAIM controversial(subject=t1.subject_2) BY role_agent STATUS asserted SOURCE "t2:s1" -> controversial_2 : CLAIM
    CLAIM ongoing(target=t1.subject_2) BY role_agent STATUS asserted SOURCE "t2:s1" -> ongoing_2 : CLAIM
    TERM duration(amount=2014, unit=unit_year) -> duration_2 : TERM
    TERM historical_event(location=united_kingdom, name="referendum_2014", period="2014") -> historical_event_2 : TERM
    CLAIM opposes(actor="majority", subject=t1.subject_2) BY role_agent STATUS asserted SOURCE "t2:s2" -> opposes_2 : CLAIM
    CLAIM argues_for(subject="political_parties", value=t1.subject_2) BY role_agent STATUS asserted SOURCE "t2:s3" -> argues_for_2 : CLAIM
    CLAIM ongoing(target=t1.subject_2) BY role_agent STATUS asserted SOURCE "t2:s3" -> ongoing_3 : CLAIM
    LINK contrast(first=opposes_2, second=argues_for_2) SOURCE "t2:s3"
    TERM time_horizon(horizon="future") -> time_horizon_2 : TERM
    CLAIM varies_with(target=time_horizon_2, condition="will_of_people_and_government_actions") BY role_agent STATUS asserted SOURCE "t2:s4" -> varies_with_2 : CLAIM
  }
  TURN t3 SPEAKER=USER {
    TERM property_question(property="closeness", subject=t2.historical_event_2) -> property_question_3 : TERM
    UTTER ask(target=property_question_3)
  }
  TURN t4 SPEAKER=AGENT {
    TERM measure(amount=55.3, unit=unit_percent) -> measure_2 : TERM
    TERM measure(amount=44.7, unit=unit_percent) -> measure_3 : TERM
    CLAIM opposes(actor=measure_2, subject=t1.subject_2) BY role_agent STATUS asserted SOURCE "t4:s1" -> opposes_3 : CLAIM
    CLAIM argues_for(subject=measure_3, value=t1.subject_2) BY role_agent STATUS asserted SOURCE "t4:s1" -> argues_for_3 : CLAIM
    TERM measure(amount=84.6, unit=unit_percent) -> measure_4 : TERM
    TERM group_size(count=3623344, group="valid_votes") -> group_size_2 : TERM
    CLAIM attribute_claim(property="turnout", subject=t2.historical_event_2, value=measure_4) BY role_agent STATUS asserted SOURCE "t4:s2" -> attribute_claim_2 : CLAIM
    CLAIM statement(fact=group_size_2) BY role_agent STATUS asserted SOURCE "t4:s2" -> statement_2 : CLAIM
    TERM measure(amount=10.6, unit=unit_percent) -> measure_5 : TERM
    CLAIM attribute_claim(property="margin", subject=t2.historical_event_2, value=measure_5) BY role_agent STATUS asserted SOURCE "t4:s3" -> attribute_claim_3 : CLAIM
    CLAIM statement(fact=t1.subject_2) BY role_agent STATUS asserted SOURCE "t4:s4" -> statement_3 : CLAIM
    LINK contrast(first=attribute_claim_3, second=statement_3) SOURCE "t4:s4"
  }
  TURN t5 SPEAKER=USER {
    TERM property_question(property="next_referendum_timing", subject=t1.subject_2) -> property_question_4 : TERM
    UTTER ask(target=property_question_4)
  }
  TURN t6 SPEAKER=AGENT {
    CLAIM attribute_claim(property="uncertain", subject=t5.property_question_4, value=TRUE) BY role_agent STATUS asserted SOURCE "t6:s1" -> attribute_claim_4 : CLAIM
    TERM duration(amount=2017, unit=unit_year) -> duration_3 : TERM
    TERM subject(kind="referendum_proposal", location=united_kingdom, qualifier="snp", time="2017") -> subject_3 : TERM
    CLAIM argues_for(subject="snp", value=subject_3) BY role_agent STATUS asserted SOURCE "t6:s2" -> argues_for_4 : CLAIM
    CLAIM opposes(actor="uk_government", subject=subject_3) BY role_agent STATUS asserted SOURCE "t6:s2" -> opposes_4 : CLAIM
    LINK contrast(first=argues_for_4, second=opposes_4) SOURCE "t6:s2"
    CLAIM ongoing(target=subject_3) BY role_agent STATUS asserted SOURCE "t6:s3" -> ongoing_4 : CLAIM
    CLAIM attribute_claim(property="official_date", subject=subject_3, value=FALSE) BY role_agent STATUS asserted SOURCE "t6:s3" -> attribute_claim_5 : CLAIM
    TERM subject(kind="legislation_devolution", location=united_kingdom, qualifier="scottish_parliament") -> subject_4 : TERM
    TERM subject(kind="greater_autonomy", location=united_kingdom, qualifier="scotland") -> subject_5 : TERM
    CLAIM enables(condition=subject_4, outcome=subject_5) BY role_agent STATUS asserted SOURCE "t6:s4" -> enables_2 : CLAIM
    TERM requirement(property="sustained_majority_support", value=TRUE) -> requirement_2 : TERM
    CLAIM argues_for(subject="uk_government", value=requirement_2) BY role_agent STATUS asserted SOURCE "t6:s5" -> argues_for_5 : CLAIM
    LINK contrast(first=enables_2, second=argues_for_5) SOURCE "t6:s5"
    TERM activity(actor="scottish_and_uk_governments", verb="agree_on_referendum") -> activity_2 : TERM
    TERM decision(activity=activity_2) -> decision_2 : TERM
    CLAIM varies_with(target=subject_3, condition=decision_2) BY role_agent STATUS asserted SOURCE "t6:s6" -> varies_with_3 : CLAIM
  }
  TURN t7 SPEAKER=USER {
    TERM property_question(property="vote_choice", subject=role_agent) -> property_question_5 : TERM
    TERM conditional(condition=t1.subject_2, consequence=property_question_5) -> conditional_2 : TERM
    UTTER ask(target=conditional_2)
  }
  TURN t8 SPEAKER=AGENT {
    UTTER apologize()
    TERM subject(kind="personal_opinions_and_beliefs") -> subject_6 : TERM
    CLAIM possesses(item=subject_6, subject=role_agent, value=FALSE) BY role_agent STATUS asserted SOURCE "t8:s1" -> possesses_2 : CLAIM
    TERM activity(actor=role_agent, verb="provide_factual_information") -> activity_3 : TERM
    CLAIM has_goal(goal=activity_3, subject=role_agent) BY role_agent STATUS asserted SOURCE "t8:s2" -> has_goal_2 : CLAIM
    CLAIM provides(actor=role_agent, subject="factual_information") BY role_agent STATUS asserted SOURCE "t8:s2" -> provides_2 : CLAIM
    TERM subject(kind="value_judgments_and_feelings") -> subject_7 : TERM
    CLAIM possesses(item=subject_7, subject=role_agent, value=FALSE) BY role_agent STATUS asserted SOURCE "t8:s3" -> possesses_3 : CLAIM
    CLAIM designed_to_be(quality="neutral_and_factual", subject=role_agent) BY role_agent STATUS asserted SOURCE "t8:s4" -> designed_to_be_2 : CLAIM
    UTTER decline(target=t7.conditional_2)
    CLAIM statement(fact=subject_6) BY role_agent STATUS asserted SOURCE "t8:s5" -> statement_4 : CLAIM
    LINK supports(conclusion=statement_4, premise=possesses_2) SOURCE "t8:s5"
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask | covered |
| n2 | object | united_kingdom, subject | covered |
| n3 | object | subject | covered |
| n4 | claim | controversial, ongoing | covered |
| n5 | claim | opposes | covered |
| n6 | object | united_kingdom | covered |
| n7 | temporal | unit_year, duration | covered |
| n8 | claim | argues_for, ongoing, contrast | covered |
| n9 | claim | time_horizon, varies_with | covered |
| n10 | speech_act | ask, property_question | covered |
| n11 | object | historical_event, united_kingdom | covered |
| n12 | claim | unit_percent, measure, opposes, argues_for | covered |
| n13 | claim | unit_percent, measure, group_size, attribute_claim, statement | covered |
| n14 | claim | unit_percent, measure, attribute_claim | covered |
| n15 | claim | statement, contrast | covered |
| n16 | speech_act | ask, property_question | covered |
| n17 | claim | attribute_claim | covered |
| n18 | claim | argues_for, opposes, contrast, subject | covered |
| n19 | temporal | unit_year, duration | covered |
| n20 | claim | ongoing, attribute_claim | covered |
| n21 | claim | subject, enables | covered |
| n22 | claim | requirement, argues_for, contrast | covered |
| n23 | claim | activity, decision, varies_with | covered |
| n24 | speech_act | ask, role_agent, conditional, property_question | covered |
| n25 | negation | possesses, subject | covered |
| n26 | claim | provides, has_goal, activity | covered |
| n27 | negation | possesses, subject | covered |
| n28 | speech_act | apologize, decline | covered |
| n29 | reasoning | supports, possesses | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t8:s5 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
