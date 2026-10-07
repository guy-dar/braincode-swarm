<|user|>DEPR: Index.is_mixed
We only use it in one place, and removing it from there doesn't break anything. Moreover, it behaves surprisingly:



```

>>> pd.Index(['a', np.nan, 'b']).is_mixed()

True



>>> Index([0, 'a', 1, 'b', 2, 'c']).is_mixed()

False

```
<|assistant|>1. Modify doc/source/whatsnew/v1.1.0.rst
2. Modify pandas/core/indexes/base.py
