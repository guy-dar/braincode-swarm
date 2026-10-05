Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="side_hustle") -> subject_2 : TERM
    TERM activity(object=subject_2, verb="plan") -> activity_2 : TERM
    UTTER ask(target=activity_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM property_question(property="skills_talents_interests", subject=role_user) -> property_question_2 : TERM
    TERM activity(object=property_question_2, verb="self_assessment") -> activity_3 : TERM
    CLAIM recommended(target=activity_3) BY role_agent STATUS asserted SOURCE "t2:s3" -> recommended_2 : CLAIM
    TERM duration(amount=1, unit=unit_week) -> duration_2 : TERM
    TERM property_question(property="time_commitment", subject=duration_2) -> property_question_3 : TERM
    CLAIM recommended(target=property_question_3) BY role_agent STATUS asserted SOURCE "t2:s5" -> recommended_3 : CLAIM
    TERM constraint_budget_limited() -> constraint_budget_limited_2 : TERM
    TERM property_question(property="startup_budget", subject=constraint_budget_limited_2) -> property_question_4 : TERM
    CLAIM recommended(target=property_question_4) BY role_agent STATUS asserted SOURCE "t2:s6" -> recommended_4 : CLAIM
    TERM subject(kind="financial_goals") -> subject_3 : TERM
    CLAIM has_goal(goal=subject_3, subject=role_user) BY role_agent STATUS asserted SOURCE "t2:s7" -> has_goal_2 : CLAIM
    TERM subject(kind="freelancing") -> subject_4 : TERM
    TERM subject(kind="ecommerce") -> subject_5 : TERM
    TERM subject(kind="content_creation") -> subject_6 : TERM
    TERM subject(kind="tutoring") -> subject_7 : TERM
    TERM subject(kind="rideshare") -> subject_8 : TERM
    TERM subject(kind="digital_products") -> subject_9 : TERM
    TERM conjunction(items=[subject_4, subject_5, subject_6, subject_7, subject_8, subject_9]) -> conjunction_2 : TERM
    TERM activity(object=conjunction_2, verb="choose_hustle") -> activity_4 : TERM
    TERM decision(activity=activity_4) -> decision_2 : TERM
    CLAIM recommended(target=decision_2) BY role_agent STATUS asserted SOURCE "t2:s9" -> recommended_5 : CLAIM
    TERM activity(object=subject_2, verb="validate_demand") -> activity_5 : TERM
    CLAIM recommended(target=activity_5) BY role_agent STATUS asserted SOURCE "t2:s18" -> recommended_6 : CLAIM
    TERM audience_targeting(audience=role_customer, criteria=["target_audience"]) -> audience_targeting_2 : TERM
    CLAIM recommended(target=audience_targeting_2) BY role_agent STATUS asserted SOURCE "t2:s20" -> recommended_7 : CLAIM
    TERM subject(kind="competition") -> subject_10 : TERM
    CLAIM recommended(target=subject_10) BY role_agent STATUS asserted SOURCE "t2:s21" -> recommended_8 : CLAIM
    TERM requirement(property="scale", value="small") -> requirement_2 : TERM
    TERM activity(purpose=requirement_2, verb="test_idea") -> activity_6 : TERM
    CLAIM recommended(target=activity_6) BY role_agent STATUS asserted SOURCE "t2:s22" -> recommended_9 : CLAIM
    TERM subject(kind="smart_goals") -> subject_11 : TERM
    CLAIM has_goal(goal=subject_11, subject=art_plan) BY role_agent STATUS asserted SOURCE "t2:s25" -> has_goal_3 : CLAIM
    TERM subject(kind="schedule_prevent_burnout") -> subject_12 : TERM
    CLAIM recommended(target=subject_12) BY role_agent STATUS asserted SOURCE "t2:s27" -> recommended_10 : CLAIM
    TERM subject(kind="tools_and_platforms") -> subject_13 : TERM
    CLAIM recommended(target=subject_13) BY role_agent STATUS asserted SOURCE "t2:s28" -> recommended_11 : CLAIM
    TERM marketing_campaign(channel="social_media", objective="launch_and_market") -> marketing_campaign_2 : TERM
    CLAIM recommended(target=marketing_campaign_2) BY role_agent STATUS asserted SOURCE "t2:s30" -> recommended_12 : CLAIM
    TERM activity(actor=role_user, object=role_customer, verb="gather_feedback") -> activity_7 : TERM
    CLAIM recommended(target=activity_7) BY role_agent STATUS asserted SOURCE "t2:s33" -> recommended_13 : CLAIM
    TERM subject(kind="income_and_expenses") -> subject_14 : TERM
    TERM performance_tracking(target=subject_14) -> performance_tracking_2 : TERM
    CLAIM recommended(target=performance_tracking_2) BY role_agent STATUS asserted SOURCE "t2:s36" -> recommended_14 : CLAIM
    TERM activity(verb="reinvest_profits") -> activity_8 : TERM
    CLAIM recommended(target=activity_8) BY role_agent STATUS asserted SOURCE "t2:s37" -> recommended_15 : CLAIM
    TERM activity(verb="scale_what_works") -> activity_9 : TERM
    CLAIM recommended(target=activity_9) BY role_agent STATUS asserted SOURCE "t2:s39" -> recommended_16 : CLAIM
    TERM requirement(property="retain_day_job_until_stable", value=TRUE) -> requirement_3 : TERM
    CLAIM recommended(target=requirement_3) BY role_agent STATUS asserted SOURCE "t2:s41" -> recommended_17 : CLAIM
    TERM subject(kind="personal_finances") -> subject_15 : TERM
    TERM subject(kind="business_finances") -> subject_16 : TERM
    TERM distinguish(first=subject_15, second=subject_16) -> distinguish_2 : TERM
    CLAIM recommended(target=distinguish_2) BY role_agent STATUS asserted SOURCE "t2:s43" -> recommended_18 : CLAIM
    TERM subject(kind="extra_income") -> subject_17 : TERM
    TERM activity(object=subject_17, verb="learn_tax_obligations") -> activity_10 : TERM
    TERM obligation(activity=activity_10, actor=role_user) -> obligation_2 : TERM
    CLAIM recommended(target=obligation_2) BY role_agent STATUS asserted SOURCE "t2:s44" -> recommended_19 : CLAIM
    TERM exclude(item="perfectionism") -> exclude_2 : TERM
    TERM activity(purpose=exclude_2, verb="start") -> activity_11 : TERM
    CLAIM recommended(target=activity_11) BY role_agent STATUS asserted SOURCE "t2:s45" -> recommended_20 : CLAIM
    TERM offer_help() -> offer_help_2 : TERM
    UTTER offer(target=offer_help_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask | covered |
| n2 | action | activity | covered |
| n3 | object | subject | covered |
| n4 | action | activity, recommended | covered |
| n5 | object | property_question, role_user | covered |
| n6 | temporal | duration, unit_week, property_question | covered |
| n7 | object | constraint_budget_limited, property_question | covered |
| n8 | object | has_goal, subject, role_user | covered |
| n9 | action | decision, activity, recommended | covered |
| n10 | object | conjunction, subject | covered |
| n11 | action | activity, recommended | covered |
| n12 | object | audience_targeting, role_customer | covered |
| n13 | object | subject, recommended | covered |
| n14 | action | activity, requirement, recommended | covered |
| n15 | action | has_goal, art_plan | covered |
| n16 | object | subject, recommended | covered |
| n17 | object | subject, recommended | covered |
| n18 | action | marketing_campaign, recommended | covered |
| n19 | action | activity, role_user, role_customer, recommended | covered |
| n20 | action | performance_tracking, subject, recommended | covered |
| n21 | action | activity, recommended | covered |
| n22 | constraint | requirement, recommended | covered |
| n23 | action | distinguish, subject, recommended | covered |
| n24 | action | obligation, activity, subject, role_user, recommended | covered |
| n25 | negation | exclude, activity, recommended | covered |
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
