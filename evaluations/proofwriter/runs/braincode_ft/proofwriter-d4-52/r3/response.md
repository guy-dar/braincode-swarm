```braincode
TERM  lexical_label(value=color_label::blue) -> lexical_label_blue : TERM
TERM lexical_label(value=color_label::green) -> lexical_label_green : TERM
TERM lexical_label(value=color_label::white) -> lexical_label_white : TERM
TERM character(name="Anne") -> character_anne : TERM
TERM character(name="Charlie") -> character_charlie : TERM
TERM character(name="Fiona") -> character_fiona : TERM
TERM character(name="Gary") -> character_gary : TERM
TERM subject(kind="Anne", qualifier="kind") -> subject_anne_kind : TERM
TERM subject(kind="Anne", qualifier=shape_round) -> subject_anne_round : TERM
TERM subject(kind="Charlie", qualifier=lexical_label_blue) -> subject_charlie_blue : TERM
TERM subject(kind="Charlie", qualifier=state_cold) -> subject_charlie_cold : TERM
TERM character_trait(property="kind", value="kind") -> character_trait_kind : TERM
TERM subject(kind="Charlie", qualifier="kind") -> subject_charlie_kind : TERM
TERM subject(kind="Charlie", qualifier="smart") -> subject_charlie_smart : TERM
TERM negation(target=subject_charlie_smart) -> negation_charlie_smart : TERM
TERM subject(kind="Fiona", qualifier="kind") -> subject_fiona_kind : TERM
TERM negation(target=subject_fiona_kind) -> negation_fiona_kind : TERM
TERM subject(kind="Fiona", qualifier="smart") -> subject_fiona_smart : TERM
TERM subject(kind="Gary", qualifier=state_cold) -> subject_gary_cold : TERM
TERM subject(kind="Gary", qualifier=lexical_label_green) -> subject_gary_green : TERM
TERM subject(kind="Gary", qualifier=shape_round) -> subject_gary_round : TERM
TERM subject(kind="Gary", qualifier=lexical_label_white) -> subject_gary_white : TERM
TERM subject(kind="Fiona", qualifier=lexical_label_blue
```
