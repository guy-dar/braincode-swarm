```braincode
TERM  activity(verb="chase", actor="dog", object=animal_label::lion) -> chase_lion : TERM
TERM  activity(verb="chase", actor="dog", object=animal_label::tiger) -> chase_tiger : TERM
TERM  requirement(property="size", value=size_large) -> size_large_req : TERM
TERM  activity(verb="like", actor="dog", object=animal_label::tiger) -> like_tiger : TERM
TERM  activity(verb="see", actor="dog", object=animal_label::lion) -> see_lion : TERM
TERM  activity(verb="see", actor="lion", object=animal_label::mouse) -> see_mouse : TERM
TERM  activity(verb="chase", actor="mouse", object=animal_label::dog) -> chase_mouse_dog : TERM
TERM  activity(verb="chase", actor="mouse", object=animal_label::lion) -> chase_mouse_lion : TERM
TERM  activity(verb="like", actor="mouse", object=animal_label::tiger) -> like_mouse_tiger : TERM
TERM  activity(verb="like", actor="tiger", object=animal_label::mouse) -> like_tiger_mouse : TERM
TERM  requirement(property="kind", value=TRUE) -> kind_req : TERM
TERM  activity(verb="chase", actor="someone", object=animal_label::mouse) -> chase_mouse_someone : TERM
TERM  requirement(property="shape", value=shape_round) -> shape_round_req : TERM
TERM  activity(verb="like", actor="someone", object=animal_label::dog) -> like_dog_someone : TERM
TERM  requirement(property="color", value=color_label::green) -> color_green_req : TERM
TERM  activity(verb="chase", actor="someone", object=animal_label::tiger) -> chase_tiger_someone
```
