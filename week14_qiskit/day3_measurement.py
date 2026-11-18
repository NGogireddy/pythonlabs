import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def calculate_probabilities(counts):
    total_shots = sum(counts.values())
    probabilities = {}
    if total_shots > 0:
        for outcome, count in counts.items():
            probabilities[outcome] = count / total_shots
    return probabilities


test_counts = {'0': 480, '1': 520}
out_probabilities = calculate_probabilities(test_counts)

assert np.isclose(out_probabilities['0'], 0.48)
assert np.isclose(out_probabilities['1'], 0.52)
assert np.isclose(sum(out_probabilities.values()), 1.0)

assert calculate_probabilities({}) == {}

shot_counts = [100, 1000, 10000]
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)
simulator = AerSimulator()

for shots in shot_counts:
    job = simulator.run(qc, shots=shots)
    result = job.result()
    counts = result.get_counts()

    probabilities = calculate_probabilities(counts)

    print(f"\nShots: {shots}")
    print("Counts:", counts)
    print("Experimental probabilities:", probabilities)


def validate_probabilities(probabilities):
    if probabilities:
        total = 0
        for value in probabilities.values():
            if 0 <= value <= 1:
                total += value
            else:
                return False
        if np.isclose(total, 1):
            return True
    return False


assert validate_probabilities({'0': 0.48, '1': 0.52})
assert not validate_probabilities({})
assert not validate_probabilities({'0': 0.9, '1': 0.52})
assert validate_probabilities({'0': 0., '1': 1.})
assert not validate_probabilities({'0': -0.3, '1': 1.3})

"""
Learning:
### Week 14 — Day 3: Measurement and Shot Counts

**Learning summary**

Qiskit Aer returns measurement counts after executing a quantum circuit for a specified number of shots.

The measurement counts can be converted into experimental probabilities:

P_experimental(x)=Count(x)/Total shots

For an ideal Hadamard gate applied to |0>, the theoretical measurement probabilities are:

P(0)=0.5, P(1)=0.5

Experimental probabilities may differ from theoretical probabilities because quantum measurements are probabilistic.
Increasing the number of shots generally improves statistical precision. The standard deviation of the measured 
proportion is:

sigma=sqrt{p(1-p)/(N)} where p is the probability and N is the number of shots. 

For a probability of 0.5:

sigma={0.5}/sqrt{N}

However, a larger number of shots does not guarantee that every individual experiment will be closer to the 
theoretical probability.

**Python concepts practised**

- `sum(counts.values())`
- Dictionary iteration using `items()` and `values()`
- Calculating experimental probabilities
- Boolean validation functions
- `np.isclose()` for floating-point comparisons
- Assertions for normal and edge-case testing

**Key takeaway**

Theoretical probabilities describe expected quantum measurement behaviour. Qiskit Aer simulates repeated measurements 
and returns sampled counts, allowing us to compare experimental results with theoretical predictions.

"""
