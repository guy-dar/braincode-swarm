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
    UTTER ask(target=property_question_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM interpersonal_stance(actor="partner", stance="commitment") -> interpersonal_stance_2 : TERM
    CLAIM important(target=interpersonal_stance_2) BY role_agent STATUS inferred SOURCE "t2:s1" -> important_2 : CLAIM
    CLAIM varies_with(target=important_2, condition="circumstances") BY role_agent STATUS inferred SOURCE "t2:s2" -> varies_with_2 : CLAIM
    LINK contrast(first=important_2, second=varies_with_2) SOURCE "t2:s2"
    CLAIM meets_needs(beneficiary="individuals", subject=t1.subject_2) BY role_agent STATUS inferred SOURCE "t2:s3" -> meets_needs_2 : CLAIM
  }
  TURN t3 SPEAKER=USER {
    TERM property_question(property="partner_type", subject=t1.subject_2) -> property_question_3 : TERM
    UTTER ask(target=property_question_3)
  }
  TURN t4 SPEAKER=AGENT {
    TERM gender_identity(identity="diverse") -> gender_identity_2 : TERM
    TERM interpersonal_stance(target=gender_identity_2, actor="romantic_partner", stance="marriage") -> interpersonal_stance_3 : TERM
    CLAIM involves(target=interpersonal_stance_3, subject=t2.important_2) BY role_agent STATUS asserted SOURCE "t4:s1" -> involves_2 : CLAIM
    CLAIM designed_to_be(quality="inclusive", subject=role_agent) BY role_agent STATUS asserted SOURCE "t4:s2" -> designed_to_be_2 : CLAIM
  }
  TURN t5 SPEAKER=USER {
    TERM property_question(property="outdated", subject=t1.subject_2) -> property_question_4 : TERM
    UTTER ask(target=property_question_4)
  }
  TURN t6 SPEAKER=AGENT {
    CLAIM unaware(person=role_agent, topic=t5.property_question_4) BY role_agent STATUS asserted SOURCE "t6:s1" -> unaware_2 : CLAIM
    CLAIM controversial(subject=t1.subject_2) BY role_agent STATUS asserted SOURCE "t6:s2" -> controversial_2 : CLAIM
    CLAIM argues_for(subject="traditional_view", value="commitment") BY role_agent STATUS reported SOURCE "t6:s3" -> argues_for_2 : CLAIM
    CLAIM ongoing(target=t1.subject_2) BY role_agent STATUS reported SOURCE "t6:s4" -> ongoing_2 : CLAIM
    CLAIM important(target=t1.subject_2) BY role_agent STATUS reported SOURCE "t6:s5" -> important_3 : CLAIM
  }
  TURN t7 SPEAKER=AGENT {
    CLAIM unaware(person=role_agent, topic=t5.property_question_4) BY role_agent STATUS asserted SOURCE "t7:s1" -> unaware_3 : CLAIM
    CLAIM controversial(subject=t1.subject_2) BY role_agent STATUS asserted SOURCE "t7:s2" -> controversial_3 : CLAIM
    CLAIM argues_for(subject="traditional_view", value="commitment") BY role_agent STATUS reported SOURCE "t7:s3" -> argues_for_3 : CLAIM
    CLAIM ongoing(target=t1.subject_2) BY role_agent STATUS reported SOURCE "t7:s4" -> ongoing_3 : CLAIM
    CLAIM important(target=t1.subject_2) BY role_agent STATUS reported SOURCE "t7:s5" -> important_4 : CLAIM
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, property_question, subject | covered |
| n2 | object | property_question, subject | covered |
| n3 | claim | important, interpersonal_stance | covered |
| n4 | claim | contrast, varies_with | covered |
| n5 | claim | meets_needs | covered |
| n6 | speech_act | ask, property_question | covered |
| n7 | claim | gender_identity, interpersonal_stance, involves | covered |
| n8 | claim | designed_to_be | covered |
| n9 | speech_act | ask, property_question | covered |
| n10 | negation | unaware | covered |
| n11 | claim | controversial | covered |
| n12 | claim | argues_for | covered |
| n13 | claim | ongoing | covered |
| n14 | claim | important | covered |
| n15 | negation | unaware | covered |
| n16 | claim | controversial | covered |
| n17 | claim | argues_for | covered |
| n18 | claim | ongoing | covered |
| n19 | claim | important | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t7:s5 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
