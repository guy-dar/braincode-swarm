# Failed translations and what they were missing

Every failed run, with the terms its translator documented as missing from the glossary (`add`) or needing a change (`refine`), from its suggestions.

| model | item | run | adds | terms it would add | refines | targets |
|---|---|---:|---:|---|---:|---|
| Claude Haiku 4.5 | alfred-1 | r1 | 2 | spatial_relation, object_descriptor | 2 | v19/value/ottoman, v19/value/couch |
| Claude Haiku 4.5 | mind2web-1 | r2 | 4 | trip_type_spec, nonstop_constraint, airline_selected, flight_selected | 0 | — |
| Claude Haiku 4.5 | paths-1 | r3 | 1 | tone_flirty | 0 | — |
| Claude Haiku 4.5 | swebench-3 | r3 | 3 | code_file_operation, package_installation, not_reproducible | 0 | — |
| Claude Sonnet 5.5 | alfred-1 | r1 | 2 | entity_description, spatial_relation | 0 | — |
| Claude Sonnet 5.5 | alfred-1 | r2 | 2 | located, described_object | 1 | v19/support/activity |
| Claude Sonnet 5.5 | alfred-1 | r3 | 2 | spatial_relation, described_entity | 0 | — |
| Claude Sonnet 5.5 | alfred-2 | r3 | 2 | entity_description, step | 0 | — |
| Claude Sonnet 5.5 | alfred-3 | r1 | 1 | spatial_relation | 2 | v19/constructor/activity, v19/constructor/requirement |
| Claude Sonnet 5.5 | alfred-3 | r3 | 1 | spatial_relation | 0 | — |
| Claude Sonnet 5.5 | mind2web-3 | r1 | 1 | unit_watt | 0 | — |
| Claude Sonnet 5.5 | mind2web-3 | r2 | 1 | unit_watt | 0 | — |
| Claude Sonnet 5.5 | mind2web-3 | r3 | 1 | unit_watt | 0 | — |
| Claude Sonnet 5.5 | paths-1 | r1 | 2 | persona, tone_flirty | 0 | — |
| Claude Sonnet 5.5 | paths-1 | r3 | 2 | tone_flirty, persona | 0 | — |
| Claude Sonnet 5.5 | paths-2 | r1 | 3 | reconcile_accounts, property_question, possible | 0 | — |
| Claude Sonnet 5.5 | paths-2 | r3 | 3 | reconcile, meaning_question, recurrence | 0 | — |
| Claude Sonnet 5.5 | paths-3 | r1 | 2 | adaptation, depicts | 0 | — |
| Claude Sonnet 5.5 | paths-3 | r2 | 1 | depicts | 1 | art_story |
| Claude Sonnet 5.5 | paths-3 | r3 | 3 | request, story_contains, adaptation_of | 0 | — |
| Claude Sonnet 5.5 | prism-1 | r3 | 2 | occurs, yes_no_question | 0 | — |
| Claude Sonnet 5.5 | prism-2 | r1 | 4 | precedes, fraction, alternatives, feasibility | 0 | — |
| Claude Sonnet 5.5 | prism-2 | r2 | 4 | requires, precedes, alternative, suitable_for | 0 | — |
| Claude Sonnet 5.5 | prism-3 | r1 | 1 | why_question | 0 | — |
| Claude Sonnet 5.5 | prism-3 | r3 | 1 | open_question | 0 | — |
| Claude Sonnet 5.5 | swebench-1 | r2 | 1 | disjunction | 0 | — |
| Claude Sonnet 5.5 | swebench-1 | r3 | 4 | variable_unassigned, reads_variable, lacks_statement, alternatives | 0 | — |
| Claude Sonnet 5.5 | swebench-2 | r3 | 0 | — | 1 | v19/constructor/chg_modify_code |
| Claude Sonnet 5.5 | swebench-3 | r2 | 1 | propose | 0 | — |
| Claude Sonnet 5.5 | thoughttrace-2 | r1 | 3 | property_question, desires, has_property | 0 | — |
| Claude Sonnet 5.5 | thoughttrace-2 | r3 | 1 | desires | 0 | — |
| Claude Sonnet 5.5 | thoughttrace-3 | r1 | 1 | fails_to | 0 | — |
| Claude Sonnet 5.5 | thoughttrace-3 | r2 | 1 | unable_to_complete | 0 | — |
| Claude Sonnet 5.5 | thoughttrace-3 | r3 | 1 | unable_to | 0 | — |
| Gemini 3.7 Flash | mind2web-3 | r2 | 1 | unit_watt | 0 | — |
| Gemini 3.7 Flash | mind2web-3 | r3 | 1 | unit_watt | 0 | — |
| Gemini 3.7 Flash | paths-8 | r3 | 3 | praise, thank, compliment | 0 | — |
| Gemini 3.7 Flash | prism-3 | r2 | 2 | national_id, verification_requirement | 0 | — |
| Gemini 3.7 Flash | prism-3 | r3 | 3 | identity_credential, account_verification, multi_factor_authentication | 0 | — |
| Gemini 3.7 Flash | swebench-4 | r1 | 2 | network_connection, hang | 1 | v19/operation-vocabulary/modify_code |
| Gemini 3.7 Flash | swebench-4 | r3 | 2 | network_connection, cli_flag | 0 | — |
| Gemini 3.7 Flash | swebench-6 | r2 | 1 | path_tools_py3tool_py | 0 | — |
| Gemini 3.7 Flash | swebench-7 | r3 | 4 | chg_deprecate_code, code_usage, code_breakage, code_evaluation | 0 | — |
| Gemini 3.7 Flash (high effort) | alfred-6 | r1 | 1 | inscribed_text | 0 | — |
| Gemini 3.7 Flash (high effort) | alfred-6 | r2 | 0 | — | 1 | v19/operation-vocabulary/pick_up |
| Gemini 3.7 Flash (high effort) | mind2web-3 | r1 | 1 | unit_watt | 0 | — |
| Gemini 3.7 Flash (high effort) | mind2web-3 | r3 | 1 | unit_watt | 0 | — |
| Gemini 3.7 Flash (high effort) | swebench-4 | r1 | 2 | connection, functions_properly | 0 | — |
| Gemini 3.7 Flash (high effort) | swebench-7 | r3 | 5 | chg_deprecate, code_usage, breakage, inconsistent_behavior, code_eval | 0 | — |
| o4-mini | alfred-1 | r1 | 2 | object_specification, path_specification | 0 | — |
| o4-mini | alfred-1 | r2 | 2 | furniture_label, colored_object | 0 | — |
| o4-mini | alfred-1 | r3 | 1 | object_description | 0 | — |
| o4-mini | alfred-2 | r1 | 2 | chill, object_at_location | 0 | — |
| o4-mini | alfred-2 | r2 | 1 | object_at_location | 0 | — |
| o4-mini | alfred-2 | r3 | 1 | chill | 0 | — |
| o4-mini | alfred-3 | r2 | 2 | entity_reference, requirement | 1 | v19/construction/activity |
| o4-mini | alfred-3 | r3 | 3 | command, walk_forward, select_object | 1 | pick_up |
| o4-mini | mind2web-1 | r1 | 1 | flight_search_request | 0 | — |
| o4-mini | mind2web-1 | r2 | 2 | flight_search, request | 0 | — |
| o4-mini | mind2web-1 | r3 | 1 | flight_search_request | 0 | — |
| o4-mini | mind2web-3 | r1 | 1 | search_request | 0 | — |
| o4-mini | mind2web-3 | r2 | 2 | power_unit_label, request_action | 1 | measure |
| o4-mini | mind2web-3 | r3 | 1 | unit_watt | 0 | — |
| o4-mini | paths-1 | r3 | 3 | tone_flirty, causal_question, availability_question | 0 | — |
| o4-mini | paths-2 | r1 | 2 | account_reconciliation, custom_report_request | 0 | — |
| o4-mini | paths-2 | r2 | 4 | reconcile_balance_sheet_accounts, explain_in_reporting, create_custom_report, schedule_recurring_report | 0 | — |
| o4-mini | paths-2 | r3 | 6 | definition, click_button, select_column, run_report, schedule_report, report_request | 0 | — |
| o4-mini | paths-3 | r1 | 3 | ask, provide, rewrite | 0 | — |
| o4-mini | paths-3 | r3 | 3 | plot_request, narrative_text, adaptation_request | 0 | — |
| o4-mini | prism-1 | r1 | 2 | problem_question, topic_personal_hobbies | 0 | — |
| o4-mini | prism-1 | r2 | 2 | work_life_balance, multiple_part_time_jobs | 0 | — |
| o4-mini | prism-1 | r3 | 4 | topic_work_personal_issues, policy_action, job_count, part_time | 1 | activity |
| o4-mini | prism-2 | r1 | 1 | inefficient | 0 | — |
| o4-mini | prism-2 | r2 | 8 | procedure_question, mower_blade_height, fractional_limit, straight_back_and_forth, sequence, possibility_question, limitation, equipment_requirement | 0 | — |
| o4-mini | prism-2 | r3 | 1 | procedure_question | 0 | — |
| o4-mini | prism-3 | r1 | 7 | reason_question, policy_document, mitigation_question, email_verification_term, requirement, two_factor_requirement, tradeoff_summary | 1 | v19/claim/enables |
| o4-mini | prism-3 | r2 | 1 | property_question | 0 | — |
| o4-mini | prism-3 | r3 | 2 | question_why, social_security_number | 0 | — |
| o4-mini | swebench-1 | r1 | 2 | assert_variable_assigned, assert_unpack_missing | 0 | — |
| o4-mini | swebench-1 | r2 | 4 | code_error_context, method_call, maintainers_list, instruct_modify_code | 0 | — |
| o4-mini | swebench-1 | r3 | 1 | code_revision | 0 | — |
| o4-mini | swebench-2 | r1 | 2 | implement_method, test_truthiness | 0 | — |
| o4-mini | swebench-2 | r2 | 1 | implement_method | 0 | — |
| o4-mini | swebench-3 | r1 | 2 | deprecation_notice, code_location | 0 | — |
| o4-mini | swebench-3 | r2 | 6 | create_file, execute_cli, deprecation_notice, originates_from, cannot_reproduce, catches_warning | 1 | v19/claim_relation/warning |
| o4-mini | swebench-3 | r3 | 1 | log_entry | 0 | — |
| o4-mini | thoughttrace-1 | r1 | 1 | story_planning_guide | 0 | — |
| o4-mini | thoughttrace-1 | r2 | 2 | classify, organization_framework | 0 | — |
| o4-mini | thoughttrace-1 | r3 | 4 | story_organization_framework, categorize_best_methods, story_genre, realize_vision | 0 | — |
| o4-mini | thoughttrace-2 | r1 | 2 | itinerary_summary, travel_intent | 0 | — |
| o4-mini | thoughttrace-2 | r2 | 2 | content_plan_trip, trip_details | 0 | — |
| o4-mini | thoughttrace-2 | r3 | 3 | role_parents, style_adventure, itinerary_plan | 0 | — |
| o4-mini | thoughttrace-3 | r1 | 1 | cannot_complete | 0 | — |
| o4-mini | thoughttrace-3 | r2 | 1 | failure_to_complete | 0 | — |
| o4-mini | thoughttrace-3 | r3 | 3 | cannot_complete, request_help, property_question | 0 | — |

