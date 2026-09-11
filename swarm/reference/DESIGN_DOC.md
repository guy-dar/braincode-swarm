# BrainCode

A language for encoding human/AI trajectories — the arc of one task, from the
human's intent through the agent's reasoning and action to completion. One
document encodes exactly one trajectory. It is never machine-executed: its
semantics are specified precisely enough that any LLM can read a document
consistently from this documentation alone.

This spec serves two tasks. **Discovery** translates one trajectory in isolation.
**Canonization** reads many translations and decides what becomes shared
vocabulary. So this file does not hand you a catalogue of constructs to choose
from: that catalogue is what canonization produces, and it has to be earned from
evidence rather than asserted here. What you get instead is the structure a
document must have and the judgment to invent good vocabulary yourself. Two
translators reaching for different names on similar material is signal, not
error — diversity in expression, uniformity in structure.

---

## What a document is for

A trajectory contains a reply. The reply has a shape: an opening, some sections,
some claims, a conclusion. **That shape is not the document.** A document records
what the agent *worked out* — the operations it performed, the facts it
established, and how those facts bear on each other. If you deleted the reply and
kept only your document, a reader should be able to say what the agent concluded
and why, not merely what subjects it touched.

Almost every bad translation is the same mistake: the reply's outline is copied
across and dressed in syntax. It has appeared as strings, as capitalised enum
members, as predicate names, as named entities, as one enum per section, and as
whole passages inside a single leaf. The disguises differ; the failure is
identical, and it is the one thing to watch for in your own work. The reliable
symptom is a block of declarations that reads like a table of contents.

So the question to ask is never "is this construct allowed?" but **"does this say
what the agent figured out, or does it just label what the agent said?"**

## Sorts

Every name belongs to exactly one of nine sorts. The set is closed.

| Sort | What it is |
|---|---|
| `Operation` | a verb: consumes what is declared or established, produces a result |
| `Intent` | a human speech act |
| `Constraint` | a restriction on an acceptable answer |
| `Entity` | a thing the trajectory refers to |
| `Content` | material the agent received |
| `Property` | a dimension along which things vary |
| `Value` | a point in a `Property`'s range |
| `Relation` | a predicate asserting how things stand — a **fact** |
| `Action` | an act the agent describes rather than performs |

The first three are **structural**: they recur across every document and are what
make two documents comparable. The rest are **domain**: specific to one
trajectory and expected never to recur. Sprawl in domain vocabulary costs
nothing. Sprawl in structural vocabulary destroys the corpus, because two
documents describing one operation under two invented verbs cannot be compared at
all. Most of the discipline below therefore falls on the verbs.

## Document shape

```
<imports>
<declarations, with a definition for each composite>

<|user|>
    statements
<|assistant|>
    statements
```

There are exactly two turn tags, `<|user|>` and `<|assistant|>`. Tool results and
retrieved material get no turn of their own — they arrive as the result of a
retrieval operation. Imports and kind declarations precede the first turn tag and
are never repeated inside a turn; they may appear in any order and may refer to
one another. Individuals are never declared anywhere — they appear inside what is
said about them, in the turns.

The imports are where a document says which of its operations it takes to be
shared and which it invented:

```
from core        import recall_knowledge, read_source, compose_response
from provisional import corroborate
```

Every operation the document uses appears in exactly one of those two lines, and
no operation appears in the body without appearing there. That partition is the
whole point of the notation, because it is the only place a reader can see the
boundary the corpus depends on — the same verb under two invented names is
invisible otherwise, and a document whose operations are *all* provisional has
said something worth knowing about itself.

There is no list of core operations in this file, and there will not be one until
canonization earns it; `core` means the ordinary name for an ordinary act, at the
altitude the Operations section describes. Nor is `provisional` a confession — it
is the channel by which a construct gets considered for adoption, so marking a
verb you minted is how it comes to be shared, and mislabelling it as core is how
it never does.

## Reference and construction

Two different things happen in a document and the notation keeps them apart. Some
things the trajectory *talks about*: a company, a product, a source, a person.
Others the document *builds* out of parts: a fact, an intent, the result of an
operation. Constructor syntax, a kind applied to arguments, means the second one
only.

**An individual is therefore never constructed.** `Company()` makes a fresh
anonymous company, so binding it to `palantir` does not denote Palantir; it names
an empty allocation and leaves the identifier to do work a reference should be
doing.

**Declaring a kind does not make an individual exist, either.** A kind is
vocabulary. An individual is something the trajectory got from somewhere, and
where it came from is part of what the document records: recalled from what the
agent knew, read out of a source, supplied by the human, invented by the agent,
derived by computation. Those are five different claims about the world, and a
block of nouns at the top of a file flattens them into one.

