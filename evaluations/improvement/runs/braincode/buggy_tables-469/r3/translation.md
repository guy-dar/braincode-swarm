```braincode
MODE REQUEST
ENTRYPOINT Conversation
CONVO Conversation {
  TURN t1 SPEAKER=USER {
    ACTION pick_up(target=table) -> table_ref : REF[STRING]
    ACTION rinse(target=table_ref, destination=csv_file) -> csv_ref : REF[STRING]
    ACTION place(target=csv_ref, destination=markdown_table) -> markdown_table_ref : REF[STRING]
    UTTER ask(target=markdown_table_ref)
  }
  TURN t2 SPEAKER=USER REPLY_TO t1 AMENDS [t1.table_ref] {
    ACTION transform_preserve_first_column(target=markdown_table_ref) -> transformed_table_ref : REF[STRING]
    LINK revises(previous=t1.table_ref, replacement=transformed_table_ref)
  }
  TURN t3 SPEAKER=USER {
    ACTION extract(target=t2.transformed_table_ref, limit=1) -> extracted_table : LIST[REF[STRING]]
    UTTER ask(target=extracted_table)
  }
  TURN t4 SPEAKER=USER {
    ACTION wait(duration=2) -> wait_result : void
    ACTION extract(target=t3.extracted_table, limit=1) -> extracted_table_2 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_2)
  }
  TURN t5 SPEAKER=USER {
    ACTION pick_up(target=extracted_table_2) -> table_ref_2 : REF[STRING]
    UTTER ask(target=table_ref_2)
  }
  TURN t6 SPEAKER=USER {
    ACTION sort(target=t5.table_ref_2, rank_direction="asc", rank_field="music_listening_minutes") -> sorted_table : LIST[REF[STRING]]
    UTTER ask(target=sorted_table)
  }
  TURN t7 SPEAKER=USER {
    ACTION extract(target=t6.sorted_table, limit=1) -> extracted_table_3 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_3)
  }
  TURN t8 SPEAKER=USER {
    ACTION pick_up(target=t7.extracted_table_3) -> table_ref_3 : REF[STRING]
    ACTION extract(target=table_ref_3, limit=1) -> extracted_table_4 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_4)
  }
  TURN t9 SPEAKER=USER {
    ACTION wait(duration=2) -> wait_result_2 : void
    ACTION extract(target=t8.extracted_table_4, limit=1) -> extracted_table_5 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_5)
  }
  TURN t10 SPEAKER=USER {
    ACTION sort(target=t9.extracted_table_5, rank_direction="asc", rank_field="study_minutes") -> sorted_table_2 : LIST[REF[STRING]]
    UTTER ask(target=sorted_table_2)
  }
  TURN t11 SPEAKER=USER {
    ACTION extract(target=t10.sorted_table_2, limit=1) -> extracted_table_6 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_6)
  }
  TURN t12 SPEAKER=USER {
    ACTION pick_up(target=t11.extracted_table_6) -> table_ref_4 : REF[STRING]
    ACTION extract(target=table_ref_4, limit=1) -> extracted_table_7 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_7)
  }
  TURN t13 SPEAKER=USER {
    ACTION wait(duration=2) -> wait_result_3 : void
    ACTION extract(target=t12.extracted_table_7, limit=1) -> extracted_table_8 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_8)
  }
  TURN t14 SPEAKER=USER {
    ACTION pick_up(target=t13.extracted_table_8) -> table_ref_5 : REF[STRING]
    ACTION extract(target=table_ref_5, limit=1) -> extracted_table_9 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_9)
  }
  TURN t15 SPEAKER=USER {
    ACTION sort(target=t14.extracted_table_9, rank_direction="asc", rank_field="music_listening_minutes") -> sorted_table_3 : LIST[REF[STRING]]
    UTTER ask(target=sorted_table_3)
  }
  TURN t16 SPEAKER=USER {
    ACTION extract(target=t15.sorted_table_3, limit=1) -> extracted_table_10 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_10)
  }
  TURN t17 SPEAKER=USER {
    ACTION pick_up(target=t16.extracted_table_10) -> table_ref_6 : REF[STRING]
    ACTION extract(target=table_ref_6, limit=1) -> extracted_table_11 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_11)
  }
  TURN t18 SPEAKER=USER {
    ACTION wait(duration=2) -> wait_result_4 : void
    ACTION extract(target=t17.extracted_table_11, limit=1) -> extracted_table_12 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_12)
  }
  TURN t19 SPEAKER=USER {
    ACTION sort(target=t18.extracted_table_12, rank_direction="asc", rank_field="study_minutes") -> sorted_table_4 : LIST[REF[STRING]]
    UTTER ask(target=sorted_table_4)
  }
  TURN t20 SPEAKER=USER {
    ACTION extract(target=t19.sorted_table_4, limit=1) -> extracted_table_13 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_13)
  }
  TURN t21 SPEAKER=USER {
    ACTION pick_up(target=t20.extracted_table_13) -> table_ref_7 : REF[STRING]
    ACTION extract(target=table_ref_7, limit=1) -> extracted_table_14 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_14)
  }
  TURN t22 SPEAKER=USER {
    ACTION sort(target=t21.extracted_table_14, rank_direction="asc", rank_field="music_listening_minutes") -> sorted_table_5 : LIST[REF[STRING]]
    UTTER ask(target=sorted_table_5)
  }
  TURN t23 SPEAKER=USER {
    ACTION extract(target=t22.sorted_table_5, limit=1) -> extracted_table_15 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_15)
  }
  TURN t24 SPEAKER=USER {
    ACTION pick_up(target=t23.extracted_table_15) -> table_ref_8 : REF[STRING]
    ACTION extract(target=table_ref_8, limit=1) -> extracted_table_16 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_16)
  }
  TURN t25 SPEAKER=USER {
    ACTION wait(duration=2) -> wait_result_5 : void
    ACTION extract(target=t24.extracted_table_16, limit=1) -> extracted_table_17 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_17)
  }
  TURN t26 SPEAKER=USER {
    ACTION sort(target=t25.extracted_table_17, rank_direction="asc", rank_field="study_minutes") -> sorted_table_6 : LIST[REF[STRING]]
    UTTER ask(target=sorted_table_6)
  }
  TURN t27 SPEAKER=USER {
    ACTION extract(target=t26.sorted_table_6, limit=1) -> extracted_table_18 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_18)
  }
  TURN t28 SPEAKER=USER {
    ACTION pick_up(target=t27.extracted_table_18) -> table_ref_9 : REF[STRING]
    ACTION extract(target=table_ref_9, limit=1) -> extracted_table_19 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_19)
  }
  TURN t29 SPEAKER=USER {
    ACTION sort(target=t28.extracted_table_19, rank_direction="asc", rank_field="music_listening_minutes") -> sorted_table_7 : LIST[REF[STRING]]
    UTTER ask(target=sorted_table_7)
  }
  TURN t30 SPEAKER=USER {
    ACTION extract(target=t29.sorted_table_7, limit=1) -> extracted_table_20 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_20)
  }
  TURN t31 SPEAKER=USER {
    ACTION pick_up(target=t30.extracted_table_20) -> table_ref_10 : REF[STRING]
    ACTION extract(target=table_ref_10, limit=1) -> extracted_table_21 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_21)
  }
  TURN t32 SPEAKER=USER {
    ACTION wait(duration=2) -> wait_result_6 : void
    ACTION extract(target=t31.extracted_table_21, limit=1) -> extracted_table_22 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_22)
  }
  TURN t33 SPEAKER=USER {
    ACTION sort(target=t32.extracted_table_22, rank_direction="asc", rank_field="study_minutes") -> sorted_table_8 : LIST[REF[STRING]]
    UTTER ask(target=sorted_table_8)
  }
  TURN t34 SPEAKER=USER {
    ACTION extract(target=t33.sorted_table_8, limit=1) -> extracted_table_23 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_23)
  }
  TURN t35 SPEAKER=USER {
    ACTION pick_up(target=t34.extracted_table_23) -> table_ref_11 : REF[STRING]
    ACTION extract(target=table_ref_11, limit=1) -> extracted_table_24 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_24)
  }
  TURN t36 SPEAKER=USER {
    ACTION sort(target=t35.extracted_table_24, rank_direction="asc", rank_field="music_listening_minutes") -> sorted_table_9 : LIST[REF[STRING]]
    UTTER ask(target=sorted_table_9)
  }
  TURN t37 SPEAKER=USER {
    ACTION extract(target=t36.sorted_table_9, limit=1) -> extracted_table_25 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_25)
  }
  TURN t38 SPEAKER=USER {
    ACTION pick_up(target=t37.extracted_table_25) -> table_ref_12 : REF[STRING]
    ACTION extract(target=table_ref_12, limit=1) -> extracted_table_26 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_26)
  }
  TURN t39 SPEAKER=USER {
    ACTION wait(duration=2) -> wait_result_7 : void
    ACTION extract(target=t38.extracted_table_26, limit=1) -> extracted_table_27 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_27)
  }
  TURN t40 SPEAKER=USER {
    ACTION sort(target=t39.extracted_table_27, rank_direction="asc", rank_field="study_minutes") -> sorted_table_10 : LIST[REF[STRING]]
    UTTER ask(target=sorted_table_10)
  }
  TURN t41 SPEAKER=USER {
    ACTION extract(target=t40.sorted_table_10, limit=1) -> extracted_table_28 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_28)
  }
  TURN t42 SPEAKER=USER {
    ACTION pick_up(target=t41.extracted_table_28) -> table_ref_13 : REF[STRING]
    ACTION extract(target=table_ref_13, limit=1) -> extracted_table_29 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_29)
  }
  TURN t43 SPEAKER=USER {
    ACTION sort(target=t42.extracted_table_29, rank_direction="asc", rank_field="music_listening_minutes") -> sorted_table_11 : LIST[REF[STRING]]
    UTTER ask(target=sorted_table_11)
  }
  TURN t44 SPEAKER=USER {
    ACTION extract(target=t43.sorted_table_11, limit=1) -> extracted_table_30 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_30)
  }
  TURN t45 SPEAKER=USER {
    ACTION pick_up(target=t44.extracted_table_30) -> table_ref_14 : REF[STRING]
    ACTION extract(target=table_ref_14, limit=1) -> extracted_table_31 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_31)
  }
  TURN t46 SPEAKER=USER {
    ACTION wait(duration=2) -> wait_result_8 : void
    ACTION extract(target=t45.extracted_table_31, limit=1) -> extracted_table_32 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_32)
  }
  TURN t47 SPEAKER=USER {
    ACTION sort(target=t46.extracted_table_32, rank_direction="asc", rank_field="study_minutes") -> sorted_table_12 : LIST[REF[STRING]]
    UTTER ask(target=sorted_table_12)
  }
  TURN t48 SPEAKER=USER {
    ACTION extract(target=t47.sorted_table_12, limit=1) -> extracted_table_33 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_33)
  }
  TURN t49 SPEAKER=USER {
    ACTION pick_up(target=t48.extracted_table_33) -> table_ref_15 : REF[STRING]
    ACTION extract(target=table_ref_15, limit=1) -> extracted_table_34 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_34)
  }
  TURN t50 SPEAKER=USER {
    ACTION sort(target=t49.extracted_table_34, rank_direction="asc", rank_field="music_listening_minutes") -> sorted_table_13 : LIST[REF[STRING]]
    UTTER ask(target=sorted_table_13)
  }
  TURN t51 SPEAKER=USER {
    ACTION extract(target=t50.sorted_table_13, limit=1) -> extracted_table_35 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_35)
  }
  TURN t52 SPEAKER=USER {
    ACTION pick_up(target=t51.extracted_table_35) -> table_ref_16 : REF[STRING]
    ACTION extract(target=table_ref_16, limit=1) -> extracted_table_36 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_36)
  }
  TURN t53 SPEAKER=USER {
    ACTION wait(duration=2) -> wait_result_9 : void
    ACTION extract(target=t52.extracted_table_36, limit=1) -> extracted_table_37 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_37)
  }
  TURN t54 SPEAKER=USER {
    ACTION sort(target=t53.extracted_table_37, rank_direction="asc", rank_field="study_minutes") -> sorted_table_14 : LIST[REF[STRING]]
    UTTER ask(target=sorted_table_14)
  }
  TURN t55 SPEAKER=USER {
    ACTION extract(target=t54.sorted_table_14, limit=1) -> extracted_table_38 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_38)
  }
  TURN t56 SPEAKER=USER {
    ACTION pick_up(target=t55.extracted_table_38) -> table_ref_17 : REF[STRING]
    ACTION extract(target=table_ref_17, limit=1) -> extracted_table_39 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_39)
  }
  TURN t57 SPEAKER=USER {
    ACTION sort(target=t56.extracted_table_39, rank_direction="asc", rank_field="music_listening_minutes") -> sorted_table_15 : LIST[REF[STRING]]
    UTTER ask(target=sorted_table_15)
  }
  TURN t58 SPEAKER=USER {
    ACTION extract(target=t57.sorted_table_15, limit=1) -> extracted_table_40 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_40)
  }
  TURN t59 SPEAKER=USER {
    ACTION pick_up(target=t58.extracted_table_40) -> table_ref_18 : REF[STRING]
    ACTION extract(target=table_ref_18, limit=1) -> extracted_table_41 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_41)
  }
  TURN t60 SPEAKER=USER {
    ACTION wait(duration=2) -> wait_result_10 : void
    ACTION extract(target=t59.extracted_table_41, limit=1) -> extracted_table_42 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_42)
  }
  TURN t61 SPEAKER=USER {
    ACTION sort(target=t60.extracted_table_42, rank_direction="asc", rank_field="study_minutes") -> sorted_table_16 : LIST[REF[STRING]]
    UTTER ask(target=sorted_table_16)
  }
  TURN t62 SPEAKER=USER {
    ACTION extract(target=t61.sorted_table_16, limit=1) -> extracted_table_43 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_43)
  }
  TURN t63 SPEAKER=USER {
    ACTION pick_up(target=t62.extracted_table_43) -> table_ref_19 : REF[STRING]
    ACTION extract(target=table_ref_19, limit=1) -> extracted_table_44 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_44)
  }
  TURN t64 SPEAKER=USER {
    ACTION sort(target=t63.extracted_table_44, rank_direction="asc", rank_field="music_listening_minutes") -> sorted_table_17 : LIST[REF[STRING]]
    UTTER ask(target=sorted_table_17)
  }
  TURN t65 SPEAKER=USER {
    ACTION extract(target=t64.sorted_table_17, limit=1) -> extracted_table_45 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_45)
  }
  TURN t66 SPEAKER=USER {
    ACTION pick_up(target=t65.extracted_table_45) -> table_ref_20 : REF[STRING]
    ACTION extract(target=table_ref_20, limit=1) -> extracted_table_46 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_46)
  }
  TURN t67 SPEAKER=USER {
    ACTION wait(duration=2) -> wait_result_11 : void
    ACTION extract(target=t66.extracted_table_46, limit=1) -> extracted_table_47 : LIST[REF[STRING]]
    UTTER ask(target=extracted_table_47)
 