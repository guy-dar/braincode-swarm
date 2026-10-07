```braincode
TERM  activity(verb="see", actor="baldeagle", object=animal_label::cat) -> see_cat : TERM
TERM requirement(property="shape", value=shape_round) -> shape_round_req : TERM
TERM activity(verb="need", actor=animal_label::cat, object=animal_label::rabbit) -> need_rabbit : TERM
TERM activity(verb="see", actor="cat", object=animal_label::lion) -> see_lion : TERM
TERM activity(verb="visit", actor="cat", object=animal_label::lion) -> visit_lion : TERM
TERM requirement(property="size", value=size_large) -> size_large_req : TERM
TERM requirement(property="state", value=state_cold) -> state_cold_req : TERM
TERM requirement(property="nice", value=TRUE) -> nice_req : TERM
TERM activity(verb="visit", actor="lion", object=animal_label::rabbit) -> lion_visit_rabbit : TERM
TERM requirement(property="nice", value=TRUE) -> lion_nice_req : TERM
TERM requirement(property="shape", value=shape_round) -> lion_shape_round_req : TERM
TERM activity(verb="see", actor="rabbit", object=animal_label::cat) -> rabbit_see_cat : TERM
TERM conditional(condition=nice_req, consequence=see_cat) -> conditional_2 : TERM
TERM conjunction(items=[nice_req, see_cat]) -> conjunction_2 : TERM
TERM conditional(condition=conjunction_2, consequence=need_rabbit) -> conditional_3 : TERM
TERM conjunction(items=[size_large_req, state_cold_req]) -> conjunction_3 : TERM
TERM conditional(condition=conjunction_3, consequence=nice_req) -> conditional_4 : TERM
TERM activity(verb="see", actor="baldeagle", object=animal_label::rabbit) -> see_rabbit : TERM
TERM conjunction(items=[see_rabbit, nice_req])
```
