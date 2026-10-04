# BrainCode Language Specification

**Version:** 19.0.0-draft.1  

The normative requirements below describe the proposed language, not capabilities of the current swarm or evidence that research KPIs have been achieved.

## 1. Purpose

BrainCode represents human requests and agent reasoning so that another reader can recover what was requested, what was understood, what was done or proposed, what was concluded, and why.

The language must be:

- **Expressive:** preserve meaningful distinctions, including negation, conditions, quantities, time, attribution, uncertainty, and reasoning dependencies.
- **Broad in coverage:** express unfamiliar combinations and domains through reusable composition, with explicit proposals when vocabulary is insufficient.
- **Deterministic in translation:** independent translators should converge on the same canonical representation or a documented semantic equivalence.
- **Interpretable:** a human or model can recover meaning using the encoding and its pinned language release.
- **Independent of incidental style:** encode differences in content and communicative intent, not superficial wording.
- **Economical without loss:** remove redundant representation, never distinct claims or required constraints merely to shorten output.

Execution order is not a substitute for reasoning structure. Naming a topic is not a substitute for expressing a claim. A definition is not evidence that the defined claim is true.

The proposal's coverage, expressivity, determinism, improvement, and interpretability KPIs remain evaluation requirements. This specification supplies a representation; empirical evaluation determines whether it is useful.

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

Accepted glossary symbols are lexically identifiers and have static type STRING. Glossary categories impose additional semantic restrictions: a tone symbol cannot fill a recipient field merely because both have type STRING. Every accepted symbol has an explicit definition and category.

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

## 4. Task and task calls

```ebnf
task         ::= "TASK" IDENT params? context? (":" type)?
                 ("DECREASES" IDENT)? "{" step+ return_stmt? "}"
params       ::= "(" param ("," param)* ")"
param        ::= IDENT ":" type
context      ::= "CONTEXT" "(" attrs ")"
task_call    ::= "CALL" IDENT "(" attrs? ")" result?
return_stmt  ::= "RETURN" value
step         ::= bind | action | generation | task_call | utterance
               | flow_if | flow_for | term | claim | link | record
```

This is the syntactic union of statements. Mode and context restrictions below are static semantic rules. REQUEST Task bodies may contain all statements except RECORD. TRACE documents use Conversation as their entrypoint and cannot execute Task calls or bare Action/Generate statements.

A task's parameters have lexical scope inside that invocation. CALL uses named arguments matching the callee exactly. A task with a declared result type must end with one top-level RETURN of that type; a task without a result type cannot bind or return a value. Early returns are not supported. A result-producing CALL must bind its result with its exact declared type.

For an entrypoint Task, parameters are supplied by an explicitly documented input environment. A translation must not invent parameter values to make a request executable.

CONTEXT permits `execution_date` and `timezone`, both STRING. A relative date requires a supplied or explicitly established calendar anchor. A time-of-day deadline additionally requires a timezone. Do not invent UTC, a deadline hour, or a particular Friday from ambiguous source wording; flag the missing context in the translation report.

### Recursion and termination

An acyclic call graph is preferred. Direct self-recursion is permitted only when:

- The task declares `DECREASES n`, with n a NUMBER parameter constrained at invocation to a nonnegative integer.
- Every self-call is textually inside the THEN branch of `IF n >= k`, where k is a positive integer literal.
- That call passes exactly `n=n-k`, with the same k; all other self-calls are rejected.

Mutual recursion is not supported. Lexical bindings are immutable, so the guard and decrement refer to the same n. A validator can check these restrictions without inferring arbitrary mathematical termination proofs. Finite structural control does not guarantee an external tool returns; runtime adapters still need timeouts.

## 5. Action and reference identity

```ebnf
action       ::= "ACTION" IDENT "(" attrs? ")" result?
```

Action denotes one external operation in REQUEST mode. Its accepted glossary entry defines required and optional attributes, exact result type, effects, failures, and any reference-identity behavior. Pure reasoning and factual claims are not external actions.

