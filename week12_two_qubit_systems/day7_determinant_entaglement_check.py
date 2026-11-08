import numpy as np


def separability_test(state):
    a, b, c, d = state
    determinant = a * d - b * c

    return np.isclose(determinant, 0)


plus_plus = np.array([0.5, 0.5, 0.5, 0.5])

phi_plus = np.array([
    1 / np.sqrt(2),
    0,
    0,
    1 / np.sqrt(2)
])

assert separability_test(plus_plus)
assert not separability_test(phi_plus)

state_11 = np.array([0, 0, 0, 1])

H = (1 / np.sqrt(2)) * np.array([
    [1, 1],
    [1, -1]
])

double_H = np.kron(H, H)
print(double_H)
print(double_H @ state_11)

"""
Learning: 
When we apply Hadamard to the first qubit only, the second qubit stays unchanged.

H on |00> --> (|00> + |10>) / sqrt(2). 

Here we applied H on the first zero of |00> as we already know H @ state zero is state_plus. Observe the result 
(|00> + |10>) / sqrt(2). It is H @ state_zero with second qubit remaining constant of zero. 

Example 2: 
H on |10> --> (|00> - |10>)/sqrt(2).

Example 3: 
H @ plus kron plus --> H @ (|00> + |01> + |10> + |11>)/2
             --> 1/2 * H @  (|00> + |01> + |10> + |11>)
             --> 1/2 * (H @ |00> + H @ |01> + H @ |10> + H @ |11>)
             --> 1/2 * ( (|00> + |10>) / sqrt(2) + (|01> + |11>) / sqrt(2) + (|00> - |10>)/sqrt(2) + (|01> - |11>)/sqrt(2))
             --> 1/(2 * sqrt(2)) * ( (|00> + |10>) + (|01> + |11>) + (|00> - |10>) + |01> - |11>))
             --> 1/(2 * sqrt(2)) * ( 2 ( |00> + |01> ) )
             --> ( |00> + |01> ) / sqrt(2)

Hadamard on the first quibit of a two qubit state represented by [a, b, c, d] is 
(H kron I)|psi> = 1/sqrt(2) [a+c, b+d, a-c, b-d]

Hadamard on the second quibit of a two qubit state represented by [a, b, c, d] is 
(I kron H)|psi> = 1/sqrt(2) [a+b, a-b, c+d, c-d]

H on first bit of Bell_state --> H @ [1/sqrt(2), 0, 0, 1/sqrt(2)]
    --> 1/sqrt(2) [1/sqrt(2) + 0, 0 + 1/sqrt(2), 1/sqrt(2) - 0, 0 - 1/sqrt(2)]
    --> 1/sqrt(2) [1/sqrt(2), 1/sqrt(2), 1/sqrt(2), -1/sqrt(2)]
    --> 1/2 [1, 1, 1, -1]

H on first bit of Bell_state --> H @ [1/sqrt(2), 0, 0, -1/sqrt(2)]
    --> 1/sqrt(2) [1/sqrt(2)+0, 0-1/sqrt(2), 1/sqrt(2)-0, 0+1/sqrt(2)]
    --> 1/sqrt(2) [1/sqrt(2), -1/sqrt(2), 1/sqrt(2), 1/sqrt(2)]
    --> 1/2 [1, -1, 1, 1]

"""

