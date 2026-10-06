# BrainCode Language Specification

**Version:** 9.0.0
**Status:** bootstrapped — base syntax established; sprints from here build incrementally.

## Purpose

BrainCode is a formal syntax for expressing human agent-requests and agentic reasoning
(task decomposition) that is:

- **Expressive** — captures what natural language captures (negation, quantifiers, conditionals,
  temporal ordering, causal chains, multi-step dependency) without redundancy.
- **Broad-coverage** — generalizes to domains not seen during its own development.
- **Deterministic** — independent translators (different models, or repeated runs) converge on
  the same or equivalent expression for the same task.
- **Interpretable** — recoverable to plain-language intent by a human or LLM reader, given only
  the expression and this documentation.
- **Style-independent** — does not encode the linguistic idiosyncrasies of whichever model wrote
  it (e.g. "email my mom" vs. "email my professor" should differ in *content* the syntax
  captures — recipient, register — not in incidental phrasing).

This document is the frozen reference during any evaluation. Do not hand-edit it outside of a
sprint — use the orchestrator so `docs/changelog.md` and `docs/glossary.md` stay in sync.

## Foundations

BrainCode is a small, statically-typed, context-free syntax for agent requests: a closed set of four value types (NUMBER, STRING, BOOL, LIST[T]) grounds every binding, comparison, and iteration, and one shared scoping/Bind-site rule set governs Task, Flow-If, Iterate, and Conversation alike. Closed, single-outcome requests decompose into typed Tasks built from strictly effectful Actions, pure boolean Checks, and a bounded Iterate/recursion model with a syntactically-enforced termination guard; open, multi-turn requests use a parallel Conversation/Turn structure that keeps effectful Actions distinct from pure Utterance speech-acts and resolves corrections via an explicit, algorithmic REVISES rule. Every document declares exactly one ENTRYPOINT, giving BrainCode a single unambiguous execution root, and no construct may be nested inline as another's argument — composition always goes through an explicit named Bind, which fixes evaluation order everywhere by construction.

Python's flat, orthogonal statements and closed control keywords shape Task/Iterate/Bind's block structure and named-parameter calls; HTML's content/attribute separation shapes Action's typed key=value attributes and its normative per-domain vocabulary; English's closed-class function words and discourse turn-taking shape Check's operator set and Conversation's TURN/REPLY_TO/REVISES model.


## Constructs

### `Types & Lexicon`

**Grammar:** `type ::= "NUMBER" | "STRING" | "BOOL" | "LIST" "[" type "]" | "REF" "[" type "]"
value ::= STRING | NUMBER | IDENT | "TRUE" | "FALSE" | list_lit | diff
list_lit ::= "[" value ("," value)* "]"
diff ::= IDENT "-" NUMBER
-- Lexical primitives:
IDENT ::= [a-zA-Z_][a-zA-Z0-9_]*
STRING ::= "\"" ( [^"\\\n] | "\\\"" | "\\\\" | "\\n" | "\\t" | "\\u" HEXHEXHEXHEX )* "\""
NUMBER ::= "-"? [0-9]+ ( "." [0-9]+ )? ( ("e"|"E") ("+"|"-")? [0-9]+ )?
COMMENT ::= "#" through end of physical line.
Reserved words (case-sensitive): TASK, ACTION, UTTER, GENERATE, IF, THEN, ELSE, FOR, EACH, IN, ANY, ALL, SATISFIES, AND, OR, NOT, LET, RETURN, TRUE, FALSE, CONVO, TURN, SPEAKER, USER, AGENT, REPLY_TO, REVISES, ENTRYPOINT, DECREASES, NUMBER, STRING, BOOL, LIST, REF.`

**Semantics:** BrainCode has exactly five closed value-type forms: NUMBER, STRING, BOOL, LIST[T], and REF[T]. REF[T] is an opaque runtime reference to one particular extant entity whose descriptive value type is T (e.g., REF[STRING] for physical objects). A REF value is not a STRING label, cannot be written as a literal, and cannot be manufactured by LET from a STRING. It enters a scope only through a typed Action result, a typed Task parameter/return, or a copied REF. Two REF[T] values compare equal only when they designate the same runtime entity. LIST[REF[T]] is legal. The other four types behave as previously defined: NUMBER, STRING, BOOL, and LIST[T] (homogeneous, finite). `diff` is a minimal arithmetic form for recursion guards. No implicit coercion exists. A value with no staticly determinable type cannot appear in a Check or as a FOR EACH iterable.

**Example:**
- NL: "Rinse the mug in the sink, then put that same mug in the coffee maker."
- BrainCode: `ENTRYPOINT RinseThenPlace

TASK RinseThenPlace {
  ACTION rinse(target="mug", destination="sink") -> mug : REF[STRING]
  ACTION place(target=mug, destination="coffee_maker")
}`

*Introduced/last revised: sprint 2, version 2.0.0*

### `Task`

