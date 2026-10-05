Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="accounts_receivable_balance_sheet_account") -> subject_2 : TERM
    TERM subject(kind="deferred_revenue_balance_sheet_account") -> subject_3 : TERM
    TERM activity(verb="reconcile", object=subject_2) -> activity_2 : TERM
    TERM activity(verb="reconcile", object=subject_3) -> activity_3 : TERM
    TERM conjunction(items=[activity_2, activity_3]) -> conjunction_2 : TERM
    TERM temporal_context(activity=conjunction_2, period="ongoing") -> temporal_context_2 : TERM
    CLAIM request(target=temporal_context_2) BY role_user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
    TERM subject(kind="balance_sheet_reconciliation_meaning_in_reporting", qualifier=platform_label::zuora) -> subject_4 : TERM
    UTTER ask(target=subject_4)
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM subject(kind="financial_statements") -> subject_2 : TERM
    TERM subject(kind="accounts_receivable_and_deferred_revenue_balance_sheet_accounts", qualifier=platform_label::zuora) -> subject_3 : TERM
    TERM activity(verb="sync", object=subject_3, purpose=subject_2) -> activity_2 : TERM
    CLAIM statement(fact=activity_2) BY role_agent STATUS asserted SOURCE "t2:s1" -> statement_2 : CLAIM
    CLAIM involves(subject=statement_2, target=subject_2) BY role_agent STATUS asserted SOURCE "t2:s2" -> involves_2 : CLAIM
    TERM subject(kind="accounts_receivable_aging_report", qualifier=platform_label::zuora) -> subject_4 : TERM
    TERM subject(kind="unpaid_invoices_by_age") -> subject_5 : TERM
    TERM subject(kind="discrepancies") -> subject_6 : TERM
    TERM activity(verb="categorize", actor="accounts_receivable_aging_report", object=subject_5, purpose=subject_6) -> activity_3 : TERM
    CLAIM statement(fact=activity_3) BY role_agent STATUS asserted SOURCE "t2:s5" -> statement_3 : CLAIM
    TERM subject(kind="deferred_revenue_schedule_report", qualifier=platform_label::zuora) -> subject_7 : TERM
    TERM subject(kind="deferred_balances_and_recognition_entries") -> subject_8 : TERM
    TERM activity(verb="show", actor="deferred_revenue_schedule_report", object=subject_8, purpose=activity_2) -> activity_4 : TERM
    CLAIM statement(fact=activity_4) BY role_agent STATUS asserted SOURCE "t2:s9" -> statement_4 : CLAIM
    TERM subject(kind="revenue_reports", qualifier=platform_label::zuora) -> subject_9 : TERM
    TERM activity(verb="review_and_investigate", object=subject_6, purpose=subject_9) -> activity_5 : TERM
    TERM activity(verb="reconcile", object=subject_3) -> activity_6 : TERM
    TERM temporal_context(activity=activity_6, period="ongoing") -> temporal_context_2 : TERM
    CLAIM enables(condition=activity_5, outcome=temporal_context_2) BY role_agent STATUS asserted SOURCE "t2:s14" -> enables_2 : CLAIM
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    TERM subject(kind="custom_report", qualifier=platform_label::zuora) -> subject_2 : TERM
    TERM subject(kind="usage_data_and_adjustment_records") -> subject_3 : TERM
    TERM subject(kind="school_with_parent_hierarchy") -> subject_4 : TERM
    TERM subject(kind="date_of_usage_and_date_billed") -> subject_5 : TERM
    TERM subject(kind="invoice_number_and_amount") -> subject_6 : TERM
    TERM conjunction(items=[subject_3, subject_4, subject_5, subject_6]) -> conjunction_2 : TERM
    TERM include(item=conjunction_2) -> include_2 : TERM
    UTTER ask(target=subject_2, constraints=[include_2])
  }
  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    TERM subject(kind="custom_report", qualifier=platform_label::zuora) -> subject_2 : TERM
    TERM activity(verb="create", object=subject_2, instrument=platform_label::zuora) -> activity_2 : TERM
    CLAIM statement(fact=activity_2) BY role_agent STATUS asserted SOURCE "t4:s1" -> statement_2 : CLAIM
    UTTER inform(target=statement_2)
    TERM document_section(title="Reporting") -> document_section_2 : TERM
    TERM activity(verb="navigate", object=document_section_2) -> activity_3 : TERM
    TERM activity(verb="create_new", object=subject_2) -> activity_4 : TERM
    TERM subject(kind="invoice_and_payment_data_source", qualifier=platform_label::zuora) -> subject_3 : TERM
    TERM activity(verb="select", object=subject_3) -> activity_5 : TERM
    TERM subject(kind="reporting_date_range") -> subject_4 : TERM
    TERM activity(verb="select", object=subject_4) -> activity_6 : TERM
    TERM subject(kind="specified_data_columns") -> subject_5 : TERM
    TERM activity(verb="add", object=subject_5) -> activity_7 : TERM
    TERM subject(kind="account_data_source", qualifier=platform_label::zuora) -> subject_6 : TERM
    TERM include(item=subject_6) -> include_2 : TERM
    TERM activity(verb="retrieve", object="parent_hierarchy_fields", instrument=platform_label::zuora, purpose=include_2) -> activity_8 : TERM
    TERM subject(kind="filters") -> subject_7 : TERM
    TERM activity(verb="apply", object=subject_7) -> activity_9 : TERM
    TERM subject(kind="groupings") -> subject_8 : TERM
    TERM activity(verb="configure", object=subject_8) -> activity_10 : TERM
    TERM activity(verb="execute", object=subject_2) -> activity_11 : TERM
    TERM sequence(items=[activity_3, activity_4, activity_5, activity_6, activity_7, activity_8, activity_9, activity_10, activity_11]) -> sequence_2 : TERM
    UTTER propose(target=sequence_2)
    TERM activity(verb="schedule", object=subject_2) -> activity_12 : TERM
    TERM temporal_context(activity=activity_12, period="recurring_intervals") -> temporal_context_2 : TERM
    UTTER propose(target=temporal_context_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | activity, subject | covered |
| n2 | action | activity, subject | covered |
| n3 | temporal | temporal_context | covered |
| n4 | speech_act | ask, subject | covered |
| n5 | object | platform_label::zuora | label-preserved |
| n6 | object | subject | covered |
| n7 | claim | statement, involves, activity | covered |
| n8 | object | subject | covered |
| n9 | claim | statement, activity | covered |
| n10 | object | subject | covered |
| n11 | claim | statement, activity | covered |
| n12 | object | subject | covered |
| n13 | claim | enables, temporal_context | covered |
| n14 | speech_act | ask, include | covered |
| n15 | object | subject | covered |
| n16 | object | subject | covered |
| n17 | object | subject | covered |
| n18 | object | subject | covered |
| n19 | claim | statement, inform | covered |
| n20 | action | document_section, activity, sequence, propose | covered |
| n21 | object | subject | covered |
| n22 | action | activity, sequence | covered |
| n23 | action | include, activity | covered |
| n24 | action | activity, sequence | covered |
| n25 | temporal | activity, temporal_context | covered |

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: t1:s1–t4:s23 represented; t2:s3–s4, t2:s6, s10, s12–s13, t4:s22, s24 only partly/not encoded (t2:s6 comparison, s13 matching revenue, t4:s22 customization, s24 caveat)
- Opaque-text spans: none
- Label-preserved spans: t1:s2 "zuora" → platform_label::zuora (label only)
- Missing constructs: no dedicated reconcile (non-code) constructor, so activity(verb="reconcile") used; role_user assumed
- Unresolved ambiguities: "it" in t1:s2 taken as the reconciliation project
- Check: see host check
