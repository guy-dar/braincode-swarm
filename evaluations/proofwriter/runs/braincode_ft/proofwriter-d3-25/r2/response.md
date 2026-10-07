```braincode
TERM  subject(kind="Gary") -> subject_gary : TERM
TERM requirement(property="rough", value=TRUE) -> requirement_rough : TERM
TERM negation(target=requirement_rough) -> negation_rough : TERM
TERM property_question(property="truth_value", subject=negation_rough) -> property_question : TERM
UTTER ask(target=property_question)
```
