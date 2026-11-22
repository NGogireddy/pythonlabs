from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def explore_bell_state(bell_state, shots=1000):
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
    qc.measure([0, 1], [0, 1])

    simulator = AerSimulator()
    job = simulator.run(qc, shots=shots)

    result = job.result()
    counts = result.get_counts()

    return {
        "bell_state": bell_state,
        "measurement_counts": counts
    }


def generate_summary(result):
    if not result:
        raise ValueError("Empty result, no summary produced")
    total_shots = sum(result["measurement_counts"].values())
    if total_shots == 0:
        raise ValueError("Total shots = 0, no summary produced")

    summary = list()
    summary.append(f"Bell State: {result['bell_state']}")
    summary.append(f"Total count:  {total_shots}")
    for outcome, count in result["measurement_counts"].items():
        if count<0:
            raise ValueError("Invalid shot count, no summary generated")
        percentage = count/total_shots*100
        summary.append(f"Outcome {outcome}: {count} ({percentage:.1f}%)")

    return summary