**Grammar:** `document ::= entrypoint (task | conversation)*
entrypoint ::= "ENTRYPOINT" IDENT
task ::= "TASK" IDENT param_list? ("CONTEXT" execution_date_param)? (":" type)? ("DECREASES" IDENT)? "{" step+ return_stmt? "}"
execution_date_param ::= "execution_date" "=" ISO_DATE
param_list ::= "(" param (,"," param)* ")"
param ::= IDENT ":" type
return_stmt ::= "RETURN" value
step ::= action | flow_if | flow_for | bind | task_call | utterance | generation
task_call ::= IDENT arg_list? ( "->" IDENT )?
arg_list ::= "(" arg (,"," arg)* ")"
arg ::= IDENT "=" value
-- ISO_DATE ::= a STRING literal matching exactly YYYY-MM-DD: four-digit year, two-digit month 01-12, two-digit day valid for that month/year (e.g. no 2025-02-30). A STRING not matching this exact calendar-date shape is a static error, never a runtime one.`

**Semantics:** A BrainCode document declares exactly one ENTRYPOINT naming a top-level TASK or CONVO; ENTRYPOINT itself carries no CONTEXT — CONTEXT is a TASK-declaration-only clause, written directly after the TASK's IDENT/param_list, never after ENTRYPOINT (a document that writes `ENTRYPOINT Foo CONTEXT execution_date=...` is grammatically invalid; CONTEXT belongs on the `TASK Foo CONTEXT execution_date=... { ... }` line). If ENTRYPOINT names a TASK, that TASK must declare zero parameters and is invoked once; if CONVO, its turns execute in document order. Other top-level TASKs are inert library declarations.

`CONTEXT execution_date=ISO_DATE` is a translation-time-only annotation: it exists so a translator has a fixed calendar anchor against which to resolve relative-date phrases in the source NL ("next Tuesday", "Friday", ...) exactly once, before the document is finalized, and it is retained verbatim in the emitted BrainCode source purely for human auditability — a reviewer can see what date the translator resolved against. It is never read, re-evaluated, or mutated by anything at runtime; no step consults it a second time, and no runtime clock derives from it beyond the one-time resolution and lifting rules defined under Action. A malformed or invalid-calendar `execution_date` value is a static error caught at translation time, not discovered at runtime.

Task names and Variable names are disjoint namespaces. Variable scoping is lexical and block-structured. `param_list` declares typed formal parameters; a task_call's `arg_list` supplies arguments by name with exact static type matching. A Task's signature may declare a result type (`: type`); if declared, the body must end with a `RETURN value` of exactly that type. If not declared, the body must have no RETURN. A `-> IDENT` on a task_call is legal only when the callee declares a result type. Recursion requires the Task to declare `DECREASES paramName` (a NUMBER parameter), and every recursive call must be guarded by an IF-THEN checking `paramName comp_op NUMBER_LITERAL` (with `>`, `>=`, `!=`) and pass `paramName - NUMBER_LITERAL`. The `step` production includes `generation` for pure, non-effectful artifact generation.

**Example:**
- NL: "Go to the flight booking site, search flights from Tel Aviv to Berlin next Tuesday, and list the three cheapest options."
- BrainCode: `ENTRYPOINT BookFlight

TASK BookFlight CONTEXT execution_date="2025-06-03" : LIST[REF[STRING]] {
  ACTION open_page(target="flight_booking_site")
  ACTION search_travel(origin="Tel Aviv", destination="Berlin", date="2025-06-10") -> raw_flights : LIST[REF[STRING]]
  ACTION sort(target=raw_flights, ordering="price_asc") -> sorted_flights : LIST[REF[STRING]]
  ACTION extract(target=sorted_flights, limit=3) -> cheapest_flights : LIST[REF[STRING]]
  RETURN cheapest_flights
}`

*Introduced/last revised: sprint 6, version 5.0.0*

### `Action`

