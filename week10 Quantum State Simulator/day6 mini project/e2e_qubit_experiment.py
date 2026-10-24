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


# Start with the |0> state
initial_state = state_zero

# Apply the Hadamard gate
final_state = H @ initial_state

# Calculate measurement probabilities
probabilities = get_probabilities(final_state)

print("Final state:", final_state)
print("Probabilities:", probabilities)
print("Total probability:", probabilities.sum())
print("")

# Apply H, then Z, then H
state_after_h = H @ initial_state
state_after_z = Z @ state_after_h
final_state = H @ state_after_z

print("After H:", state_after_h)
print("After Z:", state_after_z)
print("After final H:", final_state)
print("Probabilities:", get_probabilities(final_state))
print("")

"""
The Hadamard gate transforms the amplitudes so their relative signs determine whether they reinforce or cancel.
"""

"""
Experiment2 Result: HZH=X
"""

# Circuit A: X first, then Z
state_a = Z @ X @ state_zero

# Circuit B: Z first, then X
state_b = X @ Z @ state_zero

print("Circuit A state:", state_a)
print("Circuit B state:", state_b)

print("Circuit A probabilities:", get_probabilities(state_a))
print("Circuit B probabilities:", get_probabilities(state_b))

print(
    "Same measurement probabilities:",
    np.allclose(get_probabilities(state_a),
                get_probabilities(state_b))
)
print("")

state_c = Z @ X @ state_plus
state_d = X @ Z @ state_plus

print("Circuit C state:", state_c)
print("Circuit D state:", state_d)

print("Circuit C probabilities:", get_probabilities(state_c))
print("Circuit D probabilities:", get_probabilities(state_d))

print(
    "Same measurement probabilities:",
    np.allclose(get_probabilities(state_c),
                get_probabilities(state_d))
)

final_c = H @ state_c
final_d = H @ state_d

print("Circuit H @ C:", final_c)
print("Circuit H @ D:", final_d)
print("After H, C:", get_probabilities(final_c))
print("After H, D:", get_probabilities(final_d))

"""
Experiment2 result: XZ = -ZX
"""

"""
Learning: 
Identical measurement probabilities in the computational basis alone don't establish that two arbitrary quantum states 
are physically equivalent. Here, equivalence follows because one vector is exactly a global phase multiple of the other.
"""
