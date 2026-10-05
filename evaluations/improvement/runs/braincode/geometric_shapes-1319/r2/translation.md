```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  ACTION visualize_svg(target="svg_path") -> svg_ref : REF[STRING]
  ACTION draw_lines(svg_ref, target="lines") -> lines_ref : REF[STRING]
  ACTION visualize(target="lines_ref") -> lines_view : TERM
  ACTION check_shape(target="lines_view", shape="rectangle") -> shape_result : TERM
  ACTION check_shape(target="lines_view", shape="square") -> shape_result : TERM
  ACTION check_shape(target="lines_view", shape="triangle") -> shape_result : TERM
  ACTION check_shape(target="lines_view", shape="right_triangle") -> shape_result : TERM
  ACTION check_shape(target="lines_view", shape="parallelogram") -> shape_result : TERM
  ACTION check_shape(target="lines_view", shape="trapezoid") -> shape_result : TERM
  ACTION check_shape(target="lines_view", shape="irregular_convex_pentagon") -> shape_result : TERM
  ACTION check_shape(target="lines_view", shape="irregular_concave_pentagon") -> shape_result : TERM
  ACTION check_shape(target="lines_view", shape="regular_pentagon") -> shape_result : TERM
  ACTION check_shape(target="lines_view", shape="regular_hexagon") -> shape_result : TERM
  ACTION check_shape(target="lines_view", shape="rectangle_with_no_diagonals") -> shape_result : TERM
  ACTION check_shape(target="lines_view", shape="square_with_no_diagonals") -> shape_result : TERM
  ACTION check_shape(target="lines_view", shape="triangle_with_no_diagonals") -> shape_result : TERM
  ACTION check_shape(target="lines_view", shape="right_triangle_with_no_diagonals") -> shape_result : TERM
  ACTION check_shape(target="lines_view", shape="parallelogram_with_no_diagonals") -> shape_result : TERM
  ACTION check_shape(target="lines_view", shape="trapezoid_with_no_diagonals") -> shape_result : TERM
  ACTION check_shape(target="lines_view", shape="irregular_convex_pentagon_with_no_diagonals") -> shape_result : TERM
  ACTION check_shape(target="lines_view", shape="irregular_concave_pentagon_with_no_diagonals") -> shape_result : TERM
  ACTION check_shape(target="lines_view", shape="regular_pentagon_with_no_diagonals") -> shape_result : TERM
  ACTION check_shape(target="lines_view", shape="regular_hexagon_with_no_diagonals") -> shape_result : TERM
  ACTION check_result(target="shape_result", option="A") -> result : TERM
  ACTION check_result(target="shape_result", option="B") -> result : TERM
  ACTION check_result(target="shape_result", option="C") -> result : TERM
  ACTION check_result(target="shape_result", option="D") -> result : TERM
  ACTION check_result(target="shape_result", option="E") -> result : TERM
  ACTION check_result(target="shape_result", option="F") -> result : TERM
  ACTION check_result(target="shape_result", option="G") -> result : TERM
  ACTION check_result(target="shape_result", option="H") -> result : TERM
  ACTION check_result(target="shape_result", option="I") -> result : TERM
  ACTION check_result(target="shape_result", option="J") -> result : TERM
  ACTION check_result(target="shape_result", option="K") -> result : TERM
  ACTION check_result(target="shape_result", option="L") -> result : TERM
  ACTION check_result(target="shape_result", option="M") -> result : TERM
  ACTION check_result(target="shape_result", option="N") -> result : TERM
  ACTION check_result(target="shape_result", option="O") -> result : TERM
  ACTION check_result(target="shape_result", option="P") -> result : TERM
  ACTION check_result(target="shape_result", option="Q") -> result : TERM
  ACTION check_result(target="shape_result", option="R") -> result : TERM
  ACTION check_result(target="shape_result", option="S") -> result : TERM
  ACTION check_result(target="shape_result", option="T") -> result : TERM
  ACTION check_result(target="shape_result", option="U") -> result : TERM
  ACTION check_result(target="shape_result", option="V") -> result : TERM
  ACTION check_result(target="shape_result", option="W") -> result : TERM
  ACTION check_result(target="shape_result", option="X") -> result : TERM
  ACTION check_result(target="shape_result", option="Y") -> result : TERM
  ACTION check_result(target="shape_result", option="Z") -> result : TERM
}
```