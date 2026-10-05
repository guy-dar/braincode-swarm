### S1 | type: add | dimension: constructor | symbol: itinerary_summary
- Needs: n10 (t4:s1)
- Searches tried:
  • "itinerary summary" → art_itinerary (value), content_kyoto_itinerary (composite for Kyoto only)
  • "propose itinerary plan term" → no matching TERM constructor
  • widen "itinerary plan term" → nothing suitable
- Typed parameters:
  duration: TERM, regions: LIST[ATOM[country]], group: TERM, budget: TERM, style: STRING
- Interpretation:
  A travel itinerary plan describing its duration, regions, group of travelers, per-person budget, and style; asserts nothing.
- Example:
  TERM itinerary_summary(duration=duration(amount=2, unit=unit_week), regions=[country::IT, country::IT], group=group_size(count=3, group=role_adults), budget=measure(amount=5000, unit=currency::USD), style="adventure") -> itinerary_summary_2 : TERM
- Proposed record:
  {"symbol":"itinerary_summary","kind":"constructor","signature":"TERM itinerary_summary(duration: TERM, regions: LIST[ATOM[country]], group: TERM, budget: TERM, style: STRING) -> TERM","definition":"A structured description of a travel itinerary, specifying its duration, regions, traveler group, per-person budget, and style; asserts nothing.","not":"an executed booking or external action","aliases":["trip_itinerary_summary"]}
