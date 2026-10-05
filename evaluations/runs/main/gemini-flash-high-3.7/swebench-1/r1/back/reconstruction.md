<|user|>UnboundLocalError: local variable 'seq_length' referenced before assignment
Hello maintainers,
I called the forward method of ConvBertForTokenClassification in models.convbert in transformers.
The condition token_type_ids_is_none is TRUE.
Line 833 in modeling_convbert.py in transformers leads to seq_length_unassigned being TRUE.
inputs_embeds has property unpacks_seq_length as FALSE.
What is the cause_of_error regarding missing_unpacking_or_misuse?
Requesting ArthurZucker_and_younesbelkada.
I run modified_scripts in transformers.
I run custom_task_or_dataset in transformers.
I perform the forward calculation on ConvBertForTokenClassification.
The requirement of error_free_execution is not satisfied.
<|assistant|>I propose modifying the code in src/transformers/models/convbert/modeling_convbert.py (modeling_convbert.py) in transformers.