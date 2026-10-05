Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    UTTER content="Find a one-way nonstop flight between San Fransisco to San Diego on July 1, on United Airlines for 2 adults and 1 senior, and view the deal of the morning flight."
  }
  TURN t2 SPEAKER=AGENT {
    RECORD ACTION click(target=web_element(label="circle")) STATUS succeeded SOURCE "t2:s2" -> click_event_1 : EVENT
    RECORD ACTION click(target=web_element(label="Flights")) STATUS succeeded SOURCE "t2:s4" -> click_event_2 : EVENT
    RECORD ACTION click(target=web_element(label="One-way")) STATUS succeeded SOURCE "t2:s6" -> click_event_3 : EVENT
    RECORD ACTION type_text(target=web_element(label="City or Airport"), text="SAN FRANSISCO") STATUS succeeded SOURCE "t2:s8" -> type_text_event_4 : EVENT
    RECORD ACTION click(target=web_element(label="San Francisco, CA")) STATUS succeeded SOURCE "t2:s10" -> click_event_5 : EVENT
    RECORD ACTION type_text(target=web_element(label="City or Airport"), text="SAN DIEGO") STATUS succeeded SOURCE "t2:s12" -> type_text_event_6 : EVENT
    RECORD ACTION click(target=web_element(label="San Diego, CA")) STATUS succeeded SOURCE "t2:s14" -> click_event_7 : EVENT
    RECORD ACTION click(target=web_element(label="Thu, 6/15")) STATUS succeeded SOURCE "t2:s16" -> click_event_8 : EVENT
    RECORD ACTION click(target=web_element(label="Sat Jul 01 2023")) STATUS succeeded SOURCE "t2:s18" -> click_event_9 : EVENT
    RECORD ACTION click(target=web_element(label="Travelers 1,Economy")) STATUS succeeded SOURCE "t2:s20" -> click_event_10 : EVENT
    RECORD ACTION click(target=web_element(label="svg")) STATUS succeeded SOURCE "t2:s22" -> click_event_11 : EVENT
    RECORD ACTION click(target=web_element(label="svg")) STATUS succeeded SOURCE "t2:s24" -> click_event_12 : EVENT
    RECORD ACTION click(target=web_element(label="Close")) STATUS succeeded SOURCE "t2:s26" -> click_event_13 : EVENT
    RECORD ACTION click(target=web_element(label="span")) STATUS succeeded SOURCE "t2:s28" -> click_event_14 : EVENT
    RECORD ACTION click(target=web_element(label="Find flights")) STATUS succeeded SOURCE "t2:s30" -> click_event_15 : EVENT
    RECORD ACTION click(target=web_element(label="Show more")) STATUS succeeded SOURCE "t2:s32" -> click_event_16 : EVENT
    RECORD ACTION click(target=web_element(label="United")) STATUS succeeded SOURCE "t2:s34" -> click_event_17 : EVENT
    RECORD ACTION click(target=web_element(label="Sat 5:00 AM")) STATUS succeeded SOURCE "t2:s36" -> click_event_18 : EVENT
    RECORD ACTION click(target=web_element(label="View Deal")) STATUS succeeded SOURCE "t2:s38" -> click_event_19 : EVENT
    RECORD ACTION click(target=web_element(label="View Deal")) STATUS succeeded SOURCE "t2:s40" -> click_event_20 : EVENT
  }
}
```

## Needs coverage

| need | kind       | expressed by                                                                                             | status          |
|------|------------|----------------------------------------------------------------------------------------------------------|-----------------|
| n1   | action     | user request recorded as UTTER, not executed                                                              | not-applicable  |
| n2   | constraint | request text inside UTTER                                                                                 | not-applicable  |
| n3   | constraint | request text inside UTTER                                                                                 | not-applicable  |
| n4   | object     | request text inside UTTER                                                                                 | label-preserved |
| n5   | object     | request text inside UTTER                                                                                 | label-preserved |
| n6   | temporal   | request text inside UTTER                                                                                 | label-preserved |
| n7   | constraint | request text inside UTTER                                                                                 | label-preserved |
| n8   | constraint | request text inside UTTER                                                                                 | label-preserved |
| n9   | constraint | request text inside UTTER                                                                                 | label-preserved |
| n10  | action     | RECORD ACTION click(...)                                                                                  | covered         |

## Why the translation failed

- n7 “airline United Airlines”: no existing group or glossary entry for airlines; only recorded in UTTER content.

## Translation report

- Input kind: prompt | conversation
- Coverage status: partial
- Source-span coverage: turns t1:s1–t2:s40 recorded
- Opaque-text spans: t1:s1 — UTTER content fallback
- Label-preserved spans:
  - n4–n9: city names, date, passenger counts, airline recorded in UTTER content
- Missing constructs: lexical group airline_label
- Unresolved ambiguities: none
- Check: 1 unknown symbol (none used), label-preserved needs indicated
