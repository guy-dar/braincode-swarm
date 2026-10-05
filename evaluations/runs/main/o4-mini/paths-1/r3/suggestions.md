### S1 | type: add | dimension: vocabulary-member | symbol: tone_flirty
- Needs: n4 (t1:s1)
- Searches tried: "flirty tone" → tone_silly, tone_polite, tone_casual, style_catchy; widen "flirty tone" → no candidates
- Meaning: A playful, suggestive romantic register conveying flirtation.
- Category: tone-value
- Contextual aliases: flirtatious, suggestive
- Example: UTTER ask(constraints=[playboy_persona], tone=tone_flirty)
- not: not a general silly tone or casual register
- Proposed record: {"symbol":"tone_flirty","kind":"value","category":"tone-value","definition":"A playful, suggestive romantic register conveying flirtation.","aliases":["flirtatious","suggestive"],"not":"not a general silly or casual tone"}

### S2 | type: add | dimension: constructor | symbol: causal_question
- Needs: n7 (t1:s4)
- Searches tried: "ask what the other person did over the weekend" → ask, how should; widen "weekend activity question" → no candidates
- Typed parameters: cause: TERM, effect: TERM
- Interpretation: A question asking what effect (activity) resulted from the specified cause; describes a causal inquiry.
- Example: TERM causal_question(cause=subject(kind="algorithm", qualifier="your_algorithm"), effect=activity(verb="do", object="this weekend")) -> weekend_question : TERM
- not: not an assertion of a result
- Proposed record: {"symbol":"causal_question","kind":"constructor","signature":"TERM causal_question(cause: TERM, effect: TERM) -> TERM","definition":"A question asking what effect occurred as a result of a specified cause.","aliases":["what did X make Y do"],"not":"not a causal claim"}

### S3 | type: add | dimension: constructor | symbol: availability_question
- Needs: n9 (t1:s7)
- Searches tried: "ask about schedule availability for next week" → ask, time_point; widen "availability question" → no candidates
- Typed parameters: subject: TERM
- Interpretation: A question asking whether the specified time or period is available.
- Example: TERM availability_question(subject=time_point(period=unit_week)) -> next_week_question : TERM
- not: not a request to set availability
- Proposed record: {"symbol":"availability_question","kind":"constructor","signature":"TERM availability_question(subject: TERM) -> TERM","definition":"A question asking about schedule availability for the given subject period.","aliases":["availability_query","schedule_availability_question"],"not":"not a scheduling action"}