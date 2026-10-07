```braincode
TERM  activity(verb="eat", actor="bald_eagle", object=animal_label::tiger) -> eat_tiger : TERM
TERM negation(target=eat_tiger) -> neg_eat_tiger : TERM
TERM activity(verb="see", actor="bald_eagle", object=animal_label::cow) -> see_cow : TERM
TERM activity(verb="eat", actor="cow", object=animal_label::eagle) -> eat_eagle : TERM
TERM requirement(property="nice", value=TRUE) -> nice_req : TERM
TERM negation(target=nice_req) -> neg_nice_req : TERM
TERM activity(verb="eat", actor="mouse", object=animal_label::eagle) -> eat_mouse : TERM
TERM activity(verb="eat", actor="tiger", object=animal_label::cow) -> eat_cow : TERM
TERM requirement(property="rough", value=TRUE) -> rough_req : TERM
TERM negation(target=rough_req) -> neg_rough_req : TERM
TERM requirement(property="young", value=TRUE) -> young_req : TERM
TERM negation(target=young_req) -> neg_young_req : TERM
TERM activity(verb="see", actor="tiger", object=animal_label::cow) -> see_cow_2 : TERM
TERM conjunction(items=[eat_cow, eat_tiger]) -> conj_2 : TERM
TERM negation(target=eat_eagle) -> neg_eat_eagle : TERM
TERM conditional(condition=conj_2, consequence=neg_eat_eagle) -> cond_2 : TERM
TERM activity(verb="see", actor="cow", object=animal_label::tiger) -> see_tiger : TERM
TERM activity(verb="eat", actor="cow", object=animal_label::mouse) -> eat_mouse_2 : TERM
TERM conditional(condition=see_tiger, consequence=eat_mouse_
```
