Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(verb="plan", object="trip") -> activity_2 : TERM
    UTTER ask(target=activity_2)
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    UTTER ask(topic="destination")
    UTTER ask(topic="travel_dates")
    UTTER ask(topic="party_size")
    UTTER ask(topic="travel_style")
    UTTER ask(topic="budget_per_person")
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    TERM activity(verb="travel", location=country::IT) -> activity_2 : TERM
    TERM subject(kind="destination_city", location="Rome") -> subject_2 : TERM
    TERM time_point(date="early July of the current year") -> time_point_2 : TERM
    TERM requirement(property="travel_companions", value="parents") -> requirement_2 : TERM
    TERM requirement(property="travel_style", value="adventure") -> requirement_3 : TERM
    TERM measure(amount=5000, unit=currency::USD) -> measure_2 : TERM
    TERM requirement(property="estimated_budget_per_person", value=measure_2) -> requirement_4 : TERM
    TERM measure(amount=2, unit=unit_week) -> measure_3 : TERM
    TERM at_most(measure=measure_3) -> at_most_2 : TERM
    TERM requirement(property="stay_duration", value=at_most_2) -> requirement_5 : TERM
    UTTER ask(constraints=[subject_2, time_point_2, requirement_2, requirement_3, requirement_4, requirement_5], target=activity_2)
  }
  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    TERM subject(kind="itinerary", location="Rome") -> subject_2 : TERM
    TERM subject(kind="itinerary", location="Tuscany") -> subject_3 : TERM
    TERM duration(amount=14, unit=unit_day) -> duration_2 : TERM
    TERM group_size(count=3, group=role_adults) -> group_size_2 : TERM
    TERM requirement(property="travel_style", value="adventure") -> requirement_2 : TERM
    TERM measure(amount=5000, unit=currency::USD) -> measure_2 : TERM
    TERM at_most(measure=measure_2) -> at_most_2 : TERM
    TERM requirement(property="budget_per_person", value=at_most_2) -> requirement_3 : TERM
    UTTER propose(constraints=[duration_2, group_size_2, requirement_2, requirement_3], target=subject_2) 
    UTTER propose(constraints=[duration_2, group_size_2, requirement_2, requirement_3], target=subject_3)
    CLAIM recommended(target=subject_3) BY role_agent STATUS asserted SOURCE "t4:s14" -> recommended_2 : CLAIM
    CLAIM attribute_claim(property="july_heat", subject="Amalfi_Coast", value="extremely_hot") BY role_agent STATUS asserted SOURCE "t4:s15" -> attribute_claim_2 : CLAIM
    CLAIM attribute_claim(property="july_crowds", subject="Amalfi_Coast", value="crowded") BY role_agent STATUS asserted SOURCE "t4:s15" -> attribute_claim_3 : CLAIM
    CLAIM attribute_claim(property="expense", subject="Amalfi_Coast", value="expensive") BY role_agent STATUS asserted SOURCE "t4:s15" -> attribute_claim_4 : CLAIM
    CLAIM attribute_claim(property="adventure_suitability_for_parents", subject=subject_3, value=TRUE) BY role_agent STATUS asserted SOURCE "t4:s16" -> attribute_claim_5 : CLAIM
    LINK supports(conclusion=recommended_2, premise=attribute_claim_2) SOURCE "t4:s15"
    LINK supports(conclusion=recommended_2, premise=attribute_claim_3) SOURCE "t4:s15"
    LINK supports(conclusion=recommended_2, premise=attribute_claim_4) SOURCE "t4:s15"
    LINK supports(conclusion=recommended_2, premise=attribute_claim_5) SOURCE "t4:s16"
    TERM activity(verb="ride", object="e-bike", location="Rome") -> activity_2 : TERM
    TERM activity(verb="kayak", location="Tiber") -> activity_3 : TERM
    TERM activity(verb="tour", object="underground_rome") -> activity_4 : TERM
    CLAIM recommended(target=activity_2) BY role_agent STATUS asserted SOURCE "t4:s21" -> recommended_3 : CLAIM
    CLAIM recommended(target=activity_3) BY role_agent STATUS asserted SOURCE "t4:s22" -> recommended_4 : CLAIM
    CLAIM recommended(target=activity_4) BY role_agent STATUS asserted SOURCE "t4:s23" -> recommended_5 : CLAIM
    TERM activity(verb="ride", object="hot_air_balloon", location="Tuscany") -> activity_5 : TERM
    TERM activity(verb="tour", object="atv", location="Tuscany") -> activity_6 : TERM
    TERM activity(verb="hike", location="Chianti") -> activity_7 : TERM
    TERM activity(verb="hunt", object=food_label::truffle, location="Tuscany") -> activity_8 : TERM
    CLAIM recommended(target=activity_5) BY role_agent STATUS asserted SOURCE "t4:s29" -> recommended_6 : CLAIM
    CLAIM recommended(target=activity_6) BY role_agent STATUS asserted SOURCE "t4:s30" -> recommended_7 : CLAIM
    CLAIM recommended(target=activity_7) BY role_agent STATUS asserted SOURCE "t4:s31" -> recommended_8 : CLAIM
    CLAIM recommended(target=activity_8) BY role_agent STATUS asserted SOURCE "t4:s32" -> recommended_9 : CLAIM
    TERM measure(amount=3900, unit=currency::USD) -> measure_3 : TERM
    CLAIM attribute_claim(property="estimated_total_cost_per_person", subject=subject_2, value=measure_3) BY role_agent STATUS asserted SOURCE "t4:s44" -> attribute_claim_6 : CLAIM
    TERM measure(amount=1050, unit=currency::USD) -> measure_4 : TERM
    CLAIM attribute_claim(property="estimated_hotel_cost_per_person", subject=subject_2, value=measure_4) BY role_agent STATUS asserted SOURCE "t4:s40" -> attribute_claim_7 : CLAIM
    TERM measure(amount=850, unit=currency::USD) -> measure_5 : TERM
    CLAIM attribute_claim(property="estimated_food_cost_per_person", subject=subject_2, value=measure_5) BY role_agent STATUS asserted SOURCE "t4:s41" -> attribute_claim_8 : CLAIM
    TERM measure(amount=750, unit=currency::USD) -> measure_6 : TERM
    CLAIM attribute_claim(property="estimated_activities_cost_per_person", subject=subject_2, value=measure_6) BY role_agent STATUS asserted SOURCE "t4:s42" -> attribute_claim_9 : CLAIM
    TERM measure(amount=180, unit=currency::USD) -> measure_7 : TERM
    CLAIM attribute_claim(property="estimated_local_transport_cost_per_person", subject=subject_2, value=measure_7) BY role_agent STATUS asserted SOURCE "t4:s43" -> attribute_claim_10 : CLAIM
    TERM measure(amount=950, unit=currency::USD) -> measure_8 : TERM
    CLAIM attribute_claim(property="estimated_flights_cost_per_person_min", subject=subject_2, value=measure_8) BY role_agent STATUS asserted SOURCE "t4:s39" -> attribute_claim_11 : CLAIM
    TERM measure(amount=1300, unit=currency::USD) -> measure_9 : TERM
    CLAIM attribute_claim(property="estimated_flights_cost_per_person_max", subject=subject_2, value=measure_9) BY role_agent STATUS asserted SOURCE "t4:s39" -> attribute_claim_12 : CLAIM
    CLAIM recommended(target=subject_2) BY role_agent STATUS asserted SOURCE "t4:s49" -> recommended_10 : CLAIM
    CLAIM recommended(target=subject_3) BY role_agent STATUS asserted SOURCE "t4:s53" -> recommended_11 : CLAIM
    TERM activity(verb="finalize", object="dates") -> activity_9 : TERM
    TERM activity(verb="customize", object="activities") -> activity_10 : TERM
    TERM activity(verb="switch", object="destination", location="Amalfi_Coast") -> activity_11 : TERM
    UTTER offer(target=activity_9)
    UTTER offer(target=activity_10)
    UTTER offer(target=activity_11)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | activity, ask | covered |
