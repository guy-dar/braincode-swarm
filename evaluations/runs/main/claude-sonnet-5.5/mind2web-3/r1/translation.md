Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="psu") -> subject_2 : TERM
    TERM requirement(property="rank_field", value=rank_price) -> requirement_2 : TERM
    TERM requirement(property="rank_direction", value=dir_asc) -> requirement_3 : TERM
    TERM measure(amount=600, unit=unit_watt) -> measure_2 : TERM   # PROPOSED: S1
    TERM at_least(measure=measure_2) -> at_least_2 : TERM
    TERM requirement(property="power_output", value=at_least_2) -> requirement_4 : TERM
    UTTER ask(constraints=[requirement_2, requirement_3, requirement_4], topic=subject_2)
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM web_element(label="Search Site", tag="searchbox") -> web_element_2 : TERM
    RECORD ACTION type_text(target=web_element_2, text="600w power supply") STATUS attempted SOURCE "t2:s2" -> type_text_event : EVENT
    TERM web_element(label="", tag="button") -> web_element_3 : TERM
    RECORD ACTION click(target=web_element_3) STATUS attempted SOURCE "t2:s4" -> click_event : EVENT
    TERM web_element(label="600 W", tag="generic") -> web_element_4 : TERM
    RECORD ACTION click(target=web_element_4) STATUS attempted SOURCE "t2:s6" -> click_event_2 : EVENT
    TERM web_element(label="Featured Items", tag="combobox") -> web_element_5 : TERM
    RECORD ACTION select_option(target=web_element_5, value="Lowest Price") STATUS attempted SOURCE "t2:s8" -> select_option_event : EVENT
    TERM web_element(label="Hercules DUAL FAN 600w-Max ATX Power Supply SATA", tag="img") -> web_element_6 : TERM
    RECORD ACTION click(target=web_element_6) STATUS attempted SOURCE "t2:s11" -> click_event_3 : EVENT
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | ask, subject | covered |
| n2 | object | subject | covered |
| n3 | constraint | requirement, rank_price, dir_asc | covered |
| n4 | constraint | at_least, measure, requirement, unit_watt (PROPOSED: S1) | proposed |
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

- n4 "600W": search unit watt/power → only unit_fahrenheit, unit_gram, unit_liter, unit_percent, cap_gb; none is a power unit. measure.unit requires a unit value, so a quoted "W" is not valid. Proposed S1.

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: t1:s1–t2:s11 represented; step numbers t2:s1,s3,s5,s7,s9 are markers only
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: S1 unit_watt
- Unresolved ambiguities: "psu" used as quoted kind in subject since no lowercase-word group slot fits topic; agent click statuses set to attempted (outcomes not in source); empty button label.
- Check: not rerun after final edit; expected 1 unknown symbol (unit_watt, proposed)
