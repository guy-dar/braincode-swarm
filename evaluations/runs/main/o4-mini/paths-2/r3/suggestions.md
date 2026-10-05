### S1 | type: add | dimension: constructor | symbol: definition
- Needs: n4 (t2:s1)
- Searches tried: "definition of" → none suitable
- Typed parameters: concept: TERM, context?: TERM
- Definition: Structured representation of the meaning or definition of a concept within an optional context.
- not: an executed operation or a claim evaluation
- aliases: ["meaning","explanation"]
- Proposed record:
  {"symbol":"definition","kind":"constructor","signature":"TERM definition(concept: TERM, context?: TERM) -> TERM","definition":"Structured representation of the meaning or definition of a concept within an optional context.","not":"an executed operation or a claim evaluation","aliases":["meaning","explanation"]}

### S2 | type: add | dimension: vocabulary-member | symbol: click_button
- Needs: n20 (t4:s4)
- Searches tried: "click button" → none, "press button" → none
- Signature: (target: REF[STRING], label: STRING) -> void
- Definition: Click a button or clickable UI element identified by its label.
- not: typing or selecting a dropdown
- aliases: ["press_button","tap_button"]
- Proposed record:
  {"symbol":"click_button","kind":"operation","signature":"(target:REF[STRING],label:STRING)->void","definition":"Click a button or clickable UI element identified by its label.","not":"typing or selecting a dropdown","aliases":["press_button","tap_button"]}

### S3 | type: add | dimension: vocabulary-member | symbol: select_column
- Needs: n22 (t4:s14)
- Searches tried: "add column" → none, "report column" → no operation
- Signature: (target: REF[STRING], column: STRING) -> void
- Definition: Add a column to an existing report configuration UI.
- not: executing or scheduling the report
- aliases: ["add_column","add_report_column"]
- Proposed record:
  {"symbol":"select_column","kind":"operation","signature":"(target:REF[STRING],column:STRING)->void","definition":"Add a column to an existing report configuration UI.","not":"executing or scheduling the report","aliases":["add_column","add_report_column"]}

### S4 | type: add | dimension: vocabulary-member | symbol: run_report
- Needs: n24 (t4:s21)
- Searches tried: "run report" → none, "execute report" → no operation
- Signature: (target: REF[STRING]) -> void
- Definition: Execute the currently configured report and display its results.
- not: scheduling or saving
- aliases: ["execute_report"]
- Proposed record:
  {"symbol":"run_report","kind":"operation","signature":"(target:REF[STRING])->void","definition":"Execute the currently configured report and display its results.","not":"scheduling or saving","aliases":["execute_report"]}

### S5 | type: add | dimension: vocabulary-member | symbol: schedule_report
- Needs: n25 (t4:s23)
- Searches tried: "schedule report" → none
- Signature: (target: REF[STRING], interval: STRING) -> void
- Definition: Schedule a report to run at recurring intervals.
- not: immediate execution
- aliases: ["set_report_schedule"]
- Proposed record:
  {"symbol":"schedule_report","kind":"operation","signature":"(target:REF[STRING],interval:STRING)->void","definition":"Schedule a report to run at recurring intervals.","not":"immediate execution","aliases":["set_report_schedule"]}

### S6 | type: add | dimension: constructor | symbol: report_request
- Needs: n14 (t3:s1)
- Searches tried: "report request constructor" → nothing
- Typed parameters: fields: LIST[STRING], filters?: LIST[TERM], data_source: STRING
- Definition: A structured request to create a report retrieving specified fields from a data source.
- not: execution of the report
- aliases: ["custom_report_request"]
- Proposed record:
  {"symbol":"report_request","kind":"constructor","signature":"TERM report_request(fields:LIST[STRING],filters?:LIST[TERM],data_source:STRING)->TERM","definition":"A structured request to create a report retrieving specified fields from a data source.","not":"execution of the report","aliases":["custom_report_request"]}