### S1 | type: add | dimension: vocabulary-member | symbol: request
- Needs: n1 (t1:s1), n10 (t3:s1), n12 (t3:s1)
- Searches tried: retrieval candidates propose, inform, respond → none means requesting work from the addressee
- Meaning: speech act requesting that the addressee perform the described activity
- Category: speech act
- Contextual aliases: ask_for
- Example: `UTTER request(target=activity_2)`
- Contrast: propose (suggests an idea, not demands work)
- Proposed record: `{"symbol": "request", "kind": "speech_act", "signature": "UTTER request(target: TERM)", "definition": "Request that the addressee perform the described activity or provide the described content; asserts nothing.", "not": "propose (suggestion)", "aliases": ["ask_for"]}`

### S2 | type: add | dimension: constructor | symbol: story_contains
- Needs: n4–n9, n13–n18 (t2:s3–s17, t4:s3–s17)
- Searches tried: "story contains event" → provides, has_goal, enables; none fit
- Typed parameters: story: TERM, element: TERM
- Interpretation: the described story includes the element (event, character, relation) in its content.
- Example: `CLAIM story_contains(element=activity_4, story=adaptation_of_3) ...`
- Proposed record: `{"symbol": "story_contains", "kind": "claim_relation", "signature": "CLAIM story_contains(story: TERM, element: TERM)", "definition": "The described story includes the element as part of its content.", "not": "provides (supply of an item or service)", "aliases": ["plot_includes"]}`

### S3 | type: add | dimension: constructor | symbol: adaptation_of
- Needs: n1, n2 (t1:s1), n11 (t3:s1)
- Searches tried: "medieval adaptation of a film" → aesthetic (period+style only), art_story; none name a source work
- Typed parameters: source: STRING / TERM, setting: STRING / TERM
- Interpretation: a version of the source work transposed into the given setting; describes, asserts nothing.
- Example: `TERM adaptation_of(setting="medieval fantasy", source="Inception") -> adaptation_of_2 : TERM`
- Proposed record: `{"symbol": "adaptation_of", "kind": "constructor", "signature": "TERM adaptation_of(source: STRING / TERM, setting: STRING / TERM) -> TERM", "definition": "A version of the source work transposed into the stated setting.", "not": "aesthetic (style with period)", "aliases": ["reimagining"]}`
