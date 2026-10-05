Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(actor=role_user, object=object_label::game, verb="complete") -> activity_2 : TERM
    CLAIM fails_to(activity=activity_2, actor=role_user) BY role_user STATUS asserted SOURCE "t1:s1" -> fails_to_2 : CLAIM   # PROPOSED: S1
    UTTER inform(target=fails_to_2)
    TERM activity(actor=role_agent, object=role_user, purpose=activity_2, verb="help") -> activity_3 : TERM
    UTTER ask(target=activity_3)
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM offer_help() -> offer_help_2 : TERM
    UTTER offer(target=offer_help_2)
    TERM activity(actor=role_agent, object=role_user, purpose=activity_2, verb="help") -> activity_4 : TERM
    UTTER offer(target=activity_4)
    TERM subject(kind="game_title_and_platform") -> subject_2 : TERM
    UTTER ask(target=subject_2)
    TERM subject(kind="stuck_level_boss_puzzle_quest_or_achievement") -> subject_3 : TERM
    UTTER ask(target=subject_3)
    TERM subject(kind="error_messages_glitches_or_unusual_behavior") -> subject_4 : TERM
    UTTER ask(target=subject_4)
    TERM activity(actor=role_user, verb="provide_details") -> activity_5 : TERM
    TERM activity(actor=role_agent, object=role_user, verb="tailor_solution") -> activity_6 : TERM
    CLAIM enables(condition=activity_5, outcome=activity_6) BY role_agent STATUS asserted SOURCE "t2:s10" -> enables_2 : CLAIM
    UTTER inform(target=enables_2)
    TERM activity(actor=role_agent, object=role_user, verb="hear") -> activity_7 : TERM
    UTTER express_interest(target=activity_7)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | claim | fails_to (PROPOSED: S1), activity | proposed |
| n2 | speech_act | ask, activity | covered |
| n3 | object | object_label::game | label-preserved |
| n4 | speech_act | offer, offer_help | covered |
| n5 | action | activity, offer | covered |
| n6 | speech_act | ask, subject | covered |
| n7 | object | subject | covered |
| n8 | object | subject | covered |
| n9 | object | subject | covered |
| n10 | object | subject | covered |
| n11 | reasoning | enables, activity, inform | covered |
| n12 | speech_act | express_interest, activity | covered |

## Why the translation failed

- n1 "user is failing to complete a game": candidates failure (system: STRING/platform_label; a system failing, not a person failing at a task), outcome (needs an EVENT), user_practice (habitual practice). No claim relation for an actor failing/unable to do an activity. Proposed S1.

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: all of t1:s1–t2:s11 represented; t2:s4/s6/s8 list numerals and t2:s1 "Sure thing" (confirmation, folded into offer) not separately encoded
- Opaque-text spans: none
- Label-preserved spans: t1:s1 "game" → object_label::game (label only)
- Missing constructs: S1 fails_to claim relation; subject(kind=...) strings used for game title/platform/level/errors are descriptive labels, weakly structured
- Unresolved ambiguities: t2:s1 "Sure thing" has no CLAIM to confirm; encoded as offer
- Check: see host check
