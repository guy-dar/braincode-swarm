```braincode
TERM  activity(verb="eat", actor="bear", object=animal_label::mouse) -> eat_mouse : TERM
TERM  activity(verb="visit", actor="bear", object=animal_label::rabbit) -> visit_rabbit : TERM
TERM  activity(verb="eat", actor="cat", object=animal_label::bear) -> eat_bear : TERM
TERM  activity(verb="eat", actor="cat", object=animal_label::rabbit) -> eat_rabbit : TERM
TERM  activity(verb="visit", actor="cat", object=animal_label::mouse) -> visit_mouse : TERM
TERM  subject(kind="mouse", qualifier="kind") -> mouse_kind : TERM
TERM  activity(verb="see", actor="mouse", object=animal_label::bear) -> see_bear : TERM
TERM  activity(verb="visit", actor="mouse", object=animal_label::cat) -> visit_cat : TERM
TERM  activity(verb="visit", actor="mouse", object=animal_label::rabbit) -> visit_rabbit_2 : TERM
TERM  lexical_label(value=color_label::blue) -> blue_label : TERM
TERM  activity(verb="see", actor="rabbit", object=animal_label::bear) -> see_bear_2 : TERM
TERM  subject(kind="someone", qualifier="cold") -> someone_cold : TERM
TERM  subject(kind="they", qualifier="round") -> they_round : TERM
TERM  conditional(condition=someone_cold, consequence=they_round) -> cold_round : TERM
TERM  activity(verb="eat", actor="cat", object=animal_label::mouse) -> cat_eat_mouse : TERM
TERM  negation(target=cat_eat_mouse) -> cat_not_eat_mouse : TERM
TERM  conjunction(items=[mouse_kind, cat_not_eat_mouse]) -> conjunction_2 : TERM
TERM  subject(kind="cat", qualifier="round
```
