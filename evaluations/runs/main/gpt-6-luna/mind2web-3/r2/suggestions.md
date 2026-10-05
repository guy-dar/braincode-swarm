### S1 | type: add | dimension: constructor | symbol: rank_order
- Needs: n3 (t1:s1)
- Searches tried: `search` "price ascending TERM constructor" → `rank_price`, `dir_asc`, `sort`; `search` "represent cheapest price as a required selection or ordering criterion" and "rank lowest price requested preference as TERM" → `rank_price`, `dir_asc`, `sort`, and generic `requirement`; `widen` "represent cheapest price as a required selection or ordering criterion" → same close candidates. `sort` executes ordering on a result list, while the value symbols alone do not construct a described ranking constraint.
- Typed parameters: `field: STRING` (restricted to accepted `rank_*` search-value symbols); `direction: STRING` (restricted to accepted `dir_*` search-value symbols)
- Interpretation: Describes the requested ordering criterion without executing a sort or asserting that any results were ordered. Both the rank field and direction are required.
- Example: `TERM rank_order(field=rank_price, direction=dir_asc) -> rank_order_2 : TERM`
- Proposed record: `{"symbol":"rank_order","kind":"constructor","signature":"TERM rank_order(field: STRING, direction: STRING) -> TERM","definition":"A requested ranking criterion with a field from the accepted rank_* search-value family and a direction from the accepted dir_* search-value family. Describes ordering only; it does not execute a sort or assert an observed order.","not":"An executed sorting operation or evidence that results are actually ordered","aliases":[]}`

### S2 | type: add | dimension: constructor | symbol: minimum_power_output
- Needs: n4 (t1:s1)
- Searches tried: `search` "minimum product power output wattage", "product attribute power output requirement", and "watt as a unit in a measured power output constraint"; `widen` "power supply unit with at least 600W power output" and "find a product matching a minimum wattage output requirement" → `at_least`, `requirement`, and `measure`, but no watt unit or power-output constructor. `measure` accepts only STRING / ATOM[currency] as its unit, so it cannot represent watts; RAM/capacity and other retrieved units have different meanings.
- Typed parameters: `watts: NUMBER`
- Interpretation: Describes a required lower bound on a product's power output measured in watts; the bound is inclusive and the number must be nonnegative. It does not assert that any product meets the requirement.
- Example: `TERM minimum_power_output(watts=600) -> minimum_power_output_2 : TERM`
- Proposed record: `{"symbol":"minimum_power_output","kind":"constructor","signature":"TERM minimum_power_output(watts: NUMBER) -> TERM","definition":"A product requirement that its power output be at least the given nonnegative number of watts, inclusive. Describes a constraint and does not assert that a product satisfies it.","not":"A measured or observed output, or a claim that a product meets the requirement","aliases":["minimum wattage output"]}`
