```braincode
TERM  lexical_label(value=color_label::green) -> lexical_label_2 : TERM
TERM lexical_label(value=color_label::red) -> lexical_label_3 : TERM
TERM subject(kind="Bob") -> subject_2 : TERM
TERM subject(kind="Dave") -> subject_3 : TERM
TERM subject(kind="Erin") -> subject_4 : TERM
TERM subject(kind="Gary") -> subject_5 : TERM
TERM character_trait(property="nice", value="true") -> character_trait_2 : TERM
TERM character_trait(property="furry", value="true") -> character_trait_3 : TERM
TERM character_trait(property="big", value="true") -> character_trait_4 : TERM
TERM conjunction(items=[character_trait_2, character_trait_3]) -> conjunction_2 : TERM
TERM conditional(condition=conjunction_2, consequence=character_trait_4) -> conditional_2 : TERM
TERM conjunction(items=[lexical_label_2, character_trait_2]) -> conjunction_3 : TERM
TERM conditional(condition=conjunction_3, consequence=lexical_label_3) -> conditional_3 : TERM
TERM conditional(condition=character_trait_2, consequence=character_trait_3) -> conditional_4 : TERM
TERM conditional(condition=character_trait_4, consequence=character_trait_3) -> conditional_5 : TERM
TERM character_trait(property="young", value="true") -> character_trait_5 : TERM
TERM conditional(condition=character_trait_3, consequence=character_trait_5) -> conditional_6 : TERM
TERM conjunction(items=[character_trait_2, character_trait_5]) -> conjunction_4 : TERM
TERM conditional(condition=conjunction_4, consequence=lexical_label_2) -> conditional_7 : TERM
TERM conjunction(items=[character_trait_3, character_trait_4]) -> conjunction_5 : TERM
TERM conditional(condition=conjunction_5, consequence=lexical_label_2
```
