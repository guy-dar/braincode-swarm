Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM requirement(property="Security clearance certificate", value=TRUE) -> requirement_2 : TERM
    TERM activity(verb="search", object="IT jobs") -> activity_2 : TERM  # REFINED: S1
    TERM activity(verb="filter", object="job listings", purpose=requirement_2) -> activity_3 : TERM  # REFINED: S1
    TERM sequence(items=[activity_2, activity_3]) -> sequence_2 : TERM
    CLAIM request(target=sequence_2) BY role_user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM web_element(label="Search by job title, skill or company", tag="searchbox") -> web_element_2 : TERM
    RECORD ACTION type_text(target=web_element_2, text="IT jobs") STATUS unknown SOURCE "t2:s2" -> type_text_event : EVENT
    TERM web_element(label="Search", tag="button") -> web_element_3 : TERM
    RECORD ACTION click(target=web_element_3) STATUS unknown SOURCE "t2:s4" -> click_event : EVENT
    TERM web_element(label="Filters", tag="link") -> web_element_4 : TERM
    RECORD ACTION click(target=web_element_4) STATUS unknown SOURCE "t2:s6" -> click_event_2 : EVENT
    TERM web_element(label="Certificates", tag="link") -> web_element_5 : TERM
    RECORD ACTION click(target=web_element_5) STATUS unknown SOURCE "t2:s8" -> click_event_3 : EVENT
    TERM web_element(label="Security clearance", tag="link") -> web_element_6 : TERM
    RECORD ACTION click(target=web_element_6) STATUS unknown SOURCE "t2:s10" -> click_event_4 : EVENT
    TERM web_element(label="Display Results", tag="span") -> web_element_7 : TERM
    RECORD ACTION click(target=web_element_7) STATUS unknown SOURCE "t2:s12" -> click_event_5 : EVENT
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | request, activity, sequence | covered |
| n2 | action | activity (REFINED: S1) | proposed |
| n3 | object | activity | covered |
| n4 | action | activity (REFINED: S1) | proposed |
| n5 | constraint | requirement | unresolved |
| n6 | action | type_text | covered |
| n7 | object | type_text, web_element | covered |
| n8 | object | type_text | covered |
| n9 | action | click | covered |
| n10 | object | click | covered |
| n11 | action | click | covered |
| n12 | object | web_element | unresolved |
| n13 | action | click | covered |
| n14 | object | web_element | unresolved |
| n15 | action | click | covered |
| n16 | object | web_element | unresolved |
| n17 | action | click | covered |
| n18 | object | web_element | covered |

## Why the translation failed

- n2 “Browse or search job listings” — widened with that wording; `search_web` was the closest candidate, but it is an operation for querying a web/catalog source. This TRACE supplies a UI sequence, not a reported successful web query, so recording `search_web` would overstate the source. `activity` can describe the requested search compositionally, but `rag check` still declared this need unresolved; proposed refinement S1 explicitly defines this verb.
- n4 “Filter job search results” — widened with that wording; `apply_filters` and `select_filter` were returned. The supplied trace records clicks on UI controls, not a separate filter-operation event; adding one would invent an operation. The requested filter is represented by the `activity` term, but `rag check` declared it unresolved; proposed refinement S1 explicitly defines this verb.
- n5 “Filter by Security clearance certificate” — widened with that wording; `requirement` is the closest fitting constructor and is used with the source-supplied property name. The retrieved alternatives describe unrelated filters or permissions. `rag check` nevertheless declared the need unresolved; no more specific accepted certificate-filter vocabulary was found.
- n12 “Filters link” — widened; `web_element(label="Filters", tag="link")` uses the accepted UI-element constructor and preserves its visible label. `rag check` did not count it for this need.
- n14 “Certificates link” — widened; `web_element(label="Certificates", tag="link")` uses the accepted UI-element constructor and preserves its visible label. Certificate/product entries do not describe this UI link. `rag check` did not count it for this need.
- n16 “Security clearance link” — widened; `web_element(label="Security clearance", tag="link")` uses the accepted UI-element constructor and preserves its visible label. `rag check` did not count it for this need.

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: t1:s1 and each agent operation at t2:s2, t2:s4, t2:s6, t2:s8, t2:s10, and t2:s12 are represented.
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: S1 refines the activity constructor's definitions of the search and filter verbs; the remaining unresolved rows are `rag check` declarations despite the accepted requirement constructor and UI-element constructor.
- Unresolved ambiguities: none
- Check: `rag check` reported 6 unresolved needs before applying proposed S1 (n2, n4, n5, n12, n14, n16), 0 unknown symbols
