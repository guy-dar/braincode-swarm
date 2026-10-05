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
    TERM subject(kind="skills") -> subject_3 : TERM
    TERM subject(kind="talents") -> subject_4 : TERM
    TERM subject(kind="interests") -> subject_5 : TERM
    TERM conjunction(items=[subject_3, subject_4, subject_5]) -> conjunction_2 : TERM
    TERM activity(actor=role_user, object=conjunction_2, verb="assess") -> activity_3 : TERM
    CLAIM recommended(target=activity_3) BY role_agent STATUS asserted SOURCE "t2:s3" -> recommended_2 : CLAIM
    TERM property_question(property="time_commitment", subject=unit_week) -> property_question_2 : TERM
    CLAIM considered(subject=property_question_2) BY role_agent STATUS asserted SOURCE "t2:s5" -> considered_2 : CLAIM
    TERM constraint_budget_limited() -> constraint_budget_limited_2 : TERM
    CLAIM considered(subject=constraint_budget_limited_2) BY role_agent STATUS asserted SOURCE "t2:s6" -> considered_3 : CLAIM
    TERM subject(kind="financial_goals") -> subject_6 : TERM
    CLAIM has_goal(goal=subject_6, subject=role_user) BY role_agent STATUS asserted SOURCE "t2:s7" -> has_goal_2 : CLAIM
    TERM subject(kind="freelancing") -> subject_7 : TERM
    TERM subject(kind="ecommerce") -> subject_8 : TERM
    TERM subject(kind="content_creation") -> subject_9 : TERM
    TERM subject(kind="tutoring") -> subject_10 : TERM
    TERM subject(kind="delivery_rideshare") -> subject_11 : TERM
    TERM subject(kind="digital_products") -> subject_12 : TERM
    TERM conjunction(items=[subject_7, subject_8, subject_9, subject_10, subject_11, subject_12]) -> conjunction_3 : TERM
    TERM subject(kind="business_options", qualifier=art_plan) -> subject_13 : TERM
    TERM activity(actor=role_user, object=conjunction_3, purpose=subject_13, verb="choose") -> activity_4 : TERM
    TERM decision(activity=activity_4) -> decision_3 : TERM
    CLAIM recommended(target=decision_3) BY role_agent STATUS asserted SOURCE "t2:s9" -> recommended_3 : CLAIM
    CLAIM considered(subject=conjunction_3) BY role_agent STATUS asserted SOURCE "t2:s10" -> considered_4 : CLAIM
    TERM subject(kind="market_demand") -> subject_14 : TERM
    TERM activity(actor=role_user, object=subject_14, verb="validate") -> activity_5 : TERM
    CLAIM recommended(target=activity_5) BY role_agent STATUS asserted SOURCE "t2:s18" -> recommended_4 : CLAIM
    TERM audience_targeting(audience=role_customer, criteria=["target_demographic"]) -> audience_targeting_2 : TERM
    CLAIM considered(subject=audience_targeting_2) BY role_agent STATUS asserted SOURCE "t2:s20" -> considered_5 : CLAIM
    TERM subject(kind="competition") -> subject_15 : TERM
    CLAIM considered(subject=subject_15) BY role_agent STATUS asserted SOURCE "t2:s21" -> considered_6 : CLAIM
    TERM requirement(property="scale", value=size_small) -> requirement_2 : TERM
    TERM activity(actor=role_user, purpose=requirement_2, verb="test") -> activity_6 : TERM
    CLAIM recommended(target=activity_6) BY role_agent STATUS asserted SOURCE "t2:s22" -> recommended_5 : CLAIM
    TERM subject(kind="smart_goals") -> subject_16 : TERM
    TERM activity(actor=role_user, object=subject_16, verb="plan") -> activity_7 : TERM
    CLAIM recommended(target=activity_7) BY role_agent STATUS asserted SOURCE "t2:s24" -> recommended_6 : CLAIM
    TERM self_protection(actor=role_user, domain="workload", strategy="prevent_burnout") -> self_protection_2 : TERM
    TERM subject(kind="schedule", qualifier=self_protection_2) -> subject_17 : TERM
    CLAIM recommended(target=subject_17) BY role_agent STATUS asserted SOURCE "t2:s27" -> recommended_7 : CLAIM
    TERM subject(kind="tools_and_platforms") -> subject_18 : TERM
    TERM activity(actor=role_user, object=subject_18, verb="choose") -> activity_8 : TERM
    CLAIM recommended(target=activity_8) BY role_agent STATUS asserted SOURCE "t2:s28" -> recommended_8 : CLAIM
    TERM marketing_campaign(channel="social_media", objective="networking") -> marketing_campaign_2 : TERM
    TERM activity(actor=role_user, object=marketing_campaign_2, verb="launch") -> activity_9 : TERM
    CLAIM recommended(target=activity_9) BY role_agent STATUS asserted SOURCE "t2:s30" -> recommended_9 : CLAIM
    TERM activity(actor=role_user, object=role_customer, verb="gather_feedback") -> activity_10 : TERM
    CLAIM recommended(target=activity_10) BY role_agent STATUS asserted SOURCE "t2:s33" -> recommended_10 : CLAIM
    TERM performance_tracking(target="income_and_expenses") -> performance_tracking_2 : TERM
    TERM activity(actor=role_user, object=performance_tracking_2, verb="track") -> activity_11 : TERM
    CLAIM recommended(target=activity_11) BY role_agent STATUS asserted SOURCE "t2:s36" -> recommended_11 : CLAIM
    TERM activity(actor=role_user, object="profits", verb="reinvest") -> activity_12 : TERM
    TERM activity(actor=role_user, object="successful_strategies", verb="scale") -> activity_13 : TERM
    TERM conjunction(items=[activity_12, activity_13]) -> conjunction_4 : TERM
    CLAIM recommended(target=conjunction_4) BY role_agent STATUS asserted SOURCE "t2:s37" -> recommended_12 : CLAIM
    TERM requirement(property="stability", value="stable") -> requirement_3 : TERM
    TERM activity(actor=role_user, object="day_job", verb="retain") -> activity_14 : TERM
    TERM conditional(condition=requirement_3, consequence=activity_14) -> conditional_2 : TERM
    CLAIM recommended(target=conditional_2) BY role_agent STATUS asserted SOURCE "t2:s41" -> recommended_13 : CLAIM
    TERM subject(kind="personal_finances") -> subject_19 : TERM
    TERM subject(kind="business_finances") -> subject_20 : TERM
    TERM distinguish(first=subject_19, second=subject_20) -> distinguish_2 : TERM
    TERM activity(actor=role_user, object=distinguish_2, verb="separate") -> activity_15 : TERM
    CLAIM recommended(target=activity_15) BY role_agent STATUS asserted SOURCE "t2:s43" -> recommended_14 : CLAIM
    TERM activity(actor=role_user, object="supplemental_income", verb="tax_compliance") -> activity_16 : TERM
    TERM obligation(activity=activity_16, actor=role_user) -> obligation_2 : TERM
    CLAIM recommended(target=obligation_2) BY role_agent STATUS asserted SOURCE "t2:s44" -> recommended_15 : CLAIM
    TERM activity(actor=role_user, purpose="perfectionism", verb="delay") -> activity_17 : TERM
    TERM exclude(item=activity_17) -> exclude_2 : TERM
    CLAIM recommended(target=exclude_2) BY role_agent STATUS asserted SOURCE "t2:s45" -> recommended_16 : CLAIM
    TERM activity(actor=role_agent, purpose=t1.subject_2, verb="brainstorm") -> activity_18 : TERM
    UTTER offer(target=activity_18)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, decision | covered |
