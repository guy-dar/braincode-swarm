Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(verb="complete", actor=role_user, object="game") -> complete_game : TERM
    TERM offer_help() -> help_offer : TERM
    UTTER ask(target=help_offer)
  }
  TURN t2 SPEAKER=AGENT {
    TERM offer_help() -> help_offer_2 : TERM
    UTTER offer(target=help_offer_2)
    TERM subject(kind="game") -> game_subject : TERM
    TERM subject(kind="platform") -> platform_subject : TERM
    TERM subject(kind="level", qualifier="stuck on") -> stuck_level : TERM
    TERM subject(kind="error") -> error_subject : TERM
    TERM conjunction(items=[game_subject, platform_subject, stuck_level, error_subject]) -> game_troubleshoot_info : TERM
    UTTER ask(target=game_troubleshoot_info)
    TERM activity(verb="provide", actor=role_user, object="details") -> provide_details : TERM
    TERM activity(verb="tailor", actor=role_agent, object="solution") -> tailored_solution : TERM
    CLAIM enables(condition=provide_details, outcome=tailored_solution) BY role_agent STATUS asserted SOURCE "t2:s10" -> enables_claim : CLAIM
    UTTER express_interest(target=provide_details)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | claim | complete_game activity, ask speech act | covered |
| n2 | speech_act | ask speech act, help_offer TERM | covered |
| n3 | object | complete_game activity (object="game") | covered |
| n4 | speech_act | offer speech act | covered |
| n5 | action | offer speech act | covered |
| n6 | speech_act | ask speech act (game_troubleshoot_info target) | covered |
| n7 | object | game_subject term | covered |
| n8 | object | platform_subject term | covered |
| n9 | object | stuck_level term | covered |
| n10 | object | error_subject term | covered |
| n11 | reasoning | enables claim | covered |
| n12 | speech_act | express_interest speech act | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: all segments t1:s1, t2:s1–t2:s11 are represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reports 0 unresolved needs and 0 unknown symbols
