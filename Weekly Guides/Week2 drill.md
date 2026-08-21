# 🚀 Week 2 — Robust Error Handling & File I/O

**Quantum Computing Career Transition — Python Fluency Phase**

**Candidate Profile:** Solution Architect | 20+ Years Enterprise Experience | Mainframes | Cloud Migration | PySpark

**Week:** 2 of 12 — Python Fluency Bootstrap
**Topic:** Robust Error Handling & File I/O
**Duration:** 7 Days
**Daily Practice:** 30–45 minutes
**Primary Goal:** Build muscle memory for defensive, idiomatic Python when dealing with unreliable input, files, external data, and runtime failures.

---

# 🎯 Week 2 Mission

Week 1 focused on:

> **How can I manipulate data efficiently using Python syntax?**

Week 2 changes the question to:

> **What happens when the data, file, or operation is not what I expected?**

This is an important transition from learning Python syntax to thinking like a production Python engineer.

By the end of Week 2, you should be comfortable writing Python programs that can:

* Detect expected runtime failures.
* Catch specific exceptions.
* Use `try`, `except`, `else`, and `finally` correctly.
* Raise exceptions deliberately.
* Create custom domain exceptions.
* Read and write files safely.
* Use context managers.
* Work with `pathlib`.
* Read and write JSON.
* Process CSV data.
* Validate external data.
* Separate validation from business logic.
* Continue processing when an individual input record is invalid.
* Produce useful error messages.
* Avoid hiding programming defects behind broad `except Exception`.
* Design small functions that are easy to test.

---

# 🧠 Week 2 Learning Philosophy

Continue the successful Week 1 pattern.

Every day has **four layers**:

## Layer 1 — Muscle Memory

Write small examples from memory.

## Layer 2 — Controlled Exercise

Solve the day's prescribed exercise.

## Layer 3 — Variation Challenge

Change the input, constraints, or requirements.

## Layer 4 — Failure Injection

Intentionally break your program and observe how it behaves.

The fourth layer is particularly important this week.

Your objective is not:

> "Write code that works."

Your objective is:

> **"Write code that behaves predictably when things go wrong."**

---

# ⏱️ Recommended Daily Routine

## 5 Minutes — Recall Drill

Without looking at notes, write the syntax you learned.

Example:

```python
try:
    ...
except ValueError:
    ...
else:
    ...
finally:
    ...
```

Then explain each section in your own words.

---

## 15 Minutes — Main Exercise

Complete the day's challenge without copying a solution.

---

## 10 Minutes — Variation Challenge

Change something significant:

* input type
* data size
* file contents
* missing values
* malformed data
* business rule
* exception condition

---

## 5–10 Minutes — Failure Injection

Deliberately make the program fail.

Ask:

1. What exception occurred?
2. Why did it occur?
3. Should I catch it?
4. If yes, where?
5. What should the program do next?
6. Am I accidentally hiding a real programming bug?

---

# 📅 DAY 1 — `try` / `except`

## 🎯 Learning Objective

Understand how Python exceptions work and learn to catch **specific expected failures**.

---

## 🧠 Concepts

Study and practise:

```python
try:
    ...
except ValueError:
    ...
```

Also understand:

```python
ValueError
TypeError
ZeroDivisionError
FileNotFoundError
KeyError
IndexError
```

You do not need to memorise every Python exception.

You need to understand the principle:

> **Catch the failure you expect.**

---

# 🔥 Muscle Memory Drill

Without looking at documentation, write a program that:

1. Accepts a string.
2. Converts it to `float`.
3. Prints the converted value.
4. Handles invalid numeric input.

Test:

```text
0.75
1.25
-0.5
100
abc
hello
```

---

# 🧪 Challenge 1 — Sensor Reading

Create:

```text
sensor_reader.py
```

The program should accept a sensor reading as input.

Valid:

```text
0.5
0.75
1.0
```

Invalid:

```text
abc
hello
None
```

The program should not crash when the user enters invalid text.

---

# 🧪 Challenge 2 — Quantum-Style Validation

Add these rules:

* Input must be numeric.
* Input must not be negative.
* Input must not exceed `1.0`.

Example:

```text
0.75 → Valid
1.0  → Valid
-0.2 → Invalid
1.5  → Invalid
abc  → Invalid
```

---

# 🚨 Failure Injection

Deliberately enter:

```text
abc
```

Then deliberately enter:

```text
1.5
```

Then deliberately enter:

```text
-10
```

Notice that these are **different kinds of failure**:

* `abc` → conversion failure.
* `1.5` → business-rule failure.
* `-10` → business-rule failure.

This distinction will become important when you create custom exceptions.

---

# 🧠 End-of-Day Question

Be able to answer:

> What is the difference between an exception caused by Python's runtime and an invalid value caused by my application's business rules?

---

# 📅 DAY 2 — `else` / `finally` / `raise`

## 🎯 Learning Objective

Understand the complete exception-handling lifecycle.

---

# 🧠 Syntax Drill

Write this structure from memory:

```python
try:
    ...
except ValueError:
    ...
else:
    ...
finally:
    ...
```

Then explain:

### `try`

Code that may fail.

### `except`

What to do when an expected exception occurs.

### `else`

Code that should execute only when the `try` block succeeds.

### `finally`

Code that should execute regardless of success or failure.

---

# 🧪 Challenge 1 — File Processing Simulation

Create a function:

```python
process_reading(value)
```

It should:

1. Convert the value to `float`.
2. Validate the range.
3. Calculate the square.
4. Return the result.

Use appropriate exception handling.

---

# 🧪 Challenge 2 — Introduce `raise`

Instead of silently accepting invalid values, deliberately raise an exception.

For example:

```python
if value < 0:
    raise ValueError("Reading cannot be negative")
```

---

# 🧪 Variation Challenge

Change the validation rules:

### Version A

Valid range:

```text
0 ≤ value ≤ 1
```

### Version B

Valid range:

```text
-1 ≤ value ≤ 1
```

### Version C

Only strictly positive values:

```text
0 < value ≤ 1
```

Do not rewrite the entire program.

Modify the validation logic.

---

# 🚨 Failure Injection

Make the program fail at each stage:

```text
Conversion
Validation
Calculation
```

Determine which exception is produced.

---

# 🧠 End-of-Day Question

Why is this potentially better:

```python
try:
    value = float(raw_value)
except ValueError:
    ...
else:
    process(value)
```

than putting everything inside the `try` block?

---

# 📅 DAY 3 — File I/O & Context Managers

## 🎯 Learning Objective

Build muscle memory for safely reading and writing files.

---

# 🧠 Syntax Drill

Write from memory:

```python
with open("data.txt", "r") as file:
    contents = file.read()
```

Then practise:

```python
file.readlines()
```

and:

```python
for line in file:
    ...
```

---

# 📄 Create Your Dataset

Create:

```text
quantum_sensor_data.txt
```

Contents:

```text
0.25
0.81
invalid
1.44
None
0.36
-0.20
0.49
```

---

# 🧪 Challenge 1 — File Reader

Write a program that:

1. Opens the file.
2. Reads every line.
3. Removes whitespace.
4. Attempts to convert each value to `float`.
5. Stores valid values.
6. Reports invalid values.

Expected valid data:

```text
0.25
0.81
1.44
0.36
0.49
```

---

# 🧪 Challenge 2 — Preserve Invalid Records

Instead of simply ignoring bad values, create two collections:

```python
valid_readings = []
invalid_readings = []
```

For example:

```text
Valid:
0.25
0.81
1.44
0.36
0.49

Invalid:
invalid
None
-0.20
```

---

# 🧪 Challenge 3 — Produce a Report

Generate output such as:

```text
Quantum Sensor Processing Report
--------------------------------
Total records : 8
Valid records : 5
Invalid records: 3
```

---

# 🚨 Failure Injection

Test:

* Empty file.
* Missing file.
* File containing only invalid data.
* File containing blank lines.
* File containing spaces.
* File containing very large values.

---

# 🧠 Interview Question

Be able to explain:

> Why is `with open(...)` preferable to manually calling `open()` and `close()`?

---

# 📅 DAY 4 — `pathlib`

## 🎯 Learning Objective

Learn modern Python filesystem handling.

