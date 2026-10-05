### S1 | type: add | dimension: constructor | symbol: property_question
- Needs: n17 (t3:s1)
- Searches tried: "ask whether grass can be cut using scissors" → ask (speech_act) with TERM target; but target must be TERM property_question, not activity
- Typed parameters: property: STRING, subject: STRING / TERM
- Interpretation: an open request for the named property or method of the subject, without presupposing an answer
- Example: TERM property_question(property="cutting_method", subject=object_label::grass) -> question_2 : TERM
- Proposed record: {"symbol": "property_question", "kind": "constructor", "signature": "TERM property_question(property: STRING, subject: STRING / TERM) -> TERM", "definition": "An open request for the named property or method of the subject; does not supply the value.", "not": "An assertion of the property or its value", "aliases": ["property question", "ask for property", "method question"]}