### S1 | type: add | dimension: constructor | symbol: persona
- Needs: n2 (t1:s1)
- Searches tried: "playboy persona" → no matching constructor; widen "adopt a persona" → nothing
- Typed parameters: role: STRING
- Signature: TERM persona(role: STRING) -> TERM
- Definition: A descriptive term representing the persona or role the agent should adopt; asserts nothing.
- not: Not an identity assertion (use identity), not a user_request (use claim request)
- aliases: ["adopt persona","role"]
- Example: `TERM persona(role="playboy") -> persona_2 : TERM`
- Proposed record:
  {"symbol":"persona","kind":"constructor","signature":"TERM persona(role: STRING) -> TERM","definition":"A descriptive term representing the persona or role the agent should adopt; asserts nothing.","not":"Not an identity assertion","aliases":["adopt persona","role"]}

### S2 | type: add | dimension: vocabulary-member | symbol: tone_flirty
- Needs: n4 (t1:s1)
- Searches tried: entry tone_flirty → none; widen "flirty tone" → no tone_value candidate
- Category: tone-value
- Definition: A playful or flirtatious conversational register.
- not: Flowery or overly formal register
- aliases: ["flirtatiously","flirty"]
- Proposed record:
  {"symbol":"tone_flirty","kind":"value","category":"tone-value","definition":"A playful or flirtatious conversational register.","not":"Flowery or overly formal register","aliases":["flirtatiously","flirty"]}

### S3 | type: add | dimension: vocabulary-member | symbol: tone_intellectual
- Needs: n5 (t1:s1)
- Searches tried: entry tone_intellectual → none; widen "intellectual tone" → nothing
- Category: tone-value
- Definition: A register conveying thoughtful, analytical, or scholarly style.
- not: Just formal or persuasive tone
- aliases: ["intellectually","scholarly"]
- Proposed record:
  {"symbol":"tone_intellectual","kind":"value","category":"tone-value","definition":"A register conveying thoughtful, analytical, or scholarly style.","not":"Just formal or persuasive tone","aliases":["intellectually","scholarly"]}

### S4 | type: add | dimension: constructor | symbol: property_question
- Needs: n7 (t1:s4)
- Searches tried: entry property_question → only in examples, not glossary; widen "ask what X did" → nothing
- Typed parameters: subject: STRING, property: STRING
- Signature: TERM property_question(subject: STRING, property: STRING) -> TERM
- Definition: A structured term representing a question asking for the named property of the subject.
- not: Not an assertion of the property's value
- aliases: ["what did","what is the"]
- Example: `TERM property_question(subject="you", property="weekend activities") -> pq_2 : TERM`
- Proposed record:
  {"symbol":"property_question","kind":"constructor","signature":"TERM property_question(subject: STRING, property: STRING) -> TERM","definition":"A structured term representing a question requesting the named property of a subject.","not":"Not an assertion of a value","aliases":["what did","what is the"]}

### S5 | type: add | dimension: constructor | symbol: schedule_availability
- Needs: n9 (t1:s7)
- Searches tried: entry schedule_availability → none; widen "availability for next week" → nothing
- Typed parameters: period: STRING
- Signature: TERM schedule_availability(period: STRING) -> TERM
- Definition: A term describing a request for availability during the specified period.
- not: Not a precise timestamp (use time_point for exact dates)
- aliases: ["when free","availability"]
- Example: `TERM schedule_availability(period="next week") -> sched_2 : TERM`
- Proposed record:
  {"symbol":"schedule_availability","kind":"constructor","signature":"TERM schedule_availability(period: STRING) -> TERM","definition":"A term describing a request for availability during the specified period.","not":"Not a precise timestamp","aliases":["when free","availability"]}

### S6 | type: add | dimension: constructor | symbol: explain
- Needs: n12 (t1:s6)
- Searches tried: entry explain → none; widen "explain why late" → nothing
- Typed parameters: reason: STRING
- Signature: TERM explain(reason: STRING) -> TERM
- Definition: A structured term requesting an explanation of the specified reason.
- not: Not an assertion of fact
- aliases: ["why","explanation"]
- Example: `TERM explain(reason="I saw it too late") -> explain_2 : TERM`
- Proposed record:
  {"symbol":"explain","kind":"constructor","signature":"TERM explain(reason: STRING) -> TERM","definition":"A structured term requesting an explanation of the specified reason.","not":"Not an assertion of fact","aliases":["why","explanation"]}