Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind=object_label::powersupply) -> psu_subject : TERM
    TERM requirement(property="power_output_min_watts", value=600) -> power_min : TERM
    UTTER ask(target=psu_subject, constraints=[power_min, rank_price, dir_asc])
  }
  TURN t2 SPEAKER=AGENT {
    TERM web_element(label="Search Site") -> search_box : TERM
    RECORD ACTION type_text(target=search_box, text="600w power supply") STATUS succeeded SOURCE "t2:s2" -> type_text_event : EVENT
    
    TERM web_element(tag="button") -> search_button : TERM
    RECORD ACTION click(target=search_button) STATUS succeeded SOURCE "t2:s4" -> click_button_event : EVENT
    
    TERM web_element(label="600 W") -> filter_600w : TERM
    RECORD ACTION click(target=filter_600w) STATUS succeeded SOURCE "t2:s6" -> click_filter_event : EVENT
    
    TERM web_element(label="Featured Items", tag="select") -> featured_combobox : TERM
    RECORD ACTION select_option(target=featured_combobox, value="Lowest Price") STATUS succeeded SOURCE "t2:s8" -> select_option_event : EVENT
    
    TERM captioned_figure(caption="Hercules DUAL FAN 600w-Max ATX Power Supply SATA", label="product_listing") -> product_figure : TERM
    RECORD ACTION click(target=product_figure) STATUS succeeded SOURCE "t2:s11" -> click_product_event : EVENT
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | type_text, click, select_option | covered |
| n2 | object | object_label::powersupply | label-preserved |
| n3 | constraint | rank_price, dir_asc | covered |
| n4 | constraint | requirement | covered |
| n5 | action | type_text | covered |
| n6 | object | web_element | covered |
| n7 | constraint | type_text | covered |
| n8 | action | click | covered |
| n9 | object | web_element | covered |
| n10 | action | click | covered |
| n11 | object | web_element | covered |
| n12 | action | select_option | covered |
| n13 | object | web_element | covered |
| n14 | constraint | rank_price, dir_asc, select_option | covered |
| n15 | action | click | covered |
| n16 | object | captioned_figure | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: Every segment t1:s1 and t2:s2–t2:s11 is represented. User request (n1–n4) in t1; agent actions (n5–n16) in t2.
- Opaque-text spans: none
- Label-preserved spans: n2 "power supply unit" → `object_label::powersupply` (open label preserves the concept without a more specific glossary entry)
- Missing constructs: none; power output constraint (n4) expressed via `requirement` constructor instead of unit-based constraint (watt unit not in glossary)
- Unresolved ambiguities: none
- Check: ran `rag check`; no unknown symbols or retired bare symbols reported
