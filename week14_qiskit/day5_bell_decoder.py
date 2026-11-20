from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


qc = QuantumCircuit(2, 2)

# preparing Psi- bell state
qc.x(0)
qc.x(1)
qc.h(0)
qc.cx(0, 1)

# Decoding the bell state
qc.cx(0, 1)
qc.h(0)

# Add measurement to the circuit
qc.measure([0, 1], [0, 1])

# Simulate the circuit
simulator = AerSimulator()
job = simulator.run(qc, shots=1000)

result = job.result()
counts = result.get_counts()

assert counts == {'11': 1000}


def bell_state_decoder(bell_state):
    bell_states = [
        'phi_plus',
        'phi_minus',
        'psi_plus',
        'psi_minus'
    ]
    if bell_state in bell_states:
        qc = QuantumCircuit(2, 2)

        # preparing bell state
        if bell_state == 'phi_minus':
            qc.x(0)
        elif bell_state == 'psi_plus':
            qc.x(1)
        elif bell_state == 'psi_minus':
            qc.x(0)
            qc.x(1)

        qc.h(0)
        qc.cx(0, 1)

        # Decoding the bell state
        qc.cx(0, 1)
        qc.h(0)

        qc.measure([0, 1], [0, 1])

        simulator = AerSimulator()
        job = simulator.run(qc, shots=1000)

        result = job.result()
        counts = result.get_counts()

        return counts


states = {
    'phi_plus': {'00': 1000},
    'phi_minus': {'01': 1000},
    'psi_plus': {'10': 1000},
    'psi_minus': {'11': 1000}
}

for state, expected_result in states.items():
    counts = bell_state_decoder(state)
    assert counts == expected_result

assert not bell_state_decoder('invalid_state')

"""
Learning: 

We know H(H(qubit)) returns same qubit. This also works for two qubit circuits. 
Similarly applying CNOT twice will give us back the original circuit. 

To create a bell_state we apply h(0) and then cx(0, 1). To decode this bell_state we need to apply the same gates in 
reverse order i.e, cx(0, 1) first and then h(0). 

Note: When we decode and measure a bell_state it resolves into 00, 01, 10 or 11. The mapping is given below. 
        'phi_plus'  --> 00
        'phi_minus' --> 10
        'psi_plus'  --> 01
        'psi_minus' --> 11

However in qiskit the qubits are displayed in the reverse order, hence the validations above for phi_minus state is 
checking against 01 instead of 10. Same with psi_plus, we validate against 10 instead of 01. 
"""
