### S1 | type: add | dimension: constructor | symbol: unable_to
- Needs: n1 (t1:s1)
- Searches tried: "user failing to complete game" → failure (system only), user_practice (habitual), outcome (event output), raises_exception (runtime error); none fit
- Typed parameters: actor: STRING, activity: TERM
- Interpretation: the actor has not succeeded in / is unable to accomplish the described activity; claim relation, status via STATUS.
- Example: `CLAIM unable_to(activity=activity_2, actor=role_user) BY role_user STATUS asserted SOURCE "t1:s1" -> unable_to_2 : CLAIM`
- Proposed record: `{"symbol": "unable_to", "kind": "claim_relation", "signature": "CLAIM unable_to(actor: STRING, activity: TERM)", "definition": "The actor is failing or unable to accomplish the described activity.", "not": "failure (a system failing)", "aliases": ["failing to complete", "cannot"]}`
