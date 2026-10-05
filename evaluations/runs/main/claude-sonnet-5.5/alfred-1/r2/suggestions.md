### S1 | type: add | dimension: constructor | symbol: located
- Needs: n8 (t2:s2), n9 (t2:s2), n13 (t2:s4), n16 (t2:s4), n24 (t2:s8), n26 (t2:s8)
- Searches tried: "on the wall", "across from the couch", "behind the vase" → spatial-relation values only (STRING for place.relation), location_spec (geographic); no figure–ground constructor
- Typed parameters: ground: TERM / STRING / ATOM[object_label], relation: STRING, figure?: TERM / STRING / ATOM[object_label]
- Interpretation: describes a spatial relation (spatial-relation value) to a ground entity, optionally of a figure; asserts nothing.
- Example: `TERM located(ground=described_object_3, relation=on) -> located_3 : TERM`
- Proposed record: `{"symbol": "located", "kind": "constructor", "signature": "TERM located(ground: TERM / STRING / ATOM[object_label], relation: STRING, figure?: TERM / STRING / ATOM[object_label]) -> TERM", "definition": "A spatial relation (spatial-relation value) holding relative to a ground entity, optionally for a stated figure; describes, asserts nothing.", "not": "a geographic location (location_spec) or the place operation", "aliases": ["positioned"]}`

### S2 | type: add | dimension: constructor | symbol: described_object
- Needs: n3, n6, n7, n10, n14, n15, n20, n21, n25 (t1:s1, t2:s2–s8)
- Searches tried: "black end table", "white vase", "purple ottoman" → color_label only in pick_up.color/search_web.color; no object-description constructor
- Typed parameters: kind: STRING / ATOM[object_label], color?: ATOM[color_label], constraints?: LIST[TERM]
- Interpretation: description of an object of a kind with optional colour and identifying constraints; selects nothing, asserts nothing.
- Example: `TERM described_object(color=color_label::black, kind=object_label::endtable) -> described_object_5 : TERM`
- Proposed record: `{"symbol": "described_object", "kind": "constructor", "signature": "TERM described_object(kind: STRING / ATOM[object_label], color?: ATOM[color_label], constraints?: LIST[TERM]) -> TERM", "definition": "Description of an object of the given kind with optional colour and identifying constraints; asserts nothing.", "not": "a runtime REF", "aliases": []}`

### S3 | type: refine | dimension: refine-entry | target: v19/support/activity
- Needs: n4, n5, n17, n18, n22 (t2:s2, s6, s8), n1 (t1:s1)
- Searches tried: "turn left", "go through the living room to", "turn around" → turn/walk operations (not TERM), activity lacks direction/destination/via
- Before: activity(verb, actor?, object?, location?, instrument?, purpose?)
- After: add optional direction: STRING, destination: TERM / STRING / ATOM[object_label], via: TERM
- Justification: navigation and placement descriptions need destination, path and heading roles
- Affected uses: none
- Compatibility: additive
- Proposed record: `{"signature": "TERM activity(verb: STRING, actor?: STRING, object?: STRING / TERM / ATOM[object_label] / ATOM[food_label] / ATOM[animal_label], location?: STRING / ATOM[country], instrument?: STRING / ATOM[object_label] / ATOM[platform_label], purpose?: TERM, direction?: STRING, destination?: TERM / STRING / ATOM[object_label], via?: TERM) -> TERM"}`
