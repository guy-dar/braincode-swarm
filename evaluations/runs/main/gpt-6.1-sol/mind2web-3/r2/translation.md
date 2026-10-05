Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM lexical_label(value=object_label::psu) -> lexical_label_2 : TERM
    TERM measure(amount=600, unit=unit_watt) -> measure_2 : TERM # PROPOSED: S1
    TERM at_least(measure=measure_2) -> at_least_2 : TERM
    TERM requirement(property="power_output", value=at_least_2) -> requirement_2 : TERM
    TERM search_description(target=lexical_label_2, best_only=TRUE, constraints=[requirement_2], rank_direction=dir_asc, rank_field=rank_price) -> search_description_2 : TERM # PROPOSED: S2
    CLAIM request(target=search_description_2) BY role_user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT {
    TERM web_element(label="Search Site", tag="searchbox") -> web_element_2 : TERM
    RECORD ACTION type_text(target=web_element_2, text="600w power supply") STATUS unknown SOURCE "t2:s2" -> type_text_event : EVENT
    TERM web_element(label="", tag="button") -> web_element_3 : TERM
    RECORD ACTION click(target=web_element_3) STATUS unknown SOURCE "t2:s4" -> click_event : EVENT
    TERM web_element(label="600 W", tag="generic") -> web_element_4 : TERM
    RECORD ACTION click(target=web_element_4) STATUS unknown SOURCE "t2:s6" -> click_event_2 : EVENT
    TERM web_element(label="Featured Items ", tag="combobox") -> web_element_5 : TERM
    RECORD ACTION select_option(target=web_element_5, value="Lowest Price") STATUS unknown SOURCE "t2:s8" -> select_option_event : EVENT
    TERM web_element(label="Hercules DUAL FAN 600w-Max ATX Power Supply SATA, ...", tag="img") -> web_element_6 : TERM
    RECORD ACTION click(target=web_element_6) STATUS unknown SOURCE "t2:s11" -> click_event_3 : EVENT
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | search_description (PROPOSED: S2), request | proposed |
| n2 | object | lexical_label, object_label::psu | label-preserved |
| n3 | constraint | search_description (PROPOSED: S2), rank_price, dir_asc, best_only=TRUE | proposed |
| n4 | constraint | measure, unit_watt (PROPOSED: S1), at_least, requirement | proposed |
| n5 | action | RECORD ACTION type_text | covered |
| n6 | object | web_element(label="Search Site", tag="searchbox") | covered |
| n7 | constraint | type_text(text="600w power supply") | covered |
| n8 | action | RECORD ACTION click, click_event | covered |
| n9 | object | web_element(label="", tag="button") | covered |
| n10 | action | RECORD ACTION click, click_event_2 | covered |
| n11 | object | web_element(label="600 W", tag="generic") | covered |
| n12 | action | RECORD ACTION select_option | covered |
| n13 | object | web_element(label="Featured Items ", tag="combobox") | covered |
| n14 | constraint | select_option(value="Lowest Price") | covered |
| n15 | action | RECORD ACTION click, click_event_3 | covered |
| n16 | object | web_element with exact supplied product-image label | covered |

## Why the translation failed

- n4: `search "watt power output unit"`, `search "minimum electrical power watt"`, and `widen "At least 600W power output" --kind constraint` found `measure`, `at_least`, and units for temperature, mass, volume, time and capacity, but no power unit. `grep` for watt/power_output in `/reference/glossary.md` also found nothing. `unit_fahrenheit`, `unit_gram` and `cap_gb` have incompatible dimensions; a bare "W" cannot supply a pinned unit definition. S1 supplies the missing watt definition; the bound and required-property structure already exist.
- n1, n3: `search "describe a requested search action with target constraints cheapest"`, `search "search action description constructor"`, `search "describe search lowest price requested operation"`, `search "cheapest minimum price constraint"`, `widen "Find or search for a product" --kind action`, and `widen "Cheapest lowest price" --kind constraint` found `search_web`, `sort`, `activity`, `request`, `rank_price` and `dir_asc`. Executing `search_web`/`sort` inside TRACE would be invalid, and recording them would falsely claim that the user performed a search. `request` needs an independently described target; `activity` has no governed search/filter/ranking/optimal-selection parameters. Ranking alone also does not restrict the requested answer to the cheapest qualifying candidate. S2 supplies a non-executing, structured search description with explicit optimal selection.

## Translation report

- Pinned release: specification 19.0.0-draft.2-lexical-groups; glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6).
- Input kind: conversation containing a user request and a supplied agent UI-action trace.
- Coverage status: partial under the current release; suggested document requires S1 and S2.
- Source-span coverage: t1:s1 is represented subject to S1/S2; agent operations and their arguments at t2:s2, t2:s4, t2:s6, t2:s8, t2:s10 and t2:s11 are represented in source order. t2:s1, t2:s3, t2:s5, t2:s7 and t2:s9 are step-number formatting, not additional messages or claims.
- Opaque-text spans: none. Search text, UI labels/icons, option text and the truncated product name are exact operation operands/identifiers, not prose fallbacks.
- Label-preserved spans: t1:s1 "power supply unit" → object_label::psu, the abbreviated object-kind label identified in the retrieved need; no electrical capabilities or other properties are inferred from the label. The power requirement is encoded separately.
- Missing constructs: S1 unit_watt; S2 search_description.
- Unresolved ambiguities: no tie-breaking rule or price domain/currency is supplied; none is invented. The product label is truncated, and the selected product's actual output, price and optimality are not established. In particular, "600w-Max" is not promoted to proof of meeting the user's minimum output.
- Event interpretation: the trace supplies operations but no tool outcomes; STATUS unknown preserves this limitation. No successful search, filter application, resulting sort order, purchase or completed answer is asserted. Element tag values preserve the source's bracketed UI-kind tags, without reconstructing selectors or hidden DOM structure.
- Proposed glossary/spec changes: S1 and S2 in `/output/suggestions.md`; no spec change proposed.
- Check: `rag check --translation /output/translation.md` reported no unresolved need rows, n2 as label-only, one unknown constructor (`search_description`, S2), and one unbound/non-glossary attribute value (`unit_watt`, S1). These are declared proposals, not admitted vocabulary; lexical heuristic coverage does not establish that the current glossary can express n1/n3/n4 faithfully.
