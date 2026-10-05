### S1 | type: add | dimension: vocabulary-member | symbol: unit_watt
- Needs: n4 (t1:s1)
- Searches tried: "watt power output unit" → unit_gram, unit_liter, unit_fahrenheit, unit_kilometer (other quantities); entry unit_watt → none
- Meaning: the SI unit of power, one joule per second.
- Category: unit-value
- Contextual aliases: W, watt, watts
- Example: `TERM measure(amount=600, unit=unit_watt) -> measure_2 : TERM`
- Contrast: not an energy unit (watt-hour) nor a duration unit
- Proposed record: `{"symbol": "unit_watt", "kind": "value", "category": "unit-value", "definition": "SI unit of power, one joule per second.", "not": "energy units such as watt-hour", "aliases": ["W", "watt", "watts"]}`
