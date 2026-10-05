### S1 | type: add | dimension: constructor | symbol: reason_question
- Needs: n1 (t1:s1), n5 (t5:s1)
- Searches tried: “why question constructor” → nothing; widen “question for reason” → none
- Typed parameters: proposition: TERM
- Interpretation: a question asking for the reason behind the given proposition; asserts nothing.
- Example: `TERM reason_question(proposition=some_term) -> reason_question_2 : TERM`
- Proposed record: {"symbol":"reason_question","kind":"constructor","signature":"TERM reason_question(proposition: TERM) -> TERM","definition":"A question asking for the reason behind the given proposition.","not":"a generic request action (use ask)","aliases":["why question","reason for"]}

### S2 | type: add | dimension: constructor | symbol: policy_document
- Needs: n4 (t2:s1)
- Searches tried: “policy document constructor” → found existing policy_document but missing `requirements`; widen “proposed_policy profile” → policy_document exists but signature omits requirements list
- Typed parameters: title: STRING, audience?: STRING, constraints?: LIST[TERM]
- Interpretation: constructs a structured representation of a policy proposal, with optional actors and constraint terms.
- Example: `TERM policy_document(title="identity verification policy", audience="government", constraints=[...]) -> policy_doc : TERM`
- Proposed record: {"symbol":"policy_document","kind":"constructor","signature":"TERM policy_document(title: STRING, audience?: STRING, constraints?: LIST[TERM]) -> TERM","definition":"A structured representation of a proposed policy with title, optional audience, and constraint terms.","not":"an enacted law or regulation","aliases":["policy proposal","policy spec"]}

### S3 | type: add | dimension: constructor | symbol: mitigation_question
- Needs: n10 (t3:s1)
- Searches tried: “how to mitigate question constructor” → none; widen “question for measures” → nothing
- Typed parameters: topic: TERM
- Interpretation: a question asking for possible measures or solutions pertaining to the given topic.
- Example: `TERM mitigation_question(topic=some_term) -> mitigation_question_2 : TERM`
- Proposed record: {"symbol":"mitigation_question","kind":"constructor","signature":"TERM mitigation_question(topic: TERM) -> TERM","definition":"A question requesting proposed measures or solutions for the given topic.","not":"an instruction to mitigate","aliases":["how to mitigate","ways to reduce"]}

### S4 | type: add | dimension: constructor | symbol: email_verification_term
- Needs: n13 (t4:s4)
- Searches tried: “email verification term constructor” → none; widen “require email confirmation TERM” → nothing
- Typed parameters: none
- Interpretation: a descriptive term representing the requirement to verify a user’s email address.
- Example: `TERM email_verification_term() -> email_verification_term_2 : TERM`
- Proposed record: {"symbol":"email_verification_term","kind":"constructor","signature":"TERM email_verification_term() -> TERM","definition":"A term denoting the requirement that a user verify their email address.","not":"the act of sending an email (use send_email)","aliases":["email confirmation requirement"]}

### S5 | type: refine | dimension: refine-entry | target: v19/claim/enables
- Needs: n12,n14,n16,n19 (t4:s5,t4:s8,t4:s8,t5:s1)
- Searches tried: entry enables → accepts (condition: TERM/CLAIM, outcome: TERM/CLAIM) → ok
- Before: allows facilitation generally; signature is correct but examples lack multi-use context
- After: specify no change to signature; provide usage examples in policy context
- Justification: clarifies expected TERM usage in policy-measure claims
- Proposed record: {"aliases":["facilitates","allows"],"status":"Accepted"}

### S6 | type: add | dimension: constructor | symbol: requirement
- Needs: n7,n15,n17 (t2:s4,t4:s7,t4:s7)
- Searches tried: “requirement constructor” → found requirement but as alias for constraint; widen “property requirement TERM” → nothing
- Typed parameters: property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]
- Interpretation: specifies a required property constraint with an expected primitive or structured value.
- Example: `TERM requirement(property="password_strength", value="strong") -> requirement_2 : TERM`
- Proposed record: {"symbol":"requirement","kind":"constructor","signature":"TERM requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> TERM","definition":"Specifies a required property constraint with an expected value.","not":"an assertion that an existing artifact has this property","aliases":["constraint","property_requirement","structured_requirement"]}

### S7 | type: add | dimension: constructor | symbol: two_factor_requirement
- Needs: n17 (t4:s10)
- Searches tried: “two-factor TERM” → nothing; widen “two-factor authentication term” → none
- Typed parameters: none
- Interpretation: a descriptive term representing the requirement for two-factor authentication.
- Example: `TERM two_factor_requirement() -> two_factor_requirement_2 : TERM`
- Proposed record: {"symbol":"two_factor_requirement","kind":"constructor","signature":"TERM two_factor_requirement() -> TERM","definition":"A term denoting the requirement for users to employ two-factor authentication.","not":"the mechanism itself (use send_code)","aliases":["two-factor requirement"]}

### S8 | type: add | dimension: constructor | symbol: tradeoff_summary
- Needs: n21,n22 (t6:s1–t6:s5)
- Searches tried: “policy tradeoff TERM” → none; widen “tradeoff TERM for privacy vs security” → nothing
- Typed parameters: topic: TERM
- Interpretation: a term capturing the need to balance conflicting considerations for the given topic.
- Example: `TERM tradeoff_summary(topic=some_term) -> tradeoff_summary_2 : TERM`
- Proposed record: {"symbol":"tradeoff_summary","kind":"constructor","signature":"TERM tradeoff_summary(topic: TERM) -> TERM","definition":"A term expressing the need to balance conflicting considerations for the given topic.","not":"a final decision or recommendation","aliases":["trade-off summary","balance discussion"]}