Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="trip") -> trip_subject : TERM
    UTTER ask(target=trip_subject)
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM subject(kind="destination") -> destination_subject : TERM
    UTTER ask(target=destination_subject)
    TERM subject(kind="travel_dates") -> dates_subject : TERM
    UTTER ask(target=dates_subject)
    TERM group_size(count=1) -> group_size_2 : TERM
    UTTER ask(target=group_size_2)
    TERM subject(kind="travel_style", qualifier="vibe") -> style_subject : TERM
    UTTER ask(target=style_subject)
    TERM measure(amount=1, unit="budget") -> budget_subject : TERM
    UTTER ask(target=budget_subject)
  }
  TURN t3 SPEAKER=USER REPLY_TO t2 {
    CLAIM subject(kind="trip_location", location=country::IT) BY role_user STATUS asserted SOURCE "t3:s1" -> trip_location : CLAIM
    TERM time_point(date="early July") -> departure_time : TERM
    CLAIM subject(kind="trip_timing", time="early July") BY role_user STATUS asserted SOURCE "t3:s1" -> trip_timing : CLAIM
    CLAIM subject(kind="travel_companions", qualifier=role_adults) BY role_user STATUS asserted SOURCE "t3:s1" -> travel_companions : CLAIM
    CLAIM subject(kind="travel_style", qualifier="adventure") BY role_user STATUS asserted SOURCE "t3:s1" -> adventure_style : CLAIM
    TERM measure(amount=5000, unit=currency::USD) -> budget_amount : TERM
    CLAIM subject(kind="budget_per_person", qualifier=role_adults) BY role_user STATUS asserted SOURCE "t3:s2" -> user_budget : CLAIM
    TERM duration(amount=2, unit=unit_week) -> max_duration : TERM
    CLAIM subject(kind="maximum_duration") BY role_user STATUS asserted SOURCE "t3:s2" -> max_stay : CLAIM
  }
  TURN t4 SPEAKER=AGENT REPLY_TO t3 {
    TERM activity(verb="travel", location=country::IT, purpose=activity(verb="adventure")) -> italy_adventure : TERM
    TERM duration(amount=14, unit=unit_day) -> itinerary_duration : TERM
    TERM group_size(count=3, group=role_adults) -> group_of_adults : TERM
    TERM measure(amount=5000, unit=currency::USD) -> budget_per_person : TERM
    UTTER propose(target=italy_adventure)
    TERM subject(kind="destination", location="Tuscany") -> tuscany_subject : TERM
    TERM subject(kind="destination", location="Amalfi Coast") -> amalfi_subject : TERM
    CLAIM recommended(target=tuscany_subject) BY role_agent STATUS asserted SOURCE "t4:s16" -> tuscany_recommended : CLAIM
    CLAIM subject(kind="July weather", qualifier="extremely hot") BY role_agent STATUS asserted SOURCE "t4:s15" -> amalfi_heat : CLAIM
    CLAIM subject(kind="crowding level", qualifier="crowded") BY role_agent STATUS asserted SOURCE "t4:s15" -> amalfi_crowds : CLAIM
    CLAIM subject(kind="price level", qualifier="expensive") BY role_agent STATUS asserted SOURCE "t4:s15" -> amalfi_expense : CLAIM
    LINK rejects(evidence=amalfi_heat, hypothesis=amalfi_subject) SOURCE "t4:s15"
    LINK rejects(evidence=amalfi_crowds, hypothesis=amalfi_subject) SOURCE "t4:s15"
    LINK rejects(evidence=amalfi_expense, hypothesis=amalfi_subject) SOURCE "t4:s15"
    LINK supports(premise=tuscany_recommended, conclusion=italy_adventure) SOURCE "t4:s16"
    TERM activity(verb="e-bike", location=country::IT, object="Appian Way") -> rome_ebike : TERM
    TERM activity(verb="kayak", location=country::IT, object="Tiber River") -> rome_kayak : TERM
    TERM activity(verb="tour", location=country::IT, object="catacombs") -> rome_catacombs : TERM
    TERM activity(verb="tour", location=country::IT, object="Colosseum") -> rome_colosseum : TERM
    TERM activity(verb="hike", location=country::IT, object="Tivoli") -> rome_tivoli : TERM
    TERM activity(verb="aperitivo", location=country::IT, object="rooftop") -> rome_aperitivo : TERM
    UTTER propose(target=rome_ebike)
    UTTER propose(target=rome_kayak)
    UTTER propose(target=rome_catacombs)
    UTTER propose(target=rome_colosseum)
    UTTER propose(target=rome_tivoli)
    UTTER propose(target=rome_aperitivo)
    TERM activity(verb="hot air balloon", location="Tuscany") -> tuscany_balloon : TERM
    TERM activity(verb="ATV tour", location="Tuscany", object="vineyards") -> tuscany_atv : TERM
    TERM activity(verb="hike", location="Tuscany", object="Chianti hills") -> tuscany_hike : TERM
    TERM activity(verb="truffle hunt", location="Tuscany") -> tuscany_truffle : TERM
    TERM activity(verb="cooking class", location="Tuscany", object="farmhouse") -> tuscany_cooking : TERM
    UTTER propose(target=tuscany_balloon)
    UTTER propose(target=tuscany_atv)
    UTTER propose(target=tuscany_hike)
    UTTER propose(target=tuscany_truffle)
    UTTER propose(target=tuscany_cooking)
    TERM measure(amount=950, unit=currency::USD) -> flights_cost : TERM
    TERM measure(amount=1050, unit=currency::USD) -> hotels_cost : TERM
    TERM measure(amount=850, unit=currency::USD) -> food_cost : TERM
    TERM measure(amount=750, unit=currency::USD) -> activities_cost : TERM
    TERM measure(amount=180, unit=currency::USD) -> transport_cost : TERM
    TERM measure(amount=3900, unit=currency::USD) -> total_per_person : TERM
    CLAIM provides(actor="proposed itinerary", subject="cost breakdown") BY role_agent STATUS asserted SOURCE "t4:s36" -> cost_estimate : CLAIM
    UTTER inform(target=cost_estimate)
    TERM subject(kind="accommodation", location="Rome", qualifier="Trastevere") -> rome_hotel_1 : TERM
    TERM subject(kind="accommodation", location="Rome", qualifier="Monti") -> rome_hotel_2 : TERM
    TERM subject(kind="accommodation", location="Tuscany", qualifier="Chianti countryside") -> tuscany_agriturismo : TERM
    CLAIM recommended(target=rome_hotel_1) BY role_agent STATUS asserted SOURCE "t4:s48" -> recommend_rome_hotel_1 : CLAIM
    CLAIM recommended(target=tuscany_agriturismo) BY role_agent STATUS asserted SOURCE "t4:s52" -> recommend_tuscany_agriturismo : CLAIM
    UTTER propose(target=rome_hotel_1)
    UTTER propose(target=tuscany_agriturismo)
    TERM activity(verb="finalize dates") -> finalize_dates_option : TERM
    TERM activity(verb="customize activities") -> customize_option : TERM
    TERM activity(verb="switch destination", object="Amalfi Coast") -> amalfi_option : TERM
    UTTER offer(target=finalize_dates_option)
    UTTER offer(target=customize_option)
    UTTER offer(target=amalfi_option)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | propose, activity | covered |
| n2 | speech_act | ask, group_size, propose, offer | covered |
| n3 | action | activity | covered |
| n4 | object | country | covered |
| n5 | temporal | time_point, duration, unit_week, unit_day | covered |
| n6 | object | role_adults | covered |
| n7 | constraint | activity | covered |
| n8 | constraint | currency, measure | covered |
| n9 | temporal | duration, unit_week, unit_day | covered |
| n10 | speech_act | propose, activity, group_size, unit_day, ask | covered |
| n11 | reasoning | recommended, rejects, supports, activity | covered |
| n12 | action | activity | covered |
| n13 | action | activity | covered |
| n14 | claim | provides, measure | covered |
| n15 | action | recommended, subject | covered |
| n16 | speech_act | offer, activity, propose | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t4:s63 is represented
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported no unresolved needs and no unknown symbols
