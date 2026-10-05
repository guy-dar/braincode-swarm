### S1 | type: add | dimension: constructor | symbol: classify
- Needs: n3 (t1:s3)
- Searches tried: "categorize methods" → no matching constructor; widen "classify" → nothing suitable
- Typed parameters: item: TERM, criterion: STRING
- Interpretation: A classification descriptor that organizes the described item according to the given criterion; asserts nothing.
- Example: `TERM classify(item=subject(kind="methods_for_organization"), criterion="best") -> classify_2 : TERM`
- Proposed record: {"symbol":"classify","kind":"constructor","signature":"TERM classify(item: TERM, criterion: STRING) -> TERM","definition":"A classification descriptor organizing the described item by the given criterion; asserts nothing.","not":"An executed or asserted classification","aliases":["categorize","sort_into_categories"]}

### S2 | type: add | dimension: constructor | symbol: organization_framework
- Needs: n4 (t1:s3)
- Searches tried: "organization framework" → subject (too generic); widen "framework" → no framework constructor
- Typed parameters: focus: TERM
- Interpretation: A descriptive scaffold outlining how to organize the given focus; asserts nothing.
- Example: `TERM organization_framework(focus=subject(kind="organization_during_story_writing")) -> organization_framework_2 : TERM`
- Proposed record: {"symbol":"organization_framework","kind":"constructor","signature":"TERM organization_framework(focus: TERM) -> TERM","definition":"A descriptive scaffold outlining how to organize the given focus; asserts nothing.","not":"A completed plan artifact","aliases":["planning_framework","structure_template"]}