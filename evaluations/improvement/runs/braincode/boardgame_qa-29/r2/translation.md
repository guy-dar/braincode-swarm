```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  ACTION ask(target="What is the current state of the game?") -> question_1 : TERM
  ACTION describe_state(target=question_1, state="The akita tears down the castle that belongs to the starling.") -> state_1 : TERM
  ACTION describe_state(target=state_1, state="The bee is currently in Cape Town.") -> state_2 : TERM
  ACTION describe_state(target=state_2, state="The crow dances with the dugong.") -> state_3 : TERM
  ACTION describe_state(target=state_3, state="The dalmatian is named Tarzan.") -> state_4 : TERM
  ACTION describe_state(target=state_4, state="The dove destroys the wall constructed by the rhino.") -> state_5 : TERM
  ACTION describe_state(target=state_5, state="The dragon is named Charlie.") -> state_6 : TERM
  ACTION describe_state(target=state_6, state="The dragon is a grain elevator operator.") -> state_7 : TERM
  ACTION describe_state(target=state_7, state="The dugong is named Lucy.") -> state_8 : TERM
  ACTION describe_state(target=state_8, state="The fangtooth is named Bella.") -> state_9 : TERM
  ACTION describe_state(target=state_9, state="The gadwall has a card that is indigo in color, and has a football with a radius of 17 inches.") -> state_10 : TERM
  ACTION describe_state(target=state_10, state="The leopard tears down the castle that belongs to the butterfly.") -> state_11 : TERM
  ACTION describe_state(target=state_11, state="The liger has 91 dollars.") -> state_12 : TERM
  ACTION describe_state(target=state_12, state="The lizard is named Casper.") -> state_13 : TERM
  ACTION describe_state(target=state_13, state="The mermaid disarms the gorilla, and has 75 dollars.") -> state_14 : TERM
  ACTION describe_state(target=state_14, state="The mermaid is named Teddy.") -> state_15 : TERM
  ACTION describe_state(target=state_15, state="The mule has 16 dollars.") -> state_16 : TERM
  ACTION describe_state(target=state_16, state="The vampire has 15 friends, and is four years old.") -> state_17 : TERM
  ACTION describe_state(target=state_17, state="The german shepherd does not bring an oil tank for the vampire.") -> state_18 : TERM
  ACTION describe_state(target=state_18, state="The swallow does not suspect the truthfulness of the gadwall.") -> state_19 : TERM
  ACTION describe_rules(target="What are the rules of the game?") -> rules_1 : TERM
  ACTION describe_rule(target=rules_1, rule="Rule1: If there is evidence that one animal, no matter which one, invests in the company owned by the snake, then the goat enjoys the company of the shark undoubtedly.") -> rule_1 : TERM
  ACTION describe_rule(target=rule_1, rule="Rule2: If at least one animal hides the cards that she has from the badger, then the poodle falls on a square that belongs to the mouse.") -> rule_2 : TERM
  ACTION describe_rule(target=rule_2, rule="Rule3: The vampire unquestionably wants to see the dinosaur, in the case where the german shepherd does not bring an oil tank for the vampire.") -> rule_3 : TERM
  ACTION describe_rule(target=rule_3, rule="Rule4: If the crow dances with the dugong, then the dugong calls the basenji.") -> rule_4 : TERM
  ACTION describe_rule(target=rule_4, rule="Rule5: The shark does not tear down the castle of the songbird whenever at least one animal acquires a photograph of the bulldog.") -> rule_5 : TERM
  ACTION describe_rule(target=rule_5, rule="Rule6: The leopard invests in the company owned by the snake whenever at least one animal manages to persuade the cobra.") -> rule_6 : TERM
  ACTION describe_rule(target=rule_6, rule="Rule7: There exists an animal which builds a power plant close to the green fields of the seahorse?") -> rule_7 : TERM
  ACTION describe_rule(target=rule_7, rule="Rule8: If you are positive that one of the animals does not smile at the wolf, you can be certain that it will acquire a photo of the badger without a doubt.") -> rule_8 : TERM
  ACTION describe_rule(target=rule_8, rule="Rule9: This is a basic rule: if the reindeer creates one castle for the pelikan, then the conclusion that 'the pelikan surrenders to the beaver' follows immediately and effectively.") -> rule_9 : TERM
  ACTION describe_rule(target=rule_9, rule="Rule10: One of the rules of the game is that if the elk dances with the poodle, then the poodle will never fall on a square of the mouse.") -> rule_10 : TERM
  ACTION describe_rule(target=rule_10, rule="Rule11: If the gadwall has a card whose color starts with the letter 'i', then the gadwall captures the king (i.e. the most important piece) of the finch.") -> rule_11 : TERM
  ACTION describe_rule(target=rule_11, rule="Rule12: The dugong will not call the basenji if it (the dugong) has a name whose first letter is the same as the first letter of the fangtooth's name.") -> rule_12 : TERM
  ACTION describe_rule(target=rule_12, rule="Rule13: Here is an important piece of information about the dragon: if it works in computer science and engineering then it creates one castle for the ant for sure.") -> rule_13 : TERM
  ACTION describe_rule(target=rule_13, rule="Rule14: The living creature that disarms the gorilla will never shout at the mannikin.") -> rule_14 : TERM
  ACTION describe_rule(target=rule_14, rule="Rule15: If something disarms the flamingo, then it hugs the fish, too.") -> rule_15 : TERM
  ACTION describe_rule(target=rule_15, rule="Rule16: If there is evidence that one animal, no matter which one, destroys the wall constructed by the rhino, then the dinosaur builds a power plant near the green fields of the seahorse undoubtedly.") -> rule_16 : TERM
  ACTION describe_rule(target=rule_16, rule="Rule17: One of the rules of the game is that if the beaver smiles at the elk, then the elk will never dance with the poodle.") -> rule_17 : TERM
  ACTION describe_rule(target=rule_17, rule="Rule18: If there is evidence that one animal, no matter which one, borrows a weapon from the cougar, then the bee is not going to acquire a photo of the badger.") -> rule_18 : TERM
  ACTION describe_rule(target=rule_18, rule="Rule19: If the gadwall has a football that fits in a 28.9 x 27.4 x 39.7 inches box, then the gadwall captures the king of the finch.") -> rule_19 : TERM
  ACTION describe_rule(target=rule_19, rule="Rule20: There exists an animal which takes over the emperor of the stork?") -> rule_20 : TERM
  ACTION describe_rule(target=rule_20, rule="Then the dinosaur definitely dances with the shark.") -> rule_20_1 : TERM
  ACTION describe_rule(target=rule_20_1, rule="Rule21: If the pelikan does not tear down the castle of the reindeer, then the reindeer does not create a castle for the pelikan.") -> rule_21 : TERM
  ACTION describe_rule(target=rule_21, rule="Rule22: If there is evidence that one animal, no matter which one, surrenders to the beaver, then the elk dances with the poodle undoubtedly.") -> rule_22 : TERM
  ACTION describe_rule(target=rule_22, rule="Rule23: If the bee is in Africa at the moment, then the bee does not smile at the wolf.") -> rule_23 : TERM
  ACTION describe_rule(target=rule_23, rule="Rule24: If at least one animal calls the basenji, then the mannikin wants to see the crow.") -> rule_24 : TERM
  ACTION describe_rule(target=rule_24, rule="Rule25: If there is evidence that one animal, no matter which one, swims inside the pool located besides the house of the goose, then the dragon acquires a photograph of the bulldog undoubtedly.") -> rule_25 : TERM
  ACTION describe_rule(target=rule_25, rule="Rule26: If you are positive that you saw one of the animals captures the king (i.e. the most important piece) of the finch, you can be certain that it will also want to see the dolphin.") -> rule_26 : TERM
  ACTION describe_rule(target=rule_26, rule="Rule27: One of the rules of the game is that if the vampire does not build a power plant near the green fields of the ostrich, then the ostrich will, without hesitation, take over the emperor of the stork.") -> rule_27 : TERM
  ACTION describe_rule(target=rule_27, rule="Rule28: There exists an animal which tears down the castle that belongs to the starling?") -> rule_28 : TERM
  ACTION describe_rule(target=rule_28, rule="Then the duck definitely dances with the ant.") -> rule_28_1 : TERM
  ACTION describe_rule(target=rule_28_1, rule="Rule29: Here is an important piece of information about the mermaid: if it has more money than the mule and the liger combined then it shouts at the mannikin for sure.") -> rule_29 : TERM
  ACTION describe_rule(target=rule_29, rule="Rule30: Here is an important piece of information about the dragon: if it has a name whose first letter is the same as the first letter of the lizard's name then it creates one castle for the ant for sure.") -> rule_30 : TERM
  ACTION describe_rule(target=rule_30, rule="Rule31: This is a basic rule: if the coyote does not call the dragon, then the conclusion that the dragon will not create a castle for the ant follows immediately and effectively.") -> rule_31 : TERM
  ACTION describe_rule(target=rule_31, rule="Rule32: One of the rules of the game is that if the mermaid shouts at the mannikin, then the mannikin will never want to see the crow.") -> rule_32 : TERM
  ACTION describe_rule(target=rule_32, rule="Rule33: Be careful when something does not tear down the castle that belongs to the songbird but hugs the fish because in this case it will, surely, hide the cards that she has from the badger (this may or may not be problematic).") -> rule_33 : TERM
  ACTION describe_rule(target=rule_33, rule="Rule34: If the dugong is watching a movie that was released after Facebook was founded, then the dugong does not call the basenji.") -> rule_34 : TERM
  ACTION describe_rule(target=rule_34, rule="Rule35: This is a basic rule: if the leopard tears down the castle that belongs to the butterfly, then the conclusion that 'the butterfly manages to convince the cobra' follows immediately and effectively.") -> rule_35 : TERM
  ACTION describe_rule(target=rule_35, rule="Rule36: If you are positive that one of the animals does not smile at the wolf, you can be certain that it will acquire a photo of the badger without a doubt.") -> rule_36 : TERM
  ACTION describe_rule(target=rule_36, rule="Rule37: If there is evidence that one animal, no matter which one, wants to see the dolphin, then the reindeer creates a castle for the pelikan undoubtedly.") -> rule_37 : TERM
  ACTION describe_rule(target=rule_37, rule="Rule38: The vampire will not want to see the dinosaur if it (the vampire) has fewer than five friends.") -> rule_38 : TERM
  ACTION describe_rule(target=rule_38, rule="Rule39: If the mermaid has a name whose first letter is the same as the first letter of the dalmatian's name, then the mermaid shouts at the mannikin.") -> rule_39 : TERM
  ACTION describe_rule(target=rule_39, rule="Rule40: From observing that one animal wants to see the dinosaur, one can conclude that it also builds a power plant near the green fields of the ostrich, undoubtedly.") -> rule_40 : TERM
  ACTION describe_rule(target=rule_40, rule="Rule41: There exists an animal which acquires a photograph of the badger?") -> rule_41 : TERM
  ACTION describe_rule(target=rule_41, rule="Then the beetle definitely swears to the shark.") -> rule_41_1 : TERM
  ACTION describe_rule(target=rule_41_1, rule="Rule42: In order to conclude that the ant swims in the pool next to the house of the goose, two pieces of evidence are required: firstly the duck should dance with the ant and secondly the dragon should create a castle for the ant.") -> rule_42 : TERM
  ACTION describe_rule(target=rule_42, rule="Rule43: One of the rules of the game is that if the beetle swears to the shark, then the shark will, without hesitation, tear down the castle of the songbird.") -> rule_43 : TERM
  ACTION describe_rule(target=rule_43, rule="Rule12 is preferred over Rule4.") -> rule_12_preferred : TERM
  ACTION describe_rule(target=rule_12_preferred, rule="Rule17 is preferred over Rule22.") -> rule_17_preferred : TERM
  ACTION describe_rule(target=rule_17_preferred, rule="Rule18 is preferred over Rule36.") -> rule_18_preferred : TERM
  ACTION describe_rule(target=rule_18_preferred, rule="Rule2 is preferred over Rule10.") -> rule_2_preferred : TERM
  ACTION describe_rule(target=rule_2_preferred, rule="Rule21 is preferred over Rule37.") -> rule_21_preferred : TERM
  ACTION describe_rule(target=rule_21_preferred, rule="Rule24 is preferred over Rule32.") -> rule_24_preferred : TERM
  ACTION describe_rule(target=rule_24_preferred, rule="Rule29 is preferred over Rule14.") -> rule_29_preferred : TERM
  ACTION describe_rule(target=rule_29_preferred, rule="Rule3 is preferred over Rule38.") -> rule_3_preferred : TERM
  ACTION describe_rule(target=rule_3_preferred, rule="Rule31 is preferred over Rule13.") -> rule_31_preferred : TERM
  ACTION describe_rule(target=rule_31_preferred, rule="Rule31 is preferred over Rule30.") -> rule_31_preferred_1 : TERM
  ACTION describe_rule(target=rule_31_preferred_1, rule="Rule34 is preferred over Rule4.") -> rule_34_preferred : TERM
  ACTION describe_rule(target=rule_34_preferred, rule="Rule39 is preferred over Rule14.") -> rule_39_preferred : TERM
  ACTION describe_rule(target=rule_39_preferred, rule="Rule5 is preferred over Rule43.") -> rule_5_preferred : TERM
  ACTION describe_rule(target=rule_5_preferred, rule="Rule7 is preferred over Rule40.") -> rule_7_preferred : TERM
  ACTION describe_rule(target=rule_7_preferred, rule="A rule is only applicable if all of its antecedents can be proved.") -> rule_applicable : TERM
  ACTION describe_rule(target=rule_applicable, rule="If a rule is preferred over the other, it means whenever both of them can be applied to derive new conclusions and those conclusions contradict with each other (e.g., from one we derive X and from the other we derive not X), we should go with the conclusion from the rule with higher preference.") -> rule_preferred : TERM
  ACTION describe_rule(target=rule_preferred, rule="Based on the facts, rules, and preferences, what is the truth value of the statement, does the poodle fall on a square of the mouse?") -> truth_value : CLAIM
  ACTION describe_rule(target=truth_value, truth_value="proved") -> answer : CLAIM
}
```