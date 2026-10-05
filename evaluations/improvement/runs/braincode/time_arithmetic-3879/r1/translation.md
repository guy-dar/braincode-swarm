```braincode
MODE REQUEST
ENTRYPOINT Question1
TASK Question1 {
  CLAIM duration(amount=18, unit=unit_week) BY unspecified STATUS hypothesized SOURCE "task:duration" -> duration_2 : CLAIM
  CLAIM original_date(date="25-12-2021", timezone="UTC") BY unspecified STATUS asserted SOURCE "task:date" -> original_date_2 : CLAIM
  ACTION calculate_new_date(target=original_date_2, duration=duration_2) -> new_date : TERM
  CLAIM new_date BY unspecified STATUS observed SOURCE "task:date" -> new_date_2 : CLAIM
  CLAIM new_date_2 BY unspecified STATUS observed SOURCE "task:date" -> new_date_3 : CLAIM
  FORMAT new_date_3(format="mm/dd/yyyy") -> formatted_date : STRING
  RETURN formatted_date
}
TASK Question2 {
  ACTION let_x_equals_x_plus_26(target=duration_2, amount=26) -> x : TERM
  ACTION let_y_equals_x_plus_26(target=duration_2, amount=26) -> y : TERM
  ACTION let_z_equals_x_plus_26(target=duration_2, amount=26) -> z : TERM
  CLAIM duration(amount=18, unit=unit_week) BY unspecified STATUS hypothesized SOURCE "task:duration" -> duration_3 : CLAIM
  CLAIM x BY unspecified STATUS asserted SOURCE "task:x" -> x_2 : TERM
  CLAIM y BY unspecified STATUS asserted SOURCE "task:y" -> y_2 : TERM
  CLAIM z BY unspecified STATUS asserted SOURCE "task:z" -> z_2 : TERM
  ACTION let_p_equals_y_2() -> p : TERM
  ACTION let_p_equals_y_minus_9(target=y_2, amount=9) -> p_2 : TERM
  ACTION let_p_equals_y_minus_9(target=y, amount=9) -> p_3 : TERM
  ACTION let_p_equals_y_minus_9(target=y_2, amount=9) -> p_4 : TERM
  ACTION let_p_equals_y_minus_9(target=y, amount=9) -> p_5 : TERM
  ACTION let_p_equals_y_minus_9(target=y_2, amount=9) -> p_6 : TERM
  ACTION let_p_equals_y_minus_9(target=y, amount=9) -> p_7 : TERM
  ACTION let_y_equals_y_minus_9(target=y_2, amount=9) -> y_3 : TERM
  ACTION let_y_equals_y_minus_9(target=y, amount=9) -> y_4 : TERM
  ACTION let_y_equals_y_minus_9(target=y_2, amount=9) -> y_5 : TERM
  ACTION let_y_equals_y_minus_9(target=y, amount=9) -> y_6 : TERM
  ACTION let_y_equals_y_minus_9(target=y_2, amount=9) -> y_7 : TERM
  ACTION let_y_equals_y_minus_9(target=y, amount=9) -> y_8 : TERM
  ACTION let_y_equals_y_minus_9(target=y_2, amount=9) -> y_9 : TERM
  ACTION let_y_equals_y_minus_9(target=y, amount=9) -> y_10 : TERM
  ACTION let_p_equals_y_minus_9(target=p_2, amount=9) -> p_8 : TERM
  ACTION let_p_equals_y_minus_9(target=p_3, amount=9) -> p_9 : TERM
  ACTION let_p_equals_y_minus_9(target=p_4, amount=9) -> p_10 : TERM
  ACTION let_p_equals_y_minus_9(target=p_5, amount=9) -> p_11 : TERM
  ACTION let_p_equals_y_minus_9(target=p_6, amount=9) -> p_12 : TERM
  ACTION let_p_equals_y_minus_9(target=p_7, amount=9) -> p_13 : TERM
  ACTION let_p_equals_y_minus_9(target=p_8, amount=9) -> p_14 : TERM
  ACTION let_p_equals_y_minus_9(target=p_9, amount=9) -> p_15 : TERM
  ACTION let_p_equals_y_minus_9(target=p_10, amount=9) -> p_16 : TERM
  ACTION let_p_equals_y_minus_9(target=p_11, amount=9) -> p_17 : TERM
  ACTION let_p_equals_y_minus_9(target=p_12, amount=9) -> p_18 : TERM
  ACTION let_p_equals_y_minus_9(target=p_13, amount=9) -> p_19 : TERM
  ACTION let_p_equals_y_minus_9(target=p_14, amount=9) -> p_20 : TERM
  ACTION let_p_equals_y_minus_9(target=p_15, amount=9) -> p_21 : TERM
  ACTION let_p_equals_y_minus_9(target=p_16, amount=9) -> p_22 : TERM
  ACTION let_p_equals_y_minus_9(target=p_17, amount=9) -> p_23 : TERM
  ACTION let_p_equals_y_minus_9(target=p_18, amount=9) -> p_24 : TERM
  ACTION let_p_equals_y_minus_9(target=p_19, amount=9) -> p_25 : TERM
  ACTION let_p_equals_y_minus_9(target=p_20, amount=9) -> p_26 : TERM
  ACTION let_p_equals_y_minus_9(target=p_21, amount=9) -> p_27 : TERM
  ACTION let_p_equals_y_minus_9(target=p_22, amount=9) -> p_28 : TERM
  ACTION let_p_equals_y_minus_9(target=p_23, amount=9) -> p_29 : TERM
  ACTION let_p_equals_y_minus_9(target=p_24, amount=9) -> p_30 : TERM
  ACTION let_p_equals_y_minus_9(target=p_25, amount=9) -> p_31 : TERM
  ACTION let_p_equals_y_minus_9(target=p_26, amount=9) -> p_32 : TERM
  ACTION let_p_equals_y_minus_9(target=p_27, amount=9) -> p_33 : TERM
  ACTION let_p_equals_y_minus_9(target=p_28, amount=9) -> p_34 : TERM
  ACTION let_p_equals_y_minus_9(target=p_29, amount=9) -> p_35 : TERM
  ACTION let_p_equals_y_minus_9(target=p_30, amount=9) -> p_36 : TERM
  ACTION let_p_equals_y_minus_9(target=p_31, amount=9) -> p_37 : TERM
  ACTION let_p_equals_y_minus_9(target=p_32, amount=9) -> p_38 : TERM
  ACTION let_p_equals_y_minus_9(target=p_33, amount=9) -> p_39 : TERM
  ACTION let_p_equals_y_minus_9(target=p_34, amount=9) -> p_40 : TERM
  ACTION let_p_equals_y_minus_9(target=p_35, amount=9) -> p_41 : TERM
  ACTION let_p_equals_y_minus_9(target=p_36, amount=9) -> p_42 : TERM
  ACTION let_p_equals_y_minus_9(target=p_37, amount=9) -> p_43 : TERM
  ACTION let_p_equals_y_minus_9(target=p_38, amount=9) -> p_44 : TERM
  ACTION let_p_equals_y_minus_9(target=p_39, amount=9) -> p_45 : TERM
  ACTION let_p_equals_y_minus_9(target=p_40, amount=9) -> p_46 : TERM
  ACTION let_p_equals_y_minus_9(target=p_41, amount=9) -> p_47 : TERM
  ACTION let_p_equals_y_minus_9(target=p_42, amount=9) -> p_48 : TERM
  ACTION let_p_equals_y_minus_9(target=p_43, amount=9) -> p_49 : TERM
  ACTION let_p_equals_y_minus_9(target=p_44, amount=9) -> p_50 : TERM
  ACTION let_p_equals_y_minus_9(target=p_45, amount=9) -> p_51 : TERM
  ACTION let_p_equals_y_minus_9(target=p_46, amount=9) -> p_52 : TERM
  ACTION let_p_equals_y_minus_9(target=p_47, amount=9) -> p_53 : TERM
  ACTION let_p_equals_y_minus_9(target=p_48, amount=9) -> p_54 : TERM
  ACTION let_p_equals_y_minus_9(target=p_49, amount=9) -> p_55 : TERM
  ACTION let_p_equals_y_minus_9(target=p_50, amount=9) -> p_56 : TERM
  ACTION let_p_equals_y_minus_9(target=p_51, amount=9) -> p_57 : TERM
  ACTION let_p_equals_y_minus_9(target=p_52, amount=9) -> p_58 : TERM
  ACTION let_p_equals_y_minus_9(target=p_53, amount=9) -> p_59 : TERM
  ACTION let_p_equals_y_minus_9(target=p_54, amount=9) -> p_60 : TERM
  ACTION let_p_equals_y_minus_9(target=p_55, amount=9) -> p_61 : TERM
  ACTION let_p_equals_y_minus_9(target=p_56, amount=9) -> p_62 : TERM
  ACTION let_p_equals_y_minus_9(target=p_57, amount=9) -> p_63 : TERM
  ACTION let_p_equals_y_minus_9(target=p_58, amount=9) -> p_64 : TERM
  ACTION let_p_equals_y_minus_9(target=p_59, amount=9) -> p_65 : TERM
  ACTION let_p_equals_y_minus_9(target=p_60, amount=9) -> p_66 : TERM
  ACTION let_p_equals_y_minus_9(target=p_61, amount=9) -> p_67 : TERM
  ACTION let_p_equals_y_minus_9(target=p_62, amount=9) -> p_68 : TERM
  ACTION let_p_equals_y_minus_9(target=p_63, amount=9) -> p_69 : TERM
  ACTION let_p_equals_y_minus_9(target=p_64, amount=9) -> p_70 : TERM
  ACTION let_p_equals_y_minus_9(target=p_65, amount=9) -> p_71 : TERM
  ACTION let_p_equals_y_minus_9(target=p_66, amount=9) -> p_72 : TERM
  ACTION let_p_equals_y_minus_9(target=p_67, amount=9) -> p_73 : TERM
  ACTION let_p_equals_y_minus_9(target=p_68, amount=9) -> p_74 : TERM
  ACTION let_p_equals_y_minus_9(target=p_69, amount=9) -> p_75 : TERM
  ACTION let_p_equals_y_minus_9(target=p_70, amount=9) -> p_76 : TERM
  ACTION let_p_equals_y_minus_9(target=p_71, amount=9) -> p_77 : TERM
  ACTION let_p_equals_y_minus_9(target=p_72, amount=9) -> p_78 : TERM
  ACTION let_p_equals_y_minus_9(target=p_73, amount=9) -> p_79 : TERM
  ACTION let_p_equals_y_minus_9(target=p_74, amount=9) -> p_80 : TERM
  ACTION let_p_equals_y_minus_9(target=p_75, amount=9) -> p_81 : TERM
  ACTION let_p_equals_y_minus_9(target=p_76, amount=9) -> p_82 : TERM
  ACTION let_p_equals_y_minus_9(target=p_77, amount=9) -> p_83 : TERM
  ACTION let_p_equals_y_minus_9(target=p_78, amount=9) -> p_84 : TERM
  ACTION let_p_equals_y_minus_9(target=p_79, amount=9) -> p_85 : TERM
  ACTION let_p_equals_y_minus_9(target=p_80, amount=9) -> p_86 : TERM
  ACTION let_p_equals_y_minus_9(target=p_81, amount=9) -> p_87 : TERM
  ACTION let_p_equals_y_minus_9(target=p_82, amount=9) -> p_88 : TERM
  ACTION let_p_equals_y_minus_9(target=p_83, amount=9) -> p_89 : TERM
  ACTION let_p_equals_y_minus_9(target=p_84, amount=9) -> p_90 : TERM
  ACTION let_p_equals_y_minus_9(target=p_85, amount=9) -> p_91 : TERM
  ACTION let_p_equals_y_minus_9(target=p_86, amount=9) -> p_92 : TERM
  ACTION let_p_equals_y_minus_9(target=p_87, amount=9) -> p_93 : TERM
  ACTION let_p_equals_y_minus_9(target=p_88, amount=9) -> p_94 : TERM
  ACTION let_p_equals_y_minus_9(target=p_89, amount=9) -> p_95 : TERM
  ACTION let_p_equals_y_minus_9(target=p_90, amount=9) -> p_96 : TERM
  ACTION let_p_equals_y_minus_9(target=p_91, amount=9) -> p_97 : TERM
  ACTION let_p_equals_y_minus_9(target=p_92, amount=9) -> p_98 : TERM
  ACTION let_p_equals_y_minus_9(target=p_93, amount=9) -> p_99 : TERM
  ACTION let_p_equals_y_minus_9(target=p_94, amount=9) -> p_100 : TERM
  ACTION let_p_equals_y_minus_9(target=p_95, amount=9) -> p_101 : TERM
  ACTION let_p_equals_y_minus_9(target=p_96, amount=9) -> p_102 : TERM
  ACTION let_p_equals_y_minus_9(target=p_97, amount=9) -> p_103 : TERM
  ACTION let_p_equals_y_minus_9(target=p_98, amount=9) -> p_104 : TERM
  ACTION let_p_equals_y_minus_9(target=p_99, amount=9) -> p_105 : TERM
  ACTION let_p_equals_y_minus_9(target=p_100, amount=9) -> p_106 : TERM
  ACTION let_p_equals_y_minus_9(target=p_101, amount=9) -> p_107 : TERM
  ACTION let_p_equals_y_minus_9(target=p_102, amount=9) -> p_108 : TERM
  ACTION let_p_equals_y_minus_9(target=p_103, amount=9) -> p_109 : TERM
  ACTION let_p_equals_y_minus_9(target=p_104, amount=9) -> p_110 : TERM
  ACTION let_p_equals_y_minus_9(target=p_105, amount=9) -> p_111 : TERM
  ACTION let_p_equals_y_minus_9(target=p_106, amount=9) -> p_112 : TERM
  ACTION let_p_equals_y_minus_9(target=p_107, amount=9) -> p_113 : TERM
  ACTION let_p_equals_y_minus_9(target=p_108, amount=9) -> p_114 : TERM
  ACTION let_p_equals_y_minus_9(target=p_109, amount=9) -> p_115 : TERM
  ACTION let_p_equals_y_minus_9(target=p_110, amount=9) -> p_116 : TERM
  ACTION let_p_equals_y_minus_9(target=p_111, amount=9) -> p_117 : TERM
  ACTION let_p_equals_y_minus_9(target=p_112, amount=9) -> p_118 : TERM
  ACTION let_p_equals_y_minus_9(target=p_113, amount=9) -> p_119 : TERM
  ACTION let_p_equals_y_minus_9(target=p_114, amount=9) -> p_120 : TERM
  ACTION let_p_equals_y_minus_9(target=p_115, amount=9) -> p_121 : TERM
  ACTION let_p_equals_y_minus_9(target=p_116, amount=9) -> p_122 : TERM
  ACTION let_p_equals_y_minus_9(target=p_117, amount=9) -> p_123 : TERM
  ACTION let_p_equals_y_minus_9(target=p_118, amount=9) -> p_124 : TERM
  ACTION let_p_equals_y_minus_9(target=p_119, amount=9) -> p_125 : TERM
  ACTION let_p_equals_y_minus_9(target=p_120, amount=9) -> p_126 : TERM
  ACTION let_p_equals_y_minus_9(target=p_121, amount=9) -> p_127 : TERM
  ACTION let_p_equals_y_minus_9(target=p_122, amount=9) -> p_128 : TERM
  ACTION let_p_equals_y_minus_9(target=p_123, amount=9) -> p_129 : TERM
  ACTION let_p_equals_y_minus_9(target=p_124, amount=9) -> p_130 : TERM
  ACTION let_p_equals_y_minus_9(target=p_125, amount=9) -> p_131 : TERM
  ACTION let_p_equals_y_minus_9(target=p_126, amount=9) -> p_132 : TERM
  ACTION let_p_equals_y_minus_9(target=p_127, amount=9) -> p_133 : TERM
  ACTION let_p_equals_y_minus_9(target=p_128, amount=9) -> p_134 : TERM
  ACTION let_p_equals_y_minus_9(target=p_129, amount=9) -> p_135 : TERM
  ACTION let_p_equals_y_minus_9(target=p_130, amount=9) -> p_136 : TERM
  ACTION let_p_equals_y_minus_9(target=p_131, amount=9) -> p_137 : TERM
  ACTION let_p_equals_y_minus_9(target=p_132, amount=9) -> p_138 : TERM
  ACTION let_p_equals_y_minus_9(target=p_133, amount=9) -> p_139 : TERM
  ACTION let_p_equals_y_minus_9(target=p_134, amount=9) -> p_140 : TERM
  ACTION let_p_equals_y_minus_9(target=p_135, amount=9) -> p_141 : TERM
  ACTION let_p_equals_y_minus_9(target=p_136, amount=9) -> p_142 : TERM
  ACTION let_p_equals_y_minus_9(target=p_137, amount=9) -> p_143 : TERM
  ACTION let_p_equals_y_minus_9(target