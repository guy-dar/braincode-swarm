```braincode
TERM  character(name="Bob") -> bob_char : TERM
TERM character(name="Fiona") -> fiona_char : TERM
TERM character(name="Gary") -> gary_char : TERM
TERM character(name="Harry") -> harry_char : TERM
TERM lexical_label(value=color_label::white) -> white_label : TERM
TERM lexical_label(value=color_label::blue) -> blue_label : TERM
TERM character_trait(property="color", value=white_label) -> bob_color : TERM
TERM character_trait(property="state", value=state_cold) -> cold_trait : TERM
TERM character_trait(property="texture", value="rough") -> rough_trait : TERM
TERM character_trait(property="size", value=size_large) -> large_trait : TERM
TERM character_trait(property="personality", value="nice") -> nice_trait : TERM
TERM character_trait(property="texture", value="furry") -> furry_trait : TERM
TERM subject(kind="Bob", qualifier=bob_color) -> bob_subject : TERM
TERM subject(kind="Fiona", qualifier=cold_trait) -> fiona_subject : TERM
TERM subject(kind="Fiona", qualifier=rough_trait) -> fiona_rough_subject : TERM
TERM subject(kind="Gary", qualifier=large_trait) -> gary_subject : TERM
TERM subject(kind="Gary", qualifier=cold_trait) -> gary_cold_subject : TERM
TERM subject(kind="Gary", qualifier=rough_trait) -> gary_rough_subject : TERM
TERM subject(kind="Gary", qualifier=blue_label) -> gary_blue_subject : TERM
TERM subject(kind="Harry", qualifier=nice_trait) -> harry_subject : TERM
TERM conjunction(items=[bob_color, cold_trait]) -> bob_conj : TERM
TERM conditional(condition=bob_conj, consequence=blue_label) -> bob_cond : TERM
TERM subject(kind="Bob", qualifier=nice_trait) -> bob_nice_subject : TERM
TERM subject(kind="Bob
```
