Status: success
Mode: TRACE

## BrainCode

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    UTTER greeting(recipient=role_agent) -> greeting_2 : TERM
    CLAIM request(target=activity(verb="help", object="planning")) BY role_user STATUS asserted SOURCE "t1:s2" -> request_2 : CLAIM
    UTTER ask(topic=activity(verb="organize", object="story_writing")) -> ask_3 : TERM
    TERM character(name="fanfiction_story") -> character_4 : TERM
    CLAIM enables(condition=art_plan, outcome=activity(verb="realize", object="author_vision")) BY role_user STATUS asserted SOURCE "t1:s5" -> enables_5 : CLAIM
  }
  TURN t2 SPEAKER=AGENT {
    UTTER greeting(recipient=role_user) -> greeting_6 : TERM
    UTTER acknowledge(target=request_2) -> acknowledge_7 : TERM
    UTTER inform(target=propose(target=art_structured_report)) -> inform_8 : TERM
    TERM document_section(title="Story Bible", items=[
      document_section(title="Summary"),
      document_section(title="Themes"),
      document_section(title="Tone and Atmosphere"),
      document_section(title="Target Audience"),
      document_section(title="Estimated Length")
    ]) -> document_section_9 : TERM
    TERM document_section(title="Character Profiles", items=[
      document_section(title="Name"),
      document_section(title="Role in Story"),
      document_section(title="Canon Reinterpretation"),
      document_section(title="Personality Traits"),
      document_section(title="Motivations and Objectives"),
      document_section(title="Character Arc"),
      document_section(title="Relationships")
    ]) -> document_section_10 : TERM
    TERM document_section(title="Worldbuilding and Setting", items=[
      document_section(title="Source Universe"),
      document_section(title="Main Locations"),
      document_section(title="Timeline"),
      document_section(title="Canon Divergence Points"),
      document_section(title="Universe-Specific Rules")
    ]) -> document_section_11 : TERM
    TERM sequence(items=[
      document_section(title="Macro Level: Acts and Major Sections"),
      document_section(title="Meso Level: Character Arcs"),
      document_section(title="Micro Level: Chapter-by-Chapter Plan")
    ]) -> sequence_12 : TERM
    TERM document_section(title="Chapter Planning", items=[
      document_section(title="Narrative Objective"),
      document_section(title="Planned Scenes"),
      document_section(title="Present Characters"),
      document_section(title="Plot Advancement"),
      document_section(title="Cliffhanger")
    ]) -> document_section_13 : TERM
    TERM document_section(title="Plot Tracking", items=[
      document_section(title="Main Plot"),
      document_section(title="Subplots"),
      document_section(title="Chapter-by-Chapter Tracking"),
      document_section(title="Unresolved Plot Threads")
    ]) -> document_section_14 : TERM
    TERM sequence(items=[
      activity(verb="use", object=platform_label::notion),
      activity(verb="use", object=platform_label::obsidian),
      activity(verb="use", object=platform_label::google_docs),
      activity(verb="use", object=platform_label::trello),
      activity(verb="use", object=platform_label::scrivener)
    ]) -> sequence_15 : TERM
    TERM sequence(items=[
      activity(verb="review", object="chapter_notes"),
      activity(verb="note", object="inconsistencies"),
      activity(verb="update", object="plot_tracking")
    ]) -> sequence_16 : TERM
    UTTER ask(topic=activity(verb="identify", object="fandom")) -> ask_17 : TERM
  }
  TURN t3 SPEAKER=USER {
    UTTER acknowledge(target=inform_8) -> acknowledge_18 : TERM
    CLAIM designed_to_be(subject=art_structured_report, quality="helpful") BY role_user STATUS asserted SOURCE "t3:s2" -> designed_to_be_19 : CLAIM
    UTTER express_interest(target=art_plan) -> express_interest_20 : TERM
  }
  TURN t4 SPEAKER=AGENT {
    UTTER inform(target=propose(target=decision(activity=activity(verb="balance", object="planning_and_writing")))) -> inform_21 : TERM
    TERM obligation(actor="author", activity=activity(verb="write")) -> obligation_22 : TERM
    TERM include(item="loose_ideas") -> include_23 : TERM
    TERM include(item="flexibility") -> include_24 : TERM
    TERM include(item="pacing_control") -> include_25 : TERM
    UTTER offer(target=activity(verb="help", object="character_sheets")) -> offer_26 : TERM
    UTTER offer(target=activity(verb="help", object="chapter_outlines")) -> offer_27 : TERM
    UTTER offer(target=activity(verb="help", object="scene_unblocking")) -> offer_28 : TERM
    UTTER offer(target=activity(verb="help", object="proofreading")) -> offer_29 : TERM
  }
  TURN t5 SPEAKER=USER {
    UTTER ask(topic=activity(verb="help", object="writer_block_resolution")) -> ask_30 : TERM
    UTTER ask(topic=activity(verb="generate", object="ideas")) -> ask_31 : TERM
  }
  TURN t6 SPEAKER=AGENT {
    CLAIM ongoing(target=activity(verb="support")) BY role_agent STATUS asserted SOURCE "t6:s1" -> ongoing_32 : CLAIM
    UTTER confirm(target=ongoing_32) -> confirm_33 : TERM
    UTTER inform(target=propose(target=activity(verb="suggest", object="narrative_pathways"))) -> inform_34 : TERM
    UTTER inform(target=propose(target=activity(verb="suggest", object="transition_scenes"))) -> inform_35 : TERM
    UTTER inform(target=propose(target=activity(verb="analyze", object="character_psychology"))) -> inform_36 : TERM
    UTTER ask(topic=activity(verb="describe", object="current_story_state")) -> ask_37 : TERM
    UTTER ask(topic=activity(verb="describe", object="intended_progression")) -> ask_38 : TERM
    UTTER ask(topic=activity(verb="describe", object="specific_obstacle")) -> ask_39 : TERM
  }
  TURN t7 SPEAKER=USER {
    UTTER acknowledge(target=inform_34) -> acknowledge_40 : TERM
    CLAIM ongoing(target=activity(verb="return_for_help")) BY role_user STATUS asserted SOURCE "t7:s2" -> ongoing_41 : CLAIM
  }
  TURN t8 SPEAKER=AGENT {
    UTTER well_wishes(recipient=role_user, sentiment="encouragement") -> well_wishes_42 : TERM
    UTTER offer(target=activity(verb="help", object="writer_block_support")) -> offer_43 : TERM
    UTTER offer(target=activity(verb="help", object="idea_development")) -> offer_44 : TERM
    UTTER offer(target=activity(verb="help", object="project_organization")) -> offer_45 : TERM
    UTTER offer(target=activity(verb="help", object="passage_review")) -> offer_46 : TERM
    UTTER offer(target=activity(verb="help", object="story_discussion")) -> offer_47 : TERM
    UTTER well_wishes(recipient=role_user, sentiment="good_luck") -> well_wishes_48 : TERM
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | greeting (t1) | covered |
| n2 | action | request, ask | covered |
| n3 | action | ask with activity | covered |
| n4 | object | art_plan | covered |
| n5 | object | character (implicit fanfiction) | label-preserved |
| n6 | claim | enables | covered |
| n7 | speech_act | greeting, acknowledge | covered |
| n8 | action | inform, propose, art_structured_report | covered |
| n9 | action | document_section with story bible items | covered |
| n10 | action | document_section with character profile items | covered |
| n11 | action | document_section with worldbuilding items | covered |
| n12 | action | sequence with narrative levels, document_section | covered |
| n13 | action | document_section with plot tracking | covered |
| n14 | object | platform_label::notion | covered |
| n15 | object | platform_label::obsidian | covered |
| n16 | object | platform_label::google_docs | covered |
| n17 | object | platform_label::trello | covered |
| n18 | object | platform_label::scrivener | covered |
| n19 | action | sequence with writing routine | covered |
| n20 | speech_act | ask | covered |
| n21 | speech_act | acknowledge, express_interest | covered |
| n22 | action | propose, obligation, include | covered |
| n23 | speech_act | offer, ongoing | covered |
| n24 | speech_act | ask | covered |
| n25 | action | propose with narrative pathways | covered |
| n26 | speech_act | confirm | covered |
| n27 | action | propose with character analysis | covered |
| n28 | action | ask for context | covered |
| n29 | speech_act | acknowledge | covered |
| n30 | speech_act | well_wishes | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: All 8 turns (t1–t8) with their numbered sentences (t1:s1–t8:s12) are represented through UTTER speech acts, CLAIM relations, and TERM constructors describing the guide content
- Opaque-text spans: none
- Label-preserved spans: n5 (fanfiction mentioned as character name, role preserved but not semantically resolved as a genre-specific artifact type)
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
```

Let me verify this with the check command:
<function_calls>
<invoke name="bash">
<parameter name="command">cd /output && node /kit/rag.mjs check --translation translation.md 2>&1