```braincode
TERM  activity(verb="chase", actor="squirrel", object=animal_label::cow) -> chase_cow : TERM
TERM  activity(verb="eat", actor="squirrel", object=animal_label::cow) -> eat_cow : TERM
TERM  activity(verb="eat", actor="squirrel", object=animal_label::rabbit) -> eat_rabbit : TERM
TERM  activity(verb="chase", actor="squirrel", object=animal_label::rabbit) -> chase_rabbit : TERM
TERM  activity(verb="eat", actor="rabbit", object=animal_label::eagle) -> eat_eagle : TERM
TERM  activity(verb="chase", actor="cow", object=animal_label::rabbit) -> chase_rabbit_by_cow : TERM
TERM  activity(verb="chase", actor="cow", object=animal_label::squirrel) -> chase_squirrel_by_cow : TERM
TERM  activity(verb="eat", actor="cow", object=animal_label::rabbit) -> eat_rabbit_by_cow : TERM
TERM  activity(verb="eat", actor="cow", object=animal_label::squirrel) -> eat_squirrel_by_cow : TERM
TERM  activity(verb="eat", actor="rabbit", object=animal_label::cow) -> eat_cow_by_rabbit : TERM
TERM  activity(verb="eat", actor="squirrel", object=animal_label::cow) -> eat_cow_by_squirrel : TERM
TERM  activity(verb="eat", actor="squirrel", object=animal_label::rabbit) -> eat_rabbit_by_squirrel : TERM
TERM  activity(verb="eat", actor="squirrel", object=animal_label::eagle) -> eat_eagle_by_squirrel : TERM
TERM  activity(verb="chase", actor="cow", object=animal_label::squirrel) -> chase_squirrel
```