## Most frequent missing terms per model

- **Claude Haiku 4.5**: spatial_relation (1), object_descriptor (1), trip_type_spec (1), nonstop_constraint (1), airline_selected (1), flight_selected (1), tone_flirty (1), code_file_operation (1), package_installation (1), not_reproducible (1)
- **Claude Sonnet 5.5**: spatial_relation (4), unit_watt (3), entity_description (2), persona (2), tone_flirty (2), property_question (2), depicts (2), precedes (2), alternatives (2), desires (2), located (1), described_object (1), described_entity (1), step (1), reconcile_accounts (1)
- **Gemini 3.7 Flash**: unit_watt (2), network_connection (2), praise (1), thank (1), compliment (1), national_id (1), verification_requirement (1), identity_credential (1), account_verification (1), multi_factor_authentication (1), hang (1), cli_flag (1), path_tools_py3tool_py (1), chg_deprecate_code (1), code_usage (1)
- **Gemini 3.7 Flash (high effort)**: unit_watt (2), inscribed_text (1), connection (1), functions_properly (1), chg_deprecate (1), code_usage (1), breakage (1), inconsistent_behavior (1), code_eval (1)
- **o4-mini**: chill (2), object_at_location (2), requirement (2), flight_search_request (2), procedure_question (2), property_question (2), implement_method (2), deprecation_notice (2), cannot_complete (2), object_specification (1), path_specification (1), furniture_label (1), colored_object (1), object_description (1), entity_reference (1)
