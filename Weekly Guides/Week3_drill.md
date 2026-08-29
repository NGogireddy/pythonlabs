# Week 3 — Python Built-in Modules: `collections` & `itertools`

**Goal:** Build Python muscle memory by learning to recognise the standard abstraction that best expresses a data-processing problem.

**Daily limit:** 60 minutes  
**Core learning:** Monday–Friday  
**Capstone:** Saturday–Sunday  
**Testing:** Every important concept gets a small test.

---

## Weekly rhythm

| Day | Focus | Time |
|---|---|---:|
| Monday | `Counter` | 60 min |
| Tuesday | `defaultdict` | 60 min |
| Wednesday | `namedtuple` + data representation | 60 min |
| Thursday | `itertools.permutations` | 60 min |
| Friday | `itertools.combinations` | 60 min |
| Saturday | Capstone implementation | 60 min |
| Sunday | Capstone tests, refactoring & review | 60 min |

**Rule:** Stop at 60 minutes. Consistency matters more than finishing everything in one sitting.

---

# Permanent testing ritual

For each concept:

1. Learn the concept.
2. Write a tiny implementation from memory.
3. Write tests.
4. Deliberately break the implementation.
5. Confirm the test catches it.
6. Fix/refactor.

### Testing memory hooks

**Parametrization**

> ONE behaviour + MANY inputs = `pytest.mark.parametrize`

**Exception testing**

> Expected failure + specific exception = `pytest.raises()`

Do not force parametrization into every test. Use it when several inputs exercise the same behaviour.

---

# Day 1 — `Counter`

## Objective

Recognise **frequency-counting** problems.

### 0–10 min — Recall

Without notes, implement frequency counting for:

```python
states = ["00", "11", "00", "01", "11", "00"]
```

Expected:

```text
00 → 3
11 → 2
01 → 1
```

First use a normal dictionary. Then ask whether Python has a better abstraction.

### 10–25 min — Learn

Study:

```python
from collections import Counter
```

Practise:

```python
Counter(values)
counter.most_common()
counter["00"]
counter.update(...)
```

### 25–45 min — Execution drill

Write:

```python
def count_states(states):
    ...
```

Requirements:

- return a `Counter`
- handle repeated states
- handle empty input
- identify the most common state

### 45–55 min — Tests

Test:

- normal list
- repeated state
- multiple states
- empty list
- tied frequencies

Try one parametrized test.

### 55–60 min — Reflection

```text
Today I learned:
Today I struggled with:
I can now write from memory:
One thing to repeat:
```

---

# Day 2 — `defaultdict`

## Objective

Recognise **grouping and accumulation** problems.

### 0–10 min — Recall

Given:

```python
records = [
    ("simulator", 100),
    ("hardware", 200),
    ("simulator", 150),
    ("hardware", 300),
]
```

Group shot counts by backend.

Expected:

```text
simulator → [100, 150]
hardware  → [200, 300]
```

First try a normal dictionary.

### 10–25 min — Learn

Study:

```python
from collections import defaultdict
```

Practise:

```python
groups = defaultdict(list)
```

### 25–45 min — Execution drill

Write:

```python
def group_by_backend(records):
    ...
```

Then:

```python
def total_shots_by_backend(records):
    ...
```

### 45–55 min — Tests

Test:

- one backend
- multiple backends
- repeated backend
- empty input
- new/unseen backend

### 55–60 min — Design question

Why is:

```python
groups[key].append(value)
```

often clearer than repeatedly checking:

```python
if key not in groups:
    groups[key] = []
```

Record your answer.

---

# Day 3 — `namedtuple` & Data Representation

## Objective

Understand that choosing a data structure is part of establishing a **data contract**.

### 0–15 min — Recall

Represent:

```text
experiment_id = "EXP-001"
backend = "simulator"
shots = 1000
```

using:

- tuple
- dict
- namedtuple

### 15–30 min — Learn

Practise:

```python
from collections import namedtuple

Experiment = namedtuple(
    "Experiment",
    ["experiment_id", "backend", "shots"]
)
```

### 30–45 min — Execution drill

Create several experiment records.

Practise:

- field access
- iteration
- extracting a field
- calculating total shots

### 45–55 min — Tests

Test:

