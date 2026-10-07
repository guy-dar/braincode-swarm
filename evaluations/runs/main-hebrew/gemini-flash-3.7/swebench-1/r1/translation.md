<|user|>UnboundLocalError: משתנה מקומי 'seq_length' אוזכר לפני השמה
### מידע על המערכת

היי, אני משתמש במודל `ConvBertForTokenClassification` ב-models.convbert ונתקלתי בבאג בעת העברת `input_embeds` בלבד ל-`forward()`.

ה-traceback מציין שבשורה 833 ב-modeling_convbert.py

```

if token_type_ids is None:

    if hasattr(self.embeddings, "token_type_ids"):

        buffered_token_type_ids = self.embeddings.token_type_ids[:, :seq_length]

```

ל-seq_length לא הוקצה ערך.



שמתי לב שממש מעל קטע קוד זה ב-

```

elif input_ids is not None:

    input_shape = input_ids.size()

    batch_size, seq_length = input_shape

elif inputs_embeds is not None:

    input_shape = inputs_embeds.size()[:-1]

```

ל-seq_length לא מוקצה ערך אם התוכנית נכנסת ל-`elif inputs_embeds is not None`.



לא בטוח אם ה-`batch_size, seq_length = input_shape` חסר עבור `inputs_embeds` או שאני לא משתמש במודל נכון?

### מי יכול לעזור?

מודלי טקסט: @ArthurZucker ו-@younesbelkada

### מידע

- [ ] סקריפטי הדוגמה הרשמיים
- [X] סקריפטים מותאמים אישית שלי

### משימות

- [ ] משימה הנתמכת באופן רשמי בתיקיית `examples` (כגון GLUE/SQuAD, ...)
- [X] משימה או מערך נתונים משלי (פרטו להלן)

### שחזור

העברת `inputs_embeds` ו-`attention_mask` בלבד למודל `ConvBertForTokenClassification`.

### התנהגות צפויה

לא אמורה להיות שגיאה.
<|assistant|>1. לשנות את src/transformers/models/convbert/modeling_convbert.py
