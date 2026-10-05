<|user|>DEPR: Index.is_mixed
There is 1 duplicate definition of Index.is_mixed, and removing it does not break anything.
The behavior of Index.is_mixed is surprising.
pd.Index(['a', np.nan, 'b']).is_mixed() is True.
However, Index([0, 'a', 1, 'b', 2, 'c']).is_mixed() is False.
<|assistant|>1. Modify doc/source/whatsnew/v1.1.0.rst
2. Modify pandas/core/indexes/base.py