- field values
- field access
- multiple records
- empty collection
- immutability behaviour

### 55–60 min — Architecture question

Ask:

> Which representation makes the contract clearest for this problem?

Do not assume `namedtuple` is always the right answer.

---

# Day 4 — `itertools.permutations`

## Objective

Recognise problems where **order matters**.

### 0–10 min — Recall

Given:

```python
qubits = ["q0", "q1", "q2"]
```

Calculate manually:

> How many possible orderings are there?

### 10–25 min — Learn

Practise:

```python
from itertools import permutations
```

Generate:

- all permutations
- permutations of length 2

### 25–45 min — Execution drill

Create a function that accepts items and an optional permutation length.

Verify the output manually for a small input.

### 45–55 min — Tests

Test:

- three elements
- two elements
- one element
- empty input
- requested permutation length

Verify the number of results independently.

### 55–60 min — Performance drill

Think about:

```text
3 → 4 → 5 → 6 → 8 → 10 items
```

Ask:

> Why can permutation generation become expensive very quickly?

Record the observation.

---

# Day 5 — `itertools.combinations`

## Objective

Recognise problems where **order does not matter**.

### 0–10 min — Recall

For:

```python
qubits = ["q0", "q1", "q2", "q3"]
```

Calculate manually:

- number of unique pairs
- number of unique triples

### 10–25 min — Learn

Practise:

```python
from itertools import combinations
```

### 25–45 min — Execution drill

Generate:

- all pairs
- all triples

Compare against your manual calculation.

### 45–55 min — Tests

Test:

- four choose two
- four choose three
- one element
- empty input
- selection size greater than input size

Use parametrization where it naturally fits.

### 55–60 min — Quantum connection

Think about:

> Selecting pairs of qubits that could potentially interact.

Write down the difference:

```text
permutations → order matters
combinations → order does not matter
```

---

# Day 6 — Capstone: Quantum State Analysis Engine

## Objective

Combine this week's concepts into a small application.

**Do not follow a tutorial. Design it yourself first.**

## Input

Use data similar to:

```json
[
    {"state": "00", "count": 482},
    {"state": "11", "count": 498},
    {"state": "01", "count": 12},
    {"state": "10", "count": 8}
]
```

## Requirements

### 1. Validate records

Each record must contain:

```text
state
count
```

Rules:

```text
state → non-empty string
count → non-negative integer
```

### 2. Count observed states

Use `Counter` to determine:

```text
state → total count
```

### 3. Group data

Use `defaultdict` for at least one meaningful grouping operation.

Do not add it artificially.

### 4. Represent experiment data

Use `namedtuple` for one appropriate internal record.

Again, use it because it makes sense.

### 5. Generate qubit pairs

Use `combinations` to generate possible qubit pairs.

### 6. Generate ordered configurations

Use `permutations` for one meaningful configuration problem.

---

## Suggested architecture

```text
Input
  ↓
Load
  ↓
Validate
  ↓
Convert to clean internal representation
  ↓
Analyse
  ├── count states
  ├── group data
  ├── generate combinations
  └── generate permutations
  ↓
Result
```

You choose the exact implementation.

## Performance requirement

Before coding, ask:

> How many times do I need to iterate over the input?

After coding, ask:

> Did I accidentally process the same collection unnecessarily?

Do not attempt sophisticated optimisation. Develop the habit of looking for unnecessary work.

---

# Day 7 — Capstone: Tests, Refactor & Review

## 0–15 min — Failure-path testing

Deliberately test:

- missing state
- missing count
- negative count
- string count
- empty input

Your tests should detect the problems.

## 15–30 min — Parametrization

Find one group of repetitive tests.

Convert it to:

```python
@pytest.mark.parametrize(...)
```

Do not convert every test.

The goal is muscle memory.

## 30–40 min — Exception testing

For functions that reject invalid input, practise:

```python
with pytest.raises(SomeException):
    ...
```

Where useful, verify the exception message too.

## 40–50 min — Refactor

Find and improve:

- one duplicated operation
- one unclear name
- one function doing too much
- one unnecessary loop
- one unnecessarily complex section

## 50–55 min — Performance review

Record:

```text
Input size:
Number of passes:
Potential repeated work:
Biggest performance concern:
```

## 55–60 min — Explain your design

