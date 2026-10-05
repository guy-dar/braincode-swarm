Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(verb="reconcile", object="accounts receivable balance sheet accounts") -> activity_ar : TERM   # PROPOSED: S1
    TERM activity(verb="reconcile", object="deferred revenue balance sheet accounts") -> activity_dr : TERM      # PROPOSED: S1
    TERM conjunction(items=[activity_ar, activity_dr]) -> reconcile_objectives : TERM
    UTTER ask(target=reconcile_objectives, topic=subject(kind="meaning", qualifier=platform_label::zuora))
  }
  TURN t2 SPEAKER=AGENT {
    CLAIM statement(fact=subject(kind="reconciliation", qualifier="financial accounts", location=platform_label::zuora)) BY role_agent STATUS asserted SOURCE "t2:s1" -> reconciliation_context : CLAIM
    CLAIM involves(subject=reconciliation_context, target=activity(verb="sync", object="AR and deferred revenue balances with financial statements")) BY role_agent STATUS asserted SOURCE "t2:s2" -> sync_claim : CLAIM
    TERM subject(kind="Accounts Receivable Aging Report", qualifier=platform_label::zuora) -> ar_aging_report : TERM
    CLAIM statement(fact=ar_aging_report) BY role_agent STATUS asserted SOURCE "t2:s5" -> ar_report_claim : CLAIM
    CLAIM statement(fact=activity(verb="categorize", object="unpaid invoices", purpose=subject(kind="discrepancy detection"))) BY role_agent STATUS asserted SOURCE "t2:s5,t2:s6" -> ar_functionality : CLAIM
    TERM subject(kind="Deferred Revenue Schedule report", qualifier=platform_label::zuora) -> dr_schedule_report : TERM
    CLAIM statement(fact=dr_schedule_report) BY role_agent STATUS asserted SOURCE "t2:s8,t2:s9" -> dr_report_claim : CLAIM
    CLAIM statement(fact=activity(verb="show", object="deferred revenue balances and recognition entries")) BY role_agent STATUS asserted SOURCE "t2:s9" -> dr_functionality : CLAIM
    TERM subject(kind="Revenue Reports", qualifier=platform_label::zuora) -> revenue_reports : TERM
    CLAIM statement(fact=revenue_reports) BY role_agent STATUS asserted SOURCE "t2:s12" -> revenue_reports_claim : CLAIM
    CLAIM ongoing(target=activity(verb="review", object="reports", location=platform_label::zuora, purpose=subject(kind="reconciliation"))) BY role_agent STATUS asserted SOURCE "t2:s14" -> ongoing_review : CLAIM
  }
  TURN t3 SPEAKER=USER {
    TERM include(item="usage data") -> usage_item : TERM
    TERM include(item="adjustment records") -> adjustment_item : TERM
    TERM include(item=subject(kind="school", qualifier="with parent hierarchy")) -> school_item : TERM
    TERM include(item=subject(kind="date of usage")) -> date_usage_item : TERM
    TERM include(item=subject(kind="date billed")) -> date_billed_item : TERM
    TERM include(item=subject(kind="invoice number")) -> inv_number_item : TERM
    TERM include(item=subject(kind="amount")) -> amount_item : TERM
    TERM conjunction(items=[usage_item, adjustment_item, school_item, date_usage_item, date_billed_item, inv_number_item, amount_item]) -> requested_columns : TERM
    UTTER ask(target=requested_columns, topic="custom report creation in Zuora")
  }
  TURN t4 SPEAKER=AGENT {
    CLAIM statement(fact=activity(verb="create", object="custom report", location=platform_label::zuora, purpose=subject(kind="fetching requested columns"))) BY role_agent STATUS asserted SOURCE "t4:s1" -> create_report_claim : CLAIM
    TERM activity(verb="login", object="Zuora tenant") -> login_activity : TERM
    TERM activity(verb="navigate", object="Reporting tab") -> navigate_reporting : TERM
    TERM sequence(items=[login_activity, navigate_reporting]) -> step_1_2 : TERM
    TERM activity(verb="click", object="Create New Report button") -> click_create : TERM
    TERM subject(kind="Invoice and Payment data source", qualifier=platform_label::zuora) -> invoice_payment_source : TERM
    TERM activity(verb="select", object=invoice_payment_source) -> select_data_source : TERM
    TERM activity(verb="select", object="date range") -> select_date_range : TERM
    TERM sequence(items=[click_create, select_data_source, select_date_range]) -> step_3_5 : TERM
    TERM activity(verb="add", object="school, date of usage, date billed, invoice number, and amount columns") -> add_columns : TERM
    TERM activity(verb="select", object="columns", purpose=subject(kind="include requested fields")) -> column_selection : TERM
    TERM sequence(items=[add_columns, column_selection]) -> step_6 : TERM
    TERM subject(kind="Account data source", qualifier=platform_label::zuora) -> account_source : TERM
    TERM activity(verb="include", object=account_source, purpose=subject(kind="parent hierarchy retrieval")) -> include_account_source : TERM
    TERM activity(verb="apply", object="filters and groupings") -> apply_filters_groupings : TERM
    TERM activity(verb="execute", object="report") -> execute_report : TERM
    TERM sequence(items=[execute_report]) -> final_run : TERM
    CLAIM statement(fact=activity(verb="customize", object="report layout, formatting, export options")) BY role_agent STATUS asserted SOURCE "t4:s22" -> customization_capability : CLAIM
    TERM activity(verb="save", object="report") -> save_report : TERM
    TERM activity(verb="schedule", object="report", purpose=subject(kind="recurring execution at regular intervals")) -> schedule_report : TERM
    CLAIM statement(fact=activity(verb="ensure", object="column availability", purpose=subject(kind="dependent on Zuora configuration"))) BY role_agent STATUS asserted SOURCE "t4:s24" -> config_dependency : CLAIM
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | activity(verb="reconcile", object="accounts receivable...") | proposed |
| n2 | action | activity(verb="reconcile", object="deferred revenue...") | proposed |
| n3 | temporal | ongoing | covered |
| n4 | speech_act | ask | covered |
| n5 | object | platform_label::zuora | covered |
| n6 | object | subject(...platform) | label-preserved |
| n7 | claim | statement, involves | covered |
| n8 | object | subject(...AR Aging Report) | label-preserved |
| n9 | claim | statement(...categorize) | label-preserved |
| n10 | object | subject(...Deferred Revenue Schedule) | label-preserved |
| n11 | claim | statement(...show balances) | label-preserved |
| n12 | object | subject(...Revenue Reports) | label-preserved |
| n13 | claim | ongoing | covered |
| n14 | speech_act | ask, include | covered |
| n15 | object | include | label-preserved |
| n16 | object | subject(...school) | label-preserved |
| n17 | object | subject(...date) | label-preserved |
| n18 | object | subject(...invoice, amount) | label-preserved |
| n19 | claim | statement | covered |
| n20 | action | activity | label-preserved |
| n21 | object | subject(...data source) | label-preserved |
| n22 | action | activity | label-preserved |
| n23 | action | include | covered |
| n24 | action | activity | label-preserved |
| n25 | temporal | activity(verb="schedule") | label-preserved |

## Why the translation failed

- n1, n2: "reconcile accounts receivable balance sheet accounts" and "reconcile deferred revenue balance sheet accounts" — search `reconcile_code` → matches code entity reconciliation only; widen "financial reconciliation" → no glossary entry for financial account reconciliation. The `reconcile_code` constructor is specifically for reconciling code implementations (`reconcile_code(entities: LIST[TERM], objective: STRING / TERM)`), not financial accounts. Proposed S1: a new relation for financial account reconciliation.

Multiple label-preserved needs (n6, n8-n12, n15-n18, n20-n22, n24-n25) are represented using activity() and subject() TERM descriptors that preserve the source labels (report names, data field names, UI steps) without losing semantic content. These are acceptable in TRACE mode where descriptive vocabulary is the goal.

## Translation report

- Input kind: conversation (TRACE)
- Coverage status: partial (needs S1 to complete)
- Source-span coverage: every segment t1:s1–t4:s24 is represented
- Opaque-text spans: none
- Label-preserved spans: n6, n8-n12, n15-n18, n20-n22, n24-n25 — report/data field names, UI element names and UI steps preserved from source using subject() and activity() descriptors
- Missing constructs: S1 — financial account reconciliation relation (source uses "reconcile" for Zuora financial accounts, distinct from code reconciliation)
- Unresolved ambiguities: none
- Searches tried: `reconcile_code` (code entities only), widen "financial reconciliation" (no results), widen "balance sheet sync" (no specific results)

