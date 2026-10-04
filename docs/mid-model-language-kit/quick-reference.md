# Verbatim quick reference

This is an incomplete excerpt of language-spec.md, not a replacement or a revised specification. Read the full relevant sections for construct semantics, claims, evidence, constraints and examples. The following three sections are copied without edits.

## 2. Language release and document modes

A language release consists of this specification, a compatible glossary with exact signatures and definitions, and verified examples. Every translation identifies the release in its external metadata. Evaluation freezes all three components.

Every document begins with exactly one `MODE` and one `ENTRYPOINT`:

```ebnf
document     ::= "MODE" mode "ENTRYPOINT" IDENT definition+
mode         ::= "REQUEST" | "TRACE"
definition   ::= task | conversation
```

The entrypoint names exactly one Task or Conversation in the document. Definitions have unique names. Referenced task definitions must exist. Parsing or reading a BrainCode document never authorizes external execution.

### REQUEST

Represents requested behavior or an explicitly proposed plan. `ACTION`, `GENERATE`, and `CALL` describe work to be performed; they do not claim it has already happened. A request does not contain fabricated results or an answer unavailable in its source.

### TRACE

Represents supplied messages and observed behavior. External operations are recorded using `RECORD`, not executed. Requested or recommended work inside a trace is represented by speech acts and structured terms, not falsely recorded as completed work.

Maintain three distinct meanings whenever they differ:

1. The human's expressed request.
2. The agent's interpretation of that request.
3. The agent's actions and outcomes.

An agent's misunderstanding never overwrites the original request. The source may be incomplete; record that limitation instead of reconstructing hidden deliberation.


## 3. Lexicon, types, and binding

```ebnf
type         ::= "NUMBER" | "STRING" | "BOOL" | "TERM" | "CLAIM" | "EVENT"
               | "LIST" "[" type "]" | "REF" "[" type "]"
value        ::= STRING | NUMBER | "TRUE" | "FALSE" | name | list_lit | diff
name         ::= IDENT | IDENT "." IDENT
list_lit     ::= "[" (value ("," value)*)? "]"
diff         ::= IDENT "-" NUMBER
IDENT        ::= [a-zA-Z_][a-zA-Z0-9_]*
NUMBER       ::= "-"? [0-9]+ ("." [0-9]+)? (("e"|"E") ("+"|"-")? [0-9]+)?
```

Strings use JSON double-quoted escaping. Comments begin with `#` and end at the physical line boundary outside a string. Keywords are case-sensitive. Grammar notation is EBNF; lexical character classes above are regular-expression notation.

Numbers denote finite decimal values; NaN and infinity are not literals. A `diff` requires a NUMBER binding and denotes numeric subtraction. Lists are homogeneous. An empty list obtains its element type from its declared binding or parameter; an empty list without an expected element type is a static error.

Accepted glossary symbols are lexically identifiers and have static type STRING, preserving v18 behavior. Glossary categories impose additional semantic restrictions: a tone symbol cannot fill a recipient field merely because both have type STRING. Every accepted symbol has an explicit definition and category.

New semantic types:

| Type | Meaning |
|---|---|
| `TERM` | A structured concept, description, question target, or constraint; constructing it asserts nothing |
| `CLAIM` | An attributed proposition with an epistemic status and provenance; not a Boolean |
| `EVENT` | A recorded occurrence or attempted operation in a trace; not a runtime object reference |
| `REF[T]` | Identity of a selected runtime object with payload type T; cannot be created from a description string |

Bindings are immutable and cannot shadow a visible name or glossary symbol. LET copies an exactly matching type:

```ebnf
bind         ::= "LET" IDENT ":" type "=" value
attrs        ::= attr ("," attr)*
attr         ::= IDENT "=" value
result       ::= "->" IDENT ":" type
```

Duplicate attributes are errors. There are no implicit conversions, no arbitrary unbound identifiers, and no inline operation or constructor calls inside attribute values. Compose through earlier bindings. Typed result bindings of Action, Generate, and CALL follow the same scope rules as LET.


## 14. Canonical form

Canonicalization is applied after faithful semantic analysis. It may not discard a distinction or choose an interpretation merely because that makes serialization easier.

1. **Root selection:** a single REQUEST message requiring external work uses TASK. Speech-only REQUEST input uses CONVO. Multi-message input and every TRACE use CONVO.
2. **Names:** a Task entrypoint uses PascalCase of the first top-level Action target or Generate target, removing descriptor category prefixes where defined by the glossary. If no such target exists, use `Request`. Conversation entrypoints use `Conversation`. Helper Tasks use their accepted purpose names from the supplied decomposition; unexplained new helpers are reported.
3. **Attributes:** target first when present; all remaining attributes in ASCII alphabetical order. This applies to every call-shaped statement.
4. **Dependency order:** producers precede consumers. Otherwise preserve source-clause order. No reordering of effectful operations merely for alphabetical tidiness.
5. **Handles:** TERM uses its constructor name, CLAIM its relation name, EVENT its operation name plus `_event`. Action REF results use target plus `_ref` or `_refs`; other Action results use the operation name; Generate uses its target; CALL uses its callee name in snake case. Remove accepted category prefixes from target-derived handles. Repeated bases receive `_2`, `_3`, etc. Skip visible vocabulary names to avoid collisions. Loop handles use `item`, with the same collision rule.
6. **Vocabulary selection:** use accepted semantic definitions and category constraints. Aliases normalize to the published canonical symbol. Lexicographic order may break a tie only between aliases of the same meaning, never between different plausible meanings.
7. **Decomposition:** use accepted compositional definitions and operation elaborations. Do not turn every clause into an external action or every concept into an independent symbol.
8. **Reuse:** bind shared semantic content once when holder, context, and meaning are identical. Preserve genuine retries, changed results, and changed beliefs. Do not erase historically distinct events because their attributes match.
9. **Extensions:** unknown meanings become proposals. Remove v18's automatic `custom_general_<predicate>` escape hatch. Non-ASCII or multiword source phrasing is not itself an error; report an actual semantic/vocabulary gap instead.

Canonical equivalence allows local-handle renaming and expansion of accepted aliases/composite definitions. It does not automatically equate reorderings, claims by different holders, different epistemic statuses, or distinct source events. Compare exact canonical match and declared semantic equivalence separately in evaluation.

