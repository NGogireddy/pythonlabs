# 🚀 Week 2.5 --- Python Engineering: Data Contracts, Testing & Performance

**Quantum Computing Career Transition --- Python Fluency Phase**

**Candidate Profile:** Solution Architect \| 20+ Years Enterprise
Experience \| Mainframes \| Cloud Migration \| PySpark

**Week:** Consolidation Week --- between Week 2 and Week 3\
**Duration:** 7 Days\
**Daily Practice:** 45--60 minutes

------------------------------------------------------------------------

# 🎯 Week Mission

Week 2 proved that you can build a working Python application.

This week changes the question:

> **Can I design the code so that another engineer can understand, test,
> change and trust it?**

The focus is deliberately narrow:

1.  **Clean data contracts**
2.  **Separation of validation and business logic**
3.  **Unit testing with pytest**
4.  **Better-performing Python solutions**
5.  **Refactoring crude working code into maintainable code**
6.  **Designing and implementing a new capstone independently**

Do not try to learn new Python libraries this week.

The objective is to strengthen engineering judgement before moving to
Week 3.

------------------------------------------------------------------------

# 🧠 What You Should Be Able to Do by the End of the Week

You should be comfortable answering:

-   What does this function accept?
-   What does it return?
-   What happens when the input is invalid?
-   Which failures are expected exceptions?
-   Which failures should be allowed to propagate?
-   Where does validation happen?
-   Where does business logic happen?
-   Can I test this function without reading files?
-   Can I test failure cases without running the entire application?
-   Am I processing the same data more than once unnecessarily?
-   Can I explain why one implementation is more efficient than another?
-   Can I refactor without changing behaviour?

------------------------------------------------------------------------

# 🧱 The Engineering Model for This Week

Use this mental model throughout the week:

``` text
External Input
     ↓
Load
     ↓
Structural Validation
     ↓
Domain Validation
     ↓
Clean Data Contract
     ↓
Business Processing
     ↓
Result Contract
     ↓
Report / Output
```

The important idea is that each stage should have a clear
responsibility.

Avoid:

``` text
main()
 ├── open file
 ├── parse JSON
 ├── validate
 ├── calculate
 ├── catch every exception
 ├── print everything
 └── write output
```

Prefer small functions with explicit contracts.

------------------------------------------------------------------------

# 📐 Data Contract Principle

For every important function, write down:

``` text
Function:
Input:
Output:
Valid input:
Invalid input:
Exceptions:
Side effects:
```

Example:

``` text
Function:
    validate_reading

Input:
    object

Output:
    float

Valid input:
    numeric value between 0 and 1 inclusive

Invalid input:
    None
    string
    negative value
    value greater than 1

Exceptions:
    InvalidQuantumReadingError

Side effects:
    None
```

The exact implementation can change.

The contract should remain clear.

------------------------------------------------------------------------

# 📅 DAY 1 --- Function Contracts & Clean Boundaries

## 🎯 Objective

Learn to design functions before writing their implementation.

------------------------------------------------------------------------

## 🧠 Recall Drill

Take three functions from your Week 2 capstone.

For each one, write:

``` text
Input
Output
Exceptions
Side effects
```

Do this before opening the implementation.

------------------------------------------------------------------------

## 🧪 Exercise 1 --- Contract Review

Review these conceptual functions:

``` python
load_sensor_data()
validate_sensor_data()
validate_reading()
process_readings()
generate_report()
```

For each, decide:

-   What should it receive?
-   What should it return?
-   Should it raise an exception?
-   Should it print anything?
-   Should it access the filesystem?
-   Should it modify global state?

------------------------------------------------------------------------

## 🧪 Exercise 2 --- Remove Hidden Responsibilities

Find one Week 2 function that performs more than one responsibility.

Refactor it.

For example:

``` text
load + validate + process
```

should become:

``` text
load
validate
process
```

Do not add unnecessary classes.

The goal is **clear boundaries**, not maximum abstraction.

------------------------------------------------------------------------

## 🚨 Failure Injection

Ask:

> What happens if the caller gives this function the wrong type?

Then test it deliberately.

------------------------------------------------------------------------

## 🧠 End-of-Day Question

> What makes a function easy to test?

------------------------------------------------------------------------

# 📅 DAY 2 --- `pytest` Fundamentals

## 🎯 Objective

Build muscle memory for writing unit tests.

------------------------------------------------------------------------

## 🧠 Syntax Drill

Write from memory:

``` python
def test_something():
    result = some_function(...)
    assert result == expected
```

Then practise:

``` python
assert ...
```

and:

``` python
with pytest.raises(SomeException):
    ...
```

------------------------------------------------------------------------

# 🧪 Exercise 1 --- Test `validate_reading`

Write tests for:

``` text
0.5       → valid
0.0       → valid
1.0       → valid
-0.2      → invalid
1.2       → invalid
None      → invalid
"hello"   → invalid
```

Your tests should verify both successful results and expected
exceptions.

------------------------------------------------------------------------

# 🧪 Exercise 2 --- Test Failure Behaviour

Add tests for:

``` text
missing file
malformed JSON
missing required field
invalid readings structure
```

Do not test everything through `main()`.

Test the smallest useful function.

------------------------------------------------------------------------

# 🧠 Important Principle

A unit test should ideally answer:

> **Did this one piece of behaviour work?**

rather than:

> Did the entire application run?

------------------------------------------------------------------------

# 🚨 Failure Injection

Intentionally introduce a bug into your implementation.

Run pytest.

Confirm that the test fails for the right reason.

Then restore the implementation.

------------------------------------------------------------------------

# 🧠 End-of-Day Question

> Why is a failing unit test useful information rather than simply a
> problem?

------------------------------------------------------------------------

# 📅 DAY 3 --- Testing Design & Data Contracts

## 🎯 Objective

Learn to use tests to define and protect your function contracts.

------------------------------------------------------------------------

# 🧪 Exercise 1 --- Contract-Driven Development

Choose:

``` python
validate_reading(value)
```

Write the expected behaviour first.

Example:

``` text
Input       Expected result
--------------------------------
0.5         0.5
0           0
1           1
-0.1        exception
1.1         exception
None        exception
"abc"       exception
```

Then make the implementation satisfy the tests.

------------------------------------------------------------------------

# 🧪 Exercise 2 --- Test the Processor

Create tests for:

``` python
process_reading(value)
```

Test:

-   normal input
-   boundary values
-   invalid input
-   expected exception
-   returned value

------------------------------------------------------------------------

# 🧪 Exercise 3 --- Test Isolation

Your validation tests should not need:

``` text
JSON files
filesystem
main()
print()
```

Your processor tests should not need to read a file.

Your file-loading tests should not need to perform calculations.

------------------------------------------------------------------------

# 🧠 Architecture Question

Why does separating:

``` text
load_sensor_data()
```

from:

``` text
validate_sensor_data()
```

make testing easier?

------------------------------------------------------------------------

# 📅 DAY 4 --- Performance & Avoiding Repeated Work

## 🎯 Objective

Start developing performance awareness without premature optimisation.

Your goal is not to make everything "fast".

Your goal is to recognise unnecessary work.

------------------------------------------------------------------------

# 🧪 Exercise 1 --- Find Repeated Work

Return to your Week 2 code.

Look for:

-   the same list being iterated multiple times
-   validation performed more than once
-   repeated conversions
-   unnecessary intermediate lists
-   repeated file reads
-   calculations that could be performed once

Document at least three examples.

------------------------------------------------------------------------

# 🧪 Exercise 2 --- Compare Implementations

Take a small dataset and compare two approaches.

Example:

``` python
valid = list(filter(validate_reading, readings))
invalid = list(filter(is_invalid, readings))
```

versus a single pass:

``` python
valid = []
invalid = []

for reading in readings:
    ...
```

Do not assume which is better.

Explain:

-   number of passes
-   readability
-   memory behaviour
-   duplicated work
-   maintainability

------------------------------------------------------------------------

# 🧪 Exercise 3 --- Scale the Data

Generate:

``` text
100 records
10,000 records
100,000 records
```

Run your processing approach against each.

You do not need sophisticated benchmarking yet.

Use a simple timing approach and record observations.

------------------------------------------------------------------------

# 🧠 Important Principle

Remember:

> **Readable code first. Remove unnecessary work when you can identify
> it.**

Do not optimise code merely because it looks different.

------------------------------------------------------------------------

# 🚨 Failure Injection

Ask:

> What happens to this implementation when the input grows from 8
> records to 100,000?

------------------------------------------------------------------------

# 📅 DAY 5 --- Refactor the Week 2 Capstone

## 🎯 Objective

Turn your existing working capstone into a cleaner implementation.

Do not add new functionality.

This is a refactoring exercise.

------------------------------------------------------------------------

# 🧪 Step 1 --- Establish Contracts

Document contracts for:

``` python
load_sensor_data()
validate_sensor_data()
validate_reading()
process_readings()
generate_report()
```

------------------------------------------------------------------------

