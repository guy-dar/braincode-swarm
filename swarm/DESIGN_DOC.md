# BrainCode Design Thoughts and Recommendations

## What BrainCode Is

BrainCode is a general-purpose language for encoding human and AI conversations and the thinking behind them, built as a research artifact for interpretability/audit, planning specs, cross-model comparison, task decomposition, and other not-yet-identified downstream uses. Those motivating uses shape but don't bound its scope — the language must stay general enough for future uses too (0001). It is never machine-executed: its semantics are specified precisely enough that any LLM, given the documentation, can interpret ("execute" in the reading sense) a document consistently.

## Glossary

- **Trajectory** — the complete arc of a single task, from initial human intent through the agent's reasoning and action to completion. One document encodes exactly one trajectory. _(Avoid: episode, conversation, session, run.)_
- **Canonization** — the process by which a recurring concept from natural-language interaction becomes a named construct in BrainCode. _(Avoid: standardization, normalization.)_
- **Design agent** — an agent that translates trajectories into BrainCode and evolves the canonized vocabulary; distinct from the subject agent. _(Avoid: compiler, LLM-compiler, translator.)_
- **Subject agent** — the agent whose reasoning and action a trajectory encodes. _(Avoid: target agent, traced agent.)_
- **Operation** — a step the subject agent performed that warrants a construct, whether or not the source trace narrates it. _(Avoid: step, action.)_
- **Narrative feature** — an aspect of a trajectory describing how operations relate (sequencing, retrying, falling back) rather than transforming data; not encoded as constructs, and whether/how to capture these at all is unresolved. _(Avoid: control flow, connective.)_
- **Turn** — a maximal contiguous segment of one speaker's content, opened by a reserved meta-tag (e.g. `<|user|>`) and implicitly closed by the next tag or the end of the document. _(Avoid: message, block.)_

## Shape of the Language

The language is general-purpose by deliberate choice, not defaulted into: retrofitting generality onto something shaped around one use case is expensive, so BrainCode was designed general from the start rather than optimized for any single downstream use (0001).

Its basic unit is one document per trajectory (0002). Turn-level documents (one per human/agent turn, sequenced into conversations) and mandatory hierarchical decomposition (a task auto-splitting into a tree of sub-trajectory documents) were both considered and rejected — the former fragments the reasoning the language exists to capture, the latter bakes in decomposition machinery before it's known to be needed. A trajectory can still reference a child trajectory when a subtask is genuinely delegated to a separate agent invocation, but that's the exception, and the delegation mechanics themselves remain undesigned — multi-agent/subagent delegation is explicitly deferred, not because it's unimportant but because there's no clean integration mechanism yet and a solid single-agent language is already a complete result on its own (0005).

Cross-agent comparability — one of the motivating uses — is deliberately kept out of the document model rather than built in as explicit machinery. No shared/canonical intent objects referenced across documents; comparability is expected to fall out of every document using the same standardized language, plus the taxonomy canonization induces as a side effect (0003).

Grammar is shared, not split into two sublanguages. One base grammar (values, expressions, imports) covers both human and AI content, with a small number of role-specific constructs layered on top — a constraint-flavored form for human intent, for instance — rather than the original two-language sketch (BC for cognition, BUIL for human intent). A single trajectory reads more naturally as one continuous stream than a hard switch between grammars, and maintaining two full grammars is unneeded overhead; but human intent and AI cognition remain genuinely different speech acts, which is why a fully unified grammar with no role distinction was rejected too (0004). Following from this, there's no dedicated `intent.*` slot mechanism — cognition references whatever the human-intent block bound using ordinary variable reference, the same as any other reference in the shared grammar, rather than a second bridge mechanism duplicating that job (0008).

Turn boundaries are the one deliberate exception to the language's otherwise tag-free, Pythonic texture: they're marked by reserved meta-tags (e.g. `<|user|>`) rather than a native construct like a keyword block, because reserved chat-style meta-tokens are already a familiar convention to any LLM from training on chat formats — directly serving the requirement that any LLM must be able to interpret a document from documentation alone (0009).

## Vocabulary and Canonization

Vocabulary design is deliberately deferred to corpus-driven canonization rather than locked from vision. Two concrete near-misses illustrate the principle: a structural phase-cycle construct for cognition (perceive → update-belief → decide → act → observe), and a small closed set of "universal environment references" (`history`, `workspace`, `memory`, `web`) — both were nearly adopted from the original design sketch and both were walked back as premature keyword invention. Cognition stays plain imperative code with no enforced phase structure; the environment-reference set is provisional. Any small enumerated vocabulary chosen from vision rather than corpus risks the same mistake — canonization should emerge from what recurs across many real trajectories, not be guessed upfront (0006). What is decided now, independent of that deferred content, is the organizational mechanism: an import/namespace mechanism (à la `from x import y`) for canonized vocabulary. The mechanism is generic and says nothing about content, so it's safe to fix now; the packages themselves and what's importable remain deferred (0007).

When a near-match already exists, the default is to mint a new construct rather than reuse it — fidelity over vocabulary economy, since collapsing real distinctions to keep the vocabulary tight produces documents that no longer say what happened, destroying their value as research artifacts. The accepted cost is a larger vocabulary and near-synonym sprawl risk, counterweighted by an earns-existence gate: a new construct is justified only when the nearest existing one would lose a distinction that matters (0011).

## Fidelity and Semantics

Three rules, deliberately asymmetric, govern what a translation may and may not do (0014):

- **Operations are recovered, not merely transcribed.** The language targets the hypothesized operations a model actually performed, drawn from an idealized space, not just what the trace happens to narrate — encoded when a competent reader would confidently assume the operation occurred, a bound deliberately weaker than logical necessity.
- **Reasoning is never invented.** No motive, deliberation, or justification the source doesn't evidence — inferred reasoning is indistinguishable from recorded reasoning once written, and poisons the corpus for the interpretability uses motivating the project.
- **Human intent is made explicit**, anchored to the subject agent's demonstrated understanding (evidenced by what it went on to do), not the design agent's own reading. A misread request is encoded as the misreading — there's no separate value in recording what the user "really" meant.

Following the same intent-anchor logic, execution errors are not reflected in structure: a document uses the construct for the operation being performed regardless of whether it was performed correctly (miscounting letters still uses the letter-counting construct). This is recorded as the current decision rather than a settled one — it could be overturned if error-analysis use cases need failures to be structurally visible (0015).

What earns a construct in the first place: the clearest case is an operation that transforms data or brings new data into existence (extracting keywords earns one; searching again does not, since repetition is already visible as a sequence of calls). Whether data transformation is the central criterion or one signal among several is unresolved — recorded as the leading candidate, to be settled empirically rather than argued in advance. This supersedes an earlier rule ("decompose as far as the source evidences and no further"), which conflicted with the fidelity contract's license to recover unnarrated operations. Narrative features — sequencing, retrying, falling back — are connective rather than transformational and are not constructs; whether they should be captured at all, and how, is open and secondary (0016).
