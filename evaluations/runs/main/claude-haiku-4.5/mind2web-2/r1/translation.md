Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="jobs", qualifier="IT") -> it_jobs : TERM
    TERM requirement(property="security_clearance_certificate", value=TRUE) -> security_clearance_requirement : TERM
    CLAIM request(target=it_jobs) BY role_user STATUS asserted SOURCE "t1:s1" -> request_search : CLAIM
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM web_element(label="Search by job title, skill or company", tag="input") -> search_box : TERM
    RECORD ACTION type_text(target=search_box, text="IT jobs") STATUS succeeded SOURCE "t2:s2" -> type_text_event : EVENT
    TERM web_element(label="Search", tag="button") -> search_button : TERM
    RECORD ACTION click(target=search_button) STATUS succeeded SOURCE "t2:s4" -> search_click_event : EVENT
    TERM web_element(label="Filters", tag="link") -> filters_link : TERM
    RECORD ACTION click(target=filters_link) STATUS succeeded SOURCE "t2:s6" -> filters_click_event : EVENT
    TERM web_element(label="Certificates", tag="link") -> certificates_link : TERM
    RECORD ACTION click(target=certificates_link) STATUS succeeded SOURCE "t2:s8" -> certificates_click_event : EVENT
    TERM web_element(label="Security clearance", tag="link") -> security_clearance_link : TERM
    RECORD ACTION click(target=security_clearance_link) STATUS succeeded SOURCE "t2:s10" -> security_clearance_click_event : EVENT
    TERM web_element(label="Display Results", tag="span") -> display_results_element : TERM
    RECORD ACTION click(target=display_results_element) STATUS succeeded SOURCE "t2:s12" -> display_results_click_event : EVENT
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | request, role_user | covered |
| n2 | action | type_text, click | covered |
| n3 | object | subject | covered |
| n4 | action | click, type_text | covered |
| n5 | constraint | requirement | covered |
| n6 | action | type_text, web_element | covered |
| n7 | object | web_element | covered |
| n8 | object | type_text | covered |
| n9 | action | click | covered |
| n10 | object | web_element | covered |
| n11 | action | click, web_element | covered |
| n12 | object | web_element | covered |
| n13 | action | click | covered |
| n14 | object | web_element | covered |
| n15 | action | click | covered |
| n16 | object | web_element | covered |
| n17 | action | click, web_element | covered |
| n18 | object | web_element | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment from t1:s1 through t2:s12 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: ran `node /kit/rag.mjs check --translation /output/translation.md`
