
import numpy as np

Z = np.array([[1, 0], [0, -1]], dtype=complex)


def apply_pauli_z(state):
    return Z @ state


state_zero = np.array([1, 0], dtype=complex)
state_plus = np.array([1/np.sqrt(2), 1/np.sqrt(2)], dtype=complex)

print("Results after applying Pauli on state_zero and state_plus")
print(apply_pauli_z(state_zero))
print(apply_pauli_z(state_plus))

"""
Prediction of applying Pauli_z: 
On state_zero there is no impact once we apply Pauli Z gate, result will be np.array([1, 0], dtype=complex)
On state_plus the amplitude of 1 state becomes negative i.e np.array([1/np.sqrt(2), -1/np.sqrt(2)], dtype=complex)
"""

H = (1 / np.sqrt(2)) * np.array(
    [[1, 1],
     [1, -1]],
    dtype=complex
)


def apply_hadamard(state):
    return H @ state


state_one = np.array([0, 1], dtype=complex)

print("Results after applying Hadamard on state_zero and state_one and applying hadamard twice on zero and one")
print(apply_hadamard(state_zero))
print(apply_hadamard(state_one))
print(apply_hadamard(apply_hadamard(state_zero)))
print(apply_hadamard(apply_hadamard(state_one)))

"""
Prediction of applying hadamard: 
On state_zero there will be a change in the state and it becomes 1/np.sqrt(2) * np.array([1, 1], dtype=complex) having 
same amplitude for both 0 and 1. 
On state_one the amplitude of 0 and 1 states will be same but for state 1 it will carry a negative sign. result will be 
1/np.sqrt(2) * np.array([1, -1], dtype=complex)
When hadamard is applied twice to state 0 then the amplitude of state zero doubles but state one will be zero.  
"""


"""
Correction: 
Once hadamard gate is applied to state zero you have 1/sqrt(2)*[1, 1] not just [1, 1]. Apply the hadamard gate again and
your will get state zero again. 
"""

state = state_zero

result = apply_hadamard(state)
result = apply_pauli_z(result)
result = apply_hadamard(result)

print("Results after applying Hadamard, Pauli Z and Hadamard on state_zero")
print(result)
print(np.sum(np.abs(result) ** 2))


"""
Prediction: 
\(|0\rangle\) becomes \(|1\rangle\). 
"""


"""
Reflection: 

- Which gate changes the measurement probabilities for your chosen input?
    Pauli z gate does not change the measurement probabilities but the Hadamard changes it. 
     
- Can a gate change the state without changing the probabilities of measuring 0 or 1 in this basis?
    Pauli Z changes the amplitude of state 1, not the probability. for state 0 the amplitude and probability remains same
    Hadamard gates changes the state and amplitude/individual probabilities of measuring 0 or 1. 

"""

"""
Questions: 

state_zero = np.array([1, 0], dtype=complex)
state_one  = np.array([0, 1], dtype=complex)
state_plus  = np.array([1/np.sqrt(2), 1/np.sqrt(2)], dtype=complex)
state_minus = np.array([1/np.sqrt(2), -1/np.sqrt(2)], dtype=complex)

What is the significance of the plus and minus states in quantum computing?

"""

state_minus = np.array([1/np.sqrt(2), -1/np.sqrt(2)], dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)


def apply_pauli_x(state):
    return X @ state


print("X on plus:", apply_pauli_x(state_plus))
print("X on minus:", apply_pauli_x(state_minus))

print("H on plus:", apply_hadamard(state_plus))
print("H on minus:", apply_hadamard(state_minus))
