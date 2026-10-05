Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM reconcile_balance_sheet_accounts(entities=[subject(kind="accounts_receivable"), subject(kind="deferred_revenue")], system=platform_label::zuora) -> reconcile_balance_sheet_accounts_2 : TERM  # PROPOSED: S1
    UTTER ask(target=reconcile_balance_sheet_accounts_2)
    TERM explain_in_reporting(topic=subject(kind="balance_sheet_reconciliation"), system=platform_label::zuora) -> explain_in_reporting_2 : TERM  # PROPOSED: S2
    UTTER ask(target=explain_in_reporting_2)
  }
  TURN t2 SPEAKER=AGENT {
    UTTER inform(content="Explanation omitted")
  }
  TURN t3 SPEAKER=USER {
    TERM create_custom_report(data_source=subject(kind="usage and adjustment records"), columns=[subject(kind="date of usage"), subject(kind="date billed"), subject(kind="invoice number"), subject(kind="amount")], system=platform_label::zuora) -> create_custom_report_2 : TERM  # PROPOSED: S3
    UTTER ask(target=create_custom_report_2)
  }
  TURN t4 SPEAKER=AGENT {
    UTTER inform(content="Instructions omitted")
    TERM schedule_recurring_report(report=create_custom_report_2, interval=duration(amount=1, unit=unit_week)) -> schedule_recurring_report_2 : TERM  # PROPOSED: S4
    UTTER inform(target=CLAIM statement(fact=schedule_recurring_report_2))
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | reconcile_balance_sheet_accounts | proposed |
| n2 | action | reconcile_balance_sheet_accounts | proposed |
| n3 | temporal |  | unresolved |
| n4 | speech_act | ask | covered |
| n5 | object | platform_label::zuora | covered |
| n6 | object |  | unresolved |
| n7 | claim |  | unresolved |
| n8 | object |  | unresolved |
| n9 | claim |  | unresolved |
| n10 | object |  | unresolved |
| n11 | claim |  | unresolved |
| n12 | object |  | unresolved |
| n13 | claim |  | unresolved |
| n14 | speech_act | ask | covered |
| n15 | object | subject(kind="usage and adjustment records") | covered |
| n16 | object |  | unresolved |
| n17 | object |  | unresolved |
| n18 | object |  | unresolved |
| n19 | claim |  | unresolved |
| n20 | action |  | unresolved |
| n21 | object |  | unresolved |
| n22 | action |  | unresolved |
| n23 | action |  | unresolved |
| n24 | action |  | unresolved |
| n25 | temporal | schedule_recurring_report | proposed |

## Why the translation failed

- n1, n2 "reconcile accounts receivable/deferred revenue balance sheet accounts": `rag search "reconcile accounts receivable"` → only `reconcile_code` (for code entities), wrong domain; `rag widen` → no financial-account reconciliation symbol. Proposed S1.
- n3 "maintain ongoing reconciliation over time": `ongoing` exists but cannot semantic-link to reconciliation process; unresolved.
- n6 "Zuora reporting module": no symbol for a software module within a platform; unresolved.
- n7 "Zuora reconciliation involves syncing...": `involves` relation exists but lacks a term for the reconciliation action; unresolved.
- n8 "Accounts Receivable Aging Report": no symbol or constructor for this specific report entity; unresolved.
- n9, n11, n13 various claims about report contents and actions (categorization, visibility, investigation): no glossary relations or constructors; unresolved.
- n10, n12 "Deferred Revenue Schedule report" and "Revenue Reports": report entities missing; unresolved.
- n16–n18 objects for school parent hierarchy, dates, invoice number and amount: no constructors or subject variants; unresolved.
- n19 claim that a custom report can be created: no glossary relation for report capability; unresolved.
- n20–n24 agent actions (navigate UI, select filters, add columns, apply groupings, execute report): few generic operations exist but no combinator for custom report flow; unresolved.

- n25 "schedule report to run at recurring intervals": no constructor for scheduling reports; Proposed S4.

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: t1:s1–t4:s24 represented as above; detailed agent steps omitted
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: S1 reconcile_balance_sheet_accounts constructor; S2 explain_in_reporting constructor; S3 create_custom_report constructor; S4 schedule_recurring_report constructor
- Unresolved ambiguities: none beyond missing vocabulary
- Check: `rag check` reported unresolved needs and no invalid symbols beyond the PROPOSED ones
