Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(object=art_itinerary, verb="plan") -> activity_2 : TERM
    UTTER propose(target=activity_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM property_question(property="destination", subject="trip") -> property_question_2 : TERM
    TERM property_question(property="dates", subject="trip") -> property_question_3 : TERM
    TERM property_question(property="party_size", subject="trip") -> property_question_4 : TERM
    TERM property_question(property="style", subject="trip") -> property_question_5 : TERM
    TERM property_question(property="budget", subject="trip") -> property_question_6 : TERM
    UTTER ask(target=property_question_2)
    UTTER ask(target=property_question_3)
    UTTER ask(target=property_question_4)
    UTTER ask(target=property_question_5)
    UTTER ask(target=property_question_6)
  }
  TURN t3 SPEAKER=USER {
    TERM activity(location=country::IT, verb="travel") -> activity_3 : TERM
    TERM subject(kind="destination", location=country::IT, qualifier="Rome") -> subject_2 : TERM
    TERM time_point(date="early July") -> time_point_2 : TERM
    TERM requirement(property="companions", value="parents") -> requirement_2 : TERM
    TERM requirement(property="style", value="adventure") -> requirement_3 : TERM
    TERM measure(amount=5000, unit=currency::USD) -> measure_2 : TERM
    TERM requirement(property="budget_per_person", value=measure_2) -> requirement_4 : TERM
    TERM duration(amount=2, unit=unit_week) -> duration_2 : TERM
    TERM at_most(measure=duration_2) -> at_most_2 : TERM
    TERM requirement(property="duration", value=at_most_2) -> requirement_5 : TERM
    UTTER respond(target=activity_3)
  }
  TURN t4 SPEAKER=AGENT {
    TERM duration(amount=14, unit=unit_day) -> duration_3 : TERM
    TERM group_size(count=3, group=role_adults) -> group_size_2 : TERM
    TERM subject(kind="itinerary", location=country::IT, qualifier="Rome and Tuscany") -> subject_3 : TERM
    CLAIM recommended(target=subject_3) BY role_agent STATUS inferred SOURCE "t4:s1" -> recommended_2 : CLAIM
    UTTER propose(target=subject_3)
    TERM subject(kind="destination", location=country::IT, qualifier="Tuscany") -> subject_4 : TERM
    TERM subject(kind="destination", location=country::IT, qualifier="Amalfi Coast") -> subject_5 : TERM
    CLAIM recommended(target=subject_4) BY role_agent STATUS inferred SOURCE "t4:s14" -> recommended_3 : CLAIM
    CLAIM attribute_claim(property="climate", subject=subject_5, value=state_warm) BY role_agent STATUS asserted SOURCE "t4:s15" -> attribute_claim_2 : CLAIM
    CLAIM comfortable(person=group_size_2, value=TRUE) BY role_agent STATUS asserted SOURCE "t4:s16" -> comfortable_2 : CLAIM
    LINK supports(conclusion=recommended_3, premise=comfortable_2) SOURCE "t4:s16"
    TERM activity(instrument=object_label::ebike, location="Rome", verb="tour") -> activity_4 : TERM
    TERM activity(location="Tiber River", verb="kayak") -> activity_5 : TERM
    TERM activity(location="Rome", object="catacombs", verb="tour") -> activity_6 : TERM
    CLAIM recommended(target=activity_4) BY role_agent STATUS asserted SOURCE "t4:s21" -> recommended_4 : CLAIM
    CLAIM recommended(target=activity_5) BY role_agent STATUS asserted SOURCE "t4:s22" -> recommended_5 : CLAIM
    CLAIM recommended(target=activity_6) BY role_agent STATUS asserted SOURCE "t4:s23" -> recommended_6 : CLAIM
    TERM activity(instrument=object_label::balloon, location="Tuscany", verb="ride") -> activity_7 : TERM
    TERM activity(instrument=object_label::atv, location="Tuscany", verb="tour") -> activity_8 : TERM
    TERM activity(location="Tuscany", verb="hike") -> activity_9 : TERM
    TERM activity(location="Tuscany", object=food_label::truffle, verb="hunt") -> activity_10 : TERM
    TERM activity(location="Tuscany", verb="cook") -> activity_11 : TERM
    CLAIM recommended(target=activity_7) BY role_agent STATUS asserted SOURCE "t4:s29" -> recommended_7 : CLAIM
    CLAIM recommended(target=activity_8) BY role_agent STATUS asserted SOURCE "t4:s30" -> recommended_8 : CLAIM
    CLAIM recommended(target=activity_9) BY role_agent STATUS asserted SOURCE "t4:s31" -> recommended_9 : CLAIM
    CLAIM recommended(target=activity_10) BY role_agent STATUS asserted SOURCE "t4:s32" -> recommended_10 : CLAIM
    TERM measure(amount=3900, unit=currency::USD) -> measure_3 : TERM
    CLAIM provides(actor=role_agent, subject=measure_3) BY role_agent STATUS asserted SOURCE "t4:s44" -> provides_2 : CLAIM
    TERM subject(kind="lodging", location="Rome", qualifier="Hotel Santa Maria") -> subject_6 : TERM
    TERM subject(kind="lodging", location="Rome", qualifier="The Hoxton Rome") -> subject_7 : TERM
    TERM subject(kind="lodging", location="Tuscany", qualifier="Agriturismo Il Cicalino") -> subject_8 : TERM
    CLAIM recommended(target=subject_6) BY role_agent STATUS asserted SOURCE "t4:s49" -> recommended_11 : CLAIM
    CLAIM recommended(target=subject_7) BY role_agent STATUS asserted SOURCE "t4:s51" -> recommended_12 : CLAIM
    CLAIM recommended(target=subject_8) BY role_agent STATUS asserted SOURCE "t4:s53" -> recommended_13 : CLAIM
    TERM activity(object="dates", verb="finalize") -> activity_12 : TERM
    TERM activity(object="activities", verb="customize") -> activity_13 : TERM
    TERM activity(location=country::IT, object="Amalfi Coast", verb="travel") -> activity_14 : TERM
    UTTER offer(target=activity_12)
    UTTER offer(target=activity_13)
    UTTER offer(target=activity_14)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | activity, art_itinerary, propose | covered |
| n2 | speech_act | property_question, ask | covered |
| n3 | action | activity, subject | covered |
| n4 | object | country::IT | covered |
| n5 | temporal | time_point | covered |
| n6 | object | requirement | covered |
| n7 | constraint | requirement | covered |
| n8 | constraint | measure, currency::USD, requirement | covered |
| n9 | temporal | duration, unit_week, at_most, requirement | covered |
| n10 | speech_act | duration, unit_day, group_size, role_adults, subject, recommended, propose | covered |
| n11 | reasoning | subject, recommended, attribute_claim, state_warm, comfortable, supports | covered |
| n12 | action | activity, object_label::ebike, recommended | covered |
| n13 | action | activity, object_label::balloon, object_label::atv, food_label::truffle, recommended | covered |
| n14 | claim | measure, currency::USD, provides | covered |
| n15 | action | subject, recommended | covered |
| n16 | speech_act | activity, offer | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t4:s63 is represented
- Opaque-text spans: none
- Label-preserved spans: object_label::ebike, object_label::balloon, object_label::atv, food_label::truffle
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