| n2 | action | activity, decision | covered |
| n3 | object | subject | covered |
| n4 | action | activity, conjunction, recommended, subject | covered |
| n5 | object | conjunction, subject | covered |
| n6 | temporal | considered, property_question, unit_week | covered |
| n7 | object | considered, constraint_budget_limited | covered |
| n8 | object | has_goal, subject | covered |
| n9 | action | activity, conjunction, decision, recommended | covered |
| n10 | object | art_plan, conjunction, considered, subject | covered |
| n11 | action | activity, recommended, subject | covered |
| n12 | object | audience_targeting, considered, role_customer | covered |
| n13 | object | considered, subject | covered |
| n14 | action | activity, recommended, requirement, size_small | covered |
| n15 | action | activity, recommended, subject | covered |
| n16 | object | recommended, self_protection, subject | covered |
| n17 | object | activity, recommended, subject | covered |
| n18 | action | activity, marketing_campaign, recommended | covered |
| n19 | action | activity, recommended, role_customer | covered |
| n20 | action | activity, performance_tracking, recommended | covered |
| n21 | action | activity, conjunction, recommended | covered |
| n22 | constraint | activity, conditional, recommended, requirement | covered |
| n23 | action | activity, distinguish, recommended, subject | covered |
| n24 | action | activity, obligation, recommended | covered |
| n25 | negation | activity, exclude, recommended | covered |
| n26 | speech_act | activity, offer | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s46 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
