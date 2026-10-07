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
TERM activity(verb="need", actor="something", object=animal_label::rabbit) -> something_need_rabbit : TERM
TERM conditional(condition=something_need_rabbit, consequence=nice_req) -> need_nice_cond : TERM
TERM conjunction(items=[size_large_req, shape_round_req]) -> size_shape_conj : TERM
TERM conditional(condition=size_shape_conj, consequence=nice_round_cond) -> size_shape_cond : TERM
TERM
```
