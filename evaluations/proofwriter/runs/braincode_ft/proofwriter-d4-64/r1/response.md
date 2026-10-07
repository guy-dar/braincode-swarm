```braincode
TERM  lexical_label(value=color_label::blue) -> lexical_label_2 : TERM
TERM lexical_label(value=color_label::red) -> lexical_label_3 : TERM
TERM lexical_label(value=color_label::white) -> lexical_label_4 : TERM
TERM lexical_label(value=color_label::green) -> lexical_label_5 : TERM
TERM requirement(property="color", value=lexical_label_2) -> requirement_2 : TERM
TERM requirement(property="color", value=lexical_label_3) -> requirement_3 : TERM
TERM requirement(property="color", value=lexical_label_4) -> requirement_4 : TERM
TERM requirement(property="color", value=lexical_label_5) -> requirement_5 : TERM
TERM conjunction(items=[requirement_2, requirement_3]) -> conjunction_2 : TERM
TERM conditional(condition=conjunction_2, consequence=requirement_4) -> conditional_2 : TERM
TERM requirement(property="color", value=lexical_label_5) -> requirement_6 : TERM
TERM conditional(condition=requirement_6, consequence=requirement_2) -> conditional_3 : TERM
TERM requirement(property="quiet", value=TRUE) -> requirement_7 : TERM
TERM conditional(condition=requirement_4, consequence=requirement_7) -> conditional_4 : TERM
TERM requirement(property="color", value=lexical_label_3) -> requirement_8 : TERM
TERM conjunction(items=[requirement_3, requirement_8]) -> conjunction_3 : TERM
TERM conditional(condition=conjunction_3, consequence=requirement_4) -> conditional_5 : TERM
TERM requirement(property="young", value=TRUE) -> requirement_9 : TERM
TERM conjunction(items=[requirement_3, requirement_9]) -> conjunction_4 : TERM
TERM conjunction(items=[requirement_7, requirement_5]) -> conjunction_5 : TERM
TERM conditional(condition=conjunction_4, consequence=conjunction
```
