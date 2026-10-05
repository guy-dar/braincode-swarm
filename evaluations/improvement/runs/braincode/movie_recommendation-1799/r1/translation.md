```braincode
MODE REQUEST
ENTRYPOINT Task
TASK Task {
  ACTION similarity(target="A", dimension="group_of_people") -> similarity_result : TERM
  ACTION similarity(target="B", dimension="group_of_people") -> similarity_result_2 : TERM
  ACTION similarity(target="C", dimension="group_of_people") -> similarity_result_3 : TERM
  ACTION similarity(target="D", dimension="group_of_people") -> similarity_result_4 : TERM
  ACTION similarity(target="E", dimension="group_of_people") -> similarity_result_5 : TERM
  ACTION similarity(target="F", dimension="group_of_people") -> similarity_result_6 : TERM
  ACTION similarity(target="G", dimension="group_of_people") -> similarity_result_7 : TERM
  ACTION similarity(target="H", dimension="group_of_people") -> similarity_result_8 : TERM
  ACTION similarity(target="I", dimension="group_of_people") -> similarity_result_9 : TERM
  ACTION similarity(target="J", dimension="group_of_people") -> similarity_result_10 : TERM
  ACTION compare(similarity_result, similarity_result_2) -> result : CLAIM
  ACTION compare(similarity_result, similarity_result_3) -> result_2 : CLAIM
  ACTION compare(similarity_result, similarity_result_4) -> result_3 : CLAIM
  ACTION compare(similarity_result, similarity_result_5) -> result_4 : CLAIM
  ACTION compare(similarity_result, similarity_result_6) -> result_5 : CLAIM
  ACTION compare(similarity_result, similarity_result_7) -> result_6 : CLAIM
  ACTION compare(similarity_result, similarity_result_8) -> result_7 : CLAIM
  ACTION compare(similarity_result, similarity_result_9) -> result_8 : CLAIM
  ACTION compare(similarity_result, similarity_result_10) -> result_9 : CLAIM
  ACTION compare(result, result_2) -> final_result : CLAIM
  ACTION compare(result, result_3) -> final_result_2 : CLAIM
  ACTION compare(result, result_4) -> final_result_3 : CLAIM
  ACTION compare(result, result_5) -> final_result_4 : CLAIM
  ACTION compare(result, result_6) -> final_result_5 : CLAIM
  ACTION compare(result, result_7) -> final_result_6 : CLAIM
  ACTION compare(result, result_8) -> final_result_7 : CLAIM
  ACTION compare(result, result_9) -> final_result_8 : CLAIM
  ACTION compare(result, result_10) -> final_result_9 : CLAIM
}
```