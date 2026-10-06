# BrainCode Operator Glossary

One entry per construct in `language-spec.md`. Every entry has: a plain-language gloss (one or
two sentences, no jargon) and one worked example (NL → BrainCode). This file is what the
scripted doc-hygiene check enforces every attempt — a change with no gloss or no example is sent
back before the Critic even reads it (`braincode_loop/doc_hygiene.py`).


<!-- Format for each entry, written by the Documenter role (rewritten in place on `revise`):

### `<operator-name>`

**Gloss:** plain-language explanation.

**Example:**
- NL: "..."
- BrainCode: `...`

**Introduced/last revised:** sprint N, see `changelog.md#sprint-N`

-->

### `Types & Lexicon`

**Gloss:** Types & Lexicon defines BrainCode's five closed value types (NUMBER, STRING, BOOL, LIST[T], REF[T]), its token rules, and reserved words including GENERATE and REF.

**Example:**
- NL: "Rinse the mug in the sink, then put that same mug in the coffee maker."
- BrainCode: `ENTRYPOINT RinseThenPlace

TASK RinseThenPlace {
  ACTION rinse(target="mug", destination="sink") -> mug : REF[STRING]
  ACTION place(target=mug, destination="coffee_maker")
}`

**Introduced/last revised:** sprint 2, see `changelog.md#sprint-2`

### `Task`

**Gloss:** Task is a document-level container of steps with optional typed parameters, an execution-date context for resolving relative time expressions, an optional typed return, and provably terminating recursion guards. `CONTEXT execution_date=...` is written on the TASK line itself (never on ENTRYPOINT), is validated as an exact calendar date, and is kept in the source only as a translation-time record — nothing at runtime ever reads it again.

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

**Introduced/last revised:** sprint 6, see `changelog.md#sprint-6`

### `Action`

**Gloss:** Action provides normative operations to interact with external systems, each with a signature and a labeled result kind: SAME (the same real-world entity/collection, now moved or transformed, e.g. a rinsed mug or a re-sorted list), NEW (a freshly surfaced or produced entity, e.g. search results or slices), MEMBER (an item pulled out of an existing list, e.g. `extract`'s top result — already existed, just selected), or VALUE (a plain number/text/boolean, e.g. a support check or a page's read-out condition). It also fixes a checkable naming convention: a bound REF's IDENT must reflect the entity's own descriptor noun, so when the source text later says 'it' or 'the mug', the translator must reuse that same IDENT rather than restate a new string — with explicit, closed-set rules for pronouns, definite descriptions, first mentions requiring an acquiring step, and genuinely ambiguous duplicates.

**Example:**
- NL: "Rinse the mug in the sink, then put it in the coffee maker."
- BrainCode: `ENTRYPOINT RinseThenPlace

TASK RinseThenPlace {
  ACTION rinse(target="mug", destination="sink") -> mug : REF[STRING]
  ACTION place(target=mug, destination="coffee_maker")
}`

**Introduced/last revised:** sprint 9, see `changelog.md#sprint-9`

### `Utterance`

**Gloss:** Utterance (UTTER) is a pure, non-effectful speech-act record — speech-act type plus attributed content — legal only inside CONVO TURN bodies. Its optional `tone` attribute follows exactly Action's normalization rule and exact-match table (so "casually" deterministically becomes `tone="casual"`); any register that isn't an exact table hit, or that blends several facets, must instead use the separate `register_note` attribute rather than `tone` or `content`, and duplicate attributes on one UTTER are a static error just as on Action.

**Example:**
- NL: "User, casually: 'Hey, thanks so much for sorting that out today!'"
- BrainCode: `CONVO CasualThanks {
  TURN t1 SPEAKER=USER {
    UTTER acknowledge(content="Thanks so much for sorting that out today.", tone="casual", recipient="agent")
  }
}`

**Introduced/last revised:** sprint 3, see `changelog.md#sprint-3`

### `Check`

**Gloss:** Check: a pure, side-effect-free boolean expression — either a full typed comparison or a bare-value truthiness test — with fixed operator precedence, short-circuit evaluation, and comparison rules grounded in each operand's mandatory static type declaration.

**Example:**
- NL: "Only proceed if the cart total exceeds $50 and the user is a member, or the order is a gift, or there's a discount code."
- BrainCode: `LET cart_total : NUMBER = 65
LET is_member : BOOL = TRUE
LET is_gift : BOOL = FALSE
LET discount_code : STRING = ""
(cart_total > 50 AND is_member == TRUE) OR is_gift == TRUE OR discount_code`

