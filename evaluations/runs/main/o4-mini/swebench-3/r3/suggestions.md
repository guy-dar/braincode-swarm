### S1 | type: add | dimension: vocabulary-member | symbol: log_entry
- Needs: n2 (t1:s2), n3 (t1:s3), n4 (t1:s4), n5 (t1:s5), n6 (t1:s6), n7 (t1:s7), n8 (t1:s8), n9 (t1:s9), n10 (t1:s10), n11 (t1:s11), n12 (t1:s12), n13 (t1:s13), n14 (t1:s14), n15 (t1:s15), n16 (t1:s16), n17 (t1:s17), n18 (t1:s18), n19 (t1:s19), n20 (t1:s20), n21 (t1:s21), n22 (t1:s22), n23 (t1:s23), n24 (t1:s24), n25 (t2:s1), n26 (t2:s2), n27 (t2:s3), n28 (t2:s4), n29 (t2:s5), n30 (t2:s6), n31 (t2:s7), n32 (t2:s8), n33 (t2:s9), n34 (t2:s10), n35 (t2:s11), n36 (t2:s12)
- Searches tried:
  • `node /kit/rag.mjs search "log entry"` → no matching speech_act
  • `node /kit/rag.mjs widen "transcript line"` → no results
- Meaning: record a raw transcript or log line by its source locator, without carrying or asserting the text itself
- Aliases: ["transcript_line"]
- Example: `UTTER log_entry(source="t1:s1")`
- Proposed record:
  {"symbol":"log_entry","kind":"speech_act","signature":"UTTER log_entry(source: STRING)","definition":"Record a raw transcript or log line by its source locator; asserts nothing and does not carry text.","aliases":["transcript_line"]}