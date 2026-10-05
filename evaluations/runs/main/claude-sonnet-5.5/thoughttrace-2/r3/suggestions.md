### S1 | type: add | dimension: constructor | symbol: desires
- Needs: n3 (t3:s1), n14 (t4:s44)
- Searches tried: "user wants to go" → ask, recommended; "estimate" → prep_time; no relation for wanting or estimating
- Typed parameters: content: TERM
- Interpretation: the holder wants the described content; describes the wish, not its fulfilment.
- Example: `CLAIM desires(content=subject_6) BY "user" STATUS asserted SOURCE "t3:s1" -> desires_2 : CLAIM`
- Proposed record: `{"symbol": "desires", "kind": "claim_relation", "signature": "CLAIM desires(content: TERM)", "definition": "The holder wants the described content.", "not": "a request speech act or a fulfilled outcome", "aliases": ["wants"]}`
