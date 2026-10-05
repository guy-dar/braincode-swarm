```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  ACTION ask(target=unit_sentence) -> unit_sentence_2 : TERM
  ACTION identify_antecedent(target=unit_sentence_2) -> antecedent : TERM
  ACTION correct(target=antecedent, option_a="A") -> option_a : TERM
  ACTION correct(target=antecedent, option_b="B") -> option_b : TERM
  ACTION correct(target=antecedent, option_c="C") -> option_c : TERM
  ACTION correct(target=antecedent, option_d="D") -> option_d : TERM
  ACTION correct(target=antecedent, option_e="E") -> option_e : TERM
  ACTION correct(target=antecedent, option_f="F") -> option_f : TERM
  CLAIM antecedent BY user STATUS asserted SOURCE "t1:s1" -> antecedent : CLAIM
  CLAIM option_a BY user STATUS asserted SOURCE "t1:s2" -> option_a : CLAIM
  CLAIM option_b BY user STATUS asserted SOURCE "t1:s3" -> option_b : CLAIM
  CLAIM option_c BY user STATUS asserted SOURCE "t1:s4" -> option_c : CLAIM
  CLAIM option_d BY user STATUS asserted SOURCE "t1:s5" -> option_d : CLAIM
  CLAIM option_e BY user STATUS asserted SOURCE "t1:s6" -> option_e : CLAIM
  CLAIM option_f BY user STATUS asserted SOURCE "t1:s7" -> option_f : CLAIM
  LINK supports(conclusion=option_a, premise=antecedent) SOURCE "t1:s8"
  LINK supports(conclusion=option_b, premise=antecedent) SOURCE "t1:s9"
  LINK supports(conclusion=option_c, premise=antecedent) SOURCE "t1:s10"
  LINK supports(conclusion=option_d, premise=antecedent) SOURCE "t1:s11"
  LINK supports(conclusion=option_e, premise=antecedent) SOURCE "t1:s12"
  LINK supports(conclusion=option_f, premise=antecedent) SOURCE "t1:s13"
}
```