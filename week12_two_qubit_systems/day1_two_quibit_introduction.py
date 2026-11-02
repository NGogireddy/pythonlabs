import numpy as np

plus_state = np.array([1/np.sqrt(2), 1/np.sqrt(2)])
one_state = np.array([0, 1])

two_qubit_state = np.kron(plus_state, one_state)

probabilities = np.abs(two_qubit_state)**2

print(two_qubit_state)
print(probabilities)
print(probabilities.sum())

assert np.isclose(np.sum(probabilities), 1.)

zero_state = np.array([1, 0])

state = np.kron(plus_state, zero_state)

print(state)    # [[1/np.sqrt(2), 0, [1/np.sqrt(2), 0]

"""
Notes: 
# Quantum Computing Notes — Week 12, Day 1

In a two qubit system, there are 4 outcomes i.e, 00, 01, 10, 11. These are the 4 states and each state has its own 
amplitude. It is easy to remember the squence as they mimic the binary numbers. First state is 00, second state is 01, 
third state is 10 and fourth state is 11. In the given question the amplitude is 1 for the thrid state which is 10. 

The concept of measurement probabilities is same as single qubit system which is square of the amplitudes and here all 
amplitudes are zero except for third state which is 1. 

When we add up the measurement probabilities of all the states it is giving 1, hence it is normalized. 

AI notes below: 

### 1. From one qubit to two qubits

A single qubit has two computational-basis states: [0, 1]
A two-qubit system has four computational-basis states: [00, 01, 10, 11]

For this course, we use the following ordering:

| Basis state | State vector |
|---|---|
| \(|00\) | \([1,0,0,0]\) |
| \(|01\) | \([0,1,0,0]\) |
| \(|10\) | \([0,0,1,0]\) |
| \(|11\) | \([0,0,0,1]\) |

**Convention:** The first bit represents qubit A; the second bit represents qubit B.

Each additional qubit doubles the number of computational-basis states:

- 1 qubit: 2 amplitudes
- 2 qubits: 4 amplitudes
- 3 qubits: 8 amplitudes
- n qubits: \(2^n\) amplitudes

### 2. Measurement probabilities and normalization

The probability of measuring a particular basis state is the squared magnitude of its amplitude: [P_i=|a_i|^2]

For a valid normalized quantum state:

[
|a_{00}|^2+|a_{01}|^2+|a_{10}|^2+|a_{11}|^2=1
]


### 5. The Kronecker product — `np.kron()`

The Kronecker product combines vectors or matrices into a larger vector or matrix.

For vectors:

[
A=[1,2], B=[3,4]
]

[
A kron B=[3,4,6,8]
]

The operation multiplies each element of A by the entire array B, then joins the resulting blocks.

Python example:

```python
import numpy as np

A = np.array([1, 2])
B = np.array([3, 4])

print(np.kron(A, B))
# [3 4 6 8]
```

### 6. Using `np.kron()` to combine qubit states

```python
import numpy as np

plus_state = np.array([
    1/np.sqrt(2),
    1/np.sqrt(2)
])

one_state = np.array([0, 1])

two_qubit_state = np.kron(plus_state, one_state)

probabilities = np.abs(two_qubit_state)**2

print(two_qubit_state)
# [0.         0.70710678 0.         0.70710678]

print(probabilities)
# [0.  0.5 0.  0.5]

print(probabilities.sum())
# Approximately 1.0
```

### 4. Important distinctions

| Operation | Purpose |
|---|---|
| `np.kron(A, B)` | Combines vectors or matrices using the Kronecker product |
| `A @ B` | Performs matrix multiplication |
| `np.abs(state)**2` | Calculates squared magnitudes of amplitudes |
| `np.sum(probabilities)` | Checks the total probability |

For matrices, if A has shape (m X n) and B has shape (p X q), their Kronecker product has shape: [(mp) X (nq)]

For example, two 2 × 2 matrices produce a 4 × 4 matrix.

"""