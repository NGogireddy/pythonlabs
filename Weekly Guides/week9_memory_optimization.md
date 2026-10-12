# Week 9 --- Memory, Mutability & Performance-Aware Python

## Quantum Computing + Business/Technology Connection --- READ THIS FIRST

### Where this sits in the 3-month blueprint

The master blueprint lists Week 9 as **Memory Management &
Optimization**, covering:

-   Python garbage collection
-   mutable vs. immutable objects
-   generators (`yield`) for efficient data handling

You have already studied iterators and generators in Week 4, so this
week will **not repeat generator basics**. Instead, it revisits
generators only where they connect to memory behaviour, streaming, and
measurable performance.

Your path so far:

**Weeks 1--4:** Python fluency and engineering habits\
**Week 5:** NumPy fundamentals\
**Week 6:** linear algebra\
**Week 7:** complex numbers and normalisation\
**Week 8:** Matplotlib, transformations, eigenvalues/eigenvectors\
**Week 9:** memory-aware and performance-aware Python

### Why this matters for quantum computing

Quantum simulations and numerical workflows can involve many states,
repeated transformations, arrays, and intermediate results. A correct
algorithm can still be impractical if it creates unnecessary copies,
materialises data too early, or retains large objects longer than
needed.

You do not need to optimise everything prematurely. You need to learn
to:

-   identify likely allocation and memory costs
-   distinguish views from copies
-   recognise when lazy processing helps
-   measure before claiming something is faster
-   preserve correctness while optimising

### Why this matters for enterprise architecture

This is also familiar architecture territory: throughput, latency,
memory pressure, resource lifecycle, and cost. The Python-specific skill
is learning to connect those concerns to object lifetimes, data
structures, and execution patterns.

**Daily limit: 60 minutes maximum.** If a task takes longer, stop at the
hour mark and note what remains.

------------------------------------------------------------------------

# Week 9 Goal

By the end of this week, you should be able to:

1.  Explain mutability and object identity.
2.  Recognise aliasing and avoid accidental shared-state bugs.
3.  Explain the difference between a NumPy view and a copy.
4.  Understand references, object lifetime, and garbage collection at a
    practical level.
5.  Identify when a generator/iterator can avoid materialising a whole
    dataset.
6.  Use simple measurements to compare alternatives without
    overclaiming.
7.  Make a small, evidence-based optimisation without weakening
    contracts or tests.

This week is about engineering judgement---not memorising CPython
internals.

------------------------------------------------------------------------

# Day 1 --- Mutability, Identity & Aliasing

## Drill --- 10 minutes

Predict the result before running each example:

``` python
a = [1, 2, 3]
b = a
b.append(4)
```

Then compare with:

``` python
a = [1, 2, 3]
b = a.copy()
b.append(4)
```

Ask:

-   Did `b = a` create a second list?
-   What does `a is b` tell you?
-   How is `is` different from `==`?

## Learn --- 15 minutes

Focus on:

-   mutable vs. immutable objects
-   assignment and references
-   object identity
-   aliasing
-   shallow copy vs. independent top-level container

Use lists and dictionaries first. Avoid deep-copy complexity unless you
finish early.

## Implement --- 20 minutes

Write a small function that accepts a list and returns a result without
unexpectedly modifying the caller's list.

Decide explicitly whether your function:

-   mutates the input
-   returns a new list
-   permits nested mutable objects

## Test --- 10 minutes

Test:

-   normal input
-   empty input
-   whether the original list changes
-   whether the result is the same object as the input
-   whether equality and identity tell you different things

## Reflect --- 5 minutes

Explain:

> Why can two variables refer to the same mutable object, and what bug
> could that create in a larger application?

------------------------------------------------------------------------

# Day 2 --- NumPy Views, Copies & Memory Layout

## Drill --- 10 minutes

Create a NumPy array, take a slice, modify the slice, and observe the
original array.

Then repeat with `.copy()`.

Predict the outcome before running each version.

## Learn --- 15 minutes

Review:

-   slicing
-   views vs. copies
-   `.copy()`
-   `np.shares_memory()`
-   `shape`, `strides`, and `nbytes`

Do not try to memorise every memory-layout detail. Understand how a
small-looking slice may refer to a larger original allocation.

## Implement --- 20 minutes

Write a small function that returns the first `n` rows of a 2D array.

