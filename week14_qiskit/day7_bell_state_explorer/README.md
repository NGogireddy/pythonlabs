## Week 14 — From NumPy Quantum Circuits to Qiskit

### Overview

This week focused on transitioning from manually implementing quantum operations using NumPy to constructing and simulating quantum circuits using Qiskit.

The objective was to understand how quantum states, gates and measurements are represented and executed through a quantum computing SDK.

### Learning objectives

- Understand the Qiskit `QuantumCircuit` class and circuit instructions.
- Construct quantum circuits using Hadamard, Pauli-X and CNOT gates.
- Simulate quantum circuits using Qiskit Aer.
- Understand measurement outcomes, shot counts and experimental probabilities.
- Prepare and measure all four Bell states.
- Implement a Bell-state decoder.
- Apply Python engineering practices, including input validation, reusable functions and pytest.

### Bell-state exploration

The capstone brings together the concepts covered during the week.

It prepares and simulates the four Bell states:

| Bell state | Expected measurement outcomes |
|---|---|
| Phi+ | `00`, `11` |
| Phi− | `00`, `11` |
| Psi+ | `01`, `10` |
| Psi− | `01`, `10` |

Each state produces two possible computational-basis measurement outcomes with approximately equal probabilities (50% each).

The implementation supports configurable shot counts and returns structured results containing the Bell-state name and measurement counts.

### Result summary

A separate summary function processes the simulation results and generates a readable report containing:

- Bell-state name
- Total measurement count
- Individual measurement outcomes
- Number of occurrences for each outcome
- Percentage of each outcome

This separates quantum circuit execution from result presentation.

### Testing and engineering practices

Pytest was used to validate the implementation.

The test suite includes:

- Parameterised tests covering all four Bell states.
- Different shot counts to verify configurable simulation.
- Validation of expected measurement outcomes.
- Input validation for unsupported Bell-state names.
- Summary generation for valid results.
- Handling of empty results, zero totals and negative measurement counts.

### Key takeaway

Week 14 marked the transition from manually implementing quantum state transformations with NumPy to building and testing quantum circuits using Qiskit.

It also reinforced an important software engineering principle: quantum applications need both correct quantum operations and reliable Python interfaces, validation and tests.