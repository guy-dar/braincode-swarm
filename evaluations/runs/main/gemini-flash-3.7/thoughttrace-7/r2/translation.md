Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(actor=role_friend, verb="dinner") -> activity_2 : TERM
    TERM requirement(property="delicious", value=TRUE) -> requirement_2 : TERM
    TERM requirement(property="easy_to_prepare", value=TRUE) -> requirement_3 : TERM
    TERM include(item="vegetarian_option") -> include_2 : TERM
    TERM conjunction(items=[activity_2, requirement_2, requirement_3, include_2]) -> conjunction_2 : TERM
    CLAIM user_preference(constraints=conjunction_2) BY role_user STATUS asserted SOURCE "t1:s1" -> user_preference_2 : CLAIM
    UTTER ask(target=conjunction_2)
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM lexical_label(value=food_label::taco) -> lexical_label_2 : TERM
    CLAIM propose_menu(menu=lexical_label_2) BY role_agent STATUS asserted SOURCE "t2:s1" -> propose_menu_2 : CLAIM
    UTTER propose(target=lexical_label_2)

    CLAIM menu_works(property="customizable") BY role_agent STATUS asserted SOURCE "t2:s3" -> menu_works_2 : CLAIM
    CLAIM menu_works(property="easy_to_prepare") BY role_agent STATUS asserted SOURCE "t2:s3" -> menu_works_3 : CLAIM

    TERM lexical_label(value=food_label::chicken) -> lexical_label_3 : TERM
    TERM lexical_label(value=food_label::beef) -> lexical_label_4 : TERM
    TERM include(item=meat) -> include_3 : TERM

    TERM lexical_label(value=food_label::bean) -> lexical_label_5 : TERM
    TERM lexical_label(value=food_label::veggie) -> lexical_label_6 : TERM

    TERM lexical_label(value=food_label::tortilla) -> lexical_label_7 : TERM

    TERM include(item=lettuce) -> include_4 : TERM
    TERM include(item=cheese) -> include_5 : TERM
    TERM lexical_label(value=food_label::tomato) -> lexical_label_8 : TERM
    TERM lexical_label(value=food_label::guacamole) -> lexical_label_9 : TERM
    TERM lexical_label(value=food_label::salsa) -> lexical_label_10 : TERM

    TERM lexical_label(value=food_label::rice) -> lexical_label_11 : TERM
    TERM lexical_label(value=food_label::salad) -> lexical_label_12 : TERM
    TERM lexical_label(value=food_label::chips) -> lexical_label_13 : TERM
    TERM include(item=entity_sides) -> include_6 : TERM

    CLAIM menu_works(property="prep_ahead") BY role_agent STATUS asserted SOURCE "t2:s14" -> menu_works_4 : CLAIM
    TERM activity(actor="guests", verb="assemble", object=plate) -> activity_3 : TERM
    CLAIM statement(fact=activity_3) BY role_agent STATUS asserted SOURCE "t2:s14" -> statement_2 : CLAIM

    TERM activity(verb="sauté", object=food_label::bean) -> activity_4 : TERM
    TERM activity(verb="cook", object=meat) -> activity_5 : TERM
    TERM include(item=fruit_juice) -> include_7 : TERM

    TERM include(item=ice_cream) -> include_8 : TERM
    TERM include(item=entity_desserts) -> include_9 : TERM
    TERM lexical_label(value=food_label::churro) -> lexical_label_14 : TERM
    TERM lexical_label(value=food_label::brownie) -> lexical_label_15 : TERM

    TERM lexical_label(value=food_label::pasta) -> lexical_label_16 : TERM
    CLAIM propose_menu(menu=lexical_label_16) BY role_agent STATUS asserted SOURCE "t2:s36" -> propose_menu_3 : CLAIM
    UTTER propose(target=lexical_label_16)

    TERM lexical_label(value=food_label::ziti) -> lexical_label_17 : TERM
    TERM lexical_label(value=food_label::lasagna) -> lexical_label_18 : TERM
    TERM lexical_label(value=food_label::spinach) -> lexical_label_19 : TERM
    TERM lexical_label(value=food_label::ricotta) -> lexical_label_20 : TERM
    TERM include(item=bread) -> include_10 : TERM

    TERM activity(verb="assemble", object=food_label::pasta) -> activity_6 : TERM
    CLAIM prep_time(value=activity_6) BY role_agent STATUS asserted SOURCE "t2:s42" -> prep_time_2 : CLAIM
    CLAIM menu_works(property="prep_ahead") BY role_agent STATUS asserted SOURCE "t2:s42" -> menu_works_5 : CLAIM

    TERM include(item=entity_appetizers) -> include_11 : TERM
    TERM include(item=entity_grocery_list) -> include_12 : TERM
    TERM offer_help() -> offer_help_2 : TERM
    UTTER offer(target=offer_help_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, role_friend, role_user, user_preference | covered |
| n2 | constraint | requirement, menu_works | covered |
| n3 | constraint | include | covered |
| n4 | speech_act | propose, propose_menu | covered |
| n5 | object | food_label::taco | label-preserved |
| n6 | claim | menu_works | covered |
| n7 | object | food_label::chicken, food_label::beef, meat | covered |
| n8 | object | food_label::bean, food_label::veggie | label-preserved |
| n9 | object | food_label::tortilla | label-preserved |
| n10 | object | food_label::tomato, food_label::guacamole, food_label::salsa, lettuce, cheese | covered |
| n11 | object | food_label::rice, food_label::salad, food_label::chips, entity_sides | covered |
| n12 | claim | menu_works, statement, activity, plate | covered |
| n13 | action | activity, food_label::bean | covered |
| n14 | action | activity, meat, fruit_juice | covered |
| n15 | object | food_label::churro, food_label::brownie, ice_cream, entity_desserts | covered |
| n16 | speech_act | propose, propose_menu | covered |
| n17 | object | food_label::pasta, food_label::ziti, food_label::lasagna, food_label::spinach, food_label::ricotta, bread | covered |
| n18 | claim | prep_time, menu_works, activity | covered |
| n19 | speech_act | offer, offer_help, entity_appetizers, entity_grocery_list | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s49 is represented.
- Opaque-text spans: none
- Label-preserved spans: t2:s2 "taco" → food_label::taco; t2:s5 "chicken", "beef" → food_label::chicken, food_label::beef; t2:s6 "black bean", "roasted veggie" → food_label::bean, food_label::veggie; t2:s7 "tortillas" → food_label::tortilla; t2:s8 "tomatoes", "guacamole", "salsa" → food_label::tomato, food_label::guacamole, food_label::salsa; t2:s9 "rice", "salad", "tortilla chips" → food_label::rice, food_label::salad, food_label::chips; t2:s33-s34 "churros", "brownies" → food_label::churro, food_label::brownie; t2:s38-s40 "pasta", "ziti", "lasagna", "spinach", "ricotta" → food_label::pasta, food_label::ziti, food_label::lasagna, food_label::spinach, food_label::ricotta
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
