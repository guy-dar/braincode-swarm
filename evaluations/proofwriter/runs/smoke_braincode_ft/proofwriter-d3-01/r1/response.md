```braincode
TERM  activity(verb="eat", actor="cow", object=animal_label::lion) -> eat_cow_lion : TERM
TERM character_trait(property="age", value="young") -> young_cow : TERM
TERM activity(verb="like", actor="cow", object=animal_label::squirrel) -> like_cow_squirrel : TERM
TERM activity(verb="eat", actor="lion", object=animal_label::rabbit) -> eat_lion_rabbit : TERM
TERM activity(verb="eat", actor="lion", object=animal_label::squirrel) -> eat_lion_squirrel : TERM
TERM negation(target=like_cow_squirrel) -> dislike_cow_squirrel : TERM
TERM lexical_label(value=color_label::blue) -> blue_rabbit : TERM
TERM activity(verb="like", actor="rabbit", object=animal_label::cow) -> like_rabbit_cow : TERM
TERM activity(verb="like", actor="rabbit", object=animal_label::lion) -> like_rabbit_lion : TERM
TERM activity(verb="like", actor="squirrel", object=animal_label::lion) -> like_squirrel_lion : TERM
TERM activity(verb="like", actor="squirrel", object=animal_label::rabbit) -> like_squirrel_rabbit : TERM
TERM activity(verb="visit", actor="someone", object=animal_label::lion) -> visit_lion : TERM
TERM activity(verb="eat", actor="lion", object=animal_label::cow) -> eat_lion_cow : TERM
TERM conditional(condition=visit_lion, consequence=eat_lion_cow) -> conditional_visit_eat : TERM
TERM activity(verb="visit", actor="someone", object=animal_label::cow) -> visit_cow : TERM
TERM character_trait(property="shape", value=shape_round) -> round_cow : TERM
TERM conditional(condition=visit_cow
```
