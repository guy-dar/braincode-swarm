### S1 | type: add | dimension: vocabulary-member | symbol: role_seniors
- Needs: n9 (t1:s1–t1:s2), n17 (t2:s20–t2:s26)
- Searches tried: search "senior passenger" → role_adults, role_son, role_daughter, foreigners; search "elderly person senior citizen" → role_adults, role_colleague, role_user; grep senior|elder in glossary → nothing. role_adults is wrong: the source counts "2 adults and 1 senior" as separate passenger categories.
- Meaning: Senior (older adult) participant group in travel, booking or event context, as a fare/admission category distinct from ordinary adults; no specific age threshold implied.
- Category: recipient-value
- Contextual aliases: senior, seniors, senior citizen, elderly
- Example: `TERM group_size(count=1, group=role_seniors) -> group_size_3 : TERM`
- Contrast: role_adults (general adult group); does not assert a person's exact age.
- Proposed record: `{"symbol": "role_seniors", "kind": "value", "category": "recipient-value", "signature": "STRING", "definition": "Senior (older adult) participant group in travel, booking or event context, treated as a category distinct from ordinary adults; no age threshold is implied.", "not": "role_adults (general adult participant group) or an exact age requirement", "aliases": ["senior", "seniors", "senior citizen"]}`

### S2 | type: add | dimension: vocabulary-member | symbol: morning
- Needs: n11 (t1:s2), n20 (t2:s36)
- Searches tried: search "morning time of day" → daytime, unit_day, nighttime, time_point; widen "morning departure time" --kind temporal → daytime, nighttime, time_point, time_horizon, temporal_context. daytime spans sunrise to sunset (too broad; a 5:00 AM morning flight may precede sunrise); time_point needs a clock time the user did not give.
- Meaning: The early part of the day, from roughly midnight/dawn until noon, as a qualitative time-of-day period; no exact boundaries or timezone implied.
- Category: time-of-day-value
- Contextual aliases: morning, AM, in the morning
- Example: `TERM requirement(property="departure_time_of_day", value=morning) -> requirement_8 : TERM`
- Contrast: daytime (sunrise to sunset), a specific clock time (time_point).
- Proposed record: `{"symbol": "morning", "kind": "value", "category": "time-of-day-value", "signature": "STRING", "definition": "The morning part of the day (before noon) as a qualitative time-of-day period; no exact boundaries or timezone implied.", "not": "daytime (whole sunrise-to-sunset period) or a clock timestamp (time_point)", "aliases": ["morning", "in the morning"]}`
