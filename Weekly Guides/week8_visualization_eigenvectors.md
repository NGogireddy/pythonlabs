# Week 8 --- Visualization, Eigenvalues & Eigenvectors

## Quantum Computing + Business/Technology Connection --- READ THIS FIRST

### Where this sits in the 3-month journey

You have now built this numerical foundation:

**Week 5:** NumPy arrays → shapes → indexing → vectorisation →
broadcasting\
**Week 6:** vectors → matrices → matrix multiplication → transpose →
norms → linear systems\
**Week 7:** complex numbers → magnitude → phase → trigonometry →
complex-vector normalisation → probability from squared magnitude\
**Week 8:** visualisation → eigenvalues/eigenvectors → interpreting
matrix transformations

This is the final numerical bridge before the later quantum-computing
framework work.

The original master blueprint describes Week 8 as:

> Data Visualization --- rapidly plotting graphs, matrices, and state
> vectors using `matplotlib.pyplot`.

It also specifies **Milestone Project 2**:

> Generate a random multi-dimensional matrix, calculate its
> eigenvectors, and plot the resulting vector transformations on a 2D
> grid.

Our Week 8 keeps that destination, but makes the learning progression
more deliberate and testable.

### Why this matters for quantum computing

You are not learning plotting merely to make graphs look nice.

You are learning to **see mathematical objects**:

-   vectors
-   matrices
-   transformations
-   eigenvectors
-   eigenvalues
-   complex-state representations

This becomes useful later when you need to reason about quantum
operators, state vectors and transformations.

### Why this matters for enterprise / architecture work

Visualization is also an engineering communication skill.

As an architect, you will often need to make numerical behaviour
understandable to people who do not want to inspect raw arrays or
equations.

A useful progression is:

**numerical data → mathematical representation → visual representation →
engineering explanation**

That is valuable independently of quantum computing.

------------------------------------------------------------------------

# Week 8 Goal

By the end of this week you should be able to:

1.  Create basic plots using Matplotlib.
2.  Plot vectors and understand what the axes represent.
3.  Visualise 2D transformations.
4.  Understand what an eigenvalue and eigenvector mean conceptually.
5.  Calculate eigenvalues/eigenvectors using NumPy.
6.  Validate numerical eigenvalue/eigenvector results appropriately.
7.  Visualise an eigenvector transformation.
8.  Build a small, production-shaped numerical visualisation project.
9.  Explain the connection between matrix transformations and
    eigenvectors without relying on memorised terminology.

**Daily limit: 60 minutes maximum.**

Do not stretch the session to finish a task. If something takes longer,
record the obstacle and continue the next day.

------------------------------------------------------------------------

# Day 1 --- Matplotlib Fundamentals

## Drill --- 10 minutes

Before using Matplotlib, answer:

1.  What does the x-axis represent?
2.  What does the y-axis represent?
3.  What does one point `(x, y)` represent?
4.  What happens if `x` and `y` have different lengths?
5.  What does a line connecting points communicate that individual
    points do not?

Then make a tiny plot from a small set of numerical values.

## Learn --- 15 minutes

Learn:

-   `matplotlib.pyplot`
-   `plt.plot()`
-   `plt.scatter()`
-   `plt.xlabel()`
-   `plt.ylabel()`
-   `plt.title()`
-   `plt.grid()`
-   `plt.show()`

Do not spend time learning styling, subplots, legends or advanced
formatting yet.

The goal is to understand the relationship between the numerical data
and the visual output.

## Implement --- 20 minutes

Create a small function that plots a sequence of values against their
indices.

Think about the contract before coding:

-   What input is valid?
-   What should happen for an empty array?
-   Should the function return anything?
-   Should plotting be considered a side effect?

## Test --- 10 minutes

At minimum test:

-   normal input
-   empty input
-   invalid input
-   mismatched dimensions if your function accepts separate x/y values

Remember: testing a plotting function is different from testing pure
numerical calculations.

## Reflect --- 5 minutes

Answer:

> What information became easier to understand visually than from
> inspecting the NumPy array?

------------------------------------------------------------------------

# Day 2 --- Plotting Vectors

## Drill --- 10 minutes

Take a vector such as:

``` text
[2, 4, 1, 5]
```

Think about two possible interpretations:

1.  Four measurements over four positions.
2.  A 4-dimensional vector.

Ask:

> Does the same array automatically mean the same thing in both cases?

## Learn --- 15 minutes

Learn how to visualise a 2D vector geometrically.

Focus on:

-   x/y coordinates
-   origin
-   vector direction
-   vector magnitude
-   `plt.arrow()` or an equivalent simple approach

Connect this with your Week 6 knowledge of vector norms.

## Implement --- 20 minutes

Create a small function that visualises a 2D vector from the origin.

Your function should make the vector's:

-   direction
-   approximate magnitude
-   x component
-   y component

visually understandable.

## Test --- 10 minutes

Test the numerical part of your logic separately from the plotting side
effect where practical.

Include:

-   `[1, 0]`
-   `[0, 1]`
-   `[3, 4]`
-   negative components
-   invalid dimensions

## Reflect --- 5 minutes

Explain:

> How does the visual length of a vector relate to the norm you learned
> in Week 6?

------------------------------------------------------------------------

# Day 3 --- Matrix Transformations Visually

## Drill --- 10 minutes

Use a simple transformation matrix:

``` text
A = [[2, 0],
     [0, 1]]
```

and a vector:

``` text
v = [1, 1]
```

Calculate:

``` text
A @ v
```

before plotting anything.

Predict what happened geometrically.

## Learn --- 15 minutes

Learn to visualise:

-   original vector
-   transformed vector
-   coordinate axes
-   simple transformations

Focus on transformations such as:

-   scaling
-   reflection
-   rotation

You do not need to memorise every transformation matrix.

The goal is:

> Matrix multiplication is not just arithmetic; it changes geometric
> objects.

## Implement --- 20 minutes

Create a small utility that takes:

-   a 2D transformation matrix
-   one or more 2D vectors

and plots the original and transformed vectors.

Use the matrix multiplication knowledge from Week 6.

## Test --- 10 minutes

Test the transformation calculation independently.

Use:

-   identity matrix
-   simple scaling
-   reflection
-   rotation

Use `np.testing.assert_allclose()` for numerical results.

## Reflect --- 5 minutes

Explain:

> What does the matrix do to a vector geometrically?

Do not worry if the explanation is not mathematically sophisticated yet.

------------------------------------------------------------------------

# Day 4 --- Eigenvalues & Eigenvectors: The Concept

## Drill --- 10 minutes

Start with:

``` text
A = [[2, 0],
     [0, 3]]
```

Try to find vectors whose direction does not change when multiplied by
`A`.

For example, investigate:

``` text
[1, 0]
```

and:

``` text
[0, 1]
```

Ask:

> What changed?

## Learn --- 20 minutes

Learn the core idea:

An eigenvector of a matrix is a non-zero vector whose **direction
remains unchanged** when the matrix is applied.

The relationship is:

``` text
A @ v = λv
```

where:

-   `A` = matrix
-   `v` = eigenvector
-   `λ` = eigenvalue

The eigenvalue tells you how the eigenvector is scaled.

This is the conceptual heart of the week.

Do not jump into complicated derivations.

## Implement --- 15 minutes

Use NumPy to calculate eigenvalues and eigenvectors.

Explore:

``` text
np.linalg.eig()
```

Use small matrices where you can reason about the answer manually.

## Test --- 10 minutes

Do not only compare NumPy's output to a hard-coded expected array.

Test the mathematical property:

``` text
A @ v ≈ λ * v
```

using `np.testing.assert_allclose()`.

This is an important numerical-testing habit.

## Reflect --- 5 minutes

Explain in your own words:

> Why is an eigenvector different from an ordinary vector?

------------------------------------------------------------------------

# Day 5 --- Eigenvalues/Eigenvectors + Numerical Contracts

## Drill --- 10 minutes

For a matrix:

``` text
A = [[2, 0],
     [0, 3]]
```

predict:

-   how many eigenvalues you expect
-   what the eigenvectors might look like
-   what happens when the matrix acts on each eigenvector

## Learn --- 15 minutes

Focus on the engineering side.

Think about contracts for a function that calculates eigen-information.

Questions:

-   Must the input be a square matrix?
-   What should happen for a non-square matrix?
-   What dtype should the output use?
-   Can eigenvalues/eigenvectors be complex even when the input matrix
    contains real numbers?
-   How should numerical equality be tested?
-   What does the ordering of returned eigenvalues mean?

Important:

> Do not assume the order of eigenvalues returned by NumPy is something
> your application should depend on.

## Implement --- 20 minutes

Create a small numerical function that:

1.  validates the matrix
2.  calculates eigenvalues/eigenvectors
3.  returns a clearly defined result

Keep it small.

Do not build a class.

Do not build a general-purpose linear algebra framework.

## Test --- 10 minutes

Test:

-   diagonal matrix
-   symmetric matrix
-   identity matrix
-   invalid non-square matrix
-   numerical relationship `A @ v ≈ λv`

Also think about repeated eigenvalues.

## Reflect --- 5 minutes

Answer:

> What makes testing eigenvectors different from testing an ordinary
> deterministic scalar calculation?

------------------------------------------------------------------------

# Day 6 --- Milestone Project 2: Visualising Matrix Transformations

## Project

Build a small numerical visualisation program that:

1.  creates or accepts a 2D transformation matrix
2.  defines a small set of 2D vectors
3.  transforms the vectors using matrix multiplication
4.  calculates the matrix's eigenvalues/eigenvectors
5.  identifies the eigenvectors among the visualised directions where
    appropriate
6.  plots the original and transformed vectors
7.  provides a concise numerical summary

The project should be **production-shaped, not production-sized**.

------------------------------------------------------------------------

## Project Input

You may choose a deterministic matrix rather than a random matrix
initially.

