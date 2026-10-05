Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM aesthetic(period="medieval", style=style_narrative) -> aesthetic_2 : TERM
    TERM activity(object=art_story, purpose=aesthetic_2, verb="write") -> activity_2 : TERM
    UTTER propose(target=activity_2)
  }
  TURN t2 SPEAKER=AGENT {
    CLAIM provides(actor=role_agent, subject=art_story) BY role_agent STATUS asserted SOURCE "t2:s1" -> provides_2 : CLAIM
    UTTER inform(target=provides_2)
    TERM activity(actor="Dreamcrafters", object="dreams", verb="manipulate") -> activity_3 : TERM
    CLAIM statement(fact=activity_3) BY role_agent STATUS reported SOURCE "t2:s3" -> statement_2 : CLAIM
    TERM character(name="Johnathon Wyrd") -> character_2 : TERM
    TERM character(name="Lady Elyria") -> character_3 : TERM
    CLAIM statement(fact=character_2) BY role_agent STATUS reported SOURCE "t2:s5" -> statement_3 : CLAIM
    TERM character(name="Lord Amandus") -> character_4 : TERM
    TERM character(name="Prince Emory") -> character_5 : TERM
    TERM activity(actor="Johnathon Wyrd", object="idea", purpose=character_5, verb="plant") -> activity_4 : TERM
    TERM obligation(activity=activity_4, actor="Johnathon Wyrd") -> obligation_2 : TERM
    CLAIM statement(fact=obligation_2) BY role_agent STATUS reported SOURCE "t2:s9" -> statement_4 : CLAIM
    TERM character(name="Elara") -> character_6 : TERM
    TERM character(name="Silas") -> character_7 : TERM
    TERM character(name="Caelum") -> character_8 : TERM
    TERM conjunction(items=[character_6, character_7, character_8]) -> conjunction_2 : TERM
    CLAIM statement(fact=conjunction_2) BY role_agent STATUS reported SOURCE "t2:s10" -> statement_5 : CLAIM
    TERM activity(actor="group", location="dreams", verb="infiltrate") -> activity_5 : TERM
    TERM self_protection(actor="Prince Emory", domain="subconscious") -> self_protection_2 : TERM
    TERM temporal_context(activity=activity_5) -> temporal_context_2 : TERM
    CLAIM statement(fact=temporal_context_2) BY role_agent STATUS reported SOURCE "t2:s12" -> statement_6 : CLAIM
    TERM activity(actor="Johnathon Wyrd", object="inception", verb="complete") -> activity_6 : TERM
    TERM decision(activity=activity_6) -> decision_2 : TERM
    CLAIM statement(fact=decision_2) BY role_agent STATUS reported SOURCE "t2:s16" -> statement_7 : CLAIM
  }
  TURN t3 SPEAKER=USER {
    TERM substitute(original="medieval", replacement=cat_game) -> substitute_2 : TERM
    TERM activity(object=art_story, purpose=substitute_2, verb="rewrite") -> activity_2 : TERM
    UTTER propose(target=activity_2)
  }
  TURN t4 SPEAKER=AGENT {
    CLAIM provides(actor=role_agent, subject=art_story) BY role_agent STATUS asserted SOURCE "t4:s1" -> provides_2 : CLAIM
    UTTER inform(target=provides_2)
    CLAIM opposes(actor="Dreamhackers", subject="Combine") BY role_agent STATUS reported SOURCE "t4:s4" -> opposes_2 : CLAIM
    TERM character(name="Gordon Freeman") -> character_2 : TERM
    TERM character(name="Alyx Vance") -> character_3 : TERM
    CLAIM statement(fact=character_2) BY role_agent STATUS reported SOURCE "t4:s5" -> statement_2 : CLAIM
    TERM character(name="Isaac Kleiner") -> character_4 : TERM
    TERM character(name="Wallace Breen") -> character_5 : TERM
    TERM activity(actor="Gordon Freeman", object="idea", purpose=character_5, verb="plant") -> activity_3 : TERM
    CLAIM has_goal(goal=activity_3, subject="Gordon Freeman") BY role_agent STATUS reported SOURCE "t4:s9" -> has_goal_2 : CLAIM
    TERM character(name="Barney Calhoun") -> character_6 : TERM
    TERM character(name="Dog") -> character_7 : TERM
    TERM character(name="Judith Mossman") -> character_8 : TERM
    TERM conjunction(items=[character_6, character_7, character_8]) -> conjunction_2 : TERM
    CLAIM statement(fact=conjunction_2) BY role_agent STATUS reported SOURCE "t4:s10" -> statement_3 : CLAIM
    TERM activity(actor="group", location="subconscious", verb="delve") -> activity_4 : TERM
    TERM temporal_context(activity=activity_4) -> temporal_context_2 : TERM
    CLAIM statement(fact=temporal_context_2) BY role_agent STATUS reported SOURCE "t4:s12" -> statement_4 : CLAIM
    TERM activity(actor="Gordon Freeman", object="inception", verb="complete") -> activity_5 : TERM
    TERM time_horizon(horizon="future") -> time_horizon_2 : TERM
    CLAIM enables(condition=activity_5, outcome=time_horizon_2) BY role_agent STATUS reported SOURCE "t4:s16" -> enables_2 : CLAIM
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | propose, activity, art_story | covered |
| n2 | constraint | aesthetic, style_narrative | covered |
| n3 | speech_act | provides, inform, role_agent, art_story | covered |
| n4 | object | activity, statement | covered |
| n5 | object | character, statement | covered |
| n6 | action | obligation, activity, character, statement | covered |
| n7 | object | character, conjunction, statement | covered |
| n8 | action | temporal_context, self_protection, activity, statement | covered |
| n9 | action | decision, activity, statement | covered |
| n10 | action | propose, activity, art_story | covered |
| n11 | constraint | substitute, cat_game | covered |
| n12 | speech_act | provides, inform, role_agent, art_story | covered |
| n13 | object | opposes | covered |
| n14 | object | character, statement | covered |
| n15 | action | has_goal, activity, character | covered |
| n16 | object | character, conjunction, statement | covered |
| n17 | action | temporal_context, activity, statement | covered |
| n18 | action | enables, time_horizon, activity | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t4:s17 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
