```braincode
TERM  activity(verb="eat", actor="bear", object=animal_label::mouse) -> eat_mouse : TERM
TERM subject(kind="bear", qualifier=state_cold) -> cold_bear : TERM
TERM negation(target=activity(verb="visit", actor="bear", object=animal_label::rabbit)) -> neg_visit_rabbit : TERM
TERM activity(verb="eat", actor="cat", object=animal_label::bear) -> cat_eat_bear : TERM
TERM negation(target=cat_eat_bear) -> neg_cat_eat_bear : TERM
TERM activity(verb="eat", actor="cat", object=animal_label::rabbit) -> cat_eat_rabbit : TERM
TERM negation(target=activity(verb="visit", actor="cat", object=animal_label::mouse)) -> neg_cat_visit_mouse : TERM
TERM subject(kind="mouse", qualifier=color_label::blue) -> blue_mouse : TERM
TERM activity(verb="see", actor="mouse", object=animal_label::bear) -> mouse_see_bear : TERM
TERM activity(verb="visit", actor="mouse", object=animal_label::cat) -> mouse_visit_cat : TERM
TERM negation(target=mouse_visit_cat) -> neg_mouse_visit_cat : TERM
TERM activity(verb="visit", actor="mouse", object=animal_label::rabbit) -> mouse_visit_rabbit : TERM
TERM subject(kind="rabbit", qualifier=color_label::blue) -> blue_rabbit : TERM
TERM activity(verb="see", actor="rabbit", object=animal_label::bear) -> rabbit_see_bear : TERM
TERM subject(kind="someone", qualifier=state_cold) -> cold_person : TERM
TERM subject(kind="they", qualifier=shape_round) -> round_subject : TERM
TERM conditional(condition=cold_person, consequence=round_subject) -> cold_cond : TERM
TERM activity(verb="eat", actor="cat",
```
