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

H_first = np.kron(H, I)     # Extending single gate Hadamard to apply on the first qubit of a two qubit system
H_second = np.kron(I, H)    # Extending single gate Hadamard to apply on the second qubit of a two qubit system

result_first = H_first @ state_00
result_second = H_second @ state_00
print(result_first)
print(result_second)
print("")

result = H_second @ state_01
probabilities = np.abs(result) ** 2
print(result)
print(probabilities)

result1 = H_second @ (H_first @ state_00)
probabilities1 = np.abs(result1) ** 2
print(result1)
print(probabilities1)

assert np.allclose(result1, [0.5, 0.5, 0.5, 0.5])
assert np.allclose(probabilities1, [0.25, 0.25, 0.25, 0.25])

"""
Learning: In a two-qubit system, single-qubit gates are extended using tensor products. The identity matrix allows us 
to apply a gate to one qubit while leaving the other unchanged. Sequential gates are applied through matrix 
multiplication. The resulting state contains amplitudes for all four basis states.
"""
