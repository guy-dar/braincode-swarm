Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM entity_description(label="power supply unit") -> entity_description_2 : TERM  # PROPOSED: S3
    TERM measure(amount=600, unit=unit_watt) -> measure_2 : TERM  # PROPOSED: S2
    TERM at_least(measure=measure_2) -> at_least_2 : TERM
    TERM requirement(property="power_output", value=at_least_2) -> requirement_2 : TERM
    TERM catalog_search_request(target=entity_description_2, constraints=[requirement_2], rank_direction=dir_asc, rank_field=rank_price) -> catalog_search_request_2 : TERM  # PROPOSED: S1
    UTTER ask(target=catalog_search_request_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM web_element(label="Search Site", tag="searchbox") -> web_element_2 : TERM
    RECORD ACTION type_text(target=web_element_2, text="600w power supply") STATUS succeeded SOURCE "t2:s2" -> type_text_event : EVENT
    TERM web_element(label="", tag="button") -> web_element_3 : TERM
    RECORD ACTION click(target=web_element_3) STATUS succeeded SOURCE "t2:s4" -> click_event : EVENT
    TERM web_element(label="600 W", tag="generic") -> web_element_4 : TERM
    RECORD ACTION click(target=web_element_4) STATUS succeeded SOURCE "t2:s6" -> click_event_2 : EVENT
    TERM web_element(label="Featured Items", tag="combobox") -> web_element_5 : TERM
    RECORD ACTION select_option(target=web_element_5, value="Lowest Price") STATUS succeeded SOURCE "t2:s8" -> select_option_event : EVENT
    TERM web_element(label="Hercules DUAL FAN 600w-Max ATX Power Supply SATA, ...", tag="img") -> web_element_6 : TERM
    RECORD ACTION click(target=web_element_6) STATUS succeeded SOURCE "t2:s11" -> click_event_3 : EVENT
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | catalog_search_request (PROPOSED: S1) | proposed |
| n2 | object | entity_description (PROPOSED: S3) | proposed |
| n3 | constraint | rank_price, dir_asc, catalog_search_request (PROPOSED: S1) | proposed |
| n4 | constraint | measure, unit_watt (PROPOSED: S2), at_least, requirement | proposed |
| n5 | action | type_text | covered |
| n6 | object | web_element | covered |
| n7 | constraint | type_text text="600w power supply" | covered |
| n8 | action | click | covered |
| n9 | object | web_element | covered |
| n10 | action | click | covered |
| n11 | object | web_element | covered |
| n12 | action | select_option | covered |
| n13 | object | web_element | covered |
| n14 | constraint | rank_price, dir_asc, select_option | covered |
| n15 | action | click | covered |
| n16 | object | web_element | covered |

## Why the translation failed

- n1 (t1:s1), n3 (t1:s1): searched “TERM description of search action query target and filters,” “TERM product search request cheapest product minimum output,” and “request to find an item satisfying property constraints”; widened the request/search need and searched for a product-search request. Results included `search_web` and `sort`, which are executable operations and cannot describe the user's request in TRACE, and `rank_price`/`dir_asc`, which express ranking values but are not a TERM for the requested catalog search. A compositional search-request constructor is missing; proposed as S1.
- n2 (t1:s1): widened “multiword object-kind label power supply unit described as a TERM without splitting words” and searched “TERM constructor preserves exact multiword object kind label.” `object_label` is an open group but its lower_word key form rejects the source phrase with word breaks; `lexical_label` accepts the atom, not an arbitrary multiword phrase. Proposed an exact, non-inferential entity-description constructor as S3.
- n4 (t1:s1): searched “watt power output unit measure 600 W,” “600 watts power output threshold for power supply,” and widened “measure a quantity in watts, unit W.” Closest measurement constructors are `measure` and `at_least`, but the retrieved accepted units include no watt unit; `unit_gram`, `unit_liter`, and `unit_fahrenheit` have different dimensions. Proposed the missing unit value as S2.

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: t1:s1 is represented except for the missing search-request and watt vocabulary noted above; t2:s2, t2:s4, t2:s6, t2:s8, t2:s10–t2:s11 are represented by recorded UI actions and their element descriptions. The standalone numbered markers in t2:s1, t2:s3, t2:s5, t2:s7, and t2:s9 are step formatting, not additional claims or actions.
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: S1 catalog_search_request TERM constructor; S2 unit_watt unit value; S3 entity_description TERM constructor
- Unresolved ambiguities: none
- Check: `node /kit/rag.mjs check --translation /output/translation.md` reported the proposed symbols `catalog_search_request`, `unit_watt`, and `entity_description`; it declared needs n2, n7, n13, and n16 although the translation includes the exact entity phrase, search text, and UI element labels. These are checker coverage-match limitations for proposed or literal descriptive content; they are not silently omitted source spans.
