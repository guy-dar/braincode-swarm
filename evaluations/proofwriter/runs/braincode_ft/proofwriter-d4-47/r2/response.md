```braincode
TERM  activity(verb="see", actor="baldeagle", object=animal_label::cat) -> see_cat : TERM
TERM requirement(property="shape", value=shape_round) -> shape_round_req : TERM
TERM activity(verb="need", actor="cat", object=animal_label::rabbit) -> need_rabbit : TERM
TERM activity(verb="see", actor="cat", object=animal_label::lion) -> see_lion : TERM
TERM activity(verb="visit", actor="cat", object=animal_label::lion) -> visit_lion : TERM
TERM requirement(property="size", value=size_large) -> size_large_req : TERM
TERM requirement(property="state", value=state_cold) -> state_cold_req : TERM
TERM requirement(property="nice", value=TRUE) -> nice_req : TERM
TERM activity(verb="visit", actor="lion", object=animal_label::rabbit) -> lion_visit : TERM
TERM requirement(property="nice", value=TRUE) -> lion_nice_req : TERM
TERM requirement(property="shape", value=shape_round) -> lion_shape_round_req : TERM
TERM activity(verb="see", actor="rabbit", object=animal_label::cat) -> rabbit_see_cat : TERM
TERM conditional(condition=nice_req, consequence=shape_round_req) -> nice_round_cond : TERM
TERM conjunction(items=[nice_round_cond, activity(verb="see", actor="something", object=animal_label::rabbit)]) -> conjunction_2 : TERM
TERM activity(verb="need", actor="something", object=animal_label::lion) -> lion_need : TERM
TERM conditional(condition=conjunction_2, consequence=lion_need) -> conjunction_2_cond : TERM
TERM conjunction(items=[state_cold_req, shape_round_req]) -> conjunction_3 : TERM
TERM conditional(condition=conjunction_3, consequence=nice_round_cond) -> conjunction_3_cond : TERM
TERM
```
