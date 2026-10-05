Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM greeting(recipient=role_agent) -> greeting_2 : TERM
    UTTER acknowledge(target=greeting_2)
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM greeting(recipient=role_user) -> greeting_2 : TERM
    UTTER acknowledge(target=greeting_2)
    TERM offer_help() -> offer_help_2 : TERM
    UTTER offer(target=offer_help_2)
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    TERM dialogue(style=style_narrative) -> dialogue_2 : TERM
    TERM exclude(item=style_narrative) -> exclude_2 : TERM
    TERM interpersonal_stance(target=role_friend, actor=role_friend, stance="online") -> interpersonal_stance_2 : TERM
    TERM character_trait(property="height", value=size_tall) -> character_trait_2 : TERM
    UTTER propose(target=dialogue_2, tone=tone_casual)
    UTTER respond(target=character_trait_2)
  }
  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    TERM character_trait(property="height", value=size_tall) -> character_trait_2 : TERM
    UTTER respond(target=character_trait_2, tone=tone_casual)
    UTTER ask(target=t3.interpersonal_stance_2)
  }
  TURN t5 SPEAKER=USER REPLY_TO t4 {
    TERM dialogue(style=style_narrative) -> dialogue_2 : TERM
    TERM exclude(item="online") -> exclude_2 : TERM
    TERM character_trait(property="height", value=size_tall) -> character_trait_2 : TERM
    UTTER propose(target=dialogue_2, tone=tone_casual)
    UTTER respond(target=character_trait_2)
  }
  TURN t6 SPEAKER=AGENT REPLY_TO t5 {
    TERM character_trait(property="height", value=size_tall) -> character_trait_2 : TERM
    UTTER respond(target=character_trait_2)
    UTTER ask(target=character_trait_2)
  }
  TURN t7 SPEAKER=USER REPLY_TO t6 {
    TERM dialogue(style=style_narrative) -> dialogue_2 : TERM
    TERM character(name="girl") -> character_2 : TERM
    TERM interpersonal_stance(target=role_agent, actor=character_2, stance="romantic_interest") -> interpersonal_stance_2 : TERM
    TERM character_trait(property="height", value=size_tall) -> character_trait_2 : TERM
    UTTER propose(target=dialogue_2, tone=tone_casual)
    UTTER respond(target=character_trait_2)
  }
  TURN t8 SPEAKER=AGENT REPLY_TO t7 {
    TERM character_trait(property="height", value=size_tall) -> character_trait_2 : TERM
    UTTER respond(target=character_trait_2, tone=tone_silly)
    UTTER ask(target=character_trait_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | greeting, role_agent, acknowledge | covered |
| n2 | speech_act | greeting, role_user, acknowledge | covered |
| n3 | speech_act | offer_help, offer | covered |
| n4 | action | dialogue, style_narrative, propose | covered |
| n5 | object | role_friend, interpersonal_stance | covered |
| n6 | constraint | interpersonal_stance | covered |
| n7 | negation | exclude, style_narrative | covered |
| n8 | constraint | respond | covered |
| n9 | constraint | tone_casual | covered |
| n10 | constraint | character_trait, respond, size_tall | covered |
| n11 | speech_act | ask, respond, size_tall, tone_casual | covered |
| n12 | action | dialogue, propose | covered |
| n13 | negation | exclude | covered |
| n14 | constraint | character_trait, size_tall | covered |
| n15 | speech_act | ask, character_trait, respond, size_tall | covered |
| n16 | action | dialogue, interpersonal_stance, propose | covered |
| n17 | constraint | character, interpersonal_stance | covered |
| n18 | speech_act | ask, character_trait, respond, size_tall, tone_silly | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t8:s6 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
