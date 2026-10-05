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
    TERM greeting(recipient=role_user) -> greeting_3 : TERM
    UTTER respond(target=greeting_3)
    TERM offer_help() -> offer_help_2 : TERM
    UTTER offer(target=offer_help_2)
  }
  TURN t3 SPEAKER=USER {
    TERM subject(kind=art_story) -> subject_2 : TERM
    TERM dialogue(style="online") -> dialogue_2 : TERM
    TERM interpersonal_stance(target=role_friend, actor=role_friend, stance="friendship") -> interpersonal_stance_2 : TERM
    TERM exclude(item=style_narrative) -> exclude_2 : TERM
    TERM character_trait(property="height", value=size_tall) -> character_trait_2 : TERM
    CLAIM request(target=dialogue_2) BY role_user STATUS asserted SOURCE "t3:s1" -> request_2 : CLAIM
    UTTER respond(target=character_trait_2, tone=tone_casual)
  }
  TURN t4 SPEAKER=AGENT {
    UTTER respond(target=character_trait_2, tone=tone_casual)
    UTTER ask(target=dialogue_2)
  }
  TURN t5 SPEAKER=USER {
    TERM dialogue(style="casual") -> dialogue_3 : TERM
    TERM exclude(item="online_setting") -> exclude_3 : TERM
    TERM character(name="speaker") -> character_2 : TERM
    TERM character_trait(property="height", value=size_tall) -> character_trait_3 : TERM
    CLAIM request(target=dialogue_3) BY role_user STATUS asserted SOURCE "t5:s1" -> request_3 : CLAIM
    UTTER respond(target=character_trait_3, tone=tone_casual)
  }
  TURN t6 SPEAKER=AGENT {
    UTTER respond(target=character_2, tone=tone_casual)
    UTTER ask(target=character_trait_3)
  }
  TURN t7 SPEAKER=USER {
    TERM dialogue(style="romantic") -> dialogue_4 : TERM
    TERM char_female() -> char_female_2 : TERM
    TERM interpersonal_stance(target=character_2, actor=char_female_2, stance="romantic_interest") -> interpersonal_stance_3 : TERM
    CLAIM request(target=dialogue_4) BY role_user STATUS asserted SOURCE "t7:s1" -> request_4 : CLAIM
    UTTER respond(target=interpersonal_stance_3, tone=tone_casual)
  }
  TURN t8 SPEAKER=AGENT {
    UTTER respond(target=interpersonal_stance_3, tone=tone_silly)
    UTTER ask(target=character_trait_3)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | acknowledge, greeting, role_agent | covered |
| n2 | speech_act | greeting, respond, role_user | covered |
| n3 | speech_act | offer, offer_help | covered |
| n4 | action | art_story, dialogue, request, subject | covered |
| n5 | object | art_story, interpersonal_stance, role_friend, subject | covered |
| n6 | constraint | dialogue | covered |
| n7 | negation | exclude, style_narrative | covered |
| n8 | constraint | respond | covered |
| n9 | constraint | tone_casual | covered |
| n10 | constraint | character_trait, respond, size_tall | covered |
| n11 | speech_act | ask, respond, size_tall, tone_casual | covered |
| n12 | action | dialogue, request | covered |
| n13 | negation | exclude | covered |
| n14 | constraint | character, character_trait, size_tall | covered |
| n15 | speech_act | ask, character, respond, size_tall | covered |
| n16 | action | character, dialogue, interpersonal_stance, request | covered |
| n17 | constraint | char_female, interpersonal_stance | covered |
| n18 | speech_act | ask, respond, size_tall, tone_silly | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t8:s6 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
