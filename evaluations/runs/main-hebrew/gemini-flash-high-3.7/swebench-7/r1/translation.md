<|user|>DEPR: Index.is_mixed
אנו משתמשים בו רק במקום אחד, והסרתו משם אינה שוברת דבר. יתרה מזאת, הוא מתנהג באופן מפתיע:



```

>>> pd.Index(['a', np.nan, 'b']).is_mixed()

True



>>> Index([0, 'a', 1, 'b', 2, 'c']).is_mixed()

False

```
<|assistant|>1. לשנות את doc/source/whatsnew/v1.1.0.rst
2. לשנות את pandas/core/indexes/base.py
