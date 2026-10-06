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

**Gloss:** A bare glossary symbol like role_manager or tone_urgent is written without quotes, but for type-checking it counts as a STRING — so a list of such symbols can be typed LIST[STRING] without contradiction.

**Example:**
- NL: "Plan a 3-day itinerary with two named stops."
- BrainCode: `LET stops : LIST[STRING] = [temple, garden]
GENERATE(target=art_itinerary, duration=3, duration_unit=unit_day, content="itinerary") -> plan : STRING`

**Introduced/last revised:** sprint 18, see `changelog.md#sprint-18`

### `Task`

**Gloss:** Task holds one executable request. Canonical Form fixes its declaration name, action order, attributes, and result handles.

**Example:**
- NL: "Create a structured report about Peterhof."
- BrainCode: `ENTRYPOINT ArtStructuredReport

TASK ArtStructuredReport : STRING {
  GENERATE(target=art_structured_report, format=format_structured_report, topic=topic_peterhof) -> art_structured_report : STRING
  RETURN art_structured_report
}`

**Introduced/last revised:** sprint 22, see `changelog.md#sprint-22`

### `Action`

**Gloss:** Action performs one external operation with governed attributes. Search filters, ranking, selection, multiplicity, and object-reference use have fixed canonical forms.

**Example:**
- NL: "On the electronics store, filter laptops to 16 GB RAM or more under $1,200, and add the best-rated one to the cart."
- BrainCode: `ACTION search_web(currency=curr_usd, max_price=1200, min_ram=16, ram_unit=cap_gb, target=laptop) -> laptop_refs : LIST[REF[STRING]]
ACTION sort(target=laptop_refs, rank_direction=dir_desc, rank_field=rank_rating) -> sorted_laptop_refs : LIST[REF[STRING]]
ACTION extract(limit=1, target=sorted_laptop_refs) -> laptop_refs_2 : LIST[REF[STRING]]
ACTION add_to_cart(target=laptop_refs_2)`

**Introduced/last revised:** sprint 22, see `changelog.md#sprint-22`

### `Utterance`

**Gloss:** Utterance records one conversational speech act. Separate requests in the same message are retained as separate ordered utterances.

**Example:**
- NL: "What is the surface texture of oil-rig gratings, and how would you describe their specular highlights?"
- BrainCode: `CONVO Ask {
  TURN t1 SPEAKER=USER {
    UTTER ask(topic=topic_oil_rig_grating_surface_texture)
    UTTER ask(topic=topic_oil_rig_grating_specular_highlights)
  }
}`

**Introduced/last revised:** sprint 22, see `changelog.md#sprint-22`

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

**Gloss:** Flow-If lets a task branch on a Check: it runs the THEN block if the Check is true, otherwise the optional ELSE block, each in its own fresh variable scope, and works identically inside Task bodies and conversation Turn bodies.

**Example:**
- NL: "If my manager hasn't replied by Friday, send a polite follow-up; otherwise do nothing."
- BrainCode: `ENTRYPOINT FollowUpManager

TASK FollowUpManager CONTEXT execution_date="2025-06-03" {
  ACTION check_replied(target=role_manager, deadline="2025-06-06T23:59:59Z") -> replied : BOOL
  IF NOT replied THEN {
    ACTION send_email(recipient=role_manager, tone=tone_polite, content="follow-up")
  }
}`

**Introduced/last revised:** sprint 18, see `changelog.md#sprint-18`

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

**Gloss:** Conversation records supplied messages in fixed order. A message can contain several ordered speech acts, so distinct coordinated questions are not lost.

**Example:**
- NL: "What is your view on friendship? How do I become a good friend?"
- BrainCode: `ENTRYPOINT Ask

CONVO Ask {
  TURN t1 SPEAKER=USER {
    UTTER ask(topic=topic_friendship)
    UTTER ask(topic=topic_becoming_good_friend)
  }
}`

**Introduced/last revised:** sprint 22, see `changelog.md#sprint-22`

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

**Gloss:** GENERATE builds a non-effectful artifact; its target names the artifact kind (from artifact-value), and constraints like a minimum stops-per-day or a maximum walking time are now first-class numeric attributes instead of hidden inside prose content.

**Example:**
- NL: "Plan a 3-day Kyoto itinerary that includes at least one temple per day and avoids more than a 20-minute walk from the last stop."
- BrainCode: `ENTRYPOINT PlanKyotoItinerary
TASK PlanKyotoItinerary : STRING {
  GENERATE(target=art_itinerary, content="Kyoto itinerary", duration=3, duration_unit=unit_day, stop_min_per_day=1, max_walk_duration=20, max_walk_duration_unit=unit_minute) -> plan : STRING
  RETURN plan
}`

**Introduced/last revised:** sprint 18, see `changelog.md#sprint-18`

### `descriptive-value`

**Gloss:** descriptive-value is now a small, explicitly residual bucket for entity modifiers and truly unclassified domain concepts only — every other kind of descriptive word has its own dedicated category.

**Example:**
- NL: "Plan a safari."
- BrainCode: `GENERATE(target=art_plan, content="Plan a safari", style=style_narrative) -> plan : STRING`

**Introduced/last revised:** sprint 18, see `changelog.md#sprint-18`

### `canonical-form`

**Gloss:** Canonical Form is the fixed translation rulebook for BrainCode. It fixes document shape, ordering, names, action decomposition, multiplicity, and how synonymous wording maps to one expression.

**Example:**
- NL: "Put two pillows from the sofa onto the armchair."
- BrainCode: `ENTRYPOINT Pillow

TASK Pillow {
  ACTION pick_up(quantity=2, source=sofa, target=pillow) -> pillow_refs : LIST[REF[STRING]]
  FOR EACH pillow_ref IN pillow_refs {
    ACTION place(destination=armchair, target=pillow_ref)
  }
}`

