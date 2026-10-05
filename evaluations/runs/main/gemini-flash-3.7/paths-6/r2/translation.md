Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="gene", qualifier="CYP2D6") -> subject_2 : TERM
    TERM subject(kind="copy_number_variations") -> subject_3 : TERM
    TERM negation(target=subject_3) -> negation_2 : TERM
    TERM subject(kind="conserved_region", qualifier=subject_2) -> subject_4 : TERM
    TERM conjunction(items=[subject_4, negation_2]) -> conjunction_2 : TERM
    TERM property_question(property="location", subject=conjunction_2) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM subject(kind="conserved_region", qualifier="CYP2D6") -> subject_2 : TERM
    TERM subject(kind="copy_number_variations") -> subject_3 : TERM
    TERM subject(kind="enzyme", qualifier="CYP2D6") -> subject_4 : TERM
    TERM subject(kind="chromosome_22q13.31") -> subject_5 : TERM
    CLAIM spatial_state(object=subject_2, reference=subject_5, relation="in") BY role_agent STATUS asserted SOURCE "t2:s1" -> spatial_state_2 : CLAIM
    CLAIM attribute_claim(property="responsible_for", subject=subject_4, value="metabolizing_medications") BY role_agent STATUS asserted SOURCE "t2:s2" -> attribute_claim_2 : CLAIM
    CLAIM possesses(item=subject_3, subject=subject_2, value=FALSE) BY role_agent STATUS asserted SOURCE "t2:s3" -> possesses_2 : CLAIM
    UTTER inform(target=spatial_state_2)
    UTTER inform(target=attribute_claim_2)
    UTTER inform(target=possesses_2)
  }
  TURN t3 SPEAKER=USER {
    TERM activity(object="copy_number_variations", verb="call") -> activity_2 : TERM
    TERM temporal_context(activity=activity_2) -> temporal_context_2 : TERM
    TERM subject(kind="control_region", qualifier="CYP2D6") -> subject_2 : TERM
    TERM conjunction(items=[subject_2, temporal_context_2]) -> conjunction_2 : TERM
    TERM property_question(property="location", subject=conjunction_2) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
  TURN t4 SPEAKER=AGENT {
    TERM subject(kind="control_region", qualifier="CYP2D6") -> subject_2 : TERM
    TERM subject(kind="coding_region", qualifier="CYP2D6") -> subject_3 : TERM
    TERM subject(kind="chromosome_22q13.31") -> subject_4 : TERM
    CLAIM spatial_state(object=subject_2, reference=subject_3, relation="outside") BY role_agent STATUS asserted SOURCE "t4:s1" -> spatial_state_2 : CLAIM
    CLAIM spatial_state(object=subject_2, reference=subject_4, relation="in") BY role_agent STATUS asserted SOURCE "t4:s3" -> spatial_state_3 : CLAIM
    UTTER inform(target=spatial_state_2)
    UTTER inform(target=spatial_state_3)
  }
  TURN t5 SPEAKER=USER {
    TERM activity(object="copy_number_variations", verb="call") -> activity_2 : TERM
    TERM temporal_context(activity=activity_2) -> temporal_context_2 : TERM
    TERM subject(kind="control_region", qualifier="CYP2D6") -> subject_2 : TERM
    TERM conjunction(items=[subject_2, temporal_context_2]) -> conjunction_2 : TERM
    TERM activity(object=conjunction_2, verb="find") -> activity_3 : TERM
    UTTER ask(target=activity_3)
  }
  TURN t6 SPEAKER=AGENT {
    TERM subject(kind="real_time_database_access_or_internet_browsing") -> subject_2 : TERM
    CLAIM possesses(item=subject_2, subject=role_agent, value=FALSE) BY role_agent STATUS asserted SOURCE "t6:s1" -> possesses_2 : CLAIM
    TERM activity(object="scientific_literature_and_databases", verb="consult") -> activity_2 : TERM
    CLAIM recommended(target=activity_2) BY role_agent STATUS asserted SOURCE "t6:s3" -> recommended_2 : CLAIM
    UTTER apologize()
    UTTER inform(target=possesses_2)
    UTTER propose(target=activity_2)
  }
  TURN t7 SPEAKER=USER {
    TERM activity(object="copy_number_variations", verb="call") -> activity_2 : TERM
    TERM temporal_context(activity=activity_2) -> temporal_context_2 : TERM
    TERM subject(kind="control_region", qualifier="CYP2D6") -> subject_2 : TERM
    TERM conjunction(items=[subject_2, temporal_context_2]) -> conjunction_2 : TERM
    TERM property_question(property="location", subject=conjunction_2) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
  TURN t8 SPEAKER=AGENT {
    TERM subject(kind="control_region", qualifier="CYP2D6") -> subject_2 : TERM
    TERM subject(kind="gene", qualifier="CYP2D6") -> subject_3 : TERM
    TERM subject(kind="gene", qualifier="H238_CYP2D7P1") -> subject_4 : TERM
    TERM subject(kind="chromosome_22q13.31") -> subject_5 : TERM
    CLAIM spatial_state(object=subject_2, reference=subject_5, relation="in") BY role_agent STATUS asserted SOURCE "t8:s2" -> spatial_state_2 : CLAIM
    CLAIM spatial_state(object=subject_4, reference=subject_3, relation="next_to") BY role_agent STATUS asserted SOURCE "t8:s3" -> spatial_state_3 : CLAIM
    UTTER apologize()
    UTTER inform(target=spatial_state_2)
    UTTER inform(target=spatial_state_3)
  }
  TURN t9 SPEAKER=USER {
    TERM subject(kind="technology", qualifier="ampliseq") -> subject_2 : TERM
    TERM activity(instrument=platform_label::ampliseq, object="copy_number_variations", verb="call") -> activity_2 : TERM
    TERM property_question(property="method", subject=activity_2) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
  TURN t10 SPEAKER=AGENT {
    TERM activity(instrument=platform_label::ampliseq, object="sequencing_library", verb="prepare") -> activity_2 : TERM
    TERM activity(object="sequencing_library", verb="sequence") -> activity_3 : TERM
    TERM activity(instrument=platform_label::bowtie, object="sequencing_reads", verb="align") -> activity_4 : TERM
    TERM activity(instrument=platform_label::cnvkit, object="copy_number_variations", verb="call") -> activity_5 : TERM
    TERM activity(object="cnv_results", verb="interpret") -> activity_6 : TERM
    TERM activity(object="copy_number_variations", verb="validate") -> activity_7 : TERM
    TERM sequence(items=[activity_2, activity_3, activity_4, activity_5, activity_6, activity_7]) -> sequence_2 : TERM
    UTTER respond(target=sequence_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, property_question, subject, negation, conjunction | covered |
| n2 | object | subject | covered |
| n3 | negation | negation, possesses | covered |
| n4 | claim | spatial_state, role_agent | covered |
| n5 | claim | attribute_claim, role_agent | covered |
| n6 | speech_act | ask, property_question, subject, activity, temporal_context, conjunction | covered |
| n7 | object | subject | covered |
| n8 | claim | spatial_state, role_agent | covered |
| n9 | claim | spatial_state, role_agent | covered |
| n10 | speech_act | ask, activity, subject, temporal_context, conjunction | covered |
| n11 | claim | possesses, role_agent | covered |
| n12 | action | activity, recommended, propose | covered |
| n13 | speech_act | ask, property_question, subject, activity, temporal_context, conjunction | covered |
| n14 | claim | spatial_state, role_agent | covered |
| n15 | speech_act | ask, property_question, activity, platform_label::ampliseq | covered |
| n16 | object | platform_label::ampliseq | label-preserved |
| n17 | action | activity, platform_label::ampliseq | covered |
| n18 | action | activity | covered |
| n19 | action | activity, platform_label::bowtie | covered |
| n20 | object | platform_label::bowtie | label-preserved |
| n21 | action | activity, platform_label::cnvkit | covered |
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
