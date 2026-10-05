```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  ACTION setup(machine: TERM) -> machine : TERM
  ACTION short_circuit(condition: TERM) -> short_circuit : EVENT
  CLAIM short_circuit_cause(wire: STRING, short_circuit: EVENT) -> CLAIM
  CLAIM majority_opinion(opinion: STRING) -> CLAIM
  UTTER ask(target=short_circuit_cause(wire="black", short_circuit=short_circuit))
  UTTER respond(target=short_circuit_cause(wire="black", short_circuit=short_circuit), opinion=majority_opinion(opinion="yes"))
  UTTER respond(target=short_circuit_cause(wire="red", short_circuit=short_circuit), opinion=majority_opinion(opinion="no"))
  UTTER respond(target=short_circuit_cause(wire="black", short_circuit=short_circuit), opinion=majority_opinion(opinion="ambiguous"))
}
```