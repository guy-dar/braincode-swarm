### S1 | type: refine | dimension: refine-entry | target: chg_modify_code
- Needs: n24 (t2:s2), n25 (t2:s4), n26 (t2:s6), n27 (t2:s8), n28 (t2:s10), n29 (t2:s12)
- Searches tried: `rag entry chg_modify_code` shows `revision: TERM` only; `rag widen "revision as text"` yields nothing
- Before: signature `TERM chg_modify_code(target: STRING / ATOM[platform_label], file: STRING / TERM, revision: TERM) -> TERM`
- After: allow revision to be a simple STRING or TERM
- Justification: most code-change descriptions are naturally a short text description; forcing a TERM wrapper requires inventing new constructors per case
- Proposed record:  
  `{"signature":"TERM chg_modify_code(target: STRING / ATOM[platform_label], file: STRING / TERM, revision: TERM / STRING) -> TERM"}`

### S2 | type: add | dimension: constructor | symbol: system_warning
- Needs: n1 (t1:s1)
- Searches tried: `rag search "system warning"` finds only the generic warning relation, which lacks a `system:` parameter
- Typed parameters: system: TERM, message: STRING
- Interpretation: a warning emitted by a specified system (e.g. the Python interpreter); asserts no error
- Example:  
  `TERM system_warning(system=subject(kind="interpreter", qualifier=platform_label::python), message="Deprecated import") -> system_warning_2 : TERM`
- Proposed record:  
  `{"symbol":"system_warning","kind":"constructor","signature":"TERM system_warning(system: TERM, message: STRING) -> TERM","definition":"A warning emitted by a specified system; does not assert an error.","not":"an exception or error (use raises_exception)","aliases":["runtime_warning"]}`
