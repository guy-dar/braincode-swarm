### S1 | type: add | dimension: lexical-group | symbol: airline_label
- Needs: n7 (t1:s1)
- Searches tried: "United Airlines" → no airline-specific group; widen "airline name label" → nothing
- Definition: A source-supplied airline name label; denotes that carrier without implied code or properties.
- admission: open_label
- key_form: lower_word
- key_aliases: {}
- Consuming signatures: slots accepting ATOM[airline_label] for string-valued slots where atomic carrier names appear.
- Illustrative values: ["airline_label::united_airlines"]
- Proposed record: {"symbol":"airline_label","kind":"lexical_group","definition":"A source-supplied airline name label; denotes that carrier without implied code or properties.","group":{"examples":["airline_label::united_airlines"]}}