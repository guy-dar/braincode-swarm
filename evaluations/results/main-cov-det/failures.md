# Failed translations and what they were missing

Every failed run, with the terms its translator documented as missing from the glossary (`add`) or needing a change (`refine`), from its suggestions.

| model | item | run | adds | terms it would add | refines | targets |
|---|---|---:|---:|---|---:|---|
| Claude Haiku 4.5 | alfred-1 | r1 | 4 | couch, activity_with_direction, colored_object, spatial_object | 1 | v19/constructor/activity |
| Claude Haiku 4.5 | mind2web-1 | r2 | 4 | trip_type_spec, nonstop_constraint, airline_selected, flight_selected | 0 | — |
| Claude Haiku 4.5 | mind2web-3 | r3 | 1 | unit_watt | 0 | — |
| Claude Haiku 4.5 | paths-2 | r1 | 1 | reconcile_accounts | 0 | — |
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
| Claude Sonnet 5.5 | paths-1 | r2 | 2 | tone_funny, persona | 0 | — |
| Claude Sonnet 5.5 | paths-1 | r3 | 2 | tone_funny, reassure | 1 | activity |
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
| Claude Sonnet 5.5 | thoughttrace-2 | r1 | 2 | wants, property_question | 0 | — |
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
| o4-mini (Flash-tier probe) | alfred-1 | r1 | 2 | object_specification, path_specification | 0 | — |
| o4-mini (Flash-tier probe) | alfred-2 | r1 | 2 | chill, object_at_location | 0 | — |
| o4-mini (Flash-tier probe) | mind2web-1 | r1 | 1 | airline_label | 0 | — |
| o4-mini (Flash-tier probe) | paths-1 | r1 | 2 | adopt_persona, rely_on | 0 | — |
| o4-mini (Flash-tier probe) | paths-3 | r1 | 3 | ask, provide, rewrite | 0 | — |
| o4-mini (Flash-tier probe) | prism-2 | r1 | 1 | property_question | 0 | — |
| o4-mini (Flash-tier probe) | swebench-1 | r1 | 2 | assert_variable_assigned, assert_unpack_missing | 0 | — |
| o4-mini (Flash-tier probe) | swebench-2 | r1 | 2 | implement_method, test_truthiness | 0 | — |
| o4-mini (Flash-tier probe) | swebench-3 | r1 | 2 | create_file, install_package | 0 | — |
| o4-mini (Flash-tier probe) | thoughttrace-1 | r1 | 2 | planning_request, organization_system | 0 | — |
| o4-mini (Flash-tier probe) | thoughttrace-2 | r1 | 1 | itinerary_summary | 0 | — |
| o4-mini (Flash-tier probe) | thoughttrace-3 | r1 | 2 | inability, help_request | 0 | — |

## Most frequent missing terms per model

- **Claude Haiku 4.5**: couch (1), activity_with_direction (1), colored_object (1), spatial_object (1), trip_type_spec (1), nonstop_constraint (1), airline_selected (1), flight_selected (1), unit_watt (1), reconcile_accounts (1)
- **Claude Sonnet 5.5**: spatial_relation (4), unit_watt (3), entity_description (2), persona (2), tone_funny (2), property_question (2), depicts (2), precedes (2), alternatives (2), located (1), described_object (1), described_entity (1), step (1), tone_flirty (1), reassure (1)
- **Gemini 3.7 Flash**: unit_watt (2), network_connection (2), praise (1), thank (1), compliment (1), national_id (1), verification_requirement (1), identity_credential (1), account_verification (1), multi_factor_authentication (1), hang (1), cli_flag (1), path_tools_py3tool_py (1), chg_deprecate_code (1), code_usage (1)
- **Gemini 3.7 Flash (high effort)**: unit_watt (2), inscribed_text (1), connection (1), functions_properly (1), chg_deprecate (1), code_usage (1), breakage (1), inconsistent_behavior (1), code_eval (1)
- **o4-mini (Flash-tier probe)**: object_specification (1), path_specification (1), chill (1), object_at_location (1), airline_label (1), adopt_persona (1), rely_on (1), ask (1), provide (1), rewrite (1), property_question (1), assert_variable_assigned (1), assert_unpack_missing (1), implement_method (1), test_truthiness (1)
