Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM time_point(date="1980-01-05") -> time_point_2 : TERM
    TERM requirement(property="birthday", value=time_point_2) -> requirement_2 : TERM
    TERM lexical_label(value=food_label::dairy) -> lexical_label_2 : TERM
    TERM medical_condition(condition="allergy", patient=role_user) -> medical_condition_2 : TERM
    TERM requirement(property="allergy", value=lexical_label_2) -> requirement_3 : TERM
    TERM lexical_label(value=food_label::peanut) -> lexical_label_3 : TERM
    TERM requirement(property="allergy", value=lexical_label_3) -> requirement_4 : TERM
    TERM lexical_label(value=food_label::ramen) -> lexical_label_4 : TERM
    TERM requirement(property="bio", value=lexical_label_4) -> requirement_5 : TERM
    CLAIM user_preference(constraints=requirement_2) BY role_user STATUS asserted SOURCE "t1:s1" -> user_preference_2 : CLAIM
    CLAIM user_preference(constraints=requirement_3) BY role_user STATUS asserted SOURCE "t1:s1" -> user_preference_3 : CLAIM
    CLAIM user_preference(constraints=requirement_4) BY role_user STATUS asserted SOURCE "t1:s1" -> user_preference_4 : CLAIM
    CLAIM user_preference(constraints=requirement_5) BY role_user STATUS asserted SOURCE "t1:s1" -> user_preference_5 : CLAIM
    CLAIM request(target="save") BY role_user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT {
    TERM web_element(label="Profile menu", tag="generic") -> web_element_2 : TERM
    RECORD ACTION click(target=web_element_2) STATUS succeeded SOURCE "t2:s2" -> click_event : EVENT
    TERM web_element(label="Profile", tag="link") -> web_element_3 : TERM
    RECORD ACTION click(target=web_element_3) STATUS succeeded SOURCE "t2:s4" -> click_event_2 : EVENT
    TERM web_element(label="BIRTHDAY Month", tag="combobox") -> web_element_4 : TERM
    RECORD ACTION select_option(target=web_element_4, value="January") STATUS succeeded SOURCE "t2:s6" -> select_option_event : EVENT
    TERM web_element(label="Day", tag="combobox") -> web_element_5 : TERM
    RECORD ACTION select_option(target=web_element_5, value="05") STATUS succeeded SOURCE "t2:s8" -> select_option_event_2 : EVENT
    TERM web_element(label="Year", tag="combobox") -> web_element_6 : TERM
    RECORD ACTION select_option(target=web_element_6, value="1980") STATUS succeeded SOURCE "t2:s10" -> select_option_event_3 : EVENT
    TERM web_element(label="SHORT BIO", tag="textbox") -> web_element_7 : TERM
    RECORD ACTION type_text(target=web_element_7, text="Love Ramen Noodles") STATUS succeeded SOURCE "t2:s12" -> type_text_event : EVENT
    TERM web_element(label="All Dairy", tag="checkbox") -> web_element_8 : TERM
    RECORD ACTION click(target=web_element_8) STATUS succeeded SOURCE "t2:s14" -> click_event_3 : EVENT
    TERM web_element(label="Peanuts", tag="checkbox") -> web_element_9 : TERM
    RECORD ACTION click(target=web_element_9) STATUS succeeded SOURCE "t2:s16" -> click_event_4 : EVENT
    TERM web_element(label="Save", tag="button") -> web_element_10 : TERM
    RECORD ACTION click(target=web_element_10) STATUS succeeded SOURCE "t2:s18" -> click_event_5 : EVENT
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | user_preference, requirement | covered |
| n2 | temporal | time_point | covered |
| n3 | action | medical_condition, user_preference | covered |
| n4 | object | food_label::dairy, lexical_label | label-preserved |
| n5 | object | food_label::peanut, lexical_label | label-preserved |
| n6 | action | user_preference, requirement | covered |
| n7 | constraint | food_label::ramen, lexical_label | label-preserved |
| n8 | action | request | covered |
| n9 | action | click, web_element | covered |
| n10 | action | click, web_element | covered |
| n11 | action | select_option, web_element | covered |
| n12 | action | select_option, web_element | covered |
| n13 | action | select_option, web_element | covered |
| n14 | action | type_text, web_element | covered |
| n15 | action | click, web_element | covered |
| n16 | action | click, web_element | covered |
| n17 | action | click, web_element | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t2:s18 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s1 "dairy" → food_label::dairy, t1:s1 "peanut" → food_label::peanut, t1:s1 "ramen" → food_label::ramen
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
