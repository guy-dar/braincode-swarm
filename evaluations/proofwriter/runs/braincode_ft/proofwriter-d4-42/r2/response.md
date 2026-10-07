```braincode
TERM  lexical_label(value=animal_label::dog) -> lexical_label_2 : TERM
TERM  lexical_label(value=animal_label::rabbit) -> lexical_label_3 : TERM
TERM  lexical_label(value=animal_label::mouse) -> lexical_label_4 : TERM
TERM  activity(verb="visit", actor="bald_eagle", object=lexical_label_2) -> activity_2 : TERM
TERM  activity(verb="visit", actor="bald_eagle", object=lexical_label_3) -> activity_3 : TERM
TERM  activity(verb="visit", actor="bald_eagle", object=lexical_label_4) -> activity_4 : TERM
TERM  activity(verb="visit", actor="dog", object=lexical_label_2) -> activity_5 : TERM
TERM  activity(verb="eat", actor="rabbit", object=lexical_label_4) -> activity_6 : TERM
TERM  activity(verb="like", actor="rabbit", object=lexical_label_4) -> activity_7 : TERM
TERM  activity(verb="like", actor="rabbit", object=lexical_label_2) -> activity_8 : TERM
TERM  activity(verb="like", actor="mouse", object=lexical_label_2) -> activity_9 : TERM
TERM  activity(verb="visit", actor="mouse", object=lexical_label_3) -> activity_10 : TERM
TERM  activity(verb="visit", actor="mouse", object=lexical_label_4) -> activity_11 : TERM
TERM  conjunction(items=[activity_10, activity_11]) -> conjunction_2 : TERM
TERM  activity(verb="eat", actor="rabbit", object=lexical_label_4) -> activity_12 : TERM
TERM  requirement(property="rough", value=TRUE) -> requirement_2 : TERM
TERM  requirement(property="size",
```