**Introduced/last revised:** sprint 22, see `changelog.md#sprint-22`

## Vocabulary

The descriptive lexicon: every category of symbol an expression may use besides the constructs above (actions, objects, roles, attributes and their allowed values, literal forms). Closed categories list every member; open categories list representative members plus the rule that defines membership.

### `structural-word` (vocabulary)

**Gloss:** The closed inventory of BrainCode keywords, operators, delimiters, and lexical forms.

**Category:** closed — the members below are exhaustive

**Members:**
- `TASK` — Declares a task.
- `ACTION` — Executes an external operation.
- `GENERATE` — Generates a non-effectful artifact.
- `UTTER` — Records a speech act.
- `CONVO` — Declares a conversation.
- `TURN` — Declares a conversation turn.
- `ENTRYPOINT` — Names the single execution root.
- `IF` — Starts a conditional branch.
- `THEN` — Starts the true branch.
- `ELSE` — Starts the false branch.
- `FOR` — Starts iteration.
- `EACH` — Marks per-member iteration.
- `IN` — Introduces an iterable or relation.
- `ANY` — Existential quantifier.
- `ALL` — Universal quantifier.
- `SATISFIES` — Introduces a quantifier condition.
- `LET` — Binds a value.
- `RETURN` — Returns a task value.
- `NUMBER` — Numeric type.
- `STRING` — Text type.
- `BOOL` — Boolean type.
- `LIST` — List type.
- `REF` — Runtime entity-reference type.
- `TRUE` — Boolean true literal.
- `FALSE` — Boolean false literal.
- `SPEAKER` — Speaker label.
- `USER` — User speaker.
- `AGENT` — Agent speaker.
- `REPLY_TO` — Turn adjacency.
- `REVISES` — Turn correction.
- `DECREASES` — Recursion guard.
- `CONTEXT` — Task context.
- `AND` — Logical AND.
- `OR` — Logical OR.
- `NOT` — Logical NOT.
- `{` — Block start.
- `}` — Block end.
- `(` — Paren start.
- `)` — Paren end.
- `[` — Bracket start.
- `]` — Bracket end.
- `,` — Separator.
- `:` — Type annotator.
- `=` — Assignment.
- `->` — Result bind.
- `==` — Equality.
- `!=` — Inequality.
- `<` — Less-than.
- `<=` — Less-or-equal.
- `>` — Greater-than.
- `>=` — Greater-or-equal.
- `-` — Arithmetic difference.

**Membership rule:** Lexical rules: IDENT is `[a-zA-Z_][a-zA-Z0-9_]*` excluding reserved words. NUMBER is `-? [0-9]+ ( \. [0-9]+ )? ( [eE] [+-]? [0-9]+ )?`. STRING is `"` followed by any chars except unescaped `"` and `\`, escaping with `\"`, `\\`, `\n`, `\t`, `\uXXXX`, closed by `"`. COMMENT is `#` to line end. ISO_DATE is exactly `YYYY-MM-DD`. UTC_TIMESTAMP is `YYYY-MM-DDThh:mm:ssZ`. Whitespace separates tokens. Every retained lexical punctuation/form used by the full grammar is either a structural-word member or covered by these named lexical rules.

**Example:**
- NL: "Return the number 5."
- BrainCode: `ENTRYPOINT SimpleTask
TASK SimpleTask : NUMBER {
  LET five : NUMBER = 5
  RETURN five
}`

**Introduced/last revised:** sprint 17, see `changelog.md#sprint-17`

### `operation-vocabulary` (vocabulary)

**Gloss:** Operation-vocabulary contains canonical symbols for external actions and speech acts. Listed synonyms always map to one listed symbol; custom operations use the restricted Canonical Form rule.

**Category:** open — the members below are representative

**Members:**
- `open_page` — Navigate to a page. (natural-language synonyms: go to)
- `click` — Click an element.
- `select_filter` — Apply one filter.
- `apply_filters` — Apply multiple filters.
- `sort` — Rank a list. (natural-language synonyms: rank, order by)
- `search_travel` — Search travel.
- `search_transit` — Search transit.
- `search_web` — Search a catalog or web source. (natural-language synonyms: find, look for)
- `pick_up` — Acquire an entity. (natural-language synonyms: grab, take, retrieve)
- `place` — Place an acquired entity. (natural-language synonyms: put, insert)
- `rinse` — Rinse an entity. (natural-language synonyms: wash)
- `heat` — Heat an entity.
- `chill` — Chill an entity.
- `slice` — Cut an entity into pieces. (natural-language synonyms: chop, cut)
- `pour` — Pour a liquid.
- `modify_code` — Change source code. (natural-language synonyms: fix, reduce, optimize)
- `run_tests` — Run tests.
- `add_to_cart` — Add a selected item to a cart.
- `check_reservation_availability` — Check whether reservations are available. (natural-language synonyms: check reservation availability)
- `send_email` — Send email. (natural-language synonyms: email)
- `send_message` — Send a message. (natural-language synonyms: text)
- `ask` — Ask for information or advice. (natural-language synonyms: ask, how should)
- `inform` — State information.
- `respond` — Answer a request. (natural-language synonyms: answer)
- `propose` — Propose an idea.
- `correct` — Correct a statement.
- `acknowledge` — Acknowledge a statement.
- `confirm` — Confirm a statement.
- `decline` — Decline a request.

