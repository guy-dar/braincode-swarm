### S1 | type: add | dimension: constructor | symbol: account_reconciliation
- Needs: n1 (t1:s1), n2 (t1:s1)
- Searches tried: "reconcile accounts" → reconcile_code (operates on code entities, not domain accounts), "account reconciliation" → nothing
- Typed parameters: accounts: LIST[TERM]
- Interpretation: Descriptive TERM for reconciling the specified balance sheet accounts; it asserts nothing and does not execute a runtime operation.
- Example: `TERM account_reconciliation(accounts=[subject(kind="balance_sheet_account", qualifier="accounts_receivable"), subject(kind="balance_sheet_account", qualifier="deferred_revenue")]) -> account_reconciliation_2 : TERM`
- Proposed record: {"symbol":"account_reconciliation","kind":"constructor","signature":"TERM account_reconciliation(accounts: LIST[TERM]) -> TERM","definition":"Descriptive TERM for reconciling specified balance sheet accounts; asserts nothing.","not":"an executed runtime operation","aliases":["reconcile_accounts","account_reconciliation_activity"]}

### S2 | type: add | dimension: constructor | symbol: custom_report_request
- Needs: n19 (t3:s1), n20 (t4:s4), n21 (t4:s10), n22 (t4:s12), n23 (t4:s17), n24 (t4:s19)
- Searches tried: "create custom report" → format_structured_report (artifact type for GENERATE, not a TERM for request), "report request" → nothing
- Typed parameters: platform: STRING / ATOM[platform_label], data_source: STRING, columns: LIST[TERM]
- Interpretation: Descriptive TERM for requesting a custom report on a platform with a specific data source and list of column descriptors; asserts nothing.
- Example: `TERM custom_report_request(platform=platform_label::zuora, data_source="invoice_and_payment", columns=[subject(kind="school"), subject(kind="date", qualifier="usage_date"), subject(kind="invoice", qualifier="number")]) -> custom_report_request_2 : TERM`
- Proposed record: {"symbol":"custom_report_request","kind":"constructor","signature":"TERM custom_report_request(platform: STRING / ATOM[platform_label], data_source: STRING, columns: LIST[TERM]) -> TERM","definition":"Descriptive TERM for requesting a custom report on a specified platform, data source, and column list; asserts nothing.","not":"an executable operation or claim of execution","aliases":["request_custom_report","report_request"]}