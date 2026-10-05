Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM reconcile_code(entities=[subject(kind="accounts_receivable"), subject(kind="deferred_revenue")], objective="keep_reconciled") -> reconciliation_project : TERM
    UTTER ask(target=reconciliation_project)
  }
  
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    CLAIM statement(fact=subject(kind="reconciliation", qualifier=platform_label::zuora)) BY role_agent STATUS asserted SOURCE "t2:s1" -> reconciliation_meaning : CLAIM
    CLAIM involves(subject=reconciliation_meaning, target=reconcile_code(entities=[subject(kind="accounts_receivable"), subject(kind="deferred_revenue")], objective="sync_with_financial_statements")) BY role_agent STATUS asserted SOURCE "t2:s1,t2:s2" -> reconciliation_process : CLAIM
    
    TERM requirement(property="report_type", value=format_structured_report) -> ar_aging_report : TERM
    CLAIM statement(fact=requirement(property="purpose", value="categorize_unpaid_invoices_by_age")) BY role_agent STATUS asserted SOURCE "t2:s5,t2:s6" -> ar_aging_purpose : CLAIM
    
    TERM requirement(property="report_type", value=format_structured_report) -> deferred_revenue_report : TERM
    CLAIM statement(fact=requirement(property="visibility", value="deferred_balances_and_recognition_entries")) BY role_agent STATUS asserted SOURCE "t2:s8,t2:s9,t2:s10" -> deferred_revenue_content : CLAIM
    
    TERM requirement(property="report_type", value=format_structured_report) -> revenue_reports : TERM
    CLAIM statement(fact=requirement(property="purpose", value="match_revenue_recognition")) BY role_agent STATUS asserted SOURCE "t2:s12,t2:s13" -> revenue_purpose : CLAIM
    
    CLAIM ongoing(target=reconcile_code(entities=[subject(kind="accounts_receivable"), subject(kind="deferred_revenue")], objective="maintain_accuracy")) BY role_agent STATUS asserted SOURCE "t2:s14" -> ongoing_reconciliation : CLAIM
    CLAIM statement(fact=requirement(property="frequency", value="regular_review_and_prompt_investigation")) BY role_agent STATUS asserted SOURCE "t2:s14,t2:s15" -> reconciliation_maintenance : CLAIM
  }
  
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    TERM requirement(property="usage", value=TRUE) -> need_usage : TERM
    TERM requirement(property="adjustments", value=TRUE) -> need_adjustments : TERM
    TERM requirement(property="school", value=TRUE) -> need_school : TERM
    TERM requirement(property="parent_hierarchy", value=TRUE) -> need_parent : TERM
    TERM requirement(property="date_of_usage", value=TRUE) -> need_usage_date : TERM
    TERM requirement(property="date_billed", value=TRUE) -> need_billed_date : TERM
    TERM requirement(property="invoice_number", value=TRUE) -> need_invoice : TERM
    TERM requirement(property="amount", value=TRUE) -> need_amount : TERM
    UTTER ask(topic="custom report with specified columns")
  }
  
  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    CLAIM statement(fact=requirement(property="capability", value="create_custom_report")) BY role_agent STATUS asserted SOURCE "t4:s1" -> custom_report_possible : CLAIM
    
    TERM activity(verb="navigate", actor="user", object="reporting_tab") -> navigate_reporting : TERM
    UTTER propose(target=navigate_reporting)
    
    TERM activity(verb="select", actor="user", object="reports_section") -> select_reports : TERM
    UTTER propose(target=select_reports)
    
    TERM activity(verb="click", actor="user", object="create_new_report_button") -> create_report : TERM
    UTTER propose(target=create_report)
    
    TERM subject(kind="data_source", qualifier=platform_label::zuora) -> zuora_data_source : TERM
    TERM requirement(property="data_source", value="invoice_and_payment") -> invoice_payment_source : TERM
    TERM activity(verb="select", actor="user", object=invoice_payment_source) -> select_invoice_source : TERM
    UTTER propose(target=select_invoice_source)
    
    TERM time_point(date="range_selection") -> date_range : TERM
    TERM activity(verb="select", actor="user", object=date_range) -> select_date_range : TERM
    UTTER propose(target=select_date_range)
    
    TERM requirement(property="columns", value="usage") -> usage_column : TERM
    TERM requirement(property="columns", value="adjustments") -> adjustments_column : TERM
    TERM requirement(property="columns", value="school") -> school_column : TERM
    TERM requirement(property="columns", value="parent_hierarchy") -> parent_column : TERM
    TERM requirement(property="columns", value="date_of_usage") -> usage_date_column : TERM
    TERM requirement(property="columns", value="date_billed") -> billed_date_column : TERM
    TERM requirement(property="columns", value="invoice_number") -> invoice_column : TERM
    TERM requirement(property="columns", value="amount") -> amount_column : TERM
    TERM activity(verb="add_columns", actor="user", object=[usage_column, adjustments_column, school_column, parent_column, usage_date_column, billed_date_column, invoice_column, amount_column]) -> add_columns : TERM
    UTTER propose(target=add_columns)
    
    TERM subject(kind="data_source", qualifier="account") -> account_source : TERM
    TERM include(item=account_source) -> include_account_source : TERM
    TERM activity(verb="include", actor="user", object=account_source, purpose=include_account_source) -> include_account_action : TERM
    UTTER propose(target=include_account_action)
    
    TERM activity(verb="specify", actor="user", object="filters_and_groupings") -> configure_settings : TERM
    UTTER propose(target=configure_settings)
    
    TERM activity(verb="execute", actor="user", object="report") -> execute_report : TERM
    UTTER propose(target=execute_report)
    
    CLAIM statement(fact=requirement(property="save_and_schedule", value="recurring_intervals")) BY role_agent STATUS asserted SOURCE "t4:s23" -> schedule_capability : CLAIM
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
| n5 | object | platform_label::zuora | covered |
| n6 | object | requirement with format_structured_report | covered |
| n7 | claim | involves, statement, reconcile_code | covered |
| n8 | object | requirement with format_structured_report for AR Aging | covered |
| n9 | claim | statement with requirement for categorization | covered |
| n10 | object | requirement with format_structured_report for Deferred Revenue | covered |
| n11 | claim | statement with requirement for visibility | covered |
| n12 | object | requirement with format_structured_report for Revenue Reports | covered |
| n13 | claim | ongoing, statement with requirement for frequency | covered |
| n14 | speech_act | ask | covered |
| n15 | object | requirement for usage and adjustments columns | covered |
| n16 | object | subject and activity for school/parent hierarchy | covered |
| n17 | object | time_point for date range; requirement for usage_date, billed_date | covered |
| n18 | object | requirement for invoice_number and amount columns | covered |
| n19 | claim | statement with requirement | covered |
| n20 | action | activity(verb="navigate"), activity(verb="select"), activity(verb="click") | covered |
| n21 | object | requirement with invoice_and_payment value | covered |
| n22 | action | activity(verb="select") for date range, activity(verb="add_columns") | covered |
| n23 | action | activity(verb="include") with account_source and parent_hierarchy | covered |
| n24 | action | activity(verb="specify"), activity(verb="execute") | covered |
| n25 | temporal | requirement with recurring_intervals value | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: all turns t1–t4 and all primary sentences are represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: all needs fully covered with glossary symbols
