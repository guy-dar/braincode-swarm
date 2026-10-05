Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    UTTER greeting(recipient=role_agent)
    TERM offer_help() -> offer_help_2 : TERM
    UTTER ask(target=offer_help_2)
    TERM request_plan_and_categorize() -> request_plan_and_categorize_2 : TERM # PROPOSED: S1
    UTTER ask(target=request_plan_and_categorize_2)
    UTTER inform(content="Cette histoire serait une fanfiction")
    UTTER inform(content="Cela me permettra de mieux réaliser ma vision")
  }
  TURN t2 SPEAKER=AGENT {
    UTTER greeting(recipient=role_user)
    UTTER acknowledge(target=offer_help_2)
    TERM organization_system() -> organization_system_2 : TERM # PROPOSED: S2
    UTTER propose(target=organization_system_2)
    UTTER propose(target=organization_system_2)
  }
  TURN t3 SPEAKER=USER {
    UTTER acknowledge(target=organization_system_2)
  }
  TURN t4 SPEAKER=AGENT {
    UTTER offer(target=offer_help_2)
    UTTER propose(target=organization_system_2)
  }
  TURN t5 SPEAKER=USER {
    UTTER ask(target=offer_help_2)
  }
  TURN t6 SPEAKER=AGENT {
    UTTER propose(target=organization_system_2)
    UTTER ask(target=request_plan_and_categorize_2)
  }
  TURN t7 SPEAKER=USER {
    UTTER inform(content="Merci ! Je reviendrai vers toi si j'ai à nouveau besoin de ton aide.")
  }
  TURN t8 SPEAKER=AGENT {
    UTTER well_wishes(recipient=role_user)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | greeting | covered |
| n2 | action | offer_help | covered |
| n3 | action | request_plan_and_categorize (PROPOSED: S1) | proposed |
| n4 | object | organization_system (PROPOSED: S2) | proposed |
| n5 | object | inform(content) | opaque |
| n6 | claim | inform(content) | opaque |
| n7 | speech_act | greeting, acknowledge, propose, offer, ask, well_wishes | covered |

## Why the translation failed

- n3 "categorize best methods for staying organized while writing a story": no existing constructor represents a planning-and-categorization request. Proposed S1 to add `planning_request` (or similar).
- n4 "story planning and organization framework": no existing TERM constructor for an organization system or framework artifact. Proposed S2 to add `organization_system`.
- n5 "fanfiction → genre_label::<key>": no signature accepts a genre_label qualifier in a TERM constructor; current subject qualifier slot does not admit ATOM[genre_label].
- n6 "organization will help realize the author's vision": no claim relation to express enabling an author's vision; fallback to opaque utterance.

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: all turns represented; structured target requests for most speech acts; content fallbacks for fanfiction and vision.
- Opaque-text spans: t1:s4, t1:s5 — represented as raw `content` fallbacks
- Label-preserved spans: none
- Missing constructs: S1 planning_request constructor; S2 organization_system constructor
- Unresolved ambiguities: none beyond missing vocabulary
- Check: `rag check` reported 4 unknown symbols (request_plan_and_categorize, organization_system, plus their handles) and 0 other errors
