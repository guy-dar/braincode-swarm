Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM requirement(property="certificate", value="Security clearance") -> requirement_2 : TERM
    TERM job_search(criteria=[requirement_2], query="IT jobs") -> job_search_2 : TERM # PROPOSED: S1
    CLAIM request(target=job_search_2) BY role_user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM # PROPOSED: S1 (target depends on proposed constructor)
  }
  TURN t2 SPEAKER=AGENT {
    TERM web_element(label="Search by job title, skill or company", tag="searchbox") -> web_element_2 : TERM
    RECORD ACTION type_text(target=web_element_2, text="IT jobs") STATUS attempted SOURCE "t2:s2" -> type_text_event : EVENT
    TERM web_element(label="Search", tag="button") -> web_element_3 : TERM
    RECORD ACTION click(target=web_element_3) STATUS attempted SOURCE "t2:s4" -> click_event : EVENT
    TERM web_element(label=" Filters", tag="link") -> web_element_4 : TERM
    RECORD ACTION click(target=web_element_4) STATUS attempted SOURCE "t2:s6" -> click_event_2 : EVENT
    TERM web_element(label="Certificates", tag="link") -> web_element_5 : TERM
    RECORD ACTION click(target=web_element_5) STATUS attempted SOURCE "t2:s8" -> click_event_3 : EVENT
    TERM web_element(label="Security clearance", tag="link") -> web_element_6 : TERM
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
| n2 | action | job_search (PROPOSED: S1) | proposed |
| n3 | object | job_search(query="IT jobs") (PROPOSED: S1) | proposed |
| n4 | action | job_search(criteria=[requirement_2]) (PROPOSED: S1) | proposed |
| n5 | constraint | requirement(property="certificate", value="Security clearance") | covered |
| n6 | action | RECORD ACTION type_text | covered |
| n7 | object | web_element | covered |
| n8 | object | type_text(text="IT jobs") | covered |
| n9 | action | RECORD ACTION click | covered |
| n10 | object | web_element | covered |
| n11 | action | RECORD ACTION click | covered |
| n12 | object | web_element | covered |
| n13 | action | RECORD ACTION click | covered |
| n14 | object | web_element | covered |
| n15 | action | RECORD ACTION click | covered |
| n16 | object | web_element | covered |
| n17 | action | RECORD ACTION click | covered |
| n18 | object | web_element | covered |

## Why the translation failed

- n2: `widen "Browse or search job listings" --kind action` and `search "catalog query description criteria"` returned `search_web`, `search_travel`, and `search_transit`. These are executable operations, not a TERM describing the user's requested search. RECORD would falsely turn the user's request into an observed operation. `activity` has no reviewed search-specific verb or criteria argument. S1 supplies a non-executing search description.
- n3: `widen "IT jobs" --kind object`, `search "information technology job listings"`, and `search "job posting occupation domain"` returned unrelated resources, role descriptors, `topic_school_work_routine`, and unresolved domain labels. None identifies employment postings selected by this query. S1 explicitly identifies employment listings and exposes the exact search query; it does not invent a bare entity symbol or concatenate a sentence into an atom.
- n4: `widen "Filter job search results" --kind action` and `search "describe search jobs by occupation and certificate requirement"` returned `select_filter`, `apply_filters`, `search_web`, and `requirement`. The first three are operations, inappropriate for the requested behavior in a TRACE; `requirement` represents the constraint but not its governance over search results. S1 supplies the search's governed criteria.
- n5 was also widened: `widen "Filter by Security clearance certificate" --kind constraint`, `search "Security clearance certificate filter"`, and `search "credential certificate required property"`. `driver_license` and `vehicle_allowance` have the wrong meanings. Existing `requirement` suffices for the named certificate criterion when attached to the proposed search description; no new certificate entity is necessary.

## Translation report

- Pinned release: BrainCode 19.0.0-draft.2-lexical-groups; glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6).
- Input kind: conversation containing a user request and a recorded UI action trajectory.
- Coverage status: partial under the current release; the suggested document depends on S1 for n2–n4.
- Source-span coverage: t1:s1 is represented by a requested search plus its certificate criterion, conditional on S1; t2:s2, s4, s6, s8, s10, and s12 are represented as ordered recorded attempts. t2:s1, s3, s5, s7, s9, and s11 are list ordinals only; their order is retained, without inventing messages or events for them.
- Opaque-text spans: none. UI labels, category names, the certificate name, and the typed query are exact literals in defined roles, not prose fallbacks.
- Label-preserved spans: none using open lexical groups. The exact query is retained without asserting inferred taxonomy or expanding the abbreviation IT.
- Missing constructs: S1 job_search, a structured, non-executing employment-search description with governed criteria.
- Unresolved ambiguities: the source contains no tool outcomes or returned job postings. Attempts are recorded, not successes; no result-set contents, effective filter state, or achieved user goal is inferred. The bracketed UI kinds are source-supplied descriptors, not independently verified HTML tag names.
- Proposed glossary/spec changes: S1 only; no grammar or type changes. S1 is proposed vocabulary, not accepted canonical vocabulary.
- Check: `rag check` found one unknown symbol, `job_search` (proposed S1), and no unbound-value, invalid-group, retired-symbol, or quoted-entity warning. It marked six needs declaration-only (n2, n4, n5, n12, n14, n16); the table explicitly locates them in the suggested code. Its apparent n3 match through role_user does not semantically cover IT jobs: n3 remains proposed here. The unknown constructor makes this a failed translation regardless of the check's candidate-based coverage matches.
