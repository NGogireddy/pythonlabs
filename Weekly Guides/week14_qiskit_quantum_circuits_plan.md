# Week 14 — From NumPy Quantum Circuits to Qiskit

**Dates:** 16–22 November 2026  
**Theme:** Translate the quantum concepts and circuit operations you have built with NumPy into a real quantum-circuit SDK.  
**Daily time:** About 60 minutes  
**Prerequisites:** Week 13 Bell-state work, especially tensor products, CNOT, Hadamard, measurement, correlations, and the Bell-state decoder.

---

## Week 14 outcome

By the end of this week, you should be able to:

1. Explain what a quantum-circuit SDK does and how it relates to the NumPy state-vector simulations you have written.
2. Create a small circuit, add gates, and inspect its circuit diagram.
3. Run a circuit on a local simulator and interpret measurement counts.
4. Prepare and measure Bell states using a circuit SDK.
5. Recreate the Bell-state decoder and verify its outputs.
6. Write a few focused tests or assertions that validate circuit behaviour.

**Important boundary:** This is an SDK-orientation week, not a deep dive into quantum hardware, noise models, or advanced algorithms. We will make the translation from concepts you already understand to SDK operations the main learning objective.

## Before you start

Use a dedicated virtual environment for this week's work so the SDK dependencies do not interfere with your existing Python learning environment.

Suggested repository structure:

```text
week14/
├── README.md
├── requirements.txt
├── day1_sdk_orientation.py
├── day2_first_circuit.py
├── day3_measurement.py
├── day4_bell_states.py
├── day5_bell_decoder.py
├── day6_tests.py
└── notes.md
```

Keep your existing NumPy implementations. They are your reference model: when an SDK result looks surprising, compare it with the state-vector reasoning you already know.

For installation, consult the current official Qiskit installation guide and use the supported installation command for your Python environment. Record the Python and Qiskit versions you install in `README.md`; avoid pinning an old version from an outdated tutorial.

Official references:
- Qiskit documentation: https://docs.quantum.ibm.com/
- Qiskit installation: https://docs.quantum.ibm.com/guides/install-qiskit
- Qiskit circuit guide: https://docs.quantum.ibm.com/guides/construct-circuits
- Qiskit Aer guide: https://docs.quantum.ibm.com/guides/simulate-with-qiskit-aer

---

## Day 1 — SDK orientation and environment

**Quantum connection:** A quantum SDK gives you a higher-level way to describe circuits. It does not change the mathematics of amplitudes, gates, or measurement that you have already studied.

### Learn
- What a quantum circuit is as a sequence of operations.
- The roles of a circuit SDK, a simulator, and quantum hardware.
- How a circuit representation differs from your NumPy state vector.
- Why SDKs may use a circuit diagram and measurement counts rather than showing the full state vector by default.

### Tasks
1. Create a Week 14 folder and a clean virtual environment.
2. Install Qiskit using the current official instructions.
3. Confirm the installation by importing Qiskit and printing its version.
4. Add the environment and version details to `README.md`.
5. In `notes.md`, write a short comparison:
   - NumPy: you explicitly represented the state vector and multiplied matrices.
   - Circuit SDK: you describe operations; a simulator executes or interprets the circuit.

### Daily drill
In your own words, explain the difference between:
- a quantum circuit,
- a quantum simulator,
- a quantum computer.

**Deliverable:** A working environment and a short `README.md` setup section.

---

## Day 2 — Your first quantum circuit

**Quantum connection:** Translate the single-qubit gates you know—X, Z, and H—into circuit operations.

### Learn
- Creating a one-qubit quantum circuit.
- Appending gates to a circuit.
- Drawing or inspecting the circuit.
- The difference between describing a gate and applying a matrix to a state vector yourself.

### Tasks
1. Create a one-qubit circuit.
2. Add an X gate and inspect the circuit.
3. Create separate circuits for:
   - no gate,
   - X,
   - Z,
   - H.
