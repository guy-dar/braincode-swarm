```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  ACTION calculate_aop1_aop2_b(a: NUMBER, b: NUMBER, op1: STRING, op2: STRING) -> NUMBER
    BY calculate_aop1_aop2_b
    STATUS asserted SOURCE "glossary:calculate_aop1_aop2_b"
    -> result : NUMBER
  ACTION gcd(a: NUMBER, b: NUMBER) -> NUMBER
    BY gcd
    STATUS asserted SOURCE "glossary:gcd"
    -> result : NUMBER
  ACTION is_prime(n: NUMBER) -> BOOL
    BY is_prime
    STATUS asserted SOURCE "glossary:is_prime"
    -> result : BOOL
  ACTION min(a: NUMBER, b: NUMBER) -> NUMBER
    BY min
    STATUS asserted SOURCE "glossary:min"
    -> result : NUMBER
  ACTION max(a: NUMBER, b: NUMBER) -> NUMBER
    BY max
    STATUS asserted SOURCE "glossary:max"
    -> result : NUMBER
  ACTION abs(a: NUMBER) -> NUMBER
    BY abs
    STATUS asserted SOURCE "glossary:abs"
    -> result : NUMBER
  ACTION calculate_a(a: NUMBER, op: STRING) -> NUMBER
    BY calculate_a
    STATUS asserted SOURCE "glossary:calculate_a"
    -> result : NUMBER
  ACTION calculate_b(a: NUMBER, b: NUMBER, op: STRING) -> NUMBER
    BY calculate_b
    STATUS asserted SOURCE "glossary:calculate_b"
    -> result : NUMBER
  ACTION calculate_result(a: NUMBER, b: NUMBER, c: NUMBER) -> NUMBER
    BY calculate_result
    STATUS asserted SOURCE "glossary:calculate_result"
    -> result : NUMBER
  ACTION calculate_aop1_aop2_b(a: NUMBER, b: NUMBER, op1: STRING, op2: STRING) -> NUMBER
    BY calculate_aop1_aop2_b
    STATUS asserted SOURCE "glossary:calculate_aop1_aop2_b"
    -> result : NUMBER
  ACTION calculate_a_b(a: NUMBER, b: NUMBER) -> NUMBER
    BY calculate_a_b
    STATUS asserted SOURCE "glossary:calculate_a_b"
    -> result : NUMBER
  ACTION calculate_a_b_op(a: NUMBER, b: NUMBER, op: STRING) -> NUMBER
    BY calculate_a_b_op
    STATUS asserted SOURCE "glossary:calculate_a_b_op"
    -> result : NUMBER
  ACTION calculate_a_b_op_result(a: NUMBER, b: NUMBER, op: STRING) -> NUMBER
    BY calculate_a_b_op_result
    STATUS asserted SOURCE "glossary:calculate_a_b_op_result"
    -> result : NUMBER
  ACTION calculate_a_b_op_result_a_b_op_b(a: NUMBER, b: NUMBER, op: STRING) -> NUMBER
    BY calculate_a_b_op_result_a_b_op_b
    STATUS asserted SOURCE "glossary:calculate_a_b_op_result_a_b_op_b"
    -> result : NUMBER
  ACTION calculate_a_b_op_result_a_b_op_b_a_b_op_b(a: NUMBER, b: NUMBER, op: STRING) -> NUMBER
    BY calculate_a_b_op_result_a_b_op_b_a_b_op_b
    STATUS asserted SOURCE "glossary:calculate_a_b_op_result_a_b_op_b_a_b_op_b"
    -> result : NUMBER
  ACTION calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b(a: NUMBER, b: NUMBER, op: STRING) -> NUMBER
    BY calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b
    STATUS asserted SOURCE "glossary:calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b"
    -> result : NUMBER
  ACTION calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b(a: NUMBER, b: NUMBER, op: STRING) -> NUMBER
    BY calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b
    STATUS asserted SOURCE "glossary:calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b"
    -> result : NUMBER
  ACTION calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b(a: NUMBER, b: NUMBER, op: STRING) -> NUMBER
    BY calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b
    STATUS asserted SOURCE "glossary:calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b"
    -> result : NUMBER
  ACTION calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b(a: NUMBER, b: NUMBER, op: STRING) -> NUMBER
    BY calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b
    STATUS asserted SOURCE "glossary:calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b"
    -> result : NUMBER
  ACTION calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b(a: NUMBER, b: NUMBER, op: STRING) -> NUMBER
    BY calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b
    STATUS asserted SOURCE "glossary:calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b"
    -> result : NUMBER
  ACTION calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b(a: NUMBER, b: NUMBER, op: STRING) -> NUMBER
    BY calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b
    STATUS asserted SOURCE "glossary:calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b"
    -> result : NUMBER
  ACTION calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b(a: NUMBER, b: NUMBER, op: STRING) -> NUMBER
    BY calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b
    STATUS asserted SOURCE "glossary:calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b"
    -> result : NUMBER
  ACTION calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b(a: NUMBER, b: NUMBER, op: STRING) -> NUMBER
    BY calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b
    STATUS asserted SOURCE "glossary:calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b"
    -> result : NUMBER
  ACTION calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b(a: NUMBER, b: NUMBER, op: STRING) -> NUMBER
    BY calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b
    STATUS asserted SOURCE "glossary:calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b"
    -> result : NUMBER
  ACTION calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b(a: NUMBER, b: NUMBER, op: STRING) -> NUMBER
    BY calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b
    STATUS asserted SOURCE "glossary:calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b"
    -> result : NUMBER
  ACTION calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b(a: NUMBER, b: NUMBER, op: STRING) -> NUMBER
    BY calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b
    STATUS asserted SOURCE "glossary:calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b"
    -> result : NUMBER
  ACTION calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b(a: NUMBER, b: NUMBER, op: STRING) -> NUMBER
    BY calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b
    STATUS asserted SOURCE "glossary:calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b"
    -> result : NUMBER
  ACTION calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b(a: NUMBER, b: NUMBER, op: STRING) -> NUMBER
    BY calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b
    STATUS asserted SOURCE "glossary:calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b"
    -> result : NUMBER
  ACTION calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b(a: NUMBER, b: NUMBER, op: STRING) -> NUMBER
    BY calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b
    STATUS asserted SOURCE "glossary:calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b"
    -> result : NUMBER
  ACTION calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b(a: NUMBER, b: NUMBER, op: STRING) -> NUMBER
    BY calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b
    STATUS asserted SOURCE "glossary:calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b"
    -> result : NUMBER
  ACTION calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b(a: NUMBER, b: NUMBER, op: STRING) -> NUMBER
    BY calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b
    STATUS asserted SOURCE "glossary:calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b"
    -> result : NUMBER
  ACTION calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b(a: NUMBER, b: NUMBER, op: STRING) -> NUMBER
    BY calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b
    STATUS asserted SOURCE "glossary:calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b"
    -> result : NUMBER
  ACTION calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b(a: NUMBER, b: NUMBER, op: STRING) -> NUMBER
    BY calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b
    STATUS asserted SOURCE "glossary:calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b"
    -> result : NUMBER
  ACTION calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b(a: NUMBER, b: NUMBER, op: STRING) -> NUMBER
    BY calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b
    STATUS asserted SOURCE "glossary:calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b"
    -> result : NUMBER
  ACTION calculate_a_b_op_result_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b_op_b_a_b