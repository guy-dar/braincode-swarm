```braincode
TERM  activity(verb="chase", actor="rabbit", object=animal_label::squirrel) -> chase_squirrel : TERM
TERM test_condition(condition="theory_evaluation", expected=TRUE) -> test_condition_2 : TERM
TERM conjunction(items=[chase_squirrel, test_condition_2]) -> conjunction_2 : TERM
TERM activity(actor="squirrel", object=animal_label::rabbit, verb="chase") -> activity_14 : TERM
UTTER ask(target=activity_14, constraints=[conjunction_2])
```
