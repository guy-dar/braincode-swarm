Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(verb="search", object="IT jobs") -> search_activity : TERM
    TERM requirement(property="security_clearance_certificate", value=TRUE) -> cert_req : TERM
    TERM conjunction(items=[search_activity, cert_req]) -> compound_request : TERM
    CLAIM request(target=compound_request) BY role_user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT {
    TERM web_element(label="Search by job title, skill or company", tag="input") -> search_box : TERM
    RECORD ACTION type_text(target=search_box, text="IT jobs") STATUS succeeded SOURCE "t2:s2" -> type_text_event : EVENT
    
    TERM web_element(label="Search", tag="button") -> search_button : TERM
    RECORD ACTION click(target=search_button) STATUS succeeded SOURCE "t2:s4" -> click_search_event : EVENT
    
    TERM web_element(label="Filters", tag="link") -> filters_link : TERM
    RECORD ACTION click(target=filters_link) STATUS succeeded SOURCE "t2:s6" -> click_filters_event : EVENT
    
    TERM web_element(label="Certificates", tag="link") -> certificates_link : TERM
    RECORD ACTION click(target=certificates_link) STATUS succeeded SOURCE "t2:s8" -> click_certificates_event : EVENT
    
    TERM web_element(label="Security clearance", tag="link") -> security_clearance_link : TERM
    RECORD ACTION click(target=security_clearance_link) STATUS succeeded SOURCE "t2:s10" -> click_security_event : EVENT
    
    TERM web_element(label="Display Results", tag="span") -> display_results_button : TERM
    RECORD ACTION click(target=display_results_button) STATUS succeeded SOURCE "t2:s12" -> click_display_event : EVENT
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | request (CLAIM) | covered |
| n2 | action | activity | covered |
| n3 | object | activity object parameter | covered |
| n4 | action | click operations | covered |
| n5 | constraint | requirement | covered |
| n6 | action | type_text | covered |
| n7 | object | web_element | covered |
| n8 | object | type_text text parameter | covered |
| n9 | action | click | covered |
| n10 | object | web_element | covered |
| n11 | action | click | covered |
| n12 | object | web_element | covered |
| n13 | action | click | covered |
| n14 | object | web_element | covered |
| n15 | action | click | covered |
| n16 | object | web_element | covered |
| n17 | action | click | covered |
| n18 | object | web_element | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: all segments t1:s1, t2:s2, t2:s4, t2:s6, t2:s8, t2:s10, t2:s12 are represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: no unresolved needs or unknown symbols expected
```