**There is no statement that introduces an individual.** `village: Landmark`
asserts that there exists a landmark called village and identifies nothing — the
empty allocation again, wearing an annotation instead of parentheses — so the
form is gone rather than restricted. **An individual appears inside what is said
about it, and nowhere else.** A thing the document never says anything about is
not part of the trajectory; a thing it does say something about is present in
those facts already, and needs no line announcing itself.

A name is therefore bound only to something that picks a thing out, and there are
exactly two of those: a public name, `usafacts = Known("USAFacts")`, and the
result of an operation, where running is what brought the thing into being.

**There is no third form, and inventing one is how this rule gets broken.** A
marker that says "the human mentioned this" or "the agent knew this" attaches a
kind to nothing and identifies nothing — it is the empty allocation again with a
new keyword, and it will attract every noun a document cannot otherwise justify.
The case such a marker seems to be for is already covered: whatever the human
mentioned, the document says something about, and it is present in those facts.
A thing the document says nothing about is not in the trajectory at all.

So if neither form fits, you are not looking at an individual. You have a
**kind**, which is vocabulary and belongs in a declaration, or a **fact**, which
belongs on a result line. Generic nouns are one common case: a village in a
song's imagery, a workplace in a question about workplaces, men, everyone — none
picks out a particular thing. Practices, methods, and systems are another: halal
and kosher are what the facts about them say, and a document that binds them to a
kind and stops has named two things it never described.

**The other common case is a noun that is a sentence with its subject removed.**
Instability, decline, corruption, migration, scarcity, decay, fragmentation: each
names a state or a change, and a state is something that holds *of* something.
Introduce one as an individual and the subject — the part that made it a claim
about the world — is simply gone, leaving a token that can be caused by and cause
other tokens without any of it saying anything. Recover the subject and you have
a fact, which is what it always was; and since facts compose, a cause and its
effect can both be facts without any new vocabulary. A causal chain running
between abstract nouns is this failure at scale, and it reads as an explanation
while asserting nothing about anyone.

**`Known` is the narrowest of the three:** an individual any model can identify
unaided, which is to say a particular person, place, organisation, work, or event
with a proper name — `Known("Michael Jordan")`, `Known("Chicago Bulls")`. An
identifier is private to one document, so two documents about the same person
cannot be related through their bindings; the public name is the only thing they
can share, and that is the whole reason a literal is allowed to name something
here. A key is written once, where the name is bound, and every later mention is
the identifier — the same key twice in one document is one thing being introduced
twice.

Three questions keep it in its place, and any one of them settles the matter.

**Which one in the world is it?** If you cannot point to a single thing the name
picks out, there is nothing to key. "Transgender women", "men", "everyone" name
groups; "a workplace", "a washroom" name kinds; and a kind is declared, not keyed.

**Does it come apart?** A name that decomposes is a composition, and building it
is the point: gender discrimination is discrimination along a dimension, a right
to self-identification is a right to an act, a gender-neutral washroom is a
washroom with a property. Keying the phrase buries the structure that was the
content, which is the same mistake as a compound construct name and is why
`Known` may never hold a concept.

**Would any model know it without being told?** That is what `Known` claims. A
term the trajectory itself introduces or defines is not world knowledge, however
proper its capitals look.

So most individuals are not `Known`. What the human supplied, what the agent
invented, what it derived, what a source happened to mention: all of those are
introduced by the operation that brought them in, and that is their provenance. A
document where every individual carries a key has stopped recording provenance
and gone back to asserting nouns, with quotation marks this time.

**A construction with an empty argument list means one of two things, and both
are mistakes.** Either you have an individual, which is introduced rather than
constructed. Or you have a name that has eaten its own arguments:
`ExplorePerspectives()` is `Explore(perspectives)` with the object welded into
the verb, and it is empty precisely because everything it should have taken is
inside its name. That is the second case and the more common one, and it is how a
vocabulary of common words decays into a vocabulary of phrases. Every sort is
built the same way — a common word plus what it applies to — and an empty
parenthesis is the signal that something got absorbed which should have been
passed.

**Everything the trajectory says about an individual is a fact** — its parts, its
properties, what it did, what was claimed of it. That is why entity and content
kinds carry no fields: a field would be a second place to put what a fact already
says, and the two would drift.

