<|user|>כללי:  DeprecationWarning: שימוש או ייבוא של ה-ABCs מ-'collections' במקום מ-'collections.abc' הוצא משימוש, וב-3.8 זה יפסיק לעבוד
אני מקבל את אזהרת ההוצאה משימוש הזו בעת הרצת pytests באפליקציה שלי שמשתמשת ב-Google Storage.



#### פרטי הסביבה



Arch Linux

Python 3.7.1

google-api-core==1.5.1

google-auth==1.5.1

google-cloud-core==0.28.1

google-cloud-storage==1.13.0

google-resumable-media==0.3.1

googleapis-common-protos==1.5.5

pytest==3.9.1



#### שלבים לשחזור



  1. צור קובץ `test.py`.

  2. הוסף אליו את השורה `from google.protobuf.pyext import _message`.

  3. הרץ `pytest test.py` (כדי להתקין את pytest תחילה `pip install pytest==3.9.1`)

  4. Pytest ידפיס את הבא: `test.py:1: DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated, and in 3.8 it will stop working

  from google.protobuf.pyext import _message`



בבדיקות שלי אזהרה זו מגיעה מ: `google/protobuf/internal/api_implementation.py:154`



לא הצלחתי לשחזר ב-shell, אבל pytest איכשהו תופס את זה בזמן הרצת בדיקות.
<|assistant|>1. שנה את api_core/google/api_core/protobuf_helpers.py
2. שנה את bigquery/google/cloud/bigquery/client.py
3. שנה את bigquery/google/cloud/bigquery/dbapi/_helpers.py
4. שנה את bigquery/google/cloud/bigquery/dbapi/cursor.py
5. שנה את core/google/cloud/iam.py
6. שנה את firestore/google/cloud/firestore_v1beta1/_helpers.py
