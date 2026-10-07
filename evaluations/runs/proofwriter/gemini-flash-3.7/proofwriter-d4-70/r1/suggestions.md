### S1 | type: add | dimension: lexical-group | symbol: trait_label
- Needs: n31 (t1:s11), n34 (t1:s12), n41 (t1:s14), n43 (t1:s15), n47 (t1:s16), n49 (t1:s17), n50 (t1:s17), n53 (t1:s18), n57 (t1:s19), n58 (t1:s19), n60 (t1:s20), n66 (t1:s21), n72 (t1:s23)
- Searches tried: "young" → constraint_17_plus, constraint_budget_limited, unit_sentence; "kind" → enables, comfortable, important; "furry" → dog, yarn; widen found no general trait or adjective value group
- Domain: A source-supplied descriptive trait, character attribute, or adjective label denoting that labeled property without inferred taxonomy or evaluation.
- Admission: open_label
- Key form: lower_word
- Key aliases: {}
- Consuming signatures: lexical_label.value, has_attribute.attribute
- Illustrative values: trait_label::young, trait_label::kind, trait_label::furry
- Positive example: `TERM lexical_label(value=trait_label::kind) -> lexical_label_kind : TERM`
- Negative example: `color_label::blue` (color names belong to color_label)
- Overlap analysis: Existing value groups (color_label, animal_label, food_label, object_label, platform_label) do not cover general traits or adjectives like young, kind, or furry.
- Signature refinements: lexical_label (refine to accept ATOM[trait_label])
- Compatibility: Fully backward-compatible additive change.
- Proposed record: `{"symbol": "trait_label", "kind": "lexical_group", "definition": "A source-supplied descriptive trait or attribute label; denotes that labeled trait without inferred behavior or taxonomy.", "group": {"examples": ["trait_label::young", "trait_label::kind", "trait_label::furry"]}}`

### S2 | type: refine | dimension: refine-entry | target: v19/support/lexical_label
- Needs: n29 (t1:s11), n32 (t1:s12), n38 (t1:s14), n42 (t1:s15), n45 (t1:s16), n48 (t1:s17), n52 (t1:s18), n55 (t1:s19), n59 (t1:s20), n63 (t1:s21), n70 (t1:s23)
- Searches tried: entry lexical_label
- Before: `TERM lexical_label(value: ATOM[object_label] / ATOM[genre_label] / ATOM[food_label] / ATOM[animal_label] / ATOM[color_label]) -> TERM`
- After: `TERM lexical_label(value: ATOM[object_label] / ATOM[genre_label] / ATOM[food_label] / ATOM[animal_label] / ATOM[color_label] / ATOM[trait_label]) -> TERM`
- Justification: Enables wrapping trait_label atoms into typed TERM descriptors for composition in rules, claims, and questions.
- Affected uses: None (additive union variant).
- Compatibility: Fully backward-compatible.
- Proposed record: `{"signature": "TERM lexical_label(value: ATOM[object_label] / ATOM[genre_label] / ATOM[food_label] / ATOM[animal_label] / ATOM[color_label] / ATOM[trait_label]) -> TERM"}`