An identifier is a word or two, never a phrase, and never asked to assert
anything — a proposition compressed into an identifier is a quoted name with the
quotes taken off, and what it states belongs in a fact. One that is a type
abbreviation plus an index means you found nothing to name the thing with, which
is worth stopping over rather than papering over. Nor is an enumeration of proper
nouns a substitute for introducing individuals: a set of individuals is not a
dimension.

`REDACTED` and `REDACTED(Kind)` denote an individual whose name the corpus
removed. They are not a construction and not a `Known` key; they stand where the
thing would have stood.

Identifiers carry the conventions that let documents be compared: operations and
bindings in lower snake case, declared sorts in upper camel case, enum members in
upper snake case.

## Declarations

Domain vocabulary is declared one line at a time, with the sort as a keyword and
every field annotated by the sort of thing that may fill it, written `List[Sort]`
where the field takes several. Annotations make a mismatch visible and tell a
later reader what the vocabulary meant. What is declared here is vocabulary —
kinds and structures — never individuals.

```
entity   Player
entity   Team
content  PolicyDoc
property Scene(domain: Domain, quality: Quality)
relation Dominates(country: Country, sector: Sector)
action   Install(package: Package, using: PackageManager)
enum     Correctness(CORRECT, INCORRECT, PARTIAL)
```

Declarations are where bad vocabulary is caught, so the judgments below matter
more than anything else in this file.

**An entity must be something another trajectory could refer to.** A person, a
place, an organisation, a document, a product. If the thing only makes sense as a
heading for what this particular agent just said, it is not an entity — it is a
claim the agent made, and claims are facts. Test yourself by asking whether the
identifier would still mean anything in a document about a different subject.

**A kind's individuals are individuals.** So read the individuals you declared
under a kind: where they are qualities — adjectives, or answers to "which sort of
one?" — the kind is a dimension and they are its members. This is the most common
way a document ends up with vocabulary that asserts nothing, because a dimension
split into one individual per value satisfies every other rule here while moving
the whole distinction into the identifiers.

**A kind's name must say what its instances are, not that they are things.**
`Concept`, `Aspect`, `Factor`, `Feature`, `Element`, `Item`, `Topic`, `Theme`,
`Component`: each of those names only the fact that something got mentioned, so
the kind will accept anything, and the relations over it degenerate with it — a
predicate whose fields are two such kinds says no more than that two unspecified
things are related somehow. The repair is not a less obvious synonym. Ask what
the things going into it actually are and name that; if they have nothing in
common beyond being talked about, they were never one kind, and what you have is
several kinds or a pile of facts.

**Beware the generic wrapper.** A declaration whose fields are a label and a type
satisfies every rule here and means nothing, and dropping the fields does not
help: a kind whose name amounts to "one of the things in this list", constructed
empty once per item, is that same wrapper with the label moved into the
identifier. When a structure's only job is to hold a phrase, delete it and find
the parts of what was actually asserted — the items in a list of claims,
teachings, or recommendations are propositions, and a proposition is a fact.

**An atom needs no kind to hold it.** A number, a date, a quantity, a duration:
each is already a value, so a kind whose instances exist in order to *have* one is
a box around something that was never in need of boxing. Declaring a kind for
numbers, a dimension for their values, and a property to connect the two is three
constructs where the number would have done, and the kind then never appears in a
turn on its own — which is what most dead vocabulary turns out to be. Put the
value where the box was: an operation that worked out a number produces the
number.

**A property, relation, or action needs at least two fields, but declare only
fields the source speaks to.** These pull against each other, and the source
wins: padding a declaration and then inventing a value to fill the pad is worse
than not having the declaration at all. If dropping the invented field leaves one
field, you were holding a value rather than a structure. Entity and content kinds
do not come into it: they take no fields at all, so they are the one place the
question never arises.

**A field's type is one of the declared sorts, or one of the atom kinds.** There
is no general text type and you may not invent one. A field that wants to hold
arbitrary text is a field whose content has not been analysed: what belongs there
is a dimension, a fact, or a reference to something declared.

**A property is something a thing has exactly one of at a time.** That is what
makes it a dimension rather than a list. If several of its members hold of one
target simultaneously, it is a list, and each item is a separate fact needing its
own structure. Good dimensions are short, mutually exclusive, and reusable across
subjects; if you cannot name the question a dimension answers, it isn't one. One
enum cannot serve as every dimension — a bag of adjectives reused in unrelated
fields is how a document ends up saying nothing.

**Never invent a member to round out an enum.** If only one value was ever in
play, the thing was not a dimension: make it an entity, an intent, or a fact — and
a one-member enum left standing in a document is that same mistake, written down
rather than corrected. Member names are single ideas, not compounds — a member
joining two things with a conjunction is two members, or a relation between them.