4. Draw each circuit and record what you expect it to do to an initial `|0⟩` state.
5. Compare the expected results with your Week 10 NumPy notes.

### Daily drill
Before running or inspecting each circuit, predict:
- whether the computational-basis measurement probabilities change,
- whether only the phase changes,
- or whether the state becomes a superposition.

**Deliverable:** Four small circuits and a prediction table in `notes.md`.

---

## Day 3 — Measurement and shot counts

**Quantum connection:** Connect the SDK's measurement counts to your `simulate_measurements()` and `count_outcomes()` functions.

### Learn
- Adding classical bits and measurement operations.
- Running a circuit on a local simulator.
- What a shot means.
- Why repeated measurements produce counts rather than a single deterministic answer for a superposition.

### Tasks
1. Follow the current official Qiskit Aer guide to install and use the local simulator.
2. Build a circuit that prepares `|0⟩` and measure it.
3. Build a circuit that applies X and then measures.
4. Build a circuit that applies H and then measures.
5. Run the circuits with 1,000 shots.
6. Compare the counts with your NumPy predictions.

### Daily drill
For the H circuit, explain why the counts should be approximately 50% zero and 50% one, while the exact counts can vary between runs.

**Deliverable:** A short script that runs the three measurement experiments and prints their counts.

---

## Day 4 — Prepare all four Bell states

**Quantum connection:** Recreate the four Bell states you have studied using circuit operations, then compare their measurement distributions with your NumPy Bell-state explorer.

Use the basis order you have consistently used:

`|00⟩, |01⟩, |10⟩, |11⟩`

### Learn
- Creating a two-qubit circuit.
- Applying a gate to a selected qubit.
- Applying CNOT with a specified control and target.
- Preparing entangled states with H followed by CNOT.
- Measuring both qubits and interpreting bit-string counts.

### Tasks
1. Build the `|Φ+⟩` preparation circuit: H on the first qubit, then CNOT.
2. Measure both qubits and run 1,000 shots.
3. Extend the circuit construction to prepare:
   - `|Φ+⟩ = (|00⟩ + |11⟩)/√2`
   - `|Φ−⟩ = (|00⟩ − |11⟩)/√2`
   - `|Ψ+⟩ = (|01⟩ + |10⟩)/√2`
   - `|Ψ−⟩ = (|01⟩ − |10⟩)/√2`
4. For each state, predict which computational-basis outcomes are possible before running it.
5. Compare the measured distributions with the Week 13 NumPy results.

**Important:** Computational-basis measurement counts alone do not distinguish the plus and minus phase variants within each pair. You will explore phase-sensitive measurements in the next sessions.

### Daily drill
For each Bell state, state whether Z-basis measurements should produce equal or different bits.

**Deliverable:** Four Bell-state circuits and a compact counts comparison.

---

## Day 5 — Distinguish Bell states using the X basis

**Quantum connection:** Reuse your Week 13 insight that an X-basis measurement can be implemented by applying H before computational-basis measurement.

### Learn
- Changing the measurement basis with a gate before measurement.
- Why H before measurement reveals phase information that Z-basis measurement does not.
- How to interpret equal/different outcomes in the X basis.

### Tasks
1. Take each Bell-state preparation circuit from Day 4.
2. Add H to both qubits before measurement.
3. Run each circuit with 1,000 shots.
4. Record whether the X-basis outcomes are equal or different.
5. Compare the results with your Week 13 correlation table.

Expected signatures:

| Bell state | Z-basis correlation | X-basis correlation |
|---|---|---|
| `Φ+` | Equal | Equal |
| `Φ−` | Equal | Different |
| `Ψ+` | Different | Equal |
| `Ψ−` | Different | Different |

### Daily drill
Explain why `Φ+` and `Φ−` have the same Z-basis probabilities but different X-basis correlations.

**Deliverable:** A table of Z and X measurement results for all four Bell states.

---

## Day 6 — Rebuild the Bell-state decoder

**Quantum connection:** Translate your Week 13 decoder into a circuit and verify that it identifies each Bell state.

