# Week 6 --- NumPy Linear Algebra Fundamentals

## Week 6 Goal

Week 5 established the NumPy foundation: arrays, shape, dtype, indexing,
slicing, vectorisation, broadcasting, aggregation, contracts, and
numerical testing.

Week 6 now builds the next layer:

> **Linear algebra with NumPy**

No formal linear-algebra expertise is assumed.

The goal is not to memorise matrix APIs. The goal is to develop the
mental model needed for later quantum-computing work:

-   vectors
-   matrices
-   vector shape
-   matrix shape
-   transpose
-   dot products
-   matrix multiplication
-   matrix-vector multiplication
-   identity matrices
-   norms
-   solving linear systems
-   basic inverse concepts
-   numerical contracts and floating-point testing

The emphasis remains on **reasoning about shapes and operations**, not
memorising functions.

------------------------------------------------------------------------

# Pace & Working Rules

## Daily limit

**Maximum: 1 hour per day.**

Do not extend a session because an exercise is unfinished.

If you reach 60 minutes:

1.  Stop.
2.  Record what you completed.
3.  Record where you stopped.
4.  Continue only where the following day's plan explicitly allows it.

The goal is sustainable progress.

## Daily learning template

Every day is self-contained:

1.  **Drill** --- activate previous knowledge
2.  **Learn** --- understand the new concept
3.  **Implement** --- write a small piece of code
4.  **Test** --- test while developing
5.  **Reflect** --- capture the mental model

## Testing rule

Continue the Week 2.5 and Week 5 discipline:

-   `pytest`
-   `pytest.mark.parametrize` where useful
-   `pytest.raises`
-   `numpy.testing.assert_array_equal`
-   `numpy.testing.assert_allclose`
-   behaviour-focused tests
-   explicit numerical contracts

Do not force parametrisation when it makes tests harder to read.

------------------------------------------------------------------------

# Day 1 --- Vectors, Matrices & Shape

## Objective

Build the linear-algebra mental model before using linear-algebra
functions.

Understand:

-   scalar
-   vector
-   matrix
-   vector shape
-   matrix shape
-   row vector versus column vector
-   why shape matters
-   NumPy 1D arrays versus explicit 2D vectors

## 1. Drill --- 5--10 minutes

Use NumPy to create:

``` python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([
    [1, 2, 3],
    [4, 5, 6],
])
```

Predict:

``` python
a.shape
a.ndim
b.shape
b.ndim
```

Then predict the shape of:

``` python
column = np.array([
    [1],
    [2],
    [3],
])
```

Ask yourself:

> Is `[1, 2, 3]` the same shape as `[[1], [2], [3]]`?

They contain similar values, but they are not the same NumPy object
structure.

## 2. Learn --- 15 minutes

Learn:

-   scalar
-   1D vector
-   2D row vector
-   2D column vector
-   matrix
-   shape as part of the mathematical meaning

Explore:

``` python
v = np.array([1, 2, 3])

row = np.array([[1, 2, 3]])

column = np.array([
    [1],
    [2],
    [3],
])
```

Compare:

``` python
v.shape
row.shape
column.shape
```

Also investigate:

``` python
v.reshape(3, 1)
v.reshape(1, 3)
```

The important lesson:

> **In linear algebra, shape is not merely metadata. Shape determines
> which operations are mathematically valid.**

## 3. Implement --- 20 minutes

Create:

``` text
week6/
  day1/
    vector_shapes.py
    test_vector_shapes.py
```

Implement:

``` python
describe_vector(values)
```

### Contract

Input:

-   NumPy ndarray
-   exactly one-dimensional
-   numeric dtype
-   non-empty

Output:

``` python
{
    "length": ...,
    "shape": ...,
    "dtype": ...
}
```

Decide how invalid inputs behave.

Do not automatically convert arbitrary input into an array.

The purpose is to practise explicit contracts.

## 4. Test --- 10 minutes

Test:

-   normal 1D vector
-   one-element vector
-   negative values
-   floating-point vector
-   empty vector
-   2D input
-   non-array input
-   non-numeric input

Use appropriate NumPy assertions.

