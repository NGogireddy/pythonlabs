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

"""
Correlation E = P(Equal) - P(Different)
e.g: E Phi+ on Z basis = P(Equal) i.e 1 - P(Different) i.e 0 = 1
E Psi+ on Z basis = 0 - 1 = -1 

Correlation scores for all four Bell states.

- Phi+ → E_Z=+1, E_X=+1
- Phi− → E_Z=+1, E_X=-1
- Psi+ → E_Z=-1, E_X=+1
- Psi- → E_Z=-1, E_X=-1

"""


def calculate_correlation(counts):
    # Calculate total number of measurements
    n_total = sum(counts.values())

    if n_total == 0:
        raise ValueError("Cannot calculate correlation with zero measurements")

    # Calculate probability of equal outcomes
    p_equal = (counts["00"] + counts["11"]) / n_total

    # Calculate probability of different outcomes
    p_different = (counts["01"] + counts["10"]) / n_total

    # Calculate and return correlation score
    return p_equal - p_different


exp_counts1 = {
    "00": 520,
    "01": 0,
    "10": 0,
    "11": 480
}
print(f"Correlation of experiment1 is: {calculate_correlation(exp_counts1)}")

exp_counts2 = {
    "00": 0,
    "01": 498,
    "10": 502,
    "11": 0
}
print(f"Correlation of experiment2 is: {calculate_correlation(exp_counts2)}")

exp_counts3 = {
    "00": 45,
    "01": 498,
    "10": 502,
    "11": 55
}
print(f"Correlation of experiment3 is: {calculate_correlation(exp_counts3)}")

"""
Correlation of experiment3 is: -0.8181818181818181

Learning: 

The negative score tells us that different outcomes are more frequent than equal outcomes. Its magnitude, 
approximately 0.82, indicates a fairly strong bias towards different outcomes.

The two qubits show a fairly strong anti-correlation in this measurement basis.

Why?
- A score near +1 means outcomes tend to be equal.
- A score near −1 means outcomes tend to be different.
- A score near 0 means there is little bias towards either equal or different outcomes.
So −0.82 is not weak correlation. It is strong anti-correlation.

"""

"""
Correlation measures how strongly measurement outcomes are related in a chosen basis. Positive correlation favours equal
outcomes; negative correlation favours different outcomes. Measurements in multiple bases provide more information about
the underlying quantum state. However, correlation alone does not establish entanglement.
"""
