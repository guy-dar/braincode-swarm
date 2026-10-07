<|user|>לא ניתן להשלים חיבורים מרוחקים עבור שני תהליכים
צעדים לשחזור:

```
ipython console --ip=0
```

ולאחר מכן, נסו להתחבר אליו מחלון אחר:

```
ipython console --exiting
```

וזה ייתקע. אם לא מציינים --ip, הכל עובד, מכיוון שהקוד המקומי עובר דרך נתיב קוד שונה במקצת. רק פותח את זה עכשיו כדי של-@minrk יהיה משהו להתייחס אליו כשהוא מגיש את התיקון

<|assistant|>1. לשנות את IPython/consoleapp.py
2. לשנות את IPython/kernel/client.py
3. לשנות את IPython/qt/console/qtconsoleapp.py
