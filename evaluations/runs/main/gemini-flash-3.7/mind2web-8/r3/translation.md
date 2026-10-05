Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM constraint_beginner() -> constraint_beginner_2 : TERM
    TERM activity(instrument=object_label::guitar, object=song, purpose=constraint_beginner_2, verb="filter") -> activity_2 : TERM
    CLAIM request(target=activity_2) BY role_user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT {
    TERM web_element(label="Tabs", tag="link") -> web_element_2 : TERM
    RECORD ACTION click(target=web_element_2) STATUS succeeded SOURCE "t2:s2" -> click_event : EVENT
    TERM web_element(label="Beginner 554,396", tag="link") -> web_element_3 : TERM
    RECORD ACTION click(target=web_element_3) STATUS succeeded SOURCE "t2:s4" -> click_event_2 : EVENT
    LINK then(next=click_event_2, previous=click_event) SOURCE "t2:s3"
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | request | covered |
| n2 | action | activity | covered |
| n3 | object | song | covered |
| n4 | constraint | constraint_beginner | covered |
| n5 | temporal | then | covered |
| n6 | action | click | covered |
| n7 | object | web_element | covered |
| n8 | temporal | then | covered |
| n9 | action | click | covered |
| n10 | object | web_element | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s4 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s1 "guitar" -> object_label::guitar (label only; no sense resolved)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
