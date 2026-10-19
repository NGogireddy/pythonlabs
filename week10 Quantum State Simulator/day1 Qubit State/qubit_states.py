import numpy as np

state1 = np.array([1, 0], dtype=complex)

print(state1)
print(state1.dtype)

state0 = np.array([0, 1], dtype=complex)

print(state0)
print(state0.dtype)


def squared_magnitudes(state):
    """
    Magnitude is the absolute of the amplitude of alpha (0) and beta (1) states the qubit could be in.
    Amplitudes could be complex, not just real numbers. They are not the probabilities.
    :param state:
    :return:
    """
    return np.abs(state)**2


squared_magnitude_state0 = squared_magnitudes(state0)
squared_magnitude_state1 = squared_magnitudes(state1)

"""
For a normalized qubit state, the probabilities are calculated by taking the squared magnitude of each amplitude
"""

state2 = np.array([1 / np.sqrt(2), 1 / np.sqrt(2)], dtype=complex)
print(squared_magnitudes(state2))


def measurement_probabilities(state):
    """
    Returns the probabilities of a normalized quibit. It is same as the above, but with easily understandable variables.
    :param state:
    :return:
    """
    magnitudes = np.abs(state)
    probabilities = magnitudes ** 2
    return probabilities


def is_normalized(state):
    probabilities = np.abs(state) ** 2
    return np.isclose(probabilities.sum(), 1)


state_a = np.array([1, 0], dtype=complex)
state_b = np.array([1 / np.sqrt(2), 1 / np.sqrt(2)], dtype=complex)
state_c = np.array([1, 1], dtype=complex)

print(is_normalized(state_a))
print(is_normalized(state_b))
print(is_normalized(state_c))

"""
Reflection: 

My understanding about qubit's amplitude, magnitude and probabilities is mentioned in the function docstrings above. 

Do the probabilities sum to 1 for a normalized state?
Yes for a normalized qubit state the probabilities will sum to 1. 

Can two states have the same measurement probabilities but different complex amplitudes?
Yes, two states can have the same measurement probabilities but different complex amplitudes. eg [1, 0], [1j, 0]

"""
