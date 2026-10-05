### S1 | type: add | dimension: constructor | symbol: search_request
- Needs: n1 (t1:s1)
- Searches tried: 
  - `node /kit/rag.mjs search "search request" --kind action` → no constructor found
  - `node /kit/rag.mjs widen "describe a search request" --kind action` → no usable candidates
- Typed parameters: target: STRING / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], constraints: LIST[TERM], rank_field: STRING / ATOM[search-value], rank_direction: STRING / ATOM[search-value]
- Interpretation: a description of a requested web/catalog search for the specified target with optional structured constraints and sorting parameters; asserts nothing and creates no external effect
- Example: `TERM search_request(target=object_label::power_supply_unit, constraints=[at_least(measure(amount=600, unit="W"))], rank_field=rank_price, rank_direction=dir_asc) -> search_request_2 : TERM`
- Proposed record: `{"symbol":"search_request","kind":"constructor","signature":"TERM search_request(target: STRING / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], constraints: LIST[TERM], rank_field: STRING / ATOM[search-value], rank_direction: STRING / ATOM[search-value]) -> TERM","definition":"A description of a requested search for the specified target with optional structured constraints and sorting parameters; asserts nothing.","not":"an execution action (use ACTION search_web)","aliases":["search request","find items"]}`