**Membership rule:** All previously listed operation members remain legal canonical members. A missing operation may be emitted only under Canonical Form OSR as custom_general_<predicate>, where predicate is exactly one ASCII token matching [a-z]+ from a single affirmative uncoordinated imperative with an explicit target. The custom symbol denotes one atomic external general-domain action, requires target, permits only governed attributes, has no result, and is never a synonym for a listed member. All other unmatched predicates are translation errors until a glossary operation is added.

**Example:**
- NL: "Check reservation availability for an Indian restaurant."
- BrainCode: `ACTION check_reservation_availability(cuisine=cuisine_indian, target=restaurant) -> reservation_available : BOOL`

**Introduced/last revised:** sprint 22, see `changelog.md#sprint-22`

### `attribute-name` (vocabulary)

**Gloss:** Attribute-name indexes legal named arguments and the category or literal form accepted by each. Search criteria have dedicated names so filtering and ranking are not hidden in custom operations.

**Category:** open — the members below are representative

**Members:**
- `target` — The acted-on entity or generated artifact.
- `cuisine` — Restaurant or food cuisine from cuisine-value.
- `min_ram` — Minimum RAM capacity as NUMBER. (natural-language synonyms: RAM or more, at least RAM)
- `ram_unit` — Unit for min_ram from capacity-unit-value.
- `reservation_availability` — Required reservation state from reservation-status-value.
- `rank_field` — Field used by sort from search-value.
- `rank_direction` — Sort direction from search-value.
- `quantity` — Explicit count as NUMBER.

**Membership rule:** All existing attribute-name members and their existing governing categories remain valid. min_ram requires NUMBER and ram_unit requires capacity-unit-value; cuisine requires cuisine-value; reservation_availability requires reservation-status-value. rank_field and rank_direction are legal only on sort. quantity is legal on pick_up and GENERATE only where that operation signature permits it.

**Example:**
- NL: "Find laptops with at least 16 GB RAM."
- BrainCode: `ACTION search_web(min_ram=16, ram_unit=cap_gb, target=laptop) -> laptop_refs : LIST[REF[STRING]]`

**Introduced/last revised:** sprint 22, see `changelog.md#sprint-22`

### `entity-name` (vocabulary)

**Gloss:** Entity-name names selectable objects, places, services, and canonical abstract resources used by Actions. Resource symbols make implicit household equipment explicit and consistent.

**Category:** open — the members below are representative

**Members:**
- `mug` — Drinking cup. (natural-language synonyms: mug)
- `sink` — Washing basin. (natural-language synonyms: sink)
- `resource_sink` — Canonical abstract washing resource when no particular sink is named.
- `resource_heater` — Canonical abstract heating resource when no particular appliance is named.
- `resource_chiller` — Canonical abstract chilling resource when no particular appliance is named.

**Membership rule:** An entity-name is an atomic [a-z_]+ symbol denoting a selectable entity kind or canonical action resource. resource_sink, resource_heater, and resource_chiller are reserved canonical resources and may only be emitted by Canonical Form when the corresponding requested transform lacks a named resource.

**Example:**
- NL: "Put a warm glass on the shelf."
- BrainCode: `ACTION pick_up(target=glass) -> glass_ref : REF[STRING]
ACTION heat(destination=resource_heater, target=glass_ref) -> heat : REF[STRING]
ACTION place(destination=shelf, relation=on, target=heat)`

**Introduced/last revised:** sprint 22, see `changelog.md#sprint-22`

### `search-value` (vocabulary)

**Gloss:** Canonical namespaced values for ranking, sort-direction, genre, category, and availability attributes (currency now lives exclusively in currency-value).

**Category:** open — the members below are representative

**Members:**
- `rank_price` — Rank or filter field: monetary cost. (natural-language synonyms: cheapest, lowest price)
- `rank_rating` — Rank or filter field: user or critic score.
- `rank_distance` — Rank field: proximity. (natural-language synonyms: nearest, closest)
- `dir_asc` — Ascending rank direction. (natural-language synonyms: lowest first)
- `dir_desc` — Descending rank direction. (natural-language synonyms: highest first)
- `cat_game` — Category: video game.
- `cat_limited_time_offers` — Category: time-limited deals.
- `avail_in_stock` — Available for purchase now. (natural-language synonyms: available)
- `avail_out_of_stock` — Unavailable for purchase now. (natural-language synonyms: sold out)
- `genre_comedy` — Genre: comedy.

**Membership rule:** Members are prefixed by `rank_`, `dir_`, `genre_`, `cat_`, `avail_`, each an atomic `[a-z_]+` suffix. Currency no longer belongs here; use currency-value.

**Example:**
- NL: "Find the highest-rated in-stock comedy game."
- BrainCode: `ACTION search_web(target=game, genre=genre_comedy, category=cat_game, availability=avail_in_stock) -> games : LIST[REF[STRING]]
ACTION sort(target=games, rank_field=rank_rating, rank_direction=dir_desc) -> sorted_games : LIST[REF[STRING]]`

**Introduced/last revised:** sprint 18, see `changelog.md#sprint-18`

### `spatial-relation` (vocabulary)

**Gloss:** The closed set of relations used when placing one entity relative to another.

**Category:** closed — the members below are exhaustive

**Members:**
- `in` — Contained within. (natural-language synonyms: inside)
- `on` — Resting atop. (natural-language synonyms: on top of)
- `under` — Beneath. (natural-language synonyms: below)
- `next_to` — Adjacent to. (natural-language synonyms: beside)
- `left_of` — To the left of. (natural-language synonyms: left of)
- `right_of` — To the right of. (natural-language synonyms: right of)
- `in_front_of` — Positioned in front of. (natural-language synonyms: in front of)
- `behind` — Positioned behind.

