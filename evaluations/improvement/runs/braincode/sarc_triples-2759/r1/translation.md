```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    ACTION determine_sarcasm(target=POST_1, reply=REPLY_1) -> result_1 : NUMBER
    ACTION determine_sarcasm(target=POST_2, reply=REPLY_2) -> result_2 : NUMBER
    ACTION determine_sarcasm(target=POST_3, reply=REPLY_3) -> result_3 : NUMBER
    CLAIM result_1 BY USER STATUS asserted SOURCE "t1:s1" -> result_1_claim : CLAIM
    CLAIM result_2 BY USER STATUS asserted SOURCE "t1:s2" -> result_2_claim : CLAIM
    CLAIM result_3 BY USER STATUS asserted SOURCE "t1:s3" -> result_3_claim : CLAIM
    LINK supports(conclusion=result_3_claim, premise=result_2_claim) SOURCE "t1:s3"
    CLAIM result_3 BY USER STATUS asserted SOURCE "t1:s3" -> result_3_claim_2 : CLAIM
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_3 : CLAIM
    LINK supports(conclusion=result_3_claim_3, premise=result_1_claim) SOURCE "t1:s3"
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_4 : CLAIM
    LINK supports(conclusion=result_3_claim_4, premise=result_2_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_2 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_5 : CLAIM
    LINK supports(conclusion=result_3_claim_5, premise=result_1_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_3 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_6 : CLAIM
    LINK supports(conclusion=result_3_claim_6, premise=result_2_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_4 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_7 : CLAIM
    LINK supports(conclusion=result_3_claim_7, premise=result_1_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_5 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_8 : CLAIM
    LINK supports(conclusion=result_3_claim_8, premise=result_2_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_6 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_9 : CLAIM
    LINK supports(conclusion=result_3_claim_9, premise=result_1_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_7 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_10 : CLAIM
    LINK supports(conclusion=result_3_claim_10, premise=result_2_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_8 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_11 : CLAIM
    LINK supports(conclusion=result_3_claim_11, premise=result_1_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_9 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_12 : CLAIM
    LINK supports(conclusion=result_3_claim_12, premise=result_2_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_10 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_13 : CLAIM
    LINK supports(conclusion=result_3_claim_13, premise=result_1_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_11 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_14 : CLAIM
    LINK supports(conclusion=result_3_claim_14, premise=result_2_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_12 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_15 : CLAIM
    LINK supports(conclusion=result_3_claim_15, premise=result_1_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_13 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_16 : CLAIM
    LINK supports(conclusion=result_3_claim_16, premise=result_2_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_14 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_17 : CLAIM
    LINK supports(conclusion=result_3_claim_17, premise=result_1_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_15 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_18 : CLAIM
    LINK supports(conclusion=result_3_claim_18, premise=result_2_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_16 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_19 : CLAIM
    LINK supports(conclusion=result_3_claim_19, premise=result_1_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_17 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_20 : CLAIM
    LINK supports(conclusion=result_3_claim_20, premise=result_2_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_18 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_21 : CLAIM
    LINK supports(conclusion=result_3_claim_21, premise=result_1_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_19 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_22 : CLAIM
    LINK supports(conclusion=result_3_claim_22, premise=result_2_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_20 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_23 : CLAIM
    LINK supports(conclusion=result_3_claim_23, premise=result_1_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_21 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_24 : CLAIM
    LINK supports(conclusion=result_3_claim_24, premise=result_2_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_22 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_25 : CLAIM
    LINK supports(conclusion=result_3_claim_25, premise=result_1_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_23 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_26 : CLAIM
    LINK supports(conclusion=result_3_claim_26, premise=result_2_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_24 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_27 : CLAIM
    LINK supports(conclusion=result_3_claim_27, premise=result_1_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_25 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_28 : CLAIM
    LINK supports(conclusion=result_3_claim_28, premise=result_2_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_26 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_29 : CLAIM
    LINK supports(conclusion=result_3_claim_29, premise=result_1_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_27 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_30 : CLAIM
    LINK supports(conclusion=result_3_claim_30, premise=result_2_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_28 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_31 : CLAIM
    LINK supports(conclusion=result_3_claim_31, premise=result_1_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_29 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_32 : CLAIM
    LINK supports(conclusion=result_3_claim_32, premise=result_2_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_30 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_33 : CLAIM
    LINK supports(conclusion=result_3_claim_33, premise=result_1_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_31 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_34 : CLAIM
    LINK supports(conclusion=result_3_claim_34, premise=result_2_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_32 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_35 : CLAIM
    LINK supports(conclusion=result_3_claim_35, premise=result_1_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_33 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_36 : CLAIM
    LINK supports(conclusion=result_3_claim_36, premise=result_2_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_34 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_37 : CLAIM
    LINK supports(conclusion=result_3_claim_37, premise=result_1_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_35 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_38 : CLAIM
    LINK supports(conclusion=result_3_claim_38, premise=result_2_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_36 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_39 : CLAIM
    LINK supports(conclusion=result_3_claim_39, premise=result_1_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_37 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_40 : CLAIM
    LINK supports(conclusion=result_3_claim_40, premise=result_2_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_38 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_41 : CLAIM
    LINK supports(conclusion=result_3_claim_41, premise=result_1_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_39 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_42 : CLAIM
    LINK supports(conclusion=result_3_claim_42, premise=result_2_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_40 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_43 : CLAIM
    LINK supports(conclusion=result_3_claim_43, premise=result_1_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_41 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_44 : CLAIM
    LINK supports(conclusion=result_3_claim_44, premise=result_2_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_42 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_45 : CLAIM
    LINK supports(conclusion=result_3_claim_45, premise=result_1_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_43 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_46 : CLAIM
    LINK supports(conclusion=result_3_claim_46, premise=result_2_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_44 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_47 : CLAIM
    LINK supports(conclusion=result_3_claim_47, premise=result_1_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_45 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_48 : CLAIM
    LINK supports(conclusion=result_3_claim_48, premise=result_2_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_46 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_49 : CLAIM
    LINK supports(conclusion=result_3_claim_49, premise=result_1_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_47 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_50 : CLAIM
    LINK supports(conclusion=result_3_claim_50, premise=result_2_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_48 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_51 : CLAIM
    LINK supports(conclusion=result_3_claim_51, premise=result_1_claim) SOURCE "t1:s3"
    RECORD ACTION determine_sarcasm() STATUS succeeded SOURCE "t1:s3" -> result_3_event_49 : EVENT
    CLAIM result_3 BY USER STATUS observed SOURCE "t1:s3" -> result_3_claim_52 : CLAIM
    LINK supports(conclusion=result_3_claim_52, premise=result_2_claim) SOURCE "t1:s3"
    RECORD