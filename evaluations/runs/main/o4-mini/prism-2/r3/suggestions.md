### S1 | type: add | dimension: constructor | symbol: procedure_question
- Needs: n1 (t1:s1), n17 (t3:s1)
- Searches tried: "how to mow" → no question-form constructors; widen "procedure question" → no candidates
- Typed parameters: procedure: TERM
- Interpretation: an open request for step-by-step instructions to perform the described procedure; asserts nothing
- Example: `TERM procedure_question(procedure=mow_lawn_2) -> procedure_question_2 : TERM`
- Proposed record: {"symbol":"procedure_question","kind":"constructor","signature":"TERM procedure_question(procedure: TERM) -> TERM","definition":"An open request for instructions to perform the described procedure; asserts nothing.","not":"a claim that the procedure has been executed","aliases":["instruction request","how to"],"expansion":""}