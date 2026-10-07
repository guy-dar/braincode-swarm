```braincode
TERM  lexical_label(value=color_label::green) -> lexical_label_2 : TERM
TERM  lexical_label(value=color_label::red) -> lexical_label_3 : TERM
TERM  lexical_label(value=animal_label::cow) -> lexical_label_4 : TERM
TERM  lexical_label(value=animal_label::tiger) -> lexical_label_5 : TERM
TERM  activity(verb="like", actor=lexical_label_4, object=lexical_label_5) -> activity_2 : TERM
TERM  activity(verb="meet_needs", actor=lexical_label_4, object=lexical_label_5) -> activity_3 : TERM
TERM  lexical_label(value=animal_label::mouse) -> lexical_label_6 : TERM
TERM  activity(verb="see", actor=lexical_label_6, object=lexical_label_2) -> activity_4 : TERM
TERM  activity(verb="like", actor=lexical_label_5, object=lexical_label_2) -> activity_5 : TERM
TERM  activity(verb="meet_needs", actor=lexical_label_5, object=lexical_label_6) -> activity_6 : TERM
TERM  character_trait(property="age", value="young") -> character_trait_2 : TERM
TERM  activity(verb="need", actor=lexical_label_5, object=character_trait_2) -> activity_7 : TERM
TERM  activity(verb="young", actor=lexical_label_5, object=lexical_label_3) -> activity_8 : TERM
TERM  activity(verb="see", actor=lexical_label_5, object=lexical_label_2) -> activity_9 : TERM
TERM  conjunction(items=[activity_7, activity_9]) -> conjunction_2 : TERM
TERM  activity(verb="see", actor=lexical_label_2, object=lexical_label_5) -> activity_10 : TERM
TERM
```
