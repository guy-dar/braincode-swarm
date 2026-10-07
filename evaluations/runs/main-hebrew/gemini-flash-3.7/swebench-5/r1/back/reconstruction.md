<|user|>Incorrect drawing of composite gates with qubits and classical bits when using text drawer
<!-- ⚠️ If you do not respect this template, your issue will be closed -->

<!-- ⚠️ Make sure to browse the opened and closed issues -->



### Information



- **Qiskit Terra version**: 0.18.0.dev0+2ecf45d

- **Python version**: 3.7



### What is the current behavior?



The text drawer incorrectly draws composite gates containing both qubits and classical bits. This error seems to occur only when appending the composite gate and when the qreg_list or creg_list provided to qc.append() are not in ascending order. 



For example, consider the following code:



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



The text circuit drawn is as follows:



![qiskit_text_error](https://user-images.githubusercontent.com/51048173/113936418-5b64cd00-9815-11eb-9ce2-7ac910e99d1d.png)



Also, the numbering of the active wires is incorrect.



### Suggested solutions



The error seems to be caused by drawing the gate components in the wrong order. Looking at the following function will help.



https://github.com/Qiskit/qiskit-terra/blob/2ecf45d90d47b430493e218b218d6639cabf7ff1/qiskit/visualization/text.py#L1211




<|assistant|>1. Modify qiskit/visualization/text.py
