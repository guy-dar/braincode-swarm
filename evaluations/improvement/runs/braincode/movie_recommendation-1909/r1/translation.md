```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  ACTION search_web(target="movies", constraints=[similarity(target="people", dimension="liking")]) -> results : LIST[REF[STRING]]
  ACTION select_option(target=results[0], value="option_with_most_similar_movies") -> selected_option : void
  ACTION propose_menu(menu=selected_option) -> menu : TERM
  ACTION inform(target=menu) -> result : TERM
  ACTION express_interest(target=result) -> interest : void
  ACTION ask(target="how_many_options") -> answer : TERM
  ACTION propose(target="option_count") -> proposal : TERM
  ACTION inform(target=proposal) -> count : TERM
}
```