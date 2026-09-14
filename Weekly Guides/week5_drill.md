# Week 5 --- NumPy Fundamentals: Arrays, Vectorisation & Data Contracts

## Week 5 Goal

This week starts **NumPy from the beginning**. No prior NumPy knowledge
is assumed.

The goal is to build a correct mental model of: - NumPy `ndarray` -
shape, dimensions, size, and dtype - indexing and slicing - views versus
copies - vectorised numerical operations - boolean masks -
broadcasting - aggregation with axes - numerical data contracts -
testing numerical code - basic time/memory reasoning

By the end of the week, you should be comfortable asking:

> **What is my data, what is its shape, what result do I need, and what
> NumPy operation expresses that result clearly?**

## Pace & Working Rules

### Daily limit

**Maximum: 1 hour per day.**

If you reach 60 minutes: 1. Stop. 2. Record what you completed. 3.
Record where you stopped. 4. Continue only where the following day's
plan explicitly allows it.

The objective is sustainable progress, not maximising daily volume.

### Daily learning template

Every day is self-contained:

1.  **Drill** --- activate existing Python knowledge
2.  **Learn** --- understand the new NumPy concept
3.  **Implement** --- write a small piece of code
4.  **Test** --- write tests while developing
5.  **Reflect** --- capture what you now understand

### Testing rule

Continue the testing discipline from Week 2.5 and Week 4.

Use: - `pytest` - `pytest.mark.parametrize` where it genuinely improves
coverage - `pytest.raises` for exception contracts -
`numpy.testing.assert_allclose` for floating-point results -
behaviour-focused tests

Do not force parametrisation when a normal test is clearer.

------------------------------------------------------------------------

# Day 1 --- NumPy From Zero: Arrays, Shape, Dimensions & dtype

## Objective

Build your first mental model of a NumPy array.

Understand: - why NumPy exists - what an `ndarray` is - Python list
versus NumPy array - 1D versus 2D arrays - `.shape` - `.ndim` -
`.size` - `.dtype` - basic array creation

No advanced NumPy is expected today.

## 1. Drill --- 5--10 minutes

Before looking anything up, predict:

For `[1, 2, 3, 4]`: - number of elements? - dimensions? - shape?

For:

``` text
1 2 3
4 5 6
```

predict: - shape - dimensions - number of elements

What happens with:

``` python
values = [1, 2, 3]
values * 2
```

What would you expect from:

``` python
import numpy as np
values = np.array([1, 2, 3])
values * 2
```

## 2. Learn --- 15 minutes

Learn:

``` python
import numpy as np

values = np.array([1, 2, 3, 4])

values.shape
values.ndim
values.size
values.dtype
```

Also explore:

``` python
np.zeros(5)
np.ones(5)
np.arange(5)
np.arange(2, 10, 2)
```

Create a 2D array and inspect its properties.

Focus on meaning rather than memorisation.

## 3. Implement --- 20 minutes

Create:

``` text
week5/
  day1/
    array_practice.py
    test_array_practice.py
```

Implement:

``` python
describe_array(values)
```

Return:

``` python
{
    "shape": ...,
    "ndim": ...,
    "size": ...,
    "dtype": ...
}
```

### Contract

**Input:** Must be a NumPy `ndarray`.

**Output:** Dictionary containing `shape`, `ndim`, `size`, and `dtype`.

**Invalid input:** Decide and document behaviour for non-NumPy input.

**Side effects:** None.

## 4. Test --- 10 minutes

Test: - normal 1D array - normal 2D array - empty array - different
dtype - invalid input

## 5. Reflect --- 5 minutes

1.  Why is `shape` important?
2.  What does `ndim` tell you?
3.  What does `size` tell you?
4.  Why does `dtype` matter?
5.  When might a Python list still be more appropriate?

### Day 1 success criterion

You can explain an array's:

**shape → dimensions → size → dtype**

------------------------------------------------------------------------

