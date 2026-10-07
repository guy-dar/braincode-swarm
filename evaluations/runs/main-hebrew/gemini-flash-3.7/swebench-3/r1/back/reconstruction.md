<|user|>General:  DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated, and in 3.8 it will stop working
I get this deprecation warning when running pytests in my app that uses Google Storage.



#### Environment details



Arch Linux

Python 3.7.1

google-api-core==1.5.1

google-auth==1.5.1

google-cloud-core==0.28.1

google-cloud-storage==1.13.0

google-resumable-media==0.3.1

googleapis-common-protos==1.5.5

pytest==3.9.1



#### Steps to reproduce



  1. Create a `test.py` file.

  2. Add the line `from google.protobuf.pyext import _message` to it.

  3. Run `pytest test.py` (to install pytest first `pip install pytest==3.9.1`)

  4. Pytest will print the following: `test.py:1: DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated, and in 3.8 it will stop working

  from google.protobuf.pyext import _message`



In my testing this warning comes from: `google/protobuf/internal/api_implementation.py:154`



I could not reproduce in shell, but pytest somehow catches it while running tests.
<|assistant|>1. Modify api_core/google/api_core/protobuf_helpers.py
2. Modify bigquery/google/cloud/bigquery/client.py
3. Modify bigquery/google/cloud/bigquery/dbapi/_helpers.py
4. Modify bigquery/google/cloud/bigquery/dbapi/cursor.py
5. Modify core/google/cloud/iam.py
6. Modify firestore/google/cloud/firestore_v1beta1/_helpers.py
