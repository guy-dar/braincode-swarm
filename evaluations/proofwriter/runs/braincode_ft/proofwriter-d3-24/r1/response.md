```braincode
TERM  activity(verb="eat", actor="bear", object=animal_label::cat) -> eat_cat : TERM
TERM  activity(verb="visit", actor="bear", object=animal_label::dog) -> visit_dog : TERM
TERM  activity(verb="visit", actor="cat", object=animal_label::bear) -> cat_visit : TERM
TERM  activity(verb="eat", actor="dog", object=animal_label::cat) -> dog_eat_cat : TERM
TERM  lexical_label(value=color_label::blue) -> blue_label : TERM
TERM  has_attribute(attribute=blue_label, subject="dog") -> dog_blue : TERM
TERM  activity(verb="eat", actor="bear", object=animal_label::mouse) -> eat_mouse : TERM
TERM  activity(verb="visit", actor="bear", object=animal_label::mouse) -> mouse_visit : TERM
TERM  activity(verb="eat", actor="someone", object=animal_label::cat) -> eat_cat_by_person : TERM
TERM  activity(verb="visit", actor="someone", object=animal_label::cat) -> visit_cat_by_person : TERM
TERM  conditional(condition=eat_cat_by_person, consequence=visit_cat_by_person) -> conditional_cat : TERM
TERM  activity(verb="eat", actor="someone", object=animal_label::mouse) -> eat_mouse_by_person : TERM
TERM  conditional(condition=eat_cat_by_person, consequence=eat_mouse_by_person) -> conditional_mouse : TERM
TERM  activity(verb="visit", actor="dog", object=animal_label::cat) -> dog_visit_cat : TERM
TERM  activity(verb="like", actor="dog", object=animal_label::cat) -> dog_like_cat : TERM
TERM  conjunction(items=[dog_visit_cat, dog_like_cat]) -> conjunction_dog : TERM
TERM  conditional(condition=conjunction_dog, consequence=dog_like_cat
```
