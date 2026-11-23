from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


qc = QuantumCircuit(1)
state = Statevector.from_instruction(qc)

print("Initial statevector:", state.data)

qc.x(0)
state = Statevector.from_instruction(qc)

print("Statevector after X:", state.data)

"""
Learning: 
Statevector.from_instruction(qc) evaluates the circuit instructions and gives us the resulting statevector.
Statevector.from_instruction(qc) lets us inspect a circuit's resulting quantum state without measurement
"""

# Circuit A
qc_a = QuantumCircuit(1)
qc_a.h(0)

state_a = Statevector.from_instruction(qc_a)

# Circuit B
qc_b = QuantumCircuit(1)
qc_b.x(0)
qc_b.h(0)

state_b = Statevector.from_instruction(qc_b)

print("Circuit A:", state_a.data)
print("Circuit A probabilities:", state_a.probabilities())

print("Circuit B:", state_b.data)
print("Circuit B probabilities:", state_b.probabilities())

"""
Two quantum states can have identical measurement probabilities in one basis but be distinguishable in another basis 
because of their relative phase.
"""
