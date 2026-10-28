# Week 11 Learning Journey — Visual Qubit Intuition
## Bloch Sphere, Phase, Interference, and Gate Sequences

**Daily time budget:** about 1 hour  
**Week 10 status:** Complete — amplitudes, probabilities, Pauli-X, Pauli-Z, Hadamard, measurement shots, normalization, and basic tests.  
**Week 11 purpose:** Strengthen intuition before moving deeper into quantum programming. You can calculate what a Hadamard gate does; this week focuses on building a mental picture of *why the output changes* and how phase becomes observable through later gates.

## Why this week matters for the quantum-computing path

Quantum programs are sequences of transformations on quantum states. Being able to predict a gate’s effect—both geometrically and numerically—will make later work with Qiskit circuits, interference, and Bell states easier. This is a consolidation week, not a race to add more concepts.

## Working rules

- Keep each session to roughly **60 minutes**.
- **Predict first, calculate second, simulate third.** Write down what you expect before running NumPy or a visualizer.
- Use the interactive qubit visualizer to connect state vectors, Bloch-sphere positions, and probability bars: <https://lab.sirganguly.com/experiments/qubit>
- Use NumPy to verify the visual intuition; don’t treat the visualizer as a substitute for understanding the state.
- Keep a small `week11_visual_qubits/` folder or notebook for experiments and tests.
- You do not need to memorize every geometric detail. Aim to explain the main ideas in your own words.

---

## Day 1 — From State Vector to Picture

**Goal:** Connect the two-amplitude state vector to a qubit’s position and measurement probabilities.

### Learn and visualise
- Review the computational basis states:
  - \(|0\rangle = [1, 0]^T\)
  - \(|1\rangle = [0, 1]^T\)
- Revisit the superposition states:
  - \(|+\rangle = (|0\rangle + |1\rangle)/\sqrt{2}\)
  - \(|-\rangle = (|0\rangle - |1\rangle)/\sqrt{2}\)
- On the Bloch sphere, treat \(|0\rangle\) and \(|1\rangle\) as opposite poles. The states \(|+\rangle\) and \(|-\rangle\) lie on opposite sides of the equator.
- Connect the picture to probabilities: the squared magnitudes of amplitudes give computational-basis measurement probabilities.

### Small task
1. Open the qubit visualizer and locate \(|0\rangle\), \(|1\rangle\), \(|+\rangle\), and \(|-\rangle\).
2. For each state, write down its amplitude vector and expected probabilities `[P(0), P(1)]`.
3. Verify your predictions with NumPy.

### Checkpoint
Explain why \(|+\rangle\) and \(|-\rangle\) have the same computational-basis probabilities even though they are different states.

---

## Day 2 — Visualising Hadamard: It Changes the Basis

**Goal:** Build a reliable mental model for the Hadamard gate.

### Core idea
Hadamard does **not** always create a 50/50 result. Its effect depends on the input state:
- \(H|0\rangle = |+\rangle\): computational-basis probabilities become `[0.5, 0.5]`.
- \(H|1\rangle = |-\rangle\): probabilities are also `[0.5, 0.5]`, but the relative sign differs.
- \(H|+\rangle = |0\rangle\): probabilities become `[1, 0]`.
- \(H|-\rangle = |1\rangle\): probabilities become `[0, 1]`.

A useful first mental model: Hadamard maps the Z-basis states to X-basis states, and maps the X-basis states back to Z-basis states. It changes how the state is expressed relative to the measurement basis.

### Small task
1. Before each simulation, predict the output state and probabilities for the four transformations above.
2. Apply `H @ state` in NumPy.
3. Compare the state vector, probabilities, and visualizer position.
4. Apply H twice and verify that the original state returns.

### Checkpoint
Explain, without saying only “the matrix does it,” why H can turn a 50/50 state into a definite outcome.

---

## Day 3 — Phase: Same Probabilities, Different State

**Goal:** Distinguish global phase from relative phase.

### Learn
- A **global phase** multiplies every amplitude by the same complex factor of magnitude 1. It does not change measurement predictions.
- A **relative phase** changes the relationship between amplitudes. It can affect the result of later gates and measurements in another basis.
- \(|+\rangle = [1, 1]^T/\sqrt{2}\) and \(|-\rangle = [1, -1]^T/\sqrt{2}\) have identical computational-basis probabilities but are not the same state.
- The states \(|+\rangle\) and \(-|+\rangle\) differ only by global phase and are physically equivalent.

### Small task
Create these states in NumPy:
- `plus = [1, 1] / sqrt(2)`
- `minus = [1, -1] / sqrt(2)`
- `global_phase_plus = -plus`

For each, compare:
1. The state vector.
2. Computational-basis probabilities.
3. The result after applying H and then computing probabilities.

### Checkpoint
Explain why `plus` and `minus` look identical to a computational-basis measurement, but become distinguishable after applying H.

---

