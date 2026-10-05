Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    UTTER ask(topic="power supply unit with at least 600W power output, cheapest price")
  }
  TURN t2 SPEAKER=AGENT {
    RECORD ACTION type_text(target=web_element(label="Search Site"), text="600w power supply") STATUS succeeded SOURCE "t2:s2" -> type_text_event : EVENT
    RECORD ACTION click(target=web_element(label="search button")) STATUS succeeded SOURCE "t2:s4" -> click_search_event : EVENT
    RECORD ACTION click(target=web_element(label="600 W")) STATUS succeeded SOURCE "t2:s6" -> click_filter_event : EVENT
    RECORD ACTION select_option(target=web_element(label="Featured Items"), value="Lowest Price") STATUS succeeded SOURCE "t2:s8" -> select_option_event : EVENT
    RECORD ACTION click(target=web_element(label="Hercules DUAL FAN 600w-Max ATX Power Supply SATA")) STATUS succeeded SOURCE "t2:s11" -> click_product_event : EVENT
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | UTTER | covered |
| n2 | object | UTTER topic string | label-preserved |
| n3 | constraint | UTTER topic string | label-preserved |
| n4 | constraint | UTTER topic string (unit_watt missing, S1 proposed) | proposed |
| n5 | action | type_text, web_element | covered |
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

- n4 "At least 600W power output": The proper formal expression would be `TERM at_least(measure=TERM measure(amount=600, unit=unit_watt))`, but there is no power unit (unit_watt, unit_kilowatt, or similar) in the glossary.
  - Searches tried:
    - `rag search "600W power output"` → no power unit found
    - `rag search "watt unit"` → returns only mass, duration, temperature units; no power unit
    - `rag widen "power output unit"` → found unit_kilometer but no electrical power unit
    - `grep -i "watt\|power.*unit" /reference/glossary.md` → no matches
  - The constraint "at least 600W" cannot be fully expressed without a power unit for the measure constructor
  - I marked this as proposed (need S1: unit_watt)

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: Every source segment from t1:s1 through t2:s11 is represented:
  - t1:s1 (user request) → UTTER ask in turn t1
  - t2:s2-t2:s11 (agent actions) → RECORD ACTION statements for type_text, click, select_option, click
- Opaque-text spans: t1:s1 — The user's three constraints ("cheapest", "at least 600W", "power supply unit") are preserved as natural language in the UTTER topic string rather than formally encoded:
  - "power supply unit" (n2) should be object_label::power_supply_unit but is embedded in topic
  - "cheapest / lowest price" (n3) should be rank_price + dir_asc but these belong to a sort operation on results, not a request
  - "at least 600W" (n4) should be `at_least(measure=measure(amount=600, unit=unit_watt))` but unit_watt does not exist
- Label-preserved spans: n2 "power supply unit", n3 "cheapest", n4 "600W" — all preserved as natural language labels within the UTTER topic
- Missing constructs: S1 — unit_watt (or unit_kilowatt, or a general power unit) to enable `measure(amount=600, unit=unit_watt)` for the at_least constructor in n4
- Unresolved ambiguities: None
- Check: `rag check --translation /output/translation.md` confirms that web_element and the recorded operations are all in the glossary; the only missing symbol is unit_watt (proposed as S1).
```