**An intent is a speech act, and there are only a few.** Asking, requesting,
instructing, accepting, declining, correcting: that is the sort of list this sort
covers, and what is asked or requested rides in the argument. So an intent whose
name carries its own topic — asking about *this*, requesting *that* — is a speech
act with the domain welded on, and it is the reason this sort shows no reuse
across documents while being one of the three that exist to be comparable. What
the human wanted to know is a fact with its value left open, which is how every
other question in a document is written, so the intent takes that fact as its
argument and needs no name of its own.

An intent is itself a statement. Wrapping it in an operation that announces an
intent was stated says nothing the intent has not already said.

**A relation's object goes in a field, never in its name.** A one-place predicate
is a property assertion in disguise; say it with a general relation over a
declared dimension. Several names for what is really one relation should be one
relation over a dimension with several values, and before declaring anything,
check that you have not already declared it under another name.

The reason a one-place predicate looks acceptable while you are writing it is
that it does not feel one-place: **a single argument plus a noun in the name is
two arguments, one of them misfiled.** `RoutesRevenue(corp)`,
`MinimizesTaxes(corp)`, `CollectedAtBorder(tax)` each read as complete because
the missing participant is sitting in the identifier where an argument cannot be
compared, quantified, or referred to again. Take the noun out of the name and put
it in a field, and what is left is usually a verb general enough to serve the
rest of the document — which is the whole gain.

This is also why the property sort goes unused while relations multiply. A thing
sitting at one point on one dimension is a property, and reaching for a
one-place relation instead is what makes a document assert the same shape twenty
different ways.

**Measurements are one relation over a metric, not one relation each.** Where
several relations differ only in which quantity they carry — a deficit, a share
of output, a projected range, a peak — they are one relation whose arguments are
the subject, the metric, the period, and the value, with whether it was measured
or projected a dimension like any other. Numbers are where this sprawls worst,
because every quantity feels like its own predicate, and eleven relations for
eleven quantities leaves nothing comparable across documents.

**A construct's name is a common word.** The vocabulary of this language is the
vocabulary a thousand unrelated trajectories share: cause, part, kind, before,
more, requires, prevents, says. Those are the words that get constructs. A narrow
concept does not get one, because a narrow concept is a *composition* of common
ones, and naming it hides the composition that was the content.

A compound name is therefore a definition owed — see Definitions below, where the
obligation is stated as a condition on well-formedness rather than as advice.
Anything qualifying a relation — how strongly, how necessarily, in which
direction, on whose account, with what certainty — is a dimension, and it belongs
in an argument *of the definition*, which is what makes the qualification
comparable across documents instead of lost inside a predicate that occurs once.
A document distinguishing several near-synonyms of one common word has invented a
thesaurus rather than a vocabulary, and defining each of them is what exposes
that: three definitions that come out the same were three names for one thing.

**How to take a name apart, which is how a definition gets written.** Read the
name word by word. One word in it is the verb; keep that and nothing else. Every
word you removed is either a participant, which becomes an argument, or a
qualifier, which becomes a value on a dimension. A name with no verb left over
was never a predicate at all — it was a subject, and what you meant to assert
about it is still unwritten.

The gain is not tidiness. Two claims that differ in one qualifier come out as one
relation applied twice, at two values of one dimension, so the document can say
they are the *same* claim under a contrast — which is usually why the trajectory
raised both. Name them separately and the relation between them cannot be
written at all: two predicates that occur once each, where the reply was drawing
a distinction. Every proposition folded into a predicate name costs the document
one thing it can no longer say.

**A unit is a dimension, not a string.** A quantity carries its unit because the
number alone is not the measurement, and the set of units in play is exactly the
sort of small, closed, reusable set a dimension exists for. Quoting it puts the
one part of the value that has to match across documents into the one form that
cannot be compared.

**A declaration nothing uses is not vocabulary.** If you declared it and no
statement mentions it, it recorded an intention rather than the trajectory —
delete it. This is worth a pass at the end, because dead declarations accumulate
from restructuring rather than from any single decision.

**None of these tests may be satisfied by adding content.** Never invent an
operation, a binding, a field, a field value, an enum member, or a field read to
make a declaration well-formed. Every test above is a test on a declaration
precisely so that the only way to satisfy it is to rewrite the declaration. If a
rule appears to require adding something, you are misreading it.

## Definitions

A declaration says what shape a construct has. It does not say what the construct
*means*, and a name is not a meaning — `SystemicRacismExists` tells a reader what
its author had in mind only if the reader had it in mind already.

