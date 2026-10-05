Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="conserved_region", qualifier="CYP2D6") -> subject_2 : TERM
    TERM subject(kind="cnv") -> subject_3 : TERM
    TERM negation(target=subject_3) -> negation_2 : TERM
    TERM property_question(property="location", subject=subject_2) -> property_question_2 : TERM
    UTTER ask(target=property_question_2, constraints=[negation_2])
  }
  TURN t2 SPEAKER=AGENT {
    TERM subject(kind="chromosome_22", qualifier="22q13.31") -> subject_4 : TERM
    CLAIM spatial_state(object=t1.subject_2, reference=subject_4, relation="on") BY role_agent STATUS asserted SOURCE "t2:s1" -> spatial_state_2 : CLAIM
    CLAIM possesses(item=t1.subject_3, subject=t1.subject_2, value=FALSE) BY role_agent STATUS asserted SOURCE "t2:s1" -> possesses_2 : CLAIM
    TERM subject(kind="enzyme", qualifier="CYP2D6") -> subject_5 : TERM
    TERM activity(actor="CYP2D6", object="medications", verb="metabolize") -> activity_2 : TERM
    CLAIM enables(condition=subject_5, outcome=activity_2) BY role_agent STATUS asserted SOURCE "t2:s2" -> enables_2 : CLAIM
    UTTER inform(target=spatial_state_2)
  }
  TURN t3 SPEAKER=USER {
    TERM activity(object="cnv", verb="call") -> activity_3 : TERM
    TERM temporal_context(activity=activity_3) -> temporal_context_2 : TERM
    TERM subject(kind="control_region", qualifier="CYP2D6") -> subject_6 : TERM
    TERM property_question(property="location", subject=subject_6) -> property_question_3 : TERM
    UTTER ask(target=property_question_3)
  }
  TURN t4 SPEAKER=AGENT {
    CLAIM spatial_state(object=t3.subject_6, reference=t1.subject_2, relation="outside") BY role_agent STATUS asserted SOURCE "t4:s1" -> spatial_state_3 : CLAIM
    CLAIM spatial_state(object=t3.subject_6, reference=t2.subject_4, relation="on") BY role_agent STATUS asserted SOURCE "t4:s3" -> spatial_state_4 : CLAIM
    UTTER inform(target=spatial_state_3)
  }
  TURN t5 SPEAKER=USER {
    TERM activity(object=t3.subject_6, verb="find") -> activity_4 : TERM
    CLAIM request(target=activity_4) BY role_user STATUS asserted SOURCE "t5:s1" -> request_2 : CLAIM
    UTTER ask(target=activity_4)
  }
  TURN t6 SPEAKER=AGENT {
    TERM subject(kind="database_access") -> subject_7 : TERM
    CLAIM possesses(item=subject_7, subject=role_agent, value=FALSE) BY role_agent STATUS asserted SOURCE "t6:s1" -> possesses_3 : CLAIM
    UTTER apologize(target=possesses_3)
    TERM activity(object="scientific_literature", verb="consult") -> activity_5 : TERM
    CLAIM recommended(target=activity_5) BY role_agent STATUS asserted SOURCE "t6:s3" -> recommended_2 : CLAIM
    UTTER propose(target=activity_5)
  }
  TURN t7 SPEAKER=USER {
    UTTER ask(target=t3.property_question_3)
  }
  TURN t8 SPEAKER=AGENT {
    UTTER apologize()
    TERM subject(kind="gene", qualifier="H238") -> subject_8 : TERM
    CLAIM spatial_state(object=subject_8, reference=t1.subject_2, relation="next_to") BY role_agent STATUS asserted SOURCE "t8:s4" -> spatial_state_5 : CLAIM
    UTTER inform(target=spatial_state_5)
  }
  TURN t9 SPEAKER=USER {
    TERM activity(instrument=platform_label::ampliseq, object="cnv", verb="call") -> activity_6 : TERM
    UTTER ask(target=activity_6)
  }
  TURN t10 SPEAKER=AGENT {
    TERM activity(instrument=platform_label::ampliseq, object="targeted_sequencing_library", verb="prepare") -> activity_7 : TERM
    TERM activity(object="library", verb="sequence") -> activity_8 : TERM
    TERM activity(instrument=platform_label::bowtie, object="sequencing_reads", verb="align") -> activity_9 : TERM
    TERM activity(instrument=platform_label::cnvkit, object="cnv", verb="call") -> activity_10 : TERM
    TERM activity(object="cnv_results", verb="interpret") -> activity_11 : TERM
    TERM activity(object="cnv", verb="validate") -> activity_12 : TERM
    TERM sequence(items=[activity_7, activity_8, activity_9, activity_10, activity_11, activity_12]) -> sequence_2 : TERM
    UTTER respond(target=sequence_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, property_question, negation | covered |
| n2 | object | subject | covered |
| n3 | negation | negation, possesses | covered |
| n4 | claim | spatial_state, subject | covered |
| n5 | claim | enables, subject, activity | covered |
| n6 | speech_act | ask, property_question, temporal_context, activity | covered |
| n7 | object | subject | covered |
| n8 | claim | spatial_state | covered |
| n9 | claim | spatial_state | covered |
| n10 | speech_act | ask, request, activity | covered |
| n11 | claim | possesses, role_agent, subject | covered |
| n12 | action | activity, recommended, propose | covered |
| n13 | speech_act | ask | covered |
| n14 | claim | spatial_state, subject | covered |
| n15 | speech_act | ask, activity | covered |
| n16 | object | platform_label::ampliseq | label-preserved |
| n17 | action | activity | covered |
| n18 | action | activity | covered |
| n19 | action | activity, platform_label::bowtie | covered |
| n20 | object | platform_label::bowtie | label-preserved |
| n21 | action | activity | covered |
| n22 | object | platform_label::cnvkit | label-preserved |
| n23 | action | activity | covered |
| n24 | action | activity | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t10:s20 is represented
- Opaque-text spans: none
- Label-preserved spans: t9:s1, t10:s1 "ampliseq" → platform_label::ampliseq; t10:s9 "bowtie" → platform_label::bowtie; t10:s12 "cnvkit" → platform_label::cnvkit
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
