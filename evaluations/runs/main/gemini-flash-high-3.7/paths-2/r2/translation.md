Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="accounts_receivable") -> subject_2 : TERM
    TERM subject(kind="deferred_revenue") -> subject_3 : TERM
    TERM activity(object=subject_2, verb="reconcile") -> activity_2 : TERM
    TERM activity(object=subject_3, verb="reconcile") -> activity_3 : TERM
    TERM conjunction(items=[activity_2, activity_3]) -> conjunction_2 : TERM
    CLAIM ongoing(target=conjunction_2) BY role_user STATUS asserted SOURCE "t1:s1" -> ongoing_2 : CLAIM
    TERM subject(kind="reporting", qualifier=platform_label::zuora) -> subject_4 : TERM
    TERM property_question(property="meaning", subject=subject_4) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM activity(instrument=platform_label::zuora, object=t1.conjunction_2, verb="sync") -> activity_4 : TERM
    CLAIM statement(fact=activity_4) BY role_agent STATUS asserted SOURCE "t2:s1" -> statement_2 : CLAIM
    UTTER respond(target=statement_2)
    TERM activity(object="financial_statements", verb="reconcile") -> activity_5 : TERM
    CLAIM involves(target=activity_5, subject=statement_2) BY role_agent STATUS asserted SOURCE "t2:s2" -> involves_2 : CLAIM
    TERM requirement(property="format", value=format_structured_report) -> requirement_2 : TERM
    TERM document_section(items=[requirement_2], title="Accounts Receivable Aging Report") -> document_section_2 : TERM
    CLAIM provides(actor=platform_label::zuora, subject=document_section_2) BY role_agent STATUS asserted SOURCE "t2:s5" -> provides_2 : CLAIM
    TERM activity(object=document_section_2, verb="compare") -> activity_6 : TERM
    TERM activity(object="discrepancies", verb="rectify") -> activity_7 : TERM
    CLAIM enables(condition=activity_6, outcome=activity_7) BY role_agent STATUS asserted SOURCE "t2:s6" -> enables_2 : CLAIM
    TERM document_section(items=[requirement_2], title="Deferred Revenue Schedule") -> document_section_3 : TERM
    CLAIM provides(actor=platform_label::zuora, subject=document_section_3) BY role_agent STATUS asserted SOURCE "t2:s8" -> provides_3 : CLAIM
    CLAIM enables(condition=document_section_3, outcome=t1.activity_3) BY role_agent STATUS asserted SOURCE "t2:s10" -> enables_3 : CLAIM
    TERM document_section(items=[requirement_2], title="Revenue Reports") -> document_section_4 : TERM
    CLAIM provides(actor=platform_label::zuora, subject=document_section_4) BY role_agent STATUS asserted SOURCE "t2:s12" -> provides_4 : CLAIM
    TERM activity(object=document_section_4, verb="compare") -> activity_8 : TERM
    CLAIM enables(condition=activity_8, outcome=t1.conjunction_2) BY role_agent STATUS asserted SOURCE "t2:s13" -> enables_4 : CLAIM
    TERM activity(object="reports", verb="review") -> activity_9 : TERM
    CLAIM user_practice(activity=activity_9) BY role_agent STATUS asserted SOURCE "t2:s14" -> user_practice_2 : CLAIM
    CLAIM leads_to(cause=activity_9, effect=t1.conjunction_2) BY role_agent STATUS asserted SOURCE "t2:s14" -> leads_to_2 : CLAIM
  }
  TURN t3 SPEAKER=USER {
    TERM subject(kind="usage_and_adjustments") -> subject_5 : TERM
    TERM subject(kind="school_with_parent") -> subject_6 : TERM
    TERM time_point(date="usage_and_billed_date") -> time_point_2 : TERM
    TERM requirement(property="columns", value=format_table) -> requirement_3 : TERM
    TERM conjunction(items=[subject_5, subject_6, time_point_2, requirement_3]) -> conjunction_3 : TERM
    TERM activity(instrument=platform_label::zuora, object=conjunction_3, verb="create_custom_report") -> activity_10 : TERM
    TERM property_question(property="feasibility", subject=activity_10) -> property_question_3 : TERM
    UTTER ask(target=property_question_3)
  }
  TURN t4 SPEAKER=AGENT {
    CLAIM statement(fact=t3.activity_10) BY role_agent STATUS asserted SOURCE "t4:s1" -> statement_3 : CLAIM
    UTTER respond(target=statement_3)
    TERM activity(instrument=platform_label::zuora, object="create_new_report", verb="navigate") -> activity_11 : TERM
    TERM subject(kind="invoice_and_payment_data_source", qualifier=platform_label::zuora) -> subject_7 : TERM
    TERM activity(object=subject_7, verb="choose") -> activity_12 : TERM
    TERM activity(object=t3.conjunction_3, verb="add_columns") -> activity_13 : TERM
    TERM subject(kind="account_data_source", qualifier=platform_label::zuora) -> subject_8 : TERM
    TERM include(item=subject_8) -> include_2 : TERM
    TERM activity(object="filters_and_groupings", verb="apply") -> activity_14 : TERM
    TERM activity(object="report", verb="run") -> activity_15 : TERM
    TERM sequence(items=[activity_11, activity_12, activity_13, include_2, activity_14, activity_15]) -> sequence_2 : TERM
    CLAIM statement(fact=sequence_2) BY role_agent STATUS asserted SOURCE "t4:s2" -> statement_4 : CLAIM
    TERM temporal_context(activity=activity_15, period="recurring_intervals") -> temporal_context_2 : TERM
    CLAIM ongoing(target=temporal_context_2) BY role_agent STATUS asserted SOURCE "t4:s23" -> ongoing_3 : CLAIM
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | activity, format_structured_report | covered |
| n2 | action | activity | covered |
| n3 | temporal | ongoing | covered |
| n4 | speech_act | ask, property_question, subject | covered |
| n5 | object | platform_label::zuora | label-preserved |
| n6 | object | subject, platform_label::zuora | covered |
| n7 | claim | statement, involves, activity | covered |
| n8 | object | document_section, requirement, format_structured_report | covered |
| n9 | claim | enables, activity | covered |
| n10 | object | document_section, provides, enables | covered |
| n11 | claim | enables, document_section | covered |
| n12 | object | document_section, provides | covered |
| n13 | claim | user_practice, leads_to, activity | covered |
| n14 | speech_act | ask, property_question, activity | covered |
| n15 | object | subject | covered |
| n16 | object | subject | covered |
| n17 | object | time_point | covered |
| n18 | object | requirement, format_table | covered |
| n19 | claim | statement, activity | covered |
| n20 | action | activity, sequence | covered |
| n21 | object | subject, platform_label::zuora | covered |
| n22 | action | activity | covered |
| n23 | action | include, subject, platform_label::zuora | covered |
| n24 | action | activity, sequence | covered |
| n25 | temporal | temporal_context, ongoing | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t4:s24 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2 "zuora" -> platform_label::zuora (label only; no sense resolved)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
