import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# Circuit A: Apply X to qubit 0
qc_a = QuantumCircuit(2)
qc_a.x(0)

state_a = Statevector.from_instruction(qc_a)

# Circuit B: Apply X to qubit 1
qc_b = QuantumCircuit(2)
qc_b.x(1)

state_b = Statevector.from_instruction(qc_b)

print("Circuit A statevector:")
print(state_a.data)

print("\nCircuit B statevector:")
print(state_b.data)

print("\nCircuit A probabilities:")
print(state_a.probabilities())

print("\nCircuit B probabilities:")
print(state_b.probabilities())

# Circuit C: Apply X to both qubits
qc_c = QuantumCircuit(2)
qc_c.x(0)
qc_c.x(1)

state_c = Statevector.from_instruction(qc_c)

print("\nCircuit C statevector:")
print(state_c.data)

print("\nCircuit C probabilities:")
print(state_c.probabilities())

# Circuit D: H on qubit 0 and X on qubit 1
qc_d = QuantumCircuit(2)
qc_d.h(0)
qc_d.x(1)

state_d = Statevector.from_instruction(qc_d)

print("\nCircuit D statevector:")
print(state_d.data)

print("\nCircuit D probabilities:")
print(state_d.probabilities())

# Verify using NumPy tensor product
q0 = np.array([1, 1]) / np.sqrt(2)
q1 = np.array([0, 1])

numpy_state = np.kron(q1, q0)

print("\nNumPy combined state:")
print(numpy_state)

print("\nDo Qiskit and NumPy agree?")
print(np.allclose(state_d.data, numpy_state))

# Circuit E: Bell-state preparation
qc_e = QuantumCircuit(2)
qc_e.h(0)
qc_e.cx(0, 1)

state_e = Statevector.from_instruction(qc_e)

print("\nCircuit E statevector:")
print(state_e.data)

print("\nCircuit E probabilities:")
print(state_e.probabilities())

"""
Day 4 — Two-Qubit Statevectors and Qubit Ordering

1. Qiskit uses the basis ordering:
   [|00>, |01>, |10>, |11>]

2. In ket notation, q0 is the rightmost bit and q1
   is the leftmost bit.

3. Applying X to q0 flips the rightmost bit.
   Applying X to q1 flips the leftmost bit.

4. For two single-qubit states, the combined Qiskit
   statevector is calculated as:
   np.kron(q1, q0)

5. In CX(0, 1), q0 is the control qubit and q1 is
   the target qubit. If q0 = 1, q1 flips.

6. Bell state preparation:
   H(0) followed by CX(0, 1) produces:

   |Phi+> = (|00> + |11>) / sqrt(2)

   Statevector:
   [1/sqrt(2), 0, 0, 1/sqrt(2)]

   Probabilities:
   [0.5, 0, 0, 0.5]

7. When measuring q0 alone in this Bell state:
   - Possible outcomes: 0 and 1
   - Probability of each outcome: 0.5
   - If q0 = 1, q1 must also be 1.

Key learning:
The four-element probability vector represents
two-qubit basis-state probabilities. When measuring
only one qubit, combine the probabilities of basis
states that share the same value for that qubit.
"""