Define the contract deliberately:

-   Is the result allowed to share memory with the input?
-   What happens for invalid dimensions?
-   What happens if `n` is larger than the number of rows?
-   What happens for `n = 0`?

## Test --- 10 minutes

Test both values and memory behaviour.

A result can contain the expected values and still violate a contract
about whether the caller's array can be changed indirectly.

## Reflect --- 5 minutes

Explain:

> When might returning a view be useful, and when might returning a copy
> be safer?

------------------------------------------------------------------------

# Day 3 --- Object Lifetime & Garbage Collection

## Drill --- 10 minutes

Consider:

``` python
values = [1, 2, 3]
alias = values
del values
```

Ask:

-   Has the list necessarily been destroyed?
-   Does `alias` still refer to it?
-   What does `del` actually remove?

## Learn --- 15 minutes

Learn the practical concepts:

-   references and object lifetime
-   reference counting as a CPython implementation detail
-   cyclic garbage collection
-   why `del` removes a name/reference rather than guaranteeing
    immediate destruction
-   why explicit resource management (`with`) is different from garbage
    collection

Do not spend this session studying interpreter internals in depth.

## Implement --- 20 minutes

Create a tiny experiment that demonstrates references keeping an object
reachable.

Optionally explore `gc` in a short script, but don't build an
application around forced garbage collection.

## Test / Observe --- 10 minutes

Write down what you observed and what it does **not** prove.

Avoid tests that depend on exact memory addresses or timing.

## Reflect --- 5 minutes

Explain:

> Why is "I deleted the variable" not the same statement as "the object
> has definitely been destroyed"?

------------------------------------------------------------------------

# Day 4 --- Lazy Processing & Streaming (Revisit, Don't Repeat)

## Drill --- 10 minutes

Compare these two ideas:

-   create a complete list of transformed values
-   produce each transformed value only when requested

Predict which one retains all results at once.

## Learn --- 15 minutes

Briefly revisit Week 4:

-   generator expressions
-   `yield`
-   iterator consumption
-   streaming pipelines

The new emphasis is **memory behaviour**, not generator syntax.

Learn to distinguish:

-   lazy input processing
-   intermediate arrays/lists still allocated per item or batch
-   fully materialised output
-   one-pass iterators that cannot be restarted without recreating them

## Implement --- 20 minutes

Create two small versions of a pipeline over a sequence of numeric
records:

1.  an eager version that materialises transformed results
2.  a lazy version that yields transformed results

Keep the transformation identical so the comparison is fair.

## Test --- 10 minutes

Check that both approaches produce the same values.

Also test empty input and confirm what happens if the iterator is
consumed twice.

## Reflect --- 5 minutes

Explain:

> Does a generator guarantee that an entire program uses little memory?
> Why or why not?

------------------------------------------------------------------------

# Day 5 --- Measure Before Optimising

## Drill --- 10 minutes

Look at a small piece of code you wrote in Weeks 5--8.

Identify one possible source of unnecessary work, such as:

-   repeated calculation inside a loop
-   repeatedly growing an array
-   making a copy that isn't needed
-   materialising a list when iteration would suffice

Do not assume it is slow just because it looks inelegant.

## Learn --- 15 minutes

Learn the basics of:

-   `timeit`
-   repeatable comparisons
-   warm-up/noise and why one timing is weak evidence
-   `time.perf_counter()` for simple elapsed-time measurements
-   `tracemalloc` for Python allocation investigations, with the caveat
    that it does not capture every NumPy/native allocation in the same
    way

Avoid treating a tiny benchmark as proof of general performance.

## Implement --- 20 minutes

Choose one small, equivalent pair of implementations and compare them.

Examples:

-   repeated calculation vs. calculation once
-   eager list vs. generator for a simple transformation
-   repeated array concatenation vs. collecting chunks and combining
    once

Choose only one comparison; keep it small.

## Test --- 10 minutes

Before timing, verify both approaches return equivalent results.

Use numerical tolerance where appropriate.

Record:

-   input size
-   what was measured
-   how many repeats you ran
-   approximate results
-   what you can and cannot conclude

## Reflect --- 5 minutes

Explain:

> What evidence would you need before claiming one implementation is
> better?

------------------------------------------------------------------------

# Day 6 --- Mini Capstone: Memory-Aware Numerical Pipeline

