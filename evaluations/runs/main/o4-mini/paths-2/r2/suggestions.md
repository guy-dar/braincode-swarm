### S1 | type: add | dimension: constructor | symbol: reconcile_balance_sheet_accounts
- Needs: n1 (t1:s1), n2 (t1:s1)
- Searches tried: `rag search "reconcile accounts receivable"` → reconcile_code (for code); `rag widen "reconcile financial accounts"` → none
- Typed parameters: entities: LIST[TERM], system: STRING / ATOM[platform_label]
- Interpretation: Constructs a description of reconciling specified balance sheet accounts within a system. Entities list the balance sheet account types to reconcile; system identifies the system context. Does not assert an actual execution or completion.
- Example: `TERM reconcile_balance_sheet_accounts(entities=[subject(kind="accounts_receivable"), subject(kind="deferred_revenue")], system=platform_label::zuora) -> reconcile_balance_sheet_accounts_2 : TERM`
- Proposed record: `{ "symbol": "reconcile_balance_sheet_accounts", "kind": "constructor", "signature": "TERM reconcile_balance_sheet_accounts(entities: LIST[TERM], system: STRING / ATOM[platform_label]) -> TERM", "definition": "Description of reconciling specified balance sheet accounts within a system; does not assert execution.", "not": "An executed operation or code reconciliation (use ACTION for execution)", "aliases": ["reconcile accounts", "sync accounts"] }`

### S2 | type: add | dimension: constructor | symbol: explain_in_reporting
- Needs: n4 (t1:s2)
- Searches tried: `rag search "explain reporting"` → none; `rag widen "meaning in reporting"` → none
- Typed parameters: topic: TERM, system: STRING / ATOM[platform_label]
- Interpretation: Constructs a description of a request to explain a specified topic within a system’s reporting module. Does not assert the explanation itself.
- Example: `TERM explain_in_reporting(topic=subject(kind="balance_sheet_reconciliation"), system=platform_label::zuora) -> explain_in_reporting_2 : TERM`
- Proposed record: `{ "symbol": "explain_in_reporting", "kind": "constructor", "signature": "TERM explain_in_reporting(topic: TERM, system: STRING / ATOM[platform_label]) -> TERM", "definition": "Description of requesting an explanation of a topic within a system's reporting context.", "not": "The explanation content itself", "aliases": ["explain reporting", "define in reporting"] }`

### S3 | type: add | dimension: constructor | symbol: create_custom_report
- Needs: n14 (t3:s1), n15 (t3:s1)
- Searches tried: `rag search "create custom report"` → none; `rag widen "build report with columns"` → none
- Typed parameters: data_source: TERM, columns: LIST[TERM], system: STRING / ATOM[platform_label]
- Interpretation: Constructs a description of creating a custom report fetching specified columns from a data source within a system. Does not execute the report.
- Example: `TERM create_custom_report(data_source=subject(kind="usage and adjustment records"), columns=[subject(kind="date of usage"), subject(kind="invoice number")], system=platform_label::zuora) -> create_custom_report_2 : TERM`
- Proposed record: `{ "symbol": "create_custom_report", "kind": "constructor", "signature": "TERM create_custom_report(data_source: TERM, columns: LIST[TERM], system: STRING / ATOM[platform_label]) -> TERM", "definition": "Description of creating a custom report with specified columns from a data source in a system.", "not": "An executed report or runtime operation", "aliases": ["generate custom report"] }`

### S4 | type: add | dimension: constructor | symbol: schedule_recurring_report
- Needs: n25 (t4:s23)
- Searches tried: `rag search "schedule report"` → none; `rag widen "recurring report schedule"` → none
- Typed parameters: report: TERM, interval: TERM
- Interpretation: Constructs a description of scheduling a report to run at recurring intervals; report identifies the report to schedule; interval specifies the recurrence frequency. Does not assert execution.
- Example: `TERM schedule_recurring_report(report=create_custom_report_2, interval=duration(amount=1, unit=unit_week)) -> schedule_recurring_report_2 : TERM`
- Proposed record: `{ "symbol": "schedule_recurring_report", "kind": "constructor", "signature": "TERM schedule_recurring_report(report: TERM, interval: TERM) -> TERM", "definition": "Description of scheduling a report to run at recurring intervals; does not execute the scheduling.", "not": "An executed scheduling operation", "aliases": ["schedule report"] }`