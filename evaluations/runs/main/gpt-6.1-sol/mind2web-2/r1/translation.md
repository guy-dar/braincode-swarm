Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM job_listing_search(certificate="Security clearance", field="IT") -> job_listing_search_2 : TERM # PROPOSED: S1
    CLAIM request(target=job_listing_search_2) BY role_user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT {
    TERM web_element(label="Search by job title, skill or company") -> web_element_2 : TERM
    CLAIM role(role_type="searchbox", subject=web_element_2) BY role_agent STATUS observed SOURCE "t2:s2" -> role_2 : CLAIM
    RECORD ACTION type_text(target=web_element_2, text="IT jobs") STATUS attempted SOURCE "t2:s2" -> type_text_event : EVENT
    TERM web_element(label="Search") -> web_element_3 : TERM
    CLAIM role(role_type="button", subject=web_element_3) BY role_agent STATUS observed SOURCE "t2:s4" -> role_3 : CLAIM
    RECORD ACTION click(target=web_element_3) STATUS attempted SOURCE "t2:s4" -> click_event : EVENT
    TERM web_element(label=" Filters") -> web_element_4 : TERM
    CLAIM role(role_type="link", subject=web_element_4) BY role_agent STATUS observed SOURCE "t2:s6" -> role_4 : CLAIM
    RECORD ACTION click(target=web_element_4) STATUS attempted SOURCE "t2:s6" -> click_event_2 : EVENT
    TERM web_element(label="Certificates") -> web_element_5 : TERM
    CLAIM role(role_type="link", subject=web_element_5) BY role_agent STATUS observed SOURCE "t2:s8" -> role_5 : CLAIM
    RECORD ACTION click(target=web_element_5) STATUS attempted SOURCE "t2:s8" -> click_event_3 : EVENT
    TERM web_element(label="Security clearance") -> web_element_6 : TERM
    CLAIM role(role_type="link", subject=web_element_6) BY role_agent STATUS observed SOURCE "t2:s10" -> role_6 : CLAIM
    RECORD ACTION click(target=web_element_6) STATUS attempted SOURCE "t2:s10" -> click_event_4 : EVENT
    TERM web_element(label="Display Results", tag="span") -> web_element_7 : TERM
    RECORD ACTION click(target=web_element_7) STATUS attempted SOURCE "t2:s12" -> click_event_5 : EVENT
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | request | covered |
| n2 | action | job_listing_search (PROPOSED: S1) | proposed |
| n3 | object | job_listing_search.field (PROPOSED: S1) | proposed |
| n4 | action | job_listing_search.certificate (PROPOSED: S1) | proposed |
| n5 | constraint | job_listing_search.certificate (PROPOSED: S1) | proposed |
| n6 | action | RECORD ACTION type_text | covered |
| n7 | object | web_element, role | covered |
| n8 | object | type_text.text="IT jobs" | covered |
| n9 | action | RECORD ACTION click | covered |
| n10 | object | web_element, role | covered |
| n11 | action | RECORD ACTION click | covered |
| n12 | object | web_element, role | covered |
| n13 | action | RECORD ACTION click | covered |
| n14 | object | web_element, role | covered |
| n15 | action | RECORD ACTION click | covered |
| n16 | object | web_element, role | covered |
| n17 | action | RECORD ACTION click | covered |
| n18 | object | web_element | covered |

## Why the translation failed

- n2: `widen "Browse or search job listings"` and `search "job listing employment search description"` found search_web, search_travel and apply_filters. These execute requested work; they cannot serve as a structured description of the user's request inside this TRACE. activity lacks a governed search-criteria argument, and an unreviewed verb string does not supply a new operation definition. S1 supplies the missing nonexecuting search description.
- n3: `widen "IT jobs"` and `search "IT jobs information technology employment"` found chill, role_agent, tone_professional and topic_ai_earning_methods; none describes job postings in the named IT field. An object_label atom cannot encode both the posting class and its occupational-field qualification. S1 exposes the named field separately.
- n4: `widen "Filter job search results"` and `search "described search query criteria"` found search_web, apply_filters and select_filter. Their runtime operations do not express the filter's scope within a descriptive request term. S1 makes the certificate facet govern the requested job search without inventing a separate UI operation for t1.
- n5: `widen "Filter by Security clearance certificate"`, `search "Security clearance certificate filter"` and `search "certificate qualification requirement"` found select_filter, requirement, driver_license and vehicle_allowance. driver_license is the wrong credential; vehicle_allowance concerns vehicle permission. requirement alone does not identify which job-search facet is being filtered or attach it to a described search. S1 defines this scope and leaves the certificate name as an exact source-supplied designation, without claiming the user holds it or inferring a jurisdiction or clearance level.

## Translation report

- Pinned release: specification 19.0.0-draft.2-lexical-groups; glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6).
- Input kind: conversation; recorded user request and agent UI-action trajectory.
- Coverage status: partial under the pinned glossary; the suggested document would cover the substantive content if S1 were accepted.
- Source-span coverage: t1:s1 is represented by a request claim whose structured target requires S1. t2:s2, s4, s6, s8, s10 and s12 are represented in order by UI descriptions and recorded operations. t2:s1, s3, s5, s7, s9 and s11 are step numbers, preserved by source order rather than independent semantic statements.
- Opaque-text spans: none; no sentence is hidden in content or a topic. Exact UI labels, UI-role identifiers, the span tag and typed search text remain literals because their exact forms are the objects of interaction.
- Label-preserved spans: none using open lexical groups. S1 uses exact supplied names for the occupational field and certificate facet; it adds no taxonomy, credential level or legal meaning.
- Missing constructs: S1 job_listing_search, a structured description of browsing/searching job postings in a named field with an optional certificate-facet filter.
- Unresolved ambiguities: the trace supplies no UI outcomes or resulting listings, so operations are recorded as attempted, not succeeded. No claims about successful filtering are invented. The dataset's bracketed searchbox/button/link identifiers are represented as functional-role claims, not guessed HTML tags. The explicitly supplied span is represented as a tag.
- Proposed glossary/spec changes: accept S1 as a reviewed primitive constructor; no grammar change is proposed.
- Check: `rag check` reported one unknown symbol, job_listing_search (proposed S1), and no other warning lines. It marked n2, n4, n5, n12, n14 and n16 as DECL (coverage-table declarations); n12/n14/n16 are expressed by exact web_element labels plus role claims. Its n3 OK match to role_agent/role_user is incidental, not semantic coverage: n3 remains proposed under S1 as the table states. This lexical check does not validate the proposed constructor or establish fidelity.
