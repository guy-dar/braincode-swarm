Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    CLAIM failure(system="game") BY role_user STATUS asserted SOURCE "t1:s1" -> failure_2 : CLAIM
    TERM offer_help() -> offer_help_2 : TERM
    UTTER ask(target=offer_help_2)
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM offer_help() -> offer_help_3 : TERM
    UTTER offer(target=offer_help_3)
    
    UTTER ask(topic="Which game are you playing (title and platform)")
    UTTER ask(topic="What specific level, boss, puzzle, quest, or achievement are you stuck on")
    UTTER ask(topic="Any error messages, glitches, or unusual behavior you have noticed")
    
    TERM activity(verb="provide details about the problem", actor=role_user) -> details_activity : TERM
    TERM activity(verb="create a tailored solution", actor=role_agent) -> solution_activity : TERM
    CLAIM enables(condition=details_activity, outcome=solution_activity) BY role_agent STATUS asserted SOURCE "t2:s10" -> enables_2 : CLAIM
    UTTER inform(target=enables_2)
    
    TERM activity(verb="share more information", actor=role_user) -> sharing_activity : TERM
    UTTER express_interest(target=sharing_activity)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | claim | failure | covered |
| n2 | speech_act | ask, offer_help | covered |
| n3 | object | ask | covered |
| n4 | speech_act | offer, offer_help | covered |
| n5 | action | offer_help | covered |
| n6 | speech_act | ask, express_interest | covered |
| n7 | object | activity | covered |
| n8 | object | activity | covered |
| n9 | object | activity | covered |
| n10 | object | failure | covered |
| n11 | reasoning | enables | covered |
| n12 | speech_act | express_interest | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: t1:s1 and t2:s1–t2:s11 all represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none (the source intentionally does not specify the game name or platform until the agent asks; this is preserved)
- Check: `node /kit/rag.mjs check --translation /output/translation.md` reports all 12 needs covered, 0 unknown symbols
