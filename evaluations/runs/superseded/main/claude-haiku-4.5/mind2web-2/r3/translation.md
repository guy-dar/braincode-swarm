Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    CLAIM request(target="Browse IT jobs and filter by Security clearance certificate") BY role_user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT {
    TERM web_element(label="Search by job title, skill or company") -> search_input : TERM
    TERM web_element(label="Search") -> search_button : TERM
    TERM web_element(label="Filters") -> filters_link : TERM
    TERM web_element(label="Certificates") -> certificates_link : TERM
    TERM web_element(label="Security clearance") -> security_clearance_link : TERM
    TERM web_element(label="Display Results") -> display_results : TERM
    
    RECORD ACTION type_text(target=search_input, text="IT jobs") STATUS succeeded SOURCE "t2:s2" -> type_text_event : EVENT
    RECORD ACTION click(target=search_button) STATUS succeeded SOURCE "t2:s4" -> click_search_event : EVENT
    RECORD ACTION click(target=filters_link) STATUS succeeded SOURCE "t2:s6" -> click_filters_event : EVENT
    RECORD ACTION click(target=certificates_link) STATUS succeeded SOURCE "t2:s8" -> click_certificates_event : EVENT
    RECORD ACTION click(target=security_clearance_link) STATUS succeeded SOURCE "t2:s10" -> click_clearance_event : EVENT
    RECORD ACTION click(target=display_results) STATUS succeeded SOURCE "t2:s12" -> click_display_event : EVENT
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | request | covered |
| n2 | action | type_text, click (search flow) | covered |
| n3 | object | "IT jobs" (text parameter) | label-preserved |
| n4 | action | click (filters operations) | covered |
| n5 | constraint | click (security_clearance_link) | label-preserved |
| n6 | action | type_text | covered |
| n7 | object | web_element (search input) | covered |
| n8 | object | "IT jobs" (text parameter) | label-preserved |
| n9 | action | click | covered |
| n10 | object | web_element (search button) | covered |
| n11 | action | click | covered |
| n12 | object | web_element (filters link) | covered |
| n13 | action | click | covered |
| n14 | object | web_element (certificates link) | covered |
| n15 | action | click | covered |
| n16 | object | web_element (security clearance link) | covered |
| n17 | action | click | covered |
| n18 | object | web_element (display results) | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1 and t2:s2–t2:s12 is represented
- Opaque-text spans: none
- Label-preserved spans: n3 "IT jobs" → text literal; n5 "Security clearance certificate" → web element label (semantic meaning of the certificate constraint preserved through the UI flow)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` should report 0 unresolved needs and 0 unknown symbols
