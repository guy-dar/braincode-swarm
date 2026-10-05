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
    TERM lexical_label(value=food_label::vegetarian) -> lexical_label_2 : TERM
    TERM include(item=lexical_label_2) -> include_2 : TERM
    UTTER ask(target=activity_2, constraints=[requirement_2, requirement_3, include_2])
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM lexical_label(value=food_label::taco) -> lexical_label_3 : TERM
    CLAIM propose_menu(menu=lexical_label_3) BY role_agent STATUS asserted SOURCE "t2:s1" -> propose_menu_2 : CLAIM
    UTTER propose(target=lexical_label_3)
    CLAIM menu_works(property="customizable") BY role_agent STATUS asserted SOURCE "t2:s3" -> menu_works_2 : CLAIM
    CLAIM menu_works(property="easy_to_prepare") BY role_agent STATUS asserted SOURCE "t2:s3" -> menu_works_3 : CLAIM
    TERM lexical_label(value=food_label::chicken) -> lexical_label_4 : TERM
    TERM lexical_label(value=food_label::beef) -> lexical_label_5 : TERM
    TERM include(item=meat) -> include_3 : TERM
    TERM lexical_label(value=food_label::beans) -> lexical_label_6 : TERM
    TERM lexical_label(value=food_label::tortillas) -> lexical_label_7 : TERM
    TERM include(item=lettuce) -> include_4 : TERM
    TERM include(item=cheese) -> include_5 : TERM
    TERM lexical_label(value=food_label::salsa) -> lexical_label_8 : TERM
    TERM lexical_label(value=food_label::guacamole) -> lexical_label_9 : TERM
    TERM lexical_label(value=food_label::rice) -> lexical_label_10 : TERM
    TERM lexical_label(value=food_label::salad) -> lexical_label_11 : TERM
    TERM lexical_label(value=food_label::chips) -> lexical_label_12 : TERM
    TERM include(item=entity_sides) -> include_6 : TERM
    CLAIM menu_works(property="prep_ahead") BY role_agent STATUS asserted SOURCE "t2:s14" -> menu_works_4 : CLAIM
    TERM activity(object=food_label::vegetables, verb="saute") -> activity_3 : TERM
    TERM activity(object=food_label::beans, verb="mix") -> activity_4 : TERM
    TERM activity(object=meat, verb="cook") -> activity_5 : TERM
    TERM include(item=fruit_juice) -> include_7 : TERM
    TERM include(item=ice_cream) -> include_8 : TERM
    TERM lexical_label(value=food_label::churros) -> lexical_label_13 : TERM
    TERM lexical_label(value=food_label::brownies) -> lexical_label_14 : TERM
    TERM include(item=entity_desserts) -> include_9 : TERM
    TERM lexical_label(value=food_label::pasta) -> lexical_label_15 : TERM
    CLAIM propose_menu(menu=lexical_label_15) BY role_agent STATUS asserted SOURCE "t2:s36" -> propose_menu_3 : CLAIM
    TERM lexical_label(value=food_label::ziti) -> lexical_label_16 : TERM
    TERM lexical_label(value=food_label::lasagna) -> lexical_label_17 : TERM
    TERM lexical_label(value=food_label::spinach) -> lexical_label_18 : TERM
    TERM lexical_label(value=food_label::ricotta) -> lexical_label_19 : TERM
    TERM include(item=bread) -> include_10 : TERM
    CLAIM menu_works(property="assemble_ahead") BY role_agent STATUS asserted SOURCE "t2:s42" -> menu_works_5 : CLAIM
    TERM offer_help() -> offer_help_2 : TERM
    TERM include(item=entity_appetizers) -> include_11 : TERM
    TERM include(item=entity_recipes) -> include_12 : TERM
    UTTER offer(target=offer_help_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, activity, role_friend | covered |
| n2 | constraint | requirement | covered |
| n3 | constraint | include, lexical_label, food_label::vegetarian | covered |
| n4 | speech_act | propose, propose_menu, role_agent | covered |
| n5 | object | lexical_label, food_label::taco | label-preserved |
| n6 | claim | menu_works, role_agent | covered |
| n7 | object | meat, lexical_label, food_label::chicken, food_label::beef | covered |
| n8 | object | lexical_label, food_label::beans | label-preserved |
| n9 | object | lexical_label, food_label::tortillas | label-preserved |
| n10 | object | lettuce, cheese, lexical_label, food_label::salsa, food_label::guacamole | covered |
| n11 | object | entity_sides, lexical_label, food_label::rice, food_label::salad, food_label::chips | covered |
| n12 | claim | menu_works, role_agent | covered |
| n13 | action | activity, food_label::vegetables, food_label::beans | covered |
| n14 | action | activity, meat, fruit_juice | covered |
| n15 | object | entity_desserts, ice_cream, lexical_label, food_label::churros, food_label::brownies | covered |
| n16 | speech_act | propose_menu, lexical_label, food_label::pasta, role_agent | covered |
| n17 | object | bread, lexical_label, food_label::ziti, food_label::lasagna, food_label::spinach, food_label::ricotta | covered |
| n18 | claim | menu_works, role_agent | covered |
| n19 | speech_act | offer, offer_help, entity_appetizers, entity_recipes | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s49 is represented
- Opaque-text spans: none
- Label-preserved spans: t2:s2 "taco" -> food_label::taco; t2:s6 "beans" -> food_label::beans; t2:s7 "tortillas" -> food_label::tortillas
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
