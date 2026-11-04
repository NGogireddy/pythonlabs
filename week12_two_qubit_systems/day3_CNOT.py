import numpy as np

CNOT = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
])

state_00 = np.array([1, 0, 0, 0])
state_01 = np.array([0, 1, 0, 0])
state_10 = np.array([0, 0, 1, 0])
state_11 = np.array([0, 0, 0, 1])

print(CNOT @ state_00)
print(CNOT @ state_01)
print(CNOT @ state_10)
print(CNOT @ state_11)

print(CNOT @ (CNOT @ state_10))

assert np.array_equal(CNOT @ state_00, state_00)
assert np.array_equal(CNOT @ state_01, state_01)
assert np.array_equal(CNOT @ state_10, state_11)
assert np.array_equal(CNOT @ state_11, state_10)

assert np.array_equal(
    CNOT @ (CNOT @ state_10),
    state_10
)

state = np.array([
    1/np.sqrt(2),
    0,
    1/np.sqrt(2),
    0
])

print(CNOT @ state)

"""
Learning: 
1. CNOT's control and target behaviour.
    CNOT gate is a two qubit gate which works on the two qubits based on the value in the control qubit (first one). 
    If the control qubit (first one) is 0 the target qubit (second one) will not change. 
    If the control qubit (first one) is 1 the target qubit (second one) will flip i.e, if it is zero it changes to one
    and vice-versa.
2. The four basis-state transformations.
    When CNOT is applied on [a, b, c, d] the result will be [a, b, d, c]
    
3. The CNOT matrix in NumPy.
    np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
])
4. Reversibility: applying CNOT twice restores the original state.
    When CNOT is applied twice on a state we get back the original state. CNOT @ CNOT @ state = state or CNOT**2 = I
    
5. Applying CNOT to a superposition.
    CNOT can be applied to any two qubit system even if they are in super position. 
    When applied to a superposition, it transforms every component linearly, potentially creating entanglement.
"""
