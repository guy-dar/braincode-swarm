Status: failed
Mode: REQUEST

## Suggested translation

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM subject(kind="DataFrame instances", qualifier=platform_label::pandas) -> subject_2 : TERM
    TERM code_entity(kind="class", name="DataFrame", project=platform_label::pandas) -> code_entity_2 : TERM
    TERM code_entity(kind="method", name="__nonzero__", project=platform_label::pandas) -> code_entity_3 : TERM
    TERM requirement(property="implementation", value=code_entity_3) -> requirement_2 : TERM
    TERM chg_modify_code(target=platform_label::pandas, file="pandas/core/frame.py", revision=requirement_2) -> chg_modify_code_2 : TERM
    CLAIM request(target=chg_modify_code_2) BY user STATUS asserted SOURCE "t1:s1" -> request_2 : CLAIM
    TERM boolean_context_empty_test(subject=subject_2) -> boolean_context_empty_test_2 : TERM  # PROPOSED: S1
    CLAIM enables(condition=chg_modify_code_2, outcome=boolean_context_empty_test_2) BY user STATUS hypothesized SOURCE "t1:s2" -> enables_2 : CLAIM  # PROPOSED: S1
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM requirement(property="modified", value=TRUE) -> requirement_3 : TERM
    TERM chg_modify_code(target=platform_label::pandas, file="RELEASE.rst", revision=requirement_3) -> chg_modify_code_3 : TERM
    UTTER propose(target=chg_modify_code_3)
    TERM chg_modify_code(target=platform_label::pandas, file="doc/source/v0.11.1.txt", revision=requirement_3) -> chg_modify_code_4 : TERM
    UTTER propose(target=chg_modify_code_4)
    TERM chg_modify_code(target=platform_label::pandas, file="pandas/core/frame.py", revision=requirement_3) -> chg_modify_code_5 : TERM
    UTTER propose(target=chg_modify_code_5)
    TERM chg_modify_code(target=platform_label::pandas, file="pandas/core/generic.py", revision=requirement_3) -> chg_modify_code_6 : TERM
    UTTER propose(target=chg_modify_code_6)
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | speech_act | request, chg_modify_code | covered |
| n2 | action | chg_modify_code, requirement | covered |
| n3 | object | code_entity | covered |
| n4 | object | subject, code_entity | covered |
| n5 | action | boolean_context_empty_test (PROPOSED: S1) | proposed |
| n6 | constraint | boolean_context_empty_test (PROPOSED: S1) | proposed |
| n7 | claim | enables, boolean_context_empty_test (PROPOSED: S1) | proposed |
| n8 | action | chg_modify_code, propose | covered |
| n9 | object | chg_modify_code | covered |
| n10 | action | chg_modify_code, propose | covered |
| n11 | object | chg_modify_code | covered |
| n12 | action | chg_modify_code, propose | covered |
| n13 | object | chg_modify_code | covered |
| n14 | object | platform_label::pandas | label-preserved |
| n15 | action | chg_modify_code, propose | covered |
| n16 | object | chg_modify_code | covered |

## Why the translation failed

- n5, n6, n7 (t1:s2): `widen "test whether DataFrame is empty or not as a boolean" --kind constraint` returned `state_empty`, `test_condition`, and `run_tests`, among other candidates. `state_empty` describes an empty/used-up state and is not a DataFrame emptiness test; `test_condition` takes an opaque condition string and expected Boolean, so it cannot formally express this subject-specific boolean-context behavior. `search "boolean test empty DataFrame truthiness"` likewise found `test_condition`, `state_empty`, and general test entries, but no suitable constructor. Proposed S1 supplies the missing structured meaning. `enables` fits the source's hypothetical enabling relation, but its outcome requires S1.

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: t1:s1 and t1:s2 are represented; t2:s2, t2:s4, t2:s6, and t2:s8 are represented as proposed modifications, not completed operations. The t2:s1, t2:s3, t2:s5, and t2:s7 numerals only enumerate the following list items.
- Opaque-text spans: none
- Label-preserved spans: t1:s2 — `pandas` → `platform_label::pandas` (open platform label; no version or other platform properties inferred)
- Missing constructs: S1, a structured TERM for testing whether a subject is empty in a boolean context
- Unresolved ambiguities: t1:s2 does not specify which Boolean value corresponds to emptiness; the translation preserves the capability to test emptiness without choosing a polarity or asserting implementation behavior.
- Check: `node /kit/rag.mjs check --translation /output/translation.md` reports S1's `boolean_context_empty_test` as not in the pinned glossary and n14 as covered by an open-group label; it reports n3, n4, n5, n6, n13, and n16 as DECL (the generic code-entity/subject and proposed emptiness meanings are represented, but the checker does not count those as fully matched need coverage). The translation remains failed because S1 is not accepted vocabulary.