# 🧪 Step 2 --- Fix the Exception Model

Use a consistent model:

``` text
Valid reading
    ↓
return validated value

Invalid reading
    ↓
raise InvalidQuantumReadingError
```

Do not return exception objects as normal results.

------------------------------------------------------------------------

# 🧪 Step 3 --- Separate Concerns

Aim for:

``` text
main()
  ↓
load_sensor_data()
  ↓
validate_sensor_data()
  ↓
process_readings()
  ↓
generate_report()
```

`main()` should orchestrate.

It should not contain all the business logic.

------------------------------------------------------------------------

# 🧪 Step 4 --- Add Tests

Create tests for:

``` text
valid reading
negative reading
None
value > 1
invalid JSON
missing field
invalid readings collection
missing file
empty readings
```

------------------------------------------------------------------------

# 🧪 Step 5 --- Review the Code

Ask:

-   Is every function doing one clear job?
-   Are names meaningful?
-   Are exceptions specific?
-   Are errors handled at the correct layer?
-   Are there repeated calculations?
-   Are files opened safely?
-   Can the core processing be tested without filesystem access?
-   Can I explain the data contract for every important function?

------------------------------------------------------------------------

# 📅 DAY 6 --- New Capstone Design

## 🎯 Objective

Build a completely different problem using the same engineering
principles.

Do not copy the Week 2 sensor application.

------------------------------------------------------------------------

# 🚀 CAPSTONE --- Quantum Experiment Results Processor

You are given results from multiple simulated quantum experiments.

Create:

``` text
quantum_results.json
```

Example:

``` json
{
    "experiment_id": "EXP-001",
    "backend": "simulator",
    "shots": 1000,
    "results": [
        {"state": "00", "count": 482},
        {"state": "11", "count": 498},
        {"state": "01", "count": 12},
        {"state": "10", "count": 8}
    ]
}
```

------------------------------------------------------------------------

# 🎯 Requirements

## 1. Load the JSON

Use:

``` python
pathlib
with open(...)
json.load()
```

------------------------------------------------------------------------

## 2. Define a Data Contract

The input must contain:

``` text
experiment_id
backend
shots
results
```

Each result must contain:

``` text
state
count
```

------------------------------------------------------------------------

## 3. Validate the Experiment

Rules:

``` text
experiment_id → non-empty string
backend       → non-empty string
shots         → positive integer
results       → list
state         → non-empty string
count         → non-negative integer
```

Create appropriate custom exceptions.

------------------------------------------------------------------------

# 4. Process the Results

Calculate:

``` text
total measured shots
number of unique states
most frequently observed state
probability of each state
```

For example:

``` text
00 → 48.2%
11 → 49.8%
01 → 1.2%
10 → 0.8%
```

------------------------------------------------------------------------

# 5. Produce a Result Contract

Your processing function should return a clearly defined structure.

For example:

``` text
{
    "experiment_id": ...,
    "total_shots": ...,
    "unique_states": ...,
    "most_common_state": ...,
    "probabilities": ...
}
```

Choose the exact structure yourself.

Document the contract.

------------------------------------------------------------------------

# 6. Invalid Records

The program should distinguish between:

``` text
invalid experiment structure
```

and:

``` text
invalid individual result
```

One bad result should not necessarily destroy the entire experiment.

Define the behaviour explicitly.

------------------------------------------------------------------------

# 7. Unit Tests

Write pytest tests for at least:

``` text
valid experiment
missing experiment_id
missing shots
invalid shots
missing results
invalid result state
negative count
zero count
multiple states
single state
empty results
```

------------------------------------------------------------------------

# 8. Performance Challenge

Generate an experiment containing:

``` text
10,000 result records
```

Then ask:

> Am I unnecessarily processing the same collection multiple times?

Try to design the core aggregation so that the important calculations
can be performed efficiently.

------------------------------------------------------------------------

# 9. Architecture Challenge

Your final application should conceptually resemble:

``` text
quantum_results.json
        ↓
     Load
        ↓
Structural Validation
        ↓
Record Validation
        ↓
 Clean Data Contract
        ↓
   Aggregation
        ↓
 Result Contract
        ↓
     Report
```

------------------------------------------------------------------------

# 📅 DAY 7 --- Review, Refactor & Engineering Interview

## 🎯 Objective

Prove that you understand the concepts rather than simply completing the
capstone.

------------------------------------------------------------------------

# 🧪 Part 1 --- Refactor Without Changing Behaviour

Take your Day 6 implementation.

Identify:

