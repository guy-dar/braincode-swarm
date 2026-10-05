Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM requirement(property="security_clearance_certificate", value=TRUE) -> requirement_2 : TERM
    TERM search_request(target="IT jobs", constraints=[requirement_2]) -> search_request_2 : TERM  # PROPOSED: S1
    CLAIM request(target=search_request_2) BY role_user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT {
    TERM web_element(label="Search by job title, skill or company", tag="searchbox") -> web_element_2 : TERM
    RECORD ACTION type_text(target=web_element_2, text="IT jobs") STATUS succeeded SOURCE "t2:s2" -> type_text_event : EVENT
    TERM web_element(label="Search", tag="button") -> web_element_3 : TERM
    RECORD ACTION click(target=web_element_3) STATUS succeeded SOURCE "t2:s4" -> click_event : EVENT
    TERM web_element(label="Filters", tag="link") -> web_element_4 : TERM
    RECORD ACTION click(target=web_element_4) STATUS succeeded SOURCE "t2:s6" -> click_event_2 : EVENT
    TERM web_element(label="Certificates", tag="link") -> web_element_5 : TERM
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
| n1 | speech_act | request | covered |
| n2 | action | search_request (PROPOSED: S1) | proposed |
| n3 | object | search_request target="IT jobs" | covered |
| n4 | action | search_request (PROPOSED: S1) | proposed |
| n5 | constraint | requirement, search_request (PROPOSED: S1) | proposed |
| n6 | action | type_text, web_element | covered |
| n7 | object | type_text, web_element | covered |
| n8 | object | type_text | covered |
| n9 | action | click | covered |
| n10 | object | click, web_element | covered |
| n11 | action | click | covered |
| n12 | object | web_element | covered |
| n13 | action | click | covered |
| n14 | object | web_element | covered |
| n15 | action | click | covered |
| n16 | object | web_element | covered |
| n17 | action | click | covered |
| n18 | object | web_element | covered |

## Why the translation failed

- n2 (t1:s1), n4 (t1:s1), and n5 (t1:s1): `search_request` (S1) is needed to represent the user's requested search target together with its filter constraints as a non-executing TERM in a TRACE. `activity` can describe actions generally, but does not make a search target and its filters explicit as a structured search request. `requirement` describes the requested clearance property but does not itself express searching/filtering results. Searches tried: `widen "browse or search job listings"` → `search_web`, `search_travel`, `apply_filters`, `search_transit`, `open_page`; `widen "filter job search results"` → `search_web`, `apply_filters`, `select_filter`; `widen "filter job listings by Security clearance certificate"` → `select_filter`, `apply_filters`, `search_web`, generic reservation candidates; `search "security clearance certificate job qualification filter"` → generic reservation/filter candidates, no job-qualification constraint. `search_web` and `apply_filters` are executable operations, not the requested behavior to record in TRACE; `select_filter` applies one filter to an existing UI, not a non-effectful description of the user's request. No retrieved candidate represents this typed requested-search structure.
- n12 (t2:s6), n14 (t2:s8), and n16 (t2:s10): the exact visible labels and element kinds are represented by `web_element`; widened searches for each label returned `web_element`. The automated check still declares these needs because that symbol is absent from their initial candidate lists. No additional label symbols are proposed: `web_element` already provides a suitable generic description, and the labels are preserved literally.

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: t1:s1 is represented as a user-attributed request; t2:s2, t2:s4, t2:s6, t2:s8, t2:s10, and t2:s12 are recorded as supplied UI operations. The intervening numbered step markers contain no additional semantic content.
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: S1, a non-executing structured search-request TERM with target and filter constraints
- Unresolved ambiguities: none
- Check: `rag check` reported unresolved needs n2, n4, n5, n12, n14, and n16 before applying proposed S1; the initial-candidate-list declarations for n12, n14, and n16 are addressed by the retrieved `web_element` constructor. The proposed `search_request` is not in the current glossary.
