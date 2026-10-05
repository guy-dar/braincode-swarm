Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="independence", location=united_kingdom, qualifier="Scotland") -> subject_2 : TERM
    TERM property_question(property="sovereignty", subject=subject_2) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
  TURN t2 SPEAKER=AGENT {
    CLAIM controversial(subject="Scotland independence") BY role_agent STATUS asserted SOURCE "t2:s1" -> controversial_2 : CLAIM
    TERM time_point(date="2014") -> time_point_2 : TERM
    TERM subject(kind="referendum", location=united_kingdom, time="2014") -> subject_3 : TERM
    CLAIM statement(fact=subject_3) BY role_agent STATUS asserted SOURCE "t2:s2" -> statement_2 : CLAIM
    TERM activity(actor="parties_and_individuals", purpose=subject_3, verb="achieve_independence") -> activity_2 : TERM
    CLAIM ongoing(target=activity_2) BY role_agent STATUS asserted SOURCE "t2:s3" -> ongoing_2 : CLAIM
    CLAIM varies_with(condition="will_of_people_and_government_actions", target=statement_2) BY role_agent STATUS asserted SOURCE "t2:s4" -> varies_with_2 : CLAIM
  }
  TURN t3 SPEAKER=USER {
    TERM property_question(property="closeness", subject=t2.subject_3) -> property_question_3 : TERM
    UTTER ask(target=property_question_3)
  }
  TURN t4 SPEAKER=AGENT {
    TERM measure(amount=55.3, unit=unit_percent) -> measure_2 : TERM
    CLAIM opposes(actor="voters", subject="independence") BY role_agent STATUS reported SOURCE "t4:s1" -> opposes_2 : CLAIM
    TERM measure(amount=44.7, unit=unit_percent) -> measure_3 : TERM
    TERM measure(amount=84.6, unit=unit_percent) -> measure_4 : TERM
    TERM group_size(count=3623344, group="valid_votes") -> group_size_2 : TERM
    CLAIM statement(fact=group_size_2) BY role_agent STATUS reported SOURCE "t4:s2" -> statement_3 : CLAIM
    TERM measure(amount=10.6, unit=unit_percent) -> measure_5 : TERM
    CLAIM attribute_claim(property="margin", subject=t2.subject_3, value=measure_5) BY role_agent STATUS asserted SOURCE "t4:s3" -> attribute_claim_2 : CLAIM
    CLAIM statement(fact=t2.subject_3) BY role_agent STATUS asserted SOURCE "t4:s4" -> statement_4 : CLAIM
  }
  TURN t5 SPEAKER=USER {
    TERM property_question(property="next_referendum_timing", subject=t1.subject_2) -> property_question_4 : TERM
    UTTER ask(target=property_question_4)
  }
  TURN t6 SPEAKER=AGENT {
    CLAIM controversial(subject="next_referendum_timing") BY role_agent STATUS asserted SOURCE "t6:s1" -> controversial_3 : CLAIM
    TERM time_point(date="2017") -> time_point_3 : TERM
    CLAIM opposes(actor="UK_government", subject="2017_SNP_referendum_proposal") BY role_agent STATUS reported SOURCE "t6:s2" -> opposes_3 : CLAIM
    TERM activity(actor="SNP", verb="call_for_referendum") -> activity_3 : TERM
    CLAIM ongoing(target=activity_3) BY role_agent STATUS asserted SOURCE "t6:s3" -> ongoing_3 : CLAIM
    CLAIM provides(actor="Scottish_government", subject="powers_transfer_bill") BY role_agent STATUS reported SOURCE "t6:s4" -> provides_2 : CLAIM
    CLAIM attribute_claim(property="sustained_majority_support_requirement", subject="UK_government", value=TRUE) BY role_agent STATUS asserted SOURCE "t6:s5" -> attribute_claim_3 : CLAIM
    CLAIM attribute_claim(property="decision_power", subject="Scottish_and_UK_governments", value="referendum") BY role_agent STATUS asserted SOURCE "t6:s6" -> attribute_claim_4 : CLAIM
  }
  TURN t7 SPEAKER=USER {
    TERM property_question(property="personal_vote", subject=role_agent) -> property_question_5 : TERM
    UTTER ask(target=property_question_5)
  }
  TURN t8 SPEAKER=AGENT {
    UTTER apologize()
    TERM subject(kind="personal_opinions_and_beliefs", qualifier=beliefs) -> subject_4 : TERM
    CLAIM possesses(item=subject_4, subject=role_agent, value=FALSE) BY role_agent STATUS asserted SOURCE "t8:s1" -> possesses_2 : CLAIM
    CLAIM designed_to_be(quality="neutral_factual_provider", subject=role_agent) BY role_agent STATUS asserted SOURCE "t8:s2" -> designed_to_be_2 : CLAIM
    TERM subject(kind="value_judgments_and_feelings", qualifier=personal_values) -> subject_5 : TERM
    CLAIM possesses(item=subject_5, subject=role_agent, value=FALSE) BY role_agent STATUS asserted SOURCE "t8:s3" -> possesses_3 : CLAIM
    CLAIM designed_to_be(quality="neutral_assistant", subject=role_agent) BY role_agent STATUS asserted SOURCE "t8:s4" -> designed_to_be_3 : CLAIM
    UTTER decline(target=property_question_5)
    LINK supports(conclusion=possesses_2, premise=possesses_3) SOURCE "t8:s5"
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, property_question, united_kingdom | covered |
| n2 | object | subject, united_kingdom | covered |
| n3 | object | subject, united_kingdom | covered |
| n4 | claim | controversial | covered |
| n5 | claim | statement, subject, united_kingdom | covered |
| n6 | object | united_kingdom | covered |
| n7 | temporal | time_point | not-applicable |
| n8 | claim | ongoing, activity | covered |
| n9 | claim | varies_with | covered |
| n10 | speech_act | ask, property_question | covered |
| n11 | object | subject | covered |
| n12 | claim | opposes, measure, unit_percent | covered |
| n13 | claim | statement, group_size, measure, unit_percent | covered |
| n14 | claim | attribute_claim, measure, unit_percent | covered |
| n15 | claim | statement | covered |
| n16 | speech_act | ask, property_question | covered |
| n17 | claim | controversial | covered |
| n18 | claim | opposes | covered |
| n19 | temporal | time_point | covered |
| n20 | claim | ongoing, activity | covered |
| n21 | claim | provides | covered |
| n22 | claim | attribute_claim | covered |
| n23 | claim | attribute_claim | covered |
| n24 | speech_act | ask, property_question, role_agent | covered |
| n25 | negation | possesses, beliefs | covered |
| n26 | claim | designed_to_be | covered |
| n27 | negation | possesses, personal_values | covered |
| n28 | speech_act | decline, apologize | covered |
| n29 | reasoning | supports, possesses | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t8:s5 is represented.
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Justification for not-applicable: n7 is the temporal qualification "in 2014" on the 2014 referendum event in t2:s2, which is structurally represented via `time_point(date="2014")` and `subject(..., time="2014")`. Because the candidate list for n7 contained duration units (unit_year, unit_month) rather than a direct timestamp match, the need is structurally captured by the date attribute on time_point and subject.
- Check: `rag check` verified 0 unresolved needs and 0 unknown symbols
