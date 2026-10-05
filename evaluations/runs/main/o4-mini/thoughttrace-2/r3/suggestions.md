### S1 | type: add | dimension: vocabulary-member | symbol: role_parents
- Needs: n6 (t3:s1)
- Searches tried: "parents as travel companions" → only role_adults; widen "parent group recipient" → nothing
- Definition: A recipient-value atom denoting the user’s parents as a group.
- Category: recipient-value
- Aliases: parents
- Not: role_adults (too generic)
- Proposed record: {"symbol":"role_parents","kind":"value","category":"recipient-value","definition":"The user’s parents as a travel companion group.","aliases":["parents"]}

### S2 | type: add | dimension: vocabulary-member | symbol: style_adventure
- Needs: n7 (t3:s1)
- Searches tried: "adventure style vibe" → style_narrative (story style); widen "adventure style" → nothing
- Definition: A style-value atom denoting an adventure-oriented travel vibe.
- Category: style-value
- Aliases: adventure
- Not: style_narrative (narrative story style)
- Proposed record: {"symbol":"style_adventure","kind":"value","category":"style-value","definition":"An adventure-focused travel style or vibe.","aliases":["adventure"]}

### S3 | type: add | dimension: constructor | symbol: itinerary_plan
- Needs: n10 (t4:s1)
- Searches tried: art_itinerary (artifact class only for GENERATE), propose (speech act only); widen "itinerary summary term" → nothing
- Typed parameters: destination: STRING, dates: TERM, travelers: TERM, style: ATOM[style-value], constraints: LIST[TERM]
- Interpretation: A TERM summarizing a proposed travel plan with its key parameters.
- Example: `TERM itinerary_plan(destination="Rome+Tuscany", dates=date_pref, travelers=party_role, style=style_adventure, constraints=[budget_limit,duration_limit]) -> itinerary_plan_2 : TERM`
- Not: GENERATE (it produces an artifact, not a structured TERM)
- Proposed record: {"symbol":"itinerary_plan","kind":"constructor","signature":"TERM itinerary_plan(destination: STRING, dates: TERM, travelers: TERM, style: ATOM[style-value], constraints: LIST[TERM]) -> TERM","definition":"A structured term summarizing a proposed travel itinerary with destination, dates, travelers, style, and constraints.","not":"an artifact generation (use GENERATE for the actual plan)","aliases":[]}