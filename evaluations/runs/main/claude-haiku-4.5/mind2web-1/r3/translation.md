Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM location_spec(city="San Francisco") -> origin : TERM
    TERM location_spec(city="San Diego") -> destination : TERM
    TERM time_point(date="July 1") -> departure_date : TERM
    TERM constraint_single_choice() -> one_way : TERM
    TERM requirement(property="stops", value=0) -> nonstop : TERM
    TERM group_size(count=2, group="adults") -> adult_passengers : TERM
    TERM group_size(count=1, group="seniors") -> senior_passengers : TERM
    TERM time_point(time="morning") -> morning_departure : TERM
    UTTER ask(
      constraints=[one_way, nonstop, adult_passengers, senior_passengers, morning_departure],
      topic="flight search with deal view"
    )
  }
  TURN t2 SPEAKER=AGENT {
    RECORD ACTION click(target=web_element(label="Flights")) STATUS attempted SOURCE "t2:s4" -> click_flights : EVENT
    RECORD ACTION select_option(target=web_element(label="Flight type"), value="One-way") STATUS attempted SOURCE "t2:s6" -> select_one_way : EVENT
    RECORD ACTION type_text(target=web_element(label="Departure City"), text="San Francisco") STATUS attempted SOURCE "t2:s8" -> type_origin : EVENT
    RECORD ACTION click(target=web_element(label="San Francisco, CA")) STATUS attempted SOURCE "t2:s10" -> confirm_origin : EVENT
    RECORD ACTION type_text(target=web_element(label="Arrival City"), text="San Diego") STATUS attempted SOURCE "t2:s12" -> type_destination : EVENT
    RECORD ACTION click(target=web_element(label="San Diego, CA")) STATUS attempted SOURCE "t2:s14" -> confirm_destination : EVENT
    RECORD ACTION click(target=web_element(label="Departure Date")) STATUS attempted SOURCE "t2:s16" -> open_calendar : EVENT
    RECORD ACTION select_option(target=web_element(label="Date picker"), value="Sat Jul 01 2023") STATUS attempted SOURCE "t2:s18" -> select_date : EVENT
    RECORD ACTION click(target=web_element(label="Travelers")) STATUS attempted SOURCE "t2:s20" -> open_travelers : EVENT
    RECORD ACTION click(target=web_element(label="Increment adults")) STATUS attempted SOURCE "t2:s22" -> increment_adult_1 : EVENT
    RECORD ACTION click(target=web_element(label="Increment seniors")) STATUS attempted SOURCE "t2:s24" -> increment_senior : EVENT
    RECORD ACTION click(target=web_element(label="Close")) STATUS attempted SOURCE "t2:s26" -> close_travelers : EVENT
    RECORD ACTION click(target=web_element(label="Find flights")) STATUS attempted SOURCE "t2:s30" -> submit_search : EVENT
    RECORD ACTION click(target=web_element(label="Show more")) STATUS attempted SOURCE "t2:s32" -> show_more : EVENT
    RECORD ACTION select_filter(target=web_element(label="Airline filter"), criterion=web_element(label="United")) STATUS attempted SOURCE "t2:s34" -> filter_united : EVENT
    RECORD ACTION select_option(target=web_element(label="Flight time"), value="5:00 AM") STATUS attempted SOURCE "t2:s36" -> select_morning : EVENT
    RECORD ACTION click(target=web_element(label="View Deal")) STATUS attempted SOURCE "t2:s38" -> view_deal_1 : EVENT
    RECORD ACTION click(target=web_element(label="View Deal")) STATUS attempted SOURCE "t2:s40" -> view_deal_2 : EVENT
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | click, type_text, select_option, select_filter, submit_search | covered |
| n2 | constraint | constraint_single_choice | covered |
| n3 | constraint | requirement (property=stops, value=0) | covered |
| n4 | object | location_spec | covered |
| n5 | object | location_spec | covered |
| n6 | temporal | time_point | covered |
| n7 | constraint | select_filter | covered |
| n8 | constraint | group_size | covered |
| n9 | constraint | group_size | covered |
| n10 | action | click | covered |
| n11 | constraint | time_point (time=morning) | covered |
| n12 | action | select_option, click | covered |
| n13 | action | select_option, click | covered |
| n14 | action | type_text, click | covered |
| n15 | action | type_text, click | covered |
| n16 | action | select_option, click | covered |
| n17 | action | click | covered |
| n18 | action | click | covered |
| n19 | action | select_filter, click | covered |
| n20 | action | select_option, click | covered |
| n21 | action | click, web_element | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: All segments t1:s1–t2:s40 are represented. t1 contains the user request; t2 contains the agent's recorded UI interactions.
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: Ready for validation with `rag check`
