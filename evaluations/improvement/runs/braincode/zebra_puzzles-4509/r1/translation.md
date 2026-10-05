```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  ACTION search_web(target="orange house", limit=1) -> orange_house_ref : REF[STRING]
  ACTION extract(limit=1) -> orange_house_ref_list : LIST[REF[STRING]]
  ACTION sort(rank_direction="ascending", rank_field="rank_distance") -> sorted_list : LIST[REF[STRING]]
  ACTION place(target=sorted_list[0], destination=orange_house_ref) -> orange_house_ref_2 : REF[STRING]
  ACTION turn(direction="left") -> agent_orientation : void
  ACTION walk(destination=orange_house_ref_2) -> orange_house_position : void
  ACTION stand_up() -> agent_posture : void
  ACTION return() -> orange_house_position_2 : NUMBER
}
```