import numpy as np


state_zero = np.array([1, 0], dtype=complex)
state_one = np.array([0, 1], dtype=complex)
state_plus = np.array([1/np.sqrt(2), 1/np.sqrt(2)], dtype=complex)
state_minus = np.array([1/np.sqrt(2), -1/np.sqrt(2)], dtype=complex)
state1 = np.array(
    [np.sqrt(0.8), np.sqrt(0.2)],
    dtype=complex
)

def get_probabilities(state):
    probabilities = np.abs(state) ** 2
    return probabilities


def get_outcome(probabilities):
    outcome = np.random.choice([0, 1], p=probabilities)
    return outcome


def run_measurements(state, shots):
    p = get_probabilities(state)
    counts = {0:0, 1:0}
    for _ in range(shots):
        result = get_outcome(p)
        counts[result] += 1
    return counts


results = run_measurements(state1, 1000)
print(results)
