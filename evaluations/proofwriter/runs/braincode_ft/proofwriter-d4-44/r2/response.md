```braincode
TERM  activity(verb="visit", actor="bald_eagle", object=animal_label::cow) -> visit_cow : TERM
TERM activity(verb="like", actor="cow", object=animal_label::rabbit) -> like_rabbit : TERM
TERM activity(verb="visit", actor="cow", object=animal_label::mouse) -> visit_mouse : TERM
TERM lexical_label(value=color_label::green) -> green_label : TERM
TERM requirement(property="color", value=green_label) -> color_req : TERM
TERM requirement(property="personality", value="nice") -> nice_req : TERM
TERM requirement(property="age", value="young") -> young_req : TERM
TERM activity(verb="like", actor="rabbit", object=animal_label::mouse) -> like_mouse : TERM
TERM activity(verb="like", actor="something", object=animal_label::rabbit) -> like_rabbit_2 : TERM
TERM activity(verb="like", actor="something", object=animal_label::cow) -> like_cow : TERM
TERM conditional(condition=like_rabbit_2, consequence=like_cow) -> conditional_like : TERM
TERM activity(verb="visit", actor="something", object=animal_label::rabbit) -> visit_rabbit : TERM
TERM activity(verb="need", actor="something", object=animal_label::mouse) -> need_mouse : TERM
TERM conjunction(items=[visit_rabbit, need_mouse]) -> conjunction_need : TERM
TERM activity(verb="need", actor="something", object=animal_label::rabbit) -> need_rabbit : TERM
TERM conditional(condition=conjunction_need, consequence=need_rabbit) -> conditional_need : TERM
TERM activity(verb="like", actor="rabbit", object="bald_eagle") -> like_bald_eagle : TERM
TERM activity(verb="need", actor="bald_eagle", object=animal_label::rabbit) -> need
```
