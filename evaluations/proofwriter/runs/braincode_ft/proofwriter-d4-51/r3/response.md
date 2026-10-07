```braincode
TERM  lexical_label(value=color_label::green) -> lexical_label_2 : TERM
TERM  requirement(property="color", value=lexical_label_2) -> requirement_2 : TERM
TERM  requirement(property="size", value=size_large) -> requirement_3 : TERM
TERM  conjunction(items=[requirement_2, requirement_3]) -> conjunction_2 : TERM
TERM  requirement(property="quiet", value=TRUE) -> requirement_4 : TERM
TERM  conjunction(items=[conjunction_2, requirement_4]) -> conjunction_3 : TERM
TERM  requirement(property="color", value=color_label::red) -> requirement_5 : TERM
TERM  conditional(condition=requirement_5, consequence=requirement_3) -> conditional_2 : TERM
TERM  requirement(property="shape", value=shape_round) -> requirement_6 : TERM
TERM  conditional(condition=requirement_3, consequence=requirement_6) -> conditional_3 : TERM
TERM  requirement(property="color", value=lexical_label_2) -> requirement_7 : TERM
TERM  conjunction(items=[requirement_4, requirement_2]) -> conjunction_4 : TERM
TERM  conditional(condition=conjunction_4, consequence=requirement_7) -> conditional_4 : TERM
TERM  requirement(property="color", value=color_label::red) -> requirement_8 : TERM
TERM  conditional(condition=requirement_8, consequence=requirement_3) -> conditional_5 : TERM
TERM  requirement(property="shape", value=shape_round) -> requirement_9 : TERM
TERM  conditional(condition=requirement_3, consequence=requirement_9) -> conditional_6 : TERM
TERM  requirement(property="color", value=color_label::red) -> requirement_10 : TERM
TERM  requirement(property="color", value=color_label::green) -> requirement_11 : TERM
TERM  requirement(property="quiet", value=TRUE) ->
```