---

# 🧠 Muscle Memory

Write from memory:

```python
from pathlib import Path
```

Then:

```python
data_file = Path("data") / "quantum_sensor_data.txt"
```

Practise:

```python
data_file.exists()
data_file.name
data_file.parent
data_file.suffix
```

Also investigate:

```python
data_file.is_file()
```

---

# 🧪 Challenge 1 — Build a Data Directory

Create:

```text
week2/
    data/
        quantum_sensor_data.txt
```

Use Python to construct the path.

Do not hard-code:

```text
"week2/data/quantum_sensor_data.txt"
```

Instead use `Path`.

---

# 🧪 Challenge 2 — File Discovery

Write a program that:

1. Looks inside the `data` directory.
2. Finds all `.txt` files.
3. Prints their filenames.
4. Processes each file.

Investigate:

```python
Path.glob()
```

---

# 🧪 Challenge 3 — Multiple Sensor Files

Create:

```text
sensor_001.txt
sensor_002.txt
sensor_003.txt
```

Each file contains different readings.

Write one program that processes all of them.

---

# 🚨 Failure Injection

Test:

* Directory doesn't exist.
* File doesn't exist.
* Wrong file extension.
* Empty directory.
* Multiple files.

---

# 🧠 Architecture Question

Why is using:

```python
Path("data") / filename
```

more maintainable than scattering filesystem strings throughout your application?

---

# 📅 DAY 5 — JSON

## 🎯 Learning Objective

Learn to process structured data received from external systems.

This is the point where your Python practice begins to resemble cloud/data engineering.

---

# 📄 Create `sensor_data.json`

```json
{
    "device_id": "Q-SENSOR-001",
    "backend": "simulator",
    "location": "LAB-01",
    "readings": [
        0.25,
        0.81,
        null,
        -0.20,
        1.44,
        0.36
    ]
}
```

---

# 🧠 Muscle Memory

Practise:

```python
import json
```

Then:

```python
with open("sensor_data.json", "r") as file:
    data = json.load(file)
```

Investigate:

```python
data["device_id"]
data["backend"]
data["readings"]
```

---

# 🧪 Challenge 1 — Extract Metadata

Print:

```text
Device ID : Q-SENSOR-001
Backend   : simulator
Location  : LAB-01
```

---

# 🧪 Challenge 2 — Process Readings

Extract:

```python
readings = data["readings"]
```

Then process the readings using the Week 1 techniques.

Your program should:

1. Remove `None`.
2. Remove negative numbers.
3. Square valid values.
4. Print the results.

---

# 🧪 Challenge 3 — Validate JSON Structure

What happens if the JSON doesn't contain:

```text
device_id
```

or:

```text
readings
```

Experiment with:

```python
KeyError
```

---

# 🧪 Challenge 4 — Malformed JSON

Create an invalid JSON file.

For example, deliberately remove a comma.

Run your program.

Determine which exception occurs.

---

# 🚨 Failure Injection Matrix

Test:

| Failure           | Expected Behaviour         |
| ----------------- | -------------------------- |
| File missing      | Handle `FileNotFoundError` |
| Invalid JSON      | Handle JSON parsing error  |
| Missing key       | Handle `KeyError`          |
| `readings = null` | Validate input             |
| Reading is text   | Reject invalid reading     |
| Negative reading  | Apply business rule        |
| Empty readings    | Produce useful message     |

---

# 🧠 Architecture Question

Imagine this JSON came from:

```text
Cloud API
   ↓
Python Service
   ↓
Quantum Processing Pipeline
```

Which data should you trust?

Answer:

> **None of it until validated.**

---

# 📅 DAY 6 — Custom Exceptions

## 🎯 Learning Objective

Learn to represent **domain-specific failures**.

This is an important professional Python concept.

---

# 🧠 Create a Custom Exception

Start with:

```python
class InvalidQuantumReadingError(Exception):
    """Raised when a quantum sensor reading is invalid."""
```

---

# 🧪 Challenge 1 — Reading Validation

Create:

```python
validate_reading(value)
```

Rules:

```text
None       → invalid
non-number → invalid
negative   → invalid
> 1.0      → invalid
0–1        → valid
```

