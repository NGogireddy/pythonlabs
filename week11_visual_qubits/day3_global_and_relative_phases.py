import numpy as np

H = (1 / np.sqrt(2)) * np.array([
    [1, 1],
    [1, -1]
])

plus = (1 / np.sqrt(2)) * np.array([1, 1])
minus_plus = -plus


def apply_hadamard(state):
    return H @ state


def get_probabilities(state):
    return np.abs(state)**2


after_hadamard_plus = apply_hadamard(plus)
after_hadamard_minus_plus = apply_hadamard(minus_plus)

print("H|+>:", after_hadamard_plus)
print("H(-|+>):", after_hadamard_minus_plus)

probabilities_a = get_probabilities(after_hadamard_plus)
probabilities_b = get_probabilities(after_hadamard_minus_plus)
print("Probability of H|+> ", probabilities_a)
print("Probability of H(-|+>)", probabilities_b)

assert np.allclose(probabilities_a, probabilities_b)

"""
Learning: 
For a state the global phase of it is the same point on the bloch sphere. This is the reason applying transformations or
gates on it will give the same result with a phase difference. The measurement probabilities are same though. 
The probabilities of both the states are the same for this reason.  

The relative phase of the state will have a different state vector compared to the original vector. The probability 
remains same for both the vectors as the amplitude is same. However applying the Hadamard gate on both these states 
will result in different outcomes. 
"""

"""
## Week 11, Day 3 — Global Phase vs Relative Phase

### Global phase
A global phase multiplies every amplitude in a quantum state by the same complex phase factor. States differing only by 
global phase represent the same physical state and occupy the same point on the Bloch sphere.

Applying the same quantum gate preserves this global-phase relationship. The resulting state vectors may differ by that 
phase factor, but their physical measurement predictions remain identical.

### Relative phase
Relative phase describes the phase relationship between amplitudes in a quantum state. Changing it can produce a 
physically different state, even when the initial computational-basis measurement probabilities are the same.

For example, |+⟩ and |−⟩ both have probabilities [0.5, 0.5], but applying Hadamard produces |0⟩ and |1⟩ respectively. 
The relative sign changes how amplitudes combine, allowing the difference to be revealed through interference.

### Key takeaway
Global phase does not change physical predictions. Relative phase can affect measurement probabilities after an 
appropriate gate or change of measurement basis.
"""