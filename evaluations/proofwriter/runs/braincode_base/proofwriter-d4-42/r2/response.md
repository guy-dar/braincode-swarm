```braincode
TERM  property_question(property="truth_value", subject=subject_2) -> q : TERM
CLAIM statement(fact=q) BY role_agent STATUS hypothesized SOURCE "theory" -> candidate : CLAIM
CLAIM statement(fact=negation(target=q)) BY role_agent STATUS hypothesized SOURCE "theory" -> candidate_negation : CLAIM
```