---

# 🧪 Challenge 2 — Raise Your Exception

Instead of:

```python
raise ValueError(...)
```

use:

```python
raise InvalidQuantumReadingError(...)
```

when the value violates your application's domain rules.

---

# 🧪 Challenge 3 — Catch It

Build:

```text
JSON
 ↓
extract readings
 ↓
validate
 ↓
InvalidQuantumReadingError
 ↓
report invalid record
```

Do not terminate the entire program because one reading is invalid.

---

# 🧪 Challenge 4 — Multiple Exceptions

Create another exception:

```python
class InvalidSensorDataError(Exception):
    """Raised when the sensor data structure is invalid."""
```

Now distinguish between:

```text
InvalidSensorDataError
```

and:

```text
InvalidQuantumReadingError
```

This teaches you to model different failure domains.

---

# 🚨 Failure Injection

Create examples where:

```text
JSON structure is invalid
```

versus:

```text
JSON structure is valid
but an individual reading is invalid
```

Your program should treat these as different failures.

---

# 🧠 Key Architecture Lesson

There is a major difference between:

> "The application cannot understand this input."

and:

> "The application understands the input but one business value violates a rule."

Your exception design should communicate that distinction.

---

# 📅 DAY 7 — WEEK 2 CAPSTONE

# 🧪 Quantum Sensor File Processing Pipeline

This is your main Week 2 project.

Build a small production-style Python application.

---

# 📁 Suggested Project Structure

```text
revision_week2/
│
├── data/
│   └── sensor_data.json
│
├── exceptions.py
├── validator.py
├── processor.py
├── main.py
└── README.md
```

Do not worry if this feels slightly beyond your current level.

The purpose is to start developing engineering habits.

---

# 📄 Input

Your JSON should contain:

```json
{
    "device_id": "Q-SENSOR-001",
    "backend": "simulator",
    "readings": [
        0.5,
        -0.2,
        null,
        0.9,
        1.2,
        null,
        -0.8,
        0.25
    ]
}
```

---

# 🎯 Requirements

Your application must:

## 1. Locate the file

Use:

```python
pathlib
```

---

## 2. Open the file safely

Use:

```python
with open(...)
```

---

## 3. Parse JSON

Use:

```python
json.load()
```

---

## 4. Validate the structure

Confirm that required fields exist:

```text
device_id
backend
readings
```

---

## 5. Validate individual readings

Rules:

```text
None       → invalid
non-number → invalid
negative   → invalid
> 1.0      → invalid
0–1        → valid
```

---

## 6. Use custom exceptions

At minimum:

```python
InvalidSensorDataError
InvalidQuantumReadingError
```

---

## 7. Continue processing valid records

For the example input:

```text
0.5
-0.2
None
0.9
1.2
None
-0.8
0.25
```

valid readings should be:

```text
0.5
0.9
0.25
```

---

## 8. Calculate squared values

Produce:

```text
0.25
0.81
0.0625
```

---

## 9. Generate a processing report

Example:

```text
========================================
 Quantum Sensor Processing Report
========================================

Device ID       : Q-SENSOR-001
Backend         : simulator

Total readings  : 8
Valid readings  : 3
Invalid readings: 5

Valid Results
-------------
0.50 → 0.2500
0.90 → 0.8100
0.25 → 0.0625

Invalid Records
---------------
-0.20 → negative value
None   → missing value
1.20   → value exceeds maximum
None   → missing value
-0.80  → negative value

Processing Status: COMPLETED
========================================
```

---

# 🧪 CAPSTONE LEVEL 2 — Make It Fail Gracefully

Now introduce these failures one at a time.

### Scenario 1

Delete the JSON file.

Expected:

```text
Unable to locate sensor data file.
```

The application should not dump an ugly traceback to the user.

---

### Scenario 2

Corrupt the JSON.

Expected:

```text
Unable to parse sensor data.
```

---

### Scenario 3

Remove `device_id`.

Expected:

```text
Invalid sensor data: missing device_id.
```

---

### Scenario 4

Change:

```json
"readings": [...]
```

to:

```json
"readings": "hello"
```

Your validation should detect it.

---

### Scenario 5

