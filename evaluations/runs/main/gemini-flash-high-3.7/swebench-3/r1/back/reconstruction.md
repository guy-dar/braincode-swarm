<|user|>Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated, and in 3.8 it will stop working
Application: google_cloud_storage
arch_linux
python 3.7.1
google_api_core 1.5.1
google_auth 1.5.1
google_cloud_core 0.28.1
google_cloud_storage 1.13.0
google_resumable_media 0.3.1
googleapis_common_protos 1.5.5
pytest 3.9.1
test.py
from google.protobuf.pyext import _message
pip install pytest==3.9.1
pytest test.py
test.py:1: DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated, and in 3.8 it will stop working
DeprecationWarning originates from google/protobuf/internal/api_implementation.py:154
could not reproduce in shell
pytest catches deprecation warning while running tests
<|assistant|>Modify api_core/google/api_core/protobuf_helpers.py in google_api_core
Modify bigquery/google/cloud/bigquery/client.py in bigquery
Modify bigquery/google/cloud/bigquery/dbapi/_helpers.py in bigquery
Modify bigquery/google/cloud/bigquery/dbapi/cursor.py in bigquery
Modify core/google/cloud/iam.py in google_cloud_core
Modify firestore/google/cloud/firestore_v1beta1/_helpers.py in firestore
