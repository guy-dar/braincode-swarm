### S1 | type: add | dimension: constructor | symbol: work_life_balance
- Needs: n1 (t1:s1), n3, n4
- Searches tried:
  - search "work-life balance" → no matching constructor or composite
  - widen "balance of work and leisure" → nothing usable
- Typed parameters: location: ATOM[country]
- Interpretation: The concept of balancing work responsibilities and personal leisure time in the specified location; asserts nothing.
- Example: `TERM work_life_balance(location=country::JP) -> work_life_balance_2 : TERM`
- Proposed record: `{"symbol":"work_life_balance","kind":"constructor","signature":"TERM work_life_balance(location: ATOM[country]) -> TERM","definition":"The concept of balancing work responsibilities and personal leisure time in the specified location; asserts nothing.","not":"an actionable policy or specific working-hours change","aliases":["work-life balance","work life balance"]}`

### S2 | type: add | dimension: constructor | symbol: multiple_part_time_jobs
- Needs: n13 (t3:s1), n14
- Searches tried:
  - search "multiple part-time jobs" → no matching term
  - widen "two or more jobs" → nothing usable
- Typed parameters: subject: STRING
- Interpretation: The concept of individuals holding multiple part-time jobs; subject describes who holds these jobs.
- Example: `TERM multiple_part_time_jobs(subject="Japanese people") -> multiple_part_time_jobs_2 : TERM`
- Proposed record: `{"symbol":"multiple_part_time_jobs","kind":"constructor","signature":"TERM multiple_part_time_jobs(subject: STRING) -> TERM","definition":"The concept of individuals holding multiple part-time jobs; subject describes who holds these jobs.","not":"an assertion of prevalence or frequency","aliases":["multiple jobs","two or more jobs"]}`
