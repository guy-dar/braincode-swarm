Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM job_postings(field=employment_field_label::it) -> job_postings_2 : TERM # PROPOSED: S1, S2
    TERM certificate_filter(name="Security clearance") -> certificate_filter_2 : TERM # PROPOSED: S3
    TERM catalog_query(target=job_postings_2, criteria=[certificate_filter_2]) -> catalog_query_2 : TERM # PROPOSED: S4
    CLAIM request(target=catalog_query_2) BY role_user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
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
| n2 | action | catalog_query (PROPOSED: S4) | proposed |
| n3 | object | job_postings, employment_field_label::it (PROPOSED: S1, S2) | proposed |
| n4 | action | catalog_query.criteria (PROPOSED: S4) | proposed |
| n5 | constraint | certificate_filter (PROPOSED: S3) | proposed |
| n6 | action | RECORD ACTION type_text | covered |
| n7 | object | web_element | covered |
| n8 | object | type_text.text="IT jobs" | covered |
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

- n2: `widen "Browse or search job listings"` and `search "catalog query description criteria"` return search_web, search_travel and search_transit. These are executable operations, not TERM descriptions of a user's requested search inside TRACE. RECORD would falsely turn the request into an attempted operation. activity has no reviewed search/filter verb profile or criteria argument. S4 supplies a non-executing query description.
- n3: `widen "IT jobs"`, `search "information technology employment vacancies"`, `search "job postings constructor"`, `widen "employment field label information technology"` and `search "occupational field sector label"` return unrelated roles, tone_professional, subject, lexical_label, rank_field and platform_label. None describes employment listings qualified by an employment field. platform_label denotes software systems, not an occupational field; object_label cannot silently supply the job-posting/field relationship. S1 and S2 expose that relationship while preserving IT as a field label, without inventing an occupational taxonomy.
- n4: `widen "Filter job search results"` and `search "activity search filter verb"` return search_web, select_filter and apply_filters. They express operations, not a requested query description in this mode. S4 gives criteria their filtering scope without asserting that results were returned.
- n5: `widen "Filter by Security clearance certificate"`, `search "security clearance certificate requirement"` and `search "certificate filter credential"` return requirement, driver_license, vehicle_allowance and reservation-state filters. driver_license is a different credential; vehicle_allowance is a vehicle policy. requirement alone supplies neither an accepted certificate-filter property nor its meaning. S3 represents the explicitly named certificate filter, without claiming the user holds a clearance or inferring jurisdiction, issuer or clearance level.

## Translation report

- Pinned release: specification 19.0.0-draft.2-lexical-groups; glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6).
- Input kind: conversation with recorded UI actions.
- Coverage status: partial under the current release; suggested document requires S1–S4 to formalize the original request.
- Source-span coverage: t1:s1 is represented conditionally on the proposals; t2:s2, s4, s6, s8, s10 and s12 are represented with exact UI labels, element kinds and action arguments. t2:s1, s3, s5, s7, s9 and s11 are ordinal scaffolding preserved by event order, not separate semantic claims.
- Opaque-text spans: none; UI labels and typed text are exact literal objects, not sentence fallbacks.
- Label-preserved spans: proposed t1:s1 "IT" → employment_field_label::it, an opaque employment-field label. No automatic expansion of IT into an occupational definition is claimed. No currently accepted open labels are used.
- Missing constructs: S1 employment_field_label group; S2 job_postings constructor; S3 certificate_filter constructor; S4 catalog_query constructor.
- Unresolved ambiguities: no action outcomes or returned listings are supplied. Events are attempted, not succeeded; no successful filtering or result count is inferred. The site's certificate-filter matching semantics and any clearance jurisdiction/level are unspecified and not reconstructed.
- Proposed glossary/spec changes: S1–S4 in `/output/suggestions.md`; no grammar change.
- Check: `node /kit/rag.mjs check --translation /output/translation.md` reported three unknown constructors (catalog_query, certificate_filter, job_postings), the unbound/unknown group employment_field_label, and its invalid atom employment_field_label::it. These are exactly S1–S4. The checker marked n2, n4, n5, n12, n14 and n16 DECL (table-declared rather than candidate-matched); n12, n14 and n16 are already expressed by web_element's published visible-label signature, despite that symbol not appearing in their initial candidate lists. Its n3 match via role_user is not semantic coverage of IT jobs; n3 remains proposed. No success is claimed.
