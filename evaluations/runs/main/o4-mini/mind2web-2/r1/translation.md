Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(verb="browse", object="IT jobs") -> browse_2 : TERM
    TERM activity(verb="filter", object="IT jobs") -> filter_3 : TERM
    TERM requirement(property="security clearance certificate", value=TRUE) -> requirement_4 : TERM
    TERM conjunction(items=[browse_2, filter_3, requirement_4]) -> conjunction_5 : TERM
    CLAIM request(target=conjunction_5) BY role_user STATUS asserted SOURCE "t1:s1" -> request_6 : CLAIM
  }
  TURN t2 SPEAKER=AGENT {
    TERM web_element(label="Search by job title, skill or company") -> searchbox_2 : TERM
    RECORD ACTION type_text(target=searchbox_2, text="IT jobs") STATUS succeeded SOURCE "t2:s2" -> type_text_event : EVENT
    TERM web_element(label="Search") -> search_button_2 : TERM
    RECORD ACTION click(target=search_button_2) STATUS succeeded SOURCE "t2:s4" -> click_search_event : EVENT
    TERM web_element(label="Filters") -> filters_link_2 : TERM
    RECORD ACTION click(target=filters_link_2) STATUS succeeded SOURCE "t2:s6" -> click_filters_event : EVENT
    TERM web_element(label="Certificates") -> certificates_link_2 : TERM
    RECORD ACTION click(target=certificates_link_2) STATUS succeeded SOURCE "t2:s8" -> click_certificates_event : EVENT
    TERM web_element(label="Security clearance") -> security_link_2 : TERM
    RECORD ACTION click(target=security_link_2) STATUS succeeded SOURCE "t2:s10" -> click_security_event : EVENT
    TERM web_element(label="Display Results") -> display_link_2 : TERM
    RECORD ACTION click(target=display_link_2) STATUS succeeded SOURCE "t2:s12" -> click_display_event : EVENT
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | request | covered |
| n2 | action | activity(browse) | covered |
| n3 | object | "IT jobs" | covered |
| n4 | action | activity(filter) | covered |
| n5 | constraint | requirement | covered |
| n6 | action | type_text | covered |
| n7 | object | web_element (search input) | covered |
| n8 | object | "IT jobs" (text) | covered |
| n9 | action | click | covered |
| n10 | object | web_element (search button) | covered |
| n11 | action | click | covered |
| n12 | object | web_element (filters link) | covered |
| n13 | action | click | covered |
| n14 | object | web_element (certificates link) | covered |
| n15 | action | click | covered |
| n16 | object | web_element (security clearance link) | covered |
| n17 | action | click | covered |
| n18 | object | web_element (display results element) | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: all segments t1:s1 and t2:s2–t2:s12 are represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
