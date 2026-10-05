### S1 | type: add | dimension: vocabulary-member | symbol: ask
- Needs: n1 (t1:s1)
- Searches tried: "write the plot" → activity (existing), no speech_act for user requests; widen "speech act ask" → nothing
- Definition: A speech act representing a user request or question to perform an action described by the TERM target.
- Signature: UTTER ask(target: TERM)
- Not: not a proposal by the agent (use propose)
- Aliases: question, request
- Example: `UTTER ask(target=activity(verb="write", object="plot"))`
- Proposed record: {"symbol":"ask","kind":"speech_act","signature":"UTTER ask(target: TERM)","definition":"Represents a user request or question to perform the described action.","not":"not an assertion or confirmation","aliases":["question","request"]}

### S2 | type: add | dimension: vocabulary-member | symbol: provide
- Needs: n3 (t2:s1–s17), n12 (t4:s1–s17)
- Searches tried: "provide adaptation" → provides (claim_relation), no speech_act; widen "speech act provide" → nothing
- Definition: A speech act by an agent presenting or supplying structured content described by the TERM target.
- Signature: UTTER provide(target: TERM)
- Not: not the recording of an executed action (use RECORD)
- Aliases: present, supply, deliver
- Example: `UTTER provide(target=art_story_term)`
- Proposed record: {"symbol":"provide","kind":"speech_act","signature":"UTTER provide(target: TERM)","definition":"Represents an agent speech act presenting or supplying the described content.","not":"not a recorded action outcome","aliases":["present","supply","deliver"]}

### S3 | type: add | dimension: vocabulary-member | symbol: rewrite
- Needs: n10 (t3:s1)
- Searches tried: "rewrite this" → no candidate; widen "speech act rewrite" → nothing
- Definition: A speech act representing a user's request to produce a revised version of the described content.
- Signature: UTTER rewrite(target: TERM)
- Not: not an execution of rewriting (use ACTION for external operations)
- Aliases: revise
- Example: `UTTER rewrite(target=content_term)`
- Proposed record: {"symbol":"rewrite","kind":"speech_act","signature":"UTTER rewrite(target: TERM)","definition":"Represents a user's request to produce a revised version of the described content.","not":"not the action of rewriting executed","aliases":["revise"]}