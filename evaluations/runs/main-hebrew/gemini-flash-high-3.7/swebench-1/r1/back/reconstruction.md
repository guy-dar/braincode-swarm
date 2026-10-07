<|user|>UnboundLocalError: local variable 'seq_length' referenced before assignment
### System Info

Hi, I am using the `ConvBertForTokenClassification` model in models.convbert and encountered a bug when passing only `input_embeds` to `forward()`.

The traceback indicates that at line 833 in modeling_convbert.py

```

if token_type_ids is None:

    if hasattr(self.embeddings, "token_type_ids"):

        buffered_token_type_ids = self.embeddings.token_type_ids[:, :seq_length]

```

the seq_length is not assigned.



I noticed right above this snippet in

```

elif input_ids is not None:

    input_shape = input_ids.size()

    batch_size, seq_length = input_shape

elif inputs_embeds is not None:

    input_shape = inputs_embeds.size()[:-1]

```

no value is assigned to seq_length if the program enters `elif inputs_embeds is not None`.



Not sure if the `batch_size, seq_length = input_shape` is missing for `inputs_embeds` or am I not using the model correctly?

### Who can help?

Text models: @ArthurZucker and @younesbelkada

### Information

- [ ] The official example scripts
- [X] My own modified scripts

### Tasks

- [ ] An officially supported task in the `examples` folder (such as GLUE/SQuAD, ...)
- [X] My own task or dataset (give details below)

### Reproduction

Passing only `inputs_embeds` and `attention_mask` to the `ConvBertForTokenClassification` model.

### Expected behavior

There should be no error.
<|assistant|>1. Modify src/transformers/models/convbert/modeling_convbert.py
