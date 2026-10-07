```braincode
TERM  activity(verb="chase", actor="bald_eagle", object=animal_label::cow) -> chase_cow : TERM
TERM lexical_label(value=color_label::red) -> lexical_label_2 : TERM
TERM requirement(property="color", value=lexical_label_2) -> requirement_2 : TERM
TERM activity(verb="see", actor="bald_eagle", object=animal_label::squirrel) -> see_squirrel : TERM
TERM activity(verb="chase", actor="cow", object=animal_label::rabbit) -> chase_rabbit : TERM
TERM activity(verb="eat", actor="cow", object=animal_label::rabbit) -> eat_rabbit : TERM
TERM requirement(property="color", value=requirement_2) -> requirement_3 : TERM
TERM activity(verb="chase", actor="rabbit", object=animal_label::cow) -> chase_rabbit_2 : TERM
TERM activity(verb="eat", actor="rabbit", object=animal_label::eagle) -> eat_eagle : TERM
TERM requirement(property="nice", value=TRUE) -> requirement_4 : TERM
TERM requirement(property="rough", value=TRUE) -> requirement_5 : TERM
TERM activity(verb="eat", actor="squirrel", object=animal_label::cow) -> eat_squirrel : TERM
TERM activity(verb="eat", actor="squirrel", object=animal_label::rabbit) -> eat_squirrel_2 : TERM
TERM requirement(property="nice", value=TRUE) -> requirement_6 : TERM
TERM activity(verb="see", actor="squirrel", object=animal_label::rabbit) -> see_rabbit : TERM
TERM activity(verb="chase", actor="something", object=animal_label::squirrel) -> chase_squirrel : TERM
TERM activity(verb="chase", actor="squirrel", object=animal_label::cow) -> chase_squirrel
```
