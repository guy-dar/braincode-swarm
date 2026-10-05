Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM account_reconciliation(
      accounts=[
        subject(kind="balance_sheet_account", qualifier="accounts_receivable"),
        subject(kind="balance_sheet_account", qualifier="deferred_revenue")
      ]
    ) -> account_reconciliation_2 : TERM  # PROPOSED: S1
    UTTER ask(target=account_reconciliation_2)
  }
  TURN t1 SPEAKER=USER {
    TERM custom_report_request(
      platform=platform_label::zuora,
      data_source="invoice_and_payment",
      columns=[
        subject(kind="usage_record"),
        subject(kind="adjustment"),
        subject(kind="school", qualifier="with_parent_if_applicable"),
        subject(kind="date", qualifier="usage_date"),
        subject(kind="date", qualifier="billed_date"),
        subject(kind="invoice", qualifier="number"),
        subject(kind="amount")
      ]
    ) -> custom_report_request_2 : TERM  # PROPOSED: S2
    UTTER ask(target=custom_report_request_2)
  }
  TURN t2 SPEAKER=AGENT {
    CLAIM involves(subject=account_reconciliation_2, target=platform_label::zuora)
      BY role_respondent STATUS asserted SOURCE "t2:s1" -> involves_2 : CLAIM
    CLAIM enables(
      condition=account_reconciliation_2,
      outcome=ability_to_reconcile_financial_records
    ) BY role_respondent STATUS asserted SOURCE "t2:s1" -> enables_2 : CLAIM
  }
}
```

## Needs coverage

| need | kind      | expressed by                    | status    |
|---|-----------|---------------------------------|-----------|
| n1 | action    | account_reconciliation           | proposed  |
| n2 | action    | account_reconciliation           | proposed  |
| n3 | temporal  | —                               | unresolved|
| n4 | speech_act| ask                              | covered   |
| n5 | object    | platform_label::zuora            | covered   |
| n6 | object    | platform_label::zuora            | covered   |
| n7 | claim     | involves                         | covered   |
| n8 | object    | —                               | unresolved|
| n9 | claim     | —                               | unresolved|
| n10| object    | —                               | unresolved|
| n11| claim     | —                               | unresolved|
| n12| object    | —                               | unresolved|
| n13| claim     | —                               | unresolved|
| n14| speech_act| ask                              | covered   |
| n15| object    | subject                          | unresolved|
| n16| object    | subject                          | unresolved|
| n17| object    | subject                          | unresolved|
| n18| object    | subject                          | unresolved|
| n19| claim     | custom_report_request            | proposed  |
| n20| action    | custom_report_request            | proposed  |
| n21| object    | platform_label::zuora            | covered   |
| n22| action    | custom_report_request            | proposed  |
| n23| action    | custom_report_request            | proposed  |
| n24| action    | custom_report_request            | proposed  |
| n25| temporal  | —                               | unresolved|

## Why the translation failed

- n1, n2: No existing constructor describes reconciling specific balance sheet accounts (reconcile_code is for code entities). Proposed S1: `account_reconciliation`.
- n19–n24: No existing constructor to specify a custom report request with platform, data source, and column list. Proposed S2: `custom_report_request`.

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: t1:s1 covers reconciliation request via account_reconciliation_2; t1:s2 covers report request via custom_report_request_2; t2:s1 covers involves and enables claims
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: constructors `account_reconciliation` (S1) and `custom_report_request` (S2)
- Unresolved ambiguities: none
- Check: `rag check` reported unresolved needs and proposed symbols only
