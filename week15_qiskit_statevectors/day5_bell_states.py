from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc_a = QuantumCircuit(2)

qc_a.x(1)
qc_a.h(0)
qc_a.cx(0, 1)

state_a = Statevector.from_instruction(qc_a)

print("Circuit:")
print(qc_a.draw())

print("\nStatevector:")
print(state_a.data)

print("\nProbabilities:")
print(state_a.probabilities())

qc_b = QuantumCircuit(2)

qc_b.h(0)
qc_b.cx(0, 1)
qc_b.z(0)

state_b = Statevector.from_instruction(qc_b)

print("Statevector:")
print(state_b.data)

print("\nProbabilities:")
print(state_b.probabilities())

qc_c = QuantumCircuit(2)

qc_c.x(1)
qc_c.h(0)
qc_c.cx(0, 1)
qc_c.z(0)

state_c = Statevector.from_instruction(qc_c)

print("Statevector:")
print(state_c.data)

print("\nProbabilities:")
print(state_c.probabilities())


def prepare_bell_state(bell_state):
    bell_states = {'phi_plus', 'phi_minus', 'psi_plus', 'psi_minus'}
    if bell_state not in bell_states:
        raise ValueError("Not a valid bell state to prepare")
    qc = QuantumCircuit(2)

    if bell_state == 'phi_minus':
        qc.x(0)
    elif bell_state == "psi_plus":
        qc.x(1)
    elif bell_state == "psi_minus":
        qc.x(0)
        qc.x(1)
    qc.h(0)
    qc.cx(0, 1)

    return qc


bell_states = ['phi_plus', 'phi_minus', 'psi_plus', 'psi_minus']

for name in bell_states:
    qc = prepare_bell_state(name)
    state = Statevector.from_instruction(qc)

    print(f"\n{name}")
    print(state.data)
    print(state.probabilities())

