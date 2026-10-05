```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    TASK DinosaurHusky {
      ACTION ask(target=term(dinosaur::enjoys, husky::enjoys)) -> result : TERM
      CLAIM result BY user STATUS unknown SOURCE "t1:ask" -> result_2 : CLAIM
    }
  }
}
```