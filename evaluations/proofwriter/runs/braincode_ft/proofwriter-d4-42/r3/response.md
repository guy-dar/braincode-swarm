```braincode
TERM  lexical_label(value=animal_label::dog) -> dog_label : TERM
TERM  lexical_label(value=animal_label::mouse) -> mouse_label : TERM
TERM  activity(verb="visit", actor="mouse", object=dog_label) -> visit_mouse_to_dog : TERM
TERM  activity(verb="eat", actor="rabbit", object=animal_label::mouse) -> eat_mouse_by_rabbit : TERM
TERM  activity(verb="like", actor="rabbit", object=animal_label::dog) -> like_dog_by_rabbit : TERM
TERM  activity(verb="like", actor="rabbit", object=animal_label::mouse) -> like_mouse_by_rabbit : TERM
TERM  activity(verb="visit", actor="mouse", object=animal_label::rabbit) -> visit_mouse_to_rabbit : TERM
TERM  activity(verb="like", actor="mouse", object=animal_label::rabbit) -> like_rabbit_by_mouse : TERM
TERM  activity(verb="like", actor="mouse", object=animal_label::dog) -> like_dog_by_mouse : TERM
TERM  activity(verb="visit", actor="mouse", object=animal_label::rabbit) -> visit_mouse_to_rabbit_2 : TERM
TERM  activity(verb="eat", actor="rabbit", object=animal_label::mouse) -> eat_mouse_by_rabbit_2 : TERM
TERM  activity(verb="like", actor="rabbit", object=animal_label::mouse) -> like_mouse_by_rabbit_2 : TERM
TERM  activity(verb="like", actor="rabbit", object=animal_label::dog) -> like_dog_by_rabbit_2 : TERM
TERM  activity(verb="visit", actor="mouse", object=animal_label::rabbit) -> visit_mouse_to_rabbit_3 : TERM
TERM  activity(verb="eat", actor="rabbit", object=animal_label::mouse) -> eat_mouse
```