For example, use a small 2×2 matrix whose behaviour you can understand.

Once the deterministic version works, optionally experiment with a
random matrix.

------------------------------------------------------------------------

## Must Use

-   NumPy
-   Matplotlib
-   matrix multiplication using `@`
-   `np.linalg.eig()`
-   numerical validation
-   `np.testing.assert_allclose()` in tests
-   clear input/output contracts
-   functions with single, understandable responsibilities

------------------------------------------------------------------------

## Consider Using

-   `np.asarray()`
-   `np.eye()`
-   helper functions for transformation
-   helper functions for eigen-analysis
-   helper functions for plotting
-   `plt.axis("equal")`
-   annotations or labels
-   deterministic test matrices

------------------------------------------------------------------------

## Do Not Use Unless Justified

-   classes
-   inheritance
-   pandas
-   external numerical libraries
-   manual eigenvalue calculations for the implementation
-   global mutable state
-   unnecessary abstraction
-   large configuration frameworks

------------------------------------------------------------------------

## Important Design Constraint

Do **not** start by designing a large architecture.

First identify:

``` text
Input
  ↓
Validation
  ↓
Transformation
  ↓
Eigen-analysis
  ↓
Visualisation
  ↓
Summary
```

Then decide what small functions are actually necessary.

------------------------------------------------------------------------

## Acceptance Criteria

Your project should allow someone looking at the output to answer:

1.  What was the original vector?
2.  What happened to it after transformation?
3.  Which directions behave differently from ordinary vectors?
4.  What are the eigenvalues?
5.  Why are the highlighted directions eigenvectors?
6.  Does the numerical calculation satisfy:

``` text
A @ v ≈ λv
```

Your tests should validate the mathematics, not merely that the code
runs.

------------------------------------------------------------------------

# Day 7 --- Review, Refactor & Gate

This day is intentionally lighter.

## Test Review

Run the complete test suite.

Look specifically for:

-   tests that don't actually assert anything
-   tests depending on unstable/uninitialised data
-   tests that test implementation details instead of mathematical
    behaviour
-   missing edge cases
-   inconsistent exception contracts

## Refactoring Review

Check:

-   function names
-   docstrings
-   input/output contracts
-   unnecessary loops
-   duplicated calculations
-   plotting side effects
-   unnecessary global code
-   `if __name__ == "__main__":` usage

## Numerical Review

Check:

-   shape handling
-   dtype handling
-   floating-point comparisons
-   `assert_allclose`
-   eigenvector validation
-   transformation correctness

## Self-Assessment

Rate yourself 1--5:

-   Matplotlib fundamentals
-   Vector visualisation
-   Matrix transformations
-   Eigenvalue concept
-   Eigenvector concept
-   `np.linalg.eig`
-   Numerical testing
-   Numerical contracts
-   Visual communication
-   Engineering judgement
-   Refactoring

------------------------------------------------------------------------

# Week 8 Gate

You are ready to move forward when you can explain, without looking it
up:

### Visualization

-   What does an x/y coordinate represent?
-   Why might `axis("equal")` matter when plotting vectors?
-   Why separate numerical calculations from plotting?

### Linear algebra

-   What does `A @ v` represent?
-   What does an eigenvector mean?
-   What does an eigenvalue mean?
-   Why does `A @ v = λv` identify an eigenvector?

### Numerical engineering

-   Why use `assert_allclose()`?
-   Why shouldn't tests depend on eigenvalue ordering?
-   What shape should an eigenvector matrix have for a 2×2 matrix?
-   Why must the input matrix for `np.linalg.eig()` be square?

### Quantum bridge

You do **not** need to know quantum mechanics yet.

You should simply be able to see this progression:

``` text
NumPy arrays
    ↓
vectors and matrices
    ↓
matrix transformations
    ↓
complex vectors
    ↓
normalised complex amplitudes
    ↓
visualisation + eigenvectors
    ↓
quantum states and operators
    ↓
Qiskit
```

------------------------------------------------------------------------

# Expected Time Budget

  Day     Focus                              Maximum
  ------- -------------------------------- ---------
  Day 1   Matplotlib fundamentals             60 min
  Day 2   Vector visualisation                60 min
  Day 3   Matrix transformations              60 min
  Day 4   Eigenvalue/eigenvector concept      60 min
  Day 5   Eigen numerical contracts           60 min
  Day 6   Milestone Project 2                 60 min
  Day 7   Review/refactor/gate                60 min

**Do not extend sessions to compensate for unfinished work.**

------------------------------------------------------------------------

# Week 8 → Week 9 Bridge

Week 8 completes the numerical mathematics foundation of the original
three-month plan.

The next step is not simply "more NumPy."

It is moving from:

**What does the mathematics mean?**

to:

**How do I write efficient Python that handles large numerical
workloads?**

That leads into Week 9:

-   memory behaviour
-   mutable vs immutable objects
-   generators
-   efficient data handling
-   performance-aware Python

This also connects strongly with your existing architecture background,
where memory, throughput, streaming and resource efficiency matter.
