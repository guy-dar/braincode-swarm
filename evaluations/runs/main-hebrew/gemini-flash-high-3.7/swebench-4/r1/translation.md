<|user|>לא ניתן להשלים חיבורים מרוחקים עבור שני תהליכים
שלבים לשחזור:

```
ipython console --ip=0
```

ואז, נסו להתחבר אליו מחלון אחר:

```
ipython console --exiting
```

והוא ייתקע. אם לא מציינים --ip, הכל עובד, כי הקוד המקומי עובר דרך נתיב קוד שונה במקצת. רק פותח את זה עכשיו כדי של-@minrk יהיה משהו להתייחס אליו כשהוא מגיש את התיקון

<|assistant|>1. לשנות את IPython/consoleapp.py
2. לשנות את IPython/kernel/client.py
3. לשנות את IPython/qt/console/qtconsoleapp.py
