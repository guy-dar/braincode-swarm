```braincode
TERM  character(name="Bob") -> bob_char : TERM
TERM  character(name="Fiona") -> fiona_char : TERM
TERM  character(name="Gary") -> gary_char : TERM
TERM  character(name="Harry") -> harry_char : TERM
TERM  lexical_label(value=color_label::white) -> white_label : TERM
TERM  lexical_label(value=color_label::blue) -> blue_label : TERM
TERM  character_trait(property="color", value=white_label) -> bob_color : TERM
TERM  character_trait(property="state", value=state_cold) -> fiona_state : TERM
TERM  character_trait(property="texture", value="rough") -> rough_texture : TERM
TERM  character_trait(property="size", value=size_large) -> large_size : TERM
TERM  character_trait(property="personality", value="nice") -> bob_nice : TERM
TERM  character_trait(property="texture", value="furry") -> furry_texture : TERM
TERM  character_trait(property="color", value=blue_label) -> fiona_color : TERM
TERM  subject(kind="Bob", qualifier=bob_color) -> bob_subject : TERM
TERM  subject(kind="Fiona", qualifier=fiona_state) -> fiona_subject : TERM
TERM  subject(kind="Fiona", qualifier=rough_texture) -> fiona_rough : TERM
TERM  subject(kind="Gary", qualifier=large_size) -> gary_subject : TERM
TERM  subject(kind="Gary", qualifier=rough_texture) -> gary_rough : TERM
TERM  subject(kind="Gary", qualifier=bob_color) -> gary_white : TERM
TERM  subject(kind="Harry", qualifier=bob_nice) -> harry_nice : TERM
TERM  conjunction(items=[bob_color, fiona_state]) -> conjunction_2 : TERM
TERM  conditional(condition=conjunction_2, consequence=fiona_color) -> conditional_2 : TERM
```
