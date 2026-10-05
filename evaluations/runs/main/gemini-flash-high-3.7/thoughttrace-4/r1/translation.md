Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="side_hustle") -> subject_2 : TERM
    TERM activity(actor=role_user, object=subject_2, verb="plan") -> activity_2 : TERM
    TERM decision(activity=activity_2) -> decision_2 : TERM
    UTTER ask(target=decision_2)
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM subject(kind="skills_and_interests", qualifier=personal_values) -> subject_3 : TERM
    TERM activity(actor=role_user, object=subject_3, verb="assess") -> activity_3 : TERM
    CLAIM recommended(target=activity_3) BY role_agent STATUS asserted SOURCE "t2:s3" -> recommended_2 : CLAIM
    TERM duration(amount=1, unit=unit_week) -> duration_2 : TERM
    TERM activity(actor=role_user, object=duration_2, verb="dedicate") -> activity_4 : TERM
    CLAIM recommended(target=activity_4) BY role_agent STATUS asserted SOURCE "t2:s5" -> recommended_3 : CLAIM
    TERM constraint_budget_limited() -> constraint_budget_limited_2 : TERM
    TERM activity(actor=role_user, object=constraint_budget_limited_2, verb="budget") -> activity_5 : TERM
    CLAIM recommended(target=activity_5) BY role_agent STATUS asserted SOURCE "t2:s6" -> recommended_4 : CLAIM
    TERM subject(kind="financial_goals") -> subject_4 : TERM
    CLAIM has_goal(goal=subject_4, subject=role_user) BY role_agent STATUS asserted SOURCE "t2:s7" -> has_goal_2 : CLAIM
    TERM subject(kind="business_options", qualifier=topic_ai_earning_methods) -> subject_5 : TERM
    TERM activity(actor=role_user, object=subject_5, verb="choose") -> activity_6 : TERM
    CLAIM recommended(target=activity_6) BY role_agent STATUS asserted SOURCE "t2:s9" -> recommended_5 : CLAIM
    TERM subject(kind="market_demand") -> subject_6 : TERM
    TERM activity(actor=role_user, object=subject_6, verb="validate") -> activity_7 : TERM
    CLAIM recommended(target=activity_7) BY role_agent STATUS asserted SOURCE "t2:s18" -> recommended_6 : CLAIM
    TERM audience_targeting(audience=role_customer, criteria=["demographics"]) -> audience_targeting_2 : TERM
    CLAIM recommended(target=audience_targeting_2) BY role_agent STATUS asserted SOURCE "t2:s20" -> recommended_7 : CLAIM
    TERM marketing_campaign(channel="market_research", objective="competitive_analysis") -> marketing_campaign_2 : TERM
    CLAIM recommended(target=marketing_campaign_2) BY role_agent STATUS asserted SOURCE "t2:s21" -> recommended_8 : CLAIM
    TERM test_condition(condition="small_scale_viability", expected=TRUE) -> test_condition_2 : TERM
    TERM activity(actor=role_user, object=test_condition_2, verb="test") -> activity_8 : TERM
    CLAIM recommended(target=activity_8) BY role_agent STATUS asserted SOURCE "t2:s22" -> recommended_9 : CLAIM
    TERM subject(kind="smart_goals") -> subject_7 : TERM
    TERM activity(actor=role_user, object=subject_7, verb="plan") -> activity_9 : TERM
    CLAIM recommended(target=activity_9) BY role_agent STATUS asserted SOURCE "t2:s24" -> recommended_10 : CLAIM
    TERM duration(amount=1, unit=unit_day) -> duration_3 : TERM
    TERM activity(actor=role_user, object=duration_3, verb="schedule") -> activity_10 : TERM
    CLAIM recommended(target=activity_10) BY role_agent STATUS asserted SOURCE "t2:s27" -> recommended_11 : CLAIM
    TERM activity(actor=role_user, instrument=platform_label::platform, verb="select_tools") -> activity_11 : TERM
    CLAIM recommended(target=activity_11) BY role_agent STATUS asserted SOURCE "t2:s28" -> recommended_12 : CLAIM
    TERM marketing_campaign(channel="social_media_and_networking", objective="launch") -> marketing_campaign_3 : TERM
    CLAIM recommended(target=marketing_campaign_3) BY role_agent STATUS asserted SOURCE "t2:s30" -> recommended_13 : CLAIM
    TERM performance_tracking(target="customer_feedback") -> performance_tracking_2 : TERM
    CLAIM recommended(target=performance_tracking_2) BY role_agent STATUS asserted SOURCE "t2:s33" -> recommended_14 : CLAIM
    TERM performance_tracking(target="income_and_expenses") -> performance_tracking_3 : TERM
    CLAIM recommended(target=performance_tracking_3) BY role_agent STATUS asserted SOURCE "t2:s36" -> recommended_15 : CLAIM
    TERM performance_tracking(target="profits", adjustment="scale_successful_strategies") -> performance_tracking_4 : TERM
    CLAIM recommended(target=performance_tracking_4) BY role_agent STATUS asserted SOURCE "t2:s37" -> recommended_16 : CLAIM
    TERM duration(amount=8, unit=unit_hour) -> duration_4 : TERM
    TERM activity(actor=role_user, object=duration_4, verb="retain_day_job") -> activity_12 : TERM
    CLAIM recommended(target=activity_12) BY role_agent STATUS asserted SOURCE "t2:s41" -> recommended_17 : CLAIM
    TERM activity(actor=role_user, verb="maintain_consistency") -> activity_13 : TERM
    CLAIM recommended(target=activity_13) BY role_agent STATUS asserted SOURCE "t2:s42" -> recommended_18 : CLAIM
    TERM activity(actor=role_user, instrument=credit_card, verb="separate_finances") -> activity_14 : TERM
    CLAIM recommended(target=activity_14) BY role_agent STATUS asserted SOURCE "t2:s43" -> recommended_19 : CLAIM
    TERM activity(actor=role_user, verb="pay_taxes") -> activity_15 : TERM
    TERM obligation(activity=activity_15, actor=role_user) -> obligation_2 : TERM
    CLAIM recommended(target=obligation_2) BY role_agent STATUS asserted SOURCE "t2:s44" -> recommended_20 : CLAIM
    TERM exclude(item="perfectionism_delay") -> exclude_2 : TERM
    CLAIM recommended(target=exclude_2) BY role_agent STATUS asserted SOURCE "t2:s45" -> recommended_21 : CLAIM
    TERM offer_help() -> offer_help_2 : TERM
    UTTER offer(target=offer_help_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, offer | covered |
| n2 | action | topic_ai_earning_methods, decision | covered |
| n3 | object | role_agent, role_customer | covered |
| n4 | action | personal_values, obligation, audience_targeting, activity, has_goal, role_agent | covered |
| n5 | object | personal_values, role_agent, role_customer, role_user | covered |
| n6 | temporal | unit_day, unit_week, unit_hour, role_customer | covered |
| n7 | object | constraint_budget_limited | covered |
| n8 | object | has_goal, target, constraint_budget_limited, topic_ai_earning_methods, audience_targeting | covered |
| n9 | action | decision | covered |
| n10 | object | topic_ai_earning_methods | covered |
| n11 | action | marketing_campaign, obligation | covered |
| n12 | object | audience_targeting, role_customer, target, role_user | covered |
| n13 | object | marketing_campaign, role_customer, audience_targeting | covered |
| n14 | action | test_condition, decision, obligation, recommended | covered |
| n15 | action | has_goal | covered |
| n16 | object | performance_tracking, unit_hour, unit_day, unit_week | covered |
| n17 | object | platform_label, activity | label-preserved |
| n18 | action | offer, marketing_campaign, audience_targeting, offer_help, role_customer | covered |
| n19 | action | role_customer, performance_tracking | covered |
| n20 | action | performance_tracking, obligation, duration, topic_ai_earning_methods | covered |
| n21 | action | performance_tracking, obligation | covered |
| n22 | constraint | unit_hour, unit_week, unit_day, constraint_budget_limited | covered |
| n23 | action | personal_values, credit_card, constraint_budget_limited, role_customer, obligation | covered |
| n24 | action | obligation, constraint_budget_limited, topic_ai_earning_methods | covered |
| n25 | negation | exclude | covered |
| n26 | speech_act | offer, offer_help, role_agent, ask | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1-t2:s46 is represented
- Opaque-text spans: none
- Label-preserved spans: t2:s28 "tools/platforms" -> platform_label::platform (label only; generic software platform category)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
