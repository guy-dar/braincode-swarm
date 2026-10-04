Status: failed
Mode: REQUEST

## Suggested translation

```braincode
MODE REQUEST
ENTRYPOINT FlightSearch
TASK FlightSearch {
  ACTION search_flight(origin=location_spec(city="San Francisco"), destination=location_spec(city="San Diego"), date=time_point(date="2023-07-01"), airline="United Airlines", passengers=[group_size(count=2, group=role_adults), group_size(count=1, group=role_senior)], nonstop=TRUE, one_way=TRUE, time_of_day=daytime) -> flights : LIST[REF[STRING]]  # PROPOSED: S1
  ACTION view_deal(flight=extract(target=flights, limit=1)) -> deal_ref : REF[STRING]  # PROPOSED: S3
}
``` 

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | search_flight | proposed |
| n2 | constraint | one_way=TRUE | proposed |
| n3 | constraint | nonstop=TRUE | proposed |
| n4 | object | location_spec(city="San Francisco") | covered |
| n5 | object | location_spec(city="San Diego") | covered |
| n6 | temporal | date=time_point(date="2023-07-01") | covered |
| n7 | constraint | airline="United Airlines" | covered |
| n8 | constraint | group_size(count=2, group=role_adults) | covered |
| n9 | constraint | group_size(count=1, group=role_senior) | proposed |
| n10 | action | view_deal | proposed |
| n11 | constraint | time_of_day=daytime | covered |
| n12 | action | (UI selection steps) | not-applicable |
| n13 | action | (UI selection steps) | not-applicable |
| n14 | action | (UI typing steps) | not-applicable |
| n15 | action | (UI typing steps) | not-applicable |
| n16 | action | (UI date selection steps) | not-applicable |
| n17 | action | (UI adjust passengers) | not-applicable |
| n18 | action | (UI click find flights) | not-applicable |
| n19 | action | (UI filter by airline) | not-applicable |
| n20 | action | (UI select flight) | not-applicable |
| n21 | action | (UI view deal button) | not-applicable |

## Why the translation failed

- n1–n3: The combined operation `search_flight(origin, destination, date, airline, passengers, nonstop, one_way, time_of_day)` would cover the user request for a one-way nonstop flight and its parameters, but no such `search_flight` operation exists in the current glossary.  # S1
- n9: The request includes a senior passenger, but there is no existing `recipient-value` symbol for `role_senior`.  # S2
- n10: Viewing the deal of the selected flight is not covered by any existing operation; an operation `view_deal` would be needed.  # S3
- n12–n21: The detailed UI steps (click, type_text, select_option, etc.) are abstracted by the higher-level `search_flight` and `view_deal` operations and are not applicable under the proposed plan abstraction.

## Translation report

- Input kind: prompt | conversation
- Coverage status: partial
- Source-span coverage: the main user request (t1:s1–t1:s2) is represented by the proposed `search_flight` and `view_deal` calls; UI instruction turns t2:s1–t2:s40 are abstracted.
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: S1 search_flight operation; S2 role_senior value; S3 view_deal operation
- Unresolved ambiguities: none
- Check: `rag check` reported unresolved needs for n1, n2, n3, n9, n10 and unknown symbols `search_flight`, `role_senior`, `view_deal`