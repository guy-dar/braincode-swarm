# Group-first examples and validation cases

Design examples under this candidate, not evidence of an implemented BrainCode parser. Group examples are not admission whitelists.

## Migrated values disappear from active vocabulary

Source: move two pillows from the sofa onto the armchair, with those source-supported kind labels. Old bare pillow, sofa and armchair rows no longer exist in the active candidate.

```braincode
MODE REQUEST
ENTRYPOINT ObjectLabelPillow
TASK ObjectLabelPillow {
  ACTION pick_up(target=object_label::pillow, quantity=2, source=object_label::sofa) -> object_label_pillow_refs : LIST[REF[STRING]]
  FOR EACH item IN object_label_pillow_refs {
    ACTION place(target=item, destination=object_label::armchair, relation=on)
  }
}
```

The domain-qualified labels identify descriptions. The action still acquires REF identities, and placement requires those identities. A use depending on further unstated properties of the old nouns is not automatically preserved.

## A new word needs no new entry

Source: acquire a catalog item labeled thimble in the requested color category ochre. Neither key needs a standalone definition or a registry member.

```braincode
MODE REQUEST
ENTRYPOINT ObjectLabelThimble
TASK ObjectLabelThimble {
  ACTION pick_up(target=object_label::thimble, color=color_label::ochre) -> object_label_thimble_ref : REF[STRING]
}
```

This preserves labels, not inferred dimensions or color coordinates. The labels are reported as label-preserved. If a source requires an exact unresolved hue or object sense, the translation remains partial until the required distinction is represented.

## Registry consolidation

An amount in the South African rand currency uses:

```braincode
MODE REQUEST
ENTRYPOINT Request
TASK Request : TERM {
  TERM measure(amount=100, unit=currency::ZAR) -> measure_2 : TERM
  RETURN measure_2
}
```

curr_zar is no longer an active symbol. Its identity definition is retained in the currency registry; currency::ZZZ is invalid. No exchange rate or conversion is implied. Registered member definitions are counted separately from glossary rows.

## Required outcomes

| Case | Expected outcome |
|---|---|
| object_label::thimble or color_label::ochre absent from illustrative examples | Admit under open-group rules; source fidelity still required |
| bare pillow, color_red, curr_zar | Reject as retired vocabulary in this candidate |
| pick_up(target=genre_label::comedy) | Reject wrong atom group |
| place(target=object_label::pillow, destination=table) | Reject: target must be REF |
| LET x : STRING = color_label::ochre | Reject implicit cast |
| color_label::gray | Canonicalize through explicit sparse alias to color_label::grey |
| food_label::spud | Canonicalize through explicit sparse alias to food_label::potato |
| animal_label::tuna used for a prepared food requirement | Wrong source role; no cross-group coercion |
| object_label::bat with a required unresolved animal/tool sense | Syntax may pass; semantic completeness fails |
| object_label::phone to evade the existing exact phone meaning | Reject canonical selection; use retained exception when exactly applicable |
| food_label::boiledegg used to hide preparation | Reject hidden modifier; encode preparation explicitly |
| object_label::memory_foam | Reject open key form; material_memory_foam remains a semantic exception |
| object_label::dothisandthenquit | Reject hidden instruction in semantic review |
| a list of words encoding a sentence | Not formalized coverage |
| animal_label::tuna == food_label::tuna | Reject different atom types |
| color_label::red == color_label::red | Identity true inside a legal Check |
| color_label::red < color_label::blue | Reject atom ordering |
| IF color_label::red THEN ... | Reject atom truthiness |
| country::japan in search_web.location | Admit pinned member in declared slot |
| country::georgia | Reject unregistered member |
| plant_label::begonia before group acceptance | Reject unknown group |
| group accepted without matching consumer signature | Reject incomplete migration |
| alias cycle or duplicate canonical sense ID in a registry | Reject noncanonical group |
| executable atom or atom used as CLAIM predicate | Reject: values never introduce operations or propositions |

Mechanical checks verify record structure, mappings and type declarations. Human/independent semantic evaluation still decides whether a nominal mapping preserves the particular source meaning. No automatic losslessness claim is made for every historical use of a removed symbol.
