### S1 | type: add | dimension: vocabulary-member | symbol: instruct
- Needs: n1 (t1:s1), n2–n39 (t2:s2–t2:s14)
- Searches tried: widen “user commands agent to place pan containing knife on table” and search “imperative directive instruct someone to perform an action”; closest candidates `propose` and `ask` describe suggesting and requesting information, respectively; `request` is a claim relation, not a speech act.
- Meaning: An imperative directive that tells its recipient to perform the action or ordered plan described by a TERM; it records the speech act, not execution or success.
- Category: speech_act
- Contextual aliases: command, instruct
- Example: `UTTER instruct(target=activity_term)`
- Contrast: `propose` suggests an action; `instruct` directs a recipient to perform it.
- Proposed record: {"symbol":"instruct","kind":"speech_act","signature":"UTTER instruct(target: TERM)","definition":"An imperative directive to perform the action or ordered plan described by target. It records no execution or success.","not":"A suggestion to consider an action (use propose), or a record that the action occurred.","aliases":["command","instruct"]}

### S2 | type: refine | dimension: refine-entry | target: v19/support/subject
- Needs: n11 (t2:s2), n33 (t2:s12)
- Searches tried: entry `subject` and `color_label`; search “black color of a table” and widen “black color qualifier of table subject.” Current subject qualifier accepts STRING / TERM / ATOM[platform_label], while `color_label` is an open group and no color-compatible qualifier slot was retrieved.
- Before: `subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM`
- After: `subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label] / ATOM[color_label], location?: STRING / ATOM[country], time?: STRING) -> TERM`
- Justification: Allows an explicitly supplied color qualifier to remain typed and separate from the subject kind.
- Affected uses: Subject terms specifying a color-qualified entity, including both black-table mentions here.
- Compatibility: Additive signature refinement; existing calls remain valid.
- Proposed record: {"signature":"TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label] / ATOM[color_label], location?: STRING / ATOM[country], time?: STRING) -> TERM"}

### S3 | type: add | dimension: vocabulary-member | symbol: on_left_side_of
- Needs: n38 (t2:s14)
- Searches tried: widen “left side of table and above another object spatial constraints” and search “position object on left-side region of a surface”; `left_of` means positioned to the left of the reference object, not on the left-side region of that surface.
- Meaning: The object occupies the left-side region of the referenced surface; the relation includes being located on that surface.
- Category: spatial-relation
- Contextual aliases: none
- Example: `spatial_constraint(relation=on_left_side_of, object=pan_term, reference=table_term)`
- Contrast: `left_of` places an object to the side of a reference and does not imply that it rests on the reference surface.
- Proposed record: {"symbol":"on_left_side_of","kind":"value","category":"spatial-relation","signature":"STRING spatial-relation value","definition":"The object occupies the left-side region of the referenced surface, including being located on that surface.","not":"Positioned to the left of a reference without being on its surface (use left_of).","aliases":[]}

### S4 | type: add | dimension: vocabulary-member | symbol: above
- Needs: n39 (t2:s14)
- Searches tried: widen “left side of table and above another object spatial constraints” and search “vertical spatial relation higher than reference”; `under` means beneath and is not an equivalent relation. No `above` entry was retrieved.
- Meaning: The object is vertically higher than the reference object.
- Category: spatial-relation
- Contextual aliases: none
- Example: `spatial_constraint(relation=above, object=pan_term, reference=lettuce_term)`
- Contrast: `under` means beneath the reference object.
- Proposed record: {"symbol":"above","kind":"value","category":"spatial-relation","signature":"STRING spatial-relation value","definition":"The object is vertically higher than the reference object.","not":"Beneath the reference object (use under).","aliases":[]}