**Grammar:** `action ::= "ACTION" IDENT "(" attr_list? ")" ( "->" IDENT ":" type )?
attr_list ::= attr ("," attr)*
attr ::= IDENT "=" value

-- Normative operation vocabulary. Every listed operation has an explicit signature and a Result
-- category: SAME = output REF/LIST[REF[T]] designates the identical entity/collection named by
-- `target`, merely relocated/transformed/reordered/narrowed as a whole; MEMBER = output REF or
-- LIST[REF[T]] designates one or more pre-existing elements drawn out of a LIST[REF[T]] named by
-- `target` (the element(s) already existed inside that list; the call selects/surfaces them, it
-- does not preserve the whole collection's identity and does not fabricate anything); NEW = output
-- REF(s) designate entity/entities distinct from anything named in `target` (newly discovered or
-- newly produced); VALUE = a plain NUMBER/BOOL/STRING, never a REF; NONE = no bindable result.
-- `T` ranges over any descriptive value type per Types & Lexicon.

-- WEB:
-- open_page(target=STRING) -> NONE
-- click(target=REF[STRING]|STRING) -> NONE
-- select_filter(target=LIST[REF[T]], content=STRING) -> LIST[REF[T]]                    [SAME]
-- apply_filters(target=LIST[REF[T]], content=STRING) -> LIST[REF[T]]                    [SAME]
--   -- select_filter vs apply_filters is a deterministic count rule, not a free translator choice:
--   -- use select_filter when the source states exactly one filtering criterion; use apply_filters
--   -- when the source states two or more criteria, joined into one `content` string (e.g. "RAM >=
--   -- 16 GB; price < $1,200"). Signature and Result category are identical; only the arity of the
--   -- criterion set in the source selects which IDENT is emitted.
-- sort(target=LIST[REF[T]], ordering=STRING) -> LIST[REF[T]]                            [SAME]
-- search_travel(origin=STRING, destination=STRING, date=STRING, return_date=STRING?, passengers=NUMBER?) -> LIST[REF[STRING]]  [NEW]
-- search_web(target=STRING) -> LIST[REF[STRING]]                                        [NEW]
-- fill_field(target=REF[STRING]|STRING, content=STRING) -> NONE
-- submit(target=REF[STRING]|STRING) -> NONE
-- extract(target=LIST[REF[T]], limit=NUMBER_LITERAL) -> REF[T] if limit==1, else LIST[REF[T]]  [MEMBER]
-- read_page(target=REF[STRING]|STRING, content=STRING?) -> STRING                       [VALUE]
-- save_favorite(target=REF[STRING]) -> NONE
-- add_to_cart(target=REF[STRING]) -> NONE

-- HOUSEHOLD:
-- pick_up(target=STRING|REF[STRING]) -> REF[STRING]                                     [SAME]
-- place(target=REF[STRING], destination=STRING|REF[STRING]) -> NONE
-- heat(target=REF[STRING]|STRING, destination=STRING?) -> REF[STRING]                    [SAME]
-- chill(target=REF[STRING]|STRING, destination=STRING?) -> REF[STRING]                   [SAME]
-- rinse(target=REF[STRING]|STRING, destination=STRING) -> REF[STRING]                    [SAME]
-- slice(target=REF[STRING]|STRING) -> LIST[REF[STRING]]                                  [NEW]
-- pour(target=REF[STRING]|STRING, destination=STRING|REF[STRING]) -> NONE
-- open_container(target=REF[STRING]|STRING) -> NONE
-- close_container(target=REF[STRING]|STRING) -> NONE
-- turn_on(target=REF[STRING]|STRING) -> NONE
-- turn_off(target=REF[STRING]|STRING) -> NONE

-- CODE:
-- modify_code(target=STRING, content=STRING) -> NONE
-- run_tests(target=STRING) -> NONE
-- add_file(target=STRING, content=STRING) -> NONE
-- delete_file(target=STRING) -> NONE

-- COMMUNICATION:
-- send_email(recipient=STRING, content=STRING, tone=STRING?) -> NONE
-- send_message(recipient=STRING, content=STRING, tone=STRING?) -> NONE
-- call(recipient=STRING) -> NONE
-- check_replied(target=STRING, deadline=STRING) -> BOOL                                  [VALUE]

-- FILESYSTEM:
-- file_age_days(target=STRING) -> NUMBER                                                 [VALUE]
-- path_in_folder(target=STRING, destination=STRING) -> BOOL                               [VALUE]

-- APPLICATION_LIST:
-- create_list(target=STRING) -> REF[STRING]                                              [NEW]
-- add_to_list(target=REF[STRING]|STRING, destination=REF[STRING]) -> NONE

-- SUPPORT:
-- check_support_status(target=STRING, metric=STRING) -> BOOL                              [VALUE]

-- An operation not listed above uses the default signature target=REF[T]|STRING with optional
-- destination=REF[T]|STRING and Result NONE.`

**Semantics:** Action is BrainCode's sole construct for interacting with external state, whether causing an effect or querying a live system. Its IDENT uses a normative operation whenever one applies. Duplicate canonical attributes are static errors. target identifies the entity acted on, output artifact, or subject matter; content is literal source text, an exact instruction payload, or an exact residual execution/change condition; recipient is an effectful communication destination. An Action result binding is legal only when the operation's Result category is not NONE, and the declared bind type must exactly match that category's type (REF[T]/LIST[REF[T]] for SAME, NEW, and MEMBER; NUMBER/BOOL/STRING for VALUE).

