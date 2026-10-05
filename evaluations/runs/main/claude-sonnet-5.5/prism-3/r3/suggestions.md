### S1 | type: add | dimension: constructor | symbol: open_question
- Needs: n1 (t1:s1), n18 (t5:s1)
- Searches tried: "why does government not" -> ask (needs TERM target), negation; "wouldn't you agree" -> confirm (CLAIM speech act, not a question); widen -> nothing for a why/agreement question
- Typed parameters: kind: STRING, subject: TERM / CLAIM, condition?: TERM
- Interpretation: asks for the reason (kind="why") or agreement (kind="agree") about the subject; describes only, asserts nothing.
- Example: `TERM open_question(kind="why", subject=negation_2) -> open_question_2 : TERM`
- Proposed record: `{"symbol": "open_question", "kind": "constructor", "signature": "TERM open_question(kind: STRING, subject: TERM / CLAIM, condition?: TERM) -> TERM", "definition": "A question about the reason for, or agreement with, the subject; describes only.", "not": "a property question asking a property value", "aliases": ["why question"]}`
