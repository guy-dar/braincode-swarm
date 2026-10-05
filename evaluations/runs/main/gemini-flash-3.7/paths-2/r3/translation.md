Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(instrument=platform_label::zuora, object="accounts_receivable", verb="reconcile") -> activity_2 : TERM
    TERM activity(instrument=platform_label::zuora, object="deferred_revenue", verb="reconcile") -> activity_3 : TERM
    CLAIM ongoing(target=activity_2) BY role_user STATUS asserted SOURCE "t1:s1" -> ongoing_2 : CLAIM
    CLAIM ongoing(target=activity_3) BY role_user STATUS asserted SOURCE "t1:s1" -> ongoing_3 : CLAIM
    TERM subject(kind="reporting", qualifier=platform_label::zuora) -> subject_2 : TERM
    TERM subject(kind="balance_sheet_reconciliation", qualifier=subject_2) -> subject_3 : TERM
    UTTER ask(target=subject_3)
  }
  TURN t2 SPEAKER=AGENT {
    TERM subject(kind="financial_statements") -> subject_4 : TERM
    TERM activity(instrument=platform_label::zuora, object="accounts_receivable_and_deferred_revenue", purpose=subject_4, verb="sync") -> activity_4 : TERM
    CLAIM statement(fact=activity_4) BY role_agent STATUS asserted SOURCE "t2:s1" -> statement_2 : CLAIM
    CLAIM involves(target=subject_4, subject=statement_2) BY role_agent STATUS asserted SOURCE "t2:s2" -> involves_2 : CLAIM
    TERM document_section(title="accounts_receivable_aging_report") -> document_section_2 : TERM
    TERM subject(kind="unpaid_invoices_by_age", qualifier=document_section_2) -> subject_5 : TERM
    TERM activity(object="discrepancies", verb="identify") -> activity_5 : TERM
    CLAIM enables(condition=subject_5, outcome=activity_5) BY role_agent STATUS asserted SOURCE "t2:s5" -> enables_2 : CLAIM
    TERM document_section(title="deferred_revenue_schedule") -> document_section_3 : TERM
    TERM subject(kind="deferred_balances_and_revenue_recognition", qualifier=document_section_3) -> subject_6 : TERM
    CLAIM enables(condition=subject_6, outcome=t1.activity_3) BY role_agent STATUS asserted SOURCE "t2:s9" -> enables_3 : CLAIM
    TERM document_section(title="revenue_reports") -> document_section_4 : TERM
    TERM subject(kind="recognized_revenue", qualifier=document_section_4) -> subject_7 : TERM
    CLAIM provides(actor=platform_label::zuora, subject=subject_7) BY role_agent STATUS asserted SOURCE "t2:s12" -> provides_2 : CLAIM
    TERM activity(object="report_discrepancies", verb="review_and_investigate") -> activity_6 : TERM
    TERM activity(object="balance_sheet_accounts", verb="reconcile") -> activity_7 : TERM
    CLAIM leads_to(cause=activity_6, effect=activity_7) BY role_agent STATUS asserted SOURCE "t2:s14" -> leads_to_2 : CLAIM
  }
  TURN t3 SPEAKER=USER {
    TERM subject(kind="usage_and_adjustments") -> subject_8 : TERM
    TERM subject(kind="school_with_parent_hierarchy") -> subject_9 : TERM
    TERM time_point(date="date_of_usage_and_date_billed") -> time_point_2 : TERM
    TERM subject(kind="invoice_number_and_amount") -> subject_10 : TERM
    TERM conjunction(items=[subject_8, subject_9, time_point_2, subject_10]) -> conjunction_2 : TERM
    TERM subject(kind="custom_report", qualifier=conjunction_2) -> subject_11 : TERM
    UTTER ask(target=subject_11)
  }
  TURN t4 SPEAKER=AGENT {
    CLAIM provides(actor=platform_label::zuora, subject=t3.subject_11) BY role_agent STATUS asserted SOURCE "t4:s1" -> provides_3 : CLAIM
    TERM document_section(title="reporting_reports_new") -> document_section_5 : TERM
    TERM activity(instrument=platform_label::zuora, object=document_section_5, verb="create_custom_report") -> activity_8 : TERM
    TERM subject(kind="invoice_and_payment_data_source", qualifier=platform_label::zuora) -> subject_12 : TERM
    TERM activity(object=subject_12, verb="select_data_source") -> activity_9 : TERM
    TERM time_point(date="reporting_date_range") -> time_point_3 : TERM
    TERM include(item=t3.conjunction_2) -> include_2 : TERM
    TERM activity(object=include_2, purpose=time_point_3, verb="add_columns") -> activity_10 : TERM
    TERM subject(kind="account_data_source", qualifier=platform_label::zuora) -> subject_13 : TERM
    TERM include(item=subject_13) -> include_3 : TERM
    TERM activity(object=include_3, purpose=t3.subject_9, verb="fetch_parent_hierarchy") -> activity_11 : TERM
    TERM config_setting(option="filters_and_groupings", section="custom_report", value="apply_filters_and_groupings") -> config_setting_2 : TERM
    TERM activity(object=config_setting_2, verb="run_report") -> activity_12 : TERM
    TERM sequence(items=[activity_8, activity_9, activity_10, activity_11, activity_12]) -> sequence_2 : TERM
    CLAIM statement(fact=sequence_2) BY role_agent STATUS asserted SOURCE "t4:s21" -> statement_3 : CLAIM
    TERM temporal_context(activity=activity_12, period="regular_intervals") -> temporal_context_2 : TERM
    CLAIM ongoing(target=temporal_context_2) BY role_agent STATUS asserted SOURCE "t4:s23" -> ongoing_4 : CLAIM
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | activity | covered |
| n2 | action | activity | covered |
| n3 | temporal | ongoing | covered |
| n4 | speech_act | ask, subject | covered |
| n5 | object | platform_label::zuora | label-preserved |
| n6 | object | subject | covered |
| n7 | claim | statement, involves, activity, subject | covered |
| n8 | object | document_section | covered |
| n9 | claim | enables, subject, activity | covered |
| n10 | object | document_section | covered |
| n11 | claim | enables, subject | covered |
| n12 | object | document_section, subject, provides | covered |
| n13 | claim | leads_to, activity | covered |
| n14 | speech_act | ask, subject | covered |
| n15 | object | subject | covered |
| n16 | object | subject | covered |
| n17 | object | time_point | covered |
| n18 | object | subject | covered |
| n19 | claim | provides | covered |
| n20 | action | activity, document_section | covered |
| n21 | object | subject | covered |
| n22 | action | activity, time_point, include | covered |
| n23 | action | include, activity, subject | covered |
| n24 | action | config_setting, activity, sequence, statement | covered |
| n25 | temporal | ongoing, temporal_context | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t4:s24 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2, t2:s1, t4:s1 "Zuora" → platform_label::zuora (label only; no platform sense resolved)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
