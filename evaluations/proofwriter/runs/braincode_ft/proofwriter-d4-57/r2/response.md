```braincode
TERM  activity(verb="eat", actor="bald_eagle", object=animal_label::tiger) -> eat_tiger : TERM
TERM negation(target=eat_tiger) -> neg_eat_tiger : TERM
TERM activity(verb="see", actor="bald_eagle", object=animal_label::cow) -> see_cow : TERM
TERM activity(verb="eat", actor="cow", object=animal_label::eagle) -> eat_eagle : TERM
TERM requirement(property="nice", value=TRUE) -> nice_cow : TERM
TERM negation(target=nice_cow) -> neg_nice_cow : TERM
TERM activity(verb="eat", actor="mouse", object=animal_label::eagle) -> eat_mouse : TERM
TERM activity(verb="eat", actor="tiger", object=animal_label::cow) -> eat_cow : TERM
TERM requirement(property="rough", value=TRUE) -> rough_tiger : TERM
TERM requirement(property="young", value=TRUE) -> young_tiger : TERM
TERM negation(target=young_tiger) -> neg_young_tiger : TERM
TERM activity(verb="see", actor="tiger", object=animal_label::cow) -> see_cow_2 : TERM
TERM conjunction(items=[eat_cow, eat_eagle]) -> conjunction_2 : TERM
TERM negation(target=eat_mouse) -> neg_eat_mouse : TERM
TERM conditional(condition=conjunction_2, consequence=neg_eat_mouse) -> conditional_2 : TERM
TERM activity(verb="see", actor="mouse", object=animal_label::tiger) -> see_tiger : TERM
TERM activity(verb="eat", actor="mouse", object=animal_label::cow) -> eat_cow_2 : TERM
TERM conditional(condition=see_tiger, consequence=eat_cow_2) -> conditional_3 : TERM
```
