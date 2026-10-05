Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM requirement(property="delicious", value=TRUE) -> requirement_2 : TERM
    TERM requirement(property="easy_to_prepare", value=TRUE) -> requirement_3 : TERM
    TERM lexical_label(value=food_label::vegetarian) -> lexical_label_2 : TERM
    TERM include(item=lexical_label_2) -> include_2 : TERM
    CLAIM user_preference(constraints=requirement_2) BY role_user STATUS asserted SOURCE "t1:s1" -> user_preference_2 : CLAIM
    CLAIM user_preference(constraints=requirement_3) BY role_user STATUS asserted SOURCE "t1:s1" -> user_preference_3 : CLAIM
    CLAIM user_preference(constraints=include_2) BY role_user STATUS asserted SOURCE "t1:s1" -> user_preference_4 : CLAIM
    UTTER ask(target=include_2, audience=role_friend, recipient=role_agent)
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM lexical_label(value=food_label::taco) -> lexical_label_3 : TERM
    CLAIM propose_menu(menu=lexical_label_3) BY role_agent STATUS asserted SOURCE "t2:s1" -> propose_menu_2 : CLAIM
    UTTER propose(target=lexical_label_3)
    CLAIM menu_works(property="customizable") BY role_agent STATUS asserted SOURCE "t2:s3" -> menu_works_2 : CLAIM
    CLAIM menu_works(property="relaxed") BY role_agent STATUS asserted SOURCE "t2:s3" -> menu_works_3 : CLAIM
    CLAIM menu_works(property="easy_to_prepare") BY role_agent STATUS asserted SOURCE "t2:s3" -> menu_works_4 : CLAIM
    TERM lexical_label(value=food_label::chicken) -> lexical_label_4 : TERM
    TERM lexical_label(value=food_label::beef) -> lexical_label_5 : TERM
    TERM include(item=meat) -> include_3 : TERM
    TERM lexical_label(value=food_label::beans) -> lexical_label_6 : TERM
    TERM lexical_label(value=food_label::veggie) -> lexical_label_7 : TERM
    TERM lexical_label(value=food_label::tortilla) -> lexical_label_8 : TERM
    TERM include(item=bread) -> include_4 : TERM
    TERM lexical_label(value=food_label::tomato) -> lexical_label_9 : TERM
    TERM lexical_label(value=food_label::guacamole) -> lexical_label_10 : TERM
    TERM lexical_label(value=food_label::salsa) -> lexical_label_11 : TERM
    TERM include(item=lettuce) -> include_5 : TERM
    TERM include(item=cheese) -> include_6 : TERM
    TERM lexical_label(value=food_label::rice) -> lexical_label_12 : TERM
    TERM lexical_label(value=food_label::salad) -> lexical_label_13 : TERM
    TERM lexical_label(value=food_label::chips) -> lexical_label_14 : TERM
    TERM include(item=entity_sides) -> include_7 : TERM
    TERM include(item=plate) -> include_8 : TERM
    CLAIM menu_works(property="make_ahead") BY role_agent STATUS asserted SOURCE "t2:s14" -> menu_works_5 : CLAIM
    CLAIM menu_works(property="self_assembly") BY role_agent STATUS asserted SOURCE "t2:s15" -> menu_works_6 : CLAIM
    TERM activity(object=food_label::veggie, verb="saute") -> activity_2 : TERM
    TERM activity(object=food_label::beans, verb="mix") -> activity_3 : TERM
    TERM activity(instrument=object_label::oil, object=meat, verb="cook") -> activity_4 : TERM
    TERM activity(instrument=fruit_juice, object=meat, verb="flavor") -> activity_5 : TERM
    TERM lexical_label(value=food_label::churros) -> lexical_label_15 : TERM
    TERM lexical_label(value=food_label::brownies) -> lexical_label_16 : TERM
    TERM include(item=ice_cream) -> include_9 : TERM
    TERM include(item=entity_desserts) -> include_10 : TERM
    TERM lexical_label(value=food_label::pasta) -> lexical_label_17 : TERM
    CLAIM propose_menu(menu=lexical_label_17) BY role_agent STATUS asserted SOURCE "t2:s36" -> propose_menu_3 : CLAIM
    UTTER propose(target=lexical_label_17, topic=cuisine_italian)
    TERM lexical_label(value=food_label::ziti) -> lexical_label_18 : TERM
    TERM lexical_label(value=food_label::lasagna) -> lexical_label_19 : TERM
    TERM lexical_label(value=food_label::spinach) -> lexical_label_20 : TERM
    TERM lexical_label(value=food_label::ricotta) -> lexical_label_21 : TERM
    CLAIM menu_works(property="assemble_ahead") BY role_agent STATUS asserted SOURCE "t2:s42" -> menu_works_7 : CLAIM
    CLAIM menu_works(property="bake_before_serving") BY role_agent STATUS asserted SOURCE "t2:s42" -> menu_works_8 : CLAIM
    TERM offer_help() -> offer_help_2 : TERM
    TERM include(item=entity_grocery_list) -> include_11 : TERM
    TERM include(item=entity_recipes) -> include_12 : TERM
    TERM include(item=entity_appetizers) -> include_13 : TERM
    UTTER offer(target=offer_help_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, role_friend, role_agent | covered |
| n2 | constraint | requirement, user_preference | covered |
| n3 | constraint | include, lexical_label, food_label::vegetarian | covered |
| n4 | speech_act | propose, propose_menu | covered |
| n5 | object | food_label::taco | label-preserved |
| n6 | claim | menu_works | covered |
| n7 | object | food_label::chicken, food_label::beef, meat | covered |
| n8 | object | food_label::beans, food_label::veggie | label-preserved |
| n9 | object | food_label::tortilla, bread | covered |
| n10 | object | food_label::tomato, food_label::guacamole, food_label::salsa, lettuce, cheese | covered |
| n11 | object | food_label::rice, food_label::salad, food_label::chips, entity_sides, plate | covered |
| n12 | claim | menu_works, plate | covered |
| n13 | action | activity, food_label::veggie, food_label::beans | covered |
| n14 | action | activity, meat, fruit_juice | covered |
| n15 | object | food_label::churros, food_label::brownies, ice_cream, entity_desserts | covered |
| n16 | speech_act | propose, propose_menu, cuisine_italian | covered |
| n17 | object | food_label::ziti, food_label::lasagna, food_label::spinach, food_label::ricotta, bread | covered |
| n18 | claim | menu_works | covered |
| n19 | speech_act | offer, offer_help, entity_grocery_list, entity_recipes, entity_appetizers | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s49 is represented
- Opaque-text spans: none
- Label-preserved spans: t2:s2 "taco" → food_label::taco; t2:s6 "veggie", "beans" → food_label::veggie, food_label::beans
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
