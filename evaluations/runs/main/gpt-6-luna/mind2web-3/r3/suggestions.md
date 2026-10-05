### S1 | type: add | dimension: constructor | symbol: catalog_search_request
- Needs: n1 (t1:s1), n3 (t1:s1)
- Searches tried: search “TERM description of search action query target and filters” → `search_web`, `select_filter`, `apply_filters` are executable operations; search “TERM product search request cheapest product minimum output” → `rank_price`, `dir_asc` are ranking values, not a request description; widen “request to find an item satisfying property constraints” → `requirement` and other constraints, but no catalog-search request TERM.
- Typed parameters: target: TERM, constraints: LIST[TERM], rank_field?: STRING, rank_direction?: STRING
- Interpretation: Describes a request to search a catalog for the target subject under the supplied constraints, optionally ordering results by the specified ranking field and direction (`rank_*` and `dir_*` values, respectively). It neither executes a search nor asserts that matching products exist.
- Example: `TERM catalog_search_request(target=subject_2, constraints=[requirement_2], rank_field=rank_price, rank_direction=dir_asc) -> catalog_search_request_2 : TERM`
- Contrast: A search operation that queries a catalog or an assertion that a product was found.
- Proposed record: {"symbol":"catalog_search_request","kind":"constructor","signature":"TERM catalog_search_request(target: TERM, constraints: LIST[TERM], rank_field?: STRING, rank_direction?: STRING) -> TERM","definition":"Describes a catalog search request for a target subject under supplied constraints, optionally ordered by a rank_* field and dir_* direction. It does not execute a search or assert that matching products exist.","not":"an executable catalog query or a claim that matching products were found","aliases":["product search request","search for products"]}

### S2 | type: add | dimension: vocabulary-member | symbol: unit_watt
- Needs: n4 (t1:s1)
- Searches tried: search “unit of electrical power watts W” → no watt unit; search “watt power output unit measure 600 W” and widen “measure a quantity in watts, unit W” → `measure` accepts a unit but the retrieved nearby units (`unit_gram`, `unit_liter`, `unit_fahrenheit`) do not denote power.
- Meaning: SI unit of power equal to one joule per second.
- Category: unit-value
- Contextual aliases: W, watt, watts
- Example: `TERM measure(amount=600, unit=unit_watt) -> measure_2 : TERM`
- Contrast: Not a capacity unit such as `cap_gb`, nor a unit of energy.
- Proposed record: {"symbol":"unit_watt","kind":"value","category":"unit-value","signature":"STRING unit_watt","definition":"The SI unit of power equal to one joule per second. Used as the unit for measured power quantities.","not":"an energy unit or a digital-capacity unit","aliases":["W","watt","watts"]}

### S3 | type: add | dimension: constructor | symbol: entity_description
- Needs: n2 (t1:s1)
- Searches tried: widen “multiword object-kind label power supply unit described as a TERM without splitting words” → `object_label`, `lexical_label`; search “TERM constructor preserves exact multiword object kind label” → the same. `object_label` is an open group whose lower_word key form does not admit a phrase with spaces, and `lexical_label` requires a group atom rather than a phrase.
- Typed parameters: label: STRING
- Interpretation: A structured exact label for a source-named entity or entity kind when no accepted lexical-group value can preserve its word boundaries. It asserts no additional sense, properties, taxonomy, or behavior.
- Example: `TERM entity_description(label="power supply unit") -> entity_description_2 : TERM`
- Contrast: Not an inference that an entity has properties beyond the literal source label.
- Proposed record: {"symbol":"entity_description","kind":"constructor","signature":"TERM entity_description(label: STRING) -> TERM","definition":"Preserves the exact source-supplied label of an entity or entity kind as a TERM when no accepted leaf group can encode its word boundaries. It adds no inferred sense, properties, taxonomy, or behavior.","not":"an entity record with inferred properties or a claim that the labeled entity exists","aliases":["exact entity label"]}
