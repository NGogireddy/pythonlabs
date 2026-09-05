# Week 4 — Python Engineering: Iteration, Generators, and Clean Data Pipelines

## 🎯 Week 4 Goal

This week moves from Python collections and combinatorics into an important engineering skill:

> **Processing data efficiently without doing unnecessary work or loading everything into memory.**

You will learn:
- Iterators
- Generators
- Generator expressions
- `yield`
- `iter()` / `next()`
- `enumerate()`
- `zip()`
- `islice()`
- Lazy processing
- Pipeline-style composition

The emphasis is not on memorising APIs. The goal is to develop the instinct to ask:

> “Do I really need all this data in memory at once?”

and:

> “Can I process it incrementally?”

## 🧭 Week 4 Structure

| Day | Focus | Main Outcome |
|---|---|---|
| Day 1 | Iterables, iterators, `iter()` and `next()` | Understand the iterator protocol |
| Day 2 | Generators and `yield` | Build lazy data producers |
| Day 3 | Generator expressions | Write concise lazy transformations |
| Day 4 | `enumerate()`, `zip()`, `islice()` | Process streams cleanly |
| Day 5 | Generator pipelines | Compose lazy processing stages |
| Day 6 | Capstone implementation | Build a production-shaped data pipeline |
| Day 7 | Tests, refactor & engineering review | Make the solution cleaner and production-ready |

**Daily limit: 60 minutes.** Do not extend a session simply because an exercise is unfinished.

---

## 🧪 Testing Rule for Week 4

Continue the habit developed in Week 3:

> **Write tests while developing, not after everything is finished.**

Use:
- `pytest`
- `pytest.mark.parametrize`
- `pytest.raises` where appropriate
- fixtures where useful
- `tmp_path` when file-based testing is required

Do not force a fixture or parametrization when it makes a test worse.

The goal is testing judgement, not maximum pytest feature usage.

---

# DAY 1 — Iterables, Iterators, `iter()` and `next()`

## 🎯 Objective

Understand:
- iterable vs iterator
- iteration
- `iter()`
- `next()`
- `StopIteration`
- iterator state

You should be able to explain what Python is doing when you write:

```python
for item in items:
    ...
```

## 🔥 Drill — Predict Before Running

### Drill 1

```python
numbers = [10, 20, 30]
iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

Write down the output.

### Drill 2

```python
numbers = [10, 20]
iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

What happens on the third call?

### Drill 3

```python
numbers = [1, 2, 3]
iterator = iter(numbers)

for number in iterator:
    print(number)

print(next(iterator))
```

Explain why the final line behaves the way it does.

## 📚 Learn

Study `iter()`, `next()`, `StopIteration`, iterable vs iterator, and iterator state.

Pay particular attention to the fact that an iterator is **stateful**.

## 💻 Implement

Create:

```text
week4/
└── day1/
    ├── iterator_practice.py
    └── test_iterator.py
```

Implement:

```python
def consume_first_n(iterable, n):
    ...
```

Requirements:
- Accept any iterable.
- Return the first `n` items.
- Do not assume the input is a list.
- Do not modify the original iterable.
- Decide and document behaviour for `n == 0`, negative `n`, and an iterable shorter than `n`.

### Engineering question

Would you implement this using:

```python
list(iterable)[:n]
```

or by consuming the iterator incrementally?

Explain your choice.

## 🧪 Tests

Test:
- normal iterable
- tuple
- empty iterable
- `n == 0`
- iterable shorter than `n`
- invalid/negative `n` according to your contract
- at least one non-list iterable

## 📝 Reflection

1. What is the difference between an iterable and an iterator?
2. What state does an iterator maintain?
3. Why is converting everything to a list sometimes undesirable?
4. What did you choose for negative `n`, and why?

---

# DAY 2 — Generators and `yield`

## 🎯 Objective

Understand generators as **lazy producers of values**.

You should be able to explain why:

```python
def numbers():
    yield 1
    yield 2
    yield 3
```

does not immediately execute the body like a normal function call.

## 🔥 Drill — Predict the Execution

Before running:

```python
def generate_numbers():
    print("start")
    yield 1
    print("middle")
    yield 2
    print("end")

generator = generate_numbers()

print("A")
print(next(generator))
print("B")
print(next(generator))
print("C")
```

Predict the exact order of output. Then run it and compare.

## 📚 Learn

Study:
- generator functions
- `yield`
- generator objects
- lazy execution
- generator state
- `next()`
- `StopIteration`

Understand the difference between `return` and `yield`.

## 💻 Implement

Create:

```text
week4/
└── day2/
    ├── generator_practice.py
    └── test_generator.py
```

Implement:

```python
def generate_valid_results(results):
    ...
```

Assume each input item is a dictionary representing a result.

