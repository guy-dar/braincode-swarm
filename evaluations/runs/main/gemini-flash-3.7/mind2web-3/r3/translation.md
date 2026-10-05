Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM measure(amount=600, unit=unit_watt) -> measure_2 : TERM  # PROPOSED: S1
    TERM at_least(measure=measure_2) -> at_least_2 : TERM
    TERM requirement(property="power_output", value=at_least_2) -> requirement_2 : TERM
    TERM requirement(property="rank_direction", value=dir_asc) -> requirement_3 : TERM
    TERM requirement(property="rank_field", value=rank_price) -> requirement_4 : TERM
    TERM activity(object=object_label::psu, verb="find") -> activity_2 : TERM
    UTTER ask(target=activity_2, constraints=[requirement_2, requirement_3, requirement_4])
  }
  TURN t2 SPEAKER=AGENT {
    TERM web_element(label="Search Site", tag="searchbox") -> web_element_2 : TERM
    RECORD ACTION type_text(target=web_element_2, text="600w power supply") STATUS succeeded SOURCE "t2:s2" -> type_text_event : EVENT
    TERM web_element(label="", tag="button") -> web_element_3 : TERM
    RECORD ACTION click(target=web_element_3) STATUS succeeded SOURCE "t2:s4" -> click_event : EVENT
    TERM web_element(label="600 W", tag="generic") -> web_element_4 : TERM
    RECORD ACTION click(target=web_element_4) STATUS succeeded SOURCE "t2:s6" -> click_event_2 : EVENT
    TERM web_element(label="Featured Items ", tag="combobox") -> web_element_5 : TERM
    RECORD ACTION select_option(target=web_element_5, value="Lowest Price") STATUS succeeded SOURCE "t2:s8" -> select_option_event : EVENT
    TERM web_element(label="Hercules DUAL FAN 600w-Max ATX Power Supply SATA, ...", tag="img") -> web_element_6 : TERM
    RECORD ACTION click(target=web_element_6) STATUS succeeded SOURCE "t2:s11" -> click_event_3 : EVENT
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | ask, activity | covered |
| n2 | object | object_label::psu | label-preserved |
| n3 | constraint | dir_asc, rank_price, requirement | covered |
| n4 | constraint | at_least, measure, unit_watt (PROPOSED: S1) | proposed |
| n5 | action | type_text | covered |
| n6 | object | web_element | covered |
| n7 | constraint | type_text | covered |
| n8 | action | click | covered |
| n9 | object | web_element | covered |
| n10 | action | click | covered |
| n11 | object | web_element | covered |
| n12 | action | select_option | covered |
| n13 | object | web_element | covered |
| n14 | constraint | select_option | covered |
| n15 | action | click | covered |
| n16 | object | web_element | covered |

## Why the translation failed

- n4 "At least 600W power output": search "watt" → only capacity/duration/mass/temperature units (`cap_gb`, `unit_gram`, `unit_fahrenheit`); search "unit_watt" → no results; grep `unit-value` in `/reference/glossary.md` → only `unit_fahrenheit`, `unit_gram`, `unit_kilometer`, `unit_liter`, `unit_percent` exist. There is no standard SI unit of power in `unit-value`. Proposed S1 (`unit_watt`).

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: every segment t1:s1–t2:s11 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s1 "power supply unit" -> object_label::psu (label only; no sense resolved)
- Missing constructs: S1 unit_watt value
- Unresolved ambiguities: none
- Check: `rag check` reported 1 unresolved need (n4), 1 unknown symbol (unit_watt, proposed)
