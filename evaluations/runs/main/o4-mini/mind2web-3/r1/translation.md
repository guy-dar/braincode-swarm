Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM search_request(target=object_label::power_supply_unit, constraints=[
      at_least(measure(amount=600, unit="W"))
    ], rank_field=rank_price, rank_direction=dir_asc) -> search_request_2 : TERM  # PROPOSED: S1
    UTTER ask(target=search_request_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM web_element(label="Search Site") -> web_element_search_box_2 : TERM
    RECORD ACTION type_text(target=web_element_search_box_2, text="600w power supply") STATUS succeeded SOURCE "t2:s2" -> type_text_event : EVENT
    TERM web_element(label="") -> search_button_2 : TERM
    RECORD ACTION click(target=search_button_2) STATUS succeeded SOURCE "t2:s4" -> click_event1 : EVENT
    TERM web_element(label="600 W") -> filter_600w_2 : TERM
    RECORD ACTION click(target=filter_600w_2) STATUS succeeded SOURCE "t2:s6" -> click_event2 : EVENT
    TERM web_element(label="Featured Items") -> combobox_2 : TERM
    RECORD ACTION select_option(target=combobox_2, value="Lowest Price") STATUS succeeded SOURCE "t2:s8" -> select_event : EVENT
    TERM web_element(label="Hercules DUAL FAN 600w-Max ATX Power Supply SATA") -> listing_2 : TERM
    RECORD ACTION click(target=listing_2) STATUS succeeded SOURCE "t2:s11" -> click_event3 : EVENT
  }
}
```

## Needs coverage

| need | kind       | expressed by                           | status   |
|------|------------|----------------------------------------|----------|
| n1   | action     | search_request                         | proposed |
| n2   | object     | object_label::power_supply_unit        | covered  |
| n3   | constraint | rank_field, rank_direction             | covered  |
| n4   | constraint | at_least, measure                      | covered  |
| n5   | action     | type_text                              | covered  |
| n6   | object     | web_element(label="Search Site")      | covered  |
| n7   | constraint | web_element(label="600 W")           | covered  |
| n8   | action     | click                                  | covered  |
| n9   | object     | web_element(label="")               | covered  |
| n10  | action     | click                                  | covered  |
| n11  | object     | web_element(label="600 W")           | covered  |
| n12  | action     | select_option                          | covered  |
| n13  | object     | web_element(label="Featured Items")  | covered  |
| n14  | constraint | select_option value="Lowest Price"   | covered  |
| n15  | action     | click                                  | covered  |
| n16  | object     | web_element(label="Hercules DUAL FAN 600w-Max ATX Power Supply SATA") | covered  |

## Why the translation failed

- n1 "Find or search for a product": no existing Term constructor describes a search request combining target, constraints, and sorting; needed to represent the user's utterance in structured form.  

## Translation report

- Input kind: conversation  
- Coverage status: partial  
- Source-span coverage: user utterance t1:s1 represented as a proposed TERM; all agent actions t2:s2–t2:s11 recorded.  
- Opaque-text spans: none  
- Label-preserved spans: none  
- Missing constructs: constructor `search_request`  
- Unresolved ambiguities: none  
- Check: `rag check` reported 1 unresolved need (n1), 0 unknown symbols
