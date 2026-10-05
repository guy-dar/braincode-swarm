### S1 | type: add | dimension: constructor | symbol: flight_search
- Needs: n1–n9 (t1:s1–t1:s2)
- Searches tried: widen “one-way nonstop flight, airline United, passenger counts adults and senior” → `role_adults`, `group_size`, `search_travel`, `requirement`; search “flight one way nonstop airline passenger count adults senior constraint” → `group_size`, `requirement`, `search_travel`; widen “flight origin and destination cities with specific departure date and morning time” → `location_spec`, `time_point`, `search_travel`. `search_travel` only takes country location and generic constraints; existing constructors do not combine a route, date/period, carrier, and traveler groups as a flight-search description.
- Typed parameters: `origin: TERM, destination: TERM, departure: TERM, constraints: LIST[TERM], airline: STRING, passengers: LIST[TERM]`
- Interpretation: A descriptive request to find flights matching the supplied route, departure, constraints, carrier, and traveler groups; asserts no flight exists and does not execute a search or book travel. `constraints` contains terms such as one-way, nonstop, and departure period; `passengers` contains group descriptions and counts.
- Example: `TERM flight_search(airline="United Airlines", constraints=[one_way_2, nonstop_2], departure=departure_2, destination=destination_2, origin=origin_2, passengers=[adults_2, senior_2]) -> flight_search_2 : TERM`
- Contrast: Not a recorded or successful search operation, a booking, or an itinerary artifact.
- Proposed record: `{"symbol":"flight_search","kind":"constructor","signature":"TERM flight_search(origin: TERM, destination: TERM, departure: TERM, constraints: LIST[TERM], airline: STRING, passengers: LIST[TERM]) -> TERM","definition":"A descriptive request to find flights matching the supplied route, departure, constraints, carrier, and traveler groups. It asserts no result and neither executes a search nor books travel.","not":"A recorded search operation, booking, or itinerary artifact.","aliases":[]}`

### S2 | type: add | dimension: constructor | symbol: view_flight_deal
- Needs: n10 (t1:s2; observed clicks at t2:s38 and t2:s40)
- Searches tried: search and widen “view deal for selected flight without claiming booking” → `search_travel`, `select_option`, `click`, `open_page`. These describe querying, UI activation, or navigation, not the requested semantic goal of viewing a deal for the matching flight.
- Typed parameters: `flight: TERM`
- Interpretation: A description of the requested act of viewing the deal associated with a flight or flight search; it does not assert that a deal was available or displayed.
- Example: `TERM view_flight_deal(flight=flight_search_2) -> view_flight_deal_2 : TERM`
- Contrast: Not a booking, purchase, availability claim, or record that the deal was actually displayed.
- Proposed record: `{"symbol":"view_flight_deal","kind":"constructor","signature":"TERM view_flight_deal(flight: TERM) -> TERM","definition":"A description of the requested act of viewing the deal associated with a flight or flight search. It does not assert that a deal was available or displayed.","not":"A booking, purchase, availability claim, or record that the deal was displayed.","aliases":[]}`

### S3 | type: add | dimension: vocabulary-member | symbol: request_action
- Needs: n1 and n10 (t1:s1–t1:s2)
- Searches tried: search and widen “directive speech act asking an agent to perform an action” → `ask`, `propose`, `offer`, `express_interest`, and `request`. `ask` requests information/advice, `propose` suggests an action, `offer` and `express_interest` have different speech-act meanings, and `request` is a CLAIM relation rather than a UTTER speech act.
- Meaning: A speech act in which the speaker requests performance of the action described by its TERM target; it does not record performance or success.
- Category: speech_act
- Contextual aliases: []
- Example: `UTTER request_action(target=flight_search_2)`
- Contrast: Not a suggestion, question seeking information, or record of a completed operation.
- Proposed record: `{"symbol":"request_action","kind":"speech_act","signature":"UTTER request_action(target: TERM)","definition":"Requests that the action described by target be performed; it does not record performance or success.","not":"A suggestion, a question seeking information, or a record of a completed operation.","aliases":[]}`
