### S1 | type: add | dimension: vocabulary-member | symbol: unit_watt

- Needs: n4 (t1:s1)
- Searches tried:
  - `rag search "600W power output"` → returns only temperature (unit_fahrenheit), duration (unit_hour), and capacity units (cap_gb); no power unit
  - `rag search "watt unit"` → returns mass (unit_gram) and duration units; no power unit
  - `rag widen "power output unit"` → found unit_kilometer but no watt/power/electrical unit
  - `grep -i "watt\|power.*unit" /reference/glossary.md` → no matches

- Meaning: A unit of electrical power, used to specify power output or consumption (e.g., 600W, 1kW).
- Category: unit-value
- Contextual aliases: watt, W, watts, power, electrical power
- Example: `TERM measure(amount=600, unit=unit_watt) -> power_600w : TERM`
- Contrast: Not unit_fahrenheit (temperature), not cap_gb (storage capacity), not unit_gram (mass). Watts measure electrical power, not other physical quantities.
- Proposed record: `{"symbol": "unit_watt", "kind": "value", "category": "unit-value", "definition": "One watt unit of electrical power.", "aliases": ["watt", "W", "watts", "power"], "status": "Accepted"}`