## Scenario

You receive a stream of numerical batches. Each batch contains a
one-dimensional NumPy array of measurements. Some batches may be empty
or invalid.

Build a small pipeline that validates batches, transforms valid
measurements, and calculates a summary without retaining every
transformed measurement unless the contract requires it.

This is a deliberately small engineering exercise---not a large
framework.

## Requirements

Your pipeline should:

1.  accept an iterable of batches
2.  validate each batch according to an explicit contract
3.  apply one simple numerical transformation
4.  calculate count, minimum, maximum, and mean for accepted
    measurements
5.  define behaviour for no accepted measurements
6.  avoid unnecessary repeated array growth
7.  be testable without printing as its primary output

## Must Use

-   NumPy
-   explicit contracts
-   pytest
-   `np.testing.assert_allclose()` where floating-point results are
    compared
-   a deliberate decision about lazy vs. eager processing
-   a returned summary that can be tested

## Consider Using

-   a generator for input batches
-   boolean masks
-   `np.concatenate()` once at the end if aggregation requires it
-   incremental aggregation if it simplifies memory use without making
    the code unnecessarily complex
-   `timeit` only if you have a fair comparison

## Do Not Use Unless Justified

-   classes or inheritance
-   pandas
-   external processing frameworks
-   global mutable state
-   broad `except Exception`
-   premature micro-optimisations
-   a benchmark without correctness checks

## Contract Questions

Before coding, define:

-   What is a valid batch?
-   Are lists accepted, or only NumPy arrays?
-   Are empty batches ignored or counted?
-   Are NaN and infinity allowed?
-   What happens if no valid values are accepted?
-   Is the input mutated?
-   Is the whole input materialised?
-   What does `count` count: batches, measurements, or both?

## Acceptance Criteria

-   Valid batches are handled consistently.
-   Invalid input behaviour is explicit and tested.
-   Summary statistics are correct.
-   Empty/no-data behaviour is deliberate.
-   The input is not unexpectedly mutated.
-   The function returns data instead of relying on printing.
-   All tests pass.
-   You can explain the memory/performance trade-off you chose.

------------------------------------------------------------------------

# Day 7 --- Review, Refactor & Gate

Keep this day light. Do not add features just to fill the day.

## Test Review

-   Run the full suite.
-   Look for tests that would pass even if a bug were introduced.
-   Check empty input, invalid input, and boundary cases.
-   Ensure numerical tests use tolerances appropriately.
-   Confirm the capstone's stated contract matches implementation and
    tests.

## Engineering Review

-   Is a copy necessary?
-   Is an eager list necessary?
-   Are any calculations repeated unnecessarily?
-   Is an array repeatedly grown inside a loop?
-   Is any input mutated unexpectedly?
-   Is a performance claim backed by measurement?
-   Did optimisation make the code harder to understand without a
    meaningful benefit?

## Self-Assessment

Rate yourself 1--5:

-   Mutability and identity
-   Aliasing
-   Views vs. copies
-   Object lifetime
-   Garbage-collection basics
-   Lazy vs. eager processing
-   Memory-aware NumPy use
-   Benchmarking basics
-   Numerical contracts
-   Test quality
-   Engineering judgement
-   Refactoring

------------------------------------------------------------------------

# Week 9 Gate

You are ready to proceed when you can explain:

1.  Why `b = a` doesn't necessarily create a new list.
2.  How to tell whether two NumPy arrays share memory.
3.  Why deleting a variable doesn't guarantee immediate object
    destruction.
4.  When a generator helps memory use---and when it doesn't.
5.  Why repeatedly concatenating arrays can be inefficient.
6.  Why both implementations should be correctness-tested before
    benchmarking.
7.  Why performance should be measured on representative data.
8.  Why the simplest correct implementation is often the best starting
    point.

You do **not** need to become a CPython memory-management expert this
week.

------------------------------------------------------------------------

# Week 9 → Week 10 Bridge

Week 9 focuses on writing code that behaves well with data and
resources.

Week 10 will focus on making that code easier for other engineers to
understand, maintain, and review:

-   PEP 8
-   formatting and linting
-   type hints where useful
-   docstrings
-   module organisation
-   maintainability and review discipline

The goal is not merely code that runs. It is code whose behaviour,
contracts, and trade-offs another engineer can understand.
