# 📅 WEEK 1: ADVANCED CONTROL FLOW & FUNCTIONAL PYTHON
* **Objective:** Eliminate syntax hesitation, stop using heavy/nested `for` loops, and master native Python collection utilities.
* **Daily Commitment:** 30–45 minutes (Mon–Fri) | 60–90 minutes (Sat–Sun)

---

## 🛠️ DAILY EXECUTION SCHEDULE

### 📅 Monday: List Comprehensions (30–45 Mins)
* **Concept:** A concise, fast way to create lists. Syntax: `[expression for item in iterable if condition]`.
* **Muscle Memory Exercise (20 mins):** Type this out manually in your IDE:
  ```python
  # 1. Basic transformation
  squared = [x**2 for x in range(10)]
  
  # 2. Filtering
  evens = [x for x in range(20) if x % 2 == 0]
  
  # 3. Filtering and transforming simultaneously
  cleaned = [str(x).strip() for x in [" alpha ", " beta\n", "gamma "] if "a" in x]
  print(squared, evens, cleaned)
  ```
* **Daily Solo Drill (15 mins):** Given `prices = [120, 85, 200, 45, 150]`. Write a single-line list comprehension that applies a 10% discount (`x * 0.9`) but *only* to items that cost more than 100.

---

### 📅 Tuesday: Dictionary & Set Comprehensions (30–45 Mins)
* **Concept:** Construct key-value mappings or unique collections dynamically on a single line using curly braces `{}`.
* **Muscle Memory Exercise (20 mins):** Type this out manually:
  ```python
  # 1. Dictionary comprehension: Mapping IDs to status
  qubit_ids = [0, 1, 2, 3]
  qubit_map = {f"q{i}": "initialized" for i in qubit_ids}
  
  # 2. Set comprehension: Automatic duplicate removal
  raw_states = ["up", "down", "up", "unknown", "down"]
  unique_states = {state.upper() for state in raw_states}
  print(qubit_map, unique_states)
  ```
* **Daily Solo Drill (15 mins):** Given `components = ["resistor", "inductor", "capacitor"]`. Create a dictionary comprehension that maps each component string to its integer character count (e.g., `{"resistor": 8, ...}`).

---

### 📅 Wednesday: Lambda Functions & `map()` (30–45 Mins)
* **Concept:** `lambda` creates an anonymous inline function. `map(func, iterable)` applies that function to every element efficiently.
* **Muscle Memory Exercise (20 mins):** Type this out manually:
  ```python
  # 1. Basic inline lambda
  add_five = lambda x: x + 5
  print(add_five(10))
  
  # 2. Using map() with a lambda (cast to list to print elements)
  probabilities = [0.1, 0.5, 0.8]
  percentages = list(map(lambda p: p * 100, probabilities))
  print(percentages)
  ```
* **Daily Solo Drill (15 mins):** Write a `lambda` function that converts a string to lowercase. Use `map()` to apply it to `["Alpha", "BETA", "GaMmA"]`.

---

### 📅 Thursday: `filter()` & Sequence Unpacking (30–45 Mins)
* **Concept:** `filter()` extracts elements that satisfy a condition. Unpacking (`*`) dynamically routes remaining array values into a list variable.
* **Muscle Memory Exercise (20 mins):** Type this out manually:
  ```python
  # 1. Using filter()
  metrics = [0.99, 0.45, 0.88, 0.12]
  high_confidence = list(filter(lambda m: m > 0.5, metrics))
  
  # 2. Sequence Unpacking for structural data tracking
  hardware_specs = ["Rigetti_Ankaa", "84_qubits", "Superconducting", "UK_Based"]
  name, capacity, *other_details = hardware_specs
  print(name, capacity, other_details)
  ```
* **Daily Solo Drill (15 mins):** You have numbers from -5 to 5. Use `filter()` and a `lambda` to extract only strictly positive numbers (`> 0`).

---

### 📅 Friday: `enumerate()` & `zip()` (30–45 Mins)
* **Concept:** `enumerate()` tracks loop iteration indices automatically. `zip()` pairs two or more lists side-by-side.
* **Muscle Memory Exercise (20 mins):** Type this out manually:
  ```python
  # 1. Tracking indices cleanly without manual loop counter variables
  gates = ["Hadamard", "CNOT", "Pauli-X"]
  for index, gate in enumerate(gates):
      print(f"Gate Slot {index}: {gate}")
      
  # 2. Threading data channels together
  qubit_labels = ["q0", "q1", "q2"]
  frequencies = [4.8, 5.1, 4.9]
  for label, freq in zip(qubit_labels, frequencies):
      print(f"Device {label} operates at {freq} GHz")
  ```
* **Daily Solo Drill (15 mins):** Take `keys = ["a", "b", "c"]` and `values = [10, 20, 30]`. Loop through them simultaneously using `zip()`, and use `enumerate()` to print the current loop index alongside the key and value.

---

## 📈 WEEKEND LIVE LAB & DEEP DIVE (60–90 Mins)

### 🚀 Step 1: The Main Capstone Drill
Open a fresh file named `week_1_drill.py` in your local development environment and solve the challenge below without using standard multiline `for` loops.

```python
# ============================================================
# WEEK 1 CAPSTONE: THE QUANTUM DATA PREPROCESSOR
# ============================================================
# Scenario: You have raw state values from a simulated quantum 
# sensor. The dataset contains valid floats, negative numbers, 
# and corrupted 'None' values.
#
# Your Tasks:
# 1. Filter out all 'None' values and negative numbers using 
#    a single list comprehension.
# 2. Pass that filtered list to a native map() function with a 
#    lambda to square each number (simulating an amplitude probability).
# 3. Use enumerate() to loop over the final results and print 
#    each value paired with its final index in a clean string format.
# ============================================================

raw_data = [0.5, -0.2, None, 0.9, 1.2, None, -0.8]

# --- Write your solution below ---


### 🧠 Step 2: The Daily LeetCode Habit
* Sign up to **LeetCode**.
* Go to **Problems**, filter by **Difficulty: Easy**, and select **Topic: Array**.
* Complete 2 problems. Force yourself to use list comprehensions or pythonic filter methods instead of long structural loops to solve them.

### 💾 Step 3: Git Tracking
Commit `week_1_drill.py` and your LeetCode notes to your GitHub repository to lock in your tracking routine.

---
## 🔁 WEEKLY CHECK-IN PROMPT
When you return next week, start the session by pasting this text:
*"I am a Cloud Architect transitioning to Quantum Computing. I have finished Week 1. Here is my code implementation for the Quantum Data Preprocessor drill: [PASTE YOUR CODE]. Please run a professional code review for efficiency and give me my detailed Week 2: Robust Error Handling blueprint."*
