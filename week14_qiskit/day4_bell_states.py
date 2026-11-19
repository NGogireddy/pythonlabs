from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Phi+
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])
simulator = AerSimulator()

job = simulator.run(qc, shots=1000)

result = job.result()
counts = result.get_counts()

print("Measurement counts:", counts)
print("Total shots:", sum(counts.values()))
print("Circuit depth:", qc.depth())
print(qc.draw())

# Phi-
qc1 = QuantumCircuit(2, 2)
qc1.h(0)
qc1.z(0)
qc1.cx(0, 1)
qc1.measure([0, 1], [0, 1])

# Psi+
qc2 = QuantumCircuit(2, 2)
qc2.x(1)
qc2.h(0)
qc2.cx(0, 1)
qc2.measure([0, 1], [0, 1])

# Psi-
qc3 = QuantumCircuit(2, 2)
qc3.x(0)
qc3.x(1)
qc3.h(0)
qc3.cx(0, 1)
qc3.measure([0, 1], [0, 1])

simulator = AerSimulator()

job = simulator.run(qc3, shots=1000)
result = job.result()
counts = result.get_counts()

print("Measurement counts:", counts)
print("Circuit depth:", qc3.depth())
print(qc3.draw())


def get_bell_state(initial_circuit):
    initial_circuit.h(0)
    initial_circuit.cx(0, 1)
    initial_circuit.measure([0, 1], [0, 1])
    return initial_circuit


def test_circuit(circuit, shots=1000):
    simulator = AerSimulator()
    job = simulator.run(circuit, shots=shots)
    result = job.result()
    counts = result.get_counts()
    assert sum(counts.values()) == shots

    return counts


phi_plus_circuit = QuantumCircuit(2, 2)
phi_plus = get_bell_state(phi_plus_circuit)
phi_plus_counts = test_circuit(phi_plus)
assert set(phi_plus_counts.keys()) == {'00', '11'}

phi_minus_circuit = QuantumCircuit(2, 2)
phi_minus_circuit.x(0)
phi_minus = get_bell_state(phi_minus_circuit)
phi_minus_counts = test_circuit(phi_minus)
assert set(phi_minus_counts.keys()) == {'00', '11'}

psi_plus_circuit = QuantumCircuit(2, 2)
psi_plus_circuit.x(1)
psi_plus = get_bell_state(psi_plus_circuit)
psi_plus_counts = test_circuit(psi_plus)
assert set(psi_plus_counts.keys()) == {'01', '10'}

psi_minus_circuit = QuantumCircuit(2, 2)
psi_minus_circuit.x(0)
psi_minus_circuit.x(1)
psi_minus = get_bell_state(psi_minus_circuit)
psi_minus_counts = test_circuit(psi_minus)
assert set(psi_minus_counts.keys()) == {'01', '10'}

"""
A quantum measurement does not reveal every property of a quantum state. It reveals information relative to the 
measurement basis. Two different quantum states can produce identical measurement distributions in one basis but 
different distributions in another.
"""
