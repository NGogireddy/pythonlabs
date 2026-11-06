import numpy as np

state_00 = np.array([1, 0, 0, 0])
state_01 = np.array([0, 1, 0, 0])
state_10 = np.array([0, 0, 1, 0])
state_11 = np.array([0, 0, 0, 1])

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

# Step 1: Apply Hadamard
state_after_h = H_first @ state_00

# Step 2: Apply CNOT
bell_state = CNOT @ state_after_h

print(bell_state)
print(np.abs(bell_state) ** 2)

assert (np.sum(np.abs(bell_state) ** 2), 1)

"""
Learning: 
A Bell state can be prepared by applying Hadamard to the first qubit of (|00>), followed by CNOT with the first qubit as 
control and the second as target. The resulting state is ((|00>+|11>)/sqrt{2}), a maximally entangled two-qubit state.
"""
