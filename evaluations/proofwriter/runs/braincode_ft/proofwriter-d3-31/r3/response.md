```braincode
TERM  lexical_label(value=animal_label::cat) -> lexical_label_2 : TERM
TERM lexical_label(value=color_label::red) -> lexical_label_3 : TERM
TERM subject(kind="cat", qualifier=lexical_label_3) -> subject_3 : TERM
TERM negation(target=subject_3) -> negation_2 : TERM
TERM lexical_label(value=animal_label::mouse) -> lexical_label_4 : TERM
TERM subject(kind="mouse") -> subject_4 : TERM
TERM subject(kind="tiger") -> subject_5 : TERM
TERM activity(actor="cow", object=animal_label::cat, verb="eat") -> activity_2 : TERM
TERM subject(kind="cow", qualifier=character_trait(property="age", value="young")) -> subject_6 : TERM
TERM activity(actor="mouse", object=animal_label::cat, verb="visit") -> activity_3 : TERM
TERM activity(actor="tiger", object=animal_label::cat, verb="eat") -> activity_4 : TERM
TERM subject(kind="tiger", qualifier=lexical_label_3) -> subject_7 : TERM
TERM activity(actor="tiger", object=animal_label::cow, verb="eat") -> activity_5 : TERM
TERM negation(target=activity_5) -> negation_3 : TERM
TERM activity(actor="tiger", object=animal_label::cat, verb="visit") -> activity_6 : TERM
TERM negation(target=activity_6) -> negation_4 : TERM
TERM activity(actor="tiger", object=animal_label::cow, verb="visit") -> activity_7 : TERM
TERM activity(actor="tiger", object=animal_label::mouse, verb="visit") -> activity_8 : TERM
TERM activity(actor="mouse", object=animal_label::tiger, verb="eat") -> activity_9 : TERM
TERM conditional(condition=activity_
```
