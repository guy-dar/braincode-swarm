### S1 | type: add | dimension: constructor | symbol: occurs
- Needs: n6 (t2:s1), n9 (t2:s3), n11 (t2:s4), n16 (t4:s1), n20 (t4:s3)
- Searches tried: "companies adopting shorter hours" → user_practice (user-only habitual practice), ongoing (process TERM), occurred_recently (needs a CLAIM); "workers value free time" → none; "people usually have multiple jobs" → none
- Typed parameters: activity: TERM, regularity?: STRING
- Interpretation: the described activity/state occurs or obtains in its context; regularity (optional, e.g. "usual", "not_uncommon") qualifies how commonly; holder and status come from BY/STATUS. Not limited to a user.
- Example: `CLAIM occurs(activity=activity_2, regularity="not_uncommon") BY role_agent STATUS asserted SOURCE "t4:s1" -> occurs_2 : CLAIM`
- Proposed record: `{"symbol": "occurs", "kind": "claim_relation", "signature": "CLAIM occurs(activity: TERM, regularity?: STRING)", "definition": "The described activity or state takes place or obtains; optional regularity qualifies how commonly. Holder/status via BY/STATUS.", "not": "user_practice (a user's habitual workflow) or a recorded EVENT", "aliases": ["takes_place", "happens"]}`

### S2 | type: add | dimension: constructor | symbol: yes_no_question
- Needs: n13 (t3:s1)
- Searches tried: "ask if Japanese people usually have two or more jobs" → ask (needs TERM target), subject, requirement (none forms a polar question); widen "yes/no question about whether" → nothing
- Typed parameters: proposition: TERM, regularity?: STRING
- Interpretation: a question whether the described activity/state holds (optionally usually/regularly); asks only, presupposes no answer.
- Example: `TERM yes_no_question(proposition=activity_2, regularity="usual") -> yes_no_question_2 : TERM`
- Proposed record: `{"symbol": "yes_no_question", "kind": "constructor", "signature": "TERM yes_no_question(proposition: TERM, regularity?: STRING) -> TERM", "definition": "Polar question whether the described activity or state holds; optional regularity qualifies frequency. Asserts nothing.", "not": "a property_question seeking a value, or an assertion", "aliases": ["is it the case that"]}`