**A name with a noun in it is not well-formed without a definition.** Not
discouraged — not writable. There are exactly two legal shapes for a declared
name, and no third:

- a **verb**, with particles and prepositions as needed — `Causes`, `PlayedFor`,
  `AttributedTo`, `PartOf`. Nothing is owed; the name is already at the bottom.
- a **composite**, which is any name carrying a noun or an adjective —
  `SystemicRacismExists`, `RoutesRevenue`, `MinimizesTaxes`, `DeficitShareGDP`.
  These are allowed, and the declaration shows what the name comes apart into:

```
relation SystemicRacismExists(country: Country)
    = Exists(thing=racism, within=country, character=Character.SYSTEMIC)
```

So the noun in a name is the test, and it decides which shape you are in. A
composite without a definition is the one form this section rules out, because
it is a claim the document makes and never says.

That is the trade: in the body, write the name that fits what happened, however
specific — the reply's own distinctions are worth keeping, and forcing every
sentence through a handful of primitives loses them. What is not optional is
saying once what the specific name means. And the contrast a bare pair of names
could never express becomes recoverable: two composites whose definitions differ
at one argument are visibly the same claim under a contrast, and a reader sees it
without the document having said it twice. The decomposition procedure above is
how a definition gets written.

**A definition may use only constructs that are themselves defined, or that
cannot be defined.** The second kind is the interesting one, and the test for it
is narrow: a construct is atomic when you cannot say what it means without using
it, a synonym of it, or a paraphrase that smuggles it back in. Existence, part
and whole, cause, order, sameness, difference, negation, degree — things of that
sort bottom out, and everything else in a document should be reachable from them
in a few steps. A definition that leans on a construct as composite as the one
being defined has renamed rather than defined it.

Two things need no definition. **Atoms** — a number, a date, a quantity — are
values, not compositions. And **world knowledge** is not the language's business:
`Known("Michael Jordan")` names someone the reader can look up, and no definition
this document could give would improve on that. What has to be definable is the
language's own machinery: every operation, relation, property and action a
document invents in order to say what happened.

**What a document leaves undefined is itself a finding.** No list of primitives
appears in this file and none will be asserted here, because the set of
constructs that documents keep bottoming out in *is* the primitive basis — found
in the corpus rather than declared in advance, which is exactly the job
canonization exists to do. A document that leaves twenty things undefined has
proposed twenty primitives, and that is a claim worth making on purpose rather
than by omission.

## Statements and results

A statement is an operation call, or a binding of what one produced. Arguments
are keyword arguments written `name=value`, and a reference to a declared
individual or an earlier result is an ordinary variable reference. The colon
belongs to declarations only — `name: Kind` declares, `name=value` passes — and a
call site that borrows the colon has made two notations for one thing. A member
of an enum is always written qualified, `Dimension.MEMBER`, because a bare member
does not say which dimension it answers.

So a turn contains operations and the facts they establish, and nothing else. The
individuals were declared before the first turn tag; a turn that opens by
allocating its nouns has spent its statements on inventory rather than on what
happened.

An operation's result goes on following lines opened by `>>`. Arguments are
inputs, `>>` lines are outputs, and nothing else carries a result. Every
operation that brings data into existence must carry one; omit it only when the
result would restate the input, and bind the result where the operation is rather
than restating a binding introduced earlier, which would put the fact before its
own provenance.

**One result per `>>` line.** A result line carries a fact, or the thing the
operation made or worked out. It never carries an announcement that something
exists: an operation that recalls or reads establishes *facts*, and the things
those facts are about are present in them. An operation yielding ten facts is one
call followed by ten such lines. There is no
list literal on a result line and no assigning several names at once — those say
exactly what the plain form says, and a corpus cannot compare documents that each
chose a different way to say it.

A result may be contrastive (`A over B`, meaning the operation established A
rather than B — one conclusion, not two) or negative (`not A`, an established
absence). What a document may never do is assert both a fact and its negation, or
two values of one dimension for one subject: that is not a nuance, it is two
contradictory claims side by side. Where the reply qualified something — accurate
in one respect, misleading in another — the respect is a dimension and belongs
inside the fact, and where it changed its mind, the later finding supersedes the
earlier one and only one of them is the conclusion. You never need a second operation to express a contrast; writing two
evaluations so that both members of an enum get used invents an operation the
agent never performed. Contrast is selection, not magnitude — comparing sizes is
a comparison over a dimension.

**Bind what is referred to again; inline what is not.** A result named and read
exactly once is indirection with nothing on the other side — construct it where
it is used. This is about results, not individuals: an individual is declared
because it is referred to at all, and its declaration is a reference rather than
indirection.

