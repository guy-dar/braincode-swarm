### S1 | type: add | dimension: constructor | symbol: content_plan_trip
- Needs: n1 (t1:s1)
- Searches tried: "Plan a travel trip" → art_itinerary (artifact generation), search_travel (operation), propose_menu (claim); no TERM constructor for planning.
- Typed parameters: none
- Interpretation: represents the user's request to plan a travel trip; a structured TERM placeholder for that intent.
- Example: `TERM content_plan_trip() -> content_plan_trip_2 : TERM`
- Proposed record: `{"symbol":"content_plan_trip","kind":"constructor","signature":"TERM content_plan_trip() -> TERM","definition":"A structured representation of the user's intent to plan a travel trip.","not":"An executed operation; it does not itself generate or assert results.","aliases":[]}`

### S2 | type: add | dimension: constructor | symbol: trip_details
- Needs: n3 (t3:s1), n4 (t3:s1), n5 (t3:s1), n6 (t3:s1), n7 (t3:s1), n8 (t3:s1), n9 (t3:s1)
- Searches tried: "trip details" → nothing; "travel preferences" → no matching TERM
- Typed parameters: destination: ATOM[country], date_range: TERM, group_size: TERM, style: STRING, budget: TERM, duration: TERM
- Interpretation: a structured TERM capturing all of the user's specified trip preferences: destination country, travel timeframe, party size, desired style, per-person budget, and maximum duration.
- Example:
  ```braincode
  TERM trip_details(
    destination=country::IT,
    date_range=time_horizon(horizon="early July"),
    group_size=group_size(count=3, group=role_adults),
    style="adventure",
    budget=measure(amount=5000, unit=currency::USD),
    duration=duration(amount=2, unit=unit_week)
  ) -> trip_details_2 : TERM
  ```
- Proposed record: `{"symbol":"trip_details","kind":"constructor","signature":"TERM trip_details(destination: ATOM[country], date_range: TERM, group_size: TERM, style: STRING, budget: TERM, duration: TERM) -> TERM","definition":"A structured representation of the user's specific travel preferences, including destination country, timeframe, party size, travel style, budget, and maximum duration.","not":"A generation or booking action; it does not itself produce an itinerary.","aliases":[]}`