Every result-producing Action binds its result. Operations with no result omit the binding. Operations preserving a REF return that same identity, although an immutable new handle may name it. Do not reacquire an object that already has a usable reference.

Operation profile (the glossary supplies complete signatures):

- `search_web` returns `LIST[REF[STRING]]`. Filtering belongs in its governed criteria; ranking is a subsequent `sort`; selection is a subsequent `extract`.
- `extract(limit=1)` still returns a list. A consumer must accept that list or the program must iterate over it; do not silently coerce it to one REF.
- `pick_up` accepts an entity description. Missing quantity or literal 1 returns `REF[STRING]`; a literal integer greater than 1 returns `LIST[REF[STRING]]`. Other quantities require a separately defined signature rather than a runtime-dependent static type.
- `place` requires a REF. `rinse`, `heat`, `chill`, `slice`, and `pour` consume and return the same REF identity.

A glossary may declare an unbound-description-to-reference elaboration such as pick_up before place. Apply it only when the source semantics and operation contract warrant that elaboration. Do not assume a sink, heater, or other resource exists merely to satisfy a signature.

A corrected REQUEST example, assuming the documented mug-operation profile:

```braincode
MODE REQUEST
ENTRYPOINT Mug
TASK Mug {
  ACTION pick_up(target=mug) -> mug_ref : REF[STRING]
  ACTION rinse(target=mug_ref, destination=sink) -> mug_ref_2 : REF[STRING]
  ACTION place(target=mug_ref_2, destination=coffee_maker)
}
```

Here `mug`, `sink`, and `coffee_maker` are accepted glossary descriptors. No string is silently promoted to a runtime reference.

## 6. Generate and artifact meaning

```ebnf
generation   ::= "GENERATE" "(" attrs ")" result
```

GENERATE specifies production of an artifact in REQUEST mode. Its target must be an artifact-category symbol. Supported result types are NUMBER, STRING, BOOL, and finite lists of those types. It does not create EVENT or physical-object REF values.

Core attributes are target, audience, constraints, content, format, locale, style, tone, and topic. `constraints` has type LIST[TERM]; `topic` accepts STRING or TERM; other attributes have type STRING with appropriate glossary-category checks. The expected result type is given by the result binding and must be permitted by the artifact's glossary contract.

Domain-specific attributes are glossary extensions with exact meanings, types, and canonical expansion rules. They are not an ever-growing list of grammar exceptions. Fields such as `duration`, `stop_min_per_day`, and `max_walk_duration` require explicit glossary definitions. A minimum daily stop count alone does not encode that the stops must be temples; the constraint must also identify the class of stop.

When encoding a completed artifact in TRACE mode, recording that generation happened is insufficient. Represent the artifact's substantive properties and conclusions in terms and claims. Retain exact wording separately when that wording is the actual deliverable.

## 7. Utterance and intended meaning

```ebnf
utterance    ::= "UTTER" IDENT "(" attrs ")"
```

UTTER records or describes a speech act in a Conversation turn. It is valid only inside TURN, including nested blocks. It has no external execution effect and no result binding; reference a speech act by its source span or represent its content explicitly.

Legal attributes are audience, constraints, content, recipient, target, tone, and topic. Audience/recipient/tone use governed STRING categories. `constraints` is LIST[TERM]; `target` is TERM or CLAIM; `topic` is STRING or TERM; `content` is STRING under Section 13's limits.

Use a TERM target for a question, request, or described action. Use a CLAIM target for a statement of a proposition. A topic may help locate content but cannot replace distinctions present in the source. Multiple independently scoped speech acts in one message become separate UTTER statements in source order.

An ask about a property should expose the subject and property separately, not require a single glossary symbol for the whole question. Example vocabulary and encodings appear in Section 16.

## 8. Check, Flow-If, Iterate, and scope

