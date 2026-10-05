### S1 | type: add | dimension: constructor | symbol: planning_request
- Needs: n3 (t1:s3)
- Searches tried: "categorize best methods for staying organized" → sequence, decision, rule_category_event_value; widen "plan and categorize methods" → nothing
- Typed parameters: task: TERM
- Interpretation: a request to plan and categorize methods for a described activity; describes the user's desire without asserting execution
- Example: `TERM planning_request(task=activity(verb="plan_and_categorize", object=subject(kind="story"))) -> planning_request_2 : TERM`
- Proposed record: {"symbol":"planning_request","kind":"constructor","signature":"TERM planning_request(task: TERM) -> TERM","definition":"Represents a request to plan and categorize methods for the given task without presuming execution.","not":"An executed plan or categorization; use activity or decision for those outcomes.","aliases":["planning and categorization request"]}

### S2 | type: add | dimension: constructor | symbol: organization_system
- Needs: n4 (t1:s3)
- Searches tried: "organization framework" → art_structured_report (artifact), format_structured_report; widen "organization system" → nothing
- Typed parameters: none
- Interpretation: denotes a structured system or framework for organization tasks; an abstract artifact description
- Example: `TERM organization_system() -> organization_system_2 : TERM`
- Proposed record: {"symbol":"organization_system","kind":"constructor","signature":"TERM organization_system() -> TERM","definition":"Describes a structured system or framework to organize a process or content.","not":"A physical system or runtime object; not an executed operation.","aliases":["organization framework","organization guide"]}