```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    CLAIM corn_with_legs(location=road) BY user STATUS hypothesized SOURCE "t1:s1" -> corn_with_legs_2 : CLAIM
    UTTER ask(target=question) BY user STATUS asserted SOURCE "t1:s2" -> question_2 : TERM
    LINK motivates(target=question_2, motive=humor) BY user STATUS hypothesized SOURCE "t1:s2"
    LINK supports(conclusion=funniest, premise=humor) BY user STATUS hypothesized SOURCE "t1:s3"
    CLAIM funniest(target=term) BY user STATUS hypothesized SOURCE "t1:s4" -> funniest_2 : TERM
    RECORD ACTION search_web(target=funniest_2, constraints=[humor], location=NewYorker) STATUS attempted SOURCE "t1:s5" -> search_web_event : EVENT
    LINK rejects(evidence=search_web_event, hypothesis=humor) BY user STATUS hypothesized SOURCE "t1:s5"
    CLAIM humor(target=term) BY user STATUS hypothesized SOURCE "t1:s5" -> humor_2 : TERM
    LINK supports(conclusion=funniest_2, premise=humor_2) BY user STATUS hypothesized SOURCE "t1:s6"
    CLAIM funniest_2(target=term) BY user STATUS hypothesized SOURCE "t1:s6" -> funniest_3 : TERM
    RECORD ACTION search_web(target=funniest_3, constraints=[humor], location=NewYorker) STATUS attempted SOURCE "t1:s7" -> search_web_event_2 : EVENT
    LINK supports(conclusion=funniest_3, premise=search_web_event_2) BY user STATUS hypothesized SOURCE "t1:s7"
    RECORD ACTION search_web(target=funniest_3, constraints=[humor], location=NewYorker) STATUS succeeded SOURCE "t1:s8" -> search_web_event_3 : EVENT
    LINK supports(conclusion=funniest_3, premise=search_web_event_3) BY user STATUS observed SOURCE "t1:s8"
    RECORD ACTION select_option(target=funniest_3, value=A) STATUS attempted SOURCE "t1:s9" -> select_option_event : EVENT
    LINK rejects(evidence=select_option_event, hypothesis=funniest_3) BY user STATUS hypothesized SOURCE "t1:s9"
    RECORD ACTION select_option(target=funniest_3, value=B) STATUS attempted SOURCE "t1:s10" -> select_option_event_2 : EVENT
    LINK rejects(evidence=select_option_event_2, hypothesis=funniest_3) BY user STATUS hypothesized SOURCE "t1:s10"
    RECORD ACTION select_option(target=funniest_3, value=C) STATUS attempted SOURCE "t1:s11" -> select_option_event_3 : EVENT
    LINK rejects(evidence=select_option_event_3, hypothesis=funniest_3) BY user STATUS hypothesized SOURCE "t1:s11"
    RECORD ACTION select_option(target=funniest_3, value=D) STATUS attempted SOURCE "t1:s12" -> select_option_event_4 : EVENT
    LINK rejects(evidence=select_option_event_4, hypothesis=funniest_3) BY user STATUS hypothesized SOURCE "t1:s12"
    RECORD ACTION select_option(target=funniest_3, value=E) STATUS attempted SOURCE "t1:s13" -> select_option_event_5 : EVENT
    LINK rejects(evidence=select_option_event_5, hypothesis=funniest_3) BY user STATUS hypothesized SOURCE "t1:s13"
    RECORD ACTION select_option(target=funniest_3, value=F) STATUS attempted SOURCE "t1:s14" -> select_option_event_6 : EVENT
    LINK rejects(evidence=select_option_event_6, hypothesis=funniest_3) BY user STATUS hypothesized SOURCE "t1:s14"
    RECORD ACTION select_option(target=funniest_3, value=G) STATUS attempted SOURCE "t1:s15" -> select_option_event_7 : EVENT
    LINK rejects(evidence=select_option_event_7, hypothesis=funniest_3) BY user STATUS hypothesized SOURCE "t1:s15"
    RECORD ACTION select_option(target=funniest_3, value=H) STATUS attempted SOURCE "t1:s16" -> select_option_event_8 : EVENT
    LINK rejects(evidence=select_option_event_8, hypothesis=funniest_3) BY user STATUS hypothesized SOURCE "t1:s16"
    RECORD ACTION select_option(target=funniest_3, value=I) STATUS attempted SOURCE "t1:s17" -> select_option_event_9 : EVENT
    LINK rejects(evidence=select_option_event_9, hypothesis=funniest_3) BY user STATUS hypothesized SOURCE "t1:s17"
    RECORD ACTION select_option(target=funniest_3, value=J) STATUS attempted SOURCE "t1:s18" -> select_option_event_10 : EVENT
    LINK rejects(evidence=select_option_event_10, hypothesis=funniest_3) BY user STATUS hypothesized SOURCE "t1:s18"
  }
}```