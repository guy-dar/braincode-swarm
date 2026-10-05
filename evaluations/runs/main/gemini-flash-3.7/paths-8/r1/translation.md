Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="project") -> subject_2 : TERM
    TERM activity(object=subject_2, verb="support") -> activity_2 : TERM
    TERM include(item=activity_2) -> include_2 : TERM
    TERM subject(kind="detail") -> subject_3 : TERM
    TERM include(item=subject_3) -> include_3 : TERM
    TERM subject(kind="technical_knowledge") -> subject_4 : TERM
    TERM include(item=subject_4) -> include_4 : TERM
    TERM conjunction(items=[include_2, include_3, include_4]) -> conjunction_2 : TERM
    TERM well_wishes(recipient="Arun") -> well_wishes_2 : TERM
    UTTER propose(target=well_wishes_2, constraints=[conjunction_2], recipient="Arun")
  }
  TURN t2 SPEAKER=AGENT {
    CLAIM important(target=t1.activity_2) BY role_agent STATUS asserted SOURCE "t2:s1" -> important_2 : CLAIM
    UTTER inform(target=important_2, recipient="Arun")
    CLAIM important(target=t1.subject_3) BY role_agent STATUS asserted SOURCE "t2:s2" -> important_3 : CLAIM
    UTTER inform(target=important_3, recipient="Arun")
    UTTER acknowledge(target=t1.activity_2, recipient="Arun")
  }
  TURN t3 SPEAKER=USER {
    TERM offer_help() -> offer_help_2 : TERM
    TERM include(item=offer_help_2) -> include_5 : TERM
    TERM include(item=t1.activity_2) -> include_6 : TERM
    TERM conjunction(items=[include_5, include_6]) -> conjunction_3 : TERM
    TERM well_wishes() -> well_wishes_3 : TERM
    UTTER propose(target=well_wishes_3, constraints=[conjunction_3])
  }
  TURN t4 SPEAKER=AGENT {
    CLAIM important(target=t1.activity_2) BY role_agent STATUS asserted SOURCE "t4:s1" -> important_4 : CLAIM
    UTTER inform(target=important_4)
    UTTER acknowledge(target=t3.offer_help_2)
    UTTER acknowledge(target=t1.activity_2)
  }
  TURN t5 SPEAKER=USER {
    TERM substitute(original=t3.well_wishes_3, replacement=t3.well_wishes_3) -> substitute_2 : TERM
    UTTER propose(target=substitute_2)
  }
  TURN t6 SPEAKER=AGENT {
    CLAIM important(target=t1.activity_2) BY role_agent STATUS asserted SOURCE "t6:s1" -> important_5 : CLAIM
    UTTER inform(target=important_5)
    UTTER acknowledge(target=t1.activity_2)
    UTTER acknowledge(target=t3.offer_help_2)
    UTTER acknowledge(target=t1.activity_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | well_wishes, propose | covered |
| n2 | object | recipient="Arun" | covered |
| n3 | constraint | activity, include | covered |
| n4 | constraint | subject, include | covered |
| n5 | constraint | subject, include | covered |
| n6 | speech_act | important, inform | covered |
| n7 | speech_act | important, inform | covered |
| n8 | speech_act | acknowledge | covered |
| n9 | action | well_wishes, propose | covered |
| n10 | constraint | offer_help, activity, include, conjunction | covered |
| n11 | speech_act | important, inform | covered |
| n12 | speech_act | acknowledge, offer_help | covered |
| n13 | speech_act | acknowledge, activity | covered |
| n14 | action | substitute, propose | covered |
| n15 | speech_act | important, inform | covered |
| n16 | speech_act | acknowledge, activity | covered |
| n17 | speech_act | acknowledge, offer_help | covered |
| n18 | speech_act | acknowledge, activity | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t6:s4 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
