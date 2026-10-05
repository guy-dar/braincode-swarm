Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="side_hustle") -> subject_2 : TERM
    TERM activity(purpose=subject_2, verb="plan") -> activity_2 : TERM
    UTTER ask(target=activity_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM activity(object=personal_values, verb="self_assessment") -> activity_3 : TERM
    CLAIM recommended(target=activity_3) BY role_agent STATUS asserted SOURCE "t2:s3" -> recommended_2 : CLAIM
    TERM duration(amount=1, unit=unit_week) -> duration_2 : TERM
    TERM requirement(property="time_commitment", value=duration_2) -> requirement_2 : TERM
    CLAIM recommended(target=requirement_2) BY role_agent STATUS asserted SOURCE "t2:s5" -> recommended_3 : CLAIM
    TERM constraint_budget_limited() -> constraint_budget_limited_2 : TERM
    CLAIM recommended(target=constraint_budget_limited_2) BY role_agent STATUS asserted SOURCE "t2:s6" -> recommended_4 : CLAIM
    TERM requirement(property="financial_goal", value=TRUE) -> requirement_3 : TERM
    CLAIM has_goal(goal=requirement_3, subject=role_user) BY role_agent STATUS asserted SOURCE "t2:s7" -> has_goal_2 : CLAIM
    TERM decision(activity=t1.activity_2) -> decision_2 : TERM
    CLAIM recommended(target=decision_2) BY role_agent STATUS asserted SOURCE "t2:s9" -> recommended_5 : CLAIM
    TERM topic_ai_earning_methods() -> topic_ai_earning_methods_2 : TERM
    CLAIM recommended(target=topic_ai_earning_methods_2) BY role_agent STATUS asserted SOURCE "t2:s10" -> recommended_6 : CLAIM
    TERM marketing_campaign(channel="market_research", objective="validate_demand") -> marketing_campaign_2 : TERM
    CLAIM recommended(target=marketing_campaign_2) BY role_agent STATUS asserted SOURCE "t2:s18" -> recommended_7 : CLAIM
    TERM audience_targeting(criteria=["demographics"]) -> audience_targeting_2 : TERM
    CLAIM recommended(target=audience_targeting_2) BY role_agent STATUS asserted SOURCE "t2:s20" -> recommended_8 : CLAIM
    TERM subject(kind="competition") -> subject_3 : TERM
    CLAIM recommended(target=subject_3) BY role_agent STATUS asserted SOURCE "t2:s21" -> recommended_9 : CLAIM
    TERM test_condition(condition="small_scale_test", expected=TRUE) -> test_condition_2 : TERM
    CLAIM recommended(target=test_condition_2) BY role_agent STATUS asserted SOURCE "t2:s22" -> recommended_10 : CLAIM
    TERM policy_document(title="smart_goals") -> policy_document_2 : TERM
    CLAIM recommended(target=policy_document_2) BY role_agent STATUS asserted SOURCE "t2:s25" -> recommended_11 : CLAIM
    TERM requirement(property="schedule", value=design_parameters) -> requirement_4 : TERM
    CLAIM recommended(target=requirement_4) BY role_agent STATUS asserted SOURCE "t2:s27" -> recommended_12 : CLAIM
    TERM config_setting(option="platform", section="tools", value="operational_tools") -> config_setting_2 : TERM
    CLAIM recommended(target=config_setting_2) BY role_agent STATUS asserted SOURCE "t2:s28" -> recommended_13 : CLAIM
    TERM promotional_event(kind="social_media_and_network_launch") -> promotional_event_2 : TERM
    CLAIM recommended(target=promotional_event_2) BY role_agent STATUS asserted SOURCE "t2:s30" -> recommended_14 : CLAIM
    TERM performance_tracking(target="customer_feedback") -> performance_tracking_2 : TERM
    CLAIM recommended(target=performance_tracking_2) BY role_agent STATUS asserted SOURCE "t2:s33" -> recommended_15 : CLAIM
    TERM calculation(inputs=[performance_tracking_2], operation="track_income_and_expenses") -> calculation_2 : TERM
    CLAIM recommended(target=calculation_2) BY role_agent STATUS asserted SOURCE "t2:s36" -> recommended_16 : CLAIM
    TERM performance_tracking(target="reinvest_profits", adjustment="scale_successful_strategies") -> performance_tracking_3 : TERM
    CLAIM recommended(target=performance_tracking_3) BY role_agent STATUS asserted SOURCE "t2:s37" -> recommended_17 : CLAIM
    TERM constraint_realistic() -> constraint_realistic_2 : TERM
    CLAIM recommended(target=constraint_realistic_2) BY role_agent STATUS asserted SOURCE "t2:s41" -> recommended_18 : CLAIM
    TERM preserve(component="finances", index=1) -> preserve_2 : TERM
    CLAIM recommended(target=preserve_2) BY role_agent STATUS asserted SOURCE "t2:s43" -> recommended_19 : CLAIM
    TERM obligation(activity=t1.activity_2, actor=role_user) -> obligation_2 : TERM
    CLAIM recommended(target=obligation_2) BY role_agent STATUS asserted SOURCE "t2:s44" -> recommended_20 : CLAIM
    TERM exclude(item="delaying_launch_for_perfectionism") -> exclude_2 : TERM
    CLAIM recommended(target=exclude_2) BY role_agent STATUS asserted SOURCE "t2:s45" -> recommended_21 : CLAIM
    TERM offer_help() -> offer_help_2 : TERM
    UTTER offer(target=offer_help_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask | covered |
| n2 | action | activity, subject | covered |
| n3 | object | subject | covered |
| n4 | action | activity, personal_values, recommended | covered |
| n5 | object | personal_values | covered |
| n6 | temporal | duration, requirement, unit_week, recommended | covered |
| n7 | object | constraint_budget_limited, recommended | covered |
| n8 | object | has_goal, requirement, role_user | covered |
| n9 | action | decision, recommended | covered |
| n10 | object | topic_ai_earning_methods, recommended | covered |
| n11 | action | marketing_campaign, recommended | covered |
| n12 | object | audience_targeting, recommended | covered |
| n13 | object | subject, recommended | covered |
| n14 | action | test_condition, recommended | covered |
| n15 | action | policy_document, recommended | covered |
| n16 | object | design_parameters, requirement, recommended | covered |
| n17 | object | config_setting, recommended | covered |
| n18 | action | promotional_event, recommended | covered |
| n19 | action | performance_tracking, recommended | covered |
| n20 | action | calculation, performance_tracking, recommended | covered |
| n21 | action | performance_tracking, recommended | covered |
| n22 | constraint | constraint_realistic, recommended | covered |
| n23 | action | preserve, recommended | covered |
| n24 | action | obligation, recommended | covered |
| n25 | negation | exclude, recommended | covered |
| n26 | speech_act | offer, offer_help | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s46 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
