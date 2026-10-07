```braincode
TERM  lexical_label(value=color_label::red) -> lexical_label_2 : TERM
TERM  subject(kind="cat", qualifier=lexical_label_2) -> subject_2 : TERM
TERM  negation(target=subject_2) -> negation_2 : TERM
TERM  lexical_label(value=animal_label::mouse) -> lexical_label_3 : TERM
TERM  subject(kind="mouse", qualifier=lexical_label_3) -> subject_3 : TERM
TERM  subject(kind="cat", qualifier=subject_3) -> subject_4 : TERM
TERM  negation(target=subject_4) -> negation_3 : TERM
TERM  subject(kind="cow", qualifier=animal_label::cow) -> subject_5 : TERM
TERM  activity(actor="cow", object=animal_label::cat, verb="eat") -> activity_2 : TERM
TERM  subject(kind="cow", qualifier=animal_label::cow) -> subject_6 : TERM
TERM  activity(actor="mouse", object=animal_label::cat, verb="visit") -> activity_3 : TERM
TERM  activity(actor="tiger", object=animal_label::cat, verb="eat") -> activity_4 : TERM
TERM  subject(kind="tiger", qualifier=animal_label::tiger) -> subject_7 : TERM
TERM  activity(actor="tiger", object=animal_label::cow, verb="eat") -> activity_5 : TERM
TERM  negation(target=activity_5) -> negation_4 : TERM
TERM  subject(kind="tiger", qualifier=animal_label::tiger) -> subject_8 : TERM
TERM  activity(actor="tiger", object=animal_label::cat, verb="visit") -> activity_6 : TERM
TERM  negation(target=activity_6) -> negation_5 : TERM
TERM  activity(actor="tiger", object=animal_label::cow,
```
