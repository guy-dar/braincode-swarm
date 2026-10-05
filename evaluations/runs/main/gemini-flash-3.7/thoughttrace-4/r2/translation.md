Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(actor=role_user, object="side_hustle", verb="plan") -> activity_2 : TERM
    UTTER ask(target=activity_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM property_question(property="skills_talents_interests", subject=role_user) -> property_question_2 : TERM
    TERM duration(amount=1, unit=unit_week) -> duration_2 : TERM
    TERM property_question(property="time_commitment", subject=duration_2) -> property_question_3 : TERM
    TERM constraint_budget_limited() -> constraint_budget_limited_2 : TERM
    TERM subject(kind="financial_goals") -> subject_2 : TERM
    TERM conjunction(items=[property_question_2, property_question_3, constraint_budget_limited_2, subject_2]) -> conjunction_2 : TERM
    TERM document_section(items=[conjunction_2], title="Self-Assessment") -> document_section_2 : TERM
    TERM subject(kind="business_options", qualifier="freelancing_ecommerce_content_tutoring_rideshare_crafts") -> subject_3 : TERM
    TERM activity(actor=role_user, object=subject_3, verb="choose") -> activity_3 : TERM
    TERM decision(activity=activity_3) -> decision_2 : TERM
    TERM document_section(items=[decision_2], title="Choose Your Hustle") -> document_section_3 : TERM
    TERM subject(kind="market_demand") -> subject_4 : TERM
    TERM audience_targeting(audience=role_customer, criteria=["demographics"]) -> audience_targeting_2 : TERM
    TERM subject(kind="competition") -> subject_5 : TERM
    TERM test_condition(condition="small_scale_test", expected=TRUE) -> test_condition_2 : TERM
    TERM conjunction(items=[subject_4, audience_targeting_2, subject_5, test_condition_2]) -> conjunction_3 : TERM
    TERM document_section(items=[conjunction_3], title="Research & Validate") -> document_section_4 : TERM
    TERM subject(kind="goals", qualifier="SMART") -> subject_6 : TERM
    CLAIM has_goal(goal=subject_6, subject=role_user) BY role_agent STATUS asserted SOURCE "t2:s25" -> has_goal_2 : CLAIM
    TERM requirement(property="plan_type", value=art_plan) -> requirement_2 : TERM
    TERM self_protection(actor=role_user, domain="burnout") -> self_protection_2 : TERM
    TERM requirement(property="tools_platforms", value=TRUE) -> requirement_3 : TERM
    TERM conjunction(items=[requirement_2, self_protection_2, requirement_3]) -> conjunction_4 : TERM
    TERM document_section(items=[conjunction_4], title="Set Up a Plan") -> document_section_5 : TERM
    TERM marketing_campaign(channel="social_media_and_network", objective="launch_and_market") -> marketing_campaign_2 : TERM
    TERM performance_tracking(target=role_customer) -> performance_tracking_2 : TERM
    TERM conjunction(items=[marketing_campaign_2, performance_tracking_2]) -> conjunction_5 : TERM
    TERM document_section(items=[conjunction_5], title="Launch & Market") -> document_section_6 : TERM
    TERM calculation(inputs=[subject_2], operation="track_income_expenses") -> calculation_2 : TERM
    TERM activity(actor=role_user, object="profitable_strategies", verb="scale") -> activity_4 : TERM
    TERM conjunction(items=[calculation_2, activity_4]) -> conjunction_6 : TERM
    TERM document_section(items=[conjunction_6], title="Grow & Improve") -> document_section_7 : TERM
    TERM requirement(property="retain_day_job", value=state_full) -> requirement_4 : TERM
    TERM activity(actor=role_user, object="personal_and_business_finances", verb="separate") -> activity_5 : TERM
    TERM activity(actor=role_user, object="tax_obligations", verb="comply") -> activity_6 : TERM
    TERM obligation(activity=activity_6, actor=role_user) -> obligation_2 : TERM
    TERM exclude(item="perfectionism") -> exclude_2 : TERM
    TERM conjunction(items=[requirement_4, activity_5, obligation_2, exclude_2]) -> conjunction_7 : TERM
    TERM document_section(items=[conjunction_7], title="Key Tips") -> document_section_8 : TERM
    TERM conjunction(items=[document_section_2, document_section_3, document_section_4, document_section_5, document_section_6, document_section_7, document_section_8]) -> conjunction_8 : TERM
    CLAIM recommended(target=conjunction_8) BY role_agent STATUS asserted SOURCE "t2:s1" -> recommended_2 : CLAIM
    UTTER respond(target=recommended_2)
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
| n3 | object | activity | covered |
| n4 | action | property_question, document_section | covered |
| n5 | object | property_question | covered |
| n6 | temporal | duration, unit_week | covered |
| n7 | object | constraint_budget_limited | covered |
| n8 | object | subject | covered |
| n9 | action | decision, activity | covered |
| n10 | object | subject | covered |
| n11 | action | subject | covered |
| n12 | object | audience_targeting, role_customer | covered |
| n13 | object | subject | covered |
| n14 | action | test_condition | covered |
| n15 | action | has_goal, art_plan | covered |
| n16 | object | self_protection | covered |
| n17 | object | requirement | covered |
| n18 | action | marketing_campaign | covered |
| n19 | action | performance_tracking, role_customer | covered |
| n20 | action | calculation | covered |
| n21 | action | activity | covered |
| n22 | constraint | requirement, state_full | covered |
| n23 | action | activity | covered |
| n24 | action | obligation, activity | covered |
| n25 | negation | exclude | covered |
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
