Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(verb="travel") -> activity_2 : TERM
    TERM activity(purpose=activity_2, verb="plan") -> activity_3 : TERM
    UTTER propose(target=activity_3)
  }
  TURN t2 SPEAKER=AGENT {
    TERM property_question(property="destination", subject="trip") -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
    TERM property_question(property="dates", subject="trip") -> property_question_3 : TERM
    UTTER ask(target=property_question_3)
    TERM property_question(property="group_size", subject="trip") -> property_question_4 : TERM
    UTTER ask(target=property_question_4)
    TERM property_question(property="style", subject="trip") -> property_question_5 : TERM
    UTTER ask(target=property_question_5)
    TERM property_question(property="budget", subject="trip") -> property_question_6 : TERM
    UTTER ask(target=property_question_6)
  }
  TURN t3 SPEAKER=USER {
    TERM location_spec(city="Rome") -> location_spec_2 : TERM
    TERM activity(location=country::IT, verb="travel") -> activity_4 : TERM
    TERM time_point(date="early July this year") -> time_point_2 : TERM
    TERM requirement(property="dates", value=time_point_2) -> requirement_2 : TERM
    TERM requirement(property="companions", value=role_mother) -> requirement_3 : TERM
    TERM requirement(property="vibe", value="adventure") -> requirement_4 : TERM
    TERM measure(amount=5000, unit=currency::USD) -> measure_2 : TERM
    TERM subject(kind="person") -> subject_2 : TERM
    TERM rate(denominator=subject_2, numerator=measure_2) -> rate_2 : TERM
    TERM at_most(measure=rate_2) -> at_most_2 : TERM
    TERM requirement(property="budget", value=at_most_2) -> requirement_5 : TERM
    TERM duration(amount=2, unit=unit_week) -> duration_2 : TERM
    TERM at_most(measure=duration_2) -> at_most_3 : TERM
    TERM requirement(property="duration", value=at_most_3) -> requirement_6 : TERM
    UTTER respond(target=activity_4)
  }
  TURN t4 SPEAKER=AGENT {
    TERM duration(amount=14, unit=unit_day) -> duration_3 : TERM
    TERM group_size(count=3, group=role_adults) -> group_size_2 : TERM
    TERM subject(kind="itinerary", location=country::IT, qualifier="Rome and Tuscany") -> subject_3 : TERM
    CLAIM recommended(target=subject_3) BY agent STATUS asserted SOURCE "t4:s1" -> recommended_2 : CLAIM
    UTTER propose(target=subject_3)
    TERM activity(location="Tuscany", verb="travel") -> activity_5 : TERM
    CLAIM recommended(target=activity_5) BY agent STATUS inferred SOURCE "t4:s16" -> recommended_3 : CLAIM
    TERM activity(location="Amalfi Coast", verb="travel") -> activity_6 : TERM
    CLAIM recommended(target=activity_6) BY agent STATUS asserted SOURCE "t4:s14" -> recommended_4 : CLAIM
    CLAIM comfortable(person=group_size_2, value=TRUE) BY agent STATUS inferred SOURCE "t4:s16" -> comfortable_2 : CLAIM
    LINK supports(conclusion=recommended_3, premise=comfortable_2) SOURCE "t4:s16"
    TERM activity(instrument=object_label::ebike, location="Rome", verb="tour") -> activity_7 : TERM
    TERM activity(location="Rome", verb="kayak") -> activity_8 : TERM
    TERM activity(location="Rome", object="catacombs", verb="tour") -> activity_9 : TERM
    UTTER propose(target=activity_7)
    UTTER propose(target=activity_8)
    UTTER propose(target=activity_9)
    TERM activity(instrument=object_label::balloon, location="Tuscany", verb="ride") -> activity_10 : TERM
    TERM activity(instrument=object_label::atv, location="Tuscany", verb="tour") -> activity_11 : TERM
    TERM activity(location="Tuscany", verb="hike") -> activity_12 : TERM
    TERM activity(location="Tuscany", object=food_label::truffle, verb="hunt") -> activity_13 : TERM
    UTTER propose(target=activity_10)
    UTTER propose(target=activity_11)
    UTTER propose(target=activity_12)
    UTTER propose(target=activity_13)
    TERM measure(amount=3900, unit=currency::USD) -> measure_3 : TERM
    TERM rate(denominator=t3.subject_2, numerator=measure_3) -> rate_3 : TERM
    CLAIM provides(actor=role_agent, subject=rate_3) BY agent STATUS asserted SOURCE "t4:s44" -> provides_2 : CLAIM
    TERM subject(kind="accommodation", location="Rome", qualifier="Hotel Santa Maria") -> subject_4 : TERM
    CLAIM recommended(target=subject_4) BY agent STATUS asserted SOURCE "t4:s49" -> recommended_5 : CLAIM
    TERM subject(kind="accommodation", location="Tuscany", qualifier="Agriturismo Il Cicalino") -> subject_5 : TERM
    CLAIM recommended(target=subject_5) BY agent STATUS asserted SOURCE "t4:s53" -> recommended_6 : CLAIM
    TERM activity(object="dates", verb="finalize") -> activity_14 : TERM
    UTTER offer(target=activity_14)
    TERM activity(object="activities", verb="customize") -> activity_15 : TERM
    UTTER offer(target=activity_15)
    TERM activity(location="Amalfi Coast", verb="switch") -> activity_16 : TERM
    UTTER offer(target=activity_16)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | activity, propose | covered |
| n2 | speech_act | ask, property_question | covered |
| n3 | action | activity, location_spec | covered |
| n4 | object | country::IT | covered |
| n5 | temporal | time_point, requirement | covered |
| n6 | object | role_mother, requirement | covered |
| n7 | constraint | requirement | covered |
| n8 | constraint | measure, rate, at_most, requirement, currency::USD | covered |
| n9 | temporal | duration, unit_week, at_most, requirement | covered |
| n10 | speech_act | propose, duration, unit_day, group_size, role_adults, subject, recommended | covered |
| n11 | reasoning | recommended, comfortable, supports, group_size, role_adults | covered |
| n12 | action | activity, object_label::ebike, propose | covered |
| n13 | action | activity, object_label::balloon, object_label::atv, food_label::truffle, propose | covered |
| n14 | claim | measure, rate, currency::USD, provides, role_agent | covered |
| n15 | action | subject, recommended | covered |
| n16 | speech_act | offer, activity | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t4:s63 is represented
- Opaque-text spans: none
- Label-preserved spans: t4:s21 "e-bike" → object_label::ebike, t4:s29 "hot air balloon" → object_label::balloon, t4:s30 "ATV" → object_label::atv, t4:s32 "truffle" → food_label::truffle
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
