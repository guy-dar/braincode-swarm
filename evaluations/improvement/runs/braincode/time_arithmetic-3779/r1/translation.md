```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  TERM duration(amount=21, unit=unit_minute) -> duration_2 : TERM
  TERM duration(amount=2, unit=unit_second) -> duration_3 : TERM
  TERM duration(amount=24, unit=unit_minute) -> duration_4 : TERM
  TERM duration(amount=24, unit=unit_second) -> duration_5 : TERM
  TERM duration(amount=2, unit=unit_hour) -> duration_6 : TERM
  TERM duration(amount=5, unit=unit_minute) -> duration_7 : TERM
  TERM duration(amount=10, unit=unit_second) -> duration_8 : TERM
  TERM at_least(measure=duration_2) -> at_least_2 : TERM
  TERM at_most(measure=duration_4) -> at_most_4 : TERM
  TERM calculation(inputs=[duration_2, duration_4], operation="ratio", result?: TERM) -> calculation_2 : TERM
  TERM measure(amount=duration_5, unit=unit_second) -> measure_5 : TERM
  TERM measure(amount=duration_8, unit=unit_second) -> measure_8 : TERM
  TERM rate(denominator=duration_2, numerator=duration_4) -> rate_4 : TERM
  TERM requirement(property="answer", value=duration_6) -> requirement_6 : TERM
  TERM subject(kind="magic_tricks", qualifier=duration_2, location=Hannah, time=duration_3) -> subject_3 : TERM
  TERM test_condition(condition="magic_tricks", expected=TRUE) -> test_condition_1 : TERM
  TERM time_point(date=yyyy-mm-dd, time=hh:mm:ss, timezone=timezone) -> time_point_1 : TERM
  TERM unit_hour(unit=unit_hour) -> unit_hour_1 : TERM
  TERM unit_minute(unit=unit_minute) -> unit_minute_1 : TERM
  TERM unit_second(unit=unit_second) -> unit_second_1 : TERM
  TERM unit_day(unit=unit_day) -> unit_day_1 : TERM
  TERM unit_week(unit=unit_week) -> unit_week_1 : TERM
  TERM unit_month(unit=unit_month) -> unit_month_1 : TERM
  TERM unit_year(unit=unit_year) -> unit_year_1 : TERM
  TERM unit_sentence(unit=unit_sentence) -> unit_sentence_1 : TERM
  TERM unit_character(unit=unit_character) -> unit_character_1 : TERM
  TERM unit_kilometer(unit=unit_kilometer) -> unit_kilometer_1 : TERM
  TERM unit_hour(unit=unit_hour) -> unit_hour_2 : TERM
  TERM unit_minute(unit=unit_minute) -> unit_minute_2 : TERM
  TERM unit_second(unit=unit_second) -> unit_second_2 : TERM
  TERM unit_hour(unit=unit_hour) -> unit_hour_3 : TERM
  TERM unit_minute(unit=unit_minute) -> unit_minute_3 : TERM
  TERM unit_second(unit=unit_second) -> unit_second_3 : TERM
  TERM unit_day(unit=unit_day) -> unit_day_2 : TERM
  TERM unit_week(unit=unit_week) -> unit_week_2 : TERM
  TERM unit_month(unit=unit_month) -> unit_month_2 : TERM
  TERM unit_year(unit=unit_year) -> unit_year_2 : TERM
  TERM unit_sentence(unit=unit_sentence) -> unit_sentence_2 : TERM
  TERM unit_character(unit=unit_character) -> unit_character_2 : TERM
  TERM unit_kilometer(unit=unit_kilometer) -> unit_kilometer_2 : TERM
  TERM duration(amount=duration_5, unit=unit_second) -> duration_9 : TERM
  TERM duration(amount=duration_8, unit=unit_second) -> duration_10 : TERM
  TERM duration(amount=duration_6, unit=unit_hour) -> duration_11 : TERM
  TERM duration(amount=duration_7, unit=unit_minute) -> duration_12 : TERM
  TERM duration(amount=duration_8, unit=unit_second) -> duration_13 : TERM
  TERM duration(amount=duration_9, unit=unit_second) -> duration_14 : TERM
  TERM duration(amount=duration_10, unit=unit_second) -> duration_15 : TERM
  TERM duration(amount=duration_11, unit=unit_hour) -> duration_16 : TERM
  TERM duration(amount=duration_12, unit=unit_minute) -> duration_17 : TERM
  TERM duration(amount=duration_13, unit=unit_second) -> duration_18 : TERM
  TERM duration(amount=duration_14, unit=unit_second) -> duration_19 : TERM
  TERM duration(amount=duration_15, unit=unit_second) -> duration_20 : TERM
  TERM duration(amount=duration_16, unit=unit_hour) -> duration_21 : TERM
  TERM duration(amount=duration_17, unit=unit_minute) -> duration_22 : TERM
  TERM duration(amount=duration_18, unit=unit_second) -> duration_23 : TERM
  TERM duration(amount=duration_19, unit=unit_second) -> duration_24 : TERM
  TERM duration(amount=duration_20, unit=unit_second) -> duration_25 : TERM
  TERM duration(amount=duration_21, unit=unit_hour) -> duration_26 : TERM
  TERM duration(amount=duration_22, unit=unit_minute) -> duration_27 : TERM
  TERM duration(amount=duration_23, unit=unit_second) -> duration_28 : TERM
  TERM duration(amount=duration_24, unit=unit_second) -> duration_29 : TERM
  TERM duration(amount=duration_25, unit=unit_second) -> duration_30 : TERM
  TERM duration(amount=duration_26, unit=unit_hour) -> duration_31 : TERM
  TERM duration(amount=duration_27, unit=unit_minute) -> duration_32 : TERM
  TERM duration(amount=duration_28, unit=unit_second) -> duration_33 : TERM
  TERM duration(amount=duration_29, unit=unit_second) -> duration_34 : TERM
  TERM duration(amount=duration_30, unit=unit_second) -> duration_35 : TERM
  TERM duration(amount=duration_31, unit=unit_hour) -> duration_36 : TERM
  TERM duration(amount=duration_32, unit=unit_minute) -> duration_37 : TERM
  TERM duration(amount=duration_33, unit=unit_second) -> duration_38 : TERM
  TERM duration(amount=duration_34, unit=unit_second) -> duration_39 : TERM
  TERM duration(amount=duration_35, unit=unit_second) -> duration_40 : TERM
  TERM duration(amount=duration_36, unit=unit_hour) -> duration_41 : TERM
  TERM duration(amount=duration_37, unit=unit_minute) -> duration_42 : TERM
  TERM duration(amount=duration_38, unit=unit_second) -> duration_43 : TERM
  TERM duration(amount=duration_39, unit=unit_second) -> duration_44 : TERM
  TERM duration(amount=duration_40, unit=unit_second) -> duration_45 : TERM
  TERM duration(amount=duration_41, unit=unit_hour) -> duration_46 : TERM
  TERM duration(amount=duration_42, unit=unit_minute) -> duration_47 : TERM
  TERM duration(amount=duration_43, unit=unit_second) -> duration_48 : TERM
  TERM duration(amount=duration_44, unit=unit_second) -> duration_49 : TERM
  TERM duration(amount=duration_45, unit=unit_second) -> duration_50 : TERM
  TERM duration(amount=duration_46, unit=unit_hour) -> duration_51 : TERM
  TERM duration(amount=duration_47, unit=unit_minute) -> duration_52 : TERM
  TERM duration(amount=duration_48, unit=unit_second) -> duration_53 : TERM
  TERM duration(amount=duration_49, unit=unit_second) -> duration_54 : TERM
  TERM duration(amount=duration_50, unit=unit_second) -> duration_55 : TERM
  TERM duration(amount=duration_51, unit=unit_hour) -> duration_56 : TERM
  TERM duration(amount=duration_52, unit=unit_minute) -> duration_57 : TERM
  TERM duration(amount=duration_53, unit=unit_second) -> duration_58 : TERM
  TERM duration(amount=duration_54, unit=unit_second) -> duration_59 : TERM
  TERM duration(amount=duration_55, unit=unit_second) -> duration_60 : TERM
  TERM duration(amount=duration_56, unit=unit_hour) -> duration_61 : TERM
  TERM duration(amount=duration_57, unit=unit_minute) -> duration_62 : TERM
  TERM duration(amount=duration_58, unit=unit_second) -> duration_63 : TERM
  TERM duration(amount=duration_59, unit=unit_second) -> duration_64 : TERM
  TERM duration(amount=duration_60, unit=unit_second) -> duration_65 : TERM
  TERM duration(amount=duration_61, unit=unit_hour) -> duration_66 : TERM
  TERM duration(amount=duration_62, unit=unit_minute) -> duration_67 : TERM
  TERM duration(amount=duration_63, unit=unit_second) -> duration_68 : TERM
  TERM duration(amount=duration_64, unit=unit_second) -> duration_69 : TERM
  TERM duration(amount=duration_65, unit=unit_second) -> duration_70 : TERM
  TERM duration(amount=duration_66, unit=unit_hour) -> duration_71 : TERM
  TERM duration(amount=duration_67, unit=unit_minute) -> duration_72 : TERM
  TERM duration(amount=duration_68, unit=unit_second) -> duration_73 : TERM
  TERM duration(amount=duration_69, unit=unit_second) -> duration_74 : TERM
  TERM duration(amount=duration_70, unit=unit_second) -> duration_75 : TERM
  TERM duration(amount=duration_71, unit=unit_hour) -> duration_76 : TERM
  TERM duration(amount=duration_72, unit=unit_minute) -> duration_77 : TERM
  TERM duration(amount=duration_73, unit=unit_second) -> duration_78 : TERM
  TERM duration(amount=duration_74, unit=unit_second) -> duration_79 : TERM
  TERM duration(amount=duration_75, unit=unit_second) -> duration_80 : TERM
  TERM duration(amount=duration_76, unit=unit_hour) -> duration_81 : TERM
  TERM duration(amount=duration_77, unit=unit_minute) -> duration_82 : TERM
  TERM duration(amount=duration_78, unit=unit_second) -> duration_83 : TERM
  TERM duration(amount=duration_79, unit=unit_second) -> duration_84 : TERM
  TERM duration(amount=duration_80, unit=unit_second) -> duration_85 : TERM
  TERM duration(amount=duration_81, unit=unit_hour) -> duration_86 : TERM
  TERM duration(amount=duration_82, unit=unit_minute) -> duration_87 : TERM
  TERM duration(amount=duration_83, unit=unit_second) -> duration_88 : TERM
  TERM duration(amount=duration_84, unit=unit_second) -> duration_89 : TERM
  TERM duration(amount=duration_85, unit=unit_second) -> duration_90 : TERM
  TERM duration(amount=duration_86, unit=unit_hour) -> duration_91 : TERM
  TERM duration(amount=duration_87, unit=unit_minute) -> duration_92 : TERM
  TERM duration(amount=duration_88, unit=unit_second) -> duration_93 : TERM
  TERM duration(amount=duration_89, unit=unit_second) -> duration_94 : TERM
  TERM duration(amount=duration_90, unit=unit_second) -> duration_95 : TERM
  TERM duration(amount=duration_91, unit=unit_hour) -> duration_96 : TERM
  TERM duration(amount=duration_92, unit=unit_minute) -> duration_97 : TERM
  TERM duration(amount=duration_93, unit=unit_second) -> duration_98 : TERM
  TERM duration(amount=duration_94, unit=unit_second) -> duration_99 : TERM
  TERM duration(amount=duration_95, unit=unit_second) -> duration_100 : TERM
  TERM duration(amount=duration_96, unit=unit_hour) -> duration_101 : TERM
  TERM duration(amount=duration_97, unit=unit_minute) -> duration_102 : TERM
  TERM duration(amount=duration_98, unit=unit_second) -> duration_103 : TERM
  TERM duration(amount=duration_99, unit=unit_second) -> duration_104 : TERM
  TERM duration(amount=duration_100, unit=unit_second) -> duration_105 : TERM
  TERM duration(amount=duration_101, unit=unit_hour) -> duration_106 : TERM
  TERM duration(amount=duration_102, unit=unit_minute) -> duration_107 : TERM
  TERM duration(amount=duration_103, unit=unit_second) -> duration_108 : TERM
  TERM duration(amount=duration_104, unit=unit_second) -> duration_109 : TERM
  TERM duration(amount=duration_105, unit=unit_second) -> duration_110 : TERM
  TERM duration(amount=duration_106, unit=unit_hour) -> duration_111 : TERM
  TERM duration(amount=duration_107, unit=unit_minute) -> duration_112 : TERM
  TERM duration(amount=duration_108, unit=unit_second) -> duration_113 : TERM
  TERM duration(amount=duration_109, unit=unit_second) -> duration_114 : TERM
  TERM duration(amount=duration_110, unit=unit_second) -> duration_115 : TERM
  TERM duration(amount=duration_111, unit=unit_hour) -> duration_116 : TERM
  TERM duration(amount=duration_112, unit=unit_minute) -> duration_117 : TERM
  TERM duration(amount=duration_113, unit=unit_second) -> duration_118 : TERM
  TERM duration(amount=duration_114, unit=unit_second) -> duration_119 : TERM
  TERM duration(amount=duration_115, unit=unit_second) -> duration_120 : TERM
  TERM duration(amount=duration_116, unit=unit_hour) -> duration_121 : TERM
  TERM duration(amount=duration_117, unit=unit_minute) -> duration_122 : TERM
  TERM duration(amount=duration_118, unit=unit_second) -> duration_123 : TERM
  TERM duration(amount=duration_119, unit=unit_second) -> duration_124 : TERM
  TERM duration(amount=duration_120, unit=unit_second) -> duration_125 : TERM
  TERM duration(amount=duration_121, unit=unit_hour) -> duration_126 : TERM
  TERM duration(amount=duration_122, unit=unit_minute) -> duration_127 : TERM
  TERM duration(amount=duration_123, unit=unit_second) -> duration_128 : TERM
  TERM duration(amount=duration_124, unit=unit_second) -> duration_129 : TERM
  TERM duration(amount=duration_125, unit=unit_second) -> duration_130 : TERM
  TERM duration(amount=duration_126, unit=unit_hour) -> duration_131 : TERM
  TERM duration(amount=duration_127, unit=unit_minute) -> duration_132 : TERM
  TERM duration(amount=duration_128, unit=unit_second) -> duration_133 : TERM
  TERM duration(amount=duration_129, unit=unit_second) -> duration_134 : TERM
  TERM duration(amount=duration_130, unit=unit_second) -> duration_135 : TERM
  TERM duration(amount=duration_131, unit=unit_hour) -> duration_136 : TERM
  TERM duration(amount=duration_132, unit=unit_minute) -> duration_137 : TERM
  TERM duration(amount=duration_133, unit=unit_second) -> duration_138 : TERM
  TERM duration(amount=duration_134, unit=unit_second) -> duration_139 : TERM
  TERM duration(amount=duration_135, unit=unit_second) -> duration_140 : TERM
  TERM duration(amount=duration_136, unit=unit_hour) -> duration_141 : TERM
  TERM duration(amount=duration_137, unit=unit_minute) -> duration_142 : TERM
  TERM duration(amount=duration_138, unit=unit_second) -> duration_143 : TERM
  TERM duration(amount=duration_139, unit=unit_second) -> duration_144 : TERM
  TERM duration(amount=duration_140, unit=unit_second) -> duration_145 : TERM
  TERM duration(amount=duration_141, unit=unit_hour) -> duration_146 : TERM
  TERM duration(amount=duration_142, unit=unit_minute) -> duration_147 : TERM
  TERM duration(amount=duration_143, unit=unit_second) -> duration_148 : TERM
  TERM duration(amount=duration_144, unit=unit_second) -> duration_149 : TERM
  TERM duration(amount=duration_145, unit=unit_second) -> duration_150 : TERM
  TERM duration(amount=duration_146, unit=unit_hour) -> duration_151 : TERM
  TERM duration(amount=duration_147, unit=unit_minute) -> duration_152 : TERM
  TERM duration(amount=duration_148, unit=unit_second) -> duration_153 : TERM
  TERM duration(amount=duration_149, unit=unit_second) -> duration_154 : TERM
  TERM duration(amount=duration_150, unit=unit_second) -> duration_155 : TERM
  TERM duration(amount=duration_151, unit=unit_hour) -> duration_156 : TERM
  TERM duration(amount=duration_152, unit=unit_minute) -> duration_157 : TERM
  TERM duration(amount=duration_153, unit=unit_second) -> duration_158 : TERM
  TERM duration(amount=duration_154, unit=unit_second) -> duration_159 : TERM
  TERM duration(amount=duration_155, unit=unit_second) -> duration_160 : TERM
  TERM duration(amount=duration_156, unit=unit_hour) -> duration_161 : TERM
  TERM duration(amount=duration_157, unit=unit_minute) -> duration_162 : TERM
  TERM duration(amount=duration_158, unit=unit_second) -> duration_163 : TERM
  TERM duration(amount=duration_159, unit=unit_second) -> duration_164 : TERM
  TERM duration(amount=duration_160, unit=unit_second) -> duration_165 : TERM
  TERM duration(amount=duration_161, unit=unit_hour)