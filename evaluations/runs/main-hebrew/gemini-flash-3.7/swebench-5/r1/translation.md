<|user|>ציור שגוי של שערים מורכבים עם קיוביטים וביטים קלאסיים בעת שימוש ב-text drawer
<!-- ⚠️ If you do not respect this template, your issue will be closed -->

<!-- ⚠️ Make sure to browse the opened and closed issues -->



### מידע



- **גרסת Qiskit Terra**: 0.18.0.dev0+2ecf45d

- **גרסת Python**: 3.7



### מהי ההתנהגות הנוכחית?



ה-text drawer מצייר בצורה שגויה שערים מורכבים המכילים הן קיוביטים והן ביטים קלאסיים. נראה ששגיאה זו מתרחשת רק בעת הוספת השער המורכב וכאשר ה-qreg_list או ה-creg_list שסופקו ל-qc.append() אינם בסדר עולה. 



לדוגמה, שקלו את הקוד הבא:



```python

from qiskit import QuantumCircuit



inst = QuantumCircuit(3, 2, name='inst').to_instruction()

inst2 = QuantumCircuit(3,name='inst2').to_instruction()

qc = QuantumCircuit(4,2)

qc.append(inst,[2,1,0],[0,1])

qc.append(inst,[0,1,2],[1,0])

qc.append(inst2,[2,1,0])

qc.draw()

```



מעגל הטקסט שמצויר הוא כדלקמן:



![qiskit_text_error](https://user-images.githubusercontent.com/51048173/113936418-5b64cd00-9815-11eb-9ce2-7ac910e99d1d.png)



כמו כן, המספור של החוטים הפעילים שגוי.



### פתרונות מוצעים



נראה שהשגיאה נגרמת עקב ציור רכיבי השער בסדר שגוי. עיון בפונקציה הבאה יעזור.



https://github.com/Qiskit/qiskit-terra/blob/2ecf45d90d47b430493e218b218d6639cabf7ff1/qiskit/visualization/text.py#L1211




<|assistant|>1. לשנות את qiskit/visualization/text.py
