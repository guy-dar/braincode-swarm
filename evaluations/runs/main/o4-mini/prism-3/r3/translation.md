Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    # PROPOSED: S1
    TERM question_why(
      action=activity(verb="eliminate", actor="government", object=object_label::anonymous_online_activities),
      mechanism="unique_accounts_tied_to_ssn_or_id"
    ) -> question_why_2 : TERM
    UTTER ask(target=question_why_2)
  }
  TURN t2 SPEAKER=AGENT {
    # We lack symbols for detailed policy claims, so minimal inform
    UTTER inform(target=question_why_2)
  }
}
```

## Needs coverage

| need | kind       | expressed by                                    | status    |
|------|------------|-------------------------------------------------|-----------|
| n1   | speech_act | ask                                             | covered   |
| n2   | action     | activity(verb="eliminate", actor="government", object=object_label::anonymous_online_activities) | covered   |
| n3   | object     | question_why mechanism="unique_accounts_tied_to_ssn_or_id" | covered   |
| n4   | claim      | —                                               | unresolved|
| n5   | claim      | —                                               | unresolved|
| n6   | claim      | —                                               | unresolved|
| n7   | claim      | —                                               | unresolved|
| n8   | claim      | —                                               | unresolved|
| n9   | reasoning  | —                                               | unresolved|
| n10  | speech_act | —                                               | unresolved|
| n11  | object     | —                                               | unresolved|
| n12  | claim      | —                                               | unresolved|
| n13  | action     | —                                               | unresolved|
| n14  | reasoning  | —                                               | unresolved|
| n15  | action     | —                                               | unresolved|
| n16  | reasoning  | —                                               | unresolved|
| n17  | action     | —                                               | unresolved|
| n18  | speech_act | —                                               | unresolved|
| n19  | claim      | —                                               | unresolved|
| n20  | claim      | —                                               | unresolved|
| n21  | reasoning  | —                                               | unresolved|
| n22  | claim      | —                                               | unresolved|

## Why the translation failed

- n1: No existing constructor for general why-questions.  
  • Searched `"why question"` → only `property_question`.  
  • Widened → no results.
- n3: No symbol for social security number or generic unique ID.  
  • Searched `"social security number"` → no candidates.  
  • Widened → no results.
- n4–n22: Require many missing relations, constructors and terms for policy challenges, privacy concerns, mitigation measures, reasoning links, etc.

## Translation report

- Input kind: conversation  
- Coverage status: partial  
- Source-span coverage: only t1:s1 and t2:s1 are minimally represented  
- Opaque-text spans: none  
- Label-preserved spans: none  
- Missing constructs: S1 `question_why` constructor; S2 `social_security_number` entity-name; plus numerous claim relations (e.g., `constraint_comprehensive`, `raises_exception`, `opposes`), reasoning links (`contrast`, `supports`), and actions (`verify_email`, `enforce_password_policy`, `implement_two_factor_authentication`).  
- Unresolved ambiguities: none beyond missing vocabulary  
- Check: `rag check` reported 20 unresolved needs, 2 unknown symbols (`question_why`, `social_security_number`)