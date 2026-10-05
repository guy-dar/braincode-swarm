Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="accounts_receivable_balance_sheet_account") -> subject_2 : TERM
    TERM subject(kind="deferred_revenue_balance_sheet_account") -> subject_3 : TERM
    TERM reconcile(entities=[subject_2, subject_3]) -> reconcile_2 : TERM   # PROPOSED: S1
    TERM temporal_context(activity=reconcile_2, period="ongoing") -> temporal_context_2 : TERM
    CLAIM request(target=reconcile_2) BY "user" STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
    CLAIM request(target=temporal_context_2) BY "user" STATUS asserted SOURCE "t1:s1" -> request_3 : CLAIM
    TERM subject(kind="balance_sheet_reconciliation", qualifier=platform_label::zuora) -> subject_4 : TERM
    TERM subject(kind="reporting_module", qualifier=platform_label::zuora) -> subject_5 : TERM
    TERM meaning_question(context=subject_5, subject=subject_4) -> meaning_question_2 : TERM   # PROPOSED: S2
    UTTER ask(target=meaning_question_2)
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM subject(kind="zuora_reconciliation", qualifier=platform_label::zuora) -> subject_6 : TERM
    TERM reconcile(entities=[subject_2, subject_3]) -> reconcile_3 : TERM   # PROPOSED: S1
    CLAIM involves(subject=request_2, target=reconcile_3) BY role_agent STATUS asserted SOURCE "t2:s2" -> involves_2 : CLAIM
    UTTER inform(target=involves_2)
    TERM subject(kind="accounts_receivable_aging_report", qualifier=platform_label::zuora) -> subject_7 : TERM
    TERM subject(kind="unpaid_invoices_by_age") -> subject_8 : TERM
    CLAIM provides(actor=subject_7, subject=subject_8) BY role_agent STATUS asserted SOURCE "t2:s5" -> provides_2 : CLAIM
    TERM subject(kind="discrepancy_identification") -> subject_9 : TERM
    CLAIM enables(condition=subject_7, outcome=subject_9) BY role_agent STATUS asserted SOURCE "t2:s6" -> enables_2 : CLAIM
    TERM subject(kind="deferred_revenue_schedule_report", qualifier=platform_label::zuora) -> subject_10 : TERM
    TERM subject(kind="deferred_balances_and_recognition_entries") -> subject_11 : TERM
    CLAIM provides(actor=subject_10, subject=subject_11) BY role_agent STATUS asserted SOURCE "t2:s9" -> provides_3 : CLAIM
    CLAIM enables(condition=subject_10, outcome=reconcile_3) BY role_agent STATUS asserted SOURCE "t2:s10" -> enables_3 : CLAIM
    TERM subject(kind="revenue_reports", qualifier=platform_label::zuora) -> subject_12 : TERM
    TERM subject(kind="recognized_revenue_by_period") -> subject_13 : TERM
    CLAIM provides(actor=subject_12, subject=subject_13) BY role_agent STATUS asserted SOURCE "t2:s12" -> provides_4 : CLAIM
    TERM subject(kind="regular_review_and_prompt_investigation_of_discrepancies") -> subject_14 : TERM
    CLAIM leads_to(cause=subject_14, effect=temporal_context_2) BY role_agent STATUS asserted SOURCE "t2:s14" -> leads_to_2 : CLAIM
    UTTER inform(target=leads_to_2)
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    TERM subject(kind="usage_and_adjustment_records") -> subject_15 : TERM
    TERM subject(kind="school_with_parent_hierarchy") -> subject_16 : TERM
    TERM subject(kind="date_of_usage") -> subject_17 : TERM
    TERM subject(kind="date_billed") -> subject_18 : TERM
    TERM subject(kind="invoice_number") -> subject_19 : TERM
    TERM subject(kind="amount") -> subject_20 : TERM
    TERM include(item=subject_15) -> include_2 : TERM
    TERM include(item=subject_16) -> include_3 : TERM
    TERM include(item=subject_17) -> include_4 : TERM
    TERM include(item=subject_18) -> include_5 : TERM
    TERM include(item=subject_19) -> include_6 : TERM
    TERM include(item=subject_20) -> include_7 : TERM
    TERM policy_document(title="custom_report", constraints=[include_2, include_3, include_4, include_5, include_6, include_7]) -> policy_document_2 : TERM
    UTTER ask(target=policy_document_2)
  }
  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    CLAIM request(target=policy_document_2) BY role_agent STATUS asserted SOURCE "t4:s1" -> request_4 : CLAIM
    TERM document_section(title="Reporting") -> document_section_2 : TERM
    TERM activity(verb="navigate", object=document_section_2, instrument=platform_label::zuora) -> activity_2 : TERM
    TERM activity(verb="create", object=policy_document_2, instrument=platform_label::zuora) -> activity_3 : TERM
    TERM sequence(items=[activity_2, activity_3]) -> sequence_2 : TERM
    UTTER propose(target=sequence_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | subject, reconcile (PROPOSED: S1) | proposed |
| n2 | action | subject, reconcile (PROPOSED: S1) | proposed |
| n3 | temporal | temporal_context | covered |
| n4 | speech_act | ask, meaning_question (PROPOSED: S2) | proposed |
| n5 | object | platform_label::zuora | label-preserved |
| n6 | object | subject | covered |
| n7 | claim | involves | covered |
| n8 | object | subject | covered |
| n9 | claim | provides, enables | covered |
| n10 | object | subject | covered |
| n11 | claim | provides, enables | covered |
| n12 | object | subject | covered |
| n13 | claim | leads_to | covered |
| n14 | speech_act | ask, policy_document | covered |
| n15 | object | subject, include | covered |
| n16 | object | subject, include | covered |
| n17 | object | subject, include | covered |
| n18 | object | subject, include | covered |
| n19 | claim | request | covered |
| n20 | action | sequence, activity, document_section, propose | covered |
| n21 | object | — | unresolved |
| n22 | action | — | unresolved |
| n23 | action | — | unresolved |
| n24 | action | — | unresolved |
| n25 | temporal | — | unresolved |

## Why the translation failed

- n1/n2: search "reconcile accounts" → only `reconcile_code` (code entities, wrong meaning). Proposed S1.
- n4: "ask what X means" → `ask` needs a TERM target; no meaning/definition question constructor. Proposed S2.
- n21–n25 (t4:s10–s23, detailed procedure steps: choosing data source, date range, columns, filters, running, scheduling): candidates `select_option`, `apply_filters`, `time_point` need runtime REFs or concrete values; no data-source/schedule/recurrence constructor. Not encoded; recurrence "regular intervals" has no constructor. Covered only in part by the sequence in t4. Proposed S3.

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: t1–t3 and t4:s1–s8 represented; t4:s10–s24 procedural steps, caveat t4:s24 and scheduling not represented
- Opaque-text spans: none
- Label-preserved spans: t1:s2 "Zuora" → platform_label::zuora
- Missing constructs: S1 reconcile; S2 meaning_question; S3 recurrence (not yet used in the document)
- Unresolved ambiguities: "it" in t1:s2 taken as balance sheet reconciliation; user holder written as string "user" (no glossary user role)
- Check: not clean; see unresolved needs n21–n25
