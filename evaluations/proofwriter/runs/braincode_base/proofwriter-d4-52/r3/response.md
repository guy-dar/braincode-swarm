```braincode
TERM  lexical_label(value=color_label::blue) -> lexical_label_blue : TERM
TERM  lexical_label(value=color_label::green) -> lexical_label_green : TERM
TERM  lexical_label(value=color_label::white) -> lexical_label_white : TERM
TERM  character(name="Anne") -> character_anne : TERM
TERM  character(name="Charlie") -> character_charlie : TERM
TERM  character(name="Fiona") -> character_fiona : TERM
TERM  character(name="Gary") -> character_gary : TERM
TERM  subject(kind="Anne", qualifier="kind") -> subject_anne_kind : TERM
CLAIM has_attribute(attribute="kind", subject=character_anne) BY role_user STATUS asserted SOURCE "t1:s2" -> has_attribute_anne_kind : CLAIM
TERM  subject(kind="Anne", qualifier=shape_round) -> subject_anne_round : TERM
CLAIM statement(fact=subject_anne_round) BY role_user STATUS asserted SOURCE "t1:s3" -> statement_anne_round : CLAIM
TERM  subject(kind="Charlie", qualifier=lexical_label_blue) -> subject_charlie_blue : TERM
CLAIM statement(fact=subject_charlie_blue) BY role_user STATUS asserted SOURCE "t1:s4" -> statement_charlie_blue : CLAIM
TERM  subject(kind="Charlie", qualifier=state_cold) -> subject_charlie_cold : TERM
CLAIM statement(fact=subject_charlie_cold) BY role_user STATUS asserted SOURCE "t1:s5" -> statement_charlie_cold : CLAIM
TERM  character_trait(property="kind", value="kind") -> character_trait_kind : TERM
TERM  subject(kind="Charlie", qualifier="kind") -> subject_charlie_kind : TERM
CLAIM has_attribute(attribute=character_trait_kind, subject=character_charlie) BY role_user STATUS asserted SOURCE "t1:s6" -> has_attribute_charlie_kind : CLAIM
TERM  subject(kind="Charlie", qualifier="smart") ->
```
