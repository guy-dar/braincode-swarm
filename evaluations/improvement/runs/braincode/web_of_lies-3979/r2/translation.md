```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  ACTION run_tests(target=platform_label::braincode_language_specification, assertion=statement(fact="all people either always tell the truth or always lie")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="all people either always tell the truth or always lie")) -> result : BOOL
  ACTION run_tests(target=platform_label::value_group_catalog, assertion=statement(fact="all people either always tell the truth or always lie")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_symbols, assertion=statement(fact="all people either always tell the truth or always lie")) -> result : BOOL
  ACTION run_tests(target=platform_label::local_handles, assertion=statement(fact="all people either always tell the truth or always lie")) -> result : BOOL
  ACTION run_tests(target=platform_label::literals, assertion=statement(fact="all people either always tell the truth or always lie")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Bernita says Elanor tells the truth")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="McKenzie says Miranda lies")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Maurice says Minnie tells the truth")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Ofelia says Oprah tells the truth")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Amberly says exactly two of Alejandro, Miranda and McKenzie tell the truth")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Ophelia says Monica lies")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Orin says Moses tells the truth")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Elanor says only one of Sherrie, Morris and Ollie lies")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Fletcher says Delfina lies")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Alejandro tells the truth")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Delfina says either all three of Gwenn, Moses and Orin lie, or two of them tell the truth")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Mallory says Oprah lies")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Marsha says Osbert tells the truth")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Odile says Maria tells the truth")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Marlon says Otto tells the truth")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Marina says Otis tells the truth")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Kandi says only one of Willian, Mike and Oswin lies")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Tamika says only one of Vina, Marshall and Max lies")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Octavia says Mateo lies")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Sal says either all three of Fletcher, Marsha and Osbert lie, or two of them tell the truth")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Marvin says Oakley tells the truth")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Oden says Minnie lies")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Dallas says either exactly one of Raymond, Otis and Marina tells the truth, or all three of them")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Ryan says only one of Sima, Ofelia and Mallory lies")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Sima says either all three of Amberly, Octavius and Mary tell the truth or only one of them")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Otis says Marina tells the truth")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Mateo says Octavia lies")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Otto says Marlon tells the truth")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Odin says Maria lies")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Morris says John tells the truth")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Raymond says either exactly two of Ryan, Marlon and Otto tell the truth or none of them")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Teressa says Alexis lies")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Vina says either exactly one of Teressa, Oakley and Marvin tells the truth, or all three of them")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Lalit says Monica tells the truth")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Gwenn says Bernita, Maurice and Oden all tell the truth")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Octavius says Mary tells the truth")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Oswin says Melinda lies")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Sherrie says only one of Fidel, Odile and Odin lies")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Willian says Tamika tells the truth")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Miranda says McKenzie lies")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Osbert says Marsha tells the truth")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Marshall says Orhan tells the truth")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Vernell says only one of Shenna, Miguel and Olga lies")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Miguel says Ozzy tells the truth")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Alexis says only one of Dallas, Lalit and Ophelia tells the truth")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Moses says Orin tells the truth")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Max says Orhan lies")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Mary says Octavius tells the truth")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Olga says Ozzy lies")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Fidel says Vernell lies")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Ollie says John lies")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Mike says Melinda tells the truth")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Oakley says Marvin tells the truth")) -> result : BOOL
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="Shenna says exactly two of Kandi, Mateo and Octavia tells the truth")) -> result : BOOL
  UTTER ask(target=statement(fact="Do Fidel, Gwenn, and Sal tell the truth?")) -> ask_2 : TERM
  ACTION run_tests(target=platform_label::glossary_entries, assertion=statement(fact="ask_2")) -> result : BOOL
  ACTION generate(target=art_short_text, format=format_bullet_list, tone=tone_neutral, topic=ask_2) -> short_text : STRING
  ACTION send_message(content=short_text, recipient=role_agent)
}