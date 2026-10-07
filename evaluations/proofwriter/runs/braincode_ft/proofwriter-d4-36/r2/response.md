```braincode
TERM  activity(verb="see", actor="someone", object=animal_label::cat) -> see_cat : TERM
TERM activity(verb="eat", actor="someone", object=lexical_label(color=color_label::red)) -> eat_red : TERM
TERM conjunction(items=[see_cat, eat_red]) -> conjunction_2 : TERM
TERM activity(verb="eat", actor="someone", object=animal_label::bear) -> eat_bear : TERM
TERM negation(target=eat_bear) -> negation_2 : TERM
TERM conditional(condition=conjunction_2, consequence=negation_2) -> q : TERM
TERM activity(verb="eat", actor="someone", object=animal_label::cat) -> eat_cat : TERM
TERM activity(verb="eat", actor="someone", object=animal_label::lion) -> eat_lion : TERM
TERM conjunction(items=[eat_cat, eat_lion]) -> conjunction_3 : TERM
TERM activity(verb="eat", actor="someone", object=animal_label::bear) -> eat_bear_2 : TERM
TERM negation(target=eat_bear_2) -> negation_3 : TERM
TERM conditional(condition=conjunction_3, consequence=negation_3) -> conjunction_4 : TERM
TERM activity(verb="eat", actor="someone", object=animal_label::baldeagle) -> eat_baldeagle : TERM
TERM lexical_label(value=color_label::green) -> lexical_label_2 : TERM
TERM activity(verb="eat", actor="someone", object=lexical_label_2) -> eat_green : TERM
TERM conjunction(items=[eat_baldeagle, eat_green]) -> conjunction_5 : TERM
TERM conditional(condition=conjunction_5, consequence=eat_bear) -> conjunction_6 : TERM
TERM activity(verb="eat", actor="someone", object=animal_label::cat) -> eat_cat_2 :
```
