```braincode
MODE REQUEST
ENTRYPOINT Conversation
TASK Translate {
  ACTION translate(target="the eagle's snake", source_language="English", target_language="Vai") -> result : TERM
  ACTION search_web(query="Vai language", attributes=["glossary", "phrase", "translation"]) -> result : LIST[REF[STRING]]
  ACTION generate(target="Vai translation", content=result, attributes=["glossary", "phrase", "translation"]) -> result : TERM
  ACTION send_translation(target=result, attributes=["glossary", "phrase", "translation"]) -> result : TERM
}
```