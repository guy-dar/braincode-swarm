Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="reconciliation_project") -> project_goal : TERM
    UTTER ask(target=project_goal, topic="zuora_reporting")
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM activity(verb="reconcile", object=conjunction(items=[subject(kind="accounts_receivable"), subject(kind="deferred_revenue")])) -> reconciliation_activity : TERM
    CLAIM statement(fact=reconciliation_activity) BY agent STATUS asserted SOURCE "t2:s1, t2:s2" -> what_reconciliation_means : CLAIM
    TERM subject(kind="ar_aging_report") -> ar_aging_report : TERM
    CLAIM attribute_claim(subject=ar_aging_report, property="categorizes_unpaid_invoices", value="by_age") BY agent STATUS asserted SOURCE "t2:s5, t2:s6" -> ar_aging_characterization : CLAIM
    TERM subject(kind="deferred_revenue_schedule") -> deferred_revenue_schedule : TERM
    CLAIM attribute_claim(subject=deferred_revenue_schedule, property="provides_visibility", value="deferred_balances_and_recognition_entries") BY agent STATUS asserted SOURCE "t2:s9, t2:s10" -> deferred_revenue_characterization : CLAIM
    TERM subject(kind="revenue_reports") -> revenue_reports : TERM
    CLAIM attribute_claim(subject=revenue_reports, property="provides_insights", value="recognized_revenue") BY agent STATUS asserted SOURCE "t2:s12, t2:s13" -> revenue_reports_characterization : CLAIM
    TERM activity(verb="maintain_reconciliation", object=conjunction(items=[subject(kind="accounts_receivable"), subject(kind="deferred_revenue")]), period="ongoing") -> ongoing_reconciliation : TERM
    CLAIM ongoing(target=ongoing_reconciliation) BY agent STATUS asserted SOURCE "t2:s14, t2:s15" -> ongoing_reconciliation_need : CLAIM
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    TERM include(item=conjunction(items=[subject(kind="usage_data"), subject(kind="adjustments"), subject(kind="school"), subject(kind="date_usage_recorded"), subject(kind="date_billed"), subject(kind="invoice_number"), subject(kind="amount")])) -> requested_report_columns : TERM
    UTTER ask(target=requested_report_columns, topic="zuora_custom_report_creation")
  }
  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    CLAIM provides(actor=platform_label::zuora, subject=requested_report_columns) BY agent STATUS asserted SOURCE "t4:s1" -> zuora_custom_report_possible : CLAIM
    UTTER inform(target=zuora_custom_report_possible)
    TERM sequence(items=[
      activity(verb="login", object=platform_label::zuora),
      activity(verb="navigate", object=web_element(label="Reporting")),
      activity(verb="click", object=web_element(label="Reports")),
      activity(verb="click", object=web_element(label="Create New Report")),
      activity(verb="select_data_source", object=web_element(label="Invoice and Payment")),
      activity(verb="select_date_range"),
      activity(verb="add_report_columns", object=conjunction(items=[subject(kind="usage"), subject(kind="date_usage_recorded"), subject(kind="date_billed"), subject(kind="invoice_number"), subject(kind="amount")])),
      activity(verb="include_account_data", object=subject(kind="parent_hierarchy")),
      activity(verb="apply_filters_and_groupings"),
      activity(verb="execute_report", object=web_element(label="Run Report")),
      activity(verb="schedule_recurring", object=subject(kind="report_execution"))
    ]) -> create_custom_report_steps : TERM
    UTTER propose(target=create_custom_report_steps)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | activity(verb="reconcile") | covered |
| n2 | action | activity(verb="reconcile") | covered |
| n3 | temporal | ongoing_reconciliation, ongoing | covered |
| n4 | speech_act | ask, inform | covered |
| n5 | object | platform_label::zuora | covered |
| n6 | object | platform_label::zuora, web_element, provides | covered |
| n7 | claim | statement, ongoing | covered |
| n8 | object | ar_aging_report (subject) | covered |
| n9 | claim | ongoing | covered |
| n10 | object | deferred_revenue_schedule (subject) | covered |
| n11 | claim | ongoing | covered |
| n12 | object | revenue_reports (subject) | covered |
| n13 | claim | ongoing | covered |
| n14 | speech_act | ask, inform, propose, include | covered |
| n15 | object | include, subject | covered |
| n16 | object | subject(kind="school") | label-preserved |
| n17 | object | subject | covered |
| n18 | object | subject | covered |
| n19 | claim | provides, include | covered |
| n20 | action | include, sequence | covered |
| n21 | object | web_element(label="Invoice and Payment") | label-preserved |
| n22 | action | activity, sequence | covered |
| n23 | action | include | covered |
| n24 | action | include, sequence | covered |
| n25 | temporal | activity | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t4:s24 is represented and attributed to sources
- Opaque-text spans: none
- Label-preserved spans: n16 "school entity with parent hierarchy" (informal description as subject), n21 "Invoice and Payment data source" (UI label preserved in web_element)
- Missing constructs: none; domain-specific accounting concepts (Zuora reports, accounting data fields) are described through available constructors (subject, activity, attribute_claim, sequence, include, provide)
- Unresolved ambiguities: none
- Check result: no unknown symbols, all glossary symbols are valid, 2 open-group labels, all needs covered or appropriately label-preserved
```

Now let me run the final check:
<function_calls>
<invoke name="bash">
<parameter name="command">node /kit/rag.mjs check --translation /output/translation.md