## 5. Reflect --- 5 minutes

Answer:

1.  What is the difference between a vector and a matrix?
2.  Why is `(3,)` different from `(3, 1)`?
3.  Why does shape matter in linear algebra?
4.  What is a column vector?
5.  Why might NumPy's 1D arrays require extra care when doing linear
    algebra?

### Day 1 success criterion

You can look at a NumPy array and explain its mathematical shape before
performing an operation.

------------------------------------------------------------------------

# Day 2 --- Vector Operations & Dot Products

## Objective

Understand:

-   vector addition
-   scalar multiplication
-   element-wise multiplication
-   dot product
-   why dot product is different from element-wise multiplication
-   output shape

## 1. Drill --- 5--10 minutes

Given:

``` python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
```

Predict:

``` python
a + b
a * b
2 * a
```

Now think about:

``` python
np.dot(a, b)
```

What type of result should a dot product produce?

Calculate it manually before running NumPy.

## 2. Learn --- 15 minutes

Learn:

### Vector addition

``` python
a + b
```

### Scalar multiplication

``` python
3 * a
```

### Element-wise multiplication

``` python
a * b
```

### Dot product

``` python
np.dot(a, b)
```

Also investigate:

``` python
a @ b
```

For 1D vectors, understand why `a @ b` represents the dot product.

Do not treat:

``` python
a * b
```

and:

``` python
a @ b
```

as interchangeable.

## 3. Implement --- 20 minutes

Create:

``` text
week6/
  day2/
    vector_operations.py
    test_vector_operations.py
```

Implement:

``` python
vector_dot_product(a, b)
```

### Contract

-   both inputs must be 1D NumPy arrays
-   both must contain numeric values
-   both vectors must have the same length
-   return the scalar dot product
-   do not mutate inputs

Decide what exception should be raised for incompatible shapes.

## 4. Test --- 10 minutes

Test:

-   normal vectors
-   zero vector
-   negative values
-   floating-point values
-   different lengths
-   2D input
-   invalid types

For floating-point results use `assert_allclose`.

## 5. Reflect --- 5 minutes

1.  What is the difference between `*` and `@`?
2.  What does a dot product produce?
3.  Why must the vector lengths match?
4.  Why is shape validation useful here?
5.  What would happen if you silently accepted mismatched vectors?

### Day 2 success criterion

You can explain the difference between:

``` text
element-wise multiplication
        vs
dot product
```

without relying on memorised syntax.

------------------------------------------------------------------------

# Day 3 --- Matrix Multiplication

## Objective

Understand matrix multiplication through shapes before relying on NumPy.

Learn:

-   matrix multiplication
-   `@`
-   compatible matrix shapes
-   matrix-vector multiplication
-   output shape
-   why `*` is not matrix multiplication

## 1. Drill --- 5--10 minutes

Consider:

``` python
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

B = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
])
```

Predict:

``` python
A.shape
B.shape
```

Then ask:

``` text
(2, 3) @ (3, 2)
```

What should the output shape be?

Do the same for:

``` text
(3, 2) @ (2, 1)
```

## 2. Learn --- 15 minutes

Learn the rule:

``` text
(m, n) @ (n, p) → (m, p)
```

The **inner dimensions must match**.

For example:

``` text
(2, 3) @ (3, 4) → (2, 4)
```

But:

``` text
(2, 3) @ (2, 4)
```

is invalid.

Use:

``` python
A @ B
```

and compare with:

``` python
A * B
```

The distinction is fundamental for later quantum-computing work.

## 3. Implement --- 20 minutes

Create:

``` text
week6/
  day3/
    matrix_operations.py
    test_matrix_operations.py
```

Implement:

``` python
multiply_matrices(left, right)
```

### Contract

-   both inputs are 2D numeric NumPy arrays
-   matrix multiplication must be mathematically valid
-   return the matrix product
-   do not mutate either input

Do not reshape inputs silently to make multiplication work.

## 4. Test --- 10 minutes

Test:

-   normal matrix multiplication
-   identity matrix
-   rectangular matrices
-   negative values
-   floating-point matrices
-   incompatible shapes
-   1D input
-   invalid types

