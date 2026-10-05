<|user|>In qiskit_terra, drawing correctness is false.
The software version of qiskit_terra is "0.18.0.dev0+2ecf45d".
The software version of python is "3.7".
In qiskit_terra, composite gate drawing is false.
It is hypothesized that in qiskit_terra, drawing order sensitivity is "non_ascending_register_list".
An example snippet "reproduction_circuit" is provided for qiskit_terra.
Figure captioned "qiskit_text_error": https://user-images.githubusercontent.com/51048173/113936418-5b64cd00-9815-11eb-9ce2-7ac910e99d1d.png
In qiskit_terra, active wire numbering is false.
It is hypothesized that the root cause in qiskit_terra is "component_drawing_order", which causes composite gate drawing to fail.
In qiskit_terra, file "qiskit/visualization/text.py", function "line_1211".
<|assistant|>I propose modifying the code in qiskit_terra for file "qiskit/visualization/text.py" at "line_1211".
