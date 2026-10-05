Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    UTTER ask(target="i am failing to complete a certain game, can you help me?")
  }
  TURN t2 SPEAKER=AGENT {
    UTTER respond(target="Sure thing!")
    UTTER offer(target="I’d love to help you get past the tricky part.")
    UTTER ask(target="Could you let me know:")
    UTTER ask(target="Which game you’re playing (title, platform, etc.)")
    UTTER ask(target="What specific part or level you’re stuck on (e.g., a boss fight, puzzle, quest, achievement)")
    UTTER ask(target="Any error messages, glitches, or unusual behavior you’ve noticed")
    UTTER express_interest(target="Looking forward to hearing more!")
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | claim | — | unresolved |
| n2 | speech_act | ask | covered |
| n3 | object | "game" (in string) | label-preserved |
| n4 | speech_act | respond | covered |
| n5 | action | offer | covered |
| n6 | speech_act | ask | covered |
| n7 | object | "Which game ..." (in string) | covered |
| n8 | object | "Which game ..." (in string) | covered |
| n9 | object | "What specific part ..." (in string) | covered |
| n10 | object | "Any error messages ..." (in string) | covered |
| n11 | reasoning | "better I can tailor a solution" (in string) | covered |
| n12 | speech_act | express_interest | covered |

## Why the translation failed

- n1 "User is failing to complete a specific video game": no existing claim relation expresses inability to complete an activity. 

## Translation report

- Input kind: conversation
- Coverage status: partial (1 unresolved need)
- Source-span coverage: all spans preserved as string literals except the failure claim in t1:s1
- Opaque-text spans: t1:s1 "i am failing to complete a certain game, can you help me?"; t2:s2 "I’d love to help you get past the tricky part."; t2:s10 "The more details you give, the better I can tailor a solution for you."
- Label-preserved spans: n3 object "game"
- Missing constructs: inability_to_complete claim relation
- Unresolved ambiguities: none
- Check: `rag check` reported 1 unresolved need (n1), 0 unknown symbols