**Example:**
- NL: "Put the bowl right of the spoon."
- BrainCode: `ACTION pick_up(target=bowl) -> bowl : REF[STRING]
ACTION pick_up(target=spoon) -> spoon : REF[STRING]
ACTION place(target=bowl, destination=spoon, relation=right_of)`

**Introduced/last revised:** sprint 17, see `changelog.md#sprint-17`

### `platform-name` (vocabulary)

**Gloss:** Canonical platform, brand, and software environment names.

**Category:** open — the members below are representative

**Members:**
- `netflix` — Streaming platform.
- `django` — Web framework.
- `sklearn` — Machine learning library.
- `youtube` — Video platform.

**Membership rule:** An atomic symbol matching `[a-z_]+` representing a software platform, service, or brand.

**Example:**
- NL: "Find comedy tv shows on netflix."
- BrainCode: `ACTION search_web(target=tv_show, genre=genre_comedy, platform=netflix) -> tv_shows : LIST[REF[STRING]]`

**Introduced/last revised:** sprint 17, see `changelog.md#sprint-17`

### `location-name` (vocabulary)

**Gloss:** Canonical physical and conceptual locations, positions, and areas.

**Category:** open — the members below are representative

**Members:**
- `corner` — A corner area.
- `table` — A table surface.
- `eastern_cape` — Eastern Cape region.
- `japan` — Country of Japan.

**Membership rule:** An atomic symbol matching `[a-z_]+` representing a physical or conceptual location, position, or area.

**Example:**
- NL: "Place it on the table in the corner."
- BrainCode: `ACTION place(target=apple_slice, destination=table, location=corner, relation=on)`

**Introduced/last revised:** sprint 17, see `changelog.md#sprint-17`

### `descriptive-value` (vocabulary)

**Gloss:** Descriptive-value is only a residual category for entity modifiers and genuinely unclassified domain concepts. It does not contain states, tones, roles, currencies, artifact types, units, styles, locales, or metrics because each has its own category.

**Category:** open — the members below are representative

**Members:**
- `mod_mixed_case` — Mixed-case modifier. (natural-language synonyms: mixed case)
- `dom_safari` — Safari domain concept. (natural-language synonyms: safari)
- `dom_pain` — Pain domain concept. (natural-language synonyms: pain)
- `dom_ovr` — One-versus-rest domain concept.
- `dom_sgi` — SGI domain concept.

**Membership rule:** Members use mod_ for an entity modifier or dom_ for a domain concept not yet assigned a dedicated category. state_, style_, locale_, metric_, role_, tone_, curr_, art_, and unit_ are invalid here and must use their dedicated categories.

**Example:**
- NL: "Generate a narrative safari plan."
- BrainCode: `GENERATE(target=art_plan, content="safari", style=style_narrative) -> plan : STRING`

**Introduced/last revised:** sprint 19, see `changelog.md#sprint-19`

### `format-value` (vocabulary)

**Gloss:** Format-value gives canonical output layout symbols for GENERATE. Report layouts use one explicit report-format symbol rather than an undefined format word.

**Category:** open — the members below are representative

**Members:**
- `format_plain_text` — Unstructured prose text. (natural-language synonyms: plain text)
- `format_bullet_list` — Bulleted list. (natural-language synonyms: bullet points)
- `format_numbered_list` — Numbered list. (natural-language synonyms: numbered steps)
- `format_email` — Email layout. (natural-language synonyms: as an email)
- `format_markdown` — Markdown layout. (natural-language synonyms: in markdown)
- `format_table` — Tabular layout. (natural-language synonyms: as a table)
- `format_pdf` — PDF document. (natural-language synonyms: as a pdf)
- `format_newsletter` — Newsletter layout. (natural-language synonyms: newsletter)
- `format_structured_report` — Headed structured report layout. (natural-language synonyms: structured report, report)

**Membership rule:** format-value is closed for encoding: a translator may emit only a listed format symbol. A missing layout is a language gap and must be added to the glossary before use.

**Example:**
- NL: "Make a structured report."
- BrainCode: `GENERATE(target=art_structured_report, format=format_structured_report, topic=topic_peterhof) -> art_structured_report : STRING`

**Introduced/last revised:** sprint 22, see `changelog.md#sprint-22`

### `tone-value` (vocabulary)

