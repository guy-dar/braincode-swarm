Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(object=format_plain_text, verb="edit") -> activity_2 : TERM
    UTTER ask(target=activity_2)
    TERM subject(kind="researcher", location=country::DE, qualifier="visiting_researcher") -> subject_2 : TERM
    CLAIM ongoing(target=subject_2) BY user STATUS asserted SOURCE "t1:s1" -> ongoing_2 : CLAIM
    TERM time_point(date="end_of_August") -> time_point_2 : TERM
    TERM subject(kind="visa", time="end_of_August") -> subject_3 : TERM
    CLAIM allowed_to_enter(location=country::DE, subject=subject_3) BY user STATUS asserted SOURCE "t1:s1" -> allowed_to_enter_2 : CLAIM
    TERM activity(actor="university", object="stay", verb="extend") -> activity_3 : TERM
    CLAIM ongoing(target=activity_3) BY user STATUS asserted SOURCE "t1:s2" -> ongoing_3 : CLAIM
    TERM activity(object="visa_extension", verb="apply") -> activity_4 : TERM
    CLAIM ongoing(target=activity_4) BY user STATUS asserted SOURCE "t1:s2" -> ongoing_4 : CLAIM
    TERM activity(location=country::IR, object="stay", verb="reside") -> activity_5 : TERM
    CLAIM ongoing(target=activity_5) BY user STATUS asserted SOURCE "t1:s3" -> ongoing_5 : CLAIM
    TERM subject(kind="embassy", location=country::IR, qualifier=locale_de) -> subject_4 : TERM
    TERM activity(actor=subject_4, object="visa_extension", verb="obtain") -> activity_6 : TERM
    UTTER ask(target=activity_6)
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM subject(kind="updates", qualifier="immigration_policies") -> subject_5 : TERM
    TERM activity(actor="agent", object=subject_5, verb="possess") -> activity_7 : TERM
    TERM negation(target=activity_7) -> negation_2 : TERM
    CLAIM ongoing(target=negation_2) BY agent STATUS asserted SOURCE "t2:s1" -> ongoing_6 : CLAIM
    UTTER inform(target=ongoing_6)
    TERM activity(object=t1.subject_4, verb="contact") -> activity_8 : TERM
    UTTER propose(target=activity_8)
    TERM activity(object="visa_extension", verb="apply_early") -> activity_9 : TERM
    CLAIM recommended(target=activity_9) BY agent STATUS asserted SOURCE "t2:s3" -> recommended_2 : CLAIM
    UTTER inform(target=recommended_2)
    TERM subject(kind="legal_transition", qualifier="smooth_transition") -> subject_6 : TERM
    CLAIM enables(condition=activity_9, outcome=subject_6) BY agent STATUS inferred SOURCE "t2:s3" -> enables_2 : CLAIM
    LINK supports(conclusion=recommended_2, premise=enables_2) SOURCE "t2:s3"
    TERM well_wishes(recipient=role_user, sentiment="good_luck") -> well_wishes_2 : TERM
    UTTER respond(target=well_wishes_2)
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    TERM activity(object=format_plain_text, verb="edit") -> activity_10 : TERM
    UTTER ask(target=activity_10)
  }
  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    TERM subject(kind="email", qualifier="edited_text") -> subject_7 : TERM
    CLAIM provides(actor="agent", subject=subject_7) BY agent STATUS asserted SOURCE "t4:s1" -> provides_2 : CLAIM
    UTTER respond(target=provides_2)
  }
  TURN t5 SPEAKER=USER REPLY_TO t4 {
    TERM activity(object=format_plain_text, verb="rewrite") -> activity_11 : TERM
    UTTER ask(target=activity_11)
  }
  TURN t6 SPEAKER=AGENT REPLY_TO t5 {
    TERM subject(kind="draft", qualifier="rewritten_text") -> subject_8 : TERM
    CLAIM provides(actor="agent", subject=subject_8) BY agent STATUS asserted SOURCE "t6:s1" -> provides_3 : CLAIM
    UTTER respond(target=provides_3)
  }
  TURN t7 SPEAKER=USER REPLY_TO t6 {
    TERM activity(object=format_plain_text, verb="rewrite") -> activity_12 : TERM
    UTTER ask(target=activity_12)
  }
  TURN t8 SPEAKER=AGENT REPLY_TO t7 {
    TERM subject(kind="draft", qualifier="third_rewritten_text") -> subject_9 : TERM
    CLAIM provides(actor="agent", subject=subject_9) BY agent STATUS asserted SOURCE "t8:s1" -> provides_4 : CLAIM
    UTTER respond(target=provides_4)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | activity, format_plain_text, ask | covered |
| n2 | claim | subject, ongoing | covered |
| n3 | object | country::DE | covered |
| n4 | claim | allowed_to_enter, subject | covered |
| n5 | temporal | time_point | covered |
| n6 | claim | activity, ongoing | covered |
| n7 | action | activity, ongoing | covered |
| n8 | claim | activity, ongoing | covered |
| n9 | object | country::IR | covered |
| n10 | speech_act | ask | covered |
| n11 | object | subject, locale_de | covered |
| n12 | negation | negation, ongoing, inform | covered |
| n13 | speech_act | propose | covered |
| n14 | speech_act | recommended, inform | covered |
| n15 | reasoning | supports, enables | covered |
| n16 | speech_act | well_wishes, respond | covered |
| n17 | action | activity, format_plain_text, ask | covered |
| n18 | speech_act | provides, respond | covered |
| n19 | action | activity, format_plain_text, ask | covered |
| n20 | speech_act | provides, respond | covered |
| n21 | action | activity, format_plain_text, ask | covered |
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
