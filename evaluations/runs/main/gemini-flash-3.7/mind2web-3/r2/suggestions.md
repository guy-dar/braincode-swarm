### S1 | type: add | dimension: vocabulary-member | symbol: unit_watt
- Needs: n4 (t1:s1)
- Searches tried: "watt" → ram_unit, unit_gram; "unit_watt" → ram_unit, unit_gram; widen "watt" --kind unit → no electrical power unit in unit-value
- Meaning: Standard SI derived unit of power measurement (watt, W).
- Category: unit-value
- Contextual aliases: W, watt, watts
- Example: `TERM measure(amount=600, unit=unit_watt) -> measure_2 : TERM`
- Contrast: digital capacity units (like cap_gb), temporal duration units (unit_second), or temperature units (unit_fahrenheit)
- Proposed record: {"symbol": "unit_watt", "kind": "value", "category": "unit-value", "definition": "Standard SI derived unit of power measurement equal to one joule per second.", "not": "digital capacity units (like cap_gb) or temporal duration units", "aliases": ["W", "watt", "watts"]}
