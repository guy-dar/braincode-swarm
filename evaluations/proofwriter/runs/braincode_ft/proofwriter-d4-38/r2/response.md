```braincode
TERM  lexical_label(value=color_label::green) -> lexical_label_2 : TERM
TERM character_trait(property="color", value=color_label::green) -> character_trait_2 : TERM
TERM character_trait(property="shape", value=shape_round) -> character_trait_3 : TERM
TERM activity(actor="bear", object=animal_label::cow, verb="likes") -> activity_2 : TERM
TERM activity(actor="bear", object=animal_label::lion, verb="sees") -> activity_3 : TERM
TERM activity(actor="cow", object=animal_label::bear, verb="eats") -> activity_4 : TERM
TERM character_trait(property="texture", value="rough") -> character_trait_4 : TERM
TERM character_trait(property="age", value="young") -> character_trait_5 : TERM
TERM activity(actor="cow", object=animal_label::bear, verb="likes") -> activity_5 : TERM
TERM activity(actor="lion", object=animal_label::squirrel, verb="sees") -> activity_6 : TERM
TERM activity(actor="squirrel", object=animal_label::bear, verb="eats") -> activity_7 : TERM
TERM character_trait(property="texture", value="rough") -> character_trait_6 : TERM
TERM activity(actor="squirrel", object=animal_label::bear, verb="sees") -> activity_8 : TERM
TERM activity(actor="something", object=animal_label::lion, verb="eats") -> activity_9 : TERM
TERM activity(actor="something", object=animal_label::lion, verb="sees") -> activity_10 : TERM
TERM conjunction(items=[activity_9, activity_10]) -> conjunction_2 : TERM
TERM activity(actor="lion", object=animal_label::squirrel, verb="likes") -> activity_11 : TERM
TERM conditional(condition=conjunction_2, consequence=activity_
```