**Gloss:** The closed set of register/tone symbols usable wherever an attribute calls for a tone (Action's tone, UTTER's tone, GENERATE's tone).

**Category:** closed — the members below are exhaustive

**Members:**
- `tone_polite` — Courteous, respectful register. (natural-language synonyms: politely, kindly)
- `tone_formal` — Formal register. (natural-language synonyms: formally)
- `tone_casual` — Informal register. (natural-language synonyms: casually)
- `tone_concise` — Brief, to-the-point register. (natural-language synonyms: briefly, concisely)
- `tone_neutral` — Plain, unmarked register.
- `tone_urgent` — Conveys urgency. (natural-language synonyms: urgently, ASAP)
- `tone_empathetic` — Conveys empathy/understanding. (natural-language synonyms: sympathetically)
- `tone_professional` — Workplace-appropriate register. (natural-language synonyms: professionally)

**Example:**
- NL: "Send an urgent email to the manager."
- BrainCode: `ACTION send_email(recipient=role_manager, tone=tone_urgent, content="status update request")`

**Introduced/last revised:** sprint 18, see `changelog.md#sprint-18`

### `duration-unit-value` (vocabulary)

**Gloss:** This category supplies canonical units for durations and generated-output quantities. unit_character counts output characters deterministically.

**Category:** closed — the members below are exhaustive

**Members:**
- `unit_second` — Second. (natural-language synonyms: seconds, sec)
- `unit_minute` — Minute. (natural-language synonyms: minutes, min)
- `unit_hour` — Hour. (natural-language synonyms: hours)
- `unit_day` — Day. (natural-language synonyms: days)
- `unit_week` — Week. (natural-language synonyms: weeks)
- `unit_month` — Month. (natural-language synonyms: months)
- `unit_year` — Year. (natural-language synonyms: years)
- `unit_word` — Rendered whitespace-delimited word. (natural-language synonyms: words)
- `unit_item` — Top-level generated list or report item. (natural-language synonyms: items, entries)
- `unit_paragraph` — Paragraph of text. (natural-language synonyms: paragraphs, paragraph)
- `unit_character` — One Unicode scalar value in the final rendered artifact; line endings are normalized to LF before counting. (natural-language synonyms: characters, chars)

**Example:**
- NL: "Create a dialogue longer than 4,500 characters."
- BrainCode: `GENERATE(target=art_dialogue, quantity=4500, quantity_unit=unit_character) -> art_dialogue_ref : STRING`

**Introduced/last revised:** sprint 22, see `changelog.md#sprint-22`

### `currency-value` (vocabulary)

**Gloss:** Canonical currency-code symbols for monetary attributes such as currency and budget. Each symbol provides the unit for a numeric monetary amount.

**Category:** open — the members below are representative

**Members:**
- `curr_usd` — United States dollar. (natural-language synonyms: $, usd, dollars)
- `curr_eur` — Euro. (natural-language synonyms: eur, euros)
- `curr_clp` — Chilean peso. (natural-language synonyms: clp, Chilean pesos, Chilean peso)

**Membership rule:** An atomic symbol matching curr_[a-z]{3} naming an ISO-4217-style currency code. A currency-valued binding is valid only when it retains currency-value provenance.

**Example:**
- NL: "Set a budget of 1 million Chilean pesos."
- BrainCode: `UTTER inform(budget=1000000, currency=curr_clp, recipient=role_agent, target=art_itinerary)`

**Introduced/last revised:** sprint 19, see `changelog.md#sprint-19`

### `recipient-value` (vocabulary)

**Gloss:** Canonical role/recipient symbols for the recipient and audience attributes.

**Category:** open — the members below are representative

**Members:**
- `role_user` — The requesting human. (natural-language synonyms: me, I)
- `role_agent` — The assistant. (natural-language synonyms: you, the assistant)
- `role_manager` — The user's manager. (natural-language synonyms: my manager, boss)
- `role_professor` — The user's professor/instructor. (natural-language synonyms: my professor, teacher)
- `role_friend` — A friend of the user. (natural-language synonyms: my friend)
- `role_colleague` — A coworker of the user. (natural-language synonyms: my colleague, coworker)
- `role_support_team` — A customer-support team. (natural-language synonyms: support, customer service)
- `role_customer` — A customer/client of the user. (natural-language synonyms: the customer, client)

**Membership rule:** An atomic symbol matching `role_[a-z_]+` naming a person-role, class, or audience type. For a specific named individual not covered by any role symbol (e.g. a personal name like 'John'), a quoted STRING remains a transitional exception — exactly as entity-name allows for physical objects — pending a dedicated proper-name literal category under N5; a role_ symbol must be used instead whenever one applies. This preserves existing coverage of named recipients rather than making them inexpressible.

**Example:**
- NL: "Send an urgent email to the manager."
- BrainCode: `ACTION send_email(recipient=role_manager, tone=tone_urgent, content="status update request")`

**Introduced/last revised:** sprint 18, see `changelog.md#sprint-18`

### `artifact-value` (vocabulary)

**Gloss:** The canonical set of generated-artifact-type symbols usable as GENERATE's target attribute.

**Category:** open — the members below are representative

**Members:**
- `art_story` — Narrative story.
- `art_short_text` — Short free text.
- `art_plan` — Actionable plan.
- `art_structured_report` — Headed/structured report.
- `art_technical_explanation` — Technical explanation of a concept.
- `art_character_profile` — Descriptive character profile.

**Membership rule:** An atomic symbol matching `art_[a-z_]+` naming a class of generated artifact (document type, narrative form, structured output). Per N6, assume the complete glossary already contains the needed artifact member for a given request; a genuinely new artifact type is added as a new member in a future sprint, never expressed as free text.

**Example:**
- NL: "Explain the importance of nonparametric control charts."
- BrainCode: `GENERATE(target=art_technical_explanation, content="Explain the importance of nonparametric control charts for process mean and variability monitoring") -> explanation : STRING`

**Introduced/last revised:** sprint 18, see `changelog.md#sprint-18`

### `product-attribute-value` (vocabulary)

**Gloss:** Canonical color, size, and gender/demographic-audience symbols for product search and filtering attributes.

**Category:** open — the members below are representative

**Members:**
- `color_yellow` — Yellow.
- `color_red` — Red.
- `color_black` — Black.
- `color_white` — White.
- `size_small` — Small size. (natural-language synonyms: small, S)
- `size_medium` — Medium size. (natural-language synonyms: medium, M)
- `size_large` — Large size. (natural-language synonyms: large, L)
- `gender_women` — Women's/female-targeted. (natural-language synonyms: women, female)
- `gender_men` — Men's/male-targeted. (natural-language synonyms: men, male)
- `gender_unisex` — Unisex. (natural-language synonyms: unisex)

**Membership rule:** An atomic symbol matching `(color|size|gender)_[a-z_]+` naming a product color, garment/item size, or demographic-audience facet. New values are added as new members following this prefix pattern, never as free text.

**Example:**
- NL: "Find yellow t-shirts for women, small size, under $20."
- BrainCode: `ACTION search_web(target=t_shirt, color=color_yellow, size=size_small, gender=gender_women, currency=curr_usd, max_price=20) -> t_shirts : LIST[REF[STRING]]`

**Introduced/last revised:** sprint 18, see `changelog.md#sprint-18`

### `shape-value` (vocabulary)

**Gloss:** The closed set of geometric-shape symbols usable wherever an attribute calls for an object's shape (Action's shape attribute).

