### S1 | type: add | dimension: vocabulary-member | symbol: search_flight
- Needs: n1 (t1:s1), n2 (t1:s1), n3 (t1:s1), n7 (t1:s1), n11 (t1:s2)
- Searches tried: `node /kit/rag.mjs search "search flight"` → only `search_travel` (missing origin/destination params); widen "flight search by origin destination date airline passenger nonstop" → nothing
- Kind: operation
- Signature: `search_flight(origin: TERM, destination: TERM, date: TERM, airline: STRING, passengers: LIST[TERM], nonstop: BOOL, one_way: BOOL, time_of_day: STRING) -> LIST[REF[STRING]]`
- Definition: Query available flights meeting the specified origin, destination, date, airline, passenger composition, and travel constraints (nonstop, one-way, time of day); returns a list of flight references.
- not: Does not perform booking or ticket purchase (use a booking operation separately)
- aliases: find_flight, search_flights, flight_search
- Proposed record: {"symbol":"search_flight","kind":"operation","signature":"search_flight(origin: TERM, destination: TERM, date: TERM, airline: STRING, passengers: LIST[TERM], nonstop: BOOL, one_way: BOOL, time_of_day: STRING) -> LIST[REF[STRING]]","definition":"Query available flights meeting the specified origin, destination, date, airline, passenger composition, and travel constraints; returns a list of flight references.","not":"Does not make a booking or purchase","aliases":["find_flight","search_flights","flight_search"]}

### S2 | type: add | dimension: vocabulary-member | symbol: role_senior
- Needs: n9 (t1:s2)
- Searches tried: `node /kit/rag.mjs search "senior passenger role"` → candidates: role_adults (wrong meaning); widen "role senior" → nothing
- Kind: value (recipient-value)
- Category: recipient-value
- Definition: A senior passenger role, denoting a traveler who qualifies for senior fares or classification.
- not: Not an adult or child role; senior-specific category
- aliases: senior, senior_passenger
- Proposed record: {"symbol":"role_senior","kind":"value","category":"recipient-value","definition":"A senior passenger role, denoting a traveler who qualifies for senior fares or classification.","not":"Not an adult or child role","aliases":["senior","senior_passenger"]}

### S3 | type: add | dimension: vocabulary-member | symbol: view_deal
- Needs: n10 (t1:s2)
- Searches tried: `node /kit/rag.mjs search "view deal"` → no matching operation; widen "view flight deal" → nothing
- Kind: operation
- Signature: `view_deal(flight: REF[STRING]) -> REF[STRING]`
- Definition: Display or navigate to the detailed deal information for the specified flight reference, returning a reference to the deal view element.
- not: Does not purchase or book the flight
- aliases: show_deal, open_deal
- Proposed record: {"symbol":"view_deal","kind":"operation","signature":"view_deal(flight: REF[STRING]) -> REF[STRING]","definition":"Display or navigate to the detailed deal information for the specified flight reference, returning a reference to the deal view element.","not":"Does not perform booking or purchase","aliases":["show_deal","open_deal"]}