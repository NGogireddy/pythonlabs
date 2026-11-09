# Week 13 --- Bell States, Measurement Bases & Quantum Correlations

**Learning path:** Python/NumPy foundations → quantum-state simulation →
multi-qubit reasoning\
**Daily time budget:** About 1 hour\
**Approach:** Predict → Learn → Implement → Test → Reflect\
**Prerequisite:** Week 12 completed --- two-qubit state vectors, tensor
products, CNOT, Bell-state construction, measurement simulation, and the
pure two-qubit separability test.

## Week 13 goal

Move from being able to construct and measure a Bell state to being able
to **reason about, distinguish, and experimentally investigate all four
Bell states**.

By the end of the week, you should be able to:

-   Write down the four Bell states and their amplitude vectors.
-   Explain why computational-basis measurements alone do not
    distinguish every Bell state.
-   Understand how applying Hadamard gates changes the measurement
    basis.
-   Calculate and simulate correlations between two measurement
    outcomes.
-   Use a small quantum circuit to distinguish the four Bell states.
-   Build a tested NumPy mini-lab that brings these ideas together.

**Quantum-computing relevance:** These are foundations for quantum
communication, entanglement-based protocols, Bell-state analysis, and
later work with quantum circuits and Qiskit. This week stays with NumPy
so the underlying mathematics remains visible.

------------------------------------------------------------------------

## Daily working rhythm

Aim for approximately 60 minutes:

  Activity                                         Time
  ----------------------------------------- -----------
  Recall drill and prediction                 5--10 min
  Learn and work through the quantum idea        15 min
  Implement a small NumPy experiment             20 min
  Test, inspect results, and explain them        10 min
  Photon notebook reflection                      5 min

Do not rush to code before making a prediction. If a concept is unclear,
spend the session resolving it rather than forcing progress to the next
day.

------------------------------------------------------------------------

## Day 1 --- The four Bell states

### Learn

Study the four maximally entangled two-qubit Bell states:

\[ \|`\Phi`{=tex}\^+`\rangle `{=tex}=
`\frac{|00\rangle+|11\rangle}{\sqrt{2}}`{=tex} \]

\[ \|`\Phi`{=tex}\^-`\rangle `{=tex}=
`\frac{|00\rangle-|11\rangle}{\sqrt{2}}`{=tex} \]

\[ \|`\Psi`{=tex}\^+`\rangle `{=tex}=
`\frac{|01\rangle+|10\rangle}{\sqrt{2}}`{=tex} \]

\[ \|`\Psi`{=tex}\^-`\rangle `{=tex}=
`\frac{|01\rangle-|10\rangle}{\sqrt{2}}`{=tex} \]

Keep the basis order fixed:

\[
\[\|00`\rangle`{=tex}, \|01`\rangle`{=tex}, \|10`\rangle`{=tex}, \|11`\rangle`{=tex}\]
\]

### Drill

Without coding, write the amplitude vector for each Bell state. Identify
which amplitudes carry a negative relative sign.

### Implement

Create the four states as NumPy complex arrays. Write a helper that
returns their computational-basis probabilities.

### Test

-   Each state has four amplitudes.
-   Each state is normalized.
-   Each probability vector sums to 1.
-   Apply the Week 12 determinant test (ad-bc): verify that all four
    states are entangled.

### Reflection

Which Bell states have the same computational-basis probability
distribution? What information does that distribution fail to reveal?

------------------------------------------------------------------------

## Day 2 --- Measuring in a different basis

### Learn

A computational-basis measurement distinguishes `0` from `1`. To
investigate phase information, we can measure in the X basis instead.

The X-basis states are:

\[ \|+`\rangle `{=tex}= `\frac{|0\rangle+|1\rangle}{\sqrt{2}}`{=tex},
`\qquad`{=tex} \|-`\rangle `{=tex}=
`\frac{|0\rangle-|1\rangle}{\sqrt{2}}`{=tex} \]

A Hadamard before a computational-basis measurement converts an X-basis
measurement into a Z-basis measurement:

\[
H\|+`\rangle`{=tex}=\|0`\rangle`{=tex},`\qquad `{=tex}H\|-`\rangle`{=tex}=\|1`\rangle`{=tex}
\]

