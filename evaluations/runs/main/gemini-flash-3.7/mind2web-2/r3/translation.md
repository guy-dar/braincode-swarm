Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(object="IT jobs", verb="browse") -> activity_2 : TERM
    TERM requirement(property="certificate", value="Security clearance") -> requirement_2 : TERM
    TERM sequence(items=[activity_2, requirement_2]) -> sequence_2 : TERM
    CLAIM request(target=sequence_2) BY role_user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT {
    TERM web_element(label="Search by job title, skill or company", tag="searchbox") -> web_element_2 : TERM
    RECORD ACTION type_text(target=web_element_2, text="IT jobs") STATUS succeeded SOURCE "t2:s2" -> type_text_event : EVENT
    TERM web_element(label="Search", tag="button") -> web_element_3 : TERM
    RECORD ACTION click(target=web_element_3) STATUS succeeded SOURCE "t2:s4" -> click_event : EVENT
    TERM web_element(label=" Filters", tag="link") -> web_element_4 : TERM
    RECORD ACTION click(target=web_element_4) STATUS succeeded SOURCE "t2:s6" -> click_event_2 : EVENT
    TERM web_element(label="Certificates", tag="link") -> web_element_5 : TERM
    RECORD ACTION click(target=web_element_5) STATUS succeeded SOURCE "t2:s8" -> click_event_3 : EVENT
    TERM web_element(label="Security clearance", tag="link") -> web_element_6 : TERM
    RECORD ACTION click(target=web_element_6) STATUS succeeded SOURCE "t2:s10" -> click_event_4 : EVENT
    TERM web_element(label="Display Results", tag="span") -> web_element_7 : TERM
    RECORD ACTION click(target=web_element_7) STATUS succeeded SOURCE "t2:s12" -> click_event_5 : EVENT
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | request, role_user | covered |
| n2 | action | activity | covered |
| n3 | object | activity | covered |
| n4 | action | sequence | covered |
| n5 | constraint | requirement | covered |
| n6 | action | type_text, web_element | covered |
| n7 | object | web_element, type_text | covered |
| n8 | object | type_text | covered |
| n9 | action | click, web_element | covered |
| n10 | object | web_element, click | covered |
| n11 | action | click, web_element | covered |
| n12 | object | web_element, click | covered |
| n13 | action | click, web_element | covered |
| n14 | object | web_element, click | covered |
| n15 | action | click, web_element | covered |
| n16 | object | web_element, click | covered |
| n17 | action | click, web_element | covered |
| n18 | object | web_element, click | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s12 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
