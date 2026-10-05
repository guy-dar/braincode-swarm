```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  ACTION search_web(query="svg path visualization") -> result : LIST[REF[STRING]]
  ACTION pick_up(target=result[0]) -> path_ref : REF[STRING]
  ACTION look(direction="straight") -> void
  ACTION search_web(query="shape geometry") -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_2 : TERM
  ACTION look(direction="straight") -> void
  ACTION search_web(query="shape geometry") -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_3 : TERM
  ACTION look(direction="straight") -> void
  ACTION search_web(query="shape geometry") -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_4 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_4, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_5 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_5, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_6 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_6, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_7 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_7, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_8 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_8, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_9 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_9, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_10 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_10, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_11 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_11, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_12 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_12, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_13 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_13, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_14 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_14, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_15 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_15, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_16 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_16, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_17 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_17, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_18 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_18, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_19 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_19, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_20 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_20, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_21 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_21, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_22 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_22, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_23 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_23, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_24 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_24, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_25 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_25, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_26 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_26, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_27 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_27, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_28 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_28, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_29 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_29, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_30 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_30, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_31 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_31, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_32 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_32, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_33 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_33, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_34 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_34, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_35 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_35, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_36 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_36, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_37 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_37, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_38 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_38, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_39 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_39, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_40 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_40, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_41 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_41, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_42 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_42, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_43 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_43, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_44 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_44, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_45 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_45, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_46 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_46, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_47 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_47, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_48 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_48, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_49 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_49, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_50 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_50, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_51 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_51, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_52 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_52, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_53 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_53, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_54 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_54, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_55 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_55, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_56 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_56, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_57 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_57, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_58 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_58, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_59 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_59, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_60 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_60, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_61 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_61, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_62 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_62, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_63 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_63, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_64 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_64, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_65 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_65, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_66 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_66, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_67 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_67, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_68 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_68, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_69 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_69, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_70 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_70, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_71 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_71, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_72 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_72, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_73 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_73, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_74 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_74, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_75 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_75, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_76 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_76, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_77 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_77, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_78 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_78, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_79 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_79, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_80 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_80, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_81 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_81, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_82 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_82, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_83 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_83, limit=10) -> result : LIST[TERM]
  ACTION pick_up(target=result[0]) -> shape_term_84 : TERM
  ACTION look(direction="straight") -> void
  ACTION extract(target=shape_term_84, limit=10) -> result : LIST[TERM]
  ACTION