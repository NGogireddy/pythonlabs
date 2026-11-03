import numpy as np

plus_state = np.array([
    1 / np.sqrt(2),
    1 / np.sqrt(2)
])

# Combine two plus states
two_qubit_state = np.kron(plus_state, plus_state)

# Calculate probabilities
probabilities = np.abs(two_qubit_state) ** 2

# Check normalization
assert np.isclose(np.sum(probabilities), 1.)

print(two_qubit_state)
print(probabilities)
print("")

"""
Learning:
1. How tensor products combine individual qubit states.
    It is similar to the cartesian product of two sets. 
     
2. Why the order of np.kron(A, B) matters.
    When A and B are not same the order of kron will give different outcomes. 
    
3. How to construct two-qubit superposition states.
    By applying the kron on the individual qubits. 
    
4. How to calculate measurement probabilities for two qubits.
    Measurement probabilities of two qubits is similar to the one qubit calculation. It is square of the amplitude. 
    
5. The difference between separable and entangled states.
    Separable states are the states that could be represented using tensor product of two individual qubits.
    Entangled states cannot be represented using tensor product of two individual qubits.
      
6. Why a Bell state cannot be represented as a tensor product of two individual pure-qubit states.
    Bell state is an entangled state and hence cannot be represented as tensor product of two individual qubits. 
    
"""

H = (1 / np.sqrt(2)) * np.array([
    [1, 1],
    [1, -1]
])

I = np.eye(2)

# Hadamard on first qubit, identity on second
H_first = np.kron(H, I)

# Initial two-qubit state |00>
state_00 = np.array([1, 0, 0, 0])

# Apply the gate
new_state = H_first @ state_00

print(new_state)

H_second = np.kron(I, H)
result = H_second @ state_00
print(result)

probabilities = np.abs(result) ** 2
print(probabilities)
