### S1 | type: add | dimension: lexical-group | symbol: property_label
- Needs: n8 (t1:s8), n10 (t1:s10), n11 (t1:s11), n13 (t1:s13), n14 (t1:s14), n15 (t1:s15), n16 (t1:s16), n17 (t1:s17)
- Searches tried: search "young" "nice" "kind" → constraint_17_plus, size_small, tone_polite, comfortable; widen "trait" → nothing for general descriptive properties or traits
- Domain: Open-label source-supplied descriptive property, trait, or characteristic label
- Admission: open_label
- Key form: lower_word
- Key aliases: {}
- Consuming signatures: has_attribute.attribute, subject.kind, subject.qualifier, requirement.property
- Illustrative values: property_label::kind, property_label::young, property_label::nice
- Positive example: `CLAIM has_attribute(attribute=property_label::kind, subject="Fiona") BY role_user STATUS asserted SOURCE "t1:s8" -> has_attribute_8 : CLAIM`
- Negative example: Do not use for physical dimensions (use size_large) or geometric shapes (use shape_round).
- Overlap analysis: No existing value group covers general behavioral, age, or qualitative entity attributes and traits.
- Signature refinements: refine has_attribute.attribute and subject.qualifier / subject.kind to accept ATOM[property_label]
- Compatibility: Additive open group; does not affect existing valid translations.
- Proposed record: {"symbol": "property_label", "kind": "lexical_group", "definition": "A source-supplied property, trait, or attribute label; denotes that named characteristic without inferred semantic hierarchy or behavior.", "group": {"admission": "open_label", "key_form": "lower_word", "examples": ["property_label::kind", "property_label::young", "property_label::nice"]}}

### S2 | type: refine | dimension: refine-entry | target: v19/support/has_attribute
- Needs: n8 (t1:s8), n10 (t1:s10), n11 (t1:s11)
- Searches tried: entry has_attribute → accepts subject: STRING / TERM, attribute: STRING / TERM
- Before: CLAIM has_attribute(subject: STRING / TERM, attribute: STRING / TERM)
- After: CLAIM has_attribute(subject: STRING / TERM, attribute: STRING / TERM / ATOM[property_label])
- Justification: Allows has_attribute to accept open property_label values directly as attribute arguments.
- Affected uses: None in existing glossary examples.
- Compatibility: Fully backward compatible.
- Proposed record: {"signature": "CLAIM has_attribute(subject: STRING / TERM, attribute: STRING / TERM / ATOM[property_label])", "status": "Accepted"}

### S3 | type: refine | dimension: refine-entry | target: v19/support/subject
- Needs: n13 (t1:s13), n14 (t1:s14), n15 (t1:s15), n16 (t1:s16), n17 (t1:s17)
- Searches tried: entry subject → qualifier accepts STRING / TERM / ATOM[platform_label]
- Before: TERM subject(kind: STRING, qualifier?: STRING / TERM / ATOM[platform_label], location?: STRING / ATOM[country], time?: STRING) -> TERM
- After: TERM subject(kind: STRING / ATOM[property_label], qualifier?: STRING / TERM / ATOM[platform_label] / ATOM[property_label] / ATOM[color_label], location?: STRING / ATOM[country], time?: STRING) -> TERM
- Justification: Enables subject terms to represent entities qualified by open property labels or color labels in reasoning premises and conditionals.
- Affected uses: None in existing glossary examples.
- Compatibility: Fully backward compatible.
- Proposed record: {"signature": "TERM subject(kind: STRING / ATOM[property_label], qualifier?: STRING / TERM / ATOM[platform_label] / ATOM[property_label] / ATOM[color_label], location?: STRING / ATOM[country], time?: STRING) -> TERM", "status": "Accepted"}