An argument may be a list, and one operation over many things is one operation.
Unrolling it into a call per item multiplies the trajectory without adding
anything.

## Facts

The operations record what the agent *did*. They do not record what it
**claimed**, and both belong in the document. This is the most important thing to
get right.

A fact is a constructed relation — a declared predicate applied to declared
things — and it belongs on the `>>` line of the operation that produced it. A
fact left standing alone has no provenance: recalled, retrieved, read, and
inferred all look alike once the link is gone.

Facts compose. A relation may take another relation as an argument, so a claim
about a claim, or a ground for a claim, needs no new vocabulary.

Construct each fact once, bind it, and reference the binding thereafter. Identity
is structural — same relation, same field values, same fact — so rebuilding one
says nothing new and makes repetition indistinguishable from two findings that
merely look alike.

Say whose claim it is. A bare fact is asserted in the document's own voice, so
when a trajectory turns on what an author, a source, or the user holds, attribute
it. Otherwise a document about someone else's argument reads as the agent
asserting it, and a contradiction between two attributed claims — a disagreement
between sources — becomes indistinguishable from the agent contradicting itself.

Say when the agent is performing rather than asserting. A roast, a parody, a
devil's-advocate case, a deliberately one-sided pitch: those claims belong to the
persona, not to the agent's considered view, and recording comic hyperbole as a
finding misreads the trajectory.

When the agent's answer turns on what a concept is *made of*, build the concept
from its parts rather than naming it. Collapsing a distinction the agent
constructed into an opaque label discards the work the document exists to record.

**A value on a dimension is not what a claim said.** If the reply held that a
technology could address climate change and cure disease, then climate change and
disease are the content, and recording an impact as *positive* keeps the sign and
throws away the claim. A dimension is for the axis a thing varies along; it is
not somewhere to put what the reply was actually about, and it is the last place
prose goes once names and literals are closed to it — the difference being that
this one leaves no trace, because a coarse value looks like conformant structure.

The test is one this documentation applies elsewhere and had not yet turned on
facts: **could you write this fact, in these words, about a different subject?**
An impact that is positive on society and good for the economy fits almost any
technology, so it distinguishes nothing and records nothing. What made the reply
worth translating is exactly what such a fact drops. Where the reply named
things, those things are participants and belong in arguments; where it gave a
mechanism, the mechanism is a fact of its own; and if a claim genuinely has no
content beyond a direction, it was an aside, not a finding.

**A question is a fact with its value left open**, and it is built the same way:
a subject, and the dimension being asked about, with nothing yet filling the
place an answer would fill. This is how every interrogative in a trajectory gets
recorded — the human's opening request, a clarification the agent asks for, a
follow-up it offers, an objection it raises in the form of a demand for evidence.
None of those is text to be preserved; each is a subject and a dimension, and
writing the sentence instead throws away both. Where an answer arrives later, it
is the value that fills the open place, which is what makes a question and its
answer legible as one movement rather than two unrelated statements.

## Atoms

Most of a document is declared vocabulary and references to it. A literal is
permitted only for things that genuinely are atoms and whose exact form carries
information: a quantity with its unit, a date, an interval, a numeric range, a
filename, a URL, a boolean or a number. These need no wrapper beyond the sort
that says what kind of atom they are. The one other place is a `Known` key, which
is an atom for the same reason a URL is — its exact form is what it does.

**Free text is not an atom, and long strings are not permitted anywhere.** Not in
a field, not on a result line, not under any wrapper. A literal is a few words at
most. There is no exception for material the agent received and no exception for
material the agent produced: a passage under analysis is represented by what is
being said about it, and a reply is represented by the facts it conveys.

Where the agent produced something whose exact wording *was* the deliverable — a
punchline, a coined phrase, a line that had to be those words — that wording may
be kept, but only as the atom it is, and only for the one part where the words
were the payload. If a single literal in your document could be pasted back as
the answer, you have written nothing.

Be strict about what qualifies. A question is not an artifact: it is a subject
and a dimension, and it is built like a fact. Nor is a heading, a topic, a
category, a summary, a recommendation, or an explanation — each of those is
something the agent worked out, and each has parts. The exception is narrow by
design, and reaching for it more than once or twice in a document is a sign you
have found a convenient place to put sentences rather than a genuine artifact.

## Operations

An operation is something the agent did, and its name should survive being moved
to an unrelated trajectory: the domain goes in the arguments, never in the verb.
A verb is a transitive verb plus a generic object, two words at most; if it wants
a third, the third is an argument. If the construct you have in mind means "*X*,
but for *Y*", then *X* is the construct and *Y* is an argument — and a candidate
name containing a token already present in your document is an application of
something you have rather than a new thing.

