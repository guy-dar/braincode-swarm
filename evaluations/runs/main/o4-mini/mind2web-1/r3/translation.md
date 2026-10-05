Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM flight_search_request(origin="San Francisco", destination="San Diego", date="2023-07-01", airline="United Airlines", one_way=TRUE, nonstop=TRUE, passengers=[group_size(count=2, group="adults"), group_size(count=1, group="seniors")]) -> flight_search_request_2 : TERM  # PROPOSED: S1
    UTTER propose(target=flight_search_request_2)
  }
  TURN t2 SPEAKER=AGENT {
    RECORD ACTION click(target=web_element(label="circle")) STATUS succeeded SOURCE "t2:s2" -> click_event : EVENT
    RECORD ACTION click(target=web_element(label="Flights")) STATUS succeeded SOURCE "t2:s4" -> click_event_2 : EVENT
    RECORD ACTION click(target=web_element(label="One-way")) STATUS succeeded SOURCE "t2:s6" -> click_event_3 : EVENT
    RECORD ACTION type_text(target=web_element(label="City or Airport"), text="SAN FRANSISCO") STATUS succeeded SOURCE "t2:s8" -> type_text_event : EVENT
    RECORD ACTION click(target=web_element(label="San Francisco, CA")) STATUS succeeded SOURCE "t2:s10" -> click_event_4 : EVENT
    RECORD ACTION type_text(target=web_element(label="City or Airport"), text="SAN DIEGO") STATUS succeeded SOURCE "t2:s12" -> type_text_event_2 : EVENT
    RECORD ACTION click(target=web_element(label="San Diego, CA")) STATUS succeeded SOURCE "t2:s14" -> click_event_5 : EVENT
    RECORD ACTION click(target=web_element(label="Thu, 6/15")) STATUS succeeded SOURCE "t2:s16" -> click_event_6 : EVENT
    RECORD ACTION click(target=web_element(label="Sat Jul 01 2023")) STATUS succeeded SOURCE "t2:s18" -> click_event_7 : EVENT
    RECORD ACTION click(target=web_element(label="Travelers 1,Economy")) STATUS succeeded SOURCE "t2:s20" -> click_event_8 : EVENT
    RECORD ACTION click(target=web_element(label="svg")) STATUS succeeded SOURCE "t2:s22" -> click_event_9 : EVENT
    RECORD ACTION click(target=web_element(label="svg")) STATUS succeeded SOURCE "t2:s24" -> click_event_10 : EVENT
    RECORD ACTION click(target=web_element(label="Close")) STATUS succeeded SOURCE "t2:s26" -> click_event_11 : EVENT
    RECORD ACTION click(target=web_element(label="")) STATUS succeeded SOURCE "t2:s28" -> click_event_12 : EVENT
    RECORD ACTION click(target=web_element(label="Find flights")) STATUS succeeded SOURCE "t2:s30" -> click_event_13 : EVENT
    RECORD ACTION click(target=web_element(label="Show more")) STATUS succeeded SOURCE "t2:s32" -> click_event_14 : EVENT
    RECORD ACTION click(target=web_element(label="United")) STATUS succeeded SOURCE "t2:s34" -> click_event_15 : EVENT
    RECORD ACTION click(target=web_element(label="Sat 5:00 AM")) STATUS succeeded SOURCE "t2:s36" -> click_event_16 : EVENT
    RECORD ACTION click(target=web_element(label="View Deal")) STATUS succeeded SOURCE "t2:s38" -> click_event_17 : EVENT
    RECORD ACTION click(target=web_element(label="View Deal")) STATUS succeeded SOURCE "t2:s40" -> click_event_18 : EVENT
  }
}
```

## Needs coverage

| need | kind       | expressed by                                         | status   |
|------|------------|------------------------------------------------------|----------|
| n1   | action     | flight_search_request_2, UTTER propose               | proposed |
| n2   | constraint | flight_search_request_2                              | proposed |
| n3   | constraint | flight_search_request_2                              | proposed |
| n4   | object     | flight_search_request_2                              | proposed |
| n5   | object     | flight_search_request_2                              | proposed |
| n6   | temporal   | flight_search_request_2                              | proposed |
| n7   | constraint | flight_search_request_2                              | proposed |
| n8   | constraint | flight_search_request_2                              | proposed |
| n9   | constraint | flight_search_request_2                              | proposed |
| n10  | action     | click_event_17                                       | covered  |
| n11  | constraint | click_event_16                                       | covered  |
| n12  | action     | click_event_2                                        | covered  |
| n13  | action     | click_event_3                                        | covered  |
| n14  | action     | type_text_event, click_event_4                       | covered  |
| n15  | action     | type_text_event_2, click_event_5                     | covered  |
| n16  | action     | click_event_7                                        | covered  |
| n17  | action     | click_event_8, click_event_9, click_event_10, click_event_11 | covered  |
| n18  | action     | click_event_13                                       | covered  |
| n19  | action     | click_event_14, click_event_15                       | covered  |
| n20  | action     | click_event_16                                       | covered  |
| n21  | action     | click_event_17                                       | covered  |

## Why the translation failed

- n1–n9: no existing TERM constructor can represent a structured flight search request with origin, destination, date, airline, trip type, and passenger counts. Operation `search_travel` exists but is an ACTION, not a TERM. Widen and search failed to find a suitable TERM constructor.

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: user request (t1:s1) and agent actions (t2:s2–t2:s40)
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: S1 flight_search_request constructor
- Unresolved ambiguities: none
- Check: `rag check` reported 9 unresolved needs, 1 unknown symbol (flight_search_request)
