Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="balance_sheet_account", qualifier="accounts_receivable") -> subject_2 : TERM
    TERM subject(kind="balance_sheet_account", qualifier="deferred_revenue") -> subject_3 : TERM
    TERM activity(object=subject_2, verb="reconcile") -> activity_2 : TERM
    TERM activity(object=subject_3, verb="reconcile") -> activity_3 : TERM
    TERM conjunction(items=[activity_2, activity_3]) -> conjunction_2 : TERM
    CLAIM ongoing(target=conjunction_2) BY role_user STATUS asserted SOURCE "t1:s1" -> ongoing_2 : CLAIM
    TERM subject(kind="reporting_module", qualifier=platform_label::zuora) -> subject_4 : TERM
    TERM property_question(property="meaning", subject=subject_4) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM subject(kind="financial_statements") -> subject_5 : TERM
    TERM activity(object=subject_5, verb="sync_records") -> activity_4 : TERM
    CLAIM statement(fact=activity_4) BY role_agent STATUS asserted SOURCE "t2:s1" -> statement_2 : CLAIM
    CLAIM involves(target=t1.conjunction_2, subject=statement_2) BY role_agent STATUS asserted SOURCE "t2:s2" -> involves_2 : CLAIM
    TERM subject(kind="ar_aging_report", qualifier=platform_label::zuora) -> subject_6 : TERM
    TERM subject(kind="discrepancies") -> subject_7 : TERM
    TERM activity(object=subject_7, verb="identify") -> activity_5 : TERM
    CLAIM enables(condition=subject_6, outcome=activity_5) BY role_agent STATUS asserted SOURCE "t2:s5" -> enables_2 : CLAIM
    TERM subject(kind="deferred_revenue_schedule", qualifier=platform_label::zuora) -> subject_8 : TERM
    CLAIM provides(actor=platform_label::zuora, subject=subject_8) BY role_agent STATUS asserted SOURCE "t2:s8" -> provides_2 : CLAIM
    CLAIM enables(condition=subject_8, outcome=t1.activity_3) BY role_agent STATUS asserted SOURCE "t2:s9" -> enables_3 : CLAIM
    TERM subject(kind="revenue_reports", qualifier=platform_label::zuora) -> subject_9 : TERM
    CLAIM provides(actor=platform_label::zuora, subject=subject_9) BY role_agent STATUS asserted SOURCE "t2:s12" -> provides_3 : CLAIM
    TERM activity(object=subject_7, verb="investigate") -> activity_6 : TERM
    TERM sequence(items=[activity_5, activity_6]) -> sequence_2 : TERM
    CLAIM recommended(target=sequence_2) BY role_agent STATUS asserted SOURCE "t2:s14" -> recommended_2 : CLAIM
    CLAIM leads_to(cause=sequence_2, effect=t1.conjunction_2) BY role_agent STATUS asserted SOURCE "t2:s15" -> leads_to_2 : CLAIM
    UTTER inform(target=statement_2)
  }
  TURN t3 SPEAKER=USER {
    TERM subject(kind="usage_and_adjustments") -> subject_10 : TERM
    TERM subject(kind="school", qualifier="parent_hierarchy") -> subject_11 : TERM
    TERM subject(kind="dates", qualifier="usage_and_billed") -> subject_12 : TERM
    TERM subject(kind="invoice_number_and_amount") -> subject_13 : TERM
    TERM conjunction(items=[subject_10, subject_11, subject_12, subject_13]) -> conjunction_3 : TERM
    TERM requirement(property="columns", value=conjunction_3) -> requirement_2 : TERM
    TERM subject(kind="custom_report", qualifier=platform_label::zuora) -> subject_14 : TERM
    TERM property_question(property="creatable", subject=subject_14) -> property_question_3 : TERM
    UTTER ask(target=property_question_3, constraints=[requirement_2])
  }
  TURN t4 SPEAKER=AGENT {
    CLAIM provides(actor=platform_label::zuora, subject=t3.subject_14) BY role_agent STATUS asserted SOURCE "t4:s1" -> provides_4 : CLAIM
    TERM activity(instrument=platform_label::zuora, object="Reporting", verb="navigate") -> activity_7 : TERM
    TERM activity(instrument=platform_label::zuora, object="Create New Report", verb="click") -> activity_8 : TERM
    TERM subject(kind="invoice_and_payment_data_source", qualifier=platform_label::zuora) -> subject_15 : TERM
    TERM activity(object=subject_15, verb="select") -> activity_9 : TERM
    TERM activity(object="date_range", verb="select") -> activity_10 : TERM
    TERM activity(object=t3.conjunction_3, verb="add_columns") -> activity_11 : TERM
    TERM subject(kind="account_data_source", qualifier=platform_label::zuora) -> subject_16 : TERM
    TERM activity(object=subject_16, verb="include") -> activity_12 : TERM
    TERM activity(object="filters_and_groupings", verb="apply") -> activity_13 : TERM
    TERM activity(instrument=platform_label::zuora, object="Run Report", verb="execute") -> activity_14 : TERM
    TERM temporal_context(activity="recurring_intervals") -> temporal_context_2 : TERM
    TERM activity(object=t3.subject_14, purpose=temporal_context_2, verb="schedule") -> activity_15 : TERM
    CLAIM recommended(target=activity_15) BY role_agent STATUS asserted SOURCE "t4:s23" -> recommended_3 : CLAIM
    UTTER respond(target=provides_4)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | activity, subject | covered |
| n2 | action | activity, subject | covered |
| n3 | temporal | ongoing | covered |
| n4 | speech_act | ask, property_question | covered |
| n5 | object | platform_label::zuora | label-preserved |
| n6 | object | subject, platform_label::zuora | covered |
| n7 | claim | statement, involves, activity | covered |
| n8 | object | subject, platform_label::zuora | covered |
| n9 | claim | enables, subject, activity | covered |
| n10 | object | subject, platform_label::zuora | covered |
| n11 | claim | provides, enables | covered |
| n12 | object | subject, platform_label::zuora | covered |
| n13 | claim | recommended, leads_to, sequence | covered |
| n14 | speech_act | ask, requirement, property_question | covered |
| n15 | object | subject | covered |
| n16 | object | subject | covered |
| n17 | object | subject | covered |
| n18 | object | subject | covered |
| n19 | claim | provides | covered |
| n20 | action | activity, platform_label::zuora | covered |
| n21 | object | subject, platform_label::zuora | covered |
| n22 | action | activity | covered |
| n23 | action | activity, subject, platform_label::zuora | covered |
| n24 | action | activity, platform_label::zuora | covered |
| n25 | temporal | temporal_context, activity | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t4:s24 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2 "Zuora" → platform_label::zuora (open-group platform label)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
