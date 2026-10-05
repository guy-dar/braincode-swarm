```braincode
MODE REQUEST
ENTRYPOINT Task
TASK ThrowPoisonousTestTube {
  ACTION throw(target=poisonous_test_tube, direction=down) -> test_tube_ref : REF[STRING]
  ACTION see(target=test_tube_ref, observer=agent_x) -> test_tube_seen : TERM
  ACTION duck(target=test_tube_seen, observer=agent_x) -> agent_x_ref : REF[STRING]
  ACTION miss(target=poisonous_test_tube, observer=agent_x_ref) -> test_tube_missed : TERM
  ACTION survive(target=agent_x_ref) -> survival_claim : CLAIM
  ACTION throw_necessary_cause(target=survival_claim, condition=poisonous_test_tube) -> cause_question : CLAIM
  UTTER ask(target=cause_question)
}
```