Reach for the plain, obvious verb for a plain thing. Stating an intent,
searching, recalling, reading a source, citing, extracting, classifying,
computing, comparing, evaluating, inferring, summarising, synthesising, defining,
decomposing, generating an artifact, composing a response, requesting
clarification, offering a follow-up, stating a limitation, refusing: these recur
across nearly every corpus, and using the ordinary name for the ordinary thing is
what lets canonization see the pattern. That is an illustration of altitude, not a
closed list — invent what you need at the same altitude, and record what you
invented.

Do not lean on one generic verb. If a single operation accounts for most of your
calls, appearing again and again with near-identical arguments and emitting one
more value each time, you are walking through the reply section by section rather
than recovering what the agent did.

When a trajectory argues rather than answers, the argumentative moves are
themselves operations: distinguishing, conceding, rebutting, reattributing a
cause, bounding where a term applies, concluding from having searched and found
nothing. These look like connective tissue but they are the content, and they
consume one another's outputs — which is what makes an argument chain where a run
of lookups merely fans out.

Composing the reply is an operation like any other, and what it conveys is the
conclusions the reply actually put forward — never a single synthesis handle,
never an assembled passage, and never a list of every fact in the document. A
composition that enumerates the whole document says only that the reply happened,
and it is what forces facts to be named `f1` through `f66`: a fact nothing refers
to needs no name, so a document full of numbered facts is usually a document whose
composition swallowed everything. The grounds stay reachable through the
conclusions they support.

Instructional trajectories are full of acts the agent did not perform and instead
told the user to. Those are actions, declared and constructed like other domain
vocabulary — a verb plus what it acts on, held to the same discipline as an
operation, so an action that takes no arguments has its object inside its name.
An imperative readable out of a literal you wrote should have been one. Order a sequence of them explicitly rather than numbering steps, and when
advice depends on a condition, that conditionality is usually the whole point of
the answer and must survive. It is not control flow: nothing branches when the
document is read, the branch is content the agent asserted.

## What an operation produced, and how

An operation's name says what act was performed. It says nothing about what came
out, and a document that names the act and stops has recorded that something
happened rather than what happened.

**When the agent made something, the thing it made is content, and content is
statements.** A song has a subject, a stance, images, a form, a turn at its end;
a plan has steps, an order, a condition on each; a program has parts and what
each one does. All of that is what the agent decided, and all of it belongs in
the document as facts about the artifact it built. Naming the act of writing a
song and giving it a bare result is a label where the deliverable should be — the same failure
as a quoted passage, arrived at from the opposite direction, and neither is fixed
by the other. If your document would let a reader say only *that* a song was
written, the operation is the only thing you translated.

**When the reply shows its work, the working belongs in a `via` scope.** A `via`
attached to an operation holds the operations that produced its result, indented
under it, as ordinary statements with their own results:

The scope is opened by `via`, indented under the operation whose result it
explains, and holds ordinary statements with their own result lines. The
operation's own result follows the scope, not inside it.

Reach for it exactly when the reply exhibits reasoning rather than asserting a
conclusion: a calculation carried out in steps, a derivation, a candidate
considered and rejected before the answer, a source consulted mid-argument. Those
intermediate steps are the part a reader cannot reconstruct from the result, and
they are the reason this language exists. Where the reply gives a conclusion and
no working, there is no `via` — inventing plausible steps for it is inventing
reasoning, and that is the one thing this document may never do.

## Where a literal may appear

Argument positions carry expectations, and honouring them is what keeps a
document from becoming labelled prose. A target, subject, or `about` position
takes an individual already introduced. A topic or `on` position takes a dimension. A
conclusion, claim, finding, or ground position takes a fact. A literal belongs
where an atom belongs — inside a declared structure's field, or as a result —
and never as a stand-in for something that has not been declared yet. Declaring
it is not a way to launder a phrase: a field is a home for an atom, not a wrapper
for a sentence.

**No argument holds a phrase, and the aboutness positions are where that gets
tested.** `about`, `topic`, `query`, `on`: these read as labels rather than as
content, which is why prose survives in them after being driven out of everywhere
else. What an operation concerns is said in the language — the individuals it
concerns, and the open fact it seeks — never described. A recall aimed at the
Persian conquest of Judea and Babylon concerns Persia, Judea, Babylon and the
conquest relating them, every one of which the document needs anyway, because the
facts that follow are about them. A search is issued *for* something, and what it
seeks is a fact with its value left open, which is how every other question in a
document is written.