Define a contract such as:

```text
{
    "experiment_id": str,
    "state": str,
    "count": int
}
```

Only yield records satisfying your validation rules.

**Do not return a list. The function must be a generator.**

## 🧪 Tests

Test:
- all valid records
- mixture of valid/invalid records
- no valid records
- empty input
- generator output behaviour
- that values are produced incrementally

Use parametrization where it improves clarity.

## 📝 Reflection

1. When does the generator body actually execute?
2. Why can a generator be useful for large datasets?
3. What happens after the generator is exhausted?
4. Why might returning a list be inappropriate here?

---

# DAY 3 — Generator Expressions

## 🎯 Objective

Learn when a generator expression is appropriate and when a normal list comprehension is better.

Compare:

```python
[x * 2 for x in numbers]
```

with:

```python
(x * 2 for x in numbers)
```

## 🔥 Drill — Predict Memory Behaviour

Identify whether each expression creates the entire result immediately or produces values lazily:

```python
[x * 2 for x in range(10)]
```

```python
(x * 2 for x in range(10))
```

Then consider:

```python
sum(x * 2 for x in range(1_000_000))
```

Why does this not require a million-element result list?

## 📚 Learn

Study:
- generator expressions
- list comprehensions vs generator expressions
- lazy evaluation
- consuming generators
- one-time iteration

Important:

> A generator is not automatically “better”.

Choose based on how the data is consumed.

## 💻 Implement

Create:

```text
week4/
└── day3/
    ├── generator_expression_practice.py
    └── test_generator_expression.py
```

Implement:

```python
def sum_valid_counts(results):
    ...
```

The function should:
1. process records lazily where appropriate
2. ignore invalid records according to your contract
3. calculate the total count
4. avoid creating an unnecessary intermediate list

Also implement one transformation where you deliberately choose a **list** instead of a generator. Document why.

## 🧪 Tests

Test:
- normal records
- invalid records
- empty input
- all invalid input
- large/lazy input if practical

Focus on behaviour rather than implementation details.

## 📝 Reflection

1. When would you prefer a list comprehension?
2. When would you prefer a generator expression?
3. What does “lazy” mean in practical terms?
4. Did using a generator actually improve the solution, or did you use it just because this is Generator Week?

---

# DAY 4 — `enumerate()`, `zip()`, and `islice()`

## 🎯 Objective

Learn Python's built-ins for clean iteration without unnecessary indexing, list construction, or manual counters.

## 🔥 Drill — Replace the Manual Code

### Drill 1

Rewrite:

```python
index = 0

for result in results:
    print(index, result)
    index += 1
```

using the appropriate built-in.

### Drill 2

Rewrite:

```python
for i in range(len(states)):
    print(states[i], counts[i])
```

using the appropriate built-in.

### Drill 3

Given:

```python
results = range(1_000_000)
```

How would you process only the first 10 values without creating:

```python
list(results)[:10]
```

## 📚 Learn

Study:
- `enumerate()`
- `zip()`
- `itertools.islice()`

Understand:
- why `range(len(...))` is often unnecessary
- how `zip()` behaves with different lengths
- how `islice()` differs from normal slicing
- why iterators cannot always be sliced using `[:]`

## 💻 Implement

Create:

```text
week4/
└── day4/
    ├── iteration_tools.py
    └── test_iteration_tools.py
```

Implement:

```python
def pair_results(states, counts):
    ...
```

and:

```python
def first_n_results(results, n):
    ...
```

Requirements:

### `pair_results`
- pair corresponding state/count values
- define behaviour when lengths differ
- do not manually index the lists

### `first_n_results`
- work with any iterable
- process lazily
- do not convert the complete input into a list

## 🧪 Tests

Test:
- equal-length inputs
- different-length inputs
- empty inputs
- generator inputs
- `n == 0`
- `n` greater than available records

## 📝 Reflection

1. Why is `enumerate()` preferable to manually maintaining an index?
2. What happens when two inputs to `zip()` have different lengths?
3. Why is `islice()` useful for iterators?
4. Which of today's tools do you expect to use most often?

---

# DAY 5 — Generator Pipelines

## 🎯 Objective

Combine this week's concepts into a simple lazy-processing pipeline.

Think:

```text
Input
  ↓
Filter
  ↓
Transform
  ↓
Filter
  ↓
Consumer
```

without materialising every intermediate stage.

## 🔥 Drill — Trace the Pipeline

Consider:

```python
numbers = range(10)

pipeline = (
    number * 2
    for number in numbers
    if number % 2 == 0
)

print(next(pipeline))
print(next(pipeline))
```

Answer:
1. What values are produced?
2. When does multiplication happen?
3. Are all values processed before the first `next()`?
4. What happens if the consumer stops after two values?

