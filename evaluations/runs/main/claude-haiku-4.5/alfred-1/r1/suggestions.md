# Suggestions for missing constructors

### S1 | type: add | dimension: constructor | symbol: spatial_relation

- Needs: n8 (t2:s2), n9 (t2:s2), n13 (t2:s4), n24 (t2:s8), n26 (t2:s8)
- Searches tried: 
  - `search "behind the vase"` → vase, behind (values), but no constructor for positioned relationships
  - `search "on the wall"` → wall (location-name), on (spatial-relation value), but spatial-relation is only used in operation signatures
  - `widen "constraint for spatial position"` → returned constraint_exclude_* (style exclusions only), no positional constraint
  - Spatial-relation values (behind, left_of, on, other_side_of, etc.) exist in glossary but only as operation parameters; no TERM constructor uses them

- Typed parameters: target: STRING / TERM, relation: STRING / ATOM[spatial-relation], reference: STRING / TERM
- Interpretation: Describes the spatial position of a target object relative to a reference object or location; relation identifies the spatial relationship (behind, left_of, on, etc.); neither asserts a fact nor modifies the target object. This is a descriptive construction for specifying locations in instructions.
- Example: 
  ```braincode
  TERM spatial_relation(target="keys", relation=behind, reference="vase") -> keys_position : TERM
  ```
- Rationale: Instructions in the item describe objects by their positions (keys behind vase, ottoman across from couch, keys on left of cell phone, end table on wall). The activity constructor captures verb and involved objects but cannot represent spatial relationships. Spatial-relation values exist in the glossary but are only available as operation parameters (place.relation, walk.relation), not as standalone descriptors.
- Proposed record: `{"symbol": "spatial_relation", "kind": "constructor", "signature": "TERM spatial_relation(target: STRING / TERM, relation: STRING / ATOM[spatial-relation], reference: STRING / TERM) -> TERM", "definition": "Describes the spatial position of a target relative to a reference object or location. Uses the same spatial-relation values as place/walk operations. Neither asserts nor modifies; purely descriptive.", "not": "not a property of the target object, nor a constraint on placement (use with activity to describe intent)", "aliases": ["positioned", "located", "relative_position"]}`

### S2 | type: add | dimension: constructor | symbol: object_descriptor

- Needs: n6 (t2:s2), n14 (t2:s4), n20 (t2:s6), n10 (t2:s2), n15 (t2:s4), n19 (t2:s6), n25 (t2:s8)
- Searches tried:
  - `search "black end table"` → table (location-name), color_label::black (group), but activity constructor has no color/property parameter
  - `search "white vase"` → vase (entity-name), color_label::white (group), no property descriptor
  - `search "purple ottoman"` → ottoman (not in glossary), color_label::purple (group), no way to attach color to object
  - `widen "object with color property"` → only entity-name values for objects; no property TERM constructor
  - Checked activity signature: accepts verb, actor, object, location, instrument, purpose; no color, size, material, or other properties

- Typed parameters: target: STRING / TERM, property: STRING, value: STRING / ATOM[color_label] / ATOM[product-attribute-value] / NUMBER
- Interpretation: Attaches a property descriptor to an object name or TERM. Common properties include visual attributes (color, size, material). The value may be a color_label atom, a general product-attribute value, or a free STRING. Used to disambiguate or fully describe objects when more than the bare object name is needed.
- Example:
  ```braincode
  TERM object_descriptor(target="end_table", property="color", value=color_label::black) -> black_table : TERM
  TERM activity(verb="go", location=black_table) -> go_activity : TERM
  ```
- Rationale: Source instructions specify objects by multiple properties (black end table, white vase, purple ottoman). The color_label, product-attribute-value, and other descriptor groups exist in the glossary. The activity TERM cannot capture these as parameters, and there is no general property/descriptor constructor.
- Proposed record: `{"symbol": "object_descriptor", "kind": "constructor", "signature": "TERM object_descriptor(target: STRING / TERM, property: STRING, value: STRING / ATOM[color_label] / ATOM[product-attribute-value] / NUMBER) -> TERM", "definition": "Attaches a property descriptor to an object. Common properties are color, size, material, condition. Does not assert; purely descriptive. Value may reference color_label for visual color, product-attribute-value for product market facets, or a free string for other properties.", "not": "not a constraint or assertion about the object; not a modification", "aliases": ["property_descriptor", "object_property", "qualified_object"]}`

### S3 | type: refine | dimension: refine-entry | target: v19/value/ottoman

- Needs: n3 (t1:s1), n21 (t2:s6), n26 (t2:s8)
- Searches tried: 
  - Ottoman not found in glossary entity-name or location-name values
  - Candidates returned "chair" (explicitly excludes ottoman/sofa), so ottoman is distinct from chair
  - Ottoman is a common furniture object in domestic instructions, essential for this item

- Before: (ottoman not in glossary)
- After: Add ottoman to entity-name values
- Justification: Ottoman is a distinct furniture object (different from chair, bed, desk, dresser, shelf). It is used in this item three times and is common in household environments. The glossary includes many entity-name furniture values (chair, desk, dresser, shelf, etc.) but excludes ottoman.
- Affected uses: n3, n21, n26 in this item; potential future items describing furniture arrangement
- Compatibility: Adding ottoman to entity-name values has no negative impact; it does not conflict with existing values
- Proposed record: `{"symbol": "ottoman", "kind": "value", "category": "entity-name", "definition": "A low upholstered seat or footstool, typically without a backrest.", "not": "not a chair (which has a backrest), not a bed, not a general seating surface", "aliases": ["footstool", "ottoman_seat"]}`

### S4 | type: refine | dimension: refine-entry | target: v19/value/couch

- Needs: n10 (t2:s2)
- Searches tried:
  - Couch candidates returned "chair" (explicitly excludes sofa), but couch and sofa are the same or very similar
  - Couch/sofa is a common furniture object, needed to identify spatial relations in this item
  
- Before: (couch not in glossary; chair explicitly excludes sofa)
- After: Add couch to entity-name values (as sofa/couch alias)
- Justification: The item refers to "couch" as a spatial reference. Chair explicitly excludes sofa. Couch/sofa is a standard household furniture item.
- Affected uses: n10 in this item
- Compatibility: Adding couch as a distinct entity-name (or as an alias for sofa, if sofa is added) does not conflict
- Proposed record: `{"symbol": "couch", "kind": "value", "category": "entity-name", "definition": "A large upholstered sofa for seating multiple people.", "not": "not a chair (which seats one), not a bed", "aliases": ["sofa"]}`



