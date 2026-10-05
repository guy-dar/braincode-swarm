Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(object="passage", verb="edit") -> activity_2 : TERM
    CLAIM role(role_type="visiting_researcher", subject=role_user) BY role_user STATUS asserted SOURCE "t1:s1" -> role_2 : CLAIM
    TERM subject(kind="visiting_researcher", location=country::DE, qualifier="Hagen University") -> subject_2 : TERM
    TERM time_point(date="August", time="end") -> time_point_2 : TERM
    CLAIM has_state(state="valid", subject=subject_2) BY role_user STATUS asserted SOURCE "t1:s1" -> has_state_2 : CLAIM
    CLAIM provides(actor="Hagen University", subject="stay_extension") BY role_user STATUS asserted SOURCE "t1:s2" -> provides_2 : CLAIM
    TERM activity(object="visa_extension", verb="apply") -> activity_3 : TERM
    CLAIM exists_in(location=country::IR, subject=role_user) BY role_user STATUS asserted SOURCE "t1:s3" -> exists_in_2 : CLAIM
    TERM subject(kind="embassy", location=country::IR, qualifier="German Embassy in Tehran") -> subject_3 : TERM
    TERM activity(location=country::IR, object="visa_extension", verb="extend_visa") -> activity_4 : TERM
    UTTER ask(target=activity_4)
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM subject(kind="immigration_policy_updates", qualifier="latest") -> subject_4 : TERM
    CLAIM possesses(item=subject_4, subject=role_agent, value=FALSE) BY role_agent STATUS asserted SOURCE "t2:s1" -> possesses_2 : CLAIM
    UTTER inform(target=possesses_2)
    TERM activity(object="German Embassy in Tehran", verb="contact") -> activity_5 : TERM
    CLAIM recommended(target=activity_5) BY role_agent STATUS asserted SOURCE "t2:s2" -> recommended_2 : CLAIM
    UTTER propose(target=activity_5)
    TERM activity(object="visa_extension", verb="apply_early") -> activity_6 : TERM
    CLAIM recommended(target=activity_6) BY role_agent STATUS asserted SOURCE "t2:s3" -> recommended_3 : CLAIM
    TERM subject(kind="outcome", qualifier="avoid_legal_implications_and_smooth_transition") -> subject_5 : TERM
    CLAIM enables(condition=activity_6, outcome=subject_5) BY role_agent STATUS inferred SOURCE "t2:s3" -> enables_2 : CLAIM
    LINK supports(conclusion=recommended_3, premise=enables_2) SOURCE "t2:s3"
    UTTER propose(target=activity_6)
    TERM well_wishes(recipient=role_user, sentiment="good_luck") -> well_wishes_2 : TERM
    UTTER respond(target=well_wishes_2)
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    TERM activity(object="passage", verb="edit") -> activity_7 : TERM
    UTTER ask(target=activity_7)
  }
  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    TERM subject(kind="email_draft", qualifier="edited_version") -> subject_6 : TERM
    CLAIM provides(actor=role_agent, subject=subject_6) BY role_agent STATUS asserted SOURCE "t4:s1" -> provides_3 : CLAIM
    UTTER respond(target=subject_6)
  }
  TURN t5 SPEAKER=USER REPLY_TO t4 {
    TERM activity(object="passage", verb="rewrite") -> activity_8 : TERM
    UTTER ask(target=activity_8)
  }
  TURN t6 SPEAKER=AGENT REPLY_TO t5 {
    TERM subject(kind="email_draft", qualifier="rewritten_draft_2") -> subject_7 : TERM
    CLAIM provides(actor=role_agent, subject=subject_7) BY role_agent STATUS asserted SOURCE "t6:s1" -> provides_4 : CLAIM
    UTTER respond(target=subject_7)
  }
  TURN t7 SPEAKER=USER REPLY_TO t6 {
    TERM activity(object="passage", verb="rewrite") -> activity_9 : TERM
    UTTER ask(target=activity_9)
  }
  TURN t8 SPEAKER=AGENT REPLY_TO t7 {
    TERM subject(kind="email_draft", qualifier="rewritten_draft_3") -> subject_8 : TERM
    CLAIM provides(actor=role_agent, subject=subject_8) BY role_agent STATUS asserted SOURCE "t8:s1" -> provides_5 : CLAIM
    UTTER respond(target=subject_8)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | activity | covered |
| n2 | claim | role, subject | covered |
| n3 | object | country::DE | covered |
| n4 | claim | has_state | covered |
| n5 | temporal | time_point | covered |
| n6 | claim | provides | covered |
| n7 | action | activity | covered |
| n8 | claim | exists_in | covered |
| n9 | object | country::IR | covered |
| n10 | speech_act | ask | covered |
| n11 | object | subject | covered |
| n12 | negation | possesses | covered |
| n13 | speech_act | propose, recommended | covered |
| n14 | speech_act | propose, recommended | covered |
| n15 | reasoning | enables, supports | covered |
| n16 | speech_act | well_wishes, respond | covered |
| n17 | action | activity, ask | covered |
| n18 | speech_act | provides, respond | covered |
| n19 | action | activity, ask | covered |
| n20 | speech_act | provides, respond | covered |
| n21 | action | activity, ask | covered |
| n22 | speech_act | provides, respond | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t8:s4 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
