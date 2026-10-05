```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    ACTION search_web(target="funny cartoon caption", constraints=[constraint_exclude_liberation_theme]) -> search_web_2 : LIST[REF[STRING]]
    UTTER ask(target=select_option(value="funniest caption"), options=[
      "Believe me, learning to speak was way harder",
      "Relax. When I find the flight-deck, instinct takes over.",
      "Sorry about the water landing--old habit.",
      "Thank you! We know you have a choice when you migrate....",
      "I knew our pilot was Canadian",
      "Of course, I only do water landings...",
      "Make Way, Dude!",
      "And in the event of a water landing, just stick your feet out in front of you",
      "Hey! I appreciate you ordered the fish.",
      "I know what youre thinking, but don't you worry. I'm only silly when I'm off work."
    ])
  }
}
```