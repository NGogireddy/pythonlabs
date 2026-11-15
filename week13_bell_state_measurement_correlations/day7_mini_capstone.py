import numpy as np

bell_states = {
    "phi_plus":  [1/np.sqrt(2), 0, 0, 1/np.sqrt(2)],
    "phi_minus": [1/np.sqrt(2), 0, 0, -1/np.sqrt(2)],
    "psi_plus":  [0, 1/np.sqrt(2), 1/np.sqrt(2), 0],
    "psi_minus": [0, 1/np.sqrt(2), -1/np.sqrt(2), 0]
}

I = np.eye(2)
H = (1 / np.sqrt(2)) * np.array([
    [1, 1],
    [1, -1]
])


CNOT = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
])

H_first = np.kron(H, I)

bell_decoder = H_first @ CNOT

expected_probabilities = {
    "phi_plus":  [1, 0, 0, 0],
    "phi_minus":  [0, 0, 1, 0],
    "psi_plus":  [0, 1, 0, 0],
    "psi_minus":  [0, 0, 0, 1]
}


def get_probabilities(state):
    return np.abs(state)**2


def separability_test(state):
    a, b, c, d = state
    determinant = a * d - b * c

    return np.isclose(determinant, 0)


def calculate_correlation(counts):
    n_total = sum(counts.values())
    if n_total == 0:
        raise ValueError("Cannot calculate correlation with zero measurements")

    p_equal = (counts["00"] + counts["11"]) / n_total
    p_different = (counts["01"] + counts["10"]) / n_total

    # Calculate and return correlation score
    return p_equal - p_different


def apply_gate(state, gate):
    return gate @ state


def get_determinant(state):
    a, b, c, d = state
    return a*d-b*c


def is_entangled(state):
    return not np.isclose(get_determinant(state), 0)


def simulate_measurements(state, shots=1000):
    probabilities = get_probabilities(state)
    outcomes = ["00", "01", "10", "11"]

    # Generate random measurement results
    measurements = np.random.choice(
        outcomes,
        size=shots,
        p=probabilities
    )
    return measurements


def count_outcomes(measurements):
    counts = {'00':0, '01':0, '10':0, '11':0}
    for result in measurements:
        counts[result] += 1

    return counts


for name, state in bell_states.items():

    probabilities = get_probabilities(state)
    entangled = not separability_test(state)
    assert np.isclose(np.sum(probabilities), 1.0)

    print(name)
    print("Probabilities:", probabilities)
    print("Entangled:", entangled)

H = (1 / np.sqrt(2)) * np.array([
    [1, 1],
    [1, -1]
])

H_both = np.kron(H, H)

for name, state in bell_states.items():
    Z_probabilities = get_probabilities(state)
    Z_measurements = simulate_measurements(state)
    Z_outcomes = count_outcomes(Z_measurements)
    Z_correlation = calculate_correlation(Z_outcomes)
    X_state = apply_gate(state, H_both)
    X_probabilities = get_probabilities(X_state)
    X_measurements = simulate_measurements(X_state)
    X_outcomes = count_outcomes(X_measurements)
    X_correlation = calculate_correlation(X_outcomes)

    print(name)
    print("X_state:", X_state)
    print("Z_Probabilities:", Z_probabilities)
    print("X_Probabilities:", X_probabilities)
    print("Z basis entangled:", is_entangled(state))
    print("X basis entangled:", is_entangled(X_state))
    print("Z basis correlation score:", Z_correlation)
    print("X basis correlation score:", X_correlation)
    print("")

for name, state in bell_states.items():
    bell_decoded_state = apply_gate(state, bell_decoder)
    probabilities = get_probabilities(bell_decoded_state)
    print(name)
    print("Bell Decoded State:", bell_decoded_state)
    print("Outcome probabilities:", probabilities)
    print("")
    assert np.allclose(probabilities, expected_probabilities[name])
    assert np.isclose(np.sum(probabilities), 1.0)
