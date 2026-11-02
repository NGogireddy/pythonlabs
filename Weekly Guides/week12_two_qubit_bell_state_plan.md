# Week 12 — Two Qubits, CNOT and the First Bell State

## Why this week matters

Until now, the quantum exercises have focused on one qubit. This week moves to **two-qubit systems** and introduces entanglement.

The milestone is to build and understand your first Bell state using Python and NumPy. This connects directly to the longer-term goal of quantum software engineering and hybrid quantum-classical architecture.

By the end of the week, you should be able to:
- Represent a two-qubit system as a four-amplitude state vector.
- Explain why tensor products are needed to combine qubits.
- Apply a two-qubit CNOT gate.
- Build the Bell state `|Φ+⟩ = (|00⟩ + |11⟩)/√2`.
- Simulate measurements and explain the correlation between the two qubits.
- Explain, at an introductory level, why this Bell state is entangled rather than a product of two independent qubit states.

**Daily time budget:** about 1 hour. Stop when the session reaches the time limit; unfinished optional work can move to the next day.

## Conventions for this week

To keep the NumPy calculations consistent, we will use the mathematical basis ordering:

`|00⟩, |01⟩, |10⟩, |11⟩`

The first bit is qubit A and the second bit is qubit B. State vectors therefore have four complex amplitudes in this order:

```python
state = np.array([a00, a01, a10, a11])
```

We will explicitly revisit bit ordering if/when we use Qiskit. Qiskit displays bitstrings using its own little-endian convention, so do not assume its printed bitstring order is identical to the convention used in our NumPy exercises.

---

## Day 1 — From one qubit to two qubits

**Goal:** Understand the four computational-basis states and the four-element state vector.

### Learn
- A two-qubit computational basis has four states: `|00⟩`, `|01⟩`, `|10⟩`, and `|11⟩`.
- A general two-qubit pure state has four complex amplitudes.
- The probabilities are the squared magnitudes of those amplitudes.
- A valid state must satisfy that all four probabilities sum to 1.

### Guided reasoning
1. Write the four basis states as four-element column vectors.
2. Identify which vector represents `|00⟩`, and which represents `|11⟩`.
3. Predict the measurement result for each basis state.
4. Compare a definite basis state such as `|10⟩` with an equal superposition of all four basis states.

### Small coding task
Create NumPy arrays for:
- `zero_zero`
- `zero_one`
- `one_zero`
- `one_one`

Write or adapt a `get_probabilities(state)` function and a normalization check that work for four amplitudes.

### Day 1 drill
Explain in your own words why two qubits require four amplitudes rather than two.

**Done when:** You can identify the four basis states and verify that each is normalized.

---

## Day 2 — Tensor products and Kronecker products

**Goal:** Understand how two single-qubit states combine into a joint state.

### Learn
The tensor product combines the amplitudes of two systems. In NumPy, `np.kron()` calculates the Kronecker product.

For example:

`|0⟩ ⊗ |0⟩ = |00⟩`

`|+⟩ ⊗ |0⟩ = (1/√2) [1, 0, 1, 0]ᵀ`

### Guided reasoning
1. Predict the four amplitudes of `|0⟩ ⊗ |1⟩`.
2. Predict the four amplitudes of `|+⟩ ⊗ |0⟩`.
3. Explain why the order of the inputs to a tensor product matters.
4. Calculate the probabilities and confirm normalization.

### Small coding task
Use `np.kron()` to construct:
- `|00⟩`
- `|01⟩`
- `|10⟩`
- `|11⟩`
- `|+⟩ ⊗ |0⟩`
- `|+⟩ ⊗ |+⟩`

Reuse your probability and normalization functions.

### Day 2 drill
For `|+⟩ ⊗ |+⟩`, predict the probability of each of the four outcomes before running Python.

**Done when:** You can explain what `np.kron()` represents physically, not just what the function returns.

---

## Day 3 — The CNOT gate: one qubit controls another

**Goal:** Understand a controlled operation and its truth table.

### Learn
CNOT means controlled-NOT:
- The first qubit is the control.
- The second qubit is the target.
- If the control is 0, the target is unchanged.
- If the control is 1, the target is flipped.

Using this week's basis ordering `|00⟩, |01⟩, |10⟩, |11⟩`:

```text
|00⟩ → |00⟩
|01⟩ → |01⟩
|10⟩ → |11⟩
|11⟩ → |10⟩
```

### Guided reasoning
1. Complete the CNOT truth table yourself.
2. Predict what happens when CNOT is applied to each of the four basis states.
3. Notice that the target only flips when the control is 1.

### Small coding task
Create the 4 × 4 CNOT matrix for the convention above. Apply it to the four basis-state vectors and verify the truth table.

### Day 3 drill
Explain the difference between applying X to the target unconditionally and applying CNOT.

**Done when:** Your CNOT matrix produces all four expected basis-state transformations.

---

## Day 4 — Applying gates to a two-qubit system

**Goal:** Learn how a single-qubit gate acts within a two-qubit state.

### Learn
To apply a gate to one qubit while leaving the other unchanged, use a tensor product with the identity matrix.

For this week's ordering:
- `np.kron(H, I)` applies H to the first (left-hand) qubit.
- `np.kron(I, H)` applies H to the second (right-hand) qubit.

### Guided reasoning
1. Start with `|00⟩`.
2. Predict the result of applying H to the first qubit only.
3. Predict the result of applying H to the second qubit only.
4. Compare the two resulting four-amplitude vectors.

### Small coding task
Implement a reusable `apply_gate(gate, state)` function that works with a 4 × 4 gate and a four-element state vector.

Create the expanded matrices using `np.kron()` and test them on `|00⟩` and `|10⟩`.

