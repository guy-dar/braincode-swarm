Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM reconcile_code(entities=[subject(kind="accounts_receivable"), subject(kind="deferred_revenue")], objective="financial_reconciliation") -> reconcile_code_2 : TERM
    CLAIM ongoing(target=reconcile_code_2) BY "user" STATUS asserted SOURCE "t1:s1" -> ongoing_2 : CLAIM
    TERM subject(kind="reconciliation", qualifier=platform_label::zuora, location="reporting") -> zuora_reconciliation : TERM
    UTTER ask(target=zuora_reconciliation)
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    CLAIM involves(subject=t1.ongoing_2, target=subject(kind="sync", qualifier="financial_statements")) BY "agent" STATUS asserted SOURCE "t2:s1" -> involves_2 : CLAIM
    TERM subject(kind="accounts_receivable_aging_report", qualifier=platform_label::zuora) -> ar_aging_report : TERM
    TERM subject(kind="deferred_revenue_schedule", qualifier=platform_label::zuora) -> deferred_revenue_schedule : TERM
    TERM subject(kind="revenue_reports", qualifier=platform_label::zuora) -> revenue_reports : TERM
    CLAIM statement(fact=ar_aging_report) BY "agent" STATUS asserted SOURCE "t2:s5" -> ar_aging_statement : CLAIM
    CLAIM statement(fact=subject(kind="categorization", object="invoices", property="age")) BY "agent" STATUS asserted SOURCE "t2:s5" -> categorization_claim : CLAIM
    CLAIM leads_to(cause=subject(kind="comparison", object="reports", property="financial_records"), effect=subject(kind="identification", object="discrepancies")) BY "agent" STATUS asserted SOURCE "t2:s6" -> comparison_leads : CLAIM
    CLAIM statement(fact=deferred_revenue_schedule) BY "agent" STATUS asserted SOURCE "t2:s8" -> deferred_statement : CLAIM
    CLAIM statement(fact=subject(kind="visibility", object="deferred_revenue_balances")) BY "agent" STATUS asserted SOURCE "t2:s9" -> visibility_claim : CLAIM
    CLAIM enables(condition=deferred_revenue_schedule, outcome=subject(kind="reconciliation", object="deferred_revenue")) BY "agent" STATUS asserted SOURCE "t2:s10" -> enables_deferred : CLAIM
    CLAIM statement(fact=revenue_reports) BY "agent" STATUS asserted SOURCE "t2:s12" -> revenue_statement : CLAIM
    CLAIM enables(condition=subject(kind="review", property="regular"), outcome=subject(kind="maintenance", object="reconciliation")) BY "agent" STATUS asserted SOURCE "t2:s14" -> enables_review : CLAIM
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    TERM document_section(title="report_columns", items=[subject(kind="usage_data"), subject(kind="adjustment_records"), subject(kind="school", qualifier="parent_hierarchy"), subject(kind="date_of_usage"), subject(kind="date_billed"), subject(kind="invoice_number"), subject(kind="amount")]) -> report_spec : TERM
    UTTER ask(target=subject(kind="custom_report", qualifier=platform_label::zuora, property="can_be_created"))
  }
  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    CLAIM statement(fact=subject(kind="custom_report", qualifier=platform_label::zuora, property="can_be_created")) BY "agent" STATUS asserted SOURCE "t4:s1" -> custom_report_possible : CLAIM
    TERM activity(verb="navigate", instrument=platform_label::zuora) -> navigate_zuora : TERM
    TERM activity(verb="select", object="reporting_tab") -> select_reporting : TERM
    TERM activity(verb="select", object="Reports_menu") -> select_reports : TERM
    TERM activity(verb="create", object="new_report") -> create_report : TERM
    TERM include(item=subject(kind="data_source", qualifier="Invoice_and_Payment")) -> include_data_source : TERM
    TERM time_point(date="specified_range") -> date_range_specification : TERM
    TERM activity(verb="add", object="column_school") -> add_school : TERM
    TERM activity(verb="add", object="column_usage_date") -> add_usage_date : TERM
    TERM activity(verb="add", object="column_billed_date") -> add_billed_date : TERM
    TERM activity(verb="add", object="column_invoice_number") -> add_invoice : TERM
    TERM activity(verb="add", object="column_amount") -> add_amount : TERM
    TERM include(item=subject(kind="data_source", qualifier="Account", property="parent_hierarchy")) -> include_account : TERM
    TERM activity(verb="apply", object="filters") -> apply_filters : TERM
    TERM activity(verb="apply", object="groupings") -> apply_groupings : TERM
    TERM activity(verb="execute", object="report") -> execute_report : TERM
    TERM duration(amount=1, unit="recurring") -> recurring_schedule : TERM
    CLAIM statement(fact=subject(kind="report_scheduling", property="recurring")) BY "agent" STATUS asserted SOURCE "t4:s23" -> schedule_claim : CLAIM
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | reconcile_code | covered |
| n2 | action | reconcile_code | covered |
| n3 | temporal | ongoing | covered |
| n4 | speech_act | ask | covered |
| n5 | object | platform_label::zuora | label-preserved |
| n6 | object | subject, include | covered |
| n7 | claim | involves, statement, leads_to, enables, ongoing | covered |
| n8 | object | ar_aging_report | covered |
| n9 | claim | categorization_claim, comparison_leads, leads_to, enables | covered |
| n10 | object | deferred_revenue_schedule | covered |
| n11 | claim | visibility_claim, enables_deferred, leads_to | covered |
| n12 | object | revenue_reports | covered |
| n13 | claim | enables_review, enables, leads_to, ongoing | covered |
| n14 | speech_act | ask, document_section, include | covered |
| n15 | object | report_spec, document_section | covered |
| n16 | object | report_spec, document_section | covered |
| n17 | object | time_point, report_spec, document_section | covered |
| n18 | object | report_spec, document_section | covered |
| n19 | claim | custom_report_possible, statement | covered |
| n20 | action | navigate_zuora, select_reporting, select_reports, create_report, activity | covered |
| n21 | object | include_data_source | covered |
| n22 | action | add_school, add_usage_date, add_billed_date, add_invoice, add_amount, time_point, date_range_specification, activity | covered |
| n23 | action | include_account, include, activity | covered |
| n24 | action | apply_filters, apply_groupings, activity | covered |
| n25 | temporal | recurring_schedule, duration, schedule_claim | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: All segments t1:s1–t4:s23 represented through speech acts, claims, and descriptive TERMs (activity, subject, include, document_section, duration, time_point)
- Opaque-text spans: none
- Label-preserved spans: n5 — Zuora subscription management platform (preserved as platform_label::zuora; no additional semantic meaning required)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: Translation validates against current glossary
```