```ebnf
check        ::= disjunction
disjunction  ::= conjunction ("OR" conjunction)*
conjunction  ::= negation ("AND" negation)*
negation     ::= "NOT" negation | primary
primary      ::= "(" check ")" | quantifier | comparison
comparison   ::= value (comp_op value)?
comp_op      ::= "==" | "!=" | "<" | "<=" | ">" | ">="
flow_if      ::= "IF" check "THEN" "{" step+ "}"
                 ("ELSE" "{" step+ "}")?
flow_for     ::= "FOR" "EACH" IDENT "IN" iterable "{" step+ "}"
iterable     ::= name | list_lit
quantifier   ::= ("ANY" | "ALL") IDENT "IN" iterable "SATISFIES" check
```

Check is pure. It cannot contain an Action, Generate, CALL, TERM constructor, or CLAIM constructor. Precedence is OR, AND, NOT, then comparison; parentheses override. Evaluation is left-to-right and short-circuiting.

NUMBER and STRING support all comparison operators, with numeric and codepoint ordering respectively. BOOL and LIST support only equality/inequality. List equality is recursive and requires a comparable element type; lists containing TERM, CLAIM, or EVENT are therefore not comparable. Operands must have exactly equal types. REF supports only identity equality/inequality for matching parameter types. TERM, CLAIM, and EVENT cannot be compared by Check; a claim does not become true because it exists or was asserted.

Truthiness: zero, empty strings, FALSE, and empty lists are false. Other values of those four type families are true. REF and the new semantic types have no truthiness. A bare comparison used as a standalone statement is invalid.

IF branches create separate child scopes. FOR iterates over a finite LIST[T] in order, with a fresh child scope and a loop binding of type T per iteration. Bindings do not escape branches or iterations; there is no implicit accumulation. ANY returns false on an empty list; ALL returns true. Quantifier variables are scoped only over their own predicate, and cannot shadow visible names.

Control constructs are legal only in REQUEST mode. A conditional claim, a causal relationship, or a described procedure in a TRACE is semantic content, represented with glossary-defined terms and claims. Do not confuse “if X, Y would follow” with an instruction to execute Y.

## 9. Structured terms and glossary composition

```ebnf
term         ::= "TERM" IDENT "(" attrs? ")" "->" IDENT ":" "TERM"
```

A TERM is an application of an accepted constructor to typed values. Its glossary signature and definition determine its meaning. It neither asserts a fact nor runs an operation. Terms support reusable entities/descriptions, open questions, action descriptions, quantities with units, and constraints.

Constructors must expose meaningful arguments. For example, a property question has a subject and a property; a quantity has a number and unit; a requirement identifies both what is constrained and the condition imposed. Domain-specific composites are permitted when their definitions expand into accepted constructors.

An expression may reference an earlier TERM binding as an argument. Inline nested calls remain banned; compose through explicit bindings.

### Required glossary entry contract

Each accepted entry includes a stable ID, symbol, kind, plain-language meaning, category if applicable, typed signature, semantic restrictions, positive example, distinguishing example, aliases, and status. Constructor/relationship entries are either:

- **Primitive:** intentionally irreducible within this release, with a precise interpretation and reviewed examples.
- **Composite:** an acyclic, typed expansion into already defined entries with explicit parameter substitution.

The expansion is a structured glossary template, not an opaque sentence or a claim of synonymy. Renaming a complex phrase does not constitute a definition. A shared primitive need not be derived from English morphology; membership is an explicit release decision.

Unrelated domain terms may grow without changing grammar. The same relationship in a new domain should reuse its accepted constructor. A new relational capacity requires a meaningful signature and definition, not just a new noun.

## 10. Claims, attribution, and provenance

```ebnf
claim        ::= "CLAIM" IDENT "(" attrs? ")"
                 "BY" value "STATUS" epistemic "SOURCE" STRING
                 "->" IDENT ":" "CLAIM"
epistemic    ::= "asserted" | "observed" | "inferred" | "assumed"
               | "hypothesized" | "reported"
```

The predicate must be an accepted glossary relation with a typed signature. Arguments may include TERM, CLAIM, or EVENT where its signature permits. `BY` identifies a holder/source using a STRING symbol or TERM. Anonymous attribution must be explicit; do not quietly attribute every proposition to the encoder.

Statuses mean:

