### S1 | type: add | dimension: constructor | symbol: reconcile_accounts
- Needs: n1 (t1:s1), n2 (t1:s1), n7 (t2:s1, t2:s2)
- Searches tried: "reconcile accounts receivable balance sheet" → reconcile_code (code entities only), calculation; no financial reconciliation constructor
- Typed parameters: accounts: LIST[TERM], against?: STRING / TERM
- Interpretation: description of bringing the listed accounts into agreement with the reference records; asserts nothing.
- Example: `TERM reconcile_accounts(accounts=[subject_2, subject_3], against="financial_statements") -> reconcile_accounts_2 : TERM`
- Proposed record: `{"symbol": "reconcile_accounts", "kind": "constructor", "signature": "TERM reconcile_accounts(accounts: LIST[TERM], against?: STRING / TERM) -> TERM", "definition": "Description of making the listed accounting accounts agree with the reference records; asserts nothing.", "not": "reconcile_code (code entities)", "aliases": ["reconcile accounts"]}`

### S2 | type: add | dimension: constructor | symbol: property_question
- Needs: n4 (t1:s2)
- Searches tried: "ask what X means" → ask (needs a TERM target), subject, attribute_claim; no question constructor
- Typed parameters: subject: STRING / TERM, property: STRING, context?: TERM
- Interpretation: asks for the named property of the subject (optionally within context), without presupposing an answer.
- Example: `TERM property_question(property="meaning", subject=subject_4, context=subject_5) -> property_question_2 : TERM`
- Proposed record: `{"symbol": "property_question", "kind": "constructor", "signature": "TERM property_question(subject: STRING / TERM, property: STRING, context?: TERM) -> TERM", "definition": "Asks for the named property of the subject, optionally in a context; presupposes no answer.", "not": "attribute_claim (an assertion)", "aliases": ["what is the"]}`

### S3 | type: add | dimension: constructor | symbol: possible
- Needs: n19 (t4:s1)
- Searches tried: "can be created capability possibility" → enables, statement, request; none express possibility
- Typed parameters: target: TERM
- Interpretation: describes that the target activity is feasible/permitted; asserts nothing until wrapped in a claim.
- Example: `TERM possible(target=activity_4) -> possible_2 : TERM`
- Proposed record: `{"symbol": "possible", "kind": "constructor", "signature": "TERM possible(target: TERM) -> TERM", "definition": "Describes that the target activity can be done; asserts nothing.", "not": "occurred or request", "aliases": ["can", "is able to"]}`