For two qubits: - Apply (H`\otimes `{=tex}I) to change the first qubit's
measurement basis. - Apply (I`\otimes `{=tex}H) to change the second
qubit's measurement basis. - Apply (H`\otimes `{=tex}H) to change both
qubits' measurement bases.

### Drill

Predict what happens when both qubits of each Bell state are transformed
by (H`\otimes `{=tex}H). Do not calculate all four immediately; start
with (\|`\Phi`{=tex}\^+`\rangle`{=tex}) and
(\|`\Phi`{=tex}\^-`\rangle`{=tex}).

### Implement

Create `H_first = np.kron(H, I)` and `H_both = np.kron(H, H)`. Apply
them to selected Bell states and calculate the resulting probabilities.

### Test

-   Verify the transformed states remain normalized.
-   Check that probabilities are calculated from squared amplitude
    magnitudes.
-   Compare the outcomes for (\|`\Phi`{=tex}\^+`\rangle`{=tex}) and
    (\|`\Phi`{=tex}\^-`\rangle`{=tex}).

### Reflection

Why can a relative phase be invisible in one measurement basis but
affect results in another?

------------------------------------------------------------------------

## Day 3 --- Correlations between two qubits

### Learn

Entanglement is not just about the probability of each individual
outcome. It is also about the relationship between the two outcomes.

For a pair of measured bits: - `00` and `11` are **equal** outcomes. -
`01` and `10` are **different** outcomes.

Investigate correlations for the Bell states in: - The computational (Z)
basis. - The X basis, using Hadamard gates before computational-basis
measurement.

### Drill

For each Bell state, predict whether the two measured bits will always
be equal or always different in the Z basis. Then make the same
prediction in the X basis.

### Implement

Write a helper that classifies a two-bit measurement as equal or
different. Simulate repeated measurements for selected Bell states.

### Test

-   Confirm that each shot produces one of the four valid two-bit
    outcomes.
-   Check that the observed relationship matches the theoretical
    prediction.
-   Remember that individual counts fluctuate; compare relationships and
    approximate frequencies, not exact counts.

### Reflection

How can two states have the same individual outcome probabilities but
different two-qubit correlations?

------------------------------------------------------------------------

## Day 4 --- Quantifying correlation

### Learn

Define a simple correlation score for measurements in a chosen basis:

\[ E = P(`\text{equal}`{=tex}) - P(`\text{different}`{=tex}) \]

Interpretation: - (E=+1): outcomes are always equal. - (E=-1): outcomes
are always different. - (E) near zero: equal and different outcomes
occur at similar rates.

This is a useful first way to summarize two-qubit measurement data. It
is not, by itself, a complete entanglement test.

### Drill

Given a hypothetical 1,000-shot experiment with 900 equal outcomes and
100 different outcomes, calculate (E). Repeat for 100 equal and 900
different outcomes.

### Implement

Write a function that accepts measurement results and returns the equal
count, different count, and correlation score. Run it for Bell-state
experiments in Z and X measurement bases.

### Test

-   The equal and different counts add up to the number of shots.
-   The score lies between -1 and +1.
-   Perfectly equal outcomes give +1; perfectly different outcomes give
    -1.

### Reflection

Why is a correlation score more informative than looking only at the
count of `0` and `1` for one qubit?

------------------------------------------------------------------------

## Day 5 --- Bell-state identification circuit

### Learn

A Bell-state measurement circuit can transform the four Bell states into
four different computational-basis states.

Using the convention that the first qubit is the CNOT control and the
second is the target, apply:

1.  CNOT.
2.  Hadamard to the first qubit.

In matrix notation, the combined operation is:

\[ (H`\otimes `{=tex}I),`\mathrm{CNOT}`{=tex} \]

The expected mapping is:

  Input Bell state   Output basis state
  ------------------ ---------------------------------
  (                  `\Phi`{=tex}\^+`\rangle`{=tex})
  (                  `\Phi`{=tex}\^-`\rangle`{=tex})
  (                  `\Psi`{=tex}\^+`\rangle`{=tex})
  (                  `\Psi`{=tex}\^-`\rangle`{=tex})

### Drill

Before coding, explain why the circuit can distinguish states that had
identical computational-basis probabilities before the circuit.

### Implement