**Introduced/last revised:** sprint 0, see `changelog.md#sprint-0`

### `Flow-If`

**Gloss:** Flow-If: branch execution on a Check, with an explicit optional ELSE arm and its own bounded per-branch variable scope, usable identically inside Task and Turn bodies. Its flagship example places `CONTEXT execution_date` on the TASK line (not on ENTRYPOINT) and uses `check_replied`'s fully-specified UTC-instant `deadline`.

**Example:**
- NL: "If my manager hasn't replied by Friday, send a polite follow-up; otherwise do nothing."
- BrainCode: `ENTRYPOINT FollowUpManager

TASK FollowUpManager CONTEXT execution_date="2025-06-03" {
  ACTION check_replied(target="manager", deadline="2025-06-06T23:59:59Z") -> replied : BOOL
  IF NOT replied THEN {
    ACTION send_email(recipient="manager", tone="polite", content="follow-up")
  }
}`

**Introduced/last revised:** sprint 6, see `changelog.md#sprint-6`

### `Iterate`

**Gloss:** Iterate: sequential FOR EACH looping over a statically LIST[T]-typed, therefore finite, collection with a fresh per-iteration variable scope, plus ANY/ALL pure quantifiers whose bound variable is scoped to a single check expression only — all under the shared no-shadowing rule.

**Example:**
- NL: "For each stop on the itinerary, book a hotel."
- BrainCode: `LET itinerary : LIST[STRING] = ["Paris", "Lyon", "Nice"]
FOR EACH stop IN itinerary {
  ACTION book_hotel(target=stop)
}`

**Introduced/last revised:** sprint 0, see `changelog.md#sprint-0`

### `Bind`

**Gloss:** Bind gives a value a name for later steps in the same allowed scope, now including the results of GENERATE steps alongside LET, Action, UTTER, and task_call, and fully incorporating REF[STRING] semantics.

**Example:**
- NL: "Rinse one mug in the sink, then place that same selected mug in the coffee maker."
- BrainCode: `ENTRYPOINT RinseThenPlace

TASK RinseThenPlace {
  ACTION rinse(target="mug", destination="sink") -> mug : REF[STRING]
  ACTION place(target=mug, destination="coffee_maker")
}`

**Introduced/last revised:** sprint 2, see `changelog.md#sprint-2`

### `Conversation`

**Gloss:** Conversation (CONVO/TURN): a document-level, ordered sequence of speaker-labeled turns, each holding effectful Actions and/or pure Utterances, with structurally-resolved REPLY_TO adjacency and a strictly linear, tip-only REVISES correction chain resolved by a defined `effective()` function.

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

**Introduced/last revised:** sprint 0, see `changelog.md#sprint-0`

### `types-lexicon`

**Gloss:** Deprecated entry; merged into Types & Lexicon.

**Example:**
- NL: "Deprecated."
- BrainCode: `ENTRYPOINT Deprecated

TASK Deprecated {}`

**Introduced/last revised:** sprint 2, see `changelog.md#sprint-2`

### `action`

**Gloss:** Deprecated entry; merged into Action.

**Example:**
- NL: "Deprecated."
- BrainCode: `ENTRYPOINT Deprecated

TASK Deprecated {}`

**Introduced/last revised:** sprint 2, see `changelog.md#sprint-2`

### `bind`

**Gloss:** Deprecated entry; merged into Bind.

**Example:**
- NL: "Deprecated."
- BrainCode: `ENTRYPOINT Deprecated

TASK Deprecated {}`

**Introduced/last revised:** sprint 2, see `changelog.md#sprint-2`

### `Generate`

**Gloss:** GENERATE produces a non-effectful value using only ordinary values such as text, numbers, booleans, and lists of them; it cannot create entity references. If quantity is present, it is an unsigned whole-number exact count: list items for a list result, or Unicode-defined words for a text result.

**Example:**
- NL: "Give the user an opinion about taxes in exactly 50 words."
- BrainCode: `ENTRYPOINT TaxesOpinion

TASK TaxesOpinion : STRING {
  GENERATE(target="response", audience="user", content="Respond to the user's view that taxes are bad.", quantity=50) -> response : STRING
  RETURN response
}`

**Introduced/last revised:** sprint 7, see `changelog.md#sprint-7`
