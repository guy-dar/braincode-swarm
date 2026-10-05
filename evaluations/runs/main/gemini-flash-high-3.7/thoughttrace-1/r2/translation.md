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
    TERM subject(kind="planning", qualifier="organization") -> subject_2 : TERM
    CLAIM request(target=subject_2) BY role_user STATUS asserted SOURCE "t1:s2" -> request_2 : CLAIM
    TERM activity(object=art_story, verb="write") -> activity_2 : TERM
    TERM temporal_context(activity=activity_2) -> temporal_context_2 : TERM
    TERM lexical_label(value=genre_label::fanfiction) -> lexical_label_2 : TERM
    CLAIM enables(condition=subject_2, outcome=lexical_label_2) BY role_user STATUS asserted SOURCE "t1:s5" -> enables_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT {
    TERM greeting(recipient=role_user) -> greeting_3 : TERM
    UTTER acknowledge(target=greeting_3)
    TERM document_section(title="Bible de l'histoire") -> document_section_2 : TERM
    TERM audience_targeting(criteria=["general"]) -> audience_targeting_2 : TERM
    TERM character(name="protagonist") -> character_2 : TERM
    TERM character_trait(property="personality", value="determined") -> character_trait_2 : TERM
    TERM location_spec(area="setting") -> location_spec_2 : TERM
    TERM time_horizon(horizon="timeline") -> time_horizon_2 : TERM
    TERM sequence(items=[document_section_2]) -> sequence_2 : TERM
    TERM performance_tracking(target=art_story) -> performance_tracking_2 : TERM
    CLAIM provides(actor=platform_label::notion, subject=art_structured_report) BY role_agent STATUS asserted SOURCE "t2:s61" -> provides_2 : CLAIM
    CLAIM provides(actor=platform_label::obsidian, subject=art_structured_report) BY role_agent STATUS asserted SOURCE "t2:s61" -> provides_3 : CLAIM
    CLAIM provides(actor=platform_label::google_docs, subject=art_story) BY role_agent STATUS asserted SOURCE "t2:s62" -> provides_4 : CLAIM
    CLAIM provides(actor=platform_label::trello, subject=art_plan) BY role_agent STATUS asserted SOURCE "t2:s63" -> provides_5 : CLAIM
    CLAIM provides(actor=platform_label::scrivener, subject=art_story) BY role_agent STATUS asserted SOURCE "t2:s64" -> provides_6 : CLAIM
    UTTER ask(target=t1.subject_2)
  }
  TURN t3 SPEAKER=USER {
    UTTER acknowledge(target=t2.greeting_3)
  }
  TURN t4 SPEAKER=AGENT {
    CLAIM recommended(target=t1.activity_2) BY role_agent STATUS asserted SOURCE "t4:s4" -> recommended_2 : CLAIM
    CLAIM ongoing(target=t2.character_2) BY role_agent STATUS asserted SOURCE "t4:s12" -> ongoing_2 : CLAIM
    UTTER offer(target=t2.character_2)
  }
  TURN t5 SPEAKER=USER {
    UTTER ask(target=t1.activity_2)
  }
  TURN t6 SPEAKER=AGENT {
    CLAIM statement(fact=t2.character_2) BY role_agent STATUS asserted SOURCE "t6:s1" -> statement_2 : CLAIM
    UTTER confirm(target=statement_2)
    TERM dialogue(style="consistent") -> dialogue_2 : TERM
    UTTER propose(target=dialogue_2)
    CLAIM provides(actor=role_user, subject=t1.subject_2) BY role_agent STATUS asserted SOURCE "t6:s19" -> provides_7 : CLAIM
  }
  TURN t7 SPEAKER=USER {
    UTTER acknowledge(target=t1.greeting_2)
  }
  TURN t8 SPEAKER=AGENT {
    TERM well_wishes(recipient=role_user, sentiment="good_luck") -> well_wishes_2 : TERM
    UTTER acknowledge(target=well_wishes_2)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | greeting, role_agent, acknowledge | covered |
| n2 | action | request, subject, role_user | covered |
| n3 | action | temporal_context, activity, art_story | covered |
| n4 | object | art_story, subject | covered |
| n5 | object | genre_label::fanfiction, lexical_label | label-preserved |
| n6 | claim | enables, role_user | covered |
| n7 | speech_act | greeting, role_user, acknowledge | covered |
| n8 | action | art_structured_report, provides | covered |
| n9 | action | document_section, audience_targeting | covered |
| n10 | action | character, character_trait | covered |
| n11 | action | location_spec, time_horizon | covered |
| n12 | action | sequence, document_section | covered |
| n13 | action | performance_tracking, art_story | covered |
| n14 | object | platform_label::notion | label-preserved |
| n15 | object | platform_label::obsidian | label-preserved |
| n16 | object | platform_label::google_docs | label-preserved |
| n17 | object | platform_label::trello | label-preserved |
| n18 | object | platform_label::scrivener | label-preserved |
| n19 | action | sequence, document_section | covered |
| n20 | speech_act | ask, subject | covered |
| n21 | speech_act | acknowledge, role_agent | covered |
| n22 | action | recommended, role_agent | covered |
| n23 | speech_act | offer, ongoing, character | covered |
| n24 | speech_act | ask, activity | covered |
| n25 | action | activity, art_story | covered |
| n26 | speech_act | confirm, statement | covered |
| n27 | action | dialogue, propose | covered |
| n28 | action | provides, role_user | covered |
| n29 | speech_act | acknowledge, role_agent | covered |
| n30 | speech_act | well_wishes, role_user | covered |

## Translation report

- Input kind: conversation
- Coverage status: complete
- Source-span coverage: every segment t1:s1–t8:s12 is represented
- Opaque-text spans: none
- Label-preserved spans: t1:s4 "fanfiction" → genre_label::fanfiction; t2:s61 "Notion" → platform_label::notion; t2:s61 "Obsidian" → platform_label::obsidian; t2:s62 "Google Docs" → platform_label::google_docs; t2:s63 "Trello" → platform_label::trello; t2:s64 "Scrivener" → platform_label::scrivener
- Missing constructs: none
- Unresolved ambiguities: none
- Check: `rag check` reported 0 unresolved needs and 0 unknown symbols
