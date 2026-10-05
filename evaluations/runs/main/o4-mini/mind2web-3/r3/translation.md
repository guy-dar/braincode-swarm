Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM measure(amount=600, unit=unit_watt) -> measure_2 : TERM  # PROPOSED: S1
    TERM requirement(property="power_output", value=measure_2) -> requirement_power_2 : TERM  # PROPOSED: S1
    TERM requirement(property="price", value=rank_price) -> requirement_price_2 : TERM
    UTTER ask(target=object_label::power_supply_unit, constraints=[requirement_price_2, requirement_power_2])
  }
  TURN t2 SPEAKER=AGENT {
    RECORD ACTION type_text(target=web_element(label="Search Site"), text="600w power supply") STATUS succeeded SOURCE "t2:s2" -> type_text_event : EVENT
    RECORD ACTION click(target=web_element(label="", tag="button")) STATUS succeeded SOURCE "t2:s4" -> click_event : EVENT
    RECORD ACTION click(target=web_element(label="600 W")) STATUS succeeded SOURCE "t2:s6" -> click_event_2 : EVENT
    RECORD ACTION select_option(target=web_element(label="Featured Items", tag="combobox"), value="Lowest Price") STATUS succeeded SOURCE "t2:s8" -> select_option_event : EVENT
    RECORD ACTION click(target=web_element(label="Hercules DUAL FAN 600w-Max ATX Power Supply SATA")) STATUS succeeded SOURCE "t2:s11" -> click_event_3 : EVENT
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | type_text, click, select_option | covered |
| n2 | object | object_label::power_supply_unit | covered |
| n3 | constraint | requirement(property="price", ...) | covered |
| n4 | constraint | requirement(property="power_output", ...) | proposed |

## Why the translation failed

- n4 "At least 600W power output": need a unit-value `unit_watt` to construct a measure(amount=600, unit=unit_watt). No such symbol exists in the glossary.

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: t1:s1 and t2:s2–t2:s11 represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: unit_watt (value for electrical power unit)
- Unresolved ambiguities: none
- Check: `rag check` reported 1 unresolved need (n4), 0 unknown symbols
