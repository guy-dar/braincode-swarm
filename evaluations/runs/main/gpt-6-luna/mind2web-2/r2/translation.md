Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM job_search(domain="IT jobs") -> job_search_2 : TERM  # PROPOSED: S1
    TERM job_posting_filter(criterion="Security clearance certificate") -> job_posting_filter_2 : TERM  # PROPOSED: S2
    TERM sequence(items=[job_search_2, job_posting_filter_2]) -> sequence_2 : TERM
    CLAIM request(target=sequence_2) BY role_user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
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
| n1 | speech_act | request, sequence | covered |
| n2 | action | job_search (PROPOSED: S1) | proposed |
| n3 | object | job_search(domain="IT jobs") (PROPOSED: S1), type_text | proposed |
| n4 | action | job_posting_filter (PROPOSED: S2) | proposed |
| n5 | constraint | job_posting_filter (PROPOSED: S2) | proposed |
| n6 | action | type_text | covered |
| n7 | object | web_element, type_text | covered |
| n8 | object | type_text | covered |
| n9 | action | click | covered |
| n10 | object | web_element, click | covered |
| n11 | action | click | covered |
| n12 | object | web_element(label="Filters", tag="link") | covered |
| n13 | action | click | covered |
| n14 | object | web_element(label="Certificates", tag="link") | covered |
| n15 | action | click | covered |
| n16 | object | web_element(label="Security clearance", tag="link") | covered |
| n17 | action | click | covered |
| n18 | object | web_element | covered |

## Why the translation failed

- n2/n3 (t1:s1): widened “Browse or search job listings in a user request represented in TRACE, without claiming search was executed” and searched “job posting employment vacancy occupational category information technology jobs”. `search_web` is the closest operation, but REQUEST-only execution semantics and the TRACE prohibition on bare Action statements make it invalid for representing the user's unexecuted requested work. `activity` can describe actions generally but does not provide the explicit job-search concept identified by the need. Proposed S1.
- n4/n5 (t1:s1): widened “Filter job search results in the user's requested behavior, not as a falsely recorded completed operation” and “A requested Security clearance certificate filter criterion for job postings”. `select_filter` and `apply_filters` are operations for an existing UI, not the unexecuted request; `requirement` describes a required property but does not specify the job-posting-filter relation or credential criterion. Proposed S2.
- The widened searches for n12 (Filters link), n14 (Certificates link), and n16 (Security clearance link) returned `web_element`, whose definition covers the supplied visible label and element role. These needs are represented by the existing constructor, notwithstanding `rag check`'s DECL results for them; they are not glossary gaps.

## Translation report

- Input kind: conversation (a user request followed by a supplied agent trace)
- Coverage status: partial
- Source-span coverage: t1:s1 and all observed agent actions at t2:s2, t2:s4, t2:s6, t2:s8, t2:s10, and t2:s12 are represented in source order.
- Opaque-text spans: none; exact search/UI labels are retained in query or UI-element fields.
- Label-preserved spans: none.
- Missing constructs: S1 job_search TERM constructor; S2 job_posting_filter TERM constructor.
- Unresolved ambiguities: none
- Check: `rag check` reports DECL for n2, n4, n5, n12, n14, and n16, and lists `job_search` and `job_posting_filter` as proposed unknown symbols. It marks n3 OK via `role_user`, which does not express the IT-jobs object; n3 is therefore correctly marked proposed via S1. Needs n12/n14/n16 are represented by the existing `web_element` contract despite the checker's DECL results.
