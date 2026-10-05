### S1 | type: add | dimension: constructor | symbol: itinerary_summary
- Needs: n10
- Searches tried: "14-day adventure itinerary summary" → no matching constructor; widen → none suitable
- Typed parameters: destination: LIST[TERM], duration: TERM, party_size: TERM, budget: TERM, style: TERM
- Interpretation: A concise representation of a proposed itinerary, including destinations, total duration, party size, budget, and style; asserts nothing.
- Example: `TERM itinerary_summary(destination=[trip_subject_2], duration=duration_limit_2, party_size=group_size_2, budget=budget_req_2, style=vibe_req_2) -> itinerary_summary_2 : TERM`
- Proposed record: {"symbol":"itinerary_summary","kind":"constructor","signature":"TERM itinerary_summary(destination: LIST[TERM], duration: TERM, party_size: TERM, budget: TERM, style: TERM) -> TERM","definition":"A concise representation of a proposed itinerary, including destinations, total duration, party size, budget, and style.","not":"A generated artifact or booking; does not enact the plan.","aliases":["plan_summary","trip_summary"]}

### S2 | type: add | dimension: constructor | symbol: travel_intent
- Needs: n1, n3, n4, n5, n6, n7
- Searches tried: "I want to go to X" → no matching constructor; widen → none suitable
- Typed parameters: destination: ATOM[country], city: STRING / ATOM[object_label], time: STRING, companions: LIST[STRING / TERM], style: STRING
- Interpretation: A structured representation of a user's travel intent, capturing destination country, city, travel time, companions, and desired style; asserts nothing.
- Example: `TERM travel_intent(destination=country::IT, city=object_label::rome, time="early July 2025", companions=[role_adults], style="adventure") -> travel_intent_2 : TERM`
- Proposed record: {"symbol":"travel_intent","kind":"constructor","signature":"TERM travel_intent(destination: ATOM[country], city: STRING / ATOM[object_label], time: STRING, companions: LIST[STRING / TERM], style: STRING) -> TERM","definition":"A structured representation of a user's travel intent, capturing destination, city, travel time, companions, and travel style.","not":"An executed travel action; does not assume travel has occurred.","aliases":["trip_intent","travel_preferences"]}