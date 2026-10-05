# Suggestions for translator mind2web-1-r2

### S1 | type: add | dimension: constructor | symbol: trip_type_spec
- Needs: n2 (t1:s1), n13 (t2:s6)
- Searches tried: search "one-way trip" → `constraint_single_choice` (selects one from list, not trip structure); widen "trip type classification" → no glossary entry for trip topology; search "round-trip vs one-way" → no glossary match
- Typed parameters: type: STRING
- Interpretation: Specifies the structure of a trip: one-way, round-trip, multi-city, or open-jaw. The value names the trip structure type without asserting the trip exists. One-way is a common constraint in travel search.
- Example: `TERM trip_type_spec(type="one_way") -> trip_type_spec_2 : TERM` used in search_travel(constraints=[...])
- Contrast: Not `constraint_single_choice` (which means pick one option from a list); not a claim that the trip is one-way.
- Proposed record: `{"symbol": "trip_type_spec", "kind": "constructor", "signature": "TERM trip_type_spec(type: STRING) -> TERM", "definition": "Specifies the structure of a trip: one-way, round-trip, multi-city, or open-jaw. Used as a travel search constraint.", "not": "a claim that a trip is booked as one-way; constraint_single_choice (which means select one option from a list)", "aliases": ["trip structure", "journey type"]}`

### S2 | type: add | dimension: constructor | symbol: nonstop_constraint
- Needs: n3 (t1:s1), n2 (implicit in flight search context)
- Searches tried: search "nonstop flight" → `maximum_between_stops` (applies to ground travel between stops, not flight segments); widen "direct flight" → no glossary match; widen "zero intermediate stops" → no glossary entry for flight-specific stops
- Typed parameters: none (or optional `mode: STRING` for flights vs. transit)
- Interpretation: Specifies that a flight or transit route must be nonstop (zero intermediate stops). Common travel search constraint. Not asserting the trip is nonstop; describing the requirement.
- Example: `TERM nonstop_constraint() -> nonstop_const : TERM` used in search_travel(constraints=[...])
- Contrast: Not `maximum_between_stops` (applies to walking duration between ground stops, not flight segments); not a CLAIM about achieved nonstop routing.
- Proposed record: `{"symbol": "nonstop_constraint", "kind": "constructor", "signature": "TERM nonstop_constraint() -> TERM", "definition": "Requires a flight or transit route with zero intermediate stops. Common travel search constraint.", "not": "maximum_between_stops (which constrains walking time between ground stops); a claim that a booked trip is nonstop", "aliases": ["direct flight", "no stops"]}`

### S3 | type: add | dimension: vocabulary-member | symbol: airline_selected
- Needs: n7 (t2:s34)
- Searches tried: search "airline United selected" → no glossary match; widen "filter by carrier" → no glossary claim relation for airline; search "airline filter applied" → no entry
- Meaning: Records that a specific airline was selected or filtered in a search result or selection context.
- Category: claim_relation
- Contextual aliases: carrier_selected, airline_filtered
- Example: `CLAIM airline_selected(airline="United Airlines") BY agent STATUS observed SOURCE "t2:s34" -> airline_selected_2 : CLAIM`
- Contrast: Not a booking or reservation claim (which would use a different relation); not an availability check (which is `check_reservation_availability`).
- Proposed record: `{"symbol": "airline_selected", "kind": "claim_relation", "signature": "CLAIM airline_selected(airline: STRING)", "category": "claim_relation", "definition": "Records that a specific airline was selected or filtered in a search or selection context. Observed status typical.", "not": "a reservation or booking claim; an availability assertion", "aliases": ["carrier selected", "airline filtered"]}`

### S4 | type: add | dimension: vocabulary-member | symbol: flight_selected
- Needs: n11 (t2:s36), n20 (t2:s36 context)
- Searches tried: search "morning flight selected" → `daytime` is a time-of-day-value, not a claim; widen "select flight by time" → no glossary claim for flight time selection; search "5 AM flight" → no time-specific flight claim
- Meaning: Records that a specific flight was selected, optionally with time or period context.
- Category: claim_relation
- Contextual aliases: flight_chosen, flight_time_selected
- Example: `CLAIM flight_selected(time="5:00 AM", period="morning") BY agent STATUS observed SOURCE "t2:s36" -> flight_selected_2 : CLAIM`
- Contrast: Not a flight search or filter operation (which is an executable action); not a booking confirmation (which uses a different claim relation).
- Proposed record: `{"symbol": "flight_selected", "kind": "claim_relation", "signature": "CLAIM flight_selected(time: STRING, period?: STRING)", "category": "claim_relation", "definition": "Records that a specific flight was selected, with optional time or period. Common in travel booking interfaces.", "not": "a search operation; a reservation or booking; a time-of-day constraint (use daytime/nighttime for that)", "aliases": ["flight chosen", "flight time selected"]}`

