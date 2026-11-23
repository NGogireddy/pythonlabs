# Week 15 — Inspecting Quantum States with Qiskit

**Duration:** 7 sessions, approximately 1 hour per day  
**Environment:** Reuse the Week 14 `week14_qiskit` virtual environment unless you choose to create a separate Week 15 folder.  
**Stack:** Python 3.14, Qiskit 2.6.x, Qiskit Aer 0.18.x, NumPy, pytest.

## Why this week matters

In Week 14, you learned to build quantum circuits and observe sampled measurement outcomes using Qiskit Aer. You also prepared and decoded all four Bell states.

This week moves one level deeper: **inspect the quantum state produced by a circuit before measurement**.

You will use Qiskit's `Statevector` representation to examine amplitudes and probabilities, compare Qiskit's results with your NumPy reference implementations, and investigate phase and qubit-ordering conventions. This connects the SDK's circuit instructions to the state-vector mathematics you have already learned.

Keep the NumPy implementations as your reference model. The aim is not to replace your mathematical understanding with SDK calls, but to understand how the two representations agree.

## Learning outcomes

By the end of Week 15, you should be able to:

- Obtain a statevector from a circuit before measurement.
- Read complex amplitudes and calculate computational-basis probabilities.
- Compare Qiskit statevectors with equivalent NumPy statevectors.
- Explain why states with the same computational-basis probabilities can still be different.
- Recognise Qiskit's qubit and bit-ordering conventions when interpreting statevectors and measurement strings.
- Inspect single- and two-qubit states and visualise suitable examples.
- Write focused pytest tests for state preparation and statevector properties.

## Daily plan

### Day 1 — From a circuit to a statevector

**Quantum connection:** A circuit describes operations; a statevector represents the quantum state after those operations have been applied.

**Learn**
- What a statevector represents.
- The difference between constructing a circuit and evaluating its state.
- Use `qiskit.quantum_info.Statevector` to obtain a state from a circuit that has no measurements.
- Inspect the complex amplitudes.

**Tasks**
1. Create a one-qubit circuit with no gates and inspect its statevector.
2. Add an X gate and inspect the result.
3. Create a fresh circuit with an H gate and inspect the result.
4. Compare the amplitudes with your Week 10 NumPy results.

**Daily drill**
Predict the statevector before running the code for each circuit: `|0⟩`, `X|0⟩`, and `H|0⟩`.

**Deliverable:** A small script that prints the circuit and its statevector for the three examples.

### Day 2 — Amplitudes and probabilities

**Quantum connection:** Amplitudes are complex values; measurement probabilities are the squared magnitudes of those amplitudes.

**Learn**
- Read the amplitudes from a `Statevector`.
- Obtain computational-basis probabilities.
- Compare Qiskit's probabilities with `np.abs(statevector) ** 2`.
- Understand why probabilities do not retain all phase information.

**Tasks**
1. Inspect probabilities for `|0⟩`, `|1⟩`, and `|+⟩`.
2. Compare Qiskit's probability output with your NumPy `get_probabilities()` function.
3. Run the corresponding circuits with Aer shots and compare theoretical probabilities with sampled counts.

**Daily drill**
For each state, write down the expected probability of measuring 0 and 1 before executing the code.

**Deliverable:** A comparison of statevector-derived probabilities and sampled measurement frequencies.

### Day 3 — Relative phase and global phase

**Quantum connection:** Phase can affect interference even when it does not change computational-basis probabilities.

**Learn**
- Compare `|+⟩` and `|−⟩`.
- Understand why both give 50/50 computational-basis probabilities.
- Apply H before measurement to reveal their relative-phase difference.
- Distinguish a global phase from a relative phase.

**Tasks**
1. Construct `|+⟩` and `|−⟩` using circuits.
2. Inspect their amplitudes and probabilities.
3. Apply H to each state and inspect the resulting statevectors and probabilities.
4. Compare `|ψ⟩` with `−|ψ⟩` and explain why a global sign does not change observable predictions.

**Daily drill**
Predict the measurement outcome after applying H to `|+⟩` and to `|−⟩`. Then verify with statevectors and, if useful, Aer shots.

**Deliverable:** Photon-notebook notes explaining how phase becomes observable through interference.

### Day 4 — Two-qubit statevectors and ordering

**Quantum connection:** A two-qubit state has four amplitudes, and the order used to interpret those amplitudes matters.

**Learn**
- Inspect two-qubit statevectors.
- Relate tensor products to `np.kron()`.
- Understand Qiskit's little-endian qubit convention.
- Distinguish the mathematical ordering of qubits from the order in which measurement strings are displayed.

**Tasks**
1. Inspect circuits prepared in `|00⟩`, `|01⟩`, `|10⟩`, and `|11⟩`.
2. Apply H to qubit 0 and then to qubit 1 in separate experiments.
3. Compare the resulting amplitudes with your NumPy tensor-product calculations.
4. Write down explicitly which basis ordering you are using when reading each result.

**Daily drill**
Predict which statevector array position changes when you apply X to qubit 0 versus qubit 1. Verify the prediction.

**Deliverable:** A short reference note showing Qiskit basis ordering, qubit indices, and measurement-string ordering. Do not rely on memory alone when interpreting bit strings.

