```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  ACTION look(direction="left") -> direction : TERM
  ACTION look(direction="right") -> direction : TERM
  ACTION look(direction="straight") -> direction : TERM
  ACTION search_web(target="SVG path element") -> search_results : LIST[TERM]
  ACTION extract(target=search_results, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result, modifier="coordinates") -> picked_up : TERM
  ACTION place(destination=picked_up, target="SVG visualization") -> result : TERM
  ACTION record(result=result) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_oval, shape_square, shape_rectangular, shape_triangular]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_round, shape_oval, shape_square, shape_triangular]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_rectangular, shape_square, shape_round]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_triangular, shape_square, shape_oval]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_round, shape_oval, shape_square]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_rectangular, shape_square, shape_triangular]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_round, shape_triangular, shape_square]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_oval, shape_square, shape_rectangular]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_round, shape_square, shape_triangular]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_rectangular, shape_triangular, shape_square]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_round, shape_triangular, shape_oval]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_rectangular, shape_square, shape_oval]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_oval, shape_triangular, shape_square]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_round, shape_square, shape_triangular]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_rectangular, shape_square, shape_oval]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_triangular, shape_square, shape_round]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_round, shape_triangular, shape_oval]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_rectangular, shape_oval, shape_square]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_triangular, shape_round, shape_square]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_oval, shape_triangular, shape_square]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_round, shape_square, shape_triangular]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_rectangular, shape_triangular, shape_oval]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_round, shape_square, shape_triangular]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_oval, shape_triangular, shape_square]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_rectangular, shape_square, shape_triangular]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_round, shape_square, shape_oval]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_triangular, shape_square, shape_round]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_oval, shape_triangular, shape_round]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_rectangular, shape_round, shape_triangular]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_triangular, shape_square, shape_oval]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_round, shape_triangular, shape_square]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_rectangular, shape_square, shape_oval]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_triangular, shape_square, shape_round]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_oval, shape_triangular, shape_round]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_rectangular, shape_round, shape_triangular]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_square, shape_triangular, shape_oval]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_round, shape_square, shape_oval]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_triangular, shape_square, shape_round]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_oval, shape_square, shape_triangular]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_rectangular, shape_square, shape_oval]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_triangular, shape_round, shape_square]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_oval, shape_triangular, shape_round]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_rectangular, shape_round, shape_square]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_triangular, shape_square, shape_oval]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_round, shape_square, shape_triangular]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_rectangular, shape_square, shape_oval]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_triangular, shape_round, shape_square]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_oval, shape_triangular, shape_square]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_rectangular, shape_triangular, shape_square]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_round, shape_square, shape_oval]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_triangular, shape_square, shape_round]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_oval, shape_triangular, shape_square]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_rectangular, shape_square, shape_oval]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_triangular, shape_round, shape_square]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_oval, shape_square, shape_triangular]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_rectangular, shape_square, shape_triangular]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_round, shape_triangular, shape_square]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_rectangular, shape_square, shape_oval]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_triangular, shape_square, shape_round]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_oval, shape_triangular, shape_round]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_rectangular, shape_round, shape_triangular]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_square, shape_triangular, shape_oval]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_round, shape_square, shape_triangular]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_rectangular, shape_square, shape_oval]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_triangular, shape_square, shape_round]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_oval, shape_square, shape_triangular]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_rectangular, shape_triangular, shape_square]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_round, shape_square, shape_oval]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_triangular, shape_square, shape_round]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_oval, shape_triangular, shape_square]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_rectangular, shape_square, shape_oval]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_triangular, shape_round, shape_square]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_oval, shape_triangular, shape_square]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_rectangular, shape_square, shape_oval]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_triangular, shape_square, shape_round]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_oval, shape_triangular, shape_round]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_rectangular, shape_round, shape_triangular]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_square, shape_triangular, shape_oval]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_round, shape_square, shape_triangular]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_rectangular, shape_square, shape_oval]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_triangular, shape_square, shape_round]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_oval, shape_triangular, shape_square]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_rectangular, shape_square, shape_triangular]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_round, shape_square, shape_triangular]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_rectangular, shape_triangular, shape_square]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_triangular, shape_square, shape_round]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_oval, shape_square, shape_triangular]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_rectangular, shape_square, shape_oval]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_triangular, shape_round, shape_square]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_oval, shape_triangular, shape_round]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_rectangular, shape_round, shape_triangular]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_square, shape_triangular, shape_oval]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_round, shape_square, shape_triangular]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_rectangular, shape_square, shape_oval]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_triangular, shape_square, shape_round]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_oval, shape_triangular, shape_square]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_rectangular, shape_square, shape_triangular]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_round, shape_triangular, shape_square]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_rectangular, shape_square, shape_oval]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_triangular, shape_square, shape_round]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_oval, shape_triangular, shape_round]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_rectangular, shape_round, shape_triangular]) -> shape : TERM
  ACTION record(shape=shape) -> recorded : EVENT
  ACTION check(recorded=recorded, constraints=[shape_square, shape_triangular