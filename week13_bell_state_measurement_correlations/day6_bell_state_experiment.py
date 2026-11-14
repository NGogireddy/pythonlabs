import numpy as np


def apply_gate(state, gate):
    return gate @ state


zero_state = np.array([1, 0])
X = np.array([
    [0, 1],
    [1, 0]
])

X_on_zero = apply_gate(zero_state, X)
print(X_on_zero)

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

decoded_phi_plus = apply_gate(phi_plus, bell_decoder)
print(decoded_phi_plus)


def get_probabilities(state):
    return np.abs(state)**2


def simulate_measurements(state, shots=1000):
    # Calculate probabilities from state
    probabilities = get_probabilities(state)

    # Define measurement outcomes
    outcomes = ["00", "01", "10", "11"]

    # Generate random measurement results
    measurements = np.random.choice(
        outcomes,
        size=shots,
        p=probabilities
    )

    # Return measurements
    return measurements


measurements = simulate_measurements(phi_plus, shots=1000)

print(measurements[:10])
print(len(measurements))

assert len(measurements) == 1000
assert set(measurements).issubset({"00", "11"})


def count_outcomes(measurements):
    # Initialise counts for all four outcomes
    counts = {'00':0, '01':0, '10':0, '11':0}

    # Count how many times each outcome appears
    for result in measurements:
        counts[result] += 1

    # Return counts
    return counts


print(count_outcomes(measurements))

sample_measurements = ["00", "11", "00", "00", "11", "11", "00"]

counts = count_outcomes(sample_measurements)

print(counts)

assert counts == {
    "00": 4,
    "01": 0,
    "10": 0,
    "11": 3
}


def calculate_correlation(counts):
    # Calculate total measurements
    n_total = sum(counts.values())
    p_equal, p_diff = 0, 0

    # Calculate equal probability
    if n_total > 0:
        p_equal = (counts['00'] + counts['11']) / n_total

    # Calculate different probability
        p_diff = (counts['01'] + counts['10']) / n_total

    # Return correlation score
    return p_equal - p_diff

neg_counts = {
    "00": 0,
    "01": 4,
    "10": 3,
    "11": 0
}

eq_counts = {
    "00": 4,
    "01": 3,
    "10": 4,
    "11": 3
}

assert np.isclose(calculate_correlation(counts), 1.)
assert np.isclose(calculate_correlation(neg_counts), -1.)
assert np.isclose(calculate_correlation(eq_counts), 0.)


def orchestrate_measurements(state):
    measurements = simulate_measurements(state, shots=1000)
    counts = count_outcomes(measurements)
    correlation = calculate_correlation(counts)
    print("Counts for the given state:", counts)
    print("Correlation for the state:", correlation)


orchestrate_measurements(phi_plus)
