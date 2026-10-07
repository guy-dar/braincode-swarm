```braincode
TERM  activity(verb="chase", actor="bear", object=animal_label::lion) -> chase_lion : TERM
TERM  activity(verb="chase", actor="bear", object=animal_label::squirrel) -> chase_squirrel : TERM
TERM  activity(verb="chase", actor="lion", object=animal_label::bear) -> chase_bear : TERM
TERM  lexical_label(value=animal_label::bear) -> lexical_label_2 : TERM
TERM  has_state(state=state_cold, subject=lexical_label_2) -> has_state_2 : TERM
TERM  activity(verb="need", actor="bear", object=animal_label::lion) -> need_lion : TERM
TERM  activity(verb="need", actor="bear", object=animal_label::squirrel) -> need_squirrel : TERM
TERM  activity(verb="see", actor="lion", object=animal_label::rabbit) -> see_rabbit : TERM
TERM  activity(verb="see", actor="lion", object=animal_label::squirrel) -> see_squirrel : TERM
TERM  activity(verb="need", actor="rabbit", object=animal_label::lion) -> need_rabbit : TERM
TERM  lexical_label(value=color_label::red) -> lexical_label_3 : TERM
TERM  activity(verb="need", actor="something", object=animal_label::rabbit) -> need_rabbit_2 : TERM
TERM  subject(kind="rabbit", qualifier=lexical_label_3) -> subject_2 : TERM
TERM  conditional(condition=need_rabbit_2, consequence=subject_2) -> conditional_2 : TERM
TERM  activity(verb="see", actor="something", object=animal_label::rabbit) -> see_rabbit_2 : TERM
TERM  activity(verb="see", actor="something", object=animal_label::bear) -> see_bear : TERM
```
