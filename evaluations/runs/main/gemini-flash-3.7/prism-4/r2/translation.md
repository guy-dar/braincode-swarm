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
    TERM interpersonal_stance(target="partner", actor="individual", stance="commitment") -> interpersonal_stance_2 : TERM
    CLAIM important(target=t1.subject_2) BY role_agent STATUS asserted SOURCE "t2:s1" -> important_2 : CLAIM
    CLAIM varies_with(target=t1.subject_2, condition=personal_values) BY role_agent STATUS asserted SOURCE "t2:s2" -> varies_with_2 : CLAIM
    LINK contrast(first=important_2, second=varies_with_2) SOURCE "t2:s2"
    TERM subject(kind="happiness") -> subject_3 : TERM
    CLAIM enables(condition=t1.subject_2, outcome=subject_3) BY role_agent STATUS asserted SOURCE "t2:s3" -> enables_2 : CLAIM
  }
  TURN t3 SPEAKER=USER {
    TERM property_question(property="type", subject=t2.interpersonal_stance_2) -> property_question_3 : TERM
    UTTER ask(target=property_question_3, recipient=role_agent)
  }
  TURN t4 SPEAKER=AGENT {
    TERM gender_identity(identity="diverse") -> gender_identity_2 : TERM
    TERM interpersonal_stance(target="partner", actor="individual", stance="romantic") -> interpersonal_stance_3 : TERM
    CLAIM attribute_claim(property="partner_type", subject=interpersonal_stance_3, value=gender_identity_2) BY role_agent STATUS asserted SOURCE "t4:s1" -> attribute_claim_2 : CLAIM
    CLAIM designed_to_be(quality="inclusive", subject=t1.subject_2) BY role_agent STATUS asserted SOURCE "t4:s2" -> designed_to_be_2 : CLAIM
  }
  TURN t5 SPEAKER=USER {
    TERM property_question(property="outdated", subject=t1.subject_2) -> property_question_4 : TERM
    UTTER ask(target=property_question_4, recipient=role_agent)
  }
  TURN t6 SPEAKER=AGENT {
    CLAIM unaware(person=role_agent, topic=personal_values) BY role_agent STATUS asserted SOURCE "t6:s1" -> unaware_2 : CLAIM
    CLAIM controversial(subject=t1.subject_2) BY role_agent STATUS asserted SOURCE "t6:s2" -> controversial_2 : CLAIM
    CLAIM argues_for(subject="individual", value=personal_values) BY role_agent STATUS asserted SOURCE "t6:s3" -> argues_for_2 : CLAIM
    CLAIM ongoing(target=t1.subject_2) BY role_agent STATUS asserted SOURCE "t6:s4" -> ongoing_2 : CLAIM
    CLAIM important(target=t1.subject_2) BY role_agent STATUS asserted SOURCE "t6:s5" -> important_3 : CLAIM
  }
  TURN t7 SPEAKER=AGENT {
    CLAIM unaware(person=role_agent, topic=personal_values) BY role_agent STATUS asserted SOURCE "t7:s1" -> unaware_3 : CLAIM
    CLAIM controversial(subject=t1.subject_2) BY role_agent STATUS asserted SOURCE "t7:s2" -> controversial_3 : CLAIM
    CLAIM argues_for(subject="individual", value=personal_values) BY role_agent STATUS asserted SOURCE "t7:s3" -> argues_for_3 : CLAIM
    CLAIM ongoing(target=t1.subject_2) BY role_agent STATUS asserted SOURCE "t7:s4" -> ongoing_3 : CLAIM
    CLAIM important(target=t1.subject_2) BY role_agent STATUS asserted SOURCE "t7:s5" -> important_4 : CLAIM
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, role_agent, property_question, subject | covered |
| n2 | object | subject, property_question | covered |
| n3 | claim | important, interpersonal_stance, role_agent | covered |
| n4 | claim | varies_with, personal_values, contrast, role_agent | covered |
| n5 | claim | enables, subject, role_agent | covered |
| n6 | speech_act | ask, role_agent, property_question, interpersonal_stance | covered |
| n7 | claim | attribute_claim, gender_identity, interpersonal_stance, role_agent | covered |
| n8 | claim | designed_to_be, role_agent | covered |
| n9 | speech_act | ask, role_agent, property_question | covered |
| n10 | negation | unaware, role_agent, personal_values | covered |
| n11 | claim | controversial, role_agent | covered |
| n12 | claim | argues_for, personal_values, role_agent | covered |
| n13 | claim | ongoing, role_agent | covered |
| n14 | claim | important, role_agent | covered |
| n15 | negation | unaware, role_agent, personal_values | covered |
| n16 | claim | controversial, role_agent | covered |
| n17 | claim | argues_for, personal_values, role_agent | covered |
| n18 | claim | ongoing, role_agent | covered |
| n19 | claim | important, role_agent | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t7:s5 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
