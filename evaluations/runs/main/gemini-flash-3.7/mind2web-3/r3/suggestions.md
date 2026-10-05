### S1 | type: add | dimension: vocabulary-member | symbol: unit_watt
- Needs: n4 (t1:s1)
- Searches tried: search "watt" → ram_unit, unit_gram, lamp; search "power output" → outcome, lamp, unit_fahrenheit; search "unit_watt" → ram_unit, unit_gram; widen "At least 600W power output" → at_least, rate, min_ram; grep "unit-value" in /reference/glossary.md → unit_fahrenheit, unit_gram, unit_kilometer, unit_liter, unit_percent
- Meaning: Standard International System (SI) derived unit of power equal to one joule per second (1 W).
- Category: unit-value
- Contextual aliases: W, watt, watts
- Example: `TERM measure(amount=600, unit=unit_watt) -> measure_2 : TERM`
- Contrast: energy units, digital capacity units (like cap_gb) or temporal duration units (like unit_second)
- Proposed record: {"symbol": "unit_watt", "kind": "value", "category": "unit-value", "definition": "Standard International System (SI) derived unit of power equal to one joule per second (1 W).", "not": "energy units, digital capacity units (like cap_gb) or temporal duration units (like unit_second)", "aliases": ["W", "watt", "watts"]}
