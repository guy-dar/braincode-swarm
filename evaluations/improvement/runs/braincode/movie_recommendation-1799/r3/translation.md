```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  ACTION search_travel(target="similar_movies", constraints=["group_of_people_will_like"], location="movies") -> similar_movies_result : LIST[REF[STRING]]
  ACTION select_option(target=similar_movies_result, value="option") -> selected_option : void
}
```