### S1 | type: add | dimension: vocabulary-member | symbol: morning
- Needs: n11 (t1:s2)
- Searches tried: initial need candidates included `daytime`, `nighttime`, `unit_day`, `time_point`; `widen "morning departure flight, specifically 5:00 AM"` returned `daytime`, `nighttime`, `time_point`, none of which defines the morning period; `widen "flight departure at exact clock time five AM"` found no morning-period value.
- Meaning: The morning period of a day, without fixing an exact clock time or implying that it is naturally daylight.
- Category: time-of-day-value
- Contextual aliases: morning
- Example: `TERM requirement(property="departure_period", value=morning) -> requirement_2 : TERM`
- Contrast: `daytime` means the natural daylight period; morning can occur before sunrise and does not specify a clock time.
- Proposed record: {"symbol": "morning", "kind": "value", "category": "time-of-day-value", "definition": "The morning period of a day. It does not specify an exact clock time or imply that it is naturally daylight.", "not": "the natural daylight period (daytime) or an exact clock time", "aliases": ["morning"]}
