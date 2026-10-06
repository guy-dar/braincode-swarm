# BrainCode Language Specification

**Version:** 18.0.0
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
IDENT ::= [a-zA-Z_][a-zA-Z0-9_]*
STRING ::= "\"" ( [^"\\\n] | "\\\"" | "\\\\" | "\\n" | "\\t" | "\\u" HEXHEXHEXHEX )* "\""
NUMBER ::= "-"? [0-9]+ ( "." [0-9]+ )? ( ("e"|"E") ("+"|"-")? [0-9]+ )?
COMMENT ::= "#" through end of physical line.`

**Semantics:** As before, with one addition: a bare IDENT token that names a member of a defined vocabulary category (e.g. `role_manager`, `tone_urgent`, `art_itinerary`) is a **vocabulary symbol**. Lexically it is an IDENT (unquoted, no STRING escaping), but for all static typing purposes — RETURN type matching, LET's exact-type rule, Check comparisons, and LIST[T] element typing — a vocabulary symbol has static type STRING. This resolves the prior inconsistency where `LIST[STRING]` was declared to hold bare category symbols (e.g. itinerary stops as entity-name/location-name members) despite IDENT and STRING being distinct value forms: the rule makes that legal and precise rather than contradictory. A vocabulary symbol is never a STRING *literal* (it carries no quotes and cannot use string escapes) but it type-checks as STRING wherever STRING is required. Everything else in Types & Lexicon (REF[T], the four base types, `diff`) is unchanged.

**Example:**
- NL: "Plan a 3-day itinerary with two named stops."
- BrainCode: `LET stops : LIST[STRING] = [temple, garden]
GENERATE(target=art_itinerary, duration=3, duration_unit=unit_day, content="itinerary") -> plan : STRING`

*Introduced/last revised: sprint 18, version 11.0.0*

### `Task`

**Grammar:** `document ::= entrypoint (task | conversation)*
entrypoint ::= "ENTRYPOINT" IDENT
task ::= "TASK" IDENT param_list? ("CONTEXT" execution_date_param)? (":" type)? ("DECREASES" IDENT)? "{" step+ return_stmt? "}"
execution_date_param ::= "execution_date" "=" ISO_DATE
param_list ::= "(" param ("," param)* ")"
param ::= IDENT ":" type
return_stmt ::= "RETURN" value
step ::= action | flow_if | flow_for | bind | task_call | utterance | generation`

**Semantics:** TASK is Canonical Form's encoding for one supplied message requiring executable ACTION or GENERATE work. Its ENTRYPOINT and declaration name are PascalCase of the first executable-step HNR base with terminal _ref, _refs, and numeric suffix removed. Step order, attributes, decomposition, and result handles follow Canonical Form. CONTEXT remains a translation-time anchor and is required for relative dates. Existing parameter, return, recursion, and lexical-scope rules remain unchanged.

**Example:**
- NL: "Create a structured report about Peterhof."
- BrainCode: `ENTRYPOINT ArtStructuredReport

TASK ArtStructuredReport : STRING {
  GENERATE(target=art_structured_report, format=format_structured_report, topic=topic_peterhof) -> art_structured_report : STRING
  RETURN art_structured_report
}`

*Introduced/last revised: sprint 22, version 17.2.0*

### `Action`

**Grammar:** `action ::= "ACTION" operation-id "(" action-attrs? ")" ("->" IDENT ":" type)?
action-attrs ::= action-attr ("," action-attr)*
action-attr ::= attribute-name "=" value
operation-id ::= operation-vocabulary member`

**Semantics:** Action executes one external operation. AOR writes target first, then remaining attributes alphabetically; result handles follow Canonical Form HNR. search_web returns LIST[REF[STRING]] and accepts target plus availability, category, color, cuisine, currency, gender, genre, location, max_price, min_ram, min_rating, platform, ram_unit, reservation_availability, shape, size, and trending. Filtering criteria are always attributes of search_web; ranking is always a following sort(target=list, rank_field=search-value, rank_direction=search-value); selecting a ranked item is extract(target=list, limit=NUMBER); add_to_cart consumes the extracted selection. check_reservation_availability(target, [cuisine, location, max_price, currency]) returns BOOL. pick_up(target, [quantity, source, color, shape, state]) returns REF[STRING] when quantity is absent or 1 and LIST[REF[STRING]] when quantity is greater than 1. pick_up selects only an unbound entity descriptor; a visible REF must be consumed directly by place or a transform. place requires a REF target. rinse, heat, chill, slice, and pour require and return the same REF identity.

**Example:**
- NL: "On the electronics store, filter laptops to 16 GB RAM or more under $1,200, and add the best-rated one to the cart."
- BrainCode: `ACTION search_web(currency=curr_usd, max_price=1200, min_ram=16, ram_unit=cap_gb, target=laptop) -> laptop_refs : LIST[REF[STRING]]
ACTION sort(target=laptop_refs, rank_direction=dir_desc, rank_field=rank_rating) -> sorted_laptop_refs : LIST[REF[STRING]]
ACTION extract(limit=1, target=sorted_laptop_refs) -> laptop_refs_2 : LIST[REF[STRING]]
ACTION add_to_cart(target=laptop_refs_2)`

*Introduced/last revised: sprint 22, version 17.2.0*

### `Utterance`

**Grammar:** `utterance ::= "UTTER" speech-act "(" utter-attr ("," utter-attr)* ")" ("->" IDENT)?
speech-act ::= operation-vocabulary member
utter-attr ::= attribute-name "=" value`

**Semantics:** UTTER records one speech act inside a CONVO TURN. Legal attributes are audience, constraints, content, recipient, target, tone, and topic; attributes follow AOR. recipient and audience require recipient-value, tone requires tone-value, constraints requires LIST[constraint-value], and topic requires topic-value. content remains a transitional STRING channel. A bound result is STRING and follows HNR. Canonical Form emits separate UTTER steps for separate independently scoped speech acts in one supplied message.

**Example:**
- NL: "What is the surface texture of oil-rig gratings, and how would you describe their specular highlights?"
- BrainCode: `CONVO Ask {
  TURN t1 SPEAKER=USER {
    UTTER ask(topic=topic_oil_rig_grating_surface_texture)
    UTTER ask(topic=topic_oil_rig_grating_specular_highlights)
  }
}`

*Introduced/last revised: sprint 22, version 17.2.0*

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

**Semantics:** Conditional branching, used identically inside TASK and CONVO TURN bodies. The Check is evaluated first, at the moment control reaches the IF. If true, THEN's steps execute in order; if false and ELSE is present, its steps execute instead; if false with no ELSE, control passes to the following step. Flow-If may nest inside another Flow-If or a FOR-EACH body; nested Checks evaluate only when control actually reaches them. THEN and ELSE each open a fresh child scope: a binding inside THEN is invisible in ELSE, after the IF, or to siblings, and vice versa. An IF nested inside a TURN body may contain UTTER in its branches exactly as it may contain ACTION; the same nesting inside a TASK body remains a static error per Utterance's restriction. When a Check depends on a preceding `check_replied` with a future `deadline`, the branch inherits that deferred timing.

**Example:**
- NL: "If my manager hasn't replied by Friday, send a polite follow-up; otherwise do nothing."
- BrainCode: `ENTRYPOINT FollowUpManager

TASK FollowUpManager CONTEXT execution_date="2025-06-03" {
  ACTION check_replied(target=role_manager, deadline="2025-06-06T23:59:59Z") -> replied : BOOL
  IF NOT replied THEN {
    ACTION send_email(recipient=role_manager, tone=tone_polite, content="follow-up")
  }
}`

*Introduced/last revised: sprint 18, version 10.1.0*

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
turn ::= "TURN" IDENT "SPEAKER" "=" speaker_lit ("REPLY_TO" IDENT )? ("REVISES" IDENT )? "{" step+ "}"
speaker_lit ::= "USER" | "AGENT"`

**Semantics:** CONVO is Canonical Form's encoding for a speech-only single message or any supplied multi-message transcript. It has exactly one TURN per supplied message, named t1, t2, ... in supplied order. A TURN may contain multiple ordered UTTER steps when one supplied message contains independently scoped speech acts; Canonical Form's speech-act clause rule determines those boundaries. The CONVO and ENTRYPOINT names use the first executable-step base. Explicit replacement uses REVISES the earlier lineage tip; all other later turns use REPLY_TO the preceding turn. Existing whole-body replacement, linear revision-chain, and per-turn scope rules remain unchanged.

**Example:**
- NL: "What is your view on friendship? How do I become a good friend?"
- BrainCode: `ENTRYPOINT Ask

CONVO Ask {
  TURN t1 SPEAKER=USER {
    UTTER ask(topic=topic_friendship)
    UTTER ask(topic=topic_becoming_good_friend)
  }
}`

*Introduced/last revised: sprint 22, version 17.2.0*

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

**Grammar:** `generation ::= "GENERATE" "(" generate-attr ("," generate-attr)* ")" "->" IDENT ":" gen_type
generate-attr ::= attribute-name "=" value
gen_type ::= "NUMBER" | "STRING" | "BOOL" | "LIST" "[" gen_type "]"`

**Semantics:** Legal Generate attributes: target, audience, content, duration, duration_unit, format, locale, quantity, style, tone, stop_min_per_day, max_walk_duration, max_walk_duration_unit. `target`'s value is an artifact-value symbol (GENERATE always produces an artifact, never an entity; Action.target stays entity-name/artifact-value split by construct, not by attribute name). `audience` -> recipient-value. `tone` -> tone-value. `format` -> format-value. `duration_unit`/`max_walk_duration_unit` -> duration-unit-value. `style` -> style-value. `locale` -> locale-value. `duration`, `quantity`, `stop_min_per_day`, `max_walk_duration` are NUMBER. `stop_min_per_day` expresses a minimum-count-per-day constraint (e.g. at least one temple per day); `max_walk_duration`+`max_walk_duration_unit` express a maximum-walking-time-between-stops constraint. Canonical ordering: target first, then optional attributes alphabetically. Handle rule unchanged. `content` remains a transitional STRING channel pending N4.

**Example:**
- NL: "Plan a 3-day Kyoto itinerary that includes at least one temple per day and avoids more than a 20-minute walk from the last stop."
- BrainCode: `ENTRYPOINT PlanKyotoItinerary
TASK PlanKyotoItinerary : STRING {
  GENERATE(target=art_itinerary, content="Kyoto itinerary", duration=3, duration_unit=unit_day, stop_min_per_day=1, max_walk_duration=20, max_walk_duration_unit=unit_minute) -> plan : STRING
  RETURN plan
}`

*Introduced/last revised: sprint 18, version 11.0.0*

### `descriptive-value`

**Grammar:** `-- unchanged as a vocabulary category (no grammar production)`

**Semantics:** A narrowed residual bucket now covering only entity modifiers (`mod_`) and genuinely unclassified domain concepts (`dom_`) that have no dedicated category yet. `state`, `style`, `locale`, and `metric` are retired from this category — use state-value, style-value, locale-value, and metric-value respectively. `role_`, `tone_`, `curr_`, `art_`, and `unit_` were already retired in a prior sprint.

**Example:**
- NL: "Plan a safari."
- BrainCode: `GENERATE(target=art_plan, content="Plan a safari", style=style_narrative) -> plan : STRING`

*Introduced/last revised: sprint 18, version 11.0.0*

### `canonical-form`

**Grammar:** `-- No independent production. Normative translation rules for document selection, operation selection, ordering, decomposition, handles, and transcript structure.`

**Semantics:** Canonical Form applies to the complete supplied input. One supplied message requiring ACTION or GENERATE emits one TASK; one supplied message containing only speech acts emits one CONVO; two or more supplied messages emit one CONVO with one TURN per supplied message in order. TURN names are t1, t2, .... A replacement message uses REVISES the current lineage tip; every other later message uses REPLY_TO the immediately preceding turn. AOR writes target first when present, then remaining attributes in ASCII alphabetical order. SOR places every producer before its consumer; otherwise preserves source-clause order. HNR: scalar REF Action results use <target>_ref, LIST[REF] results use <target>_refs, Generate results use target, task-call results use callee, and bound UTTER results use speech-act; repeated bases receive _2, _3, .... A direct placement of an unbound entity expands to pick_up then place. Once a REF is bound, every later move or transform of that same entity consumes that REF; pick_up may not reacquire a visible REF. Explicit multiplicity emits pick_up(quantity=N) returning LIST[REF[STRING]], followed by FOR EACH <target>_ref IN <target>_refs; no repeated indistinguishable scalar acquisition is emitted. rinse, heat, chill, slice, and pour preserve their input REF identity; an unstated required resource uses resource_sink, resource_heater, or resource_chiller. A single message with multiple independently scoped speech acts emits one UTTER per speech-act clause in source order, including clauses joined by and, then, or numbered questions; punctuation alone does not split an otherwise single speech act. OSR first matches maximal listed operation-vocabulary synonym spans; ties select the lexicographically smallest operation symbol. Coordination produces one operation per matched predicate span, negated predicates are represented only through an existing governed constraint or Check, and noun-derived imperatives without a listed operation are rejected. A custom operation is permitted only for a single uncoordinated affirmative imperative whose predicate is exactly one ASCII token matching [a-z]+ and has an explicit target. Its symbol is custom_general_<predicate>; its defined meaning is one atomic external general-domain action named by that predicate, with target required, governed matching attributes only, no result, and no implied decomposition. Predicates containing digits, non-ASCII letters, punctuation, multiple words, negation, or coordination are translation errors unless a listed operation represents them. Relative dates require TASK CONTEXT execution_date.

**Example:**
- NL: "Put two pillows from the sofa onto the armchair."
- BrainCode: `ENTRYPOINT Pillow

TASK Pillow {
  ACTION pick_up(quantity=2, source=sofa, target=pillow) -> pillow_refs : LIST[REF[STRING]]
  FOR EACH pillow_ref IN pillow_refs {
    ACTION place(destination=armchair, target=pillow_ref)
  }
}`

*Introduced/last revised: sprint 22, version 17.2.0*
