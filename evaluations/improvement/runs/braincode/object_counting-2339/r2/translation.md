```braincode
MODE REQUEST
ENTRYPOINT Musical Instruments and Mobiles
TASK Musical Instruments and Mobiles {
  ACTION count_musical_instruments_and_mobiles() -> count : NUMBER
  ACTION count_musical_instruments() -> count_musical_instruments : NUMBER
  ACTION count_mobiles() -> count_mobiles : NUMBER
  GENERATE(target=art_itinerary, constraints=[count_musical_instruments, count_mobiles], topic=count) -> count : NUMBER
  RETURN count
}
```