import pytest
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def bell_state_decoder(bell_state, shots=1000):
    bell_states = [
        'phi_plus',
        'phi_minus',
        'psi_plus',
        'psi_minus'
    ]
    if bell_state not in bell_states:
        raise ValueError(f"Unknown Bell state: {bell_state}")

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
    job = simulator.run(qc, shots=shots)

    result = job.result()
    counts = result.get_counts()

    return counts


def test_invalid_bell_state():
    with pytest.raises(ValueError, match="Unknown Bell state"):
        bell_state_decoder("invalid_state")


def test_phi_plus_decoder():
    result = bell_state_decoder('phi_plus', 500)
    assert result == {'00': 500}


def test_all_bell_states():
    states = {
        'phi_plus': {'00': 1000},
        'phi_minus': {'01': 1000},
        'psi_plus': {'10': 1000},
        'psi_minus': {'11': 1000}
    }
    for state, expected_result in states.items():
        counts = bell_state_decoder(state)
        assert counts == expected_result


def test_shot_count():
    shots = 250
    result = bell_state_decoder('psi_minus', shots)
    assert sum(result.values()) == shots
