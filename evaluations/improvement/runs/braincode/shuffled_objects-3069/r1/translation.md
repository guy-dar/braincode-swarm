```braincode
MODE REQUEST
ENTRYPOINT SquareDance
TASK SquareDance {
  ACTION pick_up(target=object_label::dancer, quantity=7, source=object_label::dance_floor) -> object_label_dancers_refs : LIST[REF[STRING]]
  FOR EACH dancer IN object_label_dancers_refs {
    ACTION place(target=dancer, destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn(target=object_label::dance_floor, direction=left)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=right)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=right)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=right)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=left)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=right)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=left)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=left)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=right)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=right)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=left)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=right)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=left)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=left)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=right)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=right)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=left)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=left)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=right)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=left)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=right)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=left)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=right)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=left)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=left)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=right)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=left)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=right)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=left)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=right)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=left)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=left)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=right)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=left)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=left)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=right)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=right)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=left)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=left)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=right)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=right)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=left)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=left)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=right)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=left)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=left)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
  ACTION wait(duration=30)
  ACTION turn_on(target=object_label::music_player, direction=on)
  ACTION turn_on(target=object_label::dance_floor, direction=right)
  FOR EACH i IN [1, 7] {
    ACTION walk(destination=object_label::dance_floor, relation=on)
  }
  ACTION turn_on(target=object_label::music_player, direction=off)
 