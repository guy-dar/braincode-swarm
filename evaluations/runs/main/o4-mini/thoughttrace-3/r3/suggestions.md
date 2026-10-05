### S1 | type: add | dimension: vocabulary-member | symbol: cannot_complete
- Needs: n1 (t1:s1)
- Searches tried: `rag search "cannot complete game"` → no suitable claim_relation; `rag widen "unable to complete game"` → nothing
- Kind: claim_relation
- Signature: `CLAIM cannot_complete(target: STRING / TERM) -> CLAIM`
- Definition: Asserts that the subject cannot complete the specified activity or process; describes a user’s inability without implying external system failure.
- not: a general system failure or error to be recorded (use failure)
- aliases: ["unable_to_finish", "cannot_finish"]
- Proposed record: {"symbol":"cannot_complete","kind":"claim_relation","signature":"CLAIM cannot_complete(target: STRING / TERM) -> CLAIM","definition":"Asserts that the specified subject or process cannot be completed; describes an inability without implying a system error.","not":"a system failure hypothesis (use failure)","aliases":["unable_to_finish","cannot_finish"]}

### S2 | type: add | dimension: constructor | symbol: request_help
- Needs: n2 (t1:s1)
- Searches tried: `rag search "request help"` → no TERM constructor; `rag widen "ask for assistance"` → nothing
- Typed parameters: object?: STRING / TERM
- Signature: `TERM request_help(object?: STRING / TERM) -> TERM`
- Interpretation: Represents a user’s request for assistance regarding an object or topic; asserts nothing by itself.
- not: an offer of help (use offer_help)
- aliases: ["ask_for_help","help_request"]
- Proposed record: {"symbol":"request_help","kind":"constructor","signature":"TERM request_help(object?: STRING / TERM) -> TERM","definition":"Represents a request by the user to receive assistance about the specified object or topic.","not":"an offer or provision of help (use offer_help)","aliases":["ask_for_help","help_request"]}

### S3 | type: add | dimension: constructor | symbol: property_question
- Needs: n6 (t2:s5), n9 (t2:s7), n10 (t2:s9)
- Searches tried: `rag search "property question"` → no constructor; `rag widen "question target property"` → nothing
- Typed parameters: subject: STRING / TERM, property: STRING
- Signature: `TERM property_question(subject: STRING / TERM, property: STRING) -> TERM`
- Interpretation: Asks for the named property of the subject; does not presuppose an answer.
- not: a generic request or information (use ask with a different TERM)
- aliases: ["ask_property","question_about"]
- Proposed record: {"symbol":"property_question","kind":"constructor","signature":"TERM property_question(subject: STRING / TERM, property: STRING) -> TERM","definition":"Constructs a question term requesting the specified property of the given subject without presupposing an answer.","not":"a statement or assertion about the property","aliases":["ask_property","question_about"]}
