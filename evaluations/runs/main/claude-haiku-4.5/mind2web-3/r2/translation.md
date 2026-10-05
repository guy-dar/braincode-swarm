Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM measure(amount=600, unit="W") -> power_spec : TERM
    TERM at_least(measure=power_spec) -> power_constraint : TERM
    UTTER ask(target=object_label::psu, constraints=[power_constraint])
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM web_element(label="Search Site") -> searchbox : TERM
    RECORD ACTION type_text(target=searchbox, text="600w power supply") STATUS succeeded SOURCE "t2:s2" -> type_text_event : EVENT
    TERM web_element(label="search button") -> search_button : TERM
    RECORD ACTION click(target=search_button) STATUS succeeded SOURCE "t2:s4" -> click_search_event : EVENT
    TERM web_element(label="600 W") -> filter_element : TERM
    RECORD ACTION click(target=filter_element) STATUS succeeded SOURCE "t2:s6" -> click_filter_event : EVENT
    TERM web_element(label="Featured Items") -> combobox : TERM
    RECORD ACTION select_option(target=combobox, value="Lowest Price") STATUS succeeded SOURCE "t2:s8" -> select_option_event : EVENT
    TERM web_element(label="Hercules DUAL FAN 600w-Max ATX Power Supply SATA") -> product : TERM
    RECORD ACTION click(target=product) STATUS succeeded SOURCE "t2:s11" -> click_product_event : EVENT
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | object_label | label-preserved |
| n2 | object | object_label | label-preserved |
| n3 | constraint | select_option | covered |
| n4 | constraint | at_least, measure | covered |
| n5 | action | type_text, web_element | covered |
| n6 | object | web_element | label-preserved |
| n7 | constraint | type_text | label-preserved |
| n8 | action | click | covered |
| n9 | object | web_element | label-preserved |
| n10 | action | click | covered |
| n11 | object | web_element | label-preserved |
| n12 | action | select_option | covered |
| n13 | object | web_element | label-preserved |
| n14 | constraint | select_option | covered |
| n15 | action | click | covered |
| n16 | object | web_element | label-preserved |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: Every segment t1:s1 through t2:s11 is represented
- Opaque-text spans: none
- Label-preserved spans: n1, n2, n6, n7, n9, n11, n13, n16 — n1 user's expressed search request via UTTER and object_label::psu; n2 generic PSU category (open-group label); n6, n9, n11, n13, n16 are web UI element labels via web_element constructor; n7 is the literal search text preserved in type_text. These are preserved through language constructs and open-group labels rather than fully resolved glossary senses
- Missing constructs: none (web UI element labels are semantically preserved via web_element constructor and open-group labels; literal search text preserved in type_text action)
- Unresolved ambiguities: none
