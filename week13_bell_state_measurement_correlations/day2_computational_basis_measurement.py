import numpy as np


phi_plus = np.array([1/np.sqrt(2), 0, 0, 1/np.sqrt(2)])
phi_minus = np.array([1/np.sqrt(2), 0, 0, -1/np.sqrt(2)])
psi_plus = np.array([0, 1/np.sqrt(2), 1/np.sqrt(2), 0])
psi_minus = np.array([0, 1/np.sqrt(2), -1/np.sqrt(2), 0])

H = (1 / np.sqrt(2)) * np.array([
    [1, 1],
    [1, -1]
])
H_both = np.kron(H, H)

phi_plus_x = H_both @ phi_plus
phi_minus_x = H_both @ phi_minus
psi_plus_x = H_both @ psi_plus
psi_minus_x = H_both @ psi_minus

print(phi_plus_x)
print(phi_minus_x)
print(psi_plus_x)
print(psi_minus_x)
print("")


def get_probabilities(state):
    return np.abs(state)**2


phi_plus_x_probability = get_probabilities(phi_plus_x)
phi_minus_x_probability = get_probabilities(phi_minus_x)
psi_plus_x_probability = get_probabilities(psi_plus_x)
psi_minus_x_probability = get_probabilities(psi_minus_x)

assert np.allclose(phi_plus_x_probability, [0.5, 0, 0, 0.5])
assert np.allclose(phi_minus_x_probability, [0, 0.5, 0.5, 0])
assert np.allclose(psi_plus_x_probability, [0.5, 0, 0, 0.5])
assert np.allclose(psi_minus_x_probability, [0, 0.5, 0.5, 0])

assert np.isclose(np.sum(phi_plus_x_probability), 1)
assert np.isclose(np.sum(phi_minus_x_probability), 1)
assert np.isclose(np.sum(psi_plus_x_probability), 1)
assert np.isclose(np.sum(psi_minus_x_probability), 1)

assert np.allclose(phi_plus_x, phi_plus)
assert np.allclose(phi_minus_x, psi_plus)
assert np.allclose(psi_plus_x, phi_minus)
assert np.allclose(psi_minus, -psi_minus_x)

"""
Learning: 

H_both (np.kron(H, H)) on phi_plus --> phi_plus
H_both on phi_minus --> psi_plus
H_both on psi_plus  --> phi_minus
H_both on psi_minus --> -ve (psi_minus)

Today we established four important concepts:
1. Applying H_both transforms Bell states differently depending on their relative phase.
2. Phi+ remains unchanged.
3. Phi- and Psi+ transform into each other.
4. Psi- acquires a global negative sign, which has no observable physical effect.

The probabilities of the measured outcomes of the original state are based on the basis Z-axis. 
Once Hadamard is applied on both the qubits, the measurement outcomes are on the basis of X-axis.  

Before applying H, measuring in the computational basis is a Z-basis measurement.
Applying H to both qubits and then measuring in the computational basis is equivalent to measuring both 
qubits in the X basis.
"""