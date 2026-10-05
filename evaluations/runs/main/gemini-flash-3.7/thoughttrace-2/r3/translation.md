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
    TERM requirement(property="destination", value="unspecified") -> requirement_2 : TERM
    UTTER ask(target=requirement_2)
    TERM requirement(property="travel_dates", value="unspecified") -> requirement_3 : TERM
    UTTER ask(target=requirement_3)
    TERM group_size(count=0) -> group_size_2 : TERM
    UTTER ask(target=group_size_2)
    TERM requirement(property="travel_style", value="unspecified") -> requirement_4 : TERM
    UTTER ask(target=requirement_4)
    TERM requirement(property="budget", value="unspecified") -> requirement_5 : TERM
    UTTER ask(target=requirement_5)
  }
  TURN t3 SPEAKER=USER {
    TERM time_point(date="early July", timezone="current_year") -> time_point_2 : TERM
    TERM activity(location=country::IT, object="Rome", purpose=time_point_2, verb="travel") -> activity_3 : TERM
    TERM group_size(count=3, group=role_adults) -> group_size_3 : TERM
    TERM requirement(property="companions", value=role_adults) -> requirement_6 : TERM
    TERM requirement(property="travel_style", value="adventure") -> requirement_7 : TERM
    TERM measure(amount=5000, unit=currency::USD) -> measure_2 : TERM
    TERM rate(denominator=role_adults, numerator=measure_2) -> rate_2 : TERM
    TERM requirement(property="budget_per_person", value=rate_2) -> requirement_8 : TERM
    TERM duration(amount=2, unit=unit_week) -> duration_2 : TERM
    TERM at_most(measure=duration_2) -> at_most_2 : TERM
    TERM requirement(property="duration", value=at_most_2) -> requirement_9 : TERM
    UTTER respond(target=activity_3)
  }
  TURN t4 SPEAKER=AGENT {
    TERM duration(amount=14, unit=unit_day) -> duration_3 : TERM
    TERM group_size(count=3, group=role_adults) -> group_size_4 : TERM
    TERM requirement(property="destination", value="Rome and Tuscany") -> requirement_10 : TERM
    TERM activity(object=art_itinerary, purpose=requirement_10, verb="itinerary") -> activity_4 : TERM
    UTTER propose(target=activity_4)
    TERM activity(location=country::IT, object="Tuscany", verb="visit") -> activity_5 : TERM
    CLAIM recommended(target=activity_5) BY role_agent STATUS inferred SOURCE "t4:s14" -> recommended_2 : CLAIM
    TERM activity(location=country::IT, object="Amalfi", verb="visit") -> activity_6 : TERM
    CLAIM recommended(target=activity_6) BY role_agent STATUS inferred SOURCE "t4:s15" -> recommended_3 : CLAIM
    LINK rejects(evidence=recommended_2, hypothesis=recommended_3) SOURCE "t4:s14"
    TERM requirement(property="comfort_for_parents", value=role_adults) -> requirement_11 : TERM
    CLAIM recommended(target=requirement_11) BY role_agent STATUS asserted SOURCE "t4:s16" -> recommended_4 : CLAIM
    LINK supports(conclusion=recommended_2, premise=recommended_4) SOURCE "t4:s16"
    TERM activity(location=country::IT, object="Rome e-bike tour and Tiber kayaking and underground tours", verb="tour") -> activity_7 : TERM
    UTTER propose(target=activity_7)
    TERM activity(location=country::IT, object="Tuscany hot air balloon and ATV and hiking and truffle hunting", verb="tour") -> activity_8 : TERM
    UTTER propose(target=activity_8)
    TERM measure(amount=3900, unit=currency::USD) -> measure_3 : TERM
    TERM rate(denominator=role_adults, numerator=measure_3) -> rate_3 : TERM
    CLAIM provides(actor=role_agent, subject=rate_3) BY role_agent STATUS asserted SOURCE "t4:s44" -> provides_2 : CLAIM
    TERM activity(location=country::IT, object="Hotel Santa Maria and The Hoxton in Rome, Agriturismo Il Cicalino in Tuscany", verb="stay") -> activity_9 : TERM
    CLAIM recommended(target=activity_9) BY role_agent STATUS asserted SOURCE "t4:s47" -> recommended_5 : CLAIM
    TERM requirement(property="next_steps", value="finalize_dates_or_customize_activities_or_switch_to_amalfi") -> requirement_12 : TERM
    UTTER offer(target=requirement_12)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | activity, art_itinerary, propose | covered |
| n2 | speech_act | ask, requirement, group_size | covered |
| n3 | action | activity | covered |
| n4 | object | country::IT | covered |
| n5 | temporal | time_point | covered |
| n6 | object | role_adults, group_size | covered |
| n7 | constraint | requirement | covered |
| n8 | constraint | requirement, rate, measure, currency::USD | covered |
| n9 | temporal | requirement, at_most, duration, unit_week | covered |
| n10 | speech_act | propose, activity, art_itinerary, duration, unit_day, group_size, role_adults | covered |
| n11 | reasoning | recommended, rejects, supports | covered |
| n12 | action | activity, propose | covered |
| n13 | action | activity, propose | covered |
| n14 | claim | provides, rate, measure, currency::USD | covered |
| n15 | action | recommended, activity | covered |
| n16 | speech_act | offer, requirement | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every turn t1:s1–t4:s63 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
