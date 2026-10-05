Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(verb="plan", actor="user", object="trip") -> plan_trip_2 : TERM
  }
  TURN t2 SPEAKER=AGENT {
    UTTER ask(target="First, tell me a bit more so I can help you properly:")
    UTTER ask(target="Where do you want to go?")
    UTTER ask(target="When are you thinking of traveling?")
    UTTER ask(target="How many people?")
    UTTER ask(target="What's your vibe?")
    UTTER ask(target="What's your rough budget?")
  }
  TURN t3 SPEAKER=USER {
    TERM activity(verb="travel", actor="user", location=country::IT) -> travel_2 : TERM
    TERM time_point(date="early July this year") -> time_point_2 : TERM
    TERM group_size(count=3, group=role_adults) -> group_size_2 : TERM
    TERM requirement(property="vibe", value="adventure") -> requirement_2 : TERM
    TERM requirement(property="budget_per_person", value=measure(amount=5000, unit=currency::USD)) -> requirement_3 : TERM
    TERM requirement(property="max_duration_weeks", value=2) -> requirement_4 : TERM
  }
  TURN t4 SPEAKER=AGENT {
    TERM itinerary_summary(duration=duration(amount=2, unit=unit_week),
                           regions=[country::IT, country::IT],
                           group=group_size_2,
                           budget=measure(amount=5000, unit=currency::USD),
                           style="adventure") -> itinerary_summary_2 : TERM  # PROPOSED: S1
    UTTER propose(target=itinerary_summary_2)                                                  # PROPOSED: S1
  }
}
```

## Needs coverage

| need | kind        | expressed by                            | status    |
|------|-------------|-----------------------------------------|-----------|
| n1   | action      | activity(verb="plan",…)                 | covered   |
| n2   | speech_act  | ask                                     | covered   |
| n3   | action      | activity(verb="travel",…)               | covered   |
| n4   | object      | country::IT                             | covered   |
| n5   | temporal    | time_point                              | covered   |
| n6   | object      | group_size                              | covered   |
| n7   | constraint  | requirement(property="vibe",…)          | covered   |
| n8   | constraint  | requirement(property="budget_per_person",…) | covered |
| n9   | temporal    | requirement(property="max_duration_weeks",…) | covered |
| n10  | speech_act  | propose(target=itinerary_summary_2)     | proposed  |
| n11  | reasoning   | —                                       | unresolved|
| n12  | action      | —                                       | unresolved|
| n13  | action      | —                                       | unresolved|
| n14  | claim       | —                                       | unresolved|
| n15  | action      | —                                       | unresolved|
| n16  | speech_act  | —                                       | unresolved|

## Why the translation failed

- n10 “Propose a 14-day adventure itinerary combining Rome and Tuscany for three adults within budget”: no existing TERM constructor can bundle duration, regions, group, budget and style into one structured concept for UTTER propose(target=…).
- n11–n16 reasoning links and detailed steps require additional constructors or composites.

## Translation report

- Input kind: conversation  
- Coverage status: partial  
- Source-span coverage: t1:s1; t2:s2–t2:s13; t3:s1–t3:s2  
- Opaque-text spans: none  
- Label-preserved spans: none  
- Missing constructs: S1 itinerary_summary constructor  
- Unresolved ambiguities: none  
- Check: `rag check` reported 7 unresolved needs (n10–n16), 1 unknown symbol (itinerary_summary)
