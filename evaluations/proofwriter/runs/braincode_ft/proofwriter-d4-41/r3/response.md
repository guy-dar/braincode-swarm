```braincode
TERM  activity(verb="chase", actor="dog", object=animal_label::lion) -> chase_lion : TERM
TERM  activity(verb="chase", actor="dog", object=animal_label::rabbit) -> chase_rabbit : TERM
TERM  activity(verb="like", actor="dog", object=animal_label::lion) -> like_lion : TERM
TERM  activity(verb="like", actor="dog", object=animal_label::mouse) -> like_mouse : TERM
TERM  lexical_label(value=color_label::blue) -> lexical_label_2 : TERM
TERM  activity(verb="chase", actor="mouse", object=animal_label::rabbit) -> chase_mouse_rabbit : TERM
TERM  activity(verb="like", actor="mouse", object=animal_label::dog) -> like_mouse_dog : TERM
TERM  activity(verb="like", actor="mouse", object=animal_label::lion) -> like_mouse_lion : TERM
TERM  activity(verb="chase", actor="rabbit", object=animal_label::lion) -> chase_rabbit_lion : TERM
TERM  requirement(property="shape", value=shape_round) -> requirement_2 : TERM
TERM  activity(verb="see", actor="something", object=animal_label::lion) -> see_lion : TERM
TERM  activity(verb="chase", actor="something", object=animal_label::lion) -> chase_lion_2 : TERM
TERM  conditional(condition=requirement_2, consequence=see_lion) -> conditional_2 : TERM
TERM  activity(verb="like", actor="mouse", object=animal_label::mouse) -> like_mouse_mouse : TERM
TERM  requirement(property="state", value=state_cold) -> requirement_3 : TERM
TERM  activity(verb="see", actor="something", object=animal_label::lion) -> see_lion_2 :
```
