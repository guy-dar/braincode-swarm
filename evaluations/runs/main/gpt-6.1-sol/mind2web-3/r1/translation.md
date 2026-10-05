Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM measure(amount=600, unit=unit_watt) -> measure_2 : TERM # PROPOSED: S1
    TERM at_least(measure=measure_2) -> at_least_2 : TERM
    TERM requirement(property="power_output", value=at_least_2) -> requirement_2 : TERM
    TERM search_request(target=object_label::psu, constraints=[requirement_2], limit=1, rank_direction=dir_asc, rank_field=rank_price) -> search_request_2 : TERM # PROPOSED: S2
    CLAIM request(target=search_request_2) BY role_user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT {
    TERM web_element(label="Search Site") -> web_element_2 : TERM
    CLAIM role(role_type="searchbox", subject=web_element_2) BY role_agent STATUS observed SOURCE "t2:s2" -> role_2 : CLAIM
    RECORD ACTION type_text(target=web_element_2, text="600w power supply") STATUS attempted SOURCE "t2:s2" -> type_text_event : EVENT
    TERM web_element(label="") -> web_element_3 : TERM
    CLAIM role(role_type="button", subject=web_element_3) BY role_agent STATUS observed SOURCE "t2:s4" -> role_3 : CLAIM
    RECORD ACTION click(target=web_element_3) STATUS attempted SOURCE "t2:s4" -> click_event : EVENT
    TERM web_element(label="600 W") -> web_element_4 : TERM
    CLAIM role(role_type="generic", subject=web_element_4) BY role_agent STATUS observed SOURCE "t2:s6" -> role_4 : CLAIM
    RECORD ACTION click(target=web_element_4) STATUS attempted SOURCE "t2:s6" -> click_event_2 : EVENT
    TERM web_element(label="Featured Items ") -> web_element_5 : TERM
    CLAIM role(role_type="combobox", subject=web_element_5) BY role_agent STATUS observed SOURCE "t2:s8" -> role_5 : CLAIM
    RECORD ACTION select_option(target=web_element_5, value="Lowest Price") STATUS attempted SOURCE "t2:s8" -> select_option_event : EVENT
    TERM web_element(label="Hercules DUAL FAN 600w-Max ATX Power Supply SATA, ...", tag="img") -> web_element_6 : TERM
    RECORD ACTION click(target=web_element_6) STATUS attempted SOURCE "t2:s11" -> click_event_3 : EVENT
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | search_request (PROPOSED: S2), request | proposed |
| n2 | object | object_label::psu | label-preserved |
| n3 | constraint | search_request (PROPOSED: S2), rank_price, dir_asc | proposed |
| n4 | constraint | measure, unit_watt (PROPOSED: S1), at_least, requirement | proposed |
| n5 | action | RECORD ACTION type_text | covered |
| n6 | object | web_element, role | covered |
| n7 | constraint | type_text.text="600w power supply" | covered |
| n8 | action | RECORD ACTION click | covered |
| n9 | object | web_element, role | covered |
| n10 | action | RECORD ACTION click | covered |
| n11 | object | web_element(label="600 W"), role | covered |
| n12 | action | RECORD ACTION select_option | covered |
| n13 | object | web_element, role | covered |
| n14 | constraint | select_option.value="Lowest Price" | covered |
| n15 | action | RECORD ACTION click | covered |
| n16 | object | web_element(label="Hercules DUAL FAN 600w-Max ATX Power Supply SATA, ...", tag="img") | covered |

## Why the translation failed

- n4: `search "watt power output unit"`, `search "watts SI power measurement"`, and `widen "At least 600W power output"` returned measure and units for mass, volume, temperature, distance, or time, but no power unit. Those units cannot denote watts. A targeted glossary grep for watt/power output found no entry. Proposed S1 supplies the missing interpreted unit, not a number-specific symbol.
- n1, n3: `search "describe requested search action with target and constraints"`, `search "descriptive search query criteria ordering"`, `search "minimum price selection cheapest product"`, `search "search goal lowest price among qualifying products"`, and `widen "Find cheapest product described search request ordered by ascending price"` returned request, search_web, sort, rank_price and dir_asc. request accepts a TERM but does not construct the search's structured meaning. search_web and sort are executable operations, not action-description constructors; TRACE cannot use them as bare actions or falsely record the user's request as a completed search. activity lacks criteria, ordering and selection arguments. Proposed S2 describes the search goal without claiming execution.

## Translation report

- Pinned release: specification 19.0.0-draft.2-lexical-groups; glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6).
- Input kind: conversation with recorded UI trajectory.
- Coverage status: partial under the current release; suggested document depends on S1 and S2 being accepted.
- Source-span coverage: t1:s1 is represented by the requested goal and its constraints, conditional on acceptance. t2:s2, s4, s6 and s8 are recorded in source order. t2:s10 supplies the product image's exact identifying label; t2:s11 supplies its click. t2:s1, s3, s5, s7 and s9 are step-number scaffolding, preserved by operation order rather than independent propositions.
- Opaque-text spans: none. UI labels, icon glyphs, option wording and typed text are exact operation arguments or identifiers, not prose fallback.
- Label-preserved spans: t1:s1 "power supply unit" → object_label::psu, an acronym for that source object-kind phrase; no inferred properties, synonym registry or English sense is supplied by this open label. Its output-power constraint is represented separately; its electrical engineering definition is not resolved.
- Missing constructs: S1 unit_watt; S2 search_request constructor. Neither proposal is currently accepted vocabulary.
- Unresolved ambiguities: the source does not specify the meaning of the UI's exact "600 W" facet (equality, threshold, or another classification), whether "600w-Max" establishes continuous output, or whether the selected listing actually meets the request. No such conclusion is asserted. The image label is truncated in the source and remains truncated here; no hidden product properties are reconstructed.
- Event outcomes: attempted records preserve the supplied operations without claiming successful input, navigation, selection, satisfaction of the request, or purchase. No reasoning links are invented from action order.
- Proposed glossary/spec changes: S1 and S2 only; no grammar changes.
- Check: `rag check --translation /output/translation.md` reported no unresolved need rows, n2 as label-preserved, and two vocabulary warnings: unknown TERM constructor search_request (S2) and unbound attribute value unit_watt (S1). Its lexical coverage matches do not establish that the request is expressible; the semantic gaps above remain.