Construct the four Bell states, apply CNOT, then apply `H_first`.
Calculate the output probabilities.

### Test

-   Each Bell state maps to its expected basis state.
-   Each output is normalized.
-   The output has probability 1 for exactly one basis outcome, allowing
    for numerical tolerance.

### Reflection

What does this circuit teach us about extracting information encoded in
relative phase?

------------------------------------------------------------------------

## Day 6 --- Build a reusable Bell-state experiment

### Learn

Bring together state preparation, gate application, measurement
probabilities, repeated sampling, and correlation analysis.

A useful experiment should keep these stages separate: 1. Prepare a
state. 2. Apply gates or a basis change. 3. Calculate theoretical
probabilities. 4. Simulate repeated measurements. 5. Summarize and
validate the results.

### Implement

Build a small set of reusable functions, for example:

-   `get_probabilities(state)`
-   `apply_gate(gate, state)`
-   `simulate_measurements(state, shots, rng=None)`
-   `count_outcomes(measurements)`
-   `calculate_correlation(measurements)`

Use a NumPy random generator (`np.random.default_rng`) so experiments
can be reproduced with a fixed seed when needed.

### Test

Include tests for: - Normalized input states. - Probability vectors
summing to 1. - Correct output length for the requested number of
shots. - Counts summing to the number of shots. - Bell-state correlation
expectations. - Bell-state identification circuit outputs.

Use approximate floating-point comparisons where appropriate. Test
invalid inputs and exception behaviour where it makes sense; do not add
unnecessary framework complexity.

### Reflection

Which functions represent quantum mathematics, and which functions
represent the classical simulation of measurement?

------------------------------------------------------------------------

## Day 7 --- Mini-capstone: Bell-state explorer

### Goal

Create a compact NumPy program that accepts one of the four Bell states
and reports:

1.  Its amplitude vector.
2.  Its computational-basis probabilities.
3.  Whether it is entangled, using (ad-bc).
4.  Its predicted Z-basis equal/different relationship.
5.  Its predicted X-basis equal/different relationship.
6.  The output of the Bell-state identification circuit.
7.  A simulated measurement summary for a configurable number of shots.

### Suggested structure

Keep the code modular and readable. Reuse the tested functions from Day
6 rather than duplicating logic.

### Acceptance checks

-   All four Bell states are represented correctly.
-   All four are normalized and entangled.
-   Their theoretical measurement relationships are correct in both
    bases.
-   The Bell-state identification circuit maps each state to the
    expected basis state.
-   Repeated simulations produce valid outcomes and statistically
    plausible counts.
-   Tests cover the important mathematical contracts and at least one
    invalid-input case.

### Final reflection

Write short answers to these questions:

-   What is the difference between a state vector and a measurement
    result?
-   Why do measurement probabilities alone sometimes hide relative
    phase?
-   How can a basis change make phase information observable?
-   What makes a Bell state entangled?
-   How does the Bell-state identification circuit extract the
    information needed to distinguish the four states?

------------------------------------------------------------------------

## End-of-week self-assessment

Rate each item from 1 (not confident) to 5 (confident):

  Skill                                                               Rating
  ----------------------------------------------------------------- --------
  I can write the four Bell-state vectors from memory.              
  I can explain Z-basis and X-basis measurements.                   
  I can predict equal/different measurement correlations.           
  I can calculate and interpret the correlation score.              
  I understand the Bell-state identification circuit.               
  I can implement the experiments using NumPy.                      
  I can write meaningful tests for the simulation.                  
  I can explain the quantum meaning without relying only on code.   

## Scope and guardrails

-   Keep each day's work to about one hour.
-   Prioritize conceptual understanding over finishing every optional
    experiment.
-   Continue using NumPy before introducing a quantum SDK; the goal is
    to understand what a circuit simulator is doing.
-   Do not treat finite-shot measurement counts as exact theoretical
    probabilities.
-   Keep the basis ordering fixed as `|00>, |01>, |10>, |11>`.
-   Distinguish mathematical state transformations from measurement
    sampling.
-   If a day exposes a conceptual gap, pause and resolve it before
    advancing.

**Week 13 outcome:** You should be able to reason about all four Bell
states, investigate their correlations in different measurement bases,
and identify them with a small quantum circuit implemented in NumPy.
