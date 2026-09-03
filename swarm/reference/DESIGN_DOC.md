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
| `Operation` | a verb: consumes bindings, produces one |
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
<domain declarations>

<|user|>
    statements
<|assistant|>
    statements
```

There are exactly two turn tags, `<|user|>` and `<|assistant|>`. Tool results and
retrieved material get no turn of their own — they arrive as the result of a
retrieval operation. All imports and declarations precede the first turn tag and
are never repeated inside a turn. Declarations may appear in any order and may
refer to one another.

## Identity lives in bindings

There is no name literal, and quoted names are not permitted. A thing's identity
is carried by the identifier you bind it to, which is where a label belongs:
write `karl_malone = Player(team=jazz, position=Position.FORWARD)`. The binding
name is subject to the same discipline as every other identifier — a word or two,
readable, no sentences.

This is not a notational preference. A quoted name is the easiest way to smuggle
a phrase into a document while appearing to have declared something, and an
entity whose only content is its own name records nothing at all. Nor is an
enumeration of proper nouns a substitute: a set of individuals is not a dimension,
and an entity holding a name-member plus a type is the same empty wrapper with
different punctuation.

It follows that an entity declaration is often just a **kind** — a bare type with
no fields, whose instances are distinguished by what they are bound to and by the
facts asserted about them. Fields belong on an entity only where it genuinely has
parts the trajectory uses. But constructing a bare kind is a way of *referring* to
something, not of saying anything, so it is only ever half of a translation: what
makes it worth writing is the facts that follow about the thing. A document that
is mostly bare constructions has its identifiers doing all the work, and has
recorded the reply's nouns.

Because identity lives in the identifier, the identifier is load-bearing in both
directions. It has to actually name the thing: an identifier that is a type
abbreviation plus an index means you had nothing to name it with, and throws away
the only place its identity could have lived. And it must never be asked to
assert anything — a proposition compressed into an identifier is a quoted name
with the quotes taken off, and what it states belongs in a fact. A binding is a
word or two, never a phrase.

Identifiers carry the conventions that let documents be compared: operations and
bindings in lower snake case, declared sorts in upper camel case, enum members in
upper snake case.

## Declarations

Domain vocabulary is declared one line at a time, with the sort as a keyword and
every field annotated by the sort of thing that may fill it, written `List[Sort]`
where the field takes several. Annotations make a mismatch visible and tell a
later reader what the vocabulary meant.

```
entity   Player(team: Team, position: Position)
content  PolicyDoc(publisher: Organization, published: Date)
property Scene(domain: Domain, quality: Quality)
relation Dominates(country: Country, sector: Sector)
action   InstallPackage(package: Package, via: PackageManager)
enum     Correctness(CORRECT, INCORRECT, PARTIAL)
```

Declarations are where bad vocabulary is caught, so the judgments below matter
more than anything else in this file.

**An entity must be something another trajectory could refer to.** A person, a
place, an organisation, a document, a product. If the thing only makes sense as a
heading for what this particular agent just said, it is not an entity — it is a
claim the agent made, and claims are facts. Test yourself by asking whether the
identifier would still mean anything in a document about a different subject.

**Beware the generic wrapper.** A declaration whose fields are a label and a type
satisfies every rule here and means nothing, and dropping the fields does not
help: a kind whose name amounts to "one of the things in this list", constructed
empty once per item, is that same wrapper with the label moved into the
identifier. When a structure's only job is to hold a phrase, delete it and find
the parts of what was actually asserted — the items in a list of claims,
teachings, or recommendations are propositions, and a proposition is a fact.

**A property, relation, or action needs at least two fields, but declare only
fields the source speaks to.** These pull against each other, and the source
wins: padding a declaration and then inventing a value to fill the pad is worse
than not having the declaration at all. If dropping the invented field leaves one
field, you were holding a value rather than a structure. Entities are exempt —
they are kinds, and a kind with no fields is ordinary.

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
play, the thing was not a dimension: make it an entity, an intent, or a fact.
Member names are single ideas, not compounds — a member joining two things with a
conjunction is two members, or a relation between them.

**A relation's object goes in a field, never in its name.** A one-place predicate
is a property assertion in disguise; say it with a general relation over a
declared dimension. Several names for what is really one relation should be one
relation over a dimension with several values. Prefer few general relations to
many specific ones, and before declaring anything, check that you have not
already declared it under another name.

**None of these tests may be satisfied by adding content.** Never invent an
operation, a binding, a field, a field value, an enum member, or a field read to
make a declaration well-formed. Every test above is a test on a declaration
precisely so that the only way to satisfy it is to rewrite the declaration. If a
rule appears to require adding something, you are misreading it.

## Statements and results

A statement is a binding or a bare operation call. Arguments are keyword
arguments. References to earlier bindings are ordinary variable references.

An operation's result goes on following lines opened by `>>`. Arguments are
inputs, `>>` lines are outputs, and nothing else carries a result. Every
operation that brings data into existence must carry one; omit it only when the
result would restate the input, and bind the result where the operation is rather
than restating a binding introduced earlier, which would put the fact before its
own provenance.

A result may be contrastive (`A over B`, meaning the operation established A
rather than B — one conclusion, not two) or negative (`not A`, an established
absence). You never need a second operation to express a contrast; writing two
evaluations so that both members of an enum get used invents an operation the
agent never performed. Contrast is selection, not magnitude — comparing sizes is
a comparison over a dimension.

**Bind what is referred to again; inline what is not.** A name introduced and
read exactly once is indirection with nothing on the other side — construct the
thing where it is used. The exception is a binding that carries a thing's
identity, which is not indirection at all, since the identifier is where its
label lives.

An argument may be a list, and one operation over many things is one operation.
Unrolling it into a call per item multiplies the trajectory without adding
anything, and an operation that produced ten findings takes one `>>` line holding
ten facts.

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
that says what kind of atom they are.

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

Composing the reply is an operation like any other. What it conveys is the facts
and findings communicated, never a single synthesis handle and never an assembled
passage.

Instructional trajectories are full of acts the agent did not perform and instead
told the user to. Those are actions, declared and constructed like other domain
vocabulary, and an imperative readable out of a literal you wrote should have been
one. Order a sequence of them explicitly rather than numbering steps, and when
advice depends on a condition, that conditionality is usually the whole point of
the answer and must survive. It is not control flow: nothing branches when the
document is read, the branch is content the agent asserted.

## Where a literal may appear

Argument positions carry expectations, and honouring them is what keeps a
document from becoming labelled prose. A target, subject, or `about` position
takes an entity or a binding. A topic or `on` position takes a dimension. A
conclusion, claim, finding, or ground position takes a fact. A literal belongs
where an atom belongs — inside a declared structure's field, or as a result —
and never as a stand-in for something that has not been declared yet. Declaring
it is not a way to launder a phrase: a field is a home for an atom, not a wrapper
for a sentence.

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
argument position the thing itself would have occupied. It is neither declared
nor bound: a redacted thing has no identity to carry, so binding one to an
indexed identifier invents an entity the trajectory does not contain. Repeat the
placeholder rather than numbering it, and where the trajectory turns on one
redacted thing recurring, bind it to the role it plays there. The redaction is
not a fact, not an uncertainty, and not a gap in what the agent did: invent no
vocabulary for it and do not guess what it was.

## Completeness and granularity

Encode the whole trajectory. Every distinct claim, finding, and comparison gets
constructs, because a translation that thins out as the trajectory goes on is
indistinguishable from a translation of something shorter. No elision markers, no
count standing in for content, no comments — anything worth a comment belongs in
a construct, on a result line, or in your decisions file. Length is not a reason
to compress.

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

Then read your declaration block on its own. If it reads like the reply's table
of contents, start again.
