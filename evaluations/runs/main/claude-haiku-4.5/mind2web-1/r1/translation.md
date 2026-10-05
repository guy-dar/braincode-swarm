Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM location_spec(city="San Francisco", state="CA") -> departure_location : TERM
    TERM location_spec(city="San Diego", state="CA") -> arrival_location : TERM
    TERM time_point(date="2023-07-01") -> departure_date : TERM
    TERM requirement(property="trip_type", value="one-way") -> oneway_requirement : TERM
    TERM requirement(property="stops", value="nonstop") -> nonstop_requirement : TERM
    TERM group_size(count=2, group="adults") -> adults_constraint : TERM
    TERM group_size(count=1, group="senior") -> senior_constraint : TERM
    TERM requirement(property="airline", value="United Airlines") -> airline_requirement : TERM
    TERM requirement(property="departure_time", value=daytime) -> morning_requirement : TERM
    UTTER ask(target=departure_location)
    UTTER ask(target=arrival_location)
    UTTER ask(target=departure_date)
    UTTER ask(target=oneway_requirement)
    UTTER ask(target=nonstop_requirement)
    UTTER ask(target=adults_constraint)
    UTTER ask(target=senior_constraint)
    UTTER ask(target=airline_requirement)
    UTTER ask(target=morning_requirement)
  }
  TURN t2 SPEAKER=AGENT {
    RECORD ACTION click(target=web_element(label="Flights")) STATUS succeeded SOURCE "t2:s4"
    RECORD ACTION click(target=web_element(label="One-way")) STATUS succeeded SOURCE "t2:s6"
    RECORD ACTION type_text(target=web_element(label="City or Airport", tag="textbox"), text="SAN FRANCISCO") STATUS succeeded SOURCE "t2:s8"
    RECORD ACTION click(target=web_element(label="San Francisco, CA")) STATUS succeeded SOURCE "t2:s10"
    RECORD ACTION type_text(target=web_element(label="City or Airport", tag="textbox"), text="SAN DIEGO") STATUS succeeded SOURCE "t2:s12"
    RECORD ACTION click(target=web_element(label="San Diego, CA")) STATUS succeeded SOURCE "t2:s14"
    RECORD ACTION click(target=web_element(label="Thu, 6/15", tag="div")) STATUS succeeded SOURCE "t2:s16"
    RECORD ACTION click(target=web_element(label="Sat Jul 01 2023", tag="gridcell")) STATUS succeeded SOURCE "t2:s18"
    RECORD ACTION click(target=web_element(label="Travelers 1,Economy")) STATUS succeeded SOURCE "t2:s20"
    RECORD ACTION click(target=web_element(tag="svg")) STATUS succeeded SOURCE "t2:s22"
    RECORD ACTION click(target=web_element(tag="svg")) STATUS succeeded SOURCE "t2:s24"
    RECORD ACTION click(target=web_element(label="Close")) STATUS succeeded SOURCE "t2:s26"
    RECORD ACTION click(target=web_element(tag="span")) STATUS succeeded SOURCE "t2:s28"
    RECORD ACTION search_travel(target="flights", constraints=[t1.oneway_requirement, t1.nonstop_requirement, t1.airline_requirement, t1.morning_requirement], location=country::US) STATUS succeeded SOURCE "t2:s30" -> search_travel_event : EVENT
    RECORD ACTION click(target=web_element(label="Show more")) STATUS succeeded SOURCE "t2:s32"
    RECORD ACTION click(target=web_element(label="United", tag="label")) STATUS succeeded SOURCE "t2:s34"
    RECORD ACTION click(target=web_element(label="Sat 5:00 AM")) STATUS succeeded SOURCE "t2:s36"
    RECORD ACTION click(target=web_element(label="View Deal", tag="button")) STATUS succeeded SOURCE "t2:s38"
    RECORD ACTION click(target=web_element(label="View Deal", tag="button")) STATUS succeeded SOURCE "t2:s40"
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | search_travel | covered |
| n2 | constraint | oneway_requirement | covered |
| n3 | constraint | nonstop_requirement | covered |
| n4 | object | departure_location | covered |
| n5 | object | arrival_location | covered |
| n6 | temporal | departure_date | covered |
| n7 | constraint | airline_requirement | covered |
| n8 | constraint | adults_constraint | covered |
| n9 | constraint | senior_constraint | covered |
| n10 | action | click, web_element | covered |
| n11 | constraint | morning_requirement | covered |
| n12 | action | click | covered |
| n13 | action | click | covered |
| n14 | action | type_text, departure_location | covered |
| n15 | action | type_text | covered |
| n16 | action | click, search_travel | covered |
| n17 | action | click, adults_constraint, senior_constraint | covered |
| n18 | action | search_travel | covered |
| n19 | action | click, airline_requirement | covered |
| n20 | action | click, daytime | covered |
| n21 | action | click | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: all segments t1:s1–t2:s40 are represented with semantic operations and UI-level recordings
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none (see note on flight search vocabulary below)
- Unresolved ambiguities: none
- Check: 17 needs marked [OK], 5 needs marked [DECL], 1 target warning

### Check result notes

The check reports [DECL] for n3, n4, n5, n7, n9 (nonstop flight, cities, airline, senior passenger). These needs ARE fully expressed in the BrainCode as TERM constructors:
- n3: `nonstop_requirement = requirement(property="stops", value="nonstop")`
- n4: `departure_location = location_spec(city="San Francisco", state="CA")`
- n5: `arrival_location = location_spec(city="San Diego", state="CA")`
- n7: `airline_requirement = requirement(property="airline", value="United Airlines")`
- n9: `senior_constraint = group_size(count=1, group="senior")`

The [DECL] status indicates the checker cannot auto-verify these via heuristics, not that they are uncovered. These are domain-specific flight search attributes (stops, airlines, age categories) that the glossary does not have dedicated symbols for; expressing them with generic `requirement`, `location_spec`, and `group_size` constructors is the correct approach per spec §9 (composing from existing constructors).

The target="flights" warning is about passing a STRING literal where the glossary _could_ have an entity; "flights" is an acceptable STRING value per search_travel's signature.
