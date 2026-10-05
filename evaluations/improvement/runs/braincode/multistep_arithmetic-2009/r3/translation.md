```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  ACTION compute_a_plus_b_minus_c() -> result : NUMBER
  ACTION extract_value(target: LIST[REF[STRING]]) -> value : NUMBER
  ACTION format_numbered_list(items: LIST[STRING]) -> result : STRING
  ACTION generate_artifact(target: TERM, format: STRING) -> artifact : STRING
  ACTION pick_up(target: TERM) -> target_ref : REF[STRING]
  ACTION place(target: TERM, destination: TERM) -> target_ref : REF[STRING]
  ACTION record(event: EVENT) -> event_ref : REF[STRING]
  ACTION sequence(items: LIST[TERM]) -> result : TERM
  ACTION transform_preserve_first_column(source: TERM, target: TERM) -> result : TERM
  ACTION unit_second(amount: NUMBER) -> result : NUMBER
  ACTION wait(duration?: NUMBER) -> void : void
  ACTION at_least(measure: TERM) -> result : TERM
  ACTION at_most(measure: TERM) -> result : TERM
  ACTION maximum_between_stops(activity: STRING, amount: NUMBER, unit: STRING) -> result : TERM
  ACTION measure(amount: NUMBER, unit: STRING) -> result : TERM
  ACTION rate(denominator: TERM, numerator: TERM) -> result : TERM
  ACTION requirement(property: STRING, value: STRING / NUMBER / BOOL / TERM / ATOM[platform_label]) -> result : TERM
  ACTION sequence(items: LIST[TERM]) -> result : TERM
  ACTION subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> result : TERM
  ACTION test_condition(condition: TERM, expected: BOOL) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION leads_to(cause: TERM, effect: TERM) -> result : TERM
  ACTION motivated_by(claim: CLAIM, motive: STRING / TERM) -> result : TERM
  ACTION occurred_recently(target: CLAIM) -> result : TERM
  ACTION outcome(event: EVENT, value: STRING / NUMBER / BOOL) -> result : TERM
  ACTION provides(actor: STRING / TERM / ATOM[platform_label], subject: STRING / TERM / ATOM[platform_label]) -> result : TERM
  ACTION raises_exception(target?: TERM, exception_type: STRING, message?: STRING) -> result : TERM
  ACTION validates_parameter(condition: STRING, entity: TERM, parameter: STRING) -> result : TERM
  ACTION constraint_budget_limited() -> result : TERM
  ACTION constraint_realistic() -> result : TERM
  ACTION transform_preserve_first_column(source: TERM, target: TERM) -> result : TERM
  ACTION duplicate_definition(count: NUMBER, entity: TERM, location?: STRING / TERM) -> result : TERM
  ACTION enables(condition: TERM / CLAIM, outcome: TERM / CLAIM) -> result : TERM
  ACTION example_of(example: TERM, concept: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?:TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?:TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?:TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result :TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?:TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?:TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?:TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?:TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?:TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?:TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?:TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?:TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?:TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?:TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?:TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?:TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?:TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?:TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?:TERM) -> result : TERM
  ACTION instantiates(target: STRING / TERM, condition?: TERM, entity?: TERM) -> result : TERM
  ACTION instant