The test is quick: a topic string is a promise that facts will follow. If they
follow, the string was redundant. If they do not, it is the only thing the
document has, and it is prose. The same goes for anything else broken down too
coarsely to be an atom — an atom is a quantity, a date, a name, a number, and if
what you have written has parts, those parts are the content.

## Fidelity

Three asymmetric rules govern what a translation may and may not do.

**Operations are recovered, not merely transcribed.** Target the operations the
agent actually performed rather than only those the trace narrates, encoded when
a competent reader would confidently assume the operation occurred — a bound
deliberately weaker than logical necessity.

**Reasoning is never invented.** No motive or justification the source does not
evidence. Inferred reasoning is indistinguishable from recorded reasoning once
written, and poisons the corpus for the uses that motivate the project.

**Human intent is made explicit**, anchored to what the agent demonstrably
understood the request to be — shown by what it went on to do — rather than to
your own reading of the words. A misread request is encoded as the misreading.

Execution errors are not reflected in structure: a miscount uses the counting
operation, with the wrong value on its result line.

**Redaction is an artifact of the corpus, not content.** These trajectories come
from a PII-redacted dataset, so a redaction marker stands for something that was
ordinary — a person, an employer, a filename. Write it as the reserved
`REDACTED`, or `REDACTED(Kind)` where the kind of thing matters, standing in the
argument position the thing itself would have occupied. It is not declared as
an individual, because it has no name to declare, and it is not bound: binding
one to an indexed identifier invents an entity the trajectory does not contain. Repeat the
placeholder rather than numbering it, and where the trajectory turns on one
redacted thing recurring, bind it to the role it plays there. The redaction is
not a fact, not an uncertainty, and not a gap in what the agent did: invent no
vocabulary for it and do not guess what it was.

## Completeness and granularity

Encode the whole trajectory. Every distinct claim, finding, and comparison gets
constructs, because a translation that thins out as the trajectory goes on is
indistinguishable from a translation of something shorter. No count standing in
for content, no comments — anything worth a comment belongs in a construct, on a
result line, or in your decisions file. Length is not a reason to compress.

**Nothing in this documentation is a licence to record less.** Most of what it
says is a prohibition, and a prohibition can always be obeyed by leaving the
material out — which satisfies the letter of every rule here and produces a
document that says nothing wrong and nothing at all. So the rules bear on *how*
each thing is said, never on how much: what they take out is ceremony, and as
ceremony goes the count of things asserted should hold or rise, never fall.

If a rule appears to forbid recording something the agent plainly established,
you have found the wrong reading of it. There is a way to say it — as a fact, as
a dimension, as a step inside a `via` — and finding that way is the task. Silence
is the one thing that is never the answer.

**An ellipsis is never part of a document.** Not as a value, not as an argument,
not standing where a construction belongs: `x = …` says that something was meant
to go there and did not, which is a note to yourself rather than a translation.
Where this documentation shows a form, it is describing a shape you fill in, and
copying the shape itself is how a document ends up asserting that its own content
is missing. If you do not know what belongs in a position, the honest move is to
leave the position out and say so in your uncertainties file.

A single step of agent activity usually expands into several operations. Expand
along operations, not along narration.

There is no control flow. Sequence is statement order and nothing else.

Do not re-encode repetition. An operation repeating one already written, with the
same inputs and the same result, carries no information; genuine repetition
differs in its inputs or its result, as a retry or a revised estimate does.
Duplicated text in a source is a property of the transcript rather than something
the agent did, and reusing one verb with identical arguments to walk through
successive parts of the reply is narration.

## Before you finish

Look at what your bindings feed. If most are referenced only by the response
composition, you have written a fan — many independent lookups emptying into a
bibliography — and a fan is almost never what the agent did. Real reasoning
chains: a distinction feeds a comparison, a comparison feeds a conclusion, an
objection feeds a rebuttal.

**But a list is not an argument, and turning one into an argument is inventing
reasoning.** A reply that sets out four things it holds has given you four
findings, not a derivation, and grounding one in another because the document
looked too flat is the worst thing a translation can do — it is indistinguishable
from recorded reasoning afterwards, and it is precisely the failure the fidelity
rules exist to prevent. So the check above is a question to ask, never a shape to
produce: if the chains are missing because the agent laid out a list, the honest
document is flat and says so. Where a reply genuinely argues, the connectives are
already in it — because, therefore, which is why, this follows from — and those
are what a ground relation records.

Then read your declaration block on its own. If it reads like the reply's table
of contents, start again.
