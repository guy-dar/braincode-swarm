```braincode
TERM  character_trait(property="furry", value="furry") -> character_trait_2 : TERM
TERM character_trait(property="rough", value="rough") -> character_trait_3 : TERM
TERM has_attribute(attribute=state_cold, subject="Dave") -> has_attribute_2 : TERM
TERM has_attribute(attribute="quiet", subject="Dave") -> has_attribute_3 : TERM
TERM lexical_label(value=color_label::blue) -> lexical_label_2 : TERM
TERM has_attribute(attribute=lexical_label_2, subject="Fiona") -> has_attribute_4 : TERM
TERM character_trait(property="furry", value="furry") -> character_trait_5 : TERM
TERM lexical_label(value=color_label::green) -> lexical_label_3 : TERM
TERM has_attribute(attribute=lexical_label_3, subject="Gary") -> has_attribute_6 : TERM
TERM conditional(condition=lexical_label_2, consequence=lexical_label_3) -> conditional_2 : TERM
TERM has_attribute(attribute=state_cold, subject="Gary") -> has_attribute_7 : TERM
TERM conjunction(items=[lexical_label_2, lexical_label_3]) -> conjunction_2 : TERM
TERM negation(target=conjunction_2) -> negation_2 : TERM
TERM conditional(condition=negation_2, consequence=character_trait_3) -> conditional_3 : TERM
TERM subject(kind=shape_round) -> subject_2 : TERM
TERM has_attribute(attribute=subject_2, subject="Dave") -> has_attribute_8 : TERM
TERM has_attribute(attribute="quiet", subject="Dave") -> has_attribute_9 : TERM
TERM conditional(condition=subject_2, consequence=has_attribute_9) -> conditional_4 : TERM
TERM subject(kind="rough", qualifier="Fiona") -> subject_3 : TERM
TERM subject(kind=shape_round, qualifier="Fiona") -> subject_4 : TERM
TERM conditional
```
