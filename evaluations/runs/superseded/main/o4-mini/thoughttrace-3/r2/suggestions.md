### S1 | type: add | dimension: vocabulary-member | symbol: inability_to_complete
- Needs: n1 (t1:s1)
- Searches tried: "inability to complete a game" → no matching claim_relation; widen "fail to complete activity" → nothing suitable
- Category: claim_relation
- Meaning: The holder is unable to complete the described activity; asserts a failure to achieve completion.
- Contextual aliases: cannot_complete, fail_to_complete
- Example: `CLAIM inability_to_complete(activity=activity(verb="complete", actor=role_user, object=game_subject)) -> inability_to_complete_2 : CLAIM`
- Contrast: a general system failure
- Proposed record: {"symbol":"inability_to_complete","kind":"claim_relation","signature":"CLAIM inability_to_complete(activity: TERM)","definition":"The holder is unable to complete the described activity; asserts a failure to achieve completion.","not":"a general system failure","aliases":["cannot_complete","fail_to_complete"]}