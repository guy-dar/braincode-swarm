Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="conserved_region", qualifier="CYP2D6") -> subject_2 : TERM
    TERM exclude(item="copy_number_variations") -> exclude_2 : TERM
    TERM conjunction(items=[subject_2, exclude_2]) -> conjunction_2 : TERM
    TERM property_question(property="location", subject=conjunction_2) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
  TURN t2 SPEAKER=AGENT {
    TERM subject(kind="chromosome", qualifier="22q13.31") -> subject_2 : TERM
    CLAIM spatial_state(object=t1.subject_2, reference=subject_2, relation=in) BY role_agent STATUS asserted SOURCE "t2:s1" -> spatial_state_2 : CLAIM
    TERM activity(object="medications", verb="metabolize") -> activity_2 : TERM
    CLAIM enables(condition=t1.subject_2, outcome=activity_2) BY role_agent STATUS asserted SOURCE "t2:s2" -> enables_2 : CLAIM
    TERM subject(kind="variation", qualifier="copy_number_variation") -> subject_3 : TERM
    CLAIM possesses(item=subject_3, subject=t1.subject_2, value=FALSE) BY role_agent STATUS asserted SOURCE "t2:s3" -> possesses_2 : CLAIM
    UTTER inform(target=spatial_state_2)
  }
  TURN t3 SPEAKER=USER {
    TERM temporal_context(activity="call_cnv") -> temporal_context_2 : TERM
    TERM subject(kind="control_region", qualifier="CYP2D6") -> subject_2 : TERM
    TERM conjunction(items=[subject_2, temporal_context_2]) -> conjunction_2 : TERM
    TERM property_question(property="location", subject=conjunction_2) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
  TURN t4 SPEAKER=AGENT {
    TERM subject(kind="coding_region", qualifier="CYP2D6") -> subject_2 : TERM
    CLAIM spatial_state(object=t3.subject_2, reference=subject_2, relation=other_side_of) BY role_agent STATUS asserted SOURCE "t4:s1" -> spatial_state_2 : CLAIM
    CLAIM varies_with(target=t3.subject_2, condition="cnv_analysis_method") BY role_agent STATUS asserted SOURCE "t4:s2" -> varies_with_2 : CLAIM
    TERM subject(kind="chromosome", qualifier="22q13.31") -> subject_3 : TERM
    CLAIM spatial_state(object=t3.subject_2, reference=subject_3, relation=in) BY role_agent STATUS asserted SOURCE "t4:s3" -> spatial_state_3 : CLAIM
    UTTER inform(target=spatial_state_2)
  }
  TURN t5 SPEAKER=USER {
    TERM activity(object=t3.subject_2, verb="find") -> activity_2 : TERM
    UTTER ask(target=activity_2)
  }
  TURN t6 SPEAKER=AGENT {
    TERM subject(kind="capability", qualifier="real_time_database_and_internet_access") -> subject_2 : TERM
    CLAIM possesses(item=subject_2, subject=role_agent, value=FALSE) BY role_agent STATUS asserted SOURCE "t6:s1" -> possesses_2 : CLAIM
    CLAIM unaware(person=role_agent, topic=t3.subject_2) BY role_agent STATUS asserted SOURCE "t6:s2" -> unaware_2 : CLAIM
    TERM activity(object="scientific_literature_and_databases_and_experts", verb="consult") -> activity_2 : TERM
    CLAIM recommended(target=activity_2) BY role_agent STATUS asserted SOURCE "t6:s3" -> recommended_2 : CLAIM
    UTTER inform(target=recommended_2)
  }
  TURN t7 SPEAKER=USER {
    TERM property_question(property="control_region", subject=t3.subject_2) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
  TURN t8 SPEAKER=AGENT {
    TERM subject(kind="gene", qualifier="H238_CYP2D7P1") -> subject_2 : TERM
    TERM subject(kind="gene", qualifier="CYP2D6") -> subject_3 : TERM
    CLAIM spatial_state(object=subject_2, reference=subject_3, relation=next_to) BY role_agent STATUS asserted SOURCE "t8:s4" -> spatial_state_2 : CLAIM
    CLAIM attribute_claim(property="reference_control_region", subject=subject_2, value=TRUE) BY role_agent STATUS asserted SOURCE "t8:s3" -> attribute_claim_2 : CLAIM
    UTTER inform(target=spatial_state_2)
  }
  TURN t9 SPEAKER=USER {
    TERM activity(instrument=platform_label::ampliseq, object="copy_number_variations", verb="call_cnv") -> activity_2 : TERM
    UTTER ask(target=activity_2)
  }
  TURN t10 SPEAKER=AGENT {
    TERM activity(instrument=platform_label::ampliseq, object="targeted_sequencing_library", verb="prepare_library") -> activity_2 : TERM
    TERM activity(instrument="next_generation_sequencing_platform", object="sequencing_library", verb="sequence") -> activity_3 : TERM
    TERM activity(instrument=platform_label::bowtie, object="sequencing_reads", verb="align_reads") -> activity_4 : TERM
    TERM activity(instrument=platform_label::cnvkit, object="read_depth_coverage", verb="call_cnv") -> activity_5 : TERM
    TERM activity(object="cnv_results", verb="interpret_results") -> activity_6 : TERM
    TERM activity(object="copy_number_variations", verb="validate_cnv") -> activity_7 : TERM
    TERM sequence(items=[activity_2, activity_3, activity_4, activity_5, activity_6, activity_7]) -> sequence_2 : TERM
    UTTER respond(target=sequence_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | ask, property_question, subject, conjunction, exclude | covered |
| n2 | object | subject | covered |
| n3 | negation | exclude, possesses | covered |
| n4 | claim | spatial_state, subject, in | covered |
| n5 | claim | enables, activity | covered |
| n6 | speech_act | ask, property_question, subject, conjunction, temporal_context | covered |
| n7 | object | subject | covered |
| n8 | claim | spatial_state, other_side_of | covered |
| n9 | claim | spatial_state, subject, in | covered |
| n10 | speech_act | ask, activity | covered |
| n11 | claim | possesses, unaware, subject, role_agent | covered |
| n12 | action | activity, recommended | covered |
| n13 | speech_act | ask, property_question | covered |
| n14 | claim | spatial_state, attribute_claim, subject, next_to | covered |
| n15 | speech_act | ask, activity, platform_label::ampliseq | covered |
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
- Label-preserved spans: t9:s1, t10:s1 "AmpliSeq" → platform_label::ampliseq; t10:s9 "Bowtie" → platform_label::bowtie; t10:s12 "CNVkit" → platform_label::cnvkit
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
