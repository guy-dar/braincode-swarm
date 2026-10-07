```braincode
TERM  activity(verb="visit", actor="bald_eagle", object=animal_label::cow) -> visit_cow : TERM
TERM activity(verb="like", actor="cow", object=animal_label::rabbit) -> like_rabbit : TERM
TERM activity(verb="visit", actor="cow", object=animal_label::mouse) -> visit_mouse : TERM
TERM lexical_label(value=color_label::green) -> lexical_label_2 : TERM
TERM requirement(property="color", value=lexical_label_2) -> requirement_2 : TERM
TERM requirement(property="personality", value="nice") -> requirement_3 : TERM
TERM requirement(property="age", value="young") -> requirement_4 : TERM
TERM activity(verb="like", actor="rabbit", object=animal_label::mouse) -> like_mouse : TERM
TERM activity(verb="like", actor="cow", object=animal_label::rabbit) -> like_rabbit_2 : TERM
TERM activity(verb="visit", actor="cow", object=animal_label::rabbit) -> visit_rabbit : TERM
TERM activity(verb="need", actor="cow", object=animal_label::rabbit) -> need_rabbit : TERM
TERM activity(verb="like", actor="cow", object="bald_eagle") -> like_bald_eagle : TERM
TERM activity(verb="visit", actor="cow", object="bald_eagle") -> visit_bald_eagle : TERM
TERM activity(verb="like", actor="rabbit", object="bald_eagle") -> like_rabbit_3 : TERM
TERM activity(verb="need", actor="rabbit", object="bald_eagle") -> need_bald_eagle : TERM
TERM activity(verb="like", actor="cow", object="bald_eagle") -> like_cow : TERM
TERM activity(verb="like", actor="cow", object="bald_eagle")
```
