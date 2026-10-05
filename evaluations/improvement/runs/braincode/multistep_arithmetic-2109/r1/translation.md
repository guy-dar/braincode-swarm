```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  ACTION a & b -> result : TERM
  ACTION a <> b -> result : TERM
  ACTION a # b -> result : TERM
  ACTION a ~ b -> result : TERM
  ACTION a ; b -> result : TERM
  ACTION a : b -> result : TERM
  ACTION a <op1><op2> b -> result : TERM
  ACTION ((a op1 b) op2 b) -> result : TERM
  ACTION A = (((((((((((((-2 *+ 1) *: -8) - five) + eight) +& -10) <>:& -9) && one) :-+ -10) # 10) - -8) <> four) *# 10) -> A : TERM
  ACTION B = ((((10 -+ 6) <> (5 <>#: six)) ;: ((-6 *; -5) <>* (six -& 2))) &+* (((-10 * -2) ; (5 #+& three)) - ((-9 *+ -4) :-~ (three *:; -6)))) -> B : TERM
  ACTION C = (((((((((((((three #  -3) -: four) <>~ four) <> 3) ~~ 1) +<> -6) -;& 6) * -9) +~ -5) :-: two) : 5) +<>; nine) -> C : TERM
  ACTION result = A + B - C -> result : NUMBER
  -> result : NUMBER
}
```