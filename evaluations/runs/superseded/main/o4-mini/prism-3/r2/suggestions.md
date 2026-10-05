### S1 | type: add | dimension: constructor | symbol: why_question
- Needs: n1 (t1:s1), n10 (t3:s1), n18 (t5:s1)
- Searches tried: "why question" → no matching constructor; widen "question constructor" → nothing
- Typed parameters: text: STRING
- Interpretation: A descriptive term representing a why‐question with its full text; asserts nothing.
- Example: TERM why_question(text="Why...?" ) -> why_question_2 : TERM
- Proposed record: {"symbol":"why_question","kind":"constructor","signature":"TERM why_question(text: STRING) -> TERM","definition":"A descriptive term representing a why‐question; includes the full question text without asserting an answer.","not":"a statement or answer","aliases":["why ask","why question"]}

### S3 | type: add | dimension: constructor | symbol: difficulty
- Needs: n4 (t2:s1)
- Searches tried: "challenges" → no matching TERM; widen "difficulty term" → none
- Typed parameters: activity: TERM, type: STRING
- Interpretation: A descriptive term for practical or policy challenges of an activity; asserts nothing.
- Example: TERM difficulty(activity=policy_document(title="..."), type="practical_and_policy_challenges") -> difficulty_2 : TERM
- Proposed record: {"symbol":"difficulty","kind":"constructor","signature":"TERM difficulty(activity: TERM, type: STRING) -> TERM","definition":"Describes a practical or policy challenge associated with an activity; asserts nothing.","not":"an executable operation or claim of failure","aliases":["challenge","difficulty"]}

### S4 | type: add | dimension: constructor | symbol: investment
- Needs: n5 (t2:s2)
- Searches tried: "investment" → no matching TERM; widen "invest amount term" → none
- Typed parameters: actor: STRING, object: STRING, amount: STRING
- Interpretation: A descriptive term representing an actor's investment in an object with a qualitative or quantitative description; asserts nothing.
- Example: TERM investment(actor="government", object="technology infrastructure", amount="significant") -> investment_2 : TERM
- Proposed record: {"symbol":"investment","kind":"constructor","signature":"TERM investment(actor: STRING, object: STRING, amount: STRING) -> TERM","definition":"A descriptive term for an investment by an actor in a specified object, described by amount; asserts nothing.","not":"a financial transaction execution","aliases":["invest","investment"]}