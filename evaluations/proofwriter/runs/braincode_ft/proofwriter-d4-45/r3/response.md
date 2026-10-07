```braincode
TERM  subject(kind="Bob", qualifier=size_large) -> bob_large : TERM
TERM lexical_label(value=color_label::red) -> red_label : TERM
TERM subject(kind="Bob", qualifier=red_label) -> bob_red : TERM
TERM subject(kind="Bob", qualifier=size_large) -> bob_smart : TERM
TERM subject(kind="Erin", qualifier=size_large) -> erin_quiet : TERM
TERM subject(kind="Fiona", qualifier=size_large) -> fiona_cold : TERM
TERM lexical_label(value=color_label::blue) -> blue_label : TERM
TERM subject(kind="Fiona", qualifier=blue_label) -> fiona_smart : TERM
TERM subject(kind="Fiona", qualifier=state_cold) -> fiona_cold_temp : TERM
TERM subject(kind="Gary", qualifier=size_large) -> gary_smart : TERM
TERM subject(kind="Gary", qualifier=red_label) -> gary_red : TERM
TERM requirement(property="quiet", value=TRUE) -> quiet_req : TERM
TERM subject(kind="Bob", qualifier=quiet_req) -> bob_quiet : TERM
TERM subject(kind="Bob", qualifier=state_cold) -> bob_cold : TERM
TERM conditional(condition=bob_quiet, consequence=bob_cold) -> conditional_bob : TERM
TERM requirement(property="color", value=red_label) -> color_req : TERM
TERM subject(kind="person", qualifier=color_req) -> person_color : TERM
TERM subject(kind="person", qualifier=quiet_req) -> person_quiet : TERM
TERM conditional(condition=person_color, consequence=person_quiet) -> conditional_person : TERM
TERM requirement(property="color", value=red_label) -> color_req_2 : TERM
TERM requirement(property="temperature", value=state_cold) -> temp_req : TERM
TERM conjunction(items=[color_req_2, temp_req]) -> conjunction_req : TERM
TERM subject(kind="person", qualifier=con
```
