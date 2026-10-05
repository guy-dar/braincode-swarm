```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  ACTION determine_sarcasm(target=POST_1, tone?: tone_silly) -> tone_result : TERM
  ACTION determine_sarcasm(target=POST_2, tone?: tone_silly) -> tone_result_2 : TERM
  ACTION determine_sarcasm(target=POST_3, tone?: tone_silly) -> tone_result_3 : TERM
  ACTION label_reply(tone_result: TERM, tone_result_2: TERM, tone_result_3: TERM) -> result : TERM
  ACTION format_result(result: TERM) -> formatted_result : TERM
  ACTION check_reply(tone_result: TERM, tone_result_2: TERM, tone_result_3: TERM) -> result : TERM
}
```