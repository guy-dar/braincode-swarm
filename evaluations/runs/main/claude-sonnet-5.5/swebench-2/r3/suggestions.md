### S1 | type: refine | dimension: refine-entry | target: v19/constructor/chg_modify_code
- Needs: n8 (t2:s2), n10 (t2:s4), n12 (t2:s6), n15 (t2:s8)
- Searches tried: "modify file" → modify_code, chg_modify_code (both require revision); "describe change to file" → policy_revision_request, substitute (wrong domain)
- Before: revision: TERM required
- After: revision?: TERM optional; omitted means the change content is unspecified
- Justification: sources may name files to modify without stating the change; a required revision forces fabrication.
- Affected uses: none lost; existing calls remain valid
- Compatibility: backward compatible
- Proposed record: `{"signature": "TERM chg_modify_code(target: STRING / ATOM[platform_label], file: STRING / TERM, revision?: TERM) -> TERM"}`
