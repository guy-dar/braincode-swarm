```braincode
TERM  activity(verb="like", actor="rabbit", object=animal_label::cow) -> likes_rabbit_cow : TERM
TERM  character_trait(property="shape", value=shape_round) -> round : TERM
TERM  requirement(property="basis", value="theory") -> basis : TERM
TERM  constraint_single_choice() -> choice : TERM
CLAIM statement(fact=round) BY role_agent STATUS inferred SOURCE "theory" -> verdict : CLAIM
```
