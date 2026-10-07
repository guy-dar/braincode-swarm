```braincode
TERM  activity(verb="chase", actor="dog", object=animal_label::lion) -> chase_lion : TERM
TERM activity(verb="chase", actor="dog", object=animal_label::rabbit) -> chase_rabbit : TERM
TERM activity(verb="like", actor="dog", object=animal_label::lion) -> like_lion : TERM
TERM activity(verb="like", actor="dog", object=animal_label::mouse) -> like_mouse : TERM
TERM lexical_label(value=color_label::blue) -> lexical_label_2 : TERM
TERM activity(verb="chase", actor="rabbit", object=animal_label::mouse) -> chase_mouse : TERM
TERM activity(verb="like", actor="mouse", object=animal_label::rabbit) -> like_rabbit : TERM
TERM activity(verb="like", actor="mouse", object=animal_label::lion) -> like_lion_2 : TERM
TERM activity(verb="chase", actor="rabbit", object=animal_label::lion) -> chase_lion_2 : TERM
TERM requirement(property="shape", value=shape_round) -> requirement_2 : TERM
TERM activity(verb="see", actor="something", object=requirement_2) -> see_round : TERM
TERM activity(verb="chase", actor="something", object=animal_label::lion) -> chase_lion_3 : TERM
TERM conditional(condition=see_round, consequence=chase_lion_3) -> conditional_2 : TERM
TERM activity(verb="see", actor="something", object=animal_label::mouse) -> see_mouse : TERM
TERM requirement(property="state", value=state_cold) -> requirement_3 : TERM
TERM conditional(condition=see_mouse, consequence=requirement_3) -> conditional_3 : TERM
TERM activity(verb="see", actor="something", object=animal_label::mouse) -> see_mouse_2
```
