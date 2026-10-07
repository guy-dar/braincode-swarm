```braincode
TERM  character_trait(property="color", value=color_label::blue) -> char_color_blue : TERM
TERM character_trait(property="color", value=color_label::green) -> char_color_green : TERM
TERM character_trait(property="shape", value=shape_round) -> char_shape_round : TERM
TERM character_trait(property="intelligence", value="smart") -> char_intelligent : TERM
TERM character_trait(property="age", value="young") -> char_young : TERM
TERM character_trait(property="nice", value=1) -> char_nice : TERM
TERM negation(target=char_nice) -> neg_nice : TERM
TERM conjunction(items=[char_color_blue, char_shape_round, char_intelligent, char_young]) -> conj_blue_round_intelligent : TERM
TERM conjunction(items=[char_color_green, neg_nice, char_young]) -> conj_green_nice : TERM
TERM conjunction(items=[char_color_blue, char_age]) -> conj_blue_age : TERM
TERM requirement(property="color", value=color_label::blue) -> req_blue : TERM
TERM requirement(property="age", value="young") -> req_age : TERM
TERM conjunction(items=[req_blue, req_age]) -> conj_blue_age_req : TERM
TERM requirement(property="intelligence", value="smart") -> req_intelligent : TERM
TERM requirement(property="shape", value=shape_round) -> req_round : TERM
TERM requirement(property="color", value=color_label::green) -> req_green : TERM
TERM requirement(property="size", value=size_large) -> req_large : TERM
TERM conjunction(items=[conj_blue_age, conj_blue_round_intelligent]) -> conj_blue_round_int : TERM
TERM conjunction(items=[conj_green_nice, conj_round]) -> conj_green_round : TERM
TERM conjunction(items=[conj_blue_age_req, conj_intelligent]) -> conj_blue_int : TERM
TERM conjunction(items=[conj_round, conj_green]) -> conj_round_green : TERM
TERM conjunction(items
```
