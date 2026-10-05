Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(verb="complete", actor=role_user, object=object_label::game) -> complete_game : TERM
    TERM inability(activity=complete_game) -> inability_2 : TERM    # PROPOSED: S1
    TERM help_request(activity=inability_2) -> help_request_3 : TERM  # PROPOSED: S2
    UTTER ask(target=help_request_3)
  }
  TURN t2 SPEAKER=AGENT {
    TERM offer_help() -> offer_help_4 : TERM
    UTTER offer(target=offer_help_4)
    UTTER ask(target="Which game you’re playing (title, platform, etc.)")
    UTTER ask(target="What specific part or level you’re stuck on (e.g., a boss fight, puzzle, quest, achievement)")
    UTTER ask(target="Any error messages, glitches, or unusual behavior you’ve noticed")
    CLAIM enables(condition=help_request_3, outcome=offer_help_4) BY role_agent STATUS asserted SOURCE "t2:s10" -> enables_5 : CLAIM
    UTTER express_interest(target="user response")
  }
}
```

## Needs coverage

| need | kind        | expressed by                         | status    |
|------|-------------|--------------------------------------|-----------|
| n1   | claim       | inability_2                          | proposed  |
| n2   | speech_act  | ask, help_request_3                  | proposed  |
| n3   | object      | object_label::game                   | covered   |
| n4   | speech_act  | offer, offer_help_4                  | covered   |
| n5   | action      | help_request_3                       | proposed  |
| n6   | speech_act  | ask                                  | covered   |
| n7   | object      | "Which game you’re playing..."      | covered   |
| n8   | object      | "What specific part or level..."    | covered   |
| n9   | object      | "Any error messages..."             | covered   |
| n10  | object      | "Any error messages..."             | covered   |
| n11  | reasoning   | enables_5                            | covered   |
| n12  | speech_act  | express_interest                     | covered   |

## Why the translation failed

- n1 “User is failing to complete a specific video game”: no existing constructor for expressing inability of a user activity.
- n2 “User asks the assistant for help completing a game” & n5 “Help the user overcome a difficult part in a game”: no constructor wrapping an underlying activity into a help request.

## Translation report

- Input kind: conversation  
- Coverage status: partial  
- Source-span coverage: all turns t1:s1–t2:s11 represented; n1, n2, n5 unresolved.  
- Opaque-text spans: none  
- Label-preserved spans: none  
- Missing constructs: S1 inability, S2 help_request  
- Unresolved ambiguities: none  
- Check: `rag check` reported 2 unresolved needs (n1, n2, n5), 2 unknown symbols (inability, help_request)