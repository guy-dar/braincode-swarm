### S1 | type: add | dimension: constructor | symbol: adopt_persona
- Needs: n2 (t1:s1)
- Searches tried: "adopt a playboy persona" → only gender_identity (constructs demographic identity), persona constructors none; widen "assume persona" → no results
- Typed parameters: persona: STRING
- Interpretation: descriptive term for adopting the specified persona; asserts nothing
- Example: `TERM adopt_persona(persona="playboy") -> adopt_persona_2 : TERM`
- Proposed record: {"symbol":"adopt_persona","kind":"constructor","signature":"TERM adopt_persona(persona: STRING) -> TERM","definition":"A descriptive term for adopting the specified persona; asserts nothing.","not":"an assertion that the persona change has occurred","aliases":["assume_persona","take_on_persona"]}

### S2 | type: add | dimension: vocabulary-member | symbol: rely_on
- Needs: n20 (t6:s2)
- Searches tried: "rely on charm" → enables (facilitates outcome), widen "rely on" → nothing
- Category: claim_relation
- Signature: CLAIM rely_on(condition: TERM / CLAIM, basis: STRING / TERM) -> CLAIM
- Definition: expresses dependence on a factor as the basis for an action or outcome
- not: a guarantee of success or facilitation (use enables)
- aliases: ["depend_on"]
- Proposed record: {"symbol":"rely_on","kind":"claim_relation","signature":"CLAIM rely_on(condition: TERM / CLAIM, basis: STRING / TERM) -> CLAIM","definition":"Expresses dependence on a factor as the basis for an action or outcome.","not":"a claim of facilitation or guarantee of success","aliases":["depend_on"]}