Use:

``` python
np.testing.assert_array_equal
```

or:

``` python
np.testing.assert_allclose
```

as appropriate.

## 5. Reflect --- 5 minutes

1.  What is the matrix multiplication shape rule?
2.  Why are the inner dimensions important?
3.  What does the output shape represent?
4.  Why should you not silently reshape invalid input?
5.  Why is `@` important for future quantum-computing work?

### Day 3 success criterion

Given two matrix shapes, you can determine whether multiplication is
valid and predict the output shape before running the code.

------------------------------------------------------------------------

# Day 4 --- Transpose, Identity & Matrix Properties

## Objective

Learn:

-   transpose
-   identity matrix
-   symmetry
-   matrix shape transformation
-   why transpose is useful
-   basic matrix properties

## 1. Drill --- 5--10 minutes

Given:

``` python
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
])
```

Predict:

``` python
A.T
A.T.shape
```

Then consider:

``` python
I = np.eye(3)
```

What should:

``` python
A @ I
```

represent?

## 2. Learn --- 15 minutes

Learn:

``` python
A.T
np.transpose(A)
np.eye(n)
```

Understand:

``` text
(m, n) → transpose → (n, m)
```

Understand the identity matrix:

``` text
A @ I = A
I @ A = A
```

when the dimensions are compatible.

Also explore symmetric matrices:

``` python
A == A.T
```

Do not spend time learning advanced matrix classifications today.

The goal is to build the foundation.

## 3. Implement --- 20 minutes

Create:

``` text
week6/
  day4/
    matrix_properties.py
    test_matrix_properties.py
```

Implement:

``` python
is_symmetric(matrix)
```

### Contract

-   input must be a 2D square numeric NumPy array
-   return `True` if the matrix equals its transpose
-   return `False` otherwise
-   decide how invalid input is handled

For floating-point matrices, do not rely on exact equality if numerical
rounding can matter. Use an appropriate tolerance-based comparison.

## 4. Test --- 10 minutes

Test:

-   symmetric matrix
-   non-symmetric matrix
-   identity matrix
-   1x1 matrix
-   floating-point matrix
-   rectangular matrix
-   1D input
-   invalid input

## 5. Reflect --- 5 minutes

1.  What does transpose do to shape?
2.  What makes a matrix symmetric?
3.  Why is the identity matrix useful?
4.  Why might floating-point equality require tolerance?
5.  Why must `is_symmetric` require a square matrix?

### Day 4 success criterion

You can explain transpose and identity matrices without treating them as
just NumPy functions to memorise.

------------------------------------------------------------------------

# Day 5 --- Norms, Solving Linear Systems & Numerical Contracts

## Objective

Introduce two important numerical ideas:

-   vector/matrix norms
-   solving linear systems

Also reinforce the Week 5 engineering discipline.

## 1. Drill --- 10 minutes

Consider:

``` python
v = np.array([3.0, 4.0])
```

What is the geometric length of this vector?

Calculate it manually.

Then investigate:

``` python
np.linalg.norm(v)
```

Now consider the system:

``` text
2x + y = 5
x  - y = 1
```

Can you solve it manually?

Do not worry if you need time.

## 2. Learn --- 15 minutes

Learn:

``` python
np.linalg.norm(...)
```

and the idea of a linear system:

``` text
A x = b
```

Learn:

``` python
np.linalg.solve(A, b)
```

Focus on understanding what `solve` is doing conceptually.

For:

``` text
A x = b
```

the goal is to find `x`.

Do not focus on manually implementing a matrix inverse.

Understand why solving a system is generally a better numerical
operation than blindly calculating an inverse just to multiply by
another vector.

## 3. Implement --- 20 minutes

Create:

``` text
week6/
  day5/
    linear_systems.py
    test_linear_systems.py
```

Implement:

``` python
solve_linear_system(matrix, vector)
```

### Contract

Input:

-   square numeric 2D NumPy array `matrix`
-   1D numeric NumPy array `vector`
-   dimensions must be compatible

Output:

-   1D NumPy array containing the solution

Invalid cases should have explicit behaviour for:

-   non-square matrix
-   incompatible vector length
-   non-array input
-   non-numeric input
-   singular matrix

Do not silently reshape inputs.

## 4. Test --- 10 minutes

Test:

-   simple 2x2 system
-   3x3 system
-   identity matrix
-   negative values
-   floating-point values
-   incompatible dimensions
-   non-square matrix
-   singular matrix
-   invalid input

Use `assert_allclose` for numerical solutions.

## 5. Reflect --- 5 minutes

Answer:

1.  What is a vector norm?
2.  What does `A x = b` mean?
3.  What does `np.linalg.solve` return?
4.  Why should singular matrices be part of your contract?
5.  Why is explicit validation important for numerical functions?

### Day 5 success criterion

You understand the basic purpose of:

``` text
norm
solve
A x = b
```

and can write an explicit contract around a numerical operation.

------------------------------------------------------------------------

# Day 6 --- Capstone: Linear Transformation Engine

## Objective

Build a small, production-shaped linear-algebra component.

This is **not production-sized**.

The goal is to combine the week's concepts naturally.

Do not force every feature into the solution.

## Problem

A simple transformation system receives:

-   a transformation matrix
-   one or more vectors

The system applies the transformation:

``` text
transformed = matrix @ vector
```

For example:

``` python
matrix = np.array([
    [2, 0],
    [0, 3],
])

vectors = np.array([
    [1, 2],
    [3, 4],
])
```

You need to design a small component that applies the matrix to the
supplied vectors and returns the transformed vectors.

## Before coding

Define:

### Input contract

Decide:

-   Is the transformation matrix always square?
-   Are vectors represented as `(n,)`, `(n, 1)`, or
    `(number_of_vectors, n)`?
-   Are multiple vectors allowed?
-   Are empty inputs allowed?
-   Are integer and floating-point arrays allowed?
-   What happens with incompatible dimensions?
-   What happens with non-numeric data?
-   Is the matrix allowed to be singular?
-   Are NaN/inf values allowed?

Do not silently invent behaviour.

### Output contract

Define:

-   output type
-   output shape
-   dtype expectations
-   whether the input is mutated
-   numerical precision expectations

## Concepts

### Must use

-   NumPy arrays
-   matrix multiplication with `@`
-   shape validation
-   numerical testing
-   explicit contracts

### Consider using

-   transpose
-   `np.asarray`
-   `np.eye`
-   `numpy.testing.assert_allclose`
-   vectorised multiplication across multiple vectors

### Do not use unless justified

-   classes
-   inheritance
-   pandas
-   external libraries
-   manual element-by-element loops
-   unnecessary abstractions

## Acceptance Criteria

Tests should cover appropriate cases such as:

-   identity transformation
-   scaling transformation
-   multiple vectors
-   negative values
-   floating-point values
-   incompatible shapes
-   invalid dimensionality
-   invalid dtype
-   empty input according to your contract

Tests should verify behaviour, not implementation details.

## Timebox

**Maximum: 60 minutes.**

If unfinished:

1.  Stop.
2.  Record what remains.
3.  Do not extend the session.

Do not try to make the project production-complete.

## Important

Do not design the architecture before understanding the problem.

First establish:

``` text
input
output
constraints
acceptance criteria
```

Then design the implementation.

## Reflection

Answer:

1.  What is the matrix shape?
2.  What is the vector shape?
3.  Why is the multiplication valid?
4.  What is the output shape?
5.  Where is validation performed?
6.  Where is the numerical calculation performed?
7.  Are any unnecessary copies created?
8.  What happens with 10 vectors?
9.  What happens with 100,000 vectors?
10. What is the dominant computational cost?
11. What would you change before production?

------------------------------------------------------------------------

# Day 7 --- Test, Refactor & Linear-Algebra Review

## Objective

No new major concept.

Review whether you can reason about linear algebra rather than merely
produce working NumPy code.

## 1. Drill --- 10 minutes

Review the capstone and look for:

-   unclear shape contracts
-   unnecessary conversions
-   unnecessary copies
-   hidden reshaping
-   manual loops
-   unclear variable names
-   duplicated validation
-   implementation-coupled tests
-   missing edge cases
-   weak floating-point assertions

