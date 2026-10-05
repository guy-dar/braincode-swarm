Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="marriage") -> subject_2 : TERM
    TERM property_question(property="importance", subject=subject_2) -> property_question_2 : TERM
    UTTER ask(target=property_question_2, recipient=role_agent)
  }
  TURN t2 SPEAKER=AGENT {
    TERM interpersonal_stance(target=t1.subject_2, actor="partners", stance="commitment") -> interpersonal_stance_2 : TERM
    CLAIM important(target=interpersonal_stance_2) BY role_agent STATUS asserted SOURCE "t2:s1" -> important_2 : CLAIM
    CLAIM varies_with(target=important_2, condition=personal_values) BY role_agent STATUS asserted SOURCE "t2:s2" -> varies_with_2 : CLAIM
    LINK contrast(first=important_2, second=varies_with_2) SOURCE "t2:s2"
    TERM subject(kind="paths_to_fulfillment") -> subject_3 : TERM
    TERM subject(kind="happiness") -> subject_4 : TERM
    CLAIM enables(condition=subject_3, outcome=subject_4) BY role_agent STATUS asserted SOURCE "t2:s3" -> enables_2 : CLAIM
  }
  TURN t3 SPEAKER=USER {
    TERM property_question(property="partner_types", subject=t1.subject_2) -> property_question_3 : TERM
    UTTER ask(target=property_question_3, recipient=role_agent)
  }
  TURN t4 SPEAKER=AGENT {
    TERM gender_identity(identity="diverse_genders") -> gender_identity_2 : TERM
    TERM interpersonal_stance(target=gender_identity_2, actor="romantic_partner", stance="romantic_partner") -> interpersonal_stance_3 : TERM
    CLAIM attribute_claim(property="inclusive", subject=interpersonal_stance_3, value=TRUE) BY role_agent STATUS asserted SOURCE "t4:s1" -> attribute_claim_2 : CLAIM
    CLAIM designed_to_be(quality="inclusive", subject=role_agent) BY role_agent STATUS asserted SOURCE "t4:s2" -> designed_to_be_2 : CLAIM
  }
  TURN t5 SPEAKER=USER {
    TERM property_question(property="outdated", subject=t1.subject_2) -> property_question_4 : TERM
    UTTER ask(target=property_question_4, recipient=role_agent)
  }
  TURN t6 SPEAKER=AGENT {
    CLAIM unaware(person=role_agent, topic=personal_values) BY role_agent STATUS asserted SOURCE "t6:s1" -> unaware_2 : CLAIM
    CLAIM controversial(subject=t1.subject_2) BY role_agent STATUS asserted SOURCE "t6:s2" -> controversial_2 : CLAIM
    CLAIM argues_for(subject="proponents", value=t1.subject_2) BY role_agent STATUS reported SOURCE "t6:s2" -> argues_for_2 : CLAIM
    CLAIM attitude(target=t1.subject_2, holder="many", type="commitment") BY role_agent STATUS reported SOURCE "t6:s3" -> attitude_2 : CLAIM
    CLAIM attitude(target=t1.subject_2, holder="others", type="less_relevant") BY role_agent STATUS reported SOURCE "t6:s3" -> attitude_3 : CLAIM
    LINK contrast(first=attitude_2, second=attitude_3) SOURCE "t6:s3"
    TERM temporal_context(activity="evolution", period="history") -> temporal_context_2 : TERM
    CLAIM ongoing(target=temporal_context_2) BY role_agent STATUS asserted SOURCE "t6:s4" -> ongoing_2 : CLAIM
    CLAIM perceived_as(concept="necessity", subject=t1.subject_2) BY role_agent STATUS reported SOURCE "t6:s5" -> perceived_as_2 : CLAIM
    CLAIM important(target=t1.subject_2) BY role_agent STATUS hypothesized SOURCE "t6:s5" -> important_3 : CLAIM
  }
  TURN t7 SPEAKER=AGENT {
    CLAIM unaware(person=role_agent, topic=personal_values) BY role_agent STATUS asserted SOURCE "t7:s1" -> unaware_3 : CLAIM
    CLAIM controversial(subject=t1.subject_2) BY role_agent STATUS asserted SOURCE "t7:s2" -> controversial_3 : CLAIM
    CLAIM argues_for(subject="proponents", value=t1.subject_2) BY role_agent STATUS reported SOURCE "t7:s2" -> argues_for_3 : CLAIM
    CLAIM attitude(target=t1.subject_2, holder="many", type="commitment") BY role_agent STATUS reported SOURCE "t7:s3" -> attitude_4 : CLAIM
    CLAIM attitude(target=t1.subject_2, holder="others", type="less_relevant") BY role_agent STATUS reported SOURCE "t7:s3" -> attitude_5 : CLAIM
    LINK contrast(first=attitude_4, second=attitude_5) SOURCE "t7:s3"
    TERM temporal_context(activity="evolution", period="history") -> temporal_context_3 : TERM
    CLAIM ongoing(target=temporal_context_3) BY role_agent STATUS asserted SOURCE "t7:s4" -> ongoing_3 : CLAIM
    CLAIM perceived_as(concept="necessity", subject=t1.subject_2) BY role_agent STATUS reported SOURCE "t7:s5" -> perceived_as_3 : CLAIM
    CLAIM important(target=t1.subject_2) BY role_agent STATUS hypothesized SOURCE "t7:s5" -> important_4 : CLAIM
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, role_agent, property_question, subject | covered |
| n2 | object | subject | covered |
| n3 | claim | interpersonal_stance, important | covered |
| n4 | claim | varies_with, personal_values, contrast | covered |
| n5 | claim | enables, subject | covered |
| n6 | speech_act | ask, role_agent, property_question | covered |
| n7 | claim | gender_identity, interpersonal_stance, attribute_claim | covered |
| n8 | claim | designed_to_be | covered |
| n9 | speech_act | ask, role_agent, property_question | covered |
| n10 | negation | unaware, role_agent, personal_values | covered |
| n11 | claim | controversial, argues_for | covered |
| n12 | claim | attitude, contrast | covered |
| n13 | claim | temporal_context, ongoing | covered |
| n14 | claim | perceived_as, important | covered |
| n15 | negation | unaware, role_agent, personal_values | covered |
| n16 | claim | controversial, argues_for | covered |
| n17 | claim | attitude, contrast | covered |
| n18 | claim | temporal_context, ongoing | covered |
| n19 | claim | perceived_as, important | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t7:s5 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: rag check reported 0 unresolved needs and 0 unknown symbols