Put a dictionary inside `readings`.

Example:

```json
"readings": [0.5, {"value": 0.9}, 0.25]
```

Your application should reject the invalid record without crashing.

---

# 🧠 CAPSTONE LEVEL 3 — Refactor

After you get the program working, stop.

Then ask:

> "How would I make this production quality?"

Refactor into functions such as:

```python
load_sensor_data()
validate_sensor_data()
validate_reading()
process_readings()
generate_report()
main()
```

Avoid creating one giant `main()` function.

---

# 🧪 CAPSTONE LEVEL 4 — Testing Challenge

Write tests for at least:

```text
Valid reading
Negative reading
None reading
Reading > 1
Invalid JSON structure
Missing JSON field
Missing file
Empty readings
```

You are not required to achieve 100% test coverage yet.

The goal is to begin developing the habit:

> **Every important failure mode deserves a test.**

---

# 🧠 WEEK 2 INTERVIEW DRILLS

At the end of the week, answer these without looking anything up.

## Question 1

What is an exception in Python?

---

## Question 2

What is the difference between:

```python
except ValueError:
```

and:

```python
except Exception:
```

---

## Question 3

When should you use `else` with `try/except`?

---

## Question 4

When is `finally` useful?

---

## Question 5

Why should you avoid:

```python
except:
    pass
```

---

## Question 6

What is a context manager?

---

## Question 7

Why is this useful?

```python
with open(...) as file:
```

---

## Question 8

What does `json.load()` do?

---

## Question 9

What is the difference between:

```python
json.load()
```

and:

```python
json.loads()
```

---

## Question 10

When would you create a custom exception?

---

## Question 11

What is the advantage of `pathlib.Path` over manually constructing filesystem strings?

---

## Question 12

Should every invalid input result in an exception?

Explain your reasoning.

---

# 🔄 WEEK 2 VARIATION CHALLENGES

Once your daily exercise works, choose **one** variation.

## Variation A — Scale

Change:

```text
8 readings
```

to:

```text
10,000 readings
```

Think about whether your implementation still makes sense.

---

## Variation B — Multiple Devices

Change the JSON to contain multiple sensors.

```text
Q-SENSOR-001
Q-SENSOR-002
Q-SENSOR-003
```

Process all devices.

---

## Variation C — Multiple Files

Put multiple JSON files into:

```text
data/
```

Use `pathlib` to discover them.

---

## Variation D — Error Log

Write invalid records to:

```text
errors.log
```

while allowing valid records to continue processing.

---

## Variation E — Output JSON

Instead of only printing the results, write:

```text
processed_sensor_data.json
```

containing the cleaned data.

---

# 🏆 WEEK 2 COMPLETION CRITERIA

Do not judge success by:

> "Did I finish seven exercises?"

Judge success using the following checklist.

* [Y] I can write `try/except` without looking up the syntax.
* [Y] I understand when to catch `ValueError`.
* [Y] I understand the purpose of `else`.
* [Y] I understand the purpose of `finally`.
* [Y] I can deliberately raise an exception.
* [Y] I can explain why broad exception handling can be dangerous.
* [Y] I can read a text file using `with open()`.
* [N] I can write to a file.
* [Y] I can use `pathlib.Path`.
* [Y] I can parse JSON.
* [Y] I can handle malformed JSON.
* [Y] I can detect missing JSON fields.
* [Y] I can create a custom exception.
* [Y] I can separate validation from processing.
* [Y] I can process valid records while reporting invalid ones.
* [Y] I deliberately tested failure scenarios.
* [N] I wrote tests for important failure cases.
* [Y] I can explain my code without reading it line by line.

---

# 📊 WEEK 2 SELF-ASSESSMENT

Score yourself from 1–5.

| Skill              | Score |
| ------------------ | ----: |
| `try/except`       |   5/5 |
| `else/finally`     |   5/5 |
| `raise`            |   5/5 |
| File I/O           |   3/5 |
| Context managers   |   4/5 |
| `pathlib`          |   5/5 |
| JSON               |   5/5 |
| Custom exceptions  |   5/5 |
| Input validation   |   5/5 |
| Debugging failures |   4/5 |
| Testing            |   3/5 |
| Code organisation  |   3/5 |

