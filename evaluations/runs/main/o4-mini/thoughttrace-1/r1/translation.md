Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    UTTER greeting(recipient=role_agent)
    TERM offer_help() -> offer_help_2 : TERM
    UTTER ask(target=offer_help_2)
    TERM activity(verb="categorize", actor=role_user, object="méthodes d'organisation") -> categorize_methods_2 : TERM
    UTTER ask(target=categorize_methods_2)
    TERM genre_label::fanfiction -> fanfiction_2 : TERM
    UTTER inform(target=fanfiction_2)
  }
  TURN t2 SPEAKER=AGENT {
    UTTER greeting(recipient=role_user)
    TERM sections_seq: TERM
    TERM sequence(items=[
      document_section(title="LA BIBLE DE L'HISTOIRE", items=[
        include(item="Résumé global"),
        include(item="Thèmes principaux"),
        include(item="Ton et ambiance"),
        include(item="Public visé"),
        include(item="Longueur estimée")
      ]),
      document_section(title="FICHES PERSONNAGES", items=[
        include(item="Nom / surnom"),
        include(item="Rôle dans ton histoire"),
        include(item="Comment tu le réinterprètes"),
        include(item="Traits de personnalité"),
        include(item="Motivations & objectifs"),
        include(item="Arc narratif prévu"),
        include(item="Relations avec les autres personnages")
      ]),
      document_section(title="WORLDBUILDING & CADRE", items=[
        include(item="Univers d'origine"),
        include(item="Lieu(x) principaux"),
        include(item="Époque / timeline"),
        include(item="Points de divergence"),
        include(item="Règles spécifiques à ton univers")
      ])
    ]) -> sections_seq_2 : TERM  # PROPOSED: S1
    UTTER propose(target=sections_seq_2)
  }
}
```

## Needs coverage

| need   | kind       | expressed by                                     | status    |
|--------|------------|--------------------------------------------------|-----------|
| n1     | speech_act | greeting                                         | covered   |
| n2     | action     | offer_help, ask                                  | covered   |
| n3     | action     | activity(verb="categorize",…)                  | covered   |
| n4     | object     | sequence(document_section…)                      | proposed  |
| n5     | object     | genre_label::fanfiction                          | covered   |
| n6     | claim      | —                                                | unresolved|
| n7     | speech_act | greeting                                         | covered   |
| n8     | action     | sequence(document_section…)                      | proposed  |
| n9–n30 | various    | —                                                | unresolved|

## Why the translation failed

- n4 “story planning and organization framework” and n8 “present a comprehensive organization guide for fanfiction writing” require a term to package multiple document_section items into a single planning guide term; sequence alone is insufficient for semantic clarity.
- Remaining needs (detailed sections beyond t2) likewise require higher-level constructors or composites.

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: turns t1–t2 represented; turns t3–t8 not fully covered
- Opaque-text spans: none
- Missing constructs: S1: `sequence` does not semantically represent a planning guide term
- Unresolved ambiguities: none
- Check: `rag check` reported unresolved needs and unknown symbol `sections_seq`
