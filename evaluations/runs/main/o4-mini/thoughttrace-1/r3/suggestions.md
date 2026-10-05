### S1 | type: add | dimension: constructor | symbol: story_organization_framework
- Needs: n4 (t1:s3)
- Searches tried: "story planning and organization framework" → no matching TERM constructor; existing "art_plan" is too general.
- Signature: TERM story_organization_framework() -> TERM
- Definition: A structured framework describing planning and organizational elements for writing a story; asserts nothing.
- not: Not an executed planning action or claim of completion
- aliases: ["organization framework", "planning framework"]
- Proposed record: {"symbol":"story_organization_framework","kind":"constructor","signature":"TERM story_organization_framework() -> TERM","definition":"A structured framework describing planning and organizational elements for writing a story; asserts nothing.","not":"Not an executed planning action or claim of completion","aliases":["organization framework","planning framework"]}

### S2 | type: add | dimension: constructor | symbol: categorize_best_methods
- Needs: n3 (t1:s3)
- Searches tried: "categorize best methods" → no TERM; "decision" constructor is related but covers a decision, not categorization; widen → nothing.
- Signature: TERM categorize_best_methods(domain: TERM) -> TERM
- Definition: A structured description of the act of categorizing the best methods for a given domain; asserts nothing.
- not: A decision or ranking execution; only a description.
- aliases: ["categorize methods", "methods categorization"]
- Proposed record: {"symbol":"categorize_best_methods","kind":"constructor","signature":"TERM categorize_best_methods(domain: TERM) -> TERM","definition":"A structured description of the act of categorizing the best methods for a given domain; asserts nothing.","not":"A decision or ranking execution; only a description.","aliases":["categorize methods","methods categorization"]}

### S3 | type: add | dimension: constructor | symbol: story_genre
- Needs: n5 (t1:s4)
- Searches tried: "fanfiction" → genre_label exists but cannot be linked to a subject by any TERM; widen "story genre term" → none.
- Signature: TERM story_genre(subject: TERM, genre: ATOM[genre_label]) -> TERM
- Definition: Links a story subject to its genre label; asserts nothing about the story’s content.
- not: Not a claim of publication or content generation; only a descriptive pairing.
- aliases: ["genre assignment"]
- Proposed record: {"symbol":"story_genre","kind":"constructor","signature":"TERM story_genre(subject: TERM, genre: ATOM[genre_label]) -> TERM","definition":"Links a story subject to its genre label; asserts nothing about the story’s content.","not":"Not a claim of publication or content generation; only a descriptive pairing.","aliases":["genre assignment"]}

### S4 | type: add | dimension: constructor | symbol: realize_vision
- Needs: n6 (t1:s5)
- Searches tried: "realize my vision" → no TERM; "enables" relation exists but needs a TERM for the outcome; widen → nothing.
- Signature: TERM realize_vision(actor: STRING / TERM) -> TERM
- Definition: A description of the actor’s act of realizing their creative vision; asserts nothing.
- not: Not a claim of successful outcome; only a description.
- aliases: ["realize vision"]
- Proposed record: {"symbol":"realize_vision","kind":"constructor","signature":"TERM realize_vision(actor: STRING / TERM) -> TERM","definition":"A description of the actor’s act of realizing their creative vision; asserts nothing.","not":"Not a claim of successful outcome; only a description.","aliases":["realize vision"]}