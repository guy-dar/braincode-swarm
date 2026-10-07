```braincode
TERM  lexical_label(value=animal_label::dog) -> lexical_label_2 : TERM
TERM  lexical_label(value=animal_label::tiger) -> lexical_label_3 : TERM
TERM  lexical_label(value=animal_label::lion) -> lexical_label_4 : TERM
TERM  subject(kind="dog", qualifier=lexical_label_2) -> subject_2 : TERM
TERM  subject(kind="tiger", qualifier=lexical_label_3) -> subject_3 : TERM
TERM  subject(kind="lion", qualifier=lexical_label_4) -> subject_4 : TERM
TERM  activity(actor="dog", object=subject_3, verb="visit") -> activity_2 : TERM
TERM  activity(actor="lion", object=subject_2, verb="visit") -> activity_3 : TERM
TERM  conjunction(items=[activity_2, activity_3]) -> conjunction_2 : TERM
TERM  activity(actor="lion", object=subject_2, verb="visit") -> activity_4 : TERM
TERM  subject(kind="lion", qualifier=subject_4) -> subject_5 : TERM
TERM  subject(kind="lion", qualifier=subject_5) -> subject_6 : TERM
TERM  activity(actor="lion", object=subject_6, verb="visit") -> activity_5 : TERM
TERM  activity(actor="dog", object=subject_4, verb="visit") -> activity_6 : TERM
TERM  subject(kind="dog", qualifier=subject_2) -> subject_7 : TERM
TERM  subject(kind="dog", qualifier=subject_7) -> subject_8 : TERM
TERM  activity(actor="dog", object=subject_8, verb="visit") -> activity_7 : TERM
TERM  subject(kind="dog", qualifier=subject_7) -> subject_9 : TERM
TERM  subject(kind="dog", qualifier=subject_9) -> subject_
```
