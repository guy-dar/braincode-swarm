```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  ACTION extract(target=(((2 ~- -8) *~ 5) ][~ -3) # -9) -> A : TERM
  ACTION extract(target=(((((((2 ~- -8) *~ 5) ][~ -3) # -9) *+][ 4) @** -3) @~ -2) #@ -1) -> B : TERM
  ACTION extract(target=(((((6 * -1) @~ three) * -3) # 3) @+ two) ~*][ -4) @ ten) *~+ 1) @ 7) @ nine) #* -4) ~* -1) --- -2) #* -1) -> C : TERM
  ACTION calculation(inputs=[A, B, C], operation=+, result=NUM) -> result : TERM
  ACTION extract(target=result) -> result : NUMBER
}
```