### Interpretation

**50–60:** Excellent — move forward.

**40–49:** Good — revisit your weakest two areas.

**30–39:** Repeat selected exercises before Week 3.

**Below 30:** Spend another week consolidating the fundamentals.

Do not rush because the calendar says Week 3.

---

# 🧠 WEEK 2 ARCHITECT'S REFLECTION

At the end of the week, write a short answer to these questions.

### 1. What surprised me about Python's exception model?
The features it provide and how gracefully we can handle errors and messages

### 2. Which exception did I initially misunderstand?
I was confused between ValueError and TypeError

### 3. Which syntax now feels automatic?
try, except, with open(), json.load() are automatic for me now. 

### 4. Which syntax still requires conscious thought?
Nothing is bothering me at this moment. 

### 5. What failure scenario did I discover only because I deliberately broke my program?
When a function has to return a value and if the flow is not returning anything it automatically returns NoneType

### 6. How would I design this differently if the input came from a cloud API instead of a local JSON file?
I need to learn more on this. I will get to it when I integrate streaming data from API's

### 7. What parts of this week's work resemble enterprise integration?
The capstone project is resembling enterprise integration. 

### 8. Where could this pattern appear in a future hybrid quantum/classical system?
This is the basic that we can expect in quantum computing to validate the input data before processing.

---

# 🚀 WEEK 2 → QUANTUM BRIDGE

Do not try to make everything "quantum" this week.

Instead, use quantum terminology only where it helps connect the concept.

Think of the architecture as:

```text
External Data
     ↓
Validation
     ↓
Error Handling
     ↓
Clean Classical Data
     ↓
Numerical Processing
     ↓
Quantum Circuit
```

Your current focus is the first three layers.

Later, those layers will become:

```text
Cloud/API/Data Lake
        ↓
Data Validation
        ↓
Classical Preprocessing
        ↓
Quantum Circuit Construction
        ↓
Quantum Backend
        ↓
Measurement Results
        ↓
Classical Postprocessing
```

That is the direction in which your Python skills should eventually evolve.

---

# ⭐ WEEK 2 GOLDEN RULE

> **Don't just practise how Python succeeds. Practise how Python fails.**

Your Week 1 work built syntax muscle memory.

Your Week 2 work should build **engineering judgement**.

By the end of this week, I want you to look at an input file and instinctively ask:

> "What can go wrong here?"

That mindset will be far more valuable to your long-term transition than memorising another 20 Python functions.

---

# 📌 GITHUB CHECK-IN TEMPLATE

When Week 2 is complete, record:

**Week:** 2
**Topic:** Robust Error Handling & File I/O
**Status:** Completed / Partially Completed

### What I practised

* `try/except`
* `else/finally`
* `raise`
* File I/O
* Context managers
* `pathlib`
* JSON
* Custom exceptions
* Validation

### Muscle Memory

What syntax can I now write without looking it up?

### Best Exercise

Which challenge taught me the most?

### Biggest Mistake

What did I initially get wrong?

### Failure I Discovered

What happened when I deliberately broke my program?

### Refactoring

What did I improve after getting the first version working?

### Architecture Connection

How does this week's Python knowledge relate to enterprise/cloud/quantum architecture?

### Confidence

Python confidence before Week 2: 5/10

Python confidence after Week 2: 6/10

### GitHub

Repository:

https://github.com/NGogireddy/pythonlabs/tree/main/revision%20week2

---

# 🏁 WEEK 2 DEFINITION OF DONE

You are finished when you can build the following **without following a tutorial step-by-step**:

```text
                sensor_data.json
                       │
                       ▼
                  pathlib.Path
                       │
                       ▼
                  open safely
                       │
                       ▼
                    JSON
                       │
                       ▼
                 Validate data
                       │
              ┌────────┴────────┐
              │                 │
           Valid              Invalid
              │                 │
              ▼                 ▼
       Process reading     Custom exception
              │                 │
              ▼                 ▼
        Calculate result    Error report
              │
              └────────┬────────┘
                       ▼
                 Final report
```

If you can implement that independently, **Week 2 has done its job.**
