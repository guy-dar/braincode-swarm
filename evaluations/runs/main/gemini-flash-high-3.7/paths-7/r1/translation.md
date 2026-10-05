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
  TURN t2 SPEAKER=AGENT {
    TERM greeting(recipient=role_user) -> greeting_2 : TERM
    UTTER acknowledge(target=greeting_2)
    TERM offer_help() -> offer_help_2 : TERM
    UTTER offer(target=offer_help_2)
  }
  TURN t3 SPEAKER=USER {
    TERM interpersonal_stance(target=role_user, actor=role_friend, stance="friendship") -> interpersonal_stance_2 : TERM
    TERM exclude(item=style_narrative) -> exclude_2 : TERM
    TERM requirement(property="setting", value="online") -> requirement_2 : TERM
    TERM requirement(property="perspective", value="second_person") -> requirement_3 : TERM
    TERM character_trait(property="height", value=size_tall) -> character_trait_2 : TERM
    TERM dialogue(style=tone_casual) -> dialogue_2 : TERM
    UTTER propose(target=dialogue_2, constraints=[interpersonal_stance_2, exclude_2, requirement_2, requirement_3, character_trait_2], tone=tone_casual)
  }
  TURN t4 SPEAKER=AGENT {
    TERM character_trait(property="height", value=size_tall) -> character_trait_2 : TERM
    UTTER respond(target=character_trait_2, tone=tone_casual)
    TERM subject(kind="friendship", qualifier="online") -> subject_2 : TERM
    UTTER ask(target=subject_2, tone=tone_casual)
  }
  TURN t5 SPEAKER=USER {
    TERM exclude(item="online") -> exclude_2 : TERM
    TERM character_trait(property="height", value="6'5\"") -> character_trait_2 : TERM
    TERM character_trait(property="partner_height", value="5'5\"") -> character_trait_3 : TERM
    TERM dialogue(style=tone_casual) -> dialogue_2 : TERM
    UTTER propose(target=dialogue_2, constraints=[exclude_2, character_trait_2, character_trait_3], tone=tone_casual)
  }
  TURN t6 SPEAKER=AGENT {
    TERM character_trait(property="height", value=size_tall) -> character_trait_2 : TERM
    UTTER respond(target=character_trait_2, tone=tone_casual)
    TERM subject(kind="height_advantage") -> subject_2 : TERM
    UTTER ask(target=subject_2, tone=tone_casual)
  }
  TURN t7 SPEAKER=USER {
    TERM char_female() -> char_female_2 : TERM
    TERM interpersonal_stance(target=role_agent, actor=role_friend, stance="romantic_interest") -> interpersonal_stance_2 : TERM
    TERM dialogue(style=tone_casual) -> dialogue_2 : TERM
    UTTER propose(target=dialogue_2, constraints=[char_female_2, interpersonal_stance_2], tone=tone_casual)
  }
  TURN t8 SPEAKER=AGENT {
    TERM character_trait(property="height", value=size_tall) -> character_trait_2 : TERM
    UTTER respond(target=character_trait_2, tone=tone_silly)
    TERM subject(kind="tall_people") -> subject_2 : TERM
    UTTER ask(target=subject_2, tone=tone_silly)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | greeting, role_agent, acknowledge | covered |
| n2 | speech_act | greeting, role_user, acknowledge | covered |
| n3 | speech_act | offer_help, offer | covered |
| n4 | action | dialogue, propose, tone_casual | covered |
| n5 | object | interpersonal_stance, role_friend, role_user | covered |
| n6 | constraint | dialogue, requirement, role_friend | covered |
| n7 | negation | exclude, style_narrative | covered |
| n8 | constraint | requirement, dialogue, respond | covered |
| n9 | constraint | tone_casual, dialogue | covered |
| n10 | constraint | character_trait, size_tall | covered |
| n11 | speech_act | respond, ask, tone_casual, size_tall | covered |
| n12 | action | dialogue, propose, tone_casual | covered |
| n13 | negation | exclude, dialogue | covered |
| n14 | constraint | character_trait, size_tall | covered |
| n15 | speech_act | respond, ask, tone_casual, size_tall, character_trait | covered |
| n16 | action | dialogue, propose, interpersonal_stance | covered |
| n17 | constraint | char_female, interpersonal_stance, role_friend, role_agent | covered |
| n18 | speech_act | respond, ask, tone_silly, size_tall | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t8:s6 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
