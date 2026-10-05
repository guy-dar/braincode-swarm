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
    TERM dialogue(style=style_narrative) -> dialogue_2 : TERM
    TERM interpersonal_stance(target=role_friend, actor=role_user, stance="friendship") -> interpersonal_stance_2 : TERM
    TERM exclude(item=style_narrative) -> exclude_2 : TERM
    TERM character_trait(property="height", value=size_tall) -> character_trait_2 : TERM
    UTTER propose(target=dialogue_2, constraints=[character_trait_2, exclude_2, interpersonal_stance_2], tone=tone_casual)
  }
  TURN t4 SPEAKER=AGENT {
    TERM character_trait(property="height", value="5'5\"") -> character_trait_2 : TERM
    UTTER respond(target=character_trait_2, tone=tone_casual)
    TERM subject(kind="online_friendships") -> subject_2 : TERM
    UTTER ask(target=subject_2)
  }
  TURN t5 SPEAKER=USER {
    TERM dialogue(style=style_narrative) -> dialogue_2 : TERM
    TERM exclude(item="online_mention") -> exclude_2 : TERM
    TERM character_trait(property="height", value="6'5\"") -> character_trait_2 : TERM
    UTTER propose(target=dialogue_2, constraints=[character_trait_2, exclude_2], tone=tone_casual)
  }
  TURN t6 SPEAKER=AGENT {
    TERM character_trait(property="height", value=size_tall) -> character_trait_2 : TERM
    UTTER respond(target=character_trait_2, tone=tone_casual)
    TERM subject(kind="height_advantage") -> subject_2 : TERM
    UTTER ask(target=subject_2)
  }
  TURN t7 SPEAKER=USER {
    TERM dialogue(style=style_narrative) -> dialogue_2 : TERM
    TERM interpersonal_stance(target=role_user, actor=role_friend, stance="romantic_interest") -> interpersonal_stance_2 : TERM
    TERM character_trait(property="gender", value="female") -> character_trait_2 : TERM
    UTTER propose(target=dialogue_2, constraints=[character_trait_2, interpersonal_stance_2], tone=tone_casual)
  }
  TURN t8 SPEAKER=AGENT {
    TERM character_trait(property="height_difference", value=size_tall) -> character_trait_2 : TERM
    UTTER respond(target=character_trait_2, tone=tone_silly)
    TERM subject(kind="tall_people") -> subject_2 : TERM
    UTTER ask(target=subject_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | greeting, role_agent, acknowledge | covered |
| n2 | speech_act | greeting, role_user, acknowledge | covered |
| n3 | speech_act | offer_help, offer | covered |
| n4 | action | dialogue, propose, style_narrative | covered |
| n5 | object | interpersonal_stance, role_friend | covered |
| n6 | constraint | interpersonal_stance, role_friend | covered |
| n7 | negation | exclude, style_narrative | covered |
| n8 | constraint | propose, dialogue | covered |
| n9 | constraint | tone_casual | covered |
| n10 | constraint | character_trait, size_tall | covered |
| n11 | speech_act | respond, tone_casual, ask, subject | covered |
| n12 | action | dialogue, propose, style_narrative | covered |
| n13 | negation | exclude | covered |
| n14 | constraint | character_trait | covered |
| n15 | speech_act | respond, character_trait, size_tall, tone_casual, ask, subject | covered |
| n16 | action | dialogue, propose, style_narrative | covered |
| n17 | constraint | interpersonal_stance, character_trait, role_friend, role_user | covered |
| n18 | speech_act | respond, character_trait, size_tall, tone_silly, ask, subject | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t8:s6 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
