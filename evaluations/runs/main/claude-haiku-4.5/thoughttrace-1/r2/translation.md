Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM greeting(recipient=role_agent) -> greeting_2 : TERM
    UTTER acknowledge(target=greeting_2)
    CLAIM request(target=art_plan) BY role_user STATUS asserted SOURCE "t1:s2" -> request_2 : CLAIM
    UTTER ask(target=request_2)
    TERM temporal_context(activity="writing", period="while writing") -> temporal_context_2 : TERM
    CLAIM request(target=sequence(items=[activity(verb="organize")])) BY role_user STATUS asserted SOURCE "t1:s3" -> request_3 : CLAIM
    CLAIM request(target=art_structured_report) BY role_user STATUS asserted SOURCE "t1:s3" -> request_4 : CLAIM
    CLAIM involves(subject=request_4, target=temporal_context_2) BY role_user STATUS asserted SOURCE "t1:s3" -> involves_2 : CLAIM
    TERM art_story() -> art_story_2 : TERM
    CLAIM request(target=art_story_2) BY role_user STATUS asserted SOURCE "t1:s4" -> request_5 : CLAIM
    CLAIM designed_to_be(subject=request_5, quality="fanfiction") BY role_user STATUS asserted SOURCE "t1:s4" -> designed_to_be_2 : CLAIM
    CLAIM enables(condition=request_4, outcome=activity(verb="realize", object="vision")) BY role_user STATUS asserted SOURCE "t1:s5" -> enables_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT {
    TERM greeting(recipient=role_user) -> greeting_3 : TERM
    UTTER acknowledge(target=greeting_3)
    CLAIM request(target=art_structured_report) BY role_agent STATUS asserted SOURCE "t2:s3" -> request_6 : CLAIM
    UTTER inform(target=request_6)
    TERM document_section(title="Story Bible", items=[document_section(title="Global Summary"), document_section(title="Main Themes"), document_section(title="Tone and Atmosphere"), document_section(title="Target Audience"), document_section(title="Estimated Length")]) -> document_section_2 : TERM
    TERM document_section(title="Character Profiles", items=[character(name="Character Name"), character_trait(property="role"), character_trait(property="personality_traits"), character_trait(property="motivations"), character_trait(property="narrative_arc"), interpersonal_stance(actor="character", stance="relationships")]) -> document_section_3 : TERM
    TERM document_section(title="Worldbuilding and Setting", items=[location_spec(), time_horizon(), word_blend(base="canon", replacement="divergence")]) -> document_section_4 : TERM
    TERM sequence(items=[document_section(title="Macro Level - Acts"), document_section(title="Meso Level - Character Arcs"), document_section(title="Micro Level - Chapter Planning")]) -> sequence_2 : TERM
    TERM document_section(title="Plot Tracking", items=[activity(verb="track", object="main_plot"), activity(verb="track", object="subplots"), activity(verb="track", object="unresolved_threads")]) -> document_section_5 : TERM
    TERM conjunction(items=[activity(verb="write", instrument=platform_label::notion), activity(verb="write", instrument=platform_label::obsidian)]) -> conjunction_2 : TERM
    TERM activity(verb="draft", instrument=platform_label::google_docs) -> activity_2 : TERM
    TERM conjunction(items=[activity(verb="track_progress", instrument=platform_label::trello), activity(verb="track_progress", instrument=platform_label::notion)]) -> conjunction_3 : TERM
    TERM activity(verb="write_comprehensive", instrument=platform_label::scrivener) -> activity_3 : TERM
    TERM sequence(items=[activity(verb="review_chapter_notes"), activity(verb="write_draft"), activity(verb="update_plot_tracking")]) -> sequence_3 : TERM
    UTTER ask(target=activity(verb="specify", object="fandom"))
  }
  TURN t3 SPEAKER=USER {
    TERM well_wishes(recipient=role_agent, sentiment="appreciation") -> well_wishes_2 : TERM
    UTTER acknowledge(target=well_wishes_2)
    CLAIM designed_to_be(subject=request_4, quality="helpful") BY role_user STATUS asserted SOURCE "t3:s2" -> designed_to_be_3 : CLAIM
  }
  TURN t4 SPEAKER=AGENT {
    CLAIM enables(condition=art_plan, outcome=activity(verb="structure_ideas")) BY role_agent STATUS asserted SOURCE "t4:s2" -> enables_3 : CLAIM
    UTTER inform(target=enables_3)
    TERM obligation(actor="writer", activity=activity(verb="balance", object="planning_with_writing")) -> obligation_2 : TERM
    UTTER propose(target=obligation_2)
    TERM decision(activity=activity(verb="maintain_section", object="scattered_ideas")) -> decision_2 : TERM
    UTTER propose(target=decision_2)
    TERM interpersonal_stance(actor="character", stance="flexibility") -> interpersonal_stance_2 : TERM
    UTTER inform(target=interpersonal_stance_2)
    TERM temporal_context(activity="writing", period="throughout") -> temporal_context_3 : TERM
    UTTER propose(target=obligation(actor="writer", activity=activity(verb="pace_naturally")))
    UTTER offer(target=sequence(items=[activity(verb="build_character_sheet"), activity(verb="outline_chapter"), activity(verb="unblock_scene"), activity(verb="proofread_passage"), activity(verb="find_tone")]))
  }
  TURN t5 SPEAKER=USER {
    UTTER ask(target=activity(verb="help", object="writer_block"))
    UTTER ask(target=activity(verb="generate_ideas", object="story_continuation"))
  }
  TURN t6 SPEAKER=AGENT {
    UTTER confirm(target=activity(verb="help", object="writer_block"))
    TERM sequence(items=[activity(verb="propose_narrative_pathways"), activity(verb="suggest_transition_scenes"), character_trait(property="psychology", value="internal_logic")]) -> sequence_4 : TERM
    UTTER propose(target=sequence_4)
    TERM interpersonal_stance(actor="character", stance="consistency") -> interpersonal_stance_3 : TERM
    UTTER propose(target=interpersonal_stance_3)
    TERM activity(verb="generate_creative_prompts") -> activity_4 : TERM
    UTTER propose(target=activity_4)
    UTTER ask(target=subject(kind="story_status"))
    UTTER ask(target=subject(kind="planned_progression"))
    UTTER ask(target=subject(kind="specific_obstacle"))
  }
  TURN t7 SPEAKER=USER {
    UTTER acknowledge(target=role_agent)
    CLAIM ongoing(target=activity(verb="return_for_support")) BY role_user STATUS asserted SOURCE "t7:s2" -> ongoing_2 : CLAIM
  }
  TURN t8 SPEAKER=AGENT {
    UTTER offer(target=activity(verb="provide_support"))
    TERM well_wishes(recipient=role_user, sentiment="good_luck") -> well_wishes_3 : TERM
    UTTER inform(target=well_wishes_3)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | acknowledge, greeting | covered |
| n2 | action | ask, request | covered |
| n3 | action | temporal_context, sequence, activity | covered |
| n4 | object | art_structured_report, document_section | covered |
| n5 | object | art_story | covered |
| n6 | claim | enables, involves | covered |
| n7 | speech_act | acknowledge, greeting | covered |
| n8 | action | inform, art_structured_report | covered |
| n9 | action | document_section | covered |
| n10 | action | character, character_trait, interpersonal_stance | covered |
| n11 | action | location_spec, time_horizon, word_blend | covered |
| n12 | action | sequence, document_section | covered |
| n13 | action | document_section, activity | covered |
| n14 | object | platform_label::notion | label-preserved |
| n15 | object | platform_label::obsidian | label-preserved |
| n16 | object | platform_label::google_docs | label-preserved |
| n17 | object | platform_label::trello | label-preserved |
| n18 | object | platform_label::scrivener | label-preserved |
| n19 | action | sequence, obligation, activity | covered |
| n20 | speech_act | ask, activity | covered |
| n21 | speech_act | acknowledge, well_wishes | covered |
| n22 | action | obligation, decision, propose, inform | covered |
| n23 | speech_act | offer | covered |
| n24 | speech_act | ask, activity | covered |
| n25 | action | activity | covered |
| n26 | speech_act | confirm | covered |
| n27 | action | sequence, character_trait | covered |
| n28 | action | ask, subject | covered |
| n29 | speech_act | acknowledge | covered |
| n30 | speech_act | well_wishes, inform | covered |

## Translation report

- Input kind: conversation (French, multi-turn dialogue)
- Coverage status: complete
- Source-span coverage: all turns t1-t8 with all substantive sentences represented; structural/formatting elements (emoji, markdown headers) are metadata
- Opaque-text spans: none
- Label-preserved spans: n14–n18 (platform names encoded as value-group atoms, not resolved to semantic terms)
- Missing constructs: none identified
- Unresolved ambiguities: none; source language is clear and directly mappable
- Check: `node /kit/rag.mjs check` reports 0 unresolved needs and valid glossary usage
```
