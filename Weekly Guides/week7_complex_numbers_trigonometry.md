# Week 7 --- Complex Numbers & Trigonometry for Quantum Computing

## How this week connects to Quantum Computing and business

### Why are we learning this now?

Weeks 5--6 built the numerical foundation:

**NumPy arrays → vectors → matrices → matrix multiplication → linear
systems**

Week 7 adds the next piece that quantum computing depends on:

**complex numbers + magnitude + phase + trigonometry**

A quantum state is represented using **complex amplitudes**. Those
amplitudes are not just ordinary real numbers. Their:

-   real and imaginary parts
-   magnitude
-   phase
-   conjugate

all matter.

For example, a simple quantum state may contain amplitudes such as:

``` python
0.707 + 0j
0.707 + 0j
```

and another state may involve:

``` python
0.707 + 0.707j
```

You do not need to learn quantum mechanics this week. The goal is to
become comfortable with the **mathematical objects that quantum software
uses**.

### Why this matters from a technology/business perspective

As a future hybrid cloud/quantum architect, you eventually need to
translate between:

**Business problem** → optimisation / simulation / probability / state
representation\
→ **classical numerical processing**\
→ **quantum state / circuit representation**\
→ **quantum or hybrid execution**\
→ **business result**

Complex numbers and phase are part of the technical layer that makes
that translation possible.

This week therefore is not "extra mathematics." It is preparing the
numerical vocabulary you will later see in quantum SDKs, simulators,
algorithms, and hybrid workloads.

------------------------------------------------------------------------

# Week 7 Goal

By the end of the week, you should be able to:

-   represent complex numbers using Python and NumPy
-   understand real and imaginary components
-   calculate magnitude and phase
-   use complex conjugates
-   work with NumPy complex arrays
-   understand radians and basic trigonometric functions
-   use Euler's formula conceptually
-   test complex numerical calculations correctly
-   write explicit numerical contracts for complex-valued functions
-   explain why complex numbers and phase are relevant to quantum states

## Daily limit

**Maximum: 1 hour/day**

Each day is self-contained:

**Drill → Learn → Implement → Test → Reflect**

Do not extend a day simply to complete optional exploration.

------------------------------------------------------------------------

# Day 1 --- Complex Numbers Fundamentals

## Drill

Without running Python first, predict:

``` python
z = 3 + 4j

z.real
z.imag
abs(z)
```

Then verify your predictions.

Also try:

``` python
z + 2
z * 2
z * (1 + 1j)
```

## Learn

Understand:

-   real part
-   imaginary part
-   Python's `j` notation
-   complex number addition
-   complex number multiplication
-   magnitude

Key idea:

``` text
z = a + bj

a → real part
b → imaginary part
```

For:

``` python
z = 3 + 4j
```

the magnitude is:

``` text
|z| = sqrt(3² + 4²) = 5
```

Connect this to Week 6 vector norms:

A complex number's magnitude is closely related to the same geometric
idea you learned with vector norms.

## Implement

Implement:

``` python
complex_magnitude(value)
```

Contract:

-   input: one numeric Python complex value
-   output: real-valued magnitude
-   invalid input: reject explicitly
-   no side effects

## Test

Test:

-   `3 + 4j → 5`
-   purely real complex number
-   purely imaginary complex number
-   zero
-   negative real/imaginary components
-   invalid input

Use an appropriate floating-point assertion where necessary.

## Reflect

Answer:

1.  What are the real and imaginary parts?
2.  What does magnitude represent?
3.  How is magnitude related to the Week 6 vector norm?

------------------------------------------------------------------------

# Day 2 --- Complex Arrays and Conjugates

## Drill

Create:

``` python
values = np.array([
    1 + 2j,
    3 - 4j,
    2 + 0j,
])
```

Predict:

``` python
values.real
values.imag
np.abs(values)
np.conjugate(values)
```

Then verify.

## Learn

Understand:

-   NumPy complex dtypes
-   `.real`
-   `.imag`
-   `np.abs`
-   `np.conjugate`
-   why conjugation changes `a + bj` into `a - bj`

Connect this to vectors:

``` text
complex scalar
        ↓
complex vector
        ↓
complex matrix
```

The same shape rules from Week 6 still apply.

## Implement

Implement:

``` python
conjugate_vector(values)
```

Contract:

-   input: 1D NumPy array with complex dtype
-   output: 1D NumPy array containing the complex conjugates
-   preserve shape
-   invalid input should be rejected explicitly

