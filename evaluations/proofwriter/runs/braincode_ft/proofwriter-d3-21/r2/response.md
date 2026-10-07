```braincode
TERM  character(name="Bob") -> bob_char : TERM
TERM  character(name="Fiona") -> fiona_char : TERM
TERM  character(name="Gary") -> gary_char : TERM
TERM  character(name="Harry") -> harry_char : TERM
TERM  lexical_label(value=color_label::white) -> white_label : TERM
TERM  lexical_label(value=color_label::blue) -> blue_label : TERM
TERM  character_trait(property="color", value=white_label) -> bob_color : TERM
TERM  character_trait(property="state", value=state_cold) -> cold_trait : TERM
TERM  character_trait(property="texture", value="rough") -> rough_trait : TERM
TERM  character_trait(property="size", value=size_large) -> large_trait : TERM
TERM  character_trait(property="personality", value="nice") -> nice_trait : TERM
TERM  character_trait(property="texture", value="furry") -> furry_trait : TERM
TERM  character_trait(property="color", value=blue_label) -> fiona_color : TERM
TERM  subject(kind="Bob", qualifier=bob_color) -> bob_subject : TERM
TERM  CLAIM statement(fact=bob_subject) BY role_user STATUS asserted SOURCE "t1:s2" -> bob_claim : CLAIM
TERM  subject(kind="Fiona", qualifier=fiona_color) -> fiona_subject : TERM
TERM  CLAIM statement(fact=fiona_subject) BY role_user STATUS asserted SOURCE "t1:s3" -> fiona_claim : CLAIM
TERM  subject(kind="Fiona", qualifier=cold_trait) -> fiona_cold_subject : TERM
TERM  CLAIM statement(fact=fiona_cold_subject) BY role_user STATUS asserted SOURCE "t1:s4" -> fiona_cold_claim : CLAIM
TERM  subject(kind="Gary", qualifier=large_trait) -> gary_large_subject : TERM
TERM  CLAIM statement(fact=gary_large_subject)
```
