Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM location_spec(city="San Francisco") -> origin : TERM
    TERM location_spec(city="San Diego") -> destination : TERM
    TERM time_point(date="2023-07-01") -> departure_date : TERM
    TERM group_size(group=role_adults, count=2) -> adults_count : TERM
    TERM group_size(group=role_senior, count=1) -> seniors_count : TERM
    UTTER propose(target=flight_search_request(origin=origin, destination=destination, date=departure_date, airline=object_label::united_airlines, adults=adults_count, seniors=seniors_count, trip_type="one-way", stops="nonstop", time_of_day=daytime)) # PROPOSED: S1
  }
  TURN t2 SPEAKER=AGENT {
    RECORD ACTION click(target="Flights") STATUS succeeded SOURCE "t2:s4" -> click_event_2 : EVENT
    RECORD ACTION click(target="One-way") STATUS succeeded SOURCE "t2:s6" -> click_event_3 : EVENT
    RECORD ACTION type_text(target="City or Airport", text="SAN FRANSISCO") STATUS succeeded SOURCE "t2:s8" -> type_event : EVENT
    RECORD ACTION click(target="San Francisco, CA") STATUS succeeded SOURCE "t2:s10" -> click_event_5 : EVENT
    RECORD ACTION type_text(target="City or Airport", text="SAN DIEGO") STATUS succeeded SOURCE "t2:s12" -> type_event_2 : EVENT
    RECORD ACTION click(target="San Diego, CA") STATUS succeeded SOURCE "t2:s14" -> click_event_6 : EVENT
    RECORD ACTION click(target="Thu, 6/15") STATUS succeeded SOURCE "t2:s16" -> click_event_7 : EVENT
    RECORD ACTION click(target="Sat Jul 01 2023") STATUS succeeded SOURCE "t2:s18" -> click_event_8 : EVENT
    RECORD ACTION click(target="Travelers 1,Economy") STATUS succeeded SOURCE "t2:s20" -> click_event_9 : EVENT
    RECORD ACTION click(target="Close") STATUS succeeded SOURCE "t2:s26" -> click_event_10 : EVENT
    RECORD ACTION click(target="Find flights") STATUS succeeded SOURCE "t2:s30" -> click_event_11 : EVENT
    RECORD ACTION click(target="Show more") STATUS succeeded SOURCE "t2:s32" -> click_event_12 : EVENT
    RECORD ACTION click(target="United") STATUS succeeded SOURCE "t2:s34" -> click_event_13 : EVENT
    RECORD ACTION click(target="Sat 5:00 AM") STATUS succeeded SOURCE "t2:s36" -> click_event_14 : EVENT
    RECORD ACTION click(target="View Deal") STATUS succeeded SOURCE "t2:s38" -> click_event_15 : EVENT
    RECORD ACTION click(target="View Deal") STATUS succeeded SOURCE "t2:s40" -> click_event_16 : EVENT
  }
}
```

## Needs coverage

| need | kind       | expressed by                                              | status    |
|------|------------|-----------------------------------------------------------|-----------|
| n1   | action     | flight_search_request (PROPOSED: S1)                      | proposed  |
| n2   | constraint | include(item="one-way")                                 | covered   |
| n3   | constraint | exclude(item="nonstop")                                 | covered   |
| n4   | object     | location_spec(city="San Francisco")                     | covered   |
| n5   | object     | location_spec(city="San Diego")                         | covered   |
| n6   | temporal   | time_point(date="2023-07-01")                           | covered   |
| n7   | constraint | object_label::united_airlines                             | label-preserved |
| n8   | constraint | group_size(count=2, group=role_adults)                    | covered   |
| n9   | constraint | group_size(count=1, group=role_senior)                    | covered   |
| n10  | action     | click                                                     | covered   |
| n11  | constraint | include(item=daytime)                                     | covered   |
| n12  | action     | click                                                     | covered   |
| n13  | action     | click                                                     | covered   |
| n14  | action     | type_text                                                 | covered   |
| n15  | action     | type_text                                                 | covered   |
| n16  | action     | click                                                     | covered   |
| n17  | action     | click                                                     | covered   |
| n18  | action     | click                                                     | covered   |
| n19  | action     | click                                                     | covered   |
| n20  | action     | click                                                     | covered   |
| n21  | action     | click                                                     | covered   |

## Why the translation failed

- n1 "search for flights": the translation requires a TERM constructor `flight_search_request` to represent the composite flight search request; no such constructor exists in the glossary. Proposed S1.

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: user request t1:s1–s2 represented by proposed `flight_search_request`; all agent click/type operations t2:s4–t2:s40 recorded.
- Opaque-text spans: none
- Label-preserved spans: n7 t1:s1 "United Airlines" → object_label::united_airlines
- Missing constructs: S1 flight_search_request constructor
- Unresolved ambiguities: none
- Check: `rag check` reported 1 unresolved need (n1), 0 unknown symbols
