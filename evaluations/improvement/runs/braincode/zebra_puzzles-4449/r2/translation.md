```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    ACTION generate(target=person_profile) -> person_profile : TERM
    ACTION place(target=person_profile, destination=table) -> table : TERM
    ACTION record(event=person_profile, status=solved) -> event : EVENT
    ACTION record(event=event, status=question) -> question : EVENT
    ACTION record(event=event, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY USER STATUS asserted SOURCE "t1:s1" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s1" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s2" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s2" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s3" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s3" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s4" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s4" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s5" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s5" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s6" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s6" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s7" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s7" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s8" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s8" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s9" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s9" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s10" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s10" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s11" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s11" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s12" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s12" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s13" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s13" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s14" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s14" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s15" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s15" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s16" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s16" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s17" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s17" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s18" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s18" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s19" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s19" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s20" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s20" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s21" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s21" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s22" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s22" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s23" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s23" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s24" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s24" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s25" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s25" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s26" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s26" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s27" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s27" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s28" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s28" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s29" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s29" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s30" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s30" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s31" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s31" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s32" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s32" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s33" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s33" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s34" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s34" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s35" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s35" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s36" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s36" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s37" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s37" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s38" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s38" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s39" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s39" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s40" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s40" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s41" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s41" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s42" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s42" -> claim : CLAIM
    ACTION record(event=claim, status=correct) -> correct : EVENT
    ACTION record(event=correct, status=question) -> question : EVENT
    ACTION record(event=question, status=answer) -> answer : EVENT
    ACTION claim(answer=answer, status=correct) BY user STATUS asserted SOURCE "t1:s43" -> claim : CLAIM
    CLAIM claim BY user STATUS asserted SOURCE "t1:s43" -> claim : CLAIM
