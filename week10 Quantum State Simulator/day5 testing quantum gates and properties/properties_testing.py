import numpy as np


def is_normalized(state):
    """
    Returns True if the state is normalized otherwise False
    :param state:
    :return:
    """
    total_probability = np.sum(np.abs(state)**2)
    return np.isclose(total_probability, 1)


state_zero = np.array([1, 0], dtype=complex)
state_one = np.array([0, 1], dtype=complex)
state_plus = np.array([1/np.sqrt(2), 1/np.sqrt(2)], dtype=complex)
state_minus = np.array([1/np.sqrt(2), -1/np.sqrt(2)], dtype=complex)
state_a = np.array([1, 1], dtype=complex)

"""
Prediction:
True: state_zero, state_one, state_plus, state_minus
False: state_a
"""

print(is_normalized(state_zero))
print(is_normalized(state_one))
print(is_normalized(state_plus))
print(is_normalized(state_minus))
print(is_normalized(state_a))
print("")


X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
H = (1 / np.sqrt(2)) * np.array(
    [[1, 1],
     [1, -1]],
    dtype=complex
)

print(np.allclose(X @ X @ state_plus, state_plus))
print(np.allclose(Z @ Z @ state_plus, state_plus))
print(np.allclose(H @ H @ state_plus, state_plus))
print("")

"""
Prediction: All of the three statements return True
"""


def get_probabilities(state):
    """
    Return the probabilities of the state
    :param state:
    :return:
    """
    return np.abs(state)**2


print(np.allclose(get_probabilities(state_zero).sum(), 1))
print(np.allclose(get_probabilities(state_plus).sum(), 1))
print(np.all(get_probabilities(state_plus) >= 0))
print("")

"""
Prediction: All of the three statements return True
"""


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


shots = 1000
counts = run_measurements(state_plus, shots)

observed_probabilities = {
    outcome: count / shots
    for outcome, count in counts.items()
}

print(counts)
print(observed_probabilities)

