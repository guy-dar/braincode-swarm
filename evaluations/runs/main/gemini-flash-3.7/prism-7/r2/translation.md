Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="independence", location=country::GB, qualifier="scotland") -> subject_2 : TERM
    TERM property_question(property="status", subject=subject_2) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM subject(kind="independence_debate", location=country::GB, qualifier="scotland") -> subject_2 : TERM
    CLAIM controversial(subject=subject_2) BY role_agent STATUS asserted SOURCE "t2:s1" -> controversial_2 : CLAIM
    CLAIM ongoing(target=subject_2) BY role_agent STATUS asserted SOURCE "t2:s1" -> ongoing_2 : CLAIM
    TERM time_point(date="2014") -> time_point_2 : TERM
    TERM activity(location=country::GB, time="2014", verb="vote_remain") -> activity_2 : TERM
    CLAIM statement(fact=activity_2) BY role_agent STATUS reported SOURCE "t2:s2" -> statement_2 : CLAIM
    TERM subject(kind="efforts", qualifier="independence") -> subject_3 : TERM
    CLAIM ongoing(target=subject_3) BY role_agent STATUS reported SOURCE "t2:s3" -> ongoing_3 : CLAIM
    CLAIM has_goal(goal=subject_2, subject="parties_and_individuals") BY role_agent STATUS reported SOURCE "t2:s3" -> has_goal_2 : CLAIM
    TERM time_horizon(horizon="future") -> time_horizon_2 : TERM
    TERM subject(kind="actions", qualifier="will_of_people_and_government") -> subject_4 : TERM
    CLAIM varies_with(condition=subject_4, target=subject_2) BY role_agent STATUS inferred SOURCE "t2:s4" -> varies_with_2 : CLAIM
    UTTER inform(target=controversial_2)
  }
  TURN t3 SPEAKER=USER {
    TERM time_point(date="2014") -> time_point_2 : TERM
    TERM subject(kind="referendum", location=country::GB, time="2014") -> subject_2 : TERM
    TERM property_question(property="margin", subject=subject_2) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
  TURN t4 SPEAKER=AGENT {
    TERM measure(amount=55.3, unit=unit_percent) -> measure_2 : TERM
    TERM rate(denominator=measure_2, numerator=measure_2) -> rate_2 : TERM
    TERM measure(amount=44.7, unit=unit_percent) -> measure_3 : TERM
    TERM rate(denominator=measure_3, numerator=measure_3) -> rate_3 : TERM
    CLAIM opposes(actor="majority_voters", subject="independence") BY role_agent STATUS reported SOURCE "t4:s1" -> opposes_2 : CLAIM
    TERM measure(amount=84.6, unit=unit_percent) -> measure_4 : TERM
    TERM group_size(count=3623344, group="valid_votes") -> group_size_2 : TERM
    CLAIM statement(fact=group_size_2) BY role_agent STATUS reported SOURCE "t4:s2" -> statement_2 : CLAIM
    TERM measure(amount=10.6, unit=unit_percent) -> measure_5 : TERM
    CLAIM statement(fact=measure_5) BY role_agent STATUS reported SOURCE "t4:s3" -> statement_3 : CLAIM
    TERM subject(kind="referendum_decision", time="2014") -> subject_2 : TERM
    CLAIM statement(fact=subject_2) BY role_agent STATUS reported SOURCE "t4:s4" -> statement_4 : CLAIM
    UTTER inform(target=statement_2)
  }
  TURN t5 SPEAKER=USER {
    TERM subject(kind="referendum_opportunity", location=country::GB, qualifier="scotland") -> subject_2 : TERM
    TERM property_question(property="timing", subject=subject_2) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
  TURN t6 SPEAKER=AGENT {
    TERM subject(kind="referendum_timing", location=country::GB) -> subject_2 : TERM
    CLAIM statement(fact=subject_2) BY role_agent STATUS asserted SOURCE "t6:s1" -> statement_2 : CLAIM
    TERM time_point(date="2017") -> time_point_2 : TERM
    TERM subject(kind="referendum_proposal", time="2017") -> subject_3 : TERM
    CLAIM opposes(actor="uk_government", subject=subject_3) BY role_agent STATUS reported SOURCE "t6:s2" -> opposes_2 : CLAIM
    CLAIM ongoing(target=subject_3) BY role_agent STATUS reported SOURCE "t6:s3" -> ongoing_2 : CLAIM
    TERM subject(kind="official_date", time="none") -> subject_4 : TERM
    CLAIM exists_in(location="calendar", subject=subject_4) BY role_agent STATUS reported SOURCE "t6:s3" -> exists_in_2 : CLAIM
    TERM subject(kind="legislation", qualifier="powers_transfer") -> subject_5 : TERM
    TERM subject(kind="autonomy", qualifier="greater_autonomy") -> subject_6 : TERM
    CLAIM enables(condition=subject_5, outcome=subject_6) BY role_agent STATUS reported SOURCE "t6:s4" -> enables_2 : CLAIM
    CLAIM leads_to(cause=subject_5, effect=subject_6) BY role_agent STATUS reported SOURCE "t6:s4" -> leads_to_2 : CLAIM
    TERM requirement(property="sustained_majority_support", value=TRUE) -> requirement_2 : TERM
    CLAIM statement(fact=requirement_2) BY role_agent STATUS reported SOURCE "t6:s5" -> statement_3 : CLAIM
    TERM decision(activity=subject_3) -> decision_2 : TERM
    CLAIM varies_with(condition="scottish_and_uk_governments", target=decision_2) BY role_agent STATUS reported SOURCE "t6:s6" -> varies_with_2 : CLAIM
    UTTER inform(target=statement_2)
  }
  TURN t7 SPEAKER=USER {
    TERM subject(kind="scottish_citizenship", qualifier="hypothetical") -> subject_2 : TERM
    TERM activity(actor=role_agent, location=country::GB, verb="vote_independence") -> activity_2 : TERM
    TERM decision(activity=activity_2) -> decision_2 : TERM
    TERM conditional(condition=subject_2, consequence=decision_2) -> conditional_2 : TERM
    UTTER ask(target=conditional_2)
  }
  TURN t8 SPEAKER=AGENT {
    UTTER apologize()
    TERM subject(kind="personal_opinions", qualifier="agent_beliefs") -> subject_2 : TERM
    TERM negation(target=subject_2) -> negation_2 : TERM
    CLAIM possesses(item=negation_2, subject=role_agent, value=FALSE) BY role_agent STATUS asserted SOURCE "t8:s1" -> possesses_2 : CLAIM
    TERM subject(kind="factual_information", qualifier="neutral") -> subject_3 : TERM
    CLAIM provides(actor=role_agent, subject=subject_3) BY role_agent STATUS asserted SOURCE "t8:s2" -> provides_2 : CLAIM
    CLAIM has_goal(goal=subject_3, subject=role_agent) BY role_agent STATUS asserted SOURCE "t8:s2" -> has_goal_2 : CLAIM
    TERM subject(kind="value_judgments_and_feelings", qualifier="agent") -> subject_4 : TERM
    TERM negation(target=subject_4) -> negation_3 : TERM
    CLAIM possesses(item=negation_3, subject=role_agent, value=FALSE) BY role_agent STATUS asserted SOURCE "t8:s3" -> possesses_3 : CLAIM
    CLAIM designed_to_be(quality="neutral_factual_assistant", subject=role_agent) BY role_agent STATUS asserted SOURCE "t8:s4" -> designed_to_be_2 : CLAIM
    TERM decision(activity=subject_2) -> decision_2 : TERM
    UTTER decline(target=decision_2)
    CLAIM statement(fact=decision_2) BY role_agent STATUS asserted SOURCE "t8:s5" -> statement_2 : CLAIM
    LINK supports(conclusion=statement_2, premise=possesses_2) SOURCE "t8:s5"
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, property_question, subject, country::GB | covered |
| n2 | object | subject, country::GB | covered |
| n3 | object | subject | covered |
| n4 | claim | controversial, ongoing, subject, country::GB | covered |
| n5 | claim | statement, activity, country::GB, time_point | covered |
| n6 | object | country::GB | covered |
| n7 | temporal | time_point | covered |
| n8 | claim | ongoing, has_goal, subject | covered |
| n9 | claim | varies_with, time_horizon, subject | covered |
| n10 | speech_act | ask, property_question, subject, time_point, country::GB | covered |
| n11 | object | subject, time_point, country::GB | covered |
| n12 | claim | opposes, measure, rate, unit_percent | covered |
| n13 | claim | statement, measure, rate, unit_percent, group_size | covered |
| n14 | claim | statement, measure, unit_percent | covered |
| n15 | claim | statement, subject | covered |
| n16 | speech_act | ask, property_question, subject, country::GB | covered |
| n17 | claim | statement, subject, country::GB | covered |
| n18 | claim | opposes, subject, time_point | covered |
| n19 | temporal | time_point | covered |
| n20 | claim | ongoing, exists_in, subject | covered |
| n21 | claim | enables, leads_to, subject | covered |
| n22 | claim | statement, requirement | covered |
| n23 | claim | varies_with, decision, subject | covered |
| n24 | speech_act | ask, conditional, decision, activity, subject, country::GB, role_agent | covered |
| n25 | negation | negation, possesses, subject, role_agent | covered |
| n26 | claim | provides, has_goal, designed_to_be, subject, role_agent | covered |
| n27 | negation | negation, possesses, subject, role_agent | covered |
| n28 | speech_act | decline, apologize, decision, subject | covered |
| n29 | reasoning | supports, possesses, statement, negation, role_agent | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every turn and clause across t1:s1–t8:s5 is represented.
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: passed `rag check` validation
