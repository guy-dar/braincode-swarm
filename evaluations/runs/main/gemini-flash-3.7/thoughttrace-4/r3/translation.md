Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="business", qualifier="side_hustle") -> subject_2 : TERM
    TERM activity(object=art_plan, purpose=subject_2, verb="create") -> activity_2 : TERM
    UTTER ask(target=activity_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM subject(kind="skills_talents_interests") -> subject_3 : TERM
    TERM activity(object=subject_3, verb="self_assessment") -> activity_3 : TERM
    CLAIM recommended(target=activity_3) BY role_agent STATUS asserted SOURCE "t2:s3" -> recommended_2 : CLAIM
    TERM duration(amount=1, unit=unit_week) -> duration_2 : TERM
    TERM requirement(property="time_commitment", value=duration_2) -> requirement_2 : TERM
    CLAIM recommended(target=requirement_2) BY role_agent STATUS asserted SOURCE "t2:s5" -> recommended_3 : CLAIM
    TERM constraint_budget_limited() -> constraint_budget_limited_2 : TERM
    CLAIM recommended(target=constraint_budget_limited_2) BY role_agent STATUS asserted SOURCE "t2:s6" -> recommended_4 : CLAIM
    TERM subject(kind="financial_goals") -> subject_4 : TERM
    CLAIM has_goal(goal=subject_4, subject=role_user) BY role_agent STATUS asserted SOURCE "t2:s7" -> has_goal_2 : CLAIM
    TERM activity(object="side_hustle", verb="choose") -> activity_4 : TERM
    TERM decision(activity=activity_4) -> decision_2 : TERM
    CLAIM recommended(target=decision_2) BY role_agent STATUS asserted SOURCE "t2:s9" -> recommended_5 : CLAIM
    TERM topic_ai_earning_methods() -> topic_ai_earning_methods_2 : TERM
    CLAIM considered(subject=topic_ai_earning_methods_2) BY role_agent STATUS asserted SOURCE "t2:s10" -> considered_2 : CLAIM
    TERM subject(kind="market_demand") -> subject_5 : TERM
    TERM activity(object=subject_5, verb="validate") -> activity_5 : TERM
    CLAIM recommended(target=activity_5) BY role_agent STATUS asserted SOURCE "t2:s18" -> recommended_6 : CLAIM
    TERM audience_targeting(criteria=["demographics"]) -> audience_targeting_2 : TERM
    CLAIM recommended(target=audience_targeting_2) BY role_agent STATUS asserted SOURCE "t2:s20" -> recommended_7 : CLAIM
    TERM subject(kind="competition") -> subject_6 : TERM
    CLAIM considered(subject=subject_6) BY role_agent STATUS asserted SOURCE "t2:s21" -> considered_3 : CLAIM
    TERM requirement(property="scale", value=size_small) -> requirement_3 : TERM
    TERM test_condition(condition="business_idea", expected=TRUE) -> test_condition_2 : TERM
    CLAIM recommended(target=test_condition_2) BY role_agent STATUS asserted SOURCE "t2:s22" -> recommended_8 : CLAIM
    TERM subject(kind="smart_goals") -> subject_7 : TERM
    CLAIM has_goal(goal=subject_7, subject=role_user) BY role_agent STATUS asserted SOURCE "t2:s25" -> has_goal_3 : CLAIM
    TERM requirement(property="schedule_prevent_burnout", value=TRUE) -> requirement_4 : TERM
    CLAIM recommended(target=requirement_4) BY role_agent STATUS asserted SOURCE "t2:s27" -> recommended_9 : CLAIM
    TERM requirement(property="tools_platforms", value=platform_label::tools) -> requirement_5 : TERM
    CLAIM recommended(target=requirement_5) BY role_agent STATUS asserted SOURCE "t2:s28" -> recommended_10 : CLAIM
    TERM marketing_campaign(target=object_label::offering, channel="social_media_network") -> marketing_campaign_2 : TERM
    CLAIM recommended(target=marketing_campaign_2) BY role_agent STATUS asserted SOURCE "t2:s30" -> recommended_11 : CLAIM
    TERM performance_tracking(target=role_customer) -> performance_tracking_2 : TERM
    CLAIM recommended(target=performance_tracking_2) BY role_agent STATUS asserted SOURCE "t2:s33" -> recommended_12 : CLAIM
    TERM performance_tracking(target="income_expenses") -> performance_tracking_3 : TERM
    CLAIM recommended(target=performance_tracking_3) BY role_agent STATUS asserted SOURCE "t2:s36" -> recommended_13 : CLAIM
    TERM activity(object="profits_and_strategies", verb="reinvest_and_scale") -> activity_6 : TERM
    CLAIM recommended(target=activity_6) BY role_agent STATUS asserted SOURCE "t2:s37" -> recommended_14 : CLAIM
    TERM requirement(property="keep_day_job", value=state_full) -> requirement_6 : TERM
    CLAIM recommended(target=requirement_6) BY role_agent STATUS asserted SOURCE "t2:s41" -> recommended_15 : CLAIM
    TERM activity(object="personal_and_business_finances", verb="separate") -> activity_7 : TERM
    CLAIM recommended(target=activity_7) BY role_agent STATUS asserted SOURCE "t2:s43" -> recommended_16 : CLAIM
    TERM activity(object="tax_obligations", verb="learn_and_comply") -> activity_8 : TERM
    TERM obligation(activity=activity_8, actor=role_user) -> obligation_2 : TERM
    CLAIM recommended(target=obligation_2) BY role_agent STATUS asserted SOURCE "t2:s44" -> recommended_17 : CLAIM
    TERM exclude(item="delay_due_to_perfectionism") -> exclude_2 : TERM
    CLAIM recommended(target=exclude_2) BY role_agent STATUS asserted SOURCE "t2:s45" -> recommended_18 : CLAIM
    TERM offer_help() -> offer_help_2 : TERM
    UTTER offer(target=offer_help_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask | covered |
| n2 | action | art_plan, activity | covered |
| n3 | object | subject | covered |
| n4 | action | activity, recommended | covered |
| n5 | object | subject | covered |
| n6 | temporal | duration, unit_week | covered |
| n7 | object | constraint_budget_limited | covered |
| n8 | object | has_goal, role_user | covered |
| n9 | action | decision, activity, recommended | covered |
| n10 | object | topic_ai_earning_methods, considered | covered |
| n11 | action | activity, recommended | covered |
| n12 | object | audience_targeting | covered |
| n13 | object | subject, considered | covered |
| n14 | action | requirement, size_small, test_condition | covered |
| n15 | action | has_goal, subject | covered |
| n16 | object | requirement | covered |
| n17 | object | requirement, platform_label::tools | label-preserved |
| n18 | action | marketing_campaign, object_label::offering | label-preserved |
| n19 | action | performance_tracking, role_customer | covered |
| n20 | action | performance_tracking | covered |
| n21 | action | activity, recommended | covered |
| n22 | constraint | requirement, state_full | covered |
| n23 | action | activity, recommended | covered |
| n24 | action | obligation, activity | covered |
| n25 | negation | exclude | covered |
| n26 | speech_act | offer, offer_help | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s46 is represented
- Opaque-text spans: none
- Label-preserved spans:
  - t2:s28 "tools/platforms" → platform_label::tools (label only; no sense resolved)
  - t2:s30 "offering" → object_label::offering (label only; no sense resolved)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
