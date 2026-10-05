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
    TERM temporal_context(activity=activity_2) -> temporal_context_2 : TERM
    CLAIM ongoing(target=temporal_context_2) BY role_user STATUS asserted SOURCE "t1:s1" -> ongoing_2 : CLAIM
    TERM document_section(title="reporting") -> document_section_2 : TERM
    TERM subject(kind="reconciliation", qualifier=platform_label::zuora) -> subject_2 : TERM
    UTTER ask(target=subject_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM subject(kind="financial_statements") -> subject_3 : TERM
    CLAIM statement(fact=subject_3) BY role_agent STATUS asserted SOURCE "t2:s1" -> statement_2 : CLAIM
    CLAIM involves(target=t1.activity_2, subject=statement_2) BY role_agent STATUS asserted SOURCE "t2:s2" -> involves_2 : CLAIM
    TERM document_section(title="accounts_receivable_aging_report") -> document_section_3 : TERM
    CLAIM enables(condition=document_section_3, outcome=statement_2) BY role_agent STATUS asserted SOURCE "t2:s6" -> enables_2 : CLAIM
    TERM document_section(title="deferred_revenue_schedule") -> document_section_4 : TERM
    CLAIM provides(actor=platform_label::zuora, subject=document_section_4) BY role_agent STATUS asserted SOURCE "t2:s9" -> provides_2 : CLAIM
    CLAIM enables(condition=document_section_4, outcome=statement_2) BY role_agent STATUS asserted SOURCE "t2:s10" -> enables_3 : CLAIM
    TERM document_section(title="revenue_reports") -> document_section_5 : TERM
    CLAIM provides(actor=platform_label::zuora, subject=document_section_5) BY role_agent STATUS asserted SOURCE "t2:s12" -> provides_3 : CLAIM
    TERM activity(instrument=platform_label::zuora, verb="review_reports") -> activity_4 : TERM
    CLAIM leads_to(cause=activity_4, effect=t1.activity_2) BY role_agent STATUS asserted SOURCE "t2:s14" -> leads_to_2 : CLAIM
    TERM temporal_context(activity=activity_4) -> temporal_context_3 : TERM
    CLAIM ongoing(target=temporal_context_3) BY role_agent STATUS asserted SOURCE "t2:s14" -> ongoing_3 : CLAIM
  }
  TURN t3 SPEAKER=USER {
    TERM subject(kind="usage_and_adjustments") -> subject_4 : TERM
    TERM subject(kind="school_hierarchy") -> subject_5 : TERM
    TERM time_point(date="usage_and_billing_dates") -> time_point_2 : TERM
    TERM subject(kind="invoice_and_amount_columns") -> subject_6 : TERM
    TERM document_section(items=[subject_4, subject_5, time_point_2, subject_6], title="custom_report") -> document_section_6 : TERM
    UTTER ask(target=document_section_6)
  }
  TURN t4 SPEAKER=AGENT {
    CLAIM provides(actor=platform_label::zuora, subject=t3.document_section_6) BY role_agent STATUS asserted SOURCE "t4:s1" -> provides_4 : CLAIM
    TERM activity(instrument=platform_label::zuora, object="reporting", verb="navigate") -> activity_5 : TERM
    TERM activity(instrument=platform_label::zuora, object="custom_report", verb="create") -> activity_6 : TERM
    TERM subject(kind="invoice_and_payment_data_source", qualifier=platform_label::zuora) -> subject_7 : TERM
    TERM time_point(date="reporting_date_range") -> time_point_3 : TERM
    TERM activity(instrument=platform_label::zuora, object="date_range_and_columns", verb="configure") -> activity_7 : TERM
    TERM subject(kind="account_data_source", qualifier=platform_label::zuora) -> subject_8 : TERM
    TERM include(item=subject_8) -> include_2 : TERM
    TERM activity(instrument=platform_label::zuora, object="filters_and_groupings", verb="apply") -> activity_8 : TERM
    TERM activity(instrument=platform_label::zuora, object="report", verb="execute") -> activity_9 : TERM
    TERM sequence(items=[activity_5, activity_6, activity_7, include_2, activity_8, activity_9]) -> sequence_2 : TERM
    TERM activity(instrument=platform_label::zuora, object="report", verb="schedule") -> activity_10 : TERM
    TERM temporal_context(activity=activity_10, period="recurring") -> temporal_context_4 : TERM
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | activity | covered |
| n2 | action | activity | covered |
| n3 | temporal | ongoing, temporal_context | covered |
| n4 | speech_act | ask, subject | covered |
| n5 | object | platform_label::zuora | label-preserved |
| n6 | object | document_section | covered |
| n7 | claim | involves, statement | covered |
| n8 | object | document_section | covered |
| n9 | claim | enables | covered |
| n10 | object | document_section | covered |
| n11 | claim | enables, provides | covered |
| n12 | object | document_section, provides | covered |
| n13 | claim | leads_to, ongoing | covered |
| n14 | speech_act | ask, document_section | covered |
| n15 | object | subject | covered |
| n16 | object | subject | covered |
| n17 | object | time_point | covered |
| n18 | object | subject | covered |
| n19 | claim | provides | covered |
| n20 | action | activity, sequence | covered |
| n21 | object | subject | covered |
| n22 | action | activity, time_point | covered |
| n23 | action | include, subject | covered |
| n24 | action | activity, sequence | covered |
| n25 | temporal | activity, temporal_context | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t4:s24 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s1–t4:s24 "zuora" → platform_label::zuora (n5)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
