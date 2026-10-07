```braincode
TERM  activity(actor="baldeagle", object=animal_label::cat, verb="see") -> see_cat : TERM
TERM requirement(property="size", value=size_large) -> size_large : TERM
TERM subject(kind="baldeagle", qualifier=size_large) -> q : TERM
TERM negation(target=q) -> not_q : TERM
CLAIM statement(fact=not_q) BY role_agent STATUS hypothesized SOURCE "theory" -> candidate : CLAIM
CLAIM statement(fact=q) BY role_agent STATUS hypothesized SOURCE "theory" -> candidate_negation : CLAIM
```
