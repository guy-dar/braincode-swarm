Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM location_spec(city="Sydney") -> location_spec_2 : TERM
    TERM subject(kind="university", qualifier=location_spec_2) -> subject_2 : TERM
    TERM promotional_event(kind="special_offer") -> promotional_event_2 : TERM
    TERM requirement(property="promotion", value=promotional_event_2) -> requirement_2 : TERM
    TERM include(item=requirement_2) -> include_2 : TERM
    TERM subject(kind="property", qualifier=include_2) -> subject_3 : TERM
    CLAIM associated_with(concept=subject_2, subject=subject_3) BY role_user STATUS asserted SOURCE "t1:s1" -> associated_with_2 : CLAIM
    CLAIM request(target=subject_3) BY role_user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM web_element(label="Search by college, city or property", tag="textbox") -> web_element_2 : TERM
    RECORD ACTION click(target=web_element_2) STATUS succeeded SOURCE "t2:s2" -> click_event : EVENT
    TERM web_element(label="Sydney", tag="span") -> web_element_3 : TERM
    RECORD ACTION click(target=web_element_3) STATUS succeeded SOURCE "t2:s4" -> click_event_2 : EVENT
    TERM web_element(label="Special offer", tag="button") -> web_element_4 : TERM
    RECORD ACTION click(target=web_element_4) STATUS succeeded SOURCE "t2:s6" -> click_event_3 : EVENT
    TERM web_element(label="", tag="button") -> web_element_5 : TERM
    RECORD ACTION click(target=web_element_5) STATUS succeeded SOURCE "t2:s8" -> click_event_4 : EVENT
    TERM web_element(label="Select University", tag="div") -> web_element_6 : TERM
    RECORD ACTION click(target=web_element_6) STATUS succeeded SOURCE "t2:s10" -> click_event_5 : EVENT
    TERM web_element(label="Macquarie University", tag="div") -> web_element_7 : TERM
    RECORD ACTION click(target=web_element_7) STATUS succeeded SOURCE "t2:s12" -> click_event_6 : EVENT
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | request | covered |
| n2 | action | subject | covered |
| n3 | object | subject | covered |
| n4 | constraint | include, promotional_event, requirement | covered |
| n5 | constraint | associated_with, location_spec | covered |
| n6 | object | location_spec, subject | covered |
| n7 | action | click, web_element | covered |
| n8 | action | click, web_element | covered |
| n9 | action | click, web_element | covered |
| n10 | action | click, web_element | covered |
| n11 | action | click, web_element | covered |
| n12 | action | click, web_element | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s12 is represented.
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
