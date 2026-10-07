### S1 | type: add | dimension: vocabulary-member | symbol: texture_rough
- Needs: n4 (t1:s2), n37 (t1:s11), n47 (t1:s15), n52 (t1:s19), n53 (t1:s20)
- Searches tried: search "rough" "texture" -> state_dirty, spatula, mattress, aesthetic; widen "rough" --kind constraint -> state_dirty, shape_oval, dom_pain
- Meaning: A coarse, uneven, or rough physical surface texture.
- Category: descriptive-value
- Contextual aliases: rough, coarse, uneven
- Example: `TERM requirement(property="texture", value=texture_rough) -> rough_prop : TERM`
- Contrast: state_dirty (cleanliness condition) or shape_oval (geometric shape)
- Proposed record: {"symbol": "texture_rough", "kind": "value", "category": "descriptive-value", "definition": "A coarse, uneven, or rough physical surface texture.", "not": "state_dirty (environmental cleanliness condition) or shape_oval (geometric shape)", "aliases": ["rough", "coarse", "uneven"]}

### S2 | type: add | dimension: constructor | symbol: likes
- Needs: n8 (t1:s3), n41 (t1:s12), n45 (t1:s13), n49 (t1:s16), n50 (t1:s17), n54 (t1:s21)
- Searches tried: search "likes" "affinity" -> has_style, style_narrative, similarity; widen "likes" --kind action -> has_style, comfortable, well_wishes
- Typed parameters: actor: STRING / TERM / ATOM[animal_label], target: STRING / TERM / ATOM[animal_label]
- Interpretation: Constructs a descriptive term representing an actor having affinity or affection for a target entity; describes, asserts nothing.
- Example: `TERM likes(actor=animal_label::baldeagle, target=animal_label::dog) -> likes_2 : TERM`
- Proposed record: {"symbol": "likes", "kind": "constructor", "signature": "TERM likes(actor: STRING / TERM / ATOM[animal_label], target: STRING / TERM / ATOM[animal_label]) -> TERM", "definition": "Constructs a descriptive term representing an actor having affinity, fondness, or affection for a target entity.", "not": "interpersonal_stance (relational commitment in human relationships) or comfortable (affective physical/situational comfort claim)", "aliases": ["likes", "fond_of", "affinity_for"]}

### S3 | type: add | dimension: constructor | symbol: visits
- Needs: n12 (t1:s4), n16 (t1:s5), n20 (t1:s6), n30 (t1:s9), n61 (t1:s23)
- Searches tried: search "visits" -> search_travel, look, walk; widen "visits" --kind action -> search_travel, role_daughter, art_itinerary
- Typed parameters: host: STRING / TERM / ATOM[animal_label], visitor: STRING / TERM / ATOM[animal_label]
- Interpretation: Constructs a descriptive term representing a visitor entity visiting a host entity; describes, asserts nothing.
- Example: `TERM visits(host=animal_label::dog, visitor=animal_label::baldeagle) -> visits_2 : TERM`
- Proposed record: {"symbol": "visits", "kind": "constructor", "signature": "TERM visits(host: STRING / TERM / ATOM[animal_label], visitor: STRING / TERM / ATOM[animal_label]) -> TERM", "definition": "Constructs a descriptive term representing a visitor going to see or spend time with a host entity.", "not": "search_travel (external travel querying operation) or walk (physical locomotion toward a landmark)", "aliases": ["visits", "pays_visit_to", "calls_on"]}

### S4 | type: add | dimension: constructor | symbol: eats
- Needs: n34 (t1:s10), n46 (t1:s14)
- Searches tried: search "eats" "consume" -> spoon, slice, bread, plate; widen "eats" --kind action -> spoon, slice, meat, state_sliced
- Typed parameters: consumer: STRING / TERM / ATOM[animal_label], food: STRING / TERM / ATOM[animal_label]
- Interpretation: Constructs a descriptive term representing a consumer entity consuming a food or target entity; describes, asserts nothing.
- Example: `TERM eats(consumer=animal_label::rabbit, food=animal_label::baldeagle) -> eats_2 : TERM`
- Proposed record: {"symbol": "eats", "kind": "constructor", "signature": "TERM eats(consumer: STRING / TERM / ATOM[animal_label], food: STRING / TERM / ATOM[animal_label]) -> TERM", "definition": "Constructs a descriptive term representing an organism consuming or eating a target entity as food.", "not": "slice (food preparation cutting operation) or spoon (utensil entity)", "aliases": ["eats", "consumes", "devours", "preys_on"]}
