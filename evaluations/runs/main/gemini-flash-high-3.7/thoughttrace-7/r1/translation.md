Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="dinner", qualifier=role_friend) -> subject_2 : TERM
    TERM requirement(property="delicious", value=TRUE) -> requirement_2 : TERM
    TERM requirement(property="easy_to_prepare", value=TRUE) -> requirement_3 : TERM
    TERM include(item="vegetarian_option") -> include_2 : TERM
    TERM conjunction(items=[requirement_2, requirement_3, include_2]) -> conjunction_2 : TERM
    CLAIM user_preference(constraints=conjunction_2) BY role_user STATUS asserted SOURCE "t1:s1" -> user_preference_2 : CLAIM
    UTTER ask(target=subject_2, constraints=[requirement_2, requirement_3, include_2], recipient=role_agent)
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM lexical_label(value=food_label::taco) -> lexical_label_2 : TERM
    CLAIM propose_menu(menu=lexical_label_2) BY role_agent STATUS asserted SOURCE "t2:s1" -> propose_menu_2 : CLAIM
    UTTER propose(target=lexical_label_2)
    CLAIM menu_works(property="customizable") BY role_agent STATUS asserted SOURCE "t2:s3" -> menu_works_2 : CLAIM
    CLAIM menu_works(property="relaxed") BY role_agent STATUS asserted SOURCE "t2:s3" -> menu_works_3 : CLAIM
    CLAIM menu_works(property="easy_to_prepare") BY role_agent STATUS asserted SOURCE "t2:s3" -> menu_works_4 : CLAIM
    TERM include(item=meat) -> include_3 : TERM
    TERM lexical_label(value=food_label::chicken) -> lexical_label_3 : TERM
    TERM lexical_label(value=food_label::beef) -> lexical_label_4 : TERM
    TERM lexical_label(value=food_label::bean) -> lexical_label_5 : TERM
    TERM include(item=lexical_label_5) -> include_4 : TERM
    TERM lexical_label(value=food_label::tortilla) -> lexical_label_6 : TERM
    TERM lexical_label(value=food_label::shell) -> lexical_label_7 : TERM
    TERM include(item=lettuce) -> include_5 : TERM
    TERM include(item=cheese) -> include_6 : TERM
    TERM lexical_label(value=food_label::tomato) -> lexical_label_8 : TERM
    TERM lexical_label(value=food_label::guacamole) -> lexical_label_9 : TERM
    TERM lexical_label(value=food_label::salsa) -> lexical_label_10 : TERM
    TERM include(item=entity_sides) -> include_7 : TERM
    TERM lexical_label(value=food_label::rice) -> lexical_label_11 : TERM
    TERM lexical_label(value=food_label::salad) -> lexical_label_12 : TERM
    TERM lexical_label(value=food_label::chips) -> lexical_label_13 : TERM
    CLAIM menu_works(property="prep_ahead") BY role_agent STATUS asserted SOURCE "t2:s14" -> menu_works_5 : CLAIM
    CLAIM menu_works(property="self_assembly") BY role_agent STATUS asserted SOURCE "t2:s15" -> menu_works_6 : CLAIM
    TERM activity(object=food_label::vegetable, verb="saute") -> activity_2 : TERM
    TERM activity(object=food_label::bean, verb="mix") -> activity_3 : TERM
    TERM sequence(items=[activity_2, activity_3]) -> sequence_2 : TERM
    TERM activity(instrument=fruit_juice, object=meat, verb="cook") -> activity_4 : TERM
    TERM include(item=ice_cream) -> include_8 : TERM
    TERM include(item=entity_desserts) -> include_9 : TERM
    TERM lexical_label(value=food_label::churro) -> lexical_label_14 : TERM
    TERM lexical_label(value=food_label::brownie) -> lexical_label_15 : TERM
    TERM lexical_label(value=food_label::pasta) -> lexical_label_16 : TERM
    TERM substitute(original=lexical_label_2, replacement=lexical_label_16) -> substitute_2 : TERM
    CLAIM propose_menu(menu=lexical_label_16) BY role_agent STATUS asserted SOURCE "t2:s36" -> propose_menu_3 : CLAIM
    UTTER propose(target=lexical_label_16)
    TERM lexical_label(value=food_label::ziti) -> lexical_label_17 : TERM
    TERM lexical_label(value=food_label::lasagna) -> lexical_label_18 : TERM
    TERM include(item=bread) -> include_10 : TERM
    CLAIM menu_works(property="assemble_ahead") BY role_agent STATUS asserted SOURCE "t2:s42" -> menu_works_7 : CLAIM
    TERM offer_help() -> offer_help_2 : TERM
    TERM group_size(count=8) -> group_size_2 : TERM
    TERM include(item=entity_appetizers) -> include_11 : TERM
    TERM include(item=entity_grocery_list) -> include_12 : TERM
    UTTER offer(target=offer_help_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, role_friend, user_preference | covered |
| n2 | constraint | requirement, menu_works | covered |
| n3 | constraint | include | covered |
| n4 | speech_act | propose, propose_menu | covered |
| n5 | object | lexical_label, food_label::taco | label-preserved |
| n6 | claim | menu_works | covered |
| n7 | object | meat, lexical_label, food_label::chicken, food_label::beef | label-preserved |
| n8 | object | include, lexical_label, food_label::bean | label-preserved |
| n9 | object | lexical_label, food_label::tortilla, food_label::shell | label-preserved |
| n10 | object | lettuce, cheese, lexical_label, food_label::tomato, food_label::guacamole, food_label::salsa | label-preserved |
| n11 | object | entity_sides, lexical_label, food_label::rice, food_label::salad, food_label::chips | label-preserved |
| n12 | claim | menu_works | covered |
| n13 | action | activity, sequence, food_label::vegetable, food_label::bean | covered |
| n14 | action | activity, meat, fruit_juice | covered |
| n15 | object | ice_cream, entity_desserts, lexical_label, food_label::churro, food_label::brownie | label-preserved |
| n16 | speech_act | propose, propose_menu, substitute, lexical_label, food_label::pasta | covered |
| n17 | object | bread, lexical_label, food_label::ziti, food_label::lasagna | label-preserved |
| n18 | claim | menu_works | covered |
| n19 | speech_act | offer, offer_help, group_size, entity_appetizers, entity_grocery_list | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s49 is represented
- Opaque-text spans: none
- Label-preserved spans: food_label::taco, food_label::chicken, food_label::beef, food_label::bean, food_label::tortilla, food_label::shell, food_label::tomato, food_label::guacamole, food_label::salsa, food_label::rice, food_label::salad, food_label::chips, food_label::vegetable, food_label::churro, food_label::brownie, food_label::pasta, food_label::ziti, food_label::lasagna
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
