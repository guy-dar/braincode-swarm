Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="work") -> subject_work : TERM
    TERM subject(kind="working_hours") -> subject_working_hours : TERM
    TERM subject(kind="leisure_time") -> subject_leisure_time : TERM
    TERM subject(kind="personal_hobbies") -> subject_hobbies : TERM
    TERM conjunction(items=[subject_work, subject_working_hours, subject_leisure_time, subject_hobbies]) -> conjunction_topics : TERM
    TERM subject(kind="problem", location=country::JP, qualifier=conjunction_topics) -> subject_problem : TERM
    UTTER ask(target=subject_problem)
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM subject(kind="shorter_working_hours") -> subject_shorter_hours : TERM
    TERM subject(kind="flexible_working_arrangements") -> subject_flexible : TERM
    TERM conjunction(items=[subject_shorter_hours, subject_flexible]) -> conjunction_arrangements : TERM
    TERM subject(kind="employee_morale") -> subject_morale : TERM
    TERM subject(kind="work_life_balance") -> subject_wlb : TERM
    TERM conjunction(items=[subject_morale, subject_wlb]) -> conjunction_goals : TERM
    TERM activity(verb="improve", object=conjunction_goals) -> activity_improve : TERM
    TERM activity(verb="adopt", actor="japanese_companies", location=country::JP, object=conjunction_arrangements, purpose=activity_improve) -> activity_adopt : TERM
    CLAIM ongoing(target=activity_adopt) BY role_agent STATUS asserted SOURCE "t2:s1" -> ongoing_2 : CLAIM
    CLAIM occurred_recently(target=ongoing_2) BY role_agent STATUS asserted SOURCE "t2:s1" -> occurred_recently_2 : CLAIM
    TERM subject(kind="business_productivity") -> subject_productivity : TERM
    TERM subject(kind="business_growth") -> subject_growth : TERM
    TERM conjunction(items=[subject_productivity, subject_growth]) -> conjunction_business : TERM
    CLAIM enables(condition=conjunction_arrangements, outcome=conjunction_business) BY role_agent STATUS reported SOURCE "t2:s2" -> enables_2 : CLAIM
    TERM subject(kind="longer_working_hours") -> subject_longer_hours : TERM
    TERM activity(verb="finish", actor="japanese_employees", object="work") -> activity_finish : TERM
    TERM activity(verb="work", actor="japanese_employees", location=country::JP, object=subject_longer_hours, purpose=activity_finish) -> activity_work : TERM
    CLAIM leads_to(cause=conjunction_arrangements, effect=activity_work) BY role_agent STATUS hypothesized SOURCE "t2:s3" -> leads_to_2 : CLAIM
    LINK contrast(first=enables_2, second=leads_to_2) SOURCE "t2:s3"
    TERM subject(kind="workloads") -> subject_workloads : TERM
    CLAIM attribute_claim(subject=subject_workloads, property="level", value="high") BY role_agent STATUS hypothesized SOURCE "t2:s5" -> attribute_claim_2 : CLAIM
    LINK supports(conclusion=leads_to_2, premise=attribute_claim_2) SOURCE "t2:s5"
    CLAIM attribute_claim(subject=conjunction_arrangements, property="popularity", value="increasing") BY role_agent STATUS asserted SOURCE "t2:s4" -> attribute_claim_3 : CLAIM
    TERM subject(kind="issues", location=country::JP) -> subject_issues : TERM
    CLAIM leads_to(cause=conjunction_arrangements, effect=subject_issues) BY role_agent STATUS hypothesized SOURCE "t2:s4" -> leads_to_3 : CLAIM
    LINK contrast(first=attribute_claim_3, second=leads_to_3) SOURCE "t2:s4"
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    TERM measure(amount=2, unit=unit_item) -> measure_2 : TERM
    TERM at_least(measure=measure_2) -> at_least_2 : TERM
    TERM requirement(property="usual_number_of_jobs_per_person", value=at_least_2) -> requirement_2 : TERM
    TERM subject(kind="japanese_people", location=country::JP, qualifier=requirement_2) -> subject_people : TERM
    UTTER ask(target=subject_people)
  }
  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    TERM subject(kind="multiple_part_time_jobs", location=country::JP) -> subject_jobs : TERM
    TERM subject(kind="uncommon") -> subject_uncommon : TERM
    TERM negation(target=subject_uncommon) -> negation_2 : TERM
    CLAIM attribute_claim(subject=subject_jobs, property="commonness", value=negation_2) BY role_agent STATUS asserted SOURCE "t4:s1" -> attribute_claim_4 : CLAIM
    UTTER confirm(target=attribute_claim_4)
    TERM subject(kind="balance_of_time_and_income") -> subject_balance : TERM
    CLAIM enables(condition=subject_jobs, outcome=subject_balance) BY role_agent STATUS asserted SOURCE "t4:s2" -> enables_3 : CLAIM
    TERM subject(kind="lack_of_free_time") -> subject_lack_free_time : TERM
    TERM subject(kind="stress") -> subject_stress : TERM
    TERM conjunction(items=[subject_lack_free_time, subject_stress]) -> conjunction_harms : TERM
    CLAIM leads_to(cause=subject_jobs, effect=conjunction_harms) BY role_agent STATUS hypothesized SOURCE "t4:s2" -> leads_to_4 : CLAIM
    LINK contrast(first=enables_3, second=leads_to_4) SOURCE "t4:s2"
    TERM subject(kind="free_time") -> subject_free_time : TERM
    TERM subject(kind="hobbies") -> subject_hobbies_2 : TERM
    TERM subject(kind="work_life_balance") -> subject_wlb_2 : TERM
    TERM conjunction(items=[subject_free_time, subject_hobbies_2, subject_wlb_2]) -> conjunction_valued : TERM
    TERM subject(kind="japanese_workers", location=country::JP, qualifier="many") -> subject_workers : TERM
    CLAIM attribute_claim(subject=subject_workers, property="values", value=conjunction_valued) BY role_agent STATUS asserted SOURCE "t4:s3" -> attribute_claim_5 : CLAIM
    LINK contrast(first=leads_to_4, second=attribute_claim_5) SOURCE "t4:s3"
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, subject, conjunction | covered |
| n2 | object | country::JP | covered |
| n3 | object | subject, conjunction | covered |
| n4 | object | subject, conjunction | covered |
| n5 | temporal | occurred_recently | covered |
| n6 | claim | activity, ongoing | covered |
| n7 | claim | activity (purpose), conjunction | covered |
| n8 | claim | enables | covered |
| n9 | claim | leads_to, activity | covered |
| n10 | reasoning | attribute_claim, supports | covered |
| n11 | claim | attribute_claim, leads_to, contrast | covered |
| n12 | object | country::JP | covered |
| n13 | speech_act | ask, requirement | covered |
| n14 | object | subject | covered |
| n15 | constraint | at_least, measure | covered |
| n16 | speech_act | confirm, negation, attribute_claim | covered |
| n17 | object | country::JP | covered |
| n18 | claim | enables | covered |
| n19 | claim | leads_to, contrast | covered |
| n20 | claim | attribute_claim, contrast | covered |

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: all of t1:s1–t4:s6 represented; t2:s5 restated content merged into t2:s3/t2:s5 claims; t4:s4–s6 repeat t4:s1–s3 and reuse those bindings (SOURCE cites first occurrence)
- Opaque-text spans: none
- Label-preserved spans: t1:s1, t2:s4, t4:s1, t4:s4 "Japan" → country::JP (standard code)
- Missing constructs: no dedicated problem-question or frequency ("usually") constructor, so "usually" is folded into the requirement property name; "remain high" has no persistence relation; anonymous attribution of "is believed" uses role_agent with status reported
- Unresolved ambiguities: t1:s1 "things Japanese people like" encoded as leisure time/hobbies; t2:s3 "may" encoded as hypothesized
- Check: `rag check` reported n3, n4, n9 as declared-only (covered via generic subject/activity constructors with exact-kind strings; no matching glossary symbol exists); 0 unknown symbols