## Test

Test:

-   positive imaginary values
-   negative imaginary values
-   purely real values
-   empty vector, according to your chosen contract
-   invalid dimensionality
-   invalid dtype

Use `assert_allclose` where numerical comparison is appropriate.

## Reflect

Answer:

1.  What does conjugation do?
2.  Does conjugation change the shape?
3.  Why might complex vectors require different handling from ordinary
    real vectors?

------------------------------------------------------------------------

# Day 3 --- Phase and Angles

## Drill

For:

``` python
z = 1 + 1j
```

predict its phase.

Then investigate:

``` python
np.angle(z)
```

## Learn

Understand:

-   angle / phase
-   radians
-   degrees
-   `np.angle`
-   `np.real`
-   `np.imag`
-   relationship between Cartesian form and polar form

Conceptually:

``` text
a + bj
   ↓
magnitude + phase
```

You do not need to memorise every conversion formula. Focus on
understanding what the two representations mean.

Important:

NumPy trigonometric functions use **radians**.

## Implement

Implement:

``` python
complex_phase(value)
```

Contract:

-   input: one complex numeric value
-   output: phase in radians
-   explicitly define your zero-value behaviour
-   reject invalid input explicitly

## Test

Test:

-   `1 + 0j`
-   `0 + 1j`
-   `-1 + 0j`
-   `0 - 1j`
-   a value with both real and imaginary components
-   zero, according to your documented contract

## Reflect

Answer:

1.  What is phase?
2.  Why does NumPy return radians?
3.  What information does magnitude give that phase does not?
4.  What information does phase give that magnitude does not?

------------------------------------------------------------------------

# Day 4 --- Trigonometry and Euler's Formula

## Drill

Predict:

``` python
np.sin(0)
np.cos(0)
np.sin(np.pi / 2)
np.cos(np.pi)
```

Then verify.

## Learn

Understand:

-   `sin`
-   `cos`
-   `tan`
-   radians
-   periodic behaviour
-   Euler's formula conceptually:

``` text
e^(iθ) = cos(θ) + i sin(θ)
```

You do not need to derive Euler's formula.

The important connection is:

``` text
angle θ
   ↓
cos(θ) + i sin(θ)
   ↓
complex number with magnitude 1
```

This is a key bridge between trigonometry and complex-valued quantum
mathematics.

## Implement

Implement:

``` python
unit_complex_from_phase(theta)
```

The function should return the complex number represented by:

``` text
cos(theta) + i sin(theta)
```

Contract:

-   input: real numeric angle in radians
-   output: complex number
-   document units explicitly
-   reject invalid input explicitly

## Test

Test:

-   `0`
-   `π/2`
-   `π`
-   `3π/2`
-   negative angles
-   several arbitrary angles

Use tolerance-based assertions.

## Reflect

Answer:

1.  Why does a phase angle produce a complex number?
2.  Why is the magnitude of `cos(θ) + i sin(θ)` equal to 1?
3.  Why is explicit documentation of radians important?

------------------------------------------------------------------------

# Day 5 --- Complex Numerical Contracts

## Drill

Design the contract for:

``` python
normalise_complex_vector(values)
```

Before coding, decide:

-   input shape
-   dtype
-   empty input
-   output type
-   what "normalise" means
-   what happens when the vector has zero magnitude
-   whether the original array is modified
-   what exceptions are appropriate

## Learn

Focus on numerical engineering:

-   complex dtype assumptions
-   floating-point tolerance
-   magnitude of complex vectors
-   zero magnitude
-   preserving shape
-   avoiding accidental mutation
-   separating validation from calculation

Connect this to your Week 5 contract work:

> Numerical code needs explicit contracts just as much as application
> code does.

## Implement

Implement:

``` python
normalise_complex_vector(values)
```

A sensible interpretation is:

``` text
normalised_vector = values / vector_norm
```

where the vector norm is the Euclidean magnitude of the complex vector.

You must decide and document the contract for:

-   valid input
-   invalid input
-   empty vector
-   zero-magnitude vector
-   output shape
-   mutation/side effects

Do not over-engineer the function.

## Test

Include tests for:

-   ordinary complex vector
-   purely real vector represented as complex values
-   mixed positive/negative imaginary values
-   one-element vector
-   zero vector
-   empty vector if allowed
-   invalid input
-   output norm being approximately 1 for valid non-zero input
-   original input remaining unchanged

