# Week 10 — From NumPy to a Tiny Quantum-State Simulator

**Time budget:** about 1 hour per day  
**Purpose:** restore curiosity by using the mathematics you already learned to explore a simple quantum system. This is a bridge week, not another general-purpose Python engineering week.

## Quantum Computing + Business/Technology Connection

A quantum program manipulates a state, applies operations, and extracts measurement probabilities. The vectors, complex numbers, matrices, and numerical reasoning from Weeks 5–8 are the language for describing those steps. This week, use them to model a **single qubit** before moving to Qiskit and a Bell-state simulation.

In the longer term, this state → operation → measurement workflow helps explain how quantum workloads are represented and executed, including where classical orchestration and cloud quantum services fit.

## How this week is different

- **One connected experiment all week:** build a tiny one-qubit simulator in small steps.
- **Curiosity before polish:** make predictions, run experiments, and explain surprising results.
- **Engineering is present but proportionate:** test a few meaningful mathematical invariants; don't turn every exercise into a production-hardening project.
- **No repeat of generator lessons:** use the Python and NumPy skills you already have.
- **Stop at 60 minutes:** if an experiment is interesting, leave a note and continue another day rather than extending the session.

## The running model

A pure one-qubit state is represented by a two-element complex vector:

\[
|\psi\rangle = \begin{bmatrix}\alpha\\\beta\end{bmatrix}
\]

For a normalized state, \(|\alpha|^2 + |\beta|^2 = 1\). The computational-basis measurement probabilities are \(P(0)=|\alpha|^2\) and \(P(1)=|\beta|^2\).

A gate is represented by a matrix \(U\), and applying it means calculating \(U|\psi\rangle\). This week uses the Pauli-X, Pauli-Z, and Hadamard gates. Focus on what the operations do, not on building a general quantum framework.

---

## Day 1 — Meet a qubit state

**Goal:** connect complex vectors and normalization to a quantum state.

### Explore
1. Create the state `[1, 0]`, then `[0, 1]`. Explain what each represents in the computational basis.
2. Create `[1/√2, 1/√2]`. Calculate squared magnitudes and verify that the probabilities sum to 1.
3. Try a state with complex amplitudes, such as `[1/√2, i/√2]`. Compare its probabilities with the previous state.

### Build
Write a small function that returns the two computational-basis probabilities for a two-element complex NumPy vector.

### Check
- Do the probabilities sum to 1 for a normalized state?
- Can two states have the same measurement probabilities but different complex amplitudes?

**Deliverable:** a short notebook or Python script with three example states and your observations.

**If you finish early:** explain in plain language why amplitudes are not themselves probabilities.

---

## Day 2 — Apply gates as matrices

**Goal:** use matrix multiplication for a meaningful quantum operation.

### Explore
1. Define the Pauli-X matrix `X = [[0, 1], [1, 0]]`.
2. Apply it to `[1, 0]`, then to `[0, 1]`.
3. Apply X twice to the original state. Predict the result before running the code.

### Build
Write a small function that applies a 2×2 gate matrix to a two-element state vector.

### Check
- Does X swap the two basis states?
- Does applying X twice return the original state, within a numerical tolerance?

**Deliverable:** working examples plus one sentence describing the effect of X.

**Keep it simple:** validate only the essential shapes and use clear errors. Don't build a generic matrix-validation library.

---

## Day 3 — Compare X, Z, and Hadamard

**Goal:** see that different gates have different effects, even when measurement probabilities do not immediately reveal every difference.

### Explore
1. Define the Pauli-Z matrix `Z = [[1, 0], [0, -1]]`.
2. Define the Hadamard matrix `H = (1/√2) * [[1, 1], [1, -1]]`.
3. Apply X, Z, and H to `[1, 0]`.
4. Apply Z to `[1/√2, 1/√2]` and compare amplitudes and probabilities before and after.
5. Apply H twice to `[1, 0]`.

### Reflect
- Which gate changes the measurement probabilities for your chosen input?
- Can a gate change the state without changing the probabilities of measuring 0 or 1 in this basis?

