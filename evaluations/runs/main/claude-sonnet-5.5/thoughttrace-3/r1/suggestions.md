### S1 | type: add | dimension: composite | symbol: fails_to
- Needs: n1 (t1:s1)
- Searches tried: "user failing to complete a game" → failure (system failing), outcome (EVENT value), user_practice (habitual); no relation for an actor failing at an activity
- Expansion: new primitive claim relation rather than composite
- Typed parameters: actor: STRING, activity: TERM
- Interpretation: the actor is not succeeding in carrying out the described activity; asserts nothing about cause.
- Example: `CLAIM fails_to(activity=activity_2, actor=role_user) BY role_user STATUS asserted SOURCE "t1:s1" -> fails_to_2 : CLAIM`
- Proposed record: `{"symbol": "fails_to", "kind": "claim_relation", "signature": "CLAIM fails_to(actor: STRING, activity: TERM)", "definition": "The actor is failing to succeed at the described activity; no cause is implied.", "not": "failure (a system failing)", "aliases": ["unable to", "struggling to"]}`
