Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM greeting(recipient=role_agent) -> greeting_2 : TERM
    UTTER greeting(recipient=role_agent)
    TERM offer_help() -> offer_help_3 : TERM
    UTTER ask(target=offer_help_3)
    TERM classify(item=subject(kind="methods_for_organization"), criterion="best") -> classify_4 : TERM   # PROPOSED: S1
    UTTER ask(target=classify_4)
    TERM organization_framework(focus=subject(kind="organization_during_story_writing")) -> organization_framework_5 : TERM   # PROPOSED: S2
    UTTER ask(target=organization_framework_5)
    TERM subject(kind="story", qualifier=genre_label::fanfiction) -> subject_6 : TERM
    UTTER inform(target=subject_6)
    TERM subject(kind="vision") -> subject_7 : TERM
    CLAIM enables(condition=organization_framework_5, outcome=subject_7) BY role_user STATUS asserted SOURCE "t1:s5" -> enables_8 : CLAIM
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | greeting | covered |
| n2 | action | ask | covered |
| n3 | action | classify (PROPOSED: S1) | proposed |
| n4 | object | organization_framework (PROPOSED: S2) | proposed |
| n5 | object | genre_label::fanfiction | label-preserved |
| n6 | claim | enables | covered |
| n7 | speech_act | — | unresolved |
| n8 | action | — | unresolved |
| n9 | action | — | unresolved |
| n10 | action | — | unresolved |
| n11 | action | — | unresolved |
| n12 | action | — | unresolved |
| n13 | action | — | unresolved |
| n14 | object | — | unresolved |
| n15 | object | — | unresolved |
| n16 | object | — | unresolved |
| n17 | object | — | unresolved |
| n18 | object | — | unresolved |
| n19 | action | — | unresolved |
| n20 | speech_act | — | unresolved |
| n21 | speech_act | — | unresolved |
| n22 | action | — | unresolved |
| n23 | speech_act | — | unresolved |
| n24 | speech_act | — | unresolved |
| n25 | action | — | unresolved |
| n26 | speech_act | — | unresolved |
| n27 | action | — | unresolved |
| n28 | action | — | unresolved |
| n29 | speech_act | — | unresolved |
| n30 | speech_act | — | unresolved |

## Why the translation failed

- n3 "categorize best methods for staying organized while writing a story" (t1:s3): no existing constructor or composite to express classification; requires S1.
- n4 "story planning and organization framework" (t1:s3): no existing constructor for a planning scaffold; requires S2.
- n7–n30: many subsequent agent and user turns introduce specialized actions, objects, and structured templates (bible sections, character profiles, worldbuilding framework, narrative structures, tracking features, tool recommendations, routines, support offers) with no existing glossary symbols. Each major concept (e.g., character_profile, worldbuilding_framework, narrative_sequence, performance_tracking) would need suitable constructors or composites.

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: turn t1, sentences s1–s5 represented; subsequent turns not formalized
- Opaque-text spans: none
- Label-preserved spans: n5 genre_label::fanfiction
- Missing constructs: S1 classify constructor; S2 organization_framework constructor; plus many missing planning and section constructors for t2–t8
- Unresolved ambiguities: none beyond missing vocabulary
- Check: `rag check` reported 28 unresolved needs, 2 proposed symbols (classify, organization_framework) not in glossary