<|user|>DEPR: Index.is_mixed
אנחנו משתמשים בו רק במקום אחד, והסרתו משם אינה שוברת שום דבר. יתר על כן, הוא מתנהג באופן מפתיע:



```

>>> pd.Index(['a', np.nan, 'b']).is_mixed()

True



>>> Index([0, 'a', 1, 'b', 2, 'c']).is_mixed()

False

```
<|assistant|>1. שנה את doc/source/whatsnew/v1.1.0.rst
2. שנה את pandas/core/indexes/base.py
