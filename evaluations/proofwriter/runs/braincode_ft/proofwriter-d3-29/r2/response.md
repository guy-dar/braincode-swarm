```braincode
TERM  lexical_label(value=color_label::blue) -> lexical_label_blue : TERM
TERM lexical_label(value=color_label::green) -> lexical_label_green : TERM
TERM subject(kind="Bob", qualifier=lexical_label_blue) -> subject_bob : TERM
TERM subject(kind="Bob", qualifier=lexical_label_green) -> subject_bob_2 : TERM
TERM subject(kind="Bob", qualifier=shape_round) -> subject_bob_3 : TERM
TERM subject(kind="Bob", qualifier="smart") -> subject_bob_4 : TERM
TERM subject(kind="Bob", qualifier="young") -> subject_bob_5 : TERM
TERM subject(kind="Charlie", qualifier="not_nice") -> subject_charlie : TERM
TERM subject(kind="Charlie", qualifier="not_young") -> subject_charlie_2 : TERM
TERM subject(kind="Erin", qualifier=lexical_label_blue) -> subject_erin : TERM
TERM subject(kind="Harry", qualifier=size_large) -> subject_harry : TERM
TERM requirement(property="color", value=lexical_label_blue) -> req_erin_blue : TERM
TERM requirement(property="age", value="young") -> req_erin_young : TERM
TERM conjunction(items=[req_erin_blue, req_erin_young]) -> conj_erin : TERM
TERM requirement(property="intelligence", value="smart") -> req_erin_smart : TERM
TERM conjunction(items=[conj_erin, req_erin_smart]) -> conj_erin_2 : TERM
TERM requirement(property="shape", value=shape_round) -> req_someone_round : TERM
TERM conditional(condition=req_someone_round, consequence=req_erin_young) -> cond_round_young : TERM
TERM requirement(property="color", value=lexical_label_green) -> req_people_green : TERM
TERM conditional(condition=req_erin_blue, consequence=req_people_green) -> cond_blue_green : TERM
TERM requirement(property="size", value=size_large) -> req
```
