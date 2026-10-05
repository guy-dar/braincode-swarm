Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM reconcile_code(
      entities=[
        subject(kind="accounts_receivable_balance_sheet_account", qualifier=platform_label::zuora),
        subject(kind="deferred_revenue_balance_sheet_account", qualifier=platform_label::zuora)
      ],
      objective="financial_records"
    ) -> reconciliation_term : TERM
    CLAIM request(target=reconciliation_term) BY user STATUS asserted SOURCE "t1:s1" -> request_reconcile : CLAIM
    CLAIM ongoing(target=reconciliation_term) BY user STATUS asserted SOURCE "t1:s1" -> ongoing_reconcile : CLAIM

    TERM subject(kind="reporting", qualifier=platform_label::zuora) -> zuora_reporting_term : TERM
    TERM definition(concept=reconciliation_term, context=zuora_reporting_term) -> definition_term : TERM # PROPOSED: S1
    UTTER ask(target=definition_term)
  }
  TURN t2 SPEAKER=AGENT {
    # Detailed report steps unformalized due to missing operations: PROPOSED: S2, S3, S4, S5
  }
  TURN t3 SPEAKER=USER {
    TERM report_request(
      fields=["usage","adjustments","school","date_of_usage","date_billed","invoice_number","amount"],
      data_source="Zuora reporting"
    ) -> usage_request_term : TERM # PROPOSED: S6
    UTTER ask(target=usage_request_term)
  }
  TURN t4 SPEAKER=AGENT {
    # Report creation instructions unformalized due to missing operations: PROPOSED: S2, S3, S4, S5
  }
}
```

## Needs coverage

| need | kind       | expressed by               | status     |
|------|------------|----------------------------|------------|
| n1   | action     | reconcile_code             | covered    |
| n2   | action     | reconcile_code             | covered    |
| n3   | temporal   | ongoing                    | covered    |
| n4   | speech_act | ask                        | covered    |
| n5   | object     | platform_label::zuora      | covered    |
| n6   | object     | subject(...)               | covered    |
| n7   | claim      | request, ongoing           | covered    |
| n8   | object     | –                          | unresolved |
| n9   | claim      | –                          | unresolved |
| n10  | object     | –                          | unresolved |
| n11  | claim      | –                          | unresolved |
| n12  | object     | –                          | unresolved |
| n13  | claim      | –                          | unresolved |
| n14  | speech_act | ask                        | covered    |
| n15  | object     | –                          | unresolved |
| n16  | object     | –                          | unresolved |
| n17  | object     | –                          | unresolved |
| n18  | object     | –                          | unresolved |
| n19  | claim      | –                          | unresolved |
| n20  | action     | –                          | unresolved |
| n21  | object     | –                          | unresolved |
| n22  | action     | –                          | unresolved |
| n23  | action     | –                          | unresolved |
| n24  | action     | –                          | unresolved |
| n25  | temporal   | –                          | unresolved |

## Why the translation failed

- Missing a constructor to express a definition or explanation (t2:s1) → S1.
- Missing operations to formalize report-building steps (navigate, click, add column, run, schedule) → S2–S5.
- Missing a constructor to structure the custom report request (t3:s1) → S6.
- Without these, the agent’s detailed instructions and data-column requests cannot be encoded.

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: t1:s1–t1:s2 fully; t2:s1–t4:s24 unformalized
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: S1–S6
- Unresolved ambiguities: none
- Check: `rag check` reported unresolved needs and unknown symbols