### Day 4 drill
Explain why a two-qubit state needs a 4 × 4 matrix for a general two-qubit gate, even though H itself is only 2 × 2.

**Done when:** You can predict which qubit is changed by each expanded gate matrix.

---

## Day 5 — Build the first Bell state

**Goal:** Create and understand the Bell state `|Φ+⟩`.

This is the week's central milestone.

Start with:

`|00⟩`

Apply H to the first qubit, then apply CNOT with the first qubit as control and the second as target:

```text
|00⟩
  -- H on first qubit -->
(|00⟩ + |10⟩) / √2
  -- CNOT -->
(|00⟩ + |11⟩) / √2
```

The final state is:

`|Φ+⟩ = (|00⟩ + |11⟩) / √2`

### Guided reasoning
1. Predict the state after H is applied to the first qubit.
2. Identify which component has control qubit 1.
3. Predict what CNOT does to each component.
4. Explain why the final state contains `|00⟩` and `|11⟩`, but not `|01⟩` or `|10⟩`.

### Small coding task
Use your existing NumPy functions, `np.kron()`, the expanded Hadamard matrix, and your CNOT matrix to construct the Bell state.

Check:
- The final four amplitudes.
- The probabilities.
- Normalization.

Expected state vector in this week's ordering:

`(1/√2) * [1, 0, 0, 1]`

Expected probabilities:

`[0.5, 0, 0, 0.5]`

### Day 5 drill
Explain why measuring the two qubits in the computational basis can produce only `00` or `11` in an ideal simulation.

**Done when:** You can build the Bell state from the initial state using the two gates and explain every step.

---

## Day 6 — Measurement and correlated outcomes

**Goal:** Simulate repeated measurements of the Bell state.

### Learn
A single measurement of the Bell state gives:
- `00` with probability 0.5
- `11` with probability 0.5

It does not give `01` or `10` in an ideal computational-basis measurement.

Across many shots, the counts should approach a 50/50 split, but will not generally be exactly equal.

### Small coding task
Write a measurement function for a four-amplitude state:
1. Calculate probabilities.
2. Sample one of the four basis outcomes using `np.random.choice()`.
3. Run the measurement many times, for example 1,000 shots.
4. Count the outcomes.

Use the basis labels `["00", "01", "10", "11"]` to match this week's NumPy convention.

### Guided reasoning
1. Predict which outcomes should have non-zero counts.
2. Run 1,000 shots.
3. Check that `01` and `10` have zero counts.
4. Repeat the experiment and compare the 50/50 variation.

### Day 6 drill
Explain the difference between:
- Each qubit individually having a 50/50 measurement result.
- The pair having only the correlated outcomes `00` and `11`.

**Done when:** Your simulation produces only `00` and `11`, with counts fluctuating around 50/50.

---

## Day 7 — Explain, verify and consolidate

**Goal:** Demonstrate that you understand the Bell-state circuit rather than merely reproducing code.

### Part A — Predict
Without running Python, explain the circuit:

`|00⟩ → H on first qubit → CNOT → |Φ+⟩`

State:
- The intermediate state.
- The final state vector.
- The four measurement probabilities.
- The possible measurement outcomes.

### Part B — Verify
Run your complete NumPy implementation from a clean execution:
1. Define the single-qubit gates and identity matrix.
2. Define the two-qubit basis states.
3. Construct the expanded H and CNOT operations.
4. Build the Bell state.
5. Check normalization and probabilities.
6. Run repeated measurements.

### Part C — Explain entanglement
In your own words, answer:
1. Why can't this Bell state be written as a tensor product of two individual single-qubit states?
2. Why are the measurement outcomes correlated?
3. Why does a 50/50 result for each qubit not mean the pair is simply two independent random bits?

Keep the explanation intuitive. We will develop the formal treatment of entanglement further in later weeks.

### Optional exploration — See the circuit visually
If you have time, explore IBM Quantum's introductory lesson. Look at the circuit containing H followed by controlled-X (CNOT), and compare its circuit diagram with your NumPy simulation.

- [IBM Quantum: Build and run your first quantum program](https://quantum.cloud.ibm.com/learning/en/courses/use-a-qc-today/build-and-run-your-first-quantum-program)
- [IBM Quantum: Quantum mechanics basics and Bell states](https://quantum.cloud.ibm.com/learning/en/courses/use-a-qc-today/quantum-mechanics-basics)

Qiskit is optional this week. The main objective is to understand the two-qubit mathematics and complete the Bell-state simulation yourself before adding framework syntax.

**Done when:** You can explain and reproduce the Bell-state experiment without following a line-by-line solution.

---

## End-of-week success criteria

By the end of Week 12, you should be able to:

- [ ] Explain why two qubits require four complex amplitudes.
- [ ] Use `np.kron()` to combine single-qubit states and operators.
- [ ] Explain and implement the CNOT truth table.
- [ ] Apply a gate to one qubit while leaving the other unchanged.
- [ ] Build `|Φ+⟩ = (|00⟩ + |11⟩) / √2`.
- [ ] Verify its normalization and measurement probabilities.
- [ ] Simulate repeated measurements and observe correlated outcomes.
- [ ] Explain, at an introductory level, why the Bell state is entangled.

## Learning approach

Keep the same routine that has worked well:
1. Predict the result before calculating.
2. Work through the state-vector transformation.
3. Implement a small piece in NumPy.
4. Test the result.
5. Explain what the result means physically.

Do not spend time polishing the code into a large software project. Keep the implementation small and focused on quantum understanding. Reuse your existing functions where appropriate, and add tests for the new two-qubit behaviour.

**Week 12 milestone:** Your first working two-qubit Bell-state simulation, built and explained from first principles.
