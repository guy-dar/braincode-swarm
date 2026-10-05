Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM aesthetic(period="medieval", style="fantasy") -> aesthetic_2 : TERM
    TERM activity(object="Inception", verb="write") -> activity_2 : TERM
    UTTER propose(target=activity_2, constraints=[aesthetic_2])
  }
  TURN t2 SPEAKER=AGENT {
    CLAIM provides(actor=role_agent, subject=art_story) BY role_agent STATUS asserted SOURCE "t2:s1" -> provides_2 : CLAIM
    TERM activity(verb="extract_secrets_and_plant_ideas") -> activity_3 : TERM
    TERM activity(actor="Dreamcrafters", location="Aetheroth", purpose=activity_3, verb="manipulate_dreams") -> activity_4 : TERM
    TERM character(name="Johnathon Wyrd") -> character_2 : TERM
    TERM character(name="Lady Elyria") -> character_3 : TERM
    TERM character_trait(property="haunted_by_death_of", value="Lady Elyria") -> character_trait_2 : TERM
    TERM character(name="Lord Amandus") -> character_4 : TERM
    TERM character(name="Prince Emory") -> character_5 : TERM
    TERM activity(actor="Prince Emory", verb="abandon_throne") -> activity_5 : TERM
    TERM activity(actor="Johnathon Wyrd", object="Prince Emory", purpose=activity_5, verb="plant_idea") -> activity_6 : TERM
    TERM obligation(activity=activity_6, actor="Johnathon Wyrd") -> obligation_2 : TERM
    TERM character(name="Elara") -> character_6 : TERM
    TERM character(name="Silas") -> character_7 : TERM
    TERM character(name="Caelum") -> character_8 : TERM
    TERM conjunction(items=[character_6, character_7, character_8]) -> conjunction_2 : TERM
    TERM activity(actor="team", object="Prince Emory", verb="infiltrate_dreams") -> activity_7 : TERM
    TERM self_protection(actor="Prince Emory", domain="subconscious_defenses") -> self_protection_2 : TERM
    TERM temporal_context(activity=activity_7) -> temporal_context_2 : TERM
    TERM substitute(original="resurrect_Elyria", purpose="save_kingdom", replacement="complete_inception") -> substitute_2 : TERM
    TERM activity(actor="Johnathon Wyrd", purpose=substitute_2, verb="sacrifice") -> activity_8 : TERM
    UTTER respond(target=art_story)
  }
  TURN t3 SPEAKER=USER {
    TERM subject(kind="Half-Life 2", qualifier=cat_game) -> subject_2 : TERM
    TERM activity(object=art_story, verb="rewrite") -> activity_9 : TERM
    UTTER propose(target=activity_9, constraints=[subject_2])
  }
  TURN t4 SPEAKER=AGENT {
    CLAIM provides(actor=role_agent, subject=art_story) BY role_agent STATUS asserted SOURCE "t4:s1" -> provides_3 : CLAIM
    TERM activity(actor="Dreamhackers", location="City 17", object="Combine", verb="manipulate_dreams") -> activity_10 : TERM
    CLAIM opposes(actor="Dreamhackers", subject="Combine") BY role_agent STATUS reported SOURCE "t4:s4" -> opposes_2 : CLAIM
    TERM character(name="Gordon Freeman", series="Half-Life 2") -> character_9 : TERM
    TERM character(name="Alyx Vance", series="Half-Life 2") -> character_10 : TERM
    TERM character_trait(property="tormented_by_death_of", value="Alyx Vance") -> character_trait_3 : TERM
    TERM character(name="Isaac Kleiner", series="Half-Life 2") -> character_11 : TERM
    TERM character(name="Wallace Breen", series="Half-Life 2") -> character_12 : TERM
    TERM activity(actor="Wallace Breen", object="Combine", verb="betray") -> activity_11 : TERM
    TERM activity(actor="Gordon Freeman", object="Wallace Breen", purpose=activity_11, verb="plant_idea") -> activity_12 : TERM
    TERM obligation(activity=activity_12, actor="Gordon Freeman") -> obligation_3 : TERM
    CLAIM has_goal(goal=obligation_3, subject="Isaac Kleiner") BY role_agent STATUS reported SOURCE "t4:s8" -> has_goal_2 : CLAIM
    TERM character(name="Barney Calhoun", series="Half-Life 2") -> character_13 : TERM
    TERM character(name="Dog", series="Half-Life 2") -> character_14 : TERM
    TERM character(name="Judith Mossman", series="Half-Life 2") -> character_15 : TERM
    TERM conjunction(items=[character_13, character_14, character_15]) -> conjunction_3 : TERM
    TERM activity(actor="team", object="Wallace Breen", verb="infiltrate_subconscious") -> activity_13 : TERM
    TERM temporal_context(activity=activity_13) -> temporal_context_3 : TERM
    TERM time_horizon(horizon="future") -> time_horizon_2 : TERM
    TERM activity(object="Combine", verb="secure_future") -> activity_14 : TERM
    TERM activity(actor="Gordon Freeman", purpose=activity_14, verb="complete_inception") -> activity_15 : TERM
    CLAIM enables(condition=activity_15, outcome=time_horizon_2) BY role_agent STATUS reported SOURCE "t4:s16" -> enables_2 : CLAIM
    UTTER respond(target=art_story)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | activity, propose | covered |
| n2 | constraint | aesthetic | covered |
| n3 | speech_act | provides, respond, art_story | covered |
| n4 | object | activity | covered |
| n5 | object | character, character_trait | covered |
| n6 | action | character, obligation, activity | covered |
| n7 | object | character, conjunction | covered |
| n8 | action | activity, self_protection, temporal_context | covered |
| n9 | action | substitute, activity | covered |
| n10 | action | activity, propose, art_story | covered |
| n11 | constraint | subject, cat_game | covered |
| n12 | speech_act | provides, respond, art_story | covered |
| n13 | object | activity, opposes | covered |
| n14 | object | character, character_trait | covered |
| n15 | action | character, activity, obligation, has_goal | covered |
| n16 | object | character, conjunction | covered |
| n17 | action | activity, temporal_context | covered |
| n18 | action | time_horizon, activity, enables | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t4:s17 is represented.
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
