### S1 | type: add | dimension: vocabulary-member | symbol: unit_watt
- Needs: n4 (t1:s1)
- Searches tried: "watt" → ram_unit, unit_gram, unit_fahrenheit; widen "watt" --kind constraint → at_least, unit_gram, unit_fahrenheit; "power output" → rate, maximum_between_stops, outcome; no power/watt unit in unit-value
- Meaning: Standard SI derived unit of power measurement equal to one joule per second (1 W).
- Category: unit-value
- Contextual aliases: W, watt, watts, w
- Example: `TERM measure(amount=600, unit=unit_watt) -> measure_2 : TERM`
- Contrast: energy units or temporal duration units
- Proposed record: {"symbol": "unit_watt", "kind": "value", "category": "unit-value", "definition": "Standard SI derived unit of power measurement equal to one joule per second (1 W).", "not": "energy units or temporal duration units", "aliases": ["W", "watt", "watts", "w"]}