## 📚 Learn

Study:
- chaining generators
- generator pipelines
- lazy filtering
- lazy transformation
- consumers such as `sum()`, `list()`, `any()`, `all()`

Think about where materialisation happens.

For example:

```python
list(pipeline)
```

is a deliberate decision to materialise the stream.

## 💻 Implement

Create:

```text
week4/
└── day5/
    ├── pipeline.py
    └── test_pipeline.py
```

Build a small pipeline for experiment/result records.

The pipeline should have at least three logical stages:

```text
raw records
    ↓
validation/filtering
    ↓
transformation
    ↓
aggregation/consumption
```

You may use:
- generators
- generator expressions
- `Counter`
- `defaultdict`
- `enumerate`
- `zip`
- `islice`

But only where they make the solution clearer.

### Important engineering rule

**Do not add a Week 4 concept just to demonstrate that you know it.**

If a list is genuinely the better choice at one stage, use a list and explain why.

## 🧪 Tests

Test:
- valid data
- invalid data
- empty data
- partially valid data
- generator input
- expected aggregation

At least one test should verify that the pipeline can consume an iterator/generator rather than requiring a list.

## 📝 Reflection

1. Where does laziness help?
2. Where does laziness make code harder to understand?
3. Where did you deliberately materialise data?
4. Did your pipeline avoid unnecessary intermediate collections?
5. If the input contained 10 million records, what would concern you?

---

# DAY 6 — CAPSTONE: Experiment Result Streaming Pipeline

## 🎯 Objective

Build a **production-shaped, not production-sized** data-processing component.

You will receive a potentially large stream of experiment result records and produce a summary **without loading the entire dataset into memory**.

## 🧩 Capstone Problem

You are given experiment result records from a quantum experimentation platform.

The input is an iterable of dictionaries:

```python
{
    "experiment_id": "exp-001",
    "backend": "simulator",
    "state": "00",
    "count": 512
}
```

The input may be:
- a list
- a generator
- a file-backed iterator
- another streaming source

Your component must process records incrementally.

For each valid record:
1. validate the record
2. keep valid records
3. aggregate counts by backend and state
4. track the number of invalid records
5. avoid materialising the complete input

Invalid records should not stop processing of later valid records.

## 📜 Input Contract

Each record should contain:

```text
experiment_id : non-empty string
backend       : non-empty string
state         : non-empty string
count         : non-negative integer
```

You should decide and document:
- whether extra fields are allowed
- whether missing fields are invalid
- whether `bool` should be accepted as an integer count
- how invalid records are represented/reported

## 📤 Expected Output

Return a clearly defined summary structure.

For example:

```text
{
    "totals": {
        ("simulator", "00"): 1024,
        ("simulator", "01"): 512
    },
    "valid_records": 3,
    "invalid_records": 1
}
```

You may choose a different structure if you can justify it.

The important part is that the contract is explicit.

## 🚦 Acceptance Criteria

Your solution must:
- process arbitrary iterables
- not require the input to be a list
- process records incrementally
- validate records
- continue after invalid records
- aggregate valid records
- clearly separate validation from aggregation where practical
- have unit tests
- handle empty input
- handle all-invalid input
- avoid global mutable state

### Performance requirement

Do not do this:

```python
records = list(input_records)
```

unless you can justify why it is necessary.

For this problem, it should **not** be necessary.

## 🧠 Concepts Available

### Must use
- generators/iterators
- lazy processing

### Consider using
- `Counter`
- `defaultdict`
- `enumerate()`
- generator expressions
- small helper functions

### Do not use unless justified
- `namedtuple`
- permutations
- combinations
- unnecessary list conversions
- global state

The goal is to practise **engineering judgement**.

## 🏗️ Architecture Constraint

Do **not** design a large application.

Keep it small.

Aim for something like:

```text
input
  ↓
validation
  ↓
processing
  ↓
summary
```

You decide the exact function boundaries.

## 🧪 Testing Requirements

Write tests for:
- valid record
- invalid record
- mixed valid/invalid records
- empty input
- all invalid input
- multiple backends
- multiple states
- zero count
- generator input
- large-ish lazy input where practical

Use parametrization where it improves the test suite.

Use `pytest.raises` only where your chosen contract requires exceptions.

## ⏱️ Timebox

**60 minutes maximum.**

Do not attempt to make this production-sized.

The objective is to demonstrate good engineering decisions within a small scope.

## 📝 Day 6 Reflection

Before moving to Day 7, record:
1. What is the input contract?
2. What is the output contract?
3. Where is the solution lazy?
4. Where is data materialised, if anywhere?
5. What happens when a record is invalid?
6. Why did you choose your data structures?
7. What would become a problem at 10 million records?

---

