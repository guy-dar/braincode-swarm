Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM greeting() -> greeting_2 : TERM # REFINED: S6
    TERM code_entity(file="models.convbert", kind="model class", name="ConvBertForTokenClassification", project=platform_label::transformers) -> code_entity_2 : TERM
    TERM code_entity(file="modeling_convbert.py:833", kind="source location", name="line 833", project=platform_label::transformers) -> code_entity_3 : TERM
    CLAIM raises_exception(target=code_entity_2, exception_type="UnboundLocalError", message="local variable 'seq_length' referenced before assignment") BY role_user STATUS reported SOURCE "t1:s1" -> raises_exception_2 : CLAIM
    UTTER inform(target=raises_exception_2)
    TERM code_branch(condition="input_ids is not None", statements=["input_shape = input_ids.size()", "batch_size, seq_length = input_shape"], unassigned=[]) -> code_branch_2 : TERM # PROPOSED: S1
    TERM code_branch(condition="inputs_embeds is not None", statements=["input_shape = inputs_embeds.size()[:-1]"], unassigned=["batch_size", "seq_length"]) -> code_branch_3 : TERM # PROPOSED: S1
    TERM code_branch(condition="token_type_ids is None", statements=["if hasattr(self.embeddings, \"token_type_ids\"):", "buffered_token_type_ids = self.embeddings.token_type_ids[:, :seq_length]"], unassigned=[]) -> code_branch_4 : TERM # PROPOSED: S1
    TERM code_invocation(target=code_entity_2, arguments=["input_embeds"], method="forward") -> code_invocation_2 : TERM # PROPOSED: S2
    TERM code_invocation(target=code_entity_2, arguments=["inputs_embeds", "attention_mask"], method="forward") -> code_invocation_3 : TERM # PROPOSED: S2
    TERM subject(kind="diagnostic question subject", qualifier=code_branch_3) -> subject_2 : TERM
    TERM subject(kind="candidate explanation", qualifier="missing batch_size and seq_length unpacking in inputs_embeds branch") -> subject_3 : TERM
    TERM subject(kind="candidate explanation", qualifier="incorrect model usage") -> subject_4 : TERM
    TERM diagnostic_question(alternatives=[subject_3, subject_4], subject=subject_2) -> diagnostic_question_2 : TERM # PROPOSED: S3
    UTTER ask(target=diagnostic_question_2)
    TERM test_condition(condition="model_forward_raises_UnboundLocalError", expected=FALSE) -> test_condition_2 : TERM
    TERM subject(kind="maintainer", qualifier="ArthurZucker") -> subject_5 : TERM
    TERM subject(kind="maintainer", qualifier="younesbelkada") -> subject_6 : TERM
    CLAIM potential_helper(person=subject_5) BY role_user STATUS reported SOURCE "t1:s22" -> potential_helper_2 : CLAIM # PROPOSED: S5
    CLAIM potential_helper(person=subject_6) BY role_user STATUS reported SOURCE "t1:s22" -> potential_helper_3 : CLAIM # PROPOSED: S5
    TERM subject(kind="script selection", qualifier="my own modified scripts") -> subject_7 : TERM
    TERM subject(kind="script selection", qualifier="official example scripts") -> subject_8 : TERM
    CLAIM selected_context(context=subject_7, selection="selected") BY role_user STATUS reported SOURCE "t1:s25" -> selected_context_2 : CLAIM # PROPOSED: S4
    CLAIM selected_context(context=subject_8, selection="not_selected") BY role_user STATUS reported SOURCE "t1:s24" -> selected_context_3 : CLAIM # PROPOSED: S4
    TERM subject(kind="task or dataset selection", qualifier="my own task or dataset") -> subject_9 : TERM
    TERM subject(kind="task or dataset selection", qualifier="officially supported task in the examples folder") -> subject_10 : TERM
    CLAIM selected_context(context=subject_9, selection="selected") BY role_user STATUS reported SOURCE "t1:s28" -> selected_context_4 : CLAIM # PROPOSED: S4
    CLAIM selected_context(context=subject_10, selection="not_selected") BY role_user STATUS reported SOURCE "t1:s27" -> selected_context_5 : CLAIM # PROPOSED: S4
  }
  TURN t2 SPEAKER=AGENT REPLY_TO t1 {
    TERM code_entity(file="src/transformers/models/convbert/modeling_convbert.py", kind="source file", name="modeling_convbert.py", project=platform_label::transformers) -> code_entity_4 : TERM
    TERM activity(verb="modify", object=code_entity_4) -> activity_2 : TERM
    CLAIM request(target=activity_2) BY role_agent STATUS reported SOURCE "t2:s2" -> request_2 : CLAIM
  }
}
```

## Needs coverage

| need | kind | expressed by | status |
|---|---|---|---|
| n1 | claim | raises_exception | covered |
| n2 | speech_act | greeting, inform, raises_exception | proposed |
| n3 | object | code_entity, platform_label::transformers | label-preserved |
| n4 | action | code_invocation | proposed |
| n5 | object | code_entity | covered |
| n6 | claim | code_branch | proposed |
| n7 | claim | code_branch, raises_exception | proposed |
| n8 | claim | code_branch | proposed |
| n9 | speech_act | diagnostic_question, ask | proposed |
| n10 | object | potential_helper, subject | proposed |
| n11 | claim | selected_context, subject | proposed |
| n12 | claim | selected_context, subject | proposed |
| n13 | action | code_invocation | proposed |
| n14 | constraint | test_condition | covered |
| n15 | negation | test_condition | covered |
| n16 | action | request, activity, code_entity | unresolved |
| n17 | object | platform_label::transformers | covered |

## Why the translation failed

- n2 "greet and report an issue": the report is represented by the reported exception claim and inform speech act. The only retrieved greeting constructor requires a recipient, which the source does not specify; refine it to permit an omitted recipient (S6).
- n4/n13 "call forward with input_embeds" and reproduce using `inputs_embeds` and `attention_mask`: widened searches for invoking a model method with named arguments returned general activity/operation candidates, but none describes a software method invocation and its argument names. `activity` does not represent call arguments; S2 proposes `code_invocation`.
- n6/n7/n8 code facts about the `token_type_ids` slicing and `inputs_embeds` branch: widened searches for conditional code assignments and unassigned variables returned no fitting code-flow vocabulary. `state_sliced` is a state label, not the code operation, and `calculation` does not describe assignment or control flow. S1 proposes a structured code branch term preserving conditions, statements, and unassigned identifiers.
- n9 asks whether the missing unpacking is a bug or misuse: `ask` requires a sufficiently precise TERM target, and no retrieved constructor represents this diagnostic question with its alternatives. S3 proposes that constructor; `subject` alone cannot encode the question relation.
- n10 names ArthurZucker and younesbelkada as possible helpers. `subject` can preserve the names but does not assert their role as potential helpers. S5 adds that claim relation.
- n11/n12 checked selections distinguish own modified scripts/task or dataset from official examples/benchmarks. Searches returned `example_of`, `user_practice`, and `run_tests`, whose meanings do not represent the checked selection state. S4 adds a claim relation for explicitly selected or unselected source context.
- n16 asks for modification of the named file. In TRACE, `modify_code` is an effectful REQUEST operation and cannot be recorded as completed without evidence; `request` with a descriptive `activity` preserves the stated request, but `rag check` did not recognize it as covering the action need. No specific patch is supplied, so no revision is invented. Keep n16 unresolved for the checker/migrator.

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: t1:s1–t1:s32 and t2:s1–t2:s2 represented, subject to the proposed code-flow, invocation, diagnostic-question, selection and helper vocabulary noted above; n16 remains unresolved by the checker. The empty System Info heading (t1:s2) contributes no semantic content.
- Opaque-text spans: none. Exact code identifiers, diagnostic wording, and argument names are retained as literal strings because they are objects of the source's code analysis.
- Label-preserved spans: t1:s3 — `transformers` → `platform_label::transformers` (open-group label); exact model class name is also retained in the `code_entity` term.
- Missing constructs: S1 code branch/assignment-state description; S2 code method invocation; S3 diagnostic question with alternatives; S4 selected-context claim relation; S5 potential-helper claim relation; S6 optional greeting recipient.
- Unresolved ambiguities: the source does not identify the greeting recipient; S6 retains this without guessing. It asks whether the issue is a code bug or misuse and does not resolve that question. The source's checked boxes identify its own modified scripts and own task/dataset, but do not give further details.
- Check: `node /kit/rag.mjs check --translation /output/translation.md` reported proposed identifiers missing from the current glossary (`code_branch`, `code_invocation`, `diagnostic_question`, `potential_helper`, `selected_context`), unbound-value warnings for code identifiers inside proposed code-branch strings (`input_ids`, `input_shape`, `inputs_embeds`, `self`), declared/unresolved needs n7, n11, n12, n13 and n16, and label-preserved n3. These are not a successful validation; the proposed code-branch signature is needed for its string fields to be interpreted.
