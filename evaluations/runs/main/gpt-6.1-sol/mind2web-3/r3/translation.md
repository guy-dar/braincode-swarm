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
    TERM search_selection(target=lexical_label_2, constraints=[requirement_2], limit=1, rank_direction=dir_asc, rank_field=rank_price) -> search_selection_2 : TERM # PROPOSED: S2
    CLAIM request(target=search_selection_2) BY role_user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT {
    TERM web_element(label="Search Site", tag="searchbox") -> web_element_2 : TERM
    RECORD ACTION type_text(target=web_element_2, text="600w power supply") STATUS attempted SOURCE "t2:s2" -> type_text_event : EVENT
    TERM web_element(label="\uf002", tag="button") -> web_element_3 : TERM
    RECORD ACTION click(target=web_element_3) STATUS attempted SOURCE "t2:s4" -> click_event : EVENT
    TERM web_element(label="600 W", tag="generic") -> web_element_4 : TERM
    RECORD ACTION click(target=web_element_4) STATUS attempted SOURCE "t2:s6" -> click_event_2 : EVENT
    TERM web_element(label="Featured Items \uf0d7", tag="combobox") -> web_element_5 : TERM
    RECORD ACTION select_option(target=web_element_5, value="Lowest Price") STATUS attempted SOURCE "t2:s8" -> select_option_event : EVENT
    TERM web_element(label="Hercules DUAL FAN 600w-Max ATX Power Supply SATA, ...", tag="img") -> web_element_6 : TERM
    RECORD ACTION click(target=web_element_6) STATUS attempted SOURCE "t2:s11" -> click_event_3 : EVENT
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | search_selection (PROPOSED: S2), request | proposed |
| n2 | object | lexical_label, object_label::psu | label-preserved |
| n3 | constraint | search_selection (PROPOSED: S2), rank_price, dir_asc, limit=1 | proposed |
| n4 | constraint | measure, unit_watt (PROPOSED: S1), at_least, requirement | proposed |
| n5 | action | RECORD ACTION type_text | covered |
| n6 | object | web_element_2: web_element | covered |
| n7 | constraint | type_text.text="600w power supply" | covered |
| n8 | action | RECORD ACTION click: click_event | covered |
| n9 | object | web_element_3: web_element | covered |
| n10 | action | RECORD ACTION click: click_event_2 | covered |
| n11 | object | web_element_4: web_element | covered |
| n12 | action | RECORD ACTION select_option | covered |
| n13 | object | web_element_5: web_element | covered |
| n14 | constraint | select_option.value="Lowest Price" | covered |
| n15 | action | RECORD ACTION click: click_event_3 | covered |
| n16 | object | web_element_6: web_element | covered |

## Why the translation failed

- n4: `search "watt power unit"`, `search "electrical power watt"`, and `widen "At least 600W power output" --kind constraint` found `measure`, `at_least`, and units for temperature, mass, volume and time, but no watt unit. `grep` for watt/power_output in the fallback glossary found no match. S1 supplies the missing defined unit; 600 is an argument, not part of the symbol.
- n1 and n3: `widen "Find or search for a product" --kind action`, `widen "Cheapest / lowest price" --kind constraint`, and searches for "search action description query term", "sort description selection minimum", "structured description search criteria cheapest product", and "minimum price selection requirement" found `search_web`, `sort`, `rank_price`, `dir_asc`, `request`, and generic `activity`. Executable search/sort cannot appear bare in a TRACE, and recording them would falsely assert agent operations. `activity` has no criteria, ordering or selection parameters; its general verb slot does not define this compound requested behavior. `constraint_budget_limited` means neither a minimum price nor a numerical ceiling. S2 supplies a structured non-executable search-and-selection description with independently exposed arguments.

## Translation report

- Pinned release: specification 19.0.0-draft.2-lexical-groups; glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6).
- Input kind: conversation with recorded UI actions.
- Coverage status: partial under the current release; suggested document requires S1 and S2.
- Source-span coverage: t1:s1 preserves the original request separately from t2's operations. t2:s2, s4, s6, s8 and s10–s11 describe five attempted operations and their UI targets; t2:s1, s3, s5, s7 and s9 are ordinal list markers, represented by operation order rather than substantive claims. The product label at t2:s10 supplies the target for the click at t2:s11.
- Opaque-text spans: none; search text and UI labels are exact operation operands/identifiers, not prose substitutes for propositions.
- Label-preserved spans: t1:s1 "power supply unit" → object_label::psu; psu is an opaque object-kind handle, not a definition of electrical capabilities. Power output is separately constrained.
- Missing constructs: S1 unit_watt; S2 search_selection.
- Unresolved ambiguities: no tool outcomes are supplied, so attempted does not mean succeeded. The "600 W" UI filter is recorded literally; it is not assumed to implement the user's at-least condition. The truncated product label does not establish actual output power, cheapest status, availability, or successful task completion. UI role strings preserve source annotations without inferring selectors or HTML tags.
- Proposed glossary/spec changes: S1 and S2 in /output/suggestions.md; no spec change proposed.
- Check: `rag check --translation /output/translation.md` reports 0 unresolved need rows; n2 is label-preserved, n7/n13/n16 are declared coverage. It flags the proposed constructor search_selection as not in the glossary and proposed unit_watt as an unbound attribute value. These two missing entries prevent current-release validity despite the lexical coverage heuristic finding matches for n1/n3/n4. No other warning lines were reported.
