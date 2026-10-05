### S1 | type: add | dimension: constructor | symbol: inscribed_text
- Needs: n13 (t2:s4)
- Searches tried: "title" → document_section, art_short_text; "book title" → textbook, document_section; "inscribed" → pen, pencil; widen "the book that says Probabilistic Robotics" → no constructor for item title or inscribed text
- Typed parameters: target?: STRING / TERM / ATOM[object_label], text: STRING
- Interpretation: constructs a descriptive representation of text, title, or inscription appearing on an object or publication; asserts nothing.
- Example: `TERM inscribed_text(target=textbook, text="Probabilistic Robotics") -> inscribed_text_2 : TERM`
- Proposed record: {"symbol": "inscribed_text", "kind": "constructor", "signature": "TERM inscribed_text(text: STRING, target?: STRING / TERM / ATOM[object_label]) -> TERM", "definition": "Constructs a descriptive representation of text, title, or inscription appearing on an object or publication.", "not": "document_section (which describes sections of structured document artifacts) or type_text (an action entering text into a UI input field)", "aliases": ["titled", "title", "inscribed", "says"]}