Without looking at the code, explain:

- input contract
- output contract
- validation location
- exception boundaries
- why `Counter` is appropriate
- why `defaultdict` is appropriate
- why `combinations` is appropriate
- why `permutations` is appropriate
- where the solution could become expensive

---

# Daily Execution Drills

## Drill 1 — Write from memory

Each day, write a tiny example without looking at syntax documentation.

Practise:

```python
Counter(...)
defaultdict(...)
namedtuple(...)
permutations(...)
combinations(...)
```

Then check your syntax.

## Drill 2 — Predict before running

Before executing code, predict:

```text
What will this return?
How many elements will this produce?
What exception will occur?
How many times will this loop execute?
```

Then run it.

## Drill 3 — Test before/after

For one small function:

```text
write test
implement
run test
break code
run test
fix code
```

## Drill 4 — Complexity awareness

For every `itertools` exercise ask:

> How quickly does the number of results grow?

You do not need formal Big-O mastery yet.

## Drill 5 — Choose the simplest tool

Ask:

```text
Could a normal dict solve this?
Would Counter express the intent better?
Would defaultdict remove unnecessary branching?
Is a tuple enough?
Would namedtuple improve readability?
Does order matter?
```

---

# Testing Muscle-Memory Check

At the end of the week, write these from memory.

## Basic test

```python
def test_something():
    result = ...
    assert result == ...
```

## Parametrized test

```python
@pytest.mark.parametrize(
    "input_value, expected",
    [
        (..., ...),
        (..., ...),
    ],
)
def test_something(input_value, expected):
    ...
```

## Exception test

```python
def test_invalid_input():
    with pytest.raises(SomeException):
        ...
```

The objective is not perfect memorisation. It is reducing the friction of retrieving these patterns.

---

# Week 3 Self-Assessment

Score yourself from 1–5.

| Skill | Score |
|---|---:|
| `Counter` | /5 |
| `defaultdict` | /5 |
| `namedtuple` | /5 |
| `permutations` | /5 |
| `combinations` | /5 |
| Choosing the right collection | /5 |
| Understanding combinatorial growth | /5 |
| Writing pytest tests | /5 |
| `pytest.mark.parametrize` | /5 |
| `pytest.raises` | /5 |
| Predicting code behaviour | /5 |
| Identifying unnecessary work | /5 |
| Designing clean contracts | /5 |
| Refactoring | /5 |

---

# Week 3 Reflection

Answer honestly.

1. Which built-in module felt most natural?
2. Which one required the most repetition?
3. Could I write `Counter` from memory?
4. Could I write `defaultdict` from memory?
5. Can I explain permutations vs combinations without looking it up?
6. Did I use `namedtuple` because it was appropriate, or simply because the exercise required it?
7. Did I write tests while developing, or only afterwards?
8. Did parametrization start feeling more natural?
9. Did `pytest.raises()` become easier to write?
10. Where did I identify unnecessary repeated work?
11. Which function has the clearest data contract?
12. Which function would I refactor if I had another hour?

---

# Week 3 → Week 4 Gate

Move to Week 4 when you can:

- [ ] Recognise a frequency-counting problem and consider `Counter`.
- [ ] Recognise a grouping/accumulation problem and consider `defaultdict`.
- [ ] Explain when a fixed record representation is useful.
- [ ] Explain permutations vs combinations.
- [ ] Predict combinatorial growth at a basic level.
- [ ] Write a small function using each major concept.
- [ ] Write at least one unit test for each concept.
- [ ] Use `pytest.mark.parametrize` when multiple inputs exercise one behaviour.
- [ ] Use `pytest.raises()` for expected exceptions.
- [ ] Explain the input/output contract of your capstone.
- [ ] Identify at least one performance consideration.
- [ ] Refactor one working implementation into a cleaner version.

You do **not** need perfect confidence.

The goal is enough familiarity to move forward while continuing testing as a permanent habit.

---

# ⭐ Week 3 Golden Rule

> **Don't memorise Python's built-in modules. Learn to recognise the problem they solve.**

And keep the Week 2.5 principle:

> **First make it correct. Then make the contract clear. Then make it testable. Then look for unnecessary work.**

Week 3 adds one more question:

> **“Is there a standard Python abstraction that expresses this more clearly?”**
