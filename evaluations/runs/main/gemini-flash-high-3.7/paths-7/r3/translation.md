Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM greeting(recipient=role_agent) -> greeting_2 : TERM
    UTTER offer(target=greeting_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM greeting(recipient=role_user) -> greeting_2 : TERM
    TERM offer_help() -> offer_help_2 : TERM
    UTTER respond(target=greeting_2)
    UTTER offer(target=offer_help_2)
  }
  TURN t3 SPEAKER=USER {
    TERM character_trait(property="height", value="5'5\"") -> character_trait_2 : TERM
    TERM dialogue(style="conversational") -> dialogue_2 : TERM
    TERM exclude(item=style_narrative) -> exclude_2 : TERM
    TERM interpersonal_stance(actor=role_user, stance="friendship") -> interpersonal_stance_2 : TERM
    TERM requirement(property="tone", value=tone_casual) -> requirement_2 : TERM
    UTTER ask(target=dialogue_2, constraints=[character_trait_2, exclude_2, requirement_2], tone=tone_casual, topic=art_story)
  }
  TURN t4 SPEAKER=AGENT {
    TERM character_trait(property="height", value="5'5\"") -> character_trait_2 : TERM
    TERM interpersonal_stance(actor=role_user, stance="friendship") -> interpersonal_stance_2 : TERM
    UTTER respond(target=character_trait_2, tone=tone_casual, topic=role_friend)
    UTTER ask(target=interpersonal_stance_2, tone=tone_casual)
  }
  TURN t5 SPEAKER=USER {
    TERM character_trait(property="height", value="6'5\"") -> character_trait_2 : TERM
    TERM exclude(item="online_setting") -> exclude_2 : TERM
    UTTER ask(target=t3.dialogue_2, constraints=[character_trait_2, exclude_2], tone=tone_casual)
  }
  TURN t6 SPEAKER=AGENT {
    TERM character_trait(property="height", value="6'5\"") -> character_trait_2 : TERM
    UTTER respond(target=character_trait_2, tone=tone_casual)
    UTTER ask(tone=tone_casual, topic="height_advantages")
  }
  TURN t7 SPEAKER=USER {
    TERM char_female() -> char_female_2 : TERM
    TERM interpersonal_stance(target=role_agent, actor="girl", stance="romantic_interest") -> interpersonal_stance_2 : TERM
    UTTER ask(target=t3.dialogue_2, constraints=[char_female_2, interpersonal_stance_2], tone=tone_casual)
  }
  TURN t8 SPEAKER=AGENT {
    TERM character_trait(property="height", value=size_tall) -> character_trait_2 : TERM
    UTTER respond(target=character_trait_2, tone=tone_silly)
    UTTER ask(tone=tone_silly, topic="tall_people")
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | greeting, role_agent, offer | covered |
| n2 | speech_act | greeting, role_user, respond | covered |
| n3 | speech_act | offer_help, offer | covered |
| n4 | action | dialogue, art_story, ask | covered |
| n5 | object | interpersonal_stance, role_friend | covered |
| n6 | constraint | dialogue, interpersonal_stance | covered |
| n7 | negation | exclude, style_narrative | covered |
| n8 | constraint | dialogue, requirement | covered |
| n9 | constraint | requirement, tone_casual | covered |
| n10 | constraint | character_trait | covered |
| n11 | speech_act | respond, character_trait, ask, interpersonal_stance, tone_casual, role_friend | covered |
| n12 | action | dialogue, ask | covered |
| n13 | negation | exclude | covered |
| n14 | constraint | character_trait | covered |
| n15 | speech_act | respond, character_trait, ask, tone_casual | covered |
| n16 | action | dialogue, ask | covered |
| n17 | constraint | char_female, interpersonal_stance, role_agent | covered |
| n18 | speech_act | respond, character_trait, size_tall, ask, tone_silly | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t8:s6 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
