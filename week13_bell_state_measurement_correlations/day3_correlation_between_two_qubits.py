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

bell_probabilities = {
    "phi_plus": [0.5, 0, 0, 0.5],
    "phi_minus": [0.5, 0, 0, 0.5],
    "psi_plus": [0, 0.5, 0.5, 0],
    "psi_minus": [0, 0.5, 0.5, 0]
}

outcomes = ["00", "01", "10", "11"]


def simulate_measurements(probabilities, shots=1000):
    measurements = np.random.choice(outcomes, size=shots, p=probabilities)
    counts = {'00': 0, '01': 0, '10': 0, '11': 0}
    for result in measurements:
        counts[result] += 1
    equal_count = counts["00"] + counts["11"]
    different_count = counts["01"] + counts["10"]

    equal_percentage = equal_count / shots * 100
    different_percentage = different_count / shots * 100
    return counts, equal_percentage, different_percentage


for state,probabilities in bell_probabilities.items():
    print(state, simulate_measurements(probabilities))
print()

bell_x_probabilities = {
    "phi_plus": [0.5, 0, 0, 0.5],
    "phi_minus": [0, 0.5, 0.5, 0],
    "psi_plus": [0.5, 0, 0, 0.5],
    "psi_minus": [0, 0.5, 0.5, 0]
}

for state,probabilities in bell_x_probabilities.items():
    print(state, simulate_measurements(probabilities))



"""
Learning: 
Each Bell state has a characteristic combination of correlations in the Z and X bases.
Measuring them individually in Z or X bases couldn't distinguish them, but when measured on both bases will give the 
distinction between all the 4 bell states. 

Z basis: distinguishes the Phi family from the Psi family, but cannot distinguish the plus and minus states within 
either family.
X basis: distinguishes the plus and minus states within each family.

Concepts learned
1. Bell states exhibit strong correlations between their two qubits.
2. Phi states produce equal outcomes in the Z basis.
3. Psi states produce different outcomes in the Z basis.
4. In the X basis, relative phase changes the correlation pattern.
5. Combining Z- and X-basis correlations gives each Bell state a unique signature.

"""