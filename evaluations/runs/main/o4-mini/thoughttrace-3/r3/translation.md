Status: failed
Mode: REQUEST

## Suggested translation

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    CLAIM cannot_complete(target="a certain game") BY role_user STATUS asserted SOURCE "t1:s1" -> cannot_complete_2 : CLAIM  # PROPOSED: S1
    TERM request_help(object=object_label::game) -> request_help_2 : TERM  # PROPOSED: S2
    UTTER ask(target=request_help_2)
  }
  TURN t2 SPEAKER=AGENT {
    UTTER confirm(target=request_help_2)
    TERM offer_help() -> offer_help_2 : TERM
    UTTER propose(target=offer_help_2)
    TERM property_question(subject=object_label::game, property="platform") -> pq1_2 : TERM  # PROPOSED: S3
    UTTER ask(target=pq1_2)
    TERM property_question(subject=object_label::game, property="level_or_part") -> pq2_2 : TERM  # PROPOSED: S3
    UTTER ask(target=pq2_2)
    TERM property_question(subject=object_label::game, property="error_messages") -> pq3_2 : TERM  # PROPOSED: S3
    UTTER ask(target=pq3_2)
    UTTER express_interest(target=offer_help_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | claim | cannot_complete | proposed |
| n2 | speech_act | ask | proposed |
| n3 | object | object_label::game | label-preserved |
| n4 | speech_act | confirm | covered |
| n5 | action | propose, offer_help | covered |
| n6 | speech_act | ask | proposed |
| n7 | object | object_label::game | label-preserved |
| n8 | object | property_question | covered |
| n9 | object | property_question | covered |
| n10 | object | property_question | covered |
| n11 | reasoning | — | unresolved |
| n12 | speech_act | express_interest | covered |

## Why the translation failed

- n1 "User is failing to complete a specific video game": no existing claim relation covers user inability to complete an activity. Proposed S1.
- n2 "User asks the assistant for help completing a game": ask exists, but no TERM constructor for a help request. Proposed S2.
- n6 "Assistant asks the user for more information about their issue": ask exists, but no constructor to represent property-targeted questions. Proposed S3.
- n11 "Providing more details allows the assistant to create a better tailored solution": no reasoning relation expressing enables or facilitates outcome from details. Unresolved.

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: t1:s1, t2:s1–t2:s11 represented except the reasoning link in n11
- Opaque-text spans: none
- Label-preserved spans: n3 ("game" → object_label::game), n7 ("game" → object_label::game)
- Missing constructs: cannot_complete claim relation; request_help constructor; property_question constructor
- Unresolved ambiguities: none
- Check: `rag check` reported unresolved needs (n1, n2, n6, n11) and unknown symbols (cannot_complete, request_help, property_question)
