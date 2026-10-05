Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM measure(amount=600, unit="W") -> power_measure : TERM
    TERM at_least(measure=power_measure) -> min_power_constraint : TERM
    UTTER ask(constraints=[min_power_constraint], target=object_label::psu, topic="cheapest")
  }
  
  TURN t2 SPEAKER=AGENT {
    TERM web_element(label="Search Site", tag="searchbox") -> search_box : TERM
    RECORD ACTION type_text(target=search_box, text="600w power supply") STATUS succeeded SOURCE "t2:s2" -> type_text_event : EVENT
    
    TERM web_element(label="submit", tag="button") -> search_button : TERM
    RECORD ACTION click(target=search_button) STATUS succeeded SOURCE "t2:s4" -> search_button_click_event : EVENT
    
    TERM web_element(label="600 W") -> power_filter : TERM
    RECORD ACTION click(target=power_filter) STATUS succeeded SOURCE "t2:s6" -> filter_click_event : EVENT
    
    TERM web_element(label="Featured Items", tag="combobox") -> sort_combobox : TERM
    RECORD ACTION select_option(target=sort_combobox, value="Lowest Price") STATUS succeeded SOURCE "t2:s8" -> sort_select_event : EVENT
    
    TERM web_element(label="Hercules DUAL FAN 600w-Max ATX Power Supply SATA product listing", tag="img") -> product_listing : TERM
    RECORD ACTION click(target=product_listing) STATUS succeeded SOURCE "t2:s11" -> product_click_event : EVENT
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | ask, type_text, click, select_option | covered |
| n2 | object | object_label::psu | label-preserved |
| n3 | constraint | topic (cheapest) | covered |
| n4 | constraint | at_least, measure | covered |
| n5 | action | type_text | covered |
| n6 | object | web_element | covered |
| n7 | constraint | type_text text parameter | covered |
| n8 | action | click | covered |
| n9 | object | web_element | covered |
| n10 | action | click | covered |
| n11 | object | web_element | covered |
| n12 | action | select_option | covered |
| n13 | object | web_element | covered |
| n14 | constraint | select_option value parameter | covered |
| n15 | action | click | covered |
| n16 | object | web_element | label-preserved |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1, t2:s2 (type_text), t2:s4 (click search), t2:s6 (click filter), t2:s8 (select sort), t2:s10–t2:s11 (click product) is represented
- Opaque-text spans: none
- Label-preserved spans: object_label::psu (open-group label for "power supply unit"), web_element descriptors for product listing and button
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
