```braincode
TERM  lexical_label(value=color_label::red) -> lexical_label_2 : TERM
TERM  subject(kind="cat", qualifier=lexical_label_2) -> subject_2 : TERM
TERM  negation(target=subject_2) -> negation_2 : TERM
TERM  subject(kind="mouse") -> subject_3 : TERM
TERM  subject(kind="tiger") -> subject_4 : TERM
TERM  activity(verb="eat", actor="cow", object=animal_label::cat) -> activity_2 : TERM
TERM  subject(kind="cow", qualifier=character_trait(property="age", value="young")) -> subject_5 : TERM
TERM  activity(verb="visit", actor="mouse", object=animal_label::cat) -> activity_3 : TERM
TERM  activity(verb="eat", actor="tiger", object=animal_label::cat) -> activity_4 : TERM
TERM  activity(verb="eat", actor="tiger", object=animal_label::cow) -> activity_5 : TERM
TERM  negation(target=activity_5) -> negation_3 : TERM
TERM  subject(kind="tiger", qualifier=lexical_label_2) -> subject_6 : TERM
TERM  activity(verb="eat", actor="tiger", object=animal_label::cow) -> activity_6 : TERM
TERM  activity(verb="eat", actor="tiger", object=animal_label::mouse) -> activity_7 : TERM
TERM  activity(verb="eat", actor="mouse", object=animal_label::tiger) -> activity_8 : TERM
TERM  conditional(condition=activity_7, consequence=activity_8) -> conditional_2 : TERM
TERM  activity(verb="eat", actor="mouse", object=animal_label::tiger) -> activity_9 : TERM
TERM  activity(verb="eat", actor="mouse", object=
```