### Day 5 — Bell states through statevectors

**Quantum connection:** Statevectors expose the amplitudes and relative phases that measurement counts alone cannot show.

**Learn**
- Prepare all four Bell states with Qiskit circuits.
- Inspect each Bell state's amplitudes before measurement.
- Compare the results with your Week 13 NumPy Bell-state vectors.
- Connect Bell-state phase differences with the measurement correlations you previously explored.

**Tasks**
1. Prepare Phi+, Phi−, Psi+, and Psi−.
2. Inspect their statevectors.
3. Compare amplitudes with your established NumPy reference vectors, taking Qiskit's ordering convention into account.
4. Confirm that the computational-basis probabilities alone cannot distinguish the two states within each Bell-state pair.

**Daily drill**
Before running each circuit, predict which amplitudes are non-zero and identify their signs.

**Deliverable:** A compact table of the four Bell states, their non-zero amplitudes, and their computational-basis probabilities.

### Day 6 — Visualising and testing quantum states

**Quantum connection:** Visual representations can make amplitudes, phase and multi-qubit structure easier to reason about.

**Learn**
- Choose an appropriate visual representation for a state.
- Explore Qiskit's available state visualisation tools, such as a Bloch-sphere view for single-qubit states, where the required plotting dependencies are available.
- Understand the limitation of a single-qubit Bloch sphere for representing an entangled two-qubit state.
- Test state preparation independently of sampled measurement counts.

**Tasks**
1. Visualise `|0⟩`, `|1⟩`, `|+⟩`, and `|−⟩` if the plotting environment is available.
2. Explain what changes between `|+⟩` and `|−⟩` on the Bloch sphere.
3. Investigate why a pair of individual Bloch-sphere descriptions cannot fully capture Bell-state entanglement.
4. Add pytest tests for statevector amplitudes, normalisation, and expected probabilities.

**Daily drill**
Choose one state and predict its visual position before generating the plot. Explain the relationship between its amplitudes and the visual representation.

**Deliverable:** One or more plots (if supported) and a focused pytest test module.

### Day 7 — Mini-capstone: NumPy and Qiskit statevector explorer

**Goal:** Build a small program that compares a circuit's Qiskit statevector with a NumPy reference result.

**Suggested capabilities**
- Accept a small, predefined circuit or state-preparation choice.
- Produce the Qiskit statevector.
- Calculate probabilities from the statevector.
- Calculate the equivalent NumPy reference result.
- Compare the two results while accounting for the agreed basis ordering.
- Return a readable summary.

**Tasks**
1. Choose a focused set of examples: single-qubit `X`, `H`, `Z`, and at least one two-qubit Bell state.
2. Implement the comparison without mixing circuit construction, calculation, and presentation unnecessarily.
3. Add pytest tests for expected amplitudes, probabilities, and normalisation.
4. Run the complete test suite.
5. Document the key learning and any ordering convention in the README.

**Daily drill**
Before running the capstone for each example, write down the expected statevector and probabilities. Use the program to verify your predictions.

**Deliverable:** A small, tested NumPy-versus-Qiskit statevector explorer.

## Engineering expectations

Keep the same engineering discipline developed in the earlier weeks:

- Use small functions with clear responsibilities.
- Validate inputs where the function has a defined input contract.
- Write tests for meaningful behaviour, including relevant invalid inputs.
- Prefer deterministic statevector tests for exact state properties.
- Use shot-based tests for sampling behaviour, but do not assert exact random distributions.
- Avoid adding abstractions that do not make the code clearer.
- Keep each daily session close to one hour. If a topic takes longer, pause and continue rather than rushing.

## Suggested project structure

```text
week15_qiskit_statevectors/
├── README.md
├── requirements.txt
├── day1_statevector_basics.py
├── day2_amplitudes_probabilities.py
├── day3_phase_experiments.py
├── day4_two_qubit_ordering.py
├── day5_bell_statevectors.py
├── day6_visualisation_tests.py
├── day7_statevector_explorer.py
└── tests/
    └── test_statevector_explorer.py
```

This is a suggested structure, not a requirement to create every file on Day 1. Build it as the week progresses.

## Scope boundaries

This week is about understanding and inspecting statevectors through Qiskit. Do not rush into:
- Quantum hardware execution.
- Noise models and error mitigation.
- Quantum algorithms such as Grover's or Shor's algorithm.
- Advanced circuit optimisation or transpiler internals.

Those topics can come later, once the statevector and circuit foundations are comfortable.

## End-of-week self-assessment

At the end of Day 7, assess yourself from 1–5:

1. I can obtain and interpret a statevector from a Qiskit circuit.
2. I can calculate and explain measurement probabilities from amplitudes.
3. I understand how relative phase affects interference.
4. I can explain Qiskit's qubit and measurement bit ordering.
5. I can compare Qiskit statevectors with NumPy calculations.
6. I can write meaningful pytest tests for deterministic quantum-state properties.
7. I can explain why a Bloch sphere is useful for one qubit but insufficient by itself for an entangled two-qubit state.

**Week 15 success criterion:** You should be able to look at a small Qiskit circuit, predict its statevector and probabilities, verify them programmatically, and explain any differences caused by representation or bit ordering.
