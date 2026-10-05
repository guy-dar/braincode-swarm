Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    UTTER ask(target=activity(verb="write", actor=role_user, object="plot", purpose=subject(kind="movie", qualifier=topic_baldurs_gate_3))) # PROPOSED: S1
  }
  TURN t2 SPEAKER=AGENT {
    UTTER provide(target=naming_pattern(description="Dreamcrafter", context="title")) # PROPOSED: S2
    UTTER provide(target=activity(verb="adapt", actor=role_agent, object=subject(kind="plot", qualifier=subject(kind="movie", qualifier=topic_baldurs_gate_3)), purpose=aesthetic(period="medieval", style="fantasy"))) # PROPOSED: S2
  }
  TURN t3 SPEAKER=USER {
    UTTER rewrite(target=subject(kind="story", qualifier=topic_spider_man_2)) # PROPOSED: S3
  }
  TURN t4 SPEAKER=AGENT {
    UTTER provide(target=naming_pattern(description="Dreamhacker", context="title")) # PROPOSED: S2
    UTTER provide(target=activity(verb="adapt", actor=role_agent, object=subject(kind="plot", qualifier=subject(kind="story", qualifier=topic_spider_man_2)), purpose=aesthetic(period="dystopian", style="narrative"))) # PROPOSED: S2
  }
}
```

## Needs coverage

| need | kind       | expressed by               | status     |
|------|------------|----------------------------|------------|
| n1   | action     | ask (target=activity)      | proposed   |
| n2   | constraint | aesthetic style=medieval   | unresolved |
| n3   | speech_act | provide                    | proposed   |
| n4   | object     | extract                    | covered    |
| n5   | object     | —                          | unresolved |
| n6   | action     | —                          | unresolved |
| n7   | object     | face                       | covered    |
| n8   | action     | —                          | unresolved |
| n9   | action     | extract                    | covered    |
| n10  | action     | rewrite                    | proposed   |
| n11  | constraint | on                         | covered    |
| n12  | speech_act | provide                    | proposed   |
| n13  | object     | —                          | unresolved |
| n14  | object     | —                          | unresolved |
| n15  | action     | —                          | unresolved |
| n16  | object     | —                          | unresolved |
| n17  | action     | —                          | unresolved |
| n18  | action     | —                          | unresolved |

## Why the translation failed

- n1: Missing speech_act `ask` for recording a user request.
- n2: No constructor or term covers setting a story in a medieval fantasy setting.
- n3: Missing speech_act `provide` for agent provision of content.
- n5, n6, n8, n13–n18: No constructors for protagonist description, hiring action, infiltration action, character profiles, or completion actions.
- n10: Missing speech_act `rewrite` for the user's request to rewrite the story.
- n12: Same missing `provide` for agent adaptation speech act.

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage:
  - t1:s1 recorded by `ask`
  - t2:s1 recorded by `provide`
  - t2:s2–s17 coverage not structured
  - t3:s1 recorded by `rewrite`
  - t4:s1 recorded by `provide`
- Opaque-text spans: t2:s2–s17, t4:s2–s17
- Label-preserved spans: none
- Missing constructs: ask (speech_act), provide (speech_act), rewrite (speech_act), plus multiple narrative constructors
- Unresolved ambiguities: none
- Check: `rag check` reported usage of non-glossary symbols ask, provide, rewrite; multiple unresolved needs
