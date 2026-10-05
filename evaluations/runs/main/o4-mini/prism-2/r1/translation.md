Status: failed
Mode: TRACE

## Suggested translation

```braincode
MODE TRACE
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TERM activity(verb="mow", object=object_label::lawn) -> activity_1 : TERM
    UTTER ask(target=activity_1)
  }
  TURN t2 SPEAKER=AGENT {
    UTTER inform(content="To mow your lawn, you'll need a lawn mower, gardening gloves, and protective eyewear.")
    UTTER inform(content="Begin by preparing the lawn area by removing any debris or obstacles.")
    UTTER inform(content="Adjust the height of your mower blades to ensure an even cut - you typically want to cut no more than one third of the grass height in one mowing.")
    UTTER inform(content="Mow in straight lines back and forth, maintaining an even pace, and trying to avoid mowing in the same direction each time to prevent uneven cutting.")
    UTTER inform(content="Once you've mowed the entire lawn, consider trimming any edges using a string trimmer or edger.")
    UTTER inform(content="Be sure to follow all safety instructions provided with your lawn mower and wear appropriate safety gear.")
    UTTER offer(target="I hope this helps! Let me know if you have any questions about the safety or process of mowing your lawn.")
  }
  TURN t3 SPEAKER=USER {
    TERM property_question(property="cutting_method", subject=object_label::grass) -> question_2 : TERM  # PROPOSED: S1
    UTTER ask(target=question_2)
  }
  TURN t4 SPEAKER=AGENT {
    UTTER inform(content="You may cut grass with scissors, but it is not a practical or efficient method for mowing large lawns.")
    UTTER inform(content="Using scissors to cut grass may be useful for small patches of grass, detailing around obstacles, or ornamental grooming of small garden areas.")
    UTTER inform(content="It can provide a neater, more precise finish than a mower.")
    UTTER inform(content="For larger lawns, it is recommended to use a mower as it will save you significant time and effort.")
    UTTER inform(content="Mowers are designed to efficiently cut large areas of grass, and they help ensure an even cut and uniform appearance across the entire lawn.")
    UTTER offer(target="Feel free to ask if you have any more questions about lawn care or gardening.")
  }
}
```

## Needs coverage

| need | kind      | expressed by                                          | status      |
|------|-----------|-------------------------------------------------------|-------------|
| n1   | speech_act| ask(target=activity_1)                                | covered     |
| n2   | action    | activity(verb="mow", object=object_label::lawn)     | covered     |
| n3   | object    | object_label::lawn_mower                              | covered     |
| n4   | object    | object_label::gardening_gloves                        | covered     |
| n5   | object    | object_label::protective_eyewear                      | covered     |
| n6   | temporal  | (speech act order)                                    | covered     |
| n7   | action    | literal in UTTER inform (remove debris and obstacles) | opaque      |
| n8   | action    | literal in UTTER inform (adjust blade height)         | opaque      |
| n9   | constraint| literal in UTTER inform (no more than one third…)      | opaque      |
| n10  | action    | literal in UTTER inform (mow in straight lines…)      | opaque      |
| n11  | negation  | literal in UTTER inform (avoid same direction…)       | opaque      |
| n12  | temporal  | (order)                                               | covered     |
| n13  | action    | literal in UTTER inform (trim edges…)                 | opaque      |
| n14  | object    | object_label::string_trimmer, object_label::edger     | covered     |
| n15  | constraint| literal in UTTER inform (follow instructions, wear gear) | opaque   |
| n16  | speech_act| offer(target=...)                                     | covered     |
| n17  | speech_act| ask(target=question_2)                                | covered     |
| n18  | object    | object_label::scissors                                | covered     |
| n19  | claim     | inform(content=... inefficient method)                | covered     |
| n20  | claim     | inform(content=... useful for small patches)          | covered     |
| n21  | claim     | inform(content=... recommended to use mower)          | covered     |
| n22  | reasoning | —                                                     | unresolved  |
| n23  | speech_act| offer(target="Feel free to ask…")                   | covered     |

## Why the translation failed

- n7, n8, n9, n10, n11, n13, n15: These procedural steps and constraints appear only as literal strings in UTTER inform, not as structured TERM constructors. Existing constructors cannot capture multi-part instructions or fractional constraints (e.g., "one third of grass height").
- n22: No glossary link relation exists to record explanatory reasoning connecting mower design to efficiency.

## Translation report

- Input kind: conversation
- Coverage status: partial
- Source-span coverage: all sentences t1:s1–t4:s7 appear, but many steps are opaque
- Opaque-text spans: t2:s3–s7 steps and constraint spans marked opaque
- Label-preserved spans: none
- Missing constructs: see suggestions
- Unresolved ambiguities: none
- Check: `rag check` reported unresolved needs (n7, n8, n9, n10, n11, n13, n15, n22) and use of proposed symbol question_2
