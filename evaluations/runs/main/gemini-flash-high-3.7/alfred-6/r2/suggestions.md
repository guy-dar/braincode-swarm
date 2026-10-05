### S1 | type: refine | dimension: refine-entry | target: v19/operation-vocabulary/pick_up
- Needs: n13 (t2:s4)
- Searches tried: "title", "book title" -> textbook, document_section, art_short_text; widen "book title" --kind constraint -> no parameter or constraint for object title/inscription
- Before: (target: STRING / ATOM[object_label] / ATOM[food_label], quantity?: NUMBER, source?: STRING / ATOM[object_label], color?: STRING / ATOM[color_label], shape?: STRING, state?: STRING) -> REF[STRING] or LIST[REF[STRING]]
- After: (target: STRING / ATOM[object_label] / ATOM[food_label], quantity?: NUMBER, source?: STRING / ATOM[object_label], color?: STRING / ATOM[color_label], shape?: STRING, state?: STRING, title?: STRING) -> REF[STRING] or LIST[REF[STRING]]
- Justification: In embodied navigation and manipulation environments (e.g. ALFRED), objects like books or packaging frequently need to be disambiguated by their printed title or text label.
- Affected uses: None in existing glossary examples.
- Compatibility: Fully backward compatible since title is an optional parameter.
- Proposed record: {"signature": "(target: STRING / ATOM[object_label] / ATOM[food_label], quantity?: NUMBER, source?: STRING / ATOM[object_label], color?: STRING / ATOM[color_label], shape?: STRING, state?: STRING, title?: STRING) -> REF[STRING] or LIST[REF[STRING]]", "definition": "Select/acquire objects with optional color, shape, state, or title qualification. Missing quantity or literal 1 returns REF; integer literal greater than 1 returns LIST[REF]. Other values are invalid for this profile."}
