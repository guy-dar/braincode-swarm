Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="balance_sheet", qualifier="accounts_receivable") -> subject_2 : TERM
    TERM activity(object=subject_2, verb="reconcile") -> activity_2 : TERM
    TERM subject(kind="balance_sheet", qualifier="deferred_revenue") -> subject_3 : TERM
    TERM activity(object=subject_3, verb="reconcile") -> activity_3 : TERM
    CLAIM ongoing(target=activity_2) BY role_user STATUS asserted SOURCE "t1:s1" -> ongoing_2 : CLAIM
    CLAIM ongoing(target=activity_3) BY role_user STATUS asserted SOURCE "t1:s1" -> ongoing_3 : CLAIM
    TERM subject(kind="reporting", qualifier=platform_label::zuora) -> subject_4 : TERM
    TERM subject(kind="reconciliation", qualifier=subject_4) -> subject_5 : TERM
    UTTER ask(target=subject_5)
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM subject(kind="financial_statements") -> subject_6 : TERM
    CLAIM involves(target=subject_6, subject=t1.ongoing_2) BY role_agent STATUS asserted SOURCE "t2:s2" -> involves_2 : CLAIM
    TERM subject(kind="accounts_receivable_aging_report", qualifier=platform_label::zuora) -> subject_7 : TERM
    TERM activity(instrument=subject_7, verb="spot_discrepancies") -> activity_4 : TERM
    CLAIM enables(condition=subject_7, outcome=activity_4) BY role_agent STATUS asserted SOURCE "t2:s6" -> enables_2 : CLAIM
    TERM subject(kind="deferred_revenue_schedule_report", qualifier=platform_label::zuora) -> subject_8 : TERM
    CLAIM enables(condition=subject_8, outcome=t1.activity_3) BY role_agent STATUS asserted SOURCE "t2:s10" -> enables_3 : CLAIM
    TERM subject(kind="revenue_reports", qualifier=platform_label::zuora) -> subject_9 : TERM
    TERM activity(instrument=subject_9, verb="compare_revenue") -> activity_5 : TERM
    CLAIM enables(condition=subject_9, outcome=activity_5) BY role_agent STATUS asserted SOURCE "t2:s13" -> enables_4 : CLAIM
    TERM activity(object="discrepancies", verb="review_and_investigate") -> activity_6 : TERM
    TERM conjunction(items=[t1.activity_2, t1.activity_3]) -> conjunction_2 : TERM
    CLAIM leads_to(cause=activity_6, effect=conjunction_2) BY role_agent STATUS asserted SOURCE "t2:s14" -> leads_to_2 : CLAIM
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    TERM subject(kind="usage_and_adjustments") -> subject_10 : TERM
    TERM subject(kind="school", qualifier="parent_hierarchy") -> subject_11 : TERM
    TERM subject(kind="dates", qualifier="usage_and_billed") -> subject_12 : TERM
    TERM subject(kind="invoice_and_amount") -> subject_13 : TERM
    TERM conjunction(items=[subject_10, subject_11, subject_12, subject_13]) -> conjunction_3 : TERM
    TERM subject(kind="custom_report", qualifier=platform_label::zuora) -> subject_14 : TERM
    TERM activity(instrument=subject_14, object=conjunction_3, verb="fetch_columns") -> activity_7 : TERM
    UTTER ask(target=activity_7)
  }
  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    CLAIM provides(actor=platform_label::zuora, subject=t3.subject_14) BY role_agent STATUS asserted SOURCE "t4:s1" -> provides_2 : CLAIM
    TERM activity(location="reporting_section", verb="create_new_report") -> activity_8 : TERM
    TERM subject(kind="data_source", qualifier="invoice_and_payment") -> subject_15 : TERM
    TERM activity(object="date_range_and_columns", verb="select_and_add") -> activity_9 : TERM
    TERM subject(kind="data_source", qualifier="account") -> subject_16 : TERM
    TERM include(item=subject_16) -> include_2 : TERM
    TERM activity(object="filters_and_groupings", verb="apply_and_run") -> activity_10 : TERM
    TERM temporal_context(activity="recurring_intervals") -> temporal_context_2 : TERM
    TERM activity(purpose=temporal_context_2, verb="schedule_report") -> activity_11 : TERM
    TERM sequence(items=[activity_8, activity_9, activity_10, activity_11]) -> sequence_2 : TERM
    CLAIM statement(fact=sequence_2) BY role_agent STATUS asserted SOURCE "t4:s2" -> statement_2 : CLAIM
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | activity | covered |
| n2 | action | activity | covered |
| n3 | temporal | ongoing | covered |
| n4 | speech_act | ask | covered |
| n5 | object | platform_label::zuora | label-preserved |
| n6 | object | subject | covered |
| n7 | claim | involves | covered |
| n8 | object | subject | covered |
| n9 | claim | enables | covered |
| n10 | object | subject | covered |
| n11 | claim | enables | covered |
| n12 | object | subject | covered |
| n13 | claim | leads_to | covered |
| n14 | speech_act | ask | covered |
| n15 | object | subject | covered |
| n16 | object | subject | covered |
| n17 | object | subject | covered |
| n18 | object | subject | covered |
| n19 | claim | provides | covered |
| n20 | action | activity | covered |
| n21 | object | subject | covered |
| n22 | action | activity | covered |
| n23 | action | include | covered |
| n24 | action | activity | covered |
| n25 | temporal | temporal_context | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t4:s24 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2, t2:s5, t2:s8, t2:s12, t3:s1, t4:s1 "Zuora" → platform_label::zuora (label only; platform name)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
