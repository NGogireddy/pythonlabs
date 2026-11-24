import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# Create a two-qubit circuit
qc = QuantumCircuit(2)

# Prepare the quantum state
qc.h(0)
qc.s(0)
qc.cx(0, 1)

# Extract the statevector
state = Statevector.from_instruction(qc)

# Display the amplitudes
print("Statevector:")
print(state.data)

# Display measurement probabilities
print("\nProbabilities:")
print(state.probabilities())

# Calculate probabilities using NumPy
numpy_probabilities = np.abs(state.data) ** 2

print("\nProbabilities calculated using NumPy:")
print(numpy_probabilities)

# Verify against Qiskit
print("\nDo NumPy and Qiskit agree?")
print(np.allclose(numpy_probabilities, state.probabilities()))

# Verify normalisation
print("\nTotal probability:")
print(np.sum(numpy_probabilities))

# Circuit A: (|00> + i|11>) / sqrt(2)
qc_a = QuantumCircuit(2)
qc_a.h(0)
qc_a.s(0)
qc_a.cx(0, 1)

# Circuit B: (|00> - |11>) / sqrt(2)
qc_b = QuantumCircuit(2)
qc_b.h(0)
qc_b.cx(0, 1)
qc_b.z(0)

# Inspect both states
state_a = Statevector.from_instruction(qc_a)
state_b = Statevector.from_instruction(qc_b)

print("\nOriginal probabilities:")
print("Circuit A:", state_a.probabilities())
print("Circuit B:", state_b.probabilities())

# Apply Hadamard to both qubits
qc_a.h(0)
qc_a.h(1)

qc_b.h(0)
qc_b.h(1)

# Inspect the resulting states
final_state_a = Statevector.from_instruction(qc_a)
final_state_b = Statevector.from_instruction(qc_b)

print("\nProbabilities after H on both qubits:")
print("Circuit A:", final_state_a.probabilities())
print("Circuit B:", final_state_b.probabilities())

