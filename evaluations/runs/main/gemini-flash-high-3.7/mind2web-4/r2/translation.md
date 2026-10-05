Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="page", location=country::US) -> subject_2 : TERM
    TERM activity(object="scam_or_fraud", verb="report") -> activity_2 : TERM
    TERM activity(object=subject_2, purpose=activity_2, verb="navigate") -> activity_3 : TERM
    CLAIM request(target=activity_3) BY role_user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT {
    TERM web_element(label="File a Complaint", tag="link") -> web_element_2 : TERM
    RECORD ACTION click(target=web_element_2) STATUS succeeded SOURCE "t2:s2" -> click_event : EVENT
    TERM web_element(label="I want to warn others about a business or offer th...", tag="radio") -> web_element_3 : TERM
    RECORD ACTION click(target=web_element_3) STATUS succeeded SOURCE "t2:s5" -> click_event_2 : EVENT
    TERM web_element(label="Report a Scam", tag="link") -> web_element_4 : TERM
    RECORD ACTION click(target=web_element_4) STATUS succeeded SOURCE "t2:s7" -> click_event_3 : EVENT
    TERM web_element(label="Report a Scam", tag="button") -> web_element_5 : TERM
    RECORD ACTION click(target=web_element_5) STATUS succeeded SOURCE "t2:s9" -> click_event_4 : EVENT
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | request | covered |
| n2 | action | activity | covered |
| n3 | object | country::US, subject | covered |
| n4 | object | activity | covered |
| n5 | action | click | covered |
| n6 | object | web_element | covered |
| n7 | action | click | covered |
| n8 | object | web_element | covered |
| n9 | action | click | covered |
| n10 | object | web_element | covered |
| n11 | action | click | covered |
| n12 | object | web_element | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1-t2:s9 is represented.
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
