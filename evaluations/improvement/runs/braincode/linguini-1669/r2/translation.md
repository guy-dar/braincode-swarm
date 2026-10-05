```braincode
MODE REQUEST
ENTRYPOINT Translation
TASK Translation {
  ACTION translate(target=ile, source_language="Tundra Yukaghir", target_language="English") -> translation : STRING
  ACTION lookup(source_language="Tundra Yukaghir", target_language="English", target=ewce) -> ewce_translation : STRING
  CLAIM tip_point_means(target=ewce_translation) BY source STATUS asserted SOURCE "source text" -> tip_point_means_2 : CLAIM
  CLAIM translation_means(target=translation) BY source STATUS asserted SOURCE "source text" -> translation_means_2 : CLAIM
  LINK supports(conclusion=translation_means_2, premise=tip_point_means_2) SOURCE "source text"
}
```