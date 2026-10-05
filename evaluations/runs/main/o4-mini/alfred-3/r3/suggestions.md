### S1 | type: add | dimension: vocabulary-member | symbol: command
- Needs: n1 (t1:s1)
- Searches tried: `rag search "command" --kind speech_act` → no speech_act; `rag widen "issue a command"` → no match
- Proposed record: {"symbol":"command","kind":"speech_act","signature":"UTTER command(target: TERM)","definition":"Record a directive speech act with a TERM describing the commanded action.","not":"a suggestion or question (use propose/respond)","aliases":["instruct","order"]}

### S2 | type: add | dimension: vocabulary-member | symbol: walk_forward
- Needs: n2 (t2:s2)
- Searches tried: `rag search "walk forward"` → only `walk(destination)` exists; no exact match
- Proposed record: {"symbol":"walk_forward","kind":"operation","signature":"() -> void","definition":"Move the agent one step forward in its current facing direction.","not":"walk toward a particular entity (use walk(destination))","aliases":["step_forward"]}

### S3 | type: add | dimension: constructor | symbol: select_object
- Needs: n15 (t2:s4), n20 (t2:s8), n39 (t2:s14)
- Searches tried: `rag search "select the knife next to lettuce"` → no candidate; `rag widen "choose object by relation"` → nothing suitable
- Typed parameters: reference: STRING / ATOM[object_label], target_class: STRING / ATOM[object_label], relation: STRING / ATOM[spatial-relation]
- Interpretation: yields a TERM identifying the one object of the given class satisfying the spatial relation to the reference.
- Example: `TERM select_object(reference=object_label::lettuce, target_class=object_label::knife, relation=next_to) -> knife_target : TERM`
- Proposed record: {"symbol":"select_object","kind":"TERM constructor","signature":"TERM select_object(reference: STRING / ATOM[object_label], target_class: STRING / ATOM[object_label], relation: STRING / ATOM[spatial-relation]) -> TERM","definition":"Identify the single target object of the given class located in the specified spatial relation to a reference object.","not":"a bulk search of multiple objects","aliases":["find_nearest","choose_adjacent"]}

### S4 | type: refine | dimension: refine-entry | target: pick_up
- Needs: n12 (t2:s4)
- Searches tried: `rag entry pick_up` → signature only accepts STRING/ATOM, not TERM
- Before: `pick_up(target: STRING / ATOM[object_label] / ATOM[food_label], …)`
- After: allow `target: STRING / ATOM[...] / TERM` so results of select_object can be piped directly into pick_up.
- Justification: enable compositional pipelines where abstract TERM descriptors feed into ACTION.
- Affected uses: none—existing STRING/ATOM targets still valid.
- Proposed record: {"symbol":"pick_up","signature":"(target: STRING / ATOM[object_label] / ATOM[food_label] / TERM, quantity?: NUMBER, source?: STRING / ATOM[object_label], color?: STRING / ATOM[color_label], shape?: STRING, state?: STRING) -> REF[STRING] or LIST[REF[STRING]]"}