# Day 2 --- Indexing, Slicing, Views & Copies

## Objective

Learn how to access parts of arrays and understand that a slice can be a
**view** into the original array.

## 1. Drill --- 5--10 minutes

For:

``` python
values = np.array([10, 20, 30, 40, 50])
```

Predict:

``` python
values[0]
values[-1]
values[1:4]
values[:3]
values[2:]
```

For:

``` python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
])
```

Predict:

``` python
matrix[0]
matrix[:, 1]
matrix[1:, :2]
```

## 2. Learn --- 15 minutes

Learn: - integer indexing - negative indexing - slicing - row/column
selection - `:` notation - views - copies

Experiment by modifying a slice and observing whether the original
changes.

Then investigate `.copy()`.

Key lesson:

> **Selecting part of an array and creating an independent copy are not
> always the same operation.**

## 3. Implement --- 20 minutes

Create:

``` text
week5/
  day2/
    slicing_practice.py
    test_slicing_practice.py
```

Implement:

``` python
first_n_rows(matrix, n)
```

### Contract

**Input:** - 2D NumPy `ndarray` - non-negative integer `n`

**Output:** First `n` rows.

Decide and document whether the result is a view or copy.

Consider: - `n = 0` - `n = 1` - `n` smaller than row count - `n` larger
than row count - empty matrix - invalid `n` - 1D input

## 4. Test --- 10 minutes

Test returned values and your documented view/copy contract.

Also test invalid inputs.

## 5. Reflect --- 5 minutes

1.  Why are views useful?
2.  Why can views be dangerous?
3.  When would you deliberately request a copy?
4.  Why can unnecessary copies matter for large arrays?

### Day 2 success criterion

You can explain whether your operation returns shared data or
independent data.

------------------------------------------------------------------------

# Day 3 --- Vectorisation, Element-wise Operations & Boolean Masks

## Objective

Learn to express numerical work as array operations rather than manually
iterating through every element.

Also learn boolean masks.

## 1. Drill --- 5--10 minutes

For `[1, 2, 3, 4]`, describe the Python-loop approach for doubling every
value.

Then ask how the same operation could be expressed with a NumPy array.

Predict:

``` python
values = np.array([0.2, 0.7, 0.4, 0.9])

values > 0.5
```

And:

``` python
values[values > 0.5]
```

## 2. Learn --- 15 minutes

Learn: - element-wise arithmetic - array/scalar operations -
comparisons - boolean arrays - boolean masks - why vectorisation is
useful - why vectorisation is not automatically the answer to every
problem

Explore:

``` python
values * 2
values + 10
values / 2
values > 0.5
values[values > 0.5]
```

Mental shift:

``` text
Python loop:
  take one value
  calculate
  repeat

NumPy:
  describe the operation over the array
```

## 3. Implement --- 20 minutes

Create:

``` text
week5/
  day3/
    vectorisation.py
    test_vectorisation.py
```

Implement:

``` python
normalise_values(values, minimum, maximum)
```

Map `[minimum, maximum]` to `[0, 1]`.

### Contract

**Input:** - 1D numeric NumPy array - `minimum` - `maximum`

**Rules:** - `minimum` must be less than `maximum` - no Python `for`
loop - return a NumPy array - do not mutate input

Decide/document behaviour for: - empty array - negative values -
floating-point values - `minimum == maximum` - invalid input

## 4. Test --- 10 minutes

Test: - normal values - minimum maps to 0 - maximum maps to 1 -
intermediate values - negative values - floating-point values - empty
array according to contract - invalid range

Use:

``` python
numpy.testing.assert_allclose
```

## 5. Reflect --- 5 minutes

1.  What does vectorisation mean in your own words?
2.  Why can it be faster than a Python loop?
3.  Does vectorised automatically mean better?
4.  What is a boolean mask?
5.  What does `values[mask]` mean conceptually?

### Day 3 success criterion

You can recognise when a numerical loop can naturally become an array
operation.

