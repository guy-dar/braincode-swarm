# Suggestions

### S1 | type: add | dimension: composite | symbol: constraint_oneway

- Needs: n2 (t1:s1)
- Searches tried: 
  - search "one-way flight type" → constraint_single_choice (means pick one option, not trip type), dom_ovr, design_parameters, etc.
  - widen "one-way trip" → no flight-type constraint
  - widen "round-trip alternative" → no trip type constraint vocabulary
- Meaning: A constraint requiring a one-way (single-leg) flight, not round-trip.
- Expansion: Expands to requirement constructor with trip type property set to one-way.
- Proposed record: `{"symbol": "constraint_oneway", "kind": "composite", "category": "constraint-value", "expansion": "requirement(property=\"trip_type\", value=\"one_way\")", "definition": "Requires a one-way (single-leg) flight, not round-trip.", "not": "Round-trip or multi-leg flights.", "aliases": ["one-way only", "single leg"]}`

### S2 | type: add | dimension: composite | symbol: constraint_nonstop

- Needs: n3 (t1:s1)
- Searches tried:
  - search "nonstop direct flight" → maximum_between_stops (duration between stops, not number of stops), spatial_constraint
  - widen "zero connecting flights" → no matches for this constraint type
  - widen "direct flight only" → no flight-specific constraints found
- Meaning: A constraint requiring nonstop/direct flights with zero connecting flights.
- Expansion: Expands to requirement constructor with stops property set to zero.
- Proposed record: `{"symbol": "constraint_nonstop", "kind": "composite", "category": "constraint-value", "expansion": "requirement(property=\"connecting_stops\", value=0)", "definition": "Requires nonstop (direct) flights with zero connecting flights or segments.", "not": "Flights with one or more connections or stops.", "aliases": ["direct flight", "nonstop only", "no connections"]}`