Your NumPy decoder was:

`U_decoder = (H ⊗ I) CNOT`

The operation order matters: apply CNOT first, then H to the first qubit.

### Tasks
1. Build a circuit that applies CNOT, followed by H on the first qubit.
2. Append this decoder after each Bell-state preparation circuit.
3. Measure both qubits.
4. Check that each Bell state maps to its expected computational-basis outcome:

| Input Bell state | Expected decoded outcome |
|---|---|
| `Φ+` | `00` |
| `Φ−` | `10` |
| `Ψ+` | `01` |
| `Ψ−` | `11` |

5. Compare the circuit results with your NumPy decoder from Week 13.
6. Add assertions or simple tests that check the expected outcome for each state.

**Daily drill**
Explain why the decoder is useful: it converts information stored in the Bell-state correlations and relative phase into a computational-basis outcome that can be measured.

**Deliverable:** A Bell-state decoder circuit and verification results for all four inputs.

---

## Day 7 — Mini-capstone: Bell-state SDK explorer

**Quantum connection:** Bring together state preparation, measurement basis changes, correlations, and decoding in one small experiment.

### Tasks
Create a compact program that, for each of the four Bell states:

1. Builds its preparation circuit.
2. Runs Z-basis measurements and records counts.
3. Runs X-basis measurements and records counts.
4. Runs the Bell decoder and records the decoded outcome.
5. Compares observed results with the theoretical signatures.
6. Prints a concise experiment report.

Suggested report columns:

| Bell state | Z result | X result | Decoder result |
|---|---|---|---|
| `Φ+` | Equal | Equal | `00` |
| `Φ−` | Equal | Different | `10` |
| `Ψ+` | Different | Equal | `01` |
| `Ψ−` | Different | Different | `11` |

### Testing checklist
- [ ] All four Bell-state circuits are constructed.
- [ ] Z-basis results agree with the expected equal/different pattern.
- [ ] X-basis results agree with the expected equal/different pattern.
- [ ] Decoder outputs match the expected bit strings.
- [ ] Shot counts add up to the requested number of shots.
- [ ] The report labels each state and measurement basis clearly.
- [ ] No test assumes that finite-shot counts must be exactly 50/50.

### Reflection
Write a short answer to each:
1. What did the SDK make easier than your NumPy implementation?
2. What did NumPy make more transparent than the SDK?
3. Which part of the circuit or measurement workflow still feels unclear?
4. How did the SDK results reinforce your understanding of Bell-state correlations and phase?

**Deliverable:** A runnable mini-capstone, tests/assertions, and a short reflection in `README.md` or `notes.md`.

---

## Week 14 completion criteria

You are ready to close the week when you can:

- [ ] Explain the relationship between a circuit, simulator, and hardware.
- [ ] Construct and draw basic one- and two-qubit circuits.
- [ ] Add measurements and interpret shot counts.
- [ ] Prepare all four Bell states.
- [ ] Explain and demonstrate Z- and X-basis correlation signatures.
- [ ] Implement the Bell-state decoder in the SDK.
- [ ] Validate results with meaningful assertions or tests.
- [ ] Compare SDK behaviour with your NumPy reference implementation.

## Study approach and guardrails

- Keep each session to roughly one hour. If installation or environment setup takes longer, stop and resolve that before compressing the learning exercises.
- Predict the result before running each circuit. This preserves the reasoning habit you developed during the NumPy weeks.
- Use the same qubit-order convention consistently. SDKs may display bit strings in a different order from the way you have written basis vectors; verify the convention rather than assuming.
- Do not treat one finite-shot result as an exact probability.
- Avoid adding cloud hardware access, accounts, advanced noise models, or unrelated algorithms this week.
- If a result differs from your prediction, inspect circuit order, control/target selection, measurement mapping, and displayed bit order before changing the theory.

**Suggested next step after Week 14:** Once the SDK workflow feels comfortable, move toward simulator configuration, noise, and the difference between ideal and noisy quantum circuits.
