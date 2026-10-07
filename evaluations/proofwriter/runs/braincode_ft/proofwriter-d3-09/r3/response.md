```braincode
TERM  activity(verb="eat", actor="cat", object=animal_label::mouse) -> eat_mouse : TERM
TERM activity(verb="eat", actor="cat", object=animal_label::squirrel) -> eat_squirrel : TERM
TERM activity(verb="see", actor="cat", object=animal_label::lion) -> see_lion : TERM
TERM activity(verb="see", actor="cat", object=animal_label::mouse) -> see_mouse : TERM
TERM activity(verb="see", actor="cat", object=animal_label::squirrel) -> see_squirrel : TERM
TERM activity(verb="see", actor="lion", object=animal_label::cat) -> lion_sees_cat : TERM
TERM activity(verb="see", actor="lion", object=animal_label::squirrel) -> lion_sees_squirrel : TERM
TERM activity(verb="see", actor="mouse", object=animal_label::squirrel) -> mouse_sees_squirrel : TERM
TERM activity(verb="like", actor="squirrel", object=animal_label::lion) -> squirrel_likes_lion : TERM
TERM activity(verb="be_cold") -> be_cold : TERM
TERM activity(verb="be_kind") -> be_kind : TERM
TERM conditional(condition=be_cold, consequence=be_kind) -> cold_cond : TERM
TERM activity(verb="eat", actor="someone", object=animal_label::mouse) -> eat_mouse_by_someone : TERM
TERM activity(verb="eat", actor="cat", object=animal_label::mouse) -> cat_eats_mouse : TERM
TERM conditional(condition=eat_mouse_by_someone, consequence=cat_eats_mouse) -> eat_mouse_cond : TERM
TERM activity(verb="eat", actor="someone", object=animal_label::squirrel) -> eat_squirrel_by_someone : TERM
TERM activity(verb="be_cold") -> cold_by
```