| n2 | speech_act | ask | covered |
| n3 | action | activity, country::IT, subject | covered |
| n4 | object | country::IT | covered |
| n5 | temporal | time_point | covered |
| n6 | object | requirement | covered |
| n7 | constraint | requirement | covered |
| n8 | constraint | requirement, measure, currency::USD | covered |
| n9 | temporal | at_most, measure, unit_week, requirement | covered |
| n10 | speech_act | propose, duration, unit_day, group_size, role_adults, at_most | covered |
| n11 | reasoning | recommended, attribute_claim, supports | covered |
| n12 | action | activity, recommended | covered |
| n13 | action | activity, recommended, food_label::truffle | covered |
| n14 | claim | attribute_claim, measure | covered |
| n15 | action | recommended | covered |
| n16 | speech_act | offer, activity | covered |

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: t1–t4 key content represented; formatting/greeting (t2:s1, s14–s20), itinerary day lists (t4:s11–s13, s19, s25–s27, s33–s34), best-fit hotel/other details omitted or approximated.
- Opaque-text spans: none (short string labels used as topic/property/value atoms, not sentences)
- Label-preserved spans: t4:s32 "truffle" → food_label::truffle
- Missing constructs: no travel-destination/party/date request relation; "wants" speech act for user statements approximated by ask(constraints); Rome/Tuscany/Amalfi as city/region names are string literals (no group); ranges and agent-dated July 3–17 not encoded; "approximately" qualifier on 3900 not encoded; hotel names not encoded (recommendation targets only the itinerary subjects).
- Unresolved ambiguities: t3 "Rome in Italy" encoded as travel activity with country::IT plus Rome subject; user's request speech act is approximated.
- Check: see host check
