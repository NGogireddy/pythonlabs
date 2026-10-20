import numpy as np

X = np.array([
    [0, 1],
    [1, 0]
], dtype=complex)

state = np.array([1, 0], dtype=complex)

print(f'Original State: {state}')
new_state = X @ state
print(f'Pauli X applied State: {new_state}')

next_state = X @ new_state
print(f'Pauli X applied again: {next_state}')


def apply_pauli_x(state):
    # Multiply the Pauli-X matrix by the state vector
    # Return the transformed state
    new_state = X @ state
    return new_state


state_zero = np.array([1, 0], dtype=complex)
state_plus = np.array(
    [1 / np.sqrt(2), 1 / np.sqrt(2)],
    dtype=complex
)

print(apply_pauli_x(state_zero))
print(apply_pauli_x(state_plus))

"""
Pauli X gate is the equivalent of the NOT gate. It flips the qubit upside down i.e, once the gate is applied the chances
of measures |0> after applying the gate will be the chances of measuring |1> and vice versa
"""

complex_state = np.array(
    [1/np.sqrt(2), 1j/np.sqrt(2)],
    dtype=complex
)
print(f'A complex state: {complex_state}')
print(f'Pauli X on complex state: {apply_pauli_x(complex_state)}')
print(f'Pauli X twice on complex: {apply_pauli_x(apply_pauli_x(complex_state))}')

transformed = apply_pauli_x(complex_state)
print("Sum of the probabilities before and after applying the Pauli X gate")
print(np.sum(np.abs(complex_state) ** 2))
print(np.sum(np.abs(transformed) ** 2))


one_state = np.array([np.sqrt(0.8), np.sqrt(0.2)])
once = apply_pauli_x(one_state)
twice = apply_pauli_x(once)

print("Validating X**2 == I")
# Applying X twice should restore the original state
print(np.allclose(twice, one_state))

# The probabilities should swap after one application
print(np.abs(one_state) ** 2)
print(np.abs(once) ** 2)


def pauli_test1(state=None):
    """
    validates X**2 == I
    :param state:
    :return:
    """
    if state is None:
        state = np.array([1, 0], dtype=complex)
    transformed = apply_pauli_x(state)
    second_transform = apply_pauli_x(transformed)
    return np.allclose(state, second_transform)


def pauli_test2(state=None):
    """
    probabilities of each state are swapped after applying the X gate.
    :param state:
    :return:
    """
    if state is None:
        state = np.array([1, 0], dtype=complex)
    transformed = apply_pauli_x(state)
    state_probabilities = np.abs(state)**2
    transformed_probabilities = np.abs(transformed)**2
    return np.isclose(state_probabilities[0], transformed_probabilities[1]) and \
           np.isclose(state_probabilities[1], transformed_probabilities[0])


def pauli_test3(state=None):
    """
    sum of the probabilities of the normalized state after applying the X gate still remains as 1.
    If the state is not normalized then validates that the sum of the magnitudes remain same.
    :param state:
    :return:
    """
    if state is None:
        state = np.array([1, 0], dtype=complex)
    transformed = apply_pauli_x(state)
    return np.isclose(np.sum(np.abs(transformed)**2), np.sum(np.abs(state)**2))


state_zero = np.array([1, 0], dtype=complex)
state_plus = np.array([1 / np.sqrt(2), 1 / np.sqrt(2)], dtype=complex)
complex_state = np.array([1 / np.sqrt(2), 1j / np.sqrt(2)], dtype=complex)

print("Validating the pauli X properties")

for state in [state_zero, state_plus, complex_state]:
    print(
        pauli_test1(state),
        pauli_test2(state),
        pauli_test3(state),
    )
