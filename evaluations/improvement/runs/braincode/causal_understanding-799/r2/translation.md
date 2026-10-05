```braincode
MODE REQUEST
ENTRYPOINT Request
TASK Request {
  ACTION throw(target=REF[STRING], target_type=object_label::test_tube) -> REF[STRING]
  ACTION see(target=REF[STRING]) -> REF[STRING]
  ACTION duck(target=REF[STRING]) -> REF[STRING]
  ACTION miss(target=REF[STRING]) -> REF[STRING]
  ACTION survive(target=REF[STRING]) -> REF[STRING]
  CLAIM is_necessary_cause(cause=CLAIM, effect=CLAIM) BY logician STATUS asserted SOURCE "t1:question" -> is_necessary_cause_2 : CLAIM
  CLAIM is_necessary_cause_2 BY logician STATUS hypothesized SOURCE "t1:question" -> is_necessary_cause_3 : CLAIM
  CLAIM is_necessary_cause_3 BY logician STATUS observed SOURCE "t1:question" -> is_necessary_cause_4 : CLAIM
  CLAIM is_necessary_cause_4 BY logician STATUS assumed SOURCE "t1:question" -> is_necessary_cause_5 : CLAIM
  CLAIM is_necessary_cause_5 BY logician STATUS assumed SOURCE "t1:question" -> is_necessary_cause_6 : CLAIM
  LINK supports(conclusion=is_necessary_cause_6, premise=is_necessary_cause_5) SOURCE "t1:answer"
}
```