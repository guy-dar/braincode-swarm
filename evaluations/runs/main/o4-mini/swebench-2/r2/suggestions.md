### S1 | type: add | dimension: constructor | symbol: implement_method
- Needs: n2 (t1:s1), n3 (t1:s1), n4 (t1:s2)
- Searches tried: "implement method in class" → no matching constructor; widen → nothing relevant
- Typed parameters: class: STRING / TERM, method: STRING
- Interpretation: Describes the action of implementing a specified method in the given class; asserts nothing by itself.
- Example: `TERM implement_method(class=subject(kind="class", qualifier="DataFrame", project=platform_label::pandas), method="__nonzero__") -> implement_method_2 : TERM`
- Proposed record: {"symbol": "implement_method", "kind": "constructor", "signature": "TERM implement_method(class: STRING / TERM, method: STRING) -> TERM", "definition": "Describes the action of installing or defining the specified method in the given class; asserts nothing.", "not": "A test or execution of the method (use ACTION modify_code or test_condition)", "aliases": ["implement method", "add method"]}