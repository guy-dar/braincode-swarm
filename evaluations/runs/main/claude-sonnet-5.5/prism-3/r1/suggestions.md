### S1 | type: add | dimension: constructor | symbol: why_question
- Needs: n1 (t1:s1)
- Searches tried: "why does government not do X" → ask (speech act needing TERM target), negation (no question), enables (claim, not question); no constructor for a reason/cause-seeking question
- Typed parameters: target: TERM / CLAIM
- Interpretation: asks for the reason or explanation of the described state of affairs; describes a question, asserts nothing and presupposes no answer.
- Example: `TERM why_question(target=negation_2) -> why_question_2 : TERM`
- Proposed record: `{"symbol": "why_question", "kind": "constructor", "signature": "TERM why_question(target: TERM / CLAIM) -> TERM", "definition": "A question asking for the reason or explanation of the target state of affairs; presupposes no answer.", "not": "property_question or a causal claim", "aliases": ["why", "why not"]}`
