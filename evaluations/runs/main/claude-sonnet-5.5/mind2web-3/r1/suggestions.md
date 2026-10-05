### S1 | type: add | dimension: vocabulary-member | symbol: unit_watt
- Needs: n4 (t1:s1)
- Searches tried: "600W power output" → at_least (needs a measure), unit_fahrenheit/unit_gram/unit_liter/unit_percent (other quantities), no power unit
- Meaning: watt, SI unit of power.
- Category: unit-value
- Contextual aliases: W, watt, watts
- Example: `TERM measure(amount=600, unit=unit_watt) -> measure_2 : TERM`
- Contrast: not an energy unit (watt-hour) nor a duration unit
- Proposed record: `{"symbol": "unit_watt", "kind": "value", "category": "unit-value", "definition": "Standard SI unit of power (watt, W).", "not": "energy units such as watt-hour", "aliases": ["W", "watt", "watts"]}`
