Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM work_life_balance(location=country::JP) -> work_life_balance_2 : TERM    # PROPOSED: S1
    UTTER ask(target=work_life_balance_2)
  }
  TURN t2 SPEAKER=AGENT {
    # Most detailed claims about policies and outcomes are unresolved under current glossary
  }
  TURN t3 SPEAKER=USER {
    TERM multiple_part_time_jobs(subject=country::JP) -> multiple_part_time_jobs_2 : TERM    # PROPOSED: S2
    UTTER ask(target=multiple_part_time_jobs_2)
  }
  TURN t4 SPEAKER=AGENT {
    UTTER confirm(target=multiple_part_time_jobs_2)
  }
}
```

## Needs coverage

| need | kind       | expressed by                           | status     |
|------|------------|----------------------------------------|------------|
| n1   | speech_act | ask                                    | covered    |
| n2   | object     | country::JP                            | covered    |
| n3   | object     | work_life_balance (PROPOSED: S1)       | proposed   |
| n4   | object     | work_life_balance (PROPOSED: S1)       | proposed   |
| n5   | temporal   | —                                      | unresolved |
| n6   | claim      | —                                      | unresolved |
| n7   | claim      | —                                      | unresolved |
| n8   | claim      | —                                      | unresolved |
| n9   | claim      | —                                      | unresolved |
| n10  | reasoning  | —                                      | unresolved |
| n11  | claim      | —                                      | unresolved |
| n12  | object     | country::JP                            | covered    |
| n13  | speech_act | ask                                    | covered    |
| n14  | object     | multiple_part_time_jobs (PROPOSED: S2) | proposed   |
| n15  | constraint | —                                      | unresolved |
| n16  | speech_act | confirm                                | covered    |
| n17  | object     | country::JP                            | covered    |
| n18  | claim      | —                                      | unresolved |
| n19  | claim      | —                                      | unresolved |
| n20  | claim      | —                                      | unresolved |

## Why the translation failed

- n3, n4 “work and working hours” and “leisure time and personal hobbies”: no existing TERM constructor covers the broad concept of work-life balance or leisure-time enjoyment in a location.
- n14 “multiple part-time jobs”: no existing TERM constructor expresses the concept of having multiple jobs.
- All intermediate claims (n5–n11, n15, n18–n20) about policy details, outcomes, and reasoning links lack suitable constructors or composites in the glossary.

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: t1:s1, t3:s1, t4:s1 covered; other spans formalized only with proposed symbols or unresolved
- Opaque-text spans: none
- Label-preserved spans: none
- Missing constructs: S1 work_life_balance constructor; S2 multiple_part_time_jobs constructor
- Unresolved ambiguities: none
- Check: `rag check` reported 13 unresolved needs (n5, n6, n7, n8, n9, n10, n11, n15, n18, n19, n20), 2 proposed symbols (work_life_balance, multiple_part_time_jobs)
