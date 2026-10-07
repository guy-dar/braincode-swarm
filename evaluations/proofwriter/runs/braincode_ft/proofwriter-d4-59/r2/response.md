```braincode
TERM  lexical_label(value=animal_label::baldeagle) -> lexical_label_2 : TERM
TERM lexical_label(value=animal_label::dog) -> lexical_label_3 : TERM
TERM lexical_label(value=animal_label::tiger) -> lexical_label_4 : TERM
TERM lexical_label(value=animal_label::lion) -> lexical_label_5 : TERM
TERM lexical_label(value=color_label::red) -> lexical_label_6 : TERM
TERM lexical_label(value=color_label::blue) -> lexical_label_7 : TERM
TERM subject(kind="bald_eagle", qualifier="kind") -> subject_2 : TERM
TERM subject(kind="bald_eagle", qualifier="red") -> subject_3 : TERM
TERM activity(actor="bald_eagle", object=animal_label::dog, verb="need") -> activity_2 : TERM
TERM activity(actor="bald_eagle", object=animal_label::tiger, verb="visit") -> activity_3 : TERM
TERM subject(kind="dog", qualifier=size_large) -> subject_4 : TERM
TERM activity(actor="dog", object=animal_label::lion, verb="like") -> activity_4 : TERM
TERM activity(actor="dog", object=animal_label::tiger, verb="like") -> activity_5 : TERM
TERM activity(actor="dog", object=animal_label::lion, verb="need") -> activity_6 : TERM
TERM activity(actor="dog", object=animal_label::tiger, verb="need") -> activity_7 : TERM
TERM activity(actor="dog", object=animal_label::baldeagle, verb="visit") -> activity_8 : TERM
TERM subject(kind="lion", qualifier="red") -> subject_5 : TERM
TERM activity(actor="lion", object=animal_label::baldeagle, verb="like") -> activity_9 : TERM
TERM subject(kind="tiger", qualifier=size_large) -> subject
```