Result categories, precisely: SAME means the operation acts on, transforms, relocates, or reorders the entity or collection already named by `target` in its entirety, and its output REF/LIST[REF[T]] designates that identical runtime entity/collection, now in a new state (e.g. `rinse` — the mug already existed; `sort` — the same list, reordered). NEW means the output REF(s) designate entity/entities distinct from anything named in `target` (`search_travel`/`search_web` surface previously-unreferenced entities; `slice` produces pieces distinct from the whole). MEMBER means the output REF or LIST[REF[T]] designates one or more elements that already existed *inside* the LIST[REF[T]] named by `target` — the call selects and surfaces a subset, it neither fabricates a new entity (unlike NEW) nor preserves the whole collection's identity (unlike SAME): `extract(target=ranked_laptops, limit=1) -> best_laptop` binds the identical runtime entity that was already the first element of `ranked_laptops`, not a newly produced item and not the list itself. `extract`'s result type is statically determined by its `limit` attribute, which must be a NUMBER literal (never a variable): `limit=1` yields REF[T] under MEMBER, any other literal value yields LIST[REF[T]] under MEMBER. VALUE means the result is an ordinary NUMBER/BOOL/STRING with no entity identity at all; `read_page(target=REF[STRING]|STRING, content=STRING?) -> STRING [VALUE]` reads and returns the textual content or condition present at/on the located `target` (a page, listing, or record) — `content`, if given, names which specific field or condition to read (e.g. `content="current conditions"`); this closes the gap where search/extract could locate a result entity but nothing could return the fact the request actually asked for.

Coreference conformance rule (static, mechanically checkable from source NL plus emitted BrainCode alone — no external lexicon required): BrainCode adopts a naming convention that makes each REF-typed and LIST[REF[T]]-typed binding's descriptor recoverable directly from the emitted source. Bind IDENT-naming requirement: the IDENT chosen for any REF-typed or LIST[REF[T]]-typed Action or task_call result must be the normalized (lowercase, singular, underscore-joined for multi-word) form of the head noun of the entity/collection it designates (as already shown in every worked example: `rinse(target="mug", ...) -> mug`); choosing an unrelated IDENT name for such a binding is a static naming-convention error. This IDENT itself is that binding's descriptor label — no separate hidden field is needed.

