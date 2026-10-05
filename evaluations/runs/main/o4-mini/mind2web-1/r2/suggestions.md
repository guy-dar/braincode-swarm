### S1 | type: add | dimension: constructor | symbol: flight_search
- Needs: n1, n2, n3, n4, n5, n6, n7, n8, n10, n11 (t1:s1–t1:s2)
- Searches tried:
  • "flight search constructor" → none
  • "search_travel" → operation, not TERM
  • "flight_request" → no entry
- Signature:
  TERM flight_search(
    origin: TERM,
    destination: TERM,
    departure_date: TERM,
    one_way: BOOL,
    nonstop: BOOL,
    airline: STRING,
    passengers: LIST[TERM],
    view_deal: BOOL,
    view_time: ATOM[time_of_day_value]
  ) -> TERM
- Definition:
  Constructs a structured description of a flight search request with specified origin and destination locations, departure date, one-way and nonstop flags, preferred airline, a list of passenger‐count terms, a view-deal indicator, and preferred time of day.
- not: Does not execute the search or assert any result; it is purely a request description.
- aliases: ["search_flights","find_flight"]
- Proposed record:
  {"symbol":"flight_search","kind":"constructor","signature":"TERM flight_search(origin: TERM, destination: TERM, departure_date: TERM, one_way: BOOL, nonstop: BOOL, airline: STRING, passengers: LIST[TERM], view_deal: BOOL, view_time: ATOM[time_of_day_value]) -> TERM","definition":"Constructs a structured description of a flight search request with specified origin, destination, date, one-way and nonstop flags, airline, passenger counts, view-deal indicator, and preferred time of day.","not":"Does not execute the search or represent an observed event; a request description only.","aliases":["search_flights","find_flight"]}

### S2 | type: add | dimension: vocabulary-member | symbol: request
- Needs: implicit user speech act at t1:s1–t1:s2
- Searches tried:
  • "UTTER request" → no speech_act entry
  • "ask" → exists but semantically for questions/suggestions
- Kind: speech_act
- Signature: UTTER request(target: TERM)
- Definition:
  Records a user's direct request speech act targeting the specified term; no execution effect.
- not: Not a question or suggestion speech act (use `ask` or `propose`).
- aliases: ["ask_for","request_action"]
- Proposed record:
  {"symbol":"request","kind":"speech_act","signature":"UTTER request(target: TERM)","definition":"Records a user's direct request speech act targeting the specified term; no execution effect.","not":"Not a question or suggestion speech act.","aliases":["ask_for","request_action"]}