| Status | Interpretation |
|---|---|
| asserted | The holder states the proposition without represented justification |
| observed | The source supplies an observation of it |
| inferred | The holder presents it as a conclusion from grounds |
| assumed | The holder adopts it without establishing it |
| hypothesized | The holder considers it as a candidate explanation |
| reported | The holder reports it from another source, without necessarily endorsing it |

None means objective truth. `SOURCE` is a stable locator into the supplied input/evidence manifest, not a URL the translator invents and not a prose justification. Every locator must resolve. Source text remains available externally for audit; the encoded content must still convey the proposition to a reader without that text.

Repeated use of one established claim references the same binding. A new speaker, changed status, different time or condition, or later revision can justify a new claim record. Contradictory claims are allowed when attribution, time, or epistemic context makes the difference explicit. An unqualified contradiction attributed to the same holder is reported as a source inconsistency, never silently reconciled.

Negative, conditional, temporal, and causal propositions are represented through glossary-defined relations. They are distinct from Check's runtime Boolean operators. Common semantic relations must have shared definitions, rather than relying on each translator's English interpretation.

## 11. Reasoning links and recorded operations

```ebnf
link         ::= "LINK" IDENT "(" attrs ")" "SOURCE" STRING
record       ::= "RECORD" record_kind IDENT "(" attrs? ")"
                 "STATUS" event_status "SOURCE" STRING
                 "->" IDENT ":" "EVENT"
record_kind  ::= "ACTION" | "GENERATE"
event_status ::= "attempted" | "succeeded" | "failed" | "unknown"
```

LINK records a source-supported semantic relationship using an accepted glossary signature. Common relations include supports, contradicts, rejects, revises, motivates, and produces. They are not interchangeable: temporal adjacency alone never proves support or causation.

A reasoning link needs its own source locator. If no grounds were supplied for an inferred conclusion, preserve the conclusion's status but report the missing grounds externally; do not manufacture a proof. A flat list of findings is valid when the source supplies no argument.

RECORD is permitted only in TRACE mode. Its attributes follow the referenced operation's descriptive signature, but runtime REF arguments are represented by TERM descriptions of identified objects. Each operation used in a trace must declare this recording signature in the glossary. Recording GENERATE uses an accepted generation-profile identifier, not a fabricated external operation.

The result is an EVENT describing what occurred, not an executable result or newly acquired physical REF. Record the actual outcome using CLAIM relations referring to that event. Wrong answers, failed operations, and mismatched output types remain representable as claims about the event; they do not become falsely valid runtime values.

An event with status attempted does not imply success; unknown indicates that the source does not establish its outcome. Preserve source-supported outputs and relevant changes separately. Do not record a requested operation as an observed event.

## 12. Conversation, cross-turn references, and corrections

```ebnf
conversation ::= "CONVO" IDENT "{" turn+ "}"
turn         ::= "TURN" IDENT "SPEAKER" "=" speaker
                 ("REPLY_TO" IDENT)?
                 ("REVISES" IDENT | "AMENDS" "[" name ("," name)* "]")?
                 "{" step+ "}"
speaker      ::= "USER" | "AGENT"
```

One supplied message maps to one TURN, with names t1, t2, ... in order. Do not invent intermediate messages. Tool observations attach to the relevant agent turn as RECORD statements with source locators; `SPEAKER` describes the conversational role, while BY preserves specific claim attribution.

Bare runtime bindings are local to a turn and its child scopes. Earlier turns' top-level TERM, CLAIM, and EVENT bindings may be referenced read-only as `t1.claim_name`. This permits evidence and reference identity to persist across a conversation without importing mutable runtime variables. Forward references and references into nested child scopes are invalid.

`REPLY_TO` names the actual reply target when supplied; otherwise it defaults to the immediately preceding turn. Adjacency is not evidence of agreement, support, or causation.

Corrections have two distinct forms:

- `REVISES t1` explicitly replaces the whole active semantic content of an earlier turn. It must target the current tip of that replacement lineage. The old turn remains in the trace. Do not use this for a partial correction.
- `AMENDS [t1.claim_name]` replaces only the listed top-level CLAIM targets. Each target must have exactly one new CLAIM in the amending turn and a `LINK revises(previous=..., replacement=...)`. Unmentioned claims and requirements remain active. Follow the replacement chain to its latest member when selecting a target.