**Category:** closed — the members below are exhaustive

**Members:**
- `shape_round` — Circular/round. (natural-language synonyms: round, circular)
- `shape_square` — Square. (natural-language synonyms: square)
- `shape_rectangular` — Rectangular. (natural-language synonyms: rectangular, rectangle)
- `shape_oval` — Oval. (natural-language synonyms: oval)
- `shape_triangular` — Triangular. (natural-language synonyms: triangular, triangle)

**Example:**
- NL: "Find the lowest-priced gray round mirror in stock."
- BrainCode: `ACTION search_web(target=mirror, color=color_gray, shape=shape_round, availability=avail_in_stock) -> mirrors : LIST[REF[STRING]]`

**Introduced/last revised:** sprint 18, see `changelog.md#sprint-18`

### `state-value` (vocabulary)

**Gloss:** State-value gives canonical symbols for an object's condition when an Action needs to select or assert that condition. Full and empty are distinct, explicit states rather than inferred variants.

**Category:** open — the members below are representative

**Members:**
- `state_warm` — Warm or heated condition. (natural-language synonyms: warm, hot)
- `state_cold` — Cold or chilled condition. (natural-language synonyms: cold, chilled)
- `state_microwaved` — Has been microwaved. (natural-language synonyms: microwaved)
- `state_clean` — Clean condition. (natural-language synonyms: clean)
- `state_dirty` — Dirty condition. (natural-language synonyms: dirty)
- `state_full` — Contains its intended material or remaining usable amount. (natural-language synonyms: full, filled)
- `state_empty` — Contains no intended material or usable remaining amount. (natural-language synonyms: empty, used up)

**Membership rule:** An atomic symbol matching state_[a-z_]+ naming an object condition. New states are added as glossary members and are never free text.

**Example:**
- NL: "Move a full roll and an empty roll of toilet paper to the counter."
- BrainCode: `ACTION pick_up(target=toilet_paper, state=state_full) -> full_roll : REF[STRING]
ACTION place(target=full_roll, destination=counter)
ACTION pick_up(target=toilet_paper, state=state_empty) -> empty_roll : REF[STRING]
ACTION place(target=empty_roll, destination=counter)`

**Introduced/last revised:** sprint 19, see `changelog.md#sprint-19`

### `style-value` (vocabulary)

**Gloss:** Canonical writing/production style symbols for GENERATE's style attribute.

**Category:** open — the members below are representative

**Members:**
- `style_narrative` — Story-like narrative style. (natural-language synonyms: narrative, story-style)
- `style_technical` — Technical/expository style. (natural-language synonyms: technical)
- `style_academic` — Academic style. (natural-language synonyms: academic)
- `style_persuasive` — Persuasive/argumentative style. (natural-language synonyms: persuasive)
- `style_catchy` — Catchy, attention-grabbing style. (natural-language synonyms: catchy)

**Membership rule:** An atomic symbol matching `style_[a-z_]+` naming a compositional/rhetorical style. New styles are added as new members, never as free text.

**Example:**
- NL: "Give another catchy SEO title."
- BrainCode: `GENERATE(target=art_short_text, content="SEO title", style=style_catchy) -> title : STRING`

**Introduced/last revised:** sprint 18, see `changelog.md#sprint-18`

### `locale-value` (vocabulary)

**Gloss:** Canonical language/region locale symbols for GENERATE's locale attribute.

**Category:** open — the members below are representative

**Members:**
- `locale_en_us` — US English. (natural-language synonyms: english, en-us)
- `locale_en_gb` — UK English. (natural-language synonyms: british english)
- `locale_hi_en` — Hinglish (Hindi-English mix). (natural-language synonyms: hinglish)
- `locale_es` — Spanish. (natural-language synonyms: spanish)
- `locale_fr` — French. (natural-language synonyms: french)

**Membership rule:** An atomic symbol matching `locale_[a-z_]+` naming a language/region variant. New locales are added as new members, never as free text.

**Example:**
- NL: "Give a Hinglish SEO title."
- BrainCode: `GENERATE(target=art_short_text, content="SEO title", locale=locale_hi_en, style=style_catchy) -> title : STRING`

**Introduced/last revised:** sprint 18, see `changelog.md#sprint-18`

### `metric-value` (vocabulary)

**Gloss:** Canonical symbols for a queryable status metric, used with check_support_status's metric attribute — covering both service-support metrics and order/customer status facts.

**Category:** open — the members below are representative

**Members:**
- `metric_uptime` — Service uptime status. (natural-language synonyms: uptime, is up)
- `metric_response_time` — Support response time. (natural-language synonyms: response time)
- `metric_compatibility` — Compatibility status. (natural-language synonyms: compatible)
- `metric_order_late` — Whether an order is late. (natural-language synonyms: order is late, delayed)
- `metric_first_time_buyer` — Whether the customer is a first-time buyer. (natural-language synonyms: first-time buyer, new customer)
- `metric_repeat_buyer` — Whether the customer is a repeat buyer. (natural-language synonyms: repeat buyer, returning customer)

**Membership rule:** An atomic symbol matching `metric_[a-z_]+` naming a boolean-queryable status fact. New metrics are added as new members, never as free text.

