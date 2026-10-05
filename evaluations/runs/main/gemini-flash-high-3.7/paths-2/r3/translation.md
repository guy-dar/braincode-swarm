Status: success
Mode: TRACE

## BrainCode
```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="accounts_receivable") -> subject_2 : TERM
    TERM activity(object=subject_2, verb="reconcile") -> activity_2 : TERM
    TERM subject(kind="deferred_revenue") -> subject_3 : TERM
    TERM activity(object=subject_3, verb="reconcile") -> activity_3 : TERM
    CLAIM ongoing(target=activity_2) BY role_user STATUS asserted SOURCE "t1:s1" -> ongoing_2 : CLAIM
    CLAIM ongoing(target=activity_3) BY role_user STATUS asserted SOURCE "t1:s1" -> ongoing_3 : CLAIM
    TERM document_section(title="Reporting") -> document_section_2 : TERM
    TERM subject(kind="balance_sheet", qualifier=platform_label::zuora) -> subject_4 : TERM
    TERM property_question(property="meaning", subject=subject_4) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    CLAIM statement(fact=t1.subject_4) BY role_agent STATUS asserted SOURCE "t2:s1" -> statement_2 : CLAIM
    TERM subject(kind="financial_statement") -> subject_2 : TERM
    CLAIM involves(target=subject_2, subject=statement_2) BY role_agent STATUS asserted SOURCE "t2:s2" -> involves_2 : CLAIM
    TERM document_section(title="Accounts Receivable Aging Report") -> document_section_2 : TERM
    CLAIM enables(condition=document_section_2, outcome=statement_2) BY role_agent STATUS asserted SOURCE "t2:s6" -> enables_2 : CLAIM
    TERM document_section(title="Deferred Revenue Schedule") -> document_section_3 : TERM
    CLAIM enables(condition=document_section_3, outcome=statement_2) BY role_agent STATUS asserted SOURCE "t2:s10" -> enables_3 : CLAIM
    TERM document_section(title="Revenue Reports") -> document_section_4 : TERM
    CLAIM leads_to(cause=document_section_4, effect=t1.activity_2) BY role_agent STATUS asserted SOURCE "t2:s14" -> leads_to_2 : CLAIM
    UTTER respond(target=involves_2)
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    TERM subject(kind="usage_and_adjustments") -> subject_2 : TERM
    TERM subject(kind="school", qualifier=platform_label::zuora) -> subject_3 : TERM
    TERM time_point(date="usage_date") -> time_point_2 : TERM
    TERM subject(kind="invoice_number_and_amount") -> subject_4 : TERM
    TERM conjunction(items=[subject_2, subject_3, time_point_2, subject_4]) -> conjunction_2 : TERM
    TERM document_section(items=[conjunction_2], title="custom_report") -> document_section_2 : TERM
    TERM property_question(property="can_create_report", subject=document_section_2) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    CLAIM provides(actor=platform_label::zuora, subject=platform_label::zuora) BY role_agent STATUS asserted SOURCE "t4:s1" -> provides_2 : CLAIM
    TERM document_section(title="Reporting") -> document_section_2 : TERM
    TERM activity(object=document_section_2, verb="create_report") -> activity_2 : TERM
    TERM subject(kind="Invoice_and_Payment_data_source", qualifier=platform_label::zuora) -> subject_2 : TERM
    TERM duration(amount=1, unit=unit_month) -> duration_2 : TERM
    TERM subject(kind="Account_data_source") -> subject_3 : TERM
    TERM include(item=subject_3) -> include_2 : TERM
    TERM config_setting(option="filters", section="report", value=platform_label::zuora) -> config_setting_2 : TERM
    TERM sequence(items=[activity_2, include_2, config_setting_2]) -> sequence_2 : TERM
    TERM performance_tracking(target=sequence_2) -> performance_tracking_2 : TERM
    CLAIM user_practice(activity=performance_tracking_2) BY role_agent STATUS asserted SOURCE "t4:s23" -> user_practice_2 : CLAIM
    UTTER respond(target=provides_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | activity | covered |
| n2 | action | activity | covered |
| n3 | temporal | ongoing | covered |
| n4 | speech_act | ask, property_question | covered |
| n5 | object | platform_label::zuora | label-preserved |
| n6 | object | document_section, subject | covered |
| n7 | claim | statement, involves | covered |
| n8 | object | document_section | covered |
| n9 | claim | enables | covered |
| n10 | object | document_section | covered |
| n11 | claim | enables | covered |
| n12 | object | document_section | covered |
| n13 | claim | leads_to | covered |
| n14 | speech_act | ask, property_question | covered |
| n15 | object | subject | covered |
| n16 | object | subject | covered |
| n17 | object | time_point | covered |
| n18 | object | subject | covered |
| n19 | claim | provides | covered |
| n20 | action | document_section, activity | covered |
| n21 | object | subject | covered |
| n22 | action | duration, unit_month | covered |
| n23 | action | include | covered |
| n24 | action | config_setting, sequence, performance_tracking | covered |
| n25 | temporal | user_practice, performance_tracking | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t4:s24 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2 "zuora" -> platform_label::zuora (label only; no sense resolved)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
