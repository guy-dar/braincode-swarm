Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(actor="user", location=country::DE, verb="research") -> activity_2 : TERM
    CLAIM ongoing(target=activity_2) BY role_user STATUS asserted SOURCE "t1:s1" -> ongoing_2 : CLAIM
    TERM time_point(date="end of August") -> time_point_2 : TERM
    TERM subject(kind="visa", location=country::DE, time="end of August") -> subject_2 : TERM
    CLAIM has_state(state="valid", subject=subject_2) BY role_user STATUS asserted SOURCE "t1:s1" -> has_state_2 : CLAIM
    TERM activity(actor="Hagen University", object="stay", verb="extend") -> activity_3 : TERM
    CLAIM ongoing(target=activity_3) BY role_user STATUS asserted SOURCE "t1:s2" -> ongoing_3 : CLAIM
    TERM activity(actor="user", object="visa extension", verb="apply") -> activity_4 : TERM
    TERM subject(kind="user", location=country::IR, time="end of August") -> subject_3 : TERM
    CLAIM has_state(state="present", subject=subject_3) BY role_user STATUS asserted SOURCE "t1:s3" -> has_state_3 : CLAIM
    TERM subject(kind="embassy", location=country::IR, qualifier=locale_de) -> subject_4 : TERM
    TERM activity(actor="user", location=country::IR, object="visa extension", verb="obtain") -> activity_5 : TERM
    UTTER ask(target=activity_5)
  }
  TURN t2 SPEAKER=AGENT {
    TERM subject(kind="immigration_policies", qualifier="latest") -> subject_5 : TERM
    TERM negation(target=subject_5) -> negation_2 : TERM
    CLAIM has_state(state="not_updated", subject=subject_5) BY role_agent STATUS asserted SOURCE "t2:s1" -> has_state_4 : CLAIM
    TERM activity(actor="user", location=country::IR, object="details", verb="contact") -> activity_6 : TERM
    UTTER propose(target=activity_6)
    TERM activity(actor="user", object="visa extension", verb="apply_early") -> activity_7 : TERM
    CLAIM recommended(target=activity_7) BY role_agent STATUS asserted SOURCE "t2:s3" -> recommended_2 : CLAIM
    TERM subject(kind="legal_transition", qualifier="smooth") -> subject_6 : TERM
    CLAIM enables(condition=activity_7, outcome=subject_6) BY role_agent STATUS inferred SOURCE "t2:s3" -> enables_2 : CLAIM
    LINK supports(conclusion=recommended_2, premise=enables_2) SOURCE "t2:s3"
    TERM well_wishes(recipient=role_user, sentiment="good luck") -> well_wishes_2 : TERM
    UTTER respond(target=well_wishes_2)
  }
  TURN t3 SPEAKER=USER {
    TERM activity(actor="user", object="text", verb="edit") -> activity_8 : TERM
    UTTER ask(target=activity_8)
  }
  TURN t4 SPEAKER=AGENT {
    TERM activity(actor="agent", object="visa extension inquiry", verb="edit") -> activity_9 : TERM
    UTTER respond(target=activity_9)
  }
  TURN t5 SPEAKER=USER {
    TERM activity(actor="user", object="text", verb="rewrite") -> activity_10 : TERM
    UTTER ask(target=activity_10)
  }
  TURN t6 SPEAKER=AGENT {
    TERM activity(actor="agent", object="visa extension inquiry", verb="rewrite") -> activity_11 : TERM
    UTTER respond(target=activity_11)
  }
  TURN t7 SPEAKER=USER {
    TERM activity(actor="user", object="text", verb="rewrite") -> activity_12 : TERM
    UTTER ask(target=activity_12)
  }
  TURN t8 SPEAKER=AGENT {
    TERM activity(actor="agent", object="visa extension inquiry", verb="rewrite") -> activity_13 : TERM
    UTTER respond(target=activity_13)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | activity | covered |
| n2 | claim | ongoing, activity, country::DE | covered |
| n3 | object | country::DE | covered |
| n4 | claim | has_state, subject | covered |
| n5 | temporal | time_point | covered |
| n6 | claim | ongoing, activity | covered |
| n7 | action | activity | covered |
| n8 | claim | has_state, subject, country::IR | covered |
| n9 | object | country::IR | covered |
| n10 | speech_act | ask, activity | covered |
| n11 | object | subject, locale_de, country::IR | covered |
| n12 | negation | negation, has_state | covered |
| n13 | speech_act | propose, activity | covered |
| n14 | speech_act | recommended | covered |
| n15 | reasoning | enables, supports | covered |
| n16 | speech_act | well_wishes, respond | covered |
| n17 | action | activity, ask | covered |
| n18 | speech_act | respond, activity | covered |
| n19 | action | activity, ask | covered |
| n20 | speech_act | respond, activity | covered |
| n21 | action | activity, ask | covered |
| n22 | speech_act | respond, activity | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t8:s4 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
