```braincode
MODE REQUEST
ENTRYPOINT Table
TASK Table {
  ACTION pick_up(target=table, quantity=35, source=source_code) -> table_ref : REF[STRING]
  ACTION place(target=table_ref, destination=csv_format) -> table_ref_2 : REF[STRING]
  ACTION save(target=table_ref_2, destination=csv_file) -> save_result : EVENT
  ACTION rinse(target=save_result, destination=csv_file) -> csv_file_ref : REF[STRING]
  ACTION record(event=csv_file_ref, status="failed") -> record_event : EVENT
  ACTION extract(target=csv_file_ref, location=null_values) -> null_values_list : LIST[REF[STRING]]
  ACTION sort(target=null_values_list, rank_direction=dir_asc, rank_field=rank_distance) -> sorted_null_values : LIST[REF[STRING]]
  ACTION extract(target=sorted_null_values, location=column_coding_minutes) -> coding_minutes_sum : NUMBER
  ACTION extract(target=sorted_null_values, location=column_study_minutes) -> study_minutes_sum : NUMBER
  ACTION at_least(target=coding_minutes_sum, measure=study_minutes_sum) -> result : TERM
  ACTION time_point(target=result, timezone=timezone_utc) -> rounded_result : TERM
  ACTION assert_multinomial_scorer() -> outcome : CLAIM
  ACTION record(event=rounded_result, value="0") -> outcome_event : EVENT
}
```