```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  ACTION search_web(target="svg_path") -> svg_path_result : LIST[TERM]
  ACTION pick_up(target=svg_path_result[0]) -> svg_path_ref : REF[STRING]
  ACTION visualize(target=svg_path_ref) -> visualization_result : LIST[TERM]
  ACTION ask(what=visualization_result, question="which shape can be viewed") -> answer : LIST[TERM]
  ACTION extract(target=answer[0]) -> possible_shapes : LIST[TERM]
  ACTION rank_direction(target=possible_shapes, direction="ascending") -> ranked_shapes : LIST[TERM]
  ACTION select_option(target=ranked_shapes[0], value="C") -> selected_shape : TERM
  ACTION supports(condition=selected_shape, outcome="can be viewed") -> outcome : CLAIM
  ACTION asserts(condition=outcome, conclusion="the shape is a triangle") -> conclusion : CLAIM
  ACTION supports(condition=conclusion, outcome="the triangle is not a right triangle") -> outcome : CLAIM
  ACTION asserts(condition=outcome, conclusion="the shape is a triangle") -> conclusion : CLAIM
  ACTION supports(condition=conclusion, outcome="the triangle is not a right triangle") -> outcome : CLAIM
  ACTION asserts(condition=outcome, conclusion="the shape is a triangle") -> conclusion : CLAIM
  ACTION supports(condition=conclusion, outcome="the triangle is not a right triangle") -> outcome : CLAIM
}
```