------------------------------------------------------------------------

# Day 4 --- Broadcasting & Aggregation

## Objective

Understand: - broadcasting - compatible shapes - aggregation - `sum` -
`mean` - `min` - `max` - `axis`

## 1. Drill --- 5--10 minutes

Consider:

``` python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

offset = np.array([10, 20, 30])
```

Predict:

``` python
matrix + offset
```

Why might it work?

Now consider:

``` python
offset = np.array([10, 20])
```

Would the operation work? Why?

## 2. Learn --- 15 minutes

Learn the basic idea of broadcasting:

> NumPy can align compatible shapes so an operation can be applied
> without explicitly creating repeated data.

Explore:

``` python
np.sum(matrix)
np.sum(matrix, axis=0)
np.sum(matrix, axis=1)

np.mean(matrix)
np.min(matrix)
np.max(matrix)
```

Mental model for a 2D array: - `axis=0` → operate down rows, producing
one result per column - `axis=1` → operate across columns, producing one
result per row

Verify this with small arrays instead of only memorising it.

## 3. Implement --- 20 minutes

Create:

``` text
week5/
  day4/
    aggregation.py
    test_aggregation.py
```

Implement:

``` python
column_statistics(matrix)
```

Return the mean of each column.

### Contract

**Input:** 2D numeric NumPy array.

**Output:** 1D NumPy array containing column means.

Explicitly decide behaviour for: - empty arrays - zero-row arrays -
one-row arrays - one-column arrays - negative values - invalid
dimensionality - non-numeric data

Do not manually loop over columns.

## 4. Test --- 10 minutes

Test: - normal 2D matrix - single row - single column - negative
values - floating-point values - empty input according to contract -
invalid dimensionality

## 5. Reflect --- 5 minutes

1.  What does `axis=0` mean for a 2D array?
2.  What does `axis=1` mean?
3.  Why did broadcasting work with a length-3 array?
4.  Why did length-2 create a shape problem?
5.  When should shape mismatch make you reconsider the data model?

### Day 4 success criterion

You can reason about:

**input shape → operation → output shape**

------------------------------------------------------------------------

# Day 5 --- Numerical Contracts, Validation & Testing

## Objective

Bring the engineering discipline from Week 2.5 and Week 4 into numerical
programming.

Main lesson:

> Numerical code needs explicit contracts just as much as application
> code does.

## 1. Drill --- 10 minutes

Before coding, define the contract for:

``` python
calculate_state_statistics(values)
```

Write down: - Input - Output - Valid input - Invalid input -
Exceptions - Shape - dtype - Empty input behaviour - Side effects

## 2. Learn --- 10--15 minutes

Review: - shape assumptions - dtype assumptions - floating-point
comparison - empty-array behaviour - separating validation from
calculation - why implicit numerical assumptions can become production
defects

Think about the difference between:

> "This works for the example."

and:

> "This function has a defined contract."

## 3. Implement --- 20 minutes

Create:

``` text
week5/
  day5/
    statistics.py
    test_statistics.py
```

Implement:

``` python
calculate_state_statistics(values)
```

Return:

``` python
{
    "count": ...,
    "mean": ...,
    "minimum": ...,
    "maximum": ...
}
```

Use a **1D numeric NumPy array** as input.

Explicitly define behaviour for: - normal values - one value - negative
values - floating-point values - empty array - wrong dimensionality -
non-numeric input

Where practical, keep validation and calculation logically separated.

## 4. Test --- 10 minutes

Test: - normal array - single element - negative values - floating-point
values - empty input - invalid dimension - invalid type

Use `numpy.testing.assert_allclose` for floating-point results.

## 5. Reflect --- 5 minutes

1.  What guarantees does your function provide?
2.  Which assumptions are explicit?
3.  Which boundary conditions were dangerous when unspecified?
4.  Why should validation be deliberate?
5.  What would make this function safer for another engineer to use?

### Day 5 success criterion

You can write a numerical function contract before writing its
implementation.

