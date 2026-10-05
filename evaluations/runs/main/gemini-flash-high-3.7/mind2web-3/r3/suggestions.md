### S1 | type: add | dimension: vocabulary-member | symbol: unit_watt
- Needs: n4 (t1:s1)
- Searches tried: search "watt" "power" "unit_watt" "power_output" → only duration/mass/temperature units (unit_gram, unit_fahrenheit, unit_hour, cap_gb); widen "watt" --kind constraint → no electrical or power unit in the glossary
- Meaning: Standard SI unit of power equal to one joule per second (symbol: W).
- Category: unit-value
- Contextual aliases: ["watt", "watts", "W"]
- Example: `TERM measure(amount=600, unit=unit_watt) -> measure_2 : TERM`
- Contrast: energy units (joules, kilowatt-hours), electrical potential (volts), or digital capacity (cap_gb)
- Proposed record: {"symbol": "unit_watt", "kind": "value", "category": "unit-value", "definition": "Standard SI unit of power equal to one joule per second.", "not": "energy units (like joules or kilowatt-hours) or electrical potential (volts)", "aliases": ["watt", "watts", "W"]}
