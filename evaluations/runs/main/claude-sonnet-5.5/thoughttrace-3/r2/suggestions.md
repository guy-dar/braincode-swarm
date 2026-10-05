### S1 | type: add | dimension: constructor | symbol: unable_to_complete
- Needs: n1 (t1:s1)
- Searches tried: "user failing to complete a game" → failure (system failing), user_practice (habitual), outcome (needs EVENT), cat_game (search category); no relation for an actor failing to accomplish an activity
- Typed parameters: activity: TERM
- Interpretation: the holder-described actor is currently unable to complete the described activity; asserts nothing about cause.
- Example: `CLAIM unable_to_complete(activity=activity_2) BY role_user STATUS asserted SOURCE "t1:s1" -> unable_to_complete_2 : CLAIM`
- Proposed record: `{"symbol": "unable_to_complete", "kind": "claim_relation", "signature": "CLAIM unable_to_complete(activity: TERM)", "definition": "The actor of the described activity has not succeeded in completing it and is struggling to do so.", "not": "failure (a system failing)", "aliases": ["failing to complete", "stuck on"]}`