Given this, resolving any REF[T]- or LIST[REF[T]]-typed attribute (wherever an operation's signature expects one — not limited to a fixed attribute name, and never applying to opaque STRING payload attributes like `content`) proceeds as: (a) build the candidate set from every REF[T]- or LIST[REF[T]]-typed IDENT already bound in the currently visible scope chain (Bind's rules); (b) filter immediately by type compatibility — a REF[T]-expected attribute may only match REF[T]-typed candidates, a LIST[REF[T]]-expected attribute only LIST[REF[T]]-typed candidates; the two pools never cross. (c) A bare pronoun/demonstrative with no noun ('it', 'them', 'this', 'that') resolves, among the type-filtered pool, to the single nearest-preceding bound candidate in source order — no lexicon lookup needed. (d) A demonstrative-plus-noun or definite description ('that mug', 'the mug') resolves, among the type-filtered pool, to the candidate(s) whose IDENT contains that exact noun token (normalized as above); ties resolve to the nearest-preceding one. (e) An indefinite phrase ('a mug', 'another mug') signals a genuinely new instance: if the consuming operation's attribute accepts STRING as an alternative (`REF[T]|STRING`), emit a fresh STRING literal directly. If the attribute's signature requires REF[T] only (no STRING alternative, e.g. `place`'s `target`), a bare indefinite mention cannot be consumed directly: the translator must first emit an appropriate acquiring Action from the normative vocabulary that establishes the REF (e.g. `pick_up` for a physical object, `create_list` for a list, `search_web`/`search_travel` for an informational entity, `slice` for a piece) and then pass its bound result; if no acquiring operation exists for the entity's domain, this is a static translation error flagging a vocabulary gap rather than a silent guess. (f) If step (d) yields exactly one candidate, use it — reusing that IDENT instead of a fresh STRING literal is mandatory; emitting a fresh STRING literal when exactly one type-compatible, noun-matching candidate exists is a static conformance error. If it yields zero, treat as first mention per (e). If it yields two or more (genuine duplicate labels, e.g. two mugs both bound as `mug`/`mug2`), the source must carry an explicit disambiguating modifier from the closed set {first, second, third, ..., last, other, another, previous, new}; apply it against candidates ordered by bind (source) order — 'first'/'second'/... select by that position, 'last' selects the most recently bound, 'other'/'previous' selects the non-most-recent one when exactly two candidates remain. A duplicate-label ambiguity with no such modifier anywhere in the source is a static ambiguous-antecedent translation error rather than a guess.

The SUPPORT domain adds check_support_status(target=STRING, metric=STRING) -> BOOL, which queries a support case or customer record for an explicit live status condition. Valid canonical `metric` values are strictly limited to `is_late`, `is_first_time_buyer`, and `is_repeat_buyer`; any other metric string is a static translation error. `target` must be a canonical identifier string naming the specific customer, order, or support case. To guarantee single customer/order relationship correlation across multiple queries, all related check_support_status calls for a single evaluation context must use consistent canonical entity identifiers (e.g., target="customer_order" for order-level queries and target="customer" for customer-level queries). `is_first_time_buyer` and `is_repeat_buyer` are logical complements for any valid single customer record; if a support record is missing, inaccessible, ambiguous, or contains contradictory buyer-status flags, check_support_status treats the query as an external Action failure and halts the entire enclosing Task immediately, aligning with BrainCode's fail-fast external Action rule. Any other external Action failure likewise halts execution.

**Example:**
- NL: "Rinse the mug in the sink, then put it in the coffee maker."
- BrainCode: `ENTRYPOINT RinseThenPlace

TASK RinseThenPlace {
  ACTION rinse(target="mug", destination="sink") -> mug : REF[STRING]
  ACTION place(target=mug, destination="coffee_maker")
}`

*Introduced/last revised: sprint 9, version 8.0.0*

### `Utterance`

**Grammar:** `utterance ::= "UTTER" IDENT "(" attr_list? ")" ( "->" IDENT )?
-- IDENT after UTTER is an open speech-act vocabulary; canonical forms, used whenever applicable: ask, respond, inform, propose, correct, acknowledge, confirm, decline.
-- attr_list uses Action's core attribute vocabulary (content, recipient, audience, tone, register_note, format, target, deadline, quantity, ...).
-- utterance is one alternative of Task's `step` production, but is a static error anywhere inside a TASK body (directly or nested in IF/FOR); it is legal only inside a CONVO TURN body (see Conversation).`

**Semantics:** UTTER is BrainCode's pure, non-effectful counterpart to Action: it records that a communicative act of a given speech-act type occurred, with attributed content, but performs no real-world or system side effect. Grammatically it is one alternative of `step` (so it can appear anywhere a step can, including nested inside IF/FOR), but semantically it is legal only inside a CONVO TURN body — a Task body containing an UTTER, at any nesting depth, is a static error. A TURN body may freely mix ACTION (a real side effect actually taken during that turn) and UTTER (what was said). UTTER's `content` attribute is its primary payload and, per BrainCode's open-item design, remains natural-language prose: BrainCode formalizes who said what, in what register, to whom, and in what order, not the substance itself. Like Action, an UTTER call is subject to the shared duplicate-canonical-attribute static error (no attribute name, including `register_note`, may appear twice in one UTTER call). UTTER's optional `tone` attribute is governed by exactly the same closed 14-value enum, normalization procedure, and exact-match translation-selection table defined under Action: a conversational register word that normalizes to an exact table or canonical-label match (e.g. "casually" -> `tone="casual"`, per the table's adverbial entries) is rewritten to its canonical value; a register with no exact match — including any phrase merely containing a register word, or one blending more than one facet — must omit `tone` and instead carry the full register description in `register_note`, exactly as on Action and GENERATE. `tone` and `register_note` remain mutually exclusive on the same UTTER call. This makes conversational register exactly as deterministic, and exactly as structurally separated from substance, as generated or effectful register — there is no separate, looser tone rule for dialogue. An optional `-> IDENT` binds the STRING value of this utterance's `content` attribute (not `tone`, not `register_note`, not the whole record) into the enclosing scope under Bind's ordinary rules, for reuse by a later step in the same TURN; using `->` on an UTTER with no `content` attribute is a static error. Like Action, an UTTER statement itself can never appear directly inside a Check — only a value it has bound via `->` can.

**Example:**
- NL: "User, casually: 'Hey, thanks so much for sorting that out today!'"
- BrainCode: `CONVO CasualThanks {
  TURN t1 SPEAKER=USER {
    UTTER acknowledge(content="Thanks so much for sorting that out today.", tone="casual", recipient="agent")
  }
}`

*Introduced/last revised: sprint 3, version 3.0.0*

### `Check`

**Grammar:** `check ::= disjunction
disjunction ::= conjunction ( "OR" conjunction )*
conjunction ::= negation ( "AND" negation )*
negation ::= "NOT" negation | primary
primary ::= "(" check ")" | quantifier | comparison
comparison ::= value ( comp_op value )?
comp_op ::= "==" | "!=" | "<" | "<=" | ">" | ">="`

**Semantics:** Check is a pure boolean expression with no side effects; an Action or UTTER call may never appear inside a Check directly — only a value with a statically determinable type (per Types & Lexicon: a literal, a typed LET, a typed parameter, a typed Action `-> IDENT : type`, a task_call `->` inheriting the callee's declared type, or an UTTER's bound content STRING) may appear as a `value`; a reference with no such statically determined type is a static error. Precedence, lowest to highest: OR, then AND, then NOT, then comparison/parenthesized primary; parentheses override. Evaluation is left-to-right and short-circuiting: in `A OR B`, B is evaluated only if A is false; in `A AND B`, B is evaluated only if A is true. `comparison` has two forms: a full `value comp_op value` comparison, or a bare `value` alone used as a truthiness test (e.g. `IF replied THEN`, `IF NOT replied THEN`). Truthiness: NUMBER 0 is false, any other NUMBER is true; empty STRING is false, non-empty STRING is true; TRUE/FALSE are themselves; an empty LIST is false, non-empty LIST is true. Referencing an IDENT not yet bound in the current or an enclosing scope is a static error. comp_op requires both operands' statically declared types to match exactly, with no implicit coercion; a type mismatch is a static error caught before any execution, not discovered at runtime. NUMBER supports all six operators with ordinary numeric ordering. STRING supports all six: `==`/`!=` test literal equality, the four ordering operators test lexicographic (codepoint) order. BOOL supports only `==`/`!=`; an ordering operator on BOOL is a static error. LIST supports only `==`/`!=`, testing structural equality (equal length, every element equal under this same rule, recursively); an ordering operator on LIST is a static error.

**Example:**
- NL: "Only proceed if the cart total exceeds $50 and the user is a member, or the order is a gift, or there's a discount code."
- BrainCode: `LET cart_total : NUMBER = 65
LET is_member : BOOL = TRUE
LET is_gift : BOOL = FALSE
LET discount_code : STRING = ""
(cart_total > 50 AND is_member == TRUE) OR is_gift == TRUE OR discount_code`

*Introduced/last revised: sprint 0, version 0.1.0*

### `Flow-If`

**Grammar:** `flow_if ::= "IF" check "THEN" "{" step+ "}" ( "ELSE" "{" step+ "}" )?`

**Semantics:** Conditional branching, used identically inside TASK and CONVO TURN bodies (both use the same `step` production). The Check is evaluated first, at the moment control reaches the IF. If true, the THEN block's steps execute in order; if false and an ELSE block is present, its steps execute instead; if false with no ELSE, control passes to whatever step follows. Flow-If may nest inside another Flow-If's THEN/ELSE or inside a FOR-EACH body; nested Checks evaluate only when outer control flow actually reaches them, never speculatively. THEN and ELSE each open their own fresh child variable scope under Task's unified scoping model: each may read any name already visible from the enclosing scope, but a LET/`->` binding made inside THEN is not visible inside ELSE, after the IF, or from any sibling construct, and vice versa. Because `step` now includes `utterance`, an IF nested inside a TURN body may contain UTTER in its branches exactly as it may contain ACTION; the same nesting containing UTTER inside a TASK body remains a static error per Utterance's restriction. When a Flow-If's Check depends on a preceding `check_replied` result with a future `deadline` instant, the branch's evaluation inherits check_replied's deferred timing (see Action): control does not reach the IF's Check until the underlying deferred query has resolved at its deadline instant.

**Example:**
- NL: "If my manager hasn't replied by Friday, send a polite follow-up; otherwise do nothing."
- BrainCode: `ENTRYPOINT FollowUpManager

TASK FollowUpManager CONTEXT execution_date="2025-06-03" {
  ACTION check_replied(target="manager", deadline="2025-06-06T23:59:59Z") -> replied : BOOL
  IF NOT replied THEN {
    ACTION send_email(recipient="manager", tone="polite", content="follow-up")
  }
}`

*Introduced/last revised: sprint 6, version 5.0.0*

### `Iterate`

**Grammar:** `flow_for ::= "FOR" "EACH" IDENT "IN" iterable "{" step+ "}"
iterable ::= IDENT | list_lit
quantifier ::= ("ANY" | "ALL") IDENT "IN" iterable "SATISFIES" check`

**Semantics:** `iterable` must have static type LIST[T] for some element type T (per Types & Lexicon): either a list_lit (whose element type is the common type of its necessarily-homogeneous elements), or an IDENT whose declared type (from a parameter, LET, Action `->`, or task_call `->`) is LIST[T]; an iterable with no LIST[T] type is a static error at translation time. FOR EACH binds its loop IDENT to each element of iterable in turn, in list order, once per element, strictly sequentially (no parallel iteration in this basis). Because LIST is always a finite, closed collection under this type system (never an open runtime stream), FOR EACH is guaranteed to terminate independent of Task's DECREASES mechanism, which governs recursion instead. The loop body opens a fresh child variable scope, re-created independently for every iteration: the loop IDENT (statically typed T) and any LET/`->` binding made inside the body are visible only within that one iteration, discarded before the next iteration begins and after the loop ends — no accumulation, no leakage. Like every other bound name, the loop IDENT may not shadow a name already visible in an enclosing scope (static error). ANY/ALL are quantifiers usable anywhere a `check` is valid (Check-level, hence pure) over an iterable subject to the same LIST[T] typing requirement: `ANY x IN L SATISFIES c` short-circuits to true on the first element satisfying c, false if none do (false on empty L); `ALL x IN L SATISFIES c` short-circuits to false on the first failing element, true if every element satisfies it (vacuously true on empty L). The quantifier's bound IDENT `x` follows the identical typing and no-shadowing rule but is a narrower, single-use lexical binding: it exists only for static name resolution inside that quantifier's own `check` expression, is freshly bound and discarded per candidate element as evaluation proceeds, may never be referenced after the SATISFIES check, and creates no lasting Bind-site of its own.

**Example:**
- NL: "For each stop on the itinerary, book a hotel."
- BrainCode: `LET itinerary : LIST[STRING] = ["Paris", "Lyon", "Nice"]
FOR EACH stop IN itinerary {
  ACTION book_hotel(target=stop)
}`

*Introduced/last revised: sprint 0, version 0.1.0*

### `Bind`

**Grammar:** `bind ::= "LET" IDENT ":" type "=" value
-- Additional Bind-site forms: action_result ::= "->" IDENT ":" type ; task_call_result ::= "->" IDENT ; utterance_result ::= "->" IDENT ; generation_result ::= "->" IDENT ":" type`

**Semantics:** Bind is BrainCode's shared named data-flow rule. Its five Bind sites are: (1) `LET IDENT : type = value`; (2) an Action result `-> IDENT : type`; (3) a task_call result `-> IDENT`, whose type is the callee Task's declared result type; (4) an UTTER result `-> IDENT`, whose type is STRING and whose value is that UTTER's content; and (5) a GENERATE result `-> IDENT : type`. LET requires an exactly matching static type and may bind a REF only by copying an already visible REF of exactly the same type; it cannot create a reference from a descriptor STRING. A binding in a Task body is visible only to lexically later steps in that Task body and its subsequently entered IF branch or FOR iteration child scopes. A binding in a Turn body is visible only to lexically later steps in that same Turn body and its subsequently entered IF branch or FOR iteration child scopes; an UTTER binding never crosses into another TURN. A binding in an IF THEN body is visible only to later steps of that same THEN body; one in an ELSE body is visible only to later steps of that same ELSE body. A binding in a FOR EACH body is visible only during that one iteration's body. Parameters and task-call results are scoped to their own task-call invocation. Shadowing any currently visible name is a static error. Source-order execution guarantees operation order and propagates bound descriptor values or REF identities.

**Example:**
- NL: "Rinse one mug in the sink, then place that same selected mug in the coffee maker."
- BrainCode: `ENTRYPOINT RinseThenPlace

TASK RinseThenPlace {
  ACTION rinse(target="mug", destination="sink") -> mug : REF[STRING]
  ACTION place(target=mug, destination="coffee_maker")
}`

*Introduced/last revised: sprint 2, version 2.0.0*

### `Conversation`

**Grammar:** `conversation ::= "CONVO" IDENT "{" turn+ "}"
turn ::= "TURN" IDENT "SPEAKER" "=" speaker_lit ( "REPLY_TO" IDENT )? ( "REVISES" IDENT )? "{" step+ "}"
speaker_lit ::= "USER" | "AGENT"
-- document ::= entrypoint (task | conversation)* ; CONVO is a top-level declaration form, alongside TASK.`

**Semantics:** CONVO is a document-level declaration giving BrainCode a construct for multi-turn conversational structure. Each CONVO has its own Turn-name namespace, private to that CONVO: a Turn IDENT is meaningful only as a REPLY_TO/REVISES target inside the same CONVO, and a REPLY_TO/REVISES may only reference a Turn already declared above it in document order (no forward reference, matching Bind's rule). A Turn's body (`step+`) may freely mix ACTION (a real effectful step actually taken during that turn) and UTTER (a pure speech-act record of what was said, legal here precisely because it is inside a TURN); it runs in its own fresh, independent variable scope exactly like a Task body — Turns do not share variables with each other or with any Task; the only value that legitimately crosses a Turn/Task boundary is a Task's RETURN via `->` (richer cross-turn data flow remains a known gap). SPEAKER labels whether a Turn originates from the human (`USER`) or the assistant (`AGENT`); it does not change how the Turn's steps execute, only how the record is read. `REPLY_TO IDENT` marks direct conversational adjacency and has no data-flow effect; it is resolved purely structurally, exactly as written, regardless of whether its target has since been revised — a turn that means to address a lineage's current state must itself REPLY_TO the lineage's current tip (BrainCode does not auto-redirect a stale REPLY_TO; a translator must choose deliberately). `REVISES IDENT` defines a strictly linear correction chain, resolved algorithmically: (1) a turn may be the REVISES-target of at most one other turn — declaring a second REVISES of the same target is a static error; a further correction must instead target the existing chain's current tip, never the root or an intermediate link, so every lineage stays a simple chain rather than a branching tree; (2) revision is whole-body replacement, not field merge — a turn `T2` with `REVISES T1` replaces T1's entire step body as 'the current request' for that lineage, and if T2 needs something from T1 it must restate it; (3) define `effective(T)` recursively: if no turn revises T, `effective(T)` is T's own step body; if some T' has `REVISES T`, `effective(T) = effective(T')` — rule (1) guarantees this recursion always terminates at a unique tip. Any reader/executor determining 'what is currently being asked' in a lineage must use `effective(root)`, never an intermediate turn's literal body.

**Example:**
- NL: "User: 'Tell me what's happening in New Zealand politics.' User: 'Are you up to date?' User, correcting the first ask: 'Actually, give me 2023 Aotearoa political events specifically, using current information.'"
- BrainCode: `CONVO CurrentAotearoaPolitics {
  TURN t1 SPEAKER=USER {
    UTTER ask(content="Explain current political developments in New Zealand.")
  }
  TURN t2 SPEAKER=USER REPLY_TO t1 {
    UTTER ask(content="State whether your information is up to date.")
  }
  TURN t3 SPEAKER=USER REVISES t1 {
    UTTER ask(content="Explain current political events in Aotearoa for 2023 using current information.")
  }
}
-- effective(t1) = effective(t3) = t3's body, since t3 REVISES t1 and no turn revises t3.`

*Introduced/last revised: sprint 0, version 0.1.0*

### `types-lexicon`

**Grammar:** `-- Merged into Types & Lexicon`

**Semantics:** This entry is deprecated and fully merged into the capitalized Types & Lexicon construct. It is no longer a separately indexed normative construct.

**Example:**
- NL: "Deprecated."
- BrainCode: `ENTRYPOINT Deprecated

TASK Deprecated {}`

*Introduced/last revised: sprint 2, version 2.0.0*

### `action`

**Grammar:** `-- Merged into Action`

**Semantics:** This entry is deprecated and fully merged into the capitalized Action construct. It is no longer a separately indexed normative construct.

**Example:**
- NL: "Deprecated."
- BrainCode: `ENTRYPOINT Deprecated

TASK Deprecated {}`

*Introduced/last revised: sprint 2, version 2.0.0*

### `bind`

**Grammar:** `-- Merged into Bind`

**Semantics:** This entry is deprecated and fully merged into the capitalized Bind construct. It is no longer a separately indexed normative construct.

**Example:**
- NL: "Deprecated."
- BrainCode: `ENTRYPOINT Deprecated

TASK Deprecated {}`

*Introduced/last revised: sprint 2, version 2.0.0*

### `Generate`

**Grammar:** `generation ::= "GENERATE" "(" gen_attr_list? ")" "->" IDENT ":" gen_type
gen_attr_list ::= gen_attr ("," gen_attr)*
gen_attr ::= "quantity" "=" UNSIGNED_INT | IDENT "=" value
UNSIGNED_INT ::= "0" | [1-9][0-9]*
gen_type ::= "NUMBER" | "STRING" | "BOOL" | "LIST" "[" gen_type "]"
-- A quantity attribute, if present, must use the quantity production above; quantity=NUMBER through the generic attribute production is a static error.`

**Semantics:** GENERATE is a pure, non-effectful construct that invokes a generative model to produce a value without external side effects. It shares Action's canonical attribute vocabulary and duplicate-attribute prohibition. target is always the requested output artifact, never content; content is the source instruction or text payload; audience is the intended reader; recipient is forbidden. Its optional tone and register_note follow Action's shared tone normalization rules and are mutually exclusive.

A GENERATE result type must be a gen_type: NUMBER, STRING, BOOL, or a finite nesting of LIST around those types. REF[T] is prohibited at every nesting depth: GENERATE may not declare REF[T], LIST[REF[T]], or any type containing REF. This restriction follows the global REF rule: generated text or values cannot manufacture an opaque runtime identity. The generator must return a value exactly matching its declared gen_type, including homogeneous recursively valid list elements.

quantity is an exact output-size constraint, not a maximum, minimum, estimate, or preference. Its lexical form is UNSIGNED_INT only: it may have no sign, decimal point, exponent, whitespace, or leading zero except for the literal 0. quantity is legal only for results declared STRING or LIST[T]. For LIST[T], the result contains exactly quantity elements. For STRING, it contains exactly quantity words. A word is a maximal non-empty sequence of Unicode characters whose General_Category is a Letter category (L*) or Decimal_Number (Nd); every other Unicode character is a separator. Thus quantity=0 on STRING requires a string containing no such sequence, and quantity=0 on LIST[T] requires an empty list. The executor validates the declared type and quantity condition before completion; inability to produce a conforming result fails the step under the general external-failure rule.

GENERATE must always bind its result using -> IDENT : gen_type. Use GENERATE to produce an artifact for the agent environment; use CONVO and UTTER to record observed dialogue or dialogue history.

**Example:**
- NL: "Give the user an opinion about taxes in exactly 50 words."
- BrainCode: `ENTRYPOINT TaxesOpinion

TASK TaxesOpinion : STRING {
  GENERATE(target="response", audience="user", content="Respond to the user's view that taxes are bad.", quantity=50) -> response : STRING
  RETURN response
}`

*Introduced/last revised: sprint 7, version 6.0.0*
