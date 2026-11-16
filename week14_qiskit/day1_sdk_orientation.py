import qiskit
from qiskit import QuantumCircuit

print(qiskit.__version__)

qc = QuantumCircuit(1)
qc.h(0)

print(qc)
print("Number of qubits:", qc.num_qubits)
print("Number of classical bits:", qc.num_clbits)
print("Circuit depth:", qc.depth())
print(qc.draw())

"""
A quantum circuit does not need classical bits simply because it runs on a classical simulator.
- Quantum bits represent quantum information in the circuit.
- Classical bits store the results when we measure quantum bits.

print(qc) --> displays the quantum circuit. 

Circuit depth measures the number of sequential operation layers along the circuit's critical path.

In NumPy, we explicitly perform the matrix multiplication [new_state = H @ state]. In Qiskit, we describe the operation
qc.h(0). 
Qiskit constructs and stores the circuit instructions; Aer performs the simulation of those instructions. The 
matrix-based state evolution is handled by the simulator rather than written explicitly in the code
"""