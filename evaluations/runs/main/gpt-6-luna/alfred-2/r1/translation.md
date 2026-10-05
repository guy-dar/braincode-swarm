Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM food_portion(food=food_label::lettuce, form="slice", quantity=1) -> food_portion_2 : TERM # PROPOSED: S2
    TERM action_description(verb="cool", target=food_portion_2) -> action_description_2 : TERM # PROPOSED: S1
    TERM action_description(verb="place", target=food_portion_2, destination=object_label::counter, relation=on) -> action_description_3 : TERM # PROPOSED: S1
    TERM sequence(items=[action_description_2, action_description_3]) -> sequence_2 : TERM
    CLAIM request(target=sequence_2) BY role_user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
  }
  TURN t2 SPEAKER=AGENT {
    TERM subject(kind=lettuce, location=counter) -> subject_2 : TERM
    TERM food_portion(food=subject_2, form="slice", quantity=1) -> food_portion_3 : TERM # PROPOSED: S2
    TERM action_description(verb="turn", direction="left") -> action_description_4 : TERM # PROPOSED: S1
    TERM action_description(verb="walk", destination=object_label::sink, manner="across the room") -> action_description_5 : TERM # PROPOSED: S1
    TERM action_description(verb="face", target=object_label::sink) -> action_description_6 : TERM # PROPOSED: S1
    TERM action_description(verb="pick_up", target=object_label::knife, source=object_label::sink) -> action_description_7 : TERM # PROPOSED: S1
    TERM action_description(verb="turn", direction="around") -> action_description_8 : TERM # PROPOSED: S1
    TERM action_description(verb="step", direction="forward") -> action_description_9 : TERM # PROPOSED: S1
    TERM action_description(verb="face", target=subject_2) -> action_description_10 : TERM # PROPOSED: S1
    TERM action_description(verb="cut", target=subject_2, source=object_label::counter, result_state=state_sliced) -> action_description_11 : TERM # PROPOSED: S1
    TERM action_description(verb="turn", direction="around") -> action_description_12 : TERM # PROPOSED: S1
    TERM action_description(verb="step", direction="forward") -> action_description_13 : TERM # PROPOSED: S1
    TERM action_description(verb="face", target=object_label::counter) -> action_description_14 : TERM # PROPOSED: S1
    TERM action_description(verb="place", target=object_label::knife, destination=object_label::counter, relation=on) -> action_description_15 : TERM # PROPOSED: S1
    TERM action_description(verb="turn", direction="around") -> action_description_16 : TERM # PROPOSED: S1
    TERM action_description(verb="step", direction="forward") -> action_description_17 : TERM # PROPOSED: S1
    TERM action_description(verb="face", target=subject_2) -> action_description_18 : TERM # PROPOSED: S1
    TERM action_description(verb="pick_up", target=food_portion_3, source=object_label::counter) -> action_description_19 : TERM # PROPOSED: S1
    TERM action_description(verb="turn", direction="around") -> action_description_20 : TERM # PROPOSED: S1
    TERM action_description(verb="step", direction="forward") -> action_description_21 : TERM # PROPOSED: S1
    TERM action_description(verb="face", target=object_label::fridge) -> action_description_22 : TERM # PROPOSED: S1
    TERM action_description(verb="cool", target=food_portion_3, resource=object_label::fridge) -> action_description_23 : TERM # PROPOSED: S1
    TERM action_description(verb="remove", target=food_portion_3, source=object_label::fridge) -> action_description_24 : TERM # PROPOSED: S1
    TERM action_description(verb="step", direction="left") -> action_description_25 : TERM # PROPOSED: S1
    TERM action_description(verb="face", target=object_label::counter) -> action_description_26 : TERM # PROPOSED: S1
    TERM action_description(verb="place", target=food_portion_3, destination=object_label::counter, relation=right_of, relative_to=object_label::sink) -> action_description_27 : TERM # PROPOSED: S1
    TERM sequence(items=[action_description_4, action_description_5, action_description_6, action_description_7, action_description_8, action_description_9, action_description_10, action_description_11, action_description_12, action_description_13, action_description_14, action_description_15, action_description_16, action_description_17, action_description_18, action_description_19, action_description_20, action_description_21, action_description_22, action_description_23, action_description_24, action_description_25, action_description_26, action_description_27]) -> sequence_3 : TERM
    UTTER propose(target=sequence_3)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | action | action_description (PROPOSED: S1) | proposed |
| n2 | object | food_portion (PROPOSED: S2) | proposed |
| n3 | action | action_description (PROPOSED: S1) | proposed |
| n4 | object | object_label::counter | label-preserved |
| n5 | action | action_description (PROPOSED: S1) | proposed |
| n6 | object | object_label::sink | label-preserved |
| n7 | action | action_description (PROPOSED: S1) | proposed |
| n8 | object | object_label::knife | label-preserved |
| n9 | action | action_description (PROPOSED: S1) | proposed |
| n10 | object | food_label::lettuce | label-preserved |
| n11 | action | action_description (PROPOSED: S1) | proposed |
| n12 | action | action_description (PROPOSED: S1) | proposed |
| n13 | action | action_description (PROPOSED: S1) | proposed |
| n14 | action | action_description (PROPOSED: S1) | proposed |
| n15 | action | action_description (PROPOSED: S1) | proposed |
| n16 | action | action_description (PROPOSED: S1) | proposed |
| n17 | object | object_label::fridge | label-preserved |
| n18 | action | action_description (PROPOSED: S1) | proposed |
| n19 | action | action_description (PROPOSED: S1) | proposed |
| n20 | action | action_description (PROPOSED: S1) | proposed |

## Why the translation failed

- n1 / n2 (t1:s1), n3 (t2:s2), n5 (t2:s4), n7 (t2:s6), n9 (t2:s8), n12 (t2:s10), n13 (t2:s12), n14 (t2:s14), n15 (t2:s16), n16 (t2:s18), n18 (t2:s20), n19 (t2:s22), n20 (t2:s24): `widen "user requests cooling a lettuce slice and placing it on counter"`, `widen "chill or cool food using fridge resource, then remove from fridge"`, and `widen "turn around and step forward toward target, locomotion step distance and orientation"`; also searched "describe action as a structured TERM target of request speech act", "cool lettuce slice in fridge", "step forward locomotion", "remove food object from fridge", and "record object changed state after operation". `activity` can describe an action but does not provide the needed destination/resource, direction, relation, and result-state roles together; `sequence` only orders existing terms; `chill` and `remove` are operations for execution/recording, not descriptions of requested or proposed work. The retrieved `place` operation additionally requires a runtime REF and is not a TRACE speech-act representation. S1 proposes one compositional TERM action description to preserve the operations and their roles without claiming they happened.
- n2 (t1:s1), n10 (t2:s6), n15 (t2:s16), n18 (t2:s20), n20 (t2:s24): the food label can preserve `lettuce` but cannot express a singular slice/portion. `state_sliced` describes lettuce cut into pieces and does not identify one slice. Searched/widened "cool lettuce slice in fridge", "remove food object from fridge", and "represent a requested sequence of actions as a TERM, with actions as structured descriptions". S2 proposes a reusable portion TERM with an explicit form and quantity.

## Translation report

- Pinned release: Glossary 19.0.0-draft.2-lexical-groups+g19 (sha be5d8379f7a6); language spec 19.0.0-draft.2-lexical-groups.
- Input kind: conversation / supplied trajectory.
- Coverage status: partial.
- Source-span coverage: t1:s1 represented as the user's active request; agent action clauses in t2:s2, t2:s4, t2:s6, t2:s8, t2:s10, t2:s12, t2:s14, t2:s16, t2:s18, t2:s20, t2:s22, and t2:s24 represented in source order as the agent's proposed sequence. Number-only markers t2:s1, t2:s3, t2:s5, t2:s7, t2:s9, t2:s11, t2:s13, t2:s15, t2:s17, t2:s19, t2:s21, and t2:s23 add no semantic content.
- Opaque-text spans: none.
- Label-preserved spans: t1:s1 and t2:s16 "lettuce" → food_label::lettuce; t1:s1 and t2:s24 "counter" → object_label::counter; t2:s2 and t2:s4 "sink" → object_label::sink; t2:s4 and t2:s12 "knife" → object_label::knife; t2:s18 and t2:s20 "fridge" → object_label::fridge. These open-group labels preserve source labels only; they do not assert additional properties.
- Missing constructs: S1 action-description TERM constructor; S2 food-portion TERM constructor. Proposed meanings/signatures are listed in `/output/suggestions.md`.
- Unresolved ambiguities: none material to the source clauses represented. The trace does not establish that the proposed actions succeeded; therefore the agent's step list is represented as a proposal and not as successful RECORD events.
- Check: `node /kit/rag.mjs check --translation /output/translation.md` reported all 20 needs matched by its heuristic coverage check, but flagged the two proposed, currently unknown constructors `action_description` and `food_portion`. The item therefore remains a failed translation until the suggestions are accepted and the proposed document is validated.