Do not rewrite the entire project.

## 2. Test Review --- 10 minutes

Check:

-   normal cases
-   boundary cases
-   invalid dimensions
-   incompatible shapes
-   numerical tolerance
-   test isolation
-   useful parametrisation

Ask:

> Would these tests still be useful if I completely rewrote the
> implementation?

If yes, they are probably behaviour-focused.

## 3. Refactor --- 20 minutes

Make **2--4 meaningful improvements**.

For every change record:

``` text
Before:
Problem:
After:
Why:
```

Focus on:

-   clearer contracts
-   clearer shape validation
-   simpler NumPy expressions
-   better numerical tests
-   removal of unnecessary code
-   clearer naming
-   better separation of responsibilities

## 4. Performance Review --- 10 minutes

Think about scaling:

``` text
1 vector
100 vectors
10,000 vectors
100,000 vectors
```

Ask:

1.  Are operations vectorised?
2.  Are arrays unnecessarily copied?
3.  Are repeated matrix operations performed unnecessarily?
4.  What is the approximate computational cost?
5.  What is the dominant memory cost?

You do not need to benchmark large datasets.

## 5. Final Week 6 Self-Assessment

Score yourself from **1--5**:

  Area                           Score
  ---------------------------- -------
  Vector/matrix fundamentals        /5
  Shape reasoning                   /5
  Vector operations                 /5
  Dot product                       /5
  Matrix multiplication             /5
  Transpose                         /5
  Identity matrices                 /5
  Symmetry                          /5
  Norms                             /5
  Solving linear systems            /5
  Numerical contracts               /5
  Numerical testing                 /5
  Performance awareness             /5
  Engineering judgement             /5
  Refactoring                       /5

Score based on how confidently you can explain and reproduce the
concepts, not simply whether the exercises were completed.

------------------------------------------------------------------------

# Week 6 Gate --- Before Moving to Week 7

You should be able to explain:

## Linear-Algebra Fundamentals

-   scalar
-   vector
-   matrix
-   row vector
-   column vector
-   vector shape
-   matrix shape
-   why shape matters

## Vector Operations

-   vector addition
-   scalar multiplication
-   element-wise multiplication
-   dot product
-   difference between `*` and `@`

## Matrix Operations

-   matrix multiplication
-   matrix-vector multiplication
-   multiplication shape rule
-   transpose
-   identity matrix
-   symmetric matrix

## Numerical Linear Algebra

-   vector norm
-   `A x = b`
-   purpose of `np.linalg.solve`
-   why singular systems need explicit handling
-   why numerical equality may require tolerance

## Engineering

-   explicit shape contracts
-   explicit dtype contracts
-   invalid-input behaviour
-   no silent reshaping
-   no unnecessary copies
-   no hidden side effects

## Testing

-   behaviour-focused tests
-   `pytest`
-   `pytest.mark.parametrize`
-   `pytest.raises`
-   `assert_array_equal`
-   `assert_allclose`
-   edge cases
-   invalid dimensions

## Performance

-   vectorisation
-   matrix multiplication cost at a conceptual level
-   unnecessary copies
-   repeated computation
-   scaling with number of vectors

------------------------------------------------------------------------

# Connection to the Quantum Computing Roadmap

Week 5 established NumPy.

Week 6 now establishes the linear-algebra foundation required for later
quantum-computing concepts.

The progression is:

``` text
Week 5
NumPy arrays
    ↓
Week 6
Vectors + matrices + linear algebra
    ↓
Week 7
Complex numbers + trigonometry
    ↓
Week 8
Visualisation + matrix/eigenvector work
    ↓
Later
Quantum states + operators + simulation
```

The most important habit this week is:

> **Before performing a linear-algebra operation, reason about the
> shapes.**

Do not start with:

> "Which NumPy function do I call?"

Start with:

> **What mathematical operation am I trying to express?**

> **What are the shapes of the inputs?**

> **What should the output shape be?**

> **What should happen if those shapes are invalid?**

That reasoning will become increasingly important as you move from NumPy
into linear algebra and eventually quantum computing.
