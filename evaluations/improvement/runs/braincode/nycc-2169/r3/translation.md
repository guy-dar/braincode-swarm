```braincode
MODE REQUEST
ENTRYPOINT CaptionContest
TASK CaptionContest {
  ACTION pick_up(target=object_label::ear_of_corn, quantity=2, source=object_label::road) -> ear_of_corn_refs : LIST[REF[STRING]]
  ACTION place(target=ear_of_corn_refs[0], destination=object_label::road, relation=on) -> ear_of_corn_ref_1 : REF[STRING]
  ACTION place(target=ear_of_corn_refs[1], destination=object_label::road, relation=on) -> ear_of_corn_ref_2 : REF[STRING]
  ACTION walk(destination=object_label::road, relation=on) -> walk_event : EVENT
  ACTION generate(target=ear_of_corn_ref_1, quantity=1, source=ear_of_corn_ref_1, color=color_label::yellow, currency=currency::USD) -> popcorn_refs : LIST[REF[STRING]]
  ACTION generate(target=ear_of_corn_ref_2, quantity=1, source=ear_of_corn_ref_2, color=color_label::yellow, currency=currency::USD) -> popcorn_refs_2 : LIST[REF[STRING]]
  ACTION generate(target=popcorn_refs[0], destination=ear_of_corn_ref_1) -> popcorn_event : EVENT
  ACTION generate(target=popcorn_refs_2[0], destination=ear_of_corn_ref_2) -> popcorn_event_2 : EVENT
  ACTION chill(target=ear_of_corn_ref_1, destination=ear_of_corn_ref_1, duration=1) -> ear_of_corn_ref_1_chilled : REF[STRING]
  ACTION chill(target=ear_of_corn_ref_2, destination=ear_of_corn_ref_2, duration=1) -> ear_of_corn_ref_2_chilled : REF[STRING]
  ACTION turn(direction=left) -> turn_event : EVENT
  ACTION search_web(target="New Yorker Caption Contest", color=color_label::yellow, currency=currency::USD, genre=genre_label::comedy, location=country::US, ...other search attributes below) -> caption_refs : LIST[REF[STRING]]
  ACTION select_option(target=ear_of_corn_ref_1_chilled, value="A") -> caption_result : void
  ACTION select_option(target=ear_of_corn_ref_2_chilled, value="B") -> caption_result_2 : void
  ACTION select_option(target=ear_of_corn_ref_1_chilled, value="C") -> caption_result_3 : void
  ACTION select_option(target=ear_of_corn_ref_2_chilled, value="D") -> caption_result_4 : void
  ACTION select_option(target=ear_of_corn_ref_1_chilled, value="E") -> caption_result_5 : void
  ACTION select_option(target=ear_of_corn_ref_2_chilled, value="F") -> caption_result_6 : void
  ACTION select_option(target=ear_of_corn_ref_1_chilled, value="G") -> caption_result_7 : void
  ACTION select_option(target=ear_of_corn_ref_2_chilled, value="H") -> caption_result_8 : void
  ACTION select_option(target=ear_of_corn_ref_1_chilled, value="I") -> caption_result_9 : void
  ACTION select_option(target=ear_of_corn_ref_2_chilled, value="J") -> caption_result_10 : void
  ACTION select_option(target=ear_of_corn_ref_1_chilled, value="A") -> caption_result_11 : void
  ACTION select_option(target=ear_of_corn_ref_2_chilled, value="B") -> caption_result_12 : void
  ACTION select_option(target=ear_of_corn_ref_1_chilled, value="C") -> caption_result_13 : void
  ACTION select_option(target=ear_of_corn_ref_2_chilled, value="D") -> caption_result_14 : void
  ACTION select_option(target=ear_of_corn_ref_1_chilled, value="E") -> caption_result_15 : void
  ACTION select_option(target=ear_of_corn_ref_2_chilled, value="F") -> caption_result_16 : void
  ACTION select_option(target=ear_of_corn_ref_1_chilled, value="G") -> caption_result_17 : void
  ACTION select_option(target=ear_of_corn_ref_2_chilled, value="H") -> caption_result_18 : void
  ACTION select_option(target=ear_of_corn_ref_1_chilled, value="I") -> caption_result_19 : void
  ACTION select_option(target=ear_of_corn_ref_2_chilled, value="J") -> caption_result_20 : void
  ACTION select_option(target=ear_of_corn_ref_1_chilled, value="A") -> caption_result_21 : void
  ACTION select_option(target=ear_of_corn_ref_2_chilled, value="B") -> caption_result_22 : void
  ACTION select_option(target=ear_of_corn_ref_1_chilled, value="C") -> caption_result_23 : void
  ACTION select_option(target=ear_of_corn_ref_2_chilled, value="D") -> caption_result_24 : void
  ACTION select_option(target=ear_of_corn_ref_1_chilled, value="E") -> caption_result_25 : void
  ACTION select_option(target=ear_of_corn_ref_2_chilled, value="F") -> caption_result_26 : void
  ACTION select_option(target=ear_of_corn_ref_1_chilled, value="G") -> caption_result_27 : void
  ACTION select_option(target=ear_of_corn_ref_2_chilled, value="H") -> caption_result_28 : void
  ACTION select_option(target=ear_of_corn_ref_1_chilled, value="I") -> caption_result_29 : void
  ACTION select_option(target=ear_of_corn_ref_2_chilled, value="J") -> caption_result_30 : void
  ACTION select_option(target=ear_of_corn_ref_1_chilled, value="A") -> caption_result_31 : void
  ACTION select_option(target=ear_of_corn_ref_2_chilled, value="B") -> caption_result_32 : void
  ACTION select_option(target=ear_of_corn_ref_1_chilled, value="C") -> caption_result_33 : void
  ACTION select_option(target=ear_of_corn_ref_2_chilled, value="D") -> caption_result_34 : void
  ACTION select_option(target=ear_of_corn_ref_1_chilled, value="E") -> caption_result_35 : void
  ACTION select_option(target=ear_of_corn_ref_2_chilled, value="F") -> caption_result_36 : void
  ACTION select_option(target=ear_of_corn_ref_1_chilled, value="G") -> caption_result_37 : void
  ACTION select_option(target=ear_of_corn_ref_2_chilled, value="H") -> caption_result_38 : void
  ACTION select_option(target=ear_of_corn_ref_1_chilled, value="I") -> caption_result_39 : void
  ACTION select_option(target=ear_of_corn_ref_2_chilled, value="J") -> caption_result_40 : void
  ACTION select_option(target=ear_of_corn_ref_1_chilled, value="A") -> caption_result_41 : void
  ACTION select_option(target=ear_of_corn_ref_2_chilled, value="B") -> caption_result_42 : void
  ACTION select_option(target=ear_of_corn_ref_1_chilled, value="C") -> caption_result_43 : void
  ACTION select_option(target=ear_of_corn_ref_2_chilled, value="D") -> caption_result_44 : void
  ACTION select_option(target=ear_of_corn_ref_1_chilled, value="E") -> caption_result_45 : void
  ACTION select_option(target=ear_of_corn_ref_2_chilled, value="F") -> caption_result_46 : void
  ACTION select_option(target=ear_of_corn_ref_1_chilled, value="G") -> caption_result_47 : void
  ACTION select_option(target=ear_of_corn_ref_2_chilled, value="H") -> caption_result_48 : void
  ACTION select_option(target=ear_of_corn_ref_1_chilled, value="I") -> caption_result_49 : void
  ACTION select_option(target=ear_of_corn_ref_2_chilled, value="J") -> caption_result_50 : void
  ACTION select_option(target=ear_of_corn_ref_1_chilled, value="A") -> caption_result_51 : void
  ACTION select_option(target=ear_of_corn_ref_2_chilled, value="B") -> caption_result_52 : void
  ACTION select_option(target=ear_of_corn_ref_1_chilled, value="C") -> caption_result_53 : void
  ACTION select_option(target=ear_of_corn_ref_2_chilled, value="D") -> caption_result_54 : void
  ACTION select_option(target=ear_of_corn_ref_1_chilled, value="E") -> caption_result_55 : void
  ACTION select_option(target=ear_of_corn_ref_2_chilled, value="F") -> caption_result_56 : void
  ACTION select_option(target=ear_of_corn_ref_1_chilled, value="G") -> caption_result_57 : void
  ACTION select_option(target=ear_of_corn_ref_2_chilled, value="H") -> caption_result_58 : void
  ACTION select_option(target=ear_of_corn_ref_1_chilled, value="I") -> caption_result_59 : void
  ACTION select_option(target=ear_of_corn_ref_2_chilled, value="J") -> caption_result_60 : void
}