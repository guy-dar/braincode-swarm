### S1 | type: add | dimension: constructor | symbol: property_question
- Needs: n1 (t1:s1)
- Searches tried:  
  • search "why X" → no question constructors in glossary
  • widen "question constructor" → nothing
- Typed parameters: subject: STRING, property: STRING
- Interpretation: a structured term representing a question asking why the subject has or lacks the specified property or action; asserts nothing.
- Example:  
  `TERM property_question(subject=policy_document(title="Example Policy"), property="effectiveness") -> property_question_2 : TERM`
- Proposed record:  
  {"symbol":"property_question","kind":"constructor","signature":"TERM property_question(subject: STRING, property: STRING) -> TERM","definition":"A term representing a question asking why the subject exhibits or does not exhibit the specified property or action.","not":"a factual claim or assertion; not an action or generation.","aliases":["why","reason for"]}