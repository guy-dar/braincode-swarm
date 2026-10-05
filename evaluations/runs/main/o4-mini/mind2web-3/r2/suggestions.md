### S1 | type: add | dimension: lexical-group | symbol: power_unit_label
- Needs: n4 (t1:s1)
- Searches tried: "unit of power" → no matching group; widen "power unit" → no results
- Domain: units of power measurement (e.g. watt, kilowatt)
- Admission: open_label
- Key form: lower_word
- Consuming signatures: refine `measure(amount: NUMBER, unit: STRING / ATOM[currency])` to accept ATOM[power_unit_label]
- Proposed record: {"symbol":"power_unit_label","kind":"lexical_group","definition":"Source-supplied power-measurement unit; denotes a unit of power without implied conversion","group":{"examples":["power_unit_label::watt"]}}

### S2 | type: refine | dimension: refine-entry | target: measure
- Needs: n4 (t1:s1)
- Searches tried: entry `measure` → unit parameter only accepts STRING/ATOM[currency]
- Before: `TERM measure(amount: NUMBER, unit: STRING / ATOM[currency]) -> TERM`
- After: `TERM measure(amount: NUMBER, unit: STRING / ATOM[currency] / ATOM[power_unit_label]) -> TERM`
- Justification: allow expressing physical power quantities like watts alongside currencies
- Proposed record: {"signature":"TERM measure(amount: NUMBER, unit: STRING / ATOM[currency] / ATOM[power_unit_label]) -> TERM"}

### S3 | type: add | dimension: constructor | symbol: request_action
- Needs: n1 (t1:s1)
- Searches tried: "record user request action" → no existing candidate; widen "user request term" → none found
- Typed parameters: action: STRING, target?: ATOM[object_label], filters?: LIST[TERM]
- Interpretation: Structured representation of a user's imperative request to perform the named action with optional target and filters; asserts nothing
- Example: `TERM request_action(action="search_web", target=object_label::power_supply_unit, filters=[rank_price, at_least(measure(amount=600, unit=power_unit_label::watt))]) -> request_action_2 : TERM`
- Proposed record: {"symbol":"request_action","kind":"constructor","signature":"TERM request_action(action: STRING, target?: ATOM[object_label], filters?: LIST[TERM]) -> TERM","definition":"Structured representation of a user's imperative request to perform the named action with optional target and constraints; does not assert execution","not":"An executed operation or factual claim; use RECORD ACTION for observed events","aliases":["user_request"]}