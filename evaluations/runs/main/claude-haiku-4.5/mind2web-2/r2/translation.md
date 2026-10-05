Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM requirement(property="security_clearance", value="certificate") -> requirement : TERM
    CLAIM request(target=requirement) BY role_user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT {
    TERM web_element(label="Search by job title, skill or company") -> web_element : TERM
    RECORD ACTION type_text(target=web_element, text="IT jobs") STATUS succeeded SOURCE "t2:s2" -> type_text_event : EVENT
    TERM web_element(label="Search") -> web_element_2 : TERM
    RECORD ACTION click(target=web_element_2) STATUS succeeded SOURCE "t2:s4" -> click_search_event : EVENT
    TERM web_element(label="Filters") -> web_element_3 : TERM
    RECORD ACTION click(target=web_element_3) STATUS succeeded SOURCE "t2:s6" -> click_filters_event : EVENT
    TERM web_element(label="Certificates") -> web_element_4 : TERM
    RECORD ACTION click(target=web_element_4) STATUS succeeded SOURCE "t2:s8" -> click_certificates_event : EVENT
    TERM web_element(label="Security clearance") -> web_element_5 : TERM
    RECORD ACTION click(target=web_element_5) STATUS succeeded SOURCE "t2:s10" -> click_security_event : EVENT
    TERM web_element(label="Display Results") -> web_element_6 : TERM
    RECORD ACTION click(target=web_element_6) STATUS succeeded SOURCE "t2:s12" -> click_display_event : EVENT
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | request, role_user | covered |
| n2 | action | type_text, click | covered |
| n3 | object | IT jobs | label-preserved |
| n4 | action | click | covered |
| n5 | constraint | requirement | covered |
| n6 | action | type_text | covered |
| n7 | object | web_element | covered |
| n8 | object | type_text with text parameter | covered |
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
- Source-span coverage: t1:s1 (user request for security clearance filter on IT jobs), t2:s2 (type search term), t2:s4 (click search button), t2:s6 (click filters), t2:s8 (click certificates category), t2:s10 (click security clearance option), t2:s12 (click display results)
- Opaque-text spans: none
- Label-preserved spans: n3 "IT jobs" → subject of search, represented implicitly in requirement constraint and request claim
- Missing constructs: none
- Unresolved ambiguities: none
- Semantic coverage notes: High-level needs for "browse/search" and "filter results" are accomplished through recorded RECORD ACTION calls (type_text, click) on web UI elements; the security clearance constraint is expressed as a TERM requirement in the user's request claim
```

Let me verify with rag check:
<function_calls>
<invoke name="bash">
<parameter name="command">node /kit/rag.mjs check --translation /output/translation.md 2>&1