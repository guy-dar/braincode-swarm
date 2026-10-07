# Suggestions from translator proofwriter-d3-30-r1

### S1 | type: add | dimension: constructor | symbol: has_property
- Needs: n2 (t1:s2), n3 (t1:s2), n4 (t1:s2), n5 (t1:s3), n6 (t1:s3), n7 (t1:s4), n8 (t1:s4), n9 (t1:s4), n10 (t1:s5), n11 (t1:s5), n12 (t1:s6), n13 (t1:s6), n14 (t1:s7), n15 (t1:s7), n16 (t1:s7), n17 (t1:s8), n18 (t1:s8), n19 (t1:s9), n21 (t1:s10), n22 (t1:s11), n25 (t1:s11), n26 (t1:s12), n27 (t1:s13), n28 (t1:s14), n29 (t1:s14), n30 (t1:s15), n31 (t1:s16), n32 (t1:s17), n36 (t1:s19), n37 (t1:s19)
- Searches tried: "subject has property" → attribute_claim (claim relation, cannot be used inside conditional terms), requirement (artifact constraint); "entity predicate" → entity_mains (menu item); widen "property attribution" → nothing suitable as a descriptive term constructor
- Typed parameters: property: STRING, subject?: STRING / TERM, value?: STRING / BOOL / NUMBER
- Interpretation: Constructs a descriptive term representing that a subject entity (or an uninstantiated generic subject if omitted) possesses a named property or attribute, optionally evaluated to a specific value; asserts nothing by itself.
- Example: `TERM has_property(property="big", subject="Anne") -> has_property_2 : TERM`
- Proposed record: `{"symbol": "has_property", "kind": "constructor", "signature": "TERM has_property(property: STRING, subject?: STRING / TERM, value?: STRING / BOOL / NUMBER) -> TERM", "definition": "Constructs a descriptive term asserting that a subject possesses a named property or attribute; asserts nothing by itself.", "not": "attribute_claim (a top-level CLAIM relation) or requirement (an artifact production constraint)", "aliases": ["entity_property", "predicate", "has_trait", "holds_property"]}`
