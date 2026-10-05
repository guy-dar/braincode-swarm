```braincode
MODE REQUEST
ENTRYPOINT TableAnalysis
TASK TableAnalysis : STRING {
  ACTION save_table(target=table, format=table) -> table_saved : REF[STRING]
  ACTION failed_save(target=table_saved) -> failed_save_2 : REF[STRING]
  ACTION extract(target=failed_save_2, locations=LIST[REF[STRING]]) -> extract_2 : LIST[REF[STRING]]
  ACTION sort(target=extract_2, field=phone_screen_time_minutes, direction=dir_asc) -> sorted_2 : LIST[REF[STRING]]
  ACTION include(target=sorted_2, criteria=LIST[CLAIM]) -> included_2 : LIST[REF[STRING]]
  ACTION calculate(target=included_2, field=LIST[TERM]) -> calculated_2 : TERM
  ACTION round(target=calculated_2, digits=2) -> rounded_2 : TERM
  ACTION assert(target=rounded_2, condition=LIST[CLAIM]) -> asserted_2 : CLAIM
  ACTION assume(target=asserted_2, condition=LIST[CLAIM]) -> assumed_2 : CLAIM
  ACTION ignore_nulls(target=assumed_2, fields=LIST[TERM]) -> ignored_nulls_2 : CLAIM
  ACTION check_condition(target=ignored_nulls_2, values=LIST[CLAIM]) -> checked_2 : CLAIM
  ACTION output(target=checked_2, format=STRING) -> output_2 : STRING
  RETURN output_2
}
```