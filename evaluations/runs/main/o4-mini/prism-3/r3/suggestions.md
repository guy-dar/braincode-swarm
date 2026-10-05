### S1 | type: add | dimension: constructor | symbol: question_why
- Needs: n1 (t1:s1)
- Searches tried:
  • `node /kit/rag.mjs search "why question"` → only `property_question`
  • widen "why question" → no results
- Typed parameters:
  • action: TERM
  • mechanism: STRING
- Definition: A WH-question term requesting the reason why the specified action (TERM) is not carried out, with an optional mechanism identifier.
- Restrictions: mechanism is a brief identifier or phrase, not a full sentence.
- Example: `TERM question_why(action=activity(verb="start", actor="engine", object=object_label::vehicle), mechanism="low_battery") -> question_why_2 : TERM`
- Not: a factual claim or conditional ('if...then...')
- Aliases: ["why question","reason why"]
- Proposed record:
  {"symbol":"question_why","kind":"constructor","signature":"TERM question_why(action: TERM, mechanism: STRING) -> TERM","definition":"A WH-question term requesting the reason why the specified action (TERM) is not carried out, with an optional mechanism identifier.","not":"a factual claim or conditional ('if...then...')","aliases":["why question","reason why"]}

### S2 | type: add | dimension: vocabulary-member | symbol: social_security_number
- Needs: n3 (t1:s1)
- Searches tried:
  • `node /kit/rag.mjs search "social security number"` → no candidates
  • widen "unique identification" → no results
- Definition: A government-issued identifier uniquely assigned to an individual, such as a U.S. Social Security Number.
- Category: entity-name
- Contextual aliases: ["SSN","social security number"]
- Example: `TERM activity(verb="store", actor="service", object="social_security_number") -> store_ssn_2 : TERM`
- Not: A database record or any broader unique ID system.
- Proposed record:
  {"symbol":"social_security_number","kind":"value","category":"entity-name","definition":"A government-issued identifier uniquely assigned to an individual, such as a U.S. Social Security Number.","aliases":["SSN","social security number"]}