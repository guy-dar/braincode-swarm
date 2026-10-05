Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM requirement(property="availability", value=avail_in_stock) -> requirement_2 : TERM
    TERM requirement(property="rank_field", value=rank_price) -> requirement_3 : TERM
    TERM requirement(property="rank_direction", value=dir_asc) -> requirement_4 : TERM
    TERM activity(object=object_label::drive, verb="show") -> activity_2 : TERM
    UTTER ask(target=activity_2, constraints=[requirement_2, requirement_3, requirement_4])
  }
  TURN t2 SPEAKER=AGENT {
    TERM web_element(label="Open Menu", tag="button") -> web_element_2 : TERM
    RECORD ACTION click(target=web_element_2) STATUS succeeded SOURCE "t2:s2" -> click_event : EVENT
    TERM web_element(label="See All", tag="link") -> web_element_3 : TERM
    RECORD ACTION click(target=web_element_3) STATUS succeeded SOURCE "t2:s4" -> click_event_2 : EVENT
    TERM web_element(label="Computers", tag="link") -> web_element_4 : TERM
    RECORD ACTION click(target=web_element_4) STATUS succeeded SOURCE "t2:s6" -> click_event_3 : EVENT
    TERM web_element(label="Drives & Storage", tag="link") -> web_element_5 : TERM
    RECORD ACTION click(target=web_element_5) STATUS succeeded SOURCE "t2:s8" -> click_event_4 : EVENT
    TERM web_element(label="External Solid State Drives", tag="link") -> web_element_6 : TERM
    RECORD ACTION click(target=web_element_6) STATUS succeeded SOURCE "t2:s10" -> click_event_5 : EVENT
    TERM web_element(label="Sort by:", tag="span") -> web_element_7 : TERM
    RECORD ACTION click(target=web_element_7) STATUS succeeded SOURCE "t2:s12" -> click_event_6 : EVENT
    TERM web_element(label="Price: Low to High", tag="option") -> web_element_8 : TERM
    RECORD ACTION click(target=web_element_8) STATUS succeeded SOURCE "t2:s14" -> click_event_7 : EVENT
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask | covered |
| n2 | action | activity | covered |
| n3 | object | object_label::drive | label-preserved |
| n4 | constraint | avail_in_stock, requirement | covered |
| n5 | constraint | dir_asc, rank_direction, rank_field, rank_price, requirement | covered |
| n6 | action | click | covered |
| n7 | object | web_element | covered |
| n8 | action | click | covered |
| n9 | object | web_element | covered |
| n10 | action | click | covered |
| n11 | object | web_element | covered |
| n12 | action | click | covered |
| n13 | object | web_element | covered |
| n14 | action | click | covered |
| n15 | object | object_label::drive, web_element | label-preserved |
| n16 | action | click | covered |
| n17 | object | web_element | covered |
| n18 | action | click | covered |
| n19 | object | web_element | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s14 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s1 "external solid state drives" → object_label::drive (label only; no sense resolved); t2:s10 "External Solid State Drives" → object_label::drive (label only; no sense resolved)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
