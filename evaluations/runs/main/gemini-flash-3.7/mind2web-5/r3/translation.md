Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM time_point(date="1980-01-05") -> time_point_2 : TERM
    TERM activity(actor=role_user, object="birthday", purpose=time_point_2, verb="add") -> activity_2 : TERM
    CLAIM request(target=activity_2) BY role_user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
    TERM lexical_label(value=food_label::dairy) -> lexical_label_2 : TERM
    TERM lexical_label(value=food_label::peanut) -> lexical_label_3 : TERM
    CLAIM user_preference(constraints=lexical_label_2) BY role_user STATUS asserted SOURCE "t1:s1" -> user_preference_2 : CLAIM
    CLAIM user_preference(constraints=lexical_label_3) BY role_user STATUS asserted SOURCE "t1:s1" -> user_preference_3 : CLAIM
    TERM lexical_label(value=food_label::ramen) -> lexical_label_4 : TERM
    TERM activity(actor=role_user, object=food_label::ramen, verb="add_bio") -> activity_3 : TERM
    CLAIM request(target=activity_3) BY role_user STATUS asserted SOURCE "t1:s1" -> request_3 : CLAIM
    TERM activity(actor=role_user, verb="save") -> activity_4 : TERM
    CLAIM request(target=activity_4) BY role_user STATUS asserted SOURCE "t1:s1" -> request_4 : CLAIM
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
| n1 | action | activity, request, user_preference | covered |
| n2 | temporal | time_point | covered |
| n3 | action | user_preference | covered |
| n4 | object | food_label::dairy | label-preserved |
| n5 | object | food_label::peanut | label-preserved |
| n6 | action | activity, lexical_label, request | covered |
| n7 | constraint | food_label::ramen | label-preserved |
| n8 | action | activity, request, role_user, user_preference | covered |
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
- Label-preserved spans: t1:s1 "dairy" → food_label::dairy (food kind label); t1:s1 "peanut" → food_label::peanut (food kind label); t1:s1 "ramen noodles" → food_label::ramen (food kind label)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