-   one overly large function
-   one unclear variable name
-   one duplicated operation
-   one unnecessary loop
-   one unclear exception
-   one missing test

Fix them.

------------------------------------------------------------------------

# 🧪 Part 2 --- Test Your Own Tests

Break the implementation deliberately.

Examples:

``` text
change > to >=
remove a validation
change a probability calculation
return the wrong state
```

Confirm that your tests detect the regression.

------------------------------------------------------------------------

# 🧠 Interview Drills

Answer these without looking anything up.

### Question 1

What is a data contract?

### Question 2

What should a function's contract tell its caller?

### Question 3

When should a function raise an exception rather than return an error
value?

### Question 4

Why should validation and processing be separated?

### Question 5

What makes a unit test different from an integration test?

### Question 6

Why is testing failure paths important?

### Question 7

How can repeated iteration over the same data affect performance?

### Question 8

When would you choose a single-pass loop over several transformations?

### Question 9

Why can returning from `finally` be dangerous?

### Question 10

How would you make your capstone easier for another developer to
maintain?

------------------------------------------------------------------------

# 🏆 WEEK COMPLETION CRITERIA

Do not judge success by:

> "Did I finish the capstone?"

Judge success using these criteria.

-   [ ] I can define a function's input/output contract before coding.
-   [ ] I can distinguish structural validation from business
    validation.
-   [ ] I can design a clean exception contract.
-   [ ] I no longer return exception objects as normal results.
-   [ ] I understand where exceptions should be caught.
-   [ ] I can write basic pytest tests from memory.
-   [ ] I can test expected exceptions.
-   [ ] I can test boundary values.
-   [ ] I can test failure scenarios independently.
-   [ ] I can explain the difference between unit and integration
    testing.
-   [ ] I can identify duplicated work in Python code.
-   [ ] I can recognise unnecessary multiple passes over data.
-   [ ] I can reason about memory and performance at a basic level.
-   [ ] I can refactor without changing behaviour.
-   [ ] I can build a new capstone without copying the Week 2 structure
    blindly.
-   [ ] I can explain the data contract of my capstone.
-   [ ] I can explain why my design is cleaner than my first
    implementation.

------------------------------------------------------------------------

# 📊 WEEK SELF-ASSESSMENT

Score yourself from 1--5.

  Skill                         Before Week   After Week
  --------------------------- ------------- ------------
  Function contracts                     /5           /5
  Input validation design                /5           /5
  Exception design                       /5           /5
  pytest fundamentals                    /5           /5
  Failure-path testing                   /5           /5
  Test isolation                         /5           /5
  Performance awareness                  /5           /5
  Avoiding repeated work                 /5           /5
  Refactoring                            /5           /5
  Code organisation                      /5           /5
  Confidence writing Python             /10          /10

------------------------------------------------------------------------

# 🧠 ARCHITECT'S REFLECTION

Answer these at the end of the week.

### 1. What changed between my first Week 2 implementation and my refactored implementation?

### 2. Which part of designing a data contract was hardest?

### 3. Which function became significantly easier to test after refactoring?

### 4. What did I learn about exceptions that I did not understand before Week 2?

### 5. What duplicated work did I discover in my original implementation?

### 6. Which performance improvement actually mattered?

### 7. Which optimisation was unnecessary?

### 8. What makes my new capstone cleaner than my Week 2 capstone?

### 9. Can I explain the code without reading it line by line?

### 10. What Python syntax still requires conscious thought?

------------------------------------------------------------------------

# 🚀 WEEK 2.5 → WEEK 3 GATE

Do not move to Week 3 simply because the seven days are complete.

Move forward when you can independently build this pattern:

``` text
External Input
      ↓
Clear Data Contract
      ↓
Structural Validation
      ↓
Domain Validation
      ↓
Custom Exceptions
      ↓
Clean Processing Function
      ↓
Clear Result Contract
      ↓
Unit Tests
      ↓
Performance Review
      ↓
Final Output
```

If you can do this on the new quantum experiment capstone **without
following a step-by-step tutorial**, Week 2.5 has done its job.

------------------------------------------------------------------------

# ⭐ WEEK 2.5 GOLDEN RULE

> **First make it correct. Then make the contract clear. Then make it
> testable. Then look for unnecessary work.**

Do not optimise prematurely.

Do not create abstractions simply to make the code look "enterprise".

Do not add classes when a small function is clearer.

Your goal this week is to develop the instinct to recognise:

> **"This works, but I can explain a cleaner contract and a simpler
> implementation."**

That is the engineering skill we want to strengthen before Week 3.
