### S1 | type: add | dimension: constructor | symbol: disjunction
- Needs: n9 (t1:s20)
- Searches tried: "bug or misuse" / "either or alternatives" → conjunction (all apply), conditional; nothing for alternatives
- Typed parameters: items: LIST[TERM]
- Interpretation: at least one of the described alternatives applies; describes, asserts nothing.
- Example: `TERM disjunction(items=[activity_6, activity_7]) -> disjunction_2 : TERM`
- Proposed record: `{"symbol": "disjunction", "kind": "constructor", "signature": "TERM disjunction(items: LIST[TERM]) -> TERM", "definition": "At least one of the described alternatives applies.", "not": "conjunction (all apply)", "aliases": ["or", "either"]}`
