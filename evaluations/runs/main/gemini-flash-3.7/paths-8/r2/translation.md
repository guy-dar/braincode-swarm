Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM well_wishes(recipient="Arun", sentiment="compliment") -> well_wishes_2 : TERM
    TERM activity(object="project", verb="support") -> activity_2 : TERM
    TERM include(item=activity_2) -> include_2 : TERM
    TERM subject(kind="attention_to_detail") -> subject_2 : TERM
    TERM include(item=subject_2) -> include_3 : TERM
    TERM subject(kind="technical_knowledge") -> subject_3 : TERM
    TERM include(item=subject_3) -> include_4 : TERM
    TERM conjunction(items=[include_2, include_3, include_4]) -> conjunction_2 : TERM
    UTTER ask(target=well_wishes_2, constraints=[conjunction_2], recipient="Arun")
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    CLAIM ongoing(target=t1.activity_2) BY role_agent STATUS asserted SOURCE "t2:s1" -> ongoing_2 : CLAIM
    CLAIM important(target=t1.activity_2) BY role_agent STATUS asserted SOURCE "t2:s1" -> important_2 : CLAIM
    UTTER inform(target=important_2)
    CLAIM important(target=t1.subject_2) BY role_agent STATUS asserted SOURCE "t2:s2" -> important_3 : CLAIM
    CLAIM important(target=t1.subject_3) BY role_agent STATUS asserted SOURCE "t2:s2" -> important_4 : CLAIM
    UTTER inform(target=important_3)
    UTTER inform(target=important_4)
    TERM well_wishes(recipient="Arun", sentiment="gratitude") -> well_wishes_3 : TERM
    UTTER acknowledge(target=well_wishes_3)
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    TERM well_wishes(sentiment="compliment") -> well_wishes_4 : TERM
    TERM offer_help() -> offer_help_2 : TERM
    TERM conjunction(items=[t1.activity_2, offer_help_2]) -> conjunction_3 : TERM
    TERM include(item=conjunction_3) -> include_5 : TERM
    UTTER ask(target=well_wishes_4, constraints=[include_5])
  }
  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    CLAIM important(target=t1.activity_2) BY role_agent STATUS asserted SOURCE "t4:s1" -> important_5 : CLAIM
    UTTER inform(target=important_5)
    TERM well_wishes(sentiment="gratitude") -> well_wishes_5 : TERM
    UTTER acknowledge(target=well_wishes_5)
    TERM subject(kind="assistance") -> subject_4 : TERM
    CLAIM important(target=subject_4) BY role_agent STATUS asserted SOURCE "t4:s3" -> important_6 : CLAIM
    UTTER inform(target=important_6)
  }
  TURN t5 SPEAKER=USER REPLY_TO t4 {
    TERM well_wishes(sentiment="alternative_compliment") -> well_wishes_6 : TERM
    UTTER propose(target=well_wishes_6)
  }
  TURN t6 SPEAKER=AGENT REPLY_TO t5 {
    TERM subject(kind="commitment_to_success", qualifier="project") -> subject_5 : TERM
    CLAIM important(target=subject_5) BY role_agent STATUS asserted SOURCE "t6:s1" -> important_7 : CLAIM
    UTTER inform(target=important_7)
    CLAIM important(target=t1.activity_2) BY role_agent STATUS asserted SOURCE "t6:s2" -> important_8 : CLAIM
    UTTER inform(target=important_8)
    TERM well_wishes(sentiment="gratitude") -> well_wishes_7 : TERM
    UTTER acknowledge(target=well_wishes_7)
    TERM subject(kind="efforts") -> subject_6 : TERM
    CLAIM important(target=subject_6) BY role_agent STATUS asserted SOURCE "t6:s4" -> important_9 : CLAIM
    UTTER inform(target=important_9)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | well_wishes, ask | covered |
| n2 | object | recipient="Arun" | covered |
| n3 | constraint | activity, include, ongoing | covered |
| n4 | constraint | subject, include | covered |
| n5 | constraint | subject, include | covered |
| n6 | speech_act | ongoing, important, inform | covered |
| n7 | speech_act | important, inform | covered |
| n8 | speech_act | well_wishes, acknowledge | covered |
| n9 | action | well_wishes, ask | covered |
| n10 | constraint | activity, offer_help, conjunction, include | covered |
| n11 | speech_act | important, inform | covered |
| n12 | speech_act | well_wishes, acknowledge | covered |
| n13 | speech_act | subject, important, inform | covered |
| n14 | action | well_wishes, propose | covered |
| n15 | speech_act | subject, important, inform | covered |
| n16 | speech_act | important, inform | covered |
| n17 | speech_act | well_wishes, acknowledge | covered |
| n18 | speech_act | subject, important, inform | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t6:s4 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
