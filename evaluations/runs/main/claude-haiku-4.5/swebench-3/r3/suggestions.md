# Suggestions from translator swebench-3-r3

## Summary

The translation is incomplete because the glossary lacks operations/constructors to properly represent three key aspects of the issue:
1. File manipulation (creating and modifying files as discrete operations)
2. Package installation operations
3. Proper representation of negation/non-reproducibility

Three suggestions are proposed below.

---

### S1 | type: add | dimension: constructor | symbol: code_file_operation

- Needs: n14 (t1:s15), n15 (t1:s17), n19 (t1:s19)
- Searches tried: "create file" → no file creation operation; "file creation" → only `code_entity` (describes entities, doesn't modify); "add line to file" → no operation exists
- Typed parameters: action: STRING, file: STRING, content?: STRING
- Interpretation: Describes an intended file operation (create, append line, write) without executing it. action is one of "create", "append_line", "write"; content is optional. This is a pure TERM constructor asserting nothing.
- Example: `TERM code_file_operation(action="create", file="test.py") -> file_create_1 : TERM`
- Proposed record: `{"symbol": "code_file_operation", "kind": "constructor", "signature": "TERM code_file_operation(action: STRING, file: STRING, content?: STRING) -> TERM", "definition": "Describes an intended file system operation on a code file (create, append line, write content) without executing it. action is create, append_line, or write.", "not": "an executed file operation or a runtime file reference", "aliases": ["file_modification", "file_action"]}`

### S2 | type: add | dimension: constructor | symbol: package_installation

- Needs: n17 (t1:s19)
- Searches tried: "install package using pip" → only `software_version` (version descriptor, not install action); "package installation" → no install operation; "pip install" → no operation accepts pip as a target
- Typed parameters: package: STRING, version?: STRING, manager: STRING / ATOM[platform_label]
- Interpretation: Describes an intended package installation step (via pip, npm, apt, etc.) without executing it. manager is the package manager (pip, npm, apt); package is the package name; version is optional. Pure TERM, asserts nothing.
- Example: `TERM package_installation(package="pytest", version="3.9.1", manager=platform_label::pip) -> install_pytest : TERM`
- Proposed record: `{"symbol": "package_installation", "kind": "constructor", "signature": "TERM package_installation(package: STRING, version?: STRING, manager: STRING / ATOM[platform_label]) -> TERM", "definition": "Describes an intended package installation or update step (e.g., via pip, npm, apt) without executing it. package is the package name; version is optional; manager is the package manager tool.", "not": "an executed installation or a runtime package environment", "aliases": ["install_package", "package_install"]}`

### S3 | type: add | dimension: vocabulary-member | symbol: not_reproducible

- Needs: n22 (t1:s24)
- Searches tried: "warning could not be reproduced" → only generic `statement()` or `warning` with no negation; "non-reproducible" → no negation claim; "failed to reproduce" → no relation for reproducibility failure
- Typed signature: CLAIM not_reproducible(target: TERM / CLAIM)
- Interpretation: Asserts that the described event, condition, or bug cannot be directly reproduced in the stated context. Typically used with STATUS hypothesized or observed when reproduction was attempted but failed.
- Example: `CLAIM not_reproducible(target=warning_condition) BY user STATUS observed SOURCE "t1:s24" -> not_repro : CLAIM`
- Proposed record: `{"symbol": "not_reproducible", "kind": "claim_relation", "signature": "CLAIM not_reproducible(target: TERM / CLAIM) -> CLAIM", "definition": "Asserts that the target event, condition, or behavior cannot be directly reproduced or observed in the stated context or environment.", "not": "absence of an entity (use exclude for requirements)", "aliases": ["cannot_reproduce", "irreproducible"]}`

---

## Affected uses

- S1 would enable proper encoding of n14 ("Create file test.py") and n15 ("Add import statement...") as `code_file_operation` TERMs with specific actions
- S2 would enable proper encoding of n17 ("Install pytest version 3.9.1 using pip") as a `package_installation` TERM
- S3 would enable proper encoding of n22 ("Warning could not be reproduced directly in the shell") as a `not_reproducible` CLAIM

## Compatibility

- S1 and S2 are compositional constructors (TERM) that would pair well with UTTER inform() to describe reproduction steps in a TRACE conversation
- S3 is a claim relation that completes the "can / cannot be observed" distinction already partially supported by `warning` and other claim relations
- No existing symbols would be deprecated; these are pure additions