**Example:**
- NL: "If the customer's order is late and they're a first-time buyer, offer a 10% discount; if repeat, offer free expedited shipping instead."
- BrainCode: `ACTION check_support_status(target=order, metric=metric_order_late) -> is_late : BOOL
ACTION check_support_status(target=customer, metric=metric_first_time_buyer) -> is_new : BOOL
IF is_late AND is_new THEN {
  ACTION offer_discount(target=order, discount_percent=10)
} ELSE {
  ACTION offer_expedited_shipping(target=order)
}`

**Introduced/last revised:** sprint 18, see `changelog.md#sprint-18`

### `semantic-category-value` (vocabulary)

**Gloss:** Semantic-category-value names an abstract class used as a constraint, not a selectable physical entity. It is the only canonical category for generic itinerary-stop requirements.

**Category:** open — the members below are representative

**Members:**
- `class_temple` — The abstract class of temples. (natural-language synonyms: temple, temples)
- `class_town` — The abstract class of towns. (natural-language synonyms: town, towns)

**Membership rule:** Members match class_[a-z_]+ and denote abstract semantic classes only. Use entity-name for a selectable object or place kind in an Action target; use semantic-category-value for a generic qualification such as stop_requirement. A translator must encode a generic requested stop class as class_<name>, never as an entity-name.

**Example:**
- NL: "Require at least one temple each day."
- BrainCode: `GENERATE(target=art_itinerary, topic=topic_kyoto_trip, stop_min_per_day=1, stop_requirement=class_temple) -> plan : STRING`

**Introduced/last revised:** sprint 20, see `changelog.md#sprint-20`

### `code-value` (vocabulary)

**Gloss:** Code-value supplies atomic symbols for code paths, program symbols, requested changes, test assertions, and code outcomes. Its prefixes determine which code attribute may use a member.

**Category:** open — the members below are representative

**Members:**
- `path_sklearn_linear_model_logistic_py` — The scikit-learn logistic module path.
- `sym_log_reg_scoring_path` — The _log_reg_scoring_path program symbol.
- `chg_inherit_multi_class` — Change requiring a constructed estimator to inherit multi_class.
- `assert_multinomial_scorer` — Assertion that multinomial probabilistic scoring succeeds.

**Membership rule:** Members are atomic symbols with exactly one prefix: path_ for file/source paths, sym_ for methods/classes/functions/properties, call_ for call patterns, chg_ for requested code changes, assert_ for test assertions, outcome_ for expected or actual outcomes, and repro_ for reproduction cases. file and source require path_; method/property require sym_; call requires call_; revision requires chg_; assertion requires assert_; expected_output/actual_output require outcome_; reproduction_step requires repro_.

**Example:**
- NL: "Fix LogisticRegressionCV scoring and test it."
- BrainCode: `ACTION modify_code(target=sklearn, file=path_sklearn_linear_model_logistic_py, method=sym_log_reg_scoring_path, revision=chg_inherit_multi_class)
ACTION run_tests(target=sklearn, assertion=assert_multinomial_scorer)`

**Introduced/last revised:** sprint 19, see `changelog.md#sprint-19`

### `content-value` (vocabulary)

**Gloss:** Content-value names an atomic structured topic, request substance, message purpose, or artifact premise. It replaces prose content where the required symbolic member exists.

**Category:** open — the members below are representative

**Members:**
- `content_status_update` — A request for a status update. (natural-language synonyms: status update)
- `content_kyoto_itinerary` — A Kyoto itinerary subject.
- `content_decision_study_sgi_japan` — A personal decision to travel to Japan to study SGI.
- `content_mixed_case_foreign_key_regression` — A mixed-case Django app-name ForeignKey regression test purpose.

**Membership rule:** Members match content_[a-z_]+ and each names one glossary-defined atomic proposition, topic, request purpose, premise, or message substance. A translator uses a listed canonical member or adds a member through a future vocabulary sprint; it may not place a phrase inside content when N4 closes transitional STRING.

**Example:**
- NL: "Give me a story premise about Gloopy and Glitter meeting a scientist."
- BrainCode: `GENERATE(target=art_story, content=content_gloopy_glitter_meet_scientist) -> story : STRING`

**Introduced/last revised:** sprint 19, see `changelog.md#sprint-19`

### `topic-value` (vocabulary)

**Gloss:** Topic-value names an atomic subject matter or premise for a conversation or artifact. It is used compositionally alongside constraints, events, and character properties.

**Category:** open — the members below are representative

**Members:**
- `topic_politics` — Politics.
- `topic_jazz_piano` — Jazz piano.
- `topic_classical_piano` — Classical piano.
- `topic_spider_man_2` — Marvel's Spider-Man 2.
- `topic_baldurs_gate_3` — Baldur's Gate 3.
- `topic_macbook_pro_2017` — MacBook Pro 2017.
- `topic_school_work_routine` — School and work routine.
- `topic_ai_earning_methods` — AI earning methods.
- `topic_pickup_lines` — Pickup lines.
- `topic_greatest_cricketer_of_all_time` — Greatest cricketer of all time.
- `topic_current_new_york_housing_market` — Current New York housing market.

**Membership rule:** Members match topic_[a-z_]+ and each names one glossary-defined atomic subject matter. Independent constraints, events, or criteria must be separated into their respective attributes rather than baked into the topic.

**Example:**
- NL: "Explain recent political shifts."
- BrainCode: `UTTER ask(topic=topic_politics)`

**Introduced/last revised:** sprint 20, see `changelog.md#sprint-20`

### `constraint-value` (vocabulary)

**Gloss:** Constraint-value names an atomic requirement, restriction, or explicit exclusion applied to a request.

