### S1 | type: add | dimension: constructor | symbol: product_search
- Needs: n1 (t1:s1), n3 (t1:s1)
- Searches tried: widen "Find or search for a product" → `search_web` (operation, cannot represent a request in TRACE); search "request to find cheapest product with constraint" → `request` (claim relation), `search_web` (operation); search "describe a requested search action as a TERM" → no suitable constructor; search "search for an item with filter and sort request" → `sort` (operation), `request` (claim relation), no request-description TERM.
- Typed parameters: target: STRING / ATOM[object_label]; constraints: LIST[TERM]; rank_field?: STRING; rank_direction?: STRING.
- Interpretation: A non-executable description of a requested product search, with explicit criteria and optional ordering field and direction. It describes intent only and does not assert that a search occurred or produced results.
- Example: `TERM product_search(target=object_label::psu, constraints=[requirement_2], rank_field=rank_price, rank_direction=dir_asc) -> product_search_2 : TERM`
- Contrast: Not the external catalog-query operation `search_web`, nor a claim that any matching product exists.
- Proposed record: {"symbol": "product_search", "kind": "constructor", "signature": "TERM product_search(target: STRING / ATOM[object_label], constraints: LIST[TERM], rank_field?: STRING, rank_direction?: STRING) -> TERM", "definition": "A structured description of a requested product search with explicit criteria and optional ranking field and direction. It describes requested intent only; it neither performs a search nor asserts that results exist.", "not": "An executed search operation or a factual claim about returned products.", "aliases": []}

### S2 | type: add | dimension: vocabulary-member | symbol: unit_watt
- Needs: n4 (t1:s1)
- Searches tried: widen "Watt unit for power measurement" → no watt unit; search "unit watt W power" and "electric power measurement unit watt" → `unit_gram`, `unit_liter`, `unit_fahrenheit`, and unrelated duration units, none denote power in watts.
- Meaning: The watt (symbol W), the SI unit of power.
- Category: unit-value.
- Contextual aliases: W, watt, watts.
- Example: `TERM measure(amount=600, unit=unit_watt) -> measure_2 : TERM`
- Contrast: Not a duration, energy, capacity, or voltage unit.
- Proposed record: {"symbol": "unit_watt", "kind": "value", "category": "unit-value", "definition": "The watt (symbol W), the SI derived unit of power. It denotes power, not energy or voltage.", "not": "A duration, energy, capacity, or voltage unit.", "aliases": ["W", "watt", "watts"]}