# DAY 7 — Test, Refactor & Engineering Review

## 🎯 Objective

Day 7 is not another feature day.

It is for turning:

> “It works”

into:

> “I understand why it works, and the design is maintainable.”

## 🔥 Drill — Code Review Without Changing Anything

Before modifying your capstone, read it as if another architect/developer wrote it.

Identify:
- unclear contracts
- mixed responsibilities
- unnecessary materialisation
- unnecessary loops
- hidden state
- unnecessary exception handling
- unclear names
- duplicated logic
- tests too tightly coupled to implementation

Write down your findings first.

## 🧪 Test Review

Check:

### Behaviour
Do tests prove the important business behaviour?

### Edge cases
Have you covered:
- empty input?
- all-invalid input?
- zero values?
- generator input?
- mixed valid/invalid input?

### Parametrization
Did you use it where it improves readability?

### Exceptions
Are exceptions tested only where the contract says they should occur?

### Test isolation
Can every test run independently?

## 🔧 Refactoring Exercise

Choose **2–4 improvements**. Do not rewrite everything.

Possible areas:
- function boundaries
- naming
- contract clarity
- validation
- aggregation
- generator usage
- test structure
- error representation
- removing unnecessary work

For each change, record:

```text
Before:
...

Problem:
...

After:
...

Why:
...
```

## ⚡ Performance Review

Think about:

```text
N = 10 records
N = 10,000 records
N = 10,000,000 records
```

Ask:
1. What is the approximate time complexity?
2. What is the memory complexity?
3. Does the input need to be fully materialised?
4. What data structure dominates memory?
5. Where could unnecessary work appear?

You do not need formal benchmarking unless useful.

## 🏆 Final Capstone Review

Score yourself from 1–5.

| Area | Score |
|---|---:|
| Python concepts | /5 |
| Iterator/generator understanding | /5 |
| Lazy processing | /5 |
| Data contracts | /5 |
| Test quality | /5 |
| Test-first habit | /5 |
| Error handling | /5 |
| Performance awareness | /5 |
| Code organisation | /5 |
| Engineering judgement | /5 |
| Refactoring | /5 |

---

# 🚪 WEEK 4 GATE

Before proceeding to Week 5, you should be able to answer **yes** to most of these.

### Python
- [ ] I can explain iterable vs iterator.
- [ ] I understand `iter()` and `next()`.
- [ ] I understand `StopIteration`.
- [ ] I can write a generator using `yield`.
- [ ] I understand generator expressions.
- [ ] I understand lazy execution.
- [ ] I can use `enumerate()` naturally.
- [ ] I can use `zip()` naturally.
- [ ] I understand when `islice()` is useful.

### Engineering
- [ ] I can decide between list and generator based on the problem.
- [ ] I think about memory usage when processing data.
- [ ] I avoid unnecessary materialisation.
- [ ] I can design an explicit input/output contract.
- [ ] I can separate validation from processing.
- [ ] I can explain the complexity of my solution.

### Testing
- [ ] I write tests while developing.
- [ ] `pytest.mark.parametrize` feels natural.
- [ ] I can use `pytest.raises` when appropriate.
- [ ] I can test generator/iterator behaviour.
- [ ] My tests focus primarily on behaviour rather than implementation details.

### Engineering judgement
- [ ] I don't force a concept into the solution just because I learned it this week.
- [ ] I can explain why I chose a particular data structure.
- [ ] I can identify unnecessary work.
- [ ] I can perform a small refactor without changing behaviour.
- [ ] I can explain what would happen if the dataset became 1,000× larger.

---

# 📌 Week 4 Key Takeaways

By the end of this week, you should have moved from:

```text
“I know Python collections”
```

towards:

```text
“I can design a Python data-processing flow
that is conscious of memory, execution,
contracts, testing, and maintainability.”
```

That engineering judgement is more important than memorising every iterator utility.

---

# 📁 Suggested Repository Structure

```text
pythonlabs/
└── week4/
    ├── day1/
    │   ├── iterator_practice.py
    │   └── test_iterator.py
    ├── day2/
    │   ├── generator_practice.py
    │   └── test_generator.py
    ├── day3/
    │   ├── generator_expression_practice.py
    │   └── test_generator_expression.py
    ├── day4/
    │   ├── iteration_tools.py
    │   └── test_iteration_tools.py
    ├── day5/
    │   ├── pipeline.py
    │   └── test_pipeline.py
    ├── day6/
    │   ├── capstone.py
    │   └── test_capstone.py
    └── day7/
        └── review.md
```

---

# 🌱 Personal Rule for Week 4

Do not chase completion.

A good Week 4 is one where:
- you understand the concept
- you can implement it without copying
- you test it
- you can explain your design
- you know when **not** to use it

**One focused hour is enough.**