Use `np.testing.assert_allclose` for numerical results.

## Reflect

Answer:

1.  Why can a zero vector not be normalised?
2.  Why is `assert_allclose` more appropriate than exact equality?
3.  What contract decision did you make about empty vectors?
4.  What contract decision did you make about mutation?

------------------------------------------------------------------------

# Day 6 --- Capstone: Complex State Representation

## Problem

Build a small numerical component that represents and analyses a set of
complex amplitudes.

The component receives a 1D NumPy array of complex amplitudes.

It should provide:

1.  validation
2.  magnitude calculation
3.  normalisation
4.  probability calculation from squared magnitudes
5.  a compact summary of the state

Example input:

``` python
np.array([
    1 / np.sqrt(2),
    1j / np.sqrt(2),
], dtype=complex)
```

For a normalised state, the squared magnitudes should sum to
approximately `1`.

## Acceptance criteria

Your solution should:

-   use NumPy
-   use complex arrays
-   have explicit input/output contracts
-   preserve the input rather than mutate it
-   use vectorised NumPy operations
-   handle invalid input explicitly
-   handle zero-magnitude input explicitly
-   use numerical tolerance in tests
-   test the public behaviour, not just helper functions

## Must use

-   NumPy
-   complex dtype
-   vectorised operations
-   numerical testing
-   explicit contracts

## Consider using

-   `np.abs`
-   `np.conjugate`
-   `np.linalg.norm`
-   `np.testing.assert_allclose`
-   helper functions where they improve clarity

## Do not use unless justified

-   classes
-   inheritance
-   manual loops over individual amplitudes
-   pandas
-   external libraries
-   quantum SDKs

The goal is numerical engineering, not building a quantum framework.

## Important

Do not try to make this production-sized.

Make it **production-shaped**:

-   clear contracts
-   clean functions
-   useful tests
-   sensible validation
-   readable implementation

------------------------------------------------------------------------

# Day 7 --- Test, Refactor and Engineering Review

## Test

Run the complete test suite.

Check:

-   happy paths
-   invalid inputs
-   zero cases
-   numerical tolerance
-   shape preservation
-   mutation behaviour
-   complex dtype handling

## Refactor

Look for:

-   duplicated validation
-   unclear function names
-   unnecessary conversions
-   unnecessary copies
-   hidden side effects
-   overly broad contracts
-   tests that verify implementation rather than behaviour

## Engineering review

Ask:

1.  Can I explain complex numbers without relying on Python syntax?
2.  Can I explain magnitude and phase?
3.  Can I explain conjugation?
4.  Can I explain why radians matter?
5.  Can I explain Euler's formula conceptually?
6.  Can I work confidently with complex NumPy arrays?
7.  Can I write a contract for complex numerical functions?
8.  Can I test complex numerical results appropriately?
9.  Can I explain why complex amplitudes matter to quantum computing?

------------------------------------------------------------------------

# Week 7 Gate

Before moving to Week 8, you should be able to answer **yes** to:

-   I understand real and imaginary components.
-   I understand complex magnitude.
-   I understand complex conjugation.
-   I understand phase.
-   I understand radians.
-   I can use NumPy complex arrays.
-   I understand Euler's formula conceptually.
-   I can normalise a complex vector.
-   I can define contracts for complex numerical functions.
-   I can test floating-point and complex-valued results appropriately.
-   I can explain how complex amplitudes connect to quantum states.

# Expected daily workload

  Day     Focus                          Target
  ------- --------------------------- ---------
  Day 1   Complex fundamentals          ≤60 min
  Day 2   Complex arrays/conjugates     ≤60 min
  Day 3   Phase                         ≤60 min
  Day 4   Trigonometry/Euler            ≤60 min
  Day 5   Numerical contracts           ≤60 min
  Day 6   Capstone                      ≤60 min
  Day 7   Tests/refactoring/review      ≤60 min

# Week 7 → Week 8

Week 7 gives you:

``` text
Complex numbers
      ↓
Magnitude + phase
      ↓
Complex vectors
      ↓
Normalisation
      ↓
Probability from squared magnitude
```

Week 8 will build on this with:

``` text
Vectors + matrices
        +
complex numbers
        +
visualisation
        +
eigenvectors/eigenvalues
        ↓
quantum-state / operator intuition
```

That is the bridge from the numerical foundations you've built in Weeks
5--7 toward actual quantum-computing concepts.