------------------------------------------------------------------------

# Day 6 --- Capstone: Quantum Measurement Statistics

## Objective

Build a small, production-shaped numerical component.

This is **not production-sized**.

The purpose is to naturally combine the week's concepts without
artificially forcing every NumPy feature into the solution.

## Problem

Imagine simulated quantum measurement data.

Each experiment produces a 1D NumPy array of numerical measurement
values.

You receive multiple experiments and need combined statistics.

Example:

``` python
[
    np.array([0.1, 0.2, 0.3]),
    np.array([0.4, 0.5, 0.6]),
    np.array([0.7, 0.8, 0.9]),
]
```

Calculate:

``` python
{
    "experiment_count": ...,
    "measurement_count": ...,
    "mean": ...,
    "minimum": ...,
    "maximum": ...
}
```

## Input Contract

The input is an iterable of 1D NumPy arrays.

You must decide and document: - Are zero experiments allowed? - Are
empty measurement arrays allowed? - Must every experiment have the same
number of measurements? - Are NaN values allowed? - Are infinite values
allowed? - Are integer arrays allowed? - Are floating-point arrays
allowed? - What happens for non-array input? - What happens for a 2D
array where a 1D array is expected? - What happens if experiment lengths
differ?

Do not silently invent behaviour.

## Output Contract

The output contains: - number of experiments - total number of
measurements - combined mean - combined minimum - combined maximum

Define numeric behaviour clearly enough that a caller knows what to
expect.

## Concepts

### Must use

-   NumPy arrays
-   vectorised numerical operations
-   NumPy aggregation
-   explicit input validation
-   pytest
-   numerical assertions

### Consider using

-   `np.asarray`
-   boolean masks if required by your contract
-   `np.concatenate`
-   `np.mean`
-   `np.min`
-   `np.max`

### Do not use unless justified

-   classes
-   inheritance
-   pandas
-   external libraries
-   unnecessary abstractions
-   manual element-by-element loops

## Acceptance Criteria

Test appropriate cases such as: - normal multiple experiments - one
experiment - negative values - floating-point values - empty outer
input - invalid dimensionality - inconsistent lengths if your contract
rejects them - invalid/non-numeric input according to your contract -
any special NaN/inf policy you define

Tests should verify **behaviour**, not implementation details.

## Timebox

**Maximum: 60 minutes.**

If unfinished: - stop - record what remains - do not extend the session

Do not make the solution production-complete.

## Important

Do **not** design the architecture before starting.

First understand: 1. input 2. output 3. constraints 4. acceptance
criteria

Then make your own design decisions.

Your architecture will be reviewed after implementation.

## Reflection

1.  What is the input contract?
2.  What is the output contract?
3.  Where does validation happen?
4.  Where does numerical processing happen?
5.  Where is data materialised?
6.  Are unnecessary copies created?
7.  What happens with 10 experiments?
8.  What happens with 10,000 experiments?
9.  What happens if each experiment contains 1 million measurements?
10. What is likely to become the dominant memory cost?
11. What would you change before production?

------------------------------------------------------------------------

# Day 7 --- Test, Refactor & Engineering Review

## Objective

No new NumPy feature today.

Turn:

> "It works."

into:

> "I understand why it works, what it guarantees, and how it will behave
> as it grows."

## 1. Drill --- 10 minutes

Review the capstone before changing anything.

Look for: - unclear input contract - unclear output contract -
unnecessary validation - mixed validation/calculation responsibilities -
unnecessary materialisation - unnecessary copies - manual loops -
unclear naming - duplicated logic - hidden assumptions - tests coupled
to implementation - missing edge cases - weak floating-point assertions

Do not immediately rewrite.

## 2. Test Review --- 10 minutes

Review: - behaviour coverage - edge cases - floating-point comparisons -
useful parametrisation - test isolation - invalid-input coverage

## 3. Refactor --- 20 minutes

Make **2--4 meaningful improvements**.

