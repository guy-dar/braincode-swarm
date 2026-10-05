```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  ACTION rule_operations_general(inputs=["a", "b"], operation="calculate", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="conditional", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="slice", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="wait", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="sequence", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="at_least", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="at_most", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="calculation", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="measure", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="preserve", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="rate", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="requirement", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="sequence", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="subject", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="test_condition", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="instantiates", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="leads_to", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="motivated_by", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="occurred_recently", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="outcome", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="provides", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="raises_exception", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="validates_parameter", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="constrained_by", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="enables", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="example_of", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="failure", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="instantiates", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="leads_to", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="motivated_by", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="occurred_recently", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="outcome", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="provides", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="rejects", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="revises", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="supports", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="assert_multinomial_scorer", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="constraint_budget_limited", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="constraint_realistic", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="transform_preserve_first_column", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="art_short_text", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="unit_character", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="unit_minute", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="unit_second", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="format_numbered_list", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="metric_order_late", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="metric_response_time", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="size_small", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="under", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="tone_concise", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="topic_current_events", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["a", "b"], operation="quantity", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="compute", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="add", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="subtract", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="multiply", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="divide", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="square_root", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="cube_root", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="absolute_value", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="negate", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="add", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="subtract", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="multiply", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="divide", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="square_root", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="cube_root", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="absolute_value", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="negate", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="add", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="subtract", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="multiply", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="divide", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="square_root", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="cube_root", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="absolute_value", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="negate", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="add", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="subtract", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="multiply", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="divide", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="square_root", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="cube_root", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="absolute_value", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="negate", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="add", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="subtract", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="multiply", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="divide", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="square_root", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="cube_root", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="absolute_value", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="negate", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="add", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="subtract", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="multiply", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="divide", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="square_root", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="cube_root", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="absolute_value", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="negate", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="add", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="subtract", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="multiply", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="divide", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="square_root", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="cube_root", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="absolute_value", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="negate", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="add", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="subtract", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="multiply", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="divide", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="square_root", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="cube_root", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="absolute_value", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="negate", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="add", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="subtract", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="multiply", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="divide", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="square_root", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="cube_root", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="absolute_value", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="negate", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="add", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="subtract", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="multiply", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="divide", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="square_root", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="cube_root", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="absolute_value", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="negate", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="add", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="subtract", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="multiply", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="divide", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="square_root", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="cube_root", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="absolute_value", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="negate", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="add", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="subtract", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="multiply", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="divide", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="square_root", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="cube_root", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="absolute_value", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="negate", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="add", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="subtract", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="multiply", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="divide", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="square_root", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="cube_root", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="absolute_value", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="negate", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "C"], operation="add", result?: NUMBER) -> NUMBER
  ACTION rule_operations_general(inputs=["A", "B", "