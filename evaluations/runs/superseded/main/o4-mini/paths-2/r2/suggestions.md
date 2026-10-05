### S1 | type: add | dimension: constructor | symbol: account_reconciliation
- Needs: n1 (t1:s1), n2 (t1:s1)
- Searches tried: "reconcile accounts receivable" → no non-code reconcile constructor; reconcile_code is for code only; widen "reconcile accounts deferred revenue balance sheet" → nothing applicable.
- Typed parameters: accounts: LIST[STRING], system: STRING
- Interpretation: a descriptive term for the action of reconciling the listed balance sheet account names in the specified system; asserts nothing and does not execute it.
- Example: `TERM account_reconciliation(accounts=["accounts_receivable", "deferred_revenue"], system=platform_label::zuora) -> account_reconciliation_2 : TERM`
- Proposed record: {"symbol":"account_reconciliation","kind":"constructor","signature":"TERM account_reconciliation(accounts: LIST[STRING], system: STRING) -> TERM","definition":"Descriptive term for the reconciliation of the specified balance sheet account names within the given system.","not":"an executable operation or code merge (use ACTION pick_up/place for physical objects)","aliases":["reconcile_accounts","balance_sheet_reconciliation"]}

### S2 | type: add | dimension: constructor | symbol: property_question
- Needs: n4 (t1:s2)
- Searches tried: "what does X mean" → no matching question constructor; widen "meaning question" → nothing.
- Typed parameters: subject: TERM, property: STRING
- Interpretation: constructs a question term asking for the named property of the provided subject; presupposes no answer.
- Example: `TERM property_question(subject=account_reconciliation_2, property="meaning in reporting") -> property_question_2 : TERM`
- Proposed record: {"symbol":"property_question","kind":"constructor","signature":"TERM property_question(subject: TERM, property: STRING) -> TERM","definition":"A question term requesting the value or definition of the specified property for the given subject.","not":"a statement or explanation (use CLAIM statement for assertions)","aliases":["meaning_question","ask_meaning"]}

### S3 | type: add | dimension: constructor | symbol: report_request
- Needs: n14 (t3:s1)
- Searches tried: "create report" → no generic report request constructor; widen "report fetch request" → nothing.
- Typed parameters: columns: LIST[STRING], system: STRING, section: STRING
- Interpretation: descriptive term representing a request to generate or fetch a report with specified columns from the given system and section; asserts nothing.
- Example: `TERM report_request(columns=["usage","adjustments","school","parent","date_of_usage","date_billed","invoice_number","amount"], system=platform_label::zuora, section="reporting") -> report_request_2 : TERM`
- Proposed record: {"symbol":"report_request","kind":"constructor","signature":"TERM report_request(columns: LIST[STRING], system: STRING, section: STRING) -> TERM","definition":"Descriptive term for requesting a report with the listed columns from the specified system and UI section.","not":"an executed GENERATE operation or external action","aliases":["custom_report_request","fetch_report"]}