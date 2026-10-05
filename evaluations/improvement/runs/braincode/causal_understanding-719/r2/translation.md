```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Machine {
  TERM property_question(property=short_circuit, subject=black_wire) -> property_question_2 : TERM
  UTTER ask(target=property_question_2)
  ACTION turn_on(target=black_wire) -> black_wire_2 : REF[STRING]
  ACTION turn_on(target=red_wire) -> red_wire_2 : REF[STRING]
  ACTION short_circuit(event=black_wire_2, red_wire_2) -> short_circuit_2 : EVENT
  CLAIM causes(condition=short_circuit_2, effect=short_circuit_2) BY majority STATUS observed SOURCE "majority" -> causes_2 : CLAIM
  UTTER confirm(target=causes_2)
  UTTER ask(target=causes_2, constraints=[constraint_single_choice])
  UTTER ask(target=causes_2, topic=short_circuit)
  UTTER ask(target=causes_2, constraints=[constraint_respectful])
}
```