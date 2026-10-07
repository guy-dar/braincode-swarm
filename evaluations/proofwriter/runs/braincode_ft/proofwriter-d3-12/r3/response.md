```braincode
TERM  character_trait(property="age", value="young") -> character_trait_2 : TERM
TERM activity(actor="bald_eagle", object=animal_label::bear, verb="see") -> activity_2 : TERM
TERM activity(actor="bald_eagle", object=animal_label::bear, verb="visit") -> activity_3 : TERM
TERM activity(actor="bear", object=animal_label::squirrel, verb="eat") -> activity_4 : TERM
TERM lexical_label(value=color_label::blue) -> lexical_label_2 : TERM
TERM character_trait(property="color", value="blue") -> character_trait_3 : TERM
TERM negation(target=character_trait_3) -> negation_2 : TERM
TERM activity(actor="bear", object=animal_label::bear, verb="visit") -> activity_5 : TERM
TERM activity(actor="mouse", object=animal_label::squirrel, verb="eat") -> activity_6 : TERM
TERM character_trait(property="color", value="green") -> character_trait_4 : TERM
TERM activity(actor="squirrel", object=animal_label::mouse, verb="eat") -> activity_7 : TERM
TERM character_trait(property="temperament", value="nice") -> character_trait_5 : TERM
TERM negation(target=character_trait_5) -> negation_3 : TERM
TERM activity(actor="squirrel", object=animal_label::eagle, verb="see") -> activity_8 : TERM
TERM activity(actor="squirrel", object=animal_label::mouse, verb="visit") -> activity_9 : TERM
TERM activity(actor="someone", object=animal_label::mouse, verb="visit") -> activity_10 : TERM
TERM conditional(condition=character_trait_5, consequence=activity_10) -> conditional_2 : TERM
TERM activity(actor="someone", object=animal_label::bear, verb="see") ->
```