**Deliverable:** a small comparison table of input state, gate, output state, and measurement probabilities.

---

## Day 4 — Measurement is probabilistic

**Goal:** distinguish theoretical probability from a finite set of measurement results.

### Explore
1. For `[1/√2, 1/√2]`, calculate the expected probabilities.
2. Simulate 100 and then 1,000 measurements using NumPy random sampling.
3. Compare observed proportions with theoretical probabilities. Repeat with a fixed random seed for reproducibility.
4. Try `[1, 0]` and check that the result is always 0 in this idealized model.

### Build
Add a small measurement-sampling function that takes a valid two-probability vector and a positive number of shots, then returns counts for 0 and 1.

### Check
- Why might 100 shots differ from a 50/50 split?
- Why does a larger number of shots usually give a more stable estimate without guaranteeing an exact split?

**Deliverable:** one plot or table comparing theoretical probabilities with observed counts.

**Optional:** skip plotting if it becomes a distraction; a clear printed table is enough.

---

## Day 5 — Test the physics, not every possible edge case

**Goal:** use tests to check a few important properties of the model.

Write focused tests for these invariants:

- The probabilities of a normalized state sum to 1, within a tolerance.
- X applied twice returns the original state.
- H applied twice returns the original state.
- X, Z, and H preserve the norm of the states you test.
- Measurement counts sum to the requested number of shots.

Use `numpy.testing.assert_allclose` or `pytest.approx` where appropriate.

### Reflection
For each test, write down the mathematical property it checks. Prefer five meaningful tests over a large number of repetitive tests.

**Deliverable:** a small test file and a brief note explaining what each invariant tells you.

---

## Day 6 — Mini-project: run a one-qubit experiment

**Goal:** combine the week's ideas in one small, understandable workflow.

### Problem statement
Create a program that starts with a chosen one-qubit state, applies a short sequence of X, Z, and H gates, and reports the final state and theoretical measurement probabilities. Optionally, sample measurements and report observed counts.

### Inputs and outputs
- **Inputs:** a two-element state vector, a sequence of named gates, and optionally a positive shot count.
- **Outputs:** final state, probabilities for 0 and 1, and optional counts.
- **Constraints:** use NumPy; keep the supported gate set small; use numerical tolerances for floating-point comparisons; no external quantum SDK yet.

### Acceptance criteria
- The same input and gate sequence produces the same final state.
- The reported probabilities are real, non-negative, and sum to 1 within tolerance for valid normalized examples.
- Unsupported gate names fail clearly.
- Tests cover at least one known gate sequence and one invariant.
- The program is easy to run and explain.

### Concept guidance
- **Must use:** complex NumPy arrays, matrix multiplication, measurement probabilities, focused tests.
- **Consider:** seeded sampling and a compact gate lookup table.
- **Avoid unless justified:** classes, a plugin-like gate architecture, broad exception handling, extensive input-hardening, and performance optimization. This is an educational simulator, not a production quantum SDK.

**Do not start by designing the architecture.** First write down a predicted result for one short circuit, then implement just enough to test that prediction.

---

## Day 7 — Review and reset

Spend no more than 30–45 minutes.

1. Run the examples and tests.
2. Explain, without looking at the code:
   - what the two amplitudes represent;
   - how a gate transforms a state;
   - how amplitudes produce measurement probabilities;
   - why finite measurement counts vary.
3. Write down one result that surprised you and one question you want to investigate later.
4. Rate your confidence from 1–5 in: state vectors, gate matrices, measurement probabilities, and explaining the output.

**Readiness gate:** you do not need a polished package. You are ready to move on if you can trace a short sequence of gates and explain its predicted output. Carry unresolved questions forward rather than repeating the whole week.

## What changes in the wider journey

- **Week 10:** this quantum bridge experiment; code quality and testing are applied where they help the experiment.
- **Week 11:** introduce Qiskit syntax and compare a small SDK circuit with your NumPy model.
- **Week 12:** build and inspect a Bell-state simulation.

The original destination remains the same. The adjustment is to make the quantum connection tangible sooner, while keeping the daily workload bounded and engineering overhead proportional.
