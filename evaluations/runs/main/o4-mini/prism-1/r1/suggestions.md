### S1 | type: add | dimension: constructor | symbol: problem_question
- Needs: n1 (t1:s1)
- Searches tried: "problem question" → no matching question-focused constructor; `property_question` is for subject/property only.
- Typed parameters: subjects: LIST[TERM], location: ATOM[country]
- Signature: TERM problem_question(subjects: LIST[TERM], location: ATOM[country]) -> TERM
- Definition: A question asking what problems exist, with respect to the listed subject terms in the given location; asserts nothing.
- not: Not a claim of facts or answers.
- aliases: ["problem question", "issues question"]

### S2 | type: add | dimension: composite | symbol: topic_personal_hobbies
- Needs: n4 (t1:s1)
- Searches tried: "personal hobbies" → no topic-VALUE or TERM constructor; `user_practice` is a claim relation, not a topic.
- Expansion: subject(kind="hobby", qualifier="personal")
- Signature: TERM topic_personal_hobbies() -> TERM
- Definition: The topic of personal hobbies; a subject matter describing leisure activities people enjoy.
- not: Not a claim that the person currently performs them.
- aliases: ["personal hobbies", "leisure activities"]
