Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM property_question(property="independence", subject=united_kingdom) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM subject(kind="independence_debate", location=united_kingdom) -> subject_2 : TERM
    CLAIM controversial(subject=subject_2) BY role_agent STATUS asserted SOURCE "t2:s1" -> controversial_2 : CLAIM
    CLAIM ongoing(target=subject_2) BY role_agent STATUS asserted SOURCE "t2:s1" -> ongoing_2 : CLAIM
    TERM measure(amount=2014, unit=unit_year) -> measure_2 : TERM
    TERM activity(actor="electorate", location=united_kingdom, object=measure_2, verb="vote_remain") -> activity_2 : TERM
    CLAIM statement(fact=activity_2) BY role_agent STATUS reported SOURCE "t2:s2" -> statement_2 : CLAIM
    TERM subject(kind="independence_campaign", location=united_kingdom) -> subject_3 : TERM
    CLAIM ongoing(target=subject_3) BY role_agent STATUS asserted SOURCE "t2:s3" -> ongoing_3 : CLAIM
    LINK contrast(first=statement_2, second=ongoing_3) SOURCE "t2:s3"
    TERM subject(kind="future_constitutional_status", location=united_kingdom) -> subject_4 : TERM
    TERM subject(kind="public_will_and_government_actions", location=united_kingdom) -> subject_5 : TERM
    CLAIM varies_with(condition=subject_5, target=subject_4) BY role_agent STATUS asserted SOURCE "t2:s4" -> varies_with_2 : CLAIM
    UTTER inform(target=controversial_2)
  }
  TURN t3 SPEAKER=USER {
    TERM property_question(property="result_margin", subject=united_kingdom) -> property_question_3 : TERM
    UTTER ask(target=property_question_3)
  }
  TURN t4 SPEAKER=AGENT {
    TERM measure(amount=55.3, unit=unit_percent) -> measure_3 : TERM
    TERM measure(amount=44.7, unit=unit_percent) -> measure_4 : TERM
    TERM activity(actor="electorate", location=united_kingdom, object=measure_3, verb="vote_remain") -> activity_3 : TERM
    CLAIM statement(fact=activity_3) BY role_agent STATUS reported SOURCE "t4:s1" -> statement_3 : CLAIM
    TERM activity(actor="electorate", location=united_kingdom, object=measure_4, verb="vote_independence") -> activity_4 : TERM
    CLAIM statement(fact=activity_4) BY role_agent STATUS reported SOURCE "t4:s1" -> statement_4 : CLAIM
    TERM measure(amount=84.6, unit=unit_percent) -> measure_5 : TERM
    TERM group_size(count=3623344, group="voters") -> group_size_2 : TERM
    CLAIM attribute_claim(property="turnout", subject=united_kingdom, value=measure_5) BY role_agent STATUS reported SOURCE "t4:s2" -> attribute_claim_2 : CLAIM
    CLAIM statement(fact=group_size_2) BY role_agent STATUS reported SOURCE "t4:s2" -> statement_5 : CLAIM
    TERM measure(amount=10.6, unit=unit_percent) -> measure_6 : TERM
    CLAIM attribute_claim(property="vote_margin", subject=united_kingdom, value=measure_6) BY role_agent STATUS reported SOURCE "t4:s3" -> attribute_claim_3 : CLAIM
    TERM subject(kind="referendum_decision", location=united_kingdom) -> subject_6 : TERM
    CLAIM statement(fact=subject_6) BY role_agent STATUS asserted SOURCE "t4:s4" -> statement_6 : CLAIM
    UTTER inform(target=statement_3)
  }
  TURN t5 SPEAKER=USER {
    TERM property_question(property="next_referendum_date", subject=united_kingdom) -> property_question_4 : TERM
    UTTER ask(target=property_question_4)
  }
  TURN t6 SPEAKER=AGENT {
    TERM time_horizon(horizon="uncertain_future") -> time_horizon_2 : TERM
    CLAIM attribute_claim(property="timing", subject=united_kingdom, value=time_horizon_2) BY role_agent STATUS asserted SOURCE "t6:s1" -> attribute_claim_4 : CLAIM
    TERM time_point(date="2017") -> time_point_2 : TERM
    TERM activity(actor="snp", location=united_kingdom, verb="propose_second_referendum") -> activity_5 : TERM
    CLAIM opposes(actor="uk_government", subject=activity_5) BY role_agent STATUS reported SOURCE "t6:s2" -> opposes_2 : CLAIM
    CLAIM ongoing(target=activity_5) BY role_agent STATUS reported SOURCE "t6:s3" -> ongoing_4 : CLAIM
    TERM subject(kind="tax_and_welfare_powers", location=united_kingdom) -> subject_7 : TERM
    TERM subject(kind="devolution_autonomy", location=united_kingdom) -> subject_8 : TERM
    CLAIM leads_to(cause=subject_7, effect=subject_8) BY role_agent STATUS asserted SOURCE "t6:s4" -> leads_to_2 : CLAIM
    TERM requirement(property="sustained_majority_support", value=TRUE) -> requirement_2 : TERM
    CLAIM proposed_policy(policy=requirement_2, requirements=[requirement_2]) BY role_agent STATUS reported SOURCE "t6:s5" -> proposed_policy_2 : CLAIM
    TERM subject(kind="bilateral_agreement", location=united_kingdom) -> subject_9 : TERM
    TERM activity(location=united_kingdom, verb="hold_referendum") -> activity_6 : TERM
    CLAIM enables(condition=subject_9, outcome=activity_6) BY role_agent STATUS asserted SOURCE "t6:s6" -> enables_2 : CLAIM
    UTTER inform(target=attribute_claim_4)
  }
  TURN t7 SPEAKER=USER {
    TERM property_question(property="hypothetical_voting_choice", subject=role_agent) -> property_question_5 : TERM
    UTTER ask(target=property_question_5)
  }
  TURN t8 SPEAKER=AGENT {
    TERM subject(kind="beliefs") -> subject_10 : TERM
    CLAIM possesses(item=subject_10, subject=role_agent, value=FALSE) BY role_agent STATUS asserted SOURCE "t8:s1" -> possesses_2 : CLAIM
    CLAIM designed_to_be(quality="neutral_factual_provider", subject=role_agent) BY role_agent STATUS asserted SOURCE "t8:s2" -> designed_to_be_2 : CLAIM
    TERM activity(actor="role_agent", verb="make_value_judgments") -> activity_7 : TERM
    CLAIM possesses(item=activity_7, subject=role_agent, value=FALSE) BY role_agent STATUS asserted SOURCE "t8:s3" -> possesses_3 : CLAIM
    TERM subject(kind="personal_viewpoint") -> subject_11 : TERM
    CLAIM opposes(actor=role_agent, subject=subject_11) BY role_agent STATUS asserted SOURCE "t8:s4" -> opposes_3 : CLAIM
    TERM activity(actor="role_agent", verb="state_voting_choice") -> activity_8 : TERM
    UTTER decline(target=activity_8)
    CLAIM unaware(person=role_agent, topic=activity_8) BY role_agent STATUS asserted SOURCE "t8:s5" -> unaware_2 : CLAIM
    LINK supports(conclusion=unaware_2, premise=possesses_2) SOURCE "t8:s5"
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, property_question, united_kingdom | covered |
| n2 | object | united_kingdom | covered |
| n3 | object | united_kingdom, property_question | covered |
| n4 | claim | controversial, ongoing, subject | covered |
| n5 | claim | statement, activity, united_kingdom | covered |
| n6 | object | united_kingdom | covered |
| n7 | temporal | measure, unit_year | covered |
| n8 | claim | ongoing, subject, contrast, statement | covered |
| n9 | claim | varies_with, subject | covered |
| n10 | speech_act | ask, property_question, united_kingdom | covered |
| n11 | object | united_kingdom, property_question | covered |
| n12 | claim | statement, activity, measure, unit_percent | covered |
| n13 | claim | attribute_claim, statement, measure, group_size, unit_percent | covered |
| n14 | claim | attribute_claim, measure, unit_percent | covered |
| n15 | claim | statement, subject | covered |
| n16 | speech_act | ask, property_question, united_kingdom | covered |
| n17 | claim | attribute_claim, time_horizon | covered |
| n18 | claim | opposes, activity, time_point | covered |
| n19 | temporal | time_point | covered |
| n20 | claim | ongoing, activity | covered |
| n21 | claim | leads_to, subject | covered |
| n22 | claim | proposed_policy, requirement | covered |
| n23 | claim | enables, subject, activity | covered |
| n24 | speech_act | ask, property_question, role_agent | covered |
| n25 | negation | possesses, subject | covered |
| n26 | claim | designed_to_be | covered |
| n27 | negation | possesses, activity | covered |
| n28 | speech_act | decline, activity | covered |
| n29 | reasoning | supports, possesses, unaware | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t8:s5 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