**Category:** open — the members below are representative

**Members:**
- `constraint_17_plus` — Rated 17+ or mature.
- `constraint_single_choice` — Must pick a single choice.
- `constraint_realistic` — Must be realistic.
- `constraint_respectful` — Must be respectful.
- `constraint_beginner` — Targeted at beginners.
- `constraint_budget_limited` — Limited budget.
- `constraint_comprehensive` — Must be comprehensive.
- `constraint_exclude_flowery_language` — Avoid flowery language.
- `constraint_exclude_liberation_theme` — Avoid liberation theme.
- `constraint_include_character_attribute_list` — Include character attributes.

**Membership rule:** Members match constraint_[a-z_]+ and each names one glossary-defined atomic constraint, including explicit exclusions (constraint_exclude_...) and inclusions (constraint_include_...).

**Example:**
- NL: "Give realistic pickup lines."
- BrainCode: `UTTER ask(constraints=[constraint_realistic], topic=topic_pickup_lines)`

**Introduced/last revised:** sprint 20, see `changelog.md#sprint-20`

### `transformation-value` (vocabulary)

**Gloss:** Transformation-value names an atomic structural or formatting change applied to an artifact.

**Category:** open — the members below are representative

**Members:**
- `transform_preserve_first_column` — Preserve the first column of a table.
- `transform_remove_br` — Remove <br /> tags.

**Membership rule:** Members match transform_[a-z_]+ and each names one glossary-defined atomic transformation.

**Example:**
- NL: "Rewrite the table and remove <br />."
- BrainCode: `GENERATE(target=art_table, topic=topic_ai_earning_methods, transformations=[transform_remove_br]) -> table : STRING`

**Introduced/last revised:** sprint 20, see `changelog.md#sprint-20`

### `event-value` (vocabulary)

**Gloss:** Event-value names an atomic narrative or causal event used in artifact generation.

**Category:** open — the members below are representative

**Members:**
- `event_camper_in_sludge_pit` — Campers interacting in a sludge pit.
- `event_sadie_adler_unmasking` — Sadie Adler taking off her hat and peeling skin.

**Membership rule:** Members match event_[a-z_]+ and name an atomic narrative event or action sequence.

**Example:**
- NL: "Include campers in the sludge pit."
- BrainCode: `GENERATE(target=art_story, events=[event_camper_in_sludge_pit], topic=topic_camp_sludge) -> story : STRING`

**Introduced/last revised:** sprint 20, see `changelog.md#sprint-20`

### `character-property-value` (vocabulary)

**Gloss:** Character-property-value names an atomic trait, demographic, or style applied to a character.

**Category:** open — the members below are representative

**Members:**
- `char_female` — Female gender. (natural-language synonyms: female)
- `char_age_14` — Age 14. (natural-language synonyms: 14)
- `char_2000s_anime_style` — 2000s anime style.

**Membership rule:** Members match char_[a-z0-9_]+ and name an atomic character trait, demographic, or aesthetic style.

**Example:**
- NL: "Create a female, age-14 character."
- BrainCode: `GENERATE(target=art_character_profile, character_properties=[char_female, char_age_14], topic=topic_alek_szahala_alabama) -> profile : STRING`

**Introduced/last revised:** sprint 20, see `changelog.md#sprint-20`

### `capacity-unit-value` (vocabulary)

**Gloss:** Capacity-unit-value supplies canonical units for hardware capacity criteria. It keeps a numeric hardware requirement separate from its unit.

**Category:** closed — the members below are exhaustive

**Members:**
- `cap_gb` — One gibibyte-equivalent RAM capacity unit. (natural-language synonyms: GB, gigabytes)
- `cap_tb` — One tebibyte-equivalent capacity unit. (natural-language synonyms: TB, terabytes)

**Example:**
- NL: "Filter to 16 GB RAM or more."
- BrainCode: `ACTION search_web(min_ram=16, ram_unit=cap_gb, target=laptop) -> laptop_refs : LIST[REF[STRING]]`

**Introduced/last revised:** sprint 22, see `changelog.md#sprint-22`

### `cuisine-value` (vocabulary)

**Gloss:** Cuisine-value names the cuisine criterion for food and restaurant searches. Synonymous cuisine wording maps to one canonical symbol.

**Category:** open — the members below are representative

**Members:**
- `cuisine_indian` — Indian cuisine. (natural-language synonyms: Indian food, Indian)
- `cuisine_italian` — Italian cuisine. (natural-language synonyms: Italian food, Italian)

**Membership rule:** Members match cuisine_[a-z_]+ and name a cuisine classification. A source cuisine maps to its listed canonical member; a missing cuisine requires a glossary member addition rather than free text.

**Example:**
- NL: "Find an Indian restaurant."
- BrainCode: `ACTION search_web(cuisine=cuisine_indian, target=restaurant) -> restaurant_refs : LIST[REF[STRING]]`

**Introduced/last revised:** sprint 22, see `changelog.md#sprint-22`

### `reservation-status-value` (vocabulary)

**Gloss:** Reservation-status-value gives canonical reservation states for restaurant and venue requests.

**Category:** closed — the members below are exhaustive

**Members:**
- `reservation_available` — A reservation can be made. (natural-language synonyms: reservation availability, available reservations)
- `reservation_unavailable` — A reservation cannot be made. (natural-language synonyms: no reservations)

**Example:**
- NL: "Find a restaurant with reservations available."
- BrainCode: `ACTION search_web(reservation_availability=reservation_available, target=restaurant) -> restaurant_refs : LIST[REF[STRING]]`

**Introduced/last revised:** sprint 22, see `changelog.md#sprint-22`
