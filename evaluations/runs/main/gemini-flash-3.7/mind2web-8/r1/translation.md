Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM constraint_beginner() -> constraint_beginner_2 : TERM
    TERM include(item=song) -> include_2 : TERM
    CLAIM request(target=constraint_beginner_2) BY role_user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT {
    TERM web_element(label="Tabs") -> web_element_2 : TERM
    RECORD ACTION click(target=web_element_2) STATUS succeeded SOURCE "t2:s2" -> click_event : EVENT
    TERM web_element(label="Beginner 554,396") -> web_element_3 : TERM
    RECORD ACTION select_filter(target=web_element_3, criterion=t1.constraint_beginner_2) STATUS succeeded SOURCE "t2:s4" -> select_filter_event : EVENT
    LINK then(next=select_filter_event, previous=click_event) SOURCE "t2:s3"
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | request, select_filter | covered |
| n2 | action | select_filter | covered |
| n3 | object | song | covered |
| n4 | constraint | constraint_beginner, include, song | covered |
| n5 | temporal | then | covered |
| n6 | action | click | covered |
| n7 | object | web_element | covered |
| n8 | temporal | then | covered |
| n9 | action | select_filter | covered |
| n10 | object | web_element | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s4 is represented.
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
