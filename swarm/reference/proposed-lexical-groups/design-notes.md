# Design and adoption notes (not translator input)

The normative translator input is one specification variant plus one complete glossary view. Both glossary views include all registered definitions. This file, the migration map, size accounting, and proposal workflow are supporting material; they supply no additional value-admission rules.

This revision removes redundant per-group metadata: definition is the domain contract, consumer signatures determine valid slots, and the spec supplies default admission/key form and shared restrictions. The Markdown glossary renders group fields and registries as tables rather than embedded JSON. Repeated glossary explanations now refer to the spec; distinct vocabulary constraints remain in the glossary.

Open groups admit new labels without per-value records. Registered groups still store member meanings. The difference between deterministic identity and resolved English meaning remains explicit; compaction does not authorize guessed senses or hidden prose.

The runtime schema, parser, retrieval and migrator still need group support. Before adoption, test unseen labels, aliases, wrong groups, hidden clauses, source-sense ambiguity and historical type migration. Artifact checks are not semantic or runtime validation.

## Historical v18 migration and adoption notes

The following material was previously specification Section 17. It records the broader v19 proposal's history; current normative rules remain in Sections 1–16.


| v18 behavior | This draft |
|---|---|
| A common execution interpretation for requests and transcripts | Explicit REQUEST/TRACE modes and descriptive event recording |
| STRING/NUMBER/BOOL/LIST plus references | Adds TERM, CLAIM, EVENT for semantic content |
| Topic symbols and transitional content fields | Compositional meanings plus measured opaque fallbacks |
| No explicit general claim/evidence layer | Attributed claims, epistemic status, provenance, reasoning links |
| Whole-turn revision | Whole replacement plus targeted claim amendment |
| Utterance STRING result binding | Removed; content is represented explicitly |
| Implicit earlier rules for calls/recursion | Explicit CALL grammar and restricted checkable recursion |
| Implicit resource defaults | No invented resources or observations |
| Arbitrary lexical custom-operation fallback | Explicit vocabulary proposals and accepted semantic definitions |
| Domain attributes embedded in grammar prose | Typed glossary profiles and compositional constraints |
| Conflicting example ordering/reference handling | Unified attribute order and explicit object acquisition |

Before adoption:

1. Migrate and review a matching glossary. Preserve original files and historical translations.
2. Define shared semantic relations and compositional constructors beyond the illustrative profiles here.
3. Publish verified examples for every construct and both modes; check all references, signatures, categories, and source locators.
4. Implement a parser/static validator and test the claimed rules. This draft has not been tested against an implemented parser.
5. Compare v18 and this draft on the same requests and traces, including unseen domains, wrong agent interpretations, unsupported hypotheses, partial corrections, and exact-wording tasks.
6. Use independent reconstruction and cross-model translation to decide whether the added semantic structure improves fidelity without excessive complexity.

This draft deliberately does not claim full natural-language coverage or executable deployment readiness. Its acceptance criterion is preserving more recoverable meaning while retaining the new specification's explicit structure and canonicalization.
