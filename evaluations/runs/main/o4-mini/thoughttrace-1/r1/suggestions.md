### S1 | type: add | dimension: constructor | symbol: story_planning_guide
- Needs: n4 (t1:s3), n8 (t2:s1, t2:s4)
- Searches tried:
  • "organisation guide for fanfiction" → format_structured_report (format), document_section (section constructor)
  • widen "structured guide with named sections" → no matching term
- Typed parameters: sections: LIST[TERM]
- Interpretation: A structured planning guide for a story, composed of named sections each containing items; it asserts nothing about execution.
- Example: `TERM story_planning_guide(sections=[document_section(title="Sections", items=[include(item="…")])]) -> story_planning_guide_2 : TERM`
- not: format_structured_report (artifact format), document_section (only a single section)
- aliases: organization_guide, planning_guide
- Proposed record:
  `{"symbol":"story_planning_guide","kind":"constructor","signature":"TERM story_planning_guide(sections: LIST[TERM]) -> TERM","definition":"A structured planning guide for a story, composed of named sections each containing items; asserts nothing about execution.","not":"format_structured_report","aliases":["organization_guide","planning_guide"]}`
