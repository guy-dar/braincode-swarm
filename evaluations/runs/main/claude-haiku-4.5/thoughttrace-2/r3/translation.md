Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    UTTER ask(topic="trip planning")
  }
  
  TURN t2 SPEAKER=AGENT {
    TERM subject(kind="destination") -> q_destination : TERM
    UTTER ask(target=q_destination)
    TERM time_point() -> q_dates : TERM
    UTTER ask(target=q_dates)
    TERM group_size(count=1) -> q_party : TERM
    UTTER ask(target=q_party)
    TERM subject(kind="travel style") -> q_vibe : TERM
    UTTER ask(target=q_vibe)
    TERM measure(amount=1, unit=currency::USD) -> q_budget : TERM
    UTTER ask(target=q_budget)
  }
  
  TURN t3 SPEAKER=USER {
    TERM subject(kind="destination", location=country::IT) -> dest : TERM
    CLAIM subject(kind="destination", location=country::IT) BY role_user STATUS asserted SOURCE "t3:s1" -> destination_claim : CLAIM
    TERM time_point(date="early July") -> travel_dates_term : TERM
    CLAIM time_point(date="early July") BY role_user STATUS asserted SOURCE "t3:s1" -> travel_dates : CLAIM
    TERM group_size(count=3, group=role_adults) -> party_term : TERM
    CLAIM group_size(count=3, group=role_adults) BY role_user STATUS asserted SOURCE "t3:s1" -> group_size_claim : CLAIM
    TERM activity(verb="adventure travel") -> adventure_vibe : TERM
    TERM measure(amount=5000, unit=currency::USD) -> budget_term : TERM
    CLAIM measure(amount=5000, unit=currency::USD) BY role_user STATUS asserted SOURCE "t3:s2" -> budget_claim : CLAIM
    TERM duration(amount=2, unit=unit_week) -> max_duration : TERM
    CLAIM at_most(measure=max_duration) BY role_user STATUS asserted SOURCE "t3:s2" -> duration_constraint : CLAIM
  }
  
  TURN t4 SPEAKER=AGENT {
    TERM subject(kind="itinerary", location=country::IT) -> itinerary_term : TERM
    CLAIM propose_menu(menu=itinerary_term) BY role_agent STATUS asserted SOURCE "t4:s1" -> itinerary_proposal : CLAIM
    
    TERM activity(verb="e-bike tour", location=country::IT) -> rome_activity_1 : TERM
    TERM activity(verb="kayaking", location=country::IT, object=object_label::river) -> rome_activity_2 : TERM
    TERM activity(verb="underground tour", location=country::IT) -> rome_activity_3 : TERM
    TERM activity(verb="hot air balloon", location=country::IT) -> tuscany_activity_1 : TERM
    TERM activity(verb="hiking", location=country::IT) -> tuscany_activity_2 : TERM
    TERM activity(verb="truffle hunting", location=country::IT) -> tuscany_activity_3 : TERM
    
    TERM subject(kind="destination", location="Tuscany") -> tuscany_dest : TERM
    CLAIM recommended(target=tuscany_dest) BY role_agent STATUS asserted SOURCE "t4:s14" -> tuscany_rec : CLAIM
    CLAIM failure(system="Amalfi Coast") BY role_agent STATUS hypothesized SOURCE "t4:s15" -> amalfi_issues : CLAIM
    TERM subject(kind="destination", location="Amalfi") -> amalfi_dest : TERM
    LINK rejects(evidence=amalfi_issues, hypothesis=amalfi_dest) SOURCE "t4:s14"
    LINK supports(conclusion=tuscany_rec, premise=tuscany_dest) SOURCE "t4:s16"
    
    TERM measure(amount=3900, unit=currency::USD) -> cost_measure : TERM
    CLAIM provides(actor=role_agent, subject=cost_measure) BY role_agent STATUS asserted SOURCE "t4:s44" -> cost_estimate : CLAIM
    TERM subject(kind="accommodation", location=country::IT) -> accommodation_term : TERM
    CLAIM recommended(target=accommodation_term) BY role_agent STATUS asserted SOURCE "t4:s47" -> accommodation_rec : CLAIM
    
    TERM subject(kind="next steps") -> next_steps_term : TERM
    UTTER offer(target=next_steps_term)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | propose_menu, subject | covered |
| n2 | speech_act | ask | covered |
| n3 | action | subject constructor (destination claim) | covered |
| n4 | object | country::IT | covered |
| n5 | temporal | time_point | covered |
| n6 | object | group_size, role_adults | covered |
| n7 | constraint | activity(verb="adventure travel") | covered |
| n8 | constraint | measure(amount=5000, unit=currency::USD) | covered |
| n9 | temporal | at_most, duration | covered |
| n10 | speech_act | propose_menu, activity | covered |
| n11 | reasoning | recommended, rejects, supports (links) | covered |
| n12 | action | activity constructors (Rome activities) | covered |
| n13 | action | activity constructors (Tuscany activities) | covered |
| n14 | claim | provides claim with measure | covered |
| n15 | action | recommended claim for accommodations | covered |
| n16 | speech_act | offer | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: All turns (t1–t4) represented with source locators. t1 (trip planning intent), t2 (five clarifying questions encoded as ask/UTTER), t3 (six requirements as CLAIMs with measures and durations), t4 (proposal, activity descriptions, cost estimate, accommodations, reasoning links, and closing offer).
- Opaque-text spans: none (specific activity details and hotel names are accessible via source locator; full itinerary summaries do not require exact wording)
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reports all 16 needs covered, no unknown symbols
```

