import numpy as np


phi_plus = np.array([1/np.sqrt(2), 0, 0, 1/np.sqrt(2)])
phi_minus = np.array([1/np.sqrt(2), 0, 0, -1/np.sqrt(2)])
psi_plus = np.array([0, 1/np.sqrt(2), 1/np.sqrt(2), 0])
psi_minus = np.array([0, 1/np.sqrt(2), -1/np.sqrt(2), 0])

"""
There are Four different bell states. 
phi_plus --> Positive relative phase between |00⟩ and |11⟩
phi_minus --> Negative relative phase between |00⟩ and |11⟩
psi_plus --> Positive relative phase between |01⟩ and |10⟩
psi_minus --> Negative relative phase between |01⟩ and |10⟩

The relative phase is physically meaningful, even though it is invisible in these particular measurement probabilities.

"""


def get_probabilities(state):
    return np.abs(state)**2


def separability_test(state):
    a, b, c, d = state
    determinant = a * d - b * c
    print(f"Determinant of {state}: {determinant}")
    return np.isclose(determinant, 0)


phi_plus_probabilities = get_probabilities(phi_plus)
phi_minus_probabilities = get_probabilities(phi_minus)
psi_plus_probabilities = get_probabilities(psi_plus)
psi_minus_probabilities = get_probabilities(psi_minus)

assert np.isclose(np.sum(phi_plus_probabilities), 1)
assert np.isclose(np.sum(phi_minus_probabilities), 1)
assert np.isclose(np.sum(psi_plus_probabilities), 1)
assert np.isclose(np.sum(psi_minus_probabilities), 1)

assert np.allclose(phi_plus_probabilities, phi_minus_probabilities)
assert np.allclose(psi_plus_probabilities, psi_minus_probabilities)

assert not separability_test(phi_plus)
assert not separability_test(phi_minus)
assert not separability_test(psi_plus)
assert not separability_test(psi_minus)
