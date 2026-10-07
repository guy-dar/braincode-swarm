```braincode
TERM  subject(kind="Bob", qualifier=requirement(property="size", value=size_large)) -> bob_large : TERM
TERM lexical_label(value=color_label::red) -> red_label : TERM
TERM subject(kind="Bob", qualifier=requirement(property="color", value=red_label)) -> bob_red : TERM
TERM subject(kind="Bob", qualifier=requirement(property="smart", value=TRUE)) -> bob_smart : TERM
TERM subject(kind="Erin", qualifier=requirement(property="quiet", value=TRUE)) -> erin_quiet : TERM
TERM subject(kind="Fiona", qualifier=requirement(property="size", value=size_large)) -> fiona_large : TERM
TERM lexical_label(value=color_label::blue) -> blue_label : TERM
TERM subject(kind="Fiona", qualifier=requirement(property="color", value=blue_label)) -> fiona_blue : TERM
TERM subject(kind="Fiona", qualifier=requirement(property="temperature", value=state_cold)) -> fiona_cold : TERM
TERM subject(kind="Fiona", qualifier=requirement(property="smart", value=TRUE)) -> fiona_smart : TERM
TERM subject(kind="Gary", qualifier=requirement(property="color", value=red_label)) -> gary_red : TERM
TERM subject(kind="Gary", qualifier=requirement(property="smart", value=TRUE)) -> gary_smart : TERM
TERM requirement(property="quiet", value=TRUE) -> quiet_req : TERM
TERM subject(kind="Bob", qualifier=requirement(property="quiet", value=quiet_req)) -> bob_quiet : TERM
TERM subject(kind="Bob", qualifier=requirement(property="temperature", value=state_cold)) -> bob_cold : TERM
TERM conditional(condition=bob_quiet, consequence=bob_cold) -> conditional_1 : TERM
TERM requirement(property="color", value=red_label) -> color_req : TERM
TERM subject(kind="person", qualifier=color_req) -> person_color : TERM
TERM
```
