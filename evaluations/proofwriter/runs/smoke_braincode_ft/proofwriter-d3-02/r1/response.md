```braincode
TERM  activity(verb="see", actor="tiger", object=animal_label::tiger) -> see_tiger : TERM
TERM  activity(verb="see", actor="tiger", object=animal_label::baldeagle) -> see_baldeagle : TERM
TERM  activity(verb="see", actor="baldeagle", object=animal_label::tiger) -> see_baldeagle_tiger : TERM
TERM  activity(verb="see", actor="baldeagle", object=animal_label::baldeagle) -> see_baldeagle_baldeagle : TERM
TERM  activity(verb="see", actor="tiger", object=animal_label::mouse) -> see_mouse : TERM
TERM  activity(verb="see", actor="mouse", object=animal_label::baldeagle) -> see_mouse_baldeagle : TERM
TERM  activity(verb="see", actor="mouse", object=animal_label::tiger) -> see_mouse_tiger : TERM
TERM  activity(verb="see", actor="baldeagle", object=animal_label::cow) -> see_cow : TERM
TERM  activity(verb="see", actor="cow", object=animal_label::baldeagle) -> see_cow_baldeagle : TERM
TERM  activity(verb="see", actor="cow", object=animal_label::tiger) -> see_cow_tiger : TERM
TERM  activity(verb="see", actor="tiger", object=animal_label::cow) -> see_tiger_cow : TERM
TERM  activity(verb="see", actor="tiger", object=animal_label::tiger) -> see_tiger_tiger : TERM
TERM  activity(verb="see", actor="baldeagle", object=animal_label::tiger) -> see_baldeagle_tiger_2 : TERM
TERM  activity(verb="see", actor="tiger",
```
