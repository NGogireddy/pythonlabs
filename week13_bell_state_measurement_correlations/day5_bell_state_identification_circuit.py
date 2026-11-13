import numpy as np

CNOT = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
])

H = (1 / np.sqrt(2)) * np.array([
    [1, 1],
    [1, -1]
])

I = np.eye(2)

H_first = np.kron(H, I)
bell_decoder = H_first @ CNOT

phi_plus = np.array([1/np.sqrt(2), 0, 0, 1/np.sqrt(2)])
phi_minus = np.array([1/np.sqrt(2), 0, 0, -1/np.sqrt(2)])
psi_plus = np.array([0, 1/np.sqrt(2), 1/np.sqrt(2), 0])
psi_minus = np.array([0, 1/np.sqrt(2), -1/np.sqrt(2), 0])

phi_plus_out = bell_decoder @ phi_plus
phi_minus_out = bell_decoder @ phi_minus
psi_plus_out = bell_decoder @ psi_plus
psi_minus_out = bell_decoder @ psi_minus


def get_probabilities(state):
    return np.abs(state)**2


phi_plus_out_probability = get_probabilities(phi_plus_out)
phi_minus_out_probability = get_probabilities(phi_minus_out)
psi_plus_out_probability = get_probabilities(psi_plus_out)
psi_minus_out_probability = get_probabilities(psi_minus_out)

print(phi_plus_out_probability)
print(phi_minus_out_probability)
print(psi_plus_out_probability)
print(psi_minus_out_probability)

assert np.isclose(np.sum(phi_plus_out_probability), 1)
assert np.isclose(np.sum(phi_minus_out_probability), 1)
assert np.isclose(np.sum(psi_plus_out_probability), 1)
assert np.isclose(np.sum(psi_minus_out_probability), 1)

assert np.allclose(phi_plus_out_probability, [1, 0, 0, 0])
assert np.allclose(phi_minus_out_probability, [0, 0, 1, 0])
assert np.allclose(psi_plus_out_probability, [0, 1, 0, 0])
assert np.allclose(psi_minus_out_probability, [0, 0, 0, 1])

"""
Learning: 

In the previous sessions we identified that measuring the two qubits on two different basis can tell us what the  
original qubits are. Today we built a circuit to distinguish them.  
"""
