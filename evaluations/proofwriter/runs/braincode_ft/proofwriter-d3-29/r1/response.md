```braincode
TERM  lexical_label(value=color_label::blue) -> lexical_label_blue : TERM
TERM lexical_label(value=color_label::green) -> lexical_label_green : TERM
TERM subject(kind="Bob", qualifier=lexical_label_blue) -> subject_bob : TERM
TERM subject(kind="Bob", qualifier=lexical_label_green) -> subject_bob_2 : TERM
TERM subject(kind="Bob", qualifier=shape_round) -> subject_bob_3 : TERM
TERM subject(kind="Bob", qualifier="smart") -> subject_bob_4 : TERM
TERM subject(kind="Bob", qualifier="young") -> subject_bob_5 : TERM
TERM subject(kind="Charlie", qualifier=lexical_label_green) -> subject_charlie : TERM
TERM character_trait(property="nice", value=0) -> character_trait_nice : TERM
TERM negation(target=character_trait_nice) -> negation_nice : TERM
TERM subject(kind="Charlie", qualifier=negation_nice) -> subject_charlie_2 : TERM
TERM subject(kind="Charlie", qualifier="young") -> subject_charlie_3 : TERM
TERM negation(target=subject_charlie_3) -> negation_young : TERM
TERM subject(kind="Erin", qualifier=lexical_label_blue) -> subject_erin : TERM
TERM subject(kind="Harry", qualifier="young") -> subject_harry : TERM
TERM requirement(property="color", value=lexical_label_blue) -> req_erin_blue : TERM
TERM requirement(property="age", value="young") -> req_erin_young : TERM
TERM conjunction(items=[req_erin_blue, req_erin_young]) -> conj_erin : TERM
TERM requirement(property="intelligence", value="smart") -> req_erin_smart : TERM
TERM enables(condition=conj_erin, outcome=req_erin_smart) -> enables_2 : TERM
TERM requirement(property="shape", value=shape_round) -> req_someone_round : TERM
```
