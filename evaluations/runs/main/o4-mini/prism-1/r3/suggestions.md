### S1 | type: add | dimension: composite | symbol: topic_work_personal_issues
- Needs: n1 (t1:s1), n4 (t1:s1)
- Searches tried:
  • "issues with work and personal time" → topic_school_work_routine (wrong domain: school)
  • no composite covering personal hobbies
- Expansion: `subject(kind="issue", qualifier=conjunction(items=[subject(kind="work"), subject(kind="hobby")]), location=$location)`
- Parameter mapping: `location: ATOM[country]`
- Proposed record:
  {"symbol":"topic_work_personal_issues","kind":"composite","signature":"TERM topic_work_personal_issues(location: ATOM[country]) -> TERM","definition":"The subject of issues arising from work and personal/leisure activities in the given location.","aliases":[],"expansion":"subject(kind=\"issue\", qualifier=conjunction(items=[subject(kind=\"work\"), subject(kind=\"hobby\")]), location=$location)"}

### S2 | type: add | dimension: constructor | symbol: policy_action
- Needs: n6 (t2:s1), n7 (t2:s1)
- Searches tried:
  • "implement shorter working hours" → activity (too generic, no list of changes)
  • no policy-oriented action constructor
- Typed parameters: actor: STRING, changes: LIST[TERM], location?: ATOM[country]
- Interpretation: Describes a policy enacted by the specified actor, consisting of the listed change terms and optional location; asserts nothing.
- Example:
  `TERM policy_action(actor="Acme Corp", changes=[subject(kind="working_hours"), subject(kind="flexible_arrangements")], location=country::US) -> policy_action_2 : TERM`
- Proposed record:
  {"symbol":"policy_action","kind":"constructor","signature":"TERM policy_action(actor: STRING, changes: LIST[TERM], location?: ATOM[country]) -> TERM","definition":"A policy enacted by the specified actor, consisting of the listed change terms and optional location.","not":"An executed operation or observed event","aliases":["enact_policy","implement_policy"]}

### S3 | type: add | dimension: constructor | symbol: job_count
- Needs: n15 (t3:s1), n14 (t3:s1)
- Searches tried:
  • "two or more jobs" → at_least (needs a measure), measure (expects unit)
  • no constructor for count of group members
- Typed parameters: group: ATOM[object_label] / STRING / TERM, count: NUMBER
- Interpretation: A term denoting that the specified group has at least the given count of members.
- Example:
  `TERM job_count(group=object_label::job, count=2) -> job_count_2 : TERM`
- Proposed record:
  {"symbol":"job_count","kind":"constructor","signature":"TERM job_count(group: ATOM[object_label] / STRING / TERM, count: NUMBER) -> TERM","definition":"Specifies that the given object group has at least the stated count.","not":"A per-period requirement or duration","aliases":["count_jobs","number_of_jobs"]}

### S4 | type: refine | dimension: refine-entry | target: activity
- Needs: n18 (t4:s1)
- Searches tried:
  • entry activity → signature has no qualifier slot
- Before: `TERM activity(verb: STRING, actor?: STRING, object?: STRING/TERM/ATOM[object_label], location?: STRING/ATOM[country], instrument?: STRING/ATOM[platform_label], purpose?: TERM) -> TERM`
- After: add parameter `qualifier?: STRING / ATOM[descriptive-value]`
- Justification: to qualify the object (e.g. part_time jobs)
- Affected uses: user_practice(activity=activity(..., qualifier=part_time))
- Compatibility: backward-compatible (optional parameter)
- Proposed record:
  {"signature":"TERM activity(verb: STRING, actor?: STRING, object?: STRING/TERM/ATOM[object_label], qualifier?: STRING/ATOM[descriptive-value], location?: STRING/ATOM[country], instrument?: STRING/ATOM[platform_label], purpose?: TERM) -> TERM"}

### S5 | type: add | dimension: vocabulary-member | symbol: part_time
- Needs: n18 (t4:s1)
- Searches tried:
  • "part-time" → no existing descriptive-value for part-time
- Meaning: indicates that the job is part-time rather than full-time.
- Contextual aliases: ["part_time_job","PT"]
- Proposed record:
  {"symbol":"part_time","kind":"value","category":"descriptive-value","definition":"Indicates that a job is part-time rather than full-time.","not":"A statement of schedule or hours per week","aliases":["part_time_job","PT"]}