## Day 4 — Interference: Why Gate Order Matters

**Goal:** See how amplitudes combine, and why phase can change later probabilities.

### Learn
Quantum amplitudes can add or cancel. This is the intuition behind interference. Probabilities are calculated from the final amplitudes; we do not add intermediate probabilities as if the gates were ordinary random choices.

### Small task
Use \(|0\rangle\) and \(|+\rangle\) as inputs. Compare these sequences:
- H, then Z, then H
- Z, then H
- H, then H

For each sequence:
1. Predict the final state before running the code.
2. Calculate the state using matrix multiplication.
3. Calculate probabilities.
4. Describe whether the sequence changes amplitudes, probabilities, or both.

If time allows, revisit `H @ Z @ H @ state` and compare the result with `X @ state` for a few test states.

### Checkpoint
Explain how two circuits can have intermediate states that differ but produce the same final measurement probabilities for a particular input.

---

## Day 5 — Bloch-Sphere Gate Intuition

**Goal:** Connect the familiar X, Z, and H gates to geometric transformations without overloading on formal geometry.

### Learn
- X swaps \(|0\rangle\) and \(|1\rangle\).
- Z leaves \(|0\rangle\) unchanged and changes the sign of the \(|1\rangle\) amplitude.
- H maps between the Z-basis and X-basis states.
- On the Bloch sphere, gates transform the state’s direction. You can use this as a picture, while still checking exact results with matrices.

**Important nuance:** Do not assume every gate is simply “a rotation around the axis you see.” For this week, focus on where the four named states move and what the transformation does to amplitudes.

### Small task
Make a table for X, Z, and H showing the output for each input: \(|0\rangle\), \(|1\rangle\), \(|+\rangle\), and \(|-\rangle\). Include expected computational-basis probabilities.

Then verify at least half the table in NumPy and use the visualizer to inspect the corresponding states.

### Checkpoint
Explain one difference between what Z does and what H does, even when both leave a state’s total probability equal to 1.

---

## Day 6 — Build a Tiny Tested Gate Playground

**Goal:** Turn the intuition into a small, dependable Python experiment.

### Implement
Write small functions for:
- `apply_gate(gate, state)`
- `get_probabilities(state)`
- `is_normalized(state)`
- `run_circuit(gates, state)` — apply gates in sequence, documenting the order clearly.

Use NumPy arrays and keep the functions simple.

### Tests to include
- Probabilities are non-negative and sum to 1 for normalized states.
- X, Z, and H preserve normalization for the states you test.
- Applying H twice returns the original state.
- Applying X twice returns the original state.
- Applying Z twice returns the original state.
- The known transformations from Day 2 are correct.
- Global-phase-related states have the same probabilities.

Use `np.allclose` for array comparisons and `np.isclose` for scalar comparisons. Add a test for a non-normalized input so the behaviour of your probability helper is explicit; do not silently assume every input is valid.

### Checkpoint
For one test, write a short comment explaining the quantum idea it protects—not just the Python operation.

---

## Day 7 — Explain, Predict, Demonstrate

**Goal:** Check whether the picture, the mathematics, and the code agree.

### Mini-challenge
Without running code first, predict the output state and computational-basis probabilities for:
1. H applied to \(|0\rangle\).
2. H applied to \(|+\rangle\).
3. Z applied to \(|+\rangle\), followed by H.
4. H applied to \(|+\rangle\), followed by H.
5. X applied to \(|0\rangle\), followed by Z.

Then verify your predictions in NumPy and, where helpful, with the visualizer.

### Write a short reflection
Answer in your own words:
- What does the Bloch-sphere picture help you understand?
- Why does Hadamard not always produce 50/50 probabilities?
- What is the difference between global phase and relative phase?
- How can a later gate make a relative phase matter?
- Which prediction did you get wrong initially, and what did you learn from it?

### Completion criteria
Week 11 is complete when you can:
- Predict the four H transformations for \(|0\rangle\), \(|1\rangle\), \(|+\rangle\), and \(|-\rangle\).
- Explain why \(|+\rangle\) and \(|-\rangle\) have the same computational-basis probabilities but behave differently after H.
- Explain global phase versus relative phase with one example.
- Trace a short gate sequence by hand and verify it with NumPy.
- Explain the output to another learner without relying only on matrix multiplication.

---

## Optional resource (use only if you have extra time)

- **Interactive qubit visualizer:** <https://lab.sirganguly.com/experiments/qubit>
- **3Blue1Brown — “Some light quantum mechanics (with minutephysics)”**: <https://www.youtube.com/results?search_query=3Blue1Brown+Some+light+quantum+mechanics+minutephysics>

## How this fits the master journey

This week reinforces the state-vector, gate, phase, and measurement intuition needed for the next stage: learning quantum programming syntax and building small circuits. Once the geometric intuition is steadier, move on to circuit construction and a first entanglement/Bell-state milestone rather than trying to learn every concept at once.
