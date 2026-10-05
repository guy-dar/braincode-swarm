```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  ACTION ask(target="Does the dinosaur enjoy the company of the husky?")
  -> answer : CLAIM
  ACTION generate(target="dinosaur", value="enjoys", qualifier="the company of", object="husky")
  -> conclusion : CLAIM
  LINK supports(conclusion=conclusion, premise="Rule3: From observing that one animal swears to the pigeon, one can conclude that it also shouts at the dalmatian, undoubtedly.")
  -> rule3 : CLAIM
  ACTION record(event="Rule3", conclusion=conclusion)
  -> rule3_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome : EVENT
  LINK supports(conclusion=conclusion, premise="Rule3 is preferred over Rule17.")
  -> rule3_preferred : CLAIM
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion")
  -> rule3_outcome_record : EVENT
  ACTION record(event="Rule3", preference="preferred")
  -> rule3_preferred_record : EVENT
  ACTION record(event="Rule3", conclusion="conclusion")
  -> rule3_conclusion_record : EVENT
  ACTION record(event="Rule3", evidence="animal swears to the pigeon")
  -> rule3_evidence_record : EVENT
  ACTION record(event="Rule3", outcome="conclusion