Do not rewrite the project.

For each change record:

``` text
Before:
Problem:
After:
Why:
```

Focus on: - clearer contracts - separation of validation/calculation -
simpler NumPy expression - fewer unnecessary copies - clearer tests -
improved naming - clearer exceptions - removal of unnecessary code

## 4. Performance Review --- 10 minutes

Think through:

``` text
10 experiments
1,000 experiments
10,000 experiments
```

and:

``` text
10 measurements
10,000 measurements
1,000,000 measurements
```

Ask: 1. What is the computational complexity? 2. What is the memory
complexity? 3. Where are arrays copied? 4. Where is data materialised?
5. Which operation dominates? 6. What happens if the dataset becomes too
large for memory?

No large benchmark is required.

## 5. Final Week 5 Self-Assessment

Score yourself from **1--5**:

  Area                                Score
  --------------------------------- -------
  NumPy array fundamentals               /5
  Shape and dimensional reasoning        /5
  Indexing and slicing                   /5
  Views and copies                       /5
  Vectorisation                          /5
  Boolean masks                          /5
  Broadcasting                           /5
  Numerical aggregation                  /5
  Data contracts                         /5
  Test quality                           /5
  Floating-point testing                 /5
  Performance awareness                  /5
  Engineering judgement                  /5
  Refactoring                            /5

Score based on how confidently you could explain and reproduce the
concepts, not simply whether you completed the exercises.

------------------------------------------------------------------------

# Week 5 Gate --- Before Moving to Week 6

You should be able to explain and demonstrate:

## NumPy Fundamentals

-   `ndarray`
-   why NumPy is useful
-   creating arrays
-   1D and 2D arrays
-   `shape`
-   `ndim`
-   `size`
-   `dtype`

## Indexing & Memory

-   indexing
-   slicing
-   row/column selection
-   why a slice can be a view
-   when a copy may be necessary
-   why unnecessary copies matter

## Vectorisation

-   element-wise arithmetic
-   comparisons
-   boolean masks
-   vectorised operations
-   why vectorisation can improve performance
-   why vectorisation is not automatically appropriate everywhere

## Broadcasting

-   what broadcasting means
-   compatible shapes
-   shape mismatch
-   why shape reasoning matters

## Aggregation

-   `sum`
-   `mean`
-   `min`
-   `max`
-   `axis`
-   output shape after aggregation

## Engineering

-   numerical data contracts
-   explicit shape assumptions
-   explicit dtype assumptions
-   empty-input behaviour
-   invalid-input behaviour
-   separation of validation and calculation
-   avoiding hidden side effects
-   thinking about copies and materialisation

## Testing

-   testing while developing
-   `pytest`
-   `pytest.mark.parametrize`
-   `pytest.raises`
-   `numpy.testing.assert_allclose`
-   edge cases
-   invalid inputs
-   behaviour versus implementation testing

## Performance

-   why NumPy arrays can be preferable to Python lists for numerical
    workloads
-   basic time/memory reasoning
-   recognising unnecessary copies
-   recognising materialisation
-   thinking about scaling

------------------------------------------------------------------------

# Connection to the Quantum Computing Blueprint

This week begins the Numerical Python and Mathematics portion of the
learning roadmap.

The intended sequence is:

``` text
Week 5 → NumPy fundamentals
Week 6 → Linear algebra
Week 7 → Complex numbers & trigonometry
Week 8 → Visualisation + matrix/eigenvector project
```

NumPy is therefore not being learned as an isolated library. It becomes
the numerical foundation for later work involving: - vectors -
matrices - complex numbers - quantum states - linear algebra - quantum
simulation

------------------------------------------------------------------------

# Week 5 Principle

Do not start with:

> "Which NumPy function should I use?"

Start with:

> **What is my data?**

> **What is its shape?**

> **What result do I need?**

> **What operation expresses that result most clearly?**

That reasoning habit is more important than memorising NumPy syntax.
