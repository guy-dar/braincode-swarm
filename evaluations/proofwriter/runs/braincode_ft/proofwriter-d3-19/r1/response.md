```braincode
TERM  activity(verb="chase", actor="bald eagle", object=animal_label::lion) -> chase_lion : TERM
TERM  requirement(property="color", value=color_label::green) -> green_req : TERM
TERM  negation(target=green_req) -> neg_green_req : TERM
TERM  requirement(property="shape", value=shape_round) -> round_req : TERM
TERM  activity(verb="like", actor="bald eagle", object=animal_label::lion) -> like_lion : TERM
TERM  requirement(property="color", value=color_label::red) -> red_req : TERM
TERM  activity(verb="chase", actor="lion", object=animal_label::dog) -> chase_dog : TERM
TERM  negation(target=chase_dog) -> neg_chase_dog : TERM
TERM  requirement(property="age", value="young") -> young_req : TERM
TERM  activity(verb="chase", actor="rabbit", object=animal_label::dog) -> chase_dog_2 : TERM
TERM  activity(verb="eat", actor="rabbit", object=animal_label::lion) -> eat_lion : TERM
TERM  activity(verb="chase", actor="something", object=animal_label::dog) -> chase_dog_3 : TERM
TERM  activity(verb="like", actor="something", object=animal_label::rabbit) -> like_rabbit : TERM
TERM  conditional(condition=chase_dog_3, consequence=like_rabbit) -> cond_like_rabbit : TERM
TERM  activity(verb="chase", actor="lion", object=animal_label::baldeagle) -> chase_baldeagle : TERM
TERM  requirement(property="size", value=size_large) -> large_size_req : TERM
TERM  activity(verb="chase", actor="something", object=animal_label::rabbit) -> chase_rabbit :
```
