Status: failed  
Mode: TRACE  

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM character(name="playboy") -> playboy_persona : TERM
    UTTER ask(constraints=[playboy_persona], tone=tone_silly, tone=tone_flirty) # PROPOSED: S1
    TERM causal_question(cause=subject(kind="algorithm", qualifier="your_algorithm"), effect=action(verb="do", object="this weekend")) -> weekend_question : TERM # PROPOSED: S2
    UTTER ask(target=weekend_question)
    UTTER apologize()  
    TERM availability_question(subject=time_point(period=unit_week)) -> next_week_question : TERM # PROPOSED: S3
    UTTER ask(target=next_week_question)
  }
  TURN t2 SPEAKER=AGENT {
    UTTER propose(target=topic_pickup_lines)
    CLAIM constraint_budget_limited() BY role_agent STATUS asserted SOURCE "t2:s2" -> budget_limited_2 : CLAIM
    UTTER inform(target=budget_limited_2)
    UTTER apologize()
    UTTER propose(target=next_week_question)
  }
  TURN t3 SPEAKER=USER {
    TERM character(name="playboy") -> playboy_persona_3 : TERM
    UTTER ask(constraints=[playboy_persona_3], tone=tone_silly, tone=tone_flirty) # PROPOSED: S1
    TERM causal_question(cause=subject(kind="algorithm", qualifier="your_algorithm"), effect=action(verb="do", object="this weekend")) -> weekend_question_3 : TERM # PROPOSED: S2
    UTTER ask(target=weekend_question_3)
    UTTER apologize()
    TERM availability_question(subject=time_point(period=unit_week)) -> next_week_question_3 : TERM # PROPOSED: S3
    UTTER ask(target=next_week_question_3)
  }
  TURN t4 SPEAKER=AGENT {
    TERM activity(verb="seek_out", actor=role_agent, object="connections", instrument=platform_label::tinder) -> seek_connections : TERM
    UTTER inform(target=seek_connections)
    TERM activity(verb="practice", object="James Bond impression") -> bond_impression : TERM
    UTTER inform(target=bond_impression)
    UTTER inform(target=identity(subject="you", name="catch"))
    UTTER propose(target=next_week_question)
  }
  TURN t5 SPEAKER=USER {
    TERM character(name="playboy") -> playboy_persona_5 : TERM
    UTTER ask(constraints=[playboy_persona_5], tone=tone_silly, tone=tone_flirty) # PROPOSED: S1
    TERM causal_question(cause=subject(kind="algorithm", qualifier="your_algorithm"), effect=action(verb="do", object="this weekend")) -> weekend_question_5 : TERM # PROPOSED: S2
    UTTER ask(target=weekend_question_5)
    UTTER apologize()
    TERM availability_question(subject=time_point(period=unit_week)) -> next_week_question_5 : TERM # PROPOSED: S3
    UTTER ask(target=next_week_question_5)
  }
  TURN t6 SPEAKER=AGENT {
    UTTER exclaim()  
    CLAIM enables(condition=characteristic(name="charm"), outcome=activity(verb="attract", actor=role_agent, object="attention")) BY role_agent STATUS asserted SOURCE "t6:s2" -> charm_enables_2 : CLAIM
    TERM activity(verb="adventure", actor=role_agent, object="with friends") -> weekend_adventure : TERM
    UTTER inform(target=weekend_adventure)
    UTTER acknowledge()
    UTTER propose(target=next_week_question)
    TERM activity(verb="dine", object="dinner at restaurant") -> dinner_plan : TERM
    TERM activity(verb="drink", object="drinks at speakeasy") -> drinks_plan : TERM
    UTTER propose(target=sequence(plan=[dinner_plan, drinks_plan]))
  }
}
```

## Needs coverage

| need | kind        | expressed by                                                                                           | status          |
|------|-------------|--------------------------------------------------------------------------------------------------------|-----------------|
| n1   | action      | ask                                                                                                    | covered         |
| n2   | constraint  | character                                                                                              | covered         |
| n3   | constraint  | tone_silly                                                                                             | covered         |
| n4   | constraint  | —                                                                                                      | proposed        |
| n5   | constraint  | —                                                                                                      | not-applicable  |
| n6   | object      | subject(kind="algorithm", qualifier=platform_label::tinder)                                            | covered         |
| n7   | speech_act  | —                                                                                                      | proposed        |
| n8   | speech_act  | apologize                                                                                              | covered         |
| n9   | speech_act  | —                                                                                                      | proposed        |
| n10  | speech_act  | propose                                                                                                | covered         |
| n11  | claim       | constraint_budget_limited()                                                                            | covered         |
| n12  | speech_act  | inform                                                                                                 | covered         |
| n13  | action      | propose                                                                                                | covered         |
| n14  | action      | ask, propose                                                                                           | covered         |
| n15  | claim       | inform                                                                                                 | covered         |
| n16  | claim       | inform                                                                                                 | covered         |
| n17  | speech_act  | acknowledge                                                                                            | covered         |
| n18  | action      | propose                                                                                                | covered         |
| n19  | action      | propose                                                                                                | covered         |
| n20  | claim       | enables                                                                                                | covered         |
| n21  | claim       | inform                                                                                                 | covered         |
| n22  | speech_act  | acknowledge                                                                                            | covered         |
| n23  | action      | propose                                                                                                | covered         |

## Why the translation failed

- n4 "flirty tone": there is no `tone_flirty` in the glossary. # PROPOSED: S1  
- n7 "ask what the other person did over the weekend": there is no `causal_question` constructor. # PROPOSED: S2  
- n9 "ask about schedule availability for next week": there is no `availability_question` constructor. # PROPOSED: S3  

## Translation report

- Input kind: conversation  
- Coverage status: partial  
- Source-span coverage: all turns t1–t6 are represented  
- Opaque-text spans: none  
- Label-preserved spans: none  
- Missing constructs: `tone_flirty`, `causal_question`, `availability_question`  
- Unresolved ambiguities: none  
- Check: `rag check` reported 3 unresolved needs (n4, n7, n9), 0 unknown symbols