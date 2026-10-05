Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM lexical_label(value=food_label::vegetarian) -> lexical_label_2 : TERM
    TERM include(item=lexical_label_2) -> include_2 : TERM
    TERM requirement(property="delicious", value=TRUE) -> requirement_2 : TERM
    TERM requirement(property="easy_to_prepare", value=TRUE) -> requirement_3 : TERM
    TERM conjunction(items=[requirement_2, requirement_3, include_2]) -> conjunction_2 : TERM
    CLAIM user_preference(constraints=conjunction_2) BY role_user STATUS asserted SOURCE "t1:s1" -> user_preference_2 : CLAIM
    TERM subject(kind="dinner", qualifier="hosting_friends") -> subject_2 : TERM
    UTTER ask(target=subject_2, constraints=[conjunction_2], recipient=role_agent)
  }
  TURN t2 SPEAKER=AGENT {
    TERM lexical_label(value=food_label::taco) -> lexical_label_3 : TERM
    CLAIM propose_menu(menu=lexical_label_3) BY role_agent STATUS asserted SOURCE "t2:s1" -> propose_menu_2 : CLAIM
    UTTER propose(target=lexical_label_3)
    CLAIM menu_works(property="customizable") BY role_agent STATUS asserted SOURCE "t2:s3" -> menu_works_2 : CLAIM
    CLAIM menu_works(property="easy_to_prepare") BY role_agent STATUS asserted SOURCE "t2:s3" -> menu_works_3 : CLAIM
    TERM lexical_label(value=food_label::chicken) -> lexical_label_4 : TERM
    TERM lexical_label(value=food_label::beef) -> lexical_label_5 : TERM
    TERM requirement(property="meat", value=meat) -> requirement_4 : TERM
    TERM lexical_label(value=food_label::bean) -> lexical_label_6 : TERM
    TERM lexical_label(value=food_label::tortilla) -> lexical_label_7 : TERM
    TERM lexical_label(value=food_label::tomato) -> lexical_label_8 : TERM
    TERM requirement(property="cheese", value=cheese) -> requirement_5 : TERM
    TERM requirement(property="lettuce", value=lettuce) -> requirement_6 : TERM
    TERM lexical_label(value=food_label::rice) -> lexical_label_9 : TERM
    TERM lexical_label(value=food_label::salad) -> lexical_label_10 : TERM
    TERM requirement(property="sides", value=entity_sides) -> requirement_7 : TERM
    CLAIM prep_time(value=lexical_label_3) BY role_agent STATUS asserted SOURCE "t2:s14" -> prep_time_2 : CLAIM
    CLAIM menu_works(property="make_ahead") BY role_agent STATUS asserted SOURCE "t2:s14" -> menu_works_4 : CLAIM
    TERM activity(object=food_label::vegetables, verb="saute") -> activity_2 : TERM
    TERM activity(object=meat, verb="cook") -> activity_3 : TERM
    TERM requirement(property="lime_juice", value=fruit_juice) -> requirement_8 : TERM
    TERM lexical_label(value=food_label::churro) -> lexical_label_11 : TERM
    TERM requirement(property="dessert", value=entity_desserts) -> requirement_9 : TERM
    TERM requirement(property="ice_cream", value=ice_cream) -> requirement_10 : TERM
    TERM lexical_label(value=food_label::pasta) -> lexical_label_12 : TERM
    CLAIM propose_menu(menu=lexical_label_12) BY role_agent STATUS asserted SOURCE "t2:s36" -> propose_menu_3 : CLAIM
    UTTER propose(target=lexical_label_12)
    TERM lexical_label(value=food_label::ziti) -> lexical_label_13 : TERM
    TERM lexical_label(value=food_label::lasagna) -> lexical_label_14 : TERM
    TERM requirement(property="garlic_bread", value=bread) -> requirement_11 : TERM
    CLAIM prep_time(value=lexical_label_12) BY role_agent STATUS asserted SOURCE "t2:s42" -> prep_time_3 : CLAIM
    CLAIM menu_works(property="make_ahead") BY role_agent STATUS asserted SOURCE "t2:s42" -> menu_works_5 : CLAIM
    TERM offer_help() -> offer_help_2 : TERM
    UTTER offer(target=offer_help_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, user_preference | covered |
| n2 | constraint | menu_works, requirement | covered |
| n3 | constraint | include | covered |
| n4 | speech_act | propose, propose_menu | covered |
| n5 | object | food_label::taco | label-preserved |
| n6 | claim | menu_works | covered |
| n7 | object | meat, food_label::chicken, food_label::beef | covered |
| n8 | object | food_label::bean | label-preserved |
| n9 | object | bread, food_label::tortilla | covered |
| n10 | object | cheese, lettuce, food_label::tomato | covered |
| n11 | object | entity_sides, food_label::rice, food_label::salad | covered |
| n12 | claim | prep_time, menu_works | covered |
| n13 | action | activity | covered |
| n14 | action | meat, fruit_juice, activity | covered |
| n15 | object | entity_desserts, ice_cream, food_label::churro | covered |
| n16 | speech_act | propose, propose_menu | covered |
| n17 | object | bread, food_label::ziti, food_label::lasagna | covered |
| n18 | claim | prep_time, menu_works | covered |
| n19 | speech_act | offer, offer_help | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s49 is represented.
- Opaque-text spans: none
- Label-preserved spans: t2:s2 "taco" → food_label::taco; t2:s6 "black bean" → food_label::bean (open-group label only; no dictionary sense resolved)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
