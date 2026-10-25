import numpy as np


state_zero = np.array([1, 0], dtype=complex)
state_one = np.array([0, 1], dtype=complex)
state_plus = np.array([1/np.sqrt(2), 1/np.sqrt(2)], dtype=complex)
state_minus = np.array([1/np.sqrt(2), -1/np.sqrt(2)], dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
H = (1 / np.sqrt(2)) * np.array(
    [[1, 1],
     [1, -1]],
    dtype=complex
)


def get_probabilities(state):
    """
    Return the probabilities of the state
    :param state:
    :return:
    """
    return np.abs(state)**2


def apply_hadamard(state):
    return H @ state


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


state_a = Z @ X @ state_plus
state_b = X @ Z @ state_plus

print("Circuit A:", state_a)
print("Circuit B:", state_b)

print("A probabilities:", get_probabilities(state_a))
print("B probabilities:", get_probabilities(state_b))

# Apply H to both outputs
final_a = H @ state_a
final_b = H @ state_b

print("A after H:", final_a)
print("B after H:", final_b)

print("A final probabilities:", get_probabilities(final_a))
print("B final probabilities:", get_probabilities(final_b))
print("")

"""
Learning: 
Applying the same quantum gate to two states that differ only by a global phase preserves that global phase relationship
"""

negative_plus = -state_plus

states = {
    "plus": state_plus,
    "negative_plus": negative_plus,
    "minus": state_minus,
}

for name, state in states.items():
    print(name, ":", state)
    print("Probabilities:", get_probabilities(state))
print("")

for name, state in states.items():
    transformed = H @ state

    print(name)
    print("After H:", transformed)
    print("Probabilities:", get_probabilities(transformed))
print("")

"""
Learning: 
Measurement probabilities alone do not fully describe a quantum state; relative phase matters when states are transformed
"""

plus_state = np.array([1 / np.sqrt(2), 1 / np.sqrt(2)])

# Experiment A
probabilities_a = get_probabilities(plus_state)

# Experiment B
state_b = apply_hadamard(plus_state)
probabilities_b = get_probabilities(state_b)

print("A — Direct measurement:", probabilities_a)
print("B — After Hadamard:", probabilities_b)
print("")

counts_a = run_measurements(plus_state, 1000)
counts_b = run_measurements(state_b, 1000)

print("Experiment A:", counts_a)
print("Experiment B:", counts_b)