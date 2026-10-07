```braincode
TERM  activity(verb="see", actor="cat", object=animal_label::cow) -> see_cow : TERM
TERM requirement(property="basis", value="theory") -> basis_req : TERM
TERM constraint_single_choice() -> choice_constr : TERM
TERM conjunction(items=[basis_req, choice_constr]) -> constr : TERM
TERM activity(verb="see", actor="bald_eagle", object=animal_label::cat) -> see_cat : TERM
UTTER ask(target=see_cat, constraints=[constr])
```
