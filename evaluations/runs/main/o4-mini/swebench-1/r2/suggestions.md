### S1 | type: add | dimension: constructor | symbol: code_error_context
- Needs: n5 (t1:s4)
- Searches tried: "source file modeling_convbert.py line 833" → location_spec (too general), code_entity (no line); widen "code context with file and line" → nothing
- Typed parameters: file: STRING, line: NUMBER
- Interpretation: describes the context of a code location identified by file and line number; asserts nothing.
- Example: TERM code_error_context(file="modeling_convbert.py", line=833) -> error_context_2 : TERM
- Proposed record: {"symbol":"code_error_context","kind":"constructor","signature":"TERM code_error_context(file: STRING, line: NUMBER) -> TERM","definition":"Describes the context of a code location identified by file and line number.","not":"A runtime exception or error event","aliases":["code_location","file_line"]}

### S2 | type: add | dimension: constructor | symbol: method_call
- Needs: n4 (t1:s3)
- Searches tried: "call forward method passing only input_embeds argument" → apply_filters (UI filter), click (no), CALL (requires Task); widen "method invocation as a term" → nothing
- Typed parameters: instance: TERM, method: STRING, args: LIST[STRING]
- Interpretation: describes the invocation of a method on an object instance with specified arguments; asserts nothing.
- Example: TERM method_call(instance=code_entity(project=platform_label::transformers,kind="model",name="ConvBertForTokenClassification"),method="forward",args=["input_embeds"]) -> call_forward_2 : TERM
- Proposed record: {"symbol":"method_call","kind":"constructor","signature":"TERM method_call(instance: TERM, method: STRING, args: LIST[STRING]) -> TERM","definition":"Describes the invocation of a method on an object instance with specified arguments.","not":"An executed runtime action or CLAIM","aliases":["invoke_method","call_method"]}

### S3 | type: add | dimension: constructor | symbol: maintainers_list
- Needs: n10 (t1:s22)
- Searches tried: "requested maintainers ArthurZucker and younesbelkada" → maintainers (no), list (no), widen "list of maintainers term" → nothing
- Typed parameters: names: LIST[STRING]
- Interpretation: describes a list of code maintainers identified by their usernames; asserts nothing.
- Example: TERM maintainers_list(names=["ArthurZucker","younesbelkada"]) -> maintainers_list_2 : TERM
- Proposed record: {"symbol":"maintainers_list","kind":"constructor","signature":"TERM maintainers_list(names: LIST[STRING]) -> TERM","definition":"A list of code maintainers identified by their usernames.","not":"A claim of assignment or permission","aliases":["maintainers"]}

### S4 | type: add | dimension: constructor | symbol: instruct_modify_code
- Needs: n16 (t2:s2)
- Searches tried: "modify src/transformers/models/convbert/modeling_convbert.py" → modify_code (ACTION only), chg_modify_code (TERM for change spec needs revision), widen "instruct to modify code" → nothing
- Typed parameters: file: STRING
- Interpretation: describes an instruction to modify the specified code file; asserts nothing.
- Example: TERM instruct_modify_code(file="src/transformers/models/convbert/modeling_convbert.py") -> instruct_modify_2 : TERM
- Proposed record: {"symbol":"instruct_modify_code","kind":"constructor","signature":"TERM instruct_modify_code(file: STRING) -> TERM","definition":"Describes an instruction to modify the specified code file.","not":"An actual modify_code operation","aliases":["instruction_modify_source"]}