Compute active content by processing turns in source order: whole-turn revision supersedes the target turn's active contents; amendment supersedes exactly the listed claim IDs; other turns preserve existing content. Historical content remains addressable, with its superseded status visible. A revision records the speaker's correction; it does not prove the new claim is true.

An ambiguous correction remains an ordinary reply plus an external ambiguity report. Do not guess what was withdrawn. REQUEST conversations describe a supplied request exchange; TRACE conversations record what occurred. UTTER is non-effectful in both.

## 13. Fidelity, literal content, and completeness

Preserve every distinct requested constraint, substantive claim, comparison, outcome, and reasoning connection supported by the input. Shorter output is not inherently better. Do not replace a mechanism with “positive impact,” a question with its heading, or an artifact with the fact that it was generated.

Encode operations warranted by the source, but never invent motives, evidence, intermediate reasoning, resources, results, or missing values. Distinguish a translator's uncertainty from uncertainty expressed by the source. The former belongs in the external translation report; the latter belongs in the language.

### Permitted literal content

Strings are appropriate for exact names/identifiers, addresses, source locators, and wording whose exact form is the deliverable or object of analysis. A date or quantity still needs a defined interpretation, including units or timezone where relevant.

Free text is not a substitute for structured claims. `content` is permitted as a transitional fallback only when the external report marks the relevant source span as opaque and explains the gap. Such a span does not count as fully formalized coverage. A complete source sentence hidden in a topic name has the same problem as a copied sentence in a STRING.

Do not universally ban meaningful long quotations or exact creative text: retain them as literal artifacts when their wording matters, while separately encoding the claims or properties the task concerns.

### Required external translation report

Record the pinned release, input kind, complete/partial/unrepresentable status, source-span coverage, opaque-text spans, missing constructs, unresolved ambiguities, and proposed glossary/spec changes. A proposal is not automatically accepted vocabulary. Do not insert invented placeholder syntax into a canonical document.

A back-translation reader must be able to reconstruct substance from the document and release, without consulting the original text or inferring propositions from arbitrary binding names. Renaming local handles should not alter recoverable meaning. Glossary symbols retain their published definitions; this test does not erase the vocabulary itself.

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
9. **Extensions:** unknown meanings become proposals. There is no automatic `custom_general_<predicate>` escape hatch. Non-ASCII or multiword source phrasing is not itself an error; report an actual semantic/vocabulary gap instead.

Canonical equivalence allows local-handle renaming and expansion of accepted aliases/composite definitions. It does not automatically equate reorderings, claims by different holders, different epistemic statuses, or distinct source events. Compare exact canonical match and declared semantic equivalence separately in evaluation.

## 15. Validation and research checks

Validation has distinct layers:

| Layer | Required checks |
|---|---|
| Syntax | Grammar, one mode/entrypoint, valid names, balanced structures |
| Static semantics | Types, categories, signatures, bindings, scope, mode restrictions, recursion guards |
| Vocabulary | Accepted symbols, resolved definitions, acyclic composite expansion |
| Provenance | Resolvable source locators, valid cross-turn references and revision targets |
| Semantic fidelity | No unsupported additions, omissions, attribution errors, or fabricated reasoning |
| Research quality | Coverage, reconstruction, cross-model determinism, task improvement, interpretability |

A parser passing a document does not establish fidelity. A model agreeing with its own translation is not independent reconstruction. A source locator establishes traceability, not correctness of the translated interpretation.

Coverage reports separate fully structured spans, opaque fallbacks, and unrepresentable spans. Evaluate on unseen domains as well as familiar examples. Reconstruction measures omissions and invented meaning, not just wording similarity. Improvement tests must not supply a completed answer when encoding an unanswered request. Human comprehension and documentation quality remain explicit tests.

## 16. Worked semantic examples

The small profiles below define all symbols used in these examples. They are illustrative entries and may not exist in the current glossary; use the glossary's definitions.

### Example profile A: a compositional question

- `oil_rig_grating`: STRING, entity-description category; a grating used on an oil rig.
- `surface_texture`: STRING, property category; the physical surface texture of an object.
- `property_question(subject: STRING, property: STRING) -> TERM`: asks for the named property of the subject, without presupposing an answer.
- `ask(target: TERM)`: UTTER speech act requesting the information described by the target.

Source: “What is the surface texture of oil-rig gratings?”

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM property_question(property=surface_texture, subject=oil_rig_grating) -> property_question_2 : TERM
    UTTER ask(target=property_question_2)
  }
}
```

The `_2` suffix avoids a collision with the glossary constructor symbol. Changing the object or property changes an argument; it does not require a new whole-question topic symbol.

### Example profile B: a supported change of hypothesis

- `agent`: STRING, claim-holder category; the agent in the supplied conversation.
- `connectivity_check`: recordable Action; no attributes in this minimal profile.
- `connectivity_works(event: EVENT)`: CLAIM relation; the referenced test reports functioning connectivity.
- `network`, `authentication`: STRING descriptors of the two systems involved in the supplied task.
- `failure(system: STRING)`: CLAIM relation; the named system is failing in the task context. The system is an argument, not welded into a new predicate name for each possible failure.
- `rejects(evidence: CLAIM, hypothesis: CLAIM)`: LINK; the holder uses the evidence to reject the hypothesis.
- `supports(conclusion: CLAIM, premise: CLAIM)`: LINK; the premise is presented as a reason for the conclusion, without asserting logical entailment.

Source manifest: `t1:s1` says the agent suspects a network problem; `t1:s2` records a successful connectivity test; `t1:s3` explicitly says that because connectivity works, the agent rejects the network explanation and instead suspects authentication. The example records that reasoning without endorsing its diagnostic strength.

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=AGENT {
    CLAIM failure(system=network) BY agent STATUS hypothesized SOURCE "t1:s1" -> failure_2 : CLAIM
    RECORD ACTION connectivity_check() STATUS succeeded SOURCE "t1:s2" -> connectivity_check_event : EVENT
    CLAIM connectivity_works(event=connectivity_check_event) BY agent STATUS observed SOURCE "t1:s2" -> connectivity_works_2 : CLAIM
    LINK rejects(evidence=connectivity_works_2, hypothesis=failure_2) SOURCE "t1:s3"
    CLAIM failure(system=authentication) BY agent STATUS hypothesized SOURCE "t1:s3" -> failure_3 : CLAIM
    LINK supports(conclusion=failure_3, premise=connectivity_works_2) SOURCE "t1:s3"
  }
}
```

The source supports a new hypothesis, not an established diagnosis. A translation that upgraded it to certainty would lose fidelity despite being syntactically valid.

### Example profile C: partial correction preserves other requirements

- `user`: STRING holder; `trip_days(value: NUMBER)` and `budget_usd(value: NUMBER)` are CLAIM relations describing requested trip duration and budget.
- `revises(previous: CLAIM, replacement: CLAIM)`: LINK; explicit replacement of the earlier claim by the later one.

Source: t1 requests a three-day trip under USD 500; t2 says “Make it four days instead.” `budget_usd` means an upper bound, not an exact spending requirement.

```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    CLAIM trip_days(value=3) BY user STATUS asserted SOURCE "t1:duration" -> trip_days_2 : CLAIM
    CLAIM budget_usd(value=500) BY user STATUS asserted SOURCE "t1:budget" -> budget_usd_2 : CLAIM
  }
  TURN t2 SPEAKER=USER REPLY_TO t1 AMENDS [t1.trip_days_2] {
    CLAIM trip_days(value=4) BY user STATUS asserted SOURCE "t2:duration" -> trip_days_2 : CLAIM
    LINK revises(previous=t1.trip_days_2, replacement=trip_days_2) SOURCE "t2:duration"
  }
}
```

The duration changes; the budget remains active. A complete domain glossary should generalize these illustrative relations into duration and monetary constraints with explicit units.
