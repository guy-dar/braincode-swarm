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
    TERM interpersonal_stance(target=t1.subject_2, actor=role_adults, stance="commitment") -> interpersonal_stance_2 : TERM
    CLAIM important(target=interpersonal_stance_2) BY role_agent STATUS asserted SOURCE "t2:s1" -> important_2 : CLAIM
    CLAIM varies_with(target=important_2, condition=personal_values) BY role_agent STATUS asserted SOURCE "t2:s2" -> varies_with_2 : CLAIM
    LINK contrast(first=important_2, second=varies_with_2) SOURCE "t2:s2"
    TERM subject(kind="lifestyle_choices") -> subject_2 : TERM
    TERM subject(kind="fulfillment") -> subject_3 : TERM
    CLAIM enables(condition=subject_2, outcome=subject_3) BY role_agent STATUS asserted SOURCE "t2:s3" -> enables_2 : CLAIM
  }
  TURN t3 SPEAKER=USER {
    TERM property_question(property="partner_type", subject=t1.subject_2) -> property_question_2 : TERM
    UTTER ask(target=property_question_2, recipient=role_agent)
  }
  TURN t4 SPEAKER=AGENT {
    TERM gender_identity(identity="any") -> gender_identity_2 : TERM
    TERM interpersonal_stance(target=gender_identity_2, actor=role_adults, stance="romantic_partner") -> interpersonal_stance_2 : TERM
    CLAIM involves(target=interpersonal_stance_2, subject=t2.important_2) BY role_agent STATUS asserted SOURCE "t4:s1" -> involves_2 : CLAIM
    CLAIM designed_to_be(quality="inclusive", subject=role_agent) BY role_agent STATUS asserted SOURCE "t4:s2" -> designed_to_be_2 : CLAIM
  }
  TURN t5 SPEAKER=USER {
    TERM property_question(property="outdated", subject=t1.subject_2) -> property_question_2 : TERM
    UTTER ask(target=property_question_2, recipient=role_agent)
  }
  TURN t6 SPEAKER=AGENT {
    TERM subject(kind="opinion", qualifier=personal_values) -> subject_2 : TERM
    CLAIM possesses(item=subject_2, subject=role_agent, value=FALSE) BY role_agent STATUS asserted SOURCE "t6:s1" -> possesses_2 : CLAIM
    CLAIM controversial(subject=t1.subject_2) BY role_agent STATUS asserted SOURCE "t6:s2" -> controversial_2 : CLAIM
    CLAIM argues_for(subject=role_adults, value=t1.subject_2) BY role_agent STATUS asserted SOURCE "t6:s2" -> argues_for_2 : CLAIM
    CLAIM attitude(target=t1.subject_2, holder=role_adults, type="values_commitment") BY role_agent STATUS reported SOURCE "t6:s3" -> attitude_2 : CLAIM
    CLAIM attitude(target=t1.subject_2, holder=role_adults, type="less_relevant") BY role_agent STATUS reported SOURCE "t6:s3" -> attitude_3 : CLAIM
    LINK contrast(first=attitude_2, second=attitude_3) SOURCE "t6:s3"
    TERM temporal_context(activity="evolved", period="over_time") -> temporal_context_2 : TERM
    CLAIM ongoing(target=temporal_context_2) BY role_agent STATUS asserted SOURCE "t6:s4" -> ongoing_2 : CLAIM
    CLAIM important(target=t1.subject_2) BY role_agent STATUS hypothesized SOURCE "t6:s5" -> important_2 : CLAIM
    CLAIM controversial(subject=important_2) BY role_agent STATUS asserted SOURCE "t6:s5" -> controversial_3 : CLAIM
  }
  TURN t7 SPEAKER=AGENT {
    TERM subject(kind="opinion", qualifier=personal_values) -> subject_2 : TERM
    CLAIM possesses(item=subject_2, subject=role_agent, value=FALSE) BY role_agent STATUS asserted SOURCE "t7:s1" -> possesses_2 : CLAIM
    CLAIM controversial(subject=t1.subject_2) BY role_agent STATUS asserted SOURCE "t7:s2" -> controversial_2 : CLAIM
    CLAIM argues_for(subject=role_adults, value=t1.subject_2) BY role_agent STATUS asserted SOURCE "t7:s2" -> argues_for_2 : CLAIM
    CLAIM attitude(target=t1.subject_2, holder=role_adults, type="values_commitment") BY role_agent STATUS reported SOURCE "t7:s3" -> attitude_2 : CLAIM
    CLAIM attitude(target=t1.subject_2, holder=role_adults, type="less_relevant") BY role_agent STATUS reported SOURCE "t7:s3" -> attitude_3 : CLAIM
    LINK contrast(first=attitude_2, second=attitude_3) SOURCE "t7:s3"
    TERM temporal_context(activity="evolved", period="over_time") -> temporal_context_2 : TERM
    CLAIM ongoing(target=temporal_context_2) BY role_agent STATUS asserted SOURCE "t7:s4" -> ongoing_2 : CLAIM
    CLAIM important(target=t1.subject_2) BY role_agent STATUS hypothesized SOURCE "t7:s5" -> important_2 : CLAIM
    CLAIM controversial(subject=important_2) BY role_agent STATUS asserted SOURCE "t7:s5" -> controversial_3 : CLAIM
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, property_question, role_agent | covered |
| n2 | object | subject | covered |
| n3 | claim | important, interpersonal_stance, role_adults | covered |
| n4 | claim | varies_with, personal_values, contrast | covered |
| n5 | claim | enables, subject | covered |
| n6 | speech_act | ask, property_question, role_agent | covered |
| n7 | claim | involves, gender_identity, interpersonal_stance, role_adults | covered |
| n8 | claim | designed_to_be, role_agent | covered |
| n9 | speech_act | ask, property_question, role_agent | covered |
| n10 | negation | possesses, subject, personal_values, role_agent | covered |
| n11 | claim | controversial, argues_for, role_adults | covered |
| n12 | claim | attitude, role_adults, contrast | covered |
| n13 | claim | temporal_context, ongoing | covered |
| n14 | claim | important, controversial | covered |
| n15 | negation | possesses, subject, personal_values, role_agent | covered |
| n16 | claim | controversial, argues_for, role_adults | covered |
| n17 | claim | attitude, role_adults, contrast | covered |
| n18 | claim | temporal_context, ongoing | covered |
| n19 | claim | important, controversial | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t7:s5 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
