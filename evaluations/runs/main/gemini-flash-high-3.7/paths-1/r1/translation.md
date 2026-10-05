Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM character(name="playboy") -> character_2 : TERM
    TERM dialogue(style=style_catchy) -> dialogue_2 : TERM
    TERM dialogue(style=style_academic) -> dialogue_3 : TERM
    UTTER respond(constraints=[character_2, dialogue_2, dialogue_3], tone=tone_silly)
    CLAIM failure(system=platform_label::tinder) BY role_user STATUS reported SOURCE "t1:s3" -> failure_2 : CLAIM
    TERM activity(verb="weekend_activity") -> activity_2 : TERM
    UTTER ask(target=activity_2)
    UTTER apologize()
    TERM duration(amount=1, unit=unit_week) -> duration_2 : TERM
    UTTER ask(target=duration_2)
  }
  TURN t2 SPEAKER=AGENT {
    UTTER respond(tone=tone_silly, topic=topic_pickup_lines)
    TERM constraint_budget_limited() -> constraint_budget_limited_2 : TERM
    CLAIM statement(fact=constraint_budget_limited_2) BY role_agent STATUS asserted SOURCE "t2:s2" -> statement_2 : CLAIM
    UTTER acknowledge(target=statement_2)
    TERM duration(amount=1, unit=unit_week) -> duration_3 : TERM
    TERM activity(purpose=duration_3, verb="plan_date") -> activity_3 : TERM
    UTTER propose(target=activity_3)
  }
  TURN t3 SPEAKER=USER {
    UTTER respond(constraints=[t1.character_2, t1.dialogue_2, t1.dialogue_3], tone=tone_silly)
  }
  TURN t4 SPEAKER=AGENT {
    TERM character(name="James Bond") -> character_3 : TERM
    TERM activity(actor=role_agent, object=character_3, verb="practice_impression") -> activity_4 : TERM
    CLAIM user_practice(activity=activity_4) BY role_agent STATUS asserted SOURCE "t4:s2" -> user_practice_2 : CLAIM
    CLAIM attitude(target=role_user, holder=role_agent, type="wit_and_charm") BY role_agent STATUS asserted SOURCE "t4:s3" -> attitude_2 : CLAIM
    UTTER acknowledge(tone=tone_silly)
    TERM activity(object=wine, verb="wine_tasting") -> activity_5 : TERM
    TERM duration(amount=1, unit=unit_week) -> duration_4 : TERM
    UTTER propose(target=activity_5)
  }
  TURN t5 SPEAKER=USER {
    UTTER respond(constraints=[t1.character_2, t1.dialogue_2, t1.dialogue_3], tone=tone_silly)
  }
  TURN t6 SPEAKER=AGENT {
    TERM activity(actor=role_agent, object=gender_women, verb="attract_attention") -> activity_6 : TERM
    CLAIM user_practice(activity=activity_6) BY role_agent STATUS asserted SOURCE "t6:s2" -> user_practice_3 : CLAIM
    TERM activity(actor=role_friend, verb="adventure") -> activity_7 : TERM
    CLAIM occurred(activity=activity_7) BY role_agent STATUS asserted SOURCE "t6:s3" -> occurred_2 : CLAIM
    CLAIM occurred_recently(target=occurred_2) BY role_agent STATUS asserted SOURCE "t6:s3" -> occurred_recently_2 : CLAIM
    UTTER acknowledge(target=role_agent)
    TERM activity(location=restaurant, object=entity_drinks, verb="dinner_and_drinks") -> activity_8 : TERM
    TERM duration(amount=1, unit=unit_week) -> duration_5 : TERM
    UTTER propose(target=activity_8)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | respond | covered |
| n2 | constraint | character | covered |
| n3 | constraint | tone_silly | covered |
| n4 | constraint | style_catchy | covered |
| n5 | constraint | style_academic | covered |
| n6 | object | platform_label::tinder | label-preserved |
| n7 | speech_act | ask, activity | covered |
| n8 | speech_act | apologize | covered |
| n9 | speech_act | ask, unit_week | covered |
| n10 | speech_act | topic_pickup_lines, tone_silly, respond | covered |
| n11 | claim | constraint_budget_limited, statement | covered |
| n12 | speech_act | acknowledge | covered |
| n13 | action | propose, unit_week | covered |
| n14 | action | respond, tone_silly | covered |
| n15 | claim | user_practice, character | covered |
| n16 | claim | attitude, role_user | covered |
| n17 | speech_act | acknowledge, tone_silly | covered |
| n18 | action | propose, wine, unit_week | covered |
| n19 | action | respond, tone_silly | covered |
| n20 | claim | user_practice, gender_women | covered |
| n21 | claim | occurred, occurred_recently, role_friend | covered |
| n22 | speech_act | acknowledge, role_agent | covered |
| n23 | action | propose, restaurant, entity_drinks, unit_week | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t6:s9 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s3 "Tinder" -> platform_label::tinder (open label only)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
