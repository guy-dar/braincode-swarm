Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(object=object_label::jobs, verb="browse") -> activity_2 : TERM
    TERM activity(object=object_label::jobs, verb="filter") -> activity_3 : TERM
    TERM requirement(property="certificate", value="security_clearance") -> requirement_2 : TERM
    TERM conjunction(items=[activity_2, activity_3, requirement_2]) -> conjunction_2 : TERM
    CLAIM request(target=conjunction_2) BY role_user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM web_element(label="Search by job title, skill or company", tag="searchbox") -> web_element_2 : TERM
    RECORD ACTION type_text(target=web_element_2, text="IT jobs") STATUS attempted SOURCE "t2:s2" -> type_text_event : EVENT
    TERM web_element(label="Search", tag="button") -> web_element_3 : TERM
    RECORD ACTION click(target=web_element_3) STATUS attempted SOURCE "t2:s4" -> click_event : EVENT
    TERM web_element(label="Filters", tag="link") -> web_element_4 : TERM
    RECORD ACTION click(target=web_element_4) STATUS attempted SOURCE "t2:s6" -> click_event_2 : EVENT
    TERM web_element(label="Certificates", tag="link") -> web_element_5 : TERM
    RECORD ACTION click(target=web_element_5) STATUS attempted SOURCE "t2:s8" -> click_event_3 : EVENT
    TERM web_element(label="Security clearance", tag="link") -> web_element_6 : TERM
    RECORD ACTION click(target=web_element_6) STATUS attempted SOURCE "t2:s10" -> click_event_4 : EVENT
    TERM web_element(label="Display Results", tag="span") -> web_element_7 : TERM
    RECORD ACTION click(target=web_element_7) STATUS attempted SOURCE "t2:s12" -> click_event_5 : EVENT
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | request, conjunction | covered |
| n2 | action | activity | covered |
| n3 | object | object_label::jobs | label-preserved |
| n4 | action | activity | covered |
| n5 | constraint | requirement | covered |
| n6 | action | type_text | covered |
| n7 | object | web_element | covered |
| n8 | object | type_text | covered |
| n9 | action | click | covered |
| n10 | object | web_element | covered |
| n11 | action | click | covered |
| n12 | object | web_element | covered |
| n13 | action | click | covered |
| n14 | object | web_element | covered |
| n15 | action | click | covered |
| n16 | object | web_element | covered |
| n17 | action | click | covered |
| n18 | object | web_element | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: t1:s1 and t2:s2–t2:s12 represented; t2:s1,s3,s5,s7,s9,s11 are step numbers, not-applicable
- Opaque-text spans: none
- Label-preserved spans: t1:s1 "IT jobs" → object_label::jobs (label only; "IT" qualifier lost, noted as gap)
- Missing constructs: none
- Unresolved ambiguities: outcomes of the agent's steps are not given, so status=attempted; "security clearance" kept as string value of requirement
- Check: rag check reported no unknown symbols; "IT" qualifier is not carried by the label
