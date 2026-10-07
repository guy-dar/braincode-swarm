```braincode
TERM  lexical_label(value=color_label::white) -> lexical_label_2 : TERM
TERM requirement(property="color", value=lexical_label_2) -> requirement_2 : TERM
TERM requirement(property="furry", value=TRUE) -> requirement_3 : TERM
TERM conjunction(items=[requirement_2, requirement_3]) -> conjunction_2 : TERM
TERM requirement(property="nice", value=TRUE) -> requirement_4 : TERM
TERM conjunction(items=[requirement_2, requirement_4]) -> conjunction_3 : TERM
TERM requirement(property="young", value=TRUE) -> requirement_5 : TERM
TERM conjunction(items=[requirement_2, requirement_5]) -> conjunction_4 : TERM
TERM requirement(property="smart", value=TRUE) -> requirement_6 : TERM
TERM conjunction(items=[requirement_3, requirement_6]) -> conjunction_5 : TERM
TERM requirement(property="big", value=TRUE) -> requirement_7 : TERM
TERM conditional(condition=conjunction_2, consequence=requirement_7) -> conditional_2 : TERM
TERM conditional(condition=conjunction_3, consequence=requirement_7) -> conditional_3 : TERM
TERM conditional(condition=conjunction_4, consequence=requirement_3) -> conditional_4 : TERM
TERM conditional(condition=conjunction_5, consequence=requirement_2) -> conditional_5 : TERM
TERM requirement(property="color", value=color_label::green) -> requirement_8 : TERM
TERM conjunction(items=[requirement_2, requirement_8]) -> conjunction_6 : TERM
TERM requirement(property="color", value=color_label::green) -> requirement_9 : TERM
TERM conjunction(items=[requirement_3, requirement_9]) -> conjunction_7 : TERM
TERM requirement(property="color", value=color_label::green) -> requirement_10 : TERM
TERM conjunction(items=[requirement_4, requirement_1
```
