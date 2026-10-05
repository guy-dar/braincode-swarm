```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  ACTION search_web(target=animal_label::human, query="BrainCode") -> braincode_ref : REF[STRING]
  ACTION extract(limit=1) -> braincode_list : LIST[REF[STRING]]
  ACTION pick_up(target=braincode_ref) -> braincode_ref_2 : REF[STRING]
  ACTION place(target=braincode_ref_2, destination=computer) -> braincode_ref_3 : REF[STRING]
  ACTION generate(target=braincode_ref_3, format=plain_text) -> braincode_text : STRING
  ACTION rinse(destination=braincode_text) -> cleaned_text : STRING
  ACTION heat(target=cleaned_text, temperature=normal) -> warmed_text : STRING
  ACTION chill(target=warmed_text, temperature=low) -> cooled_text : STRING
  ACTION extract(limit=1) -> answer : STRING
  ACTION format(target=answer, style=bullet_list) -> formatted_answer : STRING
  ACTION record(target=formatted_answer, format=plain_text) -> recorded_answer : STRING
  ACTION pick_up(target=recorded_answer) -> final_answer : REF[STRING]
  ACTION place(target=final_answer, destination=answer_box) -> final_answer_2 : REF[STRING]
  ACTION generate(target=final_answer_2, format=plain_text) -> final_answer_3 : STRING
  ACTION format(target=final_answer_3, style=plain_text) -> final_answer_4 : STRING
  ACTION record(target=final_answer_4, format=plain_text) -> final_answer_5 : STRING
}
```