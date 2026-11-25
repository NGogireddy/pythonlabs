import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# Create |+> using a Hadamard gate
qc = QuantumCircuit(1)
qc.h(0)

state_plus = Statevector.from_instruction(qc)

# Create a state with global phase -1
state_global_minus = Statevector(-state_plus.data)

print("Original state:")
print(state_plus.data)

print("\nState with global phase -1:")
print(state_global_minus.data)

print("\nOriginal probabilities:")
print(state_plus.probabilities())

print("\nGlobal phase probabilities:")
print(state_global_minus.probabilities())

# Apply Hadamard to both states
# Create a Hadamard circuit
h_circuit = QuantumCircuit(1)
h_circuit.h(0)

# Apply Hadamard to both states
state_plus_after_h = state_plus.evolve(h_circuit)

state_minus_after_h = state_global_minus.evolve(h_circuit)

print("\nAfter applying Hadamard:")
print("Original:", state_plus_after_h.data)
print("Global phase:", state_minus_after_h.data)

print("\nMeasurement probabilities:")
print("Original:", state_plus_after_h.probabilities())
print("Global phase:", state_minus_after_h.probabilities())


# Circuit A: Prepare |+>
qc_plus = QuantumCircuit(1)
qc_plus.h(0)

# Circuit B: Prepare |->
qc_minus = QuantumCircuit(1)
qc_minus.x(0)
qc_minus.h(0)

# Extract statevectors
state_plus = Statevector.from_instruction(qc_plus)
state_minus = Statevector.from_instruction(qc_minus)

print("Original statevectors:")
print("Plus:", state_plus.data)
print("Minus:", state_minus.data)

print("\nOriginal probabilities:")
print("Plus:", state_plus.probabilities())
print("Minus:", state_minus.probabilities())

# Create Hadamard circuit
h_circuit = QuantumCircuit(1)
h_circuit.h(0)

# Apply Hadamard to both states
plus_after_h = state_plus.evolve(h_circuit)
minus_after_h = state_minus.evolve(h_circuit)

print("\nAfter applying Hadamard:")
print("Plus:", plus_after_h.data)
print("Minus:", minus_after_h.data)

print("\nFinal probabilities:")
print("Plus:", plus_after_h.probabilities())
print("Minus:", minus